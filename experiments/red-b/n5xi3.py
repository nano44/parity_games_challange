#!/usr/bin/env python3
"""N5XI-G3 identity test (L-RED-B, B2 / box 209): on Gamma3(G) (eng3.build3, FULL edge set, no freezing) run N5'-xi (R118's
[N5XI] = SPEC S1-S5 «with ONE change in S4a», box 190's tie rule) and N5 (SPEC) from S3 with L-NEW's engine box190/n5v.py
(claude/l-new 311bbf81, read by `git archive` into a directory given as argument 1, not copied, not edited), and compare:
  - iterations(N5'-xi) with T3 + 3, T3 from MY HOW3 run (eng3.how3_run, tie rules keep-low and high);
  - REACH3-ALL replayed with MY values: at every state j of the N5'-xi run before its first fallback, the non-mover Even vertices
    and Odd's tau are at the standard state (P-N5-REACH par. 3), and the mover step j -> j+1 is a HOW3 step under eng3's values
    (every mover to a best successor, a best current one kept); the first fallback is at iteration T3' + 1 where T3' = the
    number of HOW3 steps of that run; iterations = T3' + 3.
Usage: n5xi3.py ARCHROOT FILE...   or   n5xi3.py ARCHROOT --rand SEED COUNT NMAX MMAX
Prints one line per genome and a summary; counters must be 0: idfail (iterations != T3' + 3), reachfail (a replay clause fails),
t3diff (T3' differs from my keep-low AND my high T3: DATA, a tie-rule difference, not a failure by itself)."""
import sys, os, random, json
import eng, eng3, gen, lev3
root = os.path.abspath(sys.argv[1])
sys.path[:0] = [os.path.join(root, "experiments/new/box190")]
import n5v, pg

def full_game(g):
    c = {k: 0 for k in lev3.CNT}; lev3.structure(g, c)
    return pg.Game(list(g.prio), list(g.owner), [sorted(s) for s in g.full])

def one(G, tag):
    g = eng3.build3(G); pgG = full_game(g)
    states, fbs, E = n5v.run(pgG, "xi")
    its = len(states) - 1
    # replay with my values
    std = {}
    for o in g.olist:
        b = g.beta[o]; std[b] = g.succ[b][0]
    K0, K1, K2, K3 = g.K
    std[K0] = g.pA; std[K1] = g.s; std[K3] = K2
    tstd = {gv: g.succ[gv][0] for gv in g.gates}; tstd[K2] = K2
    reachfail = 0; T3p = None
    sigs = []
    for j, (s, t) in enumerate(states):
        ok = all(s[v] == w for v, w in std.items()) and all(t[v] == w for v, w in tstd.items())
        sig = [g.succ[x].index(s[x]) if s[x] in g.succ[x] else -1 for x in range(g.N)]
        if not ok or -1 in sig:
            T3p = j - 1; break
        sigs.append(sig)
    if T3p is None: T3p = len(states) - 1
    # mover steps 0..T3p-1 must be HOW3 steps; at T3p no mover has a strictly better successor
    for j in range(len(sigs)):
        sbar, val, lam, pim, kk, nx = eng3.best_reply3(g, sigs[j])
        best_exists = False
        for x in range(g.N):
            vals = [val[w] for w in g.succ[x]]; bv = max(vals)
            if vals[sigs[j][x]] != bv: best_exists = True
            if j + 1 < len(sigs):
                if vals[sigs[j + 1][x]] != bv: reachfail += 1
                if vals[sigs[j][x]] == bv and sigs[j + 1][x] != sigs[j][x]: reachfail += 1
        if j < len(sigs) - 1 and not best_exists: reachfail += 1
        if j == len(sigs) - 1 and best_exists: T3last = j
    T3p = len(sigs) - 1
    # last standard state must be the HOW3 end (no mover with a strictly better successor)
    sbar, val, *_ = eng3.best_reply3(g, sigs[-1])
    if any(max(val[w] for w in g.succ[x]) != val[g.succ[x][sigs[-1][x]]] for x in range(g.N)): reachfail += 1
    T_lo = len(eng3.how3_run(g, "keep-low")) - 1; T_hi = len(eng3.how3_run(g, "high")) - 1
    idfail = int(its != T3p + 3)
    st5, fb5, _ = n5v.run(pgG, "spec")
    print("N5XI3 %s N %d M %d n3 %d its_xi %d fb_xi %d T3' %d T3_lo %d T3_hi %d its_spec %d fb_spec %d idfail %d reachfail %d" % (
        tag, g.N, g.M, g.n, its, fbs, T3p, T_lo, T_hi, len(st5) - 1, fb5, idfail, reachfail), flush=True)
    return idfail, reachfail, int(T3p not in (T_lo, T_hi))

tot = [0, 0, 0]; cnt = 0
if sys.argv[2] == "--rand":
    seed, count, Nmax, Mmax = map(int, sys.argv[3:7]); rng = random.Random(seed)
    while cnt < count:
        G = gen.shaped(rng, rng.randint(1, Nmax), "mix"); G.pop("eorder", None)
        if sum(len(o) for o in G["opts"]) > Mmax: continue
        r = one(G, "rand%d_%d" % (seed, cnt)); cnt += 1
        for i in range(3): tot[i] += r[i]
else:
    for p in sys.argv[2:]:
        r = one(eng.load(p), os.path.basename(p)); cnt += 1
        for i in range(3): tot[i] += r[i]
print("N5XI3 SUMMARY genomes %d idfail %d reachfail %d t3diff %d" % (cnt, tot[0], tot[1], tot[2]))
