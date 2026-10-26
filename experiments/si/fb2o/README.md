# fb2o: DATA for docs/si/N5-2O-box16.md (L-SI successor 11, box 16)
- fb2o.py: per-phase checks of PFZ-q, ROUTE-2, DIR, SAT-2 and the FB-2T pair count, in arithmetic κ (κopt by brute force over simple paths;
  small n only). MUT=1 is a mutation control that must fail.
- climb2o.py: hill-climb on games with exactly two Odd choice vertices (OBJ=f: fallbacks in one phase; OBJ=hyp: DIR + SAT hypothesis hits).
- lib2o.txt: the 43 repository .pg files with exactly two Odd choice vertices and n ≤ 40 (found 2026-10-26 by a scan of experiments/ and docs/).
- logs/: lib2o.txt (PASS), climb_rand.txt, climb_fts.txt, climb_hyp.txt.
- tcsw.py: terminal changes per fallback-free run, (h_D), (h3_D), W-frame ROUTE-2 (DATA for docs/si/N5-2O-T-box16.md §3); logs tcsw_*.txt.
