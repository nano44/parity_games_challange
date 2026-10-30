#!/usr/bin/env python3
"""L-NEW box 84: whole-run checks of Lemma E0-BOUND and Corollary CHARGE (docs/new/N5-WAIT-box84.md §2-§3) on random N5 runs.
An ALTERNATION at (X, g) := a block at t1 (waits.py classes) followed by the first later state t2 with sigma_t2(X) = g and
sigma_(t2-1)(X) != g. Checks: (E0-BOUND) alternations whose block is E0 number <= n - 1 per (X, g); (RISE) Xi(g) rises strictly in
[t1, t2 - 1] (R89 LATE-RISE); (CHARGE) for a REG block, some Even vertex of pi switches in [t1, t2 - 1]. DEPTH = longest chain of REG alternations,
each charged (min over its charges) to a switch that is itself a REG alternation. FAN = the most REG alternations sharing one charged
switch event; FAN1 = the same counting only alternations with exactly one charged switch (forced sharing). Usage: altcheck.py N TRIALS SEED"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import step, start_pair, Engine, dual
import pg
N, trials, seed = map(int, sys.argv[1:4]); rnd = random.Random(seed)
c = dict(alt_reg=0, alt_e0=0, e0_max=0, rise_viol=0, charge_viol=0, runs=0, depth_max=0, fan_max=0, fan1_max=0); arg = None; argf = None
for _ in range(trials):
    owner = [rnd.randint(0, 1) for _ in range(N)]; prio = rnd.sample(range(N), N)
    succ = [sorted(rnd.sample(range(N), rnd.randint(1, 3))) for _ in range(N)]
    g = pg.Game(prio, owner, succ); E, Ed = Engine(g), Engine(dual(g))
    st = ({v: rnd.choice(succ[v]) for v in range(N) if owner[v] == 0}, {v: rnd.choice(succ[v]) for v in range(N) if owner[v] == 1})
    s, t = start_pair(g, E, Ed, st); S = [tuple(s)]; TAU = [tuple(t)]
    for _ in range(20 * N * N):
        r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
        if r is None: break
        S.append(tuple(r[0])); TAU.append(tuple(r[1]))
    T = len(S) - 1; c['runs'] += 1; VS = [E.evaluate(x) for x in S]; key = E.key
    first = {}                                     # (X, g) -> list of (t1, cls, path) of blocks
    for k in range(T + 1):
        sig = S[k]; vs, sbar = VS[k]; Is = set(E.improving(sig, vs)); nxt = lambda v: sig[v] if owner[v] == 0 else sbar[v]
        for X in range(N):
            if owner[X]: continue
            for gg in succ[X]:
                if gg == sig[X] or (X, gg) in Is: continue
                path, y, ok = [], gg, False
                while y not in path:
                    if y == X: ok = True; break
                    path.append(y); y = nxt(y)
                if not ok: continue
                cyc, y = [X], sig[X]
                while y != X and y not in cyc and len(cyc) <= N: cyc.append(y); y = nxt(y)
                if y == X and any(v in cyc for v in path): continue
                e0 = vs[X][0] == X and all(E.rank[v] < E.rank[X] for v in path)
                first.setdefault((X, gg), []).append((k, 'E0' if e0 else 'REG', path))
    altev = {}                                     # (X, t2) -> list of charged switch events (y, s + 1)
    for (X, gg), bl in first.items():
        takes = [k for k in range(1, T + 1) if S[k][X] == gg and S[k - 1][X] != gg]
        e0n = 0; done = set()
        for t2 in takes:
            prior = [b for b in bl if b[0] < t2 and not any(b[0] < tk < t2 for tk in takes)]
            if not prior: continue
            t1, cls, path = prior[0]
            if (t1, t2) in done: continue
            done.add((t1, t2))
            if cls == 'E0': c['alt_e0'] += 1; e0n += 1
            else:
                c['alt_reg'] += 1
                if not any(S[k][v] != S[t1][v] for v in path if owner[v] == 0 for k in range(t1, t2 + 1)): c['charge_viol'] += 1
                altev[(X, t2)] = [(v, k + 1) for v in path if owner[v] == 0 for k in range(t1, t2) if S[k + 1][v] != S[k][v]]
            if not key(VS[t2 - 1][0][gg]) > key(VS[t1][0][gg]): c['rise_viol'] += 1
        c['e0_max'] = max(c['e0_max'], e0n)
    memo = {}
    def depth(ev):
        if ev not in altev: return 0
        if ev not in memo: memo[ev] = 1 + min(depth(x) for x in altev[ev])
        return memo[ev]
    dm = max([0] + [depth(e) for e in altev])
    fan = {}; fan1 = {}
    for e, ch in altev.items():
        for x in ch: fan[x] = fan.get(x, 0) + 1
        if len(ch) == 1: fan1[ch[0]] = fan1.get(ch[0], 0) + 1
    fm = max([0] + list(fan.values())); f1 = max([0] + list(fan1.values()))
    c['fan_max'] = max(c['fan_max'], fm)
    if f1 > c['fan1_max']: c['fan1_max'] = f1; argf = (prio, owner, succ, st)
    if dm > c['depth_max']: c['depth_max'] = dm; arg = (prio, owner, succ, st)
print("ARGMAX-depth", arg); print("ARGMAX-fan1", argf)
print(f"ALTCHECK n {N} trials {trials} seed {seed} {c}")
