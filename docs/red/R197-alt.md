# R197 The R196 escape shape (alternating single wakers on the two sides of a Ξ-fork) is NOT the engine of long IDEAL-ACYC runs: fork-shaped ladders are SHORTER than free ones (z3-exact), the exact d 3 maxima contain no alternating pair, and the bottom-level carry doubling F_1 = 2F_0 + 2 that does occur (z3-exact, pinned) runs through a DELAY LINE, not alternation; Lemma DOWN / LEVEL-RISE and WAKE-CHAIN (PROVED, lane); no compounding found (L-RED successor 47)
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
    max run 3 at d 2 (L 4 UNSAT), 5 at d 3 (L 6, L 7 UNSAT), d 4 running (L 7, L 8; cap 5400 s). Unconstrained ladders: 4 / 8 (R188), ≥ 12 at d 4.
  - XI=down (fork to level l − 1): L ≤ d by Lemma DOWN (§1); climbs hit exactly L = d at d 3-6 (DATA).
  - XI=up (fork to level l + 1): EXACT max 5 at d 3 (L 6 UNSAT); climbs (40k mutations) 5 / 7 / 8 / 15 at d 3-6 (D 2), 7 / 9 / 11 / 13
    (D 3); U 2 / 3 / 4 / 5 (D 2), 3 / 3 / 4 / 6 (D 3). Linear (DATA).
- Alternating single-wake pairs are rare and absent from the exact maxima (DATA, r196/wakeck.py per genome): 0 pairs in both exact
  d 3 maxima (R188 x3_L8, L 8; dbl_d3_F6 below, L 8), 0 in lag2c_d4 / nest / rot pins, 1-5 per run in the d 8 climb champions
  (u_d8_D3 4 of 24 steps, rk_D3_k3_d8 5 of 20, u4_d8 3 of 31, g4_L12 3 of 12). A bound on side-alternations would therefore NOT bound
  run length: long runs alternate PROMPT and LAG moves of each mover (§2), and SAME-WAKER / side-alternation speak only about two
  consecutive LAG moves. So the side-alternation bound the brief names as the fallback is not the next step toward U-LIN (READING), and
  it was not attempted beyond §3.
- What the exact search finds instead (§2): the bottom carry DOES double. z3 with a carry constraint (bmcfork FMIN) finds at d 3 a run
  with F = [2, 6, 7]: F_1 = 6 = 2F_0 + 2, the KEYFLIP / DELAY-CHARGE ceiling, i.e. both level-1 movers answer every level-0 carry at
  different steps. The late answer is carried by a DELAY LINE through level 2 (v1 moves at the carry, wakes u2, u2 wakes u1 two steps
  after the carry), not by alternating wakers (0 consecutive single-LAG pairs). Realised and pinned: dbl_d3_F6_n60 (lemck 0 violations;
  startck, Oink zlk + verify, tl + verify, xeng). At d 3 the next level cannot double (F_2 ≥ 8 UNSAT at L 8, the exact maximum run).
  d 4: running (FMIN 2:7 at L 8, 2:8 at L 9 and L 10; cap 7200 s).
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
    l − 1» and LAG = «delayed» in the sense of box 142 (DELAY_l). DATA (r197/chains.py, 10 degree-2 genomes incl. both exact d 3 maxima):
    119 moves = 20 START + 37 PROMPT + 62 LAG, 0 other; longest wake chain 3 (x3_L8, dbl_d3_F6), 5 (g4_L12). At degree ≥ 3 R191 ROT-CAP
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
- The next level does not double at d 3: F_2 ≥ 8 with L 8 is UNSAT (EXACT, FMIN=2:8), and L 9 is UNSAT outright (R188 / bmc4), so
  F_2 ≤ 7 there. The question moves to d 4 (§2b).

(Interim commit: §2b (d 4), §3 (side alternation), §4 (interval reading), §5 files follow in the final push.)
