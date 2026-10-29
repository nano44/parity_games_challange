# P-N5-REL (box 25): a clean σ̄ change strictly raises Ξ at the gate itself (GATE-RISE); settling needs σ̄ and the cycles constant only on the end state's relevant plays (STATIC-DEPTH-REL), so a fallback-free run has ≤ SEG·n − 1 transitions with SEG a cut count that readers cannot inflate (REL-SPLIT)
L-SI successor 21 (Opus 5.5; D18, Lead reading L40). Packet for the referees, FROZEN at its push; the sha1 goes to the Lead; repairs go in a NEW
file docs/si/P-N5-REL-fixes-box25.md. Lead 2026-10-29 04:10Z: «freeze a second packet: docs/si/P-N5-REL-box25.md. To sign: Lemma GATE-RISE,
Theorem STATIC-DEPTH-REL and Corollary REL-SPLIT.» Working note with data: docs/si/N5-GRUN-box25.md. Labels (D18 / L40): PROVED (lane,
unrefereed) / CONJECTURE / OPEN / DATA.
SCOPE (D1): structural lemmas and a REDUCTION for N5 inside one phase. Not a TARGET.md claim, not an algorithm claim, no running-time bound
(SEG is not bounded here); G-N5-TIME stays OPEN.
SELF-CONTAINED: §2 proves STATIC-DEPTH-REL in full. It generalises Theorem STATIC-DEPTH′ of the packet P-N5-SDPRIME-box25 (in review, sha1
54678c38…), but does NOT use it; the referees may read the two together. The premises are LANDED RESULTS entries and the SPEC text, quoted
below; every [Q path@commit:lines] «…» is verbatim, checked by experiments/si/rund/quotecheck.py (pinned in experiments/si/check.sh with a
shifted-line control that must fail).

## 0. What to sign, and what not
| § | statement | label |
| --- | --- | --- |
| §1 | Lemma GATE-RISE and its Count | PROVED (to sign) |
| §2 | Theorem STATIC-DEPTH-REL (N5, every game; REL-admissible [a, b], (H4′_rel), GEN_W) | PROVED (to sign) |
| §3 | Corollary REL-SPLIT | PROVED (to sign) |
| §4 | data (readers, anchors, GATE-RISE / REL checks, climbs), CONJECTURE SEG-RUN, the reader-proofness READING | DATA / CONJECTURE / READING (NOT to sign) |

## Premises (all LANDED)
- SPEC docs/new/N5-ssi-global.md. [Q docs/new/N5-ssi-global.md@b28123a58:28-29] «valuation of v under (σ, σ̄): (c, P, ℓ), c = the most relevant
  (max p') vertex of the cycle the play from v ends in, P = set of vertices on the play before reaching c with p' > p'(c), ℓ = number of steps
  to reach c.» A valuation is a function of the play. [Q docs/new/N5-ssi-global.md@b28123a58:30-31] «order (better for Even): compare reward of c
  (p'(c) if even, −p'(c) if odd); then P by the signed weight Σ_{u∈P} (+2^rank(u) if Ω(u) even else −2^rank(u)); then ℓ» — p′ is injective
  and distinct sets have distinct signed weights, so the order is TOTAL. [Q docs/new/N5-ssi-global.md@b28123a58:32] «Ξσ = valuation of every
  vertex under σ and Odd's OPTIMAL counterstrategy σ̄». [Q docs/new/N5-ssi-global.md@b28123a58:47] «Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v),
  Ξσ(w) strictly better than Ξσ(σ(v))}». S4a: [Q docs/new/N5-ssi-global.md@b28123a58:51] «A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v» and
  [Q docs/new/N5-ssi-global.md@b28123a58:53] «(Even's one-player optimum against τ among "keep or take an improving edge".)». S4c:
  [Q docs/new/N5-ssi-global.md@b28123a58:56] «FALLBACK, if σ_new = σ and τ_new = τ».
- RESULTS R15 (a), (d): [Q docs/RESULTS.md@b28123a58:631] «(a) Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴
  Ω_{Switch_I(σ)}.» and [Q docs/RESULTS.md@b28123a58:640] «(d) N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G)». So
  Ξ_{t+1} ⊵ Ξ_t pointwise at every in-phase S4a transition (Ω = Ξ; τ is fixed in a phase).
- RESULTS R17 (a): [Q docs/RESULTS.md@b28123a58:738] «(V1)/(V2) (prefix equation and prefix monotonicity of values)»: for v off its play's
  cycle, val(v) = v ⊕ val(next v), and x ↦ v ⊕ x is monotone.
- RESULTS R57 (a): [Q docs/RESULTS.md@b28123a58:2907] «(a) Premise (VJ), on every game: for every positional σ and every positional Odd strategy
  τ′, Ξσ(v) ⊴ V_{σ,τ′}(v) at every v».
- Pointwise optimality of S4a's step over strategies using arena edges: RESULTS R18 (d) Lemma S (a), [Q docs/RESULTS.md@b28123a58:804] «U_τ the
  pointwise maximum of V_{σ',τ} over Even's σ'», applied to the arena game (P2 as listed in RESULTS R69: [Q docs/RESULTS.md@b28123a58:3596] «P2:
  S4a's step is Even's optimum in its arena»).
- (SW): [Q docs/RESULTS.md@b28123a58:3768-3769] «(SW): every Even switch of N5 is to an edge … of Iσ».
- RESULTS R77 (c)'s signed proof steps: [Q docs/RESULTS.md@b28123a58:4204-4205] «(W-MONO) W_{t+1} ⊵ W_t (P2), (Ξ-SUCC) Ξ_t(σ_t v) non-decreasing
  ((M2κ), (SW))», on in-phase S4a transitions. GEN_W: [Q docs/RESULTS.md@b28123a58:4202] «GEN_W (for every v, different W-plays from v to the
  same cycle have different W-valuations)».
- RESULTS R80 (a): [Q docs/RESULTS.md@b28123a58:4433] «(a) (C1) EVERY-SWITCH (§2): at every transition t → t+1 of a phase, σ_{t+1} ≠ σ_t.»
- Notation. A RUN S: a maximal stretch of states of one phase with no fallback between them. Ξ_t(v): the valuation of v's honest play (σ_t,
  σ̄_t); W_t(v): that of v's (σ_t, τ)-play. W-cycle / honest cycle at t: a cycle of the successor map v ↦ σ_t(v) / τ(v), resp. σ_t(v) / σ̄_t(v)
  (vertex sequences up to rotation); a vertex on a cycle of a successor map has that cycle as its play.

## 1. Lemma GATE-RISE (PROVED, lane)
Statement. Let t → t + 1 be an in-phase S4a transition and u an Odd vertex with σ̄_t(u) = y1 ≠ y2 = σ̄_{t+1}(u), such that (i) u is on no honest
cycle at t and at t + 1, (ii) y2's honest t-play does not pass through u, (iii) Ξ_t(y1) ≠ Ξ_t(y2). Then Ξ_{t+1}(u) ▷ Ξ_t(u).
Proof.
1. By (i) and (V1): Ξ_t(u) = u ⊕ Ξ_t(y1) and Ξ_{t+1}(u) = u ⊕ Ξ_{t+1}(y2).
2. Let τ′ := σ̄_t with u's choice changed to y2. By (ii), y2's (σ_t, σ̄_t)-play does not meet u, so it is also y2's (σ_t, τ′)-play, and u's
   (σ_t, τ′)-play is u followed by it; it does not return to u, so V_{σ_t,τ′}(u) = u ⊕ Ξ_t(y2). (VJ) gives u ⊕ Ξ_t(y1) = Ξ_t(u) ⊴ u ⊕ Ξ_t(y2).
3. x ↦ u ⊕ x is strictly monotone: monotone by (V2); injective, since by S1 u ⊕ x keeps x's cycle node, adds u to x's path set exactly when
   p′(u) > p′(c) (the same for all x with cycle node c) and adds 1 to the length, so x is recovered from u ⊕ x. With the order total, step 2
   and (iii) give Ξ_t(y1) ◁ Ξ_t(y2).
4. R15 (a), (d): Ξ_{t+1}(y2) ⊵ Ξ_t(y2). So Ξ_{t+1}(u) = u ⊕ Ξ_{t+1}(y2) ⊵ u ⊕ Ξ_t(y2) ▷ u ⊕ Ξ_t(y1) = Ξ_t(u). □
Count. For a run S, an Odd u and the four kinds of σ̄(u)-changes in S (clean: (i)-(iii) hold; TIE: (iii) fails; CYC: (i) fails; THRU: (i) holds,
(ii) fails): CH_S(u) ≤ XR_S(u) + TIE_S(u) + CYC_S(u) + THRU_S(u), XR_S(u) the transitions of S that change Ξ(u). Summing over the Odd
vertices of out-degree ≥ 2: G(S) ≤ Σ_u (XR_S(u) + TIE_S(u) + CYC_S(u) + THRU_S(u)), G(S) the σ̄-changing transitions of S. (Each clean change
is a transition at which Ξ(u) changes.) □

## 2. Theorem STATIC-DEPTH-REL (PROVED, lane)
Definitions at a state b of a run S. Q := the Even vertices of out-degree ≥ 2. X_b := the least set of Even vertices containing Q and every
Even vertex on the W-play at b or on the honest play at b of one of its members. RO_b := the Odd vertices on the honest b-play of a member of
X_b. CW_b (CH_b) := the W-cycles (honest cycles) at b on which the W-plays (honest plays) at b of the members of X_b end; T_W, T_H := their
vertices; T := T_W ∪ T_H. V^W_b (V^H_b) := the vertices on the W-play (honest play) at b of a member of X_b. Every Even vertex of V^W_b ∪
V^H_b is in X_b, and V^W_b (V^H_b) is closed under the W-successor (honest successor) at b.
- [a, b] ⊆ S is REL-ADMISSIBLE if σ̄_t(u) = σ̄_b(u) for every u ∈ RO_b and t ∈ [a, b], and every cycle of CW_b (CH_b) is a W-cycle (honest
  cycle) at every t ∈ [a, b].
- Depths: dW on V^W_b, dH on V^H_b: dW(v) := 0 for v ∈ T_W; dH(v) := 0 for v ∈ T_H; Odd v: dW(v) := dW(τ v) (v ∉ T_W), dH(v) :=
  dH(σ̄_b v) (v ∉ T_H); Even v ∈ T_H ∖ T_W: dW(v) := dW(σ_b v); Even v ∈ T_W ∖ T_H: dH(v) := dH(σ_b v); Even v ∉ T: dW(v) := dH(v) := d(v)
  := 1 + max(dW(y), dH(y)), y := σ_b(v). The recursion stays in its domains: τ(v) (Odd v) and σ_b(v) (Even v) of v ∈ V^W_b are on the same
  W-play, so in V^W_b; σ̄_b(v), σ_b(v) of v ∈ V^H_b likewise in V^H_b; for Even v ∉ T, v ∈ X_b and y lies on both of v's b-plays, so y ∈
  V^W_b ∩ V^H_b. (H4′_rel): the recursion is well founded.
Statement. Let [a, b] ⊆ S be REL-admissible, with (H4′_rel) and GEN_W. Then every v ∈ V^W_b has its W-play at b at every t ∈ [a + dW(v), b],
and every v ∈ V^H_b its honest play at b at every t ∈ [a + dH(v), b]; σ_t = σ_b for t ∈ [a + max_{v ∈ Q ∖ T} d(v),
b]; and b − a ≤ max_{v ∈ Q ∖ T} d(v) ≤ |Even ∖ T| ≤ n − 1 (max ∅ := 0).
Proof. "v W-settled from s": v's W-play at every t ∈ [s, b] is its W-play at b; "H-settled": the same with honest plays. Induction along
the well-founded recursion.
1. v ∈ T_W lies on a cycle of CW_b, which is a W-cycle at every t: W-settled from a. Likewise v ∈ T_H (CH_b): H-settled from a. An Even v ∈ T
   has σ_t(v) = its successor on that cycle = σ_b(v) for all t.
2. Odd v ∈ V^W_b ∖ T_W: v's W-successor is τ(v) at every t; if τ(v) is W-settled from s, then for t ∈ [s, b] τ(v)'s W-play
   is its W-play at b, which avoids v (v ∉ T_W, and v's W-play at b is v followed by τ(v)'s, simple up to a cycle not through v); so v's
   W-play at t is its W-play at b: W-settled from a + dW(τ v). Odd v ∈ V^H_b ∖ T_H: v lies on the honest b-play of a member of X_b, so
   v ∈ RO_b and σ̄_t(v) = σ̄_b(v) on [a, b] (REL-admissible); the same argument
   with σ̄_b(v) and honest plays gives H-settled from a + dH(σ̄_b v).
3. Even v ∈ V^W_b ∩ T_H ∖ T_W (V^H_b ∩ T_W ∖ T_H): σ_t(v) = σ_b(v) =: y for all t (item 1), and item 2's argument with y gives W-settled from
   a + dW(y) (H-settled from a + dH(y)).
4. Even v ∈ (V^W_b ∪ V^H_b) ∖ T (so v ∈ X_b), y := σ_b(v), s := a + max(dW(y), dH(y)), y
   W-settled from a + dW(y) and H-settled from a + dH(y).
   (A) For t ∈ [s, b], y ∈ {σ_t v} ∪ Iσ_t(v). Otherwise σ_t(v) ≠ y and Ξ_t(y) ⊴ Ξ_t(σ_t v) (order total); v switches to y at some t′ → t′ + 1,
       t ≤ t′ < b, and (SW), Ξ-SUCC and H-settledness give Ξ_{t′}(y) ▷ Ξ_{t′}(σ_{t′} v) ⊵ Ξ_t(σ_t v) ⊵ Ξ_t(y) = Ξ_{t′}(y). Contradiction.
       (If v has out-degree 1, (A) is trivial: σ_t(v) = y.)
   (B) For t ∈ [s, b − 1], s′ := σ_{t+1} with v's choice set to y uses arena edges of state t ((A), S4a). y's W-play under σ_{t+1} is its W-play
       at b and avoids v (v ∉ T_W), so it is y's play under s′: W_{s′}(v) = v ⊕ W_b(y) = W_b(v). Pointwise optimality: W_{t+1}(v) ⊵ W_b(v);
       W-MONO: W_{t+1}(v) ⊴ W_b(v). So W_{t+1}(v) = W_b(v).
   (C) The cycle node c of W_b(v) lies on v's W-cycle at b, a cycle of CW_b (v ∈ X_b), which is c's W-play at t + 1; v's W-play at t + 1 has
       cycle node c, so it ends in that cycle; GEN_W makes it v's W-play at b. Hence σ_{t+1}(v) = y, and v's honest play at t + 1 is v followed
       by y's honest play at t + 1 = y's honest play at b, which avoids v (v ∉ T_H): v's honest play at b. v is W- and H-settled from a + d(v).
5. Length. For t ≥ a + max_{Q ∖ T} d: every v ∈ Q ∖ T has σ_t(v) = σ_b(v) (item 4), every Even v ∈ Q ∩ T has it (item 1), and every Even
   vertex outside Q has out-degree 1. So σ_t = σ_b, and a transition of S after a + max_{Q ∖ T} d would contradict R80 (a) EVERY-SWITCH. A
   longest recursion path from v ∈ Q ∖ T visits distinct Even vertices outside T ((H4′_rel)), and d(v) counts them, so max d ≤ |Even ∖ T| ≤
   n − 1 (T ≠ ∅ when Q ≠ ∅; if Q = ∅ there is no in-phase S4a step and b = a). □
Remark. If σ̄ is constant on all Odd vertices on [a, b] and every W-cycle (honest cycle) at b persists, [a, b] is REL-admissible; so
STATIC-DEPTH-REL contains STATIC-DEPTH′ (P-N5-SDPRIME) and, through it, RESULTS R77 (c). Not used below.

## 3. Corollary REL-SPLIT (PROVED, lane; a REDUCTION)
Cut a run S = [s, e] from its end: b_k := e; a_k := the least state of [s, b_k] with [a_k, b_k] REL-admissible (with respect to b_k's sets); then
b_{k−1} := a_k − 1, and so on down to s. SEG(S) := k, the number of segments.
Claim. If (H4′_rel) and GEN_W hold at every b_i, then |S| = e − s = Σ_i (b_i − a_i) + SEG − 1 ≤ SEG·n − 1. Every cut a_i − 1 → a_i (i ≥ 2) is
a transition at which σ̄ changes at a vertex of RO_{b_i} or a cycle of CW_{b_i} ∪ CH_{b_i} appears; hence SEG − 1 ≤ G(S) + CF(S), CF(S) the
transitions of S at which a W- or honest cycle appears.
Proof. STATIC-DEPTH-REL on each segment gives b_i − a_i ≤ n − 1. For i ≥ 2, [a_i − 1, b_i] is not REL-admissible though [a_i, b_i] is (the
sets are those of b_i): either σ̄_{a_i − 1}(u) ≠ σ̄_{b_i}(u) = σ̄_{a_i}(u) for some u ∈ RO_{b_i}, or a cycle of CW_{b_i} ∪ CH_{b_i}, a cycle at a_i, is
not one at a_i − 1. The cuts are distinct transitions. □

## 4. NOT to sign (details and logs in docs/si/N5-GRUN-box25.md; experiments/si/grun/)
- DATA, GATE-RISE (grun/gaterise.py): 2,114 clean changes on alt_all (3,752 with pinned starts; 1,889 lib41), 0 failures; MUT (a strict rise of
  Ξ(y2) demanded instead) fails 1,892 times. REL (grun/relseg.py): 1,908 segments on alt_all, 0 violations, (H4′_rel) fails at 45 ends; MUT
  (d − 1) 994. SEG ≤ 0.79n in the library, ≤ 1.00n after climbs. One engine (n5x).
- DATA / READING, reader-proofness: Odd readers (no predecessors) lift G on runfam_K10 from 9 to 91 at n 74 with the run unchanged, and Even
  anchors put them into RESULTS R81's K (G^K 91 at n 99); SEG stays 9 (a reader is on no play of another vertex, an anchor's plays are its own
  loop). Pins grun/out/rdr_K10, anc_K10.
- CONJECTURE SEG-RUN: SEG(S) = O(n). With REL-SPLIT (where (H4′_rel), GEN_W hold) it would give |S| = O(n²) per run. OPEN.
