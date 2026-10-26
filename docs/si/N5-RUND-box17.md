# RUN_D for twin changes: what the freeze caps, the gates' offsets, and what is left (lane note, box 17)
L-SI successor 12 (Opus 5.5; D15, D18, L37, L40), session_01HYh7NTpb8ZcvdYpgAJiDgy. Lead's GO of 06:27Z (Lead's stamp): "RUN_D for twin
changes first … Lemma: every twin change strictly raises COARSE_L(W(v)) at the twin level. Cap the changes above the freeze level using
FRZ-U_H3 … Name the remainder below the freeze exactly, and test it: library plus random start pairs, with a mutation control."
Written 2026-10-26 06:4xZ onward (date -u; the stamp is the commit). LANE NOTE: not a packet, not frozen.
- Labels (D18 / L40): PROVED (L-SI 12, unrefereed) / CONJECTURE / OPEN / READING / DATA / DEAD. D1: wrong until checked.
- Scope: one fallback-free in-phase run of N5 (SPEC S1-S5, docs/new/N5-ssi-global.md) on EVERY game, mostly under (h3_D). Structural
  counts only. Nothing here bounds N5's running time on any class. Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Builds on (cited by sha1):
  - P-N5-H3 (docs/si/P-N5-H3-box16.md, sha1 680e4528…, both referees SIGNED; fixes 5666b4a5…): C2-H3 (and its proof's factorisation),
    TC-CLASS, WM-G, P^c_L, CR-D, FRZ-U_H3 (0-based: constant from state k_0 + n − 1).
  - RESULTS R55 (a) (Ξ = W on F_D); RESULTS R19 (d), the (SG) step "Ξ_{L+1}(z) ⊵ Ξ_L(z) at any N5 transition (on all games)".
  - docs/si/N5-2O-T-box16.md §0 (stretch_D), §8 (W-CN, TC-CN, the KIND-MONO obstruction).
  - L-NEW's P-N5-EPR (docs/new/P-N5-EPR-box45.md, sha1 8fecca79…, l-new 08abd9cb, frozen 06:28Z, in review), READ, not relied on for any
    PROVED item here: an epoch (σ̄|Q constant) of a phase is a run of N5^τ on the restricted game G′_E with |D_E| Odd choice vertices.

## 1. Where RUN_D sits now (READING)
- Inside an EPR epoch, D_k = D_E is constant. So every terminal change inside an epoch has D constant, and every terminal change with
  D_k ≠ D_{k+1} is at an epoch boundary (counted by the number of epochs, which EPR leaves open).
- Under (h3_D) on a run S, λ_W = λ_Ξ on V and is constant on S (P-N5-H3 §6 proof, (ii)). So EVERY terminal change on S is a twin change
  (TC-CN's W-moving changes need λ_W to move). RUN_D under (h3_D) is the whole terminal-change count.
- Inside an epoch both frames are fixed one-player games, G_{σ̄_E} for Ξ and G_τ for W. They differ only at the |D_E| gates. RUN_D with
  |D_E| = 2 is about two one-player games that differ at two vertices.

## 2. DEAD: "every twin change strictly raises COARSE_L(W(v)) at the twin level" (my own plan of 06:23Z; never a lemma)
- Statement killed: at a twin change of v (u_k(v) ≠ u_{k+1}(v), λ_W(v) unchanged, D_k = D_{k+1}), COARSE_L(W_{k+1}(v)) ≻ COARSE_L(W_k(v))
  for L the twin level top(P(W(u)) Δ P(W(u′))).
- Obstruction: W(v) can change ONLY IN LENGTH. Then no coarse value changes at any L ≥ −1. WM-G gives W_{k+1}(v) ⊵ W_k(v); it does not
  make the path set move.
- Instance: experiments/si/rund/instances/lenonly_n8.pg (sha1 725c2766…), S3 start (`python3 -I rund.py --one instances/lenonly_n8.pg`).
  At transition 1 → 2, v = 2 switches gate 6 → 4 with D_k = D_{k+1}; W(2) = (4, ∅, 4) → (4, ∅, 3).
  - It is game #321 of `K=2 rund.py --rand 3000 5 12 41`; dumprand.py rewrites it.
  - In the same stream, #933 is a second case.
- Also (elementary, so not a lemma): a twin change of v with D constant needs a switch at an Even vertex of v's old W-prefix. So the
  terminal changes per transition are ≤ n·(switches), and TC-SWITCH is not easier than T itself (as TC-W's entry in DEAD.md already said).

## 3. FINDING (DATA): every known non-vacuous coarse freeze is content-free
- A freeze has content only if some W path set at some state of the run has a vertex above the freeze level L. rel.py reports
  "content" = max over the run's states and vertices of |P(W(v)) ∩ V_{>L}|.

| instance (start) | n | run (states) | L = max_S M_D | top rank | content |
| --- | --- | --- | --- | --- | --- |
| frz1_n24.pg (its .start; L-COMP) | 24 | 25 | 23 | 23 | 0 |
| frz3_n24.pg (its .start; L-COMP) | 24 | 25 | 23 | 23 | 0 |
| pftheta34_n32.pg (S3; L-RED) | 32 | 35 | 31 | 31 | 0 |
| pft34_h3u_P32.pg (_t33.start; REFEREE-2's constructed witness) | 34 | 35 | 32 | 33 (the decoupled added vertex) | 0 |
| lib41, all k, n ≤ 64, S3 + 4 random starts: 4 non-vacuous runs (pftheta34_n32 ×2, pftheta_cex_n32, thclimb_n16_s12) | 16-32 | ≥ n + 1 | top rank | — | 0 on all 4 |

- So on every run of ≥ n + 1 states known to the fleet, COARSE_L(W) is just the cycle node, and the freeze says nothing beyond CR-D's
  hypothesis (ii). The frames disagree at the TOP vertex of a gate's value.
- The signed lemmas are unaffected. The data notes H3-N3 / N-H3-5 read "non-vacuous by length, content-free by level".
- Consequence for the plan: "cap the changes above the freeze level" caps nothing on any long run known. RUN_D lives below the freeze.

## 4. Lemma CR-REL (PROVED, every game)
Statement. CR-D (P-N5-H3 §5) holds with hypothesis (i) replaced by EDGE ORDER TRANSFER at L, at every state k of S:
- (i_rel) for every Even x, every z ∈ succ(x) and a := σ_k(x): COARSE_L(W_k(z)) ≻_L COARSE_L(W_k(a)) ⇒ Ξ_k(z) ▷ Ξ_k(a).
Then, under (i_rel) and (ii), COARSE_L(W) is constant on S from state k_0 + n − 1 on.
Proof. P^c_L's proof uses (i) only in Case B, to turn Ω^c_k(z) ≻ Ω^c_k(a) into Ξ_k(z) ▷ Ξ_k(σ_k x), so that (x, z) ∈ Iσ_k. (i_rel) is that
step. Nothing else in P^c_L or in CR-D's proof reads Ξ. □
- (i) ⇒ (i_rel), by (C2) and (Cstrict). (i_rel) is monotone in L (a coarse strict comparison at L is strict at every L′ < L). So
  L_rel(k), the least L with (i_rel), is ≤ max(M_D, −1) under (h3_D). CR-REL needs no (h3_D), only (ii).
- DATA (rel.py): L_rel < max(M_D, −1) on 338 of 1,694 hypothesis runs (lib41, all k, n ≤ 64, S3 + 4 random starts), and finite on 93
  ¬(h3_D) runs. On the four long runs of §3, L_rel = M_D = the top rank, so CR-REL adds no content there.
- Mutation control: MUT=2 (freeze from state k_0 + 1) fails 6 times on 1,500 random 𝒞^2O (seed 51); MUT=1 (L_rel − 1) does not bite on
  the available data.

## 5. Offsets: Lemma OFFSET, Lemma MERGE-B, Theorem TWIN-GAP (PROVED, every game)
Setting. S = (k_0, …, k_1): a fallback-free run inside one phase, with (h3_D) at every state. L* := max(max_S M_D, −1), with M_D := −1 when
D_k = ∅. Write w(P) := Σ_{x ∈ P} ε(x)·2^{rank x}, ε(x) = +1 for even x and −1 for odd x (S1's signed path weight; Σ ±2^rank is injective on
sets, P-N5-FB-box7 §1 (C3)). For v ∈ V and k ∈ S: s^Ξ_k(v) := w(P(Ξ_k(v))), s^W_k(v) := w(P(W_k(v))), and the OFFSET
Δ_k(v) := s^W_k(v) − s^Ξ_k(v). For u ∈ D_k: δ_k(u) := w(P(W_k(u))) − w(P(Ξ_k(u))).
### Lemma OFFSET
- (a) λ_Ξ(v) = λ_W(v) for every v, constant on S. s^Ξ_k(v) and s^W_k(v) are non-decreasing along S.
- (b) Δ_k(v) = 0 if v ∈ F_D, or if v ∈ R_D and λ(v) ∈ π_v. Otherwise Δ_k(v) = δ_k(u(v)).
- (c) Every δ_k(u) is a sum of terms ±2^r with r ∈ P(Ξ_k(u)) Δ P(W_k(u)), a set of ranks in [ℓ_S, L*]. Here ℓ_S is the least rank in the
  union U_S := ∪_{k ∈ S, u ∈ D_k} (P(Ξ_k(u)) Δ P(W_k(u))). So every offset on S is a multiple of 2^{ℓ_S}; if U_S = ∅, every offset is 0.
Proof.
- (a) The first sentence is P-N5-H3 §6's proof of (ii) (R55 (a) on F_D; TC-CLASS and (h3_D) on R_D; λ_Ξ is constant on a phase).
  - Ξ_{k+1}(v) ⊵ Ξ_k(v) (R19 (d), (SG) step, every game) and W_{k+1}(v) ⊵ W_k(v) (WM-G).
  - With the cycle node fixed, S1's order compares path sets first, and on sets that order is the order of w.
  - So s^Ξ and s^W do not decrease.
- (b) On F_D, Ξ = W (R55 (a)). For v ∈ R_D with c := λ(v), u := u(v):
  - if c ∈ π_v, both plays follow π_v to c (HP_D: σ̄ = τ off D_k), so the path sets are equal;
  - if c ∉ π_v, C2-H3's proof (P-N5-H3 §4) gives P_F(v) = (π_v ∩ V_{>c}) ⊔ P_F(u) exactly, in both frames F = Ξ, W. w is additive over
    disjoint unions, so Δ_k(v) = w(P_W(u)) − w(P_Ξ(u)) = δ_k(u).
- (c) δ_k(u) = Σ_{r ∈ P_W(u) ∖ P_Ξ(u)} ε 2^r − Σ_{r ∈ P_Ξ(u) ∖ P_W(u)} ε 2^r. Under (h3_D) the two values share the cycle node, so
  top(P_Ξ(u) Δ P_W(u)) = lev(Ξ_k(u), W_k(u)) ≤ M_D ≤ L*. □
### Lemma MERGE-B
At a state of S, if λ(y) = λ(z) and Δ(y) = Δ(z), then s^Ξ(y) − s^Ξ(z) = s^W(y) − s^W(z). So the two frames order the path sets of y and z
the same way. (Immediate from the definition of Δ.) Inside one OFFSET CLASS (vertices with a common cycle node and a common offset) the
frames agree on every path-set comparison: this is R50's Fact B, with "same terminal" replaced by "same offset".
### Theorem TWIN-GAP
Let N_v be the number of transitions of S at which Δ(v) changes, and B := L* − ℓ_S + 1 (the width of the gates' disagreement band;
N_v = 0 if U_S = ∅). Then:
- (i) at each such transition, with d := Δ_{k+1}(v) − Δ_k(v) ≠ 0: s^W(v) rises by ≥ d if d > 0, and s^Ξ(v) rises by ≥ −d if d < 0;
- (ii) at most (2^{L*+2} − 2) / 2^{ℓ_S} < 2^{B+1} of them lie at states ≥ k_0 + n − 1;
- (iii) N_v ≤ (n − 1) + 2^{B+1}.
Proof.
- (i): s^W_{k+1} − s^W_k = (s^Ξ_{k+1} − s^Ξ_k) + d, and both rises are ≥ 0 by OFFSET (a).
- (ii): from state k_0 + n − 1 on, FRZ-U_H3 keeps COARSE_{L*}(W(v)) = COARSE_{L*}(Ξ(v)) constant. So P ∩ V_{>L*} is constant in both frames.
  - Each score then moves by a difference of w over two sets of ranks ≤ L*. Each rank r contributes at most 2^r to such a difference,
    so each score rises by ≤ 2^{L*+1} − 1 in all (it is monotone), and s^W(v) + s^Ξ(v) by ≤ 2^{L*+2} − 2.
  - By (i) and OFFSET (c), each change consumes ≥ |d| ≥ 2^{ℓ_S} of it.
  - If L* = −1, then U_S = ∅ and there is nothing to count.
- (iii): at most n − 1 transitions lie before k_0 + n − 1. □
- Corollary (PROVED): under (h3_D) on S, the terminal changes of v at which its offset changes are ≤ N_v ≤ (n − 1) + 2^{B+1}. Those
  are the twin changes between gates with different offsets, and the moves between a gate class and offset 0, when the gates' values
  do not compensate at the same transition.
- READING: TWIN-GAP is polynomial when the band is narrow, B = O(log n). In the data the band is wide (§7: B up to 39 at n ≤ 48). So
  TWIN-GAP alone does not give a polynomial count. It names the exponent: the band of ranks in which a gate's two values can differ.

## 6. The remainder below the freeze, exactly (OPEN unless marked)
Under (h3_D) on a run S (every terminal change is a twin change, §1):
- (R1) OFFSET-PRESERVING terminal changes: v moves between twin gates with δ(u) = δ(u′), or between classes of offset 0.
  - Inside an offset class the frames agree (MERGE-B), as inside R50's single class.
  - What is missing is a port of R50's per-class chain (FRZ-U in κ form, LEN, Theorem RUN) to one offset class whose vertices route to
    several gates. OPEN.
- (R2) OFFSET-CHANGING terminal changes: bounded by TWIN-GAP, but by 2^{B+1}, exponential in the band width. OPEN: a polynomial bound
  (a narrow band, or a count finer than the score range).
  - CONJECTURE OFFSET-ONCE (DEAD at 07:1xZ, §10): inside one stretch_D of S (D, R_D and the gates' two values constant), no vertex's
    offset returns to a value it has left. With it, offset changes per vertex per stretch_D are ≤ |D|, and (R2) reduces to stretch_D boundaries (ρ and W(q) changes,
    N5-2O-T §2).
  - Status: DATA only (§7: 0 returns). Climbs against it found nothing (§7). An earlier "return" on frz3_n24 from a random start was at
    a non-(h3_D) run with R_D changing: outside the conjecture's hypothesis.
- (R3) ¬(h3_D) runs: not covered here (the KIND-MONO line, N5-2O-T §8).
- (R4) The epoch count (P-N5-EPR) and the stretch_D boundaries: not this note's subject.

## 7. DATA (DATA, not proof; experiments/si/rund/, own scripts, N5 via experiments/new/box21/n5x.py step, read-only)
- rund.py (twin changes), rel.py (CR-REL, content), le.py (twin relative levels), gap.py (OFFSET, TWIN-GAP, OFFSET-ONCE),
  climbtw.py / climboff.py (climbs), dumprand.py (rewrites a random game). Logs in logs/.
- Checks with 0 violations unless stated:
  - MONO: s^Ξ, s^W non-decreasing at fixed cycle nodes.
  - JUMP: TWIN-GAP (i).
  - FAC: OFFSET (b), at (h3_D) states.
  - BOUND / POST: TWIN-GAP (iii) / (ii).
  - RETURN: OFFSET-ONCE.
  - FRZ: CR-REL.
- Mutation controls: gap.py MUT=1 (doubled jump) fails 51 times on lib2o; rel.py MUT=2 fails 6 times on 1,500 random 𝒞^2O.

| set (gap.py) | runs ((h3_D) runs) | FAC checks | offset changes (max per vertex per run) | stretch_D segments ((h3_D)) | offset changes inside them (max per vertex) | RETURN | band B (max) | twin changes in (h3_D) runs: changing / preserving |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41 (≥ 2 Odd choices, n ≤ 48), S3 + 2 random starts | 191 (119) | 7,714 | 1,285 (5) | 138 | 12 (1) | 0 | 39 | 29 / 0 |
| lib2o (43 games), S3 | 37 (32) | 1,938 | 67 (2) | 39 | 0 (0) | 0 | 17 | 0 / 1 |
| random 𝒞^2O, 6,000, n 5-14, seed 62 | 948 (923) | 12,095 | 58 (2) | 824 | 0 (0) | 0 | 7 | 0 / 3 |
| random 𝒞^kO (k 2-4), 6,000, n 5-14, seed 63 | 758 (733) | 13,866 | 47 (2) | 648 | 0 (0) | 0 | 8 | 0 / 16 |
| frz3_n24 (its .start) | 1 (1) | 96 | 28 (8) | 2 | 0 (0) | 0 | 17 | 3 / 0 (all at stretch_D boundaries) |
- No offset change lies at a state ≥ k_0 + n − 1 in any of these sets (runs are short), so TWIN-GAP (ii) is not exercised. (iii) holds
  with a wide margin: the largest count per vertex per run is 8, against (n − 1) + 2^{B+1}.
- Most offset changes come from changes of the gates' own values (stretch_D boundaries), not from moves between classes inside a
  stretch_D: 12 of 1,285 on lib41.

- Twin changes inside (h3_D) runs. The library (lib41) has offset-CHANGING ones; the random 𝒞^2O / 𝒞^kO sets have offset-PRESERVING
  ones. Both kinds of the remainder occur.
- Climbs (𝒞^2O, climb2o.py's mutations, S3 + seeded random starts):

| climb | start game | objective | best |
| --- | --- | --- | --- |
| climbtw.py, seeds 1-4, n 12, 400 steps, 2 random starts | random 𝒞^2O | twin changes in one run | 12 (in a run of 3 transitions; ≤ 1 per vertex) |
| climbtw.py, seed 5, 150 steps, 1 random start | frz40.pg (L-RED) | same | 14 (run of 15 transitions) |
| climboff.py, seeds 21-23, 250 steps, 2 random starts | frz3_n24.pg | offset changes per vertex inside one stretch_D (then in-stretch total, then all) | 0 inside a stretch_D (25-33 offset changes in all) |
| climboff.py, seed 24, 120 steps, 1 random start | frz40.pg | same | 1 per vertex (6 in-stretch, 173 in all); no RETURN |

## 8. Status
- PROVED (L-SI 12, unrefereed, every game): CR-REL; OFFSET (a)-(c); MERGE-B; TWIN-GAP (i)-(iii) and its Corollary.
- DEAD: the strict-raise lemma (§2, lenonly_n8).
- DATA FINDING: the known non-vacuous freezes are content-free (§3).
- DEAD: CONJECTURE OFFSET-ONCE (§10, offret_n23; family mkalt.py: K − 1 offset changes of one vertex in one stretch_D at n = Θ(K²)).
- OPEN: (R1) the per-offset-class RUN; (R2) a polynomial bound on offset changes; (R3); (R4).
- READING: RUN_D sits inside EPR epochs. Under (h3_D) every terminal change is a twin change. TWIN-GAP's exponent is the band width B.

## 9. What moves below the top-rank disagreement on the long runs (Lead's item (b), 06:48Z; DATA and READING)
Tools: experiments/si/rund/below.py (per-transition trace of a long run), pv.py (per-vertex changes per run).
- frz1_n24 (its .start; 24 transitions):
  - States 0-15 are one EPR epoch with D = {12}. Gate 12 has cycle node 19 (rank 4); its Ξ/W disagreement has its top at rank 23, held
    by Ξ. States 16-23 have D = ∅ (a one-player stretch, EP-0 / R17 territory).
  - Almost every change is at ranks 21-23: the top vertex enters, or a high vertex leaves, the path sets of 1-2 vertices per transition.
    Ξ and W change at the SAME vertices and levels at every transition except the two at which the gate's own value changes (k = 6, 15).
  - So the run is long because the propagation is sequential (one switch per transition along a chain), not because values move often.
- frz3_n24 and pftheta34_n32: the same pattern. frz3 has two twin gates (12, 23; cycle node 19; tops r23 in Ξ(12), r22 in W(23)).
- Per-vertex changes per run (pv.py):

  | set | runs | max transitions in a run | max Ξ-changes of one vertex in a run | max W-changes |
  | --- | --- | --- | --- | --- |
  | random 𝒞^2O, 6,000, n 5-14, seed 62 | 948 | 3 | 2 | 2 |
  | lib41, all k, n ≤ 64, S3 + 2 random starts | 1,512 | 55 (n 64, x32_rand64) | 35 (n 48, pft35_n48) | 20 |

  - The runs with one vertex changing at (almost) every transition (sc24: 20 of 20; pf_best_3621: 31 of 31; pft35_n48: 35 of 35) are all
    𝒞^1O games (polynomial by R51), and sc24's run has D = ∅ throughout (one-player; R17 bounds it).
- READING (the mechanism, and the next lemma to try): inside a stretch_D, each vertex keeps its offset, so s^Ξ and s^W rise by the same
  amount at every transition (OFFSET (b)). That is why the frames move together.
  - If, in addition, every Even edge compares the same way in both frames (Ξ(z) ▷ Ξ(a) ⟺ W(z) ▷ W(a) for z ∈ succ(x), a = σ(x)), then
    Iσ is G_τ's improving set and the S4a step is switch-best on the one-player game G_τ. R17 (c) then bounds such a sub-run (λ_W constant
    under (h3_D)) by n + m transitions. This is a two-gate form of R19 (f) PIECE (call it PIECE_D; NOT proved here, a sketch).
  - What it leaves: the transitions at states with a SPLIT EDGE, an Even edge whose two frames disagree. By MERGE-B, a split edge joins
    two vertices of different offsets, so its count is again an offset question. In frz1_n24, L_rel = 23 says split edges exist at every
    level below 23. They join offset 0 (F_D) and offset δ(12) (R_D).
- On the Lead's ¬(NC) pointer (L-COMP l-comp 589dc66c: τ changes at the next transition after 80 % of (h3_D) ∧ ¬(NC) states): I see no
  forced-switch lemma yet. σ̄(u) ≠ τ(u) says σ̄(u) is Odd's better reply against σ (Ξ frame), while S4b switches τ(u) by Odd's DUAL
  valuation (Even's best reply to τ). For u on its own W-cycle with (h3_D), both of u's successors lead to the same cycle node, so the dual
  comparison is decided by path sets, which the hypothesis does not fix. Not attempted further; a separate item if wanted.

## 10. OFFSET-ONCE is FALSE (Lead's pick 06:56Z: "Attack OFFSET-ONCE, with a proof attempt first"; DEAD, with instances)
### The proof attempt, and where it stops
- Inside a stretch_D the gates' two values are constant by definition, so every gate offset δ(u) is constant. (The Lead's question
  "can δ(u) move both ways inside a stretch_D?" has the answer no.) Offsets take the ≤ |D| + 1 values {0} ∪ {δ(u) : u ∈ D}.
- A return A → B → A of v needs only, writing x_t := w(κ_v) at the three states: x_2 ≥ x_1 + max(a_A − a_B, b_A − b_B) and
  x_3 ≥ x_2 + max(a_B − a_A, b_B − b_A). Here a_g, b_g are the gate parts of s^Ξ, s^W. That is, the route to A must gain
  ≥ |δ_A − δ_B| between the two visits. Monotonicity (WM-G, (SG)) allows exactly that, so it gives no contradiction.
- A proof would need the dynamics to forbid the route to A from improving after v left it. A delay chain on that route does the
  opposite, and that is the counterexample.
### The instance (DATA, verified trace; experiments/si/rund/mkret.py 2 4)
- experiments/si/rund/instances/offret_n23.pg (sha1 8fdfc38d…) with offret_n23.start (sha1 634dbc59…), 23 vertices:
  - two twin gates u1 = 4, u2 = 12 (Odd; τ → a_i = 2, 10; honest reply → b_i = 3, 11);
  - behind each b_i, a delay chain e_i → w → … → g_i (g_i a high even vertex on a path to c = 0). Even's escape reaches e_i only after 4
    steps. So σ̄(u_i) = b_i ≠ τ(u_i) stays, and Odd's dual valuation (Even's best reply to τ) never wants b_i, so τ is constant;
  - v = 22 with successors 20 (a delay chain 20 → 21 → h = 18 → u1) and 19 (→ u2).
- N5 trace (gap.py, and trace.py: logs/trace_offret_n23.txt):
  - states 0-3 are ONE phase and ONE stretch_D: D = {4, 12}, τ = (2, 10), the gates' values unchanged, every cycle node c = 0,
    (h3_D) holds, and there is no fallback;
  - v goes route-to-u1 (offset 131204) → route-to-u2 (264200, at step 0) → route-to-u1 (131204, at step 2, when h = 18 arrives);
  - `RETURN ('instances/offret_n23.pg', 0, 3, 22, [131204, 264200, 264200, 131204])`; all other checks PASS. Pinned in
    experiments/si/check.sh.
### A family (DATA): K − 1 offset changes of one vertex inside one stretch_D
- mkalt.py K LG: improvement j = 1..K sits on side (j mod 2) + 1, a separate delay chain of length 2j to a high even vertex h_j (ranks
  increasing in j). v switches sides each time the next h_j arrives.

  | K | n | offset changes of v in one stretch_D | RETURNs | all twin changes offset-changing |
  | --- | --- | --- | --- | --- |
  | 3 | 49 | 2 | 1 | yes |
  | 4 | 62 | 3 | 2 | yes |
  | 6 | 94 | 5 | 4 | yes |
  | 8 | 134 | 7 | 6 | yes |
  | 10 | 182 (instances/offalt_K10.pg, sha1 b03fe313…) | 9 | 8 | yes (9 / 9) |

- n = Θ(K²) (separate chains), so this family gives Θ(√n) offset changes per vertex per stretch_D: polynomial, but no |D|-type bound.
- A linear-size variant (mkalt2.py, one tapped delay line per side) FAILS to separate the arrivals: once an edge into the line is
  improving, S4a's arena optimum takes the whole improved line in one step (max 1 change at every K). Recorded as a failed construction,
  not as evidence.
### What this changes
- (R2) stays OPEN, with a sharper target: offset changes per vertex per stretch_D are not O(|D|). They are ≥ Θ(√n) on this family and
  ≤ (n − 1) + 2^{B+1} by TWIN-GAP. The family's band is wide (B = 167 at K = 10), so TWIN-GAP is far from tight here.
- The mechanism is delay chains on routes. Each return is paid by a fresh higher even vertex reaching the route, i.e. by a W-change
  at level > the previous one. CONJECTURE (new, to test): offset changes of v per stretch_D ≤ the number of distinct levels at which
  s^W(v) or s^Ξ(v) rises (≤ n). Not attempted yet.

## 11. Lemma PIECE_D and Corollary SPLIT-RED (PROVED, every game; Lead's GO 07:09Z), and the split-state count (DATA)
Setting. S: a fallback-free run inside one phase of N5 on any game (τ constant, so G_τ is one fixed one-player game). At a state k ∈ S an
Even edge (x, z), z ≠ a := σ_k(x), is SPLIT if it is improving in exactly one frame: [Ξ_k(z) ▷ Ξ_k(a)] ≠ [W_k(z) ▷ W_k(a)]. The state k is
ALIGNED if it has no split edge. N_split(S) := the number of transitions of S whose source state is not aligned.
### Lemma PIECE_D
- (a) At an aligned state k, Iσ_k equals the improving set of σ_k in the one-player game G_τ, and the S4a step k → k+1 is a switch-best
  step of G_τ from σ_k (RESULTS R17's rule, for SPEC's pointwise-optimal choice).
- (b) If every transition of a block B of consecutive transitions of S has an aligned source and λ_W is constant on B, then B has fewer
  than n + m transitions (m := the number of edges).
Proof.
- (a) SPEC S2 gives Iσ_k = {(x, z) : Ξ_k(z) ▷ Ξ_k(σ_k x)}. In G_τ every Odd vertex has out-degree 1, so S1's valuation of σ_k on G_τ is the
  play valuation W_k, and G_τ's improving set is {(x, z) : W_k(z) ▷ W_k(σ_k x)} (R17's setting, VJ00 §4.4 eq. (2)). Alignment makes the
  two sets equal.
  - S4a takes σ_{k+1} := Even's pointwise optimum in the arena H_k of G_τ, in which Even's x may use {σ_k(x)} ∪ Iσ_k(x). That is R17's
    switch-best arena on G_τ.
  - R17 (d) holds for every pointwise-optimal choice.
- (b) By (a), B is a run of switch-best on G_τ started at its first state. λ_W is G_τ's cycle-node map, so B lies in one λ-phase of that
  run. R17 (c) (Theorem PH: a λ-phase has fewer than n + m steps) bounds |B|. □
### Corollary SPLIT-RED
Under (h3_D) at every state of S: |S| ≤ N_split(S) + (N_split(S) + 1)·(n + m − 1).
Proof. λ_W is constant on S (P-N5-H3 §6, (ii)). The maximal blocks of transitions with aligned sources number ≤ N_split + 1, each with
< n + m transitions by PIECE_D (b). The other transitions number N_split. □
- This is a two-gate (indeed any-gate) form of RESULTS R19 (f) PIECE. Where R19 (f) has (h) and a route game with o's frozen continuation,
  here "aligned" is the exact condition under which N5's Even step IS switch-best on G_τ.
- On the OFFSET-ONCE counterexamples (§10) every state is aligned: offret_n23 (4 transitions) and offalt_K10 (24 transitions) are single
  aligned blocks. Their offset returns are inside one switch-best λ-phase, which R17 bounds.
### What a split edge is (by MERGE-B; READING with DATA)
- Under (h3_D), different cycle nodes compare by reward in both frames, so a split edge joins z and a with one cycle node. If Δ(z) ≠ Δ(a)
  it is an OFFSET split; if Δ(z) = Δ(a) the path sets compare alike (MERGE-B) and lengths decide, a LENGTH split.
- FORBIDDEN edges, improving in W but not in Ξ, are the ones that matter for R17's Lemma P (its Case B needs only "W-improving ⇒ in the
  arena"). EXTRA edges, the other direction, only enlarge the arena. In the data every split state has a forbidden edge.
### DATA (piece.py; checks ARENA_V (our Ξ-improving set vs G_τ's at aligned states), BLOCK_V (R17's bound per aligned block), RED_V
(SPLIT-RED); SPEC_MISMATCH (our Ξ-improving set vs n5x's Is) also 0; MUT=1 (block bound 2) fails on frz1_n24)

| set ((h3_D) runs only) | runs | transitions | split sources (forbidden / extra) | max per run | max aligned block | split edges: offset / length |
| --- | --- | --- | --- | --- | --- | --- |
| lib41 (≥ 2 Odd choices, n ≤ 48), S3 + 2 random starts | 119 | 469 | 290 (287 / 230) | 14 | 11 | 2,118 / 0 |
| lib2o, S3 | 32 | 127 | 106 (106 / 93) | 11 | 10 | 933 / 0 |
| random 𝒞^2O, 6,000, n 5-14, seed 62 | 923 | 991 | 5 (2 / 3) | 2 | 3 | 3 / 2 |
| random 𝒞^kO, 6,000, n 5-14, seed 63 | 733 | 789 | 5 (3 / 3) | 1 | 3 | 0 / 7 |
| frz1_n24 (its .start) | 2 | 28 | 20 (20 / 18) | 16 | 8 | 129 / 0 |
| frz3_n24 (its .start) | 1 | 24 | 17 | 17 | 7 | 101 / 0 |
| offret_n23, offalt_K10 (their .start) | 1 + 1 | 4 + 24 | 0 | 0 | 4, 24 | — |
| L-COMP's notnc1-8 (l-comp 95f35638, their .start) | 8 | 8 | 0 | 0 | 1 | — |

- 0 violations everywhere. On the library and on the long runs, split states are the MAJORITY of transitions (290 of 469; 17 of 24 on
  frz3_n24), all of them offset splits with a forbidden edge. So SPLIT-RED is correct but its remainder N_split is not small in data.
- Typical forbidden edge (frz1_n24, below.py): x ∈ R_D with a := σ(x) ∈ R_D and z ∈ F_D. The gate's Ξ value holds the top vertex
  (rank 23) and its W value does not, so W prefers z and Ξ does not. These edges stay forbidden for the whole stretch_D.
### What is left (OPEN)
- N_split per run. Since the forbidden edges are persistent and structural (R_D → F_D across an offset gap), the natural next statement
  is Lemma P restricted to paths whose edges are never forbidden on S. That is a per-offset-class P^c (R50 FRZ-U's "paths inside R to o"
  with the offset class for R). Then one counts the transitions not covered by it. Not attempted yet.

## 12. CONJECTURE LEVEL-COUNT (Lead's GO 07:20Z): tests, a dead strong form, and the step a proof would need
Notation: inside one stretch_D segment of a run with (h3_D), for v with constant cycle nodes, OC(v) := the transitions at which Δ(v)
changes, and RL(v) := the RISE LEVELS of v. A rise level is the top rank of P_k Δ P_{k+1} at a transition where s^W(v) or s^Ξ(v) rises.
- CONJECTURE LEVEL-COUNT (count form): |OC(v)| ≤ |RL(v)| (≤ n).
- Strong form INC ("levels only increase"): the rise level at successive offset changes of v strictly increases. It would give the count
  form at once.
### Lemma RULER (PROVED, elementary; WM-G / (SG) give exactly this and no more)
For one score (s^W(v), or s^Ξ(v)) along a run on which v's cycle node is constant, two rises at the same level r are separated by a rise at
a level > r.
Proof.
- A rise at level r flips the membership of rank r in the path set in the weight-increasing direction: an even r is added, or an odd r
  is removed. Every lower rank may change.
- A second rise at level r needs r flipped back in between. The transition doing that changes the set at level ≥ r.
- At exactly r it would be a fall, against monotonicity (WM-G for W, (SG) for Ξ). So its level is > r, and it rises. □
- Hence the rises of one score form a ruler sequence on the levels RL(v): |rises| ≤ 2^{|RL(v)|} − 1. By TWIN-GAP (i) each offset change
  is a rise of one score, so |OC(v)| ≤ 2·(2^{|RL(v)|} − 1). That is all monotonicity gives.
- The step the count form needs and RULER does not give: no level is used by two offset changes of v (two returns cannot reuse a level
  with only a higher rise in between). Neither WM-G nor (SG) gives it. A proof must use the dynamics (S4a's arena and the delay
  structure), not monotonicity.
### DEAD: the strong form INC (instance)
- experiments/si/rund/instances/incdown_n23.pg (sha1 18a5d000…) with incdown_n23.start (sha1 634dbc59…). Built by mkinc.py 2 4, which is
  mkret.py with the safe exit s1 of the u1 route made a HIGH ODD vertex (3901 > h = 3800 > y2 = 3600).
  - v = 22 leaves u1 for u2 because u1's route holds the odd s1: a rise at level 20, s1's rank.
  - It comes back when the delay chain delivers the route through h without s1: a rise at level 19 < 20.
  - Trace logs/trace_incdown_n23.txt: states 0-3 are one phase and one stretch_D (D = {4, 12}, gates unchanged, c = 0, (h3_D), no
    fallback). lvl.py prints `VIOLATION ('INC', 'instances/incdown_n23.pg', 0, 3, 22, [20, 19])`. The count form holds there (2 changes, 2 levels).
- Mechanism: a return can be paid by REMOVING a high odd vertex and winning at a lower level. So rise levels at offset changes need not
  increase. Variants mkinc.py m LG, with (m, LG) = (2, 5), (2, 6), (3, 5), (3, 6), give the same.
### DATA for the count form (lvl.py; LC_V counts violations)
| set | stretch_D segments | vertices with an offset change | max offset changes of one vertex in one segment | LC_V |
| --- | --- | --- | --- | --- |
| lib41 (≥ 2 Odd choices, n ≤ 48), S3 + 2 random starts | 138 | 12 | 1 | 0 |
| random 𝒞^2O, 6,000, n 5-14, seed 62 | 824 | 0 | 0 | 0 |
| offret_n23 / incdown_n23 | 1 / 1 | 1 / 1 | 2 / 2 | 0 / 0 |
| mkalt K = 4, 8, 10 | 1 each | 1 each | 3, 7, 9 | 0 |
- Natural data never has two offset changes of one vertex in one stretch_D. The count form is tested only on constructions, so it is
  weakly supported: CONJECTURE, DATA on the constructions only.
- Suggested attack for L-RED: combine mkalt's alternation with mkinc's odd-removal returns, so that a vertex alternates sides with rise
  levels a, b, a, … (b > a). That is the pattern RULER allows and the count form forbids. Breaking it needs routes that reuse vertices
  across time (positional routes at one time are disjoint after they diverge, but not across times).
