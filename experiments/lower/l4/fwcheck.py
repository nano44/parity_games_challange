#!/usr/bin/env python3
"""L-LOWER 4: machine check of Lemma DOUBLE-EQ' and Lemma FROZEN-WINDOW (docs/lower/L4-tower.md) on runs of L^R_d genomes.
For every run: F(l) = number of steps at which the key order of pair l changes; level l >= 1 is DOUBLING iff F(l) = 2F(l-1) + 2.
DOUBLE-EQ' (doubling level j): Phi(0) = 2, Phi(T) = 0, Phi(t-1) = 0 at every b-step, at most one member of pair j moves per step,
the flips of pair j are exactly the steps moving a member of pair j, each member moves exactly once in every j-window.
FROZEN-WINDOW: levels l, l+1, l+2 doubling, every member of pair l+1 has Xi-targets {2l, 2l+1} => no state of the run has
xt(2l, s(2l)) = xt(2l+1, s(2l+1)). Also counts the instances meeting the hypothesis (vacuity control) and, for every (l+1)-window
in which pair l is frozen at a doubling pair l+1 targeting it, whether its two moves are at t and t+1 (STEP-ADJ).
Usage: fwcheck.py genome.json [...]  (env ALLSTARTS=1: every start for N <= 12; RANDOM=n: n random genomes per d in 4..8)"""
import sys, os, json, random, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l3'))
from sim import run
from trace import keys

def orders(G, s):
    k = keys(G, s); d = G["N"] // 2
    return [0 if k[2 * l] < k[2 * l + 1] else 1 for l in range(d)]

C = dict(runs=0, dbl_levels=0, eq_viol=0, fw_hyp=0, fw_viol=0, adj_windows=0, adj_viol=0)
def check(G, s0):
    N = G["N"]; d = N // 2; S = run(G, s0); T = len(S) - 1; C["runs"] += 1
    O = [orders(G, s) for s in S]
    F = [sum(O[t][l] != O[t - 1][l] for t in range(1, T + 1)) for l in range(d)]
    dbl = [l >= 1 and F[l] == 2 * F[l - 1] + 2 for l in range(d)]
    xt = lambda x, k: G["opts"][x][k][1]
    for j in range(1, d):
        if not dbl[j]: continue
        C["dbl_levels"] += 1; p, q = 2 * j, 2 * j + 1
        c = [O[t][j - 1] for t in range(T + 1)]            # c_j(s_t) = order of pair j-1
        phi = [(S[t][p] != c[t]) + (S[t][q] != c[t]) for t in range(T + 1)]
        bad = phi[0] != 2 or phi[T] != 0
        mv = [[x for x in (p, q) if S[t][x] != S[t - 1][x]] for t in range(T + 1)] if T else []
        for t in range(1, T + 1):
            if c[t] != c[t - 1] and phi[t - 1] != 0: bad = True
            if len(mv[t]) > 1: bad = True
            if (O[t][j] != O[t - 1][j]) != (len(mv[t]) == 1): bad = True
        cuts = [0] + [t for t in range(1, T + 1) if c[t] != c[t - 1]] + [T + 1]
        for a, b in zip(cuts, cuts[1:]):
            lo = max(a, 1)
            for x in (p, q):
                if sum(1 for t in range(lo, b) if x in mv[t]) != 1: bad = True
        C["eq_viol"] += bad
    for l in range(1, d - 1):
        tg = all(sorted([xt(x, 0), xt(x, 1)]) == [2 * l, 2 * l + 1] for x in (2 * l + 2, 2 * l + 3))
        frozen = lambda s: xt(2 * l, s[2 * l]) == xt(2 * l + 1, s[2 * l + 1])
        if dbl[l] and dbl[l + 1] and tg:
            C["dd_tg"] = C.get("dd_tg", 0) + 1
            # (l+1)-windows: between consecutive pair-l moves
            mvl = [t for t in range(1, T + 1) if S[t][2 * l] != S[t - 1][2 * l] or S[t][2 * l + 1] != S[t - 1][2 * l + 1]]
            for a, b in zip(mvl, mvl[1:] + [T + 1]):
                if frozen(S[a]):
                    C["adj_windows"] += 1
                    m1 = [t for t in range(a, b) if S[t][2*l+2] != S[t-1][2*l+2] or S[t][2*l+3] != S[t-1][2*l+3]]
                    if m1 != [a, a + 1]: C["adj_viol"] += 1
        if l + 2 <= d - 1 and dbl[l] and dbl[l + 1] and dbl[l + 2] and tg:
            C["fw_hyp"] += 1
            if any(frozen(s) for s in S): C["fw_viol"] += 1

def randgenome(d, rng):
    N = 2 * d; ranks = list(range(2 * N)); rng.shuffle(ranks)
    order = list(range(N)); rng.shuffle(order); pos = {v: i for i, v in enumerate(order)}
    opts = []; m = 0
    for x in range(N):
        l = x // 2; o = []
        for k in range(2):
            cand = [-1] + [y for y in range(N) if pos[y] < pos[x]]
            o.append([2 * (l - 1) + k if l else -1, rng.choice(cand), m]); m += 1
        opts.append(o)
    gate = [[rng.random() for _ in range(2)] for _ in range(N)]
    return {"N": N, "lev": [x // 2 for x in range(N)], "opts": opts, "gate": gate, "br": ranks,
            "bp": [rng.randint(0, 1) for _ in range(2 * N)], "start": [rng.randint(0, 1) for _ in range(N)]}

if __name__ == "__main__":
    for p in sys.argv[1:]:
        G = json.load(open(p)); N = G["N"]
        if os.environ.get("ALLSTARTS") and N <= 12:
            for s0 in itertools.product((0, 1), repeat=N): check(G, list(s0))
        else: check(G, G["start"])
    rng = random.Random(4)
    for _ in range(int(os.environ.get("RANDOM", "0"))):
        for d in range(4, 9):
            G = randgenome(d, rng); check(G, G["start"])
    # hypothesis-rich random family: pair L crossed (CROSS) or parallel (PAR), pairs L+1.. targeting the pair below
    for i in range(int(os.environ.get("RANDOMCROSS", "0"))):
        d = rng.choice([int(v) for v in os.environ.get("RCD", "4,5").split(",")]); G = randgenome(d, rng); L = rng.choice(range(1, d - 1))
        N = G["N"]; order = list(range(N)); rng.shuffle(order)
        tw = list(range(2 * L - 2, min(N, 2 * L + 4)))
        slots = sorted(i for i, v in enumerate(order) if v in tw)
        for i, v in zip(slots, tw): order[i] = v
        pos = {v: i for i, v in enumerate(order)}
        for x in range(N):
            if x in tw[2:]: continue
            for k in range(2): G["opts"][x][k][1] = rng.choice([-1] + [y for y in range(N) if pos[y] < pos[x]])
        for l in range(L, min(d, L + 2)):
            a, b = 2 * l - 2, 2 * l - 1
            par = rng.random() < 0.5 and l == L
            G["opts"][2 * l][0][1], G["opts"][2 * l][1][1] = (a, b) if rng.random() < .5 else (b, a)
            x0, x1 = G["opts"][2 * l][0][1], G["opts"][2 * l][1][1]
            G["opts"][2 * l + 1][0][1], G["opts"][2 * l + 1][1][1] = (x0, x1) if par else (x1, x0)
        # acyclicity: targets only lower levels for l >= L, others were acyclic by order; re-check
        def cyc():
            st = {}
            def dfs(v):
                if st.get(v) == 1: return True
                if st.get(v) == 2: return False
                st[v] = 1
                for k in range(2):
                    y = G["opts"][v][k][1]
                    if y >= 0 and dfs(y): return True
                st[v] = 2; return False
            return any(dfs(v) for v in range(G["N"]))
        if cyc(): continue
        for s0 in itertools.product((0, 1), repeat=G["N"]): check(G, list(s0))
    print(" ".join(f"{k} {v}" for k, v in C.items()))
