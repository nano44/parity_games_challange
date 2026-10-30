# N5-GATE (box 51b): the gate lemma for W-flat Ξ-climbs (PROVED, lane, in corrected form), and why no gate or level potential can bound ZFL: on u23sw64_n32 every gate datum is constant across 8 flat transitions. A W-constant interval is a strategy-improvement run on the W-tight subgame (Theorem INTERVAL-SI)
L-SI successor 33 (Opus 5.5), D18. Lead 2026-10-30 13:34Z, BOX 51: «(1) PROVE (or kill with an instance): by R92 GP+'s prefix argument, a
strict W-flat Ξ-climb inside a fixed Z needs a change of first gate, or a non-same-pair gate. (2) Then look for a monotone order on gates
within one W-run (gate potential) that bounds ZFL_F polynomially. … (3) Measure on box 50b's corpus AND on the quadratic families l-red
rstar/instances/latew_K16_m32 and fx_K8_m32». Numbered 51b because box 51 is N5-LATEP. Working note, unrefereed, not a TARGET.md claim.
G-N5-TIME stays OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Setting and symbols as in docs/si/N5-FL-box50b.md and RESULTS R92: a W-run F (τ and λ_W constant, no S4c fallback); W_k, Ξ_k, σ̄_k, Z_k,
  D_k := {Odd o : σ̄_k(o) ≠ τ(o)}; ⊴ / ▷ the SPEC S1 order; ⊕ the prefix operation (R93 Lemma TIE; si.Engine.extend). A W-constant
  interval I of F is a maximal run of consecutive states of F with equal W; its transitions are exactly the W-flat transitions in it.
- R92 verbatim (docs/RESULTS.md l. 6656): «D_s := {Odd o : σ̄_s(o) ≠ τ(o)}» and «GATE_F the pairs (o, s) with o Odd in D_s ∪ D_{s+1}
  and s in TXC_F(o)». R92 defines no "first gate". The first gate below is an L-SI reading built on R92's D_s (Lead 13:57Z: «proceed on your
  reading, labelled "L-SI reading"»).
  - L-RED R139 (l-red 9326f166, via the Lead) and L-LIT T53 (l-lit 60bb9a56, via the Lead; not opened by me): Friedmann's exponential runs
    lie inside one fixed-cycle-node phase, so a ZFL bound must use N5's structure (τ fixed, S4a's arena optimum, W frozen), not
    Ξ-monotonicity alone. This agrees with §3: the W-frozen intervals here have fixed cycle nodes, and only S1's tie-break is left.
- Gate (L-SI reading): g_k(u) := the first vertex of D_k on the (σ_k, τ)-play from u (u itself if u ∈ D_k;
  undefined if the play avoids D_k); pre_k(u) := the vertices of that play before g_k(u). Same-pair at k: λ_Ξ_k(g) = λ_W(g).
- Tools (mine): experiments/si/gate/gate.py (classes, potential, interval checks, TXC counts), const.py (constancy of gate data per
  interval), agg.py, run.sh; L-RED instances copied read-only to gate/inst/ (sha1 equal to l-red 5374e0a5's pins). Outputs gate_sbcg.txt
  (719), gate_alt.txt (413), gate_red.txt (2), const_flat.txt. Pins: si/check.sh «box 51b».

## 1. Theorem INTERVAL-SI (PROVED, lane): a W-constant interval is strategy improvement on the W-tight subgame
- Definition. For a valuation W = val(ρ, τ) (some Even strategy ρ, [S1-val] in G_τ) and a vertex v (either player):
  OPT_W(v) := {e ∈ succ(v) : v ⊕ W(e) = W(v)} if v is not its own W-cycle node, and {e : W(e) has cycle node v and empty path set}
  otherwise. G_W := the game in which Even's edges are restricted to OPT_W (Odd keeps all its edges).
- Lemma TIGHT-VALUE. Every Even strategy σ with σ(v) ∈ OPT_W(v) for all Even v has val(σ, τ) = W.
  - Proof. τ(o) ∈ OPT_W(o) for Odd o, because W is the valuation of the (ρ, τ)-plays ((V1); for an own cycle node o, τ(o) lies on o's
    cycle and o is its most relevant vertex). Follow the (σ, τ)-play from x. At a vertex y that is not its own W-cycle node, the step
    keeps λ_W and lowers the length of W by 1. A vertex with W-length 0 is its own W-cycle node. So within n steps the play reaches a
    vertex c with λ_W(c) = c. From c it follows non-cycle-node steps (λ_W stays c) until the next own cycle node c′; then λ_W(c′) = c′
    and λ_W(c′) = c, so c′ = c. The play therefore closes a cycle Γ through c.
  - Backward induction along Γ with ⊕ gives that the path set of W(σ(c)) consists of the vertices of Γ ∖ {c} more relevant than c. That
    set is empty, so c is the most relevant vertex of Γ: val(σ, τ)(c) = (c, ∅, 0) = W(c).
  - The path from x to c is simple (lengths strictly fall), and backward induction with ⊕ gives val(σ, τ)(x) = W(x). □
- Theorem INTERVAL-SI. Let I = [p, q] be a W-constant interval of a W-run F, W := W_p = … = W_q, G_I := G_W. Then:
  - (i) σ_k is a strategy of G_I for every k ∈ I, by (V1) for W = val(σ_k, τ).
  - (ii) Ξ_k is also the [S1] valuation of σ_k in G_I: Odd's edges are the same, and σ_k is fixed.
  - (iii) every transition k → k + 1 of I switches a non-empty set of Even edges, each in Iσ_k ∩ G_I, i.e. improving for σ_k in G_I.
    Every transition of a W-run moves σ (box 50b §1). A switched v takes σ_{k+1}(v) ∈ S4a's arena {σ_k(v)} ∪ Iσ_k(v) (RESULTS R91's
    premise), different from σ_k(v), and in OPT_W(v) by (i) at k + 1.
  - (iv) every Even strategy of G_I has τ-valuation W (TIGHT-VALUE). So inside I, the S4a choice among the edges of G_I is a pure
    tie-break of SPEC S1's procedure.
  - So the transitions of I form a run of Vöge–Jurdziński strategy improvement for Even on the fixed game G_I, valuation Ξ, with some
    non-empty improving set switched at each step. □
- Corollary FL-INT (PROVED, lane). FL_F = Σ_I |I| over the W-constant intervals I of F. Their number is WCH_F + 1 ≤ (n − 1)(R*_F + 1) + 1
  (R92 FW-R*). So FL_F ≤ ((n − 1)(R*_F + 1) + 1)·max_I |I|, and FL-POLY ⇐ R*-POLY ∧ [P-INT], where [P-INT] := «every W-constant interval
  of every run has ≤ p(n) transitions». [P-INT] is about N5's tie-break only.
- READING (cross-field, D18). W-flat transitions are degenerate pivots:
  - The primal value W of the one-player game G_τ is frozen, while the dual-side valuation Ξ moves inside the optimal face G_I.
  - Network simplex knows such runs as "stalling", and anti-stalling pivot rules exist (W. H. Cunningham's work on strongly feasible
    bases; source NOT opened, so nothing is imported; ask L-LIT to open it).
  - The analogue here is R93's variant N5-LZC, which keeps σ_t(v) on W-ties. By R93 Theorem LZ-STRICT every switched vertex there
    strictly raises W, so N5-LZC has FL_F = 0 on every W-run. FL is a tie-break artefact of plain N5, and [P-INT] is exactly a
    stalling bound for SPEC S1's tie-break.

## 2. Lemma GATE (PROVED, lane): the Lead's box 51 (1), in corrected form
- Statement. Let t → t + 1 be a W-flat transition of a W-run F, and u a vertex with Ξ_{t+1}(u) ▷ Ξ_t(u) and u ∈ Z_{t+1}. Then u ∈ Z_t, and
  at least one of the following holds:
  - (a) g_t(u) ≠ g_{t+1}(u) (a change of first gate);
  - (b) g := g_t(u) = g_{t+1}(u) is not same-pair at t or at t + 1;
  - (c) g is same-pair at t and t + 1, and Ξ_{t+1}(g) ▷ Ξ_t(g) with W(g) fixed. This is a GATE_F event (g, t) of R92, g ∈ D_t ∩ D_{t+1}:
    the climb is transferred to the gate itself.
- Proof.
  - Ξ_t(u) ◁ Ξ_{t+1}(u) ⊴ W_{t+1}(u) = W_t(u) (XW, flat), so u ∈ Z_t. If u's (σ_k, τ)-play avoids D_k, it is also its (σ_k, σ̄_k)-play
    (σ̄_k = τ off D_k), so Ξ_k(u) = W_k(u). Hence u has a gate at t and at t + 1. Assume not (a) and not (b).
  - Let c := λ_W(g) (constant on F) = λ_Ξ_t(g) = λ_Ξ_{t+1}(g). Off D_k the two plays from u agree, so both run through pre_k(u) to g, and
    λ_W(u) = λ_Ξ_k(u) = c.
  - If c ∈ pre_k(u) (k = t or t + 1), both valuations of u read the same path u → c: Ξ_k(u) = W_k(u), contradicting u ∈ Z_k. So
    c ∉ pre_k(u).
  - Then the W-path from g to c avoids pre_k(u). Otherwise the play would return from some y ∈ pre_k(u) through g to y on a cycle that
    misses c, contrary to λ_W(g) = c. Likewise for the Ξ-path. So, with A_k := {y ∈ pre_k(u) : y more relevant than c} and
    ℓ_k := |pre_k(u)|, as disjoint unions:
    - W_k(u) = (c, A_k ⊔ Q, ℓ_k + ℓ), where W(g) = (c, Q, ℓ) is the same at t and t + 1 (flat);
    - Ξ_k(u) = (c, A_k ⊔ Q′_k, ℓ_k + ℓ′_k), where Ξ_k(g) = (c, Q′_k, ℓ′_k).
  - W_t(u) = W_{t+1}(u) gives A_t ⊔ Q = A_{t+1} ⊔ Q and ℓ_t = ℓ_{t+1}, so A_t = A_{t+1}.
  - Values with one cycle node compare by the signed weight of the path set, which is additive over disjoint unions, and then by the
    length. So Ξ_{t+1}(u) ▷ Ξ_t(u) ⟺ Ξ_{t+1}(g) ▷ Ξ_t(g). That is (c). □
- What changes against the box 50b §6 READING. The pure form «needs (a) or (b)» is not what the prefix argument proves. Case (c) remains:
  a same-gate, same-pair climb is possible exactly when the gate climbs. The u ∈ Z_{t+1} hypothesis is needed: if c ∈ pre_{t+1}(u), u
  leaves Z, which is FL ∖ ZFL, paid by FL-GAP.
- DATA (gate.py, all 1,132 runs; flat climbs = vertices whose Ξ strictly rises at a W-flat transition, any owner):

| class at W-flat transitions | all climbs | switched Even climbs |
| --- | --- | --- |
| (b) NSP: same gate, not same-pair | 498 | 348 |
| … of which W's cycle node lies in pre(u) (NSPW: W ignores the gate) | 176 | |
| (a) GCH: gate change | 26 | 5 |
| GSELF: u ∈ D_t ∩ D_{t+1} (u is its own gate; (c) with g = u) | 2 | 0 |
| (c) with g ≠ u (SPD) | 0 | 0 |
| same gate, same-pair, decomposition fails (NDEC; excluded by the proof) | 0 | 0 |
| no gate (NOG; excluded) / climb outside Z_t (ZZ_V; excluded by XW) | 0 / 0 | |
| TRV_V: case SPD without a gate climb (would refute the lemma) | 0 | |

  - So in all data the pure form holds for every switched Even vertex (348 + 5 = 353 climbs). The 4 other flat switches of box 50b are
    Ξ-flat (tog6a).
  - 498 / 526 climbs are NSP: the gap sits at the cycle-node level, λ_Ξ(u) ≠ λ_W(u), so LEV(u) = 0.

## 3. Box 51 (2): gate and level potentials are DEAD (instance u23sw64_n32)
- Lemma LEV-FLAT (PROVED, lane). Inside a W-constant interval, for u in Z at both states, Φ(u) := (LEV(u), Ξ's coordinate at LEV) does not
  fall, lexicographically.
  - LEV and the coordinate sequence are those of R93 Lemma LEVEL-MON: reward of the cycle node, the signed rank bits, then length.
  - Proof: Ξ_k ⊴ Ξ_{k+1} (R15 (a), (d)) ⊴ W (XW), with W fixed and the order lexicographic. Ξ_{k+1} agrees with W wherever Ξ_k does,
    before LEV_k; if LEV is kept, its coordinate does not fall. □
  - A membership coordinate takes two values. At such a LEV, Φ can only rise by LEV rising, so Φ rises at most O(n) times per vertex and
    interval (the length coordinate adds ≤ n).
  - DATA: MONO_V 0.
- DEAD: the level potential Φ as a bound for ZFL. Instance u23sw64_n32: all 8 ZFL transitions keep Φ(u) for every u ∈ Z (SUB 8, PR 0).
  - Over the whole corpus only one ZFL transition raises some Φ (PR 1, nep13_n24 with its start).
  - Reason: all 32 vertices have LEV = 0. λ_Ξ = 20 ≠ λ_W = 13, and the climbs are path-set changes to the fixed Ξ-cycle node 20, which W
    does not see.
- DEAD: any gate potential, i.e. any function of (D_k, the full gate map g_k, λ_Ξ, λ_W, Z_k, LEV_k). Instance u23sw64_n32: the
  W-constant interval of states [2, 10] holds all 8 flat transitions, and const.py finds every one of these data CONSTANT on it.
  - D = {27}; gate 27 for every vertex; σ̄(27) = 20, Ξ-cycle 20 ↔ 27; the W-cycle runs through 27 → 3 → 22 → … → 13 → 20 → 27.
  - Corpus (const_flat.txt): 74 of the 79 flat transitions (sbcg + alt lists, counted per list) lie in intervals where all of these
    data are constant. Only nep22f_n64 (D, gate) and nep13_n24 (D, gate, λ_Ξ, LEV) move them.
  - So the Lead's (2) («a monotone order on gates within one W-run») cannot bound ZFL. Whatever bounds it must see the Ξ path sets
    below the top-level gap, i.e. the SI run on G_I of §1.
- DEAD: the Bellman–Ford / Lemma P route inside G_I. It needs each step to be Ξ-optimal in its arena (R17 (b), box 31 GP), and S1's
  tie-break is neither Ξ-greedy nor switch-all:
  - XNGRD: switches whose new edge is not Ξ_t-best among the vertex's tight arena edges. 11 on u2flat73_n32 (62 greedy), 4 on
    u23sw64_n32, 4 on cw11_n24.
  - LAZY: Even vertices that keep σ_t(v) although a tight arena edge is Ξ_t-improving. 23 on u23sw64_n32.
  - Corpus totals: XGRD 311, XNGRD 46, LAZY 64.

## 4. DATA: the quadratic families, and per-vertex Ξ-changes inside one W-run
- latew_K16_m32 (n 482) and fx_K8_m32 (n 250): FL = ZFL = 0, with 561 and 281 W-constant intervals of length 0.
  - ZFL ⊆ FL by definition, so these families cannot show ZFL growth. Their quadratic counts live in W-changing transitions (R*_F, R138).
  - CORRECTION to the brief's premise «FL_F = 0, so ZFL is the right place to look for growth»: ZFL ≤ FL = 0 there.
- What does grow there are TXC events (Ξ(u) strictly climbs with W(u) fixed, at any transition, R92). On mkrw LATE=1 K m (regenerated
  with red/span/mkrw.py; K 16 m 32 is the pinned sha1 6d34c161):

| K | m | n | TXC per W-run (max) | TXV: one vertex's TXC events | XCV: one vertex's Ξ-changes |
| --- | --- | --- | --- | --- | --- |
| 4 | 16 | 186 | 261 | 8 | 9 |
| 8 | 16 | 242 | 697 | 16 | 17 |
| 8 | 32 | 370 | 905 | 16 | 17 |
| 16 | 16 | 354 | 2,337 | 32 | 33 |
| 16 | 32 | 482 | 2,673 | 32 | 33 |

  - TXV = 2K and XCV = 2K + 1 exactly, independent of m. Per-vertex Ξ-changes inside one W-run are LINEAR on this family. This is
    L-LIT T52's XI-CH-POLY and L-NEW 38's P* object.
  - fx_K8_m32: TXV 16, XCV 137 (n 250).
  - Corpus maxima (1,132 runs): TXV 50 (pp_K48_n449), XCV 63 (gate_K64_n581).
  - Gate classes of all TXC events (corpus / families): SPD 21,102 / 1,140; NOG 7,939 / 383; GSELF 5,406 / 1,186; GCH 1,772 / 496;
    NSP 1,676 / 0; NDEC 0 / 0.

## 5. What is open, exactly
- [P-INT]: polynomially many transitions per W-constant interval. Equivalently (INTERVAL-SI), a polynomial bound on the runs of VJ
  strategy improvement under SPEC S1's tie-break on W-tight subgames G_I, as long as no W-improving edge enters the arena.
  - DATA: max 8 (u23sw64_n32, n 32).
  - CONJECTURE INT-LIN: |I| ≤ n − 1 for every W-constant interval. No proof; the Bellman–Ford route is DEAD (§3).
- Kill target for L-RED (READING, not attempted here): embed a long SI run as one G_I. Requirements:
  - (R1) τ stays put: no Odd improving switch in Odd's own frame throughout;
  - (R2) all simulated Even edges are W-tight;
  - (R3) no Ξ-improving edge is W-better.
  - My one-line sketch fails at (R1): routing every Odd vertex of the simulated game to one sink makes the simulated Odd edges
    Odd-improving, because they are longer to an Even-favourable cycle node.

## 6. Lead 14:09Z (a): L-NEW's DEEP_4 restricted to W-constant intervals (DATA). The deep residual sits at the boundaries
- Tool: si/gate/deepint.py. It keeps box 87's definitions verbatim (read-only copy gate/depth_lnew_b46f7759.py, l-new b46f7759) and splits
  every path-set change of depth ≥ 4 by its transition:
  - IN: W-flat, i.e. inside a W-constant interval;
  - BD: W-changing, i.e. at an interval boundary.
- Control: D4 (IN + BD per (F, v)) reproduces box 87's DEEP_4 exactly: 42 on fcobs_6, and 10, 12, 13, 15, 17, 19, 21 on
  switchbestexp_2..8. L-NEW's own script, run on fcobs_6, prints d4 42.

| corpus | depth ≥ 4: IN / BD | depth ≥ 1: IN / BD | max per (F, v): D4_IN / D4_BD |
| --- | --- | --- | --- |
| 1,132 runs (deep_sbcg.txt, deep_alt.txt) | 102 / 23,465 | 424 / 66,651 | 5 (u23sw64_n32) / 42 (fcobs_6) |
| switchbestexp_2..8, counter_symsi_8 (deep_extra.txt) | 0 / 4,204 | 0 / 6,061 | 0 / 21 (switchbestexp_8) |

- READING: 99.6 % of the deep changes, and all of box 87's SHALLOW-k killers, happen at transitions that change W.
  - Inside intervals there are at most 10 deep changes per flat transition (u23sw64).
  - So the deep residual of LEVEL-RED is a boundary phenomenon, as far as data go. A bound on it must use what W's change does to Ξ,
    not the tie-break stalling of §1.
  - [P-INT] and DEEP_k-POLY look like two separate residuals.

## 7. Lead 14:09Z (b): is S1's tie-break a known anti-stalling rule in disguise? A fixed-order (Bland-type) rule is DEAD
- What S1 is. SPEC table row A5 (docs/new/N5-ssi-global.md), quoted: «SPEC's σ' is the counterstrategy of the VJ procedure (longest-path ties
  to the smallest index; BFS first discovery; DFS cycle choice at the cycle node)».
  - In S4a this runs on the dual of the arena H_k. W's cycle node even (in the original game) gives the BFS branch; odd gives the
    longest-path branch.
  - Inside a W-constant interval, σ_{k+1}(v) is therefore the BFS-first-discovered tight successor in H_k. In 14 of the 18 intervals of
    revisit_flat.txt every cycle node of W is even; the other 4 mix even and odd.
  - The BFS discovery order runs over H_k's reverse edges, which depend on Iσ_k at OTHER vertices. So the order on OPT(v) is
    state-dependent: S1 is a fixed deterministic map H_k ↦ σ_{k+1}, not a fixed order.
- Fact (trivial, PROVED lane). Suppose a rule picks σ_{k+1}(v) as the minimum of a fixed order <_v on OPT(v) ∩ H_k(v). Since σ_k(v) ∈ H_k(v)
  always, the rule only moves down <_v. So no vertex returns to an edge it left within the interval, and each vertex switches at most
  |OPT(v)| − 1 times; that would give |I| ≤ m_E.
- DEAD: «S1 restricted to a W-constant interval is a fixed per-vertex order rule (Bland-type)». Instance u23sw64_n32, interval [2, 10]:
  - REV 31: returns of a vertex to an edge it left inside the interval;
  - one vertex switches 6 times with |OPT(v)| = 5.
  - Also REV 5 on u1t_own6_n32 [2, 7], 2 on u1t_cex_n32 [4, 8], 1 on u2flat73_n32 [7, 10]; tool si/gate/revisit.py, outputs
    gate/revisit_flat.txt.
  - A global fixed order on strategies is consistent with the data, but it bounds |I| only by the number of strategies, so it gives
    nothing.
- Anti-CYCLING is not the issue: Ξ strictly rises, so SI cannot cycle. The relevant notion is anti-STALLING. Whether S1's BFS-first-
  discovery rule is an instance of a strongly-feasible-tree rule waits on L-LIT T54's opened source. No claim here.
- Next for [P-INT]: the structure left is «BFS-first discovery on the reverse tight arena, with layers = W-lengths fixed». Candidate
  potential (CONJECTURE, untested): the BFS discovery rank of σ_k(v) inside its W-length layer, ordered by layer from the cycle node
  outward.

## DONE / FINDINGS / NEEDS
- DONE: experiments/si/gate/ (gate.py, const.py, agg.py, run.sh, inst/ copies, outputs); si/check.sh «box 51b»; this note.
- FINDINGS:
  1. PROVED (lane): Theorem INTERVAL-SI (with Lemma TIGHT-VALUE). A W-constant interval is a VJ strategy-improvement run on the W-tight
     subgame G_I. Corollary FL-INT: FL-POLY ⇐ R*-POLY ∧ [P-INT].
  2. PROVED (lane): Lemma GATE. A flat Ξ-climb at u ∈ Z_{t+1} has (a) a gate change, (b) a non-same-pair gate, or (c) a strict climb of
     its gate (a GATE_F event). The box 50b form without (c) is not what the argument gives. DATA: (c) never occurs at flat transitions;
     NSP 498 / GCH 26 / GSELF 2 of 526.
  3. PROVED (lane): Lemma LEV-FLAT (Φ does not fall inside a W-constant interval).
  4. DEAD: level potential Φ and every gate potential (functions of D, the gate map, λ_Ξ, λ_W, Z, LEV) as bounds for ZFL. Instance
     u23sw64_n32, interval [2, 10]: all constant over 8 flat transitions. 74 / 79 corpus flat transitions lie in such intervals.
  5. DEAD: the Bellman–Ford route in G_I. S1's tie-break is not Ξ-greedy (u2flat73_n32, 11) and not switch-all (u23sw64_n32, LAZY 23).
  6. DATA: latew_K16_m32 and fx_K8_m32 have FL = ZFL = 0, so they cannot grow ZFL. mkrw LATE=1 has per-vertex Ξ-changes per W-run of
     2K + 1, linear and independent of m.
  7. READING: FL steps are degenerate pivots (stalling). N5-LZC (R93) is the anti-stalling rule and has FL = 0.
  8. CONJECTURE INT-LIN (|I| ≤ n − 1).
  9. DATA (§6): DEEP_4 lies at interval boundaries: depth ≥ 4 changes IN 102 / BD 23,465. Per (F, v) D4_IN ≤ 5, D4_BD ≤ 42. The SHALLOW-k
     killers are all BD.
  10. DEAD (§7): S1 as a fixed per-vertex order rule (u23sw64_n32 [2, 10]: REV 31; 6 switches with |OPT| = 5). S1 is BFS-first discovery,
      with an order that depends on the state.
- NEEDS: none from the owner. Lead:
  - L-LIT: open a source on network-simplex stalling and anti-stalling rules (Cunningham), and on SI with arbitrary improving-subset
    rules on games with fixed cycle nodes.
  - L-RED: the [P-INT] embedding target (§5).
