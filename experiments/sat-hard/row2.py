#!/usr/bin/env python3
"""w(2,d) and s(2,d), convention E, for a range of d: least k with a separator (search from a lower bound).
Every SAT witness is re-verified exhaustively by verify2.maximal_2 (progress-measure-free). UNSAT steps are plain
CEGAR answers (no proof); proofs are produced separately for cells that are claimed.
Usage: row2.py DMIN DMAX"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import search, check, verify2
quiet = lambda s: None
lo_w = lo_s = 1
for d in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
    row = {}
    for mode in ("weak", "strong"):
        k = lo_w if mode == "weak" else lo_s
        t = time.time()
        while True:
            aut, _ = search.run(2, d, k, log=quiet, strong=(mode == "strong"))
            if aut:
                break
            k += 1
        ev, od = verify2.maximal_2(d, 0), verify2.maximal_2(d, 1)
        assert not check.violations(aut, ev, od if mode == "weak" else []), "witness fails exhaustive check"
        if mode == "strong":
            assert check.strong_ok(aut)
        row[mode] = (k, aut, time.time() - t)
        if mode == "weak": lo_w = k
        else: lo_s = k
    print(f"d={d}: w(2,d)={row['weak'][0]} s(2,d)={row['strong'][0]}  ({row['weak'][2]:.0f}s, {row['strong'][2]:.0f}s)"
          f"  weak witness {json.dumps(row['weak'][1]['delta'])}", flush=True)
