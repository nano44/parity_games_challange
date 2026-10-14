#!/usr/bin/env python3
"""Shape checks for the fleet's state files. Exit 1 on any violation."""
import re, sys, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
errs = []
def lines(p): return (R / p).read_text().splitlines()
for p, cap in [("docs/NOW.md", 150), ("CLAUDE.md", 80), ("TARGET.md", 120)]:
    if not (R / p).exists(): errs.append(f"missing {p}")
    elif len(lines(p)) > cap: errs.append(f"{p}: {len(lines(p))} lines > {cap}")
# Every D-number in DECISIONS.md has an index row with a valid status.
dec = set(re.findall(r"^## (D\d+)\b", (R / "docs/DECISIONS.md").read_text(), re.M))
idx = {}
for l in lines("docs/DECISIONS-INDEX.md"):
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    if len(c) >= 4 and re.fullmatch(r"D\d+", c[0]): idx[c[0]] = c[3]
for d in sorted(dec):
    if d not in idx: errs.append(f"DECISIONS-INDEX: no row for {d}")
for d, s in idx.items():
    if s not in {"active", "amended", "superseded", "reversed"}: errs.append(f"DECISIONS-INDEX {d}: bad status {s!r}")
# GAPS rows: id, severity, owner, status.
for l in lines("docs/GAPS.md"):
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    if l.startswith("|") and len(c) >= 4 and c[0] not in {"id", ""} and not set(c[0]) <= set("- "):
        if c[1] not in {"blocker", "major", "minor"}: errs.append(f"GAPS {c[0]}: bad severity {c[1]!r}")
        if not c[2]: errs.append(f"GAPS {c[0]}: no owner")
        if c[3] not in {"open", "in-progress", "closed"}: errs.append(f"GAPS {c[0]}: bad status {c[3]!r}")
# RESULTS entries are labelled.
for l in lines("docs/RESULTS.md"):
    if l.startswith("### ") and not re.search(r"\[(formalized|refereed-only)\]", l):
        errs.append(f"RESULTS entry not labelled formalized|refereed-only: {l}")
# Notebooks keep sources and dead ends.
for nb in (R / "notes").glob("*.md"):
    t = nb.read_text()
    for sec in ("## Sources opened", "## Dead ends", "## Resume point"):
        if sec not in t: errs.append(f"{nb.relative_to(R)}: missing section {sec!r}")
for e in errs: print("  -", e)
sys.exit(1 if errs else 0)
