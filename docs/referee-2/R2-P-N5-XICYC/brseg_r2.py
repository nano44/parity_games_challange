#!/usr/bin/env python3
"""Box 191: BR-SEG on GENERAL games. Howard (every Even vertex to a VJ-best successor, keep current on ties) from the best-reward
start; label steps C / R / p as in subrun191.py; report max pure run vs nE (# Even vertices) and whether a switched Even vertex was its
own cycle node at the step (hypothesis H0 of BR-SEG). Usage: brseg_gen191.py random COUNT SEED n | file.pg ..."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, "experiments/si"), os.path.join(ROOT, "experiments/harness")]
import pg
TOT = [0, 0, 0]   # steps, steps with some switched v own cycle node at t (the line's count), H0 failures
from si import Engine

def howard(g, cap=100000):
    E = Engine(g); s = E.initial("best"); vs, sb = E.evaluate(s); lab = []; h0 = 0
    while len(lab) < cap:
        ns = tuple(max(E.succ[v], key=lambda w: (E.key(vs[w]), w == s[v], w)) if g.owner[v] == 0 else -1 for v in range(g.n))
        if ns == s: break
        h0 += any(ns[v] != s[v] and vs[v][0] == v for v in range(g.n))
        nvs, nsb = E.evaluate(ns)
        TOT[0] += 1; TOT[1] += any(ns[v] != s[v] and vs[v][0] == v for v in range(g.n)); TOT[2] += not any(ns[v] != s[v] and vs[v][0] != v and nvs[v][0] != v for v in range(g.n))
        lab.append("C" if any(nvs[v][0] != vs[v][0] for v in range(g.n)) else ("R" if any(nsb[v] != sb[v] for v in range(g.n) if g.owner[v] == 1) else "p"))
        s, vs, sb = ns, nvs, nsb
    lab = "".join(lab); mp = max(len(r) for r in lab.replace("R", "C").split("C")) if lab else 0
    return lab, mp, h0

if __name__ == "__main__":
    if sys.argv[1] == "random":
        cnt, seed, n = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed); viol = vh = 0; worst = 0
        for i in range(cnt):
            g = pg.Game([rng.randrange(n + 1) for _ in range(n)], [rng.randrange(2) for _ in range(n)], [sorted(rng.sample(range(n), rng.randint(1, min(3, n)))) for _ in range(n)])
            nE = sum(1 for v in range(n) if g.owner[v] == 0) or 1; lab, mp, h0 = howard(g)
            viol += mp > nE; vh += (mp > nE and h0 > 0); worst = max(worst, mp / nE)
        print("R2 steps", TOT[0], "own-cycle-node-switch steps", TOT[1], "H0 failures", TOT[2]); print(f"random count {cnt} seed {seed} n {n}: maxpure > nE in {viol} (of which with an H0 event: {vh}); max maxpure/nE {worst:.2f}")
    else:
        for f in sys.argv[1:]:
            g = pg.read(f) if hasattr(pg, "read") else pg.load(f); nE = sum(1 for v in range(g.n) if g.owner[v] == 0)
            lab, mp, h0 = howard(g); print(f"{os.path.basename(f)} n {g.n} nE {nE} T {len(lab)} C {lab.count('C')} R {lab.count('R')} p {lab.count('p')} maxpure {mp} H0events {h0}")
