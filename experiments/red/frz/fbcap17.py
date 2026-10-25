#!/usr/bin/env python3
"""Box 41: CONJECTURE FB-CAP search (in-phase Even S4c fallbacks per phase ≤ max(1, |U| − 2)), fast: own copy of ex16.trace that also
records λ_Ξ at every state. Phase = maximal run with λ_Ξ and τ constant; g = Even fallbacks with both ends in the phase; U = λ^{-1}(λ(o)).
Modes:
  exh N [ex16 options]          every game of ex16's space for n = N, every start pair (exhaustive)
  rand N SECS SEED              random 𝒞^1O games with n = N (owners, priorities 0..2N−1, successor sets uniform), every start pair
Output: per |U| the max of g − max(1, |U| − 2); violations (> 0) saved to OUT_viol*.json. Usage: fbcap17.py MODE ... --out PREFIX [--jobs 4]"""
import sys, os, itertools, json, time, random, argparse, multiprocessing as mp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import ex16, sox, pg, n5
from si import Engine

def trace(g, start, cap=500):
    n = g.n; E, Ed = Engine(g), Engine(n5.dual(g))
    sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    for v in range(n):
        if g.owner[v] == 0: sigma[v] = start[v]
        else: tau[v] = start[v]
    LAM, TAU, EFB, SIG = [], [], [], []
    while True:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        LAM.append(tuple(x[0] for x in vs)); TAU.append(tuple(tau)); SIG.append(tuple(sigma))
        if len(EFB) >= cap: break
        vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        if not Is and not It: break
        ns, nt = list(sigma), list(tau)
        if Is:
            opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
            for v, w in Is: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
            _, best = Engine(n5.dual(pg.Game(list(g.prio), list(g.owner), succ))).evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 0: ns[v] = best[v]
        if It:
            opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
            for v, w in It: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
            _, best = Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 1: nt[v] = best[v]
        fb = ns == sigma and nt == tau; efb = False
        if fb:
            if Is:
                efb = True
                for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
            else:
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        EFB.append(efb); sigma, tau = ns, nt
    return LAM, TAU, EFB, SIG

def measure(g, o, start, best, xb=None):
    """FB-CAP per phase; also FB-PHASE (docs/si/N5-FBPHASE-box14.md §4, sha1 f7aaa624) and Corollary FX (§5): X = in-phase transitions with
    R̄ changing, X_SN = S4a ones among them from states with c_w = c_θ; FX: X ≤ n(f + X_SN) + n − 1. xb collects maxima and failures."""
    LAM, TAU, EFB, SIG = trace(g, start); N = len(LAM); a = 0; worst = None; n = g.n
    rank = {v: i for i, v in enumerate(sorted(range(n), key=lambda v: (g.prio[v], v)))}
    def nxt(k, v): return SIG[k][v] if g.owner[v] == 0 else TAU[k][v]
    def Rset(k):
        R = set()
        for v in range(n):
            x, seen = v, set()
            while x not in seen and x != o: seen.add(x); x = nxt(k, x)
            if x == o: R.add(v)
        return frozenset(R)
    def cw(k):
        x, path = o, []
        while x not in path: path.append(x); x = nxt(k, x)
        cyc = path[path.index(x):]; return max(cyc, key=lambda v: rank[v])
    do = len(set(g.succ[o]))
    while a < N:
        b = a
        while b + 1 < N and LAM[b + 1] == LAM[a] and TAU[b + 1] == TAU[a]: b += 1
        c = LAM[a][o]; u = sum(1 for z in LAM[a] if z == c); gg = sum(EFB[k] for k in range(a, b))
        e = gg - max(1, u - 2)
        if e > best.get(u, -99): best[u] = e
        if e > 0: worst = (u, gg, a)
        if xb is not None:
            sizes = {}
            for z in LAM[a]: sizes[z] = sizes.get(z, 0) + 1
            N0 = max([0, u - 2] + [sz - 1 for cc, sz in sizes.items() if cc != c])
            bound = N0 + (do + n - 2) + (do + n - 1) * (u - 1) + 1
            xb["max_FBPHASE_slack"] = max(xb.get("max_FBPHASE_slack", -10 ** 9), gg - bound)
            if gg > bound: xb["FAIL_FBPHASE"] = xb.get("FAIL_FBPHASE", 0) + 1
            if b > a:
                Rs = [Rset(k) for k in range(a, b + 1)]
                X = sum(1 for k in range(a, b) if Rs[k - a] != Rs[k + 1 - a])
                XSN = sum(1 for k in range(a, b) if not EFB[k] and Rs[k - a] != Rs[k + 1 - a] and cw(k) == c)
                xb["max_X"] = max(xb.get("max_X", 0), X)
                xb["max_FX_slack"] = max(xb.get("max_FX_slack", -10 ** 9), X - (n * (gg + XSN) + n - 1))
                if X > n * (gg + XSN) + n - 1: xb["FAIL_FX"] = xb.get("FAIL_FX", 0) + 1
        a = b + 1
    return worst

def task(args):
    mode, a, part = args; best = {}; runs = 0; viol = []; xb = {}
    games = []
    if mode == "exh":
        n, o, par = part; games = ex16.games(n, o, par, a)
    else:
        n, seed, cnt = part; rng = random.Random(seed)
        def gen():
            made = 0
            while made < cnt:
                prio = [rng.randrange(2 * n) for _ in range(n)]; owner = [rng.randrange(2) for _ in range(n)]
                succ = [sorted(set(rng.sample(range(n), 1 if owner[v] else rng.randint(1, n)))) for v in range(n)]
                o = rng.randrange(n); owner[o] = 1; succ[o] = sorted(set(rng.sample(range(n), rng.randint(2, n))))
                try: g = pg.Game(prio, owner, succ)
                except Exception: continue
                if len(sox.oddchoice(g)) != 1: continue
                made += 1; yield g
        games = gen()
    for g in games:
        o = sox.oddchoice(g)[0]
        for st in itertools.product(*[g.succ[v] for v in range(g.n)]):
            runs += 1
            try: w = measure(g, o, st, best, xb)
            except Exception: continue
            if w and len(viol) < 5: viol.append(dict(prio=g.prio, owner=g.owner, succ=g.succ, start=list(st), u=w[0], g=w[1], phase=w[2]))
    return runs, best, viol, xb

if __name__ == "__main__":
    mode = sys.argv[1]; ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int); ap.add_argument("--even-maxdeg", type=int); ap.add_argument("--o-deg", type=int)
    ap.add_argument("--no-forced", action="store_true"); ap.add_argument("--jobs", type=int, default=4); ap.add_argument("--out", required=True)
    ap.add_argument("--secs", type=float, default=0); ap.add_argument("--seed", type=int, default=1); ap.add_argument("--batch", type=int, default=200)
    a = ap.parse_args(sys.argv[2:]); a.all_starts = True; t0 = time.time(); tot = 0; B = {}; V = []; XB = {}
    if mode == "exh": jobs = [("exh", a, (a.n, o, par)) for o in range(a.n) for par in itertools.product((0, 1), repeat=a.n)]
    else: jobs = (("rand", a, (a.n, a.seed * 100000 + i, a.batch)) for i in itertools.count())
    with mp.Pool(a.jobs) as P:
        for runs, best, viol, xb in P.imap_unordered(task, jobs):
            tot += runs
            for k, v in xb.items(): XB[k] = XB.get(k, 0) + v if k.startswith("FAIL") else max(XB.get(k, -10 ** 9), v)
            for u, e in best.items(): B[u] = max(B.get(u, -99), e)
            for v in viol:
                if len(V) < 20: V.append(v); json.dump(v, open(f"{a.out}_viol{len(V)}.json", "w")); print("VIOL", v, flush=True)
            print(json.dumps(dict(runs=tot, best=dict(sorted(B.items())), viol=len(V), xb=XB, secs=round(time.time() - t0))), flush=True)
            if mode == "rand" and time.time() - t0 > a.secs: P.terminate(); break
    print("DONE", tot, dict(sorted(B.items())), len(V), XB, flush=True)
