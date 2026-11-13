#!/usr/bin/env python3
"""L-RED-B B6 attempt 2: N5 ITSELF on Gamma3(G) for a genome G (gate numbers normalised to 0..M-1), against the model's key run,
against Zielonka, and on a second N5 engine.

Game: L-NEW's Gamma3 builder (box 189 gamma3.build with eg195.PADS, then eg195.topg: the calls of box 215's keyside215.states), and,
independently, THIS lane's builder (eng.build + eng3.build3, written from R104's / R117's packets, with the HOW3 freezing undone:
K0 -> {K1, pA}, K1 -> {q, s}, K3 -> {K1, K2}, beta -> {Xi-target, pb}); gdiff = 1 if the two games differ (priorities, owners,
successor sets, vertex by vertex). The game is written as PGSolver .pg into PGDIR (sha1 printed).
Engine 1: L-NEW's n5v.step (box 190), mode spec = N5 (SPEC S1-S5), from S3 = n5x.start_pair(g, E, Ed, None), run to N5's STOP.
Engine 2: L-COMP's n5b.py --mode spec (trunk experiments/n5-second, written from the SPEC text only; own S3) on the .pg file.
Per genome, one line:
  n       vertices of Gamma3(G) (= N + 7M + 10)
  T1p     steps of the key run of the model (onep.py)
  F       N5 iterations before its first fallback                              (R117 REACH3: F = L(G))
  mism    1 if N5's mover states s_0..s_F are not the key run's states         (must be 0)
  its, fb N5 iterations to its stop, number of fallbacks (engine 1)
  wrong   #vertices whose winner (engine 1's SPEC S5 output) differs from harness Zielonka   (must be 0)
  badstrat #complaints of the harness strategy verifier (experiments/harness/verify.py check) about engine 1's positional
          strategies at its stop, as TARGET.md par. 5 (D2 change 5) requires                 (must be 0)
  nonmover #transitions before the first fallback at which a non-mover Even vertex or tau changes   (must be 0)
  its2, fb2, wrong2  engine 2's iterations, fallbacks, and #vertices whose winner in its .sol differs from Zielonka (must be 0)
  engdiff 1 if (its, fb) != (its2, fb2)                                          (must be 0)
  gdiff   see above                                                             (must be 0)
Controls: B6N5_CTRL=1 compares N5's states with the HOWARD run of the model (mism must fire);
          B6N5_CTRL=2 flips the Zielonka answer at vertex 0 (wrong and wrong2 must fire); B6N5_CTRL=3 drops the strategy at one vertex of the winner's own region
          (badstrat must fire; note: sending ONE choice to another successor is NOT a reliable control here, since on these games
          most alternatives are winning too: on Gamma3(G_4) only 4 of the 94 single-edge changes are detected);
          B6N5_MODE=xi runs engine 1 as N5'-xi (not N5): engdiff must fire where the two rules differ.
Usage: b6n5.py LNEW TRUNK PGDIR G.json ...   (LNEW, TRUNK: trees holding claude/l-new's and trunk's experiments/)"""
import sys, os, json, time, hashlib, subprocess, re, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
LNEW, TRUNK, PGDIR = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]), sys.argv[3]
sys.path[:0] = [os.path.join(LNEW, p) for p in ("experiments/new/box195", "experiments/new/box189", "experiments/new/box190",
                                               "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
sys.path[:0] = [HERE, os.path.abspath(os.path.join(HERE, "..", "..", ".."))]      # this lane's eng.py / eng3.py
os.environ.setdefault("EG195_ROOT", LNEW)
import gamma3, eg195, n5v, n5x, zielonka, pg, verify
import onep, eng3
MODE = os.environ.get("B6N5_MODE", "spec")
CTRL = os.environ.get("B6N5_CTRL", "0")
N5B = os.path.join(TRUNK, "experiments/n5-second/n5b.py")
os.makedirs(PGDIR, exist_ok=True)


def own_gamma3(G):
    g = eng3.build3(G, frozen=True)
    succ = [list(s) for s in g.succ]
    K0, K1, K2, K3 = g.K
    succ[K0] = [K1, g.pA]
    succ[K1] = [g.q, g.s]
    succ[K3] = [K1, K2]
    for o in g.olist:
        xt = G["opts"][o[0]][o[1]][1]
        succ[g.beta[o]] = [xt, g.pb[o]] if xt >= 0 else [g.pb[o]]
    return list(g.prio), list(g.owner), [sorted(s) for s in succ]


for fn in sys.argv[4:]:
    G = onep.load(fn)
    name = os.path.basename(fn)[:-5]
    t0 = time.time()
    g0, _, _, V = gamma3.build(G, eg195.PADS)
    g = eg195.topg(g0)
    op, oo, osucc = own_gamma3(G)
    gdiff = int(not (op == list(g.prio) and oo == list(g.owner) and osucc == [sorted(s) for s in g.succ]))
    pgf = os.path.join(PGDIR, name + "_g3.pg")
    open(pgf, "w").write(pg.dumps(g))
    sha = hashlib.sha1(open(pgf, "rb").read()).hexdigest()
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g))
    sigma, tau = n5x.start_pair(g, E, Ed, None)
    S = [gamma3.mover_state(G, V, sigma, eg195.PADS)]
    movers = set(range(G["N"]))
    F = None
    fb = its = nonmover = 0
    states = [(tuple(sigma), tuple(tau))]
    while its < 10 ** 7:
        res = n5v.step(g, E, Ed, sigma, tau, MODE)
        if res is None:
            break
        its += 1
        ns, nt = list(res[0]), list(res[1])
        if res[4]:
            fb += 1
            if F is None:
                F = its - 1
        if F is None:
            S.append(gamma3.mover_state(G, V, ns, eg195.PADS))
            if any(ns[v] != sigma[v] for v in range(g.n) if g.owner[v] == 0 and v not in movers) or nt != list(tau):
                nonmover += 1
        sigma, tau = ns, nt
        states.append((tuple(sigma), tuple(tau)))
    if F is None:
        F = its
    t1 = time.time()
    R = onep.OneP(G).run("howard" if CTRL == "1" else "key")
    mism = int([tuple(s) for s in S] != [tuple(s) for s in R])
    win, strat = n5v.solution(g, states, E)
    zwin = list(zielonka.solve(g))
    if CTRL == "2":
        zwin[0] = 1 - zwin[0]
    wrong = sum(1 for v in range(g.n) if win[v] != zwin[v])
    if CTRL == "3":                      # control: drop the strategy at one vertex of the winner's own region
        strat = list(strat)
        strat[next(v for v in range(g.n) if strat[v] is not None)] = None
    badstrat = len(verify.check(g, win, strat))
    with tempfile.TemporaryDirectory() as td:
        sol = os.path.join(td, "out.sol")
        r = subprocess.run([sys.executable, N5B, pgf, sol, "--mode", "spec"], capture_output=True, text=True)
        m = re.search(r"iterations (\d+) fallbacks (\d+)", r.stdout)
        its2, fb2 = (int(m.group(1)), int(m.group(2))) if m else (-1, -1)
        wrong2 = -1
        if m and os.path.exists(sol):
            w2 = {}
            for line in open(sol):
                p = line.strip().rstrip(";").split()
                if len(p) >= 2 and p[0].isdigit():
                    w2[int(p[0])] = int(p[1])
            wrong2 = sum(1 for v in range(g.n) if w2.get(v) != zwin[v])
    t2 = time.time()
    engdiff = int((its, fb) != (its2, fb2))
    print(f"{name} mode {MODE} ctrl {CTRL} N {G['N']} M {sum(len(o) for o in G['opts'])} n {g.n} T1p {len(R) - 1} F {F} mism {mism} its {its} fb {fb} wrong {wrong} "
          f"nonmover {nonmover} badstrat {badstrat} its2 {its2} fb2 {fb2} wrong2 {wrong2} engdiff {engdiff} gdiff {gdiff} pg_sha1 {sha} secs1 {t1 - t0:.1f} secs2 {t2 - t1:.1f}", flush=True)
