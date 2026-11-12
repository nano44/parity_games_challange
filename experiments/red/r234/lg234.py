#!/usr/bin/env python3
"""L-RED 66 R234: kill side of Lemma LAM-GAP (L-SI 51 box 101, claude/l-si 23d39400, docs/si/box101-lamgap.md §2).
INDEPENDENT one-player VJ engine (no code from own.py / si.py / lamgap101.py): vertex i has relevance rank i (larger = more relevant),
parity par[i]; reward(i) = +(i+1) if par[i] even else -(i+1). Value of v under sigma: (L, Pi, len): L = most relevant vertex on the cycle
of v's play, path = v .. first visit of L, Pi = vertices on the path before L more relevant than L, len = #vertices before L.
Order: reward(L); then z = most relevant of Pi_a ^ Pi_b: a better iff (z in Pi_a) == (z even); then len: shorter better iff L even.
Howard: every v whose current successor is not best moves to SOME best successor (ALL legal tie resolutions are branched); a v whose
current successor is best keeps it. Window = maximal run of states a..b with L_t(v) constant for EVERY vertex; its length b - a.
Ch = vertices with >= 2 successors. LAM-GAP: b - a <= |Ch| + 1.  Must-0: gapfail; sharpfail (b - a > |Ch|: L-RED 66 SHARP, R234 §1).  eqCh: windows with b - a = |Ch| >= 1.  Descriptive: max (b - a) per |Ch|, and tight
(windows with b - a = |Ch| + 1).  CTRL=1: bound |Ch| - 1 (must fire: windows of exactly |Ch| exist).
Modes: exh N (all graphs with out-degree >= 1 on N vertices, all parity vectors, all starts) | rnd SEED COUNT NMAX | climb SEED N ITERS"""
import sys, os, random, itertools
CTRL = os.environ.get("CTRL") == "1"
def val(v, sig, par):
    pos = {}; path = []
    while v not in pos: pos[v] = len(path); path.append(v); v = sig[v]
    L = max(path[pos[v]:]); i = path.index(L)
    return (L, frozenset(u for u in path[:i] if u > L), i)
def better(a, b, par):            # True iff a strictly better than b for Even
    if a[0] != b[0]:
        ra = (a[0] + 1) * (1 if par[a[0]] == 0 else -1); rb = (b[0] + 1) * (1 if par[b[0]] == 0 else -1); return ra > rb
    d = a[1] ^ b[1]
    if d: z = max(d); return (z in a[1]) == (par[z] == 0)
    if a[2] != b[2]: return (a[2] < b[2]) if par[a[0]] == 0 else (a[2] > b[2])
    return False
def runs_all(succ, par, start, cap=200000):
    """DFS over all legal tie resolutions; yields per run the max window b - a; returns (maxwin, maxT, nruns)."""
    n = len(succ); best = [0, 0, 0]; cnt = [0]
    stack = [(tuple(start), None, 0, 0)]       # (sigma, prev Lambda vector, current window length, T)
    while stack:
        sig, plam, w, T = stack.pop(); cnt[0] += 1
        if cnt[0] > cap: return best + [True]
        vals = [val(v, sig, par) for v in range(n)]; lam = tuple(x[0] for x in vals)
        w = w + 1 if plam == lam else 0
        if w > best[0]: best[0] = w
        if T > best[1]: best[1] = T
        choices = []
        for v in range(n):
            cur = vals[sig[v]]; bst = [succ[v][0]]
            for u in succ[v][1:]:
                if better(vals[u], vals[bst[0]], par): bst = [u]
                elif not better(vals[bst[0]], vals[u], par): bst.append(u)
            if better(vals[bst[0]], cur, par): choices.append(bst)
            else: choices.append([sig[v]])
        if all(len(c) == 1 and c[0] == sig[v] for v, c in enumerate(choices)): best[2] += 1; continue
        for ns in itertools.product(*choices): stack.append((ns, lam, w, T + 1))
    return best + [False]
def ch(succ): return sum(1 for s in succ if len(s) >= 2)
def check(succ, par, starts, tot, tag=""):
    c = ch(succ); bound = c - 1 if CTRL else c + 1; mw = 0
    for st in starts:
        w, T, nr, capped = runs_all(succ, par, st); mw = max(mw, w); tot["runs"] += nr; tot["capped"] += capped
        if w > bound:
            tot["gapfail"] += 1
            if tot["gapfail"] <= 3: print("GAPFAIL", tag, "succ", succ, "par", par, "start", st, "win", w, "Ch", c, flush=True)
        if w == c + 1: tot["tight"] += 1
        if w > c: tot["sharpfail"] += 1
        if w == c and c > 0: tot["eqCh"] += 1
        k = tot["maxwin"].get(c, 0); tot["maxwin"][c] = max(k, w); tot["maxT"] = max(tot["maxT"], T)
    return mw
def main():
    mode = sys.argv[1]; tot = dict(games=0, runs=0, gapfail=0, sharpfail=0, eqCh=0, tight=0, capped=0, maxT=0, maxwin={})
    if mode == "exh":
        n = int(sys.argv[2]); subs = [list(s) for k in range(1, n + 1) for s in itertools.combinations(range(n), k)]
        for succ in itertools.product(subs, repeat=n):
            succ = [list(s) for s in succ]
            for par in itertools.product((0, 1), repeat=n):
                tot["games"] += 1; check(succ, par, itertools.product(*succ), tot)
    elif mode == "rnd":
        rng = random.Random(int(sys.argv[2])); cnt = int(sys.argv[3]); nmax = int(sys.argv[4])
        for _ in range(cnt):
            n = rng.randint(2, nmax); succ = [sorted(rng.sample(range(n), min(n, rng.choice([1, 1, 2, 2, 3])))) for _ in range(n)]
            par = tuple(rng.randint(0, 1) for _ in range(n)); tot["games"] += 1
            check(succ, par, [[rng.choice(s) for s in succ] for _ in range(3)], tot)
    elif mode == "climb":
        rng = random.Random(int(sys.argv[2])); n = int(sys.argv[3]); it = int(sys.argv[4])
        def score(succ, par):
            t = dict(games=0, runs=0, gapfail=0, sharpfail=0, eqCh=0, tight=0, capped=0, maxT=0, maxwin={})
            starts = [[s[0] for s in succ], [s[-1] for s in succ]] + [[rng.choice(s) for s in succ] for _ in range(4)]
            mw = check(succ, par, starts, t); tot["gapfail"] += t["gapfail"]; tot["capped"] += t["capped"]
            return mw - (ch(succ) + 1), mw
        succ = [sorted(rng.sample(range(n), 2)) for _ in range(n)]; par = [rng.randint(0, 1) for _ in range(n)]
        cur = score(succ, par); bestv = cur
        for i in range(it):
            s2 = [list(s) for s in succ]; p2 = list(par); r = rng.random()
            if r < 0.6:
                v = rng.randrange(n); u = rng.randrange(n)
                if u in s2[v] and len(s2[v]) > 1: s2[v].remove(u)
                elif u not in s2[v]: s2[v] = sorted(s2[v] + [u])
            else: p2[rng.randrange(n)] ^= 1
            sc = score(s2, p2)
            if sc >= cur: succ, par, cur = s2, p2, sc
            if cur > bestv: bestv = cur; print("best", i, "excess", cur[0], "win", cur[1], "Ch", ch(succ), "succ", succ, "par", par, flush=True)
        tot["games"] = it
    print("TOTAL", tot, flush=True)
if __name__ == "__main__": main()
