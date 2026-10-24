#!/usr/bin/env python3
"""Box 25: σ̄-laps on o-cyclic C^1O. A LAP is a state k inside one (τ, joint-λ)-phase where σ̄(o) returns to an exit it left
earlier in the same phase (θ is then strictly higher: θ ↑ and θ changed in between). Reports, per run: laps, θ-changes per phase.
Usage: lapsearch.py game.pg [start] | lapsearch.py --random N nmin nmax seed [--keep DIR]"""
from common import *
def laps(g, st):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g)
    rows = []
    for s, t in st:
        Xi, sb = E.evaluate(s); U, _ = Ed.evaluate(t)
        rows.append(((tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), sb[o], E.key(Xi[o])))
    nl = 0; maxth = 0; k = 0; first = None
    while k < len(rows):
        j = k
        while j + 1 < len(rows) and rows[j + 1][0] == rows[k][0]: j += 1
        seen, cur, th = [], None, 0
        for i in range(k, j + 1):
            a = rows[i][1]
            if a != cur:
                if a in seen:
                    nl += 1
                    if first is None: first = i
                seen.append(a); cur = a
            if i > k and rows[i][2] != rows[i - 1][2]: th += 1
        maxth = max(maxth, th); k = j + 1
    return nl, maxth, first
if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--random":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); keep = a[a.index("--keep") + 1] if "--keep" in a else None
        best = {}; cnt = 0
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            cnt += 1; st, _ = trace(g, check=False); nl, mt, _ = laps(g, st)
            if nl and (g.n not in best):
                best[g.n] = (nl, mt, i); print("lap at n", g.n, "game", i, "laps", nl, "maxθ/phase", mt, flush=True)
                if keep: pg.write(g, os.path.join(keep, f"lap_n{g.n}_s{seed}_{i}.pg")) if hasattr(pg, "write") else open(os.path.join(keep, f"lap_n{g.n}_s{seed}_{i}.pg"), "w").write(
                    f"parity {g.n-1};\n" + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n)))
        print("games", cnt, "smallest n with a lap:", min(best) if best else None)
    else:
        g = load(a[0]); s0 = readstart(a[1]) if len(a) > 1 else None; st, _ = trace(g, s0); print(laps(g, st), "n", g.n)
