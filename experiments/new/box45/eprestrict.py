#!/usr/bin/env python3
"""Box 45 (L-NEW successor 24) DATA for Lemma RESTRICT_E / Corollaries EP-0, EP-1 (docs/new/N5-EPR-box45.md).
For every epoch E of every phase of an N5 run on G (phase: (lambda_Xi, tau) constant; epoch: sigma-bar|Q constant), with
D := {q in Q : sigma-bar_E(q) != tau(q)}, build G'_E := G with every Odd v not in D restricted to tau(v) and every u in D to
{tau(u), sigma-bar_E(u)}. Checks:
  XI_V   Xi computed on G'_E (S1 on G'_E) != Xi on G, at some state of E                         (RESTRICT_E (i))
  OPT_V  at an in-phase transition of E, tau is NOT value-optimal in S4b's arena H' on G'_E          (RESTRICT_E (iii))
  (I_sigma, the S4a output and the S4c output (RESTRICT_E (ii)) are covered by REP_V: sigma and the fallback flag are compared at every transition.)
  REP_V  N5^tau on G'_E from E's first state does not reproduce E's sigma sequence                  (Corollary REPRO)
  EP0_V  an epoch with D empty has >= n + m transitions with both ends in it                        (Corollary EP-0, via R17 (c))
Context: DIV = epochs in which SPEC's own S4b on G'_E would move tau (a value tie) before E ends (so N5^tau, not SPEC N5, is the
simulator); epochs and max length (transitions inside E) by |D|; for |D| = 1 the length of the whole N5^tau phase on G'_E (G1PH).
Usage: eprestrict.py STARTS SEED (--list FILE | --rand C LO HI GSEED | files)   STARTS = 0: S3 start only; K > 0: S3 + K random."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from multi import rand_ckO
from n5x import load, step, start_pair, Engine, dual, pg
C = dict(runs=0, phases=0, epochs=0, XI_V=0, OPT_V=0, REP_V=0, EP0_V=0, DIV=0, G1PH=0, G1PH_n=0)
BYD = {}
MUT = os.environ.get("EPR_MUT") == "1"     # mutation control: drop sigma-bar_E(u) at u in D (XI_V and REP_V must bite when D != {})

def restrict(g, D, tau, sbE):
    succ = []
    for v in range(g.n):
        if g.owner[v] == 1: succ.append(([tau[v]] if MUT else sorted({tau[v], sbE[v]})) if v in D else [tau[v]])
        else: succ.append(list(g.succ[v]))
    return pg.Game(list(g.prio), list(g.owner), succ)

def step_tau(g, E, Ed, sigma, tau, spec=False):
    """N5^tau: SPEC step, except that S4b keeps tau whenever tau is value-optimal in its arena H'. Returns (ns, nt, fb, moved)."""
    n = g.n
    vs, _ = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
    vt, _ = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
    if not Is and not It: return None
    ns, nt = list(sigma), list(tau); moved = False
    if Is:
        opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
        for v, w in Is: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
        Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
        _, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 0: ns[v] = best[v]
    if It:
        opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
        for v, w in It: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
        Hp = pg.Game(list(g.prio), list(g.owner), succ); Er = Engine(Hp)
        vopt, best = Er.evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
        cand = [best[v] if g.owner[v] == 1 else tau[v] for v in range(n)]
        if cand != list(tau):
            fixed = [[tau[v]] if g.owner[v] == 1 else succ[v] for v in range(n)]
            vtau, _ = Engine(pg.Game(list(g.prio), list(g.owner), fixed)).evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
            if spec or [x for x in vtau] != [x for x in vopt]: nt = cand; moved = True
            else: moved = "tie"
    fb = 0
    if ns == list(sigma) and nt == list(tau):
        fb = 1
        if Is:
            for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
        else:
            for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
    return ns, nt, fb, moved

def check(g, start, cap=4000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    m = sum(len(x) for x in g.succ)
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append(dict(s=tuple(s), t=tuple(t), lam=tuple(x[0] for x in vs), vs=vs, sb=tuple(sb), q=tuple(sb[q] for q in Q),
                         fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    C["runs"] += 1
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        C["phases"] += 1; k = i
        while k <= j:
            e = k
            while e + 1 <= j and rows[e + 1]["q"] == rows[k]["q"]: e += 1
            epoch(g, rows, k, e, j, Q, m); k = e + 1
        i = j + 1

def epoch(g, rows, x, y, b, Q, m):
    C["epochs"] += 1; tau = rows[x]["t"]; sbE = rows[x]["sb"]
    D = {q for q in Q if sbE[q] != tau[q]}
    L = y - x                                      # transitions with both ends in E
    d = BYD.setdefault(len(D), [0, 0]); d[0] += 1; d[1] = max(d[1], L)
    gp = restrict(g, D, tau, sbE); Ep, Edp = Engine(gp), Engine(dual(gp))
    bad_xi = False
    for k in range(x, y + 1):
        vs_p, _ = Ep.evaluate(rows[k]["s"])
        if list(vs_p) != list(rows[k]["vs"]): bad_xi = True
    C["XI_V"] += bad_xi
    # N5^tau on G'_E from E's first state; compare sigma sequence through the transition leaving E (if it stays in the phase)
    s, t = list(rows[x]["s"]), list(tau); div = False; rep_bad = False; opt_bad = False
    last = y + 1 if y < b else y
    for k in range(x, last):
        r = step_tau(gp, Ep, Edp, s, t)
        rs = step_tau(gp, Ep, Edp, s, t, spec=True)
        if r is None: rep_bad = True; break
        if rs is None or rs[1] != list(t): div = True
        if r[3] is True: opt_bad = True
        if tuple(r[0]) != rows[k + 1]["s"] or tuple(r[1]) != tau or r[2] != rows[k]["fb"]: rep_bad = True; break
        s, t = r[0], r[1]
    C["OPT_V"] += opt_bad; C["REP_V"] += rep_bad; C["DIV"] += div
    if not D and L >= g.n + m: C["EP0_V"] += 1
    if len(D) == 1 and not rep_bad:          # whole N5^tau phase on G'_E from E's first state
        s, t = list(rows[x]["s"]), list(tau); lam0 = rows[x]["lam"]; ln = 0
        while ln < 20000:
            r = step_tau(gp, Ep, Edp, s, t)
            if r is None or r[1] != list(t): break
            vs, _ = Ep.evaluate(tuple(r[0]))
            if tuple(v[0] for v in vs) != lam0: ln += 1; break
            s = r[0]; ln += 1
        if ln > C["G1PH"]: C["G1PH"], C["G1PH_n"] = ln, g.n

if __name__ == "__main__":
    a = sys.argv[1:]; K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [load(os.path.join(R0, l.split()[0])) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [g for g in (rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    else: gs = [load(f) for f in a]
    for g in gs:
        if g.n > 64: continue
        starts = [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                            {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]
        for st in starts:
            try: check(g, st)
            except RecursionError: pass
    print(", ".join(f"{k} {v}" for k, v in C.items()), "| by |D|: (epochs, max transitions inside) " +
          " ".join(f"{k}:{v}" for k, v in sorted(BYD.items())))
