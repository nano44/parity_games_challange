#!/usr/bin/env python3
"""L-NEW N1 DISC-ANNEAL (docs/new/N1-disc-anneal.md): discount annealing gamma_j = 1 - 2^-j with warm-started
switch-all (Howard) strategy iteration for Even on the discounted game with Jurdzinski rewards +-n^pr(v); Odd's
counter-strategy by Odd's own switch-all policy iteration (one-player discounted game), warm-started.
Exact rational arithmetic (fractions.Fraction); deterministic games, so values of a pair are lasso sums.
Stop test after each phase (a certificate): win = sign of the discounted values; sigma and tau restricted to their regions
pass harness/verify.py check (closure, no losing cycle). Output: those regions and strategies.
Usage: anneal.py game.pg [out.sol] [--check] [--maxj J] [--j0 J0]   (--j0: ablation, start directly at gamma_J0) [--nocompress]
  prints: RESULT phases=J even_iters=E odd_iters=O per_phase=[...] secs=S [check: zielonka OK / strategies verified]"""
import sys, os, subprocess, time, tempfile
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, verify

VERBOSE = "--verbose" in sys.argv
COMPRESS = "--nocompress" not in sys.argv
FAST = "--fractions" not in sys.argv   # integer-scaled exact values (default) or plain Fractions
XCHECK = "--xcheck" in sys.argv   # merging same-parity neighbours; --nocompress keeps the input priorities
T0 = time.time()


def lasso_values(n, nxt, r, gamma):
    """x(v) = r(v) + gamma * x(nxt(v)) for the functional graph nxt; exact."""
    x = [None] * n
    state = [0] * n          # 0 new, 1 on stack, 2 done
    for s in range(n):
        if state[s]:
            continue
        path = []; v = s
        while state[v] == 0:
            state[v] = 1; path.append(v); v = nxt[v]
        if state[v] == 1:    # new cycle starting at v
            i = path.index(v); cyc = path[i:]
            L = len(cyc); S = Fraction(0); g = Fraction(1)
            for c in cyc:
                S += g * r[c]; g *= gamma
            x[cyc[0]] = S / (1 - g)
            for k in range(L - 1, 0, -1):          # x(c_k) = r(c_k) + gamma x(c_{k+1})
                c = cyc[k]; x[c] = r[c] + gamma * x[cyc[(k + 1) % L]]
            for c in cyc:
                state[c] = 2
            path = path[:i]
        for u in reversed(path):
            x[u] = r[u] + gamma * x[nxt[u]]; state[u] = 2
    return x


def lasso_values_int(n, nxt, r, a, b):
    """Exact values scaled to integers: returns X with X[v] = Q * x(v) for one common Q > 0 (gamma = a/b), where
    Q = b^n * prod over cycles C of (b^|C| - a^|C|). Same order as lasso_values (cross-checked by --xcheck)."""
    state = [0] * n; cycles = []; order = []
    for s in range(n):
        if state[s]:
            continue
        path = []; v = s
        while state[v] == 0:
            state[v] = 1; path.append(v); v = nxt[v]
        if state[v] == 1:                # the walk closed a new cycle
            i = path.index(v); cycles.append(path[i:]); path = path[:i]
        order.append(path)               # tree part: leads to this walk's cycle or to earlier walks
        for u in path:
            state[u] = 2
        if cycles:
            for c in cycles[-1]:
                state[c] = 2
    dens = [b ** len(C) - a ** len(C) for C in cycles]
    P = 1
    for d in dens:
        P *= d
    Q = b ** n * P
    X = [None] * n
    for C, d in zip(cycles, dens):
        L = len(C); S = 0                # S = sum_i a^i b^(L-1-i) r(c_i); x(c_0) = b * S / d ... (see below)
        for i, c in enumerate(C):
            S += a ** i * b ** (L - i) * r[c]
        # x(c_0) = sum_i gamma^i r_i / (1 - gamma^L) = sum_i a^i b^(L-i) r_i / (b^L - a^L)
        X[C[0]] = (Q // d) * S
        for k in range(L - 1, 0, -1):    # x(c_k) = r(c_k) + gamma x(c_{k+1})
            X[C[k]] = Q * r[C[k]] + a * X[C[(k + 1) % L]] // b
    for path in order:
        for u in reversed(path):
            X[u] = Q * r[u] + a * X[nxt[u]] // b
    return X


def solve(g, maxj=20000, j0=1):
    n = g.n
    succ = [sorted(set(s)) for s in g.succ]
    # compression (TARGET section 1): merge consecutive distinct priorities of equal parity, keep order and parity
    cp = {}
    # merge: a priority whose parity equals the previous kept one's takes the same value
    cur = None; prev = None
    for p in sorted(set(g.prio)):
        if prev is None:
            cur = p % 2
        elif p % 2 != prev % 2:
            cur += 1
        cp[p] = cur; prev = p
    cpr = [cp[g.prio[v]] for v in range(n)] if COMPRESS else list(g.prio)
    r = [n ** cpr[v] if cpr[v] % 2 == 0 else -(n ** cpr[v]) for v in range(n)]
    # best-reward start (L-SI's engine convention: max by (reward, index for even / -index for odd))
    def rk(w):
        rr = g.prio[w] if g.prio[w] % 2 == 0 else -g.prio[w]
        return (rr, w if rr % 2 == 0 else -w)
    sigma = [max(succ[v], key=rk) if g.owner[v] == 0 else None for v in range(n)]
    tau = [min(succ[v]) if g.owner[v] == 1 else None for v in range(n)]
    ev_it = od_it = 0; per = []
    for j in range(j0, maxj + 1):
        gamma = 1 - Fraction(1, 2 ** j); ph = 0
        while True:
            # Odd's best response to sigma: Odd switch-all on the one-player game, warm start tau
            while True:
                nxt = [sigma[v] if g.owner[v] == 0 else tau[v] for v in range(n)]
                x = lasso_values_int(n, nxt, r, 2 ** j - 1, 2 ** j) if FAST else lasso_values(n, nxt, r, gamma)
                if XCHECK:
                    xf = lasso_values(n, nxt, r, gamma); Qs = [x[v] / xf[v] for v in range(n) if xf[v] != 0]
                    assert all(q == Qs[0] for q in Qs) and all((x[v] == 0) == (xf[v] == 0) for v in range(n)), "xcheck"
                    assert all(x[v] == x[nxt[v]] * Fraction(2 ** j - 1, 2 ** j) + Qs[0] * r[v] for v in range(n)), "xcheck2"
                ch = False
                for v in range(n):
                    if g.owner[v] == 1:
                        b = min(succ[v], key=lambda w: (x[w], w))
                        if x[b] < x[tau[v]]:
                            tau[v] = b; ch = True
                if not ch:
                    break
                od_it += 1
            ch = False
            for v in range(n):
                if g.owner[v] == 0:
                    b = max(succ[v], key=lambda w: (x[w], -w))
                    if x[b] > x[sigma[v]]:
                        sigma[v] = b; ch = True
            if not ch:
                break
            ph += 1; ev_it += 1
        per.append(ph)
        if VERBOSE:
            print(f'j={j} ph={ph} ev={ev_it} od={od_it} t={time.time()-T0:.1f}', file=sys.stderr, flush=True)
        win = [0 if x[v] > 0 else 1 for v in range(n)]
        strat = [sigma[v] if g.owner[v] == 0 else tau[v] for v in range(n)]
        strat = [strat[v] if g.owner[v] == win[v] else None for v in range(n)]
        if not verify.check(g, win, strat):            # certificate: both strategies win their regions
            return (win, strat), j, ev_it, od_it, per
    raise RuntimeError("maxj reached")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    maxj = 20000
    if "--maxj" in sys.argv:
        maxj = int(sys.argv[sys.argv.index("--maxj") + 1]); args = [a for a in args if a != str(maxj)]
    g = pg.parse("".join(l for l in open(args[0]) if not l.lstrip().startswith("%"))); t0 = time.time()
    j0 = int(sys.argv[sys.argv.index("--j0") + 1]) if "--j0" in sys.argv else 1   # ablation: no annealing below j0
    if "--j0" in sys.argv: args = [a for a in args if a != str(j0)]
    sigma, J, E, O, per = solve(g, maxj, j0)
    secs = time.time() - t0
    sol = args[1] if len(args) > 1 else os.path.join(tempfile.gettempdir(), f"anneal_{os.getpid()}.sol")
    win, strat = sigma
    pg.write_sol(win, sol, strat)
    msg = f"RESULT n={g.n} phases={J} even_iters={E} odd_iters={O} max_phase={max(per)} nonzero={[p for p in per if p]} secs={secs:.2f}"
    if "--check" in sys.argv:
        import zielonka
        text = open(sol).read(); win = pg.read_sol(text, g.n)
        zw = zielonka.solve(g)
        errs = verify.check(g, win, verify.read_strategy(text, g.n))
        msg += " zielonka " + ("OK" if win == zw else "MISMATCH") + (" strategies verified" if not errs else " STRATEGY FAIL " + errs[0])
    print(msg)
