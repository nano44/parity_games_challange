#!/usr/bin/env python3
"""L-RED R183 FVCH: the circular term of FL-ANCHOR' (L-NEW 46 box 134, docs/new/N5-OVT-box134.md section 1) on every maximal FL run.
FL run as in the frozen packet P-N5-ANCHOR (no fallback, tau and sigma-bar may change? no: tau unchanged, sigma changes, W unchanged).
Per state s of a run [a, b]: anchors A_s(y) and prefixes P_s(y) (W-play: sigma_s at Even, tau_a at Odd, from y up to the first vertex of
ODIFF_s u CN), for y in T_x u {sigma_s(x)}, every Even x (T_x as in the packet: x not in CN: extend(x, W(y)) = W(x); x in CN: W(y)'s cycle
node is x). FV_s = anchors A with A_s(y) = A != A_s(z), or A_s(y) = A_s(z) = A and w_s(A) (cycle node of Xi_s(A)) on P_s(y) u P_s(z).
FVU := union of FV_s over the run. Counted per run:
  FVCH  = #{s in (a, b] : Xi_s(A) != Xi_(s-1)(A) for some A in FVU}   (box 134's FVCH, over transitions s-1 -> s)
  FVMAX = max over A in FVU of #{s : Xi_s(A) != Xi_(s-1)(A)}
  CNCH  = #{s : w_s(A) != w_(s-1)(A) for some A in ODIFF_s u CN},  SBCH = #{s : sbar_s != sbar_(s-1)}
  CROSS = order flips of cmpw.py class CROSS (anchors of y and z differ at j-1, prefixes unchanged j-2 -> j-1), FLIPS = all flips.
  CAP   = packet CAP. BOUND = CAP * (1 + SBCH + CNCH + FVCH) (FL-ANCHOR'; BVIOL if L > BOUND).
Prints one line for the run with the largest FVCH (ties: longer) and totals. Usage: fvch.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21")); sys.path.insert(0, os.path.join(HERE, "..", "r170"))
from n5x import load, start_pair, readstart, Engine, dual
import pg
from freeze import run

def analyse(g, st=None, cap=10 ** 5):
    E0, Ed0 = Engine(g), Engine(dual(g)); s, t = start_pair(g, E0, Ed0, st)
    S, T, F, E = run(g, s, t, cap=cap); n, own, pr = g.n, g.owner, g.prio
    Wc = {}
    def weng(tau):
        if tau not in Wc: Wc[tau] = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]))
        return Wc[tau]
    WV = {}
    def wval(j):
        if j not in WV: WV[j] = weng(T[j]).evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0]
        return WV[j]
    runs = []; cur = None
    for j in range(1, len(S)):
        if not F[j] and T[j] == T[j - 1] and S[j] != S[j - 1] and wval(j) == wval(j - 1):
            if cur and cur[1] == j - 1: cur[1] = j
            else: cur = [j - 1, j]; runs.append(cur)
    out = []
    for a, b in runs:
        tau = T[a]; W = wval(a); CN = {v for v in range(n) if W[v][2] == 0}
        Tx = {}
        for x in range(n):
            if own[x]: continue
            if x in CN: Tx[x] = [y for y in g.succ[x] if W[y][0] == x]
            else: Tx[x] = [y for y in g.succ[x] if E.extend(x, W[y]) == W[x]]
        lm = max([W[x][2] for x in range(n) if own[x] == 0 and x not in CN] + [1])
        CAP = (lm - 1) + sum(max(len(Tx[c]) - 1, 0) for c in CN if own[c] == 0)
        XS = {j: E.evaluate(S[j]) for j in range(a, b + 1)}
        OD = {j: {o for o in range(n) if own[o] == 1 and XS[j][1][o] != tau[o]} for j in XS}
        def pre(s, y):
            p = []; u = y
            while u not in OD[s] and u not in CN and len(p) <= n:
                p.append(u); u = S[s][u] if own[u] == 0 else tau[u]
            return tuple(p), u
        FVU = set(); PR = {}
        for s_ in range(a, b + 1):
            for x in range(n):
                if own[x]: continue
                opts = sorted(set(Tx[x]) | {S[s_][x]})
                pa = {y: pre(s_, y) for y in opts}; PR[(s_, x)] = pa
                for i, y in enumerate(opts):
                    for z in opts[i + 1:]:
                        (Py, Ay), (Pz, Az) = pa[y], pa[z]
                        if Ay != Az: FVU.add(Ay); FVU.add(Az)
                        else:
                            w = XS[s_][0][Ay][0]
                            if w in Py or w in Pz: FVU.add(Ay)
        fvch = cnch = sbch = 0; per = {A: 0 for A in FVU}
        for s_ in range(a + 1, b + 1):
            ch = [A for A in FVU if XS[s_][0][A] != XS[s_ - 1][0][A]]
            for A in ch: per[A] += 1
            fvch += bool(ch); sbch += XS[s_][1] != XS[s_ - 1][1]
            cnch += any(XS[s_][0][A][0] != XS[s_ - 1][0][A][0] for A in (OD[s_] | CN))
        flips = cross = 0
        k = lambda s_, v: E.key(XS[s_][0][v])
        for j in range(a + 2, b + 1):
            for x in range(n):
                if own[x] or S[j][x] == S[j - 1][x] or x in CN: continue
                y, z = S[j][x], S[j - 1][x]
                if k(j - 2, y) > k(j - 2, z) or not k(j - 1, y) > k(j - 1, z): continue
                flips += 1
                p2 = (pre(j - 2, y), pre(j - 2, z)); p1 = (pre(j - 1, y), pre(j - 1, z))
                if p1 == p2 and p1[0][1] != p1[1][1]: cross += 1
        L = b - a; bound = CAP * (1 + sbch + cnch + fvch)
        out.append(dict(a=a, b=b, L=L, FVCH=fvch, FVMAX=max(per.values(), default=0), FVU=len(FVU), CNCH=cnch, SBCH=sbch,
                        FLIPS=flips, CROSS=cross, CAP=CAP, BOUND=bound, BVIOL=int(L > bound)))
    return dict(n=n, K=len(S) - 1, runs=out)

if __name__ == "__main__":
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
    R = analyse(g, st); rs = R["runs"]
    best = max(rs, key=lambda r: (r["FVCH"], r["L"]), default=None)
    tot = {k: sum(r[k] for r in rs) for k in ("L", "FVCH", "CROSS", "FLIPS", "BVIOL")}
    bs = " ".join(f"{k} {v}" for k, v in best.items()) if best else "none"
    print(f"FVCH {os.path.basename(sys.argv[1])} n {R['n']} K {R['K']} runs {len(rs)} BEST {bs} | TOT " + " ".join(f"{k} {v}" for k, v in tot.items()))
