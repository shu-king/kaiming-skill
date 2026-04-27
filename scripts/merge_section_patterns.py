#!/usr/bin/env python3
"""
Merge per-batch section-pattern JSONs into final per-section files.

Inputs:
  notes/section_patterns_v2/method_batch_a.json
  notes/section_patterns_v2/method_batch_b.json
  notes/section_patterns_v2/experiments_batch_a.json
  notes/section_patterns_v2/experiments_batch_b.json
  notes/section_patterns_v2/discussion_batch_a.json
  notes/section_patterns_v2/discussion_batch_b.json

Outputs (overwrites the v1 files):
  references/research/section-patterns/method.json
  references/research/section-patterns/experiments.json
  references/research/section-patterns/discussion.json   (NEW)

Dedup strategy:
  - For pattern lists (writing_patterns, ablation_specific_patterns,
    discussion_patterns, limitations_patterns, conclusion_patterns):
    deduplicate by pattern_name (case-insensitive); when names collide,
    merge evidence_quotes from both batches.
  - For string lists (anti_patterns_kaiming_would_flag, review_checklist):
    deduplicate by normalized text (lowercased, stripped of trailing
    punctuation). Keep first occurrence.
  - For closer_sentence_examples: dedup by normalized quote text.

After merge, sort each list alphabetically by pattern_name (or text)
for stable diffs.
"""
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
IN_DIR = REPO / "notes" / "section_patterns_v2"
OUT_DIR = REPO / "references" / "research" / "section-patterns"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def norm_text(s) -> str:
    if not isinstance(s, str):
        # Tolerate dict-shaped items that should have been strings —
        # try common keys, else stringify.
        if isinstance(s, dict):
            for k in ("text", "rule", "item", "phrase", "value", "description"):
                if k in s and isinstance(s[k], str):
                    s = s[k]
                    break
            else:
                s = json.dumps(s, sort_keys=True)
        else:
            s = str(s)
    s = re.sub(r"\s+", " ", s).strip().lower()
    s = re.sub(r"[.!?,;:]+$", "", s)
    return s


def load(name: str) -> dict:
    p = IN_DIR / name
    if not p.exists():
        print(f"  [warn] missing: {p}")
        return {}
    return json.loads(p.read_text())


def merge_pattern_list(a: list, b: list, key: str = "pattern_name") -> list:
    merged: dict[str, dict] = {}
    for item in (a + b):
        k = norm_text(item.get(key, ""))
        if not k:
            continue
        if k in merged:
            existing = merged[k]
            new_quotes = item.get("evidence_quotes", []) or []
            existing_quotes = existing.get("evidence_quotes", []) or []
            seen = {norm_text(q.get("quote", "")) for q in existing_quotes}
            for q in new_quotes:
                if norm_text(q.get("quote", "")) not in seen:
                    existing_quotes.append(q)
                    seen.add(norm_text(q.get("quote", "")))
            existing["evidence_quotes"] = existing_quotes
        else:
            merged[k] = dict(item)  # shallow copy
    out = list(merged.values())
    out.sort(key=lambda x: x.get(key, ""))
    return out


def merge_string_list(a: list, b: list) -> list:
    seen = {}
    for s in (a + b):
        k = norm_text(s)
        if not k:
            continue
        if k not in seen:
            # Store the original (preserve string form if it was already a string;
            # otherwise the normalized text)
            seen[k] = s if isinstance(s, str) else norm_text(s)
    return sorted(seen.values(), key=lambda s: norm_text(s))


def merge_closer_examples(a: list, b: list) -> list:
    seen = {}
    for item in (a + b):
        k = norm_text(item.get("quote", ""))
        if k and k not in seen:
            seen[k] = item
    return sorted(seen.values(), key=lambda x: x.get("source_id", ""))


# ───────────────────── Method ─────────────────────
ma = load("method_batch_a.json")
mb = load("method_batch_b.json")
method_out = {
    "_meta": {
        "papers_distilled": 26,
        "batches": ["method_batch_a (13 papers)", "method_batch_b (13 papers)"],
        "version": "v2 (refined from v1's 10 papers to 26 papers)",
    },
    "writing_patterns": merge_pattern_list(
        ma.get("writing_patterns", []), mb.get("writing_patterns", [])
    ),
    "anti_patterns_kaiming_would_flag": merge_string_list(
        ma.get("anti_patterns_kaiming_would_flag", []),
        mb.get("anti_patterns_kaiming_would_flag", []),
    ),
    "review_checklist": merge_string_list(
        ma.get("review_checklist", []), mb.get("review_checklist", [])
    ),
}
(OUT_DIR / "method.json").write_text(json.dumps(method_out, indent=2, ensure_ascii=False))
print(f"  method.json:    {len(method_out['writing_patterns'])} patterns, "
      f"{len(method_out['anti_patterns_kaiming_would_flag'])} anti-patterns, "
      f"{len(method_out['review_checklist'])} checklist items")

# ───────────────────── Experiments ─────────────────────
ea = load("experiments_batch_a.json")
eb = load("experiments_batch_b.json")
exp_out = {
    "_meta": {
        "papers_distilled": 26,
        "batches": ["experiments_batch_a (13 papers)", "experiments_batch_b (13 papers)"],
        "version": "v2 (refined from v1's 10 papers to 26 papers)",
    },
    "writing_patterns": merge_pattern_list(
        ea.get("writing_patterns", []), eb.get("writing_patterns", [])
    ),
    "ablation_specific_patterns": merge_pattern_list(
        ea.get("ablation_specific_patterns", []),
        eb.get("ablation_specific_patterns", []),
    ),
    "anti_patterns_kaiming_would_flag": merge_string_list(
        ea.get("anti_patterns_kaiming_would_flag", []),
        eb.get("anti_patterns_kaiming_would_flag", []),
    ),
    "review_checklist": merge_string_list(
        ea.get("review_checklist", []), eb.get("review_checklist", [])
    ),
}
(OUT_DIR / "experiments.json").write_text(json.dumps(exp_out, indent=2, ensure_ascii=False))
print(f"  experiments.json: {len(exp_out['writing_patterns'])} writing, "
      f"{len(exp_out['ablation_specific_patterns'])} ablation, "
      f"{len(exp_out['anti_patterns_kaiming_would_flag'])} anti-patterns, "
      f"{len(exp_out['review_checklist'])} checklist")

# ───────────────────── Discussion / Limitations / Conclusion ─────────────────────
da = load("discussion_batch_a.json")
db = load("discussion_batch_b.json")
disc_out = {
    "_meta": {
        "papers_distilled": 26,
        "batches": ["discussion_batch_a (13 papers)", "discussion_batch_b (13 papers)"],
        "version": "v1 (new in v1.3)",
    },
    "discussion_patterns": merge_pattern_list(
        da.get("discussion_patterns", []), db.get("discussion_patterns", [])
    ),
    "limitations_patterns": merge_pattern_list(
        da.get("limitations_patterns", []), db.get("limitations_patterns", [])
    ),
    "conclusion_patterns": merge_pattern_list(
        da.get("conclusion_patterns", []), db.get("conclusion_patterns", [])
    ),
    "closer_sentence_examples": merge_closer_examples(
        da.get("closer_sentence_examples", []),
        db.get("closer_sentence_examples", []),
    ),
    "anti_patterns_kaiming_would_flag": merge_string_list(
        da.get("anti_patterns_kaiming_would_flag", []),
        db.get("anti_patterns_kaiming_would_flag", []),
    ),
    "review_checklist": merge_string_list(
        da.get("review_checklist", []), db.get("review_checklist", [])
    ),
}
(OUT_DIR / "discussion.json").write_text(json.dumps(disc_out, indent=2, ensure_ascii=False))
print(f"  discussion.json:  {len(disc_out['discussion_patterns'])} discussion, "
      f"{len(disc_out['limitations_patterns'])} limitations, "
      f"{len(disc_out['conclusion_patterns'])} conclusion, "
      f"{len(disc_out['closer_sentence_examples'])} closers, "
      f"{len(disc_out['anti_patterns_kaiming_would_flag'])} anti-patterns, "
      f"{len(disc_out['review_checklist'])} checklist")
print(f"\nWrote 3 merged files to {OUT_DIR}")
