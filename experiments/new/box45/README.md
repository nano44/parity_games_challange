# experiments/new/box45 (L-NEW successor 24): epochs as runs of N5 on the restricted game G'_E (docs/new/N5-EPR-box45.md)
DATA, not proof. Uses experiments/new/box43 (multi.rand_ckO) and box21 (n5x: SPEC N5 step, si.py Engine). Run from this directory.
- eprestrict.py STARTS SEED (--list FILE | --rand C LO HI GSEED | files): RESTRICT_E (i), (iv), REPRO, EP-0 checks per epoch; DIV, epochs
  and max length by |D|, G1PH. EPR_MUT=1: mutation control (u in D keeps only tau(u)).
- Runs 2026-10-26 05:47Z-05:50Z (date -u), outputs in out/:
  - out/lib41_k2.txt: `eprestrict.py 2 7 --list ../box41/lib41.txt` (S3 + 2 random starts; games with n > 64 skipped).
  - out/rand3000.txt: `eprestrict.py 4 8 --rand 3000 5 18 111`.
  - out/lib41_mut.txt: `EPR_MUT=1 eprestrict.py 0 7 --list ../box41/lib41.txt` (mutation bites: XI_V 2,788, REP_V 1,615).
  All three: XI_V, OPT_V, REP_V, EP0_V = 0 (unmutated), DIV = 0.
