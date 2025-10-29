from typing import Iterable, Dict, Any, Optional, List
import os, gzip, json, re
import pandas as pd





# helpers

def stream_jsonl_gz(path: str) -> Iterable[Dict[str, Any]]:
    with gzip.open(path, 'rt', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue

def get_item_id(obj: Dict[str, Any]) -> Optional[str]:
    """Prefer parent_asin; fall back to asin."""
    if obj.get("parent_asin"):
        return str(obj["parent_asin"])
    if obj.get("asin"):
        return str(obj["asin"])
    return None

def unix_seconds(ts) -> Optional[int]:
    if ts is None:
        return None
    try:
        ts = int(ts)
    except Exception:
        return None
    if ts > 10**12:  # ms -> s
        ts //= 1000
    return int(ts)

# minimal scrub + list normalizer 
def scrub(s: Optional[str]) -> str:
    if not s:
        return ""
    return re.sub(r"\s+", " ", str(s)).strip()

def to_text_list(x) -> List[str]:
    if x is None:
        return []
    if isinstance(x, str):
        return [x]
    if isinstance(x, (list, tuple)):
        return [str(t) for t in x if t is not None]
    return [str(x)]

def join_short(chunks: List[str], max_chunks: int = 3) -> str:
    chunks = [scrub(c) for c in chunks if scrub(c)]
    return ". ".join(chunks[:max_chunks])

def build_description(meta: Dict[str, Any]) -> str:
    parts = []

    # 1) Prefer FEATURES (often the synopsis). Keep up to 5 non-empty bullets.
    feats = [scrub(x) for x in to_text_list(meta.get("features")) if scrub(x)]
    if feats:
        parts.append(" • ".join(feats[:5]))

    # 2) If no features, use DESCRIPTION (list or string). Join a few chunks.
    if not parts:
        desc = meta.get("description")
        desc_list = []
        if isinstance(desc, list):
            desc_list = [scrub(d) for d in desc if scrub(d)]
        elif isinstance(desc, str) and scrub(desc):
            desc_list = [scrub(desc)]
        if desc_list:
            parts.append(join_short(desc_list, max_chunks=3))

    # 3) Fallback: title [+ subtitle] + tail categories + author.name
    if not parts:
        title = scrub(meta.get("title", ""))
        subtitle = scrub(meta.get("subtitle", ""))
        if title:
            parts.append(title + (f": {subtitle}" if subtitle else ""))

        cats = [scrub(x) for x in to_text_list(meta.get("categories")) if scrub(x)]
        if cats:
            parts.append(" > ".join(cats[-2:]) if len(cats) >= 2 else cats[-1])

        auth = meta.get("author")
        if isinstance(auth, dict) and auth.get("name"):
            parts.append(scrub(auth["name"]))

    return " ".join(p for p in parts if p)[:4000]


def shape_history(items, dedup_consec=True, max_history=None):
    """Remove consecutive duplicates and cap length to most recent `max_history`."""
    if dedup_consec and items:
        cleaned = [items[0]]
        for t in items[1:]:
            if t != cleaned[-1]:
                cleaned.append(t)
        items = cleaned
    if (max_history is not None) and len(items) > max_history:
        items = items[-max_history:]
    return items

def show_examples(df, k=3):
    print(f"Examples (k={k}):")
    for i in range(min(k, len(df))):
        r = df.iloc[i]
        print(f"- user={r.user_id} | hist_len={r.hist_len} | history[:5]={r.history[:5]}... | target={r.target}")

def eval_tail(c_loo: pd.DataFrame, target_freq: pd.Series,
              frac_list=(0.10, 0.15, 0.20, 0.25, 0.30)) -> pd.DataFrame:
    rows = []
    n_total = len(c_loo)
    for f in frac_list:
        cutoff = target_freq.quantile(f)
        tail_items = set(target_freq[target_freq <= cutoff].index)
        n_tail = int((c_loo["target"].isin(tail_items)).sum())
        rows.append({
            "tail_fraction": f,
            "freq_cutoff": int(cutoff),
            "tail_sequences": n_tail,
            "share_of_eval_%": 100.0 * n_tail / max(n_total, 1)
        })
    return pd.DataFrame(rows)