# CANDIDATE kill instances of CONJECTURE MOVES-2D (L-LOWER successor 3, BOX L3)
Label: CANDIDATE (Lead 00:33Z: until two independent replays agree). Doc: docs/lower/L3-families.md §9.
MOVES-2D (P-IDEAL-MOVES §0, claude/l-new): «on 𝓛^R_d every z ∈ Z moves at most 2d times in every run».
Each file: box150 JSON (N, lev, opts[x][k] = [W-target, Ξ-target, β index], gate, br (rank by β index), bp (parity, 0 = even),
start). Run from the stored start.

| file | sha1 | d | mover z (level) | moves(z) | 2d | T |
| --- | --- | --- | --- | --- | --- | --- |
| KILL_M2D_d6_mu13.json | 5301c716f68f219bda2806f29b317c94e0ed5df0 | 6 | 8 (4) | 13 | 12 | 13 |
| KILL_M2D_d8_mu21.json | d96c2b3657e79c410b180580d829366cbecc9ea4 | 8 | 15 (7) | 21 | 16 | 24 |
| REC_d7_mu17.json | 62917c189113bee004d02ada48803f235143a9eb | 7 | 8 (4) | 17 | 14 | 17 |
| REC_d8_mu24.json | 18d26cec2651290dfd9d137712bdadbb36d6f3d8 | 8 | 8 (4) | 24 | 16 | 25 |
| REC_d9_mu29.json | 2d034e7fcc3a9261e2fbdcaf5eae9dd5f38a2313 | 9 | 15 (7) | 29 | 18 | 31 |
| REC_d10_mu32.json | b114f4cdefaf1da6818e15512bc1fdb19c249e59 | 10 | 15 (7) | 32 | 20 | 33 |
| REC_d10_tower_mu30.json | cc94dc9c46ef63f7a3a54b536d9d3b38fdee5255 | 10 | 8 (4) | 30 | 20 | 35 |
| REC_d11_mu40.json | bbdb33d963d198c439aec63c8c75b0f080043510 | 11 | 15 (7) | 40 | 22 | 44 |
| REC_d12_mu42.json | 28e62d513b697ab3083da6310af631c14e1fc830 | 12 | 15 (7) | 42 | 24 | 48 |

## Membership checklist (one line per condition, with the check; output of every file: memcheck.out, 9 × ALL PASS)
Definitions checked against (quoted):
- R104 (docs/RESULTS.md l. 9864): «an IDEAL genome G has N movers x with levels lev(x), M := Σ deg(x) options (x, k), each with a
  W-target of level lev(x) − 1 (none at level 0), a Ξ-target xt(x, k), a mover or the exit X, a distinct β-rank with a parity, a
  distinct gate index, and a start»; «the Ξ-graph has an edge x → xt(x, k) for every option with a mover as Ξ-target».
- R110 (l. 11323): «𝓛^R_d ⊆ 𝓦_d the 2-wide degree-2 ladders in L-RED's R197 convention (movers 2l and 2l + 1 on level l, all of degree
  2, no other movers, option k of a mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k)»; «ISO the property that no option has
  Ξ-target 0 or 1» (a separate property: R110 speaks of «the ISO genomes of 𝓛^R_(m+1)»; MOVES-2D is stated on 𝓛^R_d, not on ISO).
- P-IDEAL-MOVES §0: «moves(x) := #{t ∈ [1, T] : x ∈ Mv_t}», «Z := {xt(x, k) : (x, k) an option, xt(x, k) ≠ X}», μ(d) over «z ∈ Z of
  level ≥ 1».
Checks (experiments/lower/l3/memcheck.py FILE MOVER):
- (i) IDEAL genome per R104: every option's W-target is a mover of level lev − 1, none at level 0; Ξ-target a mover index or −1 (X);
  a start of length N. memcheck line (i).
- (ii) 𝓛^R_d per R110: N = 2d, lev[x] = x // 2, every mover degree 2, opts[x][k][0] = 2(l − 1) + k for l ≥ 1. memcheck (ii); also
  movescheck.py's is_lr (xcheck.py asserts it).
- (iii) ISO: not required by 𝓛^R_d (see quote); all nine instances are NOT ISO (reported by memcheck (iii)).
- (iv) Ξ-acyclicity: DFS on the Ξ-graph (memcheck (iv)); box150/check.py TOPO 0.
- (v) ranks a permutation of 0..M − 1 (hence distinct), gates distinct, parities in {0, 1}, one β per option, levels lev[x] = x // 2
  (R110's numbering; R104 assigns levels as given in the genome). memcheck (v).
- (vi) start: one option index per mover (R104: «and a start»; no other condition). memcheck (vi).
- (vii) moves(z) counted per mover per run from the stored start, the binder of P-IDEAL-MOVES §0 (= movescheck.py's
  `sum(1 for t in range(1, T + 1) if z in Mv[t])`), z ∈ Z of level ≥ 1: memcheck (vii) by sim.py and by box150 Gen; l3check.py
  re-checks at every verify.
Simulators: own experiments/lower/l3/sim.py (from R104's definition only); L-NEW box150 Gen (trunk); box139 paths.py via box150
check.py XSIM (0 on all nine). movescheck.py check_run counters all 0 (xcheck.py with an l-new tree).
