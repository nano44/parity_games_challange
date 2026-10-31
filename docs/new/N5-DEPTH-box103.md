# N5-DEPTH (box 103): no non-circular bound on the root-chain depth D_e. The deepest chains (topfix_N: depth 6N − 11) cycle through THREE Even vertices, one transition back per step: a rotating triple, box 96's stubborn-triple shape. So «D ≤ number of distinct vertices on the chain» is DEAD. Chain steps are W-changing transitions on all but the xing flat family (42 of 5,704 chain nodes are W-flat). The only proved bound is D_e ≤ (n − 1)(R*_F + 1) + FL_F (signed Lemma SUB). That is R95's WRUN-EQ core again (WRUN ⇔ R*-POLY ∧ FL-POLY), so route (b) adds nothing new
L-NEW successor 40 (Opus 5.5), D14 / D18, Lead reading L40. Lead 23:10Z: «BOX 103 (proof side), your call between: (a) LEVEL-ONCE … (b) The
root-depth bound D_e … Is there a non-circular bound, e.g. depth ≤ the number of W-changes or of distinct cycle nodes along the chain? My
suggestion is (b) first.» Written 2026-10-30 23:11Z-23:2xZ (date -u). Working note, unrefereed. Labels: PROVED (lane) / CONJECTURE / DEAD /
DATA. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Setting, tools
- Box 100: the Even root map and its chain of nodes (x, q). Box 102: LEVEL-ONCE ⇒ RET(X; e) ≤ deg X·(D_e + 1).
- RESULTS R95 (P-N5-WRUN, LANDED 22:14Z, line L-5):
  - «(Lemma SUB, signed by both referees …) [SUB] holds»: for every sub-interval F′ of every W-run, at most (n − 1)(R*_T(F′) + 1)
    transitions of F′ change W;
  - Corollary WRUN-EQ «WRUN-POLY ⇔ … ⇔ R*-POLY ∧ FL-POLY ⇔ …».
- Tool: experiments/new/box99/retcause.py now prints two lines.
  - CHAIN: the root chain of every return. Reports how many chains repeat an Even vertex, and the longest chain with its number of
    distinct vertices (CHAINS=1 lists the first 12 nodes).
  - CHAINSTEP: per distinct chain node (x, q), whether W changes at q, and whether x's new edge is a LATE ADOPTION, i.e. blocked at an
    earlier state of F. Blocked at t here means: W_t-better than σ_t(x), and not Ξ_t-improving.
- Corpus re-run (box99/runcause.sh; box101/cause_cascl.txt). Pin: new/check.sh «box 103 DEPTH».

## 1. DATA: what the deep chains look like
- topfix_n10 (default start, W-run 6-64, |F| 58, n 210). The longest chain has 50 nodes on 3 distinct Even vertices: (193, 58), (194, 57),
  (192, 56), (193, 55), (194, 54), (192, 53), … Each step goes back exactly one transition and rotates 193 → 194 → 192.
  - 208 of the 252 chains repeat a vertex. The same holds for topfix_N, N = 3 … 10: depths 8, 14, 26, 38, 50, always 3 distinct vertices.
  - Every chain node is a W-changing transition, and none is a late adoption (R*-type event = 0 on topfix's chains).
- The quadratic pins: chains have ≤ 3 nodes with no repeated vertex (sbq2 2, obs 3). Every chain node is W-changing, and none is late.
- Corpus (603 W-runs with returns + cascl_K4_m8_N100):
  - 5,704 distinct chain nodes; 5,662 W-changing; 256 late adoptions;
  - W-flat chain nodes (W unchanged at q) occur in 4 games of L-RED's xing family: u23sw64_n32 11, u1t_own6_n32 5, u1t_cex_n32 4,
    u2flat73_n32 1 (each counted in both list runs).

## 2. Results
- DEAD: «D_e ≤ the number of distinct (Even) vertices on the chain» (or any function of them alone). Instance: topfix_N, depth 6N − 11 on
  3 vertices.
- DEAD: «every chain node is a W-changing transition» as a universal statement. Instance: u23sw64_n32 (11 W-flat chain nodes).
- Lemma DEPTH-SUB (PROVED, lane; premises: box 100 FRESH-ROOT, signed [SUB] from R95). Every root chain has
  D_e ≤ #(W-changing transitions of F) + #(W-flat transitions of F) ≤ (n − 1)(R*_F + 1) + FL_F.
  - Proof. The chain's nodes are at strictly decreasing transitions of F (box 100 §1.3). Each such transition either changes W or is
    W-flat. [SUB] on F′ = F bounds the first kind. □
- Corollary (PROVED, lane): LEVEL-ONCE ∧ R*-POLY ∧ FL-POLY ⇒ WRUN-POLY. This is REDUNDANT. R95's WRUN-EQ already gives
  WRUN-POLY ⇔ R*-POLY ∧ FL-POLY without LEVEL-ONCE.
- Reading.
  - Depth is paid by W-changes, and [SUB] charges W-changes to R*_F. So the depth question IS the R* / FL core.
  - On topfix (R*-type chain events 0) [SUB] already bounds |F| ≤ (n − 1)(R*_F + 1) + FL_F directly, so LEVEL-ONCE is not needed there
    either.
  - The cascade route (boxes 98-102) is a reformulation of the open core, not a way around it. Its genuinely new content is:
    - PAY;
    - FRESH-ROOT, CHILD, TREE (proved);
    - the mechanism data (one clock, observer re-opens, rotating triples);
    - the CONJECTURES CASC-EDGE (tight) and LEVEL-ONCE.
- Option (a) (LEVEL-ONCE) was not attempted in this box. By the corollary above, LEVEL-ONCE alone does not close W-runs unless the depth is
  bounded independently of R*_F and FL_F. CASC-EDGE remains the only cascade statement that would close W-runs by itself.

## DONE / FINDINGS / NEEDS
- DONE: this note; retcause.py CHAIN / CHAINSTEP lines; corpus re-run; new/check.sh «box 103 DEPTH». SHA: see the commit.
- FINDINGS:
  - DEAD: depth ≤ f(distinct vertices on the chain): topfix_N, 6N − 11 nodes on 3 rotating vertices (box 96's stubborn triple).
  - DEAD: chain nodes always W-changing: u23sw64_n32.
  - PROVED (lane): DEPTH-SUB, D_e ≤ (n − 1)(R*_F + 1) + FL_F. Its corollary is redundant with R95 WRUN-EQ, so route (b) collapses into
    the R* / FL core.
  - CASC-EDGE remains the one cascade statement that closes W-runs alone.
- NEEDS: Lead: the next box. My recommendation is the proof side of CASC-EDGE restricted to deg X = 2 (one X alternating between two
  targets under one root ≤ 2 times), the case pftheta34 makes tight, or a return to the R* core.
