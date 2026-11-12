# R238: independent replay of L-SI box 105's Lemma KEY-MODEL on L-RED's SPEC-exact engine — VERDICT: KEY-MODEL SURVIVES (keyfail 0)
L-RED successor 68 (Opus 5.5, D21 / L53). Lead brief 2026-11-12 (successor 68, item 3): «L-SI's box 105 (claude/l-si 516b6837,
docs/si/box105-key.md: KEY-MODEL) — replay its equivalence (N5 spec on Γ3*(G*) = the KEY rule, state for state) on your n5s237 on random
free genomes; report keyfail with controls.» Labels: DATA (unit, set, scope, counter) / SURVIVES.
D1 (owner, verbatim): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the
fleet's own, as wrong until it passes the gauntlet below.»
**Scope: box 105's statements are about N5 from S3 on Γ3*(G*) (free genomes) up to the first fallback. This replay is DATA on random and
climbed free genomes; it is not a proof of KEY-MODEL and not a referee signature. O2 (KEY-FREE) and G-N5-TIME stay OPEN.**

## 0. The statement replayed (quoted from claude/l-si 516b6837 docs/si/box105-key.md §2)
«Lemma KEY-MODEL. For every free genome G*, under the standing SPEC premise 1E-N3 … and R104's premise [RULE] …: the N5 run from S3 on
Γ3*(G*) has states 0, …, L* equal to the standard states of s_0, …, s_(L*) of KEY(G*); its transitions 1, …, L* are not fallbacks;
transition L* + 1 is its only fallback (F* = L* + 1); it makes exactly L* + 3 iterations.»

## 1. What is independent (tool experiments/red/r238/key238.py)
- N5: n5s237 mode spec (L-RED 67, written from the SPEC text; state by state equal to box 190's n5v on 8,900 random games, R237).
  Box 105 validates against n5v; here the reference N5 is mine.
- KEY's valuation V_s(x, k) = Ξ_(σ_s)(m_(x,k)): computed by n5s237.vjproc (SPEC S1 (i)-(vi)) on the standard state, not by si.Engine.
- KEY(G*): my simulator, written from box 105 §1's Definition (A_s(x) strictly better by V_s; level by level, lowest first, the key
  read under the NEW lower choices; stop at the first unchanged state).
- Borrowed, OBJECTS only: box 104's freereach104.rand_free (the random free genomes) and free104.build_free (Γ3*(G*), its standard
  state's non-mover part σ0 / τ0 and the vertex map) at claude/l-si 26704e01.
- Counters (must 0): s3fail (S3's pair ≠ the standard state of s_0 at any vertex); keyfail (some state j ≤ L* of the N5 run is not the
  standard state of s_j at EVERY Even vertex, or τ ≠ τ0, or the first fallback is not at L* + 1; this is stricter than box 105's
  keyfail, which compares the movers only); endfail (fallbacks ≠ 1 or iterations ≠ L* + 3); wrong (regions ≠ harness Zielonka);
  keymono (box 105 §3 KEY-MONO*: a mover's key increases, or it moves without a strict decrease).
- Second simulator (sampled): box 105's own key105.key_run (si.Engine valuation) on the same genome; kdiff = genomes whose KEY state
  sequence differs from mine.

## 2. DATA
### 2.1 Random free genomes (key238.py rand; out/key238.out)
| seed | genomes | depth d ≤ | width w ≤ | degree ≤ | X-rate | s3fail | keyfail | endfail | wrong | keymono | max L* | sum L* | max |V| | key105 sampled / kdiff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2381 | 2,000 | 4 | 3 | 3 | 0.15 | 0 | 0 | 0 | 0 | 0 | 4 | 1,407 | 211 | 200 / 0 |
| 2382 | 1,000 | 6 | 4 | 3 | 0.15 | 0 | 0 | 0 | 0 | 0 | 4 | 1,034 | 368 | 100 / 0 |
| 2383 | 1,000 | 8 | 2 | 2 | 0.15 | 0 | 0 | 0 | 0 | 0 | 3 | 553 | 200 | 100 / 0 |
| 2384 | 500 | 12 | 3 | 3 | 0.15 | 0 | 0 | 0 | 0 | 0 | 6 | 624 | 532 | 50 / 0 |
| 2385 | 500 | 3 | 6 | 5 | 0.15 | 0 | 0 | 0 | 0 | 0 | 4 | 610 | 476 | 50 / 0 |
| 2386 | 1,000 | 6 | 3 | 3 | 0.0 | 0 | 0 | 0 | 0 | 0 | 4 | 880 | 271 | 100 / 0 |
| 2387 | 1,000 | 6 | 3 | 3 | 0.6 | 0 | 0 | 0 | 0 | 0 | 4 | 864 | 278 | 100 / 0 |
| 2388 | 300 | 16 | 2 | 3 | 0.15 | 0 | 0 | 0 | 0 | 0 | 4 | 313 | 444 | 15 / 0 |
| total | 7,300 | | | | | 0 | 0 | 0 | 0 | 0 | 6 | 6,285 | 532 | 715 / 0 |
- Correction: commit ca8dd9a11's message says «key105 kdiff 0 on 615 sampled»; the count is 715 (this table). Typed before the sum.
- X-rate ≠ 0.15: every Ξ-target redrawn, X with that probability (0.0: no X targets; 0.6: mostly X).
### 2.2 Climbs on L* (kclimb238.py; score = (counter sum, L*); out/kclimb.log, kck_ka.json, kck_kb.json, kbest_*.json)
| climb (TAG SEED d w deg) | genomes | L* reached | sum L* (transitions checked) | max |V| | every counter | out |
| --- | --- | --- | --- | --- | --- | --- |
| ka 2391 10 3 3 | 25,000 | 19 | 243,910 | 413 | 0 | out/kclimb.log |
| kb 2392 16 2 3 | 25,000 | 21 | 326,718 | 470 | 0 | out/kclimb.log |
- The best genomes, re-run on BOTH pipelines (out/kbest_second.out): kbest_ka.json (sha1 e2433d1e3af5f96d42e0059cb795a24a4ec1eb64; N 10,
  4 levels, |V| 160): own L* 19, 22 iterations, first fallback 20, one fallback; key105 + n5v: L* 19, all counters 0, KEY states equal.
  kbest_kb.json (sha1 222287153b02007ac7bbfa7978a8b55213438dd9; N 17, 10 levels, |V| 279): own L* 21, 24 iterations, first fallback
  22; key105 + n5v: L* 21, all 0, KEY states equal.
- DEPTH-BOUND* (box 105 §3) holds on both: 19 ≤ 1,028 and 21 ≤ 2,109,374 (Π(1 + w_ℓ(Δ − 1)) − 1). DATA only: the climbed L* is
  about 2N here, far below the bound.
- Climb controls (experiments/red/r237/out/climb_ctrl.log): CTRL=1 keyfail 2,694 of 3,000 climbed genomes; CTRL=2 keyfail 2,997 of 3,000.
## 3. Controls (out/key238.out; 300 genomes, seed 2381, d ≤ 4, w ≤ 3, degree ≤ 3)
| control | change | keyfail | endfail | keymono | fires |
| --- | --- | --- | --- | --- | --- |
| CTRL=1 | keys read under the OLD lower choices (box 105's own control) | 12 | 9 | 0 | yes |
| CTRL=2 | the MOST key instead of the least | 243 | 177 | 599 | yes |
| CTRL=3 | A_s(x) with «better or equal» | 61 | 30 | 0 | yes |
| CTRL=4 (neutral, must NOT fire) | an option's value read at its gate instead of its pad (one step, no P-element: same order) | 0 | 0 | 0 | no (as required) |
- No control for s3fail and wrong.

## 4. What this does and does not touch
- KEY-MODEL survives an independent replay: on every genome tested, N5 (my SPEC-exact engine) from S3 visits exactly the standard
  states of KEY(G*)'s run, at every Even vertex, with one fallback at L* + 1 and L* + 3 iterations; box 105's own simulator gives the
  same KEY run on every sampled genome. KEY-MONO* (keymono) is 0 everywhere.
- This is DATA, not a proof; the lemma's proof (box 105 §2) still needs its referees. The runs are short (L* ≤ 6 on random genomes, ≤ 21 on the climbs), so the
  replay says little about long runs; O2 (is L* polynomial on every free genome?) stays OPEN, and so does G-N5-TIME.
