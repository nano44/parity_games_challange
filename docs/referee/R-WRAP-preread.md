# R-WRAP-preread: PRE-READ (NOT A SIGNATURE) of L-SI 52's Lemma WRAP (box 104 §3) and of the «tie item» (X-TIE) of its Statement XI-EXP (§6, Addendum A)
REFEREE successor 33 (D1 «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the
fleet's own, as wrong until it passes the gauntlet below.»; the box itself: «The same care applies to a kill»). Date -u at writing:
2026-11-12T18:23Z. Lead 17:53Z item A.
This is a read to find errors early. It is not a referee signature: nothing is frozen as a packet, WRAP is labelled «PROVED, lane» and
XI-EXP «CONDITIONAL» by the lane, and a packet review, if one comes, is a separate signature.
Objects (measured with git, not copied):
- Freeze: claude/l-si 26704e01f90135417ed6feb9dad283a580c75f9f (ancestor of origin/claude/l-si, checked), docs/si/box104-map.md, sha1
  eb6ac0457a8f0f066a10e9dd38bcbdce703bdd64, 61,768 B, 526 lines.
- Addendum A: claude/l-si 01900837bf7bdc2cd6e541ae7853ddb3c6522dab (ancestor, checked), the same file, sha1
  20cbb1c800a48570901a7fcf073eeb405ac96a69, 72,472 B, 622 lines; `git diff 26704e01 01900837b` on it removes 0 lines (append-only).
- Instances: experiments/si/box104/inst at 26704e01 by `git archive`; `sha1sum -c SHA1SUMS`: 19 of 19 OK.
- The paper, opened by me: arxiv.org/pdf/1106.0778v2, 618,145 B, 42 pages, sha256
  46c96f44775aa2b07cad20912cb325b177e38c94cb2e40297df66b6047679611 (the box's «46c96f44775aa2b0…»). Pages 5-8, 15-17 and 23 read as
  rendered pages; §2-§6.6 also as `pdftotext -layout`. [F11] below.
- Read for the re-derivation, all at claude/l-new 8db300fe: SPEC docs/new/N5-ssi-global.md (sha1 66fde9ef1726…; identical on trunk),
  docs/new/N5XI-GAUNTLET-box190.md §1 (d068343864d6…; S4a′), and the three template packets P-N5-REACH §3-§6.4 (b7bd693744fd…),
  P-N5-CHAIN §2-§3 (6e613ba762b6…), P-N5-END §1-§6 (5cae845b1da1…), each identical on trunk.
Not read before this verdict: docs/referee-2/, L-RED's and L-RED-B's records, L-LIT's T66 / T67 / T70 notes, the lane's tool code
(wrap104.py and the others of experiments/si/box104/; my counters are written from the box's statements). Of the lane's outputs I read
six rows of out/wrap_lmcs_spec.out, after my own runs, for §5 note W-2. Not read as a verdict: §1-§2 (Chain A), §4 (FREE-REACH), §5's
F_n and PGSolver rows beyond what §5 below lists, §7-§9, Addendum A.2-A.3.

## 0. Verdict
| item | verdict |
| --- | --- |
| Definition of W(H, s0); the size n + 7·m_E + 6·m_O + n_O + 9; «every edge of H is a path of exactly 6 edges with inner Ω ≤ 2» | **no gap found**; count re-derived (§1); note W-2 (index order of the new vertices) |
| (W1) [PAD], (W2) [S3-START], (W3) [core] | **no gap found** (§2) |
| (W4) (a)-(d), the new step | **no gap found** (§2.4); wording note W-1 |
| (W5) [TAU], (W6) [ESC, W-flat], (W7) [REACH], (W8) [ENDGAME] | **no gap found** (§2.5-§2.8) |
| WRAP (i)-(v) | follow from (W1)-(W8); **no gap found**; premise note W-3 (R15 is used and not named) |
| Remarks 1, 2, 3 | (1), (2) correct; (3) correct given R104's premise [RULE], which the Lemma does not name (W-3); counted (§5) |
| The «tie item» (X-TIE): is VJ switch-best with the lane's tie rule an instance of [F11]'s I^loc as Theorem 6.14 uses it | **YES, and the item can be CLOSED in its second form («no tie occurs on the run»), for every n ≥ 1**, by a three-line argument from the paper's own Lemma 5.1 and Lemma 6.7 (§3.2, Claim NT). The argument is mine, so it is not signed by this report (L41): L-SI writes it into the text, the other referee checks it independently. |
| (X-F11): [F11] Theorem 6.14 as cited | the quotation is **exact** (p. 23); two notes on what «as published» carries: F-1 (Table 4's misprint; the theorem's game is Figure 4's on a READING), F-2 (the paper's lemmas are proved for a restricted set of counter states) (§3.3) |
| Statement XI-EXP | follows from WRAP (iv), Theorem 6.14 and Claim NT **once WRAP and Claim NT are refereed**; arithmetic of the size re-derived; wording note F-3 («exponential» is in n; in the number of vertices it is 2^Ω(√\|W\|)) |
No FALSE statement found; no instance against any step. Own replay (§5): 18 must-be-0 counters (the box's six and twelve of mine),
all 0 on every set; every counter has a firing control; my engine reproduces the lane's N5′-xi iteration counts on Friedmann's
game from my own transcription of the PDF and on the lane's frozen instances.
What this read does NOT establish: that N5′-xi is super-polynomial as a refereed statement. It says that I re-derived every step of
WRAP on my own, found no hole, and that the tie item has a short proof. WRAP has had one day of scrutiny and one referee's read; D1
stands for a kill as for a bound. G-N5-TIME stays OPEN and is untouched: it is about N5, and WRAP (v) with Remark 3 says N5 is fast
on these wrappers.

## 1. The wrapper and its size
- Count from the Definition: per edge leaving an Even vertex m, g, pe, pβ and b, y, pb (7); per edge leaving an Odd vertex x1, x2, x3 and
  b, y, pb (6); per Odd vertex pe_o (1); c_W, K0, K1, K2, K3, pA, s, q, r (9); the n vertices of H. Total n + 7·m_E + 6·m_O + n_O + 9. ✓
- Paths: Even a: a → m → g → pβ → b → y → w; Odd o: o → x1 → x2 → x3 → b → y → w: 6 edges each, inner Ω ∈ {0, 1, 2}. ✓
- Rank order (R_W): Ω(v) = pr(v) + 6 keeps order, parity and index ties of H's vertices; top ≥ max Ω(V) + 2 is even; K0 = top + 2 even,
  K3 = top + 3 odd. ✓ So K0 is the most relevant EVEN vertex of W, and c_W the most relevant even vertex outside the core.
- W is a parity game in TARGET.md §1's sense (every vertex has a successor; for pr ≤ n the largest priority top + 3 ≤ n + 12 is below
  |W| ≥ 7n + 9, so the compression to {0..|W|} changes nothing but names).
- For Friedmann's G_n (n_H = 10n + 4; Even vertices t_i, c, d_i, g_i, k_i, s, r: 5n + 3; Odd a_i, e_i, f_i, h_i, x: n_O = 5n + 1; m_O =
  2n + 2n + n + n + 1 = 6n + 1; m_E = 1.5n² + 14.5n + 4): |W^L_n| = 10.5n² + 152.5n + 48 = 211, 395, 600, 826, 1,073, 1,341, 1,630, 1,940 at
  n = 1, …, 8: the box's numbers (§5.1, Addendum A.1). ✓
- Counted by my replay (counter size: |W| and every 6-edge path, on every game built): 0.

## 2. Lemma WRAP, step by step (each step re-derived on W; the landed proofs are about Γ3(G) and are used here only as templates)
Standing premise, as the Lemma says: 1E-N3 (R57 (b)), in both forms: S1's σ̄ and τ̄ are pointwise optima (P1); S4a's σ_new is a
pointwise optimum of its arena (P2). N5′-xi: SPEC with box 190 §1's S4a′ (TIE(v) := {w ∈ A(v) : W*(v) = v ⊕ W*(w)} at every Even v
with |A(v)| ≥ 2 that is not its own W*-cycle node; the Ξσ-best element; ties by SPEC's σ_new(v), then the larger index).
### 2.1 (W1): no gap found
- The new vertices outside the core form a forest of paths m → g → {pe, pβ}, pe → c_W, pβ → b, x1 → x2 → x3 → b, b → {y, pb}, y → w ∈ V,
  pb → K0, pe_o → c_W: none leads back to a new vertex without passing c_W, K0 or a vertex of H. The core has no edge out. So a cycle is
  c_W's loop, a core cycle (K2's loop, or it contains K0, K1 or K3), or contains a vertex of H: its node has Ω ≥ 3, and every pad, gate
  and valve (Ω ≤ 2) ranks below it. ✓
### 2.2 (W2), WRAP (i): no gap found
- FIX 1 at each vertex with two or more successors, re-read: v ∈ V_E (pads of Ω 2 / 0, all even: the unique Ω-2 pad); valve (y Ω 2
  even, pb Ω 1 odd: y); K0 (K1 odd, pA even: pA); K1 (q odd, s even: s); K3 (K1, K2 both odd: the lower, K2); gate (highest odd: pe);
  o ∈ V_O (x1's Ω 0 even, pe_o Ω 1 odd: pe_o); K2 (r even, K2 odd: K2). ✓ No index of a new vertex decides any of these.
### 2.3 (W3): no gap found
- The core with its four pads is a closed subgame with R117's vertices, edges, owners and relative order (K2 < K1 < K0 < K3, pads
  lowest). K3 (a)-(c) and «σ̄(K2) = r in κ0» are statements about that subgame alone (I re-computed the eight values and the three
  comparisons). K3 (d) and E1 (b) also use «K0 lies on no arena cycle»: in W the only edges into K0 are from q (whose only in-edge is
  from K1, which keeps {s} in the arena) and from the pb's, and K0 never leaves the core. ✓
### 2.4 (W4): no gap found
- (a) An Odd vertex u outside the core is a gate or a vertex of V_O. If σ̄(u) is its pe, Ξσ(u) has node c_W. A pe-free Odd strategy
  exists and sends u's play along 6-edge paths for ever (valves play y in a standard state): node in V by (W1), of smaller reward than
  c_W (c_W is even and above V). That contradicts P1 at u. ✓ (For every pointwise optimum, not only S1's.)
- (b) pe-free strategies ↔ positional Odd strategies ρ of H; the (σ, ρ)-play from v ∈ V is H's (s, ρ)-play with every edge stretched
  to 6; by (W1) the node and the P-set are H's, the length is 6ℓ. (c, P, ℓ) ↦ (c, P, 6ℓ) is strictly order-preserving (rewards compare
  as in H because ranks of V keep H's order and parity; P by the top of the symmetric difference; ℓ ↦ 6ℓ monotone). σ̄ is pe-free (a)
  and minimises at every vertex, so its ρ minimises at every vertex of H; Ω^H_s is that pointwise minimum (1E-N3 on H, a valid input
  of S1). ✓
- (c), (d): m → g → pβ → b → y → w (five steps, (a) at EVERY gate, also those of unchosen edges), no new P-element; S2 compares the
  pads of v, and (c, P, ℓ) ↦ (c, P, 6ℓ + 5) is strictly order-preserving and injective. ✓
- The step that carries the weight is the UNIFORM stretch: my control 7 (Odd edges stretched to 5, Even edges to 6) makes the run
  leave Howard's (§5: nohoward, fbwrong fire). The proof uses it exactly where it says (lengths multiplied by 6).
- Note W-1 (wording, required for a packet). The sentence «Under σ a pe-free play from a vertex outside the core runs along the 6-edge
  paths from vertex of H to vertex of H forever» is false as written for the starting vertices pe_(v,w), pe_o, pb_(a,w) and c_W (their
  plays go to c_W or into the core whatever Odd does). The proof applies it to gates, vertices of H and pads m only, where it holds.
  Say «from a vertex of H, a gate, a valve, or a pad m, pβ, x_i, y».
### 2.5 (W5), WRAP (ii): no gap found
- Ξτ(pe) = (c_W, ∅, 1) whatever Even does. From pβ_g and from every x1 of o, Even reaches a valve without passing an Odd vertex and
  may take pb → K0 → K1 → q → K0: node K0, the largest reward of all. τ̄ maximises (Fact DUAL), so the alternatives of every gate and
  of every o ∈ V_O have a strictly larger value than pe: not Odd-improving. K2: K3 (c). Iτ is a function of τ; S4b and S4c change τ
  only along Iτ. ✓ My control 6 (W without pe_o) makes w5 fire: the pads pe_o are what makes τ0 flat at V_O.
### 2.6 (W6): no gap found
- Every arena play from a pad m ∈ A(v) is m → g → pe → c_W, so W*(m) = (c_W, ∅, 3), W*(v) = (c_W, ∅, 4), v's W*-node is c_W ≠ v,
  TIE(v) = A(v). Valve: via y the arena play ends in c_W's loop (w ∈ V_E: pad, gate, pe; w ∈ V_O: pe_w), via pb in an odd core cycle
  (K3 (d)); b's arena plays never return to b; so every pointwise optimum keeps y and TIE(b) = {y} when pb ∈ A(b). (pb ∈ A(b) does
  occur: when Ξσ(w) has an odd node of H, pb is Ξσ-improving. On 300 random games, wrap_logs/valve_pb.out: 3,606 of 5,724 (standard
  state, valve) pairs have pb ∈ A(b), and SPEC's σ_new(b) = y in all 3,606; my counter w6 covers it on every set.) K1, K3 have one option in the arena by K3 (b). ✓
### 2.7 (W7), WRAP (iii) and the first half of (v): no gap found
- The induction carries exactly «state j is standard»; each cited fact ((W4)-(W6), K3) is proved for every standard state, so no step
  leaves the range its lemma was proved on (the G-P6 pattern does not occur). At v ∈ V_E with |A(v)| ≥ 2 S4a′ applies (node c_W ≠ v),
  TIE(v) = A(v) ∋ every strictly better pad, so the Ξσ-best element of A(v) is a Ξσ-best pad of v, i.e. by (W4) (d) the pad of a
  ⊴_H-best successor; if σ(v) is best, A(v) = {σ(v)}. So the H-part makes a Howard step of H. At state T: σ_new = σ, τ_new = τ,
  (K0, K1) ∈ Iσ: S4c fires at iteration T + 1. ✓
- T is finite because a Howard run of H repeats no strategy (R15 (c)); the Lemma should name it (W-3).
### 2.8 (W8), WRAP (iv) and the second half of (v): no gap found
- E1, E2, E3 on W: core only, as §2.3; in E3 TIE(K1) = {q} because K1 ⊕ W*(s) = (K0, ∅, 4) ≠ (K0, ∅, 2).
- E4 (a) on W: at κ2, Ξσ(pb) = (K0, ∅, 1); Ξσ(y) = y ⊕ Ξσ(w) and Ξσ(w) is at most the value of w's pe-play (w ∈ V_E: pad, gate,
  pe; w ∈ V_O: pe_w), node c_W, of smaller reward than K0: (b, pb) ∈ Iσ wherever σ(b) = y, and (b, y) ∉ Iσ where σ(b) = pb. Arena:
  via pb node K0, via y node c_W, b on no arena cycle: σ_new(b) = pb by (H); σ_new(K3) = K1. ✓
- E4 (b) on W: every Odd vertex outside the core has pe (value (c_W, ∅, 2)) against a path to a valve that now exits to K0's cycle;
  so σ̄* = pe everywhere, every pad m has (c_W, ∅, 3), no v ∈ V_E and no valve has an improving edge; the core at κ3 has none
  (re-computed: pA (K0, {K3}, 4) against K1 (K0, ∅, 2); s (K0, ∅, 3) against q (K0, ∅, 1); K2 (K2, ∅, 0) against K1 (K0, ∅, 2)). ✓
- For N5 the first fallback exists because N5 terminates on every game (R15 (d)) and cannot stop at κ0 (E1); name R15 (W-3).
### 2.9 Remarks
- (2) «Even wins every vertex but K2»: counted (rem2 0). (3): the key of m_(v,w) is the index sequence (pe, g, m) by R104's premise
  [RULE], static, so F ≤ m_E − |V_E| + 1 for N5: correct given [RULE]; counted on my SPEC engine (rem3 0). [RULE] is a premise the
  Lemma's header does not name; it enters Remark 3 only.

## 3. The tie item, from the opened PDF
### 3.1 What [F11] defines
- p. 3 (§2): «W.l.o.g. we assume Ω to be injective». p. 4-5 (§3): the node valuation ϑ_(σ,τ,v) = (w_1, {v_i > w_1 | 1 ≤ i ≤ k}, k) for the
  play v_1 … v_k (w_1 … w_l)^ω with v_1 = v, and its order: reward of the cycle node; then the path set by the most relevant element
  of the symmetric difference; then «e < f and u ∈ V_⊖» or «e > f and u ∈ V_⊕». This is SPEC S1's value and order (the start vertex
  counts in the path set in both; lengths as in S1).
- p. 5-6: an improvement policy is a MAP I_G : S_0(G) → S_0(G) with (1) (v, I_G(σ)(v)) an edge of the improvement arena (σ(v) ⪯_σ u)
  and (2) a strict improvement somewhere if σ is improvable. p. 6 (§4): «The locally optimizing policy I^loc_G selects a most
  profitable strategy decision in every point with respect to the current valuation. More formally, it holds for every strategy σ,
  every player 0 node v and every w ∈ vE that w ⪯_σ I^loc_G(σ)(v).» No tie-break is stated: the box's quotation and reading are exact.
- p. 23: «Theorem 6.14. Let n > 0. The Strategy Improvement Algorithm with the I^loc-policy requires at least 2^n improvement steps on
  G_n starting with ι_(G_n).» Exact as the box quotes it.
### 3.2 The answer
- (T-1) WRAP's H-policy is a policy with the I^loc property, on every game. Define I(s) := the H-part of S4a′'s result at the standard
  state of s (§2.4-§2.7 hold at every standard state, reachable or not). It is a map on S_0(H); every v goes to a ⊴_s-best successor
  (the property); (1) holds (the new successor is not worse than the old); (2) holds (if some v has a strictly better successor it
  moves to a strictly better one). The tie rule is one admissible choice among best successors.
- (T-2) **Claim NT (no tie on a 1-sink game; mine).** Let G with ι be a 1-sink game in [F11] §5's sense, with sink x, and σ a player-0
  strategy with Ξ_ι ⊴ Ξ_σ. Then Ξ_σ(u) ≠ Ξ_σ(u′) for all nodes u ≠ u′.
  Proof. By Sink Seeking (p. 8) every Ξ_σ(u) has cycle component x; every other node is more relevant than x (Sink Existence), so
  the cycle is x's loop and the path component of Ξ_σ(u) is the set of ALL nodes of the play from u before x, u itself included
  (the paper's own remark, p. 8: «the path-length component equals the cardinality of the path component»). Ξ_σ(x) = (x, ∅, 0) differs
  from every other value. If u, u′ ≠ x had equal values, u′ would lie on u's play and u on u′'s play; plays are positional, so u's
  play would return to u before reaching x: a cycle without x, against Sink Seeking. ∎
- (T-3) G_n with ι_(G_n) is a 1-sink game: [F11] Lemma 6.7 with Lemma 5.1 (p. 17, p. 8). I re-read both proofs. 6.7 (1): under
  τ(e_i) = h_i the edges of Table 4 allow no cycle but x's loop (s → f_j or x; r → g_j or x; f, e, h, k, g only move to k, x or a g of
  higher index; t, a, c, d only reach s, r, e or lower t's); 6.7 (2) and 5.1 as written. Neither uses the six priorities that differ
  between Table 4 and Figure 4.
- (T-4) Every strategy σ of an improvement run from ι has Ξ_ι ⊴ Ξ_σ ([F11] Theorem 3.2; in the fleet, landed R15 (a)). By Claim NT no
  two successors of a node tie at any state of the run, so the property of §3.1 determines I^loc(σ) uniquely there: every policy
  with the property, WRAP's included, produces the same run from ι_(G_n), which is therefore the run Theorem 6.14 speaks of. No
  reading of the proofs of Lemmas 6.2-6.13 is needed (Addendum A's route), and the lane's tie rule is never invoked on G_n.
- So (X-TIE) holds in its second form, «no tie occurs on the run», for every n ≥ 1, with premises [F11] Lemma 5.1, Lemma 6.7,
  Theorem 3.2 / R15 (a) and Claim NT. The same argument covers both priority versions (ranks by (Ω, index) are injective in SPEC).
- DATA for it (scratch/wrap_f11.py, my transcription of Table 4 / Figure 4 / ι from the PDF; Howard by H's own valuation on my
  engine): at every state of the run, sinkseek (a node whose cycle component is not x) 0, eqval (pairs of distinct nodes with equal
  values; the strong form of Claim NT) 0, tie (Even nodes with two best successors) 0, for n = 1, …, 10 with Figure 4's priorities and
  n = 1, …, 8 with Table 4's as printed (§5.3).
- Status. Claim NT and (T-4) are referee-originated: under L41 they count only when the lane has written them and the other referee
  has checked them independently. I would sign them.
### 3.3 (X-F11): what «Theorem 6.14, as published» carries
- F-1 (the game; READING, stated by the box, confirmed here). Table 4 (p. 15) prints d_i 4i + 1, e_i 4i + 2, g_i 4i + 4, k_i 8n + 4i + 7,
  f_i 8n + 4i + 9, h_i 8n + 4i + 10. Then Ω(g_n) = Ω(a_1) = 4n + 4, against p. 3's injectivity, and the highest priority is 12n + 10,
  against Fact 6.1's «12·n + 8 as highest priority» on the same page. Figure 4 (p. 16, G_3) shows d 3, 7, 11; e 4, 8, 12; g 6, 10, 14;
  k 33, 37, 41; f 35, 39, 43; h 36, 40, 44, i.e. each of the six formulas minus 2; Figure 3 / Table 3 (p. 13, «p′_1 = 3 and p_1 = 33»)
  agree with Figure 4. So the game of Theorem 6.14 is the Figure-4 game on the reading that Table 4 carries a misprint; XI-EXP must
  keep saying so (it does, §5.1 and §6). Node and edge counts: 10n + 4 and 1.5n² + 20.5n + 5, re-derived from Table 4's successor column.
- F-2 (the count). The paper proves its phase lemmas under a stated restriction (p. 17-18): «we will assume that b is different from
  0_n and that the two highest bits in b are zero and remain zero, i.e. we will only use the first n − 2 bits for counting. Note
  however, that every bit works as intended in the counter.» Lemma 6.13 gives k ≥ 4 steps per increment. So the bound 2^n is the
  theorem «as published»; what the written lemmas give line by line is of the order 4·2^(n−2) minus a constant. XI-EXP's «2^n + 3»
  inherits exactly this. For «not polynomial» any 2^Ω(n) suffices. DATA: T = 9·2^n − 10 for n = 1, …, 10 (my run), above 2^n.
- F-3 (wording). XI-EXP is exact: at least 2^n + 3 iterations on 10.5n² + 152.5n + 48 vertices. In the number of vertices this is
  2^Ω(√|W|): super-polynomial. §0 item 3's «exponential wherever Howard's is» should read «in n» or «super-polynomial» here.

## 4. Notes for the text (none is a gap of the proof)
- W-1 (required): the pe-free sentence of (W4) (§2.4).
- W-2 (required): the Definition says only «the new vertices are indexed after V». Statements (i)-(v) hold for every index order of
  the new vertices (no step uses one; my PERM = 1 sets, §5). The NUMBERS for N5 do depend on it: on W^L_n in my order N5 makes 3
  iterations (F = 1) for n = 1, …, 6; on the lane's frozen WL_1, …, WL_4 (wrap104.py's order; same vertex and edge counts and the same
  2-step signature multisets as mine, scratch/wrap_cmp.py) my engine gives 6 iterations (F = 4), the lane's column «N5 (spec) on
  W^L_n: 6». Both agree with (v) and Remark 3 (the key is an index sequence). The box should fix the order in the Definition, or say
  that its N5 columns are for wrap104.py's order. N5′-xi's counts are the same in both orders on these games, as (iii) and Claim NT
  say; on a game H with exact ties (iii)'s Howard run can depend on the order through «SPEC's choice, then the larger index».
- W-3 (required): premises to name. R15 (c) / (d) (the Howard run of H is finite; N5 terminates, so a first fallback exists in (v));
  [RULE] for Remark 3. 1E-N3 is used on W (P1, P2) and on H (Ω^H_s is the pointwise minimum).
- W-4 (for a packet): (W3) and (W8) say that K3, K2-r and E1-E4 «hold verbatim». The landed statements are about Γ3(G); a packet
  carries these proofs on W in full (they are short: §2.3, §2.8), with «valve» and «pe-play» defined for W.

## 5. Replay with my own code (docs/referee/scratch/; logs scratch/wrap_logs/; every run `python3 -I`)
### 5.1 Code
- Engine: this lane's rl_engine.py (successor 8: SPEC S1-S5 with FIX 1-4, Q1-Q4, written from the SPEC text; unchanged). New, written
  from the box's text: wrap_replay.py (the wrapper from the Definition; S4a′ from box 190 §1; Howard's step on H by H's OWN valuation
  on the same engine; a Zielonka solver; the counters). No lane code is imported.
- The box's six counters, my predicates: s3fail, nonstd, nohoward, fbwrong, endwrong, wrong. Twelve more from my reading of the proof:
  size; w1 (a pad, gate or valve as a cycle node or in a P-set, every state); w4a (σ̄ takes a pe); w4b, w4c (the values of (W4) (b),
  (c), compared as (node, P-set as a set of vertices, length)); w4d ((W4) (d), every pad); w5 (τ ≠ τ0 or Iτ ≠ ∅, every state); w6
  ((K0, K1) ∈ Iσ; W* of the pads and of v; TIE(v) = A(v); SPEC's σ_new(b) = y); w8 (κ1, κ2, κ3 after the fallback, no second
  fallback, final valves on pb, final σ̄ on pe); v5 (N5 mode: every move goes to a strictly H-better successor); rem2; rem3.
- T is computed without the run's fallback: the first state whose H-part has no strictly better successor by H's valuation.
### 5.2 Random and exhaustive games H (all 18 counters; «0» means every counter)
| set | mode | index order | files | runs (H, s0) | max T | sum T | max F | max \|W\| | sum of the 18 counters | FAIL lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exhaustive, 1 vertex, priorities 0-2 | N5 (spec) | as built | 1 | 6 | n/a | n/a | 1 | 17 | 0 | 0 |
| exhaustive, 1 vertex, priorities 0-2 | N5′-xi | as built | 1 | 6 | 0 | 0 | 1 | 17 | 0 | 0 |
| exhaustive, 2 vertices, priorities 0-2 | N5 (spec) | as built | 1 | 441 | n/a | n/a | 2 | 39 | 0 | 0 |
| exhaustive, 2 vertices, priorities 0-2 | N5′-xi | as built | 1 | 441 | 1 | 117 | 2 | 39 | 0 | 0 |
| exhaustive, 2 vertices, priorities 0-2 | N5′-xi | random (PERM 1) | 1 | 441 | 1 | 117 | 2 | 39 | 0 | 0 |
| exhaustive, 3 vertices, priorities 0-2 | N5 (spec) | as built | 4 | 185,193 | n/a | n/a | 3 | 75 | 0 | 0 |
| exhaustive, 3 vertices, priorities 0-2 | N5′-xi | as built | 4 | 185,193 | 3 | 125,643 | 4 | 75 | 0 | 0 |
| random, family dup | N5 (spec) | as built | 4 | 7,600 | n/a | n/a | 4 | 663 | 0 | 0 |
| random, family dup | N5 (spec) | random (PERM 1) | 4 | 7,600 | n/a | n/a | 4 | 595 | 0 | 0 |
| random, family dup | N5′-xi | as built | 4 | 7,600 | 7 | 6,967 | 8 | 663 | 0 | 0 |
| random, family dup | N5′-xi | random (PERM 1) | 4 | 7,600 | 6 | 6,899 | 7 | 595 | 0 | 0 |
| random, family even | N5 (spec) | as built | 4 | 7,600 | n/a | n/a | 5 | 616 | 0 | 0 |
| random, family even | N5 (spec) | random (PERM 1) | 4 | 7,600 | n/a | n/a | 6 | 640 | 0 | 0 |
| random, family even | N5′-xi | as built | 4 | 7,600 | 8 | 11,008 | 9 | 616 | 0 | 0 |
| random, family even | N5′-xi | random (PERM 1) | 4 | 7,600 | 9 | 11,205 | 10 | 640 | 0 | 0 |
| random, family odd | N5 (spec) | as built | 4 | 7,600 | n/a | n/a | 1 | 599 | 0 | 0 |
| random, family odd | N5 (spec) | random (PERM 1) | 4 | 7,600 | n/a | n/a | 1 | 623 | 0 | 0 |
| random, family odd | N5′-xi | as built | 4 | 7,600 | 0 | 0 | 1 | 599 | 0 | 0 |
| random, family odd | N5′-xi | random (PERM 1) | 4 | 7,600 | 0 | 0 | 1 | 623 | 0 | 0 |
| random, family rand | N5 (spec) | as built | 4 | 7,600 | n/a | n/a | 4 | 610 | 0 | 0 |
| random, family rand | N5 (spec) | random (PERM 1) | 4 | 7,600 | n/a | n/a | 5 | 617 | 0 | 0 |
| random, family rand | N5′-xi | as built | 4 | 7,600 | 7 | 7,068 | 8 | 610 | 0 | 0 |
| random, family rand | N5′-xi | random (PERM 1) | 4 | 7,600 | 9 | 6,996 | 10 | 617 | 0 | 0 |
| random, family twin | N5 (spec) | as built | 4 | 7,600 | n/a | n/a | 4 | 764 | 0 | 0 |
| random, family twin | N5 (spec) | random (PERM 1) | 4 | 7,600 | n/a | n/a | 4 | 831 | 0 | 0 |
| random, family twin | N5′-xi | as built | 4 | 7,600 | 8 | 5,908 | 9 | 764 | 0 | 0 |
| random, family twin | N5′-xi | random (PERM 1) | 4 | 7,600 | 7 | 5,883 | 8 | 831 | 0 | 0 |
| all rows | | | | 523,721 | | | | | 0 | |
- Families (own generator, Python `random`, seeds in the file names): rand (random owners, 1-3 successors, self-loops allowed,
  priorities from n, 2n or 4 values), dup (2 or 3 priorities: many equal values), even / odd (one-player games; odd has V_E = ∅ and
  T = 0), twin (two low twins with one common successor, offered to Even vertices: exact value ties). PERM 1: the new vertices in a
  random index order (W-2). exh: EVERY game H on 1, 2 and 3 vertices with priorities in {0, 1, 2}, every non-empty successor set,
  every owner vector and every s0.
- Controls (300 games each, family rand, seed 3310; logs ctrl_*.out). Every counter fires under at least one:
| control | N5′-xi: counters that fire (count) | N5 (spec): counters that fire (count) |
| --- | --- | --- |
| 1 best := worst in the Howard test | nohoward 568 | none |
| 2 T shifted by one | fbwrong 300, endwrong 300 | none |
| 3 standard state of another s0′ | s3fail 235 | s3fail 235 |
| 4 expected regions with K2 flipped | wrong 300, rem2 300 | wrong 300, rem2 300 |
| 5 wrapper: y of Ω 1, pb of Ω 2 | s3fail 300, nonstd 776, nohoward 388, fbwrong 194, endwrong 194, w4b 3,328, w4c 3,459, w4d 571, w6 3,419 | s3fail 300, nonstd 700, w4b 3,118, w4c 3,200, w4d 560, w6 3,128, v5 23, rem3 84 |
| 6 wrapper without pe_o | s3fail 282, nonstd 558, nohoward 22, fbwrong 50, endwrong 50, size 282, w4b 344, w4c 277, w4d 49, w5 1,404, w6 640 | s3fail 282, nonstd 463, size 282, w4b 302, w4c 236, w4d 44, w5 1,309, w6 583, v5 9, rem3 22 |
| 7 wrapper with 5-edge Odd paths | nohoward 8, fbwrong 2, endwrong 2, size 1,705, w4b 1,211, w4c 1,073, w4d 9 | size 1,705, w4b 1,005, w4c 865, w4d 9, v5 3 |
| 8 wrapper with c_W of Ω 4 | nohoward 37, fbwrong 60, endwrong 60, w4a 953, w4b 978, w4c 1,131, w4d 122, w6 1,362 | w4a 725, w4b 710, w4c 776, w4d 99, w6 1,046, v5 7 |
| 9 inverted expectations (κ1 / κ2 swapped, K1 as a pad, v5 inverted, rem3 against 0) | w1 839, w8 300 | w1 724, w8 300, v5 393, rem3 300 |
  Counters with no firing control: none (of 18).
  Controls 5-8 change the wrapper, and show which parts the proof needs: y above pb at a valve (5); the pads pe_o (6, w5: Iτ ≠ ∅); the
  UNIFORM 6-edge stretch (7: with 5-edge Odd paths the run is no longer Howard's, nohoward and fbwrong fire); c_W above H (8, w4a).
### 5.3 Friedmann's G_n, my transcription from the PDF (wrap_f11.py; logs f11_*.out)
| n | nodes, edges, highest Ω (fig4) | T fig4 | T table4 | 2^n | 9·2^n − 10 | six H-counters, fig4 / table4 | \|W^L_n\| | N5′-xi fig4: iterations, first fallback, fallbacks, 18 counters | the same, random index order | the same, table4 | N5 (spec) fig4, my order: iterations, F, 18 counters |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 14, 27, 20 | 8 | 8 | 2 | 8 | 0 / 0 | 211 | 11, 9, 1, 0 | 11, 9, 1, 0 | 11, 9, 1, 0 | 3, 1, 1, 0 |
| 2 | 24, 52, 32 | 26 | 26 | 4 | 26 | 0 / 0 | 395 | 29, 27, 1, 0 | 29, 27, 1, 0 | 29, 27, 1, 0 | 3, 1, 1, 0 |
| 3 | 34, 80, 44 | 62 | 62 | 8 | 62 | 0 / 0 | 600 | 65, 63, 1, 0 | 65, 63, 1, 0 | 65, 63, 1, 0 | 3, 1, 1, 0 |
| 4 | 44, 111, 56 | 134 | 134 | 16 | 134 | 0 / 0 | 826 | 137, 135, 1, 0 | 137, 135, 1, 0 | 137, 135, 1, 0 | 3, 1, 1, 0 |
| 5 | 54, 145, 68 | 278 | 278 | 32 | 278 | 0 / 0 | 1,073 | 281, 279, 1, 0 | 281, 279, 1, 0 | 281, 279, 1, 0 | 3, 1, 1, 0 |
| 6 | 64, 182, 80 | 566 | 566 | 64 | 566 | 0 / 0 | 1,341 | 569, 567, 1, 0 | not run | not run | 3, 1, 1, 0 |
| 7 | 74, 222, 92 | 1,142 | 1,142 | 128 | 1,142 | 0 / 0 | 1,630 | 1,145, 1,143, 1, 0 | not run | not run | not run |
| 8 | 84, 265, 104 | 2,294 | 2,294 | 256 | 2,294 | 0 / 0 | not run | not run | not run | not run | not run |
| 9 | 94, 311, 116 | 4,598 | not run | 512 | 4,598 | 0 / not run | not run | not run | not run | not run | not run |
| 10 | 104, 360, 128 | 9,206 | not run | 1,024 | 9,206 | 0 / not run | not run | not run | not run | not run | not run |
- H-run columns: T is the number of improvement steps of Howard's rule from ι on G_n by G_n's own valuation; fact61 (10n + 4 nodes,
  1.5n² + 20.5n + 5 edges, and for fig4 highest priority 12n + 8 and injective), sinkex, w1all (my Zielonka: player 1 wins every node),
  sinkseek, eqval, tie as in §3.2: all 0 on every row.
- Wrapper columns: my wrapper of my G_n under my N5′-xi: iterations = T + 3, one fallback at T + 1, all 18 counters 0, in my index order,
  in a random order (PERM 1) and for both priority versions. The lane's rows are 11, 29, 65, 137, 281, 569 (n = 1, …, 6) and 1,145
  (n = 7, Addendum A.1): equal. The n = 8 wrapper row (1,940 vertices by §1's formula; the lane's 2,297 iterations) was still
  running on my engine when this report was committed; it comes as an addendum.
### 5.4 My engine on the lane's frozen instances (wrap_inst.py; logs inst_*.out)
| file (lane's frozen instance) | vertices | N5′-xi: iterations, fallbacks, first fallback, regions = my Zielonka | N5 (spec): the same | states with τ changed or Iτ ≠ ∅ (both modes) |
| --- | --- | --- | --- | --- |
| F_2.pg | 708 | 33, 1, 31, True | not run | 0 |
| F_3.pg | 1,017 | 73, 1, 71, True | not run | 0 |
| F_4.pg | 1,326 | 153, 1, 151, True | not run | 0 |
| F_5.pg | 1,635 | 313, 1, 311, True | not run | 0 |
| W_2.pg | 567 | 33, 1, 31, True | 3, 1, 1, True | 0 |
| W_3.pg | 818 | 73, 1, 71, True | 4, 1, 2, True | 0 |
| W_4.pg | 1,069 | 153, 1, 151, True | 5, 1, 3, True | 0 |
| W_5.pg | 1,320 | 313, 1, 311, True | 6, 1, 4, True | 0 |
| W_6.pg | 1,571 | 633, 1, 631, True | 7, 1, 5, True | 0 |
| WL_1.pg | 211 | 11, 1, 9, True | 6, 1, 4, True | 0 |
| WL_2.pg | 395 | 29, 1, 27, True | 6, 1, 4, True | 0 |
| WL_3.pg | 600 | 65, 1, 63, True | 6, 1, 4, True | 0 |
| WL_4.pg | 826 | 137, 1, 135, True | 6, 1, 4, True | 0 |
- N5′-xi: the lane's iteration counts on every row run. N5 (spec): the lane's 6 on WL_n and 3, 4, 5, 6, 7 on W_2, …, W_6. The F_n rows
  belong to FREE-REACH (§4 of the box), which I did not read as a verdict; they are here as engine cross-checks only.
### 5.5 Limits, stated plainly
- Random H are small (n ≤ 40, T ≤ 9): they test each step of the proof state by state, not any length. The long runs are
  Friedmann's games only.
- One referee engine (rl_engine, SPEC-exact tie-breaks) and one S4a′ written by me; the lane has two engines of its own. Agreement of
  the counts is DATA, not a proof of WRAP; the proof is §2.
- The wrong counter compares against my own Zielonka, not the harness's.

## 6. TARGET.md diff and scope
- WRAP and XI-EXP claim no algorithm and no bound; nothing is M3 or M4. XI-EXP, if refereed, is a statement that ONE candidate
  (N5′-xi, box 190's rule) is not polynomial on all parity games (TARGET.md §2 quantifies over every parity game; W(H, s0) is one).
  It is a dead end in the making, to be recorded with its instance family under CLAUDE.md's dead-end rule and L43 («DEAD» needs a
  refereed proof): until WRAP and Claim NT are signed by two referees it is DATA with numbers.
- It says nothing against N5 (WRAP (v), Remark 3: at most m_E − |V_E| + 3 iterations on W(H, s0), given [RULE]) and nothing about
  boxes 208 / 209 on genome games (their scope lines exclude general games).
- CLAUDE.md's trap («A "counterexample" from an unfaithful implementation is not a counterexample»): the two objects were rebuilt
  here from their texts, N5′-xi from box 190 §1 on an engine written from the SPEC, G_n from the PDF; both reproduce the lane's
  counts. I did not check the lane's code against the texts line by line (not asked; a packet review would).

## 7. For a packet (what I would test a frozen text against)
- PW-1 (required): W-1, W-2, W-3 fixed in the text; W-4 (proofs on W in full).
- PW-2 (required): (X-TIE) replaced by Claim NT with its premises ([F11] Lemma 5.1, Lemma 6.7, Theorem 3.2 or R15 (a)), written by the
  lane; XI-EXP then conditional only on the referees' signatures of WRAP and Claim NT, with [F11] Theorem 6.14 as a cited published
  theorem and F-1, F-2 stated next to it.
- PW-3 (required): DATA clauses with units as the tools compute them; the N5 columns tied to an index order (W-2); the lane's tools
  were not opened by me, so the DATA rule is still to do.
- PW-4 (the Lead's call): whether FREE-REACH (§4) and the F_n rows go into the same packet; they are not needed for XI-EXP.

## 8. Tools and outputs (docs/referee/scratch/)
wrap_replay.py, wrap_f11.py, wrap_inst.py, wrap_cmp.py, wrap_summ.py, wrap_run.sh, wrap_exh_run.sh, wrap_ctrl_run.sh, wrap_f11_run.sh;
wrap_logs/: main_*.out, exh_*.out, ctrl_*.out, f11_*.out, inst_*.out, cmp.out, valve_pb.out, *_run.log, summ.out; the tables of §5 are
generated from these logs by wrap_tables.py (no number typed by hand). f11_W_xi_fig4_long7.out is `WRAP=xi python3 -I wrap_f11.py 7`.
