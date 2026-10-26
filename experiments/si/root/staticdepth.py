#!/usr/bin/env python3
"""L-SI box 22 (successor 18): DATA for docs/si/N5-GCILEN-box22.md (Theorem STATIC-DEPTH, a partial GCI-LEN). Per phase and fallback-free run,
the maximal sub-intervals [a, b] on which sigma-bar is constant on every Odd vertex (R69 (d) STATIC: two fixed one-player games). At the end
state b: D_b := {Odd u : sigma-bar(u) != tau(u)}, A_b := the vertices whose W-play ((sigma, tau)) meets no D_b vertex; PURE_b: every u in D_b has
sigma-bar(u), tau(u) in A_b. CYC_CONST (H3): at every state of [a, b] the W-cycles and the honest cycles are the same cycles (vertex sequences), constant on [a, b].
Dependency graph H_b (cycle vertices are terminals, depth 0): Even v -> sigma_b(v), depth 1 + depth; Odd v not in D_b -> tau(v), same depth;
gate u in D_b -> tau(u) and sigma-bar(u), the max depth. ACYC_b: H_b has no cycle outside the terminals (PURE_b implies it).
Claims checked when ACYC_b and CYC_CONST hold:
  SETTLE_V  some v whose W-play or honest play (up to its cycle) at a state t in [a + d*(v), b] differs from the one at b;
  LEN_V     b - a > max d* (the interval is longer than the dependency depth);
  N1_V      b - a > n - 1.
Counts: intervals, by kind (pure_b, acyc_b, cyc_const), max length, max (length - (n - 1)), GEN_W failures (two different W-plays from one
vertex with equal W-valuation, among the interval's states). MUT=1: d*(v) - 1 in place of d*(v) (must bite).
GCI=1: the intervals are the global C-intervals instead (counts gci, gci_sbconst / gci_sbchg; the theorem is checked on gci_sbconst).
Usage: staticdepth.py --one GAME [START] | --list FILE [KMIN] (env RS, NMAX) | --rand COUNT NLO NHI SEED (env K)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import rows, phases, load, readstart, Dset, avoid
C = Counter(); MUT = os.environ.get("MUT") == "1"; EX = []

def walk(nx, v):
    """v's play under the successor map nx: (prefix up to the first repeated vertex, the cycle as a tuple starting at its entry)."""
    path, pos, x = [], {}, v
    while x not in pos: pos[x] = len(path); path.append(x); x = nx[x]
    return tuple(path[:pos[x]]), tuple(path[pos[x]:])

def cycset(nx, n):
    return frozenset(frozenset(walk(nx, v)[1]) for v in range(n)), {v for v in range(n) if v in walk(nx, v)[1]}

def depth(g, B, D, oncyc):
    n = g.n; memo = {}; state = {}
    def d(v):
        if v in oncyc: return 0
        if v in memo: return memo[v]
        if state.get(v) == 1: raise ValueError("cycle")
        state[v] = 1
        if g.owner[v] == 0: r = 1 + d(B["s"][v])
        elif v in D: r = max(d(B["t"][v]), d(B["sb"][v]))
        else: r = d(B["t"][v])
        state[v] = 2; memo[v] = r; return r
    return {v: d(v) for v in range(n)}

def run(g, name, start=None):
    E, R = rows(g, start); n = g.n
    for i, j in phases(R):
        rs, s = [], i
        for k in range(i, j):
            if R[k]["fb"]: rs.append((s, k)); s = k + 1
        rs.append((s, j))
        for s, e in rs:
            if os.environ.get("GCI") == "1":                 # global C-intervals (R91 §5 / P-N5-GCX §1): A (global) non-increasing, D constant,
                info = {}                                    # the D-direct gates and their offsets equal; theorem applies when sigma-bar is constant
                for k in range(s, e + 1):
                    Dk = Dset(g, R[k]); Ak = avoid(R[k]["wn"], Dk, n)
                    DD = {u: (E.weight(R[k]["vs"][R[k]["t"][u]][1]) - E.weight(R[k]["vs"][R[k]["sb"][u]][1])) for u in Dk
                          if R[k]["sb"][u] in Ak and R[k]["t"][u] in Ak}
                    info[k] = (frozenset(Dk), frozenset(Ak), DD)
                a = s
                for k in range(s, e + 1):
                    if k == e or not (info[k + 1][1] <= info[k][1] and info[k + 1][0] == info[k][0] and info[k + 1][2] == info[k][2]):
                        if k > a:
                            C["gci"] += 1; ln = k - a; C["gci_len_max"] = max(C["gci_len_max"], ln)
                            C["gci_len_minus_n1_max_plus1000"] = max(C["gci_len_minus_n1_max_plus1000"], 1000 + ln - (n - 1))
                            if ln > n - 1: C["GCI_N1_V"] += 1; EX.append(("GCI", name, a, k, n))
                            if all(R[m]["sb"] == R[a]["sb"] for m in range(a, k + 1)): C["gci_sbconst"] += 1; interval(g, E, R, a, k, n, name)
                            else:
                                C["gci_sbchg"] += 1; C["gci_sbchg_len_max"] = max(C["gci_sbchg_len_max"], ln)
                                nch = sum(R[m]["sb"] != R[m + 1]["sb"] for m in range(a, k))          # (G1): sigma-bar changes inside
                                C["gci_sbchg_count_max"] = max(C["gci_sbchg_count_max"], nch); C["gci_sbchg_count_sum"] += nch
                                pieces = [m for m in range(a, k) if R[m]["sb"] != R[m + 1]["sb"]]
                                bnd = [a] + [m + 1 for m in pieces] + [k + 1]
                                C["gci_piece_len_max"] = max(C["gci_piece_len_max"], max(bnd[x + 1] - bnd[x] - 1 for x in range(len(bnd) - 1)))
                                if nch >= 4: EX.append(("G1", name, a, k, ln, nch, n))
                        a = k + 1
                continue
            a = s
            while a < e:
                b = a
                while b < e and R[b + 1]["sb"] == R[a]["sb"]: b += 1
                if b > a: interval(g, E, R, a, b, n, name)
                a = b + 1 if b > a else a + 1

def interval(g, E, R, a, b, n, name):
    C["intervals"] += 1; B = R[b]; ln = b - a; C["len_max"] = max(C["len_max"], ln)
    C["len_minus_n1_max_plus1000"] = max(C["len_minus_n1_max_plus1000"], 1000 + ln - (n - 1))
    if ln > n - 1: C["N1_V"] += 1; EX.append(("N1", name, a, b, n))
    D = Dset(g, B); A = avoid(B["wn"], D, n)
    pure = all(B["sb"][u] in A and B["t"][u] in A for u in D); C["pure_b"] += pure
    cw = [frozenset(walk(R[t]["wn"], v)[1] for v in range(n)) for t in range(a, b + 1)]      # cycles as vertex sequences (rotation of
    ch = [frozenset(walk(R[t]["nxt"], v)[1] for v in range(n)) for t in range(a, b + 1)]     # the entry point normalised below)
    norm = lambda cs: frozenset(min(tuple(c[k:] + c[:k]) for k in range(len(c))) for c in cs)
    cw = [norm(x) for x in cw]; ch = [norm(x) for x in ch]
    cconst = all(x == cw[0] for x in cw) and all(x == cw[0] for x in ch); C["cyc_const"] += cconst   # (H3): common and constant
    oncyc = {v for c in cw[-1] for v in c}
    try: dd = depth(g, B, D, oncyc)
    except (ValueError, RecursionError):
        C["acyc_fail"] += 1
        if os.environ.get("VERB"): print("IV", name, a, b, "len", ln, "pure", pure, "cconst", cconst, "ACYC FAIL")
        return
    if os.environ.get("VERB"): print("IV", name, a, b, "len", ln, "pure", pure, "cconst", cconst, "dmax", max(dd.values()))
    C["acyc_b"] += 1
    if pure and not cconst: C["pure_but_cycles_move"] += 1
    if not cconst: return
    C["checked"] += 1; dm = max(dd.values()); C["dstar_max"] = max(C["dstar_max"], dm)
    if D:                                            # beyond R91 §3 (D = empty): intervals with gates
        C["checked_gates"] += 1; C["gates_len_max"] = max(C["gates_len_max"], ln)
        C["gates_len_minus_n1_max_plus1000"] = max(C["gates_len_minus_n1_max_plus1000"], 1000 + ln - (n - 1))
        if ln >= 10: EX.append(("GATES", name, a, b, ln, dm, n, len(D)))
    if ln > dm: C["LEN_V"] += 1; EX.append(("LEN", name, a, b, dm))
    C["slack_min_plus1000"] = min(C.get("slack_min_plus1000", 10 ** 6), 1000 + dm - ln)      # tightness: smallest max d* - length
    if dm == ln: C["tight"] += 1; EX.append(("TIGHT", name, a, b, ln, n)) if ln >= 10 else None
    seen = {}
    for t in range(a, b + 1):
        for v in range(n):
            wp = walk(R[t]["wn"], v)[0]
            key = (v, R[t]["W"][v])
            if seen.setdefault(key, wp) != wp: C["genw_fail"] += 1
    for v in range(n):
        if v in oncyc: continue
        d0 = dd[v] - (1 if MUT else 0); fb_w, fb_h = walk(B["wn"], v)[0], walk(B["nxt"], v)[0]
        for t in range(a + max(d0, 0), b + 1):
            if walk(R[t]["wn"], v)[0] != fb_w or walk(R[t]["nxt"], v)[0] != fb_h:
                C["SETTLE_V"] += 1; EX.append(("SETTLE", name, a, b, v, t, dd[v])); break

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    elif a[0] == "--rand":
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box43")); from multi import rand_ckO
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); q = 0; K = int(os.environ.get("K", "0"))
        while q < cnt:
            g = rand_ckO(rng, lo, hi, K or rng.choice((2, 2, 3, 4)))
            if g is None: continue
            q += 1
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})
            run(g, f"rand seed {seed} #{q}", None if q % 2 else st)
    else:
        kmin = int(a[2]) if len(a) > 2 else 1; ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            f = line.split()[0] if line.strip() and not line.startswith("#") else None
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin: continue
            run(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                run(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                   {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in [e for e in EX if e[0] != "TIGHT"][:6] + [e for e in EX if e[0] == "TIGHT"][:3] + sorted([e for e in EX if e[0] == "GATES"], key=lambda e: -e[4])[:3] + sorted([e for e in EX if e[0] == "G1"], key=lambda e: -e[5])[:3]: print("EXAMPLE", x)
    print("STATICDEPTH PASS" if not any(k in C for k in ("SETTLE_V", "LEN_V", "N1_V", "GCI_N1_V")) else "STATICDEPTH FAIL")

if __name__ == "__main__":
    main()
