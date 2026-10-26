# N5-ALT (box 23): ALTERNATION and (G1). Four exact reductions, a fresh-event charging that holds on 1,590 of 1,592 σ̄-changing in-interval transitions, four DEAD statements with their instances, and the count both questions reduce to
L-SI successor 19 (Opus 5.5; D18, Lead reading L40). Lead's GO 19:03Z, queue item 1: «(G1) + ALTERNATION». Working note, unrefereed; not frozen.
Not a TARGET.md claim. Nothing here bounds N5's running time; G-N5-TIME stays OPEN.
Labels (D18 / L40): PROVED (lane, unrefereed) / CONJECTURE / OPEN / DATA / READING / DEAD.
Tools (experiments/si/root/): gateret.py, mrise.py, fresh.py. Logs: root/logs/gateret_*.txt, mrise_*.txt, fresh_*.txt, alt_kills.txt.
Instance list: root/logs/alt_all.lst. It holds 413 games, every .pg under experiments/red/*/instances, n5-epoch/instances, new/box48/instances,
new/box48/out/qpcclimb/scale, si/root/instances and n5-exhaustive/instances with n ≤ 600, each with its .start file when one exists.
"lib41" is experiments/new/box41/lib41.txt with n ≤ 48 and two random starts per game besides S3 (RS = 2).

## Summary
| § | item | label |
| --- | --- | --- |
| §1 | RISE-SW: every Even switch at an in-phase S4a transition is a strict Ξ-rise of the switcher. RISE-GATE: every gate change is a strict Ξ-rise of the abandoned option, ties at t + 1 excepted | PROVED (landed premises + BEST of N5-EXIT §2) |
| §1 | FRESH-RED: a fallback-free run S has length ≤ m_E + NOFRESH(S), where NOFRESH(S) counts the return-only transitions | PROVED (elementary) |
| §1 | Consequence: run length, ALT and (G1) all reduce to XR, the number of Ξ-changes of one vertex in one phase | PROVED (from the two lines above) |
| §2 | DATA: gate changes by kind; returns per scope; Ξ-changes per vertex ≤ 1.8n per phase | DATA |
| §3 | (G1): FRESH3, "every σ̄-changing transition inside a global C-interval carries a fresh Even edge, a fresh gate option or a shrink of A", holds on 1,590 of 1,592 such transitions and fails on ret14_n48 | DATA + DEAD (as an exact statement) |
| §4 | DEAD: GATE-ONEWAY (pp_K48_n449), TOP-ONCE (lev_l_sc), FRESH at run scope (x32_rand48: not alternation, the D = ∅ wave), FRESH2 (post31_n48), FRESH3 (ret14_n48) | DEAD |
| §5 | READING: Odd's best response is a shortest-path tree under monotone updates (Even–Shiloach), with lexicographic levels; [F] Cor. 9.9 shows that the levels alone allow counters; where N5 must differ | READING |
| §6 | open items | OPEN |

## 0. Setting
As in docs/si/N5-EXIT-box22.md §0 and §9 and docs/si/N5-GCILEN-box22.md §1. A phase has τ and λ constant (RESULTS R38 (a)). S is a fallback-free
run of one phase with λ_W constant. Runs where λ_W moves are skipped and counted (lambdaW_moves). D_t := {Odd u : σ̄_t(u) ≠ τ(u)}. A_t, D-direct
gates and offsets are as in P-N5-GCX §1; global C-intervals and cut kinds (AG / DCH / DDSET / OSB / OVAL) are as in staticdepth.py GCI=1 and
evenside.py. A GATE CHANGE at t → t+1 is an Odd u ∈ D_t ∪ D_{t+1} with σ̄_t(u) ≠ σ̄_{t+1}(u); write y1 := σ̄_t(u) and y2 := σ̄_{t+1}(u). Inside a phase,
σ̄ = τ off D and τ is constant, so every σ̄ change is a gate change. ALT_c(S) is as in N5-EXIT §9. m_E is the number of Even edges.
Ξ_t(z) = (c, P, ℓ) is the honest valuation (SPEC S1), and M is the signed weight of P. XR_P(z) := the number of transitions of P at which Ξ(z)
changes.

## 1. Reductions (PROVED, lane)
- Lemma RISE-SW. Let t → t+1 be an in-phase S4a transition and w an Even vertex with σ_{t+1}(w) = y ≠ σ_t(w), and suppose w is on no honest cycle
  at t or at t + 1. Then Ξ_{t+1}(w) ▷ Ξ_t(w).
  Proof. y ∈ Iσ_t(w) by (SW), so Ξ_t(y) ▷ Ξ_t(σ_t w), and Ξ_{t+1}(y) ⊵ Ξ_t(y) by RESULTS R15 (a) (pointwise monotone in a phase). So
  Ξ_{t+1}(y) ▷ Ξ_t(σ_t w). Both are valuations of plays that avoid w: y's honest (t+1)-play, because w is off the cycle at t + 1, and σ_t(w)'s
  honest t-play, because w is off the cycle at t. Both have w's cycle node c, as everything in U_c does in the phase. On such valuations
  w ⊕ · is strictly monotone: it adds the same vertex w to both path sets (when rank(w) > rank(c)) and 1 to both lengths. Hence
  Ξ_{t+1}(w) = w ⊕ Ξ_{t+1}(y) ▷ w ⊕ Ξ_t(σ_t w) = Ξ_t(w). (The order matters: Ξ_t(y) itself may be the valuation of a play through w.) □
- Lemma RISE-GATE. Let u be a gate change at an in-phase transition with u on no honest cycle at t or at t + 1. Then Ξ_{t+1}(y1) ⪰ Ξ_t(y1), strictly
  unless Ξ_{t+1}(y1) = Ξ_{t+1}(y2) (a tie at t + 1).
  Proof. In κ (equivalent to Ξ inside the class by (M1κ)), this is the chain of N5-EXIT §2 GATE-PUSH / P1UP with no hypothesis on exits:
  κ_t(y1) ⪯ κ_t(y2) (BEST at t) ⪯ κ_{t+1}(y2) ((M2κ)) ⪯ κ_{t+1}(y1) (BEST at t + 1). The last step is strict unless there is a tie. BEST (N5-EXIT §2)
  is κ-Y-FORM_D (RESULTS R56 (d), landed) plus Fact CL, a proof step of P-N5-OFFMONO §1 restated there from landed premises. MONO-REF (the
  conditional part of N5-EXIT) is not used. □
- Lemma FRESH-RED. Call a transition of S FRESH if some Even vertex switches at it to an edge it held at no earlier state of S. NOFRESH(S) := the
  number of other transitions (RETURN-ONLY transitions). Then |S| ≤ m_E + NOFRESH(S).
  Proof. Every transition of S changes σ: τ is constant in the phase, and an S4a step that changes neither σ nor τ is a fallback (SPEC S4c),
  which S does not contain. Map each FRESH transition to one of its fresh edges (w, y). The map is injective, because an edge is fresh only once
  per run. □
- Consequences.
  - From RISE-SW: |P| ≤ Σ_w XR_P(w) + (switches of Even vertices on honest cycles). With RISE-GATE: ALT_c(S) + (G1) changes ≤ Σ_y indeg_Odd(y)·XR_P(y)
    + ties + cycle cases.
  - So the run length and the Odd count are both bounded by the per-vertex Ξ-change count XR. XR per vertex splits as
    XR ≤ (n + 1)(1 + #M-changes): with M fixed, ℓ moves monotonically in a range of size ≤ n.
  - A polynomial bound on M-changes per vertex per phase would bound everything. This is not progress by itself: it is the same quantity that
    Friedmann's counters make exponential in other SI variants (§5). But it localises the target to one vertex's path set.
- Remark (the counter recursion; standard, stated to fix notation). For a vertex z and a rank r, let π_r(z) := P(z) ∩ {rank ≥ r}. Every π_r(z)
  is monotone in the Ξ order on its own: its top differing rank is the top differing rank of P(z) when the two differ. Let N_r(z) count the
  changes of z whose top differing rank is r. Between two changes of π_{r+1}(z), the bit r moves at most once. So
  N_r(z) ≤ 1 + Σ_{r' > r} N_{r'}(z), which allows 2^n. §4 (TOP-ONCE) shows the recursion is used non-trivially in N5's data.

## 2. DATA (gateret.py, mrise.py, fresh.py)
Gate changes by the kind of their transition (logs gateret_all.txt, gateret_lib41_n48_rs2.txt; runs with moving λ_W skipped: 125 / 233):
| sample | runs | in | AG | DCH | OSB | DDSET | OVAL | RET in same GCI | RET in run | RET in phase | most changes of one gate in one run (gate's out-degree) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alt_all (413 games) | 787 | 458 | 1,102 | 948 | 804 | 100 | 8 | 116 | 1,103 | 2,280 | 62 (2), gate_K64_n581 |
| lib41 (n ≤ 48, RS 2) | 1,177 | 700 | 293 | 68 | 1,270 | 3 | 0 | 4 | 558 | 920 | 35; largest excess over out-degree − 1 is 17 (pftheta_cex_n32: 33 changes, out-degree 17) |
- RISE-GATE in data: the abandoned option's Ξ rose at every gate change except one tie (alt_all: 3,399 in M, 20 in ℓ only, 1 unchanged). In 3,406
  of 3,420 changes y2 is strictly below y1 at t + 1. lib41: 2,310 M, 24 ℓ, 0 unchanged; 2,323 of 2,334 strict.
- Returns inside one global C-interval are rare except on L-RED's pp family: 114 of the 116 on alt_all are pp_K12 (21) and pp_K48 (93), and the
  other 2 are on ret14_n48. On lib41 there are 4.
- XR (mrise.py; logs mrise_all.txt, mrise_lib41_n48_rs2.txt; WRONG = 0 everywhere, i.e. no Ξ fall at an in-phase transition, R15 (a)):
  - alt_all: max XR = 75; max XR / n = 1.80 (nep92_n40: 72); max phase length / n = 3.37.
  - lib41: max XR = 51 (lev_l_x, n 32); max XR / n = 1.59; max phase length / n = 2.59.
  - The most M-changes of one vertex in one phase is 67 (alt_all) and 37 (lib41).
  - M-changes by the top differing vertex: odd vertices LEAVING the path set dominate (alt_all: 38,815 OUT-odd against 15,017 IN-even;
    lib41: 43,977 / 14,707; nep90: 903 / 46). Length-only changes: 5,632 / 12,343.
- FRESH-RED in data (fresh.py; logs fresh_all.txt, fresh_lib41_n48_rs2.txt):
  - alt_all: 7,344 transitions in 912 runs, NOFRESH 1,145, at most 22 in one run (x32_rand48, n 48, run length 44).
  - lib41: 10,344 transitions, NOFRESH 1,856, at most 22 in one run.
  - On the gate-growth families pp_K12, gate_K16 every transition is FRESH (NOFRESH = 0): the leapfrog is paid by the risers' fresh options x_j.
  - No size growth of NOFRESH within a family: b6_xw n = 32 / 40 / 48 / 56: 14 / 14 / 15 / 15; b6_xl n = 32 / 40 / 48: 14 / 19 / 15;
    x32_rand n = 16 / 24 / 32 / 48 / 64: 0 / 6 / 4 / 22 / 16.

## 3. (G1): σ̄ changes inside a global C-interval. A three-sided fresh-event charging; DATA; DEAD as an exact statement
- Three FRESH EVENTS at a transition t → t+1 inside a global C-interval I = [a, b]:
  - (E) an Even vertex switches to an edge it did not hold at any earlier state of I;
  - (O) a gate moves to an option it did not hold at any earlier state of I;
  - (A) A_{t+1} ⊊ A_t.
- Lemma FRESH3-COUNT (PROVED, elementary). On I, transitions with (E) number ≤ m_E, with (O) ≤ Σ_{u ∈ D} deg(u), and with (A) ≤ |A_a| ≤ n.
  A is non-increasing on a global C-interval by definition (P-N5-GCX §1), so each vertex leaves it at most once. The other two counts are
  injective maps to edges, as in FRESH-RED. □
- CONJECTURE FRESH3 (as first stated): every σ̄-changing transition inside a global C-interval carries (E), (O) or (A). With FRESH3-COUNT, the
  number of σ̄-changing transitions inside one global C-interval would be ≤ m_E + Σ_u deg(u) + n ≤ m + n. Between them, STATIC-DEPTH
  (N5-GCILEN §2; under (H3), (H4), GEN_W on each piece) bounds each σ̄-constant piece by n − 1. That gives GCI length ≤ (m + n + 1)(n − 1) + m + n:
  (G1) closed for the length question, conditional on FRESH3 and on the hypotheses of STATIC-DEPTH.
- DATA (fresh.py gci_kind_*):
  - alt_all: 497 σ̄-changing in-interval transitions: E 58, EO 188, EA 2, EOA 236, O 5, OA 5, A 1, none 2.
  - lib41: 1,095 such transitions: E 4, EO 312, EA 5, EOA 754, O 10, OA 9, A 1, none 0.
  - No single fresh event is enough. (E) alone misses 13 (alt_all) + 20 (lib41) transitions; on so_sorl_n32, for example, gate 13 (out-degree 23)
    moves to new options while Even returns. (E) or (O) misses 3 + 1 (post31_n48, ret14_n48). (The two samples overlap in games.)
- DEAD FRESH3 (exact form). Instance experiments/n5-epoch/instances/ret14_n48.pg (sha1 e10657efdaf6…, start ret14_n48.start, 3880090885ef…),
  phase [4, 58], global C-interval [18, 22] (D = {0, 17, 44} constant, offset of the direct gate 17 constant):
  - at t = 18 Even 27 goes 38 → 30 and gate 0 (out-degree 16) goes 9 → 27;
  - at t = 21 Even 27 goes back 30 → 38, gate 0 goes back 27 → 9, and |A| stays 35.
  So transition 21 carries none of (E), (O), (A).
  - Obstruction: a ONE-VERTEX FLIP-FLOP between an Even vertex and the gate that reads it. Gate 0 takes 27 as long as 27's play is the 30-route,
    and 27 moves back once the 38-route is better again. Both returns happen inside one global C-interval with A unchanged.
  - The same pattern recurs at [46, 50] (t = 49) in the same phase, so the failures are not one per phase.
  - Control: FMUT=1 (no credit for (A)) adds a failure on post31_n48 (NOFRESH3_gci_gch 0 → 1), so (A) is used.
- READING. FRESH3 fails only on flip-flops of this kind (2 of 1,592). A repaired statement must charge the flip-flop to the Ξ-rise it needs
  (RISE-GATE at both of gate 0's changes: Ξ(27) rises at t = 18, Ξ(9) at t = 21). That is the per-vertex count XR again (§1).

## 4. DEAD statements (each with its instance and the obstruction; traces in root/logs/alt_kills.txt)
- DEAD GATE-ONEWAY ("in a fallback-free run, a gate never returns to an option it left"; also its GCI form, and the bound "changes of u in S ≤
  deg(u) − 1").
  - Instance: experiments/red/usplit/instances/pp_K48_n449.pg (sha1 a161569d654c…, start ead176541505…). Gate 447 has out-degree 3. It alternates
    441 ↔ 445 at every transition t = 2 … 49, all inside ONE global C-interval: 48 changes, 47 of them returns. It leaves to 437 at the AG cut
    t = 54. gate_K64_n581: 62 changes of a gate of out-degree 2 in one run (DCH cuts).
  - Obstruction: two Even risers (L-RED R83's vA, vB) leapfrog in Ξ. Each rise is paid by a fresh option x_j of the riser (FRESH-RED: NOFRESH = 0
    on pp). The gate follows the lower riser (N5-EXIT §2 PAIR). Changes per gate grow linearly in n at fixed out-degree, so any per-gate bound
    must involve n.
- DEAD TOP-ONCE ("in one fallback-free run, each vertex's path set changes at most once with a given top vertex and direction"; it would give
  XR ≤ 2n per run).
  - Instance: experiments/si/orlens/instances/lev_l_sc.pg (sha1 86c17b078ca2…, S3 start), phase [8, 54], z = 0. In the run [8, 31] the odd
    vertex of rank 19 leaves z's path set as the top change 7 times (8, 10, 12, 14, 16, 18, 23), 11 times in the phase.
  - Obstruction: the counter recursion of §1 is live. Between two of these, a HIGHER odd vertex leaves z's path set (ranks 30, 26, 31, 29, 26,
    12, 20, 12), and rank 19 re-enters as a lower-order change. Data maximum multiplicity: 7 per run, 11 per phase (lib41); no family with
    growth is known (lev_l n = 20 / 28 / 32: 2 / 6 / 11 per phase, but these are climbs, not a parametrised family).
- DEAD FRESH at run scope ("every transition of S has a fresh Even edge", which would give |S| ≤ m_E).
  - Instance: experiments/red/xing/instances/x32_rand48.pg (sha1 865321803e5b…), one run of length 44, 22 return-only transitions.
  - Obstruction: not alternation. D = ∅ throughout. After a mass switch at t = 0, single vertices return to their start edges one per step
    (a settling wave). That case is bounded by R91 §3 (D ∩ U_c = ∅) and STATIC-DEPTH, not by freshness.
- DEAD FRESH2 ((E) or (O) at every σ̄-changing in-interval transition).
  - Instance: experiments/red/so/instances/post31_n48.pg (sha1 24f491b96e0f…), phase 4, t = 20: Even 39 returns 30 → 28, gate 0 returns 39 → 46.
  - Obstruction: the long impure interval [4, 30] with D = {0}. A shrinks by about one vertex per step, and gate 0 (out-degree 14) re-uses options.
    The A-shrink is the fresh event there, so FRESH3 adds (A).
- DEAD FRESH3: §3 (ret14_n48, t = 21).

## 5. READING: a shortest-path view across areas, and why the order alone cannot be enough
- Odd's best response σ̄_t is a shortest-path (min-Ξ) in-tree to the cycle nodes; it is the VJ00 procedure, SPEC S1. Inside a phase every Ξ_t(z)
  is non-decreasing (R15 (a)), and Even's switches only remove options Odd liked (RISE-SW). That is the setting of DECREMENTAL single-source
  shortest paths. There the Even–Shiloach tree pays O(deg) per level increase of a vertex, so total work O(m · #levels).
  - The analogue here is: phase length ≤ Σ_z XR(z) (RISE-SW), and Odd's tree changes ≤ Σ_y indeg(y)·XR(y) (RISE-GATE).
  - The Even–Shiloach bound works because BFS levels are ≤ n. N5's levels are lexicographic (cycle node, M ∈ ±2^rank sums, ℓ), and their number
    is exponential.
  - Approximate versions of the tree (Bernstein-type rounding) round levels. For N5 that would change the algorithm, so it is not available.
  - READING only: no source is cited for these classical facts beyond the description. L-LIT would open the Even–Shiloach paper before any
    citation.
- L-NEW 29's reading of Friedmann (docs/new/N5-ALTLIT-box49.md §3, l-new 3e03271f, which cites [F] Cor. 9.9 as opened there): on 1-sink games VJ's
  lexicographic order IS a discounted order with γ part of the input, and SI with I^loc / I^glo is exponential there. So no argument that uses
  only "Ξ is monotone and lexicographic" can bound XR. The bound must use N5's own structure:
  - (a) the W-choice of S4a against the fixed τ;
  - (b) the arena (only Iσ edges);
  - (c) S4b's symmetric τ step, which ENDS the phase when Odd's τ would improve.
- What (c) gives inside a phase (READING, a candidate lever). Every state of a phase has Iτ = ∅ or a τ change ends the phase (R38 (a)). In the
  counter trace of §4 (lev_l_sc), the pump consists of odd vertices LEAVING z's honest play while z's W-play (through τ) stays put. This is Odd's best
  response σ̄ drifting away from τ on the D-gates. A candidate statement to test: in a phase, the gates' σ̄ re-entries into an odd vertex's
  region are bounded by τ's optimality (Iτ = ∅ at the phase's states). Not tested yet.

## 6. OPEN
1. XR-LIN (CONJECTURE; DATA §2): in every phase, every vertex's Ξ changes ≤ 2n times. Data maximum 1.80n. It implies phase length ≤ 2n² (RISE-SW,
   off-cycle switches) and ALT + (G1) ≤ 2n·m (RISE-GATE), up to ties and cycle cases. It is the whole problem localised to one vertex, not a
   reduction in difficulty.
2. (G1), repaired: FRESH3 plus a charging of the one-vertex flip-flop (ret14_n48) to a fresh event or to an Iτ = ∅ argument.
3. §5 (c): does τ's optimality on the phase (Iτ = ∅ at every state) limit the re-entries in the counter recursion? First test: on lev_l_sc,
   ret14_n48 and nep92_n40, for each re-entry of an odd vertex h into z's path set below the top change, record whether h's region contains a
   gate whose τ-option is strictly better for Odd at that state.
4. Lead's DATA step on [F]'s H_n (routed elsewhere): if N5 runs H_n in one phase, XR there is the counter, and this note's reductions price it.
