# L-ALG notebook — HANDOVER (docs/agents/LANE-RESTART.md step 1), written 2026-10-15 15:40Z by the parked session

## Resume point
- PARKED. Successor: a written proof attempt of a polynomial bound on DTL's tangle count and running time, starting from
  L-RED R8 Lemma M (claude/l-red b72707e, docs/red/R8-DTL.md) — Lead 15:35Z. Branch claude/l-alg; trunk claude/vibrant-johnson-nxvvxo.
- Lead session for messages: session_014FBi6o334DvwT5Uw2kDfoN. Push: scripts/verify.sh && git push -u origin claude/l-alg.

## DONE (all on claude/l-alg; verify PASS at every push)
- C1 NE(k), C2 NE'(k) (nested fatal attractors): DEAD, depth = Strahler number − 1 = register number; family S_s
  (experiments/alg/strfam.py); killers instances/c1_k*_min*.pg, out/c2k1_fail_seeds.jsonl (docs/alg/DEAD.md, candidates/C1.md, C2.md).
- C3 ZP (Zielonka + psolC pruning): DEAD, family T_R (instances/zp_tile8_R*.pg; ×30 recursive calls per tile) and GA table.
- C4 TL×H (tangle learning on the prefix-maximum product): DEAD on tc (c4_product.py).
- T-ALG1 (docs/alg/T-ALG1.md): (a) psolC complete iff Strahler 1 — proved in prose, UNREFEREED, deferred by the Lead;
  (b) sharpness data; (c) conjecture NE'(k) complete iff Strahler ≤ k+1 (data: 84,571 Strahler-2 games, 45 Strahler-3 killers).
- C5-DTL (docs/alg/candidates/C5-DTL.md): provenance, line-mapped transcription of Oink dtl.cpp, correctness + verified
  strategies on 67,000+ games (dtl_check.py), growth tables on all families (ptl_sweep.py, dtl_growth.sh), DTL attack with
  tc/tc+ variants: nothing super-polynomial (REPORT table). Findings for the bench: tc+ beats PTL/SPPTL; T_R hard only for
  already-beaten solvers.
- Report: docs/alg/REPORT-2026-10-15.md; data ledger docs/alg/RESULTS.md. Tools: experiments/alg/ (README-level docstrings in each file).

## IN FLIGHT
- none. No background jobs, no timed wakes.

## NEEDS
- Lead: route T-ALG1 (a) to L-LIT + two referees when free (deferred 11:20Z). Nothing else.

## Things only I know
### DTL facts for a proof writer (from reading tools/oink/src/src/solvers/dtl.cpp at 8fbf0a7; line numbers refer to that file)
1. Vertex order: Oink sorts vertices by priority before solving (oink.cpp:35 `game.ensure_sorted()`); every "for top =
   nodecount()-1 down to 0" loop is a descending-priority sweep and `priority(nodecount()-1)` is the maximum priority.
2. Release path vs. trace: `computeDistanceValues` (553-639) is called only inside `#ifndef NDEBUG` / `if (trace)` blocks in
   `search` (1003-1012, 1042-1066): it is NOT part of the algorithm. `curdist` in best_vertices (655, 675) is only printed.
   Everything else under `trace` is logging. The work counter "N tangles" printed by `-v` is `tangles` (463): new, non-duplicate,
   non-dominion tangles; "dominions" (375) separately; "iterations" = calls of search (1111, 1119).
3. Attractor mechanics (40-101): `attracts(pl, v, Z, R)` = p's vertex with an edge into Z, or opponent vertex with an edge into
   Z and NO edge into R \ Z (edges to vertices outside R ∪ Z are ignored). `attractVertices(pl, v, R, Z, Gx, maxpr)` is one
   BFS step over the predecessors of v with a FIFO queue Q (uintqueue): u ∈ R with pr(u) ≤ maxpr is added to Z if p's or if the
   opponent's u has no edge into Gx \ Z; p's strategy str[u] := v at first attraction, and a u already in Z with str[u] = −1
   gets str[u] := v (72-73): tops get a strategy from the first attracted predecessor loop. Gx (the escape set) is R or CurR in
   best_vertices/sptl/search_rec, and G in `search` (1036). Callers that remove v from R on pop (`R[v] = false`): sptl (490),
   best_vertices' region pass (699), Dom(V,R) in search_rec (885, 969), the threshold attractor (920); best_vertices' threshold
   loop does NOT remove from R (727-731).
4. Tangle attraction (109-202): a tangle t is attracted only if its parity is pl, it is not deleted, all its vertices are in
   Z ∪ R and ≤ maxpr, at least one is not yet in Z, and every escape (tout) is in Z or outside Gx. A tangle with a vertex outside
   G (solved) is deleted lazily (tpr := −1). `tin[v]` lists tangles with escape v; attractTangles(v) tries exactly those.
5. Pruning loop best_vertices (643-776): V := p-priority vertices of R. Each round: regions for each top ∈ V from high to low,
   each computed from a FRESH copy CurR of R (690-706), so regions overlap and Z is their union; Candidates := v ∈ V with
   ¬attracts(p, v, Z, R), listed in DESCENDING index; if none: return 1. Threshold loop t = 0..maxpr (722-741): Q := every
   vertex of Z (re-pushed at each t), attract within R to Z with threshold t (no removal from R), then clear each candidate u
   with pr(u) > t that now attracts (the scan breaks at the first candidate with pr(u) ≤ t, so candidates are cleared only at
   thresholds strictly below their priority). Remaining candidates are removed from V. Return 1 if nothing removed, −1 if V became
   empty (V := prevV, the last non-empty V), else next round. A vertex removed in one round never returns within the call;
   across calls V restarts from all p-priority vertices of R.
6. sptl (476-546): called on a COPY of R (search_rec 871: `Z = R; sptl(V, W, Z, player)`), so its consumption of R does not
   touch search_rec's R. For each top ∈ V ∩ R descending: region by attraction with threshold pr(top) (removing from the copy);
   closed iff (p's top has str ≠ −1) or (opponent's top has no edge into the remaining copy); if closed and top ∉ W (W = tops
   already done in this search; reset in search 1016): extractTangles(top, Z, str). W is per search(), not per sptl call.
7. extractTangles (210-471): Pearce SCC on the graph restricted to the region Z where p's vertices follow str only and the
   opponent keeps all edges inside Z, STARTING from top: only SCCs reachable from top are found. Nontrivial SCC with no
   opponent edge leaving to G \ SCC = dominion (vertices + str to the solve queue); else duplicate check against all existing
   tangles by sorted vertex set (CHECK_UNIQUE is on: `(1 or !NDEBUG)`), else new tangle with priority pr(top).
8. search_rec (834-994): loop {best_vertices; 0 → return; 1 → repeat sptl until no change, then Dom(V,R) → X (regions of V
   with threshold pr(top), removing from R); −1 → find the LOWEST priority level t of R whose vertices attract to X (scan
   ascending; t advances only while Q is empty: 898-912); if found: attract R to Z with threshold t (removing from R), move the
   threshold-t vertices of Z to X, let the OPPONENT attract within Z to X with threshold t using attractVertices only (947: no
   tangles; Gx = Z), X |= Z, recurse search_rec(Z, p, depth+1); else Dom(V,R) → X with V = prevV}. The recursion is the only
   Zielonka-like branching; depth is unbounded by any explicit check.
9. search (997-1069): search_rec on a copy of G; then found dominions are extended by the p-attractor within G with NO
   priority bound and WITH tangles (1036-1037), solved and removed from G; returns whether tangles or dominions changed.
10. run (1071-1161): dtl = Even to exhaustion (search(0) until it returns false), then Odd; the loops stop when a search finds
    nothing even if G ≠ ∅ (the "search was incomplete!" check is NDEBUG-only) — never observed in 67,000+ games. idtl alternates
    search(0), search(1) and throws "solver stuck" if neither finds anything.
11. Where C5-DTL.md simplifies: it omits all trace/NDEBUG code; it writes "Q := all of Z" for the threshold loop (exact); it does
    not spell out that `attracts` ignores edges leaving R ∪ Z, that sptl runs on a copy of R, that W is per search, that the
    opponent's attractor on the −1 branch is tangle-free, or that extractTangles sees only SCCs reachable from top. All of these
    are in items 3-9 above.
### Scripts that reproduce the counts (experiments/alg/; out/ is gitignored, regenerate)
- DTL correctness + strategies: `python3 dtl_check.py --solver dtl --n4-random 20000` (needs out/psolc_fail_n4.jsonl from
  `python3 psolc_fail_n4.py 4 --workers 3`, 518 s). Family tangle tables: `python3 ptl_sweep.py --solvers ptl,spptl,tl,dtl`,
  `bash dtl_growth.sh`; tc wall time: the loop recorded in notes (oink --dtl -v --no-single --no-wcwc on tc N).
- tc / tc+ ports and variants: `python3 tcvar.py N [--dd --lane k --gates k --zshift s]`, `python3 tcvar_sweep.py`,
  `python3 tcplus_sweep.py`, `python3 tc_local.py N STEPS SEED`, `python3 tc_template_ga.py GENS SEED --nfit 7 --growth`,
  `python3 tcplus_template_ga.py GENS SEED --nfit 6`; Oink work counters via oink_fit.work(game, solver, raw=True).
- Families: S_s `strfam.py`; T_R `zp_curve.py out/zp_ga_K8_s1.jsonl 18 '[[0,-1,7],[21,1,4]]'` (instances/zp_tile8_R*.pg are
  committed); Oink sweep on T_R `bash oink_sweep.sh`; C1-C4 regressions `bash check.sh` (13 s, part of scripts/verify.sh).
- Oink is built by scripts/setup_oink.sh (pinned 8fbf0a7 = upstream master); trace: `oink --dtl -t -t` (prints "distance k:" lines).

## Sources opened (this lane)
- Daviaud, Jurdzinski, Thejaswini, "The Strahler number of a parity game", arXiv 2003.08627v2: p.4-5 definitions, Prop. 3,
  Lemma 7 + Thm 8 (Strahler = Lehtinen register number), Thm 32.
- van Dijk, GandALF 2019 talk slides (tvandijk.nl/pdf/2019gandalf_talk.pdf): slide 42 (path-based variants unpublished,
  "VULNERABLE! (to a different version of the TC game)"), slide 43 ("distance to opponent region").
- van Dijk, "Avoiding Distractions in Parity Games", ISoLA 2024, LNCS 15221, DOI 10.1007/978-3-031-75380-0_19 (author PDF
  tvandijk.nl/pdf/2024isola_rtl.pdf): rtl/ortl, Fig. 6 = counter_ortl, Fig. 7 = tc+, section 4 good paths; no dtl.
- Oink repository history (tools/oink/src): dtl.cpp commits e67cb4c 2019-09-14 ... 1ba8b0a 2021-07-02 (rename); counter_dtl
  never committed. HKP DTR15-4 used only through experiments/attr/psolc.py (REFEREE FAITHFUL, referee 1600917).

## Dead ends (fleet list: docs/alg/DEAD.md)
- C1, C2: nesting depth = Strahler − 1 (family S_s). C3: T_R (×30 per tile). C4: tc. DTL attack: all tc/tc+ variants polynomial.
