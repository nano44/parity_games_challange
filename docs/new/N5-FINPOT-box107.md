# Box 107 N5-FINPOT: a finer potential below the first difference (L-NEW successor 41; Lead brief after 07:47Z, 2026-10-31)
Started 07:48Z, written 08:0xZ (date -u). Labels: PROVED (lane) = proved here, not refereed; CONJECTURE; DATA; DEAD (with instance).
Nothing here is M3/M4. G-N5-TIME stays OPEN.

## 0. Setting, premises, sources
- N5 = SSI-GLOBAL as in docs/new/N5-ssi-global.md (SPEC S1-S5), engine experiments/new/box21/n5x.py (+ experiments/si/si.py).
- W-run F = [p, q]: a maximal run of transitions k → k + 1 with τ_(k+1) = τ_k, no fallback, and the W-cycle node of every vertex
  constant. This is the same detection as L-SI's ceilpot.py / treestab.py. Here Ξ_k is the valuation of σ_k against Odd's best
  response, and W_k := val(σ_k, τ) with τ = τ_p.
- CS = R93 coordinate sequences, of length n + 2: reward of the cycle node, the n signed rank bits from the top, then the signed length.
  The VJ order ⊴ is the lexicographic order on CS. This is the order L-SI box 53c uses.
- Sources read, not edited:
  - L-SI docs/si/N5-SBF-box53.md §7-§9 and experiments/si/sb53/ceilpot.py at claude/l-si c7f00306 (template; read with git show,
    because c7f00306 is not on trunk 87be2541).
  - R93 (CS), R95, R97 SRC-COUNT (source events), R15 (a) (Ξ monotone), and box 53b's Fact CEILING (Ξ_k ⊴ W_k).
  - VJ valuations and optimal counterstrategies: Friedmann, LMCS 7(3:19) 2011, arXiv 1106.0778, §3, as cited in si.py's header.
    This is the same premise SPEC and R57 use. No new external source.

## 1. Lemmas (PROVED, lane)
- Lemma W-MON. At every non-fallback transition with τ_(k+1) = τ_k: W_k ⊴ W_(k+1) pointwise. The W-cycle nodes need not be constant.
  - Proof.
    - S1 sets σ_(k+1) := Even's optimal strategy in the one-player game H_k(τ): Even is restricted to {σ_k(y)} ∪ I_σk(y), and Odd is
      fixed to τ. (In n5x.step this is `best` of the dual engine on that arena.)
    - VJ / Friedmann §3: the optimal counterstrategy's valuation is pointwise ⊵ the valuation of every strategy in the arena. This is
      SPEC's own reading of "optimal" (A5 in n5b), the same premise as R57 OUT-G.
    - σ_k is a strategy of H_k, and val(σ, τ) depends only on the play. So W_(k+1) = val(σ_(k+1), τ) ⊵ val(σ_k, τ) = W_k. □
  - DATA: WDEC 0 on 14,028 corpus W-run transitions and on all six pins.
- Lemma O-ARENA. Let O(τ) := {τ(o)} ∪ I_τ(o) (Odd's arena; it depends on τ only). On a W-run, W_k = Ξ^O(σ_k), the valuation of σ_k
  against Odd's best response INSIDE O(τ). The same holds at each start state k of a transition of F.
  - Proof.
    - S3 computes τ_(k+1) as Odd's optimum in O(τ_k) against σ_k (old σ, n5b reading A6).
    - τ_(k+1) = τ_k = τ, so τ attains the optimum. Hence val(σ_k, τ) = Ξ^O(σ_k). □
  - Reading: a W-run evaluates ONE Even strategy in two nested games, G_O ⊆ G (only Odd edges removed). W is the G_O value and Ξ the
    G value, so Ξ ⊴ W is CEILING again.
  - DATA: WOX 0 (corpus and pins).
- Lemma SANDWICH (elementary). For equal-length sequences in lexicographic order, x ⊴ y ⊴ z implies
  lcp(x, z) = min(lcp(x, y), lcp(y, z)). In particular lcp(x, z) ≤ lcp(y, z).
  - Proof.
    - Let i := lcp(x, z). Every y between x and z agrees with both on [0, i).
    - If i < length, then x_i < z_i and x_i ≤ y_i ≤ z_i, so y_i differs from x_i or from z_i. □
- Corollary FROZEN (monotone potentials with polynomial range).
  - Freeze the reference at the END instead of moving it. On F = [p, q]:
    - BW_k := Σ_v lcp(CS W_k(v), CS W_q(v)) is non-decreasing;
    - AF_k := Σ_v lcp(CS Ξ_k(v), CS W_q(v)) is non-decreasing;
    - on the whole run, LS_k := Σ_v lcp(CS Ξ_k(v), CS Ξ_end(v)) is non-decreasing.
  - All three lie in [0, n(n + 2)].
  - Proof. W-MON, R15 (a) and CEILING give, for k ≤ k′, the chains W_k ⊴ W_k′ ⊴ W_q and Ξ_k ⊴ Ξ_k′ ⊴ W_k′ ⊴ W_q. Apply SANDWICH. □
  - L-SI's A_k = Σ lcp(Ξ_k, W_k) is NOT monotone, because its reference moves (W rises). Freezing the reference is the whole gain.
  - DATA: AFDEC = BWDEC = LSDEC = 0 everywhere.
- Lemma BW-ACC (accounting). Let M := n(n + 2) + 1, and let N_F := #{transitions of F at which BW is flat and A does not fall}. Then
  |F| ≤ (M + 1)·n(n + 2) + M·N_F.
  - Proof.
    - Take Φ := M·BW − A, with Φ ∈ [−n(n + 2), M·n(n + 2)].
    - A BW-rise moves Φ by ≥ M − n(n + 2) = 1, and a BW-flat A-fall moves it by ≥ 1.
    - Every other transition (counted in N_F) moves Φ by ≥ −n(n + 2). Sum the moves. □
  - Every W-constant transition is in N_F: BW is flat, and A is non-decreasing by SANDWICH with W fixed. So
    N_F = T1_F + T4_F, where:
    - T1 = W-constant transitions;
    - T4 = W changes, BW flat, A does not fall.
  - Corollary BW-EQ: WRUN-POLY ⟺ (T1 + T4)-POLY. There is no AUP term: CEIL-ACC's AUP-POLY and AFLAT-POLY collapse into one count,
    and N_F ≤ ANDN_F.
- Theorem HIER-RED (frozen-reference hierarchy).
  - Let V_k be a vector of pointwise ⊴-monotone values on F; each choice below is valid. A level-1 block is the set of transitions
    of F at which V changes, with reference V_e (e = the block's end state) and potential P = Σ lcp(CS V_k, CS V_e).
  - Transitions where P rises are PAID at that level. Each maximal stretch of P-flat transitions is a sub-block with its own
    reference at its end.
  - h_F := the deepest level that pays. Every nonempty block pays its last transition, so h_F is finite. Then the V-changing
    transitions of F number < (R + 1)^(h_F), with R = (number of coordinates of V)·(n + 2).
  - Proof.
    - P is monotone (SANDWICH), so it rises ≤ R times per block, which leaves ≤ R + 1 sub-blocks.
    - With T(j) the transitions in a block of remaining depth j: T(1) ≤ R and T(j) ≤ R + (R + 1)·T(j − 1), so T(h) ≤ (R + 1)^h − 1. □
  - Instances:
    - (W) V = W, R = n(n + 2): |F| ≤ T1_F + (n(n + 2) + 1)^(h^W_F).
    - (V) V = (W, Ξ), R = 2n(n + 2): |F| ≤ NOV_F + (2n(n + 2) + 1)^(h^V_F), with NOV = transitions at which σ moves and neither Ξ nor W
      does.
    - (Ξ) V = Ξ over the whole run: |run| ≤ NOX + (n(n + 2) + 1)^(h^Ξ). DATA: deeper than (W) (u23sw64 3, x31_rx48 5), so splitting
  into W-runs and using W is what keeps the depth low.
  - So WRUN-POLY ⟸ BOUNDED-DEPTH: h^W_F = O(1) and T1-POLY (T1 = box 53b's INS face), or h^V_F = O(1) and NOV-POLY.
  - Honest scope: HIER-RED itself is generic, valid for any pointwise lex-monotone vector sequence. The N5 content is W-MON,
    O-ARENA, CEILING and the DATA below. A super-polynomial W-run must therefore show h_F ≥ log|F| / log(R + 1): NESTED DIGITS of W
    below the first difference with the frozen ceiling, i.e. a counter in the W-hierarchy.

## 2. DATA (experiments/new/box107/; corpus = L-SI box 53's 1,132 runs (box59 sbcg + si/root alt lists), 14,028 W-run transitions; equals
## L-SI's 14,868 minus latew_K16_m32 + fx_K8_m32 = 840)
- Classification of W-run transitions (finpot.py):
  - T2 (BW rises): 13,633 (97.2 %);
  - T3 (BW flat, A falls): 25;
  - T1 (W constant): 79;
  - T4: 291, of which 237 are source events. Max 17 in a game, 13 in one W-run (x31_rx48).
- Pins (n5x; n5b identical state by state on all six; Oink 8fbf0a7 --zlk and --tl both "solution verified", the two agree, and they
  equal N5's regions at its stop: pincheck.txt):

| pin | n | WT | T1 | T2 | T3 | T4 | h^W | h^V | h^Ξ (whole run) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| u23sw64_n32 (red/tie) | 32 | 13 | 8 | 5 | 0 | 0 | 1 | 1 | 3 |
| runfam_K40 | 79 | 171 | 0 | 171 | 0 | 0 | 1 | 1 | 2 |
| obs_K12_m24 | 272 | 324 | 0 | 24 | 300 | 0 | 2 | 2 | 2 |
| src2_K3 | 285 | 324 | 0 | 24 | 300 | 0 | 2 | 2 | not run |
| rcl_K24 | 321 | 324 | 0 | 24 | 300 | 0 | 2 | 2 | not run |
| x31_rx48 (red/xing) | 48 | 47 | 0 | 30 | 0 | 17 | 2 | 2 | 5 |

- The two A-regimes of box 53d are both paid, at level 1:
  - runfam_K40's A-flat regime: BW rises at all 171 W-run transitions, including the 154 source-free A-non-falls.
  - u23sw64's floor interval (A = 0, W constant, Ξ in another cycle class, 8 transitions): every potential referenced to W is blind
    there (A, AF, BW, RKW, LCM all flat). The joint reference (Ξ_end) pays every transition: h^V = 1 with NLV1 13.
  - The leapfrog / k-SOURCE families (obs, src2, rcl) are depth 2: 24 level-1 rises and 300 level-2 transitions in sub-blocks of
    ≤ 25. R157's degree factor sits in ONE extra level, not in many.
- Depth over the corpus (hier.py, hier2.py):
  - h^W ∈ {0: 489, 1: 532, 2: 111} runs, never 3;
  - h^V ≤ 3 (3 only on red/kw/cw11_n24, where h^W = 1);
  - MONOX 0 (no hierarchy potential ever decreased);
  - NOV = 4 (tog6a_n32, tog6b_n32; see DEAD (c)).
- Other candidates, none monotone (two-sided on runfam_K40, src2_K3, obs):
  - RKW = Σ_v #{z : W(z) ⊴ Ξ(v)}: runfam 11 up / 104 down;
  - RKX (dual rank): 95 up / 17 down;
  - PAG (common play prefix of the Ξ-play and the W-play): runfam 100 up / 69 down;
  - LCM (lcp without the cycle coordinate), |D|, and the number of distinct values. LCM is flat wherever A is.

## 3. DEAD ends (exact obstruction, instance)
- (a) «BW strictly rises at every W-changing transition» (BW alone pays everything outside T1): DEAD on red/xing/instances/x31_rx48
  (start = n5x default, written to box107/inst/x31_rx48.start). W-run 36..50 has 13 consecutive T4 transitions.
  - At each of them the W-changed vertices have Ξ = W (a = n + 2 = 50, so A is flat at 2170).
  - W moves at position 17 while b = lcp(W, W_end) = 4: BW is blind below ITS first difference, the same blindness as A one level
    down.
  - The level-2 reference (the stretch's end) pays all 13 (h^W = 2).
- (b) «A potential referenced to the W-ceiling (A, AF, BW, rank among W-values, lcp without the cycle coordinate) pays the W-constant
  floor interval»: DEAD on u23sw64_n32, states 1-9. W is constant and Ξ has a different cycle node at all 32 vertices, so every one
  of these is flat 8 times. Only a Ξ-referenced level pays it.
- (c) «NOV = 0: every σ-move strictly raises Ξ or W»: DEAD on red/so/instances/tog6a_n32 (and tog6b), k = 8.
  - The Even vertex 13 is its own Ξ-cycle node, valuation (13, 0, 0). It switches 30 → 27, an improving edge by length (5 → 4), and
    no value changes.
  - So strictness fails exactly at cycle-node switches. These are box 53b's CN switches, which INS-RED already counts separately.
- (d) RKW, RKX, PAG, |D|, NG as MONOTONE potentials: DEAD (two-sided counts above, runfam_K40).

## 4. CONJECTURE and what it asks of L-RED
- CONJECTURE HDEPTH: h^W_F ≤ 2 for every W-run of N5 (DATA: 1,132 runs + 6 pins; never 3).
  - HDEPTH + T1-POLY ⟹ |F| ≤ T1_F + (n(n + 2) + 1)² ⟹ WRUN-POLY.
  - A weaker form also suffices: h^W_F = O(1).
  - I do NOT believe HDEPTH unconditionally: a binary counter in W with three nested digits would kill it, and nothing above
    forbids one.
- L-RED target (Lead decides; it fits the FEEDBACK construction of L-RED 37).
  - A super-polynomial W-run must have h^W (or h^V) ≥ log|F| / log(n(n + 2) + 1).
  - So FEEDBACK compounding must NEST: each feedback level must create a new level of W-digits below the first difference with the
    frozen ceiling.
  - A W-run with h^W = 3 is the first concrete step. hier.py measures it.
- What is NOT proved: T1-POLY (box 53b INS-POLY), BOUNDED-DEPTH, HDEPTH. HIER-RED is a reduction, not a bound.

## DONE / FINDINGS / NEEDS
- DONE: this note.
  - experiments/new/box107/: finpot.py, t4trace.py, xtrace.py, hier.py, hier2.py, hier3.py, pinwin.py, pincheck.sh, runfin.sh,
    runhier.sh, runhier2.sh;
  - outputs fin_*.txt, hier_*.txt, hier2_*.txt, hier3_pins.txt, t4_x31_rx48.txt, pincheck.txt; inst/x31_rx48.start;
  - pins in experiments/new/check.sh «box 107 FINPOT». SHA: see the commit.
- FINDINGS:
  - PROVED (lane): W-MON, O-ARENA, SANDWICH, FROZEN (BW, AF, LS monotone with range n(n + 2)), BW-ACC (|F| ≤ (M + 1)n(n + 2) + M·N_F),
    BW-EQ (WRUN-POLY ⟺ (T1 + T4)-POLY), HIER-RED (|F| ≤ T1_F + (n(n + 2) + 1)^(h^W_F)).
  - DATA: BW pays 97.2 % of corpus W-run transitions; h^W ≤ 2 on the whole corpus; both box 53d regimes are paid at level 1.
  - DEAD: (a) BW alone (x31_rx48); (b) W-referenced potentials on the floor interval (u23sw64); (c) NOV = 0 (tog6a_n32);
    (d) rank / path-agreement potentials as monotone.
  - CONJECTURE: HDEPTH.
- NEEDS: Lead: route HDEPTH / «a W-run with h^W ≥ 3» to L-RED 37 as the measurable form of FEEDBACK nesting; W-MON and O-ARENA are short
  and could join a packet if wanted.
