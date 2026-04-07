"""
Daily arXiv paper fetcher with OpenAI summarization.
Fetches recent papers from arXiv, generates Chinese summaries, and outputs JSON.
"""
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import os
import time
from datetime import datetime, timedelta

# Configuration
CATEGORIES = ["cs.AI", "cs.LG", "cs.RO"]
KEYWORDS = [
    "large language model", "LLM", "edge computing", "cloud-edge",
    "distributed inference", "reinforcement learning", "VLM",
    "vision language model", "privacy", "federated"
]
MAX_PAPERS = 10
OUTPUT_PATH = "static/diary/arxiv-daily.json"


def fetch_arxiv_papers():
    """Fetch recent papers from arXiv API."""
    cat_query = " OR ".join(f"cat:{c}" for c in CATEGORIES)
    kw_query = " OR ".join(f'all:"{k}"' for k in KEYWORDS)
    query = f"({cat_query}) AND ({kw_query})"

    params = urllib.parse.urlencode({
        "search_query": query,
        "start": 0,
        "max_results": MAX_PAPERS * 3,  # fetch more, then filter
        "sortBy": "submittedDate",
        "sortOrder": "descending"
    })
    url = f"http://export.arxiv.org/api/query?{params}"

    req = urllib.request.Request(url, headers={"User-Agent": "DailyArxivBot/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read().decode("utf-8")

    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(data)

    papers = []
    seen = set()
    for entry in root.findall("atom:entry", ns):
        title = entry.find("atom:title", ns).text.strip().replace("\n", " ")
        arxiv_id = entry.find("atom:id", ns).text.strip().split("/abs/")[-1]
        if arxiv_id in seen:
            continue
        seen.add(arxiv_id)

        abstract = entry.find("atom:summary", ns).text.strip().replace("\n", " ")
        published = entry.find("atom:published", ns).text.strip()[:10]
        authors = [a.find("atom:name", ns).text for a in entry.findall("atom:author", ns)]
        categories = [c.get("term") for c in entry.findall("atom:category", ns)]
        link = f"https://arxiv.org/abs/{arxiv_id}"
        pdf = f"https://arxiv.org/pdf/{arxiv_id}"

        papers.append({
            "id": arxiv_id,
            "title": title,
            "abstract": abstract[:500],
            "authors": authors[:5],
            "published": published,
            "categories": categories[:5],
            "link": link,
            "pdf": pdf
        })

        if len(papers) >= MAX_PAPERS:
            break

    return papers


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


def call_llm(prompt, provider):
    """Call an LLM provider. Returns response text or raises on failure."""
    api_key = os.environ.get(provider["env_key"])
    if not api_key:
        raise ValueError(f"No {provider['env_key']} set")

    body = json.dumps({
        "model": provider["model"],
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "max_tokens": 300
    }).encode("utf-8")

    req = urllib.request.Request(
        provider["url"],
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        return result["choices"][0]["message"]["content"].strip()


def summarize_papers(papers):
    """Generate Chinese summaries with auto-fallback between providers."""
    # Find available providers
    available = [p for p in LLM_PROVIDERS if os.environ.get(p["env_key"])]
    if not available:
        print("No LLM API keys found, skipping summarization")
        return papers

    current_idx = 0
    print(f"Using {available[current_idx]['name']} (fallback: {', '.join(p['name'] for p in available[1:])} )")

    for i, paper in enumerate(papers):
        prompt = f"""请用中文对以下论文生成一句话摘要（30字以内），再用2-3句话简述核心贡献和方法。格式：
一句话：...
简述：...

标题：{paper['title']}
摘要：{paper['abstract']}"""

        summarized = False
        for attempt_idx in range(current_idx, len(available)):
            provider = available[attempt_idx]
            try:
                paper["summary_zh"] = call_llm(prompt, provider)
                paper["llm_provider"] = provider["name"]
                print(f"  [{i+1}/{len(papers)}] {provider['name']}: {paper['title'][:50]}...")
                summarized = True
                current_idx = attempt_idx  # stick with working provider
                break
            except Exception as e:
                err_msg = str(e)
                if "429" in err_msg or "insufficient" in err_msg.lower() or "quota" in err_msg.lower():
                    print(f"  [{i+1}/{len(papers)}] {provider['name']} quota/rate limit, switching...")
                    continue
                else:
                    print(f"  [{i+1}/{len(papers)}] {provider['name']} error: {err_msg}")
                    continue

        if not summarized:
            paper["summary_zh"] = ""
            print(f"  [{i+1}/{len(papers)}] All providers failed")

        time.sleep(0.5)

    return papers


def main():
    print(f"Fetching arXiv papers... ({datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')})")
    print(f"Categories: {CATEGORIES}")
    print(f"Keywords: {KEYWORDS[:5]}...")

    papers = fetch_arxiv_papers()
    print(f"Found {len(papers)} papers")

    if papers:
        print("Generating summaries...")
        papers = summarize_papers(papers)

    output = {
        "date": datetime.utcnow().strftime("%Y-%m-%d"),
        "updated_at": datetime.utcnow().isoformat() + "Z",
        "categories": CATEGORIES,
        "count": len(papers),
        "papers": papers
    }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(papers)} papers to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
