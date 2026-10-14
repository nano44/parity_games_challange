#!/usr/bin/env python3
"""REFEREE throwaway: faithful implementation of arXiv 2511.03752 v1 (van der Heijden,
"Attractors Is All You Need"), Algorithm 1 with the functions U_d, A*, A', A^k, plus a
min-parity Zielonka reference, plus a random counterexample search.

Conventions (the paper's): MIN-parity (Even wins a play iff the lowest priority seen
infinitely often is even), priorities on vertices, no self-loops, every vertex has a successor.
Game: n vertices 0..n-1; owner[v] in {0 (Even), 1 (Odd)}; pr[v] >= 0; succ[v] non-empty list.

Readings (ambiguities in the paper), chosen by flags:
  aprime_base = "lt"  : base of A'_d(A) is {v in A \\ (A* u U_d) : pr(v) < d}   (literal, eq. for A')
              = "all" : drop the "pr(v) < d" filter (a charitable reading)
  astar_scope = "G"   : A*_d computed with attractors in the whole current game G (literal)
              = "A"   : attractors restricted to the current A^k (charitable reading)
Usage: python3 -I aiayn.py [--search N] [--seed S] [--pg file.pg] [--trace]
"""
import sys, random, argparse

def attr(n, owner, succ, pred, player, U):
    """Standard attractor of set U for `player` (0 Even / 1 Odd), within vertex set `alive`."""
    inA = set(U)
    cnt = {}
    todo = list(U)
    while todo:
        u = todo.pop()
        for v in pred[u]:
            if v in inA: continue
            if owner[v] == player:
                inA.add(v); todo.append(v)
            else:
                cnt[v] = cnt.get(v, len(succ[v])) - 1
                if cnt[v] == 0:
                    inA.add(v); todo.append(v)
    return inA

class Game:
    def __init__(self, owner, pr, succ):
        self.n = len(owner); self.owner = list(owner); self.pr = list(pr)
        self.succ = [list(s) for s in succ]
        assert all(self.succ[v] for v in range(self.n)), "every vertex needs a successor"
        assert all(v not in self.succ[v] for v in range(self.n)), "no self-loops (paper's assumption)"
    def sub(self, remove):
        keep = [v for v in range(self.n) if v not in remove]
        idx = {v: i for i, v in enumerate(keep)}
        return Game([self.owner[v] for v in keep], [self.pr[v] for v in keep],
                    [[idx[w] for w in self.succ[v] if w in idx] for v in keep]), keep
    def pred(self):
        p = [[] for _ in range(self.n)]
        for v in range(self.n):
            for w in self.succ[v]: p[w].append(v)
        return p

def restricted(G, alive):
    """Return (succ, pred) restricted to vertex set alive (used for astar_scope='A')."""
    succ = [[w for w in G.succ[v] if w in alive] if v in alive else [] for v in range(G.n)]
    pred = [[] for _ in range(G.n)]
    for v in range(G.n):
        for w in succ[v]: pred[w].append(v)
    return succ, pred

def U_d(G, d):
    return {v for v in range(G.n) if G.pr[v] <= d and G.pr[v] % 2 == d % 2}

def A_star(G, d, player, succ, pred):
    """A*_d(G) = U_{k<=d, par(k)!=par(d)} { v in player-Attr(G, U_{k-1}(G)) : pr(v)=k }."""
    out = set()
    for k in range(0, d + 1):
        if k % 2 == d % 2: continue
        Uk1 = U_d(G, k - 1) if k >= 1 else set()
        At = attr(G.n, G.owner, succ, pred, player, Uk1)
        out |= {v for v in At if G.pr[v] == k}
    return out

def A_prime(G, d, A, Astar, player, succ, pred, aprime_base):
    base = {v for v in A if v not in Astar and v not in U_d(G, d) and (aprime_base == "all" or G.pr[v] < d)}
    return attr(G.n, G.owner, succ, pred, 1 - player, base)

def A_fun(G, d, aprime_base="lt", astar_scope="G", trace=False):
    """A(G,d) = intersection_k A^k(G,d). Returns the fixed-point set (may be empty)."""
    player = d % 2
    succ, pred = G.succ, G.pred()
    V = set(range(G.n))
    U = U_d(G, d)
    A = attr(G.n, G.owner, succ, pred, player, U)
    if astar_scope == "G":
        Astar = A_star(G, d, player, succ, pred)
    k = 0
    while True:
        if astar_scope == "A":
            s2, p2 = restricted(G, A); Astar = A_star(G, d, player, s2, p2) & A
        Ap = A_prime(G, d, A, Astar, player, succ, pred, aprime_base)
        X = (V - A) | Ap
        peel = attr(G.n, G.owner, succ, pred, 1 - player, X)
        if trace:
            print(f"  d={d} k={k}: U^k={sorted(U)} A^k={sorted(A)} A*={sorted(Astar)} base(A')={sorted(v for v in A if v not in Astar and v not in U_d(G,d) and (aprime_base=='all' or G.pr[v]<d))} A'={sorted(Ap)} peel={sorted(peel)}")
        Unew = U - peel
        if Unew == U:
            return A
        U = Unew
        A = attr(G.n, G.owner, succ, pred, player, U)
        k += 1

def algorithm(G, aprime_base="lt", astar_scope="G", trace=False, max_iter=None):
    """Algorithm 1. Returns (W_even, W_odd) as sets of ORIGINAL vertex ids, or raises Stuck."""
    orig = list(range(G.n)); W = [set(), set()]
    H = G
    it = 0
    while H.n > 0:
        it += 1
        if max_iter and it > max_iter: raise RuntimeError("iteration cap")
        dh = max(H.pr)                      # line 5: max priority of G
        pl = dh % 2                         # line 6
        opp = [p for p in H.pr if p % 2 != pl]
        dbar = max(opp) if opp else None    # line 7: max priority of the other player
        if trace: print(f"iter {it}: n={H.n} dhat={dh} player={pl} dbar={dbar}")
        rem = set()
        if dbar is not None:
            rem = A_fun(H, dbar, aprime_base, astar_scope, trace)   # line 8
        if rem:                                                     # lines 9-12
            W[1 - pl] |= {orig[v] for v in rem}
        else:
            rem = A_fun(H, dh, aprime_base, astar_scope, trace)     # line 14
            if not rem:
                raise Stuck(f"both A(G,{dbar}) and A(G,{dh}) empty on non-empty G (Lemma 3 fails)")
            W[pl] |= {orig[v] for v in rem}
        H, keep = H.sub(rem); orig = [orig[v] for v in keep]
    return W[0], W[1]

class Stuck(Exception): pass

def zielonka(G):
    """Min-parity Zielonka. Returns (W_even, W_odd) as sets of vertex ids of G."""
    def rec(alive):
        if not alive: return (set(), set())
        succ = [[w for w in G.succ[v] if w in alive] if v in alive else [] for v in range(G.n)]
        pred = [[] for _ in range(G.n)]
        for v in alive:
            for w in succ[v]: pred[w].append(v)
        p = min(G.pr[v] for v in alive); pl = p % 2
        T = {v for v in alive if G.pr[v] == p}
        A = attr(G.n, G.owner, succ, pred, pl, T)
        W = rec(alive - A)
        if not W[1 - pl]:
            return (alive, set()) if pl == 0 else (set(), alive)
        B = attr(G.n, G.owner, succ, pred, 1 - pl, W[1 - pl])
        W2 = rec(alive - B)
        res = [set(), set()]; res[1 - pl] = W2[1 - pl] | B; res[pl] = W2[pl]
        return tuple(res)
    return rec(set(range(G.n)))

def random_game(rng, n, maxpr, maxdeg):
    owner = [rng.randint(0, 1) for _ in range(n)]
    pr = [rng.randint(0, maxpr) for _ in range(n)]
    succ = []
    for v in range(n):
        others = [w for w in range(n) if w != v]
        k = rng.randint(1, min(maxdeg, len(others)))
        succ.append(rng.sample(others, k))
    return Game(owner, pr, succ)

def read_pg(path, minparity=True):
    """PGSolver format, MIN-parity as written unless minparity=False (then priorities are
    converted p -> M - p with M the smallest even number >= max priority, so that
    a max-parity file is turned into the equivalent min-parity game)."""
    nodes = {}
    for line in open(path):
        line = line.strip()
        if not line or line.startswith("parity"): continue
        line = line.rstrip(";")
        parts = line.split()
        v, p, o = int(parts[0]), int(parts[1]), int(parts[2])
        s = [int(x) for x in parts[3].split(",")]
        nodes[v] = (p, o, s)
    ids = sorted(nodes); assert ids == list(range(len(ids)))
    pr = [nodes[v][0] for v in ids]
    if not minparity:
        M = max(pr); M += M % 2
        pr = [M - p for p in pr]
    return Game([nodes[v][1] for v in ids], pr, [nodes[v][2] for v in ids])

def to_pg(G, maxparity=False):
    pr = G.pr
    if maxparity:
        M = max(pr); M += M % 2; pr = [M - p for p in pr]
    out = [f"parity {G.n - 1};"]
    for v in range(G.n):
        out.append(f"{v} {pr[v]} {G.owner[v]} {','.join(map(str, G.succ[v]))};")
    return "\n".join(out) + "\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pg"); ap.add_argument("--maxparity-file", action="store_true",
        help="the .pg file uses max-parity priorities; convert to min-parity before running")
    ap.add_argument("--search", type=int, default=0); ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--n", type=int, default=5); ap.add_argument("--maxpr", type=int, default=5)
    ap.add_argument("--maxdeg", type=int, default=3)
    ap.add_argument("--aprime", default="lt", choices=["lt", "all"])
    ap.add_argument("--astar", default="G", choices=["G", "A"])
    ap.add_argument("--trace", action="store_true")
    a = ap.parse_args()
    if a.pg:
        G = read_pg(a.pg, minparity=not a.maxparity_file)
        print("game (min-parity): owner", G.owner, "pr", G.pr, "succ", G.succ)
        z = zielonka(G); print("Zielonka  : W_even", sorted(z[0]), "W_odd", sorted(z[1]))
        try:
            r = algorithm(G, a.aprime, a.astar, a.trace, max_iter=10 * G.n + 10)
            print("Algorithm1: W_even", sorted(r[0]), "W_odd", sorted(r[1]), "(readings aprime=%s astar=%s)" % (a.aprime, a.astar))
            print("AGREE" if r == z else "DISAGREE")
        except Stuck as e:
            print("Algorithm1: STUCK:", e)
    if a.search:
        rng = random.Random(a.seed); bad = 0; stuck = 0; best = None
        for t in range(a.search):
            n = rng.randint(2, a.n)
            G = random_game(rng, n, a.maxpr, a.maxdeg)
            z = zielonka(G)
            try:
                r = algorithm(G, a.aprime, a.astar, max_iter=10 * n + 10)
                if r != z:
                    bad += 1
                    if best is None or (G.n, sum(map(len, G.succ))) < (best.n, sum(map(len, best.succ))): best = G
            except (Stuck, RuntimeError):
                stuck += 1
                if best is None or (G.n, sum(map(len, G.succ))) < (best.n, sum(map(len, best.succ))): best = G
        print(f"search: {a.search} games, wrong={bad}, stuck={stuck} (readings aprime={a.aprime} astar={a.astar})")
        if best is not None:
            print("smallest failing game (min-parity .pg):"); print(to_pg(best), end="")
            z = zielonka(best); print("Zielonka W_even", sorted(z[0]), "W_odd", sorted(z[1]))
            try:
                r = algorithm(best, a.aprime, a.astar, trace=True); print("Alg1 W_even", sorted(r[0]), "W_odd", sorted(r[1]))
            except Stuck as e: print("Alg1 STUCK:", e)

if __name__ == "__main__":
    main()
