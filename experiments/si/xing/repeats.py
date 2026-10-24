#!/usr/bin/env python3
"""L-SI box 4 (b): no-go test for potentials of a coarse state. For each joint λ-phase, find k < l with crossings in between and
the same coarse state at k and l, for coarse states: A = (R, θ, w); B = (R, θ, w, σ|R); C = (R, θ, w, σ̄(o)); D = (R, σ|R) (θ free).
A repeat of A between crossings means no Φ(R, θ, w) rises at every crossing transition. Usage: repeats.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xclass import *

def keys(g, r, o, E):
    R = frozenset(r["R"]); sR = tuple((v, r["s"][v]) for v in sorted(R) if g.owner[v] == 0)
    _, sb = E.evaluate(tuple(r["s"]))
    return dict(A=(R, r["th"], r["w"]), B=(R, r["th"], r["w"], sR), C=(R, r["th"], r["w"], sb[o]), D=(R, sR))

def scan(path):
    g = load(path); rows, ph = profile(g); assert_run(g, rows); o = annotate(g, rows); E = Engine(g); res = {}
    for (x, y) in ph:
        K = [keys(g, rows[k], o, E) for k in range(x, y + 1)]
        xs = [int(rows[k]["R"] != rows[k + 1]["R"]) for k in range(x, y)]
        for c in "ABCD":
            seen = {}; best = None
            for i, kk in enumerate(K):
                if kk[c] in seen:
                    j = seen[kk[c]]; nx = sum(xs[j:i])
                    if nx and (best is None or nx > best[0]): best = (nx, x + j, x + i)
                else: seen[kk[c]] = i
            if best and (c not in res or best[0] > res[c][0]): res[c] = best
    return g.n, res

if __name__ == "__main__":
    for p in sys.argv[1:]:
        n, res = scan(p); print(os.path.basename(p), "n", n, {c: f"{v[0]} crossings between states {v[1]},{v[2]}" for c, v in sorted(res.items())})
