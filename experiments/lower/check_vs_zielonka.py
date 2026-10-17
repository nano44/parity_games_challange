#!/usr/bin/env python3
"""Task L1 step 2: the unfolded Büchi SLP (Lemma 2.3) and ANP's symmetric SLP (Transfer 2.4) against the harness
Zielonka on every game with <= n vertices (full enumeration where listed, else a fixed stride).
Usage: check_vs_zielonka.py [--quick]      (prints one line per (program, n, class) with the number of games and mismatches)"""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zielonka
from slp import buchi_unfold, anp_symmetric, eval_struct, cost
from games import iter_raw, count_raw, to_game, pack

QUICK = "--quick" in sys.argv


def run(label, prog, n, prios, owners_set, stride=1, chunk=20000):
    t0 = time.time()
    total, bad, first_bad = 0, 0, None
    buf = []

    def flush():
        nonlocal total, bad, first_bad
        if not buf:
            return
        S, off = pack(buf)
        out = eval_struct(prog, S)
        ref = np.concatenate([np.array(zielonka.solve(to_game(r))) == 0 for r in buf])
        neq = out != ref
        total += len(buf)
        if neq.any():
            k = int(np.searchsorted(off, np.nonzero(neq)[0][0], side="right") - 1)
            bad += int(sum(1 for i in range(len(buf)) if neq[off[i]:off[i + 1]].any()))
            if first_bad is None:
                first_bad = buf[k]
        buf.clear()

    for raw in iter_raw(n, prios, owners_set, stride=stride):
        buf.append(raw)
        if len(buf) >= chunk:
            flush()
    flush()
    cls = "one-player" if owners_set == (0,) else "two-player"
    cov = "ALL" if stride == 1 else f"every {stride}th of {count_raw(n, prios, owners_set)}"
    print(f"{label:18s} n={n} prios={list(prios)} {cls:10s} games={total:7d} ({cov}) mismatches={bad} cost={cost(prog)} [{time.time()-t0:.1f}s]"
          + (f" FIRST BAD {first_bad}" if first_bad else ""))
    return bad


fails = 0
# Lemma 2.3: unfolded Büchi, priorities {1,2}; programs for n must also solve all games with fewer vertices.
for n in (1, 2, 3, 4):
    prog = buchi_unfold(n)
    for k in range(1, n + 1):
        fails += run(f"buchi_unfold({n})", prog, k, (1, 2), (0,))
        stride = 1 if (k < 4 or QUICK is False and False) else 1
        if k == 4:
            fails += run(f"buchi_unfold({n})", prog, k, (1, 2), (0, 1), stride=(97 if QUICK else 13))
        else:
            fails += run(f"buchi_unfold({n})", prog, k, (1, 2), (0, 1))
# Transfer 2.4: ANP symmetric with S trees, priorities {0,1,2} (d = 2), and also {1,2} games (P_0 = ∅).
for n in (2, 3, 4):
    prog = anp_symmetric(n, 2)
    for k in range(1, n + 1):
        if k <= 3:
            fails += run(f"anp_symmetric({n},2)", prog, k, (0, 1, 2), (0, 1))
        else:
            fails += run(f"anp_symmetric({n},2)", prog, k, (0, 1, 2), (0, 1), stride=(997 if QUICK else 101))
            fails += run(f"anp_symmetric({n},2)", prog, k, (1, 2), (0,))
print("ALL AGREE" if fails == 0 else f"FAILURES: {fails}")
sys.exit(1 if fails else 0)
