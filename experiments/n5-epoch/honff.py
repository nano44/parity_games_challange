#!/usr/bin/env python3
"""Box 12 add-on (Lead 09:46Z / 10:06Z): own checker for L-NEW 25's CONJECTURE HON-FF and (validation only) IMM / IMM', written from
docs/new/N5-REC1-box46.md §0, §1, §1a, §4 (iii), (v) on claude/l-new 67a7b54d+ (L-NEW's imm.py / hon2.py / ffclimb.py NOT opened).
Engine and per-state data: census.py (n5b SPEC; Xi, W, lambda per state).
Definitions (§0):
  phase      (lambda_Xi, tau) constant (R38 (a));  f = in-phase S4c fallbacks.
  W-honest   Xi_k = W_k pointwise (W_k = valuation of sigma_k in G_tau, Odd fixed to tau).
  LEV(k)     largest j <= n-1 such that Xi_k(x) >= value(r) for every x and every simple path r of G_tau with <= j edges from x to a cycle
             node c of lambda (lambda(c) = c); value(r) = (c, P(r), |r|), P(r) = vertices of r before c more relevant than c; the order is
             SI.nvo (the VJ order used by n5b).  Computed as  min(n-1, L* - 1),  L* = the shortest simple path beating Xi_k at its source:
             to a cycle node c != lambda(x) it is the G_tau BFS distance to the nearest c with value(r) beating Xi_k(x) (the cycle-node
             reward decides; a BFS-shortest path is simple); to c = lambda(x) it is a depth-first search over simple paths with
             length-pruning (BFS distance to c), capped by --budget node expansions per state (cap hit: LEV = UNK, counted, never a pass).
Checks (each per phase):
  HON-FF   for consecutive W-honest states h < h' of the phase: LEV(h') >= min(LEV(h) + 1, n - 1). Gaps classified: fallback-free,
           fallback at h (HON-FB case), fallback strictly inside (at a state h < k < h').  CONJECTURE (L-NEW 25 §1a); a failure is reported.
  HON      (L-NEW-proved, unrefereed) #W-honest states <= f + 4n^2 - 3n;  HON-FB (iv): a fallback at a W-honest h gives h+1 W-honest and the
           last state of the phase.
  IMM      after a non-fallback in-phase step h -> h+1 from W-honest h: LEV(h+1) >= min(LEV(h)+1, n-1)   (DEAD, §4 (iii): validation)
  IMM'     the same when h+1 is not the last state of its phase                                    (DEAD, §4 (v): validation)
Usage: honff.py STARTS SEED (--list FILE | --rand C NLO NHI KLO KHI GSEED | FILE.pg[:START] ...) [--budget B] [--fb-only]
  --fb-only: compute LEV only at the two ends of gaps with an inside fallback (and skip IMM) -- cheap mode for big samples."""
import os
import random
import sys
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import census as C  # noqa: E402
from census import SpecSI, EVEN, ODD  # noqa: E402

BUDGET = 2 * 10 ** 6
PRUNE = os.environ.get("HONFF_NOPRUNE") != "1"   # HONFF_NOPRUNE=1: plain search (cross-check of the prune)
VIOL = []


class Unknown(Exception):
    pass


def gtau_succ(g, tau):
    return [list(g.succ[v]) if g.owner[v] == EVEN else [tau[v]] for v in range(g.n)]


def lev(g, SG, Xi, lam, tau, budget=None):
    """LEV(k) or None (UNK)."""
    n = g.n; succ = gtau_succ(g, tau)
    pred = [[] for _ in range(n)]
    for v in range(n):
        for w in succ[v]:
            pred[w].append(v)
    cyc = sorted({c for c in range(n) if lam[c] == c})
    dist = {}
    for c in cyc:                       # BFS distances to c in G_tau (reverse edges)
        d = [None] * n; d[c] = 0; q = deque([c])
        while q:
            y = q.popleft()
            for x in pred[y]:
                if d[x] is None:
                    d[x] = d[y] + 1; q.append(x)
        dist[c] = d
    best = n                            # L* candidate; LEV = min(n-1, best-1)
    for x in range(n):                  # other cycle nodes: reward decides, BFS-shortest path is simple
        for c in cyc:
            if c == lam[x] or dist[c][x] is None or dist[c][x] >= best:
                continue
            if SG.nvo(Xi[x], (c, frozenset(), 0)) < 0:      # value(r) beats Xi(x) iff c's reward beats lambda(x)'s
                best = dist[c][x]
    cnt = [0]; lim = budget or BUDGET
    for x in range(n):
        c = lam[x]
        if x == c or dist[c][x] is None or dist[c][x] >= best:
            continue
        rc = (g.prio[c], c)
        path = [x]; onp = {x}
        P0 = Xi[x][1]
        rel = sorted((w for w in range(n) if (g.prio[w], w) > rc), key=lambda w: (g.prio[w], w), reverse=True)

        def hopeless(P):
            """optimistic completion: unvisited even vertices in, unvisited odd vertices out (the maximum, in the VJ path-set order,
            of all sets that agree with P on the visited vertices); prune if even it is strictly worse than P0 at the first difference."""
            for w in rel:
                if w in onp:
                    inn = w in P
                else:
                    inn = g.prio[w] % 2 == 0
                if inn != (w in P0):
                    good = (g.prio[w] % 2 == 0) == inn
                    return not good
            return False

        def dfs(v, P, L):
            nonlocal best
            cnt[0] += 1
            if cnt[0] > lim:
                raise Unknown
            for w in succ[v]:
                if w == c:
                    if L + 1 < best and SG.nvo(Xi[x], (c, frozenset(P), L + 1)) < 0:
                        best = L + 1
                    continue
                if w in onp or dist[c][w] is None or L + 1 + dist[c][w] >= best:
                    continue
                onp.add(w)
                P2 = P | ({w} if (g.prio[w], w) > rc else set())
                if not (PRUNE and hopeless(P2)):
                    dfs(w, P2, L + 1)
                onp.discard(w)
        try:
            dfs(x, {x} if (g.prio[x], x) > rc else set(), 0)
        except Unknown:
            return None
    return min(n - 1, best - 1)


def check_run(g, name, states, fbs, S, fb_only=False, budget=None):
    n = g.n; SG = SpecSI(g)
    A = [C.state_info(g, SG, s, t) for s, t in states]
    key = [(A[k]["lam"], states[k][1]) for k in range(len(A))]
    S["runs"] += 1
    i = 0
    while i < len(A):
        j = i
        while j + 1 < len(A) and key[j + 1] == key[i]:
            j += 1
        phase(g, name, i, j, A, states, fbs, S, SG, fb_only, budget)
        i = j + 1


def phase(g, name, a, b, A, states, fbs, S, SG, fb_only, budget):
    n = g.n; tau = states[a][1]; lam = A[a]["lam"]; S["phases"] += 1
    where = f"{name} phase[{a},{b}]"
    H = [k for k in range(a, b + 1) if A[k]["Xi"] == A[k]["W"]]
    f = sum(fbs[t] for t in range(a, b))
    S["honest_states"] += len(H); S["max_honest_per_phase"] = max(S["max_honest_per_phase"], len(H))
    if len(H) > f + 4 * n * n - 3 * n:
        viol("HON", f"{where} |H|={len(H)} f={f}")
    for h in H:
        if h < b and fbs[h]:
            S["fb_at_honest"] += 1
            if not (A[h + 1]["Xi"] == A[h + 1]["W"] and h + 1 == b):
                viol("HON-FB", f"{where} h={h}")
    memo = {}

    def L(k):
        if k not in memo:
            memo[k] = lev(g, SG, A[k]["Xi"], lam, tau, budget)
        return memo[k]
    for h, h2 in zip(H, H[1:]):
        inside = [k for k in range(h + 1, h2) if fbs[k]]
        cls = "inside" if inside else ("at_h" if fbs[h] else "free")
        S[f"gaps_{cls}"] += 1
        if fb_only and cls != "inside":
            continue
        l0, l1 = L(h), L(h2)
        if l0 is None or l1 is None:
            S[f"gaps_{cls}_UNK"] += 1; continue
        if cls == "inside":
            S["inside_fallbacks"] += len(inside)
            print(f"INSIDE-GAP {where} gap {h}->{h2} fallbacks at {inside} LEV {l0}->{l1} n={n}", flush=True)
        if l1 < min(l0 + 1, n - 1):
            S[f"gaps_{cls}_norise"] += 1
            viol("HON-FF", f"{where} gap {h}->{h2} class={cls} fallbacks={inside} LEV {l0}->{l1}")
    if fb_only:
        return
    Hs = set(H)
    for h in H:
        if h < b and not fbs[h]:
            l0, l1 = L(h), L(h + 1)
            if l0 is None or l1 is None:
                S["imm_UNK"] += 1; continue
            S["imm_steps"] += 1
            if l1 < min(l0 + 1, n - 1):
                last = h + 1 == b
                S["IMM_fail"] += 1
                print(f"IMM-FAIL {where} h={h} LEV {l0}->{l1} h+1 last-in-phase={last} h+1 honest={h + 1 in Hs}", flush=True)
                if not last:
                    S["IMMprime_fail"] += 1
                    print(f"IMMPRIME-FAIL {where} h={h} LEV {l0}->{l1}", flush=True)


def viol(tag, where):
    VIOL.append(f"{tag} {where}"); print("VIOLATION", tag, where, flush=True)


def main():
    argv = sys.argv[1:]; budget = None; fb_only = "--fb-only" in argv
    argv = [x for x in argv if x != "--fb-only"]
    if "--budget" in argv:
        i = argv.index("--budget"); budget = int(argv[i + 1]); del argv[i:i + 2]
    starts, seed = int(argv[0]), int(argv[1]); rng = random.Random(seed)
    S = Counter()
    for name, g, st in C.games_from_args(argv[2:]):
        pairs = [("S3", None, None)]
        if st:
            s, t = C.full_start(g, *C.read_start(st, g)); pairs = [("start", s, t)]
        for r in range(starts):
            s, t = C.rand_start(g, rng); pairs.append((f"R{r}", s, t))
        for tag, s, t in pairs:
            try:
                states, fbs = C.run_states(g, s, t)
            except Exception as e:   # noqa: BLE001
                S["runs_failed"] += 1; print("RUNFAIL", name, tag, repr(e)[:200]); continue
            check_run(g, f"{name}[{tag}]", states, fbs, S, fb_only, budget)
    for k in sorted(S):
        print(f"{k}: {S[k]}")
    hv = [v for v in VIOL if not v.startswith(("IMM",))]
    print("RESULT", "FAIL" if hv else "OK", f"violations={len(hv)}")


if __name__ == "__main__":
    main()
