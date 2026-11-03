# R197 The R196 escape shape does not compound: fork-shaped (alternating-waker) ladders are SHORTER than free ones (z3-exact 3 / 5 at d 2 / 3); the carry doubling that exists (F_1 = 2F_0 + 2, exact, pinned) runs through a DELAY LINE and stops at the next level: exact carry maxima 2, 6, 10 and exact max run 13 at d 4 (new; R193 queue item closed; pinned); Lemmas DOWN / LEVEL-RISE / WAKE-CHAIN (PROVED, lane); no kill, no family (L-RED successor 47)
Started 2026-11-02 20:58Z (Lead brief STEP 1, date -u). Brief: «R197: the R196 escape shape … Build an alternating-waker doubling
ladder: at each level, the two sides of the fork take turns waking the mover, and each lower carry triggers both sides. Score U against
d, realise, and pin. If it cannot compound, prove the side-alternation bound …». Labels: PROVED (lane), EXACT (z3, machine-checked, not
Lean), DATA, READING, OPEN. Model: IDEAL-ACYC on width-2 W-ladders (R191 notation; option k of a level-l ≥ 1 mover has W-target
2(l − 1) + (k mod 2); R_l = key ranking of the two level-l movers; F_l = #steps at which R_l flips («carries»); desc(x) = movers
Ξ-reachable from x; A_t(x) = availability read at state t). Premises: R178 Lemma XI-NEW, R189 Corollary LAG, L-NEW box 149 Lemma
KEYFLIP, box 142 DELAY-CHARGE, R195 MERGE-1*, R196 SAME-WAKER (lane results, quoted from their files); RESULTS R104 (REALIZE) for the
pin. Not a TARGET.md claim. G-N5-TIME OPEN. No kill, no family.

## 0. Answer
- The ladder the brief asks for was built in its literal form, a FORK ladder: the two options of every mover have as Ξ-targets the two
  movers of ONE other level (so every wake of x comes from one side or the other, R196 §0). It does not compound; it is weaker than
  the unconstrained ladder:
  - EXACT (z3, r197/bmcfork.py XI=fork, all fork ladders of width 2, degree 2, any level pairing, any ranks / gates / start):
    max run 3 at d 2 (L 4 UNSAT), 5 at d 3 (L 6, L 7 UNSAT); d 4 undecided (L 7, L 8 exact runs stopped after 80 min). Unconstrained
    ladders: 4 / 8 / 13 at d 2 / 3 / 4 (R188; d 4 = 13 is new here, §2b).
  - XI=down (fork to level l − 1): L ≤ d by Lemma DOWN (§1); climbs hit exactly L = d at d 3-6 (DATA).
  - XI=up (fork to level l + 1): EXACT max 5 at d 3 (L 6 UNSAT); climbs (40k mutations) 5 / 7 / 8 / 15 at d 3-6 (D 2), 7 / 9 / 11 / 13
    (D 3); U 2 / 3 / 4 / 5 (D 2), 3 / 3 / 4 / 6 (D 3). Linear (DATA).
- Alternating single-wake pairs are rare (DATA, r196/wakeck.py per genome): 0 in both exact d 3 maxima (R188 x3_L8; dbl_d3_F6),
  0 in the lag2c_d4 / nest / rot pins, 1-5 per run in the d 8 climb champions (u_d8_D3 4 of 24 steps, rk_D3_k3_d8 5 of 20, u4_d8 3 of
  31). They DO appear in the new exact d 4 witness of length 13 (§2b: 5 pairs in 13 steps, 3 at u3 and 2 at u1): its top mover u3 has the Ξ-fork
  [v3, v1] and moves 4 times, woken alternately by v1 (level 1) and v3 (its partner), a two-tick clock that runs twice. Every tick
  is paid by one move of the waking side (v1, v3 move 3 + 3 times), as the exact leapfrog statement in §3 requires, so the
  alternation multiplies nothing. A global side-alternation bound would bound these ticks only; it was not attempted beyond §3.
- What the exact search finds instead (§2): the bottom carry DOES double. z3 with a carry constraint (bmcfork FMIN) finds at d 3 a run
  with F = [2, 6, 7]: F_1 = 6 = 2F_0 + 2, the KEYFLIP / DELAY-CHARGE ceiling, i.e. both level-1 movers answer every level-0 carry at
  different steps. The late answer is carried by a DELAY LINE through level 2 (v1 moves at the carry, wakes u2, u2 wakes u1 two steps
  after the carry), not by alternating wakers (0 consecutive single-LAG pairs). Realised and pinned: dbl_d3_F6_n60 (lemck 0 violations;
  startck, Oink zlk + verify, tl + verify, xeng). At d 3, F_2 ≤ L ≤ 8 (R188); the witness has F_2 = 7.
- d 4 (§2b, EXACT): the next level does NOT double. Level 1 again reaches 6 and level 2 reaches 10 (witness dbl_d4_F10_n78, F = [2, 6,
  10, 2], level 2 carrying at every step), but F_2 ≥ 11 is impossible on every d 4 run, against the ceiling 2F_1 + 2 = 14. On the way
  the R193 queue item closes: the exact maximum run at d 4 is 13 (L 13 lifted and pinned, max_d4_L13_n78; L 14 UNSAT). Carry maxima
  2, 6, 10 (+ 4 per level) and run maxima 4, 8, 13: no compounding (CONJECTURE CARRY+4 in §2b; d 5 rows there).
- New lemmas (§1, PROVED, lane): DOWN (all Ξ-edges to lower W-levels ⇒ L ≤ d), LEVEL-RISE (L ≤ d (1 + #UPW), UPW = steps whose least
  mover is woken by a Ξ-descendant of W-level ≥ its own), WAKE-CHAIN (degree 2: every move after step 1 is PROMPT (key order changes)
  or LAG (woken one step earlier); wake chains run forward in π, so a response is late by at most the Ξ-depth).
- READING (§4): what compounding would need is an interval nesting: at every doubling level the late answer must land strictly inside
  the previous level's short interval, so delays must SHRINK by ≥ 1 per doubling level; delay-1 answers (the carry-maker itself wakes
  the partner one step later, the common case in the data) give additive growth, one extra carry per level per base interval, which is
  the «≈ constant per level» seen in every climb.

## 1. Lemmas (PROVED, lane)
- Lemma DOWN. If every Ξ-edge of an IDEAL-ACYC W-ladder genome (any width, any degree) goes from a mover to a mover of strictly LOWER
  W-level (or to the exit), then L ≤ d (d = number of W-levels).
  - Proof. Let m_t be the least W-level among the movers of step t. For t ≥ 2 let h be a mover of level m_t that moves at t to w.
    R178 XI-NEW: w ∉ A_(t−2)(h); and w ∈ A_(t−1)(h) (h moves to w at t). A_(t−1)(h) ≠ A_(t−2)(h) needs a change of some face value of h
    between s_(t−2) and s_(t−1) (if h itself moved at t − 1 from o to o′ with nothing in desc(h) moving, then o′ ▷ o, and w ▷ o′
    or w = o; both give w ∈ A_(t−2)(h) or o ▷ o′, a contradiction), and h's face values depend only on the states of desc(h). So some
    y ∈ desc(h) moved at t − 1, and lev(y) < lev(h) = m_t by hypothesis. Hence m_(t−1) ≤ lev(y) < m_t. So m_1 < m_2 < … < m_L, all in
    {0, …, d − 1}: L ≤ d. ∎
  - Tight: the XI=down fork climbs reach L = d exactly at d 3-6 (pin-free DATA; genome r197/lag/fdown_d6.json, L 6, F [0, 1, 1, 2, 2, 2]).
- Lemma LEVEL-RISE (same proof, no hypothesis on Ξ). Call a step t ≥ 2 UPW if some least mover of step t has a Ξ-descendant of W-level
  ≥ m_t that moved at t − 1. At every other step t ≥ 2, m_(t−1) < m_t. Hence every maximal run of non-UPW steps is strictly level-rising,
  and L ≤ d (1 + #UPW). (A sibling of box 144 CHAIN-BACK: there the charge is «unchained», here «woken from the same or a higher
  W-level».) DATA: r197/downck.py, 0 violations of the rise and of the bound on random ladders (width 2-3, degree 2-4, d 2-7).
- Lemma WAKE-CHAIN (degree 2, any width). Every move (x, t) with t ≥ 2 is PROMPT (the key order of x's options changes at step t) or
  LAG (x did not move at t − 1 and its key order is the same at s_(t−1) and s_t). A LAG move has a waker y ∈ desc(x) that moved at
  t − 1, and following wakers back gives a chain (x, t), (y_1, t − 1), …, (y_k, t − k) of LAG moves along a Ξ-path ending in a PROMPT
  or step-1 move; so k ≤ Ξ-depth − 1, and a response is late by at most the Ξ-depth.
  - Proof. If x moved at t − 1 and t, KEYFLIP (box 149) gives KP(x) at s_(t−1) ≠ KP(x) at s_t, so the key order changed at t (PROMPT).
    Otherwise x did not move at t − 1; if the key order is unchanged, R189 Corollary LAG gives a desc(x) mover at t − 1. Wakers are in
    desc, so π strictly increases along a chain. ∎
  - In a width-2 ladder at degree 2 the key order of a level-l mover x is the order of R_(l−1), so PROMPT = «moves at a carry of level
    l − 1» and LAG = «delayed» in the sense of box 142 (DELAY_l). DATA (r197/chains.py, 13 degree-2 genomes incl. the exact d 3 / d 4 witnesses):
    155 moves = 22 START + 49 PROMPT + 84 LAG, 0 other; longest wake chain 3 (x3_L8, dbl_d3_F6, dbl_d4_F10), 4 (max_d4_L13), 5 (g4_L12). At degree ≥ 3 R191 ROT-CAP
    allows key-alone moves without a key change at t (13 «other» moves in u_d8_D3, rk_D3_k3_d8, u4_d8).

## 2. The doubling that exists: F_1 = 2F_0 + 2 at d 3 (EXACT, pinned)
- Ceiling (lane): at degree 2, a level-0 mover moves at most once (its keys never change; KEYFLIP), so F_0 ≤ 2; and F_l ≤ F_(l−1) + 2 +
  DELAY_l ≤ 2F_(l−1) + 2 (box 142; each level-l mover moves at most once between two carries of level l − 1, KEYFLIP). So F_1 ≤ 6.
- EXACT (z3, r197/bmcfork.py, XI=free, FMIN=1:4, d 3, L 8; the extra constraint counts flips of R_1 among states 1..8): SAT; the model
  replays (r187/ideal.py) with F = [2, 6, 7], moves per level [2, 6, 4], L 8 (the d 3 maximum, R188), stopping «opt». Genome
  r197/lag/dbl_d3_F6.json. F_1 = 6 meets the ceiling.
- Trace (r197/trace.py; u/v = the two movers of a level; Ξ: u0 → [u1, X], v0 → [v2, X], u1 → [u2, v0], v1 → [v0, v2], u2 → [v2, v1],
  v2 → [X, X]):
  - t1 v1 (start); t2 u2 LAG<v1>; t3 u1 LAG<u2>, v2; t4 v0 LAG<v2> (carry 0), v1 PROMPT; t5 u1 LAG<v0, v1>, u2; t6 u0 LAG<u1, u2>
    (carry 0), v1 PROMPT; t7 u2 LAG<v1>; t8 u1 LAG<u2>.
  - So v1 answers each level-0 carry at once (PROMPT at t4, t6), and u1 answers it late: at t5 (delay 1, woken by the carry-maker v0
    together with v1) and at t8 (delay 2: v1 → u2 → u1, a DELAY LINE through level 2). Before the first level-0 carry the same line
    gives t1 → t2 → t3. Every level-1 move flips R_1.
  - No consecutive single-LAG pair at all (wakeck pairs 0): u1's moves are LAG, LAG, LAG but woken by u2, {v0, v1}, u2, with v1's
    PROMPT move and level-0 carries between them; SAME-WAKER does not apply (the middle wake is double).
- Pin (RESULTS R104 / P-N5-REALIZE gadgets, r187/stab.py pad 1): dbl_d3_F6_n60 (n 60; sha1 .pg 4bddce29…, .start cb9ee073…). r189/lemck.py on the real run:
  L 8, 0 violations of SBAR / TAU / ESC / W / AV / KEY / FB (one real FL run of length 8); startck, Oink 8fbf0a7 --zlk + verify,
  --tl + verify, xeng: PIN OK.
- At d 3 the next level has no room: F_2 ≤ L ≤ 8 (R188 / bmc4: L 9 UNSAT). (A FMIN=2:8 query at L 8 is UNSAT but says nothing:
  FMIN counts flips over transitions 2..L only, 7 of them.) The question moves to d 4 (§2b).

## 2b. d 4: the second level does NOT double (EXACT)
- Method (queue item «d 4 exact by repeated lifts», now r197/liftloop.py): solve the relaxation REL (bmcfork REL=1: free distinct
  nonzero integer weights instead of ±2^rank; its UNSAT is an exact upper bound), lift a REL model with FIX (Ξ-targets, gates, start
  fixed; ranks / parities free; exact), and on a failed lift add a blocking clause for that structure and repeat. FMIN=l:k asks for
  ≥ k flips of R_l over the transitions 2..L (step 1 is not counted).
- Results (width 2, degree 2, d 4, Ξ free):
  - F_2 ≥ 9 over steps 2..10 at L 10: SAT at the first lift (REL 13 s, FIX 57 s). Witness r197/lag/dbl_d4_F10.json: L 10, F =
    [2, 6, 10, 2] (all steps counted), moves per level [2, 6, 7, 2]: level 1 at its ceiling 6 again, level 2 flips at EVERY step.
    Pinned: dbl_d4_F10_n78 (sha1 .pg 8a1a86f9…, .start a42ddafb…; lemck L 10, 0 violations; PIN OK).
  - F_2 ≥ 10 over steps 2..L: REL UNSAT at L 11, 12, 13, 14 (each < 20 min; F_2 ≥ 11 UNSAT at L 12 (48 s) and L 14; F_2 ≥ 12 UNSAT at
    L 13 (53 s)). L 15: UNSAT as well.
  - So on every d 4 run of length ≤ 14, F_2 ≤ 10 (9 over steps 2..L, + step 1), against the KEYFLIP / DELAY-CHARGE ceiling
    2F_1 + 2 = 14. MAX RUN LENGTH at d 4 = 13 (EXACT; queue item 2 closed): L 13 lifts at the first REL model (REL 3204 s, FIX 16 s; witness
    r197/lag/max_d4_L13.json, pinned max_d4_L13_n78, sha1 .pg 458e7c6a…, .start 2c932e66…, lemck L 13, 0 violations, PIN OK), and L 14
    is REL-UNSAT with the lane-lemma clauses LEM + LAG + KF (≈ 6100 s; every real run satisfies them, so this is an exact bound).
    Exact maxima d 2 / 3 / 4: 4 / 8 / 13. Hence the F_2 bound covers EVERY d 4 run.
- Exact carry maxima so far: F_0 ≤ 2 (lemma), F_1 = 6 (d 3, d 4), F_2 = 10 (d 4, L ≤ 14): 2, 6, 10, i.e. + 4 per level, not × 2.
- d 5 (EXACT, first rows): F_2 ≥ 10 over steps 2..11 at L 11 is SAT (liftloop, first lift: REL 1161 s, FIX 207 s; witness
  r197/d5/f2_d5_L12.json, run length 12, F = [2, 6, 10, 7, 6], level 2 carrying at every step 2..11 but not at step 1). So with a
  fifth level the step-2..L count passes the d 4 bound 9, while total F_2 stays at the d 4 maximum 10. Running at the push (REL calls
  > 1 h each at d 5): total F_2 ≥ 11 (FMIN 2:11 at L 12, KF + LAG), F_3 ≥ 13 at L 14 and F_3 ≥ 15 at L 16 (CARRY+4 predicts F_3 ≤ 14).
- REFUTED in R198 (2026-11-03, exact d 5 witness c4x_d5_F12: F_2 = 12 = F_1 + 6). Original text: CONJECTURE CARRY+4 (DATA = the exact rows above only): on width-2 degree-2 IDEAL-ACYC ladders, F_l ≤ 4l + 2. With N5-IDEAL-STATE §5
  (IDEAL-ACYC-POLY ⟺ Σ_l F_l poly on this ladder, l-new box 149, lane) it would give O(d²) carries, hence polynomial runs, on this
  ladder class only. Not proved; the d 5 / L ≥ 15 rows are the next test.

## 3. The side-alternation question (READING, with the exact part PROVED)
- What SAME-WAKER's proof gives exactly (PROVED, lane; R196 §0 escape shape, degree 2): if x makes consecutive SINGLE LAG moves
  o_0 → o_1 at t_1 (waker y_1) and o_1 → o_0 at t_2 (waker y_2 ≠ y_1), then y_1 ∈ chain(o_1) \ chain(o_0) under s_(t_1 − 2) and
  y_2 ∈ chain(o_0) \ chain(o_1) under s_(t_2 − 2) (MERGE-1*), and the two faces leapfrog: face(o_1) ▷ face(o_0) from s_(t_1 − 1) on,
  face(o_0) ▷ face(o_1) at s_(t_2 − 1). So a run of k alternating single wakes of x needs ≥ k gains split over the two private chain
  prefixes, i.e. #alternations(x) ≤ 2 · min over the two sides of the number of steps at which a mover of that side's private
  prefix moves, + 1. This is the path-count bound in another form (R191 §1, pathck), exponential in π-depth; no global bound follows.
- Why a global side-alternation bound is not the next step (READING, from §0 DATA): alternating single pairs are 0 / 0 in the exact
  d 3 maxima, 5 in the exact d 4 maximum (each paid by a side move) and ≤ 5 per run in every champion up to d 8, while the moves that make runs long are PROMPT / LAG alternations of ONE mover
  (WAKE-CHAIN). Bounding single-pair alternations bounds a quantity that is already O(1) per run in the data and leaves U untouched.
- The quantity that does carry the open question in this language: DELAY_l (box 142) = LAG moves of level l. By WAKE-CHAIN each is the
  end of a wake chain of length ≤ Ξ-depth along a Ξ-path forward in π. U-LIN / DELAY-LIN ask that these chains, summed, stay linear.

## 4. Interval nesting: what compounding would need (READING)
- KEYFLIP: between two consecutive carries of level l − 1 (an «interval» (c, c′]) each level-l mover moves at most once, a PROMPT move
  at the right end c′ or a LAG move strictly inside. So level l contributes at most one carry at c′ and at most two inside; F_l ≈ 2F_(l−1)
  needs, in almost every level-(l − 1) interval, one LAG move strictly inside, at offset δ ≥ 1 from c.
- For level l + 1 to double as well it needs, inside the short level-l interval (c, c + δ], a LAG move at offset δ′ with 1 ≤ δ′ < δ.
  So along k consecutive levels that each double inside every interval, the offsets strictly decrease, δ_l > δ_(l+1) > … ≥ 1, and the
  bottom offset is ≥ k. By WAKE-CHAIN an offset is realised by a wake chain (or by a chain rooted at a later PROMPT move), so deep
  doubling needs long wake chains at the BOTTOM levels and short ones at the top.
- DATA (r197/delays.py, offset = t − last carry of level l − 1 before t, 0 if none, over the 16 committed genomes of R188-R197): 206
  delayed moves, offsets 1: 89, 2: 51, 3: 27, 4-11: 39. Offset 1 (the carry-maker itself, or a mover of that step, wakes the
  partner one step later; dbl_d3_F6 t5) is the most common; it leaves no room inside the short interval, so the next level can only
  add a carry per base interval there, not double. Longer offsets occur, but the climbs never stack them in the nested way above
  (their F_l stays flat in l: e.g. u4_d8 F [2, 4, 8, 8, 8, 7, 6, 4], u_d8_D3 F [1, 2, 5, 7, 3, 3, 5, 1], r197/anal.py). The only
  offset-2 answer in the exact d 3 maximum dbl_d3_F6 (t8) is the v1 → u2 → u1 delay line through the level ABOVE: lines through higher
  levels are what LEVEL-RISE charges (UPW steps).
- So the escape that a doubling ladder must build is a family of delay lines whose lengths shrink by ≥ 1 per level, each line running
  through higher levels (UPW wakes) without being consumed by them. Neither a construction nor an obstruction is known (OPEN).

## 5. OPEN / next
- CARRY+4 at d 5 (F_3 ≤ 14?) and whether extra levels above raise total F_2 beyond 10 (d 5 rows of §2b, running); a proof of F_l ≤ F_(l−1) + 4.
- The interval-nesting obstruction (§4) as a lemma, or a nested delay-line construction.
- d 5 exact max run (liftloop; REL at d 5 is slow: > 90 min per call).
- Fork ladders at d 4 exact (stopped); CNONLY in CROOT games (old queue).

## 6. Files
experiments/red/r197/: bmcfork.py (bmc4 + XI=fork|down|up, FMIN carry constraints, FREE drivers, KF = KEYFLIP clauses, BLOCK lists),
liftloop.py (REL → FIX lift loop with blocking clauses), forkclimb.py (fork / free climbs, SEEDG bottom insertion), anal.py (F_l, moves,
DELAY, waker levels), trace.py, chains.py (WAKE-CHAIN), delays.py, downck.py (DOWN / LEVEL-RISE), topext.py, curbest.py; lag/
(dbl_d3_F6, dbl_d4_F10, max_d4_L13, fdown_d6 genomes); d5/ (the d 5 F_2 witness, not pinned); instances/ (three pins + pins.sha1). check.sh block «R197». out/ is gitignored
(z3 logs, climb outputs: container-local).
