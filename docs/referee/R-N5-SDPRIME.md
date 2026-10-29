# R-N5-SDPRIME: REFEREE report on packet P-N5-SDPRIME (L-SI box 25: Theorem STATIC-DEPTH′, its Remark, Corollary EPOCH)
Referee: REFEREE (successor 17), Opus 5.5 (owner ruling D15). FIRST referee (Lead message of 2026-10-29 04:05Z by date -u).
- Object and pin: docs/si/P-N5-SDPRIME-box25.md, sha1 54678c38a04842bd936a9bf4b241d47ad8ab90a3, 106 lines, author L-SI successor 21: the same
  sha1 at l-si edc14c51 (an ancestor of origin/claude/l-si) and at the l-si head. Quote base 55e0bcbda.
- Probe and data runs 2026-10-29T04:06Z-04:32Z; report written 04:33Z-04:34Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independence: I opened no docs/referee-2/ file on SDPRIME. At 04:33Z (same turn as the fetch) names matching "sdprime": 0 on my tree, 25 on
  origin/claude/referee-2, 18 on trunk docs/referee-2/. REFEREE-2's files exist; I listed names only and read none. No lane code run or
  imported (experiments/si/piece/sdprime.py, epochs.py, n5x, quotecheck.py untouched). D1.
- Premises read against their text at 55e0bcbda and on trunk: RESULTS R77 (l. 4178-4246: claim (c), its setting line, facts W-MONO, Ξ-SUCC,
  CV, GEN_W, H_b, d*), R80 (a) (EVERY-SWITCH, which I signed as (C1) of P-N5-CORE), R18 (d) Lemma S (a) with P2 (R69's list), (SW) (R72's
  premise list), SPEC S1 (valuation, total order), S2, S4a, S4c.
- Quotes: all 12 [Q path@commit:lines] passages verbatim in their cited ranges (own checker scratch/flip_quotes.py: QUOTES 12 FAILED 0).
- Tool: scratch/sdprime_probe.py (sha1 11d9b745…; own engine rl_engine; helpers cycles / play / H_b / d* from my predecessor's depth_probe.py;
  start parsing from core_probe.py). Logs scratch/sdp_logs/.

## Verdicts (sign-off line per item)
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §2 | Theorem STATIC-DEPTH′ under (H1′), (H2), (H3′), (H4′), GEN_W: per-vertex settling from a + dW(v) / a + dH(v); σ_t = σ_b on [a + max d, b]; b − a ≤ max d ≤ |Even ∖ T| ≤ n − 1 | SIGNED |
| §2 | (H4′)'s "Equivalently" (recursion well founded ⇔ J_b acyclic) and its parenthesis | SIGNED (checked by proof) |
| §2 | Remark: STATIC-DEPTH′ contains R77 (c) ((H1) ⇒ (H1′), (H3) ⇒ (H3′), (H4) ⇒ (H4′), d ≤ d*) | SIGNED |
| §3 | Corollary EPOCH: b − a = Σ(b_i − a_i) + (k − 1), k − 1 ≤ CF, b − a ≤ (CF + 1)n − 1 under (H4′) and GEN_W at every epoch end | SIGNED (a REDUCTION: CF unbounded) |
| §4 | data, CONJECTURE PIECE, CONJECTURE STATIC-DEPTH′-TIE | not signed. Coverage figure reproduced as a RATIO (SDP-N1) |
No gap. Notes SDP-N1..N5. Nothing here bounds CF or the number of pieces; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. STATIC-DEPTH′ re-derived, item by item (every parenthetical checked)
- Premises outside R77's landed scope (SDP-N2): W-MONO and Ξ-SUCC are landed "on in-phase S4a transitions (R77's (H1))", and (H1) includes
  λ_W constancy, which (H1′) drops. Neither needs it: W-MONO is P2 at one S4a step (σ_t is in its arena; W of an arena strategy is its W in
  G, τ fixed); Ξ-SUCC is R15 (a), (d) (Ξ non-decreasing at every iteration) with (SW) (a switch goes to an Iσ edge, strictly better). ✓
- Recursion and (H4′) ✓. dW stops on T_W, dH on T_H; Odd v follows τ (W) or σ̄ (H, constant by (H2)); Even v ∈ T_H ∖ T_W continues in W only, ∈ T_W ∖ T_H
  in H only. A cycle of the recursion avoiding Even vertices outside T would be a cycle of one frame's successor map at b outside that
  frame's end-state cycles, i.e. not a cycle of that map at b: impossible ✓. Unfolding dW(y), dH(y) stops at T of the frame or at the first
  Even vertex outside T on y's play of that frame at b: exactly J_b's edges, so well founded ⇔ J_b acyclic, and d(v) = the vertices of a
  longest J_b-path from v ✓.
- Item 1 ✓: a vertex on a cycle of a successor map has that cycle as its play; (H3′) keeps Z a cycle of its frame at every t; an Even v ∈ T is
  on a W-cycle or an honest cycle, both following σ_t at v, so σ_t(v) = σ_b(v) for all t ✓.
- Item 2 ✓: v ∉ T_W is off the cycle of its W-play at b, so τ(v)'s W-play at b does not contain v (else v would recur); the W-play of v at t is
  v followed by τ(v)'s ✓. Honest frame with σ̄ constant ✓.
- Item 3 ✓ (y = σ_b(v) = σ_t(v) for all t by item 1; then item 2's argument in the other frame).
- Item 4 (A) ✓: if σ_t(v) ≠ y and y ∉ Iσ_t(v), then Ξ_t(y) ⊴ Ξ_t(σ_t v) (total order, S1); v enters y at some t′ ∈ [t, b) (σ_b(v) = y);
  (SW) at t′, Ξ-SUCC from t to t′, and y H-settled from s ≤ t (a valuation is a function of the play) give Ξ_{t′}(y) ▷ Ξ_{t′}(y) ✓.
- (B) ✓: s′ = σ_{t+1} with v ↦ y uses only state-t arena edges ((A) at v; S4a's output elsewhere, no fallback by (H1′)); y's W-play under σ_{t+1}
  is its play at b (W-settled, t + 1 ≥ s) and avoids v, so it is y's play under s′, and W_{s′}(v) = v ⊕ W_b(y) = W_b(v) (v off its W-cycle at b);
  P2 (pointwise maximum over arena strategies) gives W_{t+1}(v) ⊵ W_b(v); W-MONO from t + 1 to b gives ⊴ ✓.
- (C) ✓: equal valuations have the same cycle node c; c lies on the W-cycle Z of b, a W-cycle at t + 1 (H3′), so v's W-play at t + 1 ends in
  Z, the same cycle as at b; GEN_W makes the plays equal; σ_{t+1}(v) = y; the honest play at t + 1 is v · (y's honest play at t + 1) = v · (y's
  honest play at b), which avoids v (v ∉ T_H) ✓.
- Item 5 ✓: σ_t = σ_b on [a + max d, b]; a transition in that range would be in-phase with σ unchanged, against R80 (a) ✓; d(v) ≤ |Even ∖ T|
  by acyclicity; T ≠ ∅ ✓; "0 if there is none" (then b = a) ✓.

## 2. The Remark (R77 (c) ⊆ STATIC-DEPTH′) re-derived
- (H1) ⇒ (H1′) ✓ (drops λ_W constancy). (H3) (W-cycles = honest cycles, constant on [a, b]) ⇒ (H3′) with T_W = T_H = R77's cycle vertices ✓.
- (H4) ⇒ (H4′) ✓: a J_b-edge follows σ_b at Even vertices and τ (W) or σ̄ (honest) at Odd ones through vertices outside T. For Odd u ∉ D
  σ̄(u) = τ(u), an H_b edge; for u ∈ D both τ(u) and σ̄(u) are H_b edges. So a J_b path is an H_b path, a J_b cycle an H_b cycle off the cycle
  vertices, excluded by (H4) ✓.
- d ≤ d* ✓: both count the Even non-cycle vertices of a path, J_b's paths being H_b's. So every R77 (c) conclusion follows ✓ (settled earlier
  implies settled later).
- Data: REM 3,878 (alt_all) + 4,538 (lib41) + 6,380 (lib1140) + 2,080 (random) R77 instances; at each, (H3′) holds from R77's start (REM_H3p) and
  max(dW, dH) ≤ d* at every vertex (REM_d): 0 failures.

## 3. Corollary EPOCH re-derived
- A piece satisfies (H1′) (fallback-free, one phase) and (H2) ✓. The epoch construction: the condition "every cycle of b_i (each frame) is one
  at every state of [x, b_i]" is monotone in x, so a_i is well defined and each epoch has (H3′) with end b_i ✓.
- b − a = Σ_i (b_i − a_i) + (k − 1) (the k − 1 gaps a_i − 1 → a_i) ✓. For i ≥ 2, minimality of a_i gives a cycle Z of b_i (some frame) that is not
  one at a_i − 1 but is one at a_i: it appears at a_i − 1 → a_i, which is a CF transition; distinct for distinct i ✓. So k − 1 ≤ CF, and with
  STATIC-DEPTH′ per epoch (b_i − a_i ≤ n − 1) b − a ≤ k(n − 1) + k − 1 = kn − 1 ≤ (CF + 1)n − 1 ✓.

## 4. Data (scratch/sdp_logs/; 0 failures in every MUT=0 run)
| corpus | runs | STATIC-DEPTH′ intervals (T_W ≠ T_H / λ_W changes) | SDV / SA / SB checks | sharp (b − a = max d) | pieces (≥ 1 transition) | EPOCH pieces with hypotheses (CF ≥ 1) |
| --- | --- | --- | --- | --- | --- | --- |
| alt_all (413 games, n ≤ 600, given start else S3) | 413 | 4,791 (905 / 153) | 2,274,195 / 1,034,304 / 927,230 | 369 | 5,765 (1,132) | 5,491 (25) |
| lib41 (n ≤ 48; given + S3 + 1 random) | 727 | 5,440 (891 / 194) | 1,111,644 / 512,411 / 433,472 | 383 | 6,892 | 6,816 (41) |
| lib1140 (fbc_lib.txt, n ≤ 40; given + S3 + 1 random) | 1,857 | 7,929 (1,518 / 234) | 1,023,704 / 451,169 / 359,507 | 359 | 15,189 | 14,947 (137) |
| random rand_ck, n 6-20, k ≤ 6 | 12,000 | 2,175 (95 / 4) | 60,449 / 20,214 / 7,794 | 152 | 34,760 | 34,670 (438) |
- The extension is exercised: 3,409 intervals with T_W ≠ T_H and 585 with λ_W changing, all with 0 failures.
- Intervals with a used-form GEN_W failure: 34 / 52 / 75 / 0; in all of them the conclusion still held (SD and SDV overruns 0): CONJECTURE
  STATIC-DEPTH′-TIE survives my data too (unsigned).
- EPOCH: max epochs 6, max CF 5 per piece (as §4: "≤ 6 epochs and CF ≤ 5"); no piece longer than n − 1 (the maximum, n − 1, occurs in lib1140):
  CONJECTURE PIECE survives my data (unsigned).

## 5. Mutation controls (scratch/sdp_logs/mut*.txt; lib41 and alt_all)
| MUT | change | result |
| --- | --- | --- |
| 1 | per-vertex settling demanded from a + d − 1 | BITES: 14,126 (lib41) (0 on a 5-instance set without sharp intervals) |
| 2 | (H3′) with the W frame only (honest cycles not required to persist) | BITES: SDV 77, SD 1, SB 1 (lib41; e.g. box25/wdrop_cyc). The honest half of (H3′) is needed |
| 3 | depth with the W frame only (d(v) := 1 + dW(σ_b v)) | BITES: SD 17, SDV 3,924, SA 1,552, SB 1,669, EP_epoch 3 (lib41). The max with dH is needed |
| 4 | CF counts W-cycle appearances only | BITES: 5 (lib41), 2 (alt_all) on k − 1 ≤ CF. Honest-cycle appearances must be counted |

## 6. Notes (for L-SI's fixes file; none changes a verdict)
- SDP-N1 (§4 coverage, not signed). On my alt_all pieces with ≥ 1 transition, STATIC-DEPTH′'s hypotheses hold on 1,098 of 1,132 (97.0 %; (H3′)
  fails 25, (H4′) 2, GEN_W(used) 7) and R77's on 918 (81.1 %). §4: 844 of 872 (96.8 %) and 708 (81.2 %). The RATIOS agree; the piece COUNTS
  differ (1,132 vs 872), cause unknown (lane code not run: piece definition, one-state pieces or starts). Counting one-state pieces too, mine
  are 5,467 of 5,765.
- SDP-N2 (premise scope). W-MONO and Ξ-SUCC are landed inside R77 (c) under (H1), which includes λ_W constancy. The packet uses them on
  (H1′) intervals where λ_W may change. Both facts hold there (§1, first bullet; one line each), so this is a citation point: say "W-MONO
  (P2 at an S4a step) and Ξ-SUCC (R15 (a), (d), (SW)) hold at every in-phase S4a transition; λ_W is not used".
- SDP-N3 (quote). [Q RESULTS@55e0bcbda:3768-3769] «(SW): every Even switch of N5 is to an edge … of Iσ»: the "…" stands only for the line
  break between l. 3768 and 3769; nothing is omitted. Cosmetic.
- SDP-N4 (GEN_W). Checked in its used form (the plays compared in step (C)); the statement's GEN_W ("different W-plays from v to the same cycle
  have different W-valuations") is a property of G and τ, and is a hypothesis. In my data the conclusion held in all 161 used-form failures.
- SDP-N5 (thin spots). EPOCH is exercised with CF ≥ 1 on few pieces (25 / 41 / 137 / 438); the bound (CF + 1)n − 1 is far from reached
  (pieces ≤ n − 1). MUT=1 bites only where the per-vertex bound is sharp (lib41), none in a small named set.

## DONE / FINDINGS / NEEDS
- DONE: R-N5-SDPRIME.md (this file), scratch/sdprime_probe.py, scratch/sdp_logs/.
- FINDINGS: STATIC-DEPTH′ (with (H4′)'s equivalence), the Remark (contains R77 (c)) and EPOCH all SIGNED, no gap; both halves of (H3′), the
  dH part of d and the honest half of CF are needed (MUT 2-4 bite); W-MONO / Ξ-SUCC are used beyond their landed (H1) scope, harmlessly
  (SDP-N2); coverage reproduced as a ratio, counts differ (SDP-N1).
- NEEDS: Lead: the SDPRIME §C word (REFEREE-2's files exist; not opened); route SDP-N1..N5 to L-SI's fixes file.
