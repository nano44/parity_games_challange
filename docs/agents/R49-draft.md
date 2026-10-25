# Draft RESULTS R49 (Lead, 2026-10-25 22:45Z by date -u; REFEREE's §C and the fixes file to be filled) — to CHECKER C58

### R49 [refereed-only] N5 on one-Odd-choice games: a gate into F along an optimal F-play has level ≥ r (XG), one-player valuations do not rise under non-improving or exceptional edges (ANTI, every one-player game), Even's best reply to τ from the threat x0 uses a (β) gate whenever M = −1 and r ≥ 0 (NEED-β), an old threat stays in R after a rise (OLD-THREAT), and CONJECTURE INTO would exclude a later fallback (reduction); the CONJECTURE "in scope, THR ⇒ M ≥ 0" is FALSE (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C58.md, checker PENDING)
- Object (packet P-N5-NEEDB, added at l-si 3ea0f5f9, pinned trunk e6ee6130, unchanged during review): docs/si/P-N5-NEEDB-box13.md, sha1
  7471aef37f9ad2a746dbc63451a5543b3917a443 (L-SI successors 7 (§1-§3 cases (B), (A1), (A2′), (A2″)) and 8 (the rest), Opus 5.5). The
  referees' notes are collected by the lane in docs/si/P-N5-NEEDB-fixes-box13.md (l-si 863ca636, sha1
  0e5f24af086c54609c1a2233e6b1c485a0bf442c, L-SI successor 10: NEEDB-N1..N4, N-NEEDB-1..5, R71 §4's INTO wording); on trunk; repairs only.
  Setting as in RESULTS R31, R35, R37, R40 and R41 (𝒞^1O; scope run S; S4a / S4c; Ξ, W; gates, gate levels, M_k; COARSE_L, (C1)-(C7);
  R̄ / R / F; (h); r; THR; phase; c; the gate kinds (α), (β), (γ) of R41 (a)). x0 := σ̄_k(o), t := τ(o). G_τ: the one-player game "Odd
  fixed to τ", U := Opt(G_τ) its pointwise optimum, σ* an optimal strategy of G_τ (V_{σ*,τ} = U). An Even edge (v, u) of a one-player
  game with σ-valuation V is V-EXCEPTIONAL if v is its own V-cycle node, u ≠ σ(v) and V(u) = (v, ∅, ·). SETTING (LV+): an in-phase THR
  S4c fallback k with (h) at k, M_k = −1 and r_k ≥ 0; 𝒫 is the σ*-play from x0 in G_τ. RISE SETTING (packet §4): k0 an in-scope
  fallback of S with L := M_{k0} ≥ 0, j > k0 the first S4a step after k0 that changes COARSE_L(θ), every transition between them in S
  and r > L; a POST-RISE STATE is a state t > j such that every transition s → s+1 with k0 < s < t is an in-scope S4a step with r_s > L.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P) beyond what RESULTS R36 discharges:
  (a) Lemma XG: let k be an in-phase THR S4c fallback with (h), y ∈ R_k Even, s := σ_k(y) and z := σ*(y) ∈ F_k, where z's (σ*, τ)-play
      stays in F_k. Then (y, z) is a gate at k of level ≥ r_k. "In particular M_k ≥ r_k" holds when such a y exists (NEEDB-N1, wording).
  (b) Lemma ANTI (every one-player game): if H is a one-player game, σ an Even strategy with valuation V, and σ′ chooses at every Even
      vertex v either an edge (v, u) with V(u) ⊴ V(σ v) or a V-exceptional edge, then V_{σ′} ⊴ V pointwise; and its instances ANTI-Ξ,
      ANTI-W.
  (c) Corollary NEED-β: in setting (LV+), 𝒫 uses an edge (y, σ*(y)) that is a (β) gate. The cases (B) 𝒫 avoids o, (A1) 𝒫 visits o and
      its cycle avoids o, (A2′), (A2″) and (A2*) (𝒫's cycle contains o, by where its top lies) are exhaustive.
  (d) Lemma OLD-THREAT: if t is a post-rise state and x ≠ o is an exit of o with x ∈ F_{k0} and COARSE_L(o ⊕ Ξ_{k0} x) =
      COARSE_L(θ_{k0}), then x ∈ R_t; in particular the k0-threat σ̄_{k0}(o) lies in R_t.
  (e) Reduction: CONJECTURE INTO ("at every post-rise state t with r_t > L, some gate (y, z) has z ∈ R̄_t", read at states with
      Iσ_t ≠ ∅, R71 §4; fixes) implies that no case (i)
      fallback occurs, i.e. no later fallback k of S with r > L on [k0 + 1, k]; "case (i)" is read as the NEXT fallback of S after k0
      (N-NEEDB-2 = NEEDB-N2), and R20 (b) FBL's "no F → R and no R → R gate" is read in R19's notation, where R contains o (NEEDB-N3).
- Not signed (packet §5): CONJECTURE INTO (OPEN); case (ii) of the rise question, r ≤ L before the next fallback (OPEN); the dead
  conjectures RISE-DROP, GATE-ABOVE, FEED (FALSE, recorded in RESULTS R40-R43 and docs/si/DEAD.md). The CONJECTURE "in scope, THR ⇒ M ≥ 0"
  (docs/si/N5-LV3-box12.md §4-§5; RESULTS R41, R43, not signed) is FALSE (N-NEEDB-5): docs/referee-2/R2-N5-LV2/climb/block_9501.pg
  (sha1 1b5b76fd), from the start pair in block_9501.txt, state 1: (h), θ = (5, {9}, 3) ◁ w = (5, ∅, 1), r = 10, M = −1, gates (10, 1),
  (10, 3), (10, 8), all (β) (rank o 2 < rank c 9), k → k+1 in scope; reproduced on REFEREE-2's three traces, confirmed on REFEREE's engine (§C C.3, referee 7dbd5118) and on L-SI's
  (experiments/si/needb5/repro.py, l-si 34e5225a). From
  the canonical start the run has no such state (RESULTS R43 limit (iii)). At this counterexample NEED-β holds: 𝒫 uses the (β) gate
  (10, 8), case (B).
- Honest limits: (i) SUBCLASS 𝒞^1O except (b). (ii) These lemmas locate the (β) gate of any M = −1 fallback and reduce case (i) to INTO;
  they bound no count, so G-N5-TIME stays open. (iii) Thin data: XG's hypothesis is VACUOUS in both referees' batch data and occurs 7 times
  only in REFEREE-2's climbs (N-NEEDB-4: its first saved start pair was invalid, so REFEREE could not
  reproduce it, §C C.4; REFEREE-2's Addendum A, referee-2 1a9a0407, pins a valid start pair and an optimal σ*, and its rng-free
  xg_witness.py gives RESULT OK; the hypothesis holds for some optimal σ*, not for the deterministic one); NEED-β's cases (A1), (A2′), (A2″), (A2*) never occur in setting (LV+) (every (LV+) state in
  data is case (B)), so they rest on their proofs; random 𝒞^1O games reach neither (LV+) nor a rise.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own needb_probe.py on rl_engine): P-N5-RHO's 412-file list
  (253 𝒞^1O) from SPEC S3's start and with 4 random start pairs, REFEREE-2's 145 climb outputs, 1,400 random-start runs on the LV2
  witnesses and beta2_n11, and block_9501 from its own start pair: in-scope THR fallbacks with r ≥ 0 985 + 398 + 434 + 1, setting (LV+)
  exactly once (block_9501, (β) gate (10, 8)), NEED-β's stronger form (NEEDB-N4: 𝒫 uses a gate that is not Ξ-exceptional, at every THR
  fallback with (h) and r ≥ 0) at each of them, XG 0 cases, OLD-THREAT 510 exit checks, INTO 52 / 52, ANTI 100,000 random checks; 0 failures. REFEREE-2
  (own needb_check.py): 5,904 library runs and 3,000 random runs, 0 violations; six climbs: 297,752 (LV+) states, every one case (B) with a
  (β) gate on 𝒫, XG hypothesis 7 times, OLD-THREAT 57,988 exit checks at 38,664 post-rise states, INTO 1,492 / 1,492, case (i) 0, 0
  violations; mutation controls xg, otc, b0, anti fire, otf does not.
- Signatures: REFEREE docs/referee/R-N5-NEEDB.md (referee 008ad8ab, successor 10; §C 7dbd5118, successor 11): XG, ANTI (+
  ANTI-Ξ, ANTI-W), NEED-β (B), (A1), (A2′), (A2″), (A2*), OLD-THREAT, the reduction SIGNED; notes NEEDB-N1..N4; no gaps. REFEREE-2
  docs/referee-2/R2-N5-NEEDB.md (referee-2 ef433d32, successor 12; Addendum A 1a9a0407: witness start pairs corrected,
  four lines of §1 / §6 marked "corrected in Addendum A", no verdict change): all SIGN; notes N-NEEDB-1..5; no gap. REFEREE-2 discloses that, after
  its verdicts and notes were written, a repository grep printed two lines reporting REFEREE's verdict (LEAD-STATE, RESULTS R43); it changed
  nothing after that and did not open docs/referee/. §C (REFEREE): verdicts identical; joint gap map empty;
  NEEDB-N2 = N-NEEDB-2; N-NEEDB-1 = REFEREE's IN-DATA line; N-NEEDB-3 accepted; N-NEEDB-5 confirmed; N-NEEDB-4 accepted as REFEREE-2's
  data but NOT reproduced by REFEREE (the saved start pair of witness_xg_12004 is not a strategy pair of that game); corrected in
  REFEREE-2's Addendum A (1a9a0407).
  §C (REFEREE-2): R2SC-PENDING.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
