#!/usr/bin/env python3
"""L-NEW box 137 REL: checks of the box 137 lemmas on every maximal FL run (run detection = box132/anchor.py).
Per FL run [a, b] (W, tau constant; T_x, CN, levels as in P-N5-ANCHOR §1):
- CEIL: Xi_j(v) <= W(v) at every vertex and state (Lemma CEIL); CEILVIOL counts (v, j) with Xi_j(v) > W(v).
- SATDEC: v saturated (Xi_j(v) = W(v)) at j - 1 but not at j (Lemma SAT-MONO predicts 0).
- FROZVIOL: an Even x not in CN moves at j although its old option was saturated at j - 1 (Corollary SAT-FREEZE predicts 0).
- SYNC: Even x != x' not in CN with T_x = T_x' and sigma_(j-1)(x) = sigma_(j-1)(x'); SYNCVIOL: sigma_j(x) != sigma_j(x').
- CW: options y (not in CN) whose first ODIFF/CN vertex A on the W-play has Xi_j(A) with cycle node c = W-cycle node of y and A != y;
  CWVIOL: Xi_j(y) != (c, (Wmask(y) & ~Wmask(A)) | Ximask(A), l(y) - l(A) + Xilen(A)) (Lemma C-WORLD).
- RET: moves into an option held earlier in the same run; RETMAX = max returns of one (x, y) in one run; MOVMAX = max moves of one x.
- CWMOV / WWMOV: movers whose old and new options both have Xi-cycle node = W-cycle node (c-world) / not; DEFVIOL: a c-world
  move that does not strictly lower the deficit (W-weight minus Xi-weight, then length; Lemma DEFICIT).
- CHAIN: at every move of x, Xi_(j-1)(new option) > Xi_(j-1)(old option) and the destination values strictly increase along x's moves
  (Corollary BAND); CHAINVIOL counts failures (x not in CN).
Usage: rel.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box21")); sys.path.insert(0, os.path.join(HERE, "..", "..", "red", "r170"))
from n5x import load, start_pair, readstart, Engine, dual
import pg
from freeze import run
LAST = {}
def analyse(g, st=None, cap=10 ** 6):
    E0, Ed0 = Engine(g), Engine(dual(g)); s, t = start_pair(g, E0, Ed0, st)
    S, T, F, E = run(g, s, t, cap); n, own, pr = g.n, g.owner, g.prio
    Wc = {}
    def weng(tau):
        if tau not in Wc: Wc[tau] = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]))
        return Wc[tau]
    def wval(j):
        return weng(T[j]).evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0]
    runs = []; cur = None
    for j in range(1, len(S)):
        if not F[j] and T[j] == T[j - 1] and S[j] != S[j - 1] and wval(j) == wval(j - 1):
            if cur and cur[1] == j - 1: cur[1] = j
            else: cur = [j - 1, j]; runs.append(cur)
    K = E.key
    R = dict(runs=len(runs), fl=0, ceilviol=0, satdec=0, satgain=0, movers=0, frozviol=0, sync=0, syncviol=0, cw=0, cwviol=0, ret=0,
             retmax=0, movmax=0, chainviol=0, cnmov=0, cwmov=0, wwmov=0, defviol=0)
    ex = []
    for a, b in runs:
        tau = T[a]; W = wval(a); lvl = [W[v][2] for v in range(n)]
        CN = set(v for v in range(n) if lvl[v] == 0)
        Tx = {x: frozenset(y for y in g.succ[x] if E.extend(x, W[y]) == W[x]) for x in range(n) if own[x] == 0 and x not in CN}
        XI, SB = {}, {}
        for j in range(a, b + 1):
            XI[j], SB[j] = E.evaluate(S[j])
        R["fl"] += b - a
        held = {x: {S[a][x]} for x in range(n) if own[x] == 0}
        retc, movc, lastdest = {}, {}, {}
        for j in range(a, b + 1):
            xi = XI[j]
            for v in range(n):
                if K(xi[v]) > K(W[v]): R["ceilviol"] += 1
                if j > a:
                    s0, s1 = XI[j - 1][v] == W[v], xi[v] == W[v]
                    if s0 and not s1: R["satdec"] += 1
                    if s1 and not s0: R["satgain"] += 1
            od = set(o for o in range(n) if own[o] == 1 and SB[j][o] != tau[o])
            succ1 = [S[j][v] if own[v] == 0 else tau[v] for v in range(n)]
            for y in range(n):
                if y in CN or y in od: continue
                A = succ1[y]; steps = 0
                while A not in od and A not in CN and steps <= n: A = succ1[A]; steps += 1
                if xi[A][0] != W[y][0]: continue
                R["cw"] += 1
                pred = (W[y][0], (W[y][1] & ~W[A][1]) | xi[A][1], lvl[y] - lvl[A] + xi[A][2])
                if xi[y] != pred:
                    R["cwviol"] += 1
                    if len(ex) < 4: ex.append(("CW", a, j, y, A, xi[y], pred))
            if j == a: continue
            X0 = XI[j - 1]
            for x in Tx:
                if S[j][x] != S[j - 1][x]:
                    R["movers"] += 1
                    o, y = S[j - 1][x], S[j][x]
                    if X0[o] == W[o]: R["frozviol"] += 1
                    if X0[o][0] == W[o][0] and X0[y][0] == W[y][0]:
                        R["cwmov"] += 1
                        # Lemma DEFICIT: in the c-world, Xi-better = strictly smaller deficit (weight W - weight Xi, then length)
                        d = lambda v: (E.weight(W[v][1]) - E.weight(X0[v][1]), -X0[v][2] if E.par[W[v][0]] == 1 else X0[v][2])
                        if not d(y) < d(o): R["defviol"] += 1
                    else: R["wwmov"] += 1
                    if not K(X0[y]) > K(X0[o]): R["chainviol"] += 1
                    if x in lastdest and not K(X0[y]) > lastdest[x]: R["chainviol"] += 1
                    lastdest[x] = K(X0[y])
                    movc[x] = movc.get(x, 0) + 1
                    if y in held[x]:
                        R["ret"] += 1; retc[(x, y)] = retc.get((x, y), 0) + 1
                    held[x].add(y)
            for x in range(n):
                if own[x] == 0 and x in CN and S[j][x] != S[j - 1][x]: R["cnmov"] += 1
            xs = sorted(Tx)
            for i1 in range(len(xs)):
                for i2 in range(i1 + 1, len(xs)):
                    x1, x2 = xs[i1], xs[i2]
                    if Tx[x1] == Tx[x2] and S[j - 1][x1] == S[j - 1][x2]:
                        R["sync"] += 1
                        if S[j][x1] != S[j][x2]:
                            R["syncviol"] += 1
                            if len(ex) < 4: ex.append(("SYNC", a, j, x1, x2))
        R["retmax"] = max([R["retmax"]] + list(retc.values())); R["movmax"] = max([R["movmax"]] + list(movc.values()))
    LAST.update(S=S, T=T, F=F, E=E, runs=runs, wval=wval, retc=locals().get("retc", {}))
    return R, ex, len(S) - 1

if __name__ == "__main__":
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
    R, ex, KK = analyse(g, st)
    print(f"REL {os.path.basename(sys.argv[1])} n {g.n} K {KK} " + " ".join(f"{k.upper()} {v}" for k, v in R.items()) + (f" EX {ex}" if ex else ""))
