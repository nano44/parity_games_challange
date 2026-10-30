# R122: FG(τ) with a fixed-ranking guide on wrapped switchallexp. A climbed edge ranking makes FG run LONGER than switch-all (119 vs 70 at N = 3, 174 vs 150 at N = 4), but FG / n is 0.53 → 0.59; no super-polynomial sign. DATA + READING; GUIDE-POLY OPEN
L-RED successor 30 (Opus 5.5; D1/D18; Lead 21:05Z target (2), L-SI box 36 CONJECTURE GUIDE-POLY: "for every game, every start σ and
every fixed Odd strategy τ, FG(τ) stops after poly(n) iterations"). Written 2026-10-29 22:03Z (date -u). Labels: DATA / READING / OPEN.

## 1. The wrapped game (construction; READING)
- mix/fgt.py: every edge v → w of an Even vertex with ≥ 2 successors becomes v → o_vw.
  - o_vw is Odd, priority 0, with edges {w, t_vw}.
  - t_vw is an even self-loop with priority P_vw; the P_vw are distinct and above every original priority.
- Odd's free best reply takes w (t_vw is Even-won and top). So Ξσ and Iσ are the original game's, up to a uniform +1 in lengths.
- The guide τ(o_vw) = t_vw makes W_τ(v → o_vw) = the reward of t_vw, independent of σ: a FIXED edge ranking.
- So FG(τ)'s S4a step is "every Even vertex takes its top-ranked edge in {σ(v)} ∪ Iσ(v)". A stall (no vertex moves) is one
  switch-all step. Any edge ranking is realised by some τ, and GUIDE-POLY quantifies over every τ.

## 2. DATA (switchallexp = PGSolver port, experiments/hard-families/pgsolver_port.py)
| N | wrapped n | switch-all | FG, index / reverse / rand:1 / rand:2 | FG, climbed ranking (stalls) | FG / n |
| --- | --- | --- | --- | --- | --- |
| 2 | 155 | 30 | 22 / 23 / 23 / 22 | | |
| 3 | 225 | 70 | 37 / 32 / 39 / 31 | 119 (28) | 0.53 |
| 4 | 295 | 150 | 58 / 37 / 45 / 28 | 174 (35) | 0.59 |
- Start: original S3 mapped to the wrapped edges. Climb: swap mutations, 1500 steps (N = 3, 2 seeds: 119, 110) and 1200 steps
  (N = 4, 1 seed). Bounded, not extended.
- Second engine: from the wrapped game's own S3 start (fgt.py START=wbest), L-SI's fg.py (L-NEW's n5x engine, guide "last" = t_vw
  at every o_vw) gives the same counts as fgt.py (n5b SPEC pieces): N = 3: 64 iterations / 14 stalls; N = 4: 125 / 25.
- Pins (mix/instances/, sha1 first 12):
  - switchallexp_3.pg 3ad1b30a06c0, fg_sa3_best.order 30fd89ddd60b, fg_wrapped_sa3.pg 0dfa75734f1b;
  - switchallexp_4.pg c94d98d3961a, fg_sa4_best.order ab9fd564cbc7.
- check.sh gate: N = 3 climbed ranking 119 / 28 stalls / switch-all 70; the wrapped game regenerates.

## 3. Reading
- A fixed guide can make FG slower than switch-all on the same game. The climbed rankings delay switches until the stalls force them,
  and partial (ranked) steps are shorter than switch-all's.
- The growth is mild: FG ≈ 1.7 × and 1.16 × switch-all; FG / n 0.53 → 0.59. The corpus max is 2.66n (L-SI §7).
- No evidence here for or against GUIDE-POLY. Exponential growth would need the ranked steps to follow switch-all's exponential run
  for long stretches between stalls, and the ratio to switch-all falls from N = 3 to N = 4.
- Next (OPEN): guides whose W depends on σ: τ(o_vw) → structured continuations instead of t_vw. Also transfer the climbed
  rankings' structure across N, rather than climbing per N.

## DONE / FINDINGS / NEEDS
- DONE: mix/fgt.py (FG on the wrapped game; RANK index / rindex / rand / file; START=wbest; OUT); climbs; pins; gate; second engine.
- FINDINGS:
  1. READING: wrapping turns any fixed edge ranking into a guide τ.
  2. DATA: climbed FG exceeds switch-all at N = 3, 4, with FG / n 0.53, 0.59. GUIDE-POLY not killed.
- NEEDS: none from the owner.
