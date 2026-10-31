#!/usr/bin/env python3
"""L-NEW box 109: hill-climb on N5 games for frozen-reference W-hierarchy depth h^W >= 3 (box 107 hier.py semantics, n5x default start).
Score = (h^W, transitions paid at level h^W and deeper-1 activity NL2, W-run transitions WT). Mutations: redirect / add / remove one edge,
swap the priorities of two vertices, flip one owner. Accept if score >= current (sideways allowed). Saves the best game to
out/best_<tag>.pg and every game with h >= 3 to out/hit_<tag>_<i>.pg. Usage: climb.py SEED.pg TAG RNGSEED SECONDS"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, Engine, dual
import pg
def cs(E, n, v):
    c, m, l = v
    return (E.rew[c],) + tuple(((1 if E.rankpar[r] == 0 else -1) if (m >> r) & 1 else 0) for r in range(n - 1, -1, -1)) + ((l if E.par[c] == 1 else -l),)
def lcp(a, b):
    i = 0
    while i < len(a) and a[i] == b[i]: i += 1
    return i
def score(g, cap=400):
    n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed); S, TAU, FB = [tuple(s)], [tuple(t)], []
    while len(S) <= cap:
        r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
        if r is None: break
        S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
    Wc = {}; Wm = {}
    def Wv(k, tau):
        if (k, tau) not in Wm:
            if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
            Wm[(k, tau)] = [cs(E, n, x) for x in Wc[tau].evaluate(S[k])[0]]
        return Wm[(k, tau)]
    runs = []
    for k in range(len(S) - 1):
        if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wv(k, TAU[k])] != [x[0] for x in Wv(k + 1, TAU[k])]: continue
        if runs and runs[-1][-1] == k - 1: runs[-1].append(k)
        else: runs.append([k])
    NL = {}
    def block(ks, tau, lev):
        if not ks: return
        ref = Wv(ks[-1] + 1, tau); P = lambda j: sum(lcp(x, ref[v]) for v, x in enumerate(Wv(j, tau)))
        sub, subs = [], []
        for k in ks:
            if P(k + 1) > P(k):
                NL[lev] = NL.get(lev, 0) + 1
                if sub: subs.append(sub); sub = []
            else: sub.append(k)
        if sub: subs.append(sub)
        for sb in subs: block(sb, tau, lev + 1)
    WT = 0
    for run in runs:
        tau = TAU[run[0]]; WT += len(run); block([k for k in run if Wv(k, tau) != Wv(k + 1, tau)], tau, 1)
    h = max(NL) if NL else 0
    return (h, NL.get(h, 0) if h >= 2 else NL.get(2, 0), WT), len(S) - 1
def write(g, path):
    with open(path, "w") as f:
        f.write(f"parity {g.n - 1};\n" + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n)))
def mutate(g, R):
    n = g.n; prio, own, succ = list(g.prio), list(g.owner), [list(x) for x in g.succ]
    m = R.randrange(5); v = R.randrange(n)
    if m == 0 and succ[v]: succ[v][R.randrange(len(succ[v]))] = R.randrange(n)
    elif m == 1: succ[v].append(R.randrange(n))
    elif m == 2 and len(succ[v]) > 1: succ[v].pop(R.randrange(len(succ[v])))
    elif m == 3: w = R.randrange(n); prio[v], prio[w] = prio[w], prio[v]
    else: own[v] = 1 - own[v]
    succ = [sorted(set(x)) for x in succ]
    return pg.Game(prio, own, succ)
seed, tag, rs, secs = sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4])
R = random.Random(rs); g = load(seed); cur, T = score(g); best = cur; t0 = time.time(); it = hits = 0
print("START", tag, cur, T, flush=True)
while time.time() - t0 < secs:
    it += 1; h2 = mutate(g, R)
    try: sc, T = score(h2)
    except Exception as e: continue
    if sc >= cur:
        g, cur = h2, sc
        if sc > best:
            best = sc; write(g, os.path.join(HERE, "out", f"best_{tag}.pg")); print("BEST", tag, it, round(time.time() - t0), sc, T, flush=True)
        if sc[0] >= 3:
            hits += 1; write(g, os.path.join(HERE, "out", f"hit_{tag}_{hits}.pg")); print("HIT", tag, it, sc, T, flush=True)
            if hits >= 3: break
print("END", tag, it, best, flush=True)
