# R105: CONJECTURE SEG-COUNT is DEAD. One H-sink makes k intermediate switches at k deadlock steps of one REL segment: EXC = k − 1 at n = 10k − 1 (segcount_kill_n20; family mkk.py, pinned k = 3, 8)
L-RED successor 25 (Opus 5.5; D15/D18; Lead 2026-10-29 09:59Z box item 1: «CONJECTURE SEG-COUNT (L-SI, LAY §6) ... Attack it with
CONSTRUCTION ... a gadget with two deadlock steps in one segment charged to the same H-sink»). Written 2026-10-29 10:20Z (date -u).
Labels: DEAD / DATA / READING / OPEN. Not a TARGET.md claim; G-N5-TIME stays OPEN. The target is L-SI's statement, docs/si/N5-LAY-box27.md
§6 (claude/l-si): «in every maximal REL-admissible segment [a, b], b − a ≤ the number of Even vertices that switch in [a, b]».

## Summary
| item | label |
| --- | --- |
| segcount_kill_n20 (n 20): one fallback-free run [0, 4] = one maximal REL segment, 4 transitions, 3 switching Even vertices: EXC = +1; deadlock steps t = 0 and t = 2, both an intermediate switch of the SAME H-sink h | DEAD (SEG-COUNT) |
| family mkk.py K: segment [0, 2K], 2K transitions, K + 1 switchers, EXC = K − 1, n = 10K − 1; checked K = 2, 3, 4, 6, 8, 12, 16, 24; pins K = 3 (n 29, EXC 2), K = 8 (n 79, EXC 7) | DEAD (any SEG-COUNT + c); DATA |
| injectivity (b) of LAY §6 fails as predicted there: one H-sink, K deadlock steps, ONE joint final step | DATA |
| b − a ≤ n − 1 on REL segments is NOT touched (2K = (n + 1)/5); nor is L-WAVE′ | OPEN |
| every run starts from an explicit start pair (SPEC S3: "unless a start pair is given"); the S3 default start on the same game gives EXC 0 | caveat |

## 1. The gadget (designed by hand, no climb; experiments/red/seg/mk2d.py, then mkk.py)
Roles (vertex names are the PGSolver labels in the .pg files):
- z: Even self-loop, odd priority (41 in n20): the honest sink. Every Ξ-play ends there on the whole run (λ constant).
- A_1 > A_2 > A_3 (n20; A_1..A_{K+1} in the family): Odd self-loops with τ = self and small odd priorities (7, 5, 3): the W-cycles, lower is
  W-better for Even. Honestly Odd escapes: A_1 → B1 → w2 (into a W-sink, as 12 → 25 in seglast_kill_n29), A_2 → h, A_3 → G3 → h.
- h (Even, priority 38): the H-sink. Options z (start), A_1 (= c_1), C2 (= c_2), YH (final target).
- w1, w2 (Even): the W-sinks. w1: M0 (start) or A_2; w2: o2 (start) or A_3.
- C2 (Odd): τ(C2) = MP → w1 (W-route into A_2 once w1 is final); honest choice Bq → EQ → M2 (Odd avoids the Even-won cycle
  h → C2 → MP → w1 → A_2 → h once h sits at C2). C2 is on no honest play at b, so its σ̄ may change (REL constrains RO_b only).
- YH (Odd): τ(YH) = w2, σ̄(YH) = o2 (w2's OLD successor, as 19 → 26 in n29).
- Markers (priorities above z order the honest values): M2 50 (top, even), MP 48, B1 47, M0 46, G3 44, Bq 43.
Honest values of h's position (marker sets): z: {}; A_1: {B1, M2}; C2: {Bq, M2}; YH: {M2}. Thresholds: w1 is unblocked when Ξ(A_2) =
A_2 ⊕ Ξ(h) beats Ξ(M0) = {M0}, i.e. from h = A_1 on; w2 is unblocked when Ξ(A_3) = {G3} ∪ Ξ(h) beats Ξ(o2) = {M2}, i.e. from h = C2 on
(B1 > G3 > Bq). C2 enters h's arena only after w1 is final (before: Ξ(C2) = {MP, M0} ≺ {B1, M2}; after: {MP} ∪ {B1, M2} ≻ {B1, M2}).
τ-stability (I_τ = ∅ at every state): each Odd escape leads to an Even vertex from which Even's best reply to τ returns to a W-cycle
at least as low (EQ, o2 have an edge back to h; h's even priority 38 marks the return as worse for Odd). That is the n29 device.

Trace (n5b SPEC; experiments/red/seg/tr.py; I_τ = ∅ at all 7 states, λ constant on [0, 4], changes at 4 → 5):
| t | switches (L = last in [0, 4]) | W-sinks (σ, target, ready) | H-sinks | reading |
| --- | --- | --- | --- | --- |
| 0 | h: z → A_1 (intermediate) | w1 (M0, A_2, no), w2 (o2, A_3, no) | h | DEADLOCK 1: h takes the W-best arena edge (loop 7) |
| 1 | w1: M0 → A_2 L | w1 ready, w2 no | h | w1 unblocked by h's honest rise to {B1, M2} |
| 2 | h: A_1 → C2 (intermediate) | w2 (no) | h | DEADLOCK 2: C2 is in h's arena only now (Ξ rose through w1), W-route loop 5 |
| 3 | h: C2 → YH L, w2: o2 → A_3 L | w2 ready | h | JOINT final (LAY §6 Corollary JOINT) |
L = 4 transitions; switchers h, w1, w2: EXC = 4 − 3 = +1. The single H-sink h carries both deadlock steps, so LAY §6's injectivity (b)
fails exactly as stated there («(b) fails if one H-sink makes two intermediate switches at two deadlock steps while it is the only
H-sink; no instance shows this yet»). The sink lemmas (SINK-OFF, READY, W-STICK) hold at every step (L-SI's wsink.py: WSOFF, HSOFF, HSR,
WSL PASS; WSR and SS fail at t = 0, 2, the deadlock steps).

## 2. The family (experiments/red/seg/mkk.py K)
Level i = 2..K repeats the C2 block: C_i (τ → MP_i → w_{i−1}, honest → Bq_i → EQ_i), W-sink w_i (old successor Bp_i → M2 for
2 ≤ i < K, "ok" for i = K), W-cycle A_{i+1} (escape G_{i+1} → h). Honest values: h at c_i = {β_i, M2}; marker ladder below M2:
G_2 > β_1 > (β′_2 > G_3 > β_2) > (β′_3 > G_4 > β_3) > ... > MP's > M0 (odd β, even G). Run: h makes K intermediate switches at
t = 0, 2, ..., 2K − 2; w_i is final at t = 2i − 1; t = 2K − 1 is the joint final (h → YH, w_K → A_{K+1}).
DATA (segchk.py + xeng.py + L-SI's segsw.py, all three agree at every K):
| K | n | segment | transitions | switchers | EXC | deadlock steps |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 19 | [0, 4] | 4 | 3 | 1 | 2 |
| 3 | 29 | [0, 6] | 6 | 4 | 2 | 3 |
| 4 | 39 | [0, 8] | 8 | 5 | 3 | 4 |
| 6 | 59 | [0, 12] | 12 | 7 | 5 | 6 |
| 8 | 79 | [0, 16] | 16 | 9 | 7 | 8 |
| 12 | 119 | [0, 24] | 24 | 13 | 11 | 12 |
| 16 | 159 | [0, 32] | 32 | 17 | 15 | 16 |
| 24 | 239 | [0, 48] | 48 | 25 | 23 | 24 |
So no bound "b − a ≤ switchers + c" holds; the excess is (n − 9)/10. The counts are transitions (the family's one per-vertex count, h's
K + 1 switches, is the intrinsic thing here: one Even vertex switches K + 1 times inside ONE maximal REL segment).

## 3. Verification (experiments/red/seg/vrun.sh; outputs vrun_*.txt in the same directory)
| pin | sha1 (game / start) | n5b SPEC = n5.py (L-NEW driver, L-SI si.py) states | Oink zlk + strategies (both solutions) | L-SI relcheck.py at each deadlock | L-SI segsw.py |
| --- | --- | --- | --- | --- | --- |
| instances/segcount_kill_n20 | 2783f64d82f271ebc9a26b470b26a9938fd5295c / 97ba6b298917676e10cb209e21f49ee442b73686 | identical (7 states, 6 iterations, 0 fallbacks) | OK, OK | t = 0, 2: one run (0, 4), REL segments [(0, 4)], REL-admissible, REL fails at a − 1 (a = run start), GEN_W failures 0 | SEGCOUNT FAIL, EXC 1 |
| instances/segfam_k3_n29 | 0d242a9b99f81b1f5dc91e32da1211d12c426982 / c0f9d1af61d74af696e6b378f33279968b448bd3 | identical (9 states) | OK, OK | t = 0, 2, 4: run (0, 6) = one REL segment, GEN_W 0 | SEGCOUNT FAIL, EXC 2 |
| instances/segfam_k8_n79 | ddb67effe8a6021a5bf57eee43b4b9ee7afbfdc2 / eb865b58554f6fe6db3f7409d64b5b61a4eeee6d | identical (19 states) | OK, OK | t = 0, 8, 14: run (0, 16) = one REL segment, GEN_W 0 | SEGCOUNT FAIL, EXC 7 |
- My own checker (segchk.py) is written from LAY §0-§1 and GRUN §4 on n5b only (no lay/ or lwp/ import): runs = maximal (λ_Ξ, τ)-constant,
  fallback-free stretches; maximal REL segments cut from each run's end (σ̄ constant on RO_b, CW_b / CH_b cycles kept); it reproduces L-SI's
  seglast_kill_n29 table (t = 2: only 1: 9 → 23, W-sink 25 unready; t = 3: joint) before being used here.
- L-SI's relcheck.py cuts the same segments from n5b alone; L-SI's segsw.py (its own engine and cutting) gives the same EXC.
- Two engines: n5b (L-COMP, SPEC mode) and experiments/new/n5.py (L-NEW's driver on L-SI's si.py valuations): the full (σ, τ) state
  sequences are equal (xeng.py; also on seglast_kill_n29).

## 4. Readings and what is left
- READING: SEG-COUNT's proof route (LAY §6: charge each deadlock step to an H-sink that later finalizes jointly with its W-chain) cannot
  be repaired by counting H-sinks: the H-sink here waits for a SEQUENCE of W-sinks in series, and each one it waits for is unblocked by
  a separate intermediate switch of the H-sink itself. LAY §6's "why a second deadlock is hard" reading is right about the mechanism
  (c_{i+1} enters h's arena only after w_i finalizes, because Ξ(c_{i+1}) rises THROUGH w_i) and wrong about its cost: the cycle that this
  creates when h moves to c_{i+1} is Even-won, so Odd's honest choice at c_{i+1} simply leaves it (c_{i+1} is off RO_b), at no REL cost.
- Per segment: b − a = 2K, switchers K + 1, |E_b| ≥ K + 1; so b − a ≤ 2|E_b| (SINK-GROW's form, LAY §2) is not contradicted here, and
  b − a ≤ n − 1 holds (2K vs 10K − 1). OPEN: is b − a ≤ 2·(switchers) − 1, or ≤ |U^W_a| + |U^H_a|, on REL segments (not measured here).
- Caveat (start): the runs use explicit start pairs (allowed by SPEC S3 and used by L-SI's own "pinned starts" corpus). From the S3
  default start on segcount_kill_n20, EXC is 0. A family whose kill segment arises from the S3 start is not built (not needed for the
  statement as written; it would be stronger).

## DONE / FINDINGS / NEEDS
- DONE: experiments/red/seg/ (segchk.py own checker; tr.py named trace; xeng.py two-engine state compare; vrun.sh; mk2d.py design;
  mkk.py family); pins instances/segcount_kill_n20, segfam_k3_n29, segfam_k8_n79 (+ .start); vrun_*.txt.
- FINDINGS: (1) DEAD: CONJECTURE SEG-COUNT (segcount_kill_n20, EXC 1; two engines, Oink, L-SI's own tools agree). (2) DEAD: any
  "b − a ≤ switchers + c": family EXC = K − 1 at n = 10K − 1. (3) DATA: LAY §6 injectivity (b) fails: one H-sink, K deadlock steps.
  (4) OPEN: b − a ≤ n − 1 on REL segments without (H4′_rel) (family 2K ≈ n/5); L-WAVE′.
- NEEDS: none from the owner.
