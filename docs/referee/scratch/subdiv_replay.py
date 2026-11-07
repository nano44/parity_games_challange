"""REFEREE successor 25: DEAD SUBDIV replay (P-N5-REACH §9) with my own G^pad builder (from §9's text) and L-COMP's n5b (spec mode).
G from (σ0, τ0); G^pad from S3 (n5b's default best-reward start). Usage: subdiv_replay.py N5SECOND_DIR OUTDIR"""
import sys, os
D, OUT = sys.argv[1], sys.argv[2]; sys.path.insert(0, D); sys.path.insert(0, os.path.join(D, "..", "hard-families")); sys.path.insert(0, os.path.join(D, "..", "harness"))
import n5b, pg
n5b.MODE = "spec"
EVEN, ODD = 0, 1
inst = {"A": dict(pr=[3, 3, 1], ow=[ODD, EVEN, ODD], su=[[1], [0, 1, 2], [0]], s0={1: 1}, t0={0: 1, 2: 0}),
        "B": dict(pr=[3, 2, 4, 0, 0], ow=[ODD, ODD, EVEN, ODD, EVEN], su=[[1, 3, 4], [2, 3], [3, 4], [0, 2, 3], [1, 4]],
                  s0={2: 4, 4: 1}, t0={0: 4, 1: 2, 3: 2})}
def write(path, pr, ow, su):
    with open(path, "w") as f:
        f.write("parity %d;\n" % (len(pr) - 1))
        for v in range(len(pr)): f.write("%d %d %d %s;\n" % (v, pr[v], ow[v], ",".join(map(str, su[v]))))
def run(path, sig=None, tau=None):
    g = pg.read(path); s = n5b.N5(g); tr = []; fbt = []
    if sig is not None:
        S0 = [-1] * g.n; T0 = [-1] * g.n
        for a, b in sig.items(): S0[a] = b
        for a, b in tau.items(): T0[a] = b
        sig, tau = S0, T0
    _, _, it, fb = s.run(sig, tau, trace=tr, fbtrace=fbt); return it, fb, tr, fbt
for name, I in inst.items():
    n = len(I["pr"]); p = os.path.join(OUT, name + ".pg"); write(p, I["pr"], I["ow"], I["su"])
    edges = sorted((a, b) for a in range(n) for b in I["su"][a]); pid = {e: n + i for i, e in enumerate(edges)}
    pr = [x + 4 for x in I["pr"]]; ow = list(I["ow"]); su = [[pid[(a, b)] for b in I["su"][a]] for a in range(n)]
    for (a, b) in edges:
        om = 2 if (I["ow"][a] == EVEN and I["s0"].get(a) == b) else (1 if (I["ow"][a] == ODD and I["t0"].get(a) == b) else 0)
        pr.append(om); ow.append(EVEN); su.append([b])
    pp = os.path.join(OUT, name + "_pad.pg"); write(pp, pr, ow, su)
    it, fb, tr, fbt = run(p, I["s0"], I["t0"]); it2, fb2, tr2, fbt2 = run(pp)
    st = tr2[0]; trans = all(st[0][a] == pid[(a, b)] for a, b in I["s0"].items()) and all(st[1][a] == pid[(a, b)] for a, b in I["t0"].items())
    print(name, "n", n, "G from (s0,t0): iterations", it, "fallbacks", fb, "flags", fbt, "| G^pad n", len(pr), "from S3: iterations", it2,
          "fallbacks", fb2, "flags", fbt2, "| S3 start = transported:", trans)
