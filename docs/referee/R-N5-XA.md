# Referee report R-N5-XA: coarse valuation, fallbacks and re-entries in throttled stretches of N5 on 𝒞^1O (box 27)

Referee: REFEREE (successor 4), Opus 5.5 (owner ruling D15, Lead reading L37). Packet P-N5-XA: the Lead's message of 2026-10-24 15:22Z.
Pin: trunk claude/vibrant-johnson-nxvvxo b70aa59 (merged here; b70aa59 is an ancestor of my HEAD). Object: docs/new/P-N5-XA-box27.md,
sha1 832d0da2b45bcc0850929b0f614bb1d9b19ed7b3 (verified at the pin and in the working tree). L-NEW successor 9.
Context read: SPEC S1-S5 (docs/new/N5-ssi-global.md); RESULTS R15, R17, R18; docs/new/N5-phase-bound-box10.md §1-§3; box 21 §2.2, §2.5;
my R-N5-RE (Lemma G, PIECE, P-1/P-2) and its §C; experiments/new/box25/coarsecheck.py, fbedges.py, fbfcheck.py (read-only).
docs/referee-2/ was NOT read for this packet. Written 2026-10-24 15:23Z-15:28Z by date -u (start from the notification read at 15:21Z;
end stamp taken before the push). Every verdict is labelled (Opus 5.5, D15).
Notation as in the packet: S a throttled stretch (one joint λ-phase; τ, θ, w constant; θ ◁ w; (h) at every state; fallbacks allowed);
c the common cycle node; u* the top of P(θ) Δ P(w) (or none); V* the vertices more relevant than u*; COARSE, ⪯ the coarse order.

## Verdict
| item | verdict (Opus 5.5, D15) |
|---|---|
| §1 setting (λ_W constant on S, u* ∉ routes, (Cmono), (Cstrict), (V1c), (V2c)) | checked, correct |
| (1) Lemma C | SIGNED |
| (2) Lemma FBL | SIGNED WITH GAPS: XA-1 (step 2, F → R: the sub-claim "there are none" is not proved; the statement survives, and for u* ≠ none the sub-claim is true by a different argument, §3) |
| (3) Lemma FBF | SIGNED WITH GAPS: XA-2 (step 1 rests on XA-1's sub-claim; replaced by a one-line argument from S4c's best-key choice that covers every case, §4) |
| (4) Lemma P^c / Lemma CR | SIGNED WITH GAPS: XA-3 (B1 "x on c′'s cycle" lists (α), (β) and omits "P(π) = ∅, c′ even, shorter", inherited from R17 (R-N5-1P G2, R-N5-1OA B7); conclusion unaffected), XA-4 (Odd vertices in Case A: notation, one line) |
| (5) Theorem XA and its count | SIGNED (no data: 0 re-entries in throttled stretches in all samples, the lane's and mine) |
| (6) Corollary (READING) | not signed (READING). One gap XA-5: flat fallbacks are PIECE separators, and R15 (d) does not bound them independently of the value-changing count (§7) |
No step is WRONG in a way that breaks a statement.

## 1. Setting (§1 of the packet): checked
- λ_W constant on S: on F_k, W = Ξ (Lemma G (a)); on R_k both cycle nodes are c (Lemma G (b)). So λ_W = λ_Ξ at every state of S, and λ_Ξ is
  constant in the joint phase. Correct.
- u*: θ ◁ w with the same c and P(θ) ≠ P(w) is decided at u*, so w is the better side there. o is in both path sets or in neither (it starts
  both plays). u* ∈ P(θ) ∪ P(w) lies on o's honest play or on o's W-play at EVERY state of S (θ, w constant as values, so the sets are fixed),
  and both plays avoid R_k \ {o} (R-N5-RE §1 (b)); u* ≠ o. So u* lies on no route, at every state. Correct.
- (Cmono)/(Cstrict): if the full comparison is decided by the cycle node, COARSE sees it; if by the top t of the symmetric difference, t ∈ V*
  makes it the top of the restricted difference, and t ∉ V* puts the whole difference outside V* (a coarse tie); a length decision is a coarse tie.
  (V1c)/(V2c): prefixing adds x on both sides or neither. Correct.

## 2. Lemma C: SIGNED (Opus 5.5, D15)
F_k: Lemma G (a). R_k: Lemma G (b); A_v is disjoint from P(θ) ∪ P(w) (u* and the plays avoid routes), and P(θ), P(w) agree above u* by the
definition of u*. Monotonicity: R15 (a) holds at every N5 transition (S4a and S4c alike) and (Cmono). Note: this makes COARSE(W) non-decreasing
on S even at fallbacks, where W itself can fall (box 21 Lemma W); the lemma claims only the coarse form. Correct.

## 3. Lemma FBL: SIGNED WITH GAPS (Opus 5.5, D15)
Step 1: τ constant on S forces Even's fallback, and S4a returned σ_k, a pointwise arena optimum in G_τ (R18 (d) Lemma S (c)). The flat-case
analysis (R18 (c), box 24 §3 Step 2 (b)) then makes every W-improving gate edge flat. Correct.
Step 2:
- R → R: none (Lemma G (c), λ(x) = c ≠ x on R). Correct.
- F → F: Lemma G (a), so flat. R → F: leaves. Correct.
- F → R, XA-1. The argument shows correctly that such a gate edge has x = c. It then says "the fallback would switch c into R", violating (h)
  at k+1. But S4c switches c to its BEST gate edge by (Ξ-key, index), which can be a flat F → F edge (another z′ ∈ F with λ(z′) = c, of longer
  Ξ-length). Then the edge (c, z) stays an unswitched gate edge into R, and the sub-claim "So there are none" is not proved.
  - The STATEMENT of FBL (about switched edges) survives: a switched F → R edge must start at c and would break (h) at k+1, as the packet says.
  - For u* ≠ none the sub-claim is TRUE, by a different argument (the referee's): (c, z) W-improving and the fallback firing force it flat,
    i.e. D = A_z ∪ P(w) = ∅ (D as in R17 B2 for the cycle c, z, π_z, o, K). So P(w) = ∅, and θ ◁ w with u* ≠ none makes the top of P(θ) odd.
    Then Ξ_k(z) = (c, P(θ), ·) ◁ (c, ∅, ·) = Ξ_k(σ_k(c)): not a gate edge.
  - For u* = none (P(θ) = P(w), θ ◁ w by length, c odd) the configuration is not excluded by anything in the packet. DATA: 0 F → R gate edges
    at 41 throttled fallbacks (all with u* ≠ none); throttled stretches with u* = none occur (12 in my samples, rttf48) but had no fallback,
    so this case is untested.

## 4. Lemma FBF: SIGNED WITH GAPS (Opus 5.5, D15)
- XA-2: step 1 claims that at L no gate edge enters R from F_L. By XA-1 that is proved only for u* ≠ none. REPAIR (the referee's; covers every
  case, and replaces step 1): after the fallback at L, every Even y satisfies
      Ξ_L(σ_{L+1}(y)) ⊵ Ξ_L(z) for EVERY successor z of y.
  If y had no gate edge, σ_{L+1}(y) = σ_L(y) and no successor improves on it. If y had one, S4c switched y to z* of maximal Ξ_L-key among its
  gate edges, so Ξ_L(z*) ⊵ Ξ_L(z) for gate edges z, and Ξ_L(z) ⊴ Ξ_L(σ_L(y)) ◁ Ξ_L(z*) for the others.
  The induction of step 2 then runs from L+1 with σ_{L+1} in place of σ_L: Ξ_t(σ_t(y)) ⊵ Ξ_{L+1}(σ_{L+1}(y)) ⊵ Ξ_L(σ_{L+1}(y)) ⊵ Ξ_L(z) = Ξ_t(z)
  for z ∈ R_t (the successor value of y never falls: unchanged successors by R15 (a), switches along gate edges). The base (the transition
  L → L+1 itself) is FBL's statement, which holds. CLOSED by this text.
- The rest of step 2 checked: Ξ_t(v) = Ξ_L(v) on R_t (same path, same θ, Lemma G (b) under (h) at t); the "largest switched index" argument for
  unchanged paths; o and forced Odd vertices never switch (τ constant). Correct.
- DATA: 0 entries and 0 route changes in 151 post-fallback states (my probe) / 141 post-fallback transitions (lane), after 41 throttled
  fallbacks.

## 5. Lemma P^c and Lemma CR: SIGNED WITH GAPS (Opus 5.5, D15)
Checked case by case against R17 §2:
- Base: Ω_{k_0}(u) = (u, ∅, 0) at a W-cycle node. Correct.
- A_c / A1: transitivity in the coarse preorder, (V2c) with r′ and σ_k(x)'s path avoiding x, (V1c), then Lemma C (valid at fallbacks too).
  A2: as R17. Correct.
- XA-4: for an Odd vertex x (forced, or o with τ fixed) the only z is x's successor, so Case A_c holds with equality; the text writes σ_k(x)
  throughout. One line.
- B_c: (Cstrict) on coarse Ξ = coarse W gives a gate edge that is W-improving, so x is Even.
- B-arena: τ constant makes σ_{k+1} the S4a optimum against τ, so (F1) in G_τ applies to σ̂. B1 (x off π, off c′'s cycle), (α), (β), B2:
  R17's analysis verbatim, with "phase ends" replaced by "λ_W changes", contradicting §1. Correct.
  - XA-3 (inherited): in "B1, x on c′'s cycle", W-improvement also allows P(π) = ∅, c′ even and |π| + 1 shorter than x's length. Then val_σ̂(x) =
    (c′, ∅, |π| + 1) = x ⊕ Ω_k(z), as in (β), and the same chain concludes. Wording only (R-N5-1P G2, R-N5-1OA B7).
- B-fallback: the coarse-strict W-improving gate edge is not flat (flat edges are coarse ties: same cycle node x, empty path sets on both sides,
  length ignored) and not R → R; it is not F → R either, by the coarse-tie argument of §3 (any W-improving F → R gate edge at a fallback is flat).
  So x ∈ R_k, z ∈ F_k. S4c's z* is in F_k (no R → R gate edges). (V1) at k+1 (λ(x) = c ≠ x, joint phase), R15 (a) and the best-key choice, then
  (V2) with both paths avoiding x (z, z* ∈ F; F-plays avoid R_k), then COARSE. Correct. This case does not need XA-1's sub-claim.
- Lemma CR: W_t(x) = value(r_t) with r_t simple in G_τ ending at λ_t(x) = λ_{k_0}(x) (§1), then P^c at j = n − 1 and Lemma C. Correct.
- DATA: C1 (coarse Ξ = coarse W) 0 failures; coarse monotonicity at every transition, fallbacks included, 0 failures; λ_W constant 0
  failures; last coarse change ≤ n − 1 in every stretch (max 10 at n 32 and n 24/48: theta_tp32, rtt24, rttf48). Lane: coarsecheck.py
  --withfb, 0 failures on the same instances.

## 6. Theorem XA: SIGNED (Opus 5.5, D15)
- Step 1 is (F1) for the S4a arena with σ_L in it (box 21 Lemma W, = R18 (d) Lemma S (c)). Steps 2-3: Lemma G (a) at L+1, G (b) at L and E+1,
  R15 (a). Step 4: u* is in the symmetric difference (it is on no route, at L or at E+1, §1) and is its top when the coarse parts agree, and w
  wins at u*, contradicting step 3. Step 5: (Cmono) on step 3 plus "differ" gives ≻; COARSE(π^L ⊕ w) = COARSE(π^L ⊕ θ) (P(θ), P(w) agree
  on V*). Every step checked. u* ≠ none is used in step 4 only, and is needed (with u* = none the length decides and COARSE drops it).
- Count: the intervals of one x are disjoint as sets of transitions (the next leave is at ≥ E+1), each holds a strict coarse increase of x
  (coarse monotone, strict between L and E+1), and Lemma CR confines strict coarse increases to the first n − 1 transitions of S. So ≤ n − 1
  such re-entries per vertex, ≤ n(n − 1) in S. Correct.
- DATA: none. 0 re-entries inside throttled stretches in every sample (lane: crossings.py, coarsecheck.py; mine: xa_probe.py over 26,483 random
  runs and 25 named instances). The theorem rests on the proof alone; as with RE, it is a statement about a configuration not yet observed.

## 7. Corollary (READING): not signed; one gap
- Checked: entries before the first fallback (FBF, with XA-2's repair); re-entries there follow S4a leaves (L < E < first fallback), so XA
  applies (u* ≠ none); first entries ≤ n; leaves ≤ entries + n; a non-flat fallback switches a leave edge (FBL), so it contains a leave.
- XA-5: PIECE (P-N5-RE §5) assumes NO fallback inside a piece, so flat fallbacks are separators in "(n − 1)·(#crossings + #fallbacks + 1)".
  R15 (d) bounds only RUNS of consecutive value-flat transitions (≤ 4n(n − 1) each), so the number of flat fallbacks is bounded by
  4n(n − 1)·(#value-changing transitions + 1), and inserting that into PIECE's count is circular. Two ways out, neither in the text: show that
  PIECE's argument passes through value-flat fallbacks (they change no value, so Lemma P's induction does not advance but is not broken; the
  next arena step's optimum is with respect to the same values; my reading is that this works, but it is not written), or bound flat fallbacks
  in S separately. Until then the O(n³) total covers crossings and non-flat fallbacks, but not the value-changing transitions.
- Also as READING: u* = none stretches are outside XA and the corollary.

## 8. Data (DATA, not proof)
### 8.1 The lane's checks (unmodified; sha1 coarsecheck 249b75f4…, fbedges f6a7d65f…, fbfcheck 2116842f…)
fts_best16, theta_tp32, returns_rt48, returns_ph64, theta_thf16, thetare_n, i1h_fts_best16, fbh_drop9 (+.start), fbh_thr (+.start):
C1/C2 0 failures (max last coarse change 10, theta_tp32); FBL 38 throttled (h)-fallbacks, every switched edge D2 (a leave; 0 FLATF, 0 OTHER);
FBF 0 failures. Random (seeds 2701-2706, 4,000 each, half --randstart): 5 throttled stretches in 8,000 coarse runs, 0 throttled fallbacks in
16,000 FBL/FBF runs, so the random samples are VACUOUS for FBL, FBF and XA; the evidence is the named instances.
### 8.2 Referee's probe docs/referee/scratch/xa_probe.py (n5x.step read-only; throttled stretches defined as in the packet, fallbacks inside)
Named: the instances above plus thetare_min, rtt16, rtt24, rttf48, sc32, tr12_s3, tr20_s4, wd12_s1, wd16_s2, xc16, xc24, xcf20, wdrop_cyc,
wdrop_canon, zfrozen_thr, R2's nc_fail_n12. Random: 𝒞^1O 6,000 seed 2711, 6,000 seed 2712 --randstart; a biased "top odd" generator (one Even
vertex with the top odd priority, aimed at u* = none) 8,000 seed 2713, 8,000 seed 2714 --randstart.
- Stretches: 32 with u* (max length 56, returns_ph64), 12 with u* = none (rttf48 length 10; others length ≤ 2).
- C1, coarse monotonicity, λ_W constant, CR: 0 failures; max last coarse change 10.
- Fallbacks inside stretches: 41, all u* ≠ none; F → R gate edges at them: 0; switched edges neither leave nor flat: 0.
- FBF: 151 post-fallback states, 0 entries, 0 route changes.
- XA: 0 re-entries inside stretches (nothing to check).

## 9. Gaps (for §C)
| id | item | kind | status |
|---|---|---|---|
| XA-1 | FBL step 2, F → R "none": the switch to c's best gate edge may go to F | proof step | statement survives; sub-claim proved here for u* ≠ none; open (untested) for u* = none |
| XA-2 | FBF step 1 uses XA-1's sub-claim | proof step | CLOSED here (S4c best-key repair, every case) |
| XA-3 | P^c B1 omits "c′ even, shorter" | wording (inherited) | CLOSED (same chain as (β)) |
| XA-4 | P^c Case A for Odd vertices | wording | CLOSED (one line) |
| XA-5 | Corollary: flat fallbacks as separators | READING | open for L-NEW |
Not covered (the packet says so): states without (h); u* = none in XA. G-N5-TIME stays OPEN. TARGET.md diff: lemmas about the candidate N5 on
𝒞^1O (polynomial by other means), not statements of TARGET.md §2.
