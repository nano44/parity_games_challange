# K10: can a varying τ_k make N5's Even steps emulate CDAG's gen(m)? (L-NEW box 8; 2026-10-19, file written ~01:02Z between two date -u calls, first commit 3a6078b at 01:13Z)
L-NEW successor 3, Opus 5.5 (D8). Lead brief 00:52Z. Status: NOT BUILT, so N5 is not killed. Below are two proved lemmas
(L-NEW readings, unrefereed), DATA, and the obstruction K10 written as necessary conditions. K10 is NOT an impossibility proof.

## 0. The question
N5's Even step from (σ_k, τ_k):
- σ_{k+1} is Even's optimum in the arena A_k, where Even v may use {σ_k(v)} ∪ Iσ_k(v) and Odd is fixed to τ_k.
- Iσ_k is the set of honest improvements: VJ00 Ω_σ, against Odd's best reply σ̄_k.

To emulate gen(m) (docs/new/N5-K9-Pstrict-counter.md) inside a σ̄-segment with σ̄ = c, every Even step would have to switch
exactly the next edge of gen(m) and nothing else.

## 1. Two lemmas
Lemma F (frozen opponent). Suppose τ_k = τ for k = a..b. Then V_{σ_{k+1},τ} ≥ V_{σ_k,τ} pointwise, where V is the VJ00 valuation
in the one-player game G_τ.
Proof: σ_k ∈ A_k, and the arena optimum is pointwise maximal over A_k (VJ00 §5, in the one-player arena G_τ ∩ A_k). □
So Even's moves while τ is frozen are V_τ-monotone in G_τ. CDAG shows that such one-player sequences can be exponentially long, so
Lemma F alone bounds nothing.

Lemma G (direct gifts). Suppose, in addition, that for every Even vertex v and every successor w of v, the τ-play from w meets no
Even vertex before it reaches its cycle. Example: every edge runs through an Odd gadget whose τ-choice exits straight to a gift
ladder. Then while τ is frozen, Even makes at most Σ_v (deg(v) − 1) moves that are V_τ-strict at the moving vertex. Every other
move is a V_τ-tie, so the engine's static tie-break decides it.
Proof:
- V_{σ,τ}(v) = f(v, σ(v)) depends only on v's own edge.
- The arena optimum maximises f(v, ·) over A_k(v) ∋ σ_k(v).
- So a V_τ-strict move at v raises f(v, σ(v)) strictly.
- f(v, ·) takes at most deg(v) values. □
So masking by gifts that do not read the counter cannot carry a long chain through strict moves. That is box 4's K3 in lemma form.
Ties turn N5's step into an index rule (notebook, succ. 2).

Corollary of Lemma S (docs/new/N5-K9-Pstrict-counter.md §5). If G_c is acyclic apart from the sink loop and τ_k = c for h + 1
consecutive steps, then Even reaches its G_c-optimum within those steps.

## 2. Masking load of gen(n) (DATA, experiments/new/p_strict/cdag_load.py, load.txt)
At each state of gen(n), count the Even vertices with a non-empty honest improvement set, other than the vertex that switches.
N5 must leave each of them unmoved. By K1 (box 4), each one needs Odd's τ to be strictly worse for Odd than σ̄ on the play from its
current successor.
| n | steps | masked vertices per step: mean | max | steps with no masking |
|---|---|---|---|---|
| 4 | 11 | 1.18 | 2 | 3 |
| 6 | 57 | 2.68 | 4 | 5 |
| 8 | 247 | 4.21 | 6 | 7 |
| 10 | 1013 | 5.73 | 8 | 9 |
So Θ(n) Odd blunders must be held at almost every step, and the set of masked vertices moves along the chain. Only n − 1 steps of
the 2^n − n − 1 need no mask.

## 3. Searches (DATA; every improved best is re-run through n5.run unmodified, regions = harness Zielonka, verify.py errors = [])
- Gift-gadget CDAG (p_strict/cdag_mask.py): CDAG_n with Odd gadgets o_{v,u} on chosen edges, each choosing between u and an exit to a
  shared ladder at distance l from an Even top cycle T. The climb runs over gadget set, l, τ_0 and σ_0, with fitness = N5 iterations.
  - n = 6 (2,500 steps): 5 iterations. n = 8 (1,500 steps): 7 iterations.
  - gen(n) would need 57 and 247.
- Long σ̄-segment climb on general two-player games (n5_adv_seg.py): fitness = most Even moves inside one segment with constant σ̄,
  along N5's own run. Results: 7 at n = 16; 12 at n = 40; 12 at n = 80 (1,500 steps). So segments stay about n/6 to n/3, and the climb puts nearly the whole
  run into one segment.
- Best-reply-change climb (n5_adv_ch.py, item 2): ch_O + ch_E = 23 / 30 / 28 / 50 at n = 16 / 32 / 48 / 64, with 16 / 23 / 26 / 40
  iterations; 39 changes (24 iterations) at n = 96. Iterations stay below ch_O + ch_E, and both grow roughly linearly.
- Lane instances (n5_segments.py, segments.txt): at most 15 Even moves in one σ̄-segment.

## 4. K10 (obstruction, as necessary conditions)
A family in which N5 emulates gen(m), or any super-polynomial one-player chain, inside a σ̄-segment must have all of the following:
- (a) At almost every step, Θ(n) Even vertices locally stalled against τ_k (§2). Each stall is an Odd blunder on that vertex's current
  play (K1), and the set of stalled vertices changes from step to step.
- (b) Stall values that depend on σ downstream. By Lemma G, gifts entered directly give at most |E| strict Even moves per frozen
  period; every other move is an index-rule tie.
- (c) Odd's τ_k must change throughout. Odd's step is its optimum in its own restricted arena against the OLD σ_k. So the blunders
  must survive Odd's own improvement step: each fix must stay out of Iτ_k (mutual protection, K2) or be non-optimal against σ_k. Yet
  the one blunder that releases the next gen(m) switch must disappear on cue. This is the anticipation K7/K8 found missing on
  switchbestexp.
- (d) τ_k ≠ c except on short stretches. Once τ_k = c, Even's steps are switch-best on G_c, which is fast: Lemma S for acyclic G_c;
  data ≤ 6 iterations on general one-player games (n ≤ 24).
On the Lead's sub-question, whether CDAG's structure makes anticipation cheap: it does not remove (a). Being a DAG does remove K5's
length obstruction, which needs σ-cycles, so exit lengths can be ordered (l(o_{v,·}) decreasing towards the sink). The gift climb
exploits exactly that freedom and still gets 5-7 iterations.

## 5. Files
- Instances (sha1 in experiments/new/p_strict/climb_instances.sha1): instances/n5ch/ch_n{16,32,48,64,96}_seed*.pg,
  instances/n5seg/seg_n{16,40,80}_seed*.pg, instances/cdagmask/mask_n{4,6,8}_K*_seed*.pg (+ .start = the climbed σ_0/τ_0).
- Climb logs: experiments/new/p_strict/logs/ (every improved best line ends "check OK").
