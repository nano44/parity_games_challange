# (P*) and (P_strict) are false: a one-player family with 2^n - n - 1 Ω-strict single-switch improvements (L-NEW box 8)
L-NEW successor 3, Opus 5.5 (D8). Started 00:32Z, written 00:40Z (date -u), 2026-10-19. Status: L-NEW READING with
computer check. NOT refereed. Target: the premises in REFEREE R-N5K9 (claude/referee 160db1d) §(2) (P*) and §(3b) (P_strict).

## Statement
For every n ≥ 1, the one-player parity game CDAG_n below (n + 1 vertices, n(n+1)/2 + 1 edges, priorities ≤ 2n, every vertex
owned by the improver ⊕, so the condition "every ⊖ vertex has out-degree 1" holds vacuously) has a sequence
ρ_0, …, ρ_L of ⊕-strategies with L = 2^n − n − 1, where each ρ_{j+1} = Switch_{I_j}(ρ_j) for a ONE-element set I_j of VJ00
improvements of ρ_j (BRICS RS-00-48 §4.4 (2)), and every step is Ω-strict (Ω_{ρ_{j+1}} ≠ Ω_{ρ_j}).
So no C satisfies (P*) (L ≤ C n³) or (P_strict) (number of Ω-strict steps ≤ C n³). K9's route through either premise is
closed. VJ00 Prop. 7.4 on an "every policy" reading is false. On the switch-all reading it is untouched: switch-all from ρ_0
solves CDAG_n in 1 step.
This does NOT kill N5. N5 (and SSI) solve CDAG_n in 1 iteration (n = 8, 12, 16; n5.py output below). The family attacks the
premise K9 used, not N5's own subset sequences.

## The game CDAG_n
- Vertex 0 has priority 0 and a self-loop (the sink).
- Vertex v = 1..n has priority 2(n + 1 − v), and edges to every u < v.
- Every vertex is ⊕ (Even). Relevance = priority, so a smaller index means more relevant (among 1..n).

## The chain
gen(1) = []. gen(m) = [(m, m−1)] followed by gen(m−1), where every step (m−1, u) of gen(m−1) is replaced by the three steps
(m, u), (m−1, u), (m, m−1). Start ρ_0: every vertex → 0. A step (x, u) means: switch x to u.

## Proof (reading)
Valuations:
- Under any ρ, the play from v follows a decreasing path to 0 and stays there. So VJ00's cycle node is 0 (least relevant),
  and the path set P_ρ(v) is the set of vertices on that path, 0 excluded.
- Different paths from v have different vertex sets (the order on a path is forced). So the length component never decides.
- All priorities are even, so VJ00's order is: P ≺ Q iff the most relevant vertex of P Δ Q, i.e. min(P Δ Q), lies in Q.
- Edges go downward, so P_ρ(v) depends only on ρ restricted to {1..v}. In particular, vertices < m never see vertex m.

Claim, by induction on m (in CDAG_n, for m ≤ n): gen(m), run from ρ_0, consists of improving single switches, and:
- (a) P(m) changes only at m's own switches;
- (b) m switches 2^(m−1) − 1 times;
- (c) |gen(m)| = 2^m − m − 1.

The steps of gen(m):
1. The first step (m, m−1): P(m) goes from {m} to {m, m−1}. This is improving, because the difference {m−1} lies in the new set.
2. Invariant: between the blocks below, m points to m−1. It holds after step 1 and after each triple.
3. A step (x, u) of gen(m−1) with x < m−1 stays improving (m is invisible to x). P(m−1) does not change, by (a) for m−1. So P(m)
   = {m} ∪ P(m−1) does not change either.
4. A step (m−1, u) of gen(m−1) becomes the triple. Before the triple, P(m) = {m, m−1} ∪ T', where T' = P(ρ(m−1)). Let T = P(u),
   with T, T' ⊆ {1..m−2}. The step (m−1, u) is improving in gen(m−1), so T' ≺ T, i.e. min(T Δ T') ∈ T.
   - (m, u): the new P(m) is {m} ∪ T. The difference from the old set is (T Δ T') ∪ {m−1}, whose minimum is min(T Δ T') ∈ T.
     So the step is improving.
   - (m−1, u): improving as in gen(m−1), since m is invisible to m−1 and to u.
   - (m, m−1): P(m) goes from {m} ∪ T to {m, m−1} ∪ T. This is improving, because the difference {m−1} lies in the new set.
So (a) holds for m.

Counts:
- own(m) = 1 + 2·own(m−1), so own(m) = 2^(m−1) − 1.
- |gen(m)| = |gen(m−1)| + 1 + 2·own(m−1) = 2^m − m − 1.

Strictness: each step strictly raises Ω at the switched vertex, so every step is Ω-strict.

## Computer check (DATA)
- experiments/new/p_strict/cdag.py n checks every step with L-SI's VJ00 engine (experiments/si/si.py, read-only; the engine
  REFEREE-2 cross-checked in R2-N5T §5). It checks that (x, u) ∈ Engine.improving(ρ), that Ω_{ρ'} ≥ Ω_ρ everywhere and > somewhere,
  and that no improvement is left at the end.
  - PASS for n = 2, 3, 4, 5, 6, 8, 10, 12.
  - Chain lengths: 1, 4, 11, 26, 57, 247, 1013, 4083, which equals 2^n − n − 1 in every case.
- Independent second implementation, experiments/new/p_strict/dagchain.cpp: its own valuation, Σ ±2^rank over the path. It finds
  the longest single-switch chain over all starts by DP, and anneals over one-player sink DAG games.
  - Complete DAGs reach 26 / 57 / 120 at n = 5 / 6 / 7, which is 2^n − n − 1. That is also the ceiling Σ_v (2^(v−1) − 1).
  - Annealing on out-degree ≤ 3 gives 10, 21, 40, 72, 125 at n = 4..8.
  - The family above was read off its DP trace (dag_trace.py, n = 5).
- Instances: experiments/new/instances/cdag/cdag_N{4,6,8,10,12,16}.pg. sha1:
  - N4 ae045afc676a94d4522f819da305382f85a8ffdd
  - N6 739850de977bfe378af15e4c29e11dfebddd76a3
  - N8 4a86fa06cabd3b4365916590ff0588a6812db1de
  - N10 19ddc7bec8f1fbe164d3d136c5bc887bebbb437f
  - N12 41f780ede48ae00d4e4f15251abf2583f9094aa0
  - N16 469f015aacfbf500ae32662bd2d13f16a5e1bc99
  Each is solved by harness Zielonka (Even wins every vertex), with harness/verify.py errors = [].
- N5 on CDAG_N8 / N12 / N16: `RESULT mode=n5 … iterations=1 fallback=0`. SSI: iterations=1.

## What is left for K9
- K9 now needs a bound for the subset sequences N5 actually produces in G_c: the S4a moves are Even's optimum in the arena
  restricted to {σ(v)} ∪ Iσ(v) against τ_k.
- On CDAG_n each such move is a best response within the improving edges, and it ends the run at once.
- The open question is whether a varying τ_k can make N5's S4a moves on some G_c emulate gen(m), i.e. single or small-subset
  steps. That is the next probe (box 8 item 1, continued).

## 5. Consequence for K8's constant case, and Lemma S (switch-best in one-player 1-sink games)
K8's constant case was closed (N5-oneplayer-box7.md §2) by the same premise: "By Prop. 7.4 the segment has O(n³) Even moves,
whatever τ does". That is the any-policy reading, and CDAG_n refutes it. So that closure is WITHDRAWN.
What K8's constant case needs is narrower:
- There, τ_k = τ_sb(k) = b_(k+1) = c (N5-K8-box6.md §1 (a)-(c)), and Ω^G_σ = Ω^{G_c}_σ.
- So each Even move of N5 is the optimum of the one-player improvement arena H_σ of G_c (Even restricted to {σ(v)} ∪ Iσ(v), Odd
  fixed to c). That is switch-best on G_c, a single rule, not every policy.

Lemma S (L-NEW reading, unrefereed). Let H be a one-player game (⊖ out-degree 1) that is 1-sink: every ⊕-strategy sends every
play to the sink 0, a self-loop of least relevance. Since ⊖ has no choices, this is the same as: the graph without the sink loop
is ACYCLIC (any other cycle could be selected by some ⊕-strategy). So the lemma covers DAG-shaped one-player games only. Let ρ* be
an optimal ⊕-strategy, and h the largest number of edges on a ρ*-path to 0. Then switch-best (ρ_{k+1} = an optimal strategy of the arena H_{ρ_k}) is optimal after at most h ≤ n − 1 steps.
Proof.
- In a 1-sink game, Ω_ρ(v) is the path set, compared by the most relevant differing vertex, and P_ρ(v) = {v} ∪ P_ρ(ρ(v)) with
  v ∉ P_ρ(ρ(v)). The optimal strategy of an arena has pointwise-maximal Ω (VJ00 §5).
- H_{ρ_k} contains ρ_k, so Ω is monotone along the run, and Ω ≤ Ω* = Ω_{ρ*}.
- Let d(v) = the number of edges on v's ρ*-path. Induction on k: after k steps, Ω_{ρ_k}(v) = Ω*(v) whenever d(v) ≤ k.
- Take d(v) = k + 1 and x = ρ*(v), so d(x) = k and Ω_{ρ_k}(x) = Ω*(x). If v is already optimal, monotonicity keeps it there.
- Otherwise {v} ∪ P(ρ_k(v)) ≺ {v} ∪ P*(x) = {v} ∪ P_{ρ_k}(x). Since v lies in neither set, (v, x) is an improvement, so it is an
  edge of H_{ρ_k}.
- Let ρ̂ = ρ_k with v → x. Then ρ̂ ∈ H_{ρ_k}. By 1-sink, ρ̂ has no cycle, so the ρ_k-path from x avoids v and
  P_ρ̂(v) = {v} ∪ P_{ρ_k}(x) = P*(v).
- The arena optimum ρ_{k+1} dominates ρ̂ pointwise, so Ω_{ρ_{k+1}}(v) = Ω*(v). □

Computer checks:
- experiments/new/p_strict/sb_sink_check.py: 400 random one-player 1-sink DAG games (n ≤ 14), 5 random starts each, N5 (= switch-best
  on a one-player game) run unmodified. Violations of "iterations ≤ h": 0 of 2,000 runs; max(iterations − h) = 0.
- On general one-player games (cycles allowed, ⊖ out-degree 1; sb_1p_general.py, 600 games n ≤ 24, 4 random starts each), switch-best
  takes at most 6 iterations (n = 21, 22). 0 incorrect runs (regions = Zielonka, verify.py).
So K8's constant case is re-closed only when G_c is acyclic apart from the sink loop: a narrow case. (The two-player analogue of
the argument fails: in Friedmann's sink games the sink is the cycle node only under Odd's BEST reply, so after switching v the
opponent may reroute through v.) For a general G_c (cycles) the constant case is OPEN; the data say ≤ 6 iterations.

## 6. N5's own segments (DATA)
experiments/new/p_strict/n5_segments.py reports the maximum number of Even moves within one segment where σ̄ is constant, and of
Odd moves within one segment where τ̄ is constant. Runs are N5's own (n5_lock.step = n5.py's loop), on the lane's adversarial
instances (n5adv, n5harm, n5lock, sbfollow, switchallexp_N3, deeptrap_sae N1-5, padsae N1-2).
- The maximum is 15 Even moves in one σ̄-segment (sbe2_s22, n = 60) and 8 Odd moves (best_n24, harm_n96).
- All the others are ≤ 6.
- Full output: experiments/new/p_strict/segments.txt.
So on these instances the per-segment premise holds with room to spare. CDAG shows that no any-policy theorem can give it.
