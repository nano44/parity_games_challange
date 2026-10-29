# Draft RESULTS R88 (Lead, 2026-10-29 18:22Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C97 (Lead reviewed 18:31Z by date -u: subagent draft, sha1 ba7124b2 before review. Lead changes: Honest limits (v) (relation to RESULTS R21 (a), R62 (d), R67 (e)-(f): a drafter's — LANDED in RESULTS Results 2026-10-29 19:07Z (CHECKER C97 767bb71e PASS), after R87
reading that no referee checked) REMOVED from the entry and kept here only as a note to CHECKER; the sentence on the lane's CONJECTURE R*-TC
(DEAD in general form, lane DATA) REMOVED from Honest limits (ii) to keep the entry to refereed matter; old (vi) renumbered (v). Lead decisions for CHECKER
to check: (1) the title is G12's final line (fixes l. 65; line sha1 9e6196f2…, byte-checked by REFEREE with `cmp`) verbatim, outer quotes and final
period dropped, date inserted before " — a REDUCTION", checker stamp appended; "not M3, not a step-4 pass, not a TARGET.md claim" sits in Honest limits
(v) and the TARGET.md diff; (2) G2 (σ̄-change widening; Lead ruling 17:33Z: READING) appears only under Referee strengthening (0); (3) premise labels
[OPT-H], [OPT-σ̄] carried with the names later landed entries use (standing SPEC premise 1E-N3 of RESULTS R57, forms P2, P1, as RESULTS R67, R69 list
them); (4) a GAPS line-11 UPDATE is proposed (the entry is about N5 itself), built from the title clauses only. Trunk: the cited REFEREE-2 commits
1340def5 and 4e149b04 are on trunk since ac6048d8; R87 LANDED 06663fa8, R88 lands after it. Note to CHECKER only (not entry text), the removed
drafter reading: «
  neither the packet nor either referee cites these entries; not checked by a referee): W-MON's inequality is RESULTS R62 (d) Lemma WM-G
  (l. 3286: «for every transition k → k+1 of a run S, Ω_{k+1} ⊵ Ω_k pointwise», S a fallback-free run inside one phase, Ω_k := W_k), on the
  same premise (P2; RESULTS R67 l. 3463 «through WM-G and (F1) on H_k»); XW's first part is RESULTS R21 (a) Lemma XW (l. 933: «Ξ_k ⊴ W_k
  pointwise at every state»), «game-general by RESULTS R54 / R55» as RESULTS R74 lists it (l. 3895-3896); GP* and FW-R* are exact-value
  forms, with BLOCKED edges and per frozen W-phase, of the coarse Lemma P^c_sch and Corollary CHARGE-U of RESULTS R67 (e), (f) (l.
  3479-3486: COARSE values, FORBIDDEN edges, per vertex per fallback-free run with λ_W constant).»)

### R88 [refereed-only] In every frozen W-phase F = [a, b] of N5 on any game (N5-FRZ-box29 §0: no S4c fallback; τ, σ̄, λ_Ξ, λ_W constant; W = val(σ, τ)), (Lemma GP*) for every k ∈ [a, b], W_k(x) ⊵ value(r) for every simple path r of G_τ (Odd steps follow τ) with at most k − a edges from x to a W-cycle node u of F's first state a (λ_W(u) = u), none of whose Even edges (r_i, r_{i+1}) was BLOCKED at state k−1−i (W-better than σ's choice at r_i but not a VJ00-improving edge of Ξ); (Corollary FW-R*) F has at most (n−1)(R*_T+1) W-changing transitions, R*_T := the transitions of F at which some Even vertex adopts an edge blocked at an earlier state of F; so R*_T = 0 ⇒ ≤ n−1 (2026-10-29) — a REDUCTION (R*_T is not bounded here; FW-BF, G-N5-TIME open; per frozen W-phase only, not a bound on the run), CHECKER PASS (docs/checker/C97.md, checker PENDING)
- Object (L-SI successor 27, Opus 5.5, D18, Lead reading L40; frozen, unchanged during review): packet P-N5-GP,
  docs/si/P-N5-GP-box31.md, sha1 cd4866df18b55f44b3ef3d52de65943eeffe9140, 177 lines (l-si freeze
  d072bb285985f4b1f3f159b852c1514e1ca50366, 2026-10-29T16:32:35Z; `git diff d072bb28 2d0ada80` and `git diff d072bb28 88d49f87` on the
  file are empty; quote base 2a435f8f4 (2026-10-29T16:20:39Z) for SPEC, RESULTS and docs/new/N5-phase-bound-box10.md; 14 quotes,
  experiments/si/rund/quotecheck.py, sha1 29bb4a971680c9278f5f8c6f40eac17c0134db72, "quotes=14 bad=0", --mut "quotes=14 bad=14", "QUOTES
  FAIL", pinned in experiments/si/check.sh block "box 31 packet" (l. 707-710); the packet sha1 itself is not asserted in check.sh; both
  referees and L-SI (G12, l. 84) measured it): §0 what to sign (l. 13-21), §1 setting and premises, §2 Lemma W-MON and Lemma XW (proofs
  included, as the Lead asked 16:24Z), §3 Lemma GP*, §3a Corollaries GP and GP+, §4 Corollary FW-R*, §5 READING, §6 DATA and the pinned
  check (check.sh block "box 31 §6", l. 699-706). The RESULTS line: L-SI's wording, approved by the Lead (LEAD-STATE 16:23Z: «RESULTS line
  APPROVED with required tail '; per frozen W-phase only, not a bound on the run'»; the fixes file, REFEREE and REFEREE-2's §C call it the
  16:26Z line; REFEREE-2 checked it as «the Lead's 16:46Z message, verbatim; received 17:15Z», R2-N5-GP l. 132), dropped hypotheses that the
  packet's §3 has. REFEREE E-item GP-E1 (R-N5-GP l. 21, §4 l. 66-77): it «drops two hypotheses of GP* (path length L ≤ k − a; Odd steps
  follow τ)», FALSE as worded (rand0: phase [0, 0], k = 0, x = 0, path [0, 1, 7]; rand8: phase [2, 3], k = 3, x = 2 Odd, path [2, 4]).
  REFEREE-2 N-GP-7 (R2-N5-GP l. 36, §2.6 l. 132-154, l. 201-202, added at 894a1971): it drops L ≤ k − a (one-edge paths at k = a:
  b4_theta_n7.pg x = 1, z = 6; canonA_0.pg x = 3, z = 4; b5_os_n28.pg x = 1, z = 7; docs/referee-2/R2-N5-GP/line_probe.py, sha1
  1b63b083…), and «"a cycle node" should be "a W-cycle node" (λ_W(u) = u)». REFEREE-2 §C D1 (l. 33): REFEREE's G_τ point is «Correct, and I
  MISSED it». Corrected first by G0 (Lead 17:10Z; L ≤ k − a and G_τ restored, «a cycle node of F's first state» kept), then by G12 (Lead
  17:23Z: «G12 records the FINAL RESULTS line verbatim, superseding G0's line.»), which adds «F = [a, b]», «for every k ∈ [a, b]» and «a
  W-cycle node u of F's first state a (λ_W(u) = u)». The packet itself had all three (§3 l. 86-87: «A path r = (x = r_0, r_1, …, r_L = u)
  of G_τ (Odd r_i: r_{i+1} = τ(r_i))», «u is a cycle node of state a (λ_W(u) = u), L ≤ k − a»); G0 l. 9: «the 16:26Z line, my wording,
  dropped them». The title is G12's line: REFEREE §C §3 (l. 58): «MATCHES §3-§4 exactly; claims nothing beyond the signed items. (It does
  not carry G2's widening, correctly.)»; REFEREE addendum (l. 73-74): G12's line «is byte-identical (`cmp`) to the Lead's 17:23Z final
  line as received in this session (line sha1 9e6196f2…)»; REFEREE-2 §C C.3 (l. 58): «Verdict: G12's line MATCHES §3-§4 exactly. It
  claims nothing beyond the signed GP* and FW-R*» (bold in the source). Re-measured for this draft: `cmp` of fixes l. 65 against the
  Lead's 17:23Z text as briefed: identical; sha1 of the line with its newline 9e6196f2af7424ef8f7122706f3d82d6c6c82b2e.
  The referees' notes are answered by the lane in docs/si/P-N5-GP-fixes-box31.md: G0-G5 (L-SI successor 27, l-si
  6102969f8e2072b29d11e176d8f12bae35bb8085, 2026-10-29T17:09:21Z, sha1 3e6e0f33079a473fdf144a53faff73b66e45c667 there, 45 lines); G6-G11
  (successor 27, 64a3751c14ec43a4204671c5f2cf20fd9d38dcec, 17:16:19Z, sha1 65b59bbfdee71f5a953fe56b876554b599c88178 there, 65 lines;
  `git diff --numstat 6102969f 64a3751c`: 22 added, 2 removed); G12 (L-SI successor 28, 2d0ada80141b68cec1a4a0bed4c291b29434fdf2,
  17:26:17Z, sha1 f901b5090d036e8428ae77c68d6f8f59049c43e2, 89 lines, = trunk 88d49f87; `git diff --numstat 64a3751c 2d0ada80`: 26 added,
  2 removed). In each append the 2 removed lines are the old trailing DONE / FINDINGS / NEEDS footer, rewritten in place: not a G-item
  (G0-G5, l. 1-42, hash identically at 6102969f and 2d0ada80; REFEREE addendum l. 71-72: «the two removed lines are the old DONE/FINDINGS
  footer. G0-G11 untouched (the file's first 60 lines hash identically at 64a3751c and 2d0ada80)»; L-SI's record, docs/si/N5-RTC-box32.md
  l. 118-119: «I edited the existing DONE / FINDINGS / NEEDS footer when adding G12 (2d0ada80) instead of appending a new one.»). No quote
  check is pinned for the fixes file; its quotes were checked by the referees (REFEREE-2 §C C.4 G6: «matches box10 l. 34-35 at 2a435f8f4
  word for word (checked)»). G0 records the 16:26Z-corrected line, G1 and G7 name the standing premises, G2 the σ̄-change widening (Referee
  strengthening (0)), G3 renames §4's transition index τ to s, G4 the data scope, G5 = G8 B1′ (i) for both parities of c, G6 [CASE-A]'s
  elided parenthetical in full, G9 B1′'s cycle shape, G10 §3a's "directly", G11 R_T ≥ R*_T, G12 the final line with a word-by-word table
  against §3 (l. 70-83). The statements below are in the frozen wording, read with G3 (and G5, G6, G8-G10 in the proofs).
  Setting (every game): N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) with FIX 1-4; G = (V, E, Ω, owner), n = |V|; a run is the sequence
  of states (σ_t, τ_t), a TRANSITION is t → t + 1. Values (c, P, ℓ) and the order ⊴ (◁ strict) as in [S1-val], [S1-ord]; Ξ_t := Ξ_{σ_t}
  against S1's optimal counterstrategy σ̄_t ([S1-Xi]); Iσ_t := [S2]'s improving edges; W_t := the valuation [S1-val] of the (σ_t,
  τ_t)-plays, λ_W its cycle-node map, λ_t := Ξ_t's. A PHASE: a maximal run of states with (λ_t, τ_t) constant (RESULTS R38 (a)). [FRZ]
  (l. 64-68, docs/si/N5-FRZ-box29.md §0 restated): «A frozen W-phase F = [a, b] is a maximal run of consecutive states of one phase such
  that no transition t → t + 1 with a ≤ t < b is an S4c fallback, changes λ_W, or changes σ̄.» On F: τ, σ̄, D := {Odd u : σ̄(u) ≠ τ(u)},
  λ_Ξ and λ_W constant; ρ_t := σ_t; G_τ := G with Odd fixed to τ; W_t = Ω_{ρ_t} in G_τ. [H] (l. 69): H_t := S4a's arena at t (Even v
  keeps {ρ_t(v)} ∪ Iσ_t(v), Odd v keeps τ(v)), a one-player game. value(r) := (u, P(r), L) for r = (x = r_0, …, r_L = u) ([VAL], R17's
  object). §1 cells: REFEREE «CHECKED» (l. 14); REFEREE-2 «SIGNED (well formed; 13/14 quotes strictly verbatim, the 14th a faithful
  elision: N-GP-1)» (l. 29); both §Cs: "same content" (REFEREE §C l. 13), "agreed" (REFEREE-2 §C l. 16).
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 18, REFEREE-2 successor 20). Each item below is SIGNED in both verdict
  tables (REFEREE "## Verdicts", l. 11-23 of R-N5-GP.md; REFEREE-2 "## 0. Verdicts", l. 26-39 of R2-N5-GP.md; REFEREE §C table l. 10-21
  "SIGNED" in the joint column; REFEREE-2 §C C.1 l. 13-25 "SIGNED by both"), in the frozen wording read with G3. Every frozen W-phase of
  every game; no item uses (P). Premises LANDED: SPEC S1 ([S1-val], [S1-ord], [S1-Xi]), S2, S4a, S4c (quote base 2a435f8f4); RESULTS R15
  (d) ([STEP]); RESULTS R17 (a) [F1], [V1], [V2], with [PRE], [VAL] and R17 (b)'s Cases A, B (box10 l. 13-39 at 2a435f8f4) as the proof
  pattern GP* re-does; RESULTS R38 (a), as the phase definition only; RESULTS R84 (a) Fact DELTA (distinct values are distinct in the order,
  l. 31-32); RESULTS R57 (a) premise (VJ), for XW's first part (G7; REFEREE-2 cell «R57 (a)'s (VJ) premise»). Standing premises, named by
  G1 and G7 (disclosure, not a widening; REFEREE GP-N1, REFEREE-2 N-GP-2; both §Cs: CLARIFICATION, REFEREE-2 §C D7 «E-light (discharged
  by G1, G7)»):
  [OPT-H] (G1 l. 14-15): «the S1 procedure applied in S4a returns an optimal strategy of the one-player arena H_t (Even's one-player optimum
  against τ, pointwise), as used and signed in RESULTS R17 (e) for N5's step»; G7 (l. 48-50) adds «the exact order reversal between G^d
  and G and the SPEC-conformance premise (R57 (b)); together these are G1's [OPT-H]». It is the standing SPEC premise 1E-N3 (RESULTS R57
  (b), l. 2915-2916) in the form RESULTS R67 calls P2 (l. 3462-3463: «P2, S4a's σ_{k+1} is Even's pointwise optimum in its arena H_k»; also
  RESULTS R69, l. 3596). RESULTS R17 (e) (l. 747) is the one-player case («N5's step for the other player is switch-best»; REFEREE §1
  l. 28-30: «the same premise R17 (e) uses …, here for the one-player ARENA H_t»).
  [OPT-σ̄] (G1 l. 16-18): «σ̄_t is an optimal counterstrategy at every vertex at once and realises Ξ_t as the values of the (σ_t,
  σ̄_t)-plays (RESULTS R57 (b)'s standing premise: «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance»)» (R57
  (b), l. 2915-2916 at 88d49f87); its optimality half is 1E-N3's form P1 (RESULTS R67 l. 3462: «P1, S1's σ̄_k is Odd's pointwise optimum
  in G_{σ_k}») and, for XW's first part, R57 (a) (VJ) (G7 l. 50-51: «XW's first part is R57 (a)'s (VJ) premise»).
  Use (G1 l. 19, confirmed by REFEREE §C l. 39 «G1's split is right»): GP* uses [OPT-H] (through W-MON and [F1]) and not [OPT-σ̄]; XW
  and GP+ use [OPT-σ̄]; FW-R* uses GP*, W-MON and [S4a]; GP uses XW.
  (a) Lemma W-MON (§2, l. 72-73), premise [OPT-H]: "Let t → t + 1 be a transition inside a phase that is not an S4c fallback. Then ρ_{t+1}
      is an optimal strategy of H_t in G_τ's valuation, and W_{t+1}(v) ⊵ W_t(v) for every v." (τ_{t+1} = τ_t in a phase; [STEP] makes σ
      change; not a fallback, so σ_{t+1} = S4a's σ_new with Iσ_t ≠ ∅, Even's one-player optimum of H_t against τ; the (σ, τ)-plays of G
      and H_t coincide for ρ_t and ρ_{t+1}; [F1] in H_t.) Cells: REFEREE «SIGNED (premise: S1's procedure returns an optimal strategy of
      the one-player arena, GP-N1)» (l. 15); REFEREE-2 «SIGNED (with the standing premise that S4a's σ_new is the one-player optimum:
      N-GP-2)» (l. 30).
  (b) Lemma XW (§2, l. 78-79), premise [OPT-σ̄]: "Ξ_t(v) ⊴ W_t(v) for every v and t; and Ξ_t(v) = W_t(v) whenever the (σ_t, τ_t)-play
      from v meets no vertex of D_t := {Odd u : σ̄_t(u) ≠ τ_t(u)}." (Ξ_t is against σ̄_t, which minimises at every vertex at once, and τ_t
      is one Odd strategy; a play avoiding D_t is the same play under τ_t and σ̄_t.) Cells: REFEREE «SIGNED (premise: σ̄_t is an optimal
      counterstrategy at every vertex at once, GP-N1)» (l. 16); REFEREE-2 «SIGNED (the first part is SPEC S1-Xi's "minimising at every
      vertex at once", i.e. R57 (a)'s (VJ) premise: N-GP-2)» (l. 31).
  (c) Lemma GP* (§3, l. 85-89): Definitions: «An edge (x, z) of G with x Even is BLOCKED at state t ∈ [a, b) if W_t(z) ▷ W_t(ρ_t(x)) and
      (x, z) ∉ Iσ_t. A path r = (x = r_0, r_1, …, r_L = u) of G_τ (Odd r_i: r_{i+1} = τ(r_i)) is UNBLOCKED AT STATE k (a ≤ k ≤ b) if it is
      simple, u is a cycle node of state a (λ_W(u) = u), L ≤ k − a, and for every i < L with r_i Even the edge (r_i, r_{i+1}) is not
      blocked at state k − 1 − i.» "Lemma GP*. For every k ∈ [a, b] and every path r unblocked at state k: W_k(r_0) ⊵ value(r)." (Induction
      on k; L = 0 by λ_W constant; for r = x → z → r′, r′ is unblocked at k, IH W_k(z) ⊵ value(r′), W-MON W_{k+1} ⊵ W_k. Case A (x Odd, z =
      ρ_k(x), or (x, z) ∉ Iσ_k and not blocked, so W_k(z) ⊴ W_k(ρ_k(x))): R17 (b)'s Case A with Ω := W. Case B ((x, z) ∈ Iσ_k): ρ̂ :=
      ρ_k[x → z] ∈ H_k, so W_{k+1}(x) ⊵ val_ρ̂(x) by W-MON's first part and [F1]; «The improvement of (x, z) is in Ξ, not in W; it is NOT
      used below.» (l. 99-100); sub-cases B1, B1′ (i)-(iii), B2a, B2b (i)-(iii); the three configurations in which λ_W(x) would change
      are «impossible in F»; the three NEW ones (B1′ (iii), B2b (ii), B2b (iii) with c even) close by Case A's A1 or a direct comparison.)
      Cells: REFEREE «SIGNED. Every R17 (b) sub-case is redone without the improvement (§2 below)» (l. 17); REFEREE-2 «SIGNED. Every R17
      (b) sub-case is redone without the Ξ-improvement in Case B (the key point, §2.3)» (l. 32). Both re-derived each sub-case against
      box10 l. 29-55 (REFEREE §2 table l. 43-48; REFEREE-2 §2.3 l. 66-96; REFEREE §C l. 22-24: «checked independently by both … with the
      same sub-case partition and the same three new sub-cases»). G5 = G8 (B1′ (i) holds for c of either parity), G6 (the elided
      parenthetical of [CASE-A], box10 l. 34-35, in full) and G9 (Z is a simple cycle) are clarifications accepted by both (REFEREE §C
      l. 43-45; REFEREE-2 §C C.4 l. 75-79).
  (d) Corollary GP (§3a, l. 126-132), with G10: Definitions (state t ∈ [a, b)): U_t := the vertices whose (ρ_t, τ)-play meets no vertex of
      D; S_{d,t}, SAME-PAIR (λ_Ξ(d) = λ_W(d)), TAIL-DISJOINT at t; «ALLOWED(x, t) := {ρ_t(x)} ∪ Iσ_t(x) ∪ (x's successors in U_t)»; TIMELY
      AT STATE k: «unblocked» with «not blocked at state k − 1 − i» replaced by «r_{i+1} ∈ ALLOWED(r_i, k − 1 − i)». "Corollary GP. W_k(r_0)
      ⊵ value(r) for every path r timely at state k." (No z ∈ ALLOWED(x, t) is blocked at t: z = ρ_t(x) by definition; Iσ_t edges by
      definition; z ∈ U_t: W_t(z) = Ξ_t(z) (XW, second part) ⊴ Ξ_t(ρ_t(x)) ([S2]) ⊴ W_t(ρ_t(x)) (XW); then GP*.) G10: «each also follows
      from §3's Case A / Case B directly» (packet §0) means «run §3's induction with «timely (timely⁺) at state k» … in place of «unblocked
      at state k»»; «§3a's proof (reduction to GP*) is the one to sign». Cells: REFEREE «SIGNED» (l. 18); REFEREE-2 «SIGNED» (l. 33).
  (e) Corollary GP+ (§3a, l. 128-132): «ALLOWED⁺(x, t) := ALLOWED(x, t) ∪ {z successor of x : x, z ∈ S_{d,t} for a same-pair gate d
      tail-disjoint at t}»; "Corollary GP+. The same for every path timely⁺ at state k." (Inside S_{d,t}: W_t(y) = p(y) ⊕ W_t(d) and Ξ_t(y)
      = p(y) ⊕ Ξ_t(d) with the same cycle node c; p ⊕ A vs q ⊕ A does not depend on A; so Ξ_t(z) ⊴ Ξ_t(ρ_t(x)) gives W_t(z) ⊴ W_t(ρ_t(x)).)
      Cells: REFEREE «SIGNED» (l. 19; §3 l. 59: «(Ξ as a play value of (ρ_t, σ̄): GP-N1.)»); REFEREE-2 «SIGNED» (l. 34).
  (f) Corollary FW-R* (§4, l. 144-148), with G3: «A LATE ADOPTION in F is a transition τ → τ + 1 of F (a ≤ τ < b) at which some Even y
      switches, ρ_{τ+1}(y) = z ≠ ρ_τ(y), to an edge (y, z) that was blocked at some state t ∈ [a, τ). R*_T := the number of transitions of F
      containing at least one late adoption. WCH := the number of transitions t → t + 1 of F with W_{t+1} ≠ W_t.» G3: «read the transition
      index τ as s throughout». "Corollary FW-R*. Every frozen W-phase F of N5 on every game has WCH ≤ (n − 1)(R*_T + 1). In particular, if
      no previously blocked edge is ever adopted in F (R*_T = 0), then WCH ≤ n − 1." (At most n − 1 W-changes at k < a + n − 1; for k ≥ a
      + n − 1 with W_{k+1}(x) ≠ W_k(x), x's ρ_{k+1}-play π to u = λ_W(x) has L ≤ n − 1 ≤ k − a and value(π) = W_{k+1}(x); unblocked would
      give W_k(x) = W_{k+1}(x) by GP* and W-MON; so some Even edge of π is blocked at t = k − 1 − i ≥ a; by [S4a] ρ_{t+1}(y_i) ∈ {ρ_t(y_i)}
      ∪ Iσ_t(y_i), so y_i adopts it at a late adoption s with t < s ≤ k, k − s ≤ n − 2; each s is charged by at most n − 1 values of k.)
      Cells: REFEREE «SIGNED» (l. 20); REFEREE-2 «SIGNED» (l. 35, row "Corollary FW-R*: WCH ≤ (n − 1)(R*_T + 1) per frozen W-phase").
  The RESULTS line: the 16:26Z line DOES NOT MATCH in both reports (REFEREE l. 21, REFEREE-2 l. 36; REFEREE §C l. 20 and REFEREE-2 §C l. 23:
  «E-item = union of GP-E1 and N-GP-7»); G12's final line MATCHES (REFEREE §C §3 l. 55-58 and addendum l. 73-76; REFEREE-2 §C C.1 l. 24
  «MATCHES §3-§4 (C.3)», «the line to land», C.3 l. 45-65). The line omits W-MON, XW, GP and GP+ (REFEREE-2 l. 152: «That is fine: a line
  may claim less.»); they are signed items (a), (b), (d), (e) above.
- Not signed: §5 (READING, «NOT to sign», packet table l. 20): D = ∅ (nothing blocked, R*_T = 0, FW-R* gives ≤ n − 1; box 29 Corollary
  FW-D0); edges into U_k and inside one same-pair tail-disjoint basin never blocked; «the blocked edges are the F1 refusals of
  docs/si/N5-TORD-box30.md §9»; and its "Not claimed" list (l. 164-166). §6 (DATA, «NOT to sign», l. 21) with G4's scope (Data below).
  The superseded RESULTS lines (16:26Z; G0's): not this entry's title. G2 (the σ̄-change widening): Referee strengthening (0). G11's R_T
  (FW-R′ of docs/si/N5-SPC-box31.md §4): another quantity, R_T ≥ R*_T, so an R_T line «would be implied by FW-R*, but weaker»; not a
  statement of this entry. Lane statements outside the packet (docs/si/N5-FRZ-box29.md Theorem W-SPLIT «PROVED (lane), a REDUCTION»,
  CONJECTURES FW-BF and FW-LEN; docs/si/N5-RTC-box32.md R*-TC): not refereed here.
- Referee strengthening (NOT part of this entry; remarks of one or both referees outside the verdict cells, or optional wording):
  (0) G2 = GP-N2 (G2 l. 22-25): «GP*'s proof uses only: τ constant, no S4c transition, and λ_W constant on [a, k]. λ_Ξ and σ̄ constant are
  not used. So GP* (and FW-R*, whose proof uses GP*, W-MON and λ_W constant) hold on every maximal run of in-phase states with those three
  properties (a stretch that may contain σ̄-changes)»; the lane labels it «a READING of its proof, PROVED (lane) by the same text».
  REFEREE §C l. 40: «WIDENING … I re-checked: neither proof uses σ̄ constant … so it is TRUE; but it is not part of the signed statement.
  To land it as a result it needs both referees' signature on its own wording»; addendum l. 77-78: «G2 (Lead ruling 17:33Z, recorded): it
  stays a READING, outside the entry, under "Referee strengthening (NOT part of this entry)"; re-checked TRUE by REFEREE (§2 above), signed
  by one referee only.» Lead ruling (LEAD-STATE 17:34Z entry): «G2 = TRUE widening (σ̄-changes allowed) signed by one referee → Lead
  RULING: READING, not in the entry (Referee strengthening only)». REFEREE-2 §C (written after the ruling) D4 l. 36: «True: §2.3 of my
  report used exactly those … G2's "hold on every maximal run … with those three properties" WIDENS the statement. The Lead ruled it a
  READING outside the entry; I agree», class «opt (READING, outside the entry)»; C.4 l. 72: «True by the same proof», «WIDENING
  (one-referee)». Neither verdict table carries it; no signed item uses it.
  (i) G11 = N-GP-6: R_T ≥ R*_T «because every blocked edge is outside ALLOWED⁺ (§3a)» (REFEREE §C l. 47 «correct by §3a's proof»;
  REFEREE-2 §C C.4 l. 81). (ii) REFEREE-2 §2.4 l. 113-114, on GP+: «(equality transfers too)»; «Should GP* need repair, the four cases
  still give "not blocked", but GP* is needed to conclude.» (iii) REFEREE §2 l. 51 = REFEREE-2 §C D4: the hypotheses GP* uses of F
  (the content of (0)). (iv) G12's two readings (l. 82-83), «both forced by the packet»: «Even edges» = edges with an Even tail; W, σ, Ξ
  in the line's parenthetical are read at the state k − 1 − i (REFEREE addendum l. 75-76 «no widening»; REFEREE-2 §C l. 54-56).
- Honest limits: (i) FW-R* is a REDUCTION per frozen W-phase: R*_T is NOT bounded here (packet SCOPE l. 9-10: «R*_T is NOT bounded here;
  FW-BF and G-N5-TIME stay OPEN»); CONJECTURE FW-BF (≤ n − 1 W-changing transitions per frozen W-phase, docs/si/N5-FRZ-box29.md §4 l. 82)
  stays open; R*_T = 0 gives FW-BF for that phase only. DATA (packet §6, not refereed): largest R*_T 40 (grow_K40_n373, n 373, WCH 45);
  REFEREE-2 alt_all max R*_T 40, WCH 49. (ii) Per frozen W-phase only, not a bound on the run (packet §5 l. 164-166: «Not claimed: any
  bound on R*_T; FW-BF (≤ n − 1 per frozen W-phase) in general; any bound on |F| (W-silent transitions) or on the number of frozen
  W-phases (fallbacks FB, σ̄-changes SBCH′: box 29 W-SPLIT); anything about the whole run. FW-R* feeds box 29's W-SPLIT per frozen W-phase,
  not R86 COMPOSE's NM*/P*.»). It does not bound RESULTS R86's NM* or NM*^U: notes/L-SI.md l. 40: «FW-R* feeds box 29's W-SPLIT per frozen
  W-phase, not R86 COMPOSE's NM*/P*; gaps to the run: FB-LIN, SBCH′, FW-LEN»; docs/si/N5-RTC-box32.md §4 l. 94-96: «R86 COMPOSE (NM* /
  NM*^U): those count PHASES (τ- and λ-changes) along the run, and R*-TC / FW-R* live strictly inside one frozen W-phase (τ, σ̄, λ constant).
  They give nothing for NM* or NM*^U.» The gaps to the run are lane quantities, all OPEN and unrefereed: FB-LIN (fallbacks per phase,
  CONJECTURE, docs/si/N5-ALT-box23.md l. 325), SBCH′ (λ_W-keeping σ̄-changes per phase, OPEN, docs/si/N5-FRZ-box29.md l. 21), FW-LEN
  (< n + m transitions per frozen W-phase, CONJECTURE, same file l. 82-83), assembled by W-SPLIT (lane).
  (iii) WCH counts transitions, not bit operations; no running-time bound. (iv) [OPT-H] and [OPT-σ̄] are SPEC-conformance premises
  (1E-N3); the code's match to SPEC is DATA (R15 G-N5T-1, as R57 (b)). (v) Not M3, not a step-4 pass, not a
  TARGET.md claim; G-N5-TIME stays open.
- Data (DATA, not proof): pinned (packet §6; experiments/si/core/gp.py, sha1 270f247cf24779e22d7cd441b9f9e0de8c38c363; check.sh block
  "box 31 §6", l. 699-706; instances xing/instances/ccl_w48_n48.pg a7056dea01cd9c6398e054ef6edaaa40f60dabb1, core/instances/rlin_cex_n40.pg
  670ba1ffc22c8f9b170e11ca3e43c33cee9329ca, start e488c00fe1359818b9a665a415cc7b2962015318; all equal at d072bb28 and trunk). Re-run for
  this draft at the local merge ac6048d8 (box-31 files identical to d072bb28; experiments/si, `python3 -I`, outputs to scratch files, exit
  codes read): STAR=1 rlin_cex_n40 (+ start) «'D1': (0, 10, 10, 40, 1, 'core/instances/rlin_cex_n40.pg', 1, 11)», GP PASS, RED PASS, RLIN
  PASS, rc 0; STAR=1 ccl_w48_n48 «'D1:R_T/(n-1)': (0.02127659574468085, 1, 3, 48, 1, 'xing/instances/ccl_w48_n48.pg', 15, 18)», GP PASS,
  rc 0; MUT=all STAR=1 ccl_w48_n48 GP FAIL (EXAMPLE ('GP', 'D1', 'xing/instances/ccl_w48_n48.pg', 15, 18, 18, [9, 22])); quotecheck
  «quotes=14 bad=0», QUOTES PASS; --mut «quotes=14 bad=14», QUOTES FAIL. All as check.sh asserts. Packet corpora (§6, lane DATA): GP* 0
  violations on 2,235 frozen W-phases (1,754 with D ≠ ∅ and every gate same-pair, 481 with D = ∅); FW-R* never fails; R*_T = 0 in 1,499 of
  the 1,754; MUT=all fails on ccl_w48_n48 and runlin/instances/runfam_K100. G4 (data scope): «core/gp.py does not enumerate paths: it runs a
  path-tracking Bellman-Ford that keeps ONE best unblocked simple path per vertex and length bound», so «the GP* data … cover only these
  stored paths, not all unblocked paths. FW-R*'s data (WCH, R*_T, the RED check) are complete counts.» REFEREE (successor 18; own
  scratch/gp_probe.py, sha1 b4142cc7…, on its engine rl_engine, no lane code; pinned blocks re-run from a clean worktree at d072bb28, exit
  0): pins (ccl_w48_n48, rlin_cex_n40 + start, runfam_K100 + start) 5 runs, 71 frozen W-phases (67 with D ≠ ∅), 100,483 GP* path checks,
  W-MON / XW 78,030 / 83,459, max R*_T / WCH 1 / 123; library (n ≤ 40) 321 runs, 3,434 (2,804), 332,322, 78,720 / 173,927, 2 / 36; random
  rand_ck n 5-14 6,000 runs, 14,852 (6,588), 33,388, 9,585 / 154,935, 0 / 3; 0 violations; «No frozen W-phase in my data has WCH > n − 1»;
  DFS budget hit at many (F, k) on the pins and at some on the library («the GP* check covers only the enumerated paths (GP-N4)»); controls
  MUT=1 (no L ≤ k − a) 27,724 and MUT=2 (Odd steps off τ) 93 violations on 2,000 random runs, MUT=3 (blocked edges allowed) 756 on
  ccl_w48_n48 at [15, 18]: «So each of GP*'s three path conditions is needed.» REFEREE-2 (successor 20; own R2-N5-GP/gp_check.py, sha1
  f3bb3f92…, on its lane's dual_check.Runner and si.py; lane code only run as check.sh l. 699-710 from a detached worktree at d072bb28,
  never imported; PCAP 300 paths per (k, x)): random n 4-14 12,000 runs, 29,440 frozen W-phases, 63,315 GP* paths; random n 15-30 1,200,
  4,326, 11,430; alt_all 93, 1,970, 887,036, max R*_T / WCH 40 / 49; lib41_noref 650 (+170 with counters lost), 6,732, 3,446,322, 3 / 55;
  ccl_w48_n48 1, 39, 89, 1 / 3; rlin_cex_n40 1, 4, 58,296, 0 / 10; runfam_K100 (n 139) 2, 23, 6,909,085, 1 / 123 (bound 276); 0
  violations of WMON, XW, GPS, F1H, IMP, NOTBL, FWR; plain W-frame Lemma P (X_GPall) fails 344,537 (lib41), 125,338 (alt_all), 10,196
  (runfam_K100), 2 (ccl_w48_n48). NODECAP disclosure (l. 172, 177-182, added at 2d54649d and 1340def5): lib41 chunks 0, 5, 7 stalled on
  b6_xs_n40, xsnf42_n48, x32_rand64 and were stopped (85 files, 170 runs, «0 VIOLATION lines printed, but their counters were lost»); their
  remaining 67 files re-run with NODECAP = 20,000 DFS nodes per (k, x), «which truncated 18,437 enumerations (counted)»; runfam_K100
  «NODECAP 20,000, 66,110 truncated enumerations»; «GP*'s path enumeration partial on the dense ones; WMON, XW, F1H, IMP, NOTBL and FWR are
  exhaustive per state». Sub-case census: the NEW sub-cases occur (alt_all B1′ (iii) 4, B2b (ii) 41, B2b (iii) c even 66; lib41 B2b (ii)
  24, B2b (iii) c even 384, B1′ (iii) 0); «the impossible ones 0». REFEREE-2 §C C.3 l. 62-65: the final line's family «is exactly the
  family my gp_check.py GPS check enumerates»; «0 violations over 11.4M paths …, with the NODECAP truncations disclosed there». Run
  counts: REFEREE-2 §C D11 says «REFEREE: 6,326 runs, 466,193 GP* path checks» (= REFEREE's three rows) and «Mine: 14,117 runs (+170
  without counters)»; its §3.2 table rows sum to 13,947 runs, and 13,947 + 170 = 14,117: not reconciled by REFEREE-2. No signed statement
  uses any count.
- Signatures: REFEREE docs/referee/R-N5-GP.md (report 7dffab644b5b7ca58455f9e5fbec8eaaae3825fb, 2026-10-29T16:56:42Z, sha1
  b2b4cffa3b6257164ff68097854b31cac27b4ee2, 117 lines, = trunk; successor 18); §C docs/referee/R-N5-GP-C.md (fee33b06, 2026-10-29T17:25:20Z,
  sha1 45e9227e4f36e1daa2556c8da6d767c3a9ade121 there, 66 lines; addendum 18417cef, 2026-10-29T17:40:34Z, append-only (`git diff --numstat
  fee33b06 18417cef`: 13 added, 0 removed), sha1 943ff66aa0649c4f81183f150d24a7d9d1c569f9, 79 lines, = trunk): §1 CHECKED; W-MON, XW,
  GP*, GP, GP+, FW-R* SIGNED; 16:26Z line DOES NOT MATCH (GP-E1); §5, §6 not signed, pins exact; «No gap in the packet. One E-item, on the
  RESULTS line only (GP-E1). Notes GP-N1..N5.» (l. 23). REFEREE-2 docs/referee-2/R2-N5-GP.md (report 4835eb3dadb1f9fbb165d7c9c98e3e2117125193,
  2026-10-29T17:08:14Z, sha1 9f91fda98fd93d75d3a4fc3df610de589e9eb268 there, 189 lines; 894a1971, 17:16:25Z, sha1 e4a16a0b… there, 208
  lines (30 added, 11 removed: the "NOT CHECKED" line row, the pending §2.6, the old N-GP-6 first line and the old FINDINGS / NEEDS lines
  replaced by the line check, N-GP-7 and new lines; no signed row changed); 2d54649d, 17:54:25Z (lib41 row, 8 added, 1 removed: the
  "pending" row); 1340def5b3d26c456c36b11e52764a29aa39f032, 18:00:49Z (runfam_K100 row, 1 added, 1 removed), sha1
  ee728542a3451b9ee0bd3f6c7421e82fba2ed329, 215 lines, = claude/referee-2 head; successor 20); §C docs/referee-2/R2-N5-GP-C.md
  (4e149b046394ec040f87f827522187afce7ebdbc, 2026-10-29T18:08:49Z, sha1 423dc919ab3a8859e4d9a49a91f7d029262b1cf4, 93 lines): §1 SIGNED;
  W-MON, XW, GP*, GP, GP+, FW-R* SIGNED; 16:46Z line DOES NOT MATCH (N-GP-7); §5, §6 not signed, pins exact; «No gap. No item FALSE.»
  (l. 39). INDEPENDENCE: REFEREE l. 6: «Independence: no REFEREE-2 GP file opened.»; REFEREE §C l. 3-4: REFEREE-2's report (4835eb3d plus
  894a1971) «read only after the Lead's word (my report pushed first)». REFEREE-2 l. 13-14: name count of GP files under docs/referee/ on
  origin/claude/referee «= 0 at 16:41:06Z; 14 at 17:08:13Z (push turn, after a fresh fetch). Names only. No docs/referee/ file opened.»;
  REFEREE-2 §C l. 6-7: REFEREE's report «First opened 18:08Z; my report was pushed at 17:08Z (4835eb3d) and completed at 1340def5»; l. 11:
  «I have not read REFEREE's §C (fee33b06).» No review imported lane code.
  §C (both): verdicts identical (REFEREE §C l. 22: «VERDICTS IDENTICAL on all six signed items; no gap; nothing FALSE in the packet»;
  REFEREE-2 §C C.1: "SIGNED by both" on all six rows); joint gap map empty (REFEREE §C l. 26: «JOINT GAP MAP (packet): EMPTY.»; REFEREE-2
  §C l. 27: «Joint gap map for the packet: EMPTY.»); the one E-item is on the RESULTS line, the union GP-E1 ∪ N-GP-7 of three defects (L ≤
  k − a, both; path of G_τ, REFEREE only; W-cycle node, REFEREE-2 only), discharged by G12 (REFEREE §C l. 26-30, addendum; REFEREE-2 §C
  D1-D3 l. 33-35 «E (discharged …)»). Fixes: REFEREE §C l. 48: «G0-G11 change no signed statement. G2 is the one WIDENING (true, but
  unsigned as a result); all others are clarifications or DATA.»; addendum l. 76: «G12 is a CLARIFICATION (records the line).»; l. 79:
  «Nothing open on P-N5-GP.» REFEREE-2 §C l. 84: «G0-G12 ACCEPTED. G2 is the only widening, and it stays a READING outside the entry, per
  the Lead.»; C.5 l. 93: «NEEDS: none. Land P-N5-GP with G12's line.»
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a per-frozen-W-phase lower bound on W along unblocked paths and a REDUCTION of
  a frozen W-phase's W-changing transitions to R*_T, which is not bounded; no bound on a phase or a run, no running-time bound, no algorithm
  claim). GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), after the R86 UPDATE of G-N5-TIME (GAPS l. 11), built only from the title clauses (landing time
and CHECKER addendum to be filled at landing): «UPDATE 2026-10-29 <HH:MM>Z: RESULTS R88 (P-N5-GP; CHECKER C97 Add. <k>) [refereed-only]
LANDED: in every frozen W-phase F = [a, b] of N5 on any game (no S4c fallback; τ, σ̄, λ_Ξ, λ_W constant; W = val(σ, τ)), for every k ∈
[a, b], W_k(x) ⊵ value(r) for every simple path r of G_τ with at most k − a edges from x to a W-cycle node of F's first state none of whose
Even edges was BLOCKED at state k−1−i (W-better than σ's choice but not a VJ00-improving edge of Ξ) (Lemma GP*); so F has at most
(n−1)(R*_T+1) W-changing transitions, R*_T the transitions of F at which some Even vertex adopts an edge blocked at an earlier state of F,
and R*_T = 0 ⇒ ≤ n−1 (Corollary FW-R*): a REDUCTION per frozen W-phase only, not a bound on the run; R*_T is not bounded here; FW-BF stays
open. G-N5-TIME stays open.»
