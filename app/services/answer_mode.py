"""
Decides how an answer is built.

The manual is one self-contained section per chunk, and its procedures are
already written as numbered steps with screenshots in the right places. So when
the retrieved sections are procedural we render them verbatim (exact button
names, exact screenshot positions, no paraphrase drift) and the LLM only writes
a short lead-in. Conceptual sections fall back to normal synthesis.
"""
import re
from typing import List, Dict

from app.config import settings

VERBATIM = "verbatim"
SYNTHESIS = "synthesis"

_MARKER = re.compile(r"\[\[IMAGE:")
_STEP = re.compile(r"^\s*(?:[-*•]|\d+\.)\s*(?:click|navigate|hover|enter|select|open|go to)\b", re.I | re.M)

# Questions that want an explanation woven across sections, not a step list.
_SYNTHESIS_VERB = re.compile(
    r"\b(what is|what are|why|explain|describe|difference|differences|compare|"
    r"list all|overview|when should|who can)\b",
    re.I,
)


def gate_by_score(reranked: List[Dict]) -> List[Dict]:
    """Keep chunks scoring within RERANK_SCORE_RATIO of the top hit. The
    cross-encoder already judged query relevance — reuse that instead of
    handing the LLM chunks it will ignore."""
    if not reranked:
        return []
    top = reranked[0].get("score") or 0.0
    if top <= 0:
        kept = reranked[:1]
    else:
        cutoff = settings.RERANK_SCORE_RATIO * top
        kept = [d for d in reranked if (d.get("score") or 0.0) >= cutoff]
    return kept[: settings.MAX_ANSWER_CHUNKS]


def is_procedural(chunk: Dict) -> bool:
    md = chunk.get("content_md", "") or ""
    return bool(_MARKER.search(md) or _STEP.search(md))


def decide(query: str, chunks: List[Dict]) -> str:
    if not chunks:
        return SYNTHESIS
    if _SYNTHESIS_VERB.search(query or ""):
        return SYNTHESIS
    if any(is_procedural(c) for c in chunks):
        return VERBATIM
    return SYNTHESIS


def section_heading(chunk: Dict) -> str:
    """Last segment of the breadcrumb, e.g. '10.4. Assign IPN to a Merchant'."""
    path = chunk.get("section_path", "") or ""
    return path.split(" > ")[-1] if path else "From the manual"


def section_body(chunk: Dict) -> str:
    """content_md minus its leading breadcrumb line."""
    md = (chunk.get("content_md") or chunk.get("content") or "").strip()
    parts = md.split("\n\n", 1)
    return parts[1].strip() if len(parts) == 2 else md


def render_verbatim(chunks: List[Dict], lead_in: str) -> str:
    """Lead-in sentence + each section reproduced exactly as the manual has it,
    screenshot markers included and already in the right positions."""
    out = [lead_in.strip()] if lead_in and lead_in.strip() else []
    multi = len(chunks) > 1
    for c in chunks:
        if multi:
            out.append(f"### {section_heading(c)}")
        out.append(section_body(c))
    return "\n\n".join(p for p in out if p).strip()
