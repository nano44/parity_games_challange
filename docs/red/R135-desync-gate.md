# R135: box 82's clocked escape in real N5. A LATERAL desynchronising gate exists under σ̄-optimality with τ fixed (dg_k), but N5's arena step then runs the ladder in 4 iterations for every k. The 2^k count needs UPWARD waits (a vertex waits while its own reader sits on it), and Lemma WAIT-CYCLE shows σ̄-optimality forbids an upward wait whose signal route is ever restored. No kill
L-RED successor 33 (Opus 5.5; D1/D18). Lead 2026-10-30 (after 11:13Z): "TARGET ... L-NEW successor 37's box 82 design spec (l-new
163342eb, docs/new/N5-R2-box82.md §3) ... Build it in REAL N5 ... If it is impossible, state the exact obstruction in terms of σ̄'s
optimality (GATE-COLLAPSE)." Written 2026-10-30 from 11:15Z (date -u). Labels: PROVED (lane) / DATA / READING. Not a TARGET.md claim.
G-N5-TIME OPEN. N5 = docs/new/N5-ssi-global.md SPEC S1-S5 (engines: L-COMP experiments/n5-second/n5b.py --mode spec; L-NEW
experiments/new/n5.py on L-SI's si.py; state-by-state comparison experiments/red/seg/xeng.py).

## 0. Sources read
- l-new 163342eb docs/new/N5-R2-box82.md (§1 ogl_k, §2 ODD-GATED-LADDER, §3 GATE-COLLAPSE + design spec); experiments/new/box82/ogladder.py.
- l-new 3aac0638 docs/new/N5-WCHT-box80.md §1.1 (ladder_k, lead-follow schedule); experiments/new/box80/ladder.py and inst/ladder_K.pg/.seq
  (copied byte-for-byte to experiments/red/desync/ladder/; sha1 in check.sh).
- Ξ-monotonicity along N5: every S4a / S4c step applies a subset of Iσ, so Ξ_(σ') ⊵ Ξ_σ (the standard SI lemma as stated in the SPEC's
  "Termination" paragraph, docs/new/N5-ssi-global.md; Vöge-Jurdziński valuations as in Friedmann arXiv 1106.0778 §3). Odd steps leave σ, so
  leave Ξ_σ, unchanged.

## 1. What real N5 asks of a gate (beyond box 82's R2 model)
- τ must stay fixed through the W-run. The fleet's ogl_k gates (o(v, c) → {u(j, c) = τ(o), u(j, 1 − c)}) are not τ-stable in real N5. Under
  τ̄ the gate o(v, 1) prefers u(j, 0) (best(u(j, 0)) ◁ best(u(j, 1)) by u(j, 1)'s marker), so the edge (o(v, 1), u(j, 0)) is in Iτ. (READING
  from the S1 order; ogl_k was run in box 82 with ρ_t chosen by hand, not with N5's S4b.)
- A block must come from σ̄'s choice at a gate whose alternative is NOT τ̄-improving. Under τ̄ the escape must tie with the direct edge or be
  worse for Odd. Under σ it must be strictly better for Odd.

## 2. dg_k: a lateral desynchronising gate that works (DATA + PROVED, lane)
- Construction (experiments/red/desync/mkdg.py K).
  - ladder_k, except that copy 0 of every level (the LEADER A_j) has priority 0. Priority 0 is below the sink's 2, so A_j never enters a
    path set.
  - The FOLLOWER B_j (even marker) reads level j − 1 only through Odd gates g(B_j, c) → {p → u(j − 1, c) (τ), A_j}. Gates and pads have
    priority 0, and the two routes have equal length.
  - T is a leader at the top.
- Why it blocks (PROVED, lane; S1 order).
  - While A_j sits on the old child P, σ̄ routes BOTH gates of B_j to A_j, because A_j → P is the Odd-smaller option at g(B_j, Q).
  - At g(B_j, P) the two routes tie, with the same set and the same length. Both gates then have equal Ξ, and [S2] needs a strict rise: B_j
    is not offered. This is GATE-COLLAPSE used as the blocking device.
  - Once A_j is on Q, g(B_j, Q) has Ξ = Q ▷ P = Ξ(g(B_j, P)), so B_j is offered one iteration after A_j.
  - τ̄: the escape reads A_j's best, which is best(u(j − 1, 1)). That ties at g(B_j, 1) and is better for Even at g(B_j, 0), so Iτ has no
    gate edge and τ never changes.
- DATA (desync/dgstat.py on n5b; xeng: n5b = n5.py state by state; Oink zlk OK + strategies verified):

  | instance | n | iterations | τ-changes | W-runs | W(T) values | max WCH in a W-run | Ξ cycle nodes |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | dg_3 | 16 | 4 | 0 | 1 | 3 | 2 | sink |
  | dg_8 | 46 | 4 | 0 | 1 | 4 | 3 | sink |
  | dg_16 (pin) | 94 | 4 | 0 | 1 | 4 | 3 | sink |
  | plain ladder_8 control (GATE=0) | 18 | 1 | 0 | 1 | 2 | 1 | sink |

- Why it stays short. S4a takes the one-player W-optimum of the whole arena σ ∪ Iσ, at every level at once. Leaders and lower levels are
  never blocked, so each level advances as soon as it is offered. Each reader's W-comparison already sees the lower level's simultaneous
  flips. The gate adds a constant lag per level, and the levels overlap: 4 iterations for every k from 3 to 16 (k 3, 4, 6, 8, 12, 16 run).

## 3. Upward waits are what the 2^k count needs (DATA)
- Classification (desync/upwait.py, on box 80's own longest schedule = the one ogl_k replays). At each step, take a chooser v that is not
  the scheduled switcher but has a W-better successor; it must be blocked. The wait is UPWARD if a reader of v currently points to v, and
  LATERAL otherwise.
  - ladder_3: 20 upward, 7 lateral.
  - ladder_4: 82 upward, 28 lateral.
  - ladder_6: 756 upward, 236 lateral.
  - ladder_8: 4914 upward, 1408 lateral.
  - Upward waits are the bulk: X must not advance while a reader still reads it (box 80 proof: "C(j) advances the vertex that NEITHER
    reader points to").
- Exhaustive bound without them (desync/noup.py). Model: N5-like steps, any SET of W-improving switches per step, W monotone, fleet Engine
  values. Constraint: no step leaves an upward wait (every non-switching chooser with a W-better option has no reader on it). Longest
  T-rise count:

  | k | no upward waits | unrestricted |
  | --- | --- | --- |
  | 2 | 3 | 3 |
  | 3 | 5 | 7 |
  | 4 | 6 | 15 |
  | 5 | 7 | 31 |
  | 6 | 8 | 63 |

  That is k + 2 for k ≥ 3: linear. So on ladder_k the exponential count is exactly the upward waits.

## 4. Lemma WAIT-CYCLE (PROVED, lane): σ̄-optimality forbids a restorable self-routed wait
- Setting. Any game, any N5 run. X is an Even vertex and g is a successor of X.
  - (a) At iteration t1: σ_t1(X) ≠ g, and g is not offered at X: Ξ_t1(g) ⊴ Ξ_t1(σ_t1(X)).
  - (a) The σ̄_t1-play from g passes through X before reaching its cycle. Call π the vertices from g up to but excluding X.
  - (a) X's own Ξ_t1-play ends in a cycle (node c*) that does not contain X.
  - (b) At a later iteration t2 > t1: σ_t2(X) = g, and every Even vertex of π has the same σ-choice as at t1.
- Claim: (a) and (b) cannot both hold.
- Proof.
  - By positionality, the play from g is π, then X, then X's own play. So Ξ_t1(g) and Ξ_t1(σ_t1 X) have the same cycle node c*, and Ξ_t1(g)
    has the path set of Ξ_t1(σ_t1 X) plus the vertices of π ∪ {X} above c*, and a longer play.
  - Let m be the most relevant vertex of π ∪ {X} above c*. If m exists and is even, Ξ_t1(g) ▷ Ξ_t1(σ_t1 X) (S1: the path-set weight is
    decided at m), contradicting (a). If no such m exists and c* is odd, the longer play is better for Even, again a contradiction. So
    either m is odd, or there is no m and c* is even.
  - At t2, let ρ be σ̄_t1 on the Odd vertices of π and σ̄_t2 elsewhere. Under (σ_t2, ρ) the play from X is X → g → π → X, by (b) and the
    fixed Odd choices: a cycle Z on π ∪ {X}. Its node z is either m (odd), or below c* in relevance with c* even.
  - In both cases reward(z) < reward(c*):
    - z = m odd, c* even: reward(m) < 0 < reward(c*).
    - z = m odd, c* odd: p′(m) > p′(c*), so −p′(m) < −p′(c*).
    - z even with c* even: p′(z) < p′(c*).
    - z odd with c* even: reward(z) < 0 < reward(c*).
  - σ̄_t2 is Odd's pointwise optimum, so Ξ_t2(X) ⊴ val(σ_t2, ρ)(X), whose cycle reward is reward(z) < reward(c*). The cycle reward of
    Ξ_t1(X) is reward(c*). So Ξ_t2(X) ◁ Ξ_t1(X).
  - That contradicts Ξ-monotonicity along N5 (§0). □
- Reading for gates (READING). Suppose X waits for its reader R to leave X. The signal "R left X" changes Ξ only on plays through R. While
  R sits on X, such a play enters X, which is (a). If R later reads X again while X uses g, along the same route, that is (b).
  - In ladder_k every reader reads every value of X. So the opener of a gate g of X cannot be a reader of X, and cannot be any vertex whose
    route pattern into X recurs while X sits on g.
  - An upward wait therefore needs a signal route with a FRESH Even-choice pattern for every wait. That is a private clock with at least as
    many states as the waits it serves, which is box 82 §3's "doubling" alternative.
- The two branches of the proof, built in real N5 (pins; xeng identical, Oink OK):
  - dgu_4 (UP=1). Leader A_j's gates escape to its marked reader B_(j+1). The route carries an even marker (m even), so there is no block:
    A_2 switches at iteration 1 while B_3 still reads it. τ changes once (2 W-runs). 4 iterations.
  - dga_4 (UP=1 UPTO=A). The escape goes to the irrelevant reader A_(j+1), so there is no m. Odd closes the low cycle from the start (Ξ
    cycle node h3_0 at state 0). When the reader leaves, the cycle opens and Ξ rises. By WAIT-CYCLE it can never close again, so this wait
    happens once. 3 iterations.

## 5. The obstruction, stated for the proof side (READING)
- Box 82 §3 asks each gate for an escape whose Ξ interleaves with the ladder. In real N5 that splits into two kinds of escape.
  - LATERAL escapes (wait for a peer that reads the same lower level): realisable at constant cost (dg_k), τ-stable, with GATE-COLLAPSE as
    the block. They give O(1) iterations per level under the arena step.
  - UPWARD escapes (wait while one's own readers still read you): these carry the 2^k on ladder_k (§3: linear without them). The signal
    route passes through X, and Lemma WAIT-CYCLE allows each route pattern at most one wait before X uses g with that pattern.
- So the remaining kill route is a private clock with a fresh pattern per wait. The remaining proof target is a polynomial bound on the
  number of distinct route patterns that can serve upward waits. That is a concrete form of R3-POLY (L-NEW box 83): count the waits by
  their (X, g, Even pattern on π) triples, at most one each.
- Not covered: blocks with no escape at all. Here the new child's own Ξ lags its W through a W/Ξ gap on the child's private prefix. That
  blocks every reader of that child at once, so it is not a per-reader desync. It is R134's GAP-IN-PREFIX / TWO-SOURCE wall, which is
  unchanged.

## DONE / FINDINGS / NEEDS
- DONE:
  - Tools in experiments/red/desync/: mkdg.py (dg_k; GATE=0 control; UP=1 / UPTO=A upward variants), dgstat.py, upwait.py, noup.py.
  - ladder/: box 80's instances, copied byte-for-byte.
  - Pins in instances/: dg_16, dgu_4, dga_4. Each has xeng identical and Oink zlk OK with strategies verified.
  - check.sh "R135" section.
- FINDINGS:
  1. DATA + PROVED (lane): a lateral desync gate exists in real N5 under σ̄-optimality with τ fixed (dg_k). GATE-COLLAPSE is the blocking
     device. The run is still 4 iterations for every k, because the arena step runs all levels in parallel.
  2. DATA: on ladder_k the 2^k count rests on upward waits. Exhaustively for k ≤ 6, a ladder with no upward waits gives at most k + 2
     T-rises.
  3. PROVED (lane) Lemma WAIT-CYCLE: a gate blocked by a Ξ-play through X itself can never be taken later with the same Even pattern on that
     play. σ̄ would close a cycle of lower reward, and Ξ cannot fall.
  4. READING: box 82's spec needs one fresh signal pattern per upward wait, i.e. a private clock. No kill of G-N5-TIME or of N5.
- NEEDS: none from the owner. Lead: route Lemma WAIT-CYCLE and §5's (X, g, pattern) count to L-NEW box 83 (R3-POLY) if useful.
