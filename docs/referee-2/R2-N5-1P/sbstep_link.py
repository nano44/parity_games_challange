#!/usr/bin/env python3
"""REFEREE-2: replay L-NEW's own switch-best step (experiments/new/tail/phase_trace.sbstep at 26905f0: switch-all SI run to
convergence INSIDE the arena, which is NOT n5.py's arena-optimum computation) and check with sb1p.py's definitions that every
step is a pointwise optimum of the arena (so the data of phase_vc.py / phase_climb.py / lemmaP_check.py are about switch-best as
the packet defines it), then run my Lemma P / Theorem PH checks on that sequence.  Usage: sbstep_link.py game.pg [game.pg.start]"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get("R2_ROOT") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))   # R2_ROOT = a checkout of trunk 26905f0
for p in ("experiments/new/tail", "experiments/new", "experiments/si", "experiments/harness"):
    sys.path.insert(0, os.path.join(ROOT, p))
sys.path.insert(0, HERE)
import pg, sb1p
from n5 import Engine
from phase_trace import sbstep

def main():
    st = sb1p.Stats(); t0 = time.time()
    p = sys.argv[1]; g = pg.read(p)
    s = [g.succ[v][0] if g.owner[v] == 0 else -1 for v in range(g.n)]
    stf = sys.argv[2] if len(sys.argv) > 2 else None
    if stf:
        for tok in open(stf).readline().split()[1:]:
            a, b = map(int, tok.split(":")); s[a] = b
    my = sb1p.Game(g.prio, g.owner, g.succ)
    E = Engine(g)
    rho = [s[v] if g.owner[v] == 0 else g.succ[v][0] for v in range(g.n)]
    seq, kinds = [list(rho)], []
    while True:
        ns, lam, vs = sbstep(g, E, s)
        Om = my.omega(rho)
        if ns is None:
            if my.improving(rho, Om): st.bad("sbstep stops with improving edges left")
            break
        I = my.improving(rho, Om)
        opts = sb1p.arena_opts(my, rho, I)
        bp = my.best_plays(opts)
        if bp is None:
            print("SKIPPED (budget)"); return
        new = [ns[v] if g.owner[v] == 0 else g.succ[v][0] for v in range(g.n)]
        Om2 = my.omega(new)
        st.inc("optimum_checks")
        for v in range(g.n):
            if new[v] not in opts[v]: st.bad(f"sbstep leaves the arena at v={v}")
            if my.key(Om2[v]) != my.key(bp[v]): st.bad(f"sbstep's strategy is not a pointwise arena optimum at v={v}")
        if new == rho:
            st.bad("sbstep returned the same strategy (would loop)"); break
        lamc = any(Om2[v][0] != Om[v][0] for v in range(g.n))
        kinds.append("lambda" if lamc else ("vc" if Om2 != Om else "flat"))
        seq.append(new); rho = new; s = ns
    print(f"{os.path.basename(p)}: n={g.n} m={my.m} sbstep steps={len(kinds)} kinds={''.join(k[0] for k in kinds)}")
    sb1p.check_run(my, seq, kinds, st, lemmaP=("--nolemmaP" not in sys.argv))
    a = 0; ph = []
    for k, kd in enumerate(kinds):
        if kd == "lambda": ph.append((a, k)); a = k + 1
    ph.append((a, len(kinds)))
    print("phases (in-phase steps, value-changing, flat):", [(b - a, kinds[a:b].count("vc"), kinds[a:b].count("flat")) for a, b in ph])
    for k in sorted(st.d): print(f"  {k} = {st.d[k]}")
    for v in st.viol[:20]: print("  VIOLATION:", v)
    print(f"RESULT violations={len(st.viol)} secs={time.time() - t0:.1f}")

main()
