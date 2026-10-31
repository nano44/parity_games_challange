# Box 110 N5-WIDTH: the width lemma, proof side (L-NEW successor 41; Lead 10:12Z, 2026-10-31)
Started 10:12Z, written ~10:2xZ (date -u). Labels: PROVED (lane); CONJECTURE; DATA; DEAD; READING.
Setting as in boxes 107-109.
- F is a W-run.
- Bits: CS with UNARY length (box 109 §2). Every coordinate is oriented so that 1 = better for Even:
  - a rank-r bit is [r visited] for even r and [r not visited] for odd r;
  - the length thresholds are [sl ≥ j], j = −n..n;
  - the cycle coordinate is constant on F.
  - So each W-value is a 0/1 vector of 3n + 1 bits in lex order.
- Sources read, not edited:
  - L-RED R159 (claude/l-red 599f9571: experiments/red/hd/, hd_H40 copied read-only to experiments/new/box110/);
  - L-SI box 54 (claude/l-si 38fc41c6, docs/si/N5-SRC-box54.md: OLD-PLAY, ODD-STEP, ODD-RELAY, ODD-ADD, SRC-ROOT; sbq2_K8_m16 copied
    read-only to box110/).
  - R160 was not on claude/l-red at my fetch (10:13Z); not read.

## 0. Answer
- The WIDTH lemma is NOT proved.
- What is proved here makes it a single named count. Width IS resets: a digit can be re-fixed only after it was reset (a good bit
  turned bad), and W-runs are polynomial EXACTLY when resets are (RESET-RED, an equivalence).
- Every reset is copied from a switched vertex (RESET-ROOT). Inside a W-run no selector lags (NO-LAG). So multiplication cannot
  come from W-side selector leapfrogs; it needs the Ξ-side insertion sequence to re-arm trade-down switches (§3).
- DATA:
  - hd_H40 (depth 40) has ZERO resets: depth is free.
  - The multiplying families have a reset at almost every transition: sbq2 151 of 152, obs and src2 all 324, x31_rx48 46 of 47.
  - The corpus has resets at 12,985 of 13,949 W-changing transitions.
  - So resets are the norm, not a rare event to be charged.
- §0b corrects box 108.

## 0b. ERRATUM to box 108 (docs/new/N5-HDEPTH-box108.md §2, Remark «what depth is NOT»)
- The sentence «A reset at a fixed vertex is impossible anyway (W-MON)» is FALSE.
- W-MON is LEXICOGRAPHIC monotonicity. When W(v) improves at a position q, every lower coordinate may get worse.
- DATA: resets at fixed vertices are everywhere (RT below). Box 108's other statements do not use this sentence.

## 1. Lemmas (PROVED, lane)
- Lemma BIT-ALT. For every vertex v and bit b, along F: GOOD_F(v, b) ≤ 1 + BAD_F(v, b). Here GOOD / BAD count the transitions at
  which bit b of W(v) flips 0 → 1 / 1 → 0.
  - Proof. A 0/1 sequence alternates. □
- Lemma FIRST-GOOD. Every change of W(v) on F flips its first differing bit 0 → 1.
  - Proof. W-MON, and lex order on oriented bits. □
- Theorem RESET-RED (an equivalence). Let WCT_F be the W-changing transitions and TD_F := Σ_(v, b) BAD_F(v, b) the resets. Then
  WCT_F ≤ Σ_v WCH_F(v) ≤ n(3n + 1) + TD_F, so |F| ≤ T1_F + n(3n + 1) + TD_F. Conversely TD_F ≤ (3n + 1)·n·WCT_F.
  - Proof.
    - Each W-changing transition changes some W(v).
    - By FIRST-GOOD, WCH_F(v) ≤ Σ_b GOOD_F(v, b), and BIT-ALT bounds this by (3n + 1) + Σ_b BAD_F(v, b).
    - For the converse, a change has ≤ 3n + 1 flips. □
  - So WRUN-POLY ⟺ (T1 + TD)-POLY. T1 is box 53b's INS face.
  - Reading of the Lead's «width». Take a level-i digit of v inside one hold of level i − 1. By BIT-ALT, each re-fix after the first
    needs a reset of that bit in between. By FIRST-GOOD, each reset comes with a good flip at a higher bit of v, inside the hold
    (so between the level-(i − 1) pending digit and the level-i digit).
    - So width_i ≤ 1 + (resets of the level-i bit inside the hold), and each such reset is paid by a fix of an intermediate digit.
    - «Widths multiply» is exactly «resets nest»: the intermediate fixes are themselves re-fixes after resets.
    - «Widths add» would be TD-POLY.
  - DATA: VIOL 0 (bound) and VB 0 (BIT-ALT) on the corpus (1,132 runs) and the eight pins (res_*.txt, res2_pins.txt).
- Lemma COPY. Let k → k + 1 be a transition of F and v a vertex with successor z on both plays (Even with σ_(k+1)(v) = σ_k(v) = z,
  or Odd with z = τ(v)), v ∉ C. Then W_j(v) = Φ(v; W_j(z)) for j = k, k + 1. The map Φ(v; ·):
  - keeps v's own rank bit fixed (v is on its own play; the bit is the same at both states);
  - copies every other rank bit;
  - shifts the length thresholds by one place.
  - Hence every flip of W(v) at k is a flip of W(z) at k, the same bit or the shifted threshold, in the same direction.
  - Proof. P-N5-SRC [PLAY] (quoted in L-SI box 54 §1): val(y_0) = Φ(y_0; val(y_1)) with Φ independent of the state. On F the W-cycle
    nodes are constant, so both values share the cycle node, and Φ adds v's bit (if v is more relevant than the cycle node) and 1 to
    the length. □
- Corollary RESET-ROOT. If W(v) has a reset at k, follow v's (σ_(k+1), τ)-play through vertices that did not switch. The first
  switched Even vertex y on it exists and has the same reset in W(y).
  - Proof.
    - If no vertex on the play switched, the play is unchanged and W(v) did not change.
    - Otherwise apply COPY along the unswitched prefix. C-vertices keep the constant value (λ_W(c) = c on F), so the chain never
      passes one with a change. □
  - So TD_F ≤ n·TDROOT_F, where TDROOT_F := the resets in W(y) summed over the switched vertices y. Resets are BORN only at switches:
    a switch y: a → b with W(b) ▷ W(a), first difference at q, and some lower bit worse. Call that a TRADE-DOWN switch.
  - DATA: ROOTRES = RT on the corpus (12,985 of 12,985) and on every pin.
- Corollary NO-LAG (from box 108 NEW-EDGE). Inside F, a W-change never comes from a sibling W-overtake within an unchanged arena.
  - Proof.
    - W_(k+1) = OPT(H_k), and W_k = OPT(H_(k−1)).
    - If H_k ⊆ H_(k−1), then W_(k+1) ⊴ W_k, so W_(k+1) = W_k (W-MON).
    - Every W-changing transition re-solves the arena optimum globally, and every selector's choice is W-optimal in the arena at once.
      There is no «passive selector» lag on the W side. □
  - Consequence (READING, with L-SI's ODD-ADD). Odd vertices only relay (ODD-ADD), and Even selectors never lag on W (NO-LAG). So a
    trade-down switch at y must be enabled by a FRESH arena insertion (y, b) or (y′, b′) on y's new play (NEW-EDGE).
    - By OVERTAKE-W, that insertion is a strict Ξ-overtake.
    - Multiplication of widths therefore needs the Ξ-SIDE to re-arm trade-down insertions repeatedly inside one hold. The engine is
      Ξ(b) ◁ Ξ(a) again after each switch, with Ξ monotone, so the trailing sibling's Ξ must rise again: an Even re-climb at a Ξ-level
      selector. This is the Lead's «Even re-climbs at first-segment selectors», now derived.

## 2. DATA (experiments/new/box110/: resets.py, resets2.py, runres.sh)
- Pins (RT = transitions with a reset; RTRANK / TDRANK = rank-bit resets only, i.e. path-set resets, without the length thresholds):

| pin | n | WCT | RT | RTRANK | TDRANK | TD (all bits) |
| --- | --- | --- | --- | --- | --- | --- |
| hd_H40 (L-RED R159, depth 40) | 122 | 40 | 0 | 0 | 0 | 0 |
| u23sw64_n32 | 32 | 5 | 2 | 0 | 0 | 31 |
| hit_b6a_1 (depth 3) | 32 | 38 | 34 | 33 | 224 | 540 |
| x31_rx48 | 48 | 47 | 46 | 46 | 701 | 1,532 |
| runfam_K40 | 79 | 171 | 142 | 110 | 525 | 4,903 |
| sbq2_K8_m16 (quadratic, L-SI box 54) | 261 | 152 | 151 | 151 | 8,873 | 17,819 |
| obs_K12_m24 | 272 | 324 | 324 | — | — | 55,090 |
| src2_K3 | 285 | 324 | 324 | — | — | 68,331 |

- Corpus (1,132 runs):
  - WCT 13,949, RT 12,985, ROOTRES 12,985;
  - TD 520,674 (sbcg 341,879 + alt 178,795);
  - VIOL 0, VB 0; 541 runs have no reset at all.
- READING.
  - Depth without width is free: hd_H40 is a pure bottom-up fix with no reset, |F| = H.
  - Every family with |F| ≫ n has a path-set reset at almost every transition.
  - A proof of TD-POLY must bound trade-down switches. Their count is the open core, as XI-CH-POLY (R95) and NA-POLY (box 108) are.
    All three are equivalent forms.

## 3. The shape that would multiply (CONJECTURE that N5 admits it; construction hint for L-RED R160)
- By BIT-ALT, FIRST-GOOD, RESET-ROOT and NO-LAG, a product w_1 × w_2 × w_3 of widths over three levels needs ONE vertex v with:
  - pending digits p_1 above p_2 above p_3 (positions);
  - inside one hold of p_1, its p_2-bit reset and re-fixed w_2 times;
  - inside each of those p_2-holds, its p_3-bit reset and re-fixed w_3 times.
- Each reset is born at a trade-down switch on v's play, enabled by a fresh strict Ξ-overtake. So the switching vertex must be
  RE-ARMED w_2·w_3 times: its trailing sibling's Ξ must rise past the current target's again after each switch.
- So the product lives in the Ξ-dynamics of a few Even selectors whose Ξ-arena is re-armed by lower levels.
  - sbq2 (L-SI box 54 §5) is the two-level version: a W-round re-arms m prefix events.
  - A third level needs the re-arming itself to be a product.
- Why no proof (READING). Ξ is monotone, but a re-arm needs only a Ξ-rise at the trailing sibling, and that rise can be inherited
  (COPY on the Ξ side, ODD-RELAY) from any lower change. Nothing proved bounds how often lower changes reach the same selector's two
  siblings alternately. That is the selector re-climb count of k-SOURCE (R155 / R156), unbounded in the lemmas we have.
- CONJECTURE RESET-NEST: N5 admits W-runs where resets nest three levels deep, so that TD grows faster than n³ with |F| ≫ n². I do
  not have it; it is a target for L-RED R160.
- The opposite CONJECTURE, TD-POLY, is the WIDTH lemma in its exact form. Both are open.

## DONE / FINDINGS / NEEDS
- DONE: this note (ERRATUM to box 108 included); experiments/new/box110/:
  - resets.py, resets2.py, runres.sh;
  - res_sbcg.txt, res_alt.txt, res_pins.txt, res2_pins.txt;
  - read-only copies hd_H40.pg / .start (L-RED 599f9571) and sbq2_K8_m16.pg / .start (L-SI 38fc41c6);
  - pins in experiments/new/check.sh «box 110 WIDTH».
- FINDINGS:
  - PROVED (lane): BIT-ALT, FIRST-GOOD, RESET-RED (|F| ≤ T1 + n(3n + 1) + TD; an equivalence), COPY, RESET-ROOT, NO-LAG.
  - ERRATUM: box 108's «no reset at a fixed vertex» is false.
  - DATA: hd_H40 has no resets (depth free). Resets sit at 93 % of corpus W-changing transitions and at ~every transition of the
    long families. RESET-ROOT holds 12,985 / 12,985.
  - NOT PROVED: TD-POLY (= WIDTH). The multiplying shape (§3) is a re-armed trade-down selector.
- NEEDS: Lead: route §3 to L-RED R160 (resets nesting three levels = Ξ-side re-arming of a trade-down selector, w_2 × w_3 times per
  hold). resets2.py measures TDRANK.
