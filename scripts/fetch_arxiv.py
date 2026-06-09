"""
Daily arXiv paper fetcher with two research tracks + LLM-based filtering & summarization.
Track 1: Edge AI (LLM/VLM on edge, distributed inference, energy/latency optimization)
Track 2: Agent Memory (computational efficiency of LLM agent memory systems)
"""
import urllib.request
import urllib.parse
import urllib.error
import http.client
import socket
import xml.etree.ElementTree as ET
import json
import os
import time
from datetime import datetime

OUTPUT_PATH = "static/diary/arxiv-daily.json"
PREFS_PATH = "static/diary/arxiv-prefs.json"
SEEN_PATH = "static/diary/arxiv-seen.json"
MAX_PER_TRACK = 10
SEEN_HISTORY_DAYS = 30  # keep 30 days of seen IDs to avoid unbounded growth

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
    },
    "edge_intelligence": {
        "name_zh": "Edge Intelligence",
        "name_en": "Edge Intelligence",
        "categories": ["cs.NI", "cs.DC", "cs.LG", "cs.AI", "cs.SY", "eess.SP", "cs.MA"],
        # NOTE: only the first 15 keywords are used in the arXiv query
        # (see keywords[:15] in fetch_arxiv), so satellite-edge terms are
        # front-loaded to make sure those papers actually get fetched.
        "keywords": [
            "satellite edge computing", "LEO satellite", "non-terrestrial network",
            "satellite-terrestrial", "space-air-ground", "satellite inference",
            "edge intelligence", "edge computing", "task offloading",
            "computation offloading", "mobile edge computing", "MEC",
            "split inference", "edge-cloud collaboration", "cooperative inference",
            "IoT intelligence", "resource scheduling", "fog computing",
            "federated learning edge", "communication-efficient",
            "over-the-air computation", "semantic communication",
            "joint communication and computation", "device-edge co-inference",
            "IoT scheduling", "heterogeneous edge", "multi-access edge",
            "latency optimization edge", "energy harvesting IoT",
            "age of information", "digital twin edge",
            "LLM edge deployment", "on-device AI",
            "intelligent scheduling", "network slicing edge",
            "satellite VLM", "satellite collaborative inference"
        ],
        "filter_prompt": """你是一个Edge Intelligence方向的论文筛选助手。用户研究方向：
- 卫星边缘网络与星地协同智能（最高优先级）
- 边缘智能系统中的任务调度与资源优化
- IoT场景下的计算卸载与通信-计算联合优化
- 边缘设备上的AI模型部署、推理优化与协同
- 语义通信、Over-the-Air Computation等通信高效技术
- 联邦学习、分布式推理在边缘网络中的应用
- LLM/SLM在边缘智能场景的部署与优化

★最高优先级（命中则强烈推荐，并尽量排在最前）：
卫星边缘网络 / 星地协同 / LEO卫星 / 非地面网络(NTN) / 空天地一体化 相关，
尤其是 (satellite/LEO/NTN/space-air-ground) + (edge/inference/VLM/LLM/foundation model/collaborative/offloading)，
如"卫星协作VLM"、星上推理、星地协同推理、卫星边缘计算卸载等。

筛选规则（满足任一即推荐）：
0. 卫星边缘类（优先）：(satellite/LEO/non-terrestrial/space-air-ground) + (edge/inference/VLM/LLM/offloading/collaborative/scheduling)
1. 边缘计算调度类：(task offloading/computation offloading/resource allocation/scheduling) + (edge/MEC/IoT/fog)
2. 通信计算联合优化类：(communication/bandwidth/spectrum) + (computation/inference/edge) + (joint/co-design/trade-off)
3. 边缘AI部署类：(model deployment/split inference/cooperative inference/federated) + (edge/IoT/heterogeneous devices)
4. 语义通信类：(semantic communication/over-the-air/AirComp) + (edge/IoT/inference)
5. 边缘LLM类：(LLM/language model/foundation model) + (edge/IoT/on-device/mobile) + (scheduling/deployment/serving)
6. 加分：digital twin + edge, age of information + scheduling, multi-agent + edge network, reinforcement learning + offloading
排序：先卫星边缘相关，再其余命中项。排除：纯理论无实验、纯数据中心/云端优化（无边缘）、纯无线通信物理层（无计算/AI）、纯综述（除非核心方向最新综述）"""
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


# ─── Venue detection ───

import re

TOP_VENUES = {
    # Top ML/AI conferences
    "iclr": "ICLR", "neurips": "NeurIPS", "nips": "NeurIPS",
    "icml": "ICML", "aaai": "AAAI", "ijcai": "IJCAI",
    # NLP
    "acl": "ACL", "emnlp": "EMNLP", "naacl": "NAACL",
    # CV
    "cvpr": "CVPR", "iccv": "ICCV", "eccv": "ECCV",
    # Systems
    "osdi": "OSDI", "sosp": "SOSP", "mlsys": "MLSys",
    "asplos": "ASPLOS", "isca": "ISCA", "micro": "MICRO",
    # Journals
    "nature": "Nature", "science": "Science",
    "nature machine intelligence": "NMI",
    "nmi": "NMI", "tmlr": "TMLR", "jmlr": "JMLR",
    "tpami": "TPAMI", "tacl": "TACL",
}


def detect_venue(comment):
    """Detect top venue from arXiv comment field."""
    if not comment:
        return ""
    comment_lower = comment.lower()
    # Check longer patterns first (e.g. "nature machine intelligence" before "nature")
    for keyword in sorted(TOP_VENUES.keys(), key=len, reverse=True):
        # Use word boundary to avoid false matches (e.g. "practical" matching "acl")
        if re.search(r'\b' + re.escape(keyword) + r'\b', comment_lower):
            return TOP_VENUES[keyword]
    return ""


# ─── Deduplication ───

def load_seen_ids():
    """Load previously seen paper IDs from disk."""
    if not os.path.exists(SEEN_PATH):
        return {}
    try:
        with open(SEEN_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_seen_ids(seen_dict):
    """Save seen IDs, pruning entries older than SEEN_HISTORY_DAYS."""
    cutoff = (datetime.utcnow() - __import__("datetime").timedelta(days=SEEN_HISTORY_DAYS)).strftime("%Y-%m-%d")
    pruned = {k: v for k, v in seen_dict.items() if v >= cutoff}
    os.makedirs(os.path.dirname(SEEN_PATH), exist_ok=True)
    with open(SEEN_PATH, "w", encoding="utf-8") as f:
        json.dump(pruned, f, ensure_ascii=False)


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

    # Retry with backoff on transient HTTP errors and network timeouts.
    # arXiv frequently returns 403/406/429/5xx or simply times out under load,
    # so we treat all of these as retryable rather than crashing the whole run.
    RETRYABLE_CODES = (403, 406, 408, 429, 500, 502, 503, 504)
    MAX_ATTEMPTS = 5
    data = None
    for attempt in range(MAX_ATTEMPTS):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = resp.read().decode("utf-8")
            break
        except urllib.error.HTTPError as e:
            if e.code in RETRYABLE_CODES and attempt < MAX_ATTEMPTS - 1:
                wait = 10 * (2 ** attempt)  # 10s, 20s, 40s, 80s
                print(f"arXiv returned {e.code}, retrying in {wait}s (attempt {attempt+1}/{MAX_ATTEMPTS})...")
                time.sleep(wait)
            else:
                raise
        except (urllib.error.URLError, http.client.HTTPException,
                TimeoutError, socket.timeout, ConnectionError) as e:
            if attempt < MAX_ATTEMPTS - 1:
                wait = 10 * (2 ** attempt)  # 10s, 20s, 40s, 80s
                print(f"arXiv request failed ({type(e).__name__}: {e}), "
                      f"retrying in {wait}s (attempt {attempt+1}/{MAX_ATTEMPTS})...")
                time.sleep(wait)
            else:
                raise
    if data is None:
        raise RuntimeError("Failed to fetch from arXiv after retries")

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
        comment_el = entry.find("atom:comment", ns)
        comment = comment_el.text.strip().replace("\n", " ") if comment_el is not None and comment_el.text else ""

        # Detect top venue from comment
        venue = detect_venue(comment)

        papers.append({
            "id": arxiv_id, "title": title, "abstract": abstract[:600],
            "authors": authors[:5], "published": published,
            "categories": categories[:5], "comment": comment[:200],
            "venue": venue,
            "link": f"https://arxiv.org/abs/{arxiv_id}",
            "pdf": f"https://arxiv.org/pdf/{arxiv_id}"
        })

    return papers


# ─── LLM filtering + summarization ───

def load_user_prefs():
    """Load user preferences from arxiv-prefs.json if it exists."""
    if not os.path.exists(PREFS_PATH):
        return None
    try:
        with open(PREFS_PATH, "r", encoding="utf-8") as f:
            prefs = json.load(f)
        print(f"  Loaded user preferences: {prefs.get('total_liked', 0)} liked papers")
        return prefs
    except Exception as e:
        print(f"  Failed to load preferences: {e}")
        return None


def filter_and_summarize(papers, track_key, track_info, providers, provider_idx, user_prefs=None):
    """Use LLM to filter relevant papers and generate summaries."""
    if not papers:
        return [], provider_idx

    # Sort: venue papers first for LLM attention
    papers_sorted = sorted(papers, key=lambda p: (0 if p.get("venue") else 1))

    # Batch filter: send all titles+abstracts, ask LLM to pick relevant ones
    paper_list = "\n\n".join(
        f"[{i}] 标题: {p['title']}\n摘要: {p['abstract'][:300]}" +
        (f"\n⭐ 发表于: {p['venue']}" if p.get("venue") else "")
        for i, p in enumerate(papers_sorted)
    )

    # Build preference hint if available
    pref_hint = ""
    if user_prefs and user_prefs.get("preferred_keywords"):
        keywords = user_prefs["preferred_keywords"][:15]
        pref_hint = f"\n\n用户偏好提示：根据用户历史点赞记录，用户对以下关键词相关的论文更感兴趣：{', '.join(keywords)}。请在筛选时适当优先推荐与这些关键词相关的论文，但不要完全排除其他相关论文。"

    filter_msg = [
        {"role": "system", "content": track_info["filter_prompt"]},
        {"role": "user", "content": f"""以下是今天的{len(papers_sorted)}篇候选论文。请筛选出相关的（最多{MAX_PER_TRACK}篇），按推荐优先级排序。

重要：标有⭐的论文已被顶会/顶刊接收（如ICLR、NeurIPS、ICML、ACL、CVPR、Nature等），在同等相关性下请优先推荐这些论文，并将其priority设为"高"。{pref_hint}

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
        if 0 <= idx < len(papers_sorted):
            p = papers_sorted[idx].copy()
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
        "edge_intelligence": {"colormap": "winter", "bg": "#fafafa"},
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
    failed_tracks = []
    user_prefs = load_user_prefs()
    seen_ids = load_seen_ids()
    today = datetime.utcnow().strftime("%Y-%m-%d")

    # Load the previous run's output so we can carry forward any track that
    # fails to fetch today, instead of dropping its papers from the site.
    prev_tracks = {}
    try:
        with open(OUTPUT_PATH, encoding="utf-8") as f:
            prev_tracks = json.load(f).get("tracks", {})
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    for ti, (track_key, track_info) in enumerate(TRACKS.items()):
        if ti > 0:
            time.sleep(3)  # polite delay between arXiv API calls
        print(f"\n--- Track: {track_info['name_en']} ---")
        print(f"  Categories: {track_info['categories']}")

        try:
            papers = fetch_arxiv(track_info["categories"], track_info["keywords"], max_results=40)
        except Exception as e:
            # Don't let one track's network failure abort the whole run —
            # keep this track's previous results (if any) and move on.
            print(f"  ⚠️  Failed to fetch track '{track_key}': {type(e).__name__}: {e}")
            failed_tracks.append(track_key)
            continue
        print(f"  Fetched {len(papers)} candidate papers")

        # Deduplicate: skip papers already seen in the last {SEEN_HISTORY_DAYS} days
        before = len(papers)
        papers = [p for p in papers if p["id"] not in seen_ids]
        if before != len(papers):
            print(f"  Dedup: removed {before - len(papers)} previously seen papers, {len(papers)} remaining")

        if papers and providers:
            print(f"  Filtering with LLM...")
            filtered, provider_idx = filter_and_summarize(
                papers, track_key, track_info, providers, provider_idx, user_prefs
            )
            print(f"  Selected {len(filtered)} papers")
        else:
            filtered = papers[:MAX_PER_TRACK]

        # Mark selected papers as seen
        for p in filtered:
            seen_ids[p["id"]] = today

        all_tracks[track_key] = {
            "name_zh": track_info["name_zh"],
            "name_en": track_info["name_en"],
            "count": len(filtered),
            "papers": filtered
        }
        time.sleep(3)  # respect arXiv rate limit

    # Carry forward previous papers for any track that failed to fetch today.
    for track_key in failed_tracks:
        if track_key in prev_tracks:
            print(f"  Carrying forward previous papers for failed track '{track_key}'")
            all_tracks[track_key] = prev_tracks[track_key]

    # If every track failed and we have no prior data either, abort without
    # writing so we don't overwrite good output with an empty file.
    if not all_tracks:
        raise RuntimeError("All tracks failed to fetch and no previous data to keep")

    # Restore the original track ordering (failed tracks were appended last).
    all_tracks = {k: all_tracks[k] for k in TRACKS if k in all_tracks}

    # Persist seen IDs for future dedup
    save_seen_ids(seen_ids)
    print(f"\nSaved {len(seen_ids)} seen paper IDs (rolling {SEEN_HISTORY_DAYS}-day window)")

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

    # Send email notifications
    send_email_notifications(output)


# ─── Email Notifications ───

def build_email_html(data, track_keys=None):
    """Build HTML email for given tracks (None = all tracks)."""
    tracks = data.get("tracks", {})
    if track_keys:
        tracks = {k: v for k, v in tracks.items() if k in track_keys}

    total = sum(t["count"] for t in tracks.values())
    track_names = " / ".join(t["name_en"] for t in tracks.values())

    html = f'''<html><body style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;max-width:700px;margin:0 auto;padding:20px;background:#fafbff">
<div style="text-align:center;padding:24px;background:linear-gradient(135deg,#1e1b4b,#4338ca,#0e7490);border-radius:16px;margin-bottom:24px">
<h1 style="color:#fff;margin:0;font-size:1.5rem">📚 arXiv Daily Papers</h1>
<p style="color:rgba(255,255,255,0.7);margin:8px 0 0;font-size:0.85rem">{data.get("date","")} · {track_names} · {total} papers</p>
</div>'''

    for tk, tv in tracks.items():
        name = tv.get("name_en", tk)
        count = tv.get("count", 0)
        html += f'<h2 style="color:#4338ca;border-bottom:2px solid #e2e8f0;padding-bottom:8px;margin-top:32px">{name} ({count} papers)</h2>'

        for i, p in enumerate(tv.get("papers", [])):
            prio = p.get("priority", "")
            prio_color = {"高": "#ef4444", "中": "#f59e0b", "低": "#94a3b8"}.get(prio, "#94a3b8")
            venue = p.get("venue", "")
            venue_html = f'<span style="background:#ede9fe;color:#7c3aed;padding:2px 8px;border-radius:4px;font-size:0.7rem;font-weight:bold">📍{venue}</span> ' if venue else ""

            summary_html = ""
            for field, label, bg, color in [
                ("problem_zh", "问题", "#fef2f2", "#ef4444"),
                ("method_zh", "方法", "#eef2ff", "#6366f1"),
                ("relevance_zh", "相关", "#fffbeb", "#f59e0b"),
            ]:
                val = p.get(field, "")
                if val:
                    summary_html += f'<div style="margin:4px 0"><span style="background:{bg};color:{color};padding:1px 6px;border-radius:3px;font-size:0.7rem;font-weight:600">{label}</span> {val}</div>'

            authors = ", ".join(p.get("authors", [])[:3])
            if len(p.get("authors", [])) > 3:
                authors += " et al."

            html += f'''
<div style="background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:16px;margin:12px 0">
  <div>
    <span style="color:#6366f1;font-weight:bold;font-size:0.85rem;margin-right:8px">{i+1}</span>
    {venue_html}<span style="background:{prio_color}20;color:{prio_color};padding:2px 8px;border-radius:4px;font-size:0.7rem;font-weight:bold">{prio}</span>
    <h3 style="margin:6px 0;font-size:0.95rem"><a href="{p.get('link','')}" style="color:#1e293b;text-decoration:none">{p.get('title','')}</a></h3>
    <p style="color:#94a3b8;font-size:0.78rem;margin:0 0 8px">{authors}</p>
    <div style="font-size:0.85rem;color:#64748b;line-height:1.6">{summary_html}</div>
    <div style="margin-top:8px">
      <a href="{p.get('pdf','')}" style="background:#fef2f2;color:#ef4444;padding:3px 10px;border-radius:4px;font-size:0.7rem;text-decoration:none;font-weight:600">📄 PDF</a>
      <span style="color:#cbd5e1;font-size:0.7rem;margin-left:8px">{p.get('published','')}</span>
    </div>
  </div>
</div>'''

    html += f'''
<div style="text-align:center;padding:24px;color:#94a3b8;font-size:0.8rem;border-top:1px solid #e2e8f0;margin-top:32px">
  <p><a href="https://junfei-z.github.io/diary/" style="color:#6366f1">View in Diary</a> · Powered by arXiv Daily Bot</p>
</div></body></html>'''
    return html, total


def send_email_notifications(data):
    """Send email notifications to configured recipients."""
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    gmail_addr = os.environ.get("GMAIL_ADDRESS")
    gmail_pass = os.environ.get("GMAIL_APP_PASSWORD")
    if not gmail_addr or not gmail_pass:
        print("\nNo GMAIL credentials, skipping email notifications")
        return

    date = data.get("date", "")

    # Recipient config: (email, track_keys or None for all, label)
    recipients = [
        (os.environ.get("NOTIFY_EMAIL", ""), None, "all tracks"),  # all tracks
        (os.environ.get("NOTIFY_EMAIL_EI", ""), ["edge_intelligence"], "Edge Intelligence only"),
    ]

    for addr, track_keys, label in recipients:
        if not addr:
            continue
        try:
            html, total = build_email_html(data, track_keys)
            if total == 0:
                print(f"  Skipping {addr} ({label}): no papers")
                continue

            track_label = " / ".join(track_keys) if track_keys else "All Tracks"
            msg = MIMEMultipart("alternative")
            msg["Subject"] = f"📚 arXiv Daily: {date} - {total} papers ({track_label})"
            msg["From"] = gmail_addr
            msg["To"] = addr
            msg.attach(MIMEText(html, "html"))

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(gmail_addr, gmail_pass)
                server.send_message(msg)
            print(f"  ✉️ Email sent to {addr} ({label})")
        except Exception as e:
            print(f"  ❌ Failed to send to {addr}: {e}")


if __name__ == "__main__":
    main()
