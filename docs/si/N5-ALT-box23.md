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
| §8 | DEAD XR-LIN (reader on long121: XR 86 > 2n = 82, run unchanged); READERS inflate K, ALT, (G1), EXIT_x without changing the run | DEAD + DATA + READING |
| §9 | Even switches per Even vertex per phase: ≤ 0.58n in data; CONJECTURE SW-LIN (≤ n), robust to Odd readers | DATA + CONJECTURE |
| §10 | DEAD SW-LIN (swlin_kill_n26: one Even vertex switches 27 > n = 26 times in a phase, re-armed by 6 fallbacks; n5b agrees); CONJECTURE SW-RUN (per fallback-free run) | DEAD + DATA + CONJECTURE |
| §12 | Even readers are clean in every measured case (SAME incl. fallbacks) and raise ONE vertex's switches above the base maximum (long121: 12 → 16) | DATA + READING |
| §13 | transition counts: |P| ≤ f + (f + 1)·max run; DATA run ≤ 1.53n, f ≤ 0.78n; CONJECTURES RUN-LIN, FB-LIN; climbs found no kill | PROVED (elementary) + DATA + CONJECTURE |
| §11 | the PROVED core (C1)-(C6) in one place, with premises; independent of MONO-REF / PURE-LEN / GATE-PUSH / E-ONEWAY | PROVED (lane) |
| §7 | gap (iv): FRESH-RED at interval scope; every known impure long interval (reader_L, cxmig, ladderent, pp) has NOFRESH = 0, so length ≤ m_E there | PROVED (elementary) + DATA |

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
  Proof. In κ (equivalent to Ξ inside the class by (M1κ)), this is the same three-step chain as N5-EXIT §2 Corollary P1UP, with no hypothesis on exits (GATE-PUSH's premises, FREEZE-A, are not used):
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

## 7. Gap (iv), impure C-intervals, through FRESH-RED (written 19:40Z by date -u)
- FRESH-RED holds on any interval of a run, with the same proof (PROVED, elementary): every global C-interval I has |I| ≤ m_E + NOFRESH(I),
  where NOFRESH(I) counts I's transitions at which every switching Even vertex returns to an edge it held earlier in I. No (H3), (H4) or GEN_W
  is needed. So GCI-LEN-type bounds reduce to the return-only transitions inside the interval.
- DATA (fresh.py; logs fresh_all.txt, fresh_lib41_n48_rs2.txt):
  - The impure instances of gap (iv) have NOFRESH = 0: every transition carries a fresh Even edge. This covers reader_L10 / L20 / L40
    (sha1 31644312 / c9f3c948 / cb6b7c76; their σ̄ is constant, and the long interval [0, L + 1] fails (H3), (H4)), cxmig_k16_n138,
    ladderent_k48_n156 and pp_K48_n449 (its σ̄ changes are paid by the risers' fresh options).
  - So on every known impure long interval, the length is ≤ m_E by FRESH-RED alone, whatever (H3) / (H4) do.
  - The most return-only transitions in one global C-interval: 22 (x32_rand48, n 48, transition 41). That interval has D = ∅, where R91 §3
    already bounds the length by |U_c| − 1.
  - Return-only transitions inside global C-intervals: alt_all 375 of 4,984 (13 with a σ̄ change); lib41 635 of 7,772 (20 with a σ̄ change).
- READING. Gap (iv) as a length question is then "return-only transitions inside impure intervals", and none is known with any. The return-only
  transitions that do occur lie in D = ∅ waves and σ̄-constant settling stretches, where R91 §3 or STATIC-DEPTH apply, plus the flip-flops of §3.
  Returns of an Even vertex need a strict Ξ-rise of the retaken successor since it was left (the N5 form of N5-GCX §8's NO-RETURN: re-taking y
  needs Ξ(y) ▷ Ξ(σ w) ⊵ (Ξ-SUCC) the value that made w leave y). So a return-only transition is again priced in XR.

## 8. XR-LIN is DEAD, and the obstruction behind it: passive READERS move every per-vertex and cut count up to the phase length without changing the run (written 2026-10-28 21:10Z by date -u)
Lead's restart word (2026-10-28 21:05Z): «CONJECTURE XR-LIN ... Aim for a proof, or for an exact obstruction with the instance that kills it».
Tools: experiments/si/root/mkoreader.py (appends a reader), orcheck.py (compares the two runs). Log: root/logs/orcheck_l121reader.txt.
- READER. Append to a game an Odd vertex o with index n, priority 0, no predecessors, and edges to a set S inside one class. Its start strategy is
  τ0(o) = some y ∈ S. Nobody's play passes o.
  - Reading of SPEC: S1 computes every other vertex's valuation and choice from plays and restricted graphs that do not contain o as a
    successor. Iσ and S4a's arena optimum do not see o. S4b could move τ(o) only, but never did here.
  - So the run on the old vertices should be unchanged, and Ξ(o) = o ⊕ min_{y∈S} Ξ(y): o's rank is below the cycle node's, and o ⊕ adds 1 to
    every length, so it preserves the order. Hence XR(o) = the number of changes of the minimum of |S| monotone sequences.
  - Label: DATA. The run identity is CHECKED per instance by orcheck.py (σ, τ and σ̄ on the old vertices, the fallback flags, the phases, and
    every old vertex's Ξ as (cycle node, path-set as a vertex set, length) agree at every state; ranks shift by one, the order does not). It
    is not proved for all games.
  - CORRECTION (REFEREE, docs/referee/R-N5-READER.md at e83fd19d, gap G-READ-1 and note READ-N1). The unconditional statement is FALSE: S4b can
    move τ(o), which ends a phase inside an old phase or cancels an old Even fallback (REFEREE's 5-vertex counterexample, its §2 (A); and
    l121reader_n41 itself with any start τ0(o) ≠ 0 splits the phase, its §2 (B)). REFEREE PROVES (Theorem READER-INV, every game): the run on
    the old vertices, the fallbacks and the phases are unchanged under condition (R), "τ(o) never moves at a transition at which τ is unchanged
    on the old vertices". (R) holds when τ0(o) is maximal for Odd's dual valuation over S at the first state of a τ-constant stretch. So the
    READER device is: «o with τ0(o) maximal for Odd's dual valuation over S, started at the first state of a τ-constant stretch; then the run on
    the old vertices, the fallbacks and the phases are unchanged on that stretch (Theorem READER-INV)» (REFEREE's wording, READ-N1).
  - Measured (orcheck.py, which now prints (R)): l121reader_n41 satisfies (R) (τ(o) never moves; REFEREE: Iτ′(o) = ∅ at all 123 states).
    l121reader6_n46 satisfies (R) for all six readers (READ-N2): readers 42 and 44 move τ only at transition 0 → 1, where τ on the old vertices
    changes too; the other four never move. So the inflation table below is an instance of Theorem READER-INV, not only DATA.
  - The XR-LIN kill needs no invariance (REFEREE): l121reader_n41 is itself a game where one vertex's Ξ changes 86 > 2n times in one phase.
- DEAD XR-LIN ("in every phase, every vertex's Ξ changes ≤ 2n times").
  - Instance: experiments/si/root/instances/l121reader_n41.pg (sha1 084da8cd47707b8937ebe30fdfae88d3d988bdaf; start l121reader_n41.start,
    7ca283c43b7092acc454c5ffc6b1995e3a29bf68). It is L-NEW's long121_n40 at its own start, plus a reader o = 40 with
    S = {0, 1, 2, 6, 7, 8, 17, 20, 22, 23, 24, 30, 36, 39} (class 11) and τ0(o) = 0.
  - orcheck.py: SAME (123 states each; σ, τ, σ̄, fallbacks, Ξ all equal), phases equal.
  - In phase [1, 122] (length 121, 8 fallbacks), Ξ(o) changes 86 times > 2n = 82. o is in D at 109 of 122 states, with 75 σ̄ changes.
  - S was found by a local search over subsets of class 11 maximising the changes of the lexicographic minimum along the base run.
  - Other bases: nep92_n40 gives 81 (just under 2(n + 1)), j4_n40 75, lend107_n32 57, xsn91_n48 56.
- The obstruction is more than the constant 2.
  - XR ≤ phase length always holds. The reader shows that, on any base, max_z XR is at least the largest number of changes of a minimum over a
    subset of a class: 86 / 121 of the phase on long121. So any per-vertex bound XR ≤ f(n) bounds the min-aggregate changes of the whole run
    with n + 1 vertices. Localising to one vertex (§1's Consequences) does not make the problem smaller.
  - The same readers also inflate the Odd-side counts of the OFFMONO / ALT route. Instance experiments/si/root/instances/l121reader6_n46.pg
    (sha1 29d2c84203f97bc247986d0af90778c5194d65a7, start 7c6897065a63ce81e43c2355ac20980c81a3b515) has six two-option readers on the leapfrogging
    pairs (6, 19), (0, 2), (1, 6), (23, 27), (1, 4), (9, 24), with τ0 = the first of each pair. The run on the old 40 vertices is again SAME, and:
    | count (evenside.py / gateret.py) | long121_n40 | + 1 reader (n 41) | + 6 readers (n 46) |
    | --- | --- | --- | --- |
    | C-cuts K (sum over runs) | 53 | 57 | 73 |
    | DCH cuts | 4 | 19 | 37 |
    | global transitions inside C-intervals | 60 | 56 | 40 |
    | σ̄ changes inside C-intervals ((G1)) | 2 | 28 | 1 |
    | exit-change transitions at cuts (EXIT_x) | 23 | 41 | 57 |
    | most σ̄ changes of one gate in one run | 3 | 11 | 5 |
  - So K(S), ALT, (G1), EXIT_x and per-gate change counts are NOT intrinsic to the dynamics. Passive vertices that change nothing raise them
    (K by 20 with 6 vertices here), and with enough readers they approach the phase length.
  - What remains intrinsic: the run on the non-reader vertices, i.e. the phase length and the Even switches.
- Consequence for the route (READING). Bounding K(S) or ALT polynomially is at least as hard as bounding the phase length of the reader-free
  game: each reader adds one vertex and can cover the leapfrog times of one pair. ALTERNATION is "the classic count" in a strong sense, and no
  decomposition of the run into "cuts × pieces" makes it smaller. A proof has to count something readers cannot inflate:
  - (a) Even switches (RISE-SW: phase length ≤ Σ_w XR(w) over Even switchers off cycles). Readers are Odd, so they do not add Even switches.
    An Even reader would block fallbacks (S4c fires only when nothing changes), so Even-side inflation is not clean and is NOT claimed. On
    long121's phase there are 8 fallbacks.
  - (b) Quantities defined on the honest plays of vertices that some Even vertex reaches. A reader's play is reached by no one.
- So the next target is reader-invariant: Even switches per Even vertex per phase, or Ξ-changes of vertices with an Even predecessor.

## 9. The reader-robust candidate: Even switches per Even vertex per phase (DATA, CONJECTURE; written 2026-10-28 21:30Z by date -u)
- SW_P(w) := the switches of Even vertex w in phase P. By FRESH-RED's first step, every in-phase transition has an Even switch, so
  |P| ≤ Σ_w SW_P(w) (PROVED, elementary). A bound SW_P(w) ≤ n would give |P| ≤ n·n_E.
- Odd readers (§8) add no Even switches. An Even reader e (no predecessors) is passive only where no fallback fires: its switch would turn a
  fallback step into an S4a step. [CORRECTION, §12: this was a reading, not a measurement. Measured, Even readers stay clean (run SAME,
  fallbacks included) on long121, lend107 and swlin_kill_n26. At a fallback state S4c's switch-all moves e together with everyone else.] Inside a fallback-free stretch it switches roughly when the W-best Ξ-improving option over S changes, so it can
  add switches there. Measured: on the longest fallback-free phase in alt_all (run49_n32, phase [2, 51], 49 transitions), the best
  max-aggregate over a subset of the class changes 6 times, against a base maximum of 4 switches of one Even vertex. Fallback-free phases in
  alt_all are short (≤ 1.53n). So Even readers inflate SW only a little in the data, and only between fallbacks.
- DATA (alt_all and lib41, n ≤ 48 for lib41):
  - the most switches of one Even vertex in one phase is 14 (sc24, n 24: 0.58n; returns_rt48 and returns_rt64, out-degree 3: 14 at both
    n = 48 and 64);
  - the largest excess over out-degree − 1 is 12 (out-degree 3), so Even vertices do return within a phase (E-ONEWAY is windowed only);
  - the longest phase (lend107_n32, 108 transitions) has at most 11 switches per Even vertex.
- CONJECTURE SW-LIN (now DEAD, §10): in every phase, every Even vertex switches ≤ n times. It implies phase length ≤ n·n_E. Unlike XR-LIN, it is not killed
  by Odd readers. Even readers can raise it only between fallbacks, by the max-aggregate count. Open whether that count can be pushed past n
  in a fallback-free stretch: the ≤ 1.53n fallback-free phases known leave little room.

## 10. SW-LIN is DEAD: fallbacks re-arm an Even vertex's cycle through its options (written 2026-10-28 by date -u; climbs swclimb.py)
- Climb: experiments/si/root/swclimb.py (box43 mutations, Odd choice set fixed; score = the most switches of one Even vertex in one phase minus n).
  - Round 1, 3,000-4,000 steps each: from sc24 (seeds 1, 2), returns_rt48 (seed 3) and lend107_n32 (seed 4). Best: 24 switches at n = 30.
  - Round 2 from that best, 6,000 steps each, seeds 5 and 6: seed 6 reached 27 switches at n = 26.
  - Logs: experiments/si/root/out/sw_*.log.
- DEAD SW-LIN ("in every phase, every Even vertex switches ≤ n times").
  - Instance: experiments/si/root/instances/swlin_kill_n26.pg (sha1 e2f769e1b45bdb883f7808e84f461b318a25e8f1; start swlin_kill_n26.start,
    bf7caa60d003cb6e3112ad8dc5232c95445c00dd).
  - One phase [1, 47] (τ and λ constant, checked) of length 46 with 6 fallbacks (at 7, 16, 22, 30, 35, 42). Even vertex 19 (out-degree 8)
    switches 27 times > n = 26.
  - Cross-check by an independent implementation: L-COMP's experiments/n5-second/n5b.py in SPEC mode (imported, not edited; its own trace
    hook) gives the IDENTICAL (σ, τ) state sequence (50 states, 49 iterations, 6 fallbacks), and the same 27 switches
    (experiments/si/root/n5bcmp.py; log root/logs/n5bcmp_swlin_kill.txt).
  - Obstruction (the trace): in every fallback-free run, vertex 19 walks the same cycle of options 25 → 0 → 23 → 12 → 25 → 23 (returns inside
    the run). Each S4c fallback sends it to its Ξ-best successor (10 or 13), after which the S4a run walks the cycle again. So switches per
    phase ≈ (fallbacks + 1) × (a cycle of about the out-degree). FB-C (RESULTS R71) bounds fallbacks per configuration, not per phase on
    general games, and data phases have up to 8. So SW per phase is not bounded by n unless fallbacks per phase are.
- What survives (DATA): inside ONE fallback-free run, the most switches of one Even vertex is 14 on lib41 (sc24, n 24, out-degree 3: 12 above
  out-degree − 1) and 48 on alt_all (ladderd0_k48_n156, out-degree 49, no return).
  - CONJECTURE SW-RUN: inside a fallback-free run of a phase, every Even vertex switches ≤ n times.
  - With a polynomial bound on fallbacks per phase (OPEN on general games; RESULTS R71 is per configuration), SW-RUN would give phase length
    ≤ (f + 1)·n·n_E.
  - Even readers are passive inside a fallback-free run, so SW-RUN must also survive them: a reader's switches there are max-aggregate changes.
    The longest fallback-free runs known are ~1.5n (§9), so this is not tested at scale.
  - SW-RUN climbs (swclimb.py RUN=1, 6,000 steps each; logs root/out/swr_*.log): from sc24 (seeds 7, 8) and from swlin_kill_n26 (seed 9).
    Best: 12 switches at n = 18 (0.67n), 14 at n = 21, 7 at n = 16. No kill; SW-RUN stays a CONJECTURE (DATA ≤ 0.67n).

## 12. Even readers: clean, and they raise the switches of ONE vertex (Lead 21:27Z, 21:35Z (a); written 2026-10-28 by date -u)
Tool: experiments/si/root/ereader.py. It appends an Even vertex e (priority 0, no predecessors, edges to S in one class, start σ0(e) = Y),
checks SAME (σ, τ, σ̄ on the old vertices and the fallback flags, at every state) and counts e's switches. --search runs a local search over S
for the most switches in one phase subject to SAME. Log: root/logs/ereader_l121.txt.
- CORRECTION (REFEREE READ-N3, and my own measurement below): an Even reader is NOT clean in general. REFEREE's Lemma (b) fails for it (Iσ
  gains its edges and S4a moves it), and at a base fallback its S4a switch cancels S4c. Random Even readers (ereader.py --random, |S| = 4,
  Y random in S; log root/logs/ereader_random.txt): SAME on long121 60 of 60, on lend107 45 of 60, on swlin_kill_n26 58 of 60. In 16 of the 17
  failures the first divergence is at a base fallback. So the searches below (which keep only SAME candidates) show that SOME Even readers are
  clean and raise one vertex's switches; the table's instances are each checked SAME. The text that follows was written before this
  measurement; its "every candidate accepted" is a property of the search, not of Even readers.
- Measured reason why an Even reader is clean (DATA, every instance tried, 3 searches × 400 candidates):
  - in every candidate accepted by the search the run stayed SAME, fallback flags included;
  - in a fallback-free stretch e has no predecessor, so S4a's pointwise arena optimum for the others is unchanged;
  - at a fallback state S4c switches every Even vertex with an improving edge, e among them, without touching the others' choices.
  - The only way e could change the run is to switch at a state where the base step was a fallback (σ' = σ), turning S4c into S4a. This did not
    happen in any candidate the search kept. My §9 sentence "an Even reader blocks fallbacks" was an unmeasured reading. It is corrected there.
- Even readers DO raise the switches of ONE vertex (the reader itself) above the base's maximum, with the run SAME:
  | base | base: most switches of one Even vertex in its longest phase | Even reader e: switches in that phase (max in one fallback-free run) | S, Y |
  | --- | --- | --- | --- |
  | long121_n40 (phase [1, 122]) | 12 (vertex 34) | 16 (3); instance l121ereader_n41 (sha1 a67da45f…, start 4cec1a16…) | 13 vertices of class 11, Y = 30 |
  | lend107_n32 (phase [2, 110]) | 11 (vertex 21) | 15 (3) | {0, 10, 15, 24, 25, 28}, Y = 24 |
  | swlin_kill_n26 (phase [1, 47]) | 27 (vertex 19) | 26 (6) | {0, 10, 12, 13, 19, 23, 25}, Y = 10 |
  - So, like XR (§8), the per-vertex switch count, and the total Σ_w SW(w), can be raised by passive vertices. The phase length cannot. (C2)
    PHASE-SW stays true, because adding switches only loosens it.
  - Per fallback-free run, the reader's switches stay small (≤ 6). Every count that is invariant under readers is a function of the number of
    transitions, not of which vertex moves.
- Consequence (READING): no per-vertex localisation (XR, SW, gate changes, exits) is smaller than the phase length. A proof has to bound the
  number of transitions directly: by a potential on the whole state, or by counting events that a passive vertex cannot create (each
  transition's set of switching vertices is not such an event, since readers add to it).

## 13. Transition counts (Lead 22:06Z item 4; Lead reading: state bounds in transitions per phase, not per vertex)
- (PROVED, elementary) A phase P with f in-phase fallbacks splits into f + 1 fallback-free runs (some possibly empty), so
  |P| = f + Σ_runs |run| ≤ f + (f + 1)·max |run|.
- DATA (alt_all, 413 games n ≤ 600; lib41 n ≤ 48, S3):
  - the longest fallback-free run is 49 transitions (run49_n32, 1.53n); on lib41 34 (pftheta_cex_n32, 1.06n);
  - the most in-phase fallbacks in one phase is 37 at n = 48 (rise_fb38_n48, 0.78n); on lib41 33 at n = 48 (ccl_w48_n48);
  - the longest phase is 108 (lend107_n32, 3.38n). Long phases have short runs and many fallbacks, so the product bound above is far from tight.
- CONJECTURE RUN-LIN: every fallback-free run of a phase has ≤ 2n transitions. CONJECTURE FB-LIN: every phase has ≤ n in-phase fallbacks.
  Together they give |P| ≤ n + (n + 1)·2n. Both count transitions, so readers cannot inflate them (Theorem READER-INV under (R), REFEREE).
  Relation to landed text: RESULTS R71 FB-C bounds f per phase by |𝒞_f(P)|·(4n² − 3n), and R73 FB-C′ by n·|𝒞_f(P)|. FB-LIN would need the
  configurations at fallback sources to be O(1) per phase, or a different argument.
- Climbs (experiments/si/root/runfbclimb.py, box43 mutations, 5,000 steps each; logs root/out/rl_*.log, fb_*.log): OBJ=run from run49_n32
  (seed 11) and so_th_n32 (seed 12); OBJ=fb from farrise25_n32 (seed 13) and ccl_fbx_n32 (seed 14). No improvement over the seeds. The best stay
  run 49 at n = 32 and fallbacks 25 at n = 32. No kill.

## 11. The PROVED core in one place (freezable as a packet once a count has a proof route; Lead 21:35Z (b))
Labels: PROVED (lane, unrefereed). Every game, inside one phase P of N5 (τ and λ constant, RESULTS R38 (a)). Premises: SPEC S1-S5 with the
standing premise 1E-N3 (P1: σ̄ is Odd's pointwise-optimal strategy against σ, as P-N5-FLIP §1 names it); (SW) every Even switch of N5 is to an
edge of Iσ (S4a's arena and S4c's switch-all both take Iσ edges); RESULTS R15 (a) (Ξ_t ⊴ Ξ_{t+1} pointwise at in-phase transitions); for RISE-GATE
only, κ-Y-FORM_D (RESULTS R56 (d)) and Fact CL (N5-EXIT §2, restated from landed premises). Not used: MONO-REF, OFFSET-MONO, PURE-LEN, GATE-PUSH,
E-ONEWAY (so REFEREE's DEPTH-add gaps G-DADD-1 / G-DADD-2 do not touch this core).
- (C1) EVERY-SWITCH. Every in-phase transition changes σ. An S4a step that changes neither σ nor τ is a fallback (S4c). A fallback with
  Iσ ≠ ∅ switches every Even vertex with an improving edge, and one with Iσ = ∅ changes τ, which ends the phase.
- (C2) PHASE-SW. |P| ≤ Σ_w SW_P(w), where SW_P(w) is the number of transitions of P at which Even w switches. Immediate from (C1).
- (C3) RISE-SW (§1). If Even w switches at an in-phase transition and is on no honest cycle at t or at t + 1, then Ξ_{t+1}(w) ▷ Ξ_t(w).
  So SW_P(w) ≤ XR_P(w) + (switches of w at transitions where it is on an honest cycle).
- (C4) RISE-GATE (§1). At an in-phase gate change y1 → y2 at u, u off honest cycles at t and t + 1: Ξ_{t+1}(y1) ⪰ Ξ_t(y1), strictly unless
  Ξ_{t+1}(y1) = Ξ_{t+1}(y2).
- (C5) FRESH-RED (§1, §7). For any interval I of a fallback-free run of P: |I| ≤ m_E + NOFRESH(I), where NOFRESH(I) counts the transitions of
  I at which every switching Even vertex returns to an edge it held at an earlier state of I. (C1) and an injective map to edges.
- (C6) FRESH3-COUNT (§3). On a global C-interval I = [a, b]: transitions with a fresh Even edge ≤ m_E, with a fresh gate option ≤ Σ_{u ∈ D} deg(u),
  with A_{t+1} ⊊ A_t ≤ |A_a|.
What these do NOT give: a bound on SW, XR, NOFRESH or the flip-flops. §8 and §10 kill the per-vertex forms XR-LIN and SW-LIN; SW-RUN is open.

## 6. OPEN
1. XR-LIN is DEAD (§8: l121reader_n41, XR 86 > 2n = 82). Its old statement was: in every phase, every vertex's Ξ changes ≤ 2n times. Data maximum 1.80n. It implies phase length ≤ 2n² (RISE-SW,
   off-cycle switches) and ALT + (G1) ≤ 2n·m (RISE-GATE), up to ties and cycle cases. It is the whole problem localised to one vertex, not a
   reduction in difficulty.
2. (G1), repaired: FRESH3 plus a charging of the one-vertex flip-flop (ret14_n48) to a fresh event or to an Iτ = ∅ argument.
3. §5 (c): does τ's optimality on the phase (Iτ = ∅ at every state) limit the re-entries in the counter recursion? First test: on lev_l_sc,
   ret14_n48 and nep92_n40, for each re-entry of an odd vertex h into z's path set below the top change, record whether h's region contains a
   gate whose τ-option is strictly better for Odd at that state.
4. Lead's DATA step on [F]'s H_n (routed elsewhere): if N5 runs H_n in one phase, XR there is the counter, and this note's reductions price it.
