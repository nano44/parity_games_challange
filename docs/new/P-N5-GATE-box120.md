# P-N5-GATE (box 120): the settled set and the bracket never move back; a τ-stretch is R17's one-player climb except at inconsistent steps — a referee packet from L-NEW boxes 117-118
Frozen 2026-11-01 (date -u: see the commit), L-NEW successor 43. For REFEREE and REFEREE-2.
- Scope: REDUCTIONS / EQUIVALENCES and one DEAD at an explicit bound.
  - No count is bounded here. G-N5-TIME stays OPEN. This is not M3, not a step-4 pass and not a TARGET.md claim.
- The sandwich itself is NOT claimed here: it is landed RESULTS R18 (d) Lemma S (a)-(b) (box 21 §2.2), with Lemma R. This packet uses it as a
  premise (§1 [SQZ]).
- Source notes (history only): docs/new/N5-SQUEEZE-box117.md (l-new 401d283a, erratum 5ea2e738) and docs/new/N5-GATE-box118.md
  (l-new 5ea2e738). This packet restates everything it uses; the notes are not needed to check it.
- To sign: §2 Corollary SETTLE-MON; §3 Corollary BRACKET-MON; §4 SETTLE-RED and BRACKET-RED; §5 Lemma CONSISTENT-RED with its Corollary;
  §6 the DEAD (an instance check, explicit bound n − 1).
- Not to sign: §7 (DATA), §8 (READING).
- Line: docs/new/P-N5-GATE-line.txt (one line, no heading marker).

## 1. Setting, premises
- N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) on an arbitrary game G, n := |V|, m := |E|. A run is the sequence of states (σ_k, τ_k),
  k = 0..K; a transition is k → k + 1 (0 ≤ k < K), a FALLBACK if S4c fired at it.
- Values, ⊴ (Even's order), ◁, ▷ as in SPEC S1; Ξ_k := Ξ_(σ_k) (valuation under σ_k and Odd's optimal counterstrategy σ̄_k).
  Iσ_k := SPEC S2's improving set of σ_k.
- LO_k(v) := Ξ_k(v). HI_k(v) := Ξ^d_(τ_k)(v), the valuation of v under τ_k and Even's optimal counterstrategy on G^d (SPEC S1 on G^d), as a
  triple (c, P, ℓ) of G (RESULTS R18 (d) Lemma R: a play has the same triple in G and G^d, and G^d's order is the reverse of G's).
  W_k(v) := the valuation of the (σ_k, τ_k)-play from v.
- G_τ := the one-player game with Odd fixed to τ (Odd vertex o keeps only (o, τ(o))). For a transition k → k + 1 with τ_(k+1) = τ_k:
  IW_k := SPEC S2's formula applied to σ_k in G_τk, i.e. {(y, z) : y Even, z ≠ σ_k(y), W_k(z) ▷ W_k(σ_k(y))} (VJ00 §4.4 eq. (2) in G_τk).
- A τ-STRETCH is a maximal set of consecutive transitions k → k + 1 with τ_k = τ_(k+1) all equal. A transition of a τ-stretch is CONSISTENT if it is
  not a fallback and Iσ_k = IW_k; otherwise INCONSISTENT. INC := the number of inconsistent transitions of the stretch.
- CS(x) := RESULTS R93 (a)'s coordinate sequence of a value x (length n + 2; lexicographic order of CS = ⊴); lcp := length of the longest
  common prefix.
- Premises:
  - [SPEC] SPEC S4 with FIX 3: for every Even y, σ_(k+1)(y) ∈ {σ_k(y)} ∪ Iσ_k(y) (S4a's arena; S4c's Even branch picks from Iσ_k); for every
    Odd o, τ_(k+1)(o) ∈ {τ_k(o)} ∪ Iτ_k(o) (S4b's arena; S4c's Odd branch picks from Iτ_k, only when Iσ_k = ∅); a transition at which
    S4a and S4b change nothing is a fallback.
  - [1E-N3] the standing SPEC premise of RESULTS R57: S1's procedure realises the pointwise optimum; for S4a at k → k + 1, σ_new is a
    pointwise optimum of the one-player arena H_k (Even y keeps {σ_k(y)} ∪ Iσ_k(y), Odd follows τ_k).
  - [SQZ] RESULTS R18 (d) Lemma S (a)-(b) with Lemma R, on every game (box 21 §2.2: the proof uses VJ00 (11) on G and G^d and R15 (a);
    no 𝒞^1O hypothesis): for every k and v, LO_k(v) ⊴ W_k(v) ⊴ HI_k(v); LO_k(v) ⊴ LO_(k+1)(v); HI_(k+1)(v) ⊴ HI_k(v). (The HI half uses
    [SPEC]'s Odd arena: τ moves only along Iτ.)
  - [LEX] RESULTS R93: ⊴ is a linear order; R93 (a): CS is order-preserving and injective.
  - [SAND] RESULTS R99 (Lemma SANDWICH): for sequences x ≤ y ≤ z of one length in lexicographic order, lcp(x, z) = min(lcp(x, y), lcp(y, z)).
  - [R17] RESULTS R17 (b)-(d): on a one-player game, switch-best (ρ_(j+1) := a pointwise optimum of the arena {ρ_j(x)} ∪ I_j(x), I_j :=
    VJ00's improving edges of ρ_j) makes fewer than B := (n² − n + 1)(n + m) steps, for every pointwise-optimal choice; from any start
    (RESULTS R18 (c): «R17 Corollary 2, which both referees confirmed holds from any start»).

## 2. Corollary SETTLE-MON
- SET_k := {v : LO_k(v) = HI_k(v)}.
- Statement. For every N5 run on every game and every k < K: SET_k ⊆ SET_(k+1). For v ∈ SET_k and every j with k ≤ j ≤ K:
  LO_j(v) = W_j(v) = HI_j(v) = LO_k(v).
- Proof. Let a := LO_k(v) = HI_k(v). By [SQZ] (monotone halves, induction on j) a = LO_k(v) ⊴ LO_j(v) and HI_j(v) ⊴ HI_k(v) = a; by
  [SQZ] (sandwich at j) LO_j(v) ⊴ W_j(v) ⊴ HI_j(v). So a ⊴ LO_j(v) ⊴ W_j(v) ⊴ HI_j(v) ⊴ a, and [LEX] gives equality throughout; in
  particular v ∈ SET_j. □

## 3. Corollary BRACKET-MON
- Statement. For every N5 run on every game, every v and every k < K:
  lcp(CS LO_k(v), CS HI_k(v)) ≤ lcp(CS LO_(k+1)(v), CS HI_(k+1)(v)).
  Hence B_k := Σ_v lcp(CS LO_k(v), CS HI_k(v)) is non-decreasing, takes values in [0, n(n + 2)], and rises at most n(n + 2) times.
- Proof. Put a := CS LO_k(v), a′ := CS LO_(k+1)(v), b′ := CS HI_(k+1)(v), b := CS HI_k(v). By [SQZ] and [LEX] / R93 (a): a ≤ a′ ≤ b′ ≤ b
  lexicographically ((a′ ≤ b′) is the sandwich at k + 1). [SAND] on a ≤ a′ ≤ b: lcp(a, b) = min(lcp(a, a′), lcp(a′, b)) ≤ lcp(a′, b).
  [SAND] on a′ ≤ b′ ≤ b: lcp(a′, b) = min(lcp(a′, b′), lcp(b′, b)) ≤ lcp(a′, b′). So lcp(a, b) ≤ lcp(a′, b′). Each lcp is in [0, n + 2],
  so B_k ∈ [0, n(n + 2)]; a non-decreasing integer sequence in that range rises at most n(n + 2) times. □

## 4. SETTLE-RED and BRACKET-RED (EQUIVALENCES)
- SG := the largest number of consecutive transitions of the run at none of which SET grows (SET_(k+1) ≠ SET_k); BG := the same with «B rises».
- Statement. For every N5 run on every game: K ≤ (n + 1)(SG + 1) and K ≤ (n(n + 2) + 1)(BG + 1); and SG ≤ K, BG ≤ K. So, over any
  family of games, N5's iteration count is polynomial ⟺ SG is polynomial ⟺ BG is polynomial.
- Proof. By SETTLE-MON, SET never shrinks, so it grows at r ≤ n transitions g_1 < … < g_r. The other transitions form at most r + 1
  maximal windows, each of at most SG transitions. So K ≤ (r + 1)·SG + r ≤ (n + 1)·SG + n ≤ (n + 1)(SG + 1). The same argument with
  BRACKET-MON (at most n(n + 2) rises of B) gives K ≤ (n(n + 2) + 1)(BG + 1). SG, BG ≤ K by definition. □
- (Correction to box 117's wording «K ≤ (n + 1)·SG»: the bound proved is K ≤ (n + 1)(SG + 1); the equivalence is unchanged.)

## 5. Lemma CONSISTENT-RED and its Corollary
- Statement. Let k0 < k1 be states of an N5 run on any game, with τ_k = τ for k0 ≤ k ≤ k1, and let every transition k → k + 1,
  k0 ≤ k < k1, be consistent (not a fallback, Iσ_k = IW_k). Then (σ_(k0), …, σ_(k1)) is a sequence of k1 − k0 switch-best steps on G_τ, each
  changing the strategy; hence k1 − k0 < B.
- Proof.
  - Fix k ∈ [k0, k1). τ_(k+1) = τ_k = τ, and the transition is not a fallback. If S4a left σ unchanged (σ_new = σ_k, in particular if
    Iσ_k = ∅), then with τ_new = τ_k the transition would be a fallback ([SPEC]). So σ_(k+1) = σ_new ≠ σ_k.
  - S4a's arena H_k is the one-player arena on G_τ in which Even y may use {σ_k(y)} ∪ Iσ_k(y) = {σ_k(y)} ∪ IW_k(y), and Odd follows τ.
    By [1E-N3], σ_(k+1) is a pointwise optimum of that arena. IW_k is VJ00's improving set of σ_k in G_τ (§1). So σ_k → σ_(k+1) is one
    switch-best step of [R17] on G_τ.
  - The steps chain, so the window is a sequence of k1 − k0 switch-best steps on the one-player game G_τ from σ_(k0); [R17] (any start,
    any pointwise-optimal choice) gives k1 − k0 < B. □
- Corollary. A τ-stretch with INC inconsistent transitions has at most (INC + 1)(B − 1) + INC transitions: the inconsistent transitions split
  it into at most INC + 1 maximal consistent windows, each of < B transitions. Since INC is at most the stretch length, stretch lengths
  are polynomial over a family ⟺ their INC counts are.
- Remark. RESULTS R18 (c) Lemma 3 is the special case Ξ = W (pure transitions on o-acyclic 𝒞^1O), where every transition is consistent;
  CONSISTENT-RED needs only Iσ = IW.

## 6. DEAD (explicit bound): R17's phase bound does not transfer to a τ-stretch
- Statement killed: «in every τ-stretch of every N5 run, every λ_W-phase (maximal set of consecutive transitions of the stretch at whose
  states the map v ↦ cycle node of W(v) is constant) contains at most n − 1 transitions at which W changes» (R17 (c)'s bound for
  switch-best, transferred).
- Instance 1: experiments/new/box116/inst/fbg_K12_m6_m24.pg (sha1 2f035ca0a999…, L-RED's fbg family), start
  fbg_K12_m6_m24_fixed.start (9f03f81fae59…, box 116b's repair). n = 290, K = 404, 0 fallbacks; transitions 1 → 404 form one τ-stretch
  (403 transitions) and one λ_W-phase, and W changes at all 403: 403 > 289 = n − 1.
- Instance 2: experiments/n5-epoch/instances/lend107_n32.pg (ab4c9811b311…) with lend107_n32.start (9df4ea2ceafe…): n = 32, 107 W-changing
  transitions in one λ_W-phase of a τ-stretch: 107 > 31 (the run has 10 fallbacks).
- Check: experiments/new/box118/gate.py G START (field maxWchPerPhase), box118/pincheck.sh (output box118/pincheck.txt): L-COMP's n5b and
  n5x give identical state sequences (404 / 112 iterations); Oink 8fbf0a7 --zlk and --tl «solution verified»; N5's regions = Oink's.
- RESULTS R17's honest limit (ii) reported vc_g25 (26 > 24); this instance exceeds the explicit bound by a factor 1.39 at n = 290.

## 7. DATA (not to sign; l-new 5ea2e738 / 8ed3d366; scripts named)
- Separation (box117/squeeze.py, sep.py; switchbestexp_2..6, sha1 b3d5bc29…, e1cd8f13…, 57b27b74…, 84913ba8…, 7348edf1…). TBR := S4a against
  τ_k with τ_(k+1) := σ̄_k; ARSB := S4a with σ̄_k in place of τ_k (box115/abl.py). With HI built from the Odd strategy each variant plays
  against, [SQZ]'s HI half and SETTLE-MON FAIL for both: HI rises at 2 / 5 / 11 / 18 / 18 (TBR) and 2 / 6 / 13 / 22 / 25 (ARSB) transitions,
  settled vertices leave SET 3 / 9 / 18 / 9 / 9 and 3 / 9 / 18 / 30 / 45 times; N5: 0. Settle gap SG: N5 16 / 19 / 19 / 21 / 22, TBR
  30 / 63 / 107 / 132 / 132, ARSB 29 / 67 / 144 / 221 / 221.
- L-RED's builds (box117/runred.sh, box118/runred.sh): SET and B flat except at the end (SG = BG ≈ K, up to 404); ARSB stops in 2 to 23
  iterations; R17's ungated switch-best on G_τ from the stretch start takes 2 to 7 steps (20 on fb3) against N5's 44 to 403; INC ≈ the
  stretch length (cp_K4 43 / 44, s3quad_K8_m30 263 / 264, fbg_K12_m6_m24 395 / 403).
- Corpus (L-SI box 53's 1,132 runs, box 113's repaired starts): 0 violations of [SQZ], SETTLE-MON, BRACKET-MON; SG ≤ 3.41n, BG ≤ 2.91n;
  INC 12,433 of 17,841 climb steps; 575 runs with INC 0; 118 runs exceed the §6 bound.
- Box 119 (not part of this packet): «INC ≤ released blocked-edge switches» DEAD at constant 1 (cp_K4 43 > 9).

## 8. READING (not to sign)
- [SQZ]'s HI half is where N5's Odd step enters; it separates N5 from TBR / ARSB on switchbestexp (§7), and it is blind inside a τ-stretch,
  where HI is constant. CONSISTENT-RED says that inside a τ-stretch only the steps where Ξ's gate and W's objective disagree can be
  super-polynomial; on L-RED's builds they are almost all steps, fed by fresh Ξ-changes (box 119): the XI-CH core.

## 9. Drafter's pre-check against CHECKER's recurring E-items (line docs/new/P-N5-GATE-line.txt)
- Free symbols: v, k (transition), j, k0, k1 bound in the binder or the clause; y, z bound in IW_k's set; τ in CONSISTENT-RED is the common
  value named by «τ_k = τ»; n, m, K, B, CS, lcp, SET, B_k, SG, BG, IW_k, INC, τ-stretch, λ_W-phase defined in the line; Ξ, Ξ^d per SPEC S1
  («values … as in SPEC S1»). None free.
- DATA: the line states no DATA. The only instance-level clause is the DEAD, at the explicit bound n − 1 with both counts (L43 / R90 form).
- Asymptotic DEADs: none (L43).
- L41: no proof in this packet is referee-originated. One premise is: R17 (F1), used by R18 (d) Lemma S (a) and by R17's bound, has
  derivations written by the referees (R17 (a)). The line has a tail clause naming it.
- Landed labels: R17, R18 (c)/(d), R57, R93, R99 are cited by label, and no lane commit is pinned. R98 is not used.
- The sandwich is cited as R18 (d)'s, not claimed (Lead 00:06Z).
- Scope words: «REDUCTIONS and EQUIVALENCES», «no count is bounded here», «G-N5-TIME stays OPEN», «not M3, not a step-4 pass, not a TARGET.md
  claim».

## DONE / FINDINGS / NEEDS
- DONE: this packet; line docs/new/P-N5-GATE-line.txt.
- FINDINGS: SETTLE-MON, BRACKET-MON, SETTLE-RED / BRACKET-RED, CONSISTENT-RED (reductions / equivalences); DEAD §6 at the explicit bound
  n − 1.
- NEEDS: Lead: route to REFEREE and REFEREE-2, then CHECKER.
