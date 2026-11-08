# R223 item 5: pre-check of L-NEW 64's box 196 (ESC3 / W3 for EVERY genome, so REACH3-CYC unconditional) (L-RED successor 58, Opus 5.5)
Lead 06:35Z: hunt for a Ξ-cyclic genome where ESC3 or W3 (P-N5-REACH §6.5-§6.6, signed for IDEAL-ACYC only) FAILS on Γ3(G) for N5′-xi
from S3, or where RESULTS R118 (k) fails: «N5′-xi from S3 on Γ3(G) visits only standard states and makes Howard steps at the movers until
its first fallback, at iteration T3 + 1». Required: exhaustive N ≤ 2 (all Ξ-targets, self-loops and 2-cycles included) plus random
N = 3-4 cyclic genomes, with my own Γ3 builder and n5b / n5bxi + Oink checks. Date 2026-11-08 (date -u). Labels: SURVIVES / BROKEN,
DATA, READING.

## 0. Verdict: SURVIVES (no Ξ-cyclic counterexample)
- ESC3 (first half: (K0, K1) ∈ Iσ in the standard state; second half: S4a keeps σ off the movers), W3 (i), the standard-state invariant,
  Howard steps at the movers, and «first fallback exactly when no mover has an improving edge» hold at every pre-fallback state of every
  run. The runs cover 50,816 Ξ-cyclic genomes; counters and sets are in §2.
- READING (agrees with box 196's claim): the proofs of ESC3 and W3 in P-N5-REACH §6.5-§6.6 never follow a Ξ-edge.
  - ESC3: in H, Odd plays pe at every gate. So every H-play from xt(g) runs mover → m → gate → pe → e → … → c_W, and every H-play from
    pb_g ends in the core's odd cycle (K3 (d), every genome).
  - W3 (i)-(iii): the (σ, τ)-plays and the H-plays follow pe, so they only use W-edges, which go down one level.
  - The acyclicity they are labelled with is used only by PLAY3, SBAR3 and KEY3. Those lemmas describe Odd's β-face reply and the IDEAL
    keys, and REACH3-CYC replaces them with IDEAL-CYC's values.
  - This is a reading, not a proof. Box 196 should write it out.

## 1. Tools (my own builder; frozen algorithm)
- experiments/red/r223/own3.py: Γ3(G) built from the TEXT of RESULTS R104 [DEF] (priorities, owners, edges, vertex indices) and
  P-N5-REACH §3 (pads, their order and priorities).
  - Two choices the text leaves open: β-vertices in option order, and e-priorities = the least even number above every β, + 2 per
    e-vertex in (level, gate index) order. Both are taken from [E-LEV] / P-N5-XICYC.
  - Cross-check: build3(G) equals the frozen box189 gamma3.build(G, all pads) in priorities, owners, successor lists, start σ and τ0, on
    all 48,816 genomes of exh223 (N ≤ 2) and on every genome of §2 (counter «build»: 0).
- experiments/red/r223/reach223.py. The game is own3's, parsed by harness pg. The algorithm is the frozen box190 n5v.step (l-new
  131b4c1c) from S3 (box21 n5x.start_pair, required to equal the standard state for the genome start: counter «start»). Every check uses
  L-RED's own.py (VJ order, Odd's optimal reply), not n5v's Engine.
- Counters per pre-fallback state j (state F − 1 included):
  - nstd: σ off the movers ≠ standard, or τ ≠ τ0;
  - esc: (K0, K1) ∉ Iσ;
  - w3: some mover's (σ, τ)-play value ≠ (c_W, ∅, 5ℓ + 5), or one of its pads ≠ (c_W, ∅, 5ℓ + 4) (W3 (i), checked on ALL options, which
    is also W3 (ii)'s H-value since H-plays from pads follow pe);
  - how: some mover moves to an option that is not a Ξσ-best element of {σ_j(x)} ∪ Iσ_j(x), or a non-mover Even vertex moves (ESC3,
    second half);
  - fbx: transition j is a fallback while some mover has an improving edge, or it is not a fallback while no mover has one (this is
    «first fallback at T3 + 1»).
- Per genome: nofb (no fallback within 5,000 iterations).
- Recorded, not a failure: ties (Howard steps where two or more options tie for best; R118 [N5XI] breaks them by Ξσ, then by index).

## 2. DATA (unit: genome = a run with any counter > 0; scope: N5′-xi = n5v mode xi on own3's Γ3(G) from S3)
| set | genomes | build | start | nstd | esc | w3 | how | fbx | nofb | Howard ties (recorded) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exhaustive N ≤ 2, Ξ-graph cyclic | 43,816 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| random N 3-4, cyclic, seed 2241 | 5,000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 226 |
| random N 5-6, cyclic, seed 2242 | 2,000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 116 |
- Exhaustive set: the exh223 enumeration restricted to cyclic Ξ-graphs. It covers every genome with N ≤ 2 (levels [0], [0, 0],
  [0, 1]), degree 1-2, every W-target, every Ξ-target in {X, movers} (self-loops and the 2-cycle 0 ↔ 1 included), every start, every
  β-parity vector, β-ranks identity or reversed, and gate order identity or reversed.
- Random sets (reach223.rgen_cyc): levels non-decreasing with steps ≤ 1, degree 1-3, Ξ-target self with probability 0.2, another mover
  with 0.65, X otherwise. Re-drawn until the Ξ-graph is cyclic.
- Control (the counters can fire): MODE=spec, i.e. N5, on 500 random N 3-4 cyclic genomes (seed 2243, out/reach223_ctrl_spec.txt): how
  143, fbx 296 genomes. N5's S4a takes an arbitrary pointwise optimum of H, and by W3 (iii) TIE(x) = R(x). So N5 keeps or moves movers
  without regard to Ξσ, and its fallback comes while movers still have improving edges. R118 (k) is a statement about N5′-xi only.
- Second implementations (xend223.py, unchanged): 200 cyclic genomes (rgen_cyc, N 2-5, seed 2240). Checked: n5b (N5) exactly 1
  fallback, total = F + 2 = n5v spec's; n5bxi (N5′-xi) exactly 1 fallback, total = n5v xi's; regions = Oink 8fbf0a7 --zlk; verify clean.
  bad 0 (out/xend223_cyc.txt).
- Frozen instances: none needed (no break). The control's genomes are reproducible from the seed.

## 3. For the Lead's forward to L-NEW 64: QUIET on Γ3 (R223-q2.md §4 (2)), step by step
- Carry over verbatim, by PAD (b)-(c): pads are never cycle nodes and never in a Π, and each gate face gets exactly one pad, so the
  shifts are equal. This covers (F-cls), CN2 (extended to pads), LOC-GATE, (Q1), (Q2) (DOM through the m pad), (Q4)'s path structure and
  (Q5)'s Bellman-Ford counting (simple G_C-paths still have ≤ N movers).
- Need a new citation or proof on the Γ3 run:
  - F1 and STRICT: from R15 (a) and «movers are never cycle nodes» (PAD (b)), instead of R118 (b).
  - The frozen core and frozen β-successors used by (F-E), LOC-K2 and (Q4): from R117 K3 (every genome) plus the standard-state
    invariant, i.e. REACH3-CYC / ESC3. That is exactly what this item tested, and it is DATA-only for cyclic genomes until box 196
    proves it.
  - L recomputed with n3 = N + 7M + 10 in (Q3) and (Q6).
Not a TARGET.md claim; not M3 or M4; G-N5-TIME stays OPEN.

## 4. Sources opened
- trunk 4aaba7d52 docs/new/P-N5-REACH.md §3 (Γ3 definition and pad order, l. 127-139), §4 S3-START, §5 PAD, §6.1-§6.7 (K3, PLAY3,
  SBAR3, TAU3, ESC3, W3, KEY3; l. 140-240); docs/RESULTS.md R104 [DEF] (l. 9864 ff.: vertex indices), R117 (e)-(f), R118 (k) (via
  R223-end.md §1).
- claude/l-new 131b4c1c experiments/new/box189/gamma3.py (cross-check target), box190/n5v.py, box21/n5x.py (algorithm), n5-second/n5b.py,
  box190/n5bxi.py.
- Reproduce (env WT = WT3 = worktree of l-new 131b4c1c): `python3 experiments/red/r223/reach223.py exh OUT`;
  `… rand 2241 5000 3 4 OUT`; `… rand 2242 2000 5 6 OUT`; `MODE=spec … rand 2243 500 3 4 OUT`.
