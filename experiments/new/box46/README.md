# experiments/new/box46 (L-NEW successor 25): honest states, u-runs, REC for |D| = 1 (docs/new/N5-REC1-box46.md)
DATA, not proof. Uses experiments/new/box43 (multi.rand_ckO) and box21 (n5x: SPEC N5 step, si.py Engine). Run from this directory.
Samples: lib41 = `--list ../box41/lib41.txt` (games with n > 64 skipped), S3 + 2 random starts, seed 7; random = `--rand 3000 5 18 111`
(3,000 random 𝒞^kO, k 2-4, n 5-18), S3 + 4 random starts, seed 8.
- hon.py STARTS SEED (--list | --rand | files): Lemma HON (HON_V), the WM chain of its step 1 (WMC_V), D = ∅ ⇒ W-honest (D0NOTHON_V), fallbacks
  at W-honest states (FBH_V) and Lemma HON-FB (FBH_LAST_V, FBH_HON_V, FBH_FLAT_V), inside-gap fallbacks f_in (FBIN). out/hon_lib41_k2.txt,
  out/hon_rand3000.txt.
- dint.py STARTS SEED (...): D-intervals per phase, entries of {u}-intervals (ENT0 / ENTDIR = X_dir / ENTBIG = X_big / ENTSTART), REC-1 (a)
  (REC1R_V), N_0 against HON-0 (R0P_V) and REC-0 (R0_V). out/dint_lib41_k2.txt, out/dint_rand3000.txt.
- levels.py STARTS SEED (...) [--nmax N] [--budget B]: the permanent Ξ-level LEV_C in H_C at C-epoch ends (exact, simple-path DFS with a budget;
  UNK = budget hit); NORISE per |D_C| on fallback-free gaps (§4 (i): DEAD for |D| = 1), NORISE_FB on gaps with a fallback.
  out/levels_lib41_n34.txt (`--nmax 34 --budget 3000000`), out/levels_rand3000.txt (`--budget 1000000`).
- norise.py STARTS SEED --list FILE [--nmax N]: prints the |D| = 1 no-rise gaps (thclimb_n12_s11). out/norise_lib41_n20.txt.
- hon2.py STARTS SEED (...) [--nmax N] [--budget B]: LEV (G_τ frame) at every W-honest state; no-rise gaps split into fallback-free (HON step 1
  predicts 0), fallback at the first state (HON-FB), fallback inside (CONJECTURE HON-FF). out/hon2_lib41_n20.txt, out/hon2_lib41_n34.txt,
  out/hon2_rand3000.txt.
- fbin.py STARTS SEED --list FILE [--nmax N]: lists the gaps with an inside fallback and LEV at both ends. out/fbin_lib41_k2.txt.
