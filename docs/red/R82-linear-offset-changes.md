# R82: offset changes of ONE vertex in ONE stretch_D grow LINEARLY in n (mkgrow: K changes at n = 8K + 53), past mkalt's √n; and K unforbid-switches of that vertex in one run (L-RED successor 20, box 49; the Lead's item (b), R78 §3, date -u)
Target: the growth target of R78 §3: offset changes per vertex per stretch_D beyond √n, the remainder (R2) of docs/si/N5-RUND-box17.md
§17. Labels per L40. DATA (instances), READING. Every game. Nothing here bounds N5 or refutes a polynomial bound. Not a TARGET.md claim.
G-N5-TIME stays open.

## 0. Result
- **Family mkgrow (experiments/red/usplit/mkgrow.py K LG OUT, LG = K + 6).** One Even vertex v changes its offset K times inside
  ONE stretch_D: D, R_D and every gate's (Ξ, W) are constant. The run is fallback-free, in one phase, with (h3_D) at every state, and
  n = 8K + 53. mkalt (L-SI) needs n = Θ(K²) for K − 1 changes (0.8·√n; R78 §0).

| K | n | √n | offset changes of v in one stretch_D | iterations (n5.py) | fallbacks | Oink | L-SI lvl2.py |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 77 | 8.8 | 3 | 10 | 0 | — | — |
| 12 | 149 | 12.2 | 12 | 19 | 0 | OK | max_oc 12, segs 1, LVL PASS |
| 20 | 213 | 14.6 | 20 | 27 | 0 | — | — |
| 40 | 373 | 19.3 | 40 | 47 | 0 | OK | max_oc 40, segs 1, LVL PASS |

- The counts in the table come from three tools:
  - "offset changes" is my h3_19 (off_maxpv = lc_maxchg = K; the run has 3 stretch_D segments, and all K changes fall in one);
  - "iterations" is experiments/new/n5.py with the start pair; check_sol2 reports "zielonka(oink zlk) OK strategies verified" at K 12
    and 40;
  - "lvl2.py" is L-SI's (l-si 873c8e71, read only).
- Pins (start pairs; experiments/red/usplit/instances/):

| file | sha1 (.pg) | .start | .start.json |
| --- | --- | --- | --- |
| grow_K12_n149.pg | 71521dd56241614d43ecde6ec8173aadd3eb0b3d | 5951b0d1 | ff5322e3 |
| grow_K40_n373.pg | 42f217932aaf85309d31d622d1fdaac010968ac4 | 168a87cd | 655d6f60 |

- The same runs give v K UNFORBID-SWITCHES (L-SI §16 U events) in one run: U = 12 and 40 (usplit20). So U events of one vertex per
  run are Θ(n), not O(1). UF-ONCE was already dead (REFEREE-2 16).
  - Of these events, 6 and 20 are "neither" U-SPLIT events with no boundary of any kind (usplit20 neither_full): the GA → GB switches,
    whose offset falls.
- LC2 (|OC| ≤ |SL|) and PAIR-OC are not touched by this family. lvl2 passes: each change is paid at a fresh level C_j, so |OC| = K and
  |SL| = 2K.

## 1. The construction (R78 §3's "trigger from the other score", realised by Ξ-blocking)
- The cycle node c has rank 100000, so fillers are in no path set (only lengths count). Every route ends at a gate, so R_D is constant.
  - Gates (Odd u; τ = W branch → c; σ̄ = odd o → chain → g, kept in D by a chain of length LG): GH (o_hi, top), GA (o_A), GB (o_B).
  - A zero-offset gate Z (two branches with equal path sets; the σ̄ branch is longer).
- Two delay lines A and B: l_1 … l_L → h_side (even) → G_side. Their exits go to qx (odd, relevant) → Z, so a line is W-worse than ∅
  until wired. One wave runs down each line, one vertex per iteration.
- For j = 1..K:
  - x_j (even C_j, increasing in j) → w_j;
  - w_j (Even) has successors sH → GH and tap_j, the vertex of line A (odd j) or line B (even j) that the wave reaches at time j.
- v (Even) has successors s0 → Z and x_1 … x_K.
- Rank order: o_hi > C_K > … > C_1 > hA > hB > qx > o_A > o_B > c.
- Dynamics:
  - At the start every x_j is W-better than v's route (C_j on top). Every x_j is Ξ-blocked: o_hi is the odd top of Ξ(x_j), so (v, x_j)
    is forbidden.
  - When the wave reaches tap_j, w_j switches to it. That edge is Ξ-improving all along (it avoids o_hi), and W-better once h_side has
    arrived.
  - Then x_j is unblocked: its Ξ is {C_j, h_side, o_side}, against v's {C_{j−1}, h_other, o_other}. So v moves to x_j at the next
    transition.
  - v's class alternates GA, GB, GA, …, and o_A ≠ o_B, so every move is an offset change.
- Why this beats R78 §3's √n bound (READING): that bound assumes each arrival needs its own fresh delay line (Σ lengths = Θ(K²)).
  - Here one line per side serves all arrivals.
  - The arrival "improvement" is not a value travelling to v. It is the removal of a Ξ-block on a route v already wants in W.
  - The timing comes from where the tap sits on the shared line.
  - Later taps are not worse, because v's preference is set by C_j, which sits before the tap, and fillers are irrelevant. That is what
    killed my own earlier tapped-line attempt (my 10:20Z message to the Lead).

## 2. What it does to the remainders (READING)
- (R2) of N5-RUND §17 (offset changes per vertex per stretch_D): Θ(n) is attained. Under LC2 the bound would be ≤ 2n, so the family is
  within a constant factor of LC2's bound. It does not contradict LC2.
- CHARGE-U (§16): coarse W-changes per vertex per run ≤ (n − 1)(1 + |U(S)|). Here |U(S)| ≥ K = Θ(n) for one vertex alone, so that route
  gives at least Θ(n²) per vertex per run. That is still polynomial, but any argument that needs |U| = O(n_E) per run is dead.
- Nothing here is super-polynomial. Each change costs a fresh content level C_j, so RULER (one score per level) is respected. A
  super-polynomial count inside one stretch would need level reuse in both scores (the LC2 question, R81 §2).

## 3. Tools
- mkgrow.py (generator; the pins are byte-identical to `mkgrow.py 12 18` and `mkgrow.py 40 46`, cmp).
- h3_19.py (offset counts), usplit20.py (U events, U-SPLIT classes, Oink with --oink).
- L-SI's lvl2.py was run read-only from a detached worktree of origin/claude/l-si at 873c8e71, removed afterwards.
