# GAP-A status brief for the L32 reassessment (A_DTL, polynomially many searches)

L-ALG successor 10, box 16, 2026-10-18 (date -u ~21:45Z). Produced on Opus 5.5 (D8). Every item is a reading or DATA unless
marked as refereed. Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (L22/L26).
GAP-A (docs/GAPS.md): A_DTL makes polynomially many searches (gauntlet step 4, running time). Detail: docs/alg/GAP-A-M.md §23-§36;
dead ends: docs/alg/DEAD.md.

## 1. Bottom line
- L32 (Lead reading, 2026-10-17 09:12Z) asks for one of two things:
  - one named statement with a proof route;
  - or a proved polynomial bound on a nontrivial subclass.
- Neither exists as of box 16.
- The record narrows GAP-A to one structural point, reached by every route tried: comparing two depth-0 continuations of DTL's
  search loop that run on DIFFERENT input sets after a re-cut (§35, §36). No lemma relates them.
- No super-polynomial family is known either. L32 (1) was never triggered: all fleet families have linear or near-linear phases.

## 2. What it rests on
- **Refereed** (both referees, CHECKER PASS; RESULTS):
  - R4: GAP-C Step 5, with (ACYC) open.
  - R5: structural lemmas, including the First-Difference Lemma.
  - R7: root-call monotonicity, ROOT-BOUND.
  - R8: STR-DET.
  - R9: per-context budgets, GAP-A ⇐ (CTX⁺) ∧ (FALL).
  - R10-R11: EXACT*, PREFIX-MONO-X*, F_R ≤ 3·N*_R.
  - R12-R13: reductions through steal depth and exits.
  - R14: CHANGE-NEW, F_R ≤ 3·#fired⁺(R), and GAP-A ⇔ (CTX⁺) ∧ (FIRED⁺-R), given STR-DET.
- **Proved readings, unrefereed** (L-ALG):
  - on the one-player class 𝒞^1P: CTRL, NOSTEAL-1P, OUTCOME-MONO-1P (§27b, §28e), Lemma SAME-CTX and Lemma W (§33), Lemma LEX (§35b);
  - general: STEAL-ENTRY (§28c).
  - The packets are HELD by the Lead.

## 3. Routes tried since L32, each with its failing step and pinning instance
(Pinned instances are in experiments/alg/instances or experiments/red/**/instances, with sha1 and pinned-Oink verification in DEAD.md.)
| route (box) | failing step | instance |
| (STEALER-MONO), (STEAL-ONCE*), (STOLEN-PERM)/(STAYS-MET) (8) | steals recur at one (context, round, top, tangle) | stealer_viol_n76, stealonce_viol_n76 (RESULTS DE19, DE20) |
| (CTX-LAMINAR), (PIECES-LAMINAR), (FIRED-STEP), (FIRED-HALL) (8) | contexts and fired tangles are not laminar or step-bounded | c6_replay3_n32 and others (GAP-A-M §23i-§23m) |
| (STEAL-DEPTH_D), (EXIT_c) for constant D, c (9-10) | lagfam: steal depth D and ⌈D/2⌉ + 1 exits on n = 7D + 22 | lagfam (RESULTS DE21) |
| (FIX-d), fixed number of priorities (11) | lagfam survives at d = 3 | lagflat7_d3_D4/D8/D16 (§26) |
| all-distinct priorities (11) | lagfam refined stays long | lagdist_D4/D8/D12 (§27a) |
| 𝒞^1P via (CHAIN), (RANK-MONO), (TOP-CHAIN), (FIRE-LAMINAR), (TIE-BELOW) (11) | the §27d re-cut: a −1 result's Dom(prevV) piece shrinks | onep_chainfail_n20 05bfe58e20d7, onep_firecross_n76 59a94ce07e0b, tieabove_n20 701d309c8b8a |
| per-context firing count on 𝒞^1P: (TOP-UNIQUE@R) (12) | false; and per-context bounds cannot bound contexts | onep_topuniq_n20 6cf816c7a5ec (§30) |
| depth-0 potentials and keys, (VR-NEW_j), (v, ρ) (12) | the chain returns to earlier (context, rank) states after a re-cut | onep_vrj_n40 96ac8459cbef, onep_vr_n12 868476e00138, onep_fdkey_n20 9daa6dbcf01d (§32) |
| (VR-NEW_V), (VR-NEW_s) in two-player games (L-RED, 12-13) | a vertex returns to its (ρ, \|V\|) or (ρ, \|R\|) state | vrV_viol_n80/n40, vrs_viol_n100 (experiments/red/tcpert/instances/prod) |
| literal CORE, (SIG-DISJ), literal (TREE-PIECE) (13) | same-signature returns; identical call trees | onep_vrj_n40, tp_ident_n20 dfeb04607e88 (§33c, §34c) |
| (XCTX@p0), the core on 𝒞^1P (14) | input-monotonicity of the depth-0 continuation below a first difference: (CHAIN-NEST), (CHAIN-SIZE) false | onep_nest_n68 926bbef91e0e (§35) |
| (XCTX@p0), the §33 hypothesis on 𝒞^1P (L-RED R42, after box 16) | FALSE: a same-signature context of a different set covers N at p0 | xctx_viol_n20 742ba103cdb7 (§37; L-ALG confirmed exactly) |
| (TREE-PIECE⁺) sketch, two-player games (15) | step S4: the outcome at a fixed input FALLS (LEX false); the signed replacement gives back (CTX⁺) ∧ (FIRED⁺-R) | cm_viol_oink_n28 587d2c68a942 (§36) |
| (TC-6), the Two Counters family (10-11) | parked: single family, not L32 progress | — |
| (NO-PRE-a) proof (12) | no monotonicity between visits in two-player games | none; data only (§31) |

## 4. What survives as DATA (0 violations on all data; none proved)
- **On 𝒞^1P:**
  - (CHAIN-CHANGE). (XCTX@p0) is now FALSE (xctx_viol_n20, §37), so the §33 reduction gives no route; (FD-WITNESS_all), which it was meant to prove, still holds (margin 1 there).
  - L-RED's xcov11_n20 (sha1 47023109c198, 21:18Z) is the first PARTIAL cross-context cover at p0 (11 of 16 vertices). (XCTX@p0) still holds there.
  - (VR-NEW_all), (TOP-CHAIN@R).
- **In all games:**
  - (TREE-PIECE⁺), which would give O(n⁶) changed-tree transitions per phase (§34b-d). It is consistent with every known result; the only tension is the author's never-committed "counter_dtl" README row (L-LIT T17).
  - (NO-PRE-a).
- **Caveat:** every phase in the data is short (at most 42 transitions in the long benign families, about 27 in the hard ones (vrV_viol_n40)). These statements say "no counter"; one counter kills them.

## 5. Honest view of the most promising remaining angle
- **The decisive step is cheaper on the adversarial side.**
  - Every proof route ends at the same point: two runs of the depth-0 loop on different inputs.
  - The keys that still survive are exactly the states a counter would have to repeat.
  - L-RED now has a graded climb (xscore.py) with the gradient mine lacked, and a first partial cover (xcov11_n20).
  - Its attack on (XCTX@p0) / (TREE-PIECE⁺) should settle the direction:
    - a full cover, or a key-repeating counter, would show the re-cut mechanism compounds;
    - a long phase without one would make the surviving DATA statements much stronger evidence.
- **On the proof side,** the only ingredient I can name is a cross-context invariant of the depth-0 loop: a quantity that is equal or larger after the loop restarts on a smaller input with more tangles. Lemma LEX is the within-context version of it. No candidate for the cross-context version survived the data (CHAIN-NEST, CHAIN-SIZE, SIG-DISJ, RANK-MONO, NO-RETURN are all false on 𝒞^1P).
- **Subclasses:** I see no credible nontrivial subclass with a concrete first proof step. onep_nest_n68 already shows the obstruction inside 𝒞^1P with all priorities distinct, and fixed d does not remove lagfam.
- This is a statement about this candidate's GAP-A route, not about M4 (D5).
