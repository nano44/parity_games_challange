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

## 3. Addendum (Lead 18:10Z: PV_rel with a relevance under which SF-RED (b) holds; written from 18:20Z by date -u)
### 3.1 Definition: F-relevance via greedy one-player segments
- The Lead's candidate ("changes Iσ, the arena H, or Ξ at some vertex reachable in G_σ") counts every σ̄-change. S4a′'s arena H fixes
  each Odd vertex to σ̄(v), so H changes whenever σ̄ does; and fcobsP's o is on E0's play, so Ξ(E0) changes. I use instead the property
  SF-RED's proof actually needs.
- Segments. Put a_0 := 0. Given a segment start a, set σ̄*_a := σ̄(σ^(a)) and G*_a := G_σ̄*_a. The segment is [a, b], with b the least
  j > a such that F(σ^(j)) ≠ N5's iteration on G*_a from (σ^(j), σ̄*_a), restricted to Even. If there is no such j, b = p. The next
  segment starts at b.
- SBC_G := (number of segments) − 1. A segment boundary b is an F-RELEVANT σ̄-change.
- Per vertex: Gflips(u) := #boundaries b with σ̄(σ^(b))(u) ≠ σ̄*_a(u), where a is the start of the segment that b ends.
- Mirror on G^d for τ. Computed by experiments/new/box59/sbcg.py.
### 3.2 Theorem SF-RED-G (PROVED, lane; no assumption beyond P-N5-SF)
(a) Every segment has b − a < (n + m + 1)(n² − n + 1).
(b) #σ − 1 < (1 + SBC_G)(n + m + 1)(n² − n + 1); mirror for τ; I ≤ (#σ − 1) + (#τ − 1) by SF-TERM.
(c) SBC_G ≤ SBC and SBC_G ≤ #σ − 1. So N5-SF is polynomial on a class iff SBC_G (both sides) is.
Proof.
(a) For a ≤ j < b, F(σ^(j)) equals N5's step on G*_a from σ^(j): by the definition of b. Since G*_a is one-player (Odd has out-degree 1),
this is F_{G*_a}(σ^(j)): N5-SF's map on the game G*_a (P-N5-SF ONE-PLAYER (b) on G*_a, where G*_a's best reply is σ̄*_a itself). So
σ^(a), …, σ^(b) are consecutive distinct σ of N5-SF's run on G*_a from σ^(a), by DECOUPLE on G*_a. In that run SBC = 0, so SF-RED (b)
on G*_a gives a length < (n + m + 1)(1 + LAM) ≤ (n + m + 1)(n² − n + 1). SF-RED holds from any start σ_0, as its proof uses no
property of S3.
(b) Sum (a) over the 1 + SBC_G segments. Consecutive segments share their endpoint, so the transitions add up.
(c) At a boundary b of the segment starting at a, σ̄(σ^(b)) ≠ σ̄*_a. Otherwise G*_a = G_σ̄(σ^(b)), and P-N5-SF ONE-PLAYER (b) would
make F(σ^(b)) equal N5's step on G*_a. So σ̄ changes at some transition in [a, b). These intervals are disjoint for distinct
boundaries, which gives SBC_G ≤ SBC. And SBC_G ≤ p = #σ − 1 is trivial. The equivalence follows from (b) and SF-RED (c). □
Remark (not to sign).
- The per-segment constant (n + m + 1)(n² − n + 1) is cruder than SF-RED's λ-refined count. G*_a's LAM is not the true run's LAM.
- sbcg.py asserts at every boundary that the new segment's first step agrees (ONE-PLAYER (b)). It never fired.
### 3.3 DATA (SPEC S3 default start everywhere, NOT the corpus's pinned starts)
- box59/sbcg.lst, 719 games: the 716 of rel.lst, fcobsP_3 / 4, fcobs_6 (sha1 e6ad362a05d5 = L-RED's). Log box59/sbcg_all.txt.
- 719 PASS: no segment reached the bound (a), and the ONE-PLAYER assert never fired. SBC_G < SBC on 419 games.
| game | n | orbit | SBC | SBC_G | SEGMAX | max Gflips |
| --- | --- | --- | --- | --- | --- | --- |
| fc_3 / fcobs_3 / fcobsR_3 / fcobsP_3 | 85-90 | 122 | 9 / 111 / 111 / 111 | 8 (all four) | 27 | 5 |
| fc_4 / fcobs_4 / fcobsR_4 / fcobsP_4 | 110-115 | 216 | 16 / 202 / 202 / 202 | 15 (all four) | 33 | 7 / 9 / 9 / 9 |
| fc_6 / fcobs_6 | 160 / 163 | 521 | 36 / 498 | 35 / 35 | 45 | 11 / 19 |
| fc_5, fc_7, fc_8 | 135, 185, 210 | 347, 744, 1022 | 25, 49, 64 | 24, 48, 63 | 39, 51, 57 | 9, 13, 15 |
| so_sor5_n24 | 24 | 23 | 22 | 8 | 9 | 8 |
- SBC_G is immune to all three observer gadgets: it equals plain fcN's N² − 1.
- Gflips is not fully immune. o is charged when its change happens to coincide with a real boundary (fcobs_6: 19 vs 11), but it is
  capped by SBC_G.
- Maxima over the 719 games: Gflips(u)/n 0.708 and SBC_G/n 0.708 (red/xing/instances/j10_n24.pg).
- CONJECTURE PV_G (OPEN): Gflips(u) ≤ n for every Odd u, game and start; mirror for τ. DATA: 0 / 719 violations, max 0.708n.
  - Consequence: SBC_G ≤ k_O·n ≤ n² (each boundary has some u with a changed reply), so by SF-RED-G I < 2(1 + n²)(n + m + 1)(n² − n + 1).
  - PV_G is falsified only by σ̄-changes that alter F's step. An observer alone cannot do it.
- CONJECTURE PV (raw) stays DEAD (§2).

## 4. The loop question (Lead 18:10Z (2), L-RED R115 §2c: gated nesting collapses): READING, not proved
N-COND asks for a stale intermediate on the lower block's escape route. Its route to the upper event passes through a loop L =
d_A → s_B → … → d_A. Under the run's (σ, σ̄), such a loop is in one of three cases:
- (L1) Top priority of L even and L closable by Even alone: Even closes it in one F-step. Every vertex routed into L changes its cycle
  node: a λ-change, and LAM ≤ n(n − 1) over the whole run (P-N5-SF SF-RED (b)). This is the observed collapse (LAM = 1, every A cycle
  closes at once). The lower counter's timing is gone because its lane walks now end in a cycle node instead of the sink.
- (L2) Top priority of L odd, L closable by Even alone: Even never closes it. Every Even vertex on L leaves L at its best exit, so the
  route through L is not used. No intermediate is stale through L, and the event is prepared as in fcN's re-sets.
- (L3) An Odd vertex u_L on L can break it. Then whether L is used is Odd's best reply at u_L. The staleness becomes a σ̄-change at u_L,
  and it is F-relevant iff it changes F's step. So each stale-through-loop event costs a λ-change (L1) or an F-relevant σ̄-change at a
  break vertex (L3). It is free only in (L2), where it does not happen.
- Structural half of the nesting bound, as a CONJECTURE (LOOP, OPEN): per upper-block event, a lower-block reset via N-COND costs
  ≥ 1 λ-change or ≥ 1 F-relevant σ̄-change at a loop-break vertex. Then nesting multiplies the degree only if the break vertices
  themselves flip superlinearly in F-relevant ways, which is PV_G's territory.
- Not proved: L1-L3 assume L is a simple loop whose closing is decided either by Even alone or by one Odd vertex. Several Odd break
  vertices, or loops sharing vertices, are not covered.

## DONE / FINDINGS / NEEDS (addendum)
- DONE: box59/sbcg.py, sbcg.lst, sbcg_all.txt, out/fcobs_6.pg; §3-§4; check.sh "Box 59" pins sbcg on fcobsP_3.
- FINDINGS: (1) PROVED (lane): SF-RED-G. F-relevance via greedy one-player segments; I polynomial iff SBC_G is; no LOC needed.
  (2) DATA: SBC_G is immune to the observer gadgets (fcobs / R / P: SBC_G = N² − 1 = plain fcN). 719 / 719 PASS.
  (3) CONJECTURE PV_G (Gflips ≤ n): 0 / 719, max 0.708n (j10_n24); it would give a polynomial I bound. (4) READING / CONJECTURE LOOP:
  a nesting loop costs a λ-change (L1: the observed collapse), is never used (L2), or turns into F-relevant σ̄-changes at its Odd break (L3).
- NEEDS: none from the owner. Lead: relay L-RED's Odd-break / odd-top nested families. I will run sbcg.py (SBC_G, Gflips, I) on them.

