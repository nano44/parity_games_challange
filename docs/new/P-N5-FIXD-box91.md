# P-N5-FIXD (packet, box 91): the pair potential FIX-DEPTH is monotone in every phase (FIXD-MON), and phase length reduces to Ξ-changing transitions without a depth rise (PHASE-RED with FLATTR); PHASE-RED′ (flat Even switches) only under CONJECTURE FLAT-SW
L-NEW successor 38 (Opus 5.5), D14 / D18, Lead reading L40. Lead 2026-10-30 15:33Z: «Your short box is BOX 91, a freeze … GO: freeze
P-N5-FIXD now as a packet for the two referees. Contents: FIX-DEPTH, FIXD-MON, PHASE-RED with FLATTR. PHASE-RED′ goes in only as
conditional on CONJECTURE FLAT-SW. Use the format of your earlier packets: the exact statement of each claim, proofs, data pins, and a
proposed RESULTS line with every symbol bound.» FROZEN 2026-10-30 (this commit; sha1 reported to the Lead). Written 15:33Z-15:36Z (date -u).
Sources (working notes, unrefereed; THIS packet governs where they differ; none is cited as a proof): docs/new/N5-FIXD-box77.md §1-§2
(L-NEW successor 36, l-new 50724c74), docs/new/N5-FLATSRC-box79.md §1, §3 (successor 36).
Status: REDUCTION only. FLATTR_P (equivalently Σ FLATSW under FLAT-SW) is NOT bounded here. G-N5-TIME stays OPEN. Not M3, not a step-4
pass, not a TARGET.md claim. Object: N5 only (SPEC S1-S5). Nothing is claimed for N5-LZC.

## 0. What to sign
| § | item | label |
| --- | --- | --- |
| 2 | Definition FIX-DEPTH (DEPTH_t(v), K_t) and Lemma FIXD-MON | PROVED (to sign) |
| 3 | Theorem PHASE-RED (with FLATTR_P) | PROVED (to sign), a REDUCTION |
| 4 | Corollary PHASE-RED′ | PROVED (to sign) as an IMPLICATION from CONJECTURE FLAT-SW (FLAT-SW itself NOT to sign) |
| 5 | DATA, DEAD, READING | NOT to sign |

## 1. Setting and premises (all landed; quoted)
- N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md; FIX 1-4 as in RESULTS); any parity game, V = {0, …, n − 1}, n = |V|. A run is the sequence
  of states (σ_t, τ_t); a TRANSITION is t → t + 1. Ξ_t := Ξ_{σ_t} (SPEC S1), λ_Ξ its cycle-node map. ⊴, ◁, ⊵, ▷: the SPEC S1 order
  (better for Even) and its strict and reverse forms.
- PHASE (RESULTS R38 (a), as quoted in RESULTS R91 / R93): a maximal run of consecutive states with (λ_Ξ, τ) constant. For a phase
  P = [a, b] (states a, …, b), |P| := b − a, its transitions.
- [LEX] RESULTS R93, Fact LEX (P-N5-WCH §2.1, landed): «For a value x = (c, P, ℓ) put CS(x) := (rew(c); s_{n−1}, …, s_0; ℓ̂), where
  s_r := 0 if the vertex u_r of rank r is not in P, s_r := +1 if u_r ∈ P and Ω(u_r) is even, s_r := −1 if u_r ∈ P and Ω(u_r) is odd, and
  ℓ̂ := ℓ if Ω(c) is odd, −ℓ if Ω(c) is even. Then x ◁ y iff CS(x) < CS(y) lexicographically.» «Consequence (COMMON PREFIX): if x ⊴ z ⊴ y
  and CS(x), CS(y) agree on their first L coordinates, so does CS(z) with both.» CS has n + 2 coordinates.
- [R15] RESULTS R15 (a): «Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}». (d): «N5:
  every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and changes at least one
  of them … at most 4n(n−1) consecutive N5 iterations leave both Ωσ and Ωτ unchanged (two potentials φ, φ^d).» Hence (as in R93's packet
  §1) Ξ_{t+1} ⊵ Ξ_t pointwise at every transition (MON).
- Ωσ = Ξ_{σ} (SPEC S1). Ωτ is Odd's valuation of τ on G^d against Even's optimal reply; it depends on τ alone (SPEC S1, "Odd's side").

## 2. FIX-DEPTH and Lemma FIXD-MON (PROVED)
- Definition. Fix a phase P = [a, b] and put fin(v) := Ξ_b(v). For a state t ∈ P and a vertex v, DEPTH_t(v) is the length of the longest
  common prefix of CS(Ξ_t(v)) and CS(fin(v)), so DEPTH_t(v) = n + 2 iff Ξ_t(v) = fin(v). K_t := Σ_v DEPTH_t(v) ∈ [0, n(n + 2)].
  (K_t depends on the pair (σ_t, σ̄_t) through Ξ_t, with the phase's last value as a fixed reference.)
- Lemma FIXD-MON. For states t ≤ t′ of a phase P and every vertex v: DEPTH_{t′}(v) ≥ DEPTH_t(v). Hence K_{t′} ≥ K_t.
- Proof. By MON applied along t, …, t′, …, b: Ξ_t(v) ⊴ Ξ_{t′}(v) ⊴ Ξ_b(v) = fin(v). CS(Ξ_t(v)) and CS(fin(v)) agree on their first
  L := DEPTH_t(v) coordinates. By COMMON PREFIX ([LEX]) with x = Ξ_t(v), z = Ξ_{t′}(v), y = fin(v), CS(Ξ_{t′}(v)) agrees with CS(fin(v)) on
  those L coordinates, so DEPTH_{t′}(v) ≥ L. Summing over v gives K_{t′} ≥ K_t. □
- Remark (no premise used beyond MON and [LEX]): FIXD-MON holds on every phase of every N5 run, whatever its transitions (S4a, S4b, S4c).

## 3. Theorem PHASE-RED (PROVED; a REDUCTION)
- Definitions, for a phase P: CH_P := the transitions of P at which Ξ changes at some vertex. FLATTR_P := the transitions of P at which Ξ
  changes at some vertex and K does not change (equivalently, no DEPTH changes: by FIXD-MON each DEPTH is non-decreasing, so K is unchanged
  iff every DEPTH is).
- Statement. For every phase P of every N5 run: |P| ≤ (4n(n − 1) + 1)·(CH_P + 1) and CH_P ≤ n(n + 2) + FLATTR_P; so
  |P| ≤ (4n(n − 1) + 1)·(n(n + 2) + FLATTR_P + 1).
- Proof.
  - (i) CH_P ≤ n(n + 2) + FLATTR_P. A transition counted in CH_P either changes K or not. If it changes K, then K rises strictly (FIXD-MON).
    K takes integer values in [0, n(n + 2)], so at most n(n + 2) transitions of P raise it. The others are FLATTR_P by definition.
  - (ii) |P| ≤ (4n(n − 1) + 1)(CH_P + 1). The CH_P Ξ-changing transitions split the other transitions of P into at most CH_P + 1 maximal
    runs of consecutive transitions at which Ξ (= Ωσ) is unchanged. In a phase τ is constant, so Ωτ (a function of τ alone) is unchanged
    too. By [R15] (d) each such run has at most 4n(n − 1) transitions. Hence |P| ≤ CH_P + (CH_P + 1)·4n(n − 1) ≤ (4n(n − 1) + 1)(CH_P + 1).
  - Combine (i) and (ii). □
- What remains open: FLATTR_P, the Ξ-changing transitions with no DEPTH rise (the "dead-branch climbs": every vertex whose Ξ changes stays
  inside the sub-order below its common prefix with fin). Not bounded here.

## 4. Corollary PHASE-RED′ (PROVED as an IMPLICATION from CONJECTURE FLAT-SW; FLAT-SW itself is NOT claimed)
- CONJECTURE FLAT-SW (OPEN; data only, §5): every transition k → k + 1 counted in FLATTR_P (any phase P of any N5 run) has a switched Even
  vertex x (σ_{k+1}(x) ≠ σ_k(x)) with Ξ_{k+1}(x) ≠ Ξ_k(x).
- Definition: FLATSW_P(x) := the transitions k → k + 1 counted in FLATTR_P at which the Even vertex x is switched and Ξ_{k+1}(x) ≠ Ξ_k(x).
- Statement. If FLAT-SW holds, then for every phase P: FLATTR_P ≤ Σ_x FLATSW_P(x), and so
  |P| ≤ (4n(n − 1) + 1)·(n(n + 2) + Σ_{x Even} FLATSW_P(x) + 1).
- Proof. Under FLAT-SW, every FLATTR_P transition k → k + 1 has an x as in FLAT-SW. That transition is counted in FLATSW_P(x). Distinct
  transitions give distinct pairs (x, k), so FLATTR_P ≤ Σ_x FLATSW_P(x). Insert into Theorem PHASE-RED. □
- Note: FLATSW_P(x) ≤ SW_P(x), x's switches in P (a per-vertex decision count).

## 5. DATA, DEAD, READING (NOT to sign)
- DATA (tools: experiments/new/box77/fixdepth.py, box79/flatsrc.py; outputs fixd_*.txt, flatsrc_*.txt; corpus 1132 runs, the lists of
  box 83 (box59/sbcg.lst, 719; si/root/logs/alt_all.lst, 413)):
  - FIXD-MON: 0 decreases of K in any phase.
  - Flat transitions 6568 of 16183 Ξ-changing (box 77 count). FLATTR 6503 in N5, all containing a flat Even switch (FLAT-SW: 0 exceptions).
    Max FLATTR per phase 91 (red/n5inj returns_ph64, n 64). Max FLATSW per (x, phase) 14 (red/n5inj returns_rt64, n 64).
  - Pins (check.sh "box 77", "box 79"): experiments/n5-epoch/instances/nep92_n40.pg + .start (sha1 ce224ec31e56e18103290d4aac81a9f225f76bfc):
    FIX-DEPTH monotone; 73 flat transitions, each with a flat Even switch (≤ 8 per vertex). Climb instances experiments/new/box77/inst/
    cf_n80.pg (sha1 4b708b06…) and cfl_n24.pg (sha1 ae682d6b…).
- DEAD (box 77 §4):
  - "K rises at least once per O(1) transitions": snap_n80_s62 stalls 36 consecutive transitions, returns_ph64 stalls 91.
  - FLAT-LIN (per-vertex dead-branch climbs FLAT_P(v) ≤ n): nep92_n40 (above), vertex 0, 66 = 1.65n in one phase.
- READING. Dead-branch climbs are lexicographic counters, so no per-vertex prefix potential closes FLATTR. Under FLAT-SW the count moves to
  Even's per-vertex flat decisions. Inside W-runs those are paid by W-changes of targets (R93 RET-WCH), i.e. by the per-vertex Ξ/W-change
  count that boxes 84-90 reduce W-runs to (P-N5-WRUN, to be frozen by successor 39).

## 6. Symbols (all bound in the line file docs/new/P-N5-FIXD-box91-line.txt)
n; N5; run; state; transition; σ_t, τ_t, σ̄_t; Ξ_t; λ_Ξ; ⊴ ◁ ⊵ ▷; phase; P = [a, b]; |P|; fin; CS (R93 Fact LEX); rew; rank; DEPTH_t(v);
K_t; CH_P; FLATTR_P; Ωσ, Ωτ (R15); switched; FLATSW_P(x); SW_P(x) (note only); FLAT-SW.
