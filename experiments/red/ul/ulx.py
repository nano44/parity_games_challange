#!/usr/bin/env python3
"""L-RED successor 22: exact checker for CONJECTURE UL_C (docs/si/N5-GCX-box21.md §4, l-si f984baa0 / 5b01a939), written from the frozen
text of N5-GCX §1 (run, class, D, A, gate regions, D-direct gates), §4 (C-interval, UL_C), §5 (offset) and N5-RUND §13 / §16 (forbidden at
level -1, U(S) = unforbid-switches), not from L-SI's gcx.py (reference only).
Definitions (frozen text):
- phase: maximal run of states with lambda_Xi and tau constant; fallback-free run S = maximal interval of a phase with no S4c fallback
  transition inside (every transition an in-phase S4a step).
- class c: U = lambda_Xi^{-1}(c). D_t = {Odd u : sigma-bar_t(u) != tau(u)}. A_t = {z in U : the (sigma_t, tau)-play of z meets no D_t vertex,
  z included}. DD_t = {u in D_t cap U : sigma-bar_t(u) in A_t and tau(u) in A_t}. Offset Delta_t(u) = M(Xi_t(tau u)) - M(Xi_t(sigma-bar_t u)),
  M = signed path weight of the Xi valuation.
- C-interval of class c: maximal [a, b] in S with, for a <= k < b: A_{k+1} subset of A_k, D_{k+1} cap U = D_k cap U, DD_{k+1} = DD_k and
  Delta_{k+1} = Delta_k on DD. A C-cut = a transition of S in no C-interval.
- (y, z) Even edge FORBIDDEN at f: z != a := sigma_f(y), COARSE(W_f(z)) > COARSE(W_f(a)), not Xi_f(z) > Xi_f(a); COARSE = (reward of the
  cycle node, signed weight of the path set) (level -1); W_f = valuation of the (sigma_f, tau)-play.
- U event (k', (y, z)): sigma_k'(y) != z = sigma_{k'+1}(y), k' -> k'+1 in S, and (y, z) forbidden at some f in [k' - n + 1, k' - 1] cap S.
- UL_C: for every C-interval [a, b] of class c and every U event (k', (y, z)) with y in U and a <= k' < b: k' - a < |U| - 1.
Reported per game: classes checked (all classes; flag BIG = |U| >= 3 and Q_c nonempty, the classes gcx.py checks), C-intervals, longest
C-interval relative to |U| (LEN_SLACK = max (b - a) - (|U| - 1)), U events inside / at cuts, IDX_SLACK = max over inside U events of
(k' - a) - (|U| - 1) (>= 0 is a UL_C VIOLATION), pure (D cap U = DD), |A_a|, lambda_W constant on the interval. MUT=1: threshold 0 (control).
Also SG (Xi non-decreasing in phase) and WM (W non-decreasing at in-phase S4a transitions) are counted, not assumed.
Usage: ulx.py --one GAME [START] [-v] | --list FILE [NMAX] (env RS random starts per game, seeded by the file name)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import step, start_pair, Engine, dual, load, readstart
C = Counter(); MX = {}; EX = []; VERB = "-v" in sys.argv; MUT = os.environ.get("MUT") == "1"

def mx(k, v, info=None):
    if k not in MX or v > MX[k][0]: MX[k] = (v, info)

def wplay(E, g, s, t):
    """valuation (cycle node, path mask, length) of the (s, t)-play from every vertex, computed directly."""
    n = g.n; nx = [s[v] if g.owner[v] == 0 else t[v] for v in range(n)]; val = [None] * n
    for v in range(n):
        if val[v] is not None: continue
        path, pos, x = [], {}, v
        while x not in pos and val[x] is None: pos[x] = len(path); path.append(x); x = nx[x]
        if val[x] is None:
            cyc = path[pos[x]:]; w = max(cyc, key=lambda u: E.rank[u]); val[w] = (w, 0, 0)
            i = cyc.index(w)
            for k in range(1, len(cyc)):
                u = cyc[(i - k) % len(cyc)]; val[u] = E.extend(u, val[nx[u]])
            path = path[:pos[x]]
        for u in reversed(path): val[u] = E.extend(u, val[nx[u]])
    return val, nx

def trace(g, start, cap=4000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); R = []
    while len(R) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t); W, wn = wplay(E, g, s, t)
        R.append(dict(s=list(s), t=list(t), vs=vs, sb=list(sb), W=W, wn=wn, fb=(r[4] if r else 0),
                      lam=tuple(x[0] for x in vs), lamW=tuple(x[0] for x in W)))
        if r is None: break
        s, t = list(r[0]), list(r[1])
    return E, R

def meets(nx, D, n):
    """vertices whose play under nx meets D (start included)."""
    res = [None] * n
    for v in range(n):
        path, x, seen = [], v, set()
        while res[x] is None and x not in seen and x not in D: seen.add(x); path.append(x); x = nx[x]
        hit = res[x] if res[x] is not None else (x in D)
        for u in path: res[u] = hit
        if x in D: res[x] = True
    return {v for v in range(n) if res[v]}

def coarse(E, val): return (E.rew[val[0]], E.weight(val[1]))

def forbidden(g, E, st):
    out = set()
    for y in range(g.n):
        if g.owner[y] != 0: continue
        a = st["s"][y]
        for z in set(g.succ[y]):
            if z != a and coarse(E, st["W"][z]) > coarse(E, st["W"][a]) and not E.key(st["vs"][z]) > E.key(st["vs"][a]): out.add((y, z))
    return out

def check(g, name, start=None):
    E, R = trace(g, start); n = g.n
    Q = {v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2}
    i = 0; C["games"] += 1
    while i < len(R):
        j = i
        while j + 1 < len(R) and (R[j + 1]["lam"], R[j + 1]["t"]) == (R[i]["lam"], R[i]["t"]): j += 1
        if j > i: phase(g, E, R, i, j, Q, name)
        i = j + 1

def phase(g, E, R, i, j, Q, name):
    n = g.n; C["phases"] += 1
    for k in range(i, j):
        for v in range(n):
            if E.key(R[k + 1]["vs"][v]) < E.key(R[k]["vs"][v]): C["SG_V"] += 1
            if not R[k]["fb"] and E.key(R[k + 1]["W"][v]) < E.key(R[k]["W"][v]): C["WM_V"] += 1
    runs, s = [], i
    for k in range(i, j):
        if R[k]["fb"]: runs.append((s, k)); s = k + 1
    runs.append((s, j))
    D = {k: {u for u in range(n) if g.owner[u] == 1 and R[k]["sb"][u] != R[k]["t"][u]} for k in range(i, j + 1)}
    MEET = {k: meets(R[k]["wn"], D[k], n) for k in range(i, j + 1)}
    cls = {}
    for v in range(n): cls.setdefault(R[i]["lam"][v], set()).add(v)
    for s0, e0 in runs:
        if e0 <= s0: continue
        C["runs"] += 1; mx("run_len", e0 - s0, (name, i, s0 - i, e0 - i))
        F = {k: forbidden(g, E, R[k]) for k in range(s0, e0 + 1)}
        UE = []                                              # all U events of S (any Even y)
        for k in range(s0, e0):
            for y in range(n):
                if g.owner[y] != 0: continue
                z = R[k + 1]["s"][y]
                if z != R[k]["s"][y] and any((y, z) in F[f] for f in range(max(s0, k - n + 1), k)): UE.append((k, y, z))
        C["U_events"] += len(UE)
        gst = {}                                              # GLOBAL C-intervals (UL_G, §5): every class at once; threshold n - 1
        for k in range(s0, e0 + 1):
            A = set(range(n)) - MEET[k]; DD = {}
            for u in D[k]:
                cu = R[k]["lam"][u]
                if R[k]["sb"][u] in A and R[k]["t"][u] in A and R[k]["lam"][R[k]["sb"][u]] == cu and R[k]["lam"][R[k]["t"][u]] == cu:
                    DD[u] = E.weight(R[k]["vs"][R[k]["t"][u]][1]) - E.weight(R[k]["vs"][R[k]["sb"][u]][1])
            gst[k] = (A, D[k], DD)
        a = s0
        for k in range(s0, e0 + 1):
            ok = k < e0 and gst[k + 1][0] <= gst[k][0] and gst[k + 1][1] == gst[k][1] and gst[k + 1][2] == gst[k][2]
            if MUT and k < e0: ok = True
            if not ok:
                lw = all(R[x]["lamW"] == R[a]["lamW"] for x in range(a, k + 1))
                ginfo = (name, "phase@%d" % i, "gcint=[%d,%d]" % (a - i, k - i), "n=%d" % n, "lamW_const" if lw else "lamW_moves")
                C["gcint"] += 1; mx("G_LEN_SLACK", (k - a) - (n - 1), ginfo)
                for (kk, y, z) in UE:
                    if a <= kk < k:
                        C["G_U_in"] += 1; mx("G_IDX_SLACK", (kk - a) - (n - 1), ginfo + ("k'=%d" % (kk - i), (y, z)))
                        if kk - a >= (0 if MUT else n - 1): C["UL_G_VIOL"] += 1; EX.append(("UL_G", ginfo, kk - i, (y, z)))
                a = k + 1
        for c, U in cls.items():
            big = len(U) >= 3 and bool((Q & U) - {c})
            st = {}
            for k in range(s0, e0 + 1):
                A = U - MEET[k]; DU = D[k] & U
                DD = {u for u in DU if R[k]["sb"][u] in A and R[k]["t"][u] in A}
                off = {u: E.weight(R[k]["vs"][R[k]["t"][u]][1]) - E.weight(R[k]["vs"][R[k]["sb"][u]][1]) for u in DD}
                st[k] = (A, DU, off)
            a = s0
            for k in range(s0, e0 + 1):
                ok = k < e0 and st[k + 1][0] <= st[k][0] and st[k + 1][1] == st[k][1] and st[k + 1][2] == st[k][2]
                if MUT and k < e0: ok = True
                if not ok:
                    cint(g, R, name, i, c, U, big, a, k, st, UE); a = k + 1

def cint(g, R, name, i, c, U, big, a, b, st, UE):
    C["cint"] += 1; L = b - a; thr = len(U) - 1
    pure = st[a][1] == set(st[a][2]); lamW = all(R[k]["lamW"] == R[a]["lamW"] for k in range(a, b + 1))
    info = (name, "phase@%d" % i, "c=%d" % c, "|U|=%d" % len(U), "cint=[%d,%d]" % (a - i, b - i), "pure" if pure else "impure",
            "|A_a|=%d" % len(st[a][0]), "|DcapU|=%d" % len(st[a][1]), "DD=%d" % len(st[a][2]), "lamW_const" if lamW else "lamW_moves",
            "BIG" if big else "small", "xgate=%d" % sum(1 for u in st[a][1] if R[a]["t"][u] not in U))
    mx("LEN_SLACK" + ("" if big else "_small"), L - thr, info)
    if L >= thr: C["cint_long" + ("" if big else "_small")] += 1
    ins = [(k, y, z) for (k, y, z) in UE if y in U and a <= k < b]
    C["U_in" + ("" if big else "_small")] += len(ins)
    for k, y, z in ins:
        idx = k - a; mx("IDX_SLACK" + ("" if big else "_small"), idx - thr, info + ("k'=%d" % (k - i), (y, z)))
        if idx >= (0 if MUT else thr):
            C["UL_C_VIOL" + ("" if big else "_small")] += 1
            if len(EX) < 20: EX.append(("UL_C", info, "k'=%d idx=%d" % (k - i, idx), (y, z)))
    if VERB and (ins or L >= thr):
        print("  CINT", " ".join(map(str, info)), "len", L, "U events", [(k - a, (y, z)) for k, y, z in ins])

def main():
    a = [x for x in sys.argv[1:] if x != "-v"]
    if a[0] == "--one":
        check(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        nmax = int(a[2]) if len(a) > 2 else 60
        for line in open(a[1]):
            f = line.strip()
            if not f or f.startswith("#"): continue
            g = load(os.path.join(ROOT, f))
            if g.n > nmax: continue
            check(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                check(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for k, (v, info) in sorted(MX.items()): print("MAX", k, v, info)
    for x in EX: print("EXAMPLE", x)

if __name__ == "__main__":
    main()
