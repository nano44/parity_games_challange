# R231 item 3 (lean): depth-3 stall, i.e. a dynamic a-face added to RING (L-RED successor 65)
Written 2026-11-12 (date -u in the commit). Object: the open escape of docs/red/R230-stall.md §0 («the only escape is a DYNAMIC a-face:
an option whose e-face play gains an item later»), against L-SI 50 BOX 98 CONJECTURE U-FREE (claude/l-si dc20e816). Labels: DATA (unit,
set, scope) / DEAD / READING. Engine: L-NEW gamma3 / n5v at l-new fcba92fc through my lane's r230/elev230.measure (N5′-xi from S3 on Γ3,
permuted e-priorities). Tool: experiments/red/r231/ring3_231.py; outputs r231/out/ring3_231.out; frozen r231/inst/ring3{A,B,C,D}_k8_m12.json
(sha1 in r231/inst/SHA1SUMS).

## 1. Designs (all RING(k, m) of r230/ring230.py plus level-0 movers w whose class can change later)
- A / B / C: one w per source (w_h, w_S). Every gated source option takes W-target w instead of the constant g, so its e-face value is
  class(w) + e and rises when w re-switches. w's Ξ-targets: A (z_m, y_m), B (y_m, z_m, X), C (the observers u, u2).
- D (staged): one w per gated source option X_l (Y_l). Its Ξ-targets are y_(⌈(l+1)m/k⌉), the rival chain at stage l, or X. So the options
  are meant to rise at different times during the rival's domino.

## 2. DATA (unit: one N5′-xi run on Γ3, states up to the first fallback; T3 as in R230)
| design | k, m | N | M | U | T3 | total |
| --- | --- | --- | --- | --- | --- | --- |
| RING (R230, baseline) | 8, 12 | 51 | 89 | 2 | 12 | 15 |
| A / B / C | 4, 6 / 8, 6 / 8, 12 | 29 / 29 / 53 | 49-95 | 6 | 6 / 6 / 12 | T3 + 3 |
| D | 4, 6 / 8, 6 / 8, 12 / 8, 24 | 34 / 42 / 66 / 114 | 59 / 83 / 119 / 191 | 9 / 17 / 17 / 17 | 6 / 6 / 12 / 24 | T3 + 3 |
- T3 = m on every instance: one domino, exactly as RING. nstd 0, fb 1 everywhere.
- Traces (k 8, m 12; unit: states):
  - A and C: both sources switch once to their first gated option at t = 1 and stay; each w switches at most once (at t = 1); chain B
    dominos toward S; chain A never runs.
  - D: every w switches at t = 1 and never again; h stays on X_2 from t = 1; S returns to Y_1 at t = 2; B dominos; A never runs.

## 3. DEAD RING3 (A, B, C, D) and the obstruction
- DEAD «a dynamic a-face makes RING multiply» for these four wirings. Killing instances: inst/ring3{A,B,C,D}_k8_m12.json (T3 12 = m).
- Obstruction (DATA part): the dynamic faces never move after t = 1. No w re-switches, and no source re-switches, during the rival's
  domino. So the stall the design needs (a source's non-current option rising mid-run) never happens.
- READING (not measured: Odd's face at the source gates was not logged): a raised e-face is the face Odd refuses (Odd takes the ⊴-smaller
  face, R123 LOC-GATE). Wiring a W-lower gadget under a source option raises that option's e-face from the start. The source's option
  values are then set by their β-faces (the static observers), and the dynamic part is never seen. In A / B / C, in addition, a shared w
  lifts all of a source's options together, the current one included, so no new improving option appears.
- Lean scope: four wirings, no climb. Depth 3 stays OPEN in general. This box adds the reason above, to be checked first by anyone
  who tries it: log Odd's face at the source gates.
