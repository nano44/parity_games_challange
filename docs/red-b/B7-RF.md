# B7: attack on candidate RF (ROOT-FIRST) — L-RED-B successor 8, 2026-11-14
Lane report (owner of this file: L-RED-B). Brief: Lead 2026-11-14 14:07Z, corrected 14:28Z, 14:52Z, 15:12Z. Status under D1 and
reading L43: **KILL CANDIDATE**, DATA on this lane's engines plus a lane mechanism; nothing here is a result until two referees
sign a proof or an instance passes an explicit polynomial bound. Labels: PROVED (lane, unrefereed) / DATA / READING / NOT
ESTABLISHED.

## 0. Verdict so far
- **KILL CANDIDATE (DATA).** On the rule-built family K^s_n (§4; |V| = 3n² + 3n + 1) RF from the stated start makes exactly
  **7·2^(n−1) − 2n − 3** iterations for every n measured: n = 1..9 on the Python engine under both tie rules, n = 10, 11, 12 on
  the Python engine, n = 2..17 on the C++ port (residual 0 everywhere). The run equals a CLOSED-FORM SCHEDULE iteration by
  iteration for n ≤ 9, and the law is arithmetic on that schedule (docs/red-b/B7-RF-sched.md §1-§2). Howard
  (switch-best everywhere) needs at most 10 iterations on the same games (n ≤ 7).
- K^s_n also survives, with the same count, two repairs of RF's dependency that wait for more vertices (B7-RF-sched.md §8).
- START. K^s_n is a kill of RF from σ_0 only: from the SPEC's default start S3 (every gate closed) RF needs n(n + 1)/2
  iterations on K^s_n (n ≤ 13). The padded family K^s3_n (two one-successor pads per gate; |V| = (2n + 1)²) has S3 = σ_0, and
  RF from S3 makes 7·2^(n−1) − 2n − 3 iterations on it for n = 1..12 (B7-RF-sched.md §9): the kill candidate OF THE SPEC.
- NOT ESTABLISHED: a refereed proof (a lane proof SKETCH with its gaps G1-G5 is in B7-RF-sched.md §3-§6; seven must-0
  counters of its facts are 0 on the real runs for n ≤ 8, §7 there); an instance beyond an explicit
  polynomial (by the law the first n with more iterations than |V|² is n = 19: 1,834,967 > 1,301,881; not run); a second,
  independent engine (asked of the Lead 15:14Z).
- SURVIVALS on the way (DATA, §3): a single-gate counter with a latch and a delay line: 5n − 2 iterations; the family K_n
  (K^s_n without the selectors' skip edges): (n³ + 3n)/2 iterations exactly for n ≤ 7.

## 1. The target, as relayed
RF in L-SI 57's words (Lead 14:52Z; S1 = valuation Ξ and Odd's optimal counterstrategy σ̄ for σ, S2 = the improving edges):
«CANDIDATE S8 = RF, exact: σ := S3. Loop: (Ξ, σ̄) := S1(σ); I := S2; stop if empty. Imp := improvable Even vertices, T(v) :=
improving targets. nxt(x) := σ(x) or σ̄(x); π(x) := vertex set of the play from x. D(v) := (π(σ(v)) ∪ ⋃_{w ∈ T(v)} π(w)) ∩ Imp ∖
{v}; Δ := (Imp, v → u for u ∈ D(v)). S := union of the strongly connected components of Δ with no edge into another component.
Every v ∈ S moves to the w ∈ T(v) maximising (Ξ(w), w). Output S5.»
My implementation (si7.py `root_first`, rf7.cpp): exactly this, with the start strategy given per instance (the family's own
start, §4.1) and two tie rules for equal best targets (larger id as in the pseudocode, smaller id as a control). On K^s_n no two
successors of a vertex ever have equal valuations (a 1-sink game with distinct priorities: the valuation of a successor contains
that successor), so neither the tie rule nor S1's choice among equal counterstrategies can matter there (READING, consistent
with the equal counts under both tie rules).

## 2. Engine and self-tests (all DATA; outputs in experiments/red-b/b7/out/, runner run_b7.sh)
- Source opened: O. Friedmann, arXiv 1106.0778v2 (PDF sha1 a63a9293fec00b8078f434bfab3ea1a66e55eaf9): §3 (PDF p. 4-6: node
  valuation, the three orders, optimal counterstrategy Lemma 3.1, improvement arena, Theorems 3.2 and 3.3, Algorithm 1), §4
  (locally optimizing policy), §5 (1-sink games), Table 4 and ι_{G_n} (p. 15), Fact 6.1, Figure 4, Theorem 6.14.
- si7.py: own engine (valuation in three stages: cycle nodes in ascending reward order, then the more relevant vertices in
  descending relevance, then distances). st7.py tests it against the DEFINITION: 3,000 random games n ≤ 7, every positional Odd
  strategy enumerated (23,195): bfval 0 bfmin 0; control B7_CTRL=1 fires (bfval 445). Full runs of howard and rf on 3,000 random
  games n ≤ 12: regions against own Zielonka zwrong 0, both strategies by own check swrong 0 (control fires 200 / 200).
- xoink.py: Oink 8fbf0a7 `--zlk`, `--tl`, Oink `verify` and experiments/harness/verify.py on G_n (n ≤ 5, both priority versions)
  and 400 random games: rz rt ov hv 0 (control 40 / 40 / 40 / 40); on K^s_3, K^s_5, K^s_7: 0.
- HOWARD on Friedmann's G_n from ι (gens7.py, my transcription of Table 4; version fig4 = Figure 4's injective priorities, top
  12n + 8 as Fact 6.1; version table4 = the table as printed, top 12n + 10): 8, 26, 62, 134, 278, 566 at n = 1..6 = 9·2^n − 10
  in both versions and both tie rules. (The paper's Theorem 6.14 states «at least 2^n»; 9·2^n − 10 is the fleet's measured
  count.)
- RF on G_n from ι (out/rf_lmcs.out): 5, 9, 12, 15, 18, 21, 24 at n = 1..7, i.e. 3n + 3 for n ≥ 2, in both versions and both
  tie rules: L-SI's row.
- rf7.cpp: C++ port. cmp7.py: iterations and final strategy equal to si7.py on 1,648 runs (K^s_n n ≤ 7, G_n n ≤ 5, 400 random
  games, both rules, both tie rules): idiff 0 sdiff 0; control B7_CTRL=4 fires.

## 3. Attack log before the candidate (what each attempt taught)
All counters below use Friedmann's simple cycle gate (Even d, Odd e, e → d | h, «closed» = d → e; an entry f of odd priority just
below the bonus h) in the layout of his counter: a higher bit is on the exit plays of the lower bits.
1. **Why Friedmann-type counters fail under RF** (READING, agrees with L-RED 71's trace relayed 14:35Z): a closed gate's play
   runs through its exit selector; when a higher bit closes, the selector and the gate become improvable together, the gate
   depends on the selector, the selector moves alone, and the gate's reset is no longer improving.
2. **Decoys / probes** (not run by me; L-RED 71's fact, which I had derived the same way): a probe target whose play passes the
   blocker returns to its owner, so it is improving iff it closes an Even-won cycle; it cannot be insignificant.
3. **RFC(n; D)** (rfc.py; one gate per bit, an exit latch k_i, a delay line of D Even selectors in front of each entry, a READER
   CHAIN of Odd vertices c_i → d_i | c_(i−1) as every gate's escape). Two things work under RF: (i) the delay gives a genuine
   reset (the latch is not yet improvable when the gate opens: RF's blind spot, the y-node of H_n in L-LIT's words); (ii) the
   reader chain makes a pending gate depend on every improvable gate below it, so the lowest open bit closes first. What fails:
   the latch's own move and the line's moves are INVISIBLE to the waiting bit (they are on no play of it), and the waiting bit
   closes in that one-iteration gap. DATA: RF 8, 13, 18, 23, 28, 33, 38 at n = 2..8 = 5n − 2 (D = 2). Survival, linear.
4. **K_n** (rfc2.py without `--skip`: one gate per bit AND context, so the exit of a closed gate is structural and no latch
   exists; a shared Even selector g_c in front of the gates of bit c). The reset is genuine and needs no timing. What fails: a
   selector is attracted to a PENDING gate of its bit (an open gate whose escape already sees the new high bonus), is blocked by
   that gate, and blocks the selector below it through a stale pointer; the bit below cannot close and the pending bit closes
   early. DATA: 2, 7, 18, 38, 70, 117, 182 at n = 1..7 = (n³ + 3n)/2 exactly. Survival, cubic.
5. An invalid probe (not recorded as DATA): a patched G_n whose priorities I rescaled by an even factor (parities destroyed);
   found by its D = 0 row disagreeing with G_n; discarded.

## 4. The candidate: family K^s_n
### 4.1 Rule (generator experiments/red-b/b7/rfc2.py, `build(n, skip=True)`)
Bits i = 1..n. ctx(i) := the list (x, n, n − 1, …, i + 1) («x» = no higher bit). One cycle gate (i, c) for every bit i and
every c ∈ ctx(i). Gate list L := (n, ctx(n)), (n − 1, ctx(n − 1)), …, (1, ctx(1)), in that order; below(i, c) := the reader C of
the next gate of L, and R after the last gate.
| vertex | owner | successors |
| --- | --- | --- |
| x | Odd | x |
| R | Even | x; f(i, c) for every gate |
| C(i, c) | Odd | d(i, c); below(i, c) |
| d(i, c) | Even | e(i, c) («close»); below(i, c) («escape») |
| e(i, c) | Odd | d(i, c); h(i, c) |
| f(i, c) | Odd | e(i, c) |
| h(i, c) | Odd | x if c = x, else g_c |
| g_i (i ≥ 2) | Even | f(i, c) and s(i, c) for every c ∈ ctx(i) |
| s(i, c) (i ≥ 2) | Odd | x if c = x, else g_c |
Priorities, all distinct: x 1; R 3; then p := 5 and for each gate in L order C = p, d = p + 2, e = p + 3, p += 4; then
g_2, …, g_n = p, p + 2, … (odd); then p is made even and for i = 1, …, n with K := n − i + 1 and q := the position of c in ctx(i)
counted from 0: s(i, c) = p + 1 + 2q, then p += 2K + 2, f(i, c) = p + 2q + 1, h(i, c) = p + 2K + 2q + 2, p += 4K + 2. So per
bit the skip penalties s lie below the entry penalties f, these below the bonuses h, and the band of bit i + 1 lies above the
band of bit i.
Start σ_0: d(i, c) → below(i, c) for every gate (all open), R → x, g_i → s(i, x).
Vertex numbering in the .pg files: x, R, then per gate in L order C, d, e, f, h, then for i = 2..n the s(i, c) in ctx order
followed by g_i. Sizes: |V| = 3n² + 3n + 1 (5 per gate, n(n + 1)/2 gates; n − 1 selectors; n(n − 1)/2 skip vertices; x, R);
|E| = 32, 65, 110, 167, 236, 317, 410, 515, 632 at n = 2..10. Odd wins every vertex (a 1-sink game in Friedmann's sense, §5 of
the source: DATA, every run ends with all cycle nodes = x).
### 4.2 DATA
| n | |V| | |E| | RF iterations | 7·2^(n−1) − 2n − 3 | engine |
| --- | --- | --- | --- | --- | --- |
| 1 | 7 | 11 | 2 | 2 | py (both ties) |
| 2 | 19 | 32 | 7 | 7 | py (both ties), C++ |
| 3 | 37 | 65 | 19 | 19 | py (both ties), C++ |
| 4 | 61 | 110 | 45 | 45 | py (both ties), C++ |
| 5 | 91 | 167 | 99 | 99 | py (both ties), C++ |
| 6 | 127 | 236 | 209 | 209 | py (both ties), C++ |
| 7 | 169 | 317 | 431 | 431 | py (both ties), C++ |
| 8 | 217 | 410 | 877 | 877 | py (both ties), C++ |
| 9 | 271 | 515 | 1,771 | 1,771 | py (larger id), C++ |
| 10 | 331 | 632 | 3,561 | 3,561 | py (larger id), C++ |
| 11 | 397 | 761 | 7,143 | 7,143 | py (larger id), C++ |
| 12 | 469 | 902 | 14,309 | 14,309 | py (larger id), C++ |
| 13 | 547 | 1,055 | 28,643 | 28,643 | C++ |
| 14 | 631 | 1,220 | 57,313 | 57,313 | C++ |
| 15 | 721 | 1,397 | 114,655 | 114,655 | C++ |
| 16 | 817 | 1,586 | 229,341 | 229,341 | C++ |
| 17 | 919 | 1,787 | 458,715 | 458,715 | C++ |
Files: out/ks_py_1_9.out, out/ks_py_low_1_8.out, out/ks_py_10_12.out, out/ks_cpp_2_17.out (each line carries the sha1 of its
.pg file); instances inst/Ks_n.pg and .start for n = 2..12 with inst/SHA1SUMS. Howard on K^s_n: 2, 4, 6, 8, 8, 9, 10 iterations
at n = 1..7 (RF is exponentially slower than the rule it restricts). Regions and both strategies of the RF runs on K^s_3,
K^s_5, K^s_7: equal to Oink's, verified (out/ks_xoink.out).
Against explicit bounds, by the law (exact integers; NOT run beyond n = 14): iterations > |V|² first at n = 19
(1,834,967 > 1,141² = 1,301,881); > |V|³ first at n = 34 (60,129,542,073 > 3,571³ = 45,537,538,411); > |V|⁴ first at n = 50.
### 4.3 The run for n = 2 and n = 3 (out/ks_trace_2.out, out/ks_trace_3.out)
n = 2, seven iterations: close (1, x) | R → f(1, x) | close (2, x) | R → f(2, x) and g_2 → f(2, x) | close (1, 2) | R →
f(1, 2) | reset (1, x). The closings of n = 3 in order: (1,x), (2,x), (1,2), (3,x), (1,3), (2,3), (1,2): the 2³ − 1 increments
of a binary counter, bit i closing in the gate whose context is the lowest set bit above i.
### 4.4 Mechanism (READING of the traces; schedule, proof sketch, counters and the repaired rule: docs/red-b/B7-RF-sched.md)
1. ORDER. An open gate rests on its escape, which runs down the reader chain; at C(i′, c′) Odd drops into every open gate (its d
   is odd, so the drop is cheaper for Odd) and into a closed gate whose value is below the rest of the chain. So a gate that
   could close depends on every improvable gate later in L, and RF closes the gate of the LOWEST open bit first: the least
   significant unset bit is the dependency sink.
2. STRUCTURAL CONTEXT. The exit of gate (i, c) is the fixed edge h(i, c) → g_c: nothing on a closed gate's play belongs to bit
   i, so no vertex that the gate depends on can refresh its exit. A gate (i, c) closes iff its exit is worth more than its
   escape, which happens when c is the lowest set bit above i.
3. GENUINE RESET. After bit j closes, R moves to f(j, ·) and every closed gate below j has escape > closed value: it opens.
   A gate (i, c) whose context bit c has no closed gate stays worthless because the selector g_c then rests on a skip edge
   s(c, ·) whose odd priority is above every bonus of the bits below c: a refreshed exit through a skip never beats the escape.
4. PROMPT SELECTORS. g_c prefers a skip to the entry of an open gate of its own bit (s < f), so it is never attracted to a
   pending gate (the failure of K_n, §3.4); it moves to a newly closed gate of its bit in the iteration in which R does, with
   nothing improvable on its plays.
5. COUNT (from the traces; residual 0 on fourteen sizes): 2^n − 1 closings, each followed by one iteration of R (the selector
   moves in the same iteration), plus 3·2^(n−1) − 2n − 1 iterations of resets and skip moves.

## 5. What is not claimed
Nothing about RF from other starts or on other families beyond the rows above; nothing about any other candidate; no proof; the
law is a fit with residual 0, not a theorem. The target (TARGET.md §2) is untouched by a kill of RF.

## 6. Reproduce
`bash experiments/red-b/b7/run_b7.sh OUT` regenerates every out/*.out except the long rows (needs Oink for the xoink stages and
g++ for cmp7; about 3 minutes); `python3 experiments/red-b/b7/runks.py 10 11` (4 minutes) and
`bash experiments/red-b/b7/runks_cpp.sh RF7BIN 2 14 OUTDIR` (C++; 4 minutes for n ≤ 14, 136 s of it at n = 14) give the long rows;
rf7 has `--ckpt FILE K` for a resumable run (state = σ and the iteration count). `python3 experiments/red-b/b7/b7sched.py 1 9`,
`b7facts.py 1 8` and `rfrep.py A|B ks 1 8` give the schedule test, the fact counters and the repaired rule's rows.
`python3 experiments/red-b/b7/rfc2.py N --skip --trace` prints a run with the switching and the waiting vertices per iteration.
