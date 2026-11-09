#!/usr/bin/env python3
"""REFEREE-2 successor 35: every «…» of P-N5-QN §1 (frozen e252182d) found in TRUNK docs/RESULTS.md (git show) and attributed to the
### R-entry holding it; P-N5-XICYC.md as second source. Own code. Usage: r2q.py TRUNK (repo root)"""
import re, subprocess, sys
TR = sys.argv[1]
def show(r, p): return subprocess.run(["git", "show", f"{r}:{p}"], capture_output=True, text=True, check=True).stdout
norm = lambda s: re.sub(r"\s+", " ", s).strip()
R = show(TR, "docs/RESULTS.md"); ents = re.split(r"\n(?=### R\d+ )", R); X = norm(show(TR, "docs/new/P-N5-XICYC.md"))
pk = show("e252182d", "docs/new/P-N5-QN.md"); sec1 = pk.split("## 1. Premises")[1].split("## 2.")[0]
def quotes(t):
    out, st = [], []
    for i, ch in enumerate(t):
        if ch == "«": st.append(i)
        elif ch == "»" and st:
            j = st.pop()
            if not st: out.append(t[j + 1:i])
    return out
tot = miss = 0
for q in quotes(sec1):
    qn = norm(q); pieces = [p.strip() for p in qn.split("…") if p.strip()]
    hits = [e.split(" ", 2)[1] for e in ents if all(pc in norm(e) for pc in pieces)]
    x = all(pc in X for pc in pieces); tot += 1; miss += not hits and not x
    print(f"{','.join(hits) or ('XICYC' if x else 'MISSING')}\t{qn[:100]}")
landed = [e.split(" ", 2)[1] for e in ents if e.startswith("### R")]
print(f"quotes {tot} missing {miss}; landed R104/R118/R121/R123: {[r for r in ('R104','R118','R121','R123') if r in landed]}  (trunk {TR})")
