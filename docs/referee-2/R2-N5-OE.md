# R2-N5-OE: second-referee check of packet P-N5-OE (L-NEW box 32: σ̄(o) never outruns Even off crossings; J, ε and fallbacks per phase reduce to X and wakes). REFEREE-2 (successor 6), 2026-10-25 01:47Z (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-OE (Lead GO 01:44Z), pinned at trunk claude/vibrant-johnson-nxvvxo 361d18c (merged into my
branch as 8bae1c67). Object: docs/new/P-N5-OE-box32.md, sha1 adeccd898ad1e4de6532fc3a77a9d600d8a0bc16 (68 lines; checked at the pin and
on my tree).
Background read: P-N5-LP (sha1 d2c8121a) and its fixes file; my lane's R2-N5-LP (DF / DF′, Lemma U); RESULTS R19 (a), R22 (b) TC,
R25 (d) FB, (e) J1 and CAP-1 (with REFEREE's R-N5-FB §4.2 case split, a different packet's report); P-N5-FB §5 (J1's definition).
Independence: I have not read docs/referee/ for this packet (no OE report is on my tree). I did not run or import the lane's scripts
(oddlev.py, orise.py, lcheck.py, c1o_list.py); its instances are inputs only. I read c1o_list.py's source to explain a count difference.
Tools (docs/referee-2/R2-N5-OE/, own code on R2-N5-LP/lp_check.py and R2-N5-FB/fb_check.py): oe_check.py (every statement and every
intermediate fact of the proofs), oe_climb.py, run_all.sh, totals.py, logs/ (3 runs per library file + 4 random batches), logs1/ (1 run,
the canonical start, per library file), climb/. Every 𝒞^1O probe asserts exactly one Odd vertex with out-degree > 1.
Labels (D18 / L40): PROVED (L-NEW) is the packet's label. The §3 Reading is not to sign. Nothing here is a running-time bound, a
TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN: X and K per phase are OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §1 Lemma U-loc (any game, in a phase) | SIGN | — |
| §2 Lemma OE (𝒞^1O) | SIGN | N-OE-1: the "in particular" sentence is stronger than the proof by a level-⊥ tie move at o (0 seen; never used). N-OE-2: step 3's "honest play does not return to o" needs its one-line reason (supplied in §2). N-OE-3: phase-key transfer of the cited R22 / R25 items (valid, §4) |
| §3 Corollary OX (i)-(v) (𝒞^1O) | SIGN | (iv) uses Theorem FB on the packet's coarser phase key; FB's proof uses only λ_Ξ and τ constant (N-OE-3) |
| §3 Reading | not signed (as briefed) | Correct as a reading: with J ≤ X, R25's (J-poly) and the fallback count reduce to (X) |
| DATA lines | reproduced in substance | jcl_zcl_cu_n48: J 17 = X 17 exactly; O_k > E_k only at crossings; crossing-free ¬H1 changes 11 = packet's 11; other totals differ by file selection (§5) |
No statement is NOT SIGNED. There are no counterexamples and no gaps of substance.

## 1. Lemma U-loc: SIGN
- The proof is Lemma U's steps 2-4 (signed, R2-N5-LP §2) with the bound L used only on the prefix p_0 … p_{s−1} of v's H_{k+1}-path before
  its first visit of c = λ(v).
  - Step 2: c is its own cycle node at k and k+1 (λ is fixed in the phase), so Ξ_k(c) = Ξ_{k+1}(c) = (c, ∅, 0).
  - Step 3: every p_i has λ = c ≠ p_i, so a changed successor at p_i is a RELEVANT change (Even or Odd). By hypothesis its level is ≤ L,
    so (C2) gives COARSE_L(Ξ_k(new)) = COARSE_L(Ξ_k(old)).
  - Step 4: downward induction with (P2) and (C4). Nothing in it uses changes off the prefix. ✓
- Mechanical: I checked it at every (in-phase transition, v) with the SMALLEST admissible L (the max level of the relevant changes on
  that prefix, ⊥ if none).
  - That L was strictly below L_k in 332,186 of 373,394 checks, so the local form is a real strengthening of Lemma U.
  - I also asserted that every changed H-successor on the prefix is a relevant change. 0 failures.
  - Coverage includes 3,800 random general games (no 𝒞^1O restriction): 5,670 checks, 0 failures.

## 2. Lemma OE: SIGN
Setup (step 1).
- O_k ≠ ⊥ means a relevant σ̄(o) change x0 → x1, so λ(o) = c ≠ o at k and k+1 (phase). λ(x0) = λ(x1) = c by (P1) at k, at k+1 and the
  phase, so ℓ < ∞.
- CAP-1 (R25 (e), REFEREE's case split, signed): at an Odd vertex with λ ≠ itself, SPEC's σ̄ is a full Ξ-minimiser over its successors.
  OE uses it at state k (x0) and at state k+1 (x1). Both states have λ(o) ≠ o.
- The Lead's trap check: the full-minimiser property FAILS at own cycle nodes (420 non-minimiser states with λ(o) = o in my batch,
  3,177 such states). OE never uses it there: relevance excludes λ(o) = o. At λ(o) ≠ o it held at all 19,573 states in the batch and
  at every state of the climbs.

Step 2 (x1's H_{k+1}-path to c avoids o).
- The packet's argument is correct: a visit of o would give Ξ_{k+1}(x1) = Q ⊕ o ⊕ Ξ_{k+1}(x1), and the length grows.
- A direct reason: after o the play returns to x1, so the prefix would not be simple unless c = x1, in which case the prefix is empty.
- So the only changes on that prefix are relevant Even changes, each of level ≤ E_k. U-loc with L = E_k applies. ✓
- 2,502 checks (crossings included), 0 failures.

Step 3 (H1).
- N-OE-2: "x0's honest play does not return to o". The reason: H1 says o lies on no honest cycle. If x0's H_k-play visited o, o would lie
  on the H_k-cycle of o's play.
  - Equivalently (TC (i), statewise): if o is on its honest cycle with top c, then c's (σ, τ)-play follows that cycle up to o, so
    c ∈ R, not F.
- So x0's (σ_k, τ)-play equals its H_k-play and avoids o: x0 ∈ F_k = F_{k+1}.
- Its H_{k+1}-play agrees with its (σ_{k+1}, τ)-play up to the first visit of o, and that play never reaches o. So the H_{k+1}-play avoids
  o. (R19 (a)'s gloss in the packet is this one-line fact.)
- U-loc gives the COARSE_{E_k} values of x0 and x1 frozen. Their top difference ℓ > E_k is above E_k, and level and direction are functions
  of the COARSE_{E_k} values (as in Lemma HI's second bullet). So the strict order Ξ_k(x0) ◁ Ξ_k(x1) persists to k+1, against x1 being a
  minimiser at k+1. ✓
- Mechanical: 2,453 H1 checks (x0 ∉ R_k; x0's H_k- and H_{k+1}-plays avoid o; H1 constant off crossings), 0 failures.

Step 4 (¬H1).
- o is on its honest cycle with top c, so P(θ) = P(Ξ(x0)) = ∅. This holds at k, and with x1 at k+1 (¬H1 persists off a crossing).
- ℓ ≥ 0 puts u_ℓ in P(Ξ_k(x1)). U-loc (step 2) keeps it in P(Ξ_{k+1}(x1)) = ∅: a contradiction.
- ℓ = −1 forces E_k = ⊥, i.e. no relevant Even change. x0's prefix (along the old cycle, before o) is then unchanged, so both values are
  frozen and the strict order persists. ✓
- Mechanical: 49 ¬H1 checks in the batch (47 off crossings). The climb FIT=noh1 seeded from my df_cex.pg added 4,398 off-crossing ¬H1
  relevant σ̄(o) changes (all climbs: 4,598): P(Ξ_k(x0)) = P(Ξ_{k+1}(x1)) = ∅ at every one, 0 failures.

The statement itself (O_k ≤ E_k off crossings).
- Batch: 5,015 crossing-free in-phase transitions, 803 of them with a relevant σ̄(o) change, 0 failures.
- At crossings O_k > E_k happens (602 of 6,347), so the hypothesis R_k = R_{k+1} is needed and the lemma is not vacuous.
- N-OE-1: the proof shows O_k = ⊥ when E_k = ⊥. "σ̄(o) makes no relevant change" also excludes a tie move x0 → x1 with
  Ξ_k(x0) = Ξ_k(x1) (level ⊥), and the proof does not exclude that.
  - Not used anywhere: (i)-(iii) use the level.
  - 0 such tie moves in all my data (counter OE_in_particular_literal_fails absent from every log).
  - Read "makes no relevant change of level ≥ −1", or keep the sentence as DATA.

## 3. Corollary OX: SIGN
- (i) An Odd-only used level means E_k < L_k = O_k, so the transition is a crossing (OE). Distinct transitions, so ε ≤ X. Every ε
  transition was a crossing (602 in the batch, 279 in logs1). ✓
- (ii) J1 (P-N5-FB §5: b ≠ a and lev(Ξ_k a, Ξ_k b) > M_k, with a = σ̄_k(o), b = σ̄_{k+1}(o), the same lev as O_k).
  - λ(o) = o would make the transition tame (P-N5-LP Corollary LP′ step 3, signed), so the change is relevant.
  - E_k ≤ M_k because relevant Even switches go to gate targets (R15 (d)). So O_k > E_k: a crossing.
  - Every one of the 509 non-tame transitions (batch) was a crossing. Max J − X per phase = 0.
  - jcl_zcl_cu_n48 has J 17 = X 17, so (ii) is tight there. 22 phases had J = X > 0. ✓
- (iii) LP′ step 2's case split, with the σ̄(o) case absorbed into the crossing case: k′ ∈ [k, k′], and OE at k′ makes k′ a crossing.
  K counts transitions with a wake, at most one per rise. Each transition lies in at most two intervals [k, k′]. ✓ No failure; max ρ 14.
- (iv) Theorem FB is monotone in J, then (ii). ✓
- (v) Arithmetic: T_rel ≤ (n + 1)(ρ + 1)·n(n − 1) + ε ≤ (n + 1)(2f + 2X + K + 1)·n(n − 1) + X; then T ≤ (m − n + 1)(T_rel + 1).
  With f = O(n²(1 + X)) this gives O(m·n⁵·(1 + X + K)). ✓ No failure.

## 4. Citations and the phase key (N-OE-3)
- The packet's phase is (λ_Ξ, τ) constant, coarser than the key (λ_Ξ, λ_U, τ) under which R21-R23 and R25 are stated.
- How each cited item transfers:
  - R25 Theorem FB: P-N5-FB line 47 says "Only λ_Ξ and τ constant is used", and the proof (tame runs ≤ J + 1, blocks) uses nothing else.
    It transfers.
  - J1, CAP-1: statewise or (λ_Ξ, τ)-only. They transfer.
  - R22 TC (i) "H1 ⟺ λ_Ξ(o) ∈ F": statewise (proof in §2, step 3). It transfers.
  - R19 (a): used only as the one-line fact in §2, step 3.
- My checker uses the packet's coarse phase throughout, so every check above is on the stronger reading.

## 5. Data (DATA, not proof)
| batch | runs | in-phase transitions | key counts | violations |
| --- | --- | --- | --- | --- |
| random general, n 4-12 / 12-20 (seeds 941, 942) | 3,800 | — | U-loc 5,670 | 0 |
| random 𝒞^1O, n 6-14 / 14-24 (seeds 943, 944) | 3,800 | — | U-loc 16,092; OE 890; S4 13; J 2 | 0 |
| library, 3 runs per file (234 files; S3 start + 2 random) | 702 | 10,162 | U-loc 351,632; CAP-1 12,468; OE 4,125 (748 with a σ̄(o) change); crossings with O > E 598; J 507; f 979 | 0 |
| library, canonical start only (logs1) | 234 | 5,603 | O > E 279, all crossings; crossing-free relevant σ̄(o) changes 447 (436 H1, 11 ¬H1); non-tame 235, all crossings | 0 |
| climbs (oe_climb.py: FIT=noh1 from nowake_cex_n32 and from df_cex.pg; FIT=off from x31_rx32; FIT=jx from jcl_zcl_cu_n48) | 27,200 (6,000 + 12,000 + 6,000 + 3,200) | — | off-crossing relevant σ̄(o) changes 72,414 (¬H1: 4,598); non-tame transitions 30,002, all crossings; jx never above J − X = 0 | 0 |
- Packet instances: jcl_zcl_cu_n48 (sha1 53c69d2d) J 17, X 17, ε 17. nowake_cex_n32 (3a56e3fb) K 1, J 0. x31_rx32 (4fe9ec0e) J 2,
  X 22. 0 violations.
- Count differences against the packet's DATA (217 O > E, 175 non-tame, 431 + 11 crossing-free changes on its 220-file LIB, against
  my 279 / 235 / 436 + 11 on 234 files).
  - c1o_list.py (read, not run) tests len(succ) > 1 without deduplication and lists the trunk of its own time. My filter deduplicates
    successors and runs on 361d18c.
  - Same direction, same zero-exception statements, same 11 ¬H1 cases. Not a disagreement.
- Thin spots:
  - The ℓ = −1 sub-case of OE step 4 is never the contradiction branch (the lemma holds, so no branch is reached). My data checks only
    the intermediate facts.
  - Wakes are rare: K = 1 in all data (nowake_cex_n32), so (iii)'s wake term is barely exercised.
  - The jx climb (n 48, 800 steps) never left J − X = 0 (score 17 = the seed's J). noh1_a (seed nowake_cex_n32) found no ¬H1 change.

## Signature
REFEREE-2 (successor 6), Opus 5.5 (D15), 2026-10-25: Lemma U-loc SIGN; Lemma OE SIGN (notes N-OE-1, N-OE-2, N-OE-3; no gap of
substance); Corollary OX (i)-(v) SIGN. After two signatures (D18/L40) these become PROVED (L-NEW successor 12; REFEREE-2, and REFEREE if
it signs): U-loc on every game inside a phase; OE and OX on 𝒞^1O. OPEN: X and K per phase; G-N5-TIME.

## §C. Comparison with REFEREE (R-N5-OE, referee 5e98e33 + stamp fix 696b08c; trunk 1d35e8e). Written 2026-10-25 02:06Z onward by date -u
Order: my report (ca6e5bd1) was pushed before I opened docs/referee/R-N5-OE.md (Lead 02:06Z). REFEREE did not read mine.
### C.1 Verdicts
| statement | REFEREE | REFEREE-2 | agree? |
| --- | --- | --- | --- |
| U-loc | SIGNED | SIGN | yes |
| Lemma OE | SIGNED WITH GAPS OE-1, OE-2 (closed), OE-3 | SIGN, notes N-OE-1..3 | yes on substance; the labels differ only because REFEREE files wording items as gaps |
| Corollary OX (i)-(v) | SIGNED (OX-1 wording) | SIGN | yes |
| Reading | not signed (note 3.6) | not signed | yes |
No disagreement of substance. Both reports find no counterexample. Both reproduce J 17 = X 17 on jcl_zcl_cu_n48.
### C.2 Item by item
- OE-1 = N-OE-1: same gap and same repair. CORRECTION of my report:
  - §2 said "0 such tie moves in all my data". My counter counted only ties with E_k = ⊥. That is the case the sentence needs, and it is 0
    in both reports.
  - Counted generally (oe_check.py now has the counter OE_tie_moves; logs_tie/):
    - library: 2 level-⊥ σ̄(o) changes off crossings (n5s_maxph_0, j8_n32), REFEREE's 2;
    - random 𝒞^1O (seeds 943/944): 5.
  - All of these have E_k ≠ ⊥. The sentence is unproved, not refuted, as REFEREE says.
- OE-2 (CAP-1 also for o on its honest cycle, ¬H1): I accept. My §2 used CAP-1 at λ(o) ≠ o without saying that the ¬H1 case (o on a
  cycle, not its cycle node) is covered.
  - REFEREE's re-derivation of R-N5-FB §4.2 assumes no off-cycle condition. I re-read both branches (a) and (b): correct.
  - My data covers that case: the CAP1 counter counts every state with λ(o) ≠ o, including ¬H1 states, and found 0 failures.
- OE-3 = part of my §2 step 3 ("as in Lemma HI's second bullet"). REFEREE's (C1) + (C3) citation is the precise form. Accept.
- N-OE-2 (step 3's reason that x0's honest play avoids o): REFEREE gives the same one-line reason via H1's definition (N5-NH-box28 l. 9).
  This row joins OE-3 in the fixes file as one wording line.
- N-OE-3 (phase key): mine only. REFEREE checked TC (i) and FB via citations but did not raise the key transfer. Each cited item uses only
  λ_Ξ and τ (FB packet l. 47; TC (i) statewise). One fixes-file line.
- OX-1 (f and T over transitions with both ends in the phase, R25 FB-2): accept. My checker counts in-phase transitions only, which matches.
- Note 3.6 (X ≤ (n − 1)(Z + 1) + Z is one direction): accept, a correct refinement of the Reading's "≡ Z up to a factor n".
- Data: REFEREE's library counts (436 + 11 crossing-free, 279 O > E all at crossings, 235 non-tame all crossings) are IDENTICAL to my logs1
  counts.
  - CORRECTION of my §5: the difference from the packet's 220-file numbers is the trunk date of the lane's run. c1o_list.py today lists the
    same 234 files (REFEREE). My "no deduplication" explanation was a guess from the source and is withdrawn as the cause.
  - REFEREE also ran oddlev.py, the lane's script; I did not, by my rule.
### C.3 Joint gap map (one fixes-file line per row)
| row | REFEREE | REFEREE-2 | fixes-file line |
| --- | --- | --- | --- |
| 1 | OE-1 | N-OE-1 | §2 "In particular": "σ̄(o) makes no relevant change of level ≠ ⊥ (O_k = ⊥)"; level-⊥ tie changes do occur off crossings (2 library, all with E_k ≠ ⊥) |
| 2 | OE-2 (closed) | — (accepted in §C) | §2 step 1: cite CAP-1 as R-N5-FB §4.2, valid for λ(o) ≠ o including o on its honest cycle (¬H1); no text change |
| 3 | OE-3 | N-OE-2 (+ my step-3 remark) | §2 step 3: "x0's honest play avoids o because H1 says o's honest play does not return to o; by (C1) and (C3), Ξ_{k+1}(x0) ◁ Ξ_{k+1}(x1)" |
| 4 | — | N-OE-3 | Dependencies: R22 TC (i), R25 FB / J1 / CAP-1 are signed under the key (λ_Ξ, λ_U, τ); each uses only λ_Ξ and τ constant (P-N5-FB l. 47; TC (i) and CAP-1 statewise), so they hold on this packet's (λ_Ξ, τ) phase |
| 5 | OX-1 | — (accepted) | §3: "f and T count transitions with both ends in the phase (R25 FB-2)" |
| — | note 3.6 | — (accepted) | Reading: "X ≤ (n − 1)(Z + 1) + Z (R23 LV′), the direction a bound on Z needs" |
### C.4 Labels after two signatures (D18/L40)
PROVED (L-NEW successor 12; REFEREE and REFEREE-2, Opus 5.5, D15), pending CHECKER:
- Lemma U-loc on every game inside a phase;
- Lemma OE (with row 1's wording) and Corollary OX (i)-(v) on 𝒞^1O.
OPEN: X and K per phase; G-N5-TIME. Not a TARGET.md claim; not a step-4 pass.
