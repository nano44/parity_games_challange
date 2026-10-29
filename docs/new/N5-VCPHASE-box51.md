# N5-VCPHASE (box 51): CONJECTURE VC-PHASE is FALSE. A one-player family has phase VC d at n < 2^(2d+1) (Proposition DLC)
L-NEW successor 32 (Opus 5.5; D14, D18, Lead reading L40). Lead's brief 2026-10-29 12:43Z, BOX 51: «a proof attempt on CONJECTURE VC-PHASE:
the phase VC dimension dσ(P) = O(1) on every phase ... Pick one [tool]. Name the exact forbidden pattern you aim to prove. Test it on the pins
(vpf3_vc4, ent1_vc6, runquad, hntop_n8, b6_xl2_n32) BEFORE writing a proof, and kill it yourself if the data says so.»
This is a working note. It is unrefereed and not frozen, and it is not a TARGET.md claim. G-N5-TIME stays OPEN.
Labels: PROVED (lane) / CONJECTURE / OPEN / DATA / ASSUMPTION / READING / DEAD. Counts are TRANSITIONS (iterations).
Tools: experiments/new/box51/ (vcgad.py generator, dlccheck.py checker, dump.py / look.py / alt.py probes). Logs: box51/*.txt, box51/out/.
Definitions as in docs/new/P-N5-VC-box50.md §0 (σ^E, F_σ(P), shattering, VC, Φ_d, m). A run is a maximal fallback-free stretch of a phase.

## 0. Summary
- The tool chosen was the sign-pattern / Davenport-Schinzel view. Pattern 1 was DS-PAIR(s): the toggles of any two Even edges at different
  vertices alternate at most s + 1 times in a run. Lemma DS-VC (PROVED, §1) shows that DS-PAIR(s) gives run VC ≤ log2(2 + s·d(d−1)/2) on a
  shattered d-set, i.e. VC = O(log s). Data killed DS-PAIR(s) for every constant s before any proof was attempted (§2): 30 alternations on
  runquad_K8 and 311 on hntop_n8, growing along both scaling families.
- The data on the pins does not decide whether VC-PHASE is false. So I tried to build the obstruction directly. Proposition DLC (PROVED, §3)
  gives a ONE-PLAYER family DLC_d. All its vertices are Even, it has no Odd vertex and |D| = 0. N5 on DLC_d makes one phase of
  2^(d+1) − 1 transitions with no fallback, and that phase shatters d Even edges. n < 2^(2d+1), so
  **dσ(P) ≥ d > (log2 n − 1)/2: CONJECTURE VC-PHASE is FALSE, and so are VC-N5 and VC-RUN in their O(1) forms.**
- DATA (§4): dlccheck.py checks the trace formula state by state and gives PASS at d = 1, …, 5 (n = 7, 27, 109, 455, 1897). The phase VC
  is exactly d at d ≤ 5. L-COMP's n5b gives identical state sequences at d = 2, …, 5.
- Consequence (READING, §5): N5 is polynomial on one-player games (RESULTS R17), yet there the phase VC grows like Θ(log n). So Theorem
  VC-BOUND (P-N5-VC) with any true VC bound gives at best m^{Θ(log n)}, which is quasi-polynomial. The Sauer-Shelah route cannot prove a
  polynomial bound for N5, on phases or overall. The obstruction is that VC counts INDEPENDENT oscillators, while the price of an
  oscillation (here about 4^d delay-line vertices that switch once each) is invisible to it.

## 1. Lemma DS-VC (PROVED, lane; elementary)
Setting: a stretch S = (σ_a, …, σ_b) of consecutive states. Fix a total order on Even edges. For an edge e, a TOGGLE of e is a transition
k → k + 1 of S at which [e ∈ σ_k^E] ≠ [e ∈ σ_{k+1}^E]. The TOGGLE SEQUENCE of a set A of edges is the list of the toggles of the members of A,
ordered by time, with toggles at the same transition ordered by the edge order. alt(e, f) is the number of maximal runs of equal letters in
the toggle sequence of {e, f}.
Lemma DS-VC. Let A be a set of d Even edges at d distinct vertices, shattered by F(S) := {σ_k^E : a ≤ k ≤ b}. Suppose alt(e, f) ≤ s + 1 for
all e ≠ f in A. Then 2^d ≤ 2 + s·d(d − 1)/2. In particular VC(F(S)) = O(log s), and a run satisfying DS-PAIR(s) has
|F| ≤ Φ_{O(log s)}(m) by Corollary SAUER (P-N5-VC §1).
Proof. (i) Two edges at the same vertex are never both in σ^E, so a shattered set has one edge per vertex. (ii) Write the toggle sequence of
A as letters w_1 … w_L and collapse every maximal run of equal letters to one letter. The result u_1 … u_M has no two equal neighbours. Walk
through the columns: start at the column σ_a^E ∩ A and apply the toggles one at a time, simultaneous toggles in the fixed order. Every
column σ_k^E ∩ A is visited. A run of equal letters i visits at most one new column (x ⊕ {e_i}, after x), so the walk visits at most 1 + M
distinct columns. Shattering needs 2^d of them, so 2^d ≤ 1 + M. (iii) For each adjacent pair (u_j, u_{j+1}) = (e, f), e ≠ f, the
restriction of u to {e, f} contains these two letters adjacently, and that is a run boundary of the {e, f}-sequence. Distinct j give distinct
boundaries, and collapsing does not change the runs of a pair. So the number of adjacent positions labelled {e, f} is at most
alt(e, f) − 1 ≤ s, and M − 1 ≤ s·C(d, 2). □
(This is the elementary half of Davenport-Schinzel theory. The sharp bound λ_s(d) is not needed.)

## 2. DATA: DS-PAIR is DEAD on the pins (killed before any proof)
experiments/new/box51/alt.py (the sequence of Lemma DS-VC; runs taken from cached n5x states, box51/dump.py). Log: box51/alt_pins.txt.
| pin | max alt(e, f) in one run | pair (edges at distinct vertices) | run |
| --- | --- | --- | --- |
| vpf3_vc4 | 12 | (7, 20), (40, 20) | [5, 27] |
| ent1_vc6 | 20 | (24, 20), (31, 20) | [1, 18] |
| b6_xl2_n32 | 5 | (1, 10), (12, 5) | [19, 41] |
| runquad_K3_m4_n54 / runquad_K8_m30_n192 (L-RED) | 10 / 30 | (42, 43), (45, 46) / (102, 103), (105, 106) | [0, 20] / [0, 263] |
| hntop_n8 (L-RED R109 topfix) | **311** | (159, 160), (160, 161) | [0, 241] |
- DEAD: DS-PAIR(s) for every constant s. Obstruction: RELAY chains. On hntop_n8, 159 → 160 → 161 copy one oscillation down a chain, so two
  edges at neighbouring vertices alternate with every period. The count grows along runquad (10 → 30, K 3 → 8) and on hntop (311), while
  the phase VC stays 3 to 4. So pairwise alternation is the wrong pattern. Locked oscillators alternate without limit and still add no VC.
- Also measured on the pins (box51/look_pins.txt): W (the (σ, τ)-play valuation) never decreases and strictly rises at EVERY non-fallback
  in-phase transition (0 plateaus), and falls only at fallbacks (vpf3_vc4 at 4, b6_xl2_n32 at its 10 fallbacks). So inside a run, σ_t is a
  chain that strictly increases pointwise in W, and σ_{t+1} is the W-top of the box A_t. That is the structure a cross-vertex proof would
  have had to use. §3 shows that it does not bound the VC.

## 3. Proposition DLC (PROVED, lane): phase VC d at n < 2^(2d+1), on a one-player game
### 3.1 The family (experiments/new/box51/vcgad.py d)
Every vertex is Even (owner 0). There is no Odd vertex, so τ is empty and N5's Odd step never fires. T := 2^d.
- s: Ω 2, its only edge the self-loop s → s.
- Gadget i, for 0 ≤ i < d: vertices x_i, hA_i, hB_i (Ω 0), with x_i → {hA_i, hB_i}, hA_i → {s} ∪ heads, hB_i → {s} ∪ heads.
- Event k, for 1 ≤ k ≤ K_i := 2^(d−i) − 1, owns a reward r_k := r^(i,k) with r_k → s and Ω(r_k) even, ≥ 4 and strictly increasing in k, and
  a private DELAY LINE l_0, …, l_{p−1} with p = p_k := k·2^(i+1). Its edges are l_j → {l_{j+1}, s} for j < p − 1 and l_{p−1} → {r_k, s}. All
  line vertices have Ω 0. Line k hangs below hA_i if k is odd (edge hA_i → l_0) and below hB_i if k is even.
- n = 1 + Σ_i (3 + K_i + Σ_k p_k) = 1 + 2^d(2^(d+1) − 2 − d) + 2d + 2^(d+1) − 2 = 2^(2d+1) − d·2^d + 2d − 1 < 2^(2d+1) (d ≥ 1).
  The checker recomputes n from the file.

### 3.2 Valuations on DLC_d
Every edge leads away from s except the self-loop (the vertex order of the generator is a topological order with s first). So s is the only
cycle and every play ends in s. By SPEC S1, ranks sort by (Ω, v), so the vertices ranked above s are exactly the rewards, the only vertices
with Ω > 2. A play passes at most one reward, since r → s. So every valuation is (s, P, ℓ) with P = ∅ or P = {r}. The order of S1
(c = s fixed, even) is: {r} beats {r′} iff Ω(r) > Ω(r′); every {r} beats ∅; with equal P, the shorter length is better. Write vals as
(P, ℓ). Since there is no Odd vertex, Ξσ is the valuation of the play of σ itself (S1: «Ξσ = valuation of every vertex under σ and Odd's
OPTIMAL counterstrategy», and Odd has no choice). So Ξ_t = W_t, and S2's improving edges are Iσ_t = {(v, w) : w ≠ σ_t(v),
Ξ_t(w) ▷ Ξ_t(σ_t(v))}.
PREMISE (VJ00 correctness, as used by RESULTS R15 and R17 (a) (F1)): S4a's σ_{t+1} is an OPTIMAL strategy of the one-player arena H_t, in which
Even's v may use only A_t(v) = {σ_t(v)} ∪ Iσ_t(v). Its valuation Opt_t dominates every strategy of H_t pointwise. H_t is acyclic apart from s,
so Opt_t(v) = ext(v, max_{w ∈ A_t(v)} Opt_t(w)) (backward induction; ext(v, ·) adds a reward v to P and 1 to ℓ, and preserves the order
strictly). Whenever the maximum is attained at ONE w, σ_{t+1}(v) = w, and in that case Opt_t(v) = W_{t+1}(v). Every choice below is of this
kind, so no tie-break of S1 (iv)-(v) is used.
Start (S3, best reward: the largest even Ω, ties to the largest index): l_j → s for j < p − 1 (Ω(s) = 2 > 0), l_{p−1} → r_k (Ω ≥ 4),
hA_i, hB_i → s, and x_i → hB_i (both have Ω 0, and the tie goes to the larger index, hB_i = x_i + 2).

### 3.3 The run, step by step (induction on t)
(L) Line k (length p). For every state t: σ_t(l_j) = l_{j+1} (r_k for j = p − 1) iff j ≥ p − 1 − t, else s. So W_t(l_0) = ({r_k}, p + 1) if
t ≥ p − 1 and (∅, 1) otherwise, and A_t(l_j) = {σ_t(l_j)} ∪ {l_{j+1} if j = p − 2 − t}.
Proof. t = 0 is S3. Step t → t + 1. l_{p−1}: (l_{p−1}, s) is not improving, since (∅, 0) does not beat ({r_k}, 1). A linked l_j (j ≥ p − 1 − t)
has W_t(l_{j+1}) with reward r_k, so (l_j, s) is not improving and l_j stays. An unlinked l_j (σ_t = s, W_t(s) = (∅, 0)): if j = p − 2 − t,
then l_{j+1} is linked, W_t(l_{j+1}) = ({r_k}, ·) beats (∅, 0), so the edge is improving, Opt_t(l_{j+1}) has reward r_k > ∅ = P of
Opt_t(s), and l_j switches (a unique maximum). If j < p − 2 − t, then W_t(l_{j+1}) = (∅, 1) loses to (∅, 0), so A_t(l_j) = {s} and l_j stays.
The line's edges stay inside line ∪ {r_k, s}, so nothing outside the line enters. □
(H) Head hX ∈ {hA_i, hB_i} with its event set K_X (odd or even k). Let k_X(t) := max{k ∈ K_X : p_k ≤ t} (none if empty). Then σ_t(hX) =
the head of line k_X(t), or s if there is none, and W_t(hX) = ({r_{k_X(t)}}, p + 2), or (∅, 1).
Proof. t = 0 is S3 (p_k ≥ 2). Step t → t + 1. By (L), a head l_0^k is linked at state t iff t ≥ p_k − 1. An unlinked head has W_t = (∅, 1),
which loses to W_t(s) = (∅, 0) and to every reward, so it is never improving. A linked head with k ≤ k_X(t) carries a reward no better
than the current one, so it is not improving either. Neither is s, while hX holds a reward. The linked heads with p_k − 1 ≤ t and k > k_X(t)
are improving. They are fully linked, so Opt_t(l_0^k) = W_t(l_0^k), with distinct rewards. hX takes the one with the largest k, i.e. the
head of k_X(t + 1). □
(X) x := x_i. Let K(t) := max{k ≤ K_i : p_k ≤ t} (0 if none) = min(K_i, ⌊t/2^(i+1)⌋), and side(k) := A for odd k, B for even k (B for k = 0).
Claim: σ_t(x) = h_{side(K(t−1))} for every t ≥ 1, and σ_0(x) = hB.
By (H), at state t the side holding K(t) (if K(t) ≥ 1) has the strictly larger W_t, because k_A(t) and k_B(t) are the largest odd and
even events ≤ K(t) and rewards increase with k. The arena value of a side is Opt_t(hX) = W_{t+1}(hX), with reward k_X(t + 1).
Proof by induction. t = 1: K(0) = 0, both sides have W_0 = (∅, 1), so there is no improving edge at x and x stays on hB = h_side(0). Step,
assuming σ_t(x) = h_side(K(t−1)) =: X. (a) If K(t) = K(t − 1), then side(K(t)) = X, so (x, Y) is not improving and x stays on side(K(t)).
(b) If K(t) = K(t − 1) + 1 (an event at t = p_{K(t)}; K rises by at most 1 per unit time because events are 2^(i+1) ≥ 2 apart), then
Y := side(K(t)) ≠ X and (x, Y) is improving. The next event comes at t + 2^(i+1) ≥ t + 2, so K(t + 1) = K(t). The arena values then have
rewards r_{K(t)} on Y and less on X. x switches to Y = side(K(t)) (a unique maximum). □
The spacing 2 is necessary. With p_k = k·2^i the arena optimum sees one hop ahead, x follows the side about to improve, and the d = 4
version had phase VC 3 (first version of vcgad.py, not kept).
(END) The last event is at p = 2^(d+1) − 2 (i = 0, k = K_0), so x_0 switches at the transition into state 2^(d+1) − 1. After that every line
is linked, every head holds its largest event and every x_i holds its leading side, so Iσ = ∅ and S5 stops: I = 2^(d+1) − 1.
(PHASE) τ is empty, hence constant. Every vertex's cycle node is s at every state, so λ_Ξ is constant. So the whole execution is one phase
P = [0, 2^(d+1) − 1]. Every transition changes σ: each improving edge belongs to a line vertex, a head or an x of case (b), and each of these
switches. So S4c never fires (no fallback) and the phase is one run. D_t = ∅ (no Odd vertex).
(SHATTER) For 1 ≤ t ≤ 2^(d+1) − 1, K(t − 1) = ⌊(t − 1)/2^(i+1)⌋ (no saturation: t − 1 ≤ 2^(d+1) − 2 < (K_i + 1)·2^(i+1)). So
(x_i, hA_i) ∈ σ_t^E iff bit i of u := ⌊(t − 1)/2⌋ is 1. As t runs over 1 … 2^(d+1) − 1, u runs over 0 … 2^d − 1, so all 2^d patterns appear on
A := {(x_i, hA_i) : 0 ≤ i < d}. A is shattered by F_σ(P) and dσ(P) ≥ d.
Proposition DLC (PROVED, lane; premise: S4a computes an optimal strategy of the arena, VJ00). For every d ≥ 1, N5 on DLC_d (from SPEC S3)
runs ONE phase of 2^(d+1) − 1 transitions, with no fallback, |D| = 0 and no Odd vertex. Its σ-family shatters the d edges (x_i, hA_i), so
dσ(P) = dσ ≥ d > (log2 n − 1)/2, with n = 2^(2d+1) − d·2^d + 2d − 1. By P-N5-VC (c) also dσ ≤ log2(I + 1) = d + 1, so
d ≤ dσ(P) ≤ d + 1. □

## 4. DATA (experiments/new/box51/dlccheck.py; engine n5x via L-SI's common.rows; second engine L-COMP's n5b via L-SI's root/n5bcmp.py)
dlccheck.py d regenerates DLC_d and checks n against the formula. It checks one phase of 2^(d+1) − 1 transitions, no fallback, no Odd vertex,
D_t = ∅, the exact trace σ_t(x_i) = hA_i ⟺ t ≥ 1 and bit i + 1 of t − 1 is 1 at EVERY state, and the 2^d traces on A. It also prints the
phase VC computed by box50's vcrun.vc.
| d | n | m (varying edges) | transitions | traces on A | phase VC (vcrun.vc) | dlccheck | n5b vs n5x states |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7 | 6 | 3 | 2 | 1 | PASS | |
| 2 | 27 | 35 | 7 | 4 | 2 | PASS | identical |
| 3 | 109 | 176 | 15 | 8 | 3 | PASS | identical |
| 4 | 455 | 821 | 31 | 16 | 4 | PASS | identical |
| 5 | 1897 | 3610 | 63 | 32 | **5** | PASS (box51/dlc_d5_check.txt; about 3 min, so not in check.sh) | identical (63 iterations, 0 fallbacks) |
- d = 5 is the first phase measured with VC 5, above every library value (≤ 4) and every climb (P-N5-VC §3-§4, N5-VC §6). Pins:
  box51/out/dlc_d{1..5}.pg with .start files (S3 start, box50/mkstart.py), sha1 2514e10c…, 36d7e325…, eba06fa3…, f77955fd…, 345fae4c….

## 5. What this does to the VC route (READING; labels kept)
- DEAD: CONJECTURE VC-PHASE (dσ(P) = O(1)). Killed by DLC_d (§3, PROVED; §4 DATA). The kill is in the class where N5 is already polynomial
  (one-player, RESULTS R17), so it says nothing against N5, only against the parameter. DEAD with it: CONJECTURE VC-N5 (dσ, dτ = O(1);
  P-N5-VC §4) and the O(1) form of VC-RUN (DLC's phase is one run).
- Theorem VC-BOUND (P-N5-VC §2) stands; it is a reduction. With dσ = Θ(log n) on DLC it gives I ≤ Φ_{d+1}(m) = m^{Θ(log n)}, against the true
  I = 2^(d+1) − 1 < 2√(2n). The best this route can give is CONJECTURE VC-LOG: dσ(P) = O(log n) per phase ⇒ len(P) ≤ m^{O(log n)},
  quasi-polynomial. VC-LOG is NECESSARY for polynomial N5 (P-N5-VC (c): dσ ≤ log2(I + 1)) but not sufficient for it. So the Sauer-Shelah
  route cannot reach TARGET's polynomial bound. I stop it here.
- Obstruction (READING): VC is blind to cost. On DLC each toggle of x_i is paid for by a fresh delay line, about 2^(i+1)·k vertices that
  each switch exactly once. That makes n ≈ 4^d while the VC is d. On hntop and runquad the reverse holds: many toggles, locked together,
  little VC. A parameter that could give a polynomial bound has to charge each RETURN of an edge to switches elsewhere that happen once
  (fresh edges, line links). It cannot count patterns. That is the SW-RETURN / FRESH-RED direction (RESULTS R80 FRESH-RED:
  |I| ≤ m_E + NOFRESH(I)), which is not new to the fleet.
- Lemma DS-VC (§1) stays true but is now moot. DS-PAIR(s) is dead on data (§2), and on DLC itself x_0 and x_1 alternate about 2^d times.

## 6. Dead ends (also in notes/L-NEW.md)
- DS-PAIR(s) (pairwise toggle alternation ≤ s + 1 per run), for every constant s: DEAD on hntop_n8 (alt 311 on (159, 160), (160, 161),
  run [0, 241]) and runquad_K3 → K8 (10 → 30). Obstruction: relay chains copy an oscillation, so locked pairs alternate without bound.
- CONJECTURE VC-PHASE / VC-N5 / VC-RUN (O(1)): DEAD by DLC_d, box51/out/dlc_d4.pg (n 455, sha1 f77955fd…, phase VC 4) and dlc_d5.pg (n 1897,
  sha1 345fae4c…, 32 traces on 5 edges). The family is proved for every d (Proposition DLC). Obstruction: independent delay-line
  oscillators. The arena optimum moves news one hop per iteration along an unlinked line, and private lines give each x_i any schedule
  with events ≥ 2 apart.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box51/ (vcgad.py, dlccheck.py, dump.py, look.py, alt.py; logs alt_pins.txt, look_pins.txt; pins
  out/dlc_d1..5.{pg,start}, d = 5 logs); experiments/new/check.sh block "Box 51".
- FINDINGS: (1) PROVED (lane) Proposition DLC: one-player games with phase VC d at n < 2^(2d+1), one fallback-free phase of 2^(d+1) − 1
  transitions, |D| = 0. CONJECTURE VC-PHASE, VC-N5 and VC-RUN (O(1)) are FALSE. (2) READING: the Sauer-Shelah route gives at best
  quasi-polynomial bounds, so it cannot prove N5 polynomial. P-N5-VC's §4 conjecture needs a fixes-file line saying it is FALSE.
  (3) PROVED Lemma DS-VC (pairwise alternation ≤ s + 1 ⇒ VC = O(log s)); DS-PAIR is DEAD on data (hntop 311).
- NEEDS: none from the owner.
