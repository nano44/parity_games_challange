# N5-PV (box 60): the §4 proof plan for PV fails at step (iii); PV and its play-restricted form are DEAD
L-NEW successor 34 (Opus 5.5), D14 / D18, Lead reading L40. Lead's brief 2026-10-29 17:56Z (BOX 60: the proof plan for PV, or the
smallest counterexample). Written 2026-10-29 from 18:08Z (date -u). Working note, unrefereed, not a TARGET.md claim. Labels: PROVED (lane) /
DATA / READING / DEAD / OPEN. Symbols as in docs/new/N5-FC-box59.md. All runs from the SPEC S3 default start (NOT the corpus's pinned
starts), engine experiments/new/box54/n5sf.py.

## Summary
- The brief crossed my 18:05Z report: PV (each Odd vertex ≤ n best-reply changes) was already DEAD (N5-FC-box59.md §6.1) by L-RED's
  observer gadget. Smallest counterexample: experiments/new/box59/out/fcobs_3.pg (sbev.py 3 --drop fc,obs; n 88, sha1 719d04830887).
  Odd o makes 108 > 88 changes, and the σ-run is fc_3's (122 states).
- New here: the natural repair PV-PLAY is DEAD too. It counts a flip of u only when u lies on a (σ, σ̄)-play from an Even branching
  vertex, before or after the step.
  - It survives the plain observer: playmax 5 on fcobs_3, 7 on fcobs_4.
  - box59/reach2.py adds Z (top odd priority, self-loop) and Even E0 → {o, Z}. Even always plays E0 → o, so o is ON E0's play at every
    step, and nothing points to E0.
  - fcobsP_3 (n 90, sha1 df9fcc64bafd): o's on-play flips 108 > 90. fcobsP_4 (n 115, sha1 8c3efacd1f90): 198 > 115.
  - The run is unchanged (122 / 216 states). relcheck.py PASS (so SF-RED-R holds there, with SBC^R = 111 / 202).
- The proof plan of N5-FC §4 fails at step (iii). Plan: (i) flips charged to records, (ii) injectively, (iii) ≤ n records per chain.
  Detail in §1.

## 1. Where the plan breaks, and where the T48 barrier bites (READING, backed by the DATA above)
- The charging candidate: each flip of u is charged to a "record" on the value chain of one of u's successors, i.e. a step at which
  Ξ(successor) improves. Records per chain ≤ n by MONO-XI + injective rewards.
- MONO-XI + injective rewards bound by n only the COARSE records: changes of the cycle node, or of the most relevant path vertex.
  - Proved in N5-FC §4 (iii): the top only rises once even. ≤ n changes per cycle node.
  - A flip, however, needs only the ORDER of Ξ(a) and Ξ(b) to change. Their decisive vertex can be arbitrarily low.
- The observer o compares P0 (best even lane entry) with P1 (best odd lane entry). Each lane step improves one of them at a low path
  vertex, so the argmin alternates with the run's clock: Θ(I) flips, with ≤ 2 coarse records.
  - FLIP-REC°'s death (so_sorl_n32: 22 flips, 0 top changes) is the same phenomenon in a natural game.
- The fine records (every improvement of Ξ(successor)) are not bounded by n. There are up to I of them; MONO-XI bounds them only by the
  2^n-element order. That is exactly T48's barrier.
  - Monotone values plus an argmin over a fixed successor set permit as many argmin changes as the values have improvements.
  - In a parametric-shortest-path family that is n^Ω(log n) (T48 §1.3, L-LIT's reading).
  - So step (iii) fails for fine records, and step (ii) fails for coarse ones (FLIP-REC° DEAD).
- Why LATENCY does not rescue it: o's flips are not caused by any F-decision. They are a read-out of the run.
  - Any bound on σ̄-changes must exclude vertices whose choice F never acts on.
  - fcobsP's o is on a play and its value is read by S2 at E0 (the edge (E0, Z) is compared against it at every step). Yet o never
    changes F's step.
  - The only relevance that excludes it is "the σ̄-change changes F(σ)", and counting those is counting F's steps (READING).
- Consequence for SF-POLY (READING): SBC is a proxy that adversarial gadgets inflate at will. A per-vertex record argument cannot prove a
  polynomial bound on it, because the bound is false. The quantity to bound is the step count I directly (cubic on fcN, N5-FC §6.3),
  e.g. as stretch length × SBC^R with a NON-adversarial relevance.

## 2. Status of the box-59/60 conjectures
| item | status |
| --- | --- |
| PV (raw) | DEAD, fcobs_3 (719d04830887): 108 > 88 |
| SBC ≤ k_O·n | DEAD in growth: o's flips track I ~ N³ (fcobs_3 / 4: 108, 198); k_O·n ~ N² |
| PV-PLAY | DEAD, fcobsP_3 (df9fcc64bafd): 108 > 90; fcobsP_4 (8c3efacd1f90): 198 > 115 |
| SF-RED-R | PROVED (lane, under ASSUMPTION LOC), N5-FC §6.2; relcheck PASS on fcobsP_3 / 4 as well |
| per-chain coarse records ≤ n | READING (argument in N5-FC §4 (iii)), not refereed |

## DONE / FINDINGS / NEEDS
- DONE: box59/pvplay.py, box59/reach2.py, box59/out/fcobsP_3 / 4.pg; this note; check.sh "Box 59" pins pvplay on fcobsP_3.
- FINDINGS: (1) PV DEAD, smallest counterexample fcobs_3 (n 88, 108 flips). (2) PV-PLAY DEAD, fcobsP_3 (n 90, 108 on-play flips), with
  the run unchanged. (3) The plan fails at (iii): only coarse records are ≤ n, and flips need only fine ones. That is the T48 barrier
  exactly. (4) READING: SF-POLY must bound I directly; SBC in any form is inflatable.
- NEEDS: none from the owner. Lead: route the next box. My proposal: bound the R-stretch length × the number of stretches with
  relevance = "changes F(σ)", attacked through LATENCY on fcN-like lanes.
