#!/usr/bin/env python3
"""L-RED-B packet P-N5-EXP (fixes): N5 ITSELF on Gamma3(G_k), engine 1 only, as a RESUMABLE job (a checkpoint every CK iterations).

The same game, engine, start and counters as b6n5.py (see its header): L-NEW's gamma3.build / eg195.topg game (and this lane's
own builder, gdiff), n5v.step in mode spec from S3 = n5x.start_pair, run to N5's stop; the model's key run (onep.py) is compared
state by state while N5 runs (mism); winners against harness Zielonka at the end (wrong). Engine 2 (n5b.py) is NOT run here: it is
one subprocess with no checkpoint.
A checkpoint (pickle: sigma, tau, its, fb, F, nonmover, mism, seconds, resumes) is written to CKDIR/<name>.ck every CK iterations
(atomic rename) and removed at the end; a restarted job continues from it. The checkpoint holds the sha1 of the .pg file and is
refused if the game differs.
One line per genome: name mode spec ck CK N M n T1p F mism its fb wrong nonmover gdiff pg_sha1 secs resumes
  (T1p, F, mism, its, fb, wrong, nonmover, gdiff as in b6n5.py; mism, wrong, nonmover, gdiff are must-0 counters).
Control B6N5_CTRL=2: the Zielonka answer flipped at vertex 0 (wrong must fire).
Usage: b6n5ck.py LNEW PGDIR CKDIR G.json ...   (LNEW: a tree holding claude/l-new's experiments/, as for b6n5.py)"""
import sys, os, time, hashlib, pickle
HERE = os.path.dirname(os.path.abspath(__file__))
LNEW, PGDIR, CKDIR = os.path.abspath(sys.argv[1]), sys.argv[2], sys.argv[3]
sys.path[:0] = [os.path.join(LNEW, p) for p in ("experiments/new/box195", "experiments/new/box189", "experiments/new/box190",
                                               "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
sys.path[:0] = [HERE]
os.environ.setdefault("EG195_ROOT", LNEW)
import gamma3, eg195, n5v, n5x, zielonka, pg
import onep, eng3
CK = int(os.environ.get("B6N5_CK", "100"))
CTRL = os.environ.get("B6N5_CTRL", "0")
os.makedirs(PGDIR, exist_ok=True)
os.makedirs(CKDIR, exist_ok=True)


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
    g0, _, _, V = gamma3.build(G, eg195.PADS)
    g = eg195.topg(g0)
    op, oo, osucc = own_gamma3(G)
    gdiff = int(not (op == list(g.prio) and oo == list(g.owner) and osucc == [sorted(s) for s in g.succ]))
    pgf = os.path.join(PGDIR, name + "_g3.pg")
    open(pgf, "w").write(pg.dumps(g))
    sha = hashlib.sha1(open(pgf, "rb").read()).hexdigest()
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g))
    R = [tuple(s) for s in onep.OneP(G).run("key")]
    movers = set(range(G["N"]))
    ckf = os.path.join(CKDIR, name + ".ck")
    st = None
    if os.path.exists(ckf):
        st = pickle.load(open(ckf, "rb"))
        if st.get("sha") != sha:
            print(f"{name} checkpoint refused (game sha1 differs)", file=sys.stderr)
            st = None
        else:
            st["resumes"] += 1
    if st is None:
        sigma, tau = n5x.start_pair(g, E, Ed, None)
        st = dict(sha=sha, sigma=list(sigma), tau=list(tau), its=0, fb=0, F=None, nonmover=0,
                  mism=int(tuple(gamma3.mover_state(G, V, sigma, eg195.PADS)) != R[0]), secs=0.0, resumes=0)
    t0 = time.time()

    def save():
        st["secs"] += time.time() - save.t
        save.t = time.time()
        tmp = ckf + ".tmp"
        pickle.dump(st, open(tmp, "wb"))
        os.replace(tmp, ckf)
    save.t = t0

    while st["its"] < 10 ** 7:
        sigma, tau = st["sigma"], st["tau"]
        res = n5v.step(g, E, Ed, sigma, tau, "spec")
        if res is None:
            break
        st["its"] += 1
        ns, nt = list(res[0]), list(res[1])
        if res[4]:
            st["fb"] += 1
            if st["F"] is None:
                st["F"] = st["its"] - 1
        if st["F"] is None:
            i = st["its"]
            if i >= len(R) or tuple(gamma3.mover_state(G, V, ns, eg195.PADS)) != R[i]:
                st["mism"] = 1
            if any(ns[v] != sigma[v] for v in range(g.n) if g.owner[v] == 0 and v not in movers) or nt != list(tau):
                st["nonmover"] += 1
        st["sigma"], st["tau"] = ns, nt
        if st["its"] % CK == 0:
            save()
    F = st["F"] if st["F"] is not None else st["its"]
    mism = int(st["mism"] or F != len(R) - 1)
    win, _ = n5v.solution(g, [(tuple(st["sigma"]), tuple(st["tau"]))], E)
    zwin = list(zielonka.solve(g))
    if CTRL == "2":
        zwin[0] = 1 - zwin[0]
    wrong = sum(1 for v in range(g.n) if win[v] != zwin[v])
    secs = st["secs"] + time.time() - save.t
    print(f"{name} mode spec ctrl {CTRL} ck {CK} N {G['N']} M {sum(len(o) for o in G['opts'])} n {g.n} T1p {len(R) - 1} F {F} mism {mism} "
          f"its {st['its']} fb {st['fb']} wrong {wrong} nonmover {st['nonmover']} gdiff {gdiff} pg_sha1 {sha} secs {secs:.1f} "
          f"resumes {st['resumes']}", flush=True)
    if os.path.exists(ckf):
        os.remove(ckf)
