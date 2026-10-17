#!/usr/bin/env python3 -I
"""REFEREE scratch tool for R-psolC. My own psolC written straight from Huth-Kuo-Piterman DTR15-4: Definition 1 (reachability
of (X,p) under parity; the prefix minimum includes the start colour), Definition 2 (product graph G^p_X), Theorem 1
(Wr_p = projection of the attractor of Z = X x {c : c%2 = p}), Figure 5 (psolC / tryPlayer / fixedpoint). MIN-parity colours as
in the paper; games read from PGSolver files (max-parity) are converted with c = M - pr, M even >= max pr. Variant
`exclude_start` = the reading of DTR Example 3 step (ii) (minimum over 0 < i <= j). Also: exhaustive comparison with the
lane's experiments/attr/psolc.py on all labelled games with n <= 3 (optional, needs the lane dir).
Usage: psolccheck.py FILE.pg [--x]  |  psolccheck.py --exhaustive LANE_ATTR_DIR"""
import sys, os, itertools, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slpcheck import Game, WE

def read_pg(path):
    pr, own, succ = {}, {}, {}
    for line in open(path):
        line = line.strip().rstrip(";")
        if not line or line.startswith("parity"): continue
        parts = line.split()
        v, p, o = int(parts[0]), int(parts[1]), int(parts[2])
        succ[v] = [int(x) for x in parts[3].split(",")]; pr[v] = p; own[v] = o
    n = max(pr) + 1
    return Game(n, sum(1 << v for v in range(n) if own[v] == 0), [pr[v] for v in range(n)], [sum(1 << w for w in succ[v]) for v in range(n)])

def colours(g):
    P = max(g.pr); M = P if P % 2 == 0 else P + 1
    return [M - p for p in g.pr]

def owner(g, v): return 0 if (g.VE >> v) & 1 else 1

def attr(g, alive, X, p):
    A = set(X)
    while True:
        new = set(A)
        for v in alive:
            if v in A: continue
            s = [w for w in range(g.n) if (g.succ[v] >> w) & 1 and w in alive]
            if (owner(g, v) == p and any(w in A for w in s)) or (owner(g, v) != p and all(w in A for w in s)): new.add(v)
        if new == A: return A
        A = new

def wr(g, col, alive, X, p, exclude_start=False):
    """Wr_p(G, X) by Def. 2 + Thm 1, on the FULL product V x C_bot (not only the reachable part), then restricted to X."""
    C = sorted({col[v] for v in alive})
    BOT = -1
    nodes = [(v, l) for v in alive for l in [BOT] + C]
    def succs(v, l):
        if l != BOT and v in X and l % 2 == p: return []          # dead end = target (Def. 2: no edge when v in X and c%2 = p)
        out = []
        for w in range(g.n):
            if not ((g.succ[v] >> w) & 1) or w not in alive: continue
            if l == BOT: nl = col[w] if exclude_start else min(col[v], col[w])
            else: nl = min(l, col[w])
            out.append((w, nl))
        return out
    E = {nd: succs(*nd) for nd in nodes}
    Z = {(v, l) for (v, l) in nodes if l != BOT and v in X and l % 2 == p}
    A = set(Z)
    while True:
        new = set(A)
        for nd in nodes:
            if nd in A: continue
            s = E[nd]
            if (owner(g, nd[0]) == p and any(x in A for x in s)) or (owner(g, nd[0]) != p and s and all(x in A for x in s)): new.add(nd)
        if new == A: break
        A = new
    return {v for v in alive if (v, BOT) in A}

def fixedpoint(g, col, alive, X, p, ex, trace=False):
    X = set(X)
    while True:
        if not X: return X
        W = X & wr(g, col, alive, X, p, ex)
        if trace: print(f"    fixedpoint p={p}: X={sorted(X)} -> X ∩ Wr = {sorted(W)}")
        if X <= W: return X
        X = X & W

def psolC(g, ex=False, trace=False):
    col = colours(g); alive = set(range(g.n)); win = {}; decisions = []
    while alive:
        removed = False
        for p in (0, 1):
            X = fixedpoint(g, col, alive, {v for v in alive if col[v] % 2 == p}, p, ex, trace)
            if X:
                D = attr(g, alive, X, p)
                for v in D: win[v] = p
                decisions.append((p, sorted(X), sorted(D)))
                if trace: print(f"  player {p}: gfp {sorted(X)}, removed Attr {sorted(D)}")
                alive -= D; removed = True; break
        if not removed: break
    return win, alive, decisions

def main():
    if "--exhaustive" in sys.argv:
        lane = sys.argv[sys.argv.index("--exhaustive") + 1]
        sys.path.insert(0, os.path.join(lane, "..", "harness")); sys.path.insert(0, lane)
        import pg as lpg, psolc as lpsolc
        from slpcheck import all_games, random_game
        random.seed(5)
        for name, games in (("n=1", all_games(1, (0, 1))), ("n=2", all_games(2, (0, 1, 2))), ("n=3", all_games(3, (0, 1, 2, 3))),
                            ("n=4 random", (random_game(4, (0, 1, 2, 3, 4)) for _ in range(3000)))):
            cnt = diff = diffx = unsound = litonly = xonly = 0; comp = compx = 0
            for g in games:
                cnt += 1
                ref = WE(g)
                lg = lpg.Game(list(g.pr), [0 if (g.VE >> v) & 1 else 1 for v in range(g.n)], [[w for w in range(g.n) if (g.succ[v] >> w) & 1] for v in range(g.n)])
                for ex in (False, True):
                    win, res, _ = psolC(g, ex)
                    for v, p in win.items():
                        if ((ref >> v) & 1) != (p == 0): unsound += 1
                    lw, _, lres, _ = lpsolc.PsolC(lg, strat=None, exclude_start=ex).run()
                    lwin = {v: lw[v] for v in range(g.n) if lw[v] is not None}
                    if lwin != win or set(lres) != res:
                        if ex: diffx += 1
                        else: diff += 1
                    if not ex: comp += (not res); c_lit = not res
                    else: compx += (not res); c_x = not res
                litonly += (c_lit and not c_x); xonly += (c_x and not c_lit)
            print(f"{name}: {cnt} games; literal: mine vs lane differ on {diff}; exclude-start: differ on {diffx}; unsound decisions {unsound}; "
                  f"complete literal {comp}, complete exclude-start {compx}; literal-only {litonly}, exclude-start-only {xonly}", flush=True)
        return
    g = read_pg(sys.argv[1]); ex = "--x" in sys.argv
    print(f"{sys.argv[1]}: n={g.n}, colours (min-parity) {colours(g)}, W_E (Zielonka) = {[v for v in range(g.n) if (WE(g) >> v) & 1]}")
    win, res, dec = psolC(g, ex, trace=True)
    print(f"  reading {'EXAMPLE-3 (start colour excluded)' if ex else 'LITERAL (Def. 1)'}: decided {win}; residual {sorted(res)}")

if __name__ == "__main__":
    main()
