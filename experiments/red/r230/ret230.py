#!/usr/bin/env python3
"""L-RED 64 R230 item 6 (vs L-SI 50 BOX 98 CONJECTURE U-FREE): RETURNS in N5'-xi's mover phase on Gamma3(G).
Pigeonhole (PROVED, lane): every iteration before the first fallback switches >= 1 mover (REACH3-ALL: the mover parts form a HOW3 run,
which stops when no mover switches), and a mover can switch to an option it has NEVER held at most (deg(x) - 1) times, so
  T3 <= (M - N) + R,  R := #returns = #(iteration, mover) switches to an option the mover held before and abandoned.
So T3 super-linear in N + M needs R super-linear. Counters per genome (one run, states 0 .. first fallback):
  T3, R (returns), F (fresh switches), S (switch events = F + R), maxret (max returns of one mover).
Uses elev230.build (EKEY permutation if the genome has "ekey"; [E-LEV] order otherwise).
Usage: ret230.py G.json ... | ret230.py rand SEED COUNT [perm]"""
import sys, os, json, random
from elev230 import build, U, fix_ekey
from bonly3_230 import n5v, pg, topg, rgen
CAP = int(os.environ.get("CAP", "20000"))
def run(G):
    gm, sig0, tau0, V, O = build(G); N = G["N"]
    inv = {V[("m", q)]: q[1] for q in O}
    gp = pg.parse(topg(gm)); E, Ed = n5v.Engine(gp), n5v.Engine(n5v.dual(gp))
    s, t = n5v.n5x.start_pair(gp, E, Ed, None); seq = [tuple(inv.get(s[x], -1) for x in range(N))]
    while len(seq) <= CAP:
        r = n5v.step(gp, E, Ed, s, t, "xi")
        if r is None: break
        s, t, _, _, fb = r
        if fb: break
        seq.append(tuple(inv.get(s[x], -1) for x in range(N)))
    held = [{seq[0][x]} for x in range(N)]; R = F = 0; per = [0] * N
    for a, b in zip(seq, seq[1:]):
        for x in range(N):
            if a[x] != b[x]:
                if b[x] in held[x]: R += 1; per[x] += 1
                else: F += 1; held[x].add(b[x])
    return dict(N=N, M=len(O), U=U(G), T3=len(seq) - 1, R=R, F=F, S=R + F, maxret=max(per) if per else 0, seq=seq)
if __name__ == "__main__":
    tot = dict(genomes=0, T3=0, R=0, F=0, withR=0, maxT3=0, maxR=0)
    def add(tag, c):
        tot["genomes"] += 1; tot["T3"] += c["T3"]; tot["R"] += c["R"]; tot["F"] += c["F"]; tot["withR"] += c["R"] > 0
        tot["maxT3"] = max(tot["maxT3"], c["T3"]); tot["maxR"] = max(tot["maxR"], c["R"])
        if c["R"] or len(sys.argv) < 5 and sys.argv[1] != "rand":
            print(tag, {k: v for k, v in c.items() if k != "seq"}, flush=True)
    if sys.argv[1] == "rand":
        rng = random.Random(int(sys.argv[2])); perm = len(sys.argv) > 4
        for i in range(int(sys.argv[3])):
            G = rgen(rng, rng.randint(1, 5), rng.randint(1, 4), rng.choice([2, 3, 4]))
            if perm: G = fix_ekey(G, rng)
            add(f"r{i}", run(G))
    else:
        for f in sys.argv[1:]:
            G = json.load(open(f)); G.pop("_evals", None)
            if isinstance(G, dict) and "opts" in G: add(os.path.basename(f), run(G))
    print("TOTAL", tot, flush=True)
