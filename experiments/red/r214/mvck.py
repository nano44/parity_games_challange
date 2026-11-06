#!/usr/bin/env python3
"""L-RED R214 mvck: per-mover max number of moves over every run (all 2^N starts) of an IDEAL genome (box150-style JSON), replayed by
r187/ideal.py. moves(x) = #steps where mover x changes option. Prints per mover: level, Xi-target flag, max moves; and the max over
Xi-targets / non-targets vs 2d (d = number of levels). Usage: mvck.py g1.json [g2.json ...]   (env STARTS=stored: only the stored start)"""
import sys, os, json, itertools
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
def check(G, allstarts=True):
    N = G["N"]; d = max(G["lev"]) + 1; nopt = [len(o) for o in G["opts"]]
    tg = [any(o[1] == z for v in range(N) for o in G["opts"][v]) for z in range(N)]
    best = [0] * N; arg = [None] * N; Tmax = 0
    starts = itertools.product(*[range(k) for k in nopt]) if allstarts else [tuple(G["start"])]
    for st in starts:
        H2 = dict(G); H2["start"] = list(st); S, how = ideal.traj(H2)
        assert how in ("opt", "stuck"), (how, st)
        Tmax = max(Tmax, len(S) - 1)
        for z in range(N):
            m = sum(1 for u in range(1, len(S)) if S[u][z] != S[u - 1][z])
            if m > best[z]: best[z] = m; arg[z] = st
    return d, tg, best, arg, Tmax
if __name__ == "__main__":
    for f in sys.argv[1:]:
        G = json.load(open(f)); d, tg, best, arg, T = check(G, os.environ.get("STARTS") != "stored")
        mt = max([b for b, t in zip(best, tg) if t] or [0]); mn = max([b for b, t in zip(best, tg) if not t] or [0])
        flag = "KILL" if max(best) > 2 * d else "ok"
        print(f"{f}: d {d} N {G['N']} T {T} maxmoves target {mt} nontarget {mn} 2d {2*d} {flag} per-mover " +
              " ".join(f"{z}:L{G['lev'][z]}{'t' if tg[z] else 'n'}{best[z]}" for z in range(G['N'])), flush=True)
