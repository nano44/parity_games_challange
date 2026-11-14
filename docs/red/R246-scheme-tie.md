# R246: SCHEME-TIE — (T1) YES: the games Γ3^top(G_k) (Γ3(G_k) with the e-vertices re-prioritised above c_W, root-major) are TIE-FREE for S4a and the run of SPEC S1-S5 from S3 on them makes 2^k + 2 iterations whatever the S4a tie rule is (DATA: N5 and N5′-xi, k = 3..9, three / two engines, «S4a ties met» = 0; Theorem TOP, a lane proof written in ONE PASS, unrefereed and not yet re-read: at least L(G) + 1 iterations for every Ξ-acyclic genome G and every rule that returns an optimum of S4a's arena); tie census of N5 on Γ3(G_k): a tie at every iteration, all at movers
L-RED successor 71 (session_01V5yGRVyq25BY6qxdGPF1dD), D1 / D27 / D28 as the Lead's brief of 2026-11-14 13:44Z quotes them; written 2026-11-14 (stamps by date -u in §9).
Labels: DATA (counter, unit, scope, engines) / LANE PROOF, ONE PASS (written and checked once by me; to be re-read before anyone cites it as PROVED) / CONJECTURE / READING. Nothing here is a RESULTS entry. A kill is a claim too (D1): §8 lists what is NOT established. Lead's ruling 14:06Z: the family is carried as DATA today; «the proof re-read is a LATER item, not today».

## 0. Answer
- Question SCHEME-TIE (Lead): «is there a family of games on which SPEC S1-S5 (with FIX 1-4, from S3) makes super-polynomially many iterations WHATEVER the S4a tie rule is?»
- **(T1) YES.** Family Γ3^top(G_k), k ≥ 3 (§3): the graph of Γ3(G_k) (n = 135k − 230 vertices, m = 176k − 300 edges), with new priorities at the M e-vertices, c_W, K0 and K3 only. On it S4a's arena has exactly ONE pointwise optimum at every iteration of the run (no S4a tie is met, §1's unit), S4b never runs, and the run is the IDEAL key run of G_k: 2^k − 2 mover steps, then a fallback.
  - DATA (§4): N5 (mode spec) and N5′-xi (mode xi) make 2^k + 2 iterations at k = 3..9 on my engine; n5b (L-COMP, spec) the same at k = 3..9; L-NEW's engine (both modes) at k = 3..7. «S4a ties met» = 0 everywhere. Winners equal Oink's (zlk, tl).
  - LANE PROOF, ONE PASS: Theorem TOP (§3.3) for every Ξ-acyclic genome G; with L(G_k) = 2^k − 2 (packet P-N5-EXP, claude/l-red-b 350d84eb with line L-3 at 10dfedb6; signed by both referees and landing as RESULTS R131, per the Lead's brief; not re-proved here) it gives at least 2^k − 1 iterations on Γ3^top(G_k) for EVERY rule that returns a pointwise optimum of S4a's arena. The premise [RULE] of R104 / R117 (how SPEC's procedure breaks ties) is not used.
- **(T2)** is settled by (T1) for tie rules: one family defeats every tie rule at once, so the hybrids h1 (alternate the two tie rules), h2 (run both, stop with the first) and h3 (Ξσ-best, then root-first key) make the same 2^k + 2 iterations on Γ3^top(G_k) as N5 does. §6 names the hybrids that are NOT tie rules and are not covered.
- **Tie census of N5 on the frozen Γ3(G_k)** (§2): «S4a ties met» = 28, 81, 212, 519, 1226, 2829, 6416 at k = 3..9; a tie at EVERY iteration; every tie is at a mover and in the path case; S4b ties 0; fallback ties 0. The IDEAL model's own count agrees iteration by iteration.

## 1. The scheme, a tie, the unit
- SPEC S4a (trunk docs/new/N5-ssi-global.md l. 51-54, opened): «If Iσ ≠ ∅: A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v. Arena H: Even v keeps only edges to A(v); Odd v keeps only the edge to τ(v). σ_new = Odd's optimal counterstrategy (S1 procedure) in the dual of H to the dual-Even strategy τ, read as an Even strategy of G. (Even's one-player optimum against τ among "keep or take an improving edge".) Else σ_new = σ.»
- W* := the optimal value of H for Even (values (c, P, ℓ) and their order as in SPEC S1; ⊕ as in P-N5-REALIZE §1). A POINTWISE OPTIMUM of H is a positional Even strategy of H whose play value is W*(v) at every vertex v.
- CLASS SCHEME: SPEC S1-S5 with FIX 1-4, from S3, where S4a's σ_new is SOME pointwise optimum of H, chosen by any rule (it may read anything: ids, ranks, Ξσ, the history). N5 is in the class by premise [1E-N3] (RESULTS R57 (b), as used in R104 / R117); N5′-xi (RESULTS R118 [N5XI], box 190 §1: at an Even v that is not its own W*-cycle node, the Ξσ-best element of TIE(v) := {w ∈ A(v) : W*(v) = v ⊕ W*(w)}) differs from N5 only where |TIE(v)| ≥ 2.
- BEST(v), for an Even v with |A(v)| ≥ 2: {w ∈ A(v) : W*(v) = v ⊕ W*(w)} if v is not its own W*-cycle node (PATH case); {w ∈ A(v) : w reaches v in H through vertices of rank < rank(v)} if it is (CYCLE case: each such w closes a cycle whose node is v).
- **Unit «S4a ties met»** := the number of pairs (iteration, Even vertex v) with |A(v)| ≥ 2 and |BEST(v)| ≥ 2. If it is 0 over a run, H has one pointwise optimum at every iteration and every member of SCHEME makes that same run. The same count is taken for S4b (Odd's arena H′), and at a fallback (S4c: an Even vertex whose Ξσ-best improving option is not unique).
- Other counters (tool header, experiments/red/r246/tie246.py): choice := Σ_iterations #{Even v : |A(v)| ≥ 2}; refuse := pairs (iteration, v) with |A(v)| ≥ 2 and σ_new(v) = σ(v); refuse_strict := those with |BEST(v)| = 1; opt_bad := pairs where the engine's own choice is not in BEST(v) (must be 0).

## 2. Tie census of the N5 run on Γ3(G_k) (first deliverable; DATA)
Games: pg/G_k_r104.pg, built by my own builder g3_246.py (EMODE r104) from experiments/red/r244/gk/G_k_renum.json; byte-equal to L-RED-B's frozen data/b6b/pg/G_k_g3.pg at k = 3..10 (sha1 equal, out/build.out against `sha1sum` of the claude/l-red-b files at 10dfedb6).
### Table A: tie census of N5 (mode spec) on Gamma3(G_k), R104's priorities (file pg/G_k_r104.pg = L-RED-B's G_k_g3.pg)
| k | n | iterations | fallbacks | choice | S4a ties met | at movers | path / cycle | iterations with a tie | most ties in one iteration | refuse | refuse_strict | S4b steps / ties | fallback ties | engine v equal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 175 | 9 | 1 | 53 | 28 | 28 | 28 / 0 | 9 | 4 | 19 | 7 | 0 / 0 | 0 | yes |
| 4 | 310 | 17 | 1 | 128 | 81 | 81 | 81 / 0 | 17 | 6 | 57 | 15 | 0 / 0 | 0 | yes |
| 5 | 445 | 33 | 1 | 289 | 212 | 212 | 212 / 0 | 33 | 8 | 159 | 31 | 0 / 0 | 0 | yes |
| 6 | 580 | 65 | 1 | 642 | 519 | 519 | 519 / 0 | 65 | 10 | 409 | 63 | 0 / 0 | 0 | yes |
| 7 | 715 | 129 | 1 | 1427 | 1226 | 1226 | 1226 / 0 | 129 | 12 | 1003 | 127 | 0 / 0 | 0 | yes |
| 8 | 850 | 257 | 1 | 3172 | 2829 | 2829 | 2829 / 0 | 257 | 14 | 2381 | 255 | 0 / 0 | 0 | not run |
| 9 | 985 | 513 | 1 | 7029 | 6416 | 6416 | 6416 / 0 | 513 | 16 | 5519 | 511 | 0 / 0 | 0 | not run |
- Reading of the table: every tie is at a mover (tie = tie_mov) and in the path case, as Lemma W (iii) of P-N5-REALIZE / W3 (iii) of P-N5-REACH says (TIE(x) = R(x)); the other vertices with two kept options (K0 at every iteration, and the vertices that move after the fallback) have a strict optimum. refuse_strict = 2^k − 1 = L + 1 in every row: READING of the count (not separately instrumented): by Lemma K3 (d) of P-N5-REACH, K0 keeps pA against its improving edge (K0, K1) at each of the iterations 1..L + 1.
- Third count (the IDEAL model, no game): Σ over the IDEAL states s_0..s_L of #{movers x : |A_s(x)| ≥ 2} (trace246.py, r178 fastcyc values) = 23, 74, 201, 504, 1207, 2806 at k = 3..8 (Table E, model_avail2_sum); it equals the game's count over iterations 1..L + 1 (k = 3 per iteration: 3, 4, 4, 3, 3, 4, 2 in both; the remaining 5 of the 28 ties are met at iterations 8 and 9, after the fallback).
- Growth: ties per iteration grow linearly in k (at most 2k − 2 at one iteration, k = 3..9: 4, 6, 8, 10, 12, 14, 16); the total is Θ(k·2^k) in this range.

## 3. The tie-free variant
### 3.1 Definition of Γ^top(G) and Γ3^top(G) (G an R104 genome)
Γ(G) is R104's game (P-N5-REALIZE §3.1), Γ3(G) is R117's padded game (P-N5-REACH §3). Γ^top(G), Γ3^top(G) have the same vertices, owners, edges and indices, and the same priorities except:
- Ω(c_W) := eb, the least even number above every Ω(β) (R104's eb);
- Ω(e_g) := eb + 2 + 2·j, where j is the position of g in the order by (−lev(owner of g), −gate(g)): every e is EVEN and ABOVE c_W; a LOWER level outranks a higher one; inside one level a SMALLER gate index outranks a larger one («root-major»);
- top := the least even number ≥ 2 + (the largest priority so far); Ω(K0) := top + 2, Ω(K3) := top + 3 (R104's formulas; K0, K3 stay above every e).
Rank facts: pads, movers, gates, c_X < K2 < K1 < every β < c_W < every e < K0 < K3 (R117's list with c_W and the e-vertices exchanged). The largest priority is eb + 2M + 5 (it was eb + 2M + 3; measured on k = 3, 5: 99 against 97, 243 against 241), so the input size is the same. Builder: experiments/red/r246/g3_246.py (EMODE top), written from the two packets' texts.

### 3.2 Why the tie disappears (Lemma TOP-KEY; lane proof, one pass)
Fix a standard state of Γ3^top(G) for a mover state s (P-N5-REACH §3 «Transport»), H := S4a's arena there.
- (a) Every H-play from an option m_ℓ of a mover of level ℓ is m_ℓ → g_ℓ → pe_ℓ → e_ℓ → x_(ℓ−1) → m_(ℓ−1) → … → x_0 → m_0 → g_0 → pe_0 → e_0 → c_W (τ takes pe at every gate; P-N5-REACH KEY3 (b)'s play), with g_i ∈ gates of R(x_i) and x_(i−1) = wt(g_i). Its value is (c_W, {e_0, …, e_ℓ}, 5ℓ + 4): the cycle node is c_W, and the vertices above c_W on the play are exactly its e-vertices (rank facts), one per level 0..ℓ.
- (b) For two such plays from options of movers of ONE level, with gate sequences (g_0, …, g_ℓ) ≠ (g′_0, …, g′_ℓ): let t be the least level with g_t ≠ g′_t. The e-vertices of levels < t are common. The symmetric difference of the two P-sets contains e_(g_t) and e_(g′_t) and otherwise only e-vertices of levels > t, which rank below both (root-major). So its most relevant vertex is the one of e_(g_t), e_(g′_t) with the SMALLER gate index; it is even, so the play that contains it is strictly better for Even. Hence: P ≻ P′ ⟺ (gate(g_0), …, gate(g_ℓ)) <_lex (gate(g′_0), …, gate(g′_ℓ)), R104's key order; the lengths are equal and never decide.
- (c) By induction on the level ℓ: W*(x) for a mover x of level ℓ is x ⊕ m ⊕ (the value of the play of (a) with the lexicographically least key among all H-plays from x), and that play's first gate is the k ∈ A_s(x) with the least key key_(s′)(x, k), where s′ is the IDEAL successor choice on the levels below (R104's step). Proof: an H-play from x through option g continues from wt(g); ⊕ by e_g (a vertex in neither P-set) preserves the strict order, so the best play through g continues with the best play from wt(g), whose key is key_(s′) of wt(g)'s chosen option by induction; the key of the option is that key followed by gate(g), R104's definition.
- (d) UNIQUENESS: two options g ≠ g′ of one mover x give P-sets that differ in their level-ℓ element, so x ⊕ W*(g) ≠ x ⊕ W*(g′): BEST(x) is a singleton for every mover with |R(x)| ≥ 2; x is not a cycle node of H (the node is c_W). ∎
In R104's Γ(G) every e lies BELOW c_W, the P-sets of (a) are empty and all options are tied (Lemma W (iii)); SPEC's procedure then picks by BFS discovery order, which is the same key order ([RULE]). Γ^top turns the tie-break into a strict preference of the arena itself.

### 3.3 Theorem TOP (lane proof, one pass, unrefereed; premises [DEF] = R104's definitions, [SPEC], [VJ-LOC], [1E-N3] P1, as in P-N5-REACH; NOT [RULE])
Let G be a genome with an acyclic Ξ-graph, s_0 → … → s_L its IDEAL run (L = L(G)), and A any member of SCHEME (§1). Then the run of A on Γ3^top(G) from S3 has states 0, …, L equal to the standard states for s_0, …, s_L (P-N5-REACH §3), transition L + 1 is a fallback, and in each of the iterations 1, …, L + 1 S4a's arena has exactly one pointwise optimum and S4b does not run. So A makes at least L(G) + 1 iterations, and its first L(G) + 1 iterations do not depend on the tie rule of S4a, of S4b or of S4c.
Proof. The proof of Theorem REACH3 (P-N5-REACH §7), with these changes.
- S3-START (§4 there): S3 reads the priorities of the successors of vertices with two or more successors: the mover pads (2 / 0), xt(g) and pb_g at β_g (0 / 1), K1 and pA at K0 (5 / 0), q and s at K1 (1 / 0), K1 and K2 at K3 (5 / 3), pe_g and pβ_g at a gate (1 / 0), r and K2 at K2 (0 / 3). None of these is an e-vertex, c_W, K0 or K3, so the start is the standard state for s_0, as there.
- PAD (§5 there): unchanged (c_W's loop has Ω eb ≥ 8).
- K3 (§6.1): uses only K2 < K1 < K0 < K3 and the pads: unchanged.
- PLAY3 (§6.2): (a), (c) unchanged; (b) becomes φ(e_g) = (c_W, {e_g}, 1) for lev = 0 (e_g is now above c_W). Not used below except through the cycle node.
- SBAR3 (§6.3): (i) lev ≥ 1 uses «e_g is even and outranks every β»: true; lev = 0 uses the node c_W (even) against K1 (odd): true; K2: unchanged. (iii) uses «a cycle through a gate's e-face has an e-vertex as its most relevant vertex, an EVEN node» (every e is even and outranks movers, gates, pads, β) and the node / e_g ∈ P distinction: true.
- TAU3 (§6.4): uses «every play from pe_g under τ ends in c_W's loop» (reward p′(c_W)) and p′(K0) > p′(c_W): true. So Iτ = ∅ in every standard state.
- ESC3 (§6.5): REWARD comparisons only (even node c_W against the odd nodes of K): true. So every pointwise optimum of H agrees with σ at every Even non-mover, and Iσ ∋ (K0, K1).
- KEY3 (a) (§6.7): unchanged (Ξσ of an option is (K1, B_s(x, k) ∪ {K0, K3}, ·); no e, no c_W).
- W3 (§6.6) and KEY3 (b) are REPLACED by Lemma TOP-KEY: in a standard state for s, the unique pointwise optimum of H at the movers is σ^(s′), s′ the IDEAL step's choice from s (s′ = s when the IDEAL run stops at s).
- Induction (§7 there): state j is standard for s_j. For j < L: τ_new = τ (TAU3; S4b does not run); every pointwise optimum of H equals σ off the movers (ESC3) and σ^(s_(j+1)) on them (TOP-KEY), so A's σ_new, being a pointwise optimum, is the standard σ for s_(j+1) ≠ σ: no fallback. For j = L: the unique optimum is σ itself, τ_new = τ, Iσ ≠ ∅: S4c fires. ∎
- Remark. The transitions 1..L are NOT «FL transitions» in RESULTS R103's sense: W changes with the movers (its P-set is the key). Nothing here needs FL.
- What I re-read: P-N5-REALIZE §1-§4 and P-N5-REACH §3-§7 (trunk aeb90ac1), each comparison against the new rank facts, as listed. Their landed proofs are for R104's priorities; the list above is my check, not a referee's.

### 3.4 Corollary (with P-N5-EXP's Theorem EXP-IDEAL, not re-proved here)
For every k ≥ 3 and every member A of SCHEME, A makes at least 2^k − 1 iterations on Γ3^top(G_k), a parity game with n = 135k − 230 vertices and m = 176k − 300 edges. So no polynomial bounds the iterations of any member of SCHEME: the obstruction RIPPLE is a property of S4a's ARENA (Even's optimum against τ among «keep or take an improving edge»), not of its tie rule.

## 4. DATA on Γ3^top(G_k)
Files experiments/red/r246/pg/G_k_top.pg, k = 3..10 (sha1 in pg/SHA1SUMS_top and §9). Engines: s = my n5s237 (SPEC-exact, r237), v = L-NEW's box 190 n5v.step with si.Engine values (claude/l-new a143d406), n5b = L-COMP's trunk experiments/n5-second/n5b.py --mode spec.
### Table B (spec): the scheme on Gamma3^top(G_k), mode spec (file pg/G_k_top.pg)
| k | n | iterations | 2^k + 2 | fallbacks | choice | S4a ties met | path / cycle | refuse | refuse_strict | S4b steps / ties | fallback ties | opt_bad | engine v equal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 175 | 10 | 10 | 1 | 56 | 0 | 0 / 0 | 21 | 21 | 0 / 0 | 0 | 0 | yes |
| 4 | 310 | 18 | 18 | 1 | 134 | 0 | 0 / 0 | 60 | 60 | 0 / 0 | 0 | 0 | yes |
| 5 | 445 | 34 | 34 | 1 | 297 | 0 | 0 / 0 | 162 | 162 | 0 / 0 | 0 | 0 | yes |
| 6 | 580 | 66 | 66 | 1 | 652 | 0 | 0 / 0 | 412 | 412 | 0 / 0 | 0 | 0 | yes |
| 7 | 715 | 130 | 130 | 1 | 1439 | 0 | 0 / 0 | 1006 | 1006 | 0 / 0 | 0 | 0 | yes |
| 8 | 850 | 258 | 258 | 1 | 3186 | 0 | 0 / 0 | 2384 | 2384 | 0 / 0 | 0 | 0 | not run |
| 9 | 985 | 514 | 514 | 1 | 7045 | 0 | 0 / 0 | 5522 | 5522 | 0 / 0 | 0 | 0 | not run |
### Table B (xi): the scheme on Gamma3^top(G_k), mode xi (file pg/G_k_top.pg)
| k | n | iterations | 2^k + 2 | fallbacks | choice | S4a ties met | path / cycle | refuse | refuse_strict | S4b steps / ties | fallback ties | opt_bad | engine v equal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 175 | 10 | 10 | 1 | 56 | 0 | 0 / 0 | 21 | 21 | 0 / 0 | 0 | 0 | yes |
| 4 | 310 | 18 | 18 | 1 | 134 | 0 | 0 / 0 | 60 | 60 | 0 / 0 | 0 | 0 | yes |
| 5 | 445 | 34 | 34 | 1 | 297 | 0 | 0 / 0 | 162 | 162 | 0 / 0 | 0 | 0 | yes |
| 6 | 580 | 66 | 66 | 1 | 652 | 0 | 0 / 0 | 412 | 412 | 0 / 0 | 0 | 0 | yes |
| 7 | 715 | 130 | 130 | 1 | 1439 | 0 | 0 / 0 | 1006 | 1006 | 0 / 0 | 0 | 0 | yes |
| 8 | 850 | 258 | 258 | 1 | 3186 | 0 | 0 / 0 | 2384 | 2384 | 0 / 0 | 0 | 0 | not run |
| 9 | 985 | 514 | 514 | 1 | 7045 | 0 | 0 / 0 | 5522 | 5522 | 0 / 0 | 0 | 0 | not run |
- refuse = refuse_strict in every row: every refusal of an improving switch is forced by the arena's strict preference.
- Mover states (Table E): states 0..L of the run on Γ3^top(G_k) equal the IDEAL key run (ideal_mism 0, k = 3..8 in mode spec, 3..6 in mode xi); the first fallback is at iteration L + 1 = 2^k − 1 (fb_at); nonmover 0 (no non-mover Even vertex and no Odd vertex changes before it).
- After the fallback the run on Γ3^top makes 3 more iterations (Γ3: 2 more), hence 2^k + 2 (Γ3: 2^k + 1).
### Table C: third engine (L-COMP n5b --mode spec), iterations / fallbacks
- N5B G_3_top.pg mode spec n5b iterations 10 fallbacks 1 evals 43
- N5B G_4_top.pg mode spec n5b iterations 18 fallbacks 1 evals 75
- N5B G_5_top.pg mode spec n5b iterations 34 fallbacks 1 evals 139
- N5B G_6_top.pg mode spec n5b iterations 66 fallbacks 1 evals 267
- N5B G_7_top.pg mode spec n5b iterations 130 fallbacks 1 evals 523
- N5B G_8_top.pg mode spec n5b iterations 258 fallbacks 1 evals 1035
- N5B G_9_top.pg mode spec n5b iterations 514 fallbacks 1 evals 2059
- N5B G_3_r104.pg mode spec n5b iterations 9 fallbacks 1 evals 39
- N5B G_4_r104.pg mode spec n5b iterations 17 fallbacks 1 evals 71
- N5B G_5_r104.pg mode spec n5b iterations 33 fallbacks 1 evals 135
- N5B G_6_r104.pg mode spec n5b iterations 65 fallbacks 1 evals 263
### Table D: winners against Oink (zchk246)
- G_3_top.pg mode spec: its 10 wrong_zlk 0 wrong_tl 0
- G_3_top.pg mode xi: its 10 wrong_zlk 0 wrong_tl 0
- G_4_top.pg mode spec: its 18 wrong_zlk 0 wrong_tl 0
- G_4_top.pg mode xi: its 18 wrong_zlk 0 wrong_tl 0
- G_5_top.pg mode spec: its 34 wrong_zlk 0 wrong_tl 0
- G_5_top.pg mode xi: its 34 wrong_zlk 0 wrong_tl 0
- G_6_top.pg mode spec: its 66 wrong_zlk 0 wrong_tl 0
- G_6_top.pg mode xi: its 66 wrong_zlk 0 wrong_tl 0
- G_7_top.pg mode spec: its 130 wrong_zlk 0 wrong_tl 0
- G_7_top.pg mode xi: its 130 wrong_zlk 0 wrong_tl 0
- G_3_top.pg mode spec: its 10 wrong_zlk 1 wrong_tl 1
### Table E: mover states against the IDEAL key run (trace246)
- G_3_renum.json emode r104 mode spec: its 9 fb_at [7] F 6 nonmover 0 L 6 end stuck ideal_mism 0 model_avail2_sum 23
- G_3_renum.json emode top mode spec: its 10 fb_at [7] F 6 nonmover 0 L 6 end stuck ideal_mism 0 model_avail2_sum 23
- G_4_renum.json emode r104 mode spec: its 17 fb_at [15] F 14 nonmover 0 L 14 end stuck ideal_mism 0 model_avail2_sum 74
- G_4_renum.json emode top mode spec: its 18 fb_at [15] F 14 nonmover 0 L 14 end stuck ideal_mism 0 model_avail2_sum 74
- G_5_renum.json emode r104 mode spec: its 33 fb_at [31] F 30 nonmover 0 L 30 end stuck ideal_mism 0 model_avail2_sum 201
- G_5_renum.json emode top mode spec: its 34 fb_at [31] F 30 nonmover 0 L 30 end stuck ideal_mism 0 model_avail2_sum 201
- G_6_renum.json emode r104 mode spec: its 65 fb_at [63] F 62 nonmover 0 L 62 end stuck ideal_mism 0 model_avail2_sum 504
- G_6_renum.json emode top mode spec: its 66 fb_at [63] F 62 nonmover 0 L 62 end stuck ideal_mism 0 model_avail2_sum 504
- G_7_renum.json emode r104 mode spec: its 129 fb_at [127] F 126 nonmover 0 L 126 end stuck ideal_mism 0 model_avail2_sum 1207
- G_7_renum.json emode top mode spec: its 130 fb_at [127] F 126 nonmover 0 L 126 end stuck ideal_mism 0 model_avail2_sum 1207
- G_8_renum.json emode r104 mode spec: its 257 fb_at [255] F 254 nonmover 0 L 254 end stuck ideal_mism 0 model_avail2_sum 2806
- G_8_renum.json emode top mode spec: its 258 fb_at [255] F 254 nonmover 0 L 254 end stuck ideal_mism 0 model_avail2_sum 2806
- G_3_renum.json emode top mode xi: its 10 fb_at [7] F 6 nonmover 0 L 6 end stuck ideal_mism 0 model_avail2_sum 23
- G_4_renum.json emode top mode xi: its 18 fb_at [15] F 14 nonmover 0 L 14 end stuck ideal_mism 0 model_avail2_sum 74
- G_5_renum.json emode top mode xi: its 34 fb_at [31] F 30 nonmover 0 L 30 end stuck ideal_mism 0 model_avail2_sum 201
- G_6_renum.json emode top mode xi: its 66 fb_at [63] F 62 nonmover 0 L 62 end stuck ideal_mism 0 model_avail2_sum 504
### Table F: Lemma TOP on other genomes (rand246)
- RAND246 seed 1 nmax 6 dmax 3 degmax 3 lmin 1 ctrl 0 genomes 300 tried 494 sumL 309 maxL 2 mism 0 earlyfb 0 tie_pre 0 tie_post 0 xidiff 0 r104tie 947 r104mism 0 its_top 1289 its_r104 1209
- RAND246 seed 2 nmax 8 dmax 4 degmax 3 lmin 1 ctrl 0 genomes 300 tried 463 sumL 316 maxL 2 mism 0 earlyfb 0 tie_pre 0 tie_post 0 xidiff 0 r104tie 1109 r104mism 0 its_top 1304 its_r104 1216
- RAND246 seed 3 nmax 10 dmax 4 degmax 2 lmin 2 ctrl 0 genomes 200 tried 8678 sumL 404 maxL 3 mism 0 earlyfb 0 tie_pre 0 tie_post 0 xidiff 0 r104tie 1065 r104mism 0 its_top 1049 its_r104 1004
- RAND246 seed files nmax 0 dmax 0 degmax 0 lmin 0 ctrl 0 genomes 6 tried 6 sumL 262 maxL 136 mism 0 earlyfb 0 tie_pre 0 tie_post 0 xidiff 0 r104tie 2678 r104mism 0 its_top 288 its_r104 280
- RAND246 seed perm7 nmax 0 dmax 0 degmax 0 lmin 4 ctrl 0 genomes 100 tried 353 sumL 1080 maxL 14 mism 0 earlyfb 0 tie_pre 0 tie_post 0 xidiff 0 r104tie 6106 r104mism 0 its_top 1522 its_r104 1380
- RAND246 seed perm8 nmax 0 dmax 0 degmax 0 lmin 6 ctrl 0 genomes 60 tried 196 sumL 1378 maxL 30 mism 0 earlyfb 0 tie_pre 0 tie_post 0 xidiff 0 r104tie 9545 r104mism 0 its_top 1637 its_r104 1558
- RAND246 seed 1 nmax 6 dmax 3 degmax 3 lmin 1 ctrl 1 genomes 300 tried 494 sumL 309 maxL 2 mism 214 earlyfb 128 tie_pre 0 tie_post 0 xidiff 0 r104tie 947 r104mism 0 its_top 1176 its_r104 1209
- RAND246 seed perm7 nmax 0 dmax 0 degmax 0 lmin 4 ctrl 1 genomes 100 tried 353 sumL 1080 maxL 14 mism 100 earlyfb 100 tie_pre 0 tie_post 0 xidiff 0 r104tie 6106 r104mism 0 its_top 818 its_r104 1380
- TOTAL ctrl0: genomes 966 sumL 3749 mism 0 earlyfb 0 tie_pre 0 tie_post 0 xidiff 0 r104tie 21450 r104mism 0
- TOTAL ctrl1: genomes 400 sumL 1389 mism 314 earlyfb 228 tie_pre 0 tie_post 0 xidiff 0 r104tie 7053 r104mism 0
### Table G: control of the tie counter (TIE246_CTRL=1: P-sets ignored)
- G_3_top.pg ctrl 1: tie 31 (path 31), refuse 21, refuse_strict 7
- G_4_top.pg ctrl 1: tie 87 (path 87), refuse 60, refuse_strict 15
- G_5_top.pg ctrl 1: tie 220 (path 220), refuse 162, refuse_strict 31

## 5. Controls and the generality check
- Positive control of the tie counter: the frozen Γ3(G_k) games (ties at every iteration, equal to the model's count, §2).
- Negative control of the tie-free claim: TIE246_CTRL=1 compares options with the P-sets ignored (same cycle node and length = tied): on pg/G_k_top.pg the ties come back (Table G), so it is the P-sets, and only they, that separate the options.
- Lemma TOP on other genomes (rand246.py; Table F): random acyclic genomes (levels ≤ 4, degree ≤ 3, random gates, β-ranks, parities and starts), the frozen H5PLUS_L5 (L 136), LAD_d5_k3_s13, G_3..G_6, and random variants of G_4 and G_5 (gates and β-ranks re-drawn). Counters that must be 0 (mism, earlyfb, tie_pre, xidiff) are 0; r104tie > 0 and r104mism = 0 on the same genomes with R104's priorities; the control RAND246_CTRL=1 (wrong order inside a level) fires mism and earlyfb.
- Winners: zchk246.py against Oink --zlk and --tl with Oink's own verification; the control (one flipped vertex) fires both.

## 6. What this says to the designers (READING, not a result)
- A candidate «inside the scheme» that only changes WHICH optimum of S4a's arena is taken (any tie rule, any hybrid of tie rules, any order of applying the optimum's switches that still ends at a pointwise optimum each iteration) is dead on Γ3^top(G_k). To survive, a rule must take an improving switch that S4a's arena strictly refuses (on Γ3^top(G_9): 5,522 such refusals in 514 iterations), or change the arena (which edges are kept; what Odd plays in it).
- Two arenas are now closed by named families: Even's optimum against τ (S4a: Γ3(G_k) for the root-first key, Γ3^top(G_k) for every tie rule), and Even's optimum against σ̄ with all improving edges kept = switch-best / Howard (Friedmann's family [F11], RESULTS R130's external premise; on the wrapper W(H, s0) N5′-xi is that rule).
- NOT covered (they are not tie rules): (i) alternating whole STEPS of the two arenas (an S4a step, then a Howard step); (ii) dovetailing two complete algorithms; (iii) per-vertex or per-component mixtures. For (ii) a disjoint union Γ3^top(G_k) ⊎ F (F a Howard-exponential game) is exponential for both, if each algorithm runs on the whole game: S4a's optimum, Ξσ and the fallback test are computed component by component, and the fallback fires only when nothing changes anywhere, so the Γ3^top component is at state j after iteration j ≤ L whatever the other component does (CONJECTURE until run; one line of proof per step, no DATA yet). For (i) and (iii) an entangled composition is needed (G_k^top inside the wrapper): open; it is the next target unless a design lane names a candidate first.
- Howard / switch-best on Γ3^top(G_k): the model needs at most 4 steps (P-N5-EXP «Not claimed» paragraph); so the two kill families are disjoint in what they kill.

## 7. Reproduction
Envs: LNEW = a tree of `git archive a143d406 experiments/new experiments/si/si.py experiments/harness experiments/hard-families experiments/n5-second` (claude/l-new); TRUNK = a tree of `git archive origin/claude/vibrant-johnson-nxvvxo experiments/n5-second experiments/harness experiments/hard-families/pgsolver_si.py`; OINK = tools/oink/build/oink (8fbf0a7).
`cd experiments/red/r246; for j in build census_s census_v n5b zchk trace rand ctrl k10; do ./run246.sh $j; done; python3 summ246.py` (outputs out/<job>.out; the tables above are summ246.py's output).
Tools (own, this session): g3_246.py (builder), tie246.py (census; engines s / v), zchk246.py (winners), trace246.py (states against the IDEAL run; model tie count), rand246.py (Lemma TOP on other genomes), run246.sh, summ246.py.

## 8. NOT established / limits
- Theorem TOP is a lane proof by transfer, written in one pass: I checked each comparison of P-N5-REACH §4-§7 against the new rank facts once; I have not re-read it and no referee has. Its premises are those of R117 minus [RULE]. Until then the kill stands on the DATA of §4 (k = 3..9).
- The corollary's 2^k − 1 rests on L(G_k) = 2^k − 2 for all k (P-N5-EXP; DATA here to k = 10 on the game for N5, to k = 12 on the model in R245).
- «Exactly 2^k + 2 iterations» is DATA (k = 3..9; n5b and engine s also k = 10 when out/k10.out is present), not proved; the proof gives ≥ 2^k − 1.
- The class SCHEME fixes S4a to return a pointwise optimum of H. Rules that leave the optimum, or change S4b / S4c / the start so that the run leaves the standard states before iteration L + 1, are outside the theorem (S4b cannot matter before L + 1: it does not run).
- N5′-xi was run as box 190 defines it (engines s and v); other tie rules were not run: for them the claim rests on «S4a ties met = 0» (two engines) and on TOP-KEY (d).
- Only one start (S3) was examined.

## 9. Files, sha1, stamps
- Games (experiments/red/r246/pg/, sha1 = pg/SHA1SUMS_top):
  - 1c33a3c1915092717add91bfb347ccdecac66e79  G_10_top.pg
  - e0f3739c92979afaaf01b86b79b3977adff5941c  G_3_top.pg
  - 0d83273693d7888bde427050f1ede7bf73a02f89  G_4_top.pg
  - 07dfb3fedde7e352828461bbe22378ac5f50c84e  G_5_top.pg
  - 8ec7ea0535f350b9aec89850cc6da11a450443bd  G_6_top.pg
  - b1024a6cb69569481c43de7b4aa51bae617dfcae  G_7_top.pg
  - 9e6ff413f0461fabd5625ba5da2f7e29faa8b20e  G_8_top.pg
  - a1fb66201a7e1d40e2ca5326bd3f85da56b269eb  G_9_top.pg
- pg/SHA1SUMS_r104: the sha1 of my r104 rebuilds (files not committed; byte-equal to claude/l-red-b 10dfedb6 experiments/red-b/data/b6b/pg/G_k_g3.pg, k = 3..10).
- Tools (experiments/red/r246/):
  - 16ace6f093a7813f29af4b70a20c76afb7e0d88d  g3_246.py
  - 257fd2df3e78abf9e1b8eb5e4e9c57c4532338ca  tie246.py
  - 9689acd4174aac280df089502a13caf4d06971eb  zchk246.py
  - 302a480b83d69683351869594d02261f84b259ad  trace246.py
  - bb73c3afffcf20b8232a8d73e7d998090615baf4  rand246.py
  - 63e959bc7f51d04aec8446f0ca328e915500baa3  run246.sh
  - f4a52c34d7dbfe83d7c8423c7264d519d5adbb90  summ246.py
- Job ends (date -u inside run246.sh):
  - build.out: JOB END build 2026-11-14T14:04:24Z
  - census_s.out: JOB END census_s 2026-11-14T14:12:37Z
  - census_v.out: JOB END census_v 2026-11-14T14:07:41Z
  - ctrl.out: JOB END ctrl 2026-11-14T14:04:40Z
  - k10.out: (running or unfinished at the commit; not committed)
  - n5b.out: JOB END n5b 2026-11-14T14:06:55Z
  - rand.out: JOB END rand 2026-11-14T14:12:35Z
  - trace.out: JOB END trace 2026-11-14T14:05:42Z
  - zchk.out: JOB END zchk 2026-11-14T14:07:17Z
