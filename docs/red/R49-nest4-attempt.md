# R49: R48 §4 attack (box 16): can a −1 piece's rise feed a shallower −1 piece? (L-RED successor 10; produced on Opus 5.5)
Status: DATA plus a mechanism reading; NO kill and NO proof so far. Written 2026-10-21 (date -u; box 16 resumed 21:07Z after the
usage cap cut it at ~04:01Z on 2026-10-19). Target: Lead GO 2026-10-19 03:19Z and 2026-10-21 21:06Z (date -u).
Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, both order data, q-phases on 𝒞^1P. Chains come from L-ALG's
unmodified b12_pot.run / chain and b12_core.states (through experiments/red/xctx/xscore.py), NEST* from experiments/red/xctx/comb/neststar.py.
Every instance below: sha1, both orders give the same P, pinned Oink verified, Oink's q iteration count = S (experiments/red/nest16/kcheck.sh).

## 1. The question in chain terms
- For NEST*(P) ≥ 4 a phase needs positions a < b < c < d with a d-pair inside c's window, inside b's window, inside a's window (window =
  the elements deeper than p between p's first and last occurrence).
- Transition types at the first changed position b: G (same (rank, V), the piece grew) and O ((rank, V) rose).
- Mechanism seen in every NEST* 3 phase (nest3_n24 tlog, R48 §3): the −1 piece directly above the pool (the deepest stable piece)
  absorbs pool tangles one by one (a G-run, the "domino": each absorption removes an escape of the next pool tangle). When the domino
  ends, the pool learns a tangle that raises a shallower −1 piece by an O-rise. Example, nest3_n24 s5 → s7: position 5 absorbs 16,
  which removes escape 16 of {18}; the pool learns {18} at s6; {18} raises position 3 (rank 4 → 5) at s7. So a −1 piece's growth
  DOES feed a shallower −1 piece, but only through the pool.
- After an O-rise at b the chain below b is rebuilt, usually as one −1 piece plus the pool (DATA, §3). A fourth level needs two
  −1 levels below an O-rise that both re-rise before b rises again.

## 2. Construction attempts (all negative so far)
- Graded climb experiments/red/nest16/starclimb.py, score (NEST*, MASS, S, −n), MASS = Σ_p (1 + NEST*(window_p))²: 3 runs, 6000
  steps, stable and oink order, seeds nest3_n24, nest3_n20, GROW 0.05-0.08, NMAX 40-44. Plateau NEST* 3, MASS 28.
  - Near miss instances/near4_n26.pg (sha1 6d7c5e3839c0632c618d8da002ceb65f3259b77f): S 18, Oink 18 even iterations, verified;
    P = 3,0,7,7,7,7,5,6,6,4,5,5,4,0,3,3,3. With the first 4 before the 5/6 block it would be NEST* 4.
  - near4_n26 is a strict local maximum: every single-edge addition or removal (experiments/red/nest16/edgenbr.py) gives NEST* ≤ 3,
    MASS ≤ 28. Same for nest3_n24 (best (3, 25)).
- Wrapper search experiments/red/nest16/wrapsearch.py (1-3 new vertices plus edges into the base, around nest3_n24 and near4_n26,
  ~1000 trials): best NEST* 3. Reading on why a wrapper is hard: a tangle that the new top piece absorbs must have all escapes in that
  piece's region (dtl.cpp attractTangles, line 156), so it is learnable as soon as its vertices reach the pool; the outer level's
  second rise can be timed only by when those vertices reach the pool.
- Targeted edits on nest3_n24: adding an escape from the s9 tangle {8, 9, 19} into piece 3 ({12}), to move its effect from position 3
  to position 4: 8→12 and 19→12 change nothing; 9→12 collapses the phase to 4 transitions.
- Climb with FIT=seg (score (NEST*, max NEST* of the segment after an O-rise deeper than the phase's shallowest rising position,
  0, MASS, S, −n)), oink order, seeds near4_n26 (seeds 31, 41): plateau NEST* 3. It produced oseg_n26 (§3) and:
  - instances/win3_n27.pg (sha1 b5de9bbe5a75dff75bb0ecb5dfc06d3583b4b423; S 19, Oink 19 even iterations, verified, same P in both
    orders): P = 3,1,9,9,9,9,9,6,8,8,5,6,5,1,4,4,4,4. Position 1 (NOT the first piece) has a window of NEST* 3: O-rise at 1, then
    9-domino, 6, 8-domino, 5, 6, 5, then 1 rises again. Position 0 (piece {17}, rank 4) never changes in the phase. One rise at 0
    before index 1 and one after index 13 would give NEST* 4. Its single-edge neighbourhood: no NEST* 4 (best (3, 28)).
- So the open step is exactly an OUTER WRAP: a shallower level that rises once before and once after a NEST*-3 window of a non-first
  piece. Climb FIT=wrap (score (NEST*, W, MASS, S, −n); W counts a shallower rise before / after the deepest window, 2 = NEST* + 1)
  and wrapsearch on win3_n27: in progress (§4).

## 3. DATA laws (library: L-ALG's class set as in R48 §1, 956 q-phases per order)
- (G-NEXT) every G-transition at b is followed by a transition at a position ≤ b (or ends the phase): 382/382, stable and oink.
- After an O-rise, a segment with NEST* 2 (the positions deeper than b until the next transition at ≤ b) occurs only at b = 0:
  3 cases (nest3_n20, nest3_n24, near4_n26), both orders. Segment NEST* 1: 66; 0: 706.
- On the xctx instances and this box's climb outputs (stable and oink): every G with a stable piece below it sits directly above that stable piece (216/216);
  after an O-rise at b > 0 the first stable piece is at b + 2 in 44 cases, b + 3 in 8, b + 6 in 2.
- experiments/red/nest16/lawscan.py on the same library (identical counts in stable and oink order; NEST* histogram 0: 540, 1: 397,
  2: 16, 3: 3):
  - (G-NEXT): 382 G-transitions, 0 violations.
  - (G-ADJ) "a G sits directly above the first stable piece below it": 306 cases with a stable piece below, 1 violation
    (phi_flat_alive_n32 forced into 𝒞_0, phase (1, 0), transition 0: b 2, stable piece at 7).
  - (O-SEG) (definition below): 189 O-rises deeper than the shallowest rising position, 0 violations in the library. The only
    violation known is the climbed oseg_n26 below.
  - (W): 25 windows with NEST* ≥ 2, 4 violations (the first three: spp22_oink_n40 forced into 𝒞_0, near4_n26
    twice; the small run on near4_n26 + nest3_n24 also flags nest3_n24's position 3).
- FALSE laws:
  - (O-SEG) "a segment after an O-rise deeper than the shallowest rising position has NEST* ≤ 1": instances/oseg_n26.pg
    (sha1 381b7b9d70d75a9f9dba2b8f7c6111ec4814eb73; S 16, Oink 16 even iterations, verified, both orders):
    P = 3,1,6,6,6,6,4,5,5,3,4,4,3,0,3; the O-rise at 1 is followed by a NEST*-2 segment, and 0 rises later. NEST* is still 3 because
    1 never rises again.
  - (W) "a window of NEST* ≥ 2 contains no shallower transition": near4_n26 (5's window 5,6,6,4,5 contains 4).
    So NEST* windows do cross shallower transitions (contexts).

## 4. What a fourth level needs (reading; rests on the DATA law (G-NEXT), not on a proof)
- Every NEST* 3 phase seen (nest3_n20, nest3_n24, near4_n26, oseg_n26, win3_n27, w1_n27) has this shape. An O-rise at a level r; then
  a segment below r (G-dominoes at the piece directly above the pool, separated by O-rises of intermediate levels); then r, or a
  shallower level, rises again.
- NEST* ≥ 4 needs a level a < r whose first rise comes before the NEST*-3 window and whose last rise comes after it.
  - By (G-NEXT), a transition directly followed by a deeper one is never a G. So each transition that opens a deeper run (in particular
    the one directly before the window's first element) is an O-rise, and it recomputes every position below it.
  - The window may contain further rises of a (windows cross shallower transitions; law (W) is false). So the window need not lie in
    one context of a.
- Observed so far:
  - Every segment after an O-rise has NEST* ≤ 2.
  - Non-first pieces carry NEST*-3 windows: win3_n27 (position 1) and w1_n27 (position 3, with position 1 rising after it).
  - In no instance does a shallower level rise BEFORE such a window.
- The exact open step (R48 §4 sharpened): a NEST*-3 window at a level r together with rises at some a < r both before it and after it.
  Neither a construction nor an impossibility argument for this step is known.
  - (G-NEXT) together with a segment bound does not bound NEST* combinatorially. 0,1,0,2,0,1,0 has NEST* 3 and
    0,1,0,2,0,1,0,3,0,1,0,2,0,1,0 has NEST* 4, while every segment in both has NEST* ≤ 1.
  - Their windows cross shallower transitions. Any bound must control such cross-context windows.

## 5. NEST* 4 on 𝒞^1P (2026-10-21 22:00Z, date -u): a disjoint union
- experiments/red/nest16/pairunion.py builds B ⊎ A (no edges between them) with A's priorities shifted above B's (parity kept).
  - B = near4_n26 (sha1 6d7c5e38…), A = L-ALG's experiments/alg/instances/onep_chainfail_n20.pg (sha1 05bfe58e…).
  - Result: instances/nest4u_n46.pg, sha1 ae7ed55930f06223c5f3cd64fb1d617064bb8ede, n 46, C = 1.
  - In 𝒞^1P by L-ALG's fixd_oneplayer.inclass: q-vertices have one successor, all priorities distinct.
- q-phase (0, 0), both orders (L-ALG's unmodified b12_pot.run / chain, b12_core.states): S 18, identical P in stable and oink order:
  P = 4,1,2,6,10,10,8,9,9,6,8,8,6,1,5,5,5, NEST* 4.
  - Witness: 1 (idx 1, 13) ⊃ 6 (idx 3, 12) ⊃ 8 (idx 6, 11) ⊃ the 9-pair (idx 7, 8).
- Pinned Oink 8fbf0a7 `--dtl --no-single --no-wcwc --no-loops -v`: even iterations 18 (= S), odd 1, solution verified (40 strategies).
- Status: ONE instance with NEST* 4. This is not yet a family, and not growth with n.
