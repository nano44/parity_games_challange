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

## 13. The restricted Lemma P (Lead's GO 07:30Z, first attempt): Lemma P^c_ok and Corollary FRZ-OK (PROVED, every game) and DATA
Setting. S: a fallback-free run inside one phase on which CR-D's (ii) holds (λ_W constant; e.g. (h3_D) at every state, P-N5-H3 §6).
Level −1 ≤ L < ∞, COARSE := COARSE_L. An Even edge (x, z) is FORBIDDEN AT k (at level L) if z ≠ a := σ_k(x),
COARSE(W_k(z)) ≻ COARSE(W_k(a)) and not Ξ_k(z) ▷ Ξ_k(a). It is OK ON S if it is forbidden at no state of S.
### Lemma P^c_ok
For every j with k_0 + j ∈ S, every x, and every simple path r of G_τ from x to a vertex u with λ_W(u) = u, with ≤ j edges, ALL OF
WHOSE EVEN EDGES ARE OK ON S: Ω^c_{k_0+j}(x) ⪰ COARSE(value(r)).
Proof. P^c_L's proof (P-N5-H3 §5) verbatim, with (i) used only where it is used there:
- In Case B at the first edge (x, z) of r, at state k, (i) is used to turn Ω^c_k(z) ≻ Ω^c_k(a) into Ξ_k(z) ▷ Ξ_k(σ_k x). That is exactly
  "(x, z) is not forbidden at k". The edge is OK, so the step holds.
- The induction hypothesis is applied to the suffix r′, whose Even edges are OK too.
- Cases A, B1 and B2 use only (ii), WM-G and (F1). □
### Corollary FRZ-OK
For every t ∈ S with t ≥ k_0 + n − 1 and every x whose W-play prefix at t (to its cycle node) uses only OK Even edges:
COARSE(W_t(x)) = COARSE(W_{k_0+n−1}(x)).
Proof. As CR-D's proof. That prefix is a simple path r_t of G_τ with ≤ n − 1 edges to λ_W(x), constant by (ii), and its Even edges are
OK. Then P^c_ok at j = n − 1 and (MON) from k_0 + n − 1 to t give two inequalities, and (C3) makes them an equality. □
- This is CR-REL with the edge order transfer required only on the edges the lower bound uses. FRZ-OK freezes vertex by vertex, at
  full resolution (L = −1) if wanted, where CR-D / FRZ-U_H3 freeze globally at L ≥ max M_D (content-free in data, §3).
### DATA (okfrz.py, L = −1; logs/okfrz_long.txt; the three long (h3_D) runs; MUT=1, freeze from k_0 + 1, fails on all three)

| instance | pairs (t, x), t ≥ k_0 + n − 1 | covered (play uses only OK edges) | covered with content (non-empty path part) | edges forbidden somewhere on S | FRZOK_V |
| --- | --- | --- | --- | --- | --- |
| frz1_n24 (.start) | 24 | 2 | 1 | 9 | 0 |
| frz3_n24 (.start) | 24 | 2 | 1 | 12 | 0 |
| pftheta34_n32 (S3) | 96 | 17 | 14 | 14 | 0 |

- FRZ-OK has CONTENT where FRZ-U_H3 has none: 14 frozen full values with non-empty path parts on pftheta34_n32.
- Coverage is low: most W-plays use an edge that was forbidden at SOME state of the run (9-14 such edges per run).
### Where this stops (exact state for successor 13)
- "OK on S" is too strict: an edge forbidden only early in S blocks the lower bound for the whole run.
- Next statement to try, P^c_ok(t): with "OK on [k_0 + j′, …]", i.e. edges not forbidden after some state. The induction in P^c_L can start
  at any state of S, so the lower bound restarts at the last forbidden state of the path's edges. If edges stop being forbidden after
  ≤ p(n) transitions, the freeze holds from there. DATA needed first: per run and edge, the last state at which it is forbidden.
- If, instead, some edge stays forbidden through the whole run while x's play uses it, x is not covered. Then the count needed is how
  often x's value can change while its play uses a persistently forbidden edge. That is the N_split question of §11 in per-vertex form.

## 14. Lemma P^c_sch: the restricted Lemma P with an exact per-edge schedule (successor 13, Lead's GO 08:08Z; PROVED, every game) and DATA
Written 2026-10-26 08:1xZ onward (date -u) by L-SI successor 13 (session_018EgSbDTYEVHqL882sCoX7u). Continues §13 from its stopping point.
Setting as §13: S = states k_0, …, k_1 inside one phase, every transition an S4a step (no fallback), and CR-D's (ii) (the W-cycle-node map
λ_W is the same at every state of S). (h3_D) is NOT assumed; (ii) is all the proof uses. Level −1 ≤ L < ∞; "forbidden at k" as in §13.
- The observation: in P^c_L's step from k to k + 1 (P-N5-H3 §5), hypothesis (i) is used ONCE, in Case B, on the FIRST edge (x, z) of r,
  at state k. The suffix r′ enters only through the IH at state k. Unrolled, edge q of a path that is used at state k is looked at only at
  state k − 1 − q. "OK on S" (§13) asks for every state; the proof needs one state per edge.
- Definition. For a simple path r = (r_0, …, r_m) of G_τ ending at a W-cycle node, and a state k ∈ S: the SCHEDULE of r at k is CLEAN if
  k − m ≥ k_0 and, for every q < m with r_q Even, the edge (r_q, r_{q+1}) is not forbidden at state k − 1 − q.
### Lemma P^c_sch (PROVED, every game)
If the schedule of r at k is clean, then Ω^c_k(r_0) ⪰ COARSE(value(r)).
Proof. Induction on m, for all k at once.
- m = 0: r = (u), and Ω_k(u) = (u, ∅, 0) by (ii) (k ≥ k_0).
- m ≥ 1: r = x → z → r′ with r′ simple, avoiding x, m − 1 edges. The schedule of r′ at k − 1 is clean: (k − 1) − (m − 1) = k − m ≥ k_0,
  and edge q′ of r′ is edge q′ + 1 of r, looked at in both at state (k − 1) − 1 − q′ = k − 1 − (q′ + 1). So the IH gives
  Ω^c_{k−1}(z) ⪰ COARSE(value(r′)).
- Now P^c_L's step from k − 1 to k, verbatim (Cases A1, A2, B1, B2), with k − 1 in the role of its k:
  - Cases A1, A2 use the IH, (V2c), (MON) and (ii) only.
  - Case B (x Even, Ω^c_{k−1}(z) ≻ Ω^c_{k−1}(a), a = σ_{k−1}(x)): P^c_L uses (i) to get Ξ_{k−1}(z) ▷ Ξ_{k−1}(a). If that failed, (x, z)
    would be forbidden at k − 1 (z ≠ a, since Ω^c(z) ≠ Ω^c(a)). Edge 0 of r is not forbidden at k − 1 − 0, so it holds. The rest of
    Case B (B1, B2) uses (F1) on the S4a arena, the IH, (C4), (V2c) and (ii) only. □
### Corollary FRZ-SCH (PROVED, every game)
For s ≤ t in S and any x, let r_t be x's W-play prefix at t (to λ_W(x)), with m edges. If the schedule of r_t at s is clean, then
COARSE(W(x)) is constant on [s, t].
Proof. Ω_t(x) = value(r_t), by (ii) and λ_W(x) being a W-cycle node at every state (CR-D's proof). P^c_sch at s gives
Ω^c_s(x) ⪰ Ω^c_t(x); (MON) gives Ω^c_t(x) ⪰ Ω^c_{s′}(x) ⪰ Ω^c_s(x) for s ≤ s′ ≤ t; (C3). □
- It contains FRZ-OK (§13: an OK play is clean at every s ≥ k_0 + m) and CR-D / FRZ-U_H3 (under (i) nothing is forbidden), and it
  starts the freeze at k_0 + m, where m is the length of x's own play prefix, not at k_0 + n − 1.
### Corollary CHARGE (PROVED, every game): N_split in per-vertex form
Every change of COARSE(W(x)) at a transition s − 1 → s of S is one of:
- a WINDOW change: s − 1 − m < k_0, where m is the length of x's W-play prefix at s (so s ≤ k_0 + n − 1: at most n − 1 per x per run); or
- a CHARGED change: x's W-play prefix r at s has an Even edge (r_q, r_{q+1}) that is FORBIDDEN AT STATE s − 2 − q.
Proof. FRZ-SCH at (s − 1, s): if the schedule of r at s − 1 were clean, COARSE(W(x)) would be constant on [s − 1, s]. □
- Consequence (PROVED): per vertex x and run S, changes of COARSE_L(W(x)) ≤ (n − 1) + #{s : x's play at s has a scheduled forbidden
  edge} ≤ (n − 1) + n·|K_F(S)|, where K_F(S) := the states of S at which some Even edge is forbidden. (A charged state lies in
  [s − 1 − m, s − 2], so each forbidden state is charged by ≤ n values of s.) So a run with no forbidden state for n consecutive states
  freezes at full resolution (L = −1) from there.
- What is left is EXACTLY the forbidden (edge, state) pairs on the schedule of the vertex's own new play. That is the §11 remainder
  N_split, now per vertex and per state.
### DATA (sched.py, L = −1; runs = maximal fallback-free in-phase runs with λ_W constant; logs/sched_long.txt, logs/sched_lib41_rs2.txt)
Per forbidden edge: the states at which it is forbidden, first and last (relative to k_0), PERSISTENT if forbidden at the last state of S.

| set | runs | states | forbidden edges (persistent) | max states one edge is forbidden | max last forbidden state (rel.) | changes | window | charged (to a persistent edge) | GEN pairs checked (content) | violations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| frz1_n24 (.start) | 2 | 30 | 11 (2) | 15 | 15 (run of 24 transitions) | 59 | 20 | 39 (0) | 2,693 (2,383) | 0 |
| frz3_n24 (.start) | 1 | 25 | 12 (0) | 17 | 16 (run of 24) | 56 | 16 | 40 (0) | 2,661 (2,361) | 0 |
| pftheta34_n32 (S3) | 1 | 35 | 14 (0) | 29 | 32 (run of 34) | 84 | 56 | 28 (0) | 7,784 (7,189) | 0 |
| lib41, S3 + 2 random starts | 156 | 812 | 568 (472) | 14 | 13 | 1,646 | 1,609 | 37 (0) | 31,636 (27,724) | 0 |

- Answers to §13's DATA question (the last forbidden state per edge, long runs): on the three long runs NO edge stays forbidden to the
  end, except two edges in frz1's first, 4-transition run. Every edge stops being forbidden by relative state 15 (frz1), 16 (frz3), 32
  (pftheta34, n = 32). Forbidden states form one interval per edge in most cases (count = last − first + 1); some have gaps (frz3 (8, 23):
  8 states in 0..15).
- P^c restarted at the last forbidden state ℓ: by FRZ-SCH a vertex whose play has m edges is frozen at full resolution from state
  ℓ + 1 + m on (relative). With ℓ = 15, 16, 32 on runs of 24, 24, 34 transitions, this restart covers only short plays at the run's end;
  the per-state schedule (GEN column) covers far more pairs.
- No change is ever charged to a persistent edge (0 everywhere), and on lib41 the runs are short (≈ 5 states), so the window takes 1,609
  of 1,646 changes. Max charged changes of one vertex in one run: 4 (frz1), 3 (frz3), 1 (pftheta34, lib41).
- A forbidden edge is forbidden at most 29 states (pftheta34, n = 32); never more than n − 1 in any data (FORB_GT_N1 = 0).
- Mutation controls: MUT=1 (schedule shifted by one state: edge q at state k − q) FAILS on all three long runs, and MUT=2 (forbidden-ness
  ignored: CR-D without (i)) FAILS on all three. So the schedule is exact to the state, and the forbidden-edge condition is needed.
### OPEN (named exactly)
- (FS) |K_F(S)|: forbidden states per run. By CHARGE, a polynomial bound on |K_F(S)| (or on the scheduled forbidden pairs on each
  vertex's own play) bounds the coarse W-changes per vertex per run at L = −1. DATA: |K_F| ≤ 33 on the long runs (n 24-32). No argument
  yet; it is the N_split question of §11 in its sharpest data form. An edge (x, z) is forbidden when W says z beats σ(x) and Ξ does not;
  it stops when Ξ catches up (then (x, z) is improving) or W(σ(x)) catches up. A duration bound per edge (≤ n − 1 in all data) would be
  the next statement to try.

## 15. LEVEL-COUNT (count form) is DEAD (L-RED); a corrected form LC2 / PAIR-OC (CONJECTURE, DATA) (successor 13)
- DEAD (L-RED's kill, reproduced here with my own lvl.py; DEAD.md box 17d): CONJECTURE LEVEL-COUNT (count form) |OC(v)| ≤ |RL(v)|.
  - experiments/red/h3/instances/lcount_n23.pg (sha1 f86125a08f0e3b0caf3d825cb48e6dcdc0ee3b04), start lcount_n23.start: v = 1, OC 3,
    RL {18, 21}. lvl.py prints `VIOLATION ('LC', '…lcount_n23.pg', 0, 3, 1, 3, [18, 21])`.
  - lcount2_n23.pg (sha1 dd9847c6b19cb9f44af73bcc23de7ca2aca9a14c, L-RED's cl_171): v = 12, 16, 20 with OC 3 and RL {20, 21}.
  - Obstruction (DATA, both instances): a LAG. The events of v = 1 on lcount_n23 (transition, W rise level, Ξ rise level, offset change):
    (0, 18, –, yes), (1, –, 18, yes), (2, 21, 21, yes). W rises at 18 and changes the offset; one transition later Ξ rises at the SAME
    level 18 and changes it back. RL counts the level once; the two scores use it once each. RULER (per score) is not contradicted.
- Corrected forms (CONJECTURE, with the reason and the tests the Lead asked for):
  - SL(v) := the (score, level) pairs of v's rises (score W or Ξ), so |SL(v)| ≤ 2·|RL(v)| ≤ 2n.
  - CONJECTURE LC2: |OC(v)| ≤ |SL(v)| (so ≤ 2·|RL(v)|, the Lead's suggested form, and ≤ 2n).
  - CONJECTURE PAIR-OC (stronger; implies LC2 by TWIN-GAP (i), each offset change is a rise of a score): no (score, level) pair rises at
    two offset changes of v in one stretch_D segment.
  - Reason it may survive: the kill's mechanism uses each (score, level) once (the lag W-then-Ξ at one level). Breaking PAIR-OC needs ONE
    score to rise at a, b, a (b > a) at three offset changes, the ruler pattern RULER allows. That needs a high rise that undoes a lower
    flip and a later return at the lower level, each with a gate change. No known construction does it.
  - Reason it may not: nothing proves it. PAIR-ONCE for ALL rises (not only at offset changes) is likely false by separate delay chains
    (three routes of v delivered at times 1, 2, 3 with path sets {a}, {b}, {a, b}); it was not built, since it would not touch the count.
- Tests (lvl2.py; LC2_V, PAIROC_V, OC_NORISE (an offset change with no rise; TWIN-GAP (i) says 0), PAIR_ALL_V):

| set | stretch_D segments | v with an offset change | max OC of one v | max rises of one v | LC2_V | PAIROC_V | OC_NORISE | PAIR_ALL_V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lcount_n23 (L-RED) | 1 | 11 | 3 | 4 | 0 | 0 | 0 | 0 |
| lcount2_n23 (L-RED cl_171) | 1 | 9 | 3 | 5 | 0 | 0 | 0 | 0 |
| offret_n23 / incdown_n23 / offalt_K10 | 1 / 1 / 1 | 1 / 1 / 1 | 2 / 2 / 9 | 4 / 4 / 20 | 0 | 0 | 0 | 0 |
| lib41, S3 + 2 random starts | 138 | 12 | 1 | 6 | 0 | 0 | 0 | 0 |
| random 𝒞^2O, 6,000, n 5-14, seed 62 | 824 | 0 | 0 | 2 | 0 | 0 | 0 | 0 |
| random 𝒞^kO (k 2-4), 6,000, n 5-14, seed 63 | 648 | 0 | 0 | 4 | 0 | 0 | 0 | 0 |

  - Control: MUT=1 (count only W's pairs in SL) FAILS on lcount_n23 and lcount2_n23 (LC2_V). Logs: logs/lvl2_inst.txt, lvl2_lib41_rs2.txt,
    lvl2_rand2o.txt, lvl2_randkO.txt, lvl_lcount.txt.
  - Support is thin: natural data has ≤ 1 offset change per vertex per segment; only constructions test LC2 non-trivially (5 instances).
- Suggested attack for L-RED (not run here; L-RED owns the climbs): one score of v rising at a, b, a (b > a) at three offset changes,
  e.g. mkalt's alternation with mkinc's odd-removal step and a later re-add of the even a.

## 16. (FS) box (Lead's GO 08:32Z): FS stated; the charge goes to SWITCHES, not durations (Lemma UNF, PROVED); CONJECTURE UF-ONCE
Written 2026-10-26 08:3xZ onward (date -u), successor 13. Setting, "forbidden" and L = −1 as §14.
### CONJECTURE FS (the Lead's form, stated exactly)
For every Even edge e and every state k of S: if e is forbidden at k, then e is forbidden at no state k′ ≥ k + n. (So each edge is forbidden at
≤ n states of S, |K_F(S)| ≤ n·m, and by CHARGE coarse W-changes per vertex per run ≤ (n − 1) + n²·m.)
- DATA (sched.py FS_SPAN_V, FS_DUR_V): 0 violations on the long runs, lib41 and lib2o (S3 + 4 random starts), the five constructions, and
  14,000 random games. The largest span (last − first) is 28 at n = 32 (pftheta34). Random runs are short (≤ 3 states), so only the long runs
  and the libraries test FS.
- FS is NOT what CHARGE needs (next lemma): a forbidden edge that is never taken is never charged. FS would also fail on any run that keeps
  one edge statically forbidden (W(z), W(σx), Ξ(z), Ξ(σx) frozen) for ≥ n more states while other vertices still move; nothing excludes
  that. FS stays a CONJECTURE; I did not try to prove it.
### Fact FZ (PROVED, every game, under the standing SPEC premise that σ̄_k is Odd's optimal counterstrategy in G_{σ_k})
If (x, z) is forbidden at k, then Ξ_k(z) ◁ W_k(z), so z's W-play meets D_k.
Proof. (F1) for Odd's one-player game G_{σ_k} gives Ξ_k ⊴ W_k pointwise (σ̄_k is optimal there and τ_k is a strategy of it). With
a := σ_k(x): Ξ_k(z) ⊴ Ξ_k(a) (forbidden: not Ξ_k(z) ▷ Ξ_k(a); ⊴ is total) ⊴ W_k(a) ◁ W_k(z), the last step by COARSE W(z) ≻ COARSE W(a) and (Cstrict). If z's W-play
met no vertex of D_k, the two plays from z would coincide and Ξ_k(z) = W_k(z). □
- DATA: FZ_EQ_V = 0. Gate classes of forbidden (pair, state)s: on the long runs all 304 (67 + 93 + 144) have σ(x) ∈ F_D and z gated; on
  lib41 RS4, 2,652 of 2,946 do, 293 have z and σ(x) on different gates, 1 the same gate.
### Lemma UNF (PROVED, every game)
Let a change of COARSE W(x) at s − 1 → s be CHARGED (§14) to (q, e = (r_q, r_{q+1}), f = s − 2 − q). Then r_q SWITCHES INTO r_{q+1} at an S4a
transition k′ → k′ + 1 with f < k′ ≤ s − 1 ≤ f + n − 1, and e is not forbidden at k′.
Proof.
- r is x's W-play prefix at s and r_q is Even, so σ_s(r_q) = r_{q+1}. Forbidden at f needs r_{q+1} ≠ σ_f(r_q).
- Let k′ be the largest k ∈ [f, s − 1] with σ_k(r_q) ≠ r_{q+1}. Then σ_{k′+1}(r_q) = r_{q+1}.
- SPEC S4a: σ_{k′+1}(v) ∈ {σ_{k′}(v)} ∪ Iσ_{k′}(v). So e ∈ Iσ_{k′}: Ξ_{k′}(r_{q+1}) ▷ Ξ_{k′}(σ_{k′}(r_q)), and e is not forbidden at k′. So k′ ≠ f.
- s − 1 − f = q + 1 ≤ m ≤ n − 1. □
### Corollary CHARGE-U (PROVED, every game)
Let U(S) := the S4a switch events (k′, e) of S (e = (y, z) with σ_{k′}(y) ≠ z = σ_{k′+1}(y)) such that e is forbidden at some state in
[k′ − n + 1, k′ − 1] ∩ S (UNFORBID-SWITCHES). Then for every x, changes of COARSE_{−1}(W(x)) on S ≤ (n − 1)·(1 + |U(S)|).
Proof. ≤ n − 1 WINDOW changes (§14). A charged change at s gets an event (k′, e) ∈ U(S) by UNF, with k′ + 1 ≤ s ≤ k′ + n − 1; so one event is
used by ≤ n − 1 values of s. □
- In particular an edge that is forbidden and never taken afterwards (a persistent edge) is never charged (DATA: 0 such charges, §14).
- DATA (UNF_V = 0, SWITCH_INTO_FORB_V = 0 everywhere):

| set | runs | states | S4a switches | |U| total | max |U| per run | max U events of one vertex in one run |
| --- | --- | --- | --- | --- | --- | --- |
| frz1 / frz2 / frz3 (n 24) | 2 / 1 / 1 | 30 / 24 / 25 | 44 / 36 / 38 | 7 / 5 / 6 | 7 / 5 / 6 | 1 |
| pftheta34_n32 | 1 | 35 | 74 | 7 | 7 | 1 |
| lib41, S3 + 4 random starts | 243 | 1,230 | 1,514 | 63 | 6 | 1 |
| lib2o, S3 + 4 random starts | 121 | 828 | 956 | 30 | 3 | 1 |
| random 𝒞^2O / 𝒞^kO (6,000 each, n 5-14) and 𝒞^kO 2,000 (n 15-24) | 927 / 737 / 641 | 1,923 / 1,530 / 1,367 | 1,288 / 1,009 / 1,150 | 0 / 0 / 1 | 0 / 0 / 1 | 1 |
| lcount_n23, lcount2_n23, offret_n23, incdown_n23, offalt_K10 | 1 each | 4-25 | 10-177 | 0 | 0 | – |

### CONJECTURE UF-ONCE (DATA; replaces FS as the target)
In every run S, every Even vertex makes at most one unforbid-switch: |{(k′, e) ∈ U(S) : e leaves y}| ≤ 1 for every Even y. Then |U(S)| ≤ n_E and,
by CHARGE-U, every vertex's full-resolution coarse W value changes ≤ (n − 1)(n_E + 1) times per run (a polynomial per run; runs per phase
are cut by fallbacks and λ_W changes, counted elsewhere).
- DATA: 0 violations (UF_ONCE_V) on all sets above; max 1 per vertex per run in 101 U events. Thin support: U events occur only in the
  libraries and the long runs; the constructions have none.
- What a counterexample needs: one Even y that is W-tempted by a gated z (z's route meets D, Fact FZ), is blocked by Ξ, is later
  allowed and switches, and then again for a second gated z″ within the same run. No proof attempt yet. Suggested L-RED target.
### CORRECTION to §11's READING (successor 13)
- §11 says the typical forbidden edge has σ(x) ∈ R_D and z ∈ F_D, "W prefers z and Ξ does not". By Fact FZ that pattern cannot be
  forbidden: z ∈ F_D gives Ξ(z) = W(z) ≻ W(σx) ⊵ Ξ(σx). The data (sched.py gate classes) has σ(x) ∈ F_D and z gated. The READING is
  withdrawn; no PROVED item used it. Packet P-N5-RUND-box17 §4 carries the correction.

## 17. Proof attempt on UF-ONCE (Lead's GO 08:56Z): where it stops, Lemma OFFUP (PROVED), CONJECTURE U-SPLIT (a reduction to (R2) + (R4))
Written 2026-10-26 09:0xZ onward (date -u), successor 13. Setting of §14 / §16; offsets of §3 of the packet (note §5). L = −1.
### DATA first (sched.py USTRUCT=1; logs/ustruct.txt; the long runs, lib41 and lib2o with 4 random starts each; 118 U events)
- In all 118, Ξ(z) ROSE between the forbidden state f and the switch k (Ξ catches up); f = k − 1 in most. σ(y) was in F_D in 109.
- y has a forbidden edge again later in the same run in 4 of 118; never a second U event (UF_ONCE_V = 0).
### Lemma OFFUP (PROVED, every game)
If (x, z) is forbidden at k (L = −1), a := σ_k(x), and λ_Ξ = λ_W at z and at a, then Δ_k(z) > Δ_k(a). (Under (h3_D) on S the hypothesis
holds at every vertex, OFFSET (a).) So a forbidden edge points to a strictly HIGHER offset.
Proof.
- If λ(z) ≠ λ(a): both frames compare these values by the reward of the cycle node first, with the same cycle nodes. COARSE W(z) ≻ COARSE
  W(a) then gives reward(λ z) > reward(λ a), hence Ξ(z) ▷ Ξ(a): not forbidden. So λ(z) = λ(a).
- With one cycle node, S1's order (and COARSE_{−1}'s) compares path sets, and on sets that order is the order of w (OFFSET (a)'s proof).
  COARSE W(z) ≻ COARSE W(a) gives s^W(z) > s^W(a). Not Ξ(z) ▷ Ξ(a) gives Ξ(z) ⊴ Ξ(a), hence s^Ξ(z) ≤ s^Ξ(a) (a larger w would be a
  larger path set and Ξ(z) ▷ Ξ(a)). Subtract. □
- DATA: OFFUP_V = 0 on 4,184 forbidden (pair, state)s with matching cycle nodes; 726 had λ_Ξ ≠ λ_W at z or a (¬(h3_D) states), outside the lemma.
### Where the UF-ONCE attempt stops (READING; the obstruction)
- OFFUP says a U event of y is a move toward a higher offset at the forbidden state f. A second U event of y needs y to be tempted
  again, by a still higher offset, or after y's offset has come DOWN.
- Coming down is allowed: an ordinary (non-U) Ξ-improving switch can lower y's offset, and offset returns exist inside one stretch_D
  (OFFSET-ONCE is DEAD: offret_n23, mkalt). Nothing in OFFUP, UNF, monotonicity or S4a's arena forbids the cycle U-up, return-down,
  U-up. I see no invariant that would; so I do NOT expect UF-ONCE to be provable in this form, and it may be false. The constructions
  have no forbidden edges at all (U = 0), so the obvious test is missing. Kill shape for L-RED (sent by the Lead): mkalt-style
  return of y to offset 0 combined with two U-tempting gates of different offsets.
- UF-ONCE stays a CONJECTURE (DATA 0 / 118), weak.
### CONJECTURE U-SPLIT (DATA; replaces UF-ONCE as the statement to prove)
Under (h3_D) on S, every U event (k, (y, z)) with forbidden state f ∈ [k − n + 1, k − 1] satisfies one of:
- (UP) y's offset rises at k → k + 1: Δ_{k+1}(y) > Δ_k(y); or
- (BD) a stretch_D boundary lies in [f, k + 1]: D, or a gate's (Ξ, W) value, differs at two states of [f, k + 1].
DATA: 118 of 118 (UP 73, BD 45, neither 0; U_OTHER pinned as a violation class in sched.py).
Consequence (PROVED from U-SPLIT, CHARGE-U and OFFSET): |U(S)| ≤ Σ_y N_y^↑ + n·n_E·B(S), where N_y^↑ := the transitions of S at which Δ(y)
rises and B(S) := the stretch_D boundaries of S (a boundary is a transition b − 1 → b with f < b ≤ k + 1; it serves U events with k ∈ [b − 1, b + n − 2], ≤ n_E per state).
So per vertex and run, the coarse W-changes are ≤ (n − 1)(1 + Σ_y N_y^↑ + n·n_E·B(S)): N_split in per-vertex form reduces to the OPEN
remainders (R2) (offset changes; ≤ 2n per vertex per stretch_D under CONJECTURE LC2, ≤ (n − 1) + 2^{B+1} by TWIN-GAP) and (R4) (stretch_D
boundaries).
- Why the proof does not close yet: with no boundary in [f, k + 1], OFFUP at f gives Δ_f(z) > Δ_f(a_f). The step needs Δ_{k+1}(y) =
  Δ_{k+1}(z) > Δ_k(a_k). But z's own gate class can change between f and k + 1 inside the stretch (z's route switches; an offset change of
  z, allowed). In 85 of 118 the inequality already holds at k; the other 33 are all BD. A proof must exclude "z dropped to a lower offset
  between f and k + 1 while staying Ξ-better than a_k". OPEN.

## 18. Proof attempt on U-SPLIT (Lead's GO 09:08Z): it stops; the obstruction, exactly (READING with an explicit scenario)
Written 2026-10-26 09:1xZ (date -u), successor 13. Setting of §17; (h3_D) on S; L = −1.
### DATA (sched.py USTRUCT=1, cross-table of the 118 U events: UP = y's offset rises at k → k + 1, BD = a stretch_D boundary in [f, k + 1],
UPK = Δ_k(z) > Δ_k(σ_k y))
| UP | BD | UPK | events |
| --- | --- | --- | --- |
| yes | no | yes | 6 |
| yes | yes | yes | 67 |
| no | yes | yes | 12 |
| no | yes | no | 33 |
- 112 of 118 U events straddle a stretch_D boundary. The no-boundary case, where the gap of §17 sits, has only 6 events (2 distinct ones,
  repeated by lib41's random starts; logs/ustruct.txt lines "NB"). There, z's offset is constant on [f, k + 1] and σ(y) ∈ F_D.
### Facts usable in the no-boundary case (PROVED, given (h3_D) on S)
- (O1) Offsets are ≥ 0: Ξ ⊴ W (Fact FZ's proof) with one cycle node gives s^Ξ ≤ s^W. F_D vertices have offset 0 (R55 (a)).
- (O2) For Even y not on its own W-cycle as its cycle node, Δ(y) = Δ(σ(y)): y adds the same signed term to both scores or to neither.
- (O3) OFFUP at f: Δ_f(z) > Δ_f(σ_f y).
- (O4) At k + 1, arena optimality: W_{k+1}(z) ⊵ W_{k+1}(σ_k y) (σ_k(y) is in y's arena); and all four scores are non-decreasing.
### The obstruction (why (O1)-(O4) do not give UP)
With σ_k(y) =: a ∈ F_D (109 of 118 events), UP says Δ_{k+1}(z) > 0, i.e. z is still gated, with a positive gate offset, at k + 1. Nothing
above forces that. Scenario (weights s^Ξ / s^W, one cycle node, gates and D fixed throughout):
- at f: a ∈ F_D with 10 / 10; z routes to a gate of offset 8 with 5 / 13. (y, z) is forbidden (13 > 10, 5 ≤ 10).
- at t ∈ (f, k): a vertex w on z's route switches from the gated route to an F_D route worth 13.5 / 13.5. That switch is Ξ-improving
  (13.5 > 5) and W-preferred (13.5 > 13), so S4a's arena optimum may take it. No D change, no gate value change: no boundary.
- at k = t + 1: Ξ(z) = 13.5 > 10 = Ξ(a). y switches to z: a U event (forbidden at f ≥ k − n + 1). y's offset is 0 → 0: neither UP nor BD.
- Every constraint used by OFFUP, UNF, WM-G, (SG), S4a's arena rule and λ_W constancy is met. So U-SPLIT does not follow from them, and
  I expect it to be FALSE; the scenario was NOT built as a game (no instance), so it is not DEAD. Kill shape for L-RED: a route of z that
  leaves its gate for an F_D route better in both frames, inside one stretch_D, within n − 1 states of a W-temptation of y.
- What the scenario shows about the remainder: such a U event is paid by a ROUTE change downstream of y (on z's play), which is itself a
  coarse W-change of z, charged by CHARGE-U to a U event on z's play, and so on. That recursion runs along plays and is depth ≤ n, but each
  level multiplies by up to n − 1 (CHARGE-U is not injective), so it gives no polynomial bound as it stands. OPEN.
- Status: U-SPLIT is a CONJECTURE with almost no data in its non-trivial case (6 events), and the scenario above says it should fail.
  UF-ONCE likewise. Per the Lead's 09:08Z instruction, I switch to (R4): stretch_D boundaries per run (§19).

## 19. (R4) stretch_D boundaries per run (Lead's 09:08Z fallback after §18): DATA, Lemma GATE-XI (PROVED), and a circularity (READING)
Written 2026-10-26 09:1xZ (date -u), successor 13. Runs as §14 (one phase, no fallback, λ_W constant). A BOUNDARY is a transition at which
the stretch key (D, and (Ξ(u), W(u)) for u ∈ D) changes; causes DCH (D changes), XI (a gate's Ξ value changes), WG (a gate's W value changes).
### DATA (bnd.py; logs/bnd_long.txt, bnd_lib41_rs4.txt, bnd_lib2o_rs4.txt, bnd_rand2o.txt, bnd_randkO_big.txt, bnd_xi.txt)
| set | runs | transitions | boundaries (DCH / XI / WG) | max boundaries per run | max Ξ changes of one gate per run | max W changes of one gate per run |
| --- | --- | --- | --- | --- | --- | --- |
| frz1 / frz2 / frz3 (n 24) | 2 / 1 / 1 | 28 / 23 / 24 | 2 (1/1/0) / 8 (6/2/2) / 8 (4/3/2) | 2 / 8 / 8 | 1 / 2 / 3 | 0 / 1 / 2 |
| pftheta34_n32 | 1 | 34 | 34 (1 / 33 / 0) | 34 | 33 (gate 0) | 0 |
| lib41, S3 + 4 random starts | 243 | 987 | 183 (113 / 85 / 13) | 6 | 4 | 2 |
| lib2o, S3 + 4 random starts | 121 | 707 | 90 (39 / 62 / 2) | 5 | 3 | 1 |
| random 𝒞^2O 6,000 / 𝒞^kO 2,000 n 15-24 | 927 / 641 | 996 / 726 | 100 / 81 | 2 / 2 | 1 / 1 | 1 / 1 |
- pftheta34_n32: EVERY transition of its 34-transition run is a boundary; all but one are Ξ-changes of the single gate 0, whose W value
  never changes. So |B(S)| can be the whole run, and (R4) is not a small remainder there: it is the run.
### Lemma GATE-XI (PROVED, every game; immediate)
At a transition k → k + 1 inside one phase, let u ∈ D_k ∩ D_{k+1} with Ξ_k(u) ≠ Ξ_{k+1}(u), u ≠ λ_Ξ(u). Then σ̄_k(u) ≠ σ̄_{k+1}(u), or
b := σ̄_k(u) = σ̄_{k+1}(u) has Ξ_k(b) ≠ Ξ_{k+1}(b). If moreover b ∈ F_D at k and at k + 1, then W_k(b) ≠ W_{k+1}(b).
Proof. (V1): Ξ(u) = u ⊕ Ξ(σ̄(u)) for u not its own cycle node, at both states. R55 (a) at both states for b ∈ F_D. □
- DATA (bnd_xi.txt; 216 Ξ-changes of gates on the long runs, lib41 and lib2o): σ̄(u) changed 85; b ∈ F_D with COARSE_{−1} W(b) changed 54,
  with only W(b)'s length changed 2 (then only Ξ(u)'s length changed); b gated 75 (the change comes through another gate's honest play).
### The circularity (READING; why §16-§19 do not close a count)
- CHARGE-U: coarse W-changes of a vertex per run ≤ (n − 1)(1 + |U(S)|).
- §18: 112 of 118 U events straddle a boundary; U-SPLIT (unproved, expected false) would give |U| ≤ Σ N^↑ + n·n_E·|B(S)|.
- GATE-XI: XI-boundaries come from W-changes of the gates' σ̄-successors in F_D (bounded by CHARGE-U), from σ̄ changes, or recursively
  through gated σ̄-successors.
- So U → boundaries → W-changes → U: each bound feeds the next with a factor ≥ n. Without an injective charge or a potential that
  drops, the chain gives no polynomial bound. In data the loop is short: the long runs are explained mostly by the n-state WINDOW of
  CHARGE (pftheta34: 56 of 84 coarse W-changes are window changes; gate 0's 33 Ξ-changes follow W-changes of its σ̄-successor inside
  that window). The asymptotic question is whether a run can be ≫ n; none of the data has one (max run 34 at n = 32).
- OPEN (named exactly): a potential that strictly drops at each U event or each XI boundary, or an injective version of CHARGE-U.
  The σ̄-changes inside a phase (85 of the 216 gate Ξ-changes) are an Odd best-reply count with no bound here (OPEN).

## 20. Potentials at boundaries and U events (Lead's GO 09:31Z, item (a)): DATA, and the tie to ρ / N_ep (READING)
Written 2026-10-26 09:3xZ (date -u), successor 13. pot.py (new): per PHASE ((λ_Ξ, τ) constant, fallbacks included), per Odd choice vertex q,
the changes of Ξ(q) (RESULTS R61 (f)'s ρ_q events), each with its level (top rank of the path-set difference; −1 = length only) and its
ALT class (R61 (e): SB = σ̄(q) unchanged, the change comes through σ̄(q)'s own value; CLEAN (strict); TIE; NONCLEAN; CYC). Logs pot_long.txt,
pot_lib41_rs4.txt, pot_lib2o_rs4.txt.
### The tie to ρ (PROVED, immediate; with RESULTS R61, R63)
- Every XI boundary (§19) is a ρ event: a gate u ∈ D_k is an Odd choice vertex, and an XI boundary is a change of Ξ(u) inside a phase.
- Every DCH boundary is a change of D, which happens only at epoch boundaries (RESULTS R63, D-EPOCH).
- So per phase: |B| ≤ ρ + (epochs − 1) + WG, with WG := the transitions changing some gate's W value. Combined with R61 (f)
  (N_ep ≤ 1 + Σ_q (ρ_q + tie_q + nc_q + cyc_q)): the boundary count of §19 is ρ up to the epoch count and WG. So the circularity of §19 is
  the ρ / N_ep problem that L-NEW and L-COMP work on, plus WG (W-changes of gates; ≤ 2 per gate per run in all data).
### DATA
| set | phases | transitions | ρ (Ξ changes of Odd choice vertices) | SB / CLEAN / TIE / NONCLEAN / CYC | at gates | max ρ_q in one phase | q with a reused level |
| --- | --- | --- | --- | --- | --- | --- | --- |
| pftheta34_n32 (S3) | 1 | 35 | 34 | 0 / 34 / 0 / 0 / 0 | 33 | 34 (> n = 32) | 1 |
| frz1 / frz2 / frz3 (n 24, .start) | 1 / 1 / 1 | 29 / 24 / 24 | 6 / 15 / 13 | 5/1/0/0/0 · 5/9/0/1/0 · 8/5/0/0/0 | 1 / 4 / 5 | 4 / 6 / 7 | 0 / 1 / 1 |
| lib41, S3 + 4 random starts | 236 | 1,238 | 1,047 | 677 / 339 / 0 / 31 / 0 | 254 | 10 | 9 of 749 |
| lib2o, S3 + 4 random starts | 75 | 811 | 246 | 145 / 101 / 0 / 0 / 0 | 90 | 7 | 2 of 91 |
- pftheta34_n32: the single gate 0's 34 Ξ changes (33 of them XI boundaries of §19) are ALL CLEAN σ̄(0)-changes, strict by ALT. 24 are
  length-only; the 10 path-set changes have levels [28, 25, 24, 31, 25, 27, 25, 24, 28, 29]. Level 25 is used 3 times, 24 and 28 twice,
  each reuse separated by a higher level (RULER holds: R_RULER_V = 0 everywhere; XI_DROP_V = 0). The length-only stretches between path-set
  changes are 1, 1, 4, 1, 1, 2, 2, 4, 6, 1, 1.
### The four candidate potentials (Lead's list), at each XI boundary and U event
- (1) Σ over gates of Ξ, (2) the σ̄ vector by κ (R61's κ is Ξ restricted to the class), (3) the multiset of Odd values, (4) W's coarse
  vector: all four are MONOTONE inside a phase ((SG) for Ξ, ALT for clean σ̄ changes, WM-G for W). So each strictly moves at every event
  that changes it, trivially; on pftheta34 (1)-(3) move at all 33 XI boundaries, and (4) moves at every U event (CHARGE-U's source).
  None drops in the wrong direction (XI_DROP_V = 0).
- What decides is the RANGE, and the data says the range is not small: gate 0's path set on pftheta34 moves in a RULER pattern (a, …, b > a,
  …, a), the binary-counter signature, inside one phase, at n = 32. A "each level once" potential for a gate's Ξ is therefore FALSE on
  pftheta34 (DATA; I had not proposed it). The only per-gate bound monotonicity gives is RULER's 2^{|levels|} − 1 path-set changes, times
  ≤ n length-only changes between them.
### Status (READING)
- The candidate potentials do not give a polynomial count: they are monotone with exponential range, and pftheta34 exercises the range
  (ruler pattern at a gate inside one phase).
- The circularity of §19 is the ρ / N_ep problem, plus WG. On pftheta34 the whole run is CLEAN ρ at one gate. Any polynomial bound on
  ρ_q per phase (the target of L-NEW / L-COMP's N_ep work) bounds B(S), and then U and the coarse W-changes through §16-§19 only if the
  circularity's factors close; a polynomial ρ alone is not enough without U-SPLIT (or an injective CHARGE-U).
