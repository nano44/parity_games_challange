# R2-N5-ODD-L2: word-diff of the P-N5-ODD line, revision L-2 (REFEREE-2 successor 24, Opus 5.5, D15)
- Object: docs/si/P-N5-ODD-line-L2.txt @ l-si 6370a35f0, sha1 ee114e2fe704a8ebf278910e6097a126afe94780 (re-hashed: match).
- Compared with L-1 (ab0baf919, sha1 3e25138b; R2-N5-ODD-L1.md, 301198b4). Fixes entry 5.
- Token diff (792 → 797 tokens): one insertion and nothing else, «(Corollary FUEL-COUNT) {+for every pair (y, z),+} the number N of fuel
  re-routes of (y, z) in F …» (REFEREE's ODD-L5).
- Symbol test: (y, z) is now bound in FUEL-COUNT, and HC uses the same pair. F stays bound by «for every W-run F of the run». No new free
  symbol.
- Correction (my side): my L-1 MATCHES (301198b4) passed FUEL-COUNT with (y, z) unbound. REFEREE caught it.

## Verdict
L-2 (ee114e2f): **MATCHES** (Opus 5.5, D15). No required change.
