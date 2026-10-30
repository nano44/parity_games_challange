# R127: mkr in ONE W-world (mkrw.py). The whole run is a single guided stretch and a single W-run (no fallback, τ constant, λ_W constant), of Θ(n²) transitions. With re-blockable late adopters, R* = K·m = Θ(n²) in that one W-run: 576 at n = 554 (corpus max 17). The growth is BREADTH, not depth: each edge is late-adopted K times, each re-block paid by one W-rise of a pivot. DATA (two counters, two engines, Oink) + READING; no conjecture killed
L-RED successor 31 (Opus 5.5; D1/D18). Lead 2026-10-30 00:23Z: "a guided stretch with no boundaries (no Even fallback, no τ-change) in
which a W-rise of c₁ forces a late adoption into c₁, which forces a W-rise of c₂, and so on. Build a family where this chain depth, or R*
itself, grows with n ... Corpus max R* is 17 (so_j19_n48); hntop gives R* = 0 ... If the shape is impossible, state the exact
obstruction." Written 2026-10-30 from 00:32Z (date -u). Labels: DATA / READING / OPEN. Not a TARGET.md claim; G-N5-TIME OPEN.

## 1. Why mkr-type clocks had R* = 0, and the fix (DATA)
- On mkr (R106), frozen.py --wrun (L-NEW box 64, read only at l-new 78e1fd24) cuts at EVERY transition: lw = 76 of 76 at K 4,
  m 16. Every W-run has length 0, so R* = 0. Cause: the W-gating uses Odd self-loops (W-cycles). Every pivot step and every reactor
  hop moves a W-play to another loop, which changes λ_W at that vertex. The same holds on spanobs, carryobs and bidir (lw cuts =
  iterations).
- mkrw.py (sha1 2d7ea520e47d; mkr.py with the loop edit below, plus the LATE=1 devices of §2): each loop vertex (C1, Cp0, T_i, Tp_i) gets, instead of its self-edge, an edge to
  a marker vertex MW (Odd, single successor z). MW carries an EVEN priority above M, in mkr's loop goodness order (L′_0 < L_1 < T′_1 <
  T_1 < …). Every W-play then ends at z, the W-cycle node is z everywhere, and mkr's W-ladder becomes a path-set ladder.
- Result: the run is unchanged: 21 / 76 / 162 / 280 / 612 iterations = mkr's at (K, m) = (3, 4), (4, 16), (6, 24), (8, 32), (12, 48).
  It is ONE τ-stretch and ONE W-run (frozen.py: lw 0, fb 0, sbar 0, lx 0), 0 τ-changes. R* = 2K: the pivot steps are late adoptions
  (8 / 12 / 16 at K 4 / 6 / 8).

## 2. Late adopters (DATA; mkrw.py with LATE=1)
- Per reactor J ≥ 2:
  - v_J (Even, start on d_J) -> {d_J, c_J};
  - d_J -> th_J (even marker θ_J, small) -> h′;
  - c_J (Odd) -> {r_J (honest), yh_J (τ)}, yh_J an odd marker ω above the a-markers, -> h.
- One cycle of v_J:
  - after h's step, W(c_J) = ω ⊕ W(h) ▷ θ_J ⊕ W(h′) = W(d_J), while Ξ(c_J) = Ξ(r_J) (still V-level) ◁ Ξ(d_J): BLOCKED;
  - when the wave reaches r_J, Ξ(c_J) rises over Ξ(d_J) (the honest choice moves to yh_J): late ADOPTION;
  - at h′'s step, Ξ(d_J) and W(d_J) overtake again: v_J leaves.
- τ(c_J) = yh_J is Odd-optimal (ω makes the h-route worse for Even than r_J's best reply), so τ never changes.
  | K | m | n | iterations | W-runs | R* (frozen.py) | R* (latec.py) | late adoptions (latepair / latec) | max per (W-run, edge) | LATE-W viol |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | 4 | 16 | 186 | 76 | 1 | 64 | 64 | 65 / 65 | 4 | 0 |
  | 6 | 24 | 278 | 162 | 1 | 144 | not run | not run | not run | not run |
  | 8 | 32 | 370 | 280 | 1 | 256 | 256 | 257 / 257 | 8 | 0 |
  | 12 | 48 | 554 | 612 | 1 | 576 | not run | not run | not run | not run |
- Fit: R* = K·m exactly; with m = 4K, R* = 4K², n = 46K + 2, so R* ≈ n²/530.
- frozen.py FWR-viol 0 on every row. latec.py (sha1 727b17ce39db) is my own counter on the n5b SPEC trace and n5b's valuations, written
  from R88's definition of BLOCKED, not from L-NEW's code. It agrees with frozen.py and latepair.py on every number it ran. Control:
  plain mkr gives cuts 76, R* 0.
- L-SI cutsx.py at 94bb55db (FR=1) on latew_K8_m32: 0 cuts, 930 re-entries, ALL WPAID; FRESH 0, so box 40's LATE = 0 (no boundaries).
  The R89 late adoptions are not box 40 LATE re-entries.
- Pin experiments/red/span/instances/latew_K8_m32.pg (sha1 3498a23df6a22fc1abb694f9af296d71eb6c1c7b), .start
  (89195cae663db29bf10da0c89708ee1357bcd3a0). vrun_latew_K8_m32.txt: n5b SPEC 280 iterations, 0 fallbacks; n5.py 280, 0; state
  sequences identical (xeng.py); both solutions Oink zlk OK, strategies verified. check.sh gate: latec on K 4 (R* 64).

## 3. READING: what the family does and does not show
- Shown:
  - R* is not O(1) and not O(n). One guided stretch with Λ_Q = 0 and no boundary carries R* = Θ(n²).
  - A single W-run can be Θ(n²) long (612 W-changing transitions at n 554). The corpus maximum was about 2n (runfam_K40: 159 at n 79).
  - L-SI's Lemma WV-R then reads WCH_Q(w) ≤ (n − 1)(R* + 1) = O(n³) here. That is polynomial; nothing is killed.
- The shape: BREADTH × RE-BLOCKS, depth 2.
  - Each pivot W-rise (itself one late adoption) re-blocks the m edges (v_J, c_J) at once: W(c_J) = ω ⊕ W(h) rises with h.
  - The Ξ-wave then releases them one per transition.
  - Per edge: K late adoptions in one piece, which is exactly L-NEW's LATE-PIECE bound 1 + WCH_Q(c) (WCH(c_J) = K, CL 0).
  - No late adoption causes a W-rise that causes a further late adoption. An adoption by v_J raises only W(v_J), and v_J has no
    in-edges.
- Obstruction to DEPTH in this design class (READING, not a proof):
  - For a late adoption of (v, c₂) to be CAUSED by an earlier adoption into c₁, c₂'s W-play must pass through v (so that v's adoption
    raises W(c₂)). c₂'s honest play must avoid v, or be Ξ-lower than the alternative until the wave arrives.
  - In mkrw the only Ξ-onsets come from the reactor wave. A depth-k chain is then a chain of readers c_(i+1) ∋ v_i, and each level is a
    re-block paid by a W-rise of the level below (LATE-W).
  - Per piece: LATE(v_(i+1), c_(i+1)) ≤ 1 + WCH(c_(i+1)) + CL, and WCH(c_(i+1)) ≤ the late adoptions (switches) of v_i inside Q, plus
    the changes of the rest of c_(i+1)'s W-play. So counts do not multiply down a reader chain. They are bounded by the switches of
    the level below. Depth adds, it does not amplify, unless one adoption re-blocks MANY edges at once. That is breadth again, and it
    is paid by the number of edges.
- So in this class R* ≤ Σ_edges (1 + WCH_Q(c) + CL) with WCH_Q(c) ≤ the source rises seen by c. A super-polynomial R* needs a
  super-polynomial number of W-rises of some vertex in one guided stretch. By WV-R that is circular (WCH ≤ (n − 1)(R* + 1)). The two
  bounds give no contraction, and no family closes the loop. OPEN.
- Note: R* ≤ |Q| ≤ the λ-run (one transition per adoption). So a super-quadratic R* again needs a super-quadratic stretch (R124 §2,
  R125 §3).

## 4. Second priority (τ-changes per phase, the Odd half): not started.

## DONE / FINDINGS / NEEDS
- DONE: span/mkrw.py (one-world mkr, LATE=1 late adopters), span/latec.py (second counter), pin latew_K8_m32 + vrun (two engines,
  Oink), check.sh gate, this note.
- FINDINGS:
  1. DATA: mkr's W-runs have length 0 (λ_W changes at every hop); in one W-world (mkrw) the whole Θ(n²) run is one W-run.
  2. DATA: R* = K·m in one guided stretch (576 at n 554; 256 at n 370, three counters agree); per edge K = LATE-PIECE's bound.
  3. READING: the growth is breadth (one W-rise re-blocks m edges), not depth. Depth adds along a reader chain. A super-polynomial R*
     needs super-polynomial W-rises in one stretch (circular with WV-R); OPEN.
- NEEDS: none from the owner.
