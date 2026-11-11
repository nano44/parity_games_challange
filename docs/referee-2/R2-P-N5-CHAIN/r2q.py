#!/usr/bin/env python3
"""REFEREE-2 successor 35: every «…» quote of P-N5-CHAIN (frozen 93531b03) and of line L-1 (71b75424), looked up in TRUNK sources
(git show TRUNK:path) and in the cited lane packets at their pinned commits (whitespace collapsed; a quote with an inner «…» is split
there and every piece must occur). Own code (adapted from R2-P-N5-END/r2q.py). Usage: r2q.py TRUNK  (run from the repo root)"""
import re, subprocess, sys
TR = sys.argv[1]
def show(rev, p): return subprocess.run(["git", "show", f"{rev}:{p}"], capture_output=True, text=True, check=True).stdout
def norm(s): return re.sub(r"\s+", " ", s).strip()
SRC = {f"trunk:{p}": (TR, p) for p in ["docs/RESULTS.md", "docs/new/N5-ssi-global.md", "docs/new/P-N5-XICYC.md",
       "docs/new/P-N5-REACH.md", "docs/new/P-N5-XICYC-fixes.md", "docs/DECISIONS.md"]}
SRC["END@131b4c1c"] = ("131b4c1c", "docs/new/P-N5-END.md")
SRC["ASC@93531b03"] = ("93531b03", "docs/new/P-N5-ASC.md")
src = {}
for k, (r, p) in SRC.items():
    try: src[k] = norm(show(r, p))
    except subprocess.CalledProcessError: print(f"# source missing: {k}"); src[k] = ""
pk = show("93531b03", "docs/new/P-N5-CHAIN.md"); l1 = show("71b75424", "docs/new/P-N5-CHAIN-line-L1.txt")
def quotes(t):
    out, st = [], []
    for i, ch in enumerate(t):
        if ch == "«": st.append(i)
        elif ch == "»" and st:
            j = st.pop()
            if not st: out.append(t[j + 1:i])
    return out
tot = miss = 0
for name, t in (("packet", pk), ("L-1", l1)):
    for q in quotes(t):
        qn = norm(re.sub(r"[«»]", "", q)); pieces = [p.strip() for p in qn.split("…") if p.strip()]
        where = [k for k in src if src[k] and all(pc in src[k] for pc in pieces)]
        selfq = all(pc in norm(pk) for pc in pieces) and not where
        tot += 1
        tag = ",".join(w.split("/")[-1] for w in where) if where else "MISSING"
        if not where: miss += 1
        print(f"{name}\t{tag}\t{qn[:110]}")
print(f"quotes {tot}  not in any source {miss}  (trunk {TR})")
