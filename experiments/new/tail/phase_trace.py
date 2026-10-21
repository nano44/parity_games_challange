#!/usr/bin/env python3
"""Box 10 (ii): per-PHASE trace of switch-best (= N5's Even step on a one-player game, Odd out-degree 1; step = optimum of the arena
{rho(v)} + improving edges, computed as sb_phaselen.py does). A phase = maximal run of steps with every vertex's cycle node unchanged.
Per phase: length, switching vertices with their switch counts (leapfrogs = a vertex switching twice in one phase), and the lambda changes
that end it (the cycle that closed: vertices whose cycle node changed and the new cycle node). Usage: phase_trace.py game.pg [game.pg.start]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg
from n5 import Engine
EXACT = os.environ.get("EXACT") == "1"   # EXACT=1: the arena optimum by N5's own step (n5_lock.step = n5.py's loop: VJ00 shortest-paths
                                          # procedure on the dual of the arena, exact); default: switch-all SI on the arena to a fixpoint
def sbstep(g, E, s):
    vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs); lam = tuple(vs[v][0] for v in range(g.n))
    if not Is: return None, lam, vs
    if EXACT:
        from n5_lock import step
        from n5 import Engine as _E, dual as _d
        r = step(g, E, _E(_d(g)), list(s), [g.succ[v][0] if g.owner[v] == 1 else -1 for v in range(g.n)])
        return (list(r[0]) if r is not None else None), lam, vs
    A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n) if g.owner[v] == 0}
    h = pg.Game(list(g.prio), list(g.owner), [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(g.n)])
    Eh = Engine(h); x, _ = Eh.run(Eh.rule_switch_all, tuple(s)); return list(x), lam, vs
if __name__ == '__main__':
    p = sys.argv[1]; g = pg.read(p); s = [g.succ[v][0] if g.owner[v] == 0 else -1 for v in range(g.n)]
    st = sys.argv[2] if len(sys.argv) > 2 else (p + ".start" if os.path.exists(p + ".start") else None)
    if st:
        for tok in open(st).readline().split()[1:]: a, b = map(int, tok.split(":")); s[a] = b
    E = Engine(g); k = 0; phase = []; phases = []
    while True:
        ns, lam, vs = sbstep(g, E, s)
        if ns is None: break
        sw = [(v, s[v], ns[v]) for v in range(g.n) if g.owner[v] == 0 and ns[v] != s[v]]
        _, lam2, _ = sbstep(g, E, ns) if True else (None, None, None)
        phase.append((k, sw, lam))
        if lam2 != lam:
            chg = [(v, lam[v], lam2[v]) for v in range(g.n) if lam[v] != lam2[v]]
            phases.append((phase, chg)); phase = []
        s = ns; k += 1
    if phase: phases.append((phase, []))
    print(f"{os.path.basename(p)} n={g.n} steps={k} phases={len(phases)} max phase {max(len(ph) for ph, _ in phases)}")
    for ph, chg in phases:
        if len(ph) < 3: continue
        cnt = {}
        for _, sw, _ in ph:
            for v, a, b in sw: cnt[v] = cnt.get(v, 0) + 1
        print(f"  phase steps {ph[0][0]}..{ph[-1][0]} len {len(ph)}: switches per vertex {dict(sorted(cnt.items()))}; ends with lambda change at {len(chg)} vertices -> new cycle nodes {sorted(set(c for _, _, c in chg))}")
        for kk, sw, lam in ph: print("     ", kk, sw)
