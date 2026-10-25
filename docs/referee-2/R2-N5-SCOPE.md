# R2-N5-SCOPE: second-referee check of packet P-N5-SCOPE (L-NEW box 36: KEY, WCH, SCOPE-COUNT, FB-INT, NH1-FB, CN-LAST). REFEREE-2 (successor 8), 2026-10-25 11:55Z (draft 1f8a9109 at 11:2xZ) (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-SCOPE (Lead GO 11:09Z). Object docs/new/P-N5-SCOPE-box36.md, sha1
c3f5ed3788f0853939d247dbcfb970334c9dcf7d. I checked the sha1 with `git show 8998ee6d:docs/new/P-N5-SCOPE-box36.md | sha1sum`, at
origin/claude/l-new, and on my tree; all three agree. The pin is trunk 8998ee6. The file has one commit, 8483279d.
Background read: SPEC S1-S5 (docs/new/N5-ssi-global.md) and experiments/new/n5.py line 30; RESULTS R15 (a), (d), R18 (d), R19 (a),
R22 (a), (b), R25 (d), (e) with the proofs in docs/si/P-N5-FB-box7.md §1-§5, R28 (b), (c) with docs/new/P-N5-OE-box32.md §2-§3,
docs/new/P-N5-LP-box32.md §1 and §4, R29 (setting), R30 (d), R33 (e) with docs/new/P-N5-L2-box34.md §5, and P-N5-TOG
(docs/new/P-N5-TOG-box35.md §0, §4, §6; signed by both referees).
Independence: no REFEREE report on this packet exists on my tree or on origin/claude/referee (`git log origin/claude/referee --
docs/referee/R-N5-SCOPE.md` is empty), and I read nothing in docs/referee/ or notes/REFEREE.md. I did not run or import scopecnt.py,
lenrun.py, outclimb.py, check_sol2.py or any REFEREE probe. Lane .pg files are inputs only.
Tools: docs/referee-2/R2-N5-SCOPE/ (own code; it builds on my lane's R2-N5-FRZ/frz_check.py and R2-N5-RE/re_check.py):
- scope_check.py: the checks;
- scope_climb.py: the climbs;
- gxcheck.py: my general N5 against Oink;
- mklib.py, files.lst, gfiles.lst, run_all.sh, run_climbs.sh, logs/, climb/, totals_logs.txt, totals_climb.txt.
Every game in a 𝒞^1O mode asserts exactly one Odd vertex with out-degree > 1. The phase key is (λ_Ξ, τ).
Labels (D18 / L40): PROVED (L-NEW succ. 15) is the packet's own label. §7 is not signed, as briefed. Nothing here is a running-time
bound, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.
Attribution (my predecessor's trap). My N5 differs from SPEC (n5.py) only in S4a's choice of optimum (any arena optimum: deterministic
switch-all SI, or random-subset SI with random value-preserving re-choices), and S4b picks a pointwise-best option. So every count below
is a count on MY N5's traces, not on SPEC's. No SPEC trace was run.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| header: citation correction (R-CONST = P-N5-L2 §5) | correct as written | The source N5-SCOPE-box36.md line 64 says "P-N5-L2 §11", and P-N5-L2 has no §11 (its sections are §0-§9). §5 is R-CONST = RESULTS R33 (e). N-SC-1: the dependency table's status column is stale. R33 landed at trunk 00bd18b8 (10:37:35Z), before the packet was written (10:42Z). So "IN LANDING (… draft, CHECKER C42)" should read LANDED |
| §1 Remark KEY | SIGN | — |
| §2 Lemma WCH | SIGN | N-SC-2 (wording): "F_k = F_{k+1}" holds only off crossings. The proof gives more: Ξ(τ(o)) changes at EVERY such transition, crossings included (DATA: 242 / 242 at crossings) |
| §3 Corollary SCOPE-COUNT | SIGN | It rests on RESTARTS (P-N5-TOG §6), which both referees signed (landing as R34). Case 2 OCCURS (316 batch scope runs), so the #WCH term is needed |
| §4 Lemma FB-INT | SIGN | N-SC-3 (citation): "every non-tame transition is a crossing" is the pointwise content of R28 (c) (ii)'s PROOF; the signed statement there is the count J ≤ X. The packet re-derives it inline from J1, P-N5-LP §4 step 3, R15 (d) and OE, which is sound |
| §5 Corollary NH1-FB | SIGN | N-SC-4 (notation): here T is the actual toggle count (packet §0). In P-N5-TOG §4, T names the bound |U|(n + 1) + n − 1. "Drops ≤ ⌈T/2⌉" holds for the actual count by alternation |
| §6 Lemma CN-LAST | SIGN | Both branches of (iii) OCCUR: stop in 312 cases, τ-change in 5. Control: the hypothesis λ(y) = y cannot be dropped. 59 level −1 Even fallbacks with a non-cycle-node tail break (i) in all 59 cases, (ii) in 53 and (iii) in 46 |
| §7 | not signed (as briefed) | Observation O-1 (§8 below): in the out-of-SN regime the evicting fallbacks are themselves crossings, so they lie outside every FB-INT stretch Q. §7.2's reading "f_out ≤ n_E(2n − 1)(X_out + 1)" needs "+ X_out" (wd16_s2: 12 out-of-SN fallbacks in one phase, 0 in any crossing-free stretch) |
No statement is NOT SIGNED, and no gap is open. No counterexample turned up in 86,517 batch runs (45,656 𝒞^1O + 40,861 general) or in 5,443,544 climb runs (8 climbs).

## 1. Remark KEY: SIGN
- SPEC S1 ("Odd's side"): Ξ^d_τ and τ̄ are computed on G^d from τ alone, by the deterministic procedure. In code this is n5.py line 30,
  `vt, tbar = Ed.evaluate(tuple(tau))`, and σ is not an argument. So U_k, and with it λ_U, is a function of τ_k. ✓
- The two kinds of phase therefore coincide. A maximal run with λ_Ξ and τ constant has λ_U constant, so it is a maximal run with λ_Ξ, λ_U
  and τ constant, and conversely. Every result signed on joint λ-phases with τ constant transfers. ✓
- A by-product used in §6: Iτ is a function of τ alone too (SPEC S2 on G^d).
- DATA: λ_U was unchanged at all 69,962 transitions with τ(o) unchanged (𝒞^1O batch). My U is Even's best response to τ, so this is a
  sanity check of my code (optimal values are unique), not independent evidence.

## 2. Lemma WCH: SIGN (N-SC-2)
- TC (i), statewise. If t0 := τ(o) ∈ R̄, then o's (σ, τ)-play is o followed by t0's, which returns to o: o lies on a W-cycle (t0 = o
  included). If t0 ∈ F, t0's play avoids o, and o is not on the cycle it ends in. So H2 ⟺ t0 ∈ F at each state. ✓
- Under H2, o is not on its W-cycle, so λ_W(o) ≠ o. (V1) in G_τ gives w = o ⊕ W(t0). Off R̄, W = Ξ (R19 (a), no (h) needed), so
  w = o ⊕ Ξ(t0). ✓
- H2 at k and at k+1 gives t0 ∈ F_k and t0 ∈ F_{k+1}, separately. So w_k ≠ w_{k+1} forces Ξ_k(t0) ≠ Ξ_{k+1}(t0) at every such
  transition, crossing or not. N-SC-2: the statement's "t0 ∈ F_k = F_{k+1}" sits inside the non-crossing disjunct, where it is true.
  The proof shows the unconditional form. ✓
- Count. A non-crossing transition lies inside one crossing-free interval I. There t0 ∈ F_I, and F1° (R22 (a), with KEY) allows
  ≤ max(0, |F_I| − 1) ≤ n − 2 transitions with a Ξ-change on F_I. There are ≤ X + 1 intervals, and the crossings add ≤ X. ✓
- DATA: w = o ⊕ Ξ(τ(o)) held at all 83,660 H2 states, and TC (i) at every state. There were 1,706 WCH transitions; 242 of them are
  crossings, and Ξ(τ(o)) changed at all 1,706. Per crossing-free interval, ≤ max(0, |F| − 1) held everywhere; the max was 18 (sc24).
  The max per phase was 20 (sc24, n 24; the lane also reports 20). Control counter WCH_control… (a w-change without H2 at both ends and with Ξ(τ(o)) fixed) stayed at 0.

## 3. Corollary SCOPE-COUNT: SIGN
- Distinct scope runs have distinct first transitions k → k+1, and (h) holds at k.
- Case 1: k is the first state of its (h)-run. The map to (h)-runs is injective. ✓
- Case 2: k − 1 is an (h) state of the same (h)-run, hence of the phase.
  - k − 1 → k is an in-phase transition with (h) at k − 1 and H2 at k.
  - Maximality of the scope run excludes w_{k−1} = w_k. So it is a WCH transition (H2 at both ends).
  - k ↦ k − 1 is injective. ✓
- (h)-runs ≤ 1 + T + f is RESTARTS (P-N5-TOG §6). Its definitions of (h)-run, T and f are the same as this packet's. ✓
- The scope-run definition is R29's verbatim (RESULTS R29, Setting). ✓
- DATA: 6,141 scope runs (5,825 case 1, 316 case 2). Every case-2 start had a WCH transition k − 1 → k, and the map was injective. Max
  per phase: 5 scope runs (so_th_n32 and zcl_cu_n48; the lane reports 5 on so_th_n32), 4 of them case 2, 2 (h)-runs. RESTARTS and the
  full bound held in every phase.

## 4. Lemma FB-INT: SIGN (N-SC-3)
- Non-tame ⇒ crossing. J1 (R25 (e)): σ̄(o) switches at a level > M_k.
  - If λ(o) = o, that change is not relevant. Then L_k ≤ M_k, since Even's switches are gate edges by R15 (d). Lemma U (R27; P-N5-LP §1)
    then freezes COARSE_{L_k} and so COARSE_{M_k}: tame, a contradiction. This is P-N5-LP §4 step 3, as cited. ✓
  - So the change is relevant, and O_k > M_k ≥ E_k. OE (R28 (b)) gives O_k ≤ E_k off crossings. So the transition is a crossing. ✓
- Q has only tame transitions, and they are consecutive, so Q lies inside one tame run. FB's proof, steps (1)-(4)
  (docs/si/P-N5-FB-box7.md §4), counts the S4c fallbacks of one tame run:
  - ≤ n_E per block of level ≥ 0, and ≤ n_E(n − 1) per block of level −1;
  - one block per level value (MONO);
  - none at ∞ or ⊥.
  Total ≤ n_E(2n − 1). Q has at most that many. ✓
- N-SC-3: the pointwise fact is in the proof of R28 (c) (ii); the signed statement is J ≤ X. The packet's inline re-derivation closes the
  citation, so this is a note.
- Scope note. Q consists of non-crossing transitions. So a fallback that is itself a crossing is in no Q, and FB-INT does not count it.
  The statement is correct as written. §7.2's use of it is not (O-1).
- DATA: all 1,458 non-tame in-phase transitions were crossings. Fallbacks per maximal crossing-free stretch: max 1 in the batch and
  4 (FIT fb, n 11, n_E 7: bound 147) in the climbs. The bound n_E(2n − 1) is far from tight in my data, which is THIN for this count.

## 5. Corollary NH1-FB: SIGN (N-SC-4)
- Case A (¬H1 at k and k+1). The transition lies in a maximal ¬H1 run S. R-CONST (R33 (e); P-N5-L2 §5, checked: (⊆) via o's honest
  play, (⊇) via the unique cycle through c_θ, which is o's under ¬H1) gives R̄ = U on S. So S has no crossing, its internal transitions
  lie in one crossing-free stretch, and FB-INT applies. ✓
- Every maximal ¬H1 run, except possibly the one at the phase's first state, starts with a drop. Drops ≤ ⌈T/2⌉ by alternation, so there
  are ≤ ⌈T/2⌉ + 1 runs. If c_θ = o, ¬H1 holds throughout and T = 0 (P-N5-TOG §4). ✓
- Case B (¬H1 → H1) is a toggle: ≤ T. ✓
- N-SC-4: P-N5-TOG §4 uses "T" for the bound |U|(n + 1) + n − 1. Here T is the count, which is at most that bound; both readings give a
  valid inequality.
- DATA: R-CONST held at all 10,701 ¬H1 states, and no crossing occurred inside any ¬H1 run. 94 ¬H1 fallbacks: 61 case A, 33 case B.
  Max per phase 1 (batch) and 4 (all case A, in one ¬H1 run) (climbs). ¬H1 runs ≤ drops + 1 held everywhere.

## 6. Lemma CN-LAST: SIGN
- Setup. Every tail c_i is an own cycle node. By (F) (P-N5-TOG §0), Ξ(σ_k c_i) = (c_i, ∅, L_i − 1). Level −1 gives Ξ(z_i) = (c_i, ∅, d_i)
  with d_i strictly better.
  - z_i's play reaches c_i without meeting another c_j. A c_j on the way would give the cycle node c_j: c_j is the top of its own cycle,
    and c_i ≠ c_j cannot lie on that cycle, since a cycle has one top. ✓
- (i). Take a (σ′, σ̄_k)-play that meets some c_i first.
  - Up to c_i it is the old prefix.
  - From c_i it runs c_i → z_i → … → c_i. That path has no switched vertex, and Odd vertices follow σ̄_k as before.
  - The new cycle has top c_i (P = ∅ on z_i's path), as the old one did. So the cycle node, P and the length to the first visit are
    unchanged.
  - Hence V_{σ′, σ̄_k} = Ξ_k. S (a) (VJ00 (11)) gives Ξ_{k+1} ⊴ Ξ_k, and R15 (a) gives ⊵. The order is total on valuations (injective
    rank and weight), so they are equal. ✓
- (ii). An unswitched Even v had Iσ_k(v) = ∅, since S4c switches every vertex with a gate, and σ(v) and Ξ are unchanged. At c_i, a
  gate (c_i, w) at k+1 would satisfy Ξ_k(w) ▷ Ξ_k(z_i) ▷ Ξ_k(σ_k c_i). So (c_i, w) ∈ Iσ_k with a better target than z_i, a
  contradiction. ✓
- (iii). Iσ_{k+1} = ∅, so S4a keeps σ. If Iτ_{k+1} = ∅, N5 stops. Otherwise S4b moves τ, or else S4c falls back to Odd (Iσ = ∅) and moves
  τ. Either way k + 1 ends the phase. ✓
- Remark (mine, not needed): Iτ depends on τ alone (§1), and τ is unchanged at an Even fallback (FIX 3). So Iτ_{k+1} = Iτ_k. Hence N5
  stops at k + 1 exactly when Iτ_k = ∅, which is the common case (312 / 317).
- "At most one per phase, the last transition": by (iii). ✓
- The packet's "Consequence (READING)" follows. With every gate at level −1, either every tail is a cycle node (≤ 1 such fallback, last)
  or some tail is not. I did not sign it, since it is labelled READING.
- DATA (my two N5s; the general N5 is validated against Oink on 287 files × 2 modes, 574 / 574 OK):
  - 376 level −1 Even fallbacks, 317 of them meeting the hypothesis (𝒞^1O 177, general 140). (i), (ii), (iii), Setup, "one per phase"
    and "last transition" held in all 317. The run stopped at k + 1 in 312 cases; τ changed at k + 1 → k + 2 in 5 (general files
    n5adv best_n16_seed16, n5b9/sc24, seg10/seg_r16_s169; 𝒞^1O random 2).
  - Control, outside the hypothesis: 59 level −1 Even fallbacks with a non-cycle-node tail. (i) failed in all 59, (ii) in 53 and (iii) in
    46. oc12_s1 is one of them, and matches the lane's §7.3.
  - Climbs (FIT cnl): 555,510 hypothesis cases (153,940 stop, 401,570 τ-change), all of (i)-(iii) held; 1,257,035 control cases outside the hypothesis, (i) failed in all of them.

## 7. Batch (DATA, my N5; logs/, totals_logs.txt)
- Library: files.lst lists the 276 tracked experiments/**/*.pg on 𝒞^1O with n ≤ 64 (mklib.py), 3 starts each (S3 + 2 random) × {det,
  --rand}. It includes wd16_s2, wd12_s1, pftheta_cex_n32, oc12_s1, sc24, so_th_n32, tog6a_n32 and claimF_len_cf1.
- General games: gfiles.lst lists the other 287 tracked .pg with n ≤ 24 (CN-LAST only), 3 starts each.
- Random 𝒞^1O: 4 × 10,000 games at n 4-14 (2 det, 2 --rand) and 2 × 2,000 at n 15-30 (--rand), plus 4 × 10,000 general games at n 3-12.
- Result: 849 logs, all RESULT OK, 0 violations. 45,656 𝒞^1O runs, 11,961 phases, 94,294 transitions, 3,451 fallbacks; 40,861 general
  runs, 57,815 transitions, 321 fallbacks.
- Oink (pinned 8fbf0a7, built by scripts/setup_oink.sh in this container), regions at termination:
  - my 𝒞^1O N5: 552 / 552 OK on files.lst (../R2-N5-FRZ/oink_xcheck.py, det + --rand);
  - my general N5: 574 / 574 OK on gfiles.lst (gxcheck.py).
- §7.1 classes of in-phase fallbacks (my N5, all 𝒞^1O runs): IN 2,209; NH1 94; H1 ∧ ¬H2 360; OTHER 7; END ¬H2 15; END w-change 0.
  The library alone (det): IN 1,170; NH1 1; H1 ∧ ¬H2 170; OTHER 3. These differ from the lane's §7.1 (SPEC trace, other inputs). They
  are not a re-run of it.
- Max out-of-SN fallbacks in one phase: 12 (wd16_s2), the lane's number too. (h)-runs per phase: max 2 (tog6b_n32); the lane's 4 on
  tog6a_n32 is a SPEC-trace count that my N5 does not reproduce (attribution, not a disagreement).

## 8. Observation O-1 on §7.2 (not a verdict; §7 is not signed)
- §7.2's loop reads "FB-INT gives ≤ n_E(2n − 1) such fallbacks per crossing-free stretch, so f_out ≤ n_E(2n − 1)(X_out + 1)".
- FB-INT counts only fallbacks that are not crossings. An evicting fallback IS a crossing (R changes at it), so it is in no stretch. The
  correct form is f_out ≤ n_E(2n − 1)(X_out + 1) + X_out (as in R28 (c) (iv)).
- DATA: on wd16_s2 (my N5, 3 starts × {det, --rand}) every in-phase fallback is a crossing: max fallbacks per crossing-free stretch is 0,
  while one phase has 12 out-of-SN fallbacks. The loop is "every out-of-SN fallback is a crossing", which FB-INT does not touch. Route to L-NEW for §7.2.

## 9. Climbs (DATA, my N5; climb/, totals_climb.txt)
Eight climbs of 1,200 s (run_climbs.sh; 4 starts per evaluation, starts 2-3 with --rand): 1,360,886 evaluations = 3,486,820 𝒞^1O runs
+ 1,956,724 general runs; 0 violations (RESULT OK in all 8). Best instances in climb/ (Oink zlk: my 𝒞^1O N5 12 / 12, my general N5 4 / 4 OK).
| FIT | seed | start | n | best maxima per phase |
| --- | --- | --- | --- | --- |
| scope | 91 | random 8-16 | 9 | 3 scope runs (3 case 2), WCH 4 |
| scope | 95 | sc24 | 24 | 7 scope runs (7 case 2), WCH 11 (one interval) |
| scope | 98 | random 10-20 | 15 | 6 scope runs (5 case 2), WCH 6 |
| fb | 92 | random 8-14 | 11 | 4 fallbacks per crossing-free stretch, 4 ¬H1 fallbacks (case A, one run) |
| fb | 93 | wd12_s1 | 12 | 9 out-of-SN fallbacks, 1 per crossing-free stretch |
| fb | 96 | oc12_s1 | 12 | 7 out-of-SN fallbacks, 1 per crossing-free stretch |
| cnl | 94 | general 6-12 | 10 | CN-LAST cases with τ-change (fitness 1010) |
| cnl | 97 | general 8-14 | 9 | same (fitness 960) |
- Climb totals: 1,037,635 case-2 scope runs; 340,482 ¬H1 fallbacks (338,059 case A, 2,423 case B); 2,333 non-tame transitions, all
  crossings; CN-LAST as in §6.
- Reading of the data: SCOPE-COUNT's case 2 (the WCH term) dominates in climbs; the scope-run count grew only through WCH. FB-INT and NH1-FB
  stay far below n_E(2n − 1). The out-of-SN climbs (93, 96) again put their fallbacks at crossings (O-1). Climbs are not families.

## 10. Notes for the lane (none blocks a signature)
- N-SC-1: the dependency table's status is stale. R33 was landed (00bd18b8, 10:37:35Z) when the packet was written.
- N-SC-2: WCH. Write "Ξ_k(t0) ≠ Ξ_{k+1}(t0) at every such transition", and keep F_k = F_{k+1} for the non-crossing count only.
- N-SC-3: FB-INT. Cite "the proof of R28 (c) (ii)" for the pointwise fact (the packet already re-derives it).
- N-SC-4: NH1-FB. T is the count here and the bound in P-N5-TOG §4. Name them differently.
- O-1: §7.2. Add "+ X_out" to f_out; the evicting fallbacks are crossings.

## §C. Comparison with REFEREE's R-N5-SCOPE (written 2026-10-25 12:18Z by date -u, after my report 6d6e4bcf was pushed)
Read: docs/referee/R-N5-SCOPE.md at trunk (fb6089bf + 560ff4c4, REFEREE successor 7). Nothing else in docs/referee/ was read.
- Verdicts: identical. All six statements SIGNED by both (Opus 5.5, D15), with no gaps; §7 not signed by either. No verdict differs.
- Premises: both name RESTARTS / TOGGLE-COUNT (P-N5-TOG, landing as R34) and R-CONST (R33 (e)) as the only non-landed or newly landed
  premises. Both confirm the header's citation correction (R-CONST = P-N5-L2 §5).
- Proof readings agree point by point:
  - KEY via Ed.evaluate(τ);
  - WCH via (V1) at o, Lemma G (a) and F1°;
  - SCOPE-COUNT's two injective cases;
  - FB-INT's chain J1 → LP §4 step 3 → E_k ≤ M_k → OE;
  - NH1-FB's run count;
  - CN-LAST (i)-(iii).
  REFEREE §5's remark "several runs in one crossing-free stretch are only over-counted" is the same reading as my §5.
- Items only in my report (notes, not verdicts; REFEREE neither raises nor contradicts them):
  - N-SC-1: the dependency status is stale (R33 was landed when the packet was written).
  - N-SC-2: WCH's proof gives Ξ(τ(o)) changes at EVERY such transition, crossings included.
  - N-SC-3: FB-INT's "non-tame ⇒ crossing" is the content of R28 (c)(ii)'s proof, not its signed statement.
  - N-SC-4: "T" is the count here and the bound in P-N5-TOG §4.
  - O-1: §7.2's f_out bound needs "+ X_out", because evicting fallbacks are crossings outside every FB-INT stretch.
  - The Lead has routed all five to L-NEW successor 17 (12:08Z).
- Items only in REFEREE's report: §0's line-by-line check of the five "(filled in)" steps. I checked the same steps inside my §2-§6 and
  agree.
- DATA (different N5 implementations, so the counts are not comparable one-to-one):
  - REFEREE traces = n5.run (SPEC); mine = my own N5 with any arena optimum.
  - CN-LAST's τ-change branch: REFEREE 2 / 1,422, mine 5 / 317 (batch) and 401,570 / 555,510 (FIT cnl climbs). Both see it.
  - Non-cycle-node level −1 controls: REFEREE 1 (oc12_s1), mine 59, 49 of them on general games.
  - Max fallbacks per crossing-free stretch: REFEREE 1 (climbs aimed at scope runs, NH1 and WCH), mine 1 batch / 4 climbs (FIT fb).
    Both are far below n_E(2n − 1).
  - Max WCH per phase: both 20 (sc24).
  - Oink: REFEREE names its Oink re-runs as skipped. I ran mine (552 / 552 𝒞^1O, 574 / 574 general, 16 / 16 climb bests).
- Joint gap map: empty. Joint note list for L-NEW: N-SC-1..4 and O-1 (mine); REFEREE adds none.
