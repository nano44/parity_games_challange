# R-P-IDEAL-RISE: REFEREE report on P-IDEAL-RISE (L-NEW successor 56, box 182)
REFEREE successor 24 (Opus 5.5, D15), 2026-11-06 (date -u in the commit). Independent: I did not open or list docs/referee-2/ on this
packet before this report was pushed.
- Object: claude/l-new 2f4d96de (an ancestor of origin/claude/l-new), detached worktree. Re-measured:
  - docs/new/P-IDEAL-RISE.md: sha1 573ef1171eec0f48aad974d221050681fc09ecc4, 220 lines;
  - line L-1: 7e4273a97993e6e67fb8b7c81d6e215ceaa7bbbe, 3,914 bytes;
  - risecheck.py 404df6de; risecheck.out 3685b69b; the four box182/cert/*.json pinned in check.sh.
- Premises checked on trunk c8fefddb.

## 0. Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §1 | Lemma KEY (a), (b), (c) | SIGN |
| §2 | Theorem PHIK-DESCENT; Corollary PHIK-T | SIGN |
| §3 | Theorem OPT-K (every d; the forcing-step Lemma) | SIGN |
| §4 | RISE-EQUIV (a), (b), (c); MOVE-RISE; Corollary MOVE-RISE-R | SIGN |
| §5 | C-PHX3 (= 22 at d = 3); C-PBG (β_2 = 8, β_3, β_4 exact rationals) | SIGN as CERTIFIED machine items: all four certificates RE-VERIFIED independently (§3) |
| §6 | DATA / READING / exclusions / TARGET diff | not to sign; check.sh block PASS; optional RI-P2 |
| line | L-1 | NOT YET: REQUIRED RI-L1 (the certificate «range» must say sup − inf over all genomes and states); optional RI-L2 |

## 1. Premise route
- Byte tests on trunk c8fefddb, each FOUND verbatim (1 hit): R105 ENC, MONO, XI-NEW, RISE; R110's 𝓛^R_d wording; R111 CASCADE.
- E-2 does not bear; moves(x) uses the E2c binder.
- No unlanded premise. P-IDEAL-ALIGN's facts are re-proved as KEY, correctly.
- Optional RI-P1. The packet says R105 ENC is «used in §4 only». §5's PBG features PV / ic / io are defined through «the integers
  (ENC)». The certificates do not depend on ENC: my re-check orders the path sets by the R104 set order and reproduces all three PBG
  bounds exactly. Either add §5 to ENC's use list, or define PV by the R104 order.

## 2. Proof checks
- KEY: SIGN.
  - (a) is ALIGN (a): distinct lower prefixes decide.
  - (b) is (F2) plus the least key under s_t.
  - (c): with equal W-targets, the gates decide.
- PHIK-DESCENT: SIGN. I re-derived every case.
  - Per-level facts: KP changes at level l iff the pair below flips (KEY (a)). A moving x lands aligned, with k_s = 1 if f = 0 and
    k_s = 0 if f = 1. CASCADE on 𝓛^R gives f_l = 1 ⇒ m_l ≥ 1 or f_(l−1) = 1.
  - Cases (i)-(v) of Δ_l are correct. In (iii) with both aligned, both sit on c_l and KEY (c) makes ord_l constant, so f_l = 0.
  - Downward induction with S_(l+1) ≤ max(0, 2w_(l+1)) = w_l − 1: every case bound is correct.
  - The least moving level gives S_0 ≤ −1.
  - Corollary arithmetic: Σ_x w = 2(2^(d+1) − 2) − 2d = 2^(d+2) − 2d − 4.
- OPT-K: SIGN.
  - Forcing step: A-sets are singletons except at p, and p takes KP_s(p) = 1 − s(p) by (F3).
  - The level-l pair flips: at l ≥ 1 by the gate choice γ_l(c_l) ≠ ord_l(s); at l = 0 by the gate sandwich.
  - So the level-(l + 1) pair becomes misaligned without moving, its order is constant (equal options), and nothing above changes
    (CASCADE).
  - Weights: W_l ≥ 2W_(l+1) + 1 gives W_l ≥ 2^(d−l) − 1.
  - The all-1 and all-0 k-states exist (built level by level by (F3)), so range ≥ Σ_x w_x.
  - Equality for Φ_K: min 0, max Σ w.
- RISE-EQUIV: SIGN. (a) ENC + MONO; (b) trivial; (c) XI-NEW + RISE give a rising option value at each step t − 1 ≤ T − 1.
- MOVE-RISE: SIGN. (F2) + ENC + (a).
- MOVE-RISE-R: SIGN. Each move of z is a rise of cv(z) at that step.
- §5 certificate logic: SIGN. With y ≥ 0, a decrease ≥ 1 per transition, and Σ_j a_j = Σ_j b_j = 1:
  - Σ y ≤ Σ y ΔΦ = Σ b Φ(hi) − Σ a Φ(lo) ≤ sup Φ − inf Φ;
  - the constant a cancels. Sound.
- What the certificates prove: a lower bound on sup_(G,s) Φ − inf_(G,s) Φ over ALL genomes of 𝓛^R_d and their states TOGETHER. The
  transitions and states come from different genomes (the PHX certificate uses 73 rows over many genomes). They do NOT bound the range
  on a single genome. §5 states it exactly so («sup_(G,s) Φ − inf_(G,s) Φ ≥ 22 (over G ∈ 𝓛^R_3 and their states)»). See RI-L1 for the
  line.

## 3. Independent re-verification of all four certificates (docs/referee/scratch/cert_check.py; logs rise_logs/)
- Written from §5's text only; risecheck.py's feature code was not read. Steps:
  - every genome must be in 𝓛^R_d and acyclic;
  - every transition is recomputed with MY simulator t3r_sim.py (R104 text) and must equal the stored «next»;
  - every feature is recomputed from §5's definitions. z is by the R104 set order. h is the longest Ξ-path count. PBG's PV / ic / io are
    positions in the R104-sorted list of path sets: no ENC, positions 0-based, and a constant shift cancels since Σa = Σb;
  - the full linear system is solved by exact Fraction Gaussian elimination over ALL rows, followed by an independent residual check.
- Results:
  | certificate | rows | features | rank / free | negative | residuals | bound (exact) |
  | --- | --- | --- | --- | --- | --- | --- |
  | cert_PHX_d3_s1793 | 73 | 121 | 73 / 0 | 0 | 0 | 22 |
  | cert_PBG_d2_s179 | 38 | 72 | 38 / 0 | 0 | 0 | 8 |
  | cert_PBG_d3_s1793 | 77 | 108 | 77 / 0 | 0 | 0 | 18.859681… = p/q, EQUAL to risecheck.out's p/q |
  | cert_PBG_d4_s1794 | 108 | 144 | 108 / 0 | 0 | 0 | 35.553557… = p/q, EQUAL to risecheck.out's p/q |
  - Every transition equals my simulator's step, and every genome is in 𝓛^R_d and acyclic.
  - Σa = Σb = 1. The multipliers are unique and nonnegative.
- Controls on the PHX certificate (all bite):
  - lo and hi swapped: 61 negative multipliers, bound −22;
  - one stored «next» replaced by its «s»: caught (bad 1, inconsistent);
  - one transition row dropped: inconsistent.
- So C-PHX3 and C-PBG are verified by a second, independent implementation of the simulator, the features and the exact LP check. That
  is CERTIFIED machine evidence, not a hand proof; the trusted base is two Python programs.

## 4. Independent checks of §1-§4 (docs/referee/scratch/rise_probe.py, my simulator, set order; rise_logs/probe.txt)
- PHIK-DESCENT from EVERY state: 150 random 𝓛^R_d genomes (d 1-5) and 186 corpus 𝓛^R genomes (N ≤ 10): 100,470 transitions, 0
  violations.
- T ≤ Φ_K(s_0) on the same runs: 0 violations.
- Φ_K range = 2^(d+2) − 2d − 4 (all-1 / all-0 states): 336 genomes, 0.
- OPT-K: my own τ(l, p), built from §3's text, for d = 1-7 (56 genomes): forcing step exact, 0 failures.
- RISE-EQUIV (a)-(c), MOVE-RISE, MOVE-RISE-R: 32,966 / 615 / 473 / 2,969 / 5,234 checks, 0 violations.
- Control: weights 2^(d−l) − 2 in place of w_l fail PHIK 7,329 times. (A first run of the probe reported 10 «violations». They were all
  odd-N corpus files, N = 1 or 3, not in 𝓛^R_d, which my in_LR helper did not reject without d. The probe now requires even N; the
  artifact is fixed and recorded here.)
- check.sh block «P-IDEAL-RISE» at 2f4d96de: PASS. risecheck.py regenerates risecheck.out identically.

## 5. Diff against TARGET.md
- Every statement is inside R104's IDEAL model, or about potentials on it. Nothing is polynomial (PHIK-T is exponential; RISE-EQUIV is
  an equivalence). Not M3, not M4, not a gauntlet step. G-N5-TIME OPEN. Agreed with §6.
- Optional RI-P2: §6's READING «against T^R(d) = 4, 8, 13» uses lane DATA for T^R(4) = 13 (AL-P1 pattern; T^R(3) = 8 is now R112).
  Label it.

## 6. Line L-1
- Shape: one line, 68 «(» / 68 «)», depth never negative, 0 «|», one « — », «2026» once.
- Definitions diffed against §0: KP_s, k_s, w_l, Φ_K, v_s, cv_s, R(x, k), M and moves(x) (E2c) all MATCH. Claims KEY, PHIK-DESCENT,
  OPT-K, RISE-EQUIV and MOVE-RISE MATCH their signed forms.
- DATA, tested against risecheck.py's counters (unit, set, and the statement's scope):
  - PHIK: one step from every state of the random genomes, plus every step of the stored-start corpus runs; phik_steps 14,384,
    phik_tight 1,772.
  - OPTK: 72 = 2 · (1 + … + 8) forcing genomes; the extreme states are checked on those genomes only, as the line says.
  - RISE_* / MOVERISE: 401 runs, 1,968 moves.
  - All MATCH.
- REQUIRED RI-L1 (scope of the certificate clause). The line says every such potential «has range at least 22 for PHX at d = 3 (so
  exactly 22, attained by Φ_K) and at least 8, 18.859… and 35.553… for PBG». In the same line, OPT-K's «its range on every genome of
  𝓛^R_d» means a per-genome range. The certificates bound only the joint sup − inf over all genomes of 𝓛^R_d and their states (§2
  above; §5 «sup_(G,s) Φ − inf_(G,s) Φ … (over G ∈ 𝓛^R_3 and their states)»).
  - Fix: «has sup minus inf over all genomes of 𝓛^R_d and their states at least 22 for PHX at d = 3 (so exactly 22, attained by Φ_K)
    and at least 8, 18.859… and 35.553… for PBG at d = 2, 3, 4».
- Optional RI-L2: «18.859…» and «35.553…» could carry «(exact rationals, printed by the tool)», as in §5.
- Source note: complete now; it must name the fixes file once one exists.
- Verdict: NOT YET (RI-L1).

## DONE / FINDINGS / NEEDS
- DONE: premise byte tests; every proof re-derived; all four certificates independently re-verified in exact arithmetic with my own
  simulator and features; own checks of §1-§4 with controls; check.sh block; TARGET diff; L-1 definitions / claims / DATA (unit, set
  and scope).
- FINDINGS:
  - Everything SIGNS. C-PHX3 = 22 and C-PBG 8 / 18.8597 / 35.5536 are re-verified exactly, with p/q equal to the tool's.
  - L-1 NOT YET: RI-L1, the certificate «range» is joint over genomes, not per genome.
  - Optional RI-L2, RI-P1, RI-P2.
- NEEDS: L-NEW, via the Lead: line L-2 with RI-L1.
