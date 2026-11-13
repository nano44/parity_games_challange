# R2-P-N5-WRAP: REFEREE-2 second review of packet P-N5-WRAP (L-SI successor 53)
REFEREE-2 successor 39 (Opus 5.5, D1 «Never downgrade the referee to save money»; L53). Written 2026-11-12 by date -u (times in the
commits). Independent: I did NOT open docs/referee/ on WRAP (REFEREE 33's R-WRAP-preread, any R-P-N5-WRAP) or notes/REFEREE.md before
this verdict is on origin; what I know of REFEREE 33's text is what the packet quotes. I did not read box 104, L-COMP 20's box 44 or
L-RED 66's R236 / R237, nor any lane tool (wrap104, n5v, n5bxi, qwrap). My replay is my own code (R2-P-N5-WRAP/r2wrap.py on REFEREE-2's
R2-P-N5-END/r2end.py primitives).
Boxes: 1 = object, premises, Claim NT (the special task) and NT-RUN; 2 = Lemma WRAP (i)-(v) on W; 3 = remarks, XI-EXP, DEAD row, DATA,
own replay, TARGET.md diff, verdicts.

## Box 1: object, premises, Claim NT

### 1.0 Object (from `git show`)
- claude/l-si e01447e77d57e2cdd26b7e537546c35c49b26fc8: docs/si/P-N5-WRAP.md sha1 1670432a8a07490ff80ceed45c861515ff070b9b, 56,745 B,
  462 lines; docs/si/P-N5-WRAP-line-L1.txt sha1 896f9e97394695f903131f832a67f31bcfc23c28, 2,648 B (= the Lead's brief). Pins:
  experiments/si/pwrap/out/P-N5-WRAP.sha1, checkW.sh (not run by me).
- [F11] opened by me: https://arxiv.org/pdf/1106.0778v2, 618,145 B, sha256 46c96f44775aa2b07cad20912cb325b177e38c94cb2e40297df66b6047679611
  (= the packet's pin). Read: §2 (p. 3, injectivity), §3 (p. 4-6: ϑ_(σ,τ,v), the order, τσ, Ξσ, ◁ on game valuations, improvement
  arena and policies, Theorem 3.2), §4 (p. 6, I^loc), §5 (p. 8, page 8 also rendered as an image: Sink Existence, Sink Seeking with
  «Ξ_ιG ⊴ Ξσ» NON-strict, the path-length remark, Lemma 5.1 and its proof), §6.4 (Table 4, Fact 6.1, ι_Gn, Figure 4), Lemma 6.7 and its
  proof (p. 17), Lemma 6.13 and Theorem 6.14 (p. 23).

### 1.1 Premises (own script R2-P-N5-WRAP/r2wq.py; out r2wq.out)
- Every «…» on §1's [SPEC], [N5XI], [1E-N3], [DUAL], [R15a/c/d], [RULE] bullets, searched whitespace-normalised in its trunk source at
  7fa6aff4 (docs/new/N5-ssi-global.md; docs/new/P-N5-XICYC.md; RESULTS R104, R15): 24 quotes, 24 found (the one «SPEC (EXACT …)» is the
  prefix of the SPEC heading, l. 24 of the file). Nested quotes in [DUAL] are tested piece by piece.
- NOT checked yet: the [Q] items quoted from REFEREE 33's R-WRAP-preread (§6, §7, §9, §10). They come from docs/referee/, which I do not
  open before my verdict; I check them in an addendum after it.
- The signed-weight comparison of P = the most relevant vertex of the symmetric difference (packet §1's last sentence): true, since
  2^rank dominates the sum of all lower powers. [F11]'s set order (p. 4: «max(M Δ N) ∈ ((N ∩ V⊕) ∪ (M ∩ V⊖))») is the same rule.

### 1.2 Claim NT (REFEREE 33's claim, L41): re-derived from the opened PDF. SIGN
Setting from [F11]: Ω injective (§2, p. 3, «W.l.o.g.»); a play π_(σ,τ,v) = v_1 … v_k (w_1 … w_l)^ω with v_1 = v, v_i ≠ w_1 and w_1 the most
relevant node of the cycle; ϑ = (w_1, {v_i > w_1}, k) (p. 4); τσ an optimal counterstrategy, minimising at every node (p. 5); 1-sink
game (p. 8): (1) Sink Existence: v* with v*Ev*, Ω(v*) = 1, reachable from all nodes, «also, there is no other node w with Ω(w) ≤ Ω(v*)»;
(2) Sink Seeking: for each σ with Ξ_ιG ⊴ Ξσ (non-strict, rendered page) and each node w the cycle component of Ξσ(w) is v*.
My proof (the same route as the packet's; written before comparing the wording):
1. Fix σ with Ξ_ι ⊴ Ξσ and τ := τσ; let u be a node, π its play. By Sink Seeking w_1 = x (:= v*). Every other node w has Ω(w) > Ω(x)
   (Sink Existence), so x is the most relevant node of its cycle only if the cycle is {x}: the cycle is x's self-loop (the play uses
   the edge xEx). So π = v_1 … v_k x x x …, the v_i pairwise distinct (positional play) and ≠ x.
2. Every v_i is more relevant than x, so the path component is {v_1, …, v_k} (all of them) and k = its cardinality ([F11] p. 8's remark,
   re-derived here).
3. Ξσ(x) = (x, ∅, 0); for u ≠ x, u = v_1 is in its own path component, so Ξσ(u) ≠ Ξσ(x).
4. u ≠ u′, both ≠ x, Ξσ(u) = Ξσ(u′): equal path components, so u′ ∈ {v_1, …, v_k} of u's play, u′ = v_j with j ≥ 2 (u′ ≠ u). The play from
   u′ under the same positional (σ, τ) is the suffix v_j … v_k x x …, which does not contain v_1 = u (the v_i are distinct). So u ∉ path
   component of Ξσ(u′) = Ξσ(u) ∋ u: contradiction. Hence Ξσ is injective on nodes.
5. Distinct successors of a player-0 node have distinct valuations; ⪯ is total (p. 4-5): exactly one ⪯σ-best successor. ∎
- Uses from [F11]: Sink Existence and Sink Seeking as defined (p. 8), the valuation (p. 4), the totality of ⪯ (p. 4-5), positional plays.
  It does not use the optimality of τσ beyond its being one fixed positional strategy, and nothing of §6. Correct. Under L41 I sign Claim
  NT independently; its author is REFEREE 33 (claude/referee e44ce56b, as the packet quotes it).
- Two checks of mine. (a) The hypothesis Ξ_ι ⊴ Ξσ is non-strict in [F11] (rendered p. 8), so σ = ι is covered (also by Lemma 6.7 (2)).
  (b) The packet's statement adds «Let G be a parity game with injective Ω»; [F11] §2 assumes it throughout, and Sink Existence alone gives
  what the proof uses (x below all other nodes).

### 1.3 Corollary NT-RUN: SIGN, CONDITIONAL on Lemma WRAP (as the packet labels it)
- (G^L_n, ι) is a 1-sink game. Re-derived from [F11] Lemma 6.7 + Lemma 5.1 with Figure 4's priorities:
  - Sink Existence: from Table 4's edges every node reaches x (each node has a path to s, r, k_i or x; s, r, k_i → x). Figure-4
    priorities (Table 4's d_i, e_i, g_i, k_i, f_i, h_i each minus 2, the other formulas unchanged) are INJECTIVE with x = 1 the unique
    minimum: odd classes t (4n+3 … 8n+1), d (4i − 1 ≤ 4n − 1), k (≡ 1 mod 4, 8n+9 … 12n+5), f (≡ 3 mod 4, 8n+11 … 12n+7) and even
    classes a (4n+4 … 8n+2), e (≡ 0 mod 4, ≤ 4n), g (≡ 2 mod 4, ≤ 4n+2), c, s, r (8n+4, +6, +8), h (≥ 8n+12) do not meet; maximum 12n + 8
    = Fact 6.1's «12 · n + 8 as highest priority». Table 4 as printed is NOT injective (g_n = a_1 = 4n + 4; maximum 12n + 10). My script
    checks this for n = 1, …, 8 (injfail 0 with Figure 4; 3 of 3 with --table4). So READING F-1 (the theorem's game is the Figure-4 game)
    is the only reading under which [F11]'s standing injectivity holds; Figure 4 (G_3) prints exactly these values. Agreed.
  - Won by player 1 (6.7 (1)): with τ(e_i) = h_i, every edge of Table 4 except x's loop goes «down» (t's to lower t / c / s / r; s → f →
    e → h → k → g of HIGHER index or x; r → g; g → f or k; d → s, e, r, a; a → t): the only cycle is x's loop. Priority-free.
  - Ξ_ι's cycle component is x everywhere (6.7 (2)): under ι (t_1 → c; t_(i>1), c, d_i → r; g_i → k_i; k_i, s, r → x) with Odd free, the only
    cycle is again x's loop (e_i → d_i → r → x or e_i → h_i → k_i → x). Priority-free; uses Ω(x) = 1 odd.
  - Lemma 5.1's proof (p. 8): won by player 1 makes the cycle component odd; Ξ_ι ⊴ Ξσ gives reward ≥ −1, so Ω(u) ≤ 1: u = x. Correct.
- The run: each Howard step is Switch_I for a non-empty unambiguous set (one improving edge per moving vertex): [R15a] (= [F11] Theorem
  3.2) gives Ξ_(s_t) ⊴ Ξ_(s_(t+1)); with reflexivity at ι, Ξ_ι ⊴ Ξ_(s_t) for all t: Claim NT applies at every state.
- SPEC's values / order on G^L_n = [F11]'s: Ω injective, so SPEC's rank by (Ω, index) is Ω's order and p′ keeps parities; c = the most
  relevant cycle node = w_1; P = the nodes before reaching c that are more relevant than c = {v_i > w_1} (the prefix before the FIRST
  visit of c; [F11]'s v_i ≠ w_1 is the same cut); ℓ = k; the length rule (odd node: longer better; even: shorter) is [F11]'s (p. 5); Odd's
  pointwise optimum = τσ's values. Checked against the texts.
- With a unique best successor b_t(v) at every state, a Howard step (switch-best, keep-if-best) sets s_(t+1)(v) = b_t(v) at every
  player-0 node, and I^loc's defining property «w ⪯σ I^loc_G(σ)(v) for every w ∈ vE» (p. 6) forces I(σ)(v) = b_t(v) for EVERY policy with
  the property. So all such policies, and WRAP's Howard run with any tie rule, produce the same run from ι, which stops at the first
  non-improvable strategy (Algorithm 1). T = the number of improvement steps of Theorem 6.14. Correct. The CONDITION: «the H-parts of the
  N5′-xi run are a Howard run of H» is WRAP (iii); NT-RUN adds nothing that WRAP does not carry.
- My DATA for NT (r2wrap.py gn, own transcription of Table 4 with Figure-4 priorities, own SPEC S1): Howard from ι on G_n, n = 1, …, 8:
  T_n = 8, 26, 62, 134, 278, 566, 1,142, 2,294 = 9·2^n − 10 (≥ 2^n), ntfail 0 (unit: states with two nodes of equal value), tiefail 0
  (unit: (state, player-0 node) with ≥ 2 best successors), sinkfail 0 (unit: states with a cycle component ≠ x), over all states of the
  eight runs. Control: on random games that are not 1-sink games ntfail FIRES (box 3), so the counter is live and the 1-sink hypothesis
  is load-bearing.

## Box 2: Lemma WRAP (i)-(v), re-derived on W

### 2.1 §2 Definitions, count, (R_W), Fact (H): SIGN
- W(H, s0) as in §2.1; my builder (r2wrap.py build_W) follows the text and asserts |W| = n + 7·m_E + 6·m_O + n_O + 9 and that every vertex
  has a successor, on every game run. On W(G_n, ι) it gives 211, 395, 600, 826, 1,073 at n = 1, …, 5 (= §7's list). Edge paths of 6 edges
  with 5 inner vertices of Ω ≤ 2: correct. Size and priorities (≤ max pr + 11, ≤ |W|) polynomial at bit cost: correct.
- (R_W): pads, gates, valves Ω ≤ 2 < K2 (3) < K1 (5) < V (Ω ≥ 6) < c_W (top) < K0 < K3; pr ↦ pr + 6 keeps H's order and parities. K0 is
  the most relevant EVEN vertex (K3 is odd), so node K0 has the top reward; c_W the top reward outside the core; −p′(K1) < −p′(K2). The
  ⊕ facts: correct.
- Fact (H): N5: P2 gives a pointwise optimum σ_new of the arena, and at a vertex v that is not its own arena cycle node, v's arena value is
  v ⊕ (value of its successor) (also when v lies on the arena cycle but is not its node), so σ_new(v) ∈ TIE(v) = {w0}. N5′-xi: by [N5XI]'s
  rule directly. Correct.

### 2.2 §4.1 PAD-W, §4.2 S3-W (= WRAP (i)): SIGN
- PAD-W: the core is closed (K0 → K1, pA; pA → K3; K1 → q, s; s → K1; q → K0; K2 → r, K2; r → K1; K3 → K1, K2); new non-core vertices
  advance strictly in the order m < g < pβ < x1 < x2 < x3 < b < y (pe, pe_o, pb leave to c_W or K0; y enters V): no cycle among them. The
  core's simple cycles contain K0, K1 or K3, or are K2's loop. So every cycle node has Ω ≥ 3, and no pad, gate or valve is a cycle node or
  in a P-set. Correct.
- S3-W, FIX 1 vertex by vertex: v ∈ V_E: the unique Ω-2 pad m_(v,s0(v)); valve: y (2, even) over pb (1); K0: pA (0, even) over K1 (5,
  odd); K1: s (0) over q (1); K3: both odd, the lowest, K2; gate (Odd, rule on G^d): pe (1, odd) over pβ (0); o ∈ V_O: pe_o (the only odd
  successor); K2: K2 (3, odd) over r (0). The standard state of s0. Correct. DATA: s3fail 0 on every run (box 3).

### 2.3 §4.3 K3-W with K2-r-W: SIGN
- K2-r-W: under κ0, K2's loop has node K2, r → K1 → s → K1 has node K1; both odd, K1 more relevant, so via r is smaller; P1. Correct.
- (a) the eight values: re-computed by hand, all as printed (K0's and q's P = {K0, K3}: K0 = top + 2 and K3 = top + 3 are the only core
  vertices above K1).
- (b) K0: K1 vs pA: same node, {K3} odd in pA's set: K1 strictly better, improving. K1: q vs s: top of {K0, K3} is K3, odd, in q's set:
  not. K3: K1 vs K2: same node and set, node odd, the longer (K2, ℓ 2) better: not. Correct.
- (c) Iτ(K2) = ∅: under τ0 the loop's value has reward −p′(K2); from r Even reaches the K0-cycle K1 → q → K0 → K1, so τ̄ (maximising, [DUAL])
  gives r reward ≥ p′(K0) > 0: worse for Odd. Correct.
- (d) arena: A(K0) = {pA, K1}, A(K1) = {s}, A(K3) = {K2}, K2 → K2 (τ0); via pA node K2, via K1 node K1, −p′(K2) > −p′(K1): pA. K0 on no
  arena cycle (q ∉ A(K1)); TIE(K0) = {pA}; (H). Correct.

### 2.4 §4.4 ODD-W: SIGN
- pe-free plays from V, gates, valves, m, pβ, x_i, y run along the 6-edge paths forever (σ: pads at V_E, y at valves; Odd: pβ, x1), never
  meet pe, pe_o, pb, c_W or the core: node in V, below c_W. (a) a gate or o ∈ V_O on pe would get node c_W, a strictly larger reward than a
  pe-free alternative: not a pointwise minimum (P1). (b) pe-free strategies on V_O ↔ positional Odd strategies ρ of H; plays stretched by
  6; the cycle's most relevant vertex is H's c (inner Ω ≤ 2); the P-set is H's; (c, P, ℓ) ↦ (c, P, 6ℓ) is strictly order-preserving and
  injective (rewards and P-comparisons use only V's relative order and parities, kept by pr + 6); σ̄ is pe-free and pointwise minimal over
  all Odd strategies, hence over pe-free ones, hence ρ̄ is pointwise optimal in H and Ξσ(v) = (c, P, 6ℓ). (c) m → g → pβ → b → y → w: five
  steps, no P-element: (c, P, 6ℓ + 5). (d) follows. Correct. DATA: odd5 0 (my counter compares (b), (c) with my own S1 on H at every
  standard state).

### 2.5 §4.5 TAU-W (= WRAP (ii)): SIGN
- Iτ depends on τ only (SPEC: Ξτ, τ̄, Iτ «computed there», on G^d). Under τ0 every gate and o ∈ V_O goes to c_W; their alternatives (pβ_g →
  b; x1 → x2 → x3 → b) let Even (τ̄ maximises, [DUAL]) reach b → pb → K0 → K1 → q → K0, node K0: reward ≥ p′(K0) > p′(c_W): worse for Odd.
  K2: K3-W (c). The Odd vertices are the gates, V_O and K2: Iτ = ∅ at τ0. S4b needs Iτ ≠ ∅; S4c moves τ only when Iσ = ∅ and along Iτ
  (FIX 3); both are the same in N5 and N5′-xi. Induction from S3. Correct. DATA: e0fail 0.

### 2.6 §4.6 ESC-W: SIGN
- At a standard state: (K0, K1) ∈ Iσ (K3-W (b)). Arena: every option m of v ∈ V_E plays m → g → pe → c_W (τ0): W*(m) = (c_W, ∅, 3) for every m,
  W*(v) = (c_W, ∅, 4), TIE(v) = A(v), v not its own node. Valve: via y → w the arena play reaches c_W (w ∈ V_E: any option, a pad, gate, pe;
  w ∈ V_O: pe_w); via pb the core's odd cycle; c_W even, so y strictly better; b on no arena cycle; TIE(b) = {y}. Core: K3-W (d). Pads and
  c_W: one successor. So σ_new = σ off V_E, in both. Correct.

### 2.7 §4.7 REACH-W (= WRAP (iii), first half of (v)): SIGN
- T exists: each Howard step is Switch_I for a non-empty unambiguous I (one improving edge per moving vertex); [R15c]: no strategy repeats.
- Induction: at a standard state of s_j, τ_new = τ, S4a applies, σ_new = σ off V_E; at v ∈ V_E with |A(v)| ≥ 2, TIE(v) = A(v) and N5′-xi
  takes the Ξσ-best element of A(v); A(v) = {current pad} ∪ {pads of strictly ⊴_H-better successors} contains the pads of all ⊴_H-best
  successors, and ODD-W (d) transports the order: v moves to a pad of a ⊴_H-best successor, the tie broken by «SPEC's choice, then the
  larger index»; A(v) = {σ(v)} exactly when s_j(v) is already ⊴_H-best (strict improvements only), and then v stays: keep-if-best. So the
  new state is the standard state of a Howard step. At j < T some v moves (no fallback); at j = T, A(v) = {σ(v)} at every v ∈ V_E, σ_new = σ,
  τ_new = τ: iteration T + 1 is an Even fallback (Iσ ∋ (K0, K1)). N5: P2 gives σ_new(v) ∈ TIE(v) = A(v), so moves stay inside {s(v)} ∪
  {strictly better}, and the first σ_new = σ is the first fallback F. Correct. DATA: nonstd 0, nohoward 0, fbwrong 0.

### 2.8 §4.8 E1-W to E4-W, ENDGAME-W (= WRAP (iv), second half of (v)): SIGN
- E1-W: K3-W uses the core only (closed) plus τ0 (TAU-W): every S4a keeps κ0; so κ changes only at a fallback and Iσ ≠ ∅ before it.
- E2-W: the first fallback is an Even fallback (Iσ ∋ (K0, K1)); S4c switches every Even vertex with an improving edge to its best, keeps τ
  (FIX 3); in the core only K0 → K1: κ1.
- E3-W: κ1: σ̄(K2) = r; values (re-computed): K0 (K1, {K0}, 1), q (K1, {K0}, 2), K3 (K1, {K3}, 3), pA (K1, {K3}, 4), the rest as in (a).
  Iσ in the core = {(K1, q)} ({K0} even in q's set). Arena A(K0) = {K1}, A(K1) = {s, q}: via q the cycle K1 → q → K0 → K1 with node K0;
  W*(K1) = (K0, ∅, 2) = K1 ⊕ W*(q), K1 ⊕ W*(s) = (K0, ∅, 4): TIE(K1) = {q}; κ2, not a fallback.
- E4-W (a): κ2: K2 → r would reach node K0, so σ̄(K2) = K2; core values as printed; Iσ ∋ (K3, K1) (node K0 over K2); valves: by P1,
  Ξσ(w) ⊴ the value under «pe, pe_o, K2-loop», node c_W, so Ξσ(y) has a node of reward ≤ p′(c_W) (y is on w's play or before it, and is
  never a node, PAD-W) < p′(K0) = Ξσ(pb)'s: (b, pb) ∈ Iσ. Arena: TIE(b) = {pb}; K3: via K1 node K0 over K2's loop, K3 on no arena cycle:
  σ_new(K3) = K1. κ3, every valve on pb, not a fallback.
- E4-W (b): at σ*: Odd plays pe, pe_o and K2's loop (each alternative reaches node K0); V_E: all pads (c_W, ∅, 3), equal: no improving edge;
  valves: pb (K0, ∅, 1) over y (node c_W): none; core: K0 (pA: (K0, {K3}, 4) with K3 odd: worse), K1 (q shorter, better), K3 (K1 node K0):
  none. Iσ* = Iτ = ∅: stop.
- ENDGAME-W: a first fallback exists (N5′-xi: T + 1; N5: R15 (d) termination, and no stop at κ0); then κ1, κ2, κ3 and stop: exactly one
  fallback and F + 2 iterations. WRAP (iv): F = T + 1, T + 3 iterations. Correct. DATA: endwrong 0, kconf 0 (my counter checks the exact
  K-config sequence κ0^F, κ1, κ2, κ3).

### 2.9 Lemma WRAP (i)-(v): SIGN
All five parts follow as the packet states: (i) S3-W; (ii) TAU-W; (iii) REACH-W; (iv) ENDGAME-W with REACH-W; (v) REACH-W's N5 half and
ENDGAME-W. Premises used: [SPEC] S1-S5 with FIX 1, FIX 3; [N5XI]; [1E-N3] P1, P2; [DUAL]; [R15c], [R15d] (and [R15a] in NT-RUN only).
WRAP uses no property of H (Remark 1): correct, my random games have any owners, equal priorities, self-loops and degrees 1-3.

## Box 3: remarks, XI-EXP, DEAD row, DATA, own replay, TARGET.md diff, line L-1, verdicts

### 3.1 §5 Remarks
- Remark 1 (READING): agreed; my random games use any owners, equal priorities, self-loops, out-degrees 1-3.
- Remark 2 (READING): not checked by me; it is not to sign.
- Remark 3 (PROVED under [RULE]): given [RULE]'s choice rule as the packet quotes it (SPEC's S4a pick is the key-least option of TIE(v);
  RESULTS R24 (b)), the argument holds: by ESC-W every option's arena play is m → g → pe → c_W at every standard state, so each option's
  root-first key is a fixed index sequence, each move of v goes to a strictly smaller key, at most deg(v) − 1 moves per v, F ≤ m_E −
  |V_E| + 1. I did not re-prove [RULE] itself (a premise here). DATA, mine: rem3 0 (unit: N5 runs with F > m_E − |V_E| + 1) on 600 random
  wrapped games (300 in §2.1's order, 300 permuted); F ≤ 4 there. N5 on W(G_n, ι), n = 1, …, 4: 3 iterations (F = 1) in MY numbering of
  G_n (names x, s, c, r, t, a, d, e, g, k, f, h; successor lists by index): as the packet and REFEREE 33 (quoted in §9) say, N5's count
  depends on the indices (the lane's frozen numbering gives 6); the bound does not.

### 3.2 §7 Statement XI-EXP: SIGN as a CONDITIONAL statement
- The implication is correct: WRAP (iv) gives T + 3 iterations on W(G^L_n, ι), NT-RUN makes T the I^loc step count of [F11] Theorem 6.14,
  and the theorem gives T ≥ 2^n. |W^L_n| = 10.5n² + 152.5n + 48 (n_H = 10n + 4, m_E = 1.5n² + 14.5n + 4, m_O = 6n + 1, n_O = 5n + 1, which I
  recounted from Table 4's successor lists; m_E + m_O = Fact 6.1's 1.5n² + 20.5n + 5). Since n ≥ √(|V|/211), 2^n = 2^Ω(√|V|):
  super-polynomial in |V|. «Exponential» only in n (F-3): agreed.
- It STAYS CONDITIONAL: (1) on WRAP and Claim NT being signed by both referees (I sign both here; the other signature is REFEREE's);
  (2) on READING F-1. I checked F-1 myself (1.3): Figure-4 priorities are the only reading under which [F11]'s standing injectivity and
  Fact 6.1's «12 · n + 8 as highest priority» hold; still a reading of a misprint, so it stays named; (3) on Theorem 6.14 as published
  (F-2: its phase lemmas are written for counter states whose two top bits stay zero; any 2^Ω(n) suffices for «not polynomial»).
- My DATA: T_n = 9·2^n − 10 for n ≤ 8 on G_n from my own transcription (≥ 2^n), and T + 3 = 11, 29, 65, 137, 281 iterations of N5′-xi on
  my W(G_n, ι), n ≤ 5, with one fallback each (my counters 0). DATA, not the proof.
- «It says nothing against N5 … and nothing about RESULTS R118-R125 or boxes 208 / 209»: correct; W^L_n is not a Γ3(G) or a genome game.

### 3.3 §8 DEAD row: SIGN as a draft, DEAD-CONDITIONAL, scope right
- Candidate: N5′-xi from S3. Claim killed: «N5′-xi makes polynomially many iterations on every parity game» (gauntlet step 4, M4
  candidacy). Scope: N5′-xi as an M4 candidate only; N5 (SPEC) is explicitly not killed (Remark 3, WRAP (v)); G-N5-TIME stays OPEN. Correct.
- L43: the killed statement is asymptotic; the row rests on a proof (WRAP + Claim NT + a published theorem), not on finitely many
  instances; it says «DEAD-CONDITIONAL» until two signatures. That is what L43 allows. The instances are named with sha1 prefixes (not
  re-hashed by me: box 104's inst/ is outside what I read).
- Obstruction W-FLAT stated exactly (τ inert by TAU-W; every option of v ∈ V_E tied in S4a's arena by ESC-W; so N5′-xi's pick is Howard's
  rule on H). Correct.

### 3.4 DATA (§9, §10; L43)
- §9's clauses name counter, unit, set and scope (WRAP's six counters with units; iteration counts by family; controls named). The rule is
  met in the packet. §10 is cited DATA of other lanes / REFEREE 33, not re-run, and says so.
- L-1's DATA clause does NOT name WRAP's counters and cites «18 counters 0 on 523,721 runs» without naming them: R-2 below.

### 3.5 Own replay (R2-P-N5-WRAP/r2wrap.py; sweep.out; counters and units in the tool's doc string)
| set | runs | fail counters (sum) | notes |
| --- | --- | --- | --- |
| random H (n ≤ 8, owners and priorities uniform, out-degree 1-3, ties and self-loops allowed), N5′-xi, seed 3901 | 3,000 | 0 | s3fail, nonstd, e0fail, nohoward, fbwrong, endwrong, kconf, odd5 |
| the same, N5 (S4a = S1 on the dual arena) | 3,000 | 0 | endwrong, kconf, nonstd, nohoward (moves inside {s(v)} ∪ strictly better) |
| random H, n ≤ 12, new vertices' indices permuted, N5′-xi / N5, seed 3902 | 1,000 + 1,000 | 0 | statements independent of the order |
| random H, N5, rem3 (Remark 3's bound), seeds 3905, 3906 (permuted) | 300 + 300 | 0 | F ≤ 4 |
| W(G_n, ι), n = 1, …, 5, N5′-xi | 5 | 0 | 211 / 395 / 600 / 826 / 1,073 vertices; 11 / 29 / 65 / 137 / 281 iterations, F = T + 1 |
| W(G_n, ι), n = 1, …, 4, N5 | 4 | 0 | 3 iterations, F = 1 (my numbering) |
| G_n, n = 1, …, 8, Howard = I^loc from ι, Figure-4 priorities | 8 runs, 4,518 states | 0 | ntfail, tiefail, sinkfail, injfail 0; T_n = 9·2^n − 10 |
| CONTROL --ctrl start (τ(K2) := r at S3) | 200 | FIRES 3,571 | nonstd 800, e0fail 600, endwrong 200, odd5 1,931, nohoward 40 |
| CONTROL --ctrl worst (H-check against the WORST successor) | 200 | FIRES 222 | nohoward 222 |
| CONTROL ntrand (Claim NT's distinctness on random NON-1-sink games) | 300 | FIRES 244 | ntfail 198, tiefail 46 |
| CONTROL G_n with Table 4's printed priorities | 3 | FIRES 3 | injfail 3 (g_n = a_1); T_n unchanged on n ≤ 3 |

### 3.6 TARGET.md diff (TARGET.md at 7fa6aff4)
- §1: W(H, s0) is a parity game in §1's sense (every vertex has a successor; priorities ≤ max pr + 11, polynomial, d ≤ n + 1 holds for
  the W^L_n since max priority 12n + 19 < |W^L_n|). §3: sizes polynomial at bit cost. §2 (M4): XI-EXP, if signed, is a family on which one
  candidate takes super-polynomially many iterations: a dead end for that candidate, not an algorithm and not a bound. Not M3, not M4, not a
  gauntlet step (it is the failure of step 4 for N5′-xi). G-N5-TIME (N5) stays OPEN. PASS.

### 3.7 Line L-1 (sha1 896f9e97, 2,648 B) against «To sign»
- Carries WRAP (i)-(v) in summary, Remark 3's bound under [RULE], Claim NT with its L41 origin, NT-RUN, XI-EXP CONDITIONAL with the
  reading and «as published», the obstruction, the frozen instances, the scope tail (N5 not affected, G-N5-TIME OPEN, not M3 / M4). It
  says less than «To sign» on §2 and §4's lemma statements (named, not stated): acceptable for a line.
- R-1 (REQUIRED). The NT clause speaks of «G_n», but Claim NT's identification of SPEC's values with [F11]'s needs injective priorities,
  and NT-RUN is stated for G^L_n (Figure 4's priorities); Table 4's G_n is not injective. Old (exactly once in L-1):
  «no tie occurs on Howard's run of G_n from ι and that run»
  New: «no tie occurs on Howard's run of G_n (Figure 4's injective priorities, the READING below) from ι and that run»
- R-2 (REQUIRED, DATA rule: every DATA clause names its counter). Old (exactly once):
  «REFEREE 33 e44ce56b / 90703a81: 18 counters 0 on 523,721 runs)»
  New: «REFEREE 33 e44ce56b / 90703a81: its 18 must-be-0 counters, named in its report, 0 on 523,721 runs); WRAP's six must-0 counters
  (s3fail, nonstd, nohoward, fbwrong, endwrong, wrong; units in the packet §9) 0 on 4,000 random games for N5′-xi, 3,000 for N5, the
  frozen 300 and W(G_n, ι), W(switchallexp_n) for n ≤ 8»
  (the counts are §9's; the lane should check them against its outputs when it applies the string).
- R-3 (optional). Old: «an Even valve with an exit to R117's core» New: «an Even valve with an exit to a closed core K0-K3 (the shape of
  R117's; no R117 fact is used)». §1 says no R117 lemma is used; the line's wording could be read as a premise.

### 3.8 Verdicts (Opus 5.5, D1). Statements as frozen in P-N5-WRAP at e01447e7.
| statement | verdict | conditions, gaps |
| --- | --- | --- |
| §2 W(H, s0), order, count, (R_W), standard state; §2.4 Fact (H) | SIGN | none |
| §4.1 PAD-W; §4.2 S3-W = WRAP (i) | SIGN | none |
| §4.3 K3-W (a)-(d), K2-r-W | SIGN | none |
| §4.4 ODD-W (a)-(d) | SIGN | none |
| §4.5 TAU-W = WRAP (ii) | SIGN | none |
| §4.6 ESC-W | SIGN | none |
| §4.7 REACH-W = WRAP (iii), first half of (v) | SIGN | none |
| §4.8 E1-W to E4-W, ENDGAME-W = WRAP (iv), second half of (v) | SIGN | none |
| Lemma WRAP (i)-(v) | SIGN | none |
| §5 Remark 3 | SIGN, CONDITIONAL on [RULE] (as labelled) | [RULE] not re-proved by me |
| §6 Claim NT | SIGN (independent check under L41; author REFEREE 33) | none |
| §6 Corollary NT-RUN | SIGN, CONDITIONAL on WRAP's second signature | none |
| §7 Statement XI-EXP | SIGN as a CONDITIONAL statement | stays CONDITIONAL on WRAP and Claim NT signed by both referees, READING F-1 and Theorem 6.14 as published (F-2) |
| §8 DEAD row (draft) | SIGN as DEAD-CONDITIONAL; scope N5′-xi as an M4 candidate only | DEAD only after both signatures (L43) |
| line L-1 (896f9e97) | SIGN WITH GAP | «L-1's NT clause names G_n without its priorities; L-1's DATA clause names no counter» (R-1, R-2 exact strings in 3.7) |
- No statement is REFUSED. No signed proof keeps an open gap. N5 (SPEC) is not affected; G-N5-TIME stays OPEN; not M3, not M4.

### Statement of independence
- These verdicts rest on my derivations (boxes 1-2) from the packet's text, SPEC's text and the opened PDF, and on my own replay. Before
  this verdict was on origin I did not open docs/referee/ (REFEREE 33's R-WRAP-preread, any REFEREE review of WRAP), notes/REFEREE.md, box
  104, L-COMP 20's box 44 or L-RED 66's R236 / R237, nor any lane tool. Claim NT's proof route is REFEREE 33's as the packet quotes it; I
  re-derived each step against the PDF (1.2).

## Addendum 1 (REFEREE-2 successor 39; 2026-11-12 22:34Z by date -u; written after my verdict 07fd5ae4 was on origin): REFEREE 33's quotes
- The packet's ten [Q] items from REFEREE 33 (§6 T-2, T-3, T-4 and «Status»; §7 F-1, F-2, F-3; §9 W-2; §10 two items) are verbatim,
  whitespace-normalised, in docs/referee/R-WRAP-preread.md at claude/referee 90703a81 (35,268 B): 10 of 10 found (nested «…» tested piece
  by piece). This closes the item left open in 1.1. Nothing in it changes a verdict. I read R-WRAP-preread only for this check, after my
  verdict; agreement with REFEREE's own review of the packet (when it exists) is a separate line.

## Addendum 2 (REFEREE-2 successor 39; 2026-11-13 01:28Z by date -u): byte test of fixes entry 1 + line L-2 (claude/l-si faf0c8ff)
Objects (from git show at faf0c8ff): docs/si/P-N5-WRAP-line-L2.txt sha1 dbd5f0e83e3d0300842c46cf2ae24b30b853d784, 3,598 B, one line;
docs/si/P-N5-WRAP-fixes.md entry 1; the packet (1670432a…) and L-1 (896f9e97…) unchanged. REFEREE 34's report read now (claude/referee
99df2458, docs/referee/R-P-N5-WRAP.md), after my verdict 07fd5ae4.
### Bytes (own script R2-P-N5-WRAP/bt_wl2.py, out bt_wl2.out; not the lane's mkL2.py)
- LW-1 (REFEREE 34 §5, «old» → «new» exact) on L-1: sha1 be7da8f3a98e4c5a26158eae9aa2766c56531222, 3,190 B = REFEREE 34's L-1′.
- R-1 (mine, Old / New exact): the Old occurs once after LW-1; applied.
- R-2 (mine): its Old does NOT occur after LW-1 (LW-1 rewrote that clause; my R-2 and LW-1 were written independently on L-1). Re-anchored
  as fixes entry 1 step 3 says: LW-1's «18 counters 0 on 523,721 runs);» → my R-2 New's REFEREE 33 part + «); » + my R-2 New's WRAP
  sentence + «;». My script does the same from my report's text.
- LW-2 (files named by REFEREE 34: wrap_fried_xi.out, wrap_long.out, free_xi.out, all present in experiments/si/box104/out at faf0c8ff) and
  LW-3 («to the core K0-K3 (with pads pA, s, q, r)», REFEREE 34's string; my optional R-3 not used, as ruled): applied.
- Result: sha1 dbd5f0e8…, 3,598 B, 44 «(» = 44 «)»; cmp with the lane's L-2: EQUAL. Each old string occurs exactly once at its step.
  L-2 = L-1 + exactly LW-1, R-1, R-2 (re-anchored), LW-2, LW-3.
### Meaning
- R-1: the NT clause now reads «Howard's run of G_n (Figure 4's injective priorities, the READING below) from ι». Met.
- R-2: the DATA now names WRAP's six counters twice: in LW-1's clause, for the W^L_n rows; and in my R-2 sentence, for the random, frozen
  and switchallexp sets. REFEREE 33's 18 counters are «named in its report». The DATA rule is met.
- LW-1: the T_n numbers 8 … 2,294 = 9·2^n − 10 for n ≤ 8 equal my own replay (r2wrap.py gn); 4,598 and 9,206 for n = 9, 10 are
  9·2^n − 10 too (cited from REFEREE 33, not re-run by me). True. LW-2, LW-3: true (§2.1's core and pads; the files exist).
- Note W-L2-1 (no change required for MATCH; the Lead's call). The re-anchored R-2 sentence now stands inside the list «independent
  replays, every fail counter 0, …, cited, not re-run: L-COMP 20 (…), REFEREE 33 (…); WRAP's six must-0 counters (…) 0 on 4,000 random
  games …; L-RED 66 …». The 4,000 / 3,000 / 300 runs are the lane's own (box 104 out/), not an independent replay. A reader may take them
  for a cited replay. One exact string would remove the ambiguity, if wanted for a later line. Old (once in L-2): «; WRAP's six must-0
  counters (». New: «; and this lane's own runs (box 104, not a replay): WRAP's six must-0 counters (».
- No statement, label, condition or scope changes. XI-EXP stays CONDITIONAL; the DEAD row stays DEAD-CONDITIONAL until both signatures.
### Verdict: L-2 (faf0c8ff, sha1 dbd5f0e8) MATCHES. R-1 and R-2 are met; my SIGN WITH GAP on L-1 is closed. Note W-L2-1 is optional.

## Agreement line (REFEREE-2 successor 40; 2026-11-13T02:52Z by date -u): REFEREE 34's L-2 byte test, claude/referee 32d61d60 (R-P-N5-WRAP.md §8, pwrap_logs/l2test.out), read after my verdict 01e83df5
**Agrees.** Same objects (faf0c8ff, L-2 sha1 dbd5f0e8…, 3,598 B), same stages (L-1 + LW-1 = be7da8f3…; R-1 once; R-2's Old 0× after LW-1,
re-anchored on «18 counters 0 on 523,721 runs);» once, as fixes entry 1 step 3 says; LW-2, LW-3 once each), same result (44 «(» = 44 «)»,
cmp EQUAL), same verdict L-2 MATCHES; its note N-W2 is my note W-L2-1 (the R-2 sentence sits after the cited-replays list). No difference.
