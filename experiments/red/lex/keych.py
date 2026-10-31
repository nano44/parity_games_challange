#!/usr/bin/env python3
"""L-RED R153: KEYCH on n5b SPEC traces. For every W-run F and every vertex v not in C with Omega(lambda_W(v)) even, split F into the
maximal W-constant intervals of v (W(v) unchanged), and count KEYCH = strict lex decreases of key(v) (red/tie/o1key.key: v's
(sigma, tau)-path read from c) inside one interval; KEY-MON (R152) says key never rises there. Prints max KEYCH (vertex, interval), the
longest W-run, and n. Usage: keych.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn")); sys.path.insert(0, os.path.join(HERE, "..", "tie"))
import xcn, n5b, o1key
pg = xcn.pg
def keych(g, tr, fb):
    runs, W = xcn.wruns(g, tr, fb); best = (0, None, None, None); maxL = 0; rise = 0
    for F in runs:
        if len(F) < 2: continue
        maxL = max(maxL, len(F) - 1); t = tr[F[0]][1]; Ws = [W(tr[k][0], t) for k in F]
        for v in range(g.n):
            c = Ws[0][v][0]
            if c == v or g.prio[c] % 2: continue
            cnt = 0; st = F[0]; kp = o1key.key(g, tr[F[0]][0], t, v, c)
            for i in range(1, len(F)):
                kk = o1key.key(g, tr[F[i]][0], t, v, c)
                if Ws[i][v] != Ws[i - 1][v]: cnt = 0; st = F[i]
                elif kk < kp:
                    cnt += 1
                    if cnt > best[0]: best = (cnt, v, st, F[i])
                elif kk > kp: rise += 1
                kp = kk
    return best, maxL, rise
if __name__ == "__main__":
    g = pg.read(sys.argv[1]); st = n5b.read_start(sys.argv[2], g) if len(sys.argv) > 2 else (None, None)
    try: tr, fb = xcn.trace(g, *st)
    except Exception as e: print(f"KEYCH {os.path.basename(sys.argv[1])} n {g.n} RUN-ERROR {e}"); sys.exit(0)
    b, maxL, rise = keych(g, tr, fb)
    print(f"KEYCH {os.path.basename(sys.argv[1])} n {g.n} iters {len(tr)-1} maxL {maxL} maxKEYCH {b[0]} (v {b[1]} from {b[2]} to {b[3]}) keyrises_at_fixed_W {rise}")
