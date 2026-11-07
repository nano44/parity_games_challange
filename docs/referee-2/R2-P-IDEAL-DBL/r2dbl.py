#!/usr/bin/env python3
"""REFEREE-2 succ. 30: own replay for P-IDEAL-DBL on my R104 IDEAL simulator (R2-P-IDEAL-MOVES/r2moves.py class G; no lane code).
Per genome and start: T, F(l) per level (flips of the key order of the pair (2l, 2l+1), R113), doubling levels (F(l) = 2F(l-1) + 2),
and for every level l >= 1: ALIGN (KP = c_l, movers go to c_l(s_t), key order rule; sanity), WINDOW-ONCE, DBL-EQ (a) both directions
(the five conditions), (b) each member moves exactly once per l-window and F(l-1)+1 times, (c) γ_l(0) = γ_l(1) and first mover = 2l
iff γ false; PASS-FREEZE where the pair l+1 never moves and starts split; HIT (cv(y) rises iff a mover of y's old chain moves) for every
mover and step; ALT-MIN (a)-(d); TOWER-NEED (moves = f+1, P(x) >= f+2, f >= 2 => both targets movers with R >= (f-1)/2).
Usage: r2dbl.py [--allstarts] FILE.json ... | r2dbl.py dead ROOT_SI"""
import sys, os, json, itertools
H = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(H, '..', 'R2-P-IDEAL-MOVES', 'r2moves.py')).read().split("\nif __name__")[0]
ns = {'__name__': 'lib'}; a = sys.argv; sys.argv = ['x']; exec(src, ns); sys.argv = a
G, X = ns['G'], ns['X']
def P(g, x, memo):
    if x in memo: return memo[x]
    r = sum(1 if o[1] == X else P(g, o[1], memo) for o in g.O[x]); memo[x] = r; return r
def cv(g, s, x): return g.val(s, x, s[x])
def analyse(g, s0):
    S = g.run(list(s0)); T = len(S) - 1; N = g.N; d = N // 2; V = {k: 0 for k in 'ALIGN WO DBLa DBLb DBLc PF HIT ALTa ALTb ALTc ALTd TN'.split()}
    ck = [[g.key(s, x, s[x]) for x in range(N)] for s in S]
    order = [[ck[t][2 * j] < ck[t][2 * j + 1] for j in range(d)] for t in range(T + 1)]
    F = [sum(order[t][j] != order[t - 1][j] for t in range(1, T + 1)) for j in range(d)]
    Mv = [None] + [{x for x in range(N) if S[t][x] != S[t - 1][x]} for t in range(1, T + 1)]
    mv = [sum(x in Mv[t] for t in range(1, T + 1)) for x in range(N)]
    dbl = [l for l in range(1, d) if F[l] == 2 * F[l - 1] + 2]
    gate = lambda x, k: g.O[x][k][2]
    for l in range(1, d):
        p, q = 2 * l, 2 * l + 1
        c = [0 if order[t][l - 1] else 1 for t in range(T + 1)]            # c_l(s_t): k with mover 2(l-1)+k of smaller key
        gam = [gate(p, j) < gate(q, j) for j in range(2)]
        for t in range(T + 1):
            kp = [min(range(2), key=lambda k: g.key(S[t], x, k)) for x in (p, q)]
            if kp != [c[t], c[t]]: V['ALIGN'] += 1
            exp = (S[t][p] == c[t]) if S[t][p] != S[t][q] else gam[S[t][p]]
            if order[t][l] != exp: V['ALIGN'] += 1
            if t and any(S[t][x] != c[t] for x in (p, q) if x in Mv[t]): V['ALIGN'] += 1
        B = [t for t in range(1, T + 1) if order[t][l - 1] != order[t - 1][l - 1]]
        starts = [1] + [t for t in B if t > 1]; wins = [(a, (starts[i + 1] - 1 if i + 1 < len(starts) else T)) for i, a in enumerate(starts)] if T else []
        for a_, e in wins:
            for x in (p, q):
                if sum(x in Mv[t] for t in range(a_, e + 1)) > 1: V['WO'] += 1
        Phi = [sum(S[t][x] != c[t] for x in (p, q)) for t in range(T + 1)]
        conds = (T >= 0 and Phi[0] == 2 and Phi[T] == 0 and all(Phi[t - 1] == 0 for t in B) and not any({p, q} <= Mv[t] for t in range(1, T + 1))
                 and [t for t in range(1, T + 1) if order[t][l] != order[t - 1][l]] == [t for t in range(1, T + 1) if Mv[t] & {p, q}])
        if conds != (l in dbl): V['DBLa'] += 1
        if l in dbl:
            for a_, e in wins:
                for x in (p, q):
                    if sum(x in Mv[t] for t in range(a_, e + 1)) != 1: V['DBLb'] += 1
            if mv[p] != F[l - 1] + 1 or mv[q] != F[l - 1] + 1: V['DBLb'] += 1
            if gam[0] != gam[1]: V['DBLc'] += 1
            for a_, e in wins:
                first = min((t, x) for x in (p, q) for t in range(a_, e + 1) if x in Mv[t])[1]
                if (first == p) != (not gam[0]): V['DBLc'] += 1
            f = F[l - 1]
            for x in (p, q):
                memo = {}; Rx = [sum(cv(g, S[t], y) > cv(g, S[t - 1], y) for t in range(1, T + 1)) if y != X else 0 for y in (g.O[x][0][1], g.O[x][1][1])]
                if mv[x] != f + 1 or P(g, x, memo) < f + 2: V['TN'] += 1
                if f >= 2 and any(y == X for y in (g.O[x][0][1], g.O[x][1][1])): V['TN'] += 1
                if f >= 2 and min(Rx) * 2 < f - 1: V['TN'] += 1
        if l <= d - 2 and not (mv[2 * l + 2] or mv[2 * l + 3]) and S[0][2 * l + 2] != S[0][2 * l + 3] and F[l + 1] != F[l]: V['PF'] += 1
    R = [sum(cv(g, S[t], y) > cv(g, S[t - 1], y) for t in range(1, T + 1)) for y in range(N)]
    for y in range(N):
        for t in range(1, T + 1):
            old = [z for z, _ in g.chain(S[t - 1], y, S[t - 1][y])]
            if (cv(g, S[t], y) > cv(g, S[t - 1], y)) != bool(set(old) & Mv[t]): V['HIT'] += 1
        if R[y] < mv[y]: V['HIT'] += 1
    for x in range(N):
        if len(g.O[x]) != 2: continue
        Rk = [sum(g.val(S[t], x, k) > g.val(S[t - 1], x, k) for t in range(1, T + 1)) for k in range(2)]
        pi = [0 if g.better(g.bset(S[t], x, 0), g.bset(S[t], x, 1)) else 1 for t in range(T + 1)]
        ch = [sum(pi[t] != pi[t - 1] and pi[t] == k for t in range(1, T + 1)) for k in range(2)]
        if ch[0] > Rk[0] or ch[1] > Rk[1]: V['ALTa'] += 1
        if sum(ch) > 2 * min(Rk) + 1: V['ALTb'] += 1
        if mv[x] > 2 + 2 * min(Rk): V['ALTc'] += 1
        for k in range(2):
            y = g.O[x][k][1]
            if Rk[k] != (R[y] if y != X else 0): V['ALTd'] += 1
    return T, F, dbl, mv, V
def dead(root):
    J = lambda f: G(json.load(open(os.path.join(root, f))))
    g = J('experiments/si/box76/inst/dense_d5_l3_H10.json'); s0 = [int(c) for c in '1100110110']; T, F, dbl, mv, _ = analyse(g, s0)
    desc = set(); st = [6]
    while st:
        x = st.pop()
        for o in g.O[x]:
            if o[1] != X and o[1] not in desc: desc.add(o[1]); st.append(o[1])
    print('D1 dense_d5_l3_H10 start 1100110110: T', T, 'moves(6)', mv[6], 'level', g.lev[6], 'Xi-target', any(o[1] == 6 for ox in g.O for o in ox),
          '| max moves levels 0-2', max(mv[x] for x in range(g.N) if g.lev[x] <= 2), '| strict Xi-descendants of 6', sorted(desc), 'max moves', max(mv[y] for y in desc))
    g = J('experiments/si/box76/inst/lower/REC_d10_tower_mu30.json'); T, F, dbl, mv, _ = analyse(g, g.start)
    print('D2 REC_d10_tower_mu30 stored start', ''.join(map(str, g.start)), ': T', T, 'F(0..3)', F[:4], 'doubling levels', [l for l in dbl if l <= 3])
    g = J('experiments/si/box76/inst/passfreeze77_d5.json'); T, F, dbl, mv, _ = analyse(g, g.start)
    up = [(x, k) for x in (8, 9) for k in range(2) if g.O[x][k][1] != X and g.lev[g.O[x][k][1]] > g.lev[x]]
    print('D3 passfreeze77_d5 stored start', ''.join(map(str, g.start)), ': T', T, 'F', F, 'doubling', dbl, 'moves(8,9)', mv[8], mv[9], 'upward options of pair 4', up)
    for f, pairs in (('experiments/si/box76/inst/lower/REC_d10_tower_mu30.json', None), ('experiments/si/box76/inst/lower/KILL_M2D_d6_mu13.json', None)):
        g = J(f); out = []
        for x in range(g.N):
            for k in range(2):
                y = g.O[x][k][1]
                if y == X or g.lev[y] <= g.lev[x]: continue
                for kk in range(2):
                    z = g.O[y][kk][1]
                    if z != X and g.lev[z] <= g.lev[x] + 0 and g.lev[z] < g.lev[y]: out.append((x, g.lev[x], y, g.lev[y], z, g.lev[z]))
        print('D4', os.path.basename(f), 'upward (x, lev x) -> fuel target (y, lev y) with an option -> (z, lev z), lev z <= lev x:', out[:6])
if __name__ == '__main__':
    if sys.argv[1] == 'dead': dead(sys.argv[2]); raise SystemExit
    if sys.argv[1] == 'corpus':   # the P-IDEAL-MOVES corpus as r2moves.py loads it: every start for N <= 10, stored start otherwise
        import glob
        root = sys.argv[2]; tot = {}; runs = steps = files = ndbl = 0
        fl = sorted(f for f in glob.glob(os.path.join(root, 'box1[5-8][0-9]/**/*.json'), recursive=True) if 150 <= int(os.path.relpath(f, root)[3:6]) <= 187)
        for f in fl:
            try: raw = json.load(open(f)); g = G(raw)
            except Exception: continue
            if not isinstance(raw, dict) or not g.ok_lr(): continue
            files += 1
            for s0 in (itertools.product((0, 1), repeat=g.N) if g.N <= 10 else [g.start]):
                T, F, dbl, mv, V = analyse(g, list(s0)); runs += 1; steps += T; ndbl += len(dbl)
                for k, v in V.items(): tot[k] = tot.get(k, 0) + v
        print('CORPUS files', files, 'runs', runs, 'steps', steps, 'doubling (run, level)', ndbl, 'violations', tot); raise SystemExit
    allst = '--allstarts' in sys.argv
    for f in [a for a in sys.argv[1:] if not a.startswith('--')]:
        g = G(json.load(open(f))); assert g.ok_lr()
        starts = itertools.product((0, 1), repeat=g.N) if allst else [g.start]
        tot = {}
        for s0 in starts:
            T, F, dbl, mv, V = analyse(g, s0)
            for k, v in V.items(): tot[k] = tot.get(k, 0) + v
        print(os.path.basename(f), 'd', g.N // 2, 'T', T, 'F', F, 'doubling', dbl, 'violations', tot)
