# Draft RESULTS DE35 (Lead, 2026-10-29 18:46Z by date -u) — to CHECKER (after C97); lines 3-end are the entry

- DE35 (2026-10-29): N5-SF, the single-frame variant of N5 (SPEC S1-S5 + FIX 1-4 with S4a's opponent τ replaced by Odd's best reply
  σ̄(σ), S4b mirrored; L-NEW successors 32-33, docs/new/N5-SF-box54.md, packet docs/new/P-N5-SF-box55.md frozen at l-new 95a7a581;
  RESULTS R87 reduces its iteration count I to SBC, «polynomial iff SBC is») is a DEAD END at gauntlet step 2 (runtime growth, DATA):
  CONJECTURE SF-POLY (SBC, equivalently I, polynomial) is refuted on a family. Termination and correctness are not in question (R87:
  SF-TERM; Oink regions agree on every run below).
  Family dwN (L-RED successor 29, docs/red/R116-sf-exponential.md, claude/l-red 6e7acb3b, 2026-10-29T18:28:08Z): PGSolver's switch-best
  family switchbestexp N minus the N edges f_i → c (L-RED R115's fcN), plus one Even "repeater" u_i on each escape-chain edge
  v_i → r_(i+1) (i = 0..N−2), u_i → {r_(i+1), v_(i+1)}, with a low odd priority just above q's, all other priorities shifted up by
  2(N−1)+2 with parity kept; n = 26N + 9; generator experiments/red/sf/dlchain.py "N 1" (sha1 1abac5875f20ef15b0ca3734cdf9983fbc43ea44);
  pins experiments/red/sf/instances/dw_3..8.pg, sha1 e5f94c8003241720d5af97681b7912ca42ce5b8f (N = 3),
  eba759c1e811689c2b726f41b1a93a8b66a49c95 (4), c03e3e00578ad79bc2fe7224640f62fecb5e123c (5), 34ad93bc62d02a28d5fae86956ca7a717513bb4c (6),
  6b40922a795078895dfd10e84279c7f5e7c924bd (7), 5a7fe1cc2d782ae3c924e8275fad01110cfd70c4 (8). Start: SPEC S3 default.
  Counts (DATA): N5-SF iterations 134, 286, 590, 1,198, 2,414, 4,846 at N = 3..8 (= 19·2^N − 18 there), 9,697 at N = 9 (one engine;
  ratio 2.001); SBC_σ = 2^(N+1) − N − 2 at N = 3..9; LAM 0; no S4c fallback; the σ̄-flip word is a binary counter (h0 flips 2^N − 1
  times). Engines: L-RED's sf2.py and L-NEW's n5sf.py (claude/l-new 9faf17be) agree at N = 3..8; Oink zlk regions = N5-SF's and
  verify.py OK at N = 3..7 (L-RED).
  Independent reproduction (REFEREE-2 successor 20, docs/referee-2/R2-N5-DW.md, claude/referee-2 fef9dd1b, 2026-10-29T18:34:57Z): dwN
  built from the Lead's description only (no L-RED code), its own N5-SF (sf_check.run_sf on si.py): 134 / 286 / 590 / 1,198 / 2,414 at
  N = 3..7, SBC_σ 11 / 26 / 57 / 120 / 247, no fallbacks; Oink --zlk -v solution verified at every N, final regions = Oink's.
  Lead re-run (2026-10-29 18:46Z, trunk 0b3abd0f): dlchain.py regenerates dw_3..5 byte-identical to the pins; experiments/new/box54/sfrun.py (sha1
  cc3dfd73fb2d132610c7f95761300030d67d6e2a, n5sf.py sha1 1ea3bdc79d1ee0f4110c9a1b61e37f854210ad4f) gives SF iterations 134 / 286 / 590,
  SBC 11 / 26 / 57, LAM 0, no fallback, no cycle, and N5 41 / 47 / 55 at N = 3 / 4 / 5.
  Obstruction (READING, L-RED R116 §2 with L-NEW's Lemma LATENCY, docs/new/N5-FC-box59.md): F switches only along currently improving
  edges, so on fcN the lane learns of a new top bit one F-step before the escape chain, and the resulting cascade happens only at
  records (N² best-reply changes, cubic iterations); the repeater gives the escape chain that one-step lag at EVERY set of every bit and
  re-arms when bit i+1 resets, so every set cascades and the counter completes: N5-SF follows Even's classical switch-best run here (its
  σ-sequence lengths equal I^glo's, evseq --rule glo, N = 3..5; the counts equal I^glo's switchbestexp counts of L-NEW boxes 56/58) and
  meets BARRIERS B8 (docs/lit/BARRIERS.md: switch-best, Friedmann LMCS 7(3:19) 2011, Thm 8.4). The stale reply σ̄(σ) that protected N5-SF on switchbestexp (L-NEW box 57,
  Lemma STALE) is neutralised by the repeaters.
  Dead with it (lane conjectures, all refuted by dwN since SBC_G ≥ I/poly(n) by SF-RED-G): SF-POLY, SBC-QP / SF-QP (quasi-polynomial),
  I-CUBIC, SBCG-QUAD, PV_G (L-NEW docs/new/N5-PV-box60.md, N5-DEPTH-box61.md). Still true (refereed or lane-proved, as tools): R87
  (SF-TERM, DECOUPLE, ONE-PLAYER, SF-RED), SF-RED-G and SF-RED-R (lane), DEPTH-COUNT and DEPTH-BOUND (lane).
  Scope: plain N5 (SSI-GLOBAL) on dwN is linear in N on these points (41 / 47 / 55 / 62 / 68 at N = 3..7: REFEREE-2 dual_check.Runner
  on si.py; L-RED n5b --mode spec 41 / 47 / 55 / 62 at N = 3..6; Lead re-run 41 / 47 / 55), so DE35 says nothing about N5 or G-N5-TIME.
