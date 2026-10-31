#!/usr/bin/env python3
"""L-SI box 53: random search for a counterexample to the lemmas of Theorem ROOT-FLIP (same checks as rootflip.py, in-process).
Random games: n vertices, random owners and priorities, out-degree 1..DMAX, random start pair. BIAS=1: vertex 0 Odd with the top,
odd priority (S1's BFS branch, many tied lengths; the box-52 form that built flipev_n20). Saves any violating game to OUT/.
FLIPS / TIES: non-own sbar-flips, and those with the old target's Xi fixed (the descent case).
Usage: rsearch.py SEED COUNT N DMAX BIAS OUT"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import step, start_pair, Engine, dual
import pg
seed, cnt, N, DMAX, BIAS, OUT = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
rng = random.Random(seed)
def check(g, st):
    n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st)
    S = [tuple(s)]; TA = list(t)
    while len(S) < 400:
        r = step(g, E, Ed, list(S[-1]), TA)
        if r is None: break
        S.append(tuple(r[0])); TA = list(r[1])
    EV = [E.evaluate(x) for x in S]; ODD = [o for o in range(n) if own[o] == 1]; SU = [sorted(set(x)) for x in g.succ]
    def path(k, y):
        val, sb = EV[k]; c = val[y][0]; p = [y]; x = y
        while x != c:
            x = S[k][x] if own[x] == 0 else sb[x]; p.append(x)
            if len(p) > n + 1: return None
        return p
    bad = []; cn_ = dict(FLIPS=0, TIES=0)
    for k in range(len(S)):
        val, sb = EV[k]
        for o in ODD:
            if val[o][0] == o: continue
            T = [x for x in SU[o] if E.extend(o, val[x]) == val[o]]
            if sb[o] not in T: bad.append(('NOTT', k, o)); continue
            cn = val[o][0]
            best = min(T) if E.par[cn] == 0 else min(T, key=lambda x: tuple(reversed(path(k, x)[:-1])))
            if best != sb[o]: bad.append(('SELX', k, o))
            for y in SU[o]:
                p = path(k, y)
                if p is None: bad.append(('PATH', k, y)); continue
                if o in p[1:] and not E.key(val[y]) > E.key(val[sb[o]]): bad.append(('NCX', k, o))
    for k in range(len(S) - 1):
        (v0, b0), (v1, b1) = EV[k], EV[k + 1]
        fl = [o for o in ODD if b0[o] != b1[o] and v0[o][0] != o and v1[o][0] != o]
        if not fl: continue
        if not any(v0[b0[o]] != v1[b0[o]] for o in fl): bad.append(('ROOTX2', k, fl[0]))
        for o in fl:
            t1, t2 = b0[o], b1[o]; cn_['FLIPS'] += 1
            if v0[t1] != v1[t1]: continue
            cn_['TIES'] += 1
            if v0[o] != v1[o] or v0[t2] != v1[t2] or v0[t2] != v0[t1]: bad.append(('TIEX', k, o)); continue
            if E.par[v0[o][0]] == 0: bad.append(('EVENX', k, o))
            P = set(path(k, t1) + path(k, t2) + path(k + 1, t1) + path(k + 1, t2))
            if not any(w in P and w != o and v0[w] == v1[w] for w in fl): bad.append(('DESCX', k, o))
    return bad, len(S) - 1, cn_
tot = dict(GAMES=0, ITERS=0, FLIPS=0, TIES=0, BAD=0)
for i in range(cnt):
    n = N; own = [rng.randint(0, 1) for _ in range(n)]; pr = [rng.randint(0, n) for _ in range(n)]
    if BIAS: own[0] = 1; pr[0] = (max(pr) + 1) | 1
    succ = [rng.sample(range(n), rng.randint(1, DMAX)) for _ in range(n)]
    g = pg.Game(pr, own, succ)
    st = ({v: rng.choice(succ[v]) for v in range(n) if own[v] == 0}, {v: rng.choice(succ[v]) for v in range(n) if own[v] == 1})
    bad, it, cn_ = check(g, st); tot['GAMES'] += 1; tot['ITERS'] += it; tot['FLIPS'] += cn_['FLIPS']; tot['TIES'] += cn_['TIES']
    if bad:
        tot['BAD'] += 1; os.makedirs(OUT, exist_ok=True); f = os.path.join(OUT, f"rs_{seed}_{i}")
        with open(f + ".pg", "w") as h:
            h.write(f"parity {n - 1};\n" + "".join(f"{v} {pr[v]} {own[v]} {','.join(map(str, succ[v]))};\n" for v in range(n)))
        with open(f + ".start", "w") as h:
            h.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in st[0].items()) + "\nTAU0 " + " ".join(f"{v}:{w}" for v, w in st[1].items()) + "\n")
        print("BAD", f, bad[:3], flush=True)
print(f"RSEARCH seed {seed} n {N} dmax {DMAX} bias {BIAS} " + " ".join(f"{k} {v}" for k, v in tot.items()))
