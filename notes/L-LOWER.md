# L-LOWER notebook (T-L2 theory box, successor session; updated 2026-10-15 ~10:45Z, box ends 20:36Z)
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
Branch claude/l-lower. Read docs/lower/L2-theory.md first (the box's product), then L1-statement.md (model), L1-report.md,
L2-data.md. Running at the time of writing (logs in experiments/lower/, detached with setsid): result_b2_n5_k9.log
(general n = 5 at 9 gates, seeded with the 414-game k = 8 core; one SAT call may take hours), result_k5_deg2_k8.log and
result_k5_deg2_k9.log (family K_5, exact CEGAR). If they finished: a RESULT line ends each log; UNSAT at k = 9 means
B_2(5) ≥ 10 (gap grows); write it into L2-theory §4/§6.

## DONE (this box; see docs/lower/L2-theory.md for everything, with SHAs and commands)
- MECHANISM (the box's main finding, data): the gate above 2n − 2 is the price of serving two COUNTS of priority-2 vertices
  with one vertex-anonymous program. n = 4: every single count costs 6, every pair of counts except {1, 2} costs 6, {1, 2}
  costs 7 (class table, L2-theory §3). n = 5: |P_2| = 1 costs exactly 8 (C3, full sweep of 4.58e9 games), |P_2| ∈ {1, 2}
  costs ≥ 9 (C2'), the general class ≥ 9 (C2, two solvers), the family K_5 ≥ 9.
- B_2(4) ≥ 7 certificate minimised: 68 whole games / 217 vertices (b2_n4_k6_core3.json), UNSAT by 4 solvers; localised
  to the class K (one Even vertex e of priority 1, Odd a (P_2), b (P_2 or P_1), c (P_1), all out-degrees 2): 28 games
  (core_exact_k6.json), 97 bisimulation classes (qcore_exact_k6.json), 53-pair kernel. Table of classes in L2-theory §3.
- B_2(5) ≥ 9: 414-game core b2_n5_k8.json, UNSAT by CaDiCaL (29 min) and Glucose (50 min).
- Lemmas 2.1 (one bit per gate), 2.2 (tower) in L2-theory §2.
- Goal (a) (human-readable proof): NOT achieved; obstruction measured (DRUP 63k lemmas; chain-only enumeration 8 561
  partitions at level 4; last gate has > 1000 admissible sets). Goal (b): family K_n defined; growth unproved; data gap ≥ 1
  at n = 4, 5.

## IN FLIGHT
- result_b2_n5_k9.log (general, k = 9; round 2 with 614 games started ~13:30Z), result_k5_deg2_k9.log (K_5, k = 9),
  result_b2_n5_k9_p2sz1-2-3.log (|P_2| ∈ {1,2,3}, k = 9, seeded with the 612-game {1,2} core). UNSAT in any = B_2(5) ≥ 10.

## NEEDS
- Lead: decision on parking (L2-theory §5b: recommendation = park the theory goal; keep the two cheap n = 5 experiments).
- Owner/Lead: an independent DRAT/LRAT checker is not available in this container (the platform classifier refused
  `curl` + `gcc` of drat-trim); the standard applied is "UNSAT by ≥ 2 independent solvers" (4 at n = 4, 2 at n = 5).

## Things only I know
Tooling quirks (in addition to the previous session's list, kept below):
- `pkill -f PATTERN` kills your own shell when PATTERN occurs in the command line you typed (it did, twice). Use
  `pgrep -f "^python3 -I script.py"` (anchored) and kill the PIDs.
- `cmd | tail -N` shows nothing until cmd ends; for long runs write to a log file and `tail -n` it.
- coremin2/coremin3/qmin minimise with ONE solver instance and assumptions (seconds per call); coremin.py (plain) costs one
  full solve per call (20 s at n = 4, 30 min at n = 5). Minimal cores are not unique; several orders, keep the smallest.
- The depth-type machinery (levels.py on a core, tower.py on all 51.9M (game, vertex) pairs, 16 min, 6 GB) shows the core
  needs modal depth 4 only; the 90 mixed depth-5 types of the full class live in other games (tower.py's M_6 list).
- cegar_owner.py classes: owner mask + P_2 masks + `FILTER` (numpy expression over deg(v), loop(v)); runs take seconds to
  minutes; the class table in L2-theory §3 is exactly these runs (logs result_*.log).
- sat_shape.py 'chain+j' shapes are NOT restrictive as written (they let all gates read all earlier gates): ignore those
  results; 'full' and 'chain' are correct.
- cegar5two.py samples random 5-vertex games (no full sweep): an UNSAT core is a proof, a SAT candidate is not an upper bound.
- Memory: a k = 9 instance with ~7 000 nodes is ~11M clauses (~4 GB); keep ≤ 2 such solves at once (16 GB cgroup).
Previous session's list (still valid):
- All SAT searches encode "program with k Cpre gates" by truth tables: gate i reads (P_2, V_E, s_1..s_{i-1}); the output is
  a truth table too. UNSAT on any successor-closed subset of games is a valid lower bound (projection argument).
- One-player: satsearch.py (exact on Q_n), cegar5b.py (n=5; W per priority pattern cached in $W5_CACHE); OOM at ~20e6 clauses.
- Two-player: vec2.py, sat2.py (`exact n kmax`, `cegar4 k per_round`), depth2.py (minimal depth, ~15 min, ~6 GB).
- Running detached: `setsid nohup python3 -I x.py > log 2>&1 &` (inside parentheses).
- One-player n=4 structure (L1-report §3): the 6-gate chain uses distance and two-visit bits (pigeonhole witnesses).

## Queue (if the lane continues)
1. Read the three n = 5 results; if k = 9 UNSAT: B_2(5) ≥ 10, update L2-theory §4, §5, §6 and L2-data table.
2. If k = 9 SAT with a candidate passing 2·10^6 random games: full sweep by (owner, priority) pattern (1024 × 28.6M games,
   ~1 h) before claiming B_2(5) = 9.
3. K_6 (cegar_class5.py generalised to n = 6; 2 × 15^6 = 22.8M games, sweep feasible) at k = 10, 11: growth of the gap on
   the family.

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| Chatterjee-Dvořák-Henzinger-Loitzenbauer, arXiv 1711.09148 v1 (SODA 2018) | §1 p.1-2 model and the "2n one-step operations" remark; §2 Preliminaries (Pre/Post, Set Disjointness, Thm 2.1); Reduction 3.1; Lemma 3.4 (O(1) bits per one-step op); Reduction 3.9 (p.7); Thm 3.10 (p.7) and its proof (p.13); Thm 3.11; §4 upper bounds (Büchi O(min(SCC+D, |T|·D))) | 2026-10-14 | pdftotext of arXiv v1 PDF; Reduction 3.9 graph has out-degree ≥ 1 everywhere |
| Arnold-Niwiński-Parys, LIPIcs.CSL.2021.9 (DOI 10.4230/LIPIcs.CSL.2021.9) | §2 fixed-point expressions, f_{A,B}, trees, Prop. 2.5 (S_{n,h} universal, width n^{lg(h/lg n)+O(1)}); §3.1 definition of ‖F‖_{U,V} (cases (1)-(3)), Lemma 3.1, Lemma 3.2 (|U|·|V| queries), Remark 3.3; §3.2 Algorithm 1, Lemma 3.4, 3.5, 3.6 (worklist, |V| to |V|(1+nd) queries), Cor. 3.7; Thm 5.1; Remark 5.5 | 2026-10-14 | DROPS PDF; intro p.9:2 states the symmetric bound n^{2·lg(d/lg n)+O(1)} explicitly |
| Bradfield-Walukiewicz, "The mu-calculus and model-checking", Handbook of Model Checking (author copy www.labri.fr/perso/igw/Papers/igw-mu.pdf) | formula (1), p.19 (after Theorem 7): μZ_{2d+1}.νZ_{2d}...νZ_0.γ with γ = ∧_i (p_i ⇒ (p_Eve ∧ ⟨b⟩Z_i) ∨ (p_Adam ∧ [b]Z_i)); Acc = limsup even (p.13) | 2026-10-15 | unnumbered display; typo γ(Z_0..Z_d); used for Transfer 2.4's vertex-priority form |
| Emerson-Jutla-Sistla, TCS 258 (2001) 491-522 (people.irisa.fr/Nicolas.Markey/PDF/Papers/tcs258(1-2)-EJS.pdf) | Theorem 3.2 (parity tree automaton emptiness as μ-calculus model checking), Lemma 3.5 | 2026-10-15 | numbered primary statement for the nested-fixpoint characterisation (automata form; index convention shifted) |
| Chatterjee-Dvořák-Henzinger-Svozil, arXiv 1909.04983 v1 | Algorithm 1 (black-box set-based progress measure), lines 3-16: worklist (popActiveSet) | 2026-10-14 | adaptive; used only for the CAUTION in Transfer 2.4 |
| REFEREE report R-L1 (claude/referee 9b01cbb, docs/referee/2026-10-14-L1-statement-check.md) and L-LIT T9 (trunk 735a4c7, docs/lit/T9-L1.md) | findings 1-9, gaps G1-G6; T9 (a), (b) | 2026-10-15 | fleet documents, not sources; drove v2 of the statement |

| Chatterjee-Dvořák-Henzinger-Loitzenbauer, arXiv 1706.04889 v1 (CSL 2017), "Improved Set-based Symbolic Algorithms for Parity Games" | §1 p.3 (classical set-based algorithm O(n^c) symbolic operations, O(c) sets); Theorem 20 (App. D.1: ClassicParity, O(n^c) symbolic one-step and set operations); Lemma 27 (App. D, "Simplified Analysis"): "O(n^2) symbolic one-step and set operations for c = 2", i.e. two-player Büchi; Theorems 8, 9 (c ≥ 3) | 2026-10-15 | adaptive model (attractors, repeat-until loops); no lower bound for games beyond the one-player Ω(n) of SODA'18; SODA'18 (1711.09148) itself contains no two-player statement (the word "game" occurs only in the grant line) |

## Dead ends
- T-L1 via depth/locality: capped at 2n-1 by Theorem B (docs/lower/L1-report.md §2); instance: the lasso pair of Lemma 2.1'.
- T-L1 via two-party communication (CDHL's method): capped at Θ(n) on Reduction 3.9 (two bits per Pre); no family found where a
  Pre costs O(1) bits and the problem costs ω(n) bits.
- Uniform O(n) construction for one-player Büchi from chains: window-1 chains need >= 12 gates at n=5 (UNSAT cores
  cegar5_k{8,9,10,11}_w1.json), window-2 >= 9 (cegar5_k8_w2_b.json); the n<=4 chains are pigeonhole witnesses specific to n.
- "e-profile" witness idea (colour vertices by exact min distance to P_2, follow e-decreasing paths; a losing graph then needs
  L+1 distinct vertices on a pattern path of length L): sound, but incomplete — the greedy path may run into a losing P_2 vertex
  (instance: v -> u_1 (P_2, u_1 -> z loop) and v -> long cycle with P_2); not pursued further.
- T-L1 itself: data against (B_1 = 2n-2 for n <= 5); parked by the Lead 07:50Z.
- T-L2 (a), human-readable proof of B_2(4) = 7 (2026-10-15): no short proof; instances b2_n4_k6_core3.json (68 games),
  core_exact_k6.json (28 games of class K), qcore_exact_k6.json (97 classes), qcore_exact_k6_pairs_k6.json (53 pairs);
  obstruction: DRUP 63 298 lemmas, chain-only case tree 8 561 live partitions at level 4 (docs/lower/L2-theory.md §3b).
