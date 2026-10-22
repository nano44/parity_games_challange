#!/usr/bin/env python3
"""Box 11 (K9's factor): structure of best-reply changes along N5's run (n5_lock.step = n5.py's loop, best-reward start).
sigma-bar_k = Odd's VJ best reply to sigma_k (on Odd vertices), tau-bar_k = Even's best reply to tau_k (on Even vertices).
Per run: changes of sigma-bar / tau-bar (as whole vectors); per-vertex changes; per-vertex REVISITS (the vertex's best reply returns to a
successor it used earlier in the run); GLOBAL RETURNS (the whole vector sigma-bar or tau-bar equals an earlier one after having changed).
Usage: brstruct.py game.pg [...]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, ".."))
from n5_lock import step
from n5 import pg, Engine, dual
def analyse(g):
    E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best"))
    O = [v for v in range(g.n) if g.owner[v] == 1]; V0 = [v for v in range(g.n) if g.owner[v] == 0]
    seqs = {"sb": [], "tb": []}; it = 0
    while True:
        seqs["sb"].append(tuple(E.evaluate(tuple(s))[1][v] for v in O)); seqs["tb"].append(tuple(Ed.evaluate(tuple(t))[1][v] for v in V0))
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t = r[0], r[1]; it += 1
    out = {"iterations": it}
    for key, verts in (("sb", O), ("tb", V0)):
        seq = seqs[key]; ch = sum(1 for i in range(1, len(seq)) if seq[i] != seq[i - 1])
        # global returns
        seen = {seq[0]}; glob = 0
        for i in range(1, len(seq)):
            if seq[i] != seq[i - 1]:
                if seq[i] in seen: glob += 1
                seen.add(seq[i])
        pv_ch = {}; pv_rev = {}
        for j, v in enumerate(verts):
            used = {seq[0][j]}; c = rv = 0
            for i in range(1, len(seq)):
                if seq[i][j] != seq[i - 1][j]:
                    c += 1
                    if seq[i][j] in used: rv += 1
                    used.add(seq[i][j])
            pv_ch[v] = c; pv_rev[v] = rv
        out[key] = dict(changes=ch, global_returns=glob, max_vertex_changes=max(pv_ch.values(), default=0), max_vertex_revisits=max(pv_rev.values(), default=0),
                        vertices_with_revisit=sum(1 for v in pv_rev if pv_rev[v] > 0), sum_vertex_changes=sum(pv_ch.values()), deg_sum=sum(len(g.succ[v]) - 1 for v in verts))
    return out
if __name__ == "__main__":
    for p in sys.argv[1:]:
        g = pg.read(p); o = analyse(g)
        print(f"{os.path.basename(p)} n={g.n} it={o['iterations']} | σ̄: changes {o['sb']['changes']}, global returns {o['sb']['global_returns']}, max per-vertex changes {o['sb']['max_vertex_changes']}, max per-vertex revisits {o['sb']['max_vertex_revisits']} ({o['sb']['vertices_with_revisit']} vertices), Σ per-vertex changes {o['sb']['sum_vertex_changes']} vs Σ(deg−1) {o['sb']['deg_sum']} | τ̄: changes {o['tb']['changes']}, global returns {o['tb']['global_returns']}, max per-vertex changes {o['tb']['max_vertex_changes']}, max per-vertex revisits {o['tb']['max_vertex_revisits']} ({o['tb']['vertices_with_revisit']} vertices), Σ {o['tb']['sum_vertex_changes']} vs Σ(deg−1) {o['tb']['deg_sum']}")
