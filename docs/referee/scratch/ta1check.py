#!/usr/bin/env python3 -I
"""REFEREE scratch tool for T-A1 (docs/attr/TA1-proof.md at claude/l-attr d5d6396). Independent of experiments/attr/.
My own psolB (HKP arXiv 1405.0386v2 Fig. 3) and psolQ (Fig. 5, Def. 6) written in HKP's MIN-parity colours and fed
colour = M - pr (M even >= max pr), my own PA** (TA1-proof.md section 1, max-parity, exhaustive over X and S), Zielonka
from slpcheck.py as the reference. Games are bitmask games (slpcheck.Game). Checks: psolB-complete <=> PA**;
PA** => psolQ-complete; HKP classes (Buchi, SCC-constant, deterministic) => PA**; psolB order independence (Thm 6).
Usage: python3 -I ta1check.py [quick]"""
import sys, os, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slpcheck import Game, WE, all_games, random_game

def bits(m):
    v = 0
    while m:
        if m & 1: yield v
        m >>= 1; v += 1

# ---------------- HKP, min-parity colours, players 0/1 (owner bit: g.VE = player 0's vertices) ----------------
def attr_hkp(g, alive, X, p):
    """Def. 1: Attr_p[G, X] inside the subgame `alive`, X included."""
    A = X & alive
    while True:
        new = A
        for v in bits(alive & ~A):
            s = g.succ[v] & alive
            mine = ((g.VE >> v) & 1) == (p == 0)
            if (mine and s & A) or (not mine and s & ~A == 0): new |= 1 << v
        if new == A: return A
        A = new

def mattr_hkp(g, col, alive, X, c, p, permissive=False):
    """Def. 3 (Def. 6 if permissive): mu Z. mpre_p(Z, X, c); X external; colour >= c (or v in X if permissive)."""
    Z = 0
    while True:
        new = Z
        for v in bits(alive & ~Z):
            if not (col[v] >= c or (permissive and (X >> v) & 1)): continue
            s = g.succ[v] & alive
            mine = ((g.VE >> v) & 1) == (p == 0)
            if (mine and s & (Z | X)) or (not mine and s & ~(Z | X) == 0): new |= 1 << v
        if new == Z: return Z
        Z = new

def colours(g):
    P = max(g.pr); M = P if P % 2 == 0 else P + 1
    return [M - p for p in g.pr]

def psolB(g, order="desc"):
    """Fig. 3. Returns (win dict v->player, residual mask). order: 'desc' (HKP), 'asc', or a list (Thm 6 check)."""
    col = colours(g); alive = g.ALL; win = {}
    while alive:
        removed = False
        cs = sorted({col[v] for v in bits(alive)}, reverse=(order == "desc")) if order in ("desc", "asc") else order
        for d in cs:
            p = d % 2
            X = sum(1 << v for v in bits(alive) if col[v] == d)
            cache = -1
            while X and X != cache:
                cache = X
                MA = mattr_hkp(g, col, alive, X, d, p)
                if X & ~MA == 0:
                    D = attr_hkp(g, alive, MA, p)
                    for v in bits(D): win[v] = p
                    alive &= ~D; removed = True; break
                X &= MA
            if removed: break
        if not removed: break
    return win, alive

def layered_attr(g, col, alive, p, X):
    A = 0; b = max(col[v] for v in bits(X)); d = p
    while d <= b:
        Y = sum(1 << v for v in bits(X) if col[v] <= d)
        A = mattr_hkp(g, col, alive, A | Y, d, p, permissive=True)
        d += 2
    return A

def psolQ(g):
    col = colours(g); alive = g.ALL; win = {}
    while alive:
        removed = False
        for b in sorted({col[v] for v in bits(alive)}):
            p = b % 2
            X = sum(1 << v for v in bits(alive) if col[v] <= b and col[v] % 2 == p)
            cache = -1
            while X and X != cache:
                cache = X
                W = layered_attr(g, col, alive, p, X)
                if X & ~W == 0:
                    D = attr_hkp(g, alive, W, p)
                    for v in bits(D): win[v] = p
                    alive &= ~D; removed = True; break
                X &= W
            if removed: break
        if not removed: break
    return win, alive

# ---------------- PA** in max-parity (TA1-proof.md section 1) ----------------
def is_p(g, v, p): return ((g.VE >> v) & 1) == (p == 0)   # p = 0 Even, 1 Odd

def attr_in(g, R, X, p):
    """Attr_p^R(X): inside R, X included (X subset of R assumed)."""
    A = X & R
    while True:
        new = A
        for v in bits(R & ~A):
            s = g.succ[v] & R
            if (is_p(g, v, p) and s & A) or (not is_p(g, v, p) and s & ~A == 0): new |= 1 << v
        if new == A: return A
        A = new

def mattr_in(g, R, X, d, p):
    """MAttr_p^R(X, d): least Z subset R, pr(v) <= d, p-vertex with an R-successor in Z u X or q-vertex with all R-successors in Z u X."""
    Z = 0
    while True:
        new = Z
        for v in bits(R & ~Z):
            if g.pr[v] > d: continue
            s = g.succ[v] & R
            if (is_p(g, v, p) and s & (Z | X)) or (not is_p(g, v, p) and s & ~(Z | X) == 0): new |= 1 << v
        if new == Z: return Z
        Z = new

def is_trap_for_q(g, S, R, p):
    """S subset R is a trap for q (= 1-p) in R: q-vertices of S keep all R-successors in S, p-vertices keep one."""
    for v in bits(S):
        s = g.succ[v] & R
        if is_p(g, v, p):
            if not (s & S): return False
        else:
            if s & ~S: return False
    return True

def subsets(m):
    vs = list(bits(m))
    for r in range(1, len(vs) + 1):
        for c in itertools.combinations(vs, r):
            yield sum(1 << v for v in c)

def peelable(g, R, d, p, memo=None):
    if memo is None: memo = {}
    key = (R, d)
    if key in memo: return memo[key]
    if R == 0: return True
    if d < 0: memo[key] = False; return False
    assert all(g.pr[v] <= d for v in bits(R))
    cands = []
    T = sum(1 << v for v in bits(R) if g.pr[v] == d)
    for X in subsets(T):
        W = mattr_in(g, R, X, d, p)
        if X & ~W == 0: cands.append(attr_in(g, R, W, p))
    low = sum(1 << v for v in bits(R) if g.pr[v] <= d - 2)
    for S in subsets(low):
        if is_trap_for_q(g, S, R, p) and peelable(g, S, d - 2, p, memo): cands.append(attr_in(g, R, S, p))
    res = any(peelable(g, R & ~F, d, p, memo) for F in set(cands) if F)
    memo[key] = res
    return res

def pa2(g):
    W0 = WE(g); W1 = g.ALL & ~W0; P = max(g.pr)
    dE = P if P % 2 == 0 else P + 1; dO = P if P % 2 == 1 else P + 1
    return peelable(g, W0, dE, 0) and peelable(g, W1, dO, 1)

# ---------------- classes ----------------
def sccs(g):
    n = g.n; idx = {}; low = {}; st = []; on = set(); res = []; c = [0]
    sys.setrecursionlimit(10000)
    def dfs(v):
        idx[v] = low[v] = c[0]; c[0] += 1; st.append(v); on.add(v)
        for w in bits(g.succ[v]):
            if w not in idx: dfs(w); low[v] = min(low[v], low[w])
            elif w in on: low[v] = min(low[v], idx[w])
        if low[v] == idx[v]:
            comp = set()
            while True:
                w = st.pop(); on.discard(w); comp.add(w)
                if w == v: break
            res.append(comp)
    for v in range(n):
        if v not in idx: dfs(v)
    return res

def classes(g):
    vals = sorted(set(g.pr))
    buchi = len(vals) == 1 or (len(vals) == 2 and vals[0] % 2 != vals[1] % 2)
    scc = all(len({g.pr[v] for v in C}) == 1 for C in sccs(g))
    det = all(bin(s).count("1") == 1 for s in g.succ)
    return buchi, scc, det

def fmt(g): return f"n={g.n} VE={g.VE:0{g.n}b} pr={g.pr} succ={[bin(s) for s in g.succ]}"

def run(name, games, limit=None):
    cnt = bad = 0; cls = [0, 0, 0]; stats = dict(pb=0, pq=0, pa=0)
    for g in games:
        cnt += 1
        win, resB = psolB(g); ref = WE(g)
        for v, p in win.items():
            assert ((ref >> v) & 1) == (p == 0), ("psolB unsound", fmt(g))
        winq, resQ = psolQ(g)
        for v, p in winq.items():
            assert ((ref >> v) & 1) == (p == 0), ("psolQ unsound", fmt(g))
        if psolB(g, "asc")[1] != resB:
            bad += 1; print("  ORDER DEPENDENCE psolB:", fmt(g))
        pa = pa2(g); pbc = resB == 0; pqc = resQ == 0
        stats["pb"] += pbc; stats["pq"] += pqc; stats["pa"] += pa
        if pa != pbc:
            bad += 1
            if bad <= 5: print(f"  MISMATCH psolB-complete={pbc} PA**={pa}: {fmt(g)}")
        if pa and not pqc:
            bad += 1; print(f"  MISMATCH PA** but psolQ incomplete: {fmt(g)}")
        if pbc and not pqc:
            bad += 1; print(f"  psolB-complete but psolQ incomplete: {fmt(g)}")
        b, s, dd = classes(g)
        for i, c in enumerate((b, s, dd)):
            if c:
                cls[i] += 1
                if not pa:
                    bad += 1; print(f"  class {['buchi','scc','det'][i]} not PA**: {fmt(g)}")
        if limit and cnt >= limit: break
    print(f"{name}: {cnt} games, {bad} problems; psolB-complete {stats['pb']}, psolQ-complete {stats['pq']}, PA** {stats['pa']}; "
          f"buchi/scc/det members {cls}")

def main():
    quick = "quick" in sys.argv
    random.seed(7)
    # HKP Fig. 4(a) in max-parity (M = 4: colour c -> pr = 4 - c): v0 pr1 E, v1 pr2 O, v2 pr4 E, v3 pr2 O, v4 pr1 E
    fig4a = Game(5, 0b10101, [1, 2, 4, 2, 1], [0b00010, 0b00101, 0b01010, 0b10100, 0b01000])
    winB, resB = psolB(fig4a); winQ, resQ = psolQ(fig4a)
    print(f"HKP Fig.4(a): W_E={WE(fig4a):05b} psolB residual {resB:05b} (expect all 5 undecided), psolQ residual {resQ:05b} (expect 0), PA**={pa2(fig4a)} (expect False)")
    # the SCC-constant witness of Prop. 3: 0 3 0 0; 1 1 0 0; 2 1 0 0,2  (all Even)
    w = Game(3, 0b111, [3, 1, 1], [0b001, 0b001, 0b101])
    print(f"Prop.3 SCC witness: W_E={WE(w):03b} psolB residual {psolB(w)[1]:03b} PA**={pa2(w)} classes(buchi,scc,det)={classes(w)}")
    for n in (1, 2, 3):
        run(f"n={n} exhaustive, priorities 0..{n}", all_games(n, tuple(range(n + 1))))
    run("n=4 random, priorities 0..4", (random_game(4, (0, 1, 2, 3, 4)) for _ in range(3000 if quick else 30000)))
    run("n=4 random one-player (Even), priorities 0..4", (random_game(4, (0, 1, 2, 3, 4), True) for _ in range(2000 if quick else 20000)))
    run("n=5 random, priorities 0..5", (random_game(5, (0, 1, 2, 3, 4, 5)) for _ in range(1000 if quick else 10000)))
    run("n=5 random, priorities 0..2", (random_game(5, (0, 1, 2)) for _ in range(1000 if quick else 10000)))

if __name__ == "__main__":
    main()
