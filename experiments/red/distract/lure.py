#!/usr/bin/env python3
"""L-RED (2026-10-16, produced on Opus 5.5): a "lure" transform reading van Dijk's section 6 item 7 (see distract.py).
DTL prunes a candidate u (a p-top that cannot stay in Z) unless a threshold attractor at t < pr(u) reaches it ("good path").
Lure: shift all priorities of the base game up by 4 (parities kept), add a small dominion s_p of priority p for each
chosen player p (p-owned self-loop), and for every p-owned vertex u of p's parity a fresh p-owned vertex y_u of priority
(2 + (1-p))... i.e. between s_p's cap and pr(u), with u -> y_u -> s_p.  y_u is rescued at t = pr(y_u) (edge into s_p's
region) and then u at t = pr(y_u) < pr(u): u is never pruned.  The dominion s_p is the LOWEST priority, i.e. found last.
With LEN > 1 the lure is a path y_u^1 -> ... -> y_u^LEN -> s_p (all of priority pr(y)).
Usage: lure.py BASE.pg PLAYERS(0|1|01) [LEN] > out.pg"""
import sys


def read_pg(path):
    vs = []
    for line in open(path):
        line = line.strip()
        if not line or line.startswith("parity") or line.startswith("start"): continue
        parts = line.rstrip(";").split()
        vs.append((int(parts[0]), int(parts[1]), int(parts[2]), [int(x) for x in parts[3].rstrip(";").split(",")]))
    return vs


def lure(base, players, L=1):
    vs = [(v, pr + 4, ow, list(s)) for v, pr, ow, s in base]
    n = len(vs); out = {v: [pr, ow, s] for v, pr, ow, s in vs}
    ypr = {0: 1, 1: 2}                 # s_0 = 0 < y_0 = 1 < every Even vertex (>= 4); s_1 = 1 < y_1 = 2 < every Odd vertex (>= 5)
    for p in players:
        s = n; n += 1; out[s] = [p, p, [s]]
        for v, pr, ow, succ in vs:
            if ow == p and pr % 2 == p:
                prev = v
                for k in range(L):
                    y = n; n += 1; out[y] = [ypr[p], p, []]
                    out[prev][2].append(y); prev = y
                out[prev][2].append(s)
    lines = [f"parity {n - 1};"] + [f"{v} {pr} {ow} {','.join(map(str, s))};" for v, (pr, ow, s) in sorted(out.items())]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    players = [int(c) for c in sys.argv[2]]
    sys.stdout.write(lure(read_pg(sys.argv[1]), players, int(sys.argv[3]) if len(sys.argv) > 3 else 1))
