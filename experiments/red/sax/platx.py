#!/usr/bin/env python3
"""L-RED successor 38 (R164): run L-SI box 58 anc.py (path in env ANC, read-only; l-si 6370a35f) on an N5 run and print the longest
equal-swap-key escape plateau: (W-run, Odd s, old choice x) with labels, the W-run's span, and the (transition, swap key) list.
Usage: ANC=.../anc.py platx.py G.pg START"""
import sys, os, re, io, contextlib
src = open(os.environ["ANC"]).read(); glb = {"__file__": os.environ["ANC"], "__name__": "__main__"}
sys.argv = [os.environ["ANC"]] + sys.argv[1:]
buf = io.StringIO()
with contextlib.redirect_stdout(buf): exec(compile(src, os.environ["ANC"], "exec"), glb)
print(buf.getvalue().strip().split("\n")[-1][:160])
LAB = [l.split('"')[1] if '"' in l else str(i) for i, l in enumerate(x for x in open(sys.argv[1]) if re.match(r"\s*\d", x))]
seqs, plat, runof = glb["seqs"], glb["_plat"], glb["runof"]
best = sorted(seqs.items(), key=lambda kv: (plat(kv[1]), len(kv[1])), reverse=True)[:3]
for (r, s, x), v in best:
    span = [u for u, rr in runof.items() if rr == r]
    print(f"PLAT {plat(v)} run {r} [{min(span)}..{max(span)}] (len {len(span)}) s {s}={LAB[s]} x {x}={LAB[x]} escapes {[(u, og) for u, og in v]}")
