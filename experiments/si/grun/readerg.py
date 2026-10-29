#!/usr/bin/env python3
"""L-SI box 25 (successor 21): DATA for docs/si/N5-GRUN-box25.md §3 (G is not reader-invariant). Greedy: add Odd READER vertices (no
predecessors, priority 0, edges to a random set of 2-6 vertices of one honest class at the start, root/mkoreader.py's construction) to
GAME, keep a reader only if the run on the old vertices is unchanged (sigma, tau, sigma-bar, fallbacks on old vertices; root/orcheck.py's
SAME test, done here in-process) and tau (readers included) and every reader's cycle node stay constant on the base's longest run [a, b], so [a, b] is still a
fallback-free run of one phase; G is counted on [a, b] and kept only if it grows. Prints per added reader: n, run, G.
Usage: readerg.py GAME START READERS TRIES SEED OUTPREFIX"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
for p in (os.path.join(HERE, "..", "root"), os.path.join(HERE, "..", "runlin")): sys.path.insert(0, p)
from common import rows, load, readstart
from trace import runs
import pg

def longest(R):
    a, b, i, j = max(runs(R), key=lambda r: r[1] - r[0])
    return a, b, sum(R[t]["sb"] != R[t + 1]["sb"] for t in range(a, b))

def main():
    gp, sp, nr, tries, seed, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    rng = random.Random(seed); g = load(gp); s0, t0 = readstart(sp); n0 = g.n
    E, R0 = rows(g, (s0, t0)); a, b, G = longest(R0); print("base n", g.n, "run", b - a, "G", G, flush=True)
    cls = {}
    for v in range(n0): cls.setdefault(R0[a]["vs"][v][0], []).append(v)
    big = [c for c in cls.values() if len(c) >= 2]
    prio, owner, succ = list(g.prio), list(g.owner), [list(x) for x in g.succ]; t0 = dict(t0)
    for r in range(nr):
        best = None
        for _ in range(tries):
            S = sorted(rng.sample(rng.choice(big), min(len(rng.choice(big)), rng.randint(2, 6)))) if big else None
            if not S or len(S) < 2: continue
            h = pg.Game(prio + [0], owner + [1], succ + [S]); tt = dict(t0); tt[h.n - 1] = S[0]
            try: E1, R1 = rows(h, (s0, tt))
            except (RecursionError, RuntimeError): continue
            if len(R1) != len(R0) or any(R1[k]["s"][:n0] != R0[k]["s"][:n0] or R1[k]["sb"][:n0] != R0[k]["sb"][:n0] or R1[k]["fb"] != R0[k]["fb"]
                                         or R1[k]["t"][:n0] != R0[k]["t"][:n0] for k in range(len(R0))): continue
            if any(R1[k]["t"] != R1[a]["t"] or R1[k]["vs"][h.n - 1][0] != R1[a]["vs"][h.n - 1][0] for k in range(a, b + 1)): continue
            G1 = sum(R1[t]["sb"] != R1[t + 1]["sb"] for t in range(a, b))      # the base run's window: still one fallback-free run
            if best is None or G1 > best[0]: best = (G1, h, tt, S, b - a)
        if best is None or best[0] <= G: print("reader", r, "no gain", flush=True); continue
        G, h, t0, S, run = best; prio, owner, succ = list(h.prio), list(h.owner), [list(x) for x in h.succ]
        print("reader", r, "S", S, "n", h.n, "run", run, "G", G, flush=True)
        with open(out + ".pg", "w") as f:
            f.write("parity %d;\n" % (h.n - 1))
            for v in range(h.n): f.write("%d %d %d %s;\n" % (v, h.prio[v], h.owner[v], ",".join(map(str, h.succ[v]))))
        with open(out + ".start", "w") as f:
            f.write("SIGMA0 " + " ".join("%d:%d" % (v, s0[v]) for v in sorted(s0)) + "\n")
            f.write("TAU0 " + " ".join("%d:%d" % (v, t0[v]) for v in sorted(t0)) + "\n")

if __name__ == "__main__":
    main()
