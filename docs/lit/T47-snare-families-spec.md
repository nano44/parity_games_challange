# T47: construction specs of PGSolver's friedmannsubexp and fearnleysubexp (snare-rule lower-bound families), for L-COMP's independent port
L-LIT successor 3 (Opus 5.5), D18. Lead's message 15:39Z: «transcribe PGSolver's friedmannsubexp.ml and fearnleysubexp.ml ... into precise
construction specs ... For each generator give: vertex classes, owners, priorities, edges as functions of the parameter, and the intended
initial strategy if any. Add a reference generator script ... state your sources' line numbers.» Written 2026-10-29 from 15:41Z (date -u).
SOURCE (read only, git clone): github.com/tcsprojects/pgsolver commit d3cd624b61cd66739c45aff9554f6bbdcdd05401 (= the pin of
experiments/hard-families/pgsolver_port.py), files
  F = src/lib/generators/policyiter/generators/friedmannsubexp.ml (90 lines; ident "friedmannsubexp", l.86-87 «Friedmann's Subexponential
      Lower Bound for snare-based rules»; generator l.34-82),
  R = src/lib/generators/policyiter/generators/fearnleysubexp.ml (86 lines; ident "fearnleysubexp", l.82-83 «Subexponential Lower Bound for
      Fearnley's rule»; generator l.31-78; option "-nogadget", l.36),
  SPG = src/lib/generators/policyiter/stratimprgenerators.ml l.7-47 (SymbolicParityGame), OUT = src/lib/paritygame/paritygame.ml l.365-386.
Reference script: docs/lit/T47-gen-pgsolver-snare.py (written from the OCaml only; it does NOT import pgsolver_port.py). This is a
transcription; NOT checked against a PGSolver binary (no OCaml toolchain in this container). The papers behind the families (Friedmann, DAM 161
(2013) 1317-1337, DOI 10.1016/j.dam.2013.02.007; Fearnley's rule = arXiv 1003.2976) are NOT the source here: the generator code is. DAM 2013 is
NOT OPENED (T46).

## 0. Conventions common to both (SPG, OUT)
- Players: plr_Even = 0, plr_Odd = 1 (paritygame.ml l.130-139, as pgsolver_port.py's docstring). Max-parity, priority mod 2 = winner.
- Vertex ids: a symbol gets the next id (0, 1, 2, ...) the FIRST time it is mentioned, either as the node of an `add` call or as a successor in
  an `add` call's list (SPG l.27-45: add_node first registers the node itself (override = true), then each successor in list order (override
  = false, "touch")). So ids follow the order of `add` calls in the source, with forward references numbered when first touched. Ids are
  therefore part of the spec: §3 lists the call order exactly as the source.
- Successors are a TreeSet: printed sorted by id, duplicates merged (SPG l.16-25 iterates TreeSet). No duplicates arise here.
- Output (OUT): `parity <N-1>;` then one line per id `i pr pl s1,s2,... "desc";` (desc = symb_to_str, F l.29 / R l.26). Nodes with pr < 0
  would be skipped; every touched symbol is added in both generators (the script asserts it).
- Priorities are NOT injective (several classes share 2, 3, 4, 5); SPEC S1's (Ω, index) tie-break applies.
- Names (symb_to_str): a_i DecLaneEven, t_i DecLaneOdd, c DecLaneRoot, d(i,j) CycleNode, e_i CycleCenter, m_i CycleCenterBadEntry,
  q_i CycleCenterBadEntryX, u(i,j) CycleNodeCho, v(i,j) CycleBadEntrySel, w(i,j) CycleBadEntrySelX, f_i CycleAccess, g_i CycleSelector,
  h_i CycleLeaver, k_i UpperSelector, z FinalSink, x FinalCycle, s StartEven, r BitSelector; F only: b(i,j) CycleNodeSpecial,
  l(i,j) CycleNodeSpecialX, p(i,j) CycleNodeSpecialY.

## 1. friedmannsubexp(n), n ≥ 1 (F l.34-82)
Vertices: 4.5n² + 10.5n + 5 (= 5 + lane 6n + 9n per-bit + 6·C(n,2) lower-gadget + 3·C(n,2) upper-gadget). Checked by the script: n = 1..5 →
20, 44, 77, 119, 170 vertices; edges 41, 101, 186, 296, 431.
| class (index range) | owner | priority | successors, in source order | line |
| --- | --- | --- | --- | --- |
| x | Odd | 1 | x | 43 |
| s | Even | 10n + 8 | z, f_0, ..., f_{n−1} | 44 |
| c | Even | 10n + 6 | s, r | 45 |
| r | Even | 10n + 10 | z, g_0, ..., g_{n−1} | 46 |
| z | Odd | 18n + 12 | x | 47 |
| a_i (0 ≤ i < 3n) | Odd | 4n + 2i + 6 | t_i | 50 |
| t_i (0 ≤ i < 3n) | Even | 4n + 2i + 5 | i = 0: c, r, s; i > 0: t_{i−1}, r, s | 51 |
| u(i,j) (0 ≤ j < i < n) | Even | 3 | v(i,j), w(i,j), b(i,j) | 56 |
| b(i,j) (j < i) | Even | 5 | l(i,j), p(i,j), X | 58 |
| l(i,j) (j < i) | Even | 4 | v(i,j) | 59 |
| p(i,j) (j < i) | Even | 4 | w(i,j) | 60 |
| v(i,j) (j < i) | Odd | 3 | m_j, X | 61 |
| w(i,j) (j < i) | Odd | 2 | q_j, X | 62 |
|  where X (j < i) = e_i if j = 0, else u(i, j−1) |  |  |  | 57 |
| u(i,j) (i < j < n) | Even | 3 | v(i,j), w(i,j) | 65 |
| v(i,j) (i < j) | Odd | 3 | m_j, Y | 67 |
| w(i,j) (i < j) | Odd | 2 | q_j, Y | 68 |
|  where Y (i < j) = (if j = i + 1: e_0 when i = 0, else u(i, i−1)); (if j > i + 1: u(i, j−1)) |  |  |  | 66 |
| d(i,1) | Even | 4i + 3 | s, d(i,0), a_0, ..., a_{3i+2}, r | 70 |
| d(i,0) | Even | 4i + 3 | s, Z, a_0, ..., a_{3i+2}, r; Z = e_i if n = 1; u(i, n−2) if i = n−1 (n > 1); u(i, n−1) otherwise | 71-72 |
| e_i | Odd | 4i + 6 | d(i,1), h_i | 73 |
| m_i | Odd | 10n + 11 + 2i | e_i | 74 |
| q_i | Odd | 12n + 6i + 15 | h_i | 75 |
| h_i | Odd | 12n + 6i + 16 | k_i | 76 |
| k_i | Even | 12n + 6i + 11 | z, g_{n−1}, g_{n−2}, ..., g_{i+1} (mkli (n−i−1) (fun j -> g_{n−j−1})) | 77 |
| f_i | Odd | 12n + 6i + 13 | e_i | 78 |
| g_i | Even | 4i + 8 | f_i, k_i | 79 |
Reading of the structure (READING, not from a paper): for bit i the cycle is d(i,1) → d(i,0) → [chain of u(i,·)] → e_i → d(i,1), Odd's
e_i escapes to h_i; the u-chain (Even choices u, Odd selectors v/w with exits to m_j (→ e_j) and q_j (→ h_j)) links bit i's cycle to every
other bit j; the lower part (j < i) adds the b/l/p "special" Even nodes. Lane a/t of length 3n as in Friedmann's G_n/H_n.

## 2. fearnleysubexp(n), n ≥ 1, and -nogadget (R l.31-78)
withfearnley = true by default; "-nogadget" sets it false (R l.34-36, 58, 66, 68). Vertices: with gadget 1.5n² + 13.5n + 5 (n = 1..5: 20, 38,
59, 83, 110; edges 41, 89, 150, 224, 311); -nogadget 13n + 5 (18, 31, 44, 57, 70; edges 39, 79, 126, 180, 241).
| class | owner | priority | successors, in source order | line |
| --- | --- | --- | --- | --- |
| x | Odd | 1 | x | 46 |
| s | Even | 10n + 6 | z, f_0, ..., f_{n−1} | 47 |
| c | Even | 10n + 4 | s, r | 48 |
| r | Even | 10n + 8 | z, g_0, ..., g_{n−1} | 49 |
| z | Odd | 18n + 10 | x | 50 |
| a_i (0 ≤ i < 3n) | Odd | 4n + 2i + 4 | t_i | 53 |
| t_i (0 ≤ i < 3n) | Even | 4n + 2i + 3 | i = 0: c, r, s; i > 0: t_{i−1}, r, s | 54 |
| u(i,j) (i < j < n; gadget only) | Even | 3 | v(i,j), w(i,j) | 60 |
| v(i,j) (gadget only) | Odd | 3 | m_j, Y | 61 |
| w(i,j) (gadget only) | Odd | 2 | q_j, Y | 62 |
|  where Y = e_i if j = i + 1, else u(i, j−1) |  |  |  | 61-62 |
| d(i,1) | Even | 4i + 3 | s, d(i,0), a_0, ..., a_{3i+2}, r | 65 |
| d(i,0) | Even | 4i + 3 | s, Z, a_0, ..., a_{3i+2}, r; Z = e_i if i = n−1 or no gadget, else u(i, n−1) | 66 |
| e_i | Odd | 4i + 4 | d(i,1), h_i | 67 |
| m_i (gadget only) | Odd | 10n + 9 + 2i | e_i | 69 |
| q_i (gadget only) | Odd | 12n + 6i + 13 | h_i | 70 |
| h_i | Odd | 12n + 6i + 14 | k_i | 72 |
| k_i | Even | 12n + 6i + 9 | z, g_{n−1}, ..., g_{i+1} | 73 |
| f_i | Odd | 12n + 6i + 11 | e_i | 74 |
| g_i | Even | 4i + 6 | f_i, k_i | 75 |
Differences from F (DATA, by the diff of the two sources): all "large" priorities are 2 lower in R (s, c, r, z, a, t, m, q, h, k, f, g; e_i
4i + 4 vs 4i + 6); R has no lower gadget (j < i: no u/b/l/p/v/w), and its upper chain's base is Y = e_i for every i (F: e_0 only for i = 0,
else u(i, i−1)); d(i,0)'s Z ignores n = 1 specially only through i = n − 1.

## 3. Call order (determines the ids; both generators)
F: x, s, c, r, z (l.43-47); for i = 0..3n−1: a_i, t_i (l.49-52); for i = 0..n−1: [for j = 0..i−1: u(i,j), b(i,j), l(i,j), p(i,j), v(i,j),
w(i,j)]; [for j = i+1..n−1: u(i,j), v(i,j), w(i,j)]; d(i,1), d(i,0), e_i, m_i, q_i, h_i, k_i, f_i, g_i (l.54-80). Each `add` touches its
successors in list order right after the node itself. Example (script, n = 2): ids 0 x, 1 s, 2 z (touched by s), 3 f0, 4 f1, 5 c, 6 r, 7 g0,
8 g1, 9 a0, 10 t0, ... (file sha1 13d55b1d).
R: x, s, c, r, z; a_i, t_i; for i: [gadget: for j = i+1..n−1: u(i,j), v(i,j), w(i,j)]; d(i,1), d(i,0), e_i, [gadget: m_i, q_i], h_i, k_i,
f_i, g_i.
Pinned outputs of the script (sha1 of the .pg text, n = 1..5): friedmannsubexp aaf6175a, 13d55b1d, 90773868, 280e5e7c, 52f345dd;
fearnleysubexp 05a19c05, 77cfde64, 0e46c8e5, ad297bca, 5350cad3; fearnleysubexp -nogadget d89528f5, 1c062ba5, 917a3a61, 81fbd1f3, 87d894b1.

## 4. Intended initial strategy
- The generators define NONE (F and R build only the game; register_strat_impr_gen has no start field, stratimprgenerators.ml l.52-57).
- PGSolver's snare-memorization solver ("snarememo", switch_snare.ml l.82-91) runs `strategy_improvement game initial_strategy_by_best_reward
  ...` (l.83): Even's start = per vertex the successor of maximal reward (stratimpralgs.ml l.85-87; = SPEC S3 / FIX 1 for Even). So the
  natural start for these families is S3's best-reward start. (strategy_improvement_by_policy, used by other policies, starts from
  initial_strategy_by_last_edge instead, stratimpralgs.ml l.636-637 — not the snare solver's.)
- Caveat: PGSolver's command line runs solvers through universal_solve (switch_snare.ml l.90), which may preprocess the game (SCC
  decomposition, priority compression) before strategy improvement; a fleet run on the raw .pg from S3's start is therefore not guaranteed to
  replay PGSolver's iteration counts. L-COMP's existing binary-diff method (pgsolver-binary-diff.md) is the way to pin that, if an OCaml build
  becomes possible.
- No ι-type designed start (as Friedmann's ι_{H_n}) appears in the source. Odd's start: none needed by PGSolver (Odd best-responds); for
  N5 / N5-SF use S3's dual rule (as L-COMP's F/S3 conventions).

## 5. Sanity (DATA, not a result)
Every vertex has a successor; SPEC N5 (n5.run, from S3) solves both families for n = 1..3 with Odd winning everywhere (as for Friedmann's
sink games, x has priority 1): friedmannsubexp 4, 10, 15 iterations; fearnleysubexp 4, 8, 12. No N5-SF runs here (the adversary's job).

## DONE / FINDINGS / NEEDS
- DONE: this spec; docs/lit/T47-gen-pgsolver-snare.py (pinned outputs above).
- FINDINGS: both families = Friedmann-style lane + bit cycles (d(i,1), d(i,0), e_i) + a u/v/w chain from each bit cycle to the other bits'
  bad entries m_j (→ e_j) and q_j (→ h_j); friedmannsubexp adds a lower gadget (b/l/p) for j < i. No designed start in the source; the snare
  solver starts from best reward.
- NEEDS: none from the owner. For L-COMP: diff its port against the pinned sha1s; open issue = an OCaml build to check against PGSolver.
