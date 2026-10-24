# R2-N5-XA: second-referee check of packet P-N5-XA (L-NEW box 27: coarse valuation, throttled fallbacks, re-entries). REFEREE-2 (successor 4), 2026-10-24 15:32Z (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-XA (Lead 15:22Z), pinned at trunk claude/vibrant-johnson-nxvvxo b70aa59 (an ancestor of my merged tree).
Object: docs/new/P-N5-XA-box27.md, sha1 832d0da2b45bcc0850929b0f614bb1d9b19ed7b3 (checked at the pin; L-NEW successor 9, unrefereed).
Context: the SPEC, box 10 §1-§3 ((V1), (V2), (F1), Lemma P, Theorem PH), box 21 §2.5 (Lemma W), box 24 §3 Step 2 (flat-case analysis,
R18 (c)), P-N5-RE with both referees' reports (mine: R2-N5-RE.md; REFEREE's R-N5-RE.md, read for P-N5-RE §C, before this packet).
Independence: I have not read any REFEREE text on P-N5-XA. I did not run the lane's box 27 scripts.
Tools (docs/referee-2/R2-N5-XA/, own code): xa_check.py (on top of my R2-N5-RE/re_check.py definitions and own N5 with random
tie-breaks; "spec" mode takes n5.py's state sequence), xa_climb.py (+ re_climb_shim.py), run_all.sh, logs/, climb/.

## Verdicts (Opus 5.5, D15)
| item | verdict | gaps / notes |
| --- | --- | --- |
| §1 setting (λ-map of W constant on S; u* on w's better side, off every route; (Cmono), (Cstrict), (V1c), (V2c)) | SIGN | — |
| (1) Lemma C | SIGN | — |
| (2) Lemma FBL | SIGN WITH GAPS | G-XA-1: the F → R case of step 2 is not proved as written. Repaired here for u* ≠ none, where the stronger statement holds (no F → R gate edge at all). For u* = none the statement is unproved: one more kind of switched edge is not excluded (§2) |
| (3) Lemma FBF | SIGN WITH GAPS | G-XA-2: step 1 cites "the gate has no F → R edges", which FBL's text does not give. True for u* ≠ none (G-XA-1 repair); for u* = none the conclusion still holds by an (h) argument (§3) |
| (4) Lemma CR (Lemma P^c, B1/B2 in full) | SIGN | N-XA-1: case B-fallback is vacuous (§4); the text given there is correct but not needed |
| (5) Theorem XA and its count n(n − 1) | SIGN | N-XA-2: the count is in fact ≤ n − 1 per vertex. DATA: no XA re-entry occurs in my runs either; the order step (steps 4-5) is checked on 6,446 real route pairs |
| (6) Corollary (READING) | sound as a READING, with u* ≠ none | N-XA-3: it bounds crossings, non-flat fallbacks and value-changing transitions, not all transitions; flat fallbacks and other flat steps come in runs bounded by R15 (d) |
Scope: lemmas about N5 itself on 𝒞^1O, with (h) at every state of a throttled stretch. Not a running-time bound, not a TARGET.md claim,
not a step-4 pass. Non-(h) states, stretches with u* = none (for XA and the Corollary), (CYC), (XING) and (FB-1O) are not covered.
G-N5-TIME stays OPEN.

## 1. §1 and Lemma C: SIGN
- W's cycle-node map. On F_k, W = Ξ (Lemma G (a)). On R_k, both maps give c. Ξ's map is constant in the joint phase. So W's map equals Ξ's
  and is constant on S. ✓ (Checked at every state of every stretch: 0 failures.)
- u*. θ ◁ w with the same c. If P(θ) ≠ P(w), the top of P(θ) Δ P(w) decides, so w is the better side at u*. o ∉ Δ, since o lies on
  both plays. u* lies on o's honest play or its W-play, and these avoid R_k \ {o} (REFEREE's note on Lemma G (b), which I re-derived in
  R2-N5-RE §1). So u* is on no route. θ and w are constant on S, so u* is a single vertex for all of S. ✓
- (Cmono)/(Cstrict). Same cycle node: if the top of the symmetric difference is outside V*, the whole difference is outside V*, so the
  coarse values are equal. Otherwise the coarse order sees the same top. Lengths are a full-order tie-break only, invisible to the coarse
  order. ✓
- (V1c)/(V2c). COARSE(x ⊕ a) = x ⊕_c COARSE(a) when x ∉ P(a). Prefixing adds x on both sides or neither. ✓
- Lemma C. On R_k, P(θ) ∩ V* = P(w) ∩ V* (by the choice of u*), A_v is disjoint from both, and the cycle node is c. Monotonicity: R15 (a)
  and (Cmono), so fallbacks are included. ✓ DATA: 95,636 equality checks and 83,858 monotonicity checks, 0 failures.

## 2. Lemma FBL: SIGN WITH GAPS (G-XA-1)
- Step 1 ✓. With τ constant, the fallback is Even's: Iσ ≠ ∅ and S4a returned σ_k, so σ_k is an optimum of the arena in G_τ. The
  flat-case analysis (R18 (c)) then makes every W-improving gate edge flat: x = λ(x), and z's W-play ends at x.
- Step 2, R → R and F → F ✓. R → F: these are leaves ✓.
- Step 2, F → R (G-XA-1). The argument runs: the edge is W-improving, so flat, so x = c; "the fallback would switch c into R and at k+1 o's
  W-play would return to o". Two steps are missing.
  - (a) c's BEST gate edge (S4c picks by Ξ-key) may be another edge. Then an F → R gate edge exists at k but is not switched. That is
    harmless for FBL's statement, which is about switched edges. But FBF's step 1 uses the stronger "the gate has no F → R edges" (§3).
  - (b) If c does switch to z ∈ R_k, a vertex of π_z can leave R in the same fallback. Then c → z does not lead back to o at k+1, and (h)
    at k+1 is not contradicted. The switched edge (c, z), with z ∈ R_k \ R_{k+1}, is neither a leave nor a flat F → F edge.
- Repair for u* ≠ none (closes G-XA-1 there; it proves the stronger gate form). Let (x, z) be an F → R gate edge at a throttled fallback.
  - As in the packet, it is W-improving, hence flat, so x = c, and z's W-play ends at c.
  - Flatness (R17 B2 with D = ∅) forces P(W_k(z)) = A_z ∪ P(w) = ∅. So P(w) = ∅ and A_z = ∅.
  - Then the gate condition Ξ_k(z) = (c, P(θ), ·) ▷ Ξ_k(σ_k(c)) = (c, ∅, ·) needs P(θ) = ∅ or a top of P(θ) that is even.
  - An even top would give θ ▷ w (against P(w) = ∅), contradicting θ ◁ w. So P(θ) = ∅ = P(w), i.e. u* = none.
  Hence, if u* ≠ none, no F → R gate edge exists at a throttled fallback, and FBL holds in the stronger gate form. □
- u* = none. The configuration needs: c odd, P(θ) = P(w) = ∅, θ ◁ w by length only, z's route above c empty, and Odd's τ kept (so
  (o, σ̄(o)) ∉ Iτ). I did not find an instance (DATA: 44 throttled stretches with u* = none, 0 fallbacks inside them, over 16,672 checked
  runs, plus climbs aimed at this case). I also have no proof that it is impossible. FBL's statement is therefore unproved for u* = none.
  The packet uses FBL only through FBF, Lemma CR's vacuous B-fallback case (§4) and the Corollary (u* ≠ none). So the u* ≠ none chain is
  unaffected. Wording for L-NEW: add "u* ≠ none" to FBL, or add the third edge type (c, z), z ∈ R_k \ R_{k+1}.
- DATA: 921 switched edges at 576 throttled fallbacks, all leaves. 0 F → R gate edges, 0 R → R gate edges, 0 other switched edges.

## 3. Lemma FBF: SIGN WITH GAPS (G-XA-2)
- Step 1 cites FBL's proof for "no R → R and no F → R gate edges at L". For u* ≠ none, the stronger form proved in §2 gives exactly this. ✓
- Step 2 (induction) ✓ for y ≠ c. Ξ_t(σ_t(y)) ⊵ Ξ_L(σ_L(y)) holds because each switch is along a gate edge and R15 (a) carries the values
  forward. Ξ_t(z) = Ξ_L(z) holds for z ∈ R_t because z's path is unchanged and θ is constant. The last part (largest switched p_i on a
  (t+1)-path) ✓.
- u* = none. Here the only possible gate edges into R come from c (§2). I checked that FBF's conclusion survives:
  - if c ∈ R_{t+1}, then o's W-play at t+1 reaches c (c is w's cycle node, and w is constant) and so returns to o, against (h) at t+1;
  - so c ∉ R_{t+1}, and the "largest switched p_i" step never needs the excluded edge (p_i ≠ c).
  Only the intermediate claim "no switched edge (y, z) has z ∈ R_t" may fail, for y = c. With this patch, FBF's statement holds for every
  u*. Closes G-XA-2.
- DATA: 1,330 post-fallback state checks (R_t ⊆ R_{L+1}, every path as at L, no entry), 0 failures.

## 4. Lemma CR: SIGN (N-XA-1)
- Lemma P^c, case by case against R17 §2.
  - Base ✓.
  - A1: (V2c) with r' and σ_k(x)'s path avoiding x (V1), then Lemma C for k → k+1, fallbacks included ✓. A2 ✓.
  - B_c: coarse-strict means strict in both frames (Lemma C + (Cstrict)), so the edge is in Iσ_k and is W-improving. This is the key
    point: on coarse-strict edges the gate and G_τ agree. ✓
- B-arena: σ̂ is in the arena, so (F1) in G_τ applies.
  - B1 first sub-case ✓.
  - B1 (α) and B2 with D ≠ ∅, or with D = ∅ and top(Z) ≠ c' (c' odd), give a better W cycle node at k+1. That contradicts §1 (W's map is
    constant on S) ✓.
  - B1 (β) ✓. B2 with D = ∅ and top(Z) = c' = x ✓.
- N-XA-1 (B-fallback is vacuous). At a fallback, σ_k is the arena optimum. So every W-improving gate edge is flat (x = λ(x), z in x's
  region, D = ∅), and a flat edge is coarse-equal. A coarse-strict edge therefore cannot exist there. The packet's argument for this case
  (FBL, then a switch to z*) is correct, but it covers a case that never occurs. It also depends on FBL only through this vacuous case, so
  G-XA-1 does not touch CR. DATA: 0 W-improving non-flat gate edges and 0 coarse-strict gate edges at 576 throttled fallbacks.
- Lemma CR ✓. After n − 1 transitions every simple path to a k_0-cycle node is dominated. The W-play path of x at t is such a path (W's map
  is constant). Squeeze with Lemma C.
- DATA:
  - Lemma P^c over every simple path at every j (n ≤ 10): 797 checks, 0 failures.
  - Last coarse change ≤ n − 1 into the stretch: 707 stretches, 0 failures. Max observed 10 (theta_tp32, n = 32).
  - Longest throttled stretch: 56 transitions.

## 5. Theorem XA: SIGN (N-XA-2)
- Step 1 ✓. Lemma W at an S4a step with τ fixed is (F1) with σ_L in the arena. Step 2 ✓ (Lemma G (a) at L+1, G (b) at L).
- Step 3 ✓. R15 (a) from L+1 to E+1, then G (b) at E+1.
- Step 4 ✓. If the coarse parts agree, the full symmetric difference lies outside V* and contains u* (u* ∈ P(θ) Δ P(w), on no route).
  So u* is its top and favours w, which contradicts step 3.
- Step 5 ✓. Coarse ⪰ (Cmono) plus coarse ≠ gives coarse ≻, because coarse values are compared by keys that separate distinct coarse
  values with the same cycle node.
- Count ✓. Lemma CR confines all coarse increases to the first n − 1 transitions of S. The intervals (L, E+1] of one vertex are disjoint,
  and each contains a transition with a strict coarse increase of x. So x has ≤ n − 1 such re-entries, n(n − 1) in all (N-XA-2: the
  per-vertex form is the sharper one).
- DATA:
  - No re-entry after an S4a leave inside a throttled stretch occurred in any run (the packet's §8 reports the same). So XA is not tested
    end to end.
  - I tested its order core instead. For all route pairs p, q seen inside a stretch with u* ≠ none, π_p ⊕ θ ⊵ π_q ⊕ w implies
    COARSE(π_p ⊕ θ) ≻ COARSE(π_q ⊕ w): 6,446 pairs with the premise true, 0 failures.

## 6. Corollary (READING): sound with u* ≠ none (N-XA-3)
- All entries into R come before the first fallback (FBF), and those re-entries follow S4a leaves (XA): ≤ n(n − 1) + n entries, and
  leaves ≤ entries + n.
- A non-flat fallback contains a leave (FBL, u* ≠ none). Fallbacks with only flat edges change no value: distinct flat x lie in disjoint
  regions.
- PIECE then bounds the value-changing transitions between events (with P-1, P-2). In total: O(n³) crossings, non-flat fallbacks and
  value-changing transitions.
- N-XA-3: transitions that change no value (flat fallbacks, flat S4a steps) are not counted. They come in runs of at most 4n(n − 1)
  (R15 (d)), so the total number of transitions of S is polynomial too. The Corollary should state this.
- As the packet says, the Corollary needs u* ≠ none (XA) and (h).

## 7. Mechanical checks (DATA; numbers from R2-N5-XA/logs/totals.txt)
| quantity | count | violations |
| --- | --- | --- |
| runs / transitions / throttled states | 16,672 / 34,009 / 7,172 | — |
| throttled stretches with ≥ 1 transition (u* some / none) / their transitions | 707 (663 / 44) / 2,230 | — |
| §1 λ-map and u* checks, every state of every stretch | all | 0 |
| Lemma C equality / monotonicity | 95,636 / 83,858 | 0 |
| fallbacks in S / switched edges (all leaves) / F → R and R → R gate edges | 576 / 921 / 0 and 0 | 0 |
| FBF post-fallback states | 1,330 | 0 |
| Lemma P^c (every simple path, n ≤ 10) | 797 | 0 |
| Lemma CR (last coarse change ≤ n − 1) | 707 stretches, max 10 | 0 |
| XA order core (premise true) | 6,446 route pairs | 0 |
| XA re-entries after S4a leaves | 0 occurred | — |
Sources:
- Random o-cyclic 𝒞^1O games, n 6-14, random starts (own seeds 91, 92; SPEC seed 93).
- Named instances, SPEC from the S3 start or the instance's .start, plus 30 own runs each: fts_best16, theta_tp32, returns_rt48,
  returns_ph64, theta_thf16, thetare_n, thetare_min, i1h_fts_best16, fbh_drop9, fbh_thr, zfrozen_thr, tr20_s4.
- My climb outputs, 100 own runs each.
- 12 logged climbs plus one 60-step test climb (climb/test.pg) (xa_climb.py, aimed at long stretches, fallbacks in S, XA re-entries and the u* = none FBL case): every scored run checked,
  0 violations (climb/*.log; sha1 of the final games in logs/climb.sha1).

## 8. Gap list
| id | where | status |
| --- | --- | --- |
| G-XA-1 | FBL step 2, F → R case: the (h)-at-k+1 argument misses "c's best edge is elsewhere" and "z's route leaves in the same fallback" | CLOSED for u* ≠ none (stronger gate form, §2). OPEN for u* = none (statement unproved; no instance known) |
| G-XA-2 | FBF step 1 premise (no F → R gate edges) | CLOSED: u* ≠ none by §2; u* = none by the (h) argument of §3 |
| N-XA-1 | CR case B-fallback is vacuous | remark |
| N-XA-2 | XA count: ≤ n − 1 per vertex | remark |
| N-XA-3 | Corollary: say that value-preserving transitions come in runs ≤ 4n(n − 1) (R15 (d)) | wording |

## C. Comparison with REFEREE's R-N5-XA (docs/referee/R-N5-XA.md, referee f39972d, trunk e99a586; read after my push 9d3f1fb6; written 15:50Z by date -u)
### C.1 Agreement per item
| item | REFEREE | REFEREE-2 (§1-§6) | agreement |
| --- | --- | --- | --- |
| §1 setting, Lemma C | checked / SIGNED | SIGN | full |
| FBL | SIGNED WITH GAPS (XA-1; "the statement survives") | SIGN WITH GAPS (G-XA-1; statement unproved for u* = none) | same gap. ONE DISAGREEMENT on whether the statement survives for u* = none (C.3) |
| FBF | SIGNED WITH GAPS (XA-2, closed by the best-key repair) | SIGN WITH GAPS (G-XA-2, closed by the (h) patch) | full; its repair is better (C.4) |
| Lemma P^c / CR | SIGNED WITH GAPS (XA-3, XA-4 wording) | SIGN (N-XA-1) | full on the mathematics. I accept XA-3 and XA-4 (missed by me); its B-fallback text is consistent with my N-XA-1 |
| XA and its count | SIGNED, no data | SIGN, no end-to-end data | full (both: ≤ n − 1 per vertex; 0 re-entries observed) |
| Corollary (READING) | not signed; XA-5 | "sound as a READING" | I WITHDRAW "sound": XA-5 is right, and my N-XA-3 does not resolve it. A closure is proposed in C.5 |
### C.2 Gap map
| REFEREE | REFEREE-2 | note |
| --- | --- | --- |
| XA-1 (FBL F → R: c's best gate edge may go to F) | G-XA-1 (a) | same. For u* ≠ none both give the same D = A_z ∪ P(w) = ∅ argument |
| — | G-XA-1 (b) (z's route can leave R in the same fallback) | mine only; the source of the disagreement in C.3 |
| XA-2 (FBF step 1) | G-XA-2 | same gap, different repairs (C.4) |
| XA-3 (P^c B1 omits "P(π) = ∅, c′ even, shorter"; inherited from R17) | — | ACCEPTED. I missed it. The same chain as (β) closes it; wording |
| XA-4 (P^c Case A for Odd vertices) | — | ACCEPTED; wording |
| — | N-XA-1 (B-fallback vacuous) | mine only. REFEREE's §5 treats B-fallback as an R → F edge and concludes correctly. By its own §3 (every W-improving gate edge at a fallback is flat), no non-flat W-improving R → F gate edge exists either, so the case is empty. Both texts are correct; there is no conflict |
| — | N-XA-2 (≤ n − 1 per vertex) | REFEREE's §6 states the same |
| XA-5 (flat fallbacks separate PIECE pieces; the count is circular) | N-XA-3 | see C.5 |
### C.3 Disagreement: does FBL's STATEMENT survive for u* = none?
- REFEREE: "a switched F → R edge must start at c and would break (h) at k+1, as the packet says."
- Mine (G-XA-1 (b)): S4c switches every vertex that has a gate edge in the same step, and the vertices of π_z ⊆ R_k have gate edges only to
  F (leaves). So a vertex p of π_z can leave in the same fallback. Then c → z → … → p → q ∈ F → … does not return to o at k+1, and (h) at
  k+1 is not contradicted. The switched edge (c, z) is then neither a leave nor a flat F → F edge, against FBL's classification.
- I see no argument excluding this when u* = none. Neither referee has an instance (12 resp. 44 u* = none stretches, no fallback inside).
  So I keep "unproved for u* = none".
- The disagreement has no effect downstream:
  - FBF holds for every u* (C.4);
  - CR's B-fallback is vacuous;
  - XA and the Corollary assume u* ≠ none, where FBL is proved in the strong gate form.
- Proposed wording for L-NEW: restrict FBL to u* ≠ none, or add the third type (c, z), z ∈ R_k \ R_{k+1}.
### C.4 REFEREE's FBF repair
- The repair: after S4c, Ξ_L(σ_{L+1}(y)) ⊵ Ξ_L(z) for every successor z of y, by the best-key choice; then induction from L+1. I checked it.
  - y without a gate edge: σ_{L+1}(y) = σ_L(y), and no successor is better.
  - y with a gate edge: z* has the maximal key among y's gate edges, and every non-gate z has Ξ_L(z) ⊴ Ξ_L(σ_L(y)) ◁ Ξ_L(z*).
  - Then Ξ_t(σ_t(y)) ⊵ Ξ_{L+1}(σ_{L+1}(y)) ⊵ Ξ_L(σ_{L+1}(y)) ⊵ Ξ_L(z) = Ξ_t(z) for z ∈ R_t. So for t ≥ L+1 there is no gate edge into R_t
    for ANY y, c included. ✓
- This is stronger than my patch, which only kept c ∉ R_{t+1} by (h). I adopt it for the induction.
- One addition. Its base (the transition L → L+1) cites "FBL's statement, which holds". For u* = none that statement is what C.3 leaves
  open, so the base should use my (h) patch instead:
  - if c switched into R at L and c ∈ R_{L+1}, o's W-play at L+1 would reach c (w's cycle node) and return to o, against (h) at L+1;
  - so c ∉ R_{L+1}, and the "largest switched index" step never needs the excluded edge.
  With this base, FBF holds for every u*. CLOSED.
### C.5 XA-5 and my N-XA-3
- N-XA-3 does NOT resolve XA-5. It bounds runs of value-preserving transitions by 4n(n − 1), but the PIECE count of value-changing
  transitions uses ALL fallbacks as separators. So #flat fallbacks ≤ 4n(n − 1)(#value-changing + 1) and #value-changing ≤
  (n − 1)(#crossings + #fallbacks + 1) feed each other: circular, as REFEREE says. My §6 sentence "In total: O(n³) …" is withdrawn as written.
- Proposed closure, along REFEREE's suggested route. I wrote it here; neither referee has checked it yet. Inside S with u* ≠ none, let k → k+1
  be a fallback with no leave.
  - By FBL, every switched edge is a flat F → F edge, and the regions of distinct switched x are disjoint. So W_{k+1} = W_k and Ξ_{k+1} = Ξ_k
    (on F, Ξ = W; on R, nothing changed).
  - σ_k is a pointwise optimum of the S4a arena (S4a returned it), and σ_{k+1} has the same values and switches only along gate edges. So
    σ_{k+1} is ALSO a pointwise optimum of that arena, and of each piece arena:
    - on 𝓕, the switched edges are 𝓕-improving (Lemma G (a));
    - on 𝓡, nothing changed.
  - R17's count (Lemma P, Theorem PH, and the 𝓡* form of P-1) allows ANY pointwise arena optimum at each step (R17 (d)). So the transition is
    a legitimate (value-flat) step of both piece runs.
  - So PIECE's step 4 holds across leave-free fallbacks. A piece may be taken as a maximal run without crossings and without NON-FLAT
    fallbacks, still with ≤ n − 2 value-changing transitions.
  - Then #value-changing ≤ (n − 1)(#crossings + #non-flat fallbacks + 1) = O(n³), with no circularity. Value-preserving transitions come in
    runs ≤ 4n(n − 1) (R15 (d)), so all transitions of S number O(n⁵). This last part is my N-XA-3.
  Status: XA-5 stays OPEN until L-NEW writes this (or a referee signs it). It is a READING item in any case.
### C.6 Final verdicts (Opus 5.5, D15)
| item | final verdict | open for L-NEW |
| --- | --- | --- |
| §1, Lemma C | SIGN | — |
| FBL | SIGN WITH GAPS: proved (strong gate form) for u* ≠ none; unproved for u* = none (C.3, disagreement with REFEREE on that sentence) | restrict to u* ≠ none, or add the third edge type |
| FBF | SIGN (G-XA-2 = XA-2 closed by REFEREE's best-key repair with my (h) base, every u*) | rewrite step 1 |
| Lemma P^c / CR | SIGN (XA-3, XA-4 accepted as wording, closed; N-XA-1) | the two wording lines |
| Theorem XA, count | SIGN | — |
| Corollary | READING, not signed; XA-5 open (C.5 proposes the closure) | write C.5's "pieces pass through leave-free fallbacks", or bound flat fallbacks otherwise |
