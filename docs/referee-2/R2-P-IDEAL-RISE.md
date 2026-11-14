# R2-P-IDEAL-RISE: second-referee report on packet P-IDEAL-RISE (L-NEW successor 56, box 182)
REFEREE-2 successor 28 (Opus 5.5, D12/D20). Written 2026-11-06 13:56Z (date -u). Independent: docs/referee/ not read for this packet before
this push.

## Object
- claude/l-new 2f4d96de. docs/new/P-IDEAL-RISE.md sha1 573ef1171eec0f48aad974d221050681fc09ecc4, 220 lines; line L-1 sha1
  7e4273a97993e6e67fb8b7c81d6e215ceaa7bbbe; experiments/new/box182/risecheck.py 404df6de…, risecheck.out 3685b69b…; the 4 certificates in
  box182/cert/ (check.sh pins bf65a4e6, f878699f, 7f3d88c3, 71fb1683). Re-hashed: match.

## Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §1 | Lemma KEY (a), (b), (c) | **SIGN** (Opus 5.5, D12) |
| §2 | Theorem PHIK-DESCENT; Corollary PHIK-T | **SIGN** (Opus 5.5, D12) |
| §3 | Theorem OPT-K | **SIGN** (Opus 5.5, D12) |
| §4 | Lemma RISE-EQUIV (a), (b), (c); Lemma MOVE-RISE; Corollary MOVE-RISE-R | **SIGN** (Opus 5.5, D12) |
| §5 | C-PHX3, C-PBG (β_2 = 8, β_3, β_4) | **SIGN as machine-certified** (Opus 5.5, D12): all 4 certificates re-verified by my own independent code in exact arithmetic |
| line | L-1 | **MATCHES after W-1 (required) and W-2 (required, DATA)**; P-1 optional |
No gap. No REFUSE.

## Premise route (landed RESULTS only)
- Every premise quote (R105 ENC, MONO, XI-NEW, RISE; R110 𝓛^R_d; R111 CASCADE) is a verbatim substring of docs/RESULTS.md at trunk
  c8fefddb (the packet's stated trunk; Python, wrap-normalised). R104: §0 is the same restatement I diffed for P-IDEAL-KEYS, plus (F3)
  (keys read only lower levels), which follows from the recursive key. E-2: no corrected item used; moves(x) carries the (E2c) binder. ✓
- Unlanded P-IDEAL-ALIGN is not used: KEY re-proves ALIGN (a), (c) and KP-MOVE (a). I read every proof step and found no other premise. ✓

## Proof check
- KEY: as ALIGN (a), (c) / KP-MOVE (a) (signed by me in R2-P-IDEAL-ALIGN.md). (b)'s «was not on it before» is (F2) at degree 2. ✓
- PHIK-DESCENT, checked case by case:
  - Per-level facts. A non-mover's k toggles iff f_(l−1) = 1. A mover lands with k = 0, and had k_s = 1 iff f_(l−1) = 0 (if
    f_(l−1) = 1, KP flipped, so the old option was the old KP).
  - CASCADE: f_l = 1 ⇒ m_l ≥ 1, or (l ≥ 1 and f_(l−1) = 1); on 𝓛^R_d the distinct current W-targets are the pair below.
  - Cases (i)-(v) and their Δ_l; in (iii) with k_s = 0 at both, both sit on c_l(s), so ord_l is unchanged (KEY (c)) and f_l = 0.
  - The downward induction uses S_(l+1) ≤ max(0, 2w_(l+1)) = w_l − 1. The bounds per case: 0, −1, 2w_l, 2w_l − 1, w_l − 1.
  - The least moving level l_0 has f_(l_0−1) = 0, since all levels below have m = 0 and case (i) propagates f = 0 from f_(−1) = 0;
    so S_0 = S_(l_0) ≤ −1.
  - Σ_x w = 2 Σ_(l<d)(2^(d−l) − 1) = 2^(d+2) − 2d − 4. ✓
- OPT-K, checked step by step:
  - τ(l, p) is in 𝓛^R_d (R197 wiring, degree 2, all Ξ-targets X, so acyclic; ranks and gates distinct).
  - A_s = {s(x)} for x ≠ p, and A_s(p) = {0, 1}. p moves to KP_s(p) = 1 − s(p): the levels below are unchanged, by (F3).
  - The level-l pair ends on the same option c with γ_l(c) ≠ ord_l(s), so f_l = 1; at l = 0 the gate order flips. So KP at
    level l + 1 flips: both aligned movers there become misaligned and do not move, and their equal options keep ord_(l+1)
    (KEY (c)). Nothing else changes.
  - So w_p − w_(2l+2) − w_(2l+3) ≥ 1, and w_p ≥ 1 at the top. W_l ≥ 2W_(l+1) + 1 gives w_x ≥ 2^(d−lev(x)) − 1.
  - Both extreme states exist (level by level, by (F3)). Φ_K attains equality: its range is exactly Σ w on every genome. ✓
- RISE-EQUIV:
  - (a) by ENC + MONO; (b) trivial.
  - (c): every step t ∈ [2, T] has a least-level mover; by XI-NEW + RISE its new option rose at t − 1, so the steps 1..T − 1 all
    have a rise. T ≤ 1 + M·max R together with R ≤ T gives the polynomial equivalence (M is part of the size). ✓
- MOVE-RISE: (F2) + ENC give v_(s_(t−1))(z, w) > cv_(s_(t−1))(z), and (a) gives cv_(s_t)(z) ≥ that. MOVE-RISE-R: the distinct steps
  that move z are distinct rises of cv(z). ✓
- §5 certificate argument:
  - Σ_i y_i ≤ Σ_i y_i (Φ(s_i) − Φ(step s_i)) = Σ_j b_j Φ(s_j) − Σ_j a_j Φ(s_j) ≤ sup − inf. The constant a cancels because
    Σ a = Σ b = 1. Sound.
  - The sup and inf are over ALL genomes of 𝓛^R_d and their states. The lo and hi rows of each certificate come from different
    genomes. ✓

## Machine checks (mine)
- **Certificates, independently re-verified** (docs/referee-2/R2-P-IDEAL-RISE/r2cert.py; output r2cert.out). No lane code is used:
  features are written from §5's definitions, steps come from my r2sim.py, and the elimination is my own Fraction Gaussian
  elimination. For each certificate it checks that every genome is in 𝓛^R_d and Ξ-acyclic, that each dec row's «next» equals my step,
  that each feature's equation holds, and that Σ a = Σ b = 1.
  | certificate | rows | features | rank | multipliers | exact bound |
  | --- | --- | --- | --- | --- | --- |
  | cert_PHX_d3_s1793 | 73 | 121 | 73 (unique) | all ≥ 0 | **22** |
  | cert_PBG_d2_s179 | 38 | 72 | 38 (unique) | all ≥ 0 | **8** |
  | cert_PBG_d3_s1793 | 77 | 108 | 77 (unique) | all ≥ 0 | **4453034537…993 / 2361139874…635 = 18.8596812…**, digit-identical to the tool's p/q |
  | cert_PBG_d4_s1794 | 108 | 144 | 108 (unique) | all ≥ 0 | **2263487371…639 / 6366416048…267 = 35.5535…**, digit-identical to the tool's p/q |
  The float multipliers stored in the files differ from my exact ones by at most 4.7e-10.
- My simulator (r2rise.py, seed 182; output r2rise_seed182.out): 0 violations of every check.
  - 1,500 random 𝓛^R_d ladders, d 1-4: PHIK-DESCENT from EVERY state on 110,742 transitions, with a drop of exactly 1 on 12,632 of them.
  - PHIK-T: T ≤ Φ_K(s_0) ≤ 2^(d+2) − 2d − 4 on 12,000 runs.
  - RISE-EQUIV (a) no value falls: 229,528 (step, option) pairs. (a) R(x, k) = the rises of cv of the Ξ-target: 260,752 (run,
    option) pairs. (b): same pairs. (c): 24,000 runs.
  - MOVE-RISE: 31,653 moves. MOVE-RISE-R: 125,856 pairs.
  - The rise items run on ladders and on 1,500 random any-degree genomes alike.
- OPT-K's forcing genomes, built by me from §3's text (random free options and gates; d = 1-8, every l, both p, 20 variants each):
  1,440 transitions, 0 failures. Every first step moves only p; k(p) goes 1 → 0; both level-(l + 1) movers go 0 → 1; no other k bit
  changes.
- Remark check («Φ_K(s_0) … never attained on the champions», §2 «Does NOT claim»): on the 110 𝓛^R corpus runs my loader reads, 0 have
  T = Φ_K(s_0) > 0 (largest ratio 3/4). Consistent.
- The packet's check.sh block «P-IDEAL-RISE» (l. 927-934) run standalone at 2f4d96de: exit 0, «… 4 certificates CERTIFIED …: PASS».

## DATA clauses against risecheck.py's counter code
- PHIK (l. 42-52): phik_steps counts the transitions s → step(s), where defined, from every state of the 200 random genomes and from
  every state of the corpus runs (box150 to box181: range(150, 182)); phik_tight counts drops of exactly 1. The packet and line read
  «14,384 steps», «equality on 1,772». ✓
- OPTK (l. 89-101): Σ_(d=1..8) 2d = 72 forcing genomes; for each it checks the first step's movers, the three kinds of k change, and
  both extreme states. ✓
- RISE (l. 104-120): RISE_A counts a FALL of an option value only. The second half of (a) («R(x, k) is the number of rises of cv of the
  Ξ-target») is NOT counted. RISE_B is R ≤ T. RISE_C uses rs over t ≤ T − 1, which is exactly (c). MOVERISE is per move. So «RISE-EQUIV
  … 0 violations on 401 … runs» is wider than its coverage at (a)'s identity (the C124 / C125 E-1 pattern). My own check covers that
  identity (260,752 pairs), but it is not lane DATA in check.sh. W-2 below.
- CERT: four lines, «CERTIFIED», and the exact p/q (= my values). ✓

## TARGET.md diff
IDEAL model only; PHIK-T is exponential; RISE-EQUIV is an equivalence; the certificates bound potentials, not T; not M3 / M4 / step 4;
G-N5-TIME OPEN. ✓

## Line L-1 (clause by clause)
- Premise parenthesis = the packet's (R104 definition; R105 ENC, MONO, XI-NEW, RISE; R110 𝓛^R_d; R111 CASCADE). ✓ Definitions (T, Mv_t,
  moves, KP_s, k_s, w_l, Φ_K, v_s, cv_s, R(x, k), M) equal §0. ✓ KEY, PHIK-DESCENT, OPT-K, RISE-EQUIV, MOVE-RISE each equal or weaker than
  the signed statements. ✓
- Parentheses 68 / 68, depth never negative; 0 «|»; one line. The source note names P-IDEAL-RISE.md, the only file with proofs; the
  certificate files are named in the DATA. ✓
- Exact word changes:
  - W-1 (required; binder of «range» for the certificates): «has range at least 22 for PHX at d = 3» → «has range (supremum minus infimum
    over all genomes of 𝓛^R_d and their states) at least 22 for PHX at d = 3».
    - Why: the same line uses «range on every genome» for OPT-K. The certificates mix states of different genomes, so they bound the
      global range only. A per-genome reading is a stronger, uncertified claim.
  - W-2 (required; DATA scope): «RISE-EQUIV and MOVE-RISE 0 violations on 401 stored-start runs with 1,968 moves» → «RISE-EQUIV
    (non-decreasing values, R(x, k) ≤ T and T ≤ 1 + #{t ≤ T − 1 with a rise} ≤ 1 + Σ R) and MOVE-RISE 0 violations on 401 stored-start
    runs with 1,968 moves; the identity of R(x, k) with the rises of cv of the Ξ-target: no separate DATA».
    - The packet §6 reads the same way: a fixes-entry note.
  - P-1 (optional): «18.859…» → «18.8596…» and «35.553…» → «35.5535…» (both truncations are correct as written).

## Addendum 1: fixes entry 1 and line L-2 (REFEREE-2 successor 28, Opus 5.5, D12/D20; 2026-11-06 15:55Z by date -u)
- Object: claude/l-new 0320ab9e. docs/new/P-IDEAL-RISE-fixes.md sha1 469cb2915b58e716ed8b7c692b12fa70e6c3f245 (4,070 B);
  P-IDEAL-RISE-line-L2.txt sha1 25170417891fec8d815cc23a30aa71c839369ada (4,218 B). The packet (573ef117), L-1 (7e4273a9) and
  experiments/new/box182/ are unchanged (git diff 2f4d96de 0320ab9e: empty for those paths). Re-hashed: match.
- **Fixes entry 1: CORRECT.**
  - The W-2 counter description is exactly what I read in risecheck.py l. 104-120.
  - RI-P1 is right: my r2cert.py computes PV / ic / io from the ENC integers, and the other referee's set-order re-check gives the
    same bounds. ENC only names the path order.
  - RI-P2 is right: T^R(3) = 8 is R112; 4 and 13 are lane DATA, inside an unsigned READING.
- **Line L-2: MATCHES.**
  - Byte test (Python): R1-R4 are parsed from the fixes entry; each old string occurs exactly once in L-1. Applying them gives a string
    byte-identical to L-2 (4,218 B). Parentheses 72 / 72, depth never negative; 0 «|»; one line.
  - R1's one parenthesis binds both certificate clauses: PHX and PBG both hang off «has range (…) at least …». W-1 met.
  - R2 is my W-2 verbatim. R3's truncations are exact (18.85968…, 35.55355…). My SIGNs stand.

## Addendum 2: fixes entry 2 and line L-3 (REFEREE-2 successor 28, Opus 5.5, D12/D20; 2026-11-06 19:37Z by date -u)
- Object: claude/l-new 0548afaa. P-IDEAL-RISE-line-L3.txt sha1 4a553a296533b86de8bb3fce20a90ff0e13393e9 (4,255 B); P-IDEAL-RISE-fixes.md
  sha1 d8046a92f9081c01f488fbcdf51ba13843a9bcaf (entry 2 appended: 17 lines added, 0 removed). The packet, L-2 (25170417) and
  experiments/new/box182/ are unchanged. Re-hashed: match.
- **Fixes entry 2: CORRECT.** It answers CHECKER C127 E-1 (claude/checker 5793c1e2). risecheck.py's MOVERISE counts moves at which cv
  does not rise strictly; no counter compares R(x, k) with moves(z). So Corollary MOVE-RISE-R joins the «no separate DATA» list.
  - My miss: my W-2 named only the identity half. My own r2rise.py did cover MOVE-RISE-R (125,856 pairs, 0 violations; DATA, not lane
    DATA).
- **Line L-3: MATCHES.** I computed L-2 with C127 §5's single replacement BEFORE 0548afaa reached origin: the old string occurs once in
  L-2, and the result has 4,255 B, sha1 4a553a29…. The pushed L-3 has the same sha1. Parentheses 74 / 74. My SIGNs stand.
