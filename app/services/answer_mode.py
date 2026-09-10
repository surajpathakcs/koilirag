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

import logfire
import numpy as np

from app.config import settings
from app.services.retrieval.embedding import embed_texts

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


_LEADING_NUMBER = re.compile(r"^\s*\d+(?:\.\d+)*\.?\s*")


def heading_text(chunk: Dict) -> str:
    """Task name for a section, without its numbering, with its parent module
    for context: '10.4. Assign IPN to a Merchant' -> 'Merchant: Assign IPN to a
    Merchant'."""
    parts = [p.strip() for p in (chunk.get("section_path") or "").split(" > ") if p.strip()]
    parts = [_LEADING_NUMBER.sub("", p) for p in parts[1:]]  # drop the doc title
    if not parts:
        return chunk.get("title", "")
    return f"{parts[0]}: {parts[-1]}" if len(parts) > 1 else parts[0]


def select_sections(query: str, candidates: List[Dict]) -> List[Dict]:
    """Pick the section(s) that answer the query.

    Body text across sibling sections in this manual is near-identical
    ("Navigate to the Assigned IPNs list...") so a body reranker cannot tell
    10.3/10.4/10.5 apart. The headings can: they are literally the task names.
    So re-score the reranked candidates on query<->heading similarity, take the
    best, and add another only if it is essentially tied — the real "two ways
    to do X" case (e.g. both password-setting methods).
    """
    if not candidates:
        return []
    if len(candidates) == 1:
        return candidates

    headings = [heading_text(c) for c in candidates]
    try:
        vecs = np.array(embed_texts([query] + headings), dtype=np.float32)
    except Exception as e:
        logfire.warning("Heading selection failed, falling back to rerank order: {e}", e=str(e))
        return candidates[: settings.MAX_ANSWER_CHUNKS]

    vecs /= np.linalg.norm(vecs, axis=1, keepdims=True) + 1e-8
    sims = vecs[1:] @ vecs[0]

    order = np.argsort(-sims)
    best = float(sims[order[0]])
    kept = [candidates[i] for i in order if best - float(sims[i]) <= settings.HEADING_TIE_DELTA]

    logfire.info(
        "Heading selection: {picked} (from {n} candidates)",
        picked=[headings[i] for i in order if best - float(sims[i]) <= settings.HEADING_TIE_DELTA],
        n=len(candidates),
    )
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
