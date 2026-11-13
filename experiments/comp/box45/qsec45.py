#!/usr/bin/env python3
"""L-COMP box 45 item (b): the per-gate Λ-quiet flip maximum on a SECOND, other-lane engine: L-RED 65's HOW3 engine (claude/l-red
59daaef2 experiments/red/r232/how3_232.py, read-only, as L-SI box 100's cross100.py uses it). The counter loop is cross100's (claude/l-si
23d39400 experiments/si/box100/cross100.py one(): a flip of gate g at t -> t+1 is charged to the face a it leaves; quiet iff Λ(a) does not
change), restricted to what I need and kept PER GATE: qmax = max over gates of quiet flips, maxfl = max over gates of flips, T3.
Usage (env RED = an archive root of claude/l-red 59daaef2 (experiments/red, harness, hard-families, n5-second); env LNEW = an archive
root of claude/l-new fcba92fc (experiments/new, experiments/si/si.py, harness), which L-RED's bonly3_230 reads, as for cross100):
  qsec45.py G.json ...   -> one line per genome"""
import sys, os, json
sys.path.insert(0, os.path.join(os.environ["RED"], "experiments/red/r232"))
import how3_232 as H


def one(G):
    full = []; seq = H.how3(G, full=full); T = len(seq) - 1; V = full[0][2]; qmax = maxfl = qtot = 0
    for x in range(G["N"]):
        for k in range(len(G["opts"][x])):
            g, pe, pb = V[("g", (x, k))], V[("pe", (x, k))], V[("pbeta", (x, k))]
            ve = [f[0][pe] for f in full]; vb = [f[0][pb] for f in full]; ch = [f[1][g] for f in full]; fl = q = 0
            for t in range(T):
                if ch[t] != ch[t + 1]:
                    fl += 1; va = ve if ch[t] == pe else vb
                    if va[t][0] == va[t + 1][0]: q += 1
            qmax = max(qmax, q); maxfl = max(maxfl, fl); qtot += q
    return dict(T3=T, qmax=qmax, maxfl=maxfl, qflip=qtot)


for f in sys.argv[1:]:
    G = json.load(open(f)); G = G.get("genome", G); G.pop("_evals", None)
    print(os.path.basename(f), "N+M", G["N"] + sum(map(len, G["opts"])), json.dumps(one(G)), flush=True)
