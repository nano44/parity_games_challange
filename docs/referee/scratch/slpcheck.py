#!/usr/bin/env python3 -I
"""REFEREE scratch tool for R-L1 (docs/lower/L1-statement.md at claude/l-lower 8fcc0f2).
Brute-force checks of the SLP model: Zielonka reference solver (max-parity, vertex priorities, every vertex
has a successor), an SLP interpreter (gates: P p | VE | EMPTY | OR j k | AND j k | NOT j | CPRE j), the
Lemma 2.3 program written literally, the standard vertex-priority Buchi program, Remark 2.5's shifted
nested fixpoint, and ANP's symmetric recursion ||F||_{U,V} (CSL 2021, 3.1 cases (1)-(3)) built as a gate
list with S_{n,h} trees. Vertices are bitmasks. Usage: python3 -I slpcheck.py [quick]"""
import itertools, random, sys

# ---------- games ----------
class Game:
    __slots__ = ("n", "VE", "pr", "succ", "ALL")
    def __init__(self, n, VE, pr, succ):
        self.n, self.VE, self.pr, self.succ, self.ALL = n, VE, list(pr), list(succ), (1 << n) - 1
        assert all(s for s in succ), "every vertex needs a successor"

def cpre(g, X):
    r = 0
    for v in range(g.n):
        s = g.succ[v]
        if (g.VE >> v) & 1:
            if s & X: r |= 1 << v
        else:
            if s & ~X == 0: r |= 1 << v
    return r

def attr(g, player, U, V):
    """attractor of U for player (0 Even, 1 Odd) inside subgame V (successors restricted to V)."""
    A = U & V
    while True:
        new = A
        for v in range(g.n):
            if not (V >> v) & 1 or (A >> v) & 1: continue
            s = g.succ[v] & V
            mine = ((g.VE >> v) & 1) == (player == 0)
            if (mine and s & A) or (not mine and s & ~A == 0): new |= 1 << v
        if new == A: return A
        A = new

def zielonka(g, V=None):
    if V is None: V = g.ALL
    if V == 0: return (0, 0)
    p = max(g.pr[v] for v in range(g.n) if (V >> v) & 1)
    player = p % 2
    U = sum(1 << v for v in range(g.n) if (V >> v) & 1 and g.pr[v] == p)
    A = attr(g, player, U, V)
    W0, W1 = zielonka(g, V & ~A)
    Wopp = W1 if player == 0 else W0
    if Wopp == 0:
        return (V, 0) if player == 0 else (0, V)
    B = attr(g, 1 - player, Wopp, V)
    W0, W1 = zielonka(g, V & ~B)
    return (W0, W1 | B) if player == 0 else (W0 | B, W1)

def WE(g): return zielonka(g)[0]

# ---------- SLP ----------
class SLP:
    def __init__(self): self.gates = []
    def add(self, *gate): self.gates.append(gate); return len(self.gates) - 1
    def P(self, p): return self.add("P", p)
    def VE(self): return self.add("VE")
    def EMPTY(self): return self.add("EMPTY")
    def V(self): return self.NOT(self.EMPTY())
    def OR(self, j, k): return self.add("OR", j, k)
    def AND(self, j, k): return self.add("AND", j, k)
    def NOT(self, j): return self.add("NOT", j)
    def CPRE(self, j): return self.add("CPRE", j)
    def cost(self): return sum(1 for g in self.gates if g[0] == "CPRE")
    def depth(self):
        d = []
        for g in self.gates:
            if g[0] in ("P", "VE", "EMPTY"): d.append(0)
            elif g[0] == "NOT": d.append(d[g[1]])
            elif g[0] in ("OR", "AND"): d.append(max(d[g[1]], d[g[2]]))
            else: d.append(d[g[1]] + 1)
        return d[-1]
    def run(self, g):
        val = []
        for gate in self.gates:
            k = gate[0]
            if k == "P": val.append(sum(1 << v for v in range(g.n) if g.pr[v] == gate[1]))
            elif k == "VE": val.append(g.VE)
            elif k == "EMPTY": val.append(0)
            elif k == "OR": val.append(val[gate[1]] | val[gate[2]])
            elif k == "AND": val.append(val[gate[1]] & val[gate[2]])
            elif k == "NOT": val.append(g.ALL & ~val[gate[1]])
            else: val.append(cpre(g, val[gate[1]]))
        return val[-1]

def buchi_shifted(n):
    """Lemma 2.3 literally: Z_0 = V; for i=1..n: Y_0 = 0, Y_j = Cpre((P2 & Z_{i-1}) | (P1 & Y_{j-1})), Z_i = Y_n."""
    s = SLP(); P1, P2 = s.P(1), s.P(2); Z = s.V()
    for i in range(n):
        Y = s.EMPTY()
        for j in range(n):
            Y = s.CPRE(s.OR(s.AND(P2, Z), s.AND(P1, Y)))
        Z = Y
    return s

def buchi_std(n):
    """nu Z. mu Y. (P2 & Cpre(Z)) | (P1 & Cpre(Y)), unfolded n x n; n(n+1) Cpre gates."""
    s = SLP(); P1, P2 = s.P(1), s.P(2); Z = s.V()
    for i in range(n):
        A = s.AND(P2, s.CPRE(Z)); Y = s.EMPTY()
        for j in range(n):
            Y = s.OR(A, s.AND(P1, s.CPRE(Y)))
        Z = Y
    return s

def nested_unfold(n, d, shifted):
    """theta_d x_d ... theta_0 x_0 . f(x) with Kleene unfolding n steps per level.
    shifted: f'(x) = Cpre(U_p P_p & x_p)  (Remark 2.5);  else g(x) = U_p P_p & Cpre(x_p) (standard)."""
    s = SLP(); P = [s.P(p) for p in range(d + 1)]
    def body(xs):  # xs[p] gate id for x_p
        if shifted:
            u = s.EMPTY()
            for p in range(d + 1): u = s.OR(u, s.AND(P[p], xs[p]))
            return s.CPRE(u)
        u = s.EMPTY()
        for p in range(d + 1): u = s.OR(u, s.AND(P[p], s.CPRE(xs[p])))
        return u
    def level(p, xs):  # compute theta_p x_p . ... with xs[q] fixed for q > p
        if p < 0: return body(xs)
        x = s.V() if p % 2 == 0 else s.EMPTY()
        for _ in range(n):
            xs2 = list(xs); xs2[p] = x
            x = level(p - 1, xs2)
        return x
    level(d, [None] * (d + 1))
    return s

# ---------- ANP ----------
def S_tree(n, h):
    """ANP S_{n,h}: S_{n,0} = S_{0,h} = <>, S_{n,h} = S_{n/2,h} . <S_{n,h-1}> . S_{n/2,h}  (concatenation of child lists)."""
    if n == 0 or h == 0: return []
    half = S_tree(n // 2, h)
    return half + [S_tree(n, h - 1)] + half

def C_tree(n, h):
    return [] if h == 0 else [C_tree(n, h - 1)] * n

def width(T): return 1 if not T else sum(width(c) for c in T)
def height(T): return 0 if not T else 1 + max(height(c) for c in T)

def anp_sym(n, d, U, V, shifted):
    """||(Theta, f, (0,1))||_{U,V} as an SLP. Theta = <theta_d,...,theta_0>, theta_p = nu (p even) / mu (p odd);
    f^z substitutes the LAST open argument (x_d first). Returns the SLP; the output gate is last."""
    s = SLP(); P = [s.P(p) for p in range(d + 1)]
    def f(args):  # args[p] gate id, all instantiated
        if shifted:
            u = s.EMPTY()
            for p in range(d + 1): u = s.OR(u, s.AND(P[p], args[p]))
            return s.CPRE(u)
        u = s.EMPTY()
        for p in range(d + 1): u = s.OR(u, s.AND(P[p], s.CPRE(args[p])))
        return u
    def value(p, args, A, B, U, V):
        # Theta remaining = <theta_p, ..., theta_0>; args[q] fixed for q > p
        if p < 0:  # case (1): A + B * f()
            return s.OR(A, s.AND(B, f(args)))
        if p % 2 == 0:  # nu: case (2), descend in V
            assert V, "V too short"
            Bj = B
            for Vj in V:
                a2 = list(args); a2[p] = Bj
                Bj = value(p - 1, a2, A, Bj, U, Vj)
            return Bj
        assert U, "U too short"
        Aj = A
        for Uj in U:
            a2 = list(args); a2[p] = Aj
            Aj = value(p - 1, a2, Aj, B, Uj, V)
        return Aj
    value(d, [None] * (d + 1), s.EMPTY(), s.V(), U, V)
    return s

# ---------- enumeration ----------
def all_games(n, prios, one_player=False):
    succs = [m for m in range(1, 1 << n)]
    for VE in ([(1 << n) - 1] if one_player else range(1 << n)):
        for pr in itertools.product(prios, repeat=n):
            for succ in itertools.product(succs, repeat=n):
                yield Game(n, VE, pr, succ)

def random_game(n, prios, one_player=False):
    VE = (1 << n) - 1 if one_player else random.randrange(1 << n)
    return Game(n, VE, [random.choice(prios) for _ in range(n)], [random.randrange(1, 1 << n) for _ in range(n)])

def check(name, prog, games, limit=None):
    bad = 0; cnt = 0
    for g in games:
        cnt += 1
        if prog.run(g) != WE(g):
            bad += 1
            if bad <= 2: print(f"  MISMATCH {name}: n={g.n} VE={g.VE:0{g.n}b} pr={g.pr} succ={[bin(x) for x in g.succ]} slp={prog.run(g):b} WE={WE(g):b}")
        if limit and cnt >= limit: break
    print(f"{name}: {cnt} games, {bad} mismatches, cost {prog.cost()} Cpre, depth {prog.depth()}")
    return bad

def main():
    quick = "quick" in sys.argv
    random.seed(1)
    # Lemma 2.1 games
    for n in range(2, 6):
        succ = [1 << (v + 1) for v in range(n - 1)] + [1 << (n - 1)]
        gp = Game(n, (1 << n) - 1, [1] * (n - 1) + [2], succ); gm = Game(n, (1 << n) - 1, [1] * n, succ)
        assert WE(gp) == gp.ALL and WE(gm) == 0
    print("Lemma 2.1 games: W_E(G+) = V, W_E(G-) = empty for n = 2..5  OK")
    # Lemma 2.3 / standard, Buchi {1,2}
    for n in (1, 2, 3):
        check(f"Lemma2.3 shifted n={n} exhaustive {{1,2}}", buchi_shifted(n), all_games(n, (1, 2)))
        check(f"standard   n={n} exhaustive {{1,2}}", buchi_std(n), all_games(n, (1, 2)))
    check("Lemma2.3 shifted n=4 one-player exhaustive {1,2}", buchi_shifted(4), all_games(4, (1, 2), True))
    check("Lemma2.3 shifted n=4 random two-player {1,2}", buchi_shifted(4), (random_game(4, (1, 2)) for _ in range(20000 if quick else 300000)))
    check("Lemma2.3 shifted n=5 random two-player {1,2}", buchi_shifted(5), (random_game(5, (1, 2)) for _ in range(5000 if quick else 100000)))
    # program for n solves smaller games too (Def 1.4 'games with fewer vertices included')
    check("Lemma2.3 shifted n=4 program on n=2,3 games", buchi_shifted(4), itertools.chain(all_games(2, (1, 2)), all_games(3, (1, 2))))
    # Remark 2.5: shifted nested fixpoint, priorities {0..d}, d <= n (TARGET)
    for n, d in ((2, 2), (3, 2), (3, 3)):
        check(f"Remark2.5 shifted nested n={n} d={d} exhaustive", nested_unfold(n, d, True), all_games(n, tuple(range(d + 1))))
        check(f"standard  nested n={n} d={d} exhaustive", nested_unfold(n, d, False), all_games(n, tuple(range(d + 1))))
    check("Remark2.5 shifted nested n=4 d=3 random", nested_unfold(4, 3, True), (random_game(4, (0, 1, 2, 3)) for _ in range(3000 if quick else 30000)))
    check("Remark2.5 shifted nested n=4 d=4 random", nested_unfold(4, 4, True), (random_game(4, (0, 1, 2, 3, 4)) for _ in range(2000 if quick else 20000)))
    # ANP symmetric with S trees
    for n, d in ((2, 2), (3, 2), (3, 3), (4, 3)):
        hmu = sum(1 for p in range(d + 1) if p % 2 == 1); hnu = d // 2 + 1
        U, V = S_tree(n, hmu), S_tree(n, hnu)
        print(f"  S_{{{n},{hmu}}} width {width(U)} height {height(U)};  S_{{{n},{hnu}}} width {width(V)} height {height(V)}")
        for shifted in (False, True):
            prog = anp_sym(n, d, U, V, shifted)
            exp = width(U) * width(V) * (1 if shifted else d + 1)
            games = all_games(n, tuple(range(d + 1))) if n <= 3 else (random_game(4, tuple(range(d + 1))) for _ in range(2000 if quick else 20000))
            check(f"ANP sym S-trees n={n} d={d} {'f-shifted' if shifted else 'g-standard'} (expected cost {exp})", prog, games)
    # ANP with a NON-universal tree must fail somewhere (sanity of the harness): V = path of height hnu (width 1)
    n, d = 3, 2
    path = [[]]  # height 1, width 1 ; (3,1)-universal needs 3 leaves
    prog = anp_sym(n, d, S_tree(n, 1), [[path]], False) if False else anp_sym(n, d, S_tree(n, 1), [[[]]], False)
    print("  sanity (non-universal V, height 2 width 1):", end=" ")
    check(f"ANP sym non-universal n={n} d={d}", prog, all_games(n, (0, 1, 2)))

if __name__ == "__main__":
    main()
