#!/usr/bin/env python3
"""L-NEW box 59: CONJECTURE FLIP-REC probe. Per game: SBC_sigma, n, k (Odd vertices with >= 2 successors), and over Odd u:
max flips(u), max flips(u) - 2 REC(u) (FLIP-REC predicts <= 1), REC as in flips.rec_stats. One line per game. Usage: frec.py GAME.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import flips
g, E, seq, ev = flips.run(sys.argv[1]); rows = flips.rec_stats(g, E, seq, ev)
k = sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1)
sbc = len({e["j"] for e in ev})
mf = max((r[1] for r in rows), default=0); ex = max((r[1] - 2 * r[2] for r in rows), default=0)
w = max(rows, key=lambda r: r[1] - 2 * r[2]) if rows else None
print(f"FREC {os.path.basename(sys.argv[1])} n {g.n} k {k} orbit {len(seq)} SBC {sbc} maxflips {mf} maxexcess {ex} worst {w}", flush=True)
