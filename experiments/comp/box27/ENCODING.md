# Audit sheet: cnf.py against RESULTS R104's IDEAL model, and the exact scope of «T^R(3) = 8» (L-COMP box 27 (a))
For a referee. cnf.py sha1 fd882af16648b82c014754cadcdaf9b85ae8296d (l-comp 557b045b, the version every d 3 cube ran). Later
version 06f25e35 adds ONLY the env option XCUBE (unit clauses fixing Xi-targets, for the adaptive cube driver acube.py); the
encoding itself is unchanged (diff: one block before `info = dict`, and the build line).
Labels: EXACT-SAT = CaDiCaL 1.9.5 (pysat 1.9.dev15, solver name cadical195); no DRAT/LRAT certificate was produced or checked.

## 1. Claim and scope
- Class 𝓛^R_3: IDEAL-ACYC genomes (R104 definition) with levels 0, 1, 2, two movers per level u_l = 2l, v_l = 2l + 1, both of
  degree 2, no other movers; option k of a level-l >= 1 mover has W-target mover 2(l - 1) + k (R197 wiring); level 0 has no
  W-target. FREE: every Ξ-target (exit X or any other mover; the Ξ-graph acyclic), every rank (strict total order on the 12 β's),
  every parity, every gate (distinct), every start s_0. ISO is NOT imposed (Ξ-targets at level-0 movers allowed).
- Result: «some genome of 𝓛^R_3 and some start give T >= 9» is UNSAT (16 cubes, all UNSAT, 4,946 s CPU in total); «T >= 8» is SAT
  (out/R_d3_L8.json, replayed under sim.py and L-RED r187/ideal.py: T 8, same states). Hence T^R(3) = 8 over ALL genomes and starts.
- Symmetry break used (SYM=1): s_0(u_0) = s_0(v_0) = 0. Soundness: swapping the two option LABELS of a level-0 mover x (carrying
  along each option's Ξ-target, β (rank, parity) and gate, and flipping bit x in every state) maps a genome of 𝓛^R_3 to a genome of
  𝓛^R_3 and its run to the same run state for state with bit x flipped: level-0 options have no W-target; every other option refers
  to x only as a MOVER (W-target, Ξ-target), never to one of its options; chains through x use s(x)'s option, keys of x read
  gate(x, s(x)); distinctness of ranks and gates is preserved. Applied to u_0 and/or v_0, any start maps to one with
  s_0(u_0) = s_0(v_0) = 0 and the same T. No other symmetry break, no lane lemma, no ENC (RESULTS R105) is used.
- Cubes: CUBE fixes s_0(x) for x = 2..5 (u_1, v_1, u_2, v_2); the 16 cubes are all 2^4 assignments, so cubes x SYM cover every
  start up to the relabelling above. Logs: log/R_d3_L9/<id>.log (the build line names the cube), RESULT lines log/R_d3_L9_cubes.txt.

## 2. Variables
| cnf.py | meaning |
| --- | --- |
| S[t][x] | option of mover x at state s_t is 1 (t = 0..L) |
| Xv[(x,k)][y], Xv[(x,k)][-1] | Ξ-target of option (x,k) is mover y / the exit; exactly one (at-least-one + pairwise at-most-one) |
| pi[(x,y)] | strict total order on movers (antisymmetric by construction, transitivity clauses) |
| rk[(o,o2)] | rank(o) < rank(o2): strict total order on all options (each option has its own β) |
| par[o] | parity of β(o) is odd |
| gord[l][(o,o2)] | gate(o) < gate(o2), strict total order on the options of level l |
| Wv | W-targets: constants under W=R (R197 wiring) |

## 3. Constraint -> R104 clause
- R104 «a distinct β-rank with a parity»: rk strict total order; par free.
- R104 «a distinct gate index»: per-level strict total orders. Only same-level gates are ever compared (§4 key rule: position j of
  every key holds a level-j gate, and keys of one level have equal length), so cross-level gate order cannot matter.
- R104 «the Ξ-graph has an edge x -> xt(x,k) for every option with a mover as Ξ-target», ACYCLIC: Xv[(x,k)][y] -> pi(x < y), pi a
  strict total order (transitive). This is exactly acyclicity of the mover graph over ALL options (not only current ones).
- R104 «the Ξ-value of option (x,k) is the set of β's on its chain (x,k), (xt, s(xt)), … up to the first Ξ-target X»: chains(t)
  unrolls the chain hop by hop: cm_0(x,k) = {(x,k)}; cm_(h+1)(x,k) = {(x,k)} ∪ ⋃_y [Xv(x,k) = y] · mem_h(y), mem_h(y) =
  cm_h(y, s_t(y)); N hops (N = number of movers) reach the end of every chain because acyclic chains visit <= N movers.
- R104 comparison «by the β of largest rank in the symmetric difference: the option whose set contains that β is the better one
  if its parity is even and the worse one if odd»: better1(t, x) = ∨_o [o ∈ Δ ∧ (∀ o2 ∈ Δ, o2 ≠ o: rank(o2) < rank(o)) ∧
  (o ∈ chain(x,1) XOR odd(o))], Δ = chain(x,0) XOR chain(x,1) elementwise; better1 = «option 1 strictly better than option 0».
  Δ is never empty ((x,0) is only in chain(x,0), (x,1) only in chain(x,1): x is on no chain of its own targets, acyclicity), so
  ties do not occur and «option 0 strictly better» = NOT better1.
- R104 «A: current option and the options with a strictly better Ξ-value» (degree 2): B_t(x) = better1 XOR S[t][x] = «the other
  option is strictly better at s_t» (A-sets read at the OLD state s_t).
- R104 «an IDEAL step moves every mover to the lexicographically least key (gate indices of the chain of W-targets under the new
  state, lowest level first) among» A: S[t+1][x] = ITE(B_t(x), KP_(t+1)(x), S[t][x]), KP_(t+1)(x) = [key(x,1) < key(x,0)] under
  s_(t+1). Keys: key(y) = key(W(y, s(y))) + (gate(y, s(y)),) at level >= 1, (gate(y, s(y)),) at level 0; for two movers y, y' of
  one level, lex order of equal-length tuples gives: different W-targets w ≠ w' -> key(y) < key(y') iff key(w) < key(w') (the
  prefixes differ because distinct movers end in distinct gates); same W-target -> compare gate(y, s(y)) and gate(y', s(y')).
  keys_lt(t+1) builds these lt literals level by level from s_(t+1); kp1 applies the same rule to x's two options. Under the
  R197 wiring the two options of x always have different W-targets, so KP reads lt of the level below.
- R104 «the run stops when nothing is available or nothing changes, L(G) := its number of steps»: T >= L is encoded as
  «s_(t+1) is the step of s_t AND s_(t+1) ≠ s_t» for t = 0..L-1 (if all A-sets are singletons the rule gives s_(t+1) = s_t, so
  both stop reasons are excluded on the first L steps; conversely any run with T >= L satisfies the clauses).

## 4. Semantic checks of the encoding (independent of the max search)
- pinck.py: pin a whole genome and its start by unit clauses; the CNF must be SAT at L = T and UNSAT at L = T + 1 with T from
  sim.py (literal R104 simulator; = L-RED ideal.py on 198,085 runs, xcheck.out): 0 disagreements on 300 random d 2 and 150 random
  d 3 genomes (T 0-2) and on all 64 starts of each of the two length-8 genomes ext/dbl_d3_F6.json (L-RED R197) and
  ext/own_R_d3_L8.json (mine): 128 runs, T 0..8 (histogram 4, 26, 33, 15, 18, 16, 10, 4, 2).
- d 2 cross-method: the same encoder gives T >= 5 UNSAT at d 2, and bf2.c (exhaustive C enumeration, no SAT) finds max T = 4.
