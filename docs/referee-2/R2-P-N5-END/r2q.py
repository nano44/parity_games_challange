#!/usr/bin/env python3
"""REFEREE-2 successor 34: every «…» quote of P-N5-END (frozen 131b4c1c) and of line L-2 (2fcee038), looked up in TRUNK sources
(git show TRUNK:path; whitespace collapsed; a quote with an inner «…» is split there and every piece must occur). Own code.
Usage: r2q.py TRUNK  (run from the repo root)"""
import re, subprocess, sys
TR = sys.argv[1]
def show(rev, p): return subprocess.run(["git", "show", f"{rev}:{p}"], capture_output=True, text=True, check=True).stdout
def norm(s): return re.sub(r"\s+", " ", s).strip()
SRC = ["docs/RESULTS.md", "docs/new/N5-ssi-global.md", "docs/new/P-N5-XICYC.md", "docs/new/P-N5-REACH.md",
       "docs/new/P-N5-QUIET-fixes.md", "docs/DECISIONS.md", "docs/red/P-N5-REALIZE.md"]
src = {p: norm(show(TR, p)) for p in SRC}
pk = show("131b4c1c", "docs/new/P-N5-END.md"); l2 = show("2fcee038", "docs/new/P-N5-END-line-L2.txt")
fx = show("2fcee038", "docs/new/P-N5-END-fixes.md")
def quotes(t):  # nested-aware «…» extraction
    out, st = [], []
    for i, ch in enumerate(t):
        if ch == "«": st.append(i)
        elif ch == "»" and st:
            j = st.pop()
            if not st: out.append(t[j + 1:i])
    return out
tot = miss = 0
for name, t in (("packet", pk), ("L-2", l2)):
    for q in quotes(t):
        qn = norm(re.sub(r"[«»]", "", q)); pieces = [p.strip() for p in qn.split("…") if p.strip()]
        where = [p for p in SRC if all(pc in src[p] for pc in pieces)]
        # self-quotes of the packet/fixes (W-1 sentence, Lead freeze words, lane notes) are looked up in the fixes file too
        selfq = all(pc in norm(fx) for pc in pieces) or all(pc in norm(pk) for pc in pieces)
        tot += 1
        tag = ",".join(w.split("/")[-1] for w in where) if where else ("SELF(fixes/packet)" if selfq else "MISSING")
        if not where: miss += 1
        print(f"{name}\t{tag}\t{qn[:110]}")
print(f"quotes {tot}  not in trunk sources {miss}  (trunk {TR})")
