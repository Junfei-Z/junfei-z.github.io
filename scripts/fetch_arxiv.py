"""
Daily arXiv paper fetcher with two research tracks + LLM-based filtering & summarization.
Track 1: Edge AI (LLM/VLM on edge, distributed inference, energy/latency optimization)
Track 2: Agent Memory (computational efficiency of LLM agent memory systems)
"""
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import os
import time
from datetime import datetime

OUTPUT_PATH = "static/diary/arxiv-daily.json"
MAX_PER_TRACK = 10

# ─── Track definitions ───

TRACKS = {
    "edge_ai": {
        "name_zh": "Edge AI",
        "name_en": "Edge AI",
        "categories": ["cs.LG", "cs.DC", "cs.AI", "cs.SY", "cs.PF", "cs.CV"],
        "keywords": [
            "edge AI", "on-device inference", "edge computing LLM",
            "mobile inference", "Jetson", "IoT inference",
            "speculative decoding", "KV cache", "early exit",
            "dynamic inference", "visual token pruning",
            "quantization edge", "distributed inference",
            "cloud-edge", "LLM serving", "inference optimization",
            "energy LLM", "power model inference", "DVFS",
            "constrained MDP inference", "reinforcement learning inference",
            "federated LLM", "edge language model", "SLM edge",
            "multi-agent LLM graph", "latency model neural network",
            "scaling laws energy"
        ],
        "filter_prompt": """你是一个Edge AI方向的论文筛选助手。用户研究方向：
- LLM/VLM在边缘设备上的能耗profiling与建模
- On-device推理优化与资源调度
- Stochastic建模、constrained MDP、强化学习用于推理决策
- 分布式LLM serving与edge-cloud协同

筛选规则（满足任一即推荐）：
1. 边缘LLM/VLM系统类：同时涉及(LLM/VLM/SLM) + (edge/on-device/mobile/IoT) + (energy/efficient/inference/latency)
2. 推理优化技术类：speculative decoding / KV cache优化 / early exit / visual token pruning / quantization+edge
3. 系统调度与建模类：(MDP/RL/bandit/stochastic/DVFS/scheduling) + (LLM/inference/edge AI)
4. 分布式协同推理类：(distributed/partitioning/cloud-edge/federated) + (LLM/VLM/inference)
5. 加分：multi-agent LLM + network/topology, power/latency modeling + LLM
排除：纯训练优化、纯cloud datacenter、纯算法理论无实验、纯CV/NLP任务提升无效率分析、纯综述（除非核心方向最新综述）"""
    },
    "agent_memory": {
        "name_zh": "Agent Memory",
        "name_en": "Agent Memory",
        "categories": ["cs.CL", "cs.AI", "cs.LG", "cs.MA", "cs.IR"],
        "keywords": [
            "agent memory", "memory agent", "LLM memory",
            "memory-augmented agent", "episodic memory LLM",
            "working memory LLM", "long-term memory LLM",
            "memory compression", "context compression",
            "prompt compression", "memory summarization",
            "structured memory", "hierarchical memory",
            "latent memory", "memory token", "KV cache compression",
            "KV cache eviction", "long-horizon agent",
            "lifelong agent", "streaming memory",
            "long-context agent", "multi-agent memory",
            "shared memory agent", "infinite context",
            "context folding", "memory retrieval agent"
        ],
        "filter_prompt": """你是一个Agent Memory方向的论文筛选助手。这是一篇关于"LLM agent memory的计算效率"的综述的选文助手。

核心观点：agent memory的根本成本不在存储而在RECALL——将记忆加载回context window时的计算开销（注意力、推理干扰、上下文窗口机会成本）。

相关条件（必须同时满足）：
(a) 关于LLM agent中的memory（或密切相关：long-context LLM作为agent backbone、有显式memory的RL agent、memory-augmented multi-agent系统）
(b) 涉及计算效率：token cost, inference latency, FLOP, KV cache size, compression ratio, scalability, 定量cost-performance trade-off

三个分析轴：
- TE(Token Economy): structured/hierarchical memory, 检索优化, 摘要, prompt压缩
- LC(Latent Compression): latent memory tokens, soft prompts, KV cache复用/压缩
- SA(Scalable Architectures): long-horizon, streaming, multi-agent, lifelong, edge部署

排除：纯功能性memory分类(无效率分析)、纯RAG(无动态memory管理)、纯应用(无memory设计贡献)、纯训练/微调、硬件memory(GPU/RAM)"""
    }
}

# ─── LLM providers with auto-fallback ───

LLM_PROVIDERS = [
    {
        "name": "OpenAI",
        "env_key": "OPENAI_API_KEY",
        "url": "https://api.openai.com/v1/chat/completions",
        "model": "gpt-4o-mini",
    },
    {
        "name": "DeepSeek",
        "env_key": "DEEPSEEK_API_KEY",
        "url": "https://api.deepseek.com/v1/chat/completions",
        "model": "deepseek-chat",
    },
]


def call_llm(messages, provider, max_tokens=600):
    """Call an LLM provider. Returns response text or raises on failure."""
    api_key = os.environ.get(provider["env_key"])
    if not api_key:
        raise ValueError(f"No {provider['env_key']} set")

    body = json.dumps({
        "model": provider["model"],
        "messages": messages,
        "temperature": 0.2,
        "max_tokens": max_tokens
    }).encode("utf-8")

    req = urllib.request.Request(
        provider["url"], data=body,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        return result["choices"][0]["message"]["content"].strip()


def llm_call_with_fallback(messages, providers, current_idx=0, max_tokens=600):
    """Try providers in order, return (response, new_idx)."""
    for idx in range(current_idx, len(providers)):
        try:
            resp = call_llm(messages, providers[idx], max_tokens)
            return resp, idx
        except Exception as e:
            err = str(e)
            if any(k in err.lower() for k in ["429", "insufficient", "quota", "rate"]):
                print(f"    {providers[idx]['name']} quota/rate limit, switching...")
                continue
            else:
                print(f"    {providers[idx]['name']} error: {err}")
                continue
    return None, current_idx


# ─── arXiv fetching ───

def fetch_arxiv(categories, keywords, max_results=50):
    """Fetch papers from arXiv API."""
    cat_q = " OR ".join(f"cat:{c}" for c in categories)
    kw_q = " OR ".join(f'all:"{k}"' for k in keywords[:15])  # API limit
    query = f"({cat_q}) AND ({kw_q})"

    params = urllib.parse.urlencode({
        "search_query": query, "start": 0, "max_results": max_results,
        "sortBy": "submittedDate", "sortOrder": "descending"
    })
    url = f"http://export.arxiv.org/api/query?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "DailyArxivBot/1.0"})

    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read().decode("utf-8")

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(data)
    papers = []
    seen = set()

    for entry in root.findall("atom:entry", ns):
        arxiv_id = entry.find("atom:id", ns).text.strip().split("/abs/")[-1]
        if arxiv_id in seen:
            continue
        seen.add(arxiv_id)

        title = entry.find("atom:title", ns).text.strip().replace("\n", " ")
        abstract = entry.find("atom:summary", ns).text.strip().replace("\n", " ")
        published = entry.find("atom:published", ns).text.strip()[:10]
        authors = [a.find("atom:name", ns).text for a in entry.findall("atom:author", ns)]
        categories = [c.get("term") for c in entry.findall("atom:category", ns)]

        papers.append({
            "id": arxiv_id, "title": title, "abstract": abstract[:600],
            "authors": authors[:5], "published": published,
            "categories": categories[:5],
            "link": f"https://arxiv.org/abs/{arxiv_id}",
            "pdf": f"https://arxiv.org/pdf/{arxiv_id}"
        })

    return papers


# ─── LLM filtering + summarization ───

def filter_and_summarize(papers, track_key, track_info, providers, provider_idx):
    """Use LLM to filter relevant papers and generate summaries."""
    if not papers:
        return [], provider_idx

    # Batch filter: send all titles+abstracts, ask LLM to pick relevant ones
    paper_list = "\n\n".join(
        f"[{i}] 标题: {p['title']}\n摘要: {p['abstract'][:300]}"
        for i, p in enumerate(papers)
    )

    filter_msg = [
        {"role": "system", "content": track_info["filter_prompt"]},
        {"role": "user", "content": f"""以下是今天的{len(papers)}篇候选论文。请筛选出相关的（最多{MAX_PER_TRACK}篇），按推荐优先级排序。

对每篇相关论文，输出JSON数组格式：
[{{"index": 0, "priority": "高", "problem": "这篇论文要解决什么问题？（中文一句话，20-40字）", "method": "提出了什么方法/框架？核心思路是什么？如果摘要中有具体数值结果请包含，如延迟降低30%、内存减少2倍等（中文一句话，40-60字）", "relevance": "为什么和我的研究方向相关？这篇文章最大的创新点是什么？（中文一句话，30-50字）"}}]

只输出JSON数组，不要其他文字。如果没有相关论文，输出空数组[]。

候选论文：
{paper_list}"""}
    ]

    resp, provider_idx = llm_call_with_fallback(filter_msg, providers, provider_idx, max_tokens=2000)
    if not resp:
        print(f"  [{track_key}] LLM filtering failed, returning top papers by recency")
        return papers[:MAX_PER_TRACK], provider_idx

    # Parse LLM response
    try:
        # Extract JSON from response (handle markdown code blocks)
        json_str = resp
        if "```" in json_str:
            json_str = json_str.split("```")[1]
            if json_str.startswith("json"):
                json_str = json_str[4:]
        selected = json.loads(json_str.strip())
    except (json.JSONDecodeError, IndexError):
        print(f"  [{track_key}] Failed to parse LLM filter response, using first {MAX_PER_TRACK}")
        return papers[:MAX_PER_TRACK], provider_idx

    # Build filtered list with summaries
    result = []
    for item in selected[:MAX_PER_TRACK]:
        idx = item.get("index", -1)
        if 0 <= idx < len(papers):
            p = papers[idx].copy()
            p["priority"] = item.get("priority", "中")
            p["problem_zh"] = item.get("problem", "")
            p["method_zh"] = item.get("method", "")
            p["relevance_zh"] = item.get("relevance", "")
            p["summary_zh"] = f"问题：{p['problem_zh']}\n方法：{p['method_zh']}\n相关性：{p['relevance_zh']}"
            result.append(p)

    return result, provider_idx


# ─── Word Cloud ───

def generate_wordclouds(all_tracks):
    """Generate a word cloud image for each track from paper titles + abstracts."""
    try:
        from wordcloud import WordCloud
    except ImportError:
        print("wordcloud not installed, skipping word cloud generation")
        return

    # Common stopwords for academic papers
    stopwords = set("the a an and or of to in for on with is are was were be been by that this it its from at as we our which their can will has have do does not but also more than into such using used based use these those between however both most each".split())

    colors = {
        "edge_ai": {"colormap": "cool", "bg": "#fafafa"},
        "agent_memory": {"colormap": "autumn", "bg": "#fafafa"},
    }

    for track_key, track_data in all_tracks.items():
        papers = track_data.get("papers", [])
        if not papers:
            continue

        # Build text corpus from titles (2x weight) + abstracts
        text_parts = []
        for p in papers:
            text_parts.append(p["title"] + " " + p["title"])  # title 2x
            text_parts.append(p.get("abstract", ""))
        text = " ".join(text_parts)

        style = colors.get(track_key, {"colormap": "viridis", "bg": "#fafafa"})
        wc = WordCloud(
            width=800, height=300,
            background_color=style["bg"],
            colormap=style["colormap"],
            max_words=60,
            stopwords=stopwords,
            min_font_size=10,
            max_font_size=80,
            prefer_horizontal=0.8,
            margin=8
        ).generate(text)

        out_path = f"static/diary/wordcloud_{track_key}.png"
        wc.to_file(out_path)
        track_data["wordcloud"] = f"wordcloud_{track_key}.png"
        print(f"  Generated word cloud: {out_path}")


# ─── Main ───

def main():
    print(f"=== Daily arXiv Fetch ({datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}) ===")

    providers = [p for p in LLM_PROVIDERS if os.environ.get(p["env_key"])]
    if providers:
        print(f"LLM providers: {' → '.join(p['name'] for p in providers)}")
    else:
        print("No LLM API keys, will skip filtering/summarization")

    provider_idx = 0
    all_tracks = {}

    for track_key, track_info in TRACKS.items():
        print(f"\n--- Track: {track_info['name_en']} ---")
        print(f"  Categories: {track_info['categories']}")

        papers = fetch_arxiv(track_info["categories"], track_info["keywords"], max_results=40)
        print(f"  Fetched {len(papers)} candidate papers")

        if papers and providers:
            print(f"  Filtering with LLM...")
            filtered, provider_idx = filter_and_summarize(
                papers, track_key, track_info, providers, provider_idx
            )
            print(f"  Selected {len(filtered)} papers")
        else:
            filtered = papers[:MAX_PER_TRACK]

        all_tracks[track_key] = {
            "name_zh": track_info["name_zh"],
            "name_en": track_info["name_en"],
            "count": len(filtered),
            "papers": filtered
        }
        time.sleep(3)  # respect arXiv rate limit

    # Generate word clouds
    print("\nGenerating word clouds...")
    generate_wordclouds(all_tracks)

    output = {
        "date": datetime.utcnow().strftime("%Y-%m-%d"),
        "updated_at": datetime.utcnow().isoformat() + "Z",
        "tracks": all_tracks,
        "total_count": sum(t["count"] for t in all_tracks.values())
    }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n=== Done. Total {output['total_count']} papers saved to {OUTPUT_PATH} ===")


if __name__ == "__main__":
    main()
