#!/usr/bin/env python3
"""L-SI box 16 (successor 11): DATA for docs/si/N5-2O-box16.md (fallbacks per phase with two terminals per honest class).
N5 trace: experiments/new/box21/n5x.py step() (read-only import; same loop as n5.py). Phase := maximal run with (lambda_Xi, tau)
constant. Q := Odd vertices of out-degree >= 2; for a cycle node c, U_c := lambda^{-1}(c), T_c := (Q n U_c) u {c}. Values are compared
in ARITHMETIC kappa (FBRED §0: kappa_c(x) = (signed weight of P(x), s_c * length); path weights are summed, so a vertex may
count twice, exactly as in the lemmas); inside a class the kappa order is the S1 order (M1kappa). g_1 < g_2 < ... are the in-phase fallbacks; for a
terminal q and a state t, the q-run of t is the maximal run of states of the phase with Xi(q) constant.
Checks (per phase; each counts its checks *_n and violations *_V):
  PFZ   (Lemma PFZ-q): t in a q-run Theta with at least j fallbacks of Theta before t; z in U_c \\ T_c: Xi_t(z) >= best value of a simple
        path of G_c^q from z to q with <= j edges, extended onto Xi_t(q).
  ROUTE (Lemma ROUTE-2): in a class with two terminals q, q' != c, at every state at least one of them is DIRECT (on its honest cycle,
        or its honest play reaches c before the other terminal).
  DIR   (Lemma DIR): t > g_{|U_c|-1}, q direct at t: Xi_t(q) in A_q (q (+) kopt_c(y), y in succ(q) n U_c; or (c, {}, l), 1 <= l < |U_c|).
  SAT   (Lemma SAT-2): t > g_{|U_c|-1}, at least |U_c| - 1 fallbacks of t's q-run before t: Xi_t(q') in V_q'(Xi(q)).
  NL    (Theorem FB-2T count): distinct (Xi(q), Xi(q')) pairs at fallbacks g_j, j >= |U_c|, vs |A_q|(|V_q'|max + w) + |A_q'|(|V_q|max + w).
Records FMAX (max fallbacks per phase), PAIRS (max distinct Q-value tuples at fallbacks of one phase), RHO (max Xi(Q)-changes per phase).
Usage: fb2o.py --rand COUNT NLO NHI SEED [K]   |   fb2o.py --list FILE     (only games with exactly two Odd choice vertices are run;
K = 2 by default; K = 1, 3 run the checks on those classes too)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import step, start_pair, Engine, dual, load
import pg

MUT = os.environ.get("MUT") == "1"   # mutation control: PFZ with j + 2 edges, DIR / SAT without the cycle values (must fail)
C = dict(games=0, phases=0, FMAX=0, PAIRS=0, RHO=0, PFZ_n=0, PFZ_V=0, ROUTE_n=0, ROUTE_V=0, DIR_n=0, DIR_V=0, SAT_n=0, SAT_V=0,
         NL_n=0, NL_V=0, NLMAX=0)
VIOL = []

def trace(g, cap=3000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None); rows = []
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append(dict(s=list(s), sb=list(sb), t=tuple(t), vs=vs, lam=tuple(x[0] for x in vs), fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    return E, rows

def nxt(g, row, v): return row["s"][v] if g.owner[v] == 0 else row["sb"][v]

def play(g, row, v):
    seen, out = set(), []
    while v not in seen: seen.add(v); out.append(v); v = nxt(g, row, v)
    return out, v                     # vertices up to the first repeat; v = first repeated vertex

def kap(E, c, val):
    """kappa_c(val) = (signed weight of P, s_c * length), s_c = +1 if c odd, -1 if even (FBRED §0); val has cycle node c."""
    assert val[0] == c
    return (E.weight(val[1]), (1 if E.par[c] == 1 else -1) * val[2])

def kwt(E, c, v):
    w = 0
    if E.rank[v] > E.rank[c]: w = E.bit[v] if E.par[v] == 0 else -E.bit[v]
    return (w, 1 if E.par[c] == 1 else -1)

def add(a, b): return (a[0] + b[0], a[1] + b[1])

def best_paths(E, g, c, verts, start, sink, base, maxe=None):
    """max over simple paths p of G[verts] from start to sink (Even: any edge inside; Odd: its single edge, if inside) with <= maxe
    edges of kwt_c(p minus sink) + base (ARITHMETIC kappa sum, as in kappa-PFZ / kopt). None if no path."""
    best = [None]
    def dfs(v, path, acc):
        if v == sink:
            val = add(acc, base)
            if best[0] is None or val > best[0]: best[0] = val
            return
        if maxe is not None and len(path) - 1 >= maxe: return
        for w in g.succ[v]:
            if w in verts and w not in path: dfs(w, path + [w], add(acc, kwt(E, c, v)))
    dfs(start, [start], (0, 0)); return best[0]

def phase(E, g, rows, a, b, Q, name):
    C["phases"] += 1
    fbs = [k for k in range(a, b) if rows[k]["fb"]]           # fallback transitions k -> k+1 inside the phase
    C["FMAX"] = max(C["FMAX"], len(fbs))
    lam = rows[a]["lam"]
    C["PAIRS"] = max(C["PAIRS"], len({tuple(rows[k]["vs"][q] for q in sorted(Q)) for k in fbs}))
    C["RHO"] = max(C["RHO"], sum(1 for k in range(a, b) for q in Q if rows[k]["vs"][q] != rows[k + 1]["vs"][q]))
    for c in set(lam):
        U = {v for v in range(g.n) if lam[v] == c}
        Tq = sorted(q for q in Q if q in U and q != c); T = set(Tq) | {c}
        if not Tq: continue
        w = len(U) - 1
        def run_fbs(q, t):            # fallbacks of t's q-run before t
            i = t
            while i > a and rows[i - 1]["vs"][q] == rows[t]["vs"][q]: i -= 1
            return [k for k in fbs if i <= k < t]
        # PFZ-q
        for q in Tq:
            Gq = U - (T - {q})
            for t in range(a, b + 1):
                j = len(run_fbs(q, t))
                if j == 0: continue
                for z in U - T:
                    bp = best_paths(E, g, c, Gq, z, q, kap(E, c, rows[t]["vs"][q]), j + 2 if MUT else j)
                    if bp is None: continue
                    C["PFZ_n"] += 1
                    if kap(E, c, rows[t]["vs"][z]) < bp: C["PFZ_V"] += 1; VIOL.append(("PFZ", name, t, q, z))
        hat = fbs[w - 1] if len(fbs) >= w and w >= 1 else (a - 1 if w == 0 else None)   # t > g_w  <=>  t > hat
        Gc = U - (T - {c})
        sc = 1 if E.par[c] == 1 else -1
        cyc = set() if MUT else {(0, sc * l) for l in range(1, len(U))}
        def Aset(q):
            vals = set()
            for y in g.succ[q]:
                if y in U and y != q:
                    bp = (0, 0) if y == c else best_paths(E, g, c, Gc, y, c, (0, 0))
                    if bp is not None: vals.add(add(kwt(E, c, q), bp))
            return vals | cyc
        def Vset(qp, q, vq):
            vals = set(); Gq = U - (T - {q})
            for y in g.succ[qp]:
                if y not in U or y == qp: continue
                if y == q: cand = [vq]
                elif y == c: cand = [(0, 0)]
                else:
                    cand = [x for x in (best_paths(E, g, c, Gc, y, c, (0, 0)), best_paths(E, g, c, Gq, y, q, vq)) if x is not None]
                if cand: vals.add(add(kwt(E, c, qp), max(cand)))
            return vals | cyc
        A = {q: Aset(q) for q in Tq}
        for t in range(a, b + 1):
            row = rows[t]; direct = {}
            for q in Tq:
                pl, rep = play(g, row, q)
                oncyc = (rep == q)
                firstT = next((v for v in pl[1:] if v in T), None)
                direct[q] = oncyc or firstT == c
            if len(Tq) == 2:
                C["ROUTE_n"] += 1
                if not (direct[Tq[0]] or direct[Tq[1]]): C["ROUTE_V"] += 1; VIOL.append(("ROUTE", name, t))
            if hat is None or t <= hat: continue
            for q in Tq:
                if direct[q]:
                    C["DIR_n"] += 1
                    if kap(E, c, row["vs"][q]) not in A[q]: C["DIR_V"] += 1; VIOL.append(("DIR", name, t, q))
            if len(Tq) == 2:
                for q, qp in ((Tq[0], Tq[1]), (Tq[1], Tq[0])):
                    if len(run_fbs(q, t)) >= w:
                        C["SAT_n"] += 1
                        if kap(E, c, row["vs"][qp]) not in Vset(qp, q, kap(E, c, row["vs"][q])): C["SAT_V"] += 1; VIOL.append(("SAT", name, t, q))
        if len(Tq) == 2 and hat is not None:
            late = [k for k in fbs if k > hat]
            if late:
                q, qp = Tq
                pairs = {(rows[k]["vs"][q], rows[k]["vs"][qp]) for k in late}
                vq = {kap(E, c, rows[k]["vs"][q]) for k in late}; vqp = {kap(E, c, rows[k]["vs"][qp]) for k in late}
                mv = lambda x, y: max(len(Vset(x, y, v)) for v in (vq if y == q else vqp))
                bound = len(A[q]) * (mv(qp, q) + w) + len(A[qp]) * (mv(q, qp) + w)
                C["NL_n"] += 1; C["NLMAX"] = max(C["NLMAX"], len(pairs))
                if len(pairs) > bound: C["NL_V"] += 1; VIOL.append(("NL", name, len(pairs), bound))

def check(g, name):
    Q = {v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2}
    E, rows = trace(g)
    C["games"] += 1
    a = 0
    for k in range(1, len(rows) + 1):
        if k == len(rows) or (rows[k]["lam"], rows[k]["t"]) != (rows[a]["lam"], rows[a]["t"]):
            phase(E, g, rows, a, k - 1, Q, name); a = k

def randgame(rng, lo, hi, K):
    while True:
        n = rng.randint(lo, hi); owner = [0] * n
        O = rng.sample(range(n), K)
        for v in O: owner[v] = 1
        for v in range(n):
            if v not in O and rng.random() < 0.2: owner[v] = 1
        succ = []
        for v in range(n):
            k = 1 if (owner[v] == 1 and v not in O) else (rng.choice((2, 2, 3)) if v in O else rng.choice((1, 2, 2, 3)))
            succ.append(sorted(set(rng.sample(range(n), min(n, k)))))
        g = pg.Game([rng.randrange(n + 3) for _ in range(n)], owner, succ)
        if sum(1 for v in range(n) if owner[v] == 1 and len(set(succ[v])) >= 2) == K: return g

def main():
    a = sys.argv[1:]
    if a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); K = int(a[5]) if len(a) > 5 else 2
        rng = random.Random(seed)
        for i in range(cnt): check(randgame(rng, lo, hi, K), f"rand{K} seed {seed} #{i}")
    else:
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > 40: continue
            if sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) != 2: continue
            check(g, f)
    print(" ".join(f"{k}={v}" for k, v in C.items()))
    for v in VIOL[:20]: print("VIOLATION", v)
    print("FB2O PASS" if not VIOL else "FB2O FAIL")

if __name__ == "__main__":
    main()
