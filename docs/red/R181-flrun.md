# R181 Real N5 FL run length against n: L_FL does not grow (8 at n = 32 and 48, 7 at n = 64); gating changes inside the longest run do (48 → 156 → 240), so FL-ANCHOR's bound is far from tight on these games, and no super-linear L_FL was found (L-RED successor 42)
Started 2026-11-01 15:30Z (Lead GO 15:06Z, item 2, date -u). Brief: «climb the real N5 FL run length L_FL, with gating changes per run as
a second score (ODIFF Ξ, W-cycle-node Ξ). Measure both against n = 16-64 … Report the L_FL / n and gating / n trends, and pin anything
super-linear.» Labels: DATA, READING. Not a TARGET.md claim. G-N5-TIME stays OPEN. Nothing super-linear, so no kill pin.

## 0. Answer
- L_FL (the longest run of consecutive FL transitions in N5's own run, default S3 start) did not grow with n in any climb:

| n | start of climb | score | best L_FL | gating changes in that run | L_FL / n | gating / n |
| --- | --- | --- | --- | --- | --- | --- |
| 16 | random | 1000·L_FL + gate | 1 | 0 | 0.06 | 0 |
| 32 | u23sw64_n32 | 1000·L_FL + 30·FL_total + gate | 8 (the seed's) | 48 | 0.25 | 1.5 |
| 32 | odxi_many_n32 | same | 3 | 38 | 0.09 | 1.2 |
| 48 | u23sw64_n32 + random 16 | same | 8 | 156 | 0.17 | 3.3 |
| 64 | u23sw64_n32 + random 32 | same | 7 | 240 | 0.11 | 3.8 |
| 48 | fl_s48 | 1000·L_FL + gate, 15k more steps | 8 | 192 | 0.17 | 4.0 |
| 64 | fl_s64 | same, 12k more steps | 7 | 294 | 0.11 | 4.6 |

- Gating changes per run (ODIFF Ξ-changes plus Ξ-changes at W-cycle nodes, summed over the run's transitions) grow with n. But they
  grow by MANY vertices changing at the SAME transition: 240 changes inside a 7-transition run, ODIFF up to 33. The run does not get
  longer.
- So in these data, FL-ANCHOR's (n + m)(1 + gating changes) is loose by orders of magnitude. The climb finds gating easily and run
  length not at all.
- L_FL ≤ 8 everywhere, including the 813-pair corpus (R177: longest 8, u23sw64_n32).
- The R178 champions were not transplanted. A faithful transplant needs a stable two-face gate per option, which is the open
  stabiliser question (R177 §5); a naive build would not keep σ̄ and τ fixed. Not attempted.

## 1. Definitions (red/r181/flrun.py)
- FL transition j as in R179: no fallback; τ and σ̄ unchanged; σ changes; W (against τ_(j−1)) unchanged at every vertex.
- A run = maximal consecutive FL transitions; L_FL = its length (the longest run; ties broken by more gating).
- Gating changes of a run = Σ over its transitions of #{ODIFF o : Ξ_j(o) ≠ Ξ_(j−1)(o)} + #{W-cycle nodes c : Ξ_j(c) ≠ Ξ_(j−1)(c)}.
  This is FL-ANCHOR's gating data as the Lead relayed it (box 132), measured per transition.

## 2. Pins (each: startck OK, Oink 8fbf0a7 --zlk + verify «OINK OK», --tl + verify exit 0, xeng identical; lassock = odxi)
| pin | sha1 (12) | n | m | K | L_FL | gating in that run | FL transitions | ODIFF Ξ-changes (odxi = lassock) | max ODIFF |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fl_s48 | 3c501c3b1951 | 48 | 158 | 27 | 8 | 156 | 10 | 114 | 21 |
| fl_s64 | 8882dc61c5bb | 64 | 244 | 27 | 7 | 240 | 8 | 180 | 33 |

## 3. Pure L_FL climbs from the n = 48 / 64 champions
- red/r181/climb181p.py (score 1000·L_FL + gate) from fl_s48 (15k mutations) and fl_s64 (12k mutations): L_FL stays 8 and 7; gating
  in the longest run rises to 192 and 294 (p48.pg, p64.pg in out/, not pinned). L_FL did not move in 27k mutations.

## 4. READING
- Gating changes come in bulk: one W-flat Ξ-improving move high on a shared Ξ-play changes Ξ at every ODIFF vertex whose σ̄-play passes
  it. So «gating changes per run» can be Θ(n) per transition without any extra FL length. A sharper anchor quantity would count
  transitions with a gating change, not (transition, vertex) pairs. In these data it is ≤ L_FL by definition and ≤ 8.
- What a long real FL run needs (R177-R180): even W-cycles, D-cycles through ODIFF gates, Ξ-availability that the idealised model
  already cannot supply beyond about 2.7 per mover, and stabilisers. Why the real
  climbs never move L_FL past the seed's 8 is not diagnosed here; my guess (unchecked) is the stabiliser requirement.

## 5. Files
- red/r181/flrun.py, climb181.py (score with FL_total), climb181p.py (pure), out/ (logs, champions), instances/ (2 pins, starts,
  pins.sha1). check.sh block «R181».
