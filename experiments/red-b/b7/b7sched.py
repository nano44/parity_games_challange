#!/usr/bin/env python3
"""L-RED-B B7: the SCHEDULE of RF's run on K^s_n in closed form, tested step by step against the real run.
Counter t = 1 .. 2^n - 1.  j(t) := the lowest set bit of t; for a bit i, cx_t(i) := the lowest set bit of t above i ("x" if
none).  CUR(t) := {(i, cx_t(i)) : bit i set in t}.  A closed gate outside CUR(t) is STALE.  Step t consists of these
iterations, in this order (one line = one iteration of RF; the vertices listed are exactly the vertices that switch):
  1. d(j, c) -> e(j, c) with c = cx_t(j)                               [close]
  2. R -> f(j, c), and in the same iteration g_j -> f(j, c) if j >= 2  [root and selector]
  3. for i = j - 1, j - 2, ..., 2:  g_i -> s(i, j)                     [skip moves, one iteration each]
  4. while a stale closed gate (i, c') QUALIFIES, the one latest in the gate list L opens: d(i, c') -> below(i, c')  [resets]
     (i, c') qualifies at t iff the bits 1..i-1 are all set in t and (bit i is set in t, or (i, cx_t(i)) comes BEFORE (i, c')
     in L, i.e. no pending gate of bit i lies after (i, c')).
The run ends after step 2^n - 1.  Total: 2 (2^n - 1) + (2^(n-1) - n) + (2^n - 1 - n) = 7 * 2^(n-1) - 2n - 3 iterations.
Counters (must be 0): sdiff = iterations whose set of switches differs from the schedule; ldiff = 1 if the lengths differ.
Control B7S_CTRL=1: the schedule opens the EARLIEST qualifying gate first (sdiff must fire for n >= 3).
Usage: b7sched.py NMIN NMAX"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
for p in (HERE, os.path.join(HERE, "..", "..", "..", "b7")):
    sys.path.insert(0, p)
sys.dont_write_bytecode = True
import rfc2
from si7 import Engine, root_first
CTRL = int(os.environ.get("B7S_CTRL", "0"))


def schedule(n):
    ctx = lambda i: rfc2.ctx(i, n)
    L = [(i, c) for i in range(n, 0, -1) for c in ctx(i)]; pos = {gc: k for k, gc in enumerate(L)}
    below = {L[k]: (f"C{L[k + 1][0]}.{L[k + 1][1]}" if k + 1 < len(L) else "R") for k in range(len(L))}
    closed = set(); out = []
    for t in range(1, 2 ** n):
        bit = lambda i: (t >> (i - 1)) & 1
        def cx(i):
            for j in range(i + 1, n + 1):
                if bit(j): return str(j)
            return "x"
        j = next(i for i in range(1, n + 1) if bit(i)); c = cx(j)
        out.append({f"d{j}.{c}": f"e{j}.{c}"}); closed.add((j, c))
        ev = {"R": f"f{j}.{c}"}
        if j >= 2: ev[f"g{j}"] = f"f{j}.{c}"
        out.append(ev)
        for i in range(j - 1, 1, -1):
            out.append({f"g{i}": f"s{i}.{j}"})
        cur = {(i, cx(i)) for i in range(1, n + 1) if bit(i)}
        def qualifies(i, c1):
            if not all(bit(k) for k in range(1, i)): return False
            return bool(bit(i)) or pos[(i, cx(i))] < pos[(i, c1)]
        while True:
            q = [gc for gc in closed if gc not in cur and qualifies(*gc)]
            if not q: break
            gc = (min if CTRL == 1 else max)(q, key=lambda z: pos[z])
            out.append({f"d{gc[0]}.{gc[1]}": below[gc]}); closed.discard(gc)
    return out


def real(n):
    g, s0 = rfc2.build(n, True); E = Engine(g); nm = g.names; prev = [None]; out = []
    def tr(its, sigma, val, tau, imp):
        if prev[0] is not None:
            out.append({nm[v]: nm[sigma[v]] for v in E.evens if sigma[v] != prev[0][v]})
        prev[0] = list(sigma)
    E.run(s0, root_first("high"), trace=tr)
    return out


if __name__ == "__main__":
    bad = 0
    for n in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
        S = schedule(n); Rn = real(n)
        sdiff = sum(1 for a, b in zip(S, Rn) if a != b); ldiff = int(len(S) != len(Rn))
        first = next((k for k, (a, b) in enumerate(zip(S, Rn)) if a != b), -1)
        print(f"B7 sched n {n}: schedule {len(S)} iterations, real {len(Rn)}, law {7 * 2 ** (n - 1) - 2 * n - 3} ctrl {CTRL}: sdiff {sdiff} ldiff {ldiff} first {first}", flush=True)
        bad += sdiff + ldiff
    sys.exit(1 if bad else 0)
