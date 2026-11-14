# R177 CDAG's order as an N5 FL run: S1's tie-break is canonical (RESULTS R24 (b) TB: index-min at odd W-cycles, root-first lex-min at even ones); FL runs at odd W-cycles are ≤ deg − 1 per vertex, so gen(n) cannot be followed there; in the even regime FL runs are ≤ height(D) + 1 unless the W/Ξ dependency graph D has a cycle (CASC-G); lex-min alone allows 2(2^(d+1) − d − 2) steps on a 2-wide ladder (exact), but no Ξ-structure found supplies that availability (idealised model, DATA: linear). No kill (L-RED successor 42)
Started 2026-11-01 10:39Z (Lead STEP 1, date -u). Brief: «R177 = realise CDAG's exponential order as an N5 FL run … First read SPEC S1 (RESULTS R15 / R57)
and the code (n5x / si.py) to pin down exactly how the tie-break chooses among W-optimal strategies. If it is canonical … say whether it
can follow gen(n) at all. Report one of: a kill … or the exact obstruction with the smallest instance.» Labels: PROVED (lane), DATA,
READING. Not a TARGET.md claim. G-N5-TIME stays OPEN. Sources opened: docs/new/N5-ssi-global.md (SPEC S1-S5, Q1-Q4);
experiments/si/si.py l. 78-205 (Engine.evaluate); experiments/new/box21/n5x.py step(); l-new d4024537 docs/new/N5-FLAT-box130.md and
experiments/new/box130/flatcnt.py; docs/new/N5-K9-Pstrict-counter.md (CDAG_n, gen(m)); RESULTS R24 (packet docs/new/P-N5-U1-box31.md §2
TB, §3 CASC), R102 (S4B-OPT), R170 docs/red/R170-twofix.md (FREEZE).

## 0. Answer
- The tie-break is canonical, and it is already signed. RESULTS R24 (a) Lemma R + (b) Lemma TB (stated on 𝒞^1O; the proof uses only
  S1 (iv) and the restriction step, so it reads on every game; DATA below on every game). At a fallback-free S4a transition, a mover h
  with W'(new) = W'(old) that is not a corner picks:
  - ODD regime (h's W-cycle node c has odd priority; in the dual of the arena Odd takes the LONGEST path): the smallest-index tied
    option. So the index strictly decreases.
  - EVEN regime (c even; BFS in the dual): the tied option whose root-first key κ is lex-least. κ(x) = indices of the σ'-play from x,
    read backwards from c (c excluded).
- Odd regime: gen(n) cannot be followed. FL-IDX (PROVED, lane): in a run of consecutive FL transitions of a TWO-FIX window, a non-corner
  vertex at an odd W-cycle moves at most deg − 1 times. In gen(n) vertex m has m options and moves 2^(m−1) − 1 times.
- Even regime: no kill, and the obstruction is narrower.
  - κ is monotone along an FL run, but its range is exponential.
  - CASC-G (PROVED, lane; R24 (c) CASC's induction off route form): let D be the dependency digraph (v → u when u lies on the W-play
    prefix or on the Ξ-play of a W-tight option of v). If D is acyclic, an FL run has at most height(D) + 1 transitions.
  - Any D-cycle has an "upward" Ξ-edge, and that edge needs an ODIFF vertex (σ̄ ≠ τ) on its Ξ-play, or the W-cycle.
  - So a gen(n)-length FL run needs, at the same time: (i) even W-cycles; (ii) a D-cycle through ODIFF gates; (iii) Ξ-improvement that
    acts as the adversary which TB's lex-min rule needs.
- What lex-min alone allows (DATA, exact). With adversarial availability, a 2-wide W-ladder of depth d allows 8 / 22 / 52 FL
  transitions for d = 2 / 3 / 4. That is 2(2^(d+1) − d − 2): every level-l vertex makes its maximum, 2^l − 1 moves. At d = 5 at least 84.
- What Ξ supplies (DATA). The idealised two-face model holds τ and σ̄ fixed, so there is no stabiliser question. Search over W-ladders
  with free Ξ-faces finds linear FL runs only: 4 / 7 / 10 at d = 2 / 3 / 4, against ceilings 8 / 22 / 52. With S4c fallbacks the whole
  run stays linear too: at most about 3.6 steps per Even vertex (57 at 16, 54 at 18), fallback-free stretches ≤ 14.
- The exact obstruction, with the smallest instance: the 2-wide ladder at d = 2 (4 moving Even vertices).
  - TB allows 8 FL transitions there.
  - The best Ξ-structure found gives 4. My hand designs fail on the same "corner-symmetric" comparison: the set that closes the
    D-cycle must be Ξ-worse at one state and Ξ-better at a later one (§5).
  - In the real game a second obstruction comes on top: every two-face option needs a stable ODIFF gate (R175 §3 (ii)).
- Nothing here is a kill. Nothing here bounds FL in general either: CASC-G needs D acyclic, and the idealised model is DATA.

## 1. The tie-break among W-optimal options (RESULTS R24 (a), (b); re-read here on every game)
Setting: a fallback-free S4a transition j (I_σ ≠ ∅). The arena H = H_(j−1): Even v keeps A(v) = {σ_(j−1)(v)} ∪ I_σ(v), Odd keeps
τ_(j−1). σ_j = the S1 procedure's dual-Odd choices on dual(H) against τ_(j−1). W_j = the valuation of σ_j in G with Odd fixed to τ_(j−1).
A FLAT move: h moves o = σ_(j−1)(h) → w = σ_j(h) with W_j(o) = W_j(w). CORNER: h lies on the σ_j-play from o or from w, or h = c.
- Why (sketch; R24 TB is the signed proof, this is the reading on every game):
  - In dual(H), Ω + 1 flips c's parity. si.py l. 154-170: if c is odd in G, dual-Odd (= G-Even) h takes the first strict maximum of
    longest(y) over hs[h], in increasing index (FIX 4). If c is even in G, h's choice is the vertex of the previous BFS layer that is
    scanned first (l. 171-179).
  - Lemma R (R24 (a)): every fully optimal successor survives the restriction. Both o and w are fully optimal: flat and non-corner.
  - Odd regime: both attain the maximum, and the first one in index order is chosen, so w < o.
  - Even regime: within a layer, BFS discovery order is (order of parent, index), since gp lists predecessors in increasing index and
    restrict() keeps that order. By induction on the layer, this is the lex order of κ, so h's parent is its κ-least tied successor:
    κ_j(w) <lex κ_j(o). The BFS tree is the σ_j ∪ τ_(j−1) play graph, so κ_j(x) is read off the σ_j-play.
- DATA: experiments/red/r177/tbcheck.py checks both rules at every flat non-corner move of the whole run (not only inside windows).
  - Corpus: 813 distinct (game, start) pairs, RESULTS Erratum E-1 (red/r177/runcorp.sh, c_corpus.txt), 0 errors. 435 flat non-corner moves
    (12 odd, 423 even), 0 violations; 33 corner flat moves (not tested); 48 FL transitions (W_j = W_(j−1), σ changes), longest FL run 8.
  - 3,000 random games (tbrand.py, seed 177): 6 odd, 25 even, 0 violations.
  - Pins: u23sw64_n32 (sha1 18b46837d2f0…): 66 even flat moves, FL run 8; u2flat73_n32 (bc1547d42172…): 73, FL run 3; 0 violations.
    Both from the default S3 start, written out as r177/instances/*_default.start (u2flat73's equals box 130's file). Each passes
    startck, Oink 8fbf0a7 --zlk + verify, --tl + verify (regions agree) and xeng (n5b identical state by state).
  - R24's referees had 113 TB-odd and 535 TB-even arena cases, 0 failures (their DATA).

## 2. Odd regime: FL-IDX (PROVED, lane)
Statement. Take a run of consecutive FL transitions a+1..b of a TWO-FIX window (τ, σ̄ constant, no fallback). A vertex h whose W-cycle
node is odd, and which is not a corner at any of its moves, moves at most deg(h) − 1 times in the run.
Proof.
1. W is constant on the run. If h moves at j (o → w, non-corner), then W_j(h) = h ⊕ W_j(w) and W_(j−1)(h) = h ⊕ W_(j−1)(o) = h ⊕ W_j(o).
   So the move is flat (box 130 FL-TIGHT's argument).
2. h's cycle node is the same at every state, so TB-odd applies at every move: the index of σ(h) strictly decreases.
3. An index can strictly decrease at most deg(h) − 1 times. □
- Consequence for gen(n): vertex m of CDAG_n has m options and switches 2^(m−1) − 1 times. For m ≥ 3 that is more than m − 1. So no
  FL run whose CDAG vertices sit at odd W-cycles follows gen(n). The bound is per FL run. A fallback or a W-change ends the run.

## 3. Even regime: monotone κ and CASC-G
- κ-MON (PROVED, lane): in an FL run of a TWO-FIX window, κ_(j+1)(x) ≤lex κ_j(x) for every x at an even W-cycle.
  - σ_j's play from x lies in H_j and is fully optimal there (FL-OPT, box 130), and BFS gives the lex-least such path.
  - Strict at non-corner movers. The range is exponential (paths), so κ-MON gives no polynomial bound.
- CASC-G (PROVED, lane; R24 (c) CASC's induction, without route form).
  - Setting: a run J of consecutive FL transitions of a TWO-FIX window, with no corner mover in J. Opt(v) = the W-tight options of v,
    constant on J (FL-TIGHT).
  - D: v → u iff, at some state of J, u (Even) lies on the W-play of some z ∈ Opt(v) before its cycle node, or on the Ξ-play (G_σ̄)
    of some z ∈ Opt(v).
  - Statement. If D is acyclic, a vertex of D-height h switches only at run steps ≤ h. So J has at most height(D) + 1 ≤ n_E transitions.
  - Proof (CASC §3, step 3 verbatim with "lower level" := "lower D-height"):
    - Let S_h be the first step from which no vertex of height ≤ h switches. S_0 = 0: a vertex of height 0 has candidates whose W-plays
      and Ξ-plays meet no Even vertex, so its keys and Ξ-values are constant, and a key-least arena choice stays key-least.
    - From step j = S_(h−1) on, every vertex below v is fixed. So Ξ(z) and κ(z) are constant for every z ∈ Opt(v): the plays read only σ
      at D-successors, and τ, σ̄ are fixed.
    - v moves at most once more, to z1 = the key-least option of A_j(v) ∩ Opt(v) (TB).
    - At a later step j' with σ_(j')(v) = z1, every arena option z ≠ z1 has Ξ(z) ▷ Ξ(z1) ⊵ Ξ_j(σ_j v). So z was in A_j(v), hence
      κ(z) > κ(z1), and v keeps z1. □
  - Corner movers are excluded by hypothesis. DATA: 33 corner flat moves in the corpus.
- UP (PROVED, lane): every D-cycle contains an edge v → u, from the Ξ-play of some z ∈ Opt(v), such that the Ξ-play from z to u passes
  an Odd vertex with σ̄ ≠ τ, or u lies on z's W-cycle.
  - Proof. W-edges of D strictly lower the W-length (W-tight plays before the cycle node). So a D-cycle has an edge that does not lower
    it. Suppose that edge is a Ξ-edge whose play from z to u meets no Odd vertex with σ̄ ≠ τ. Then that play is z's W-play, since both
    follow σ at Even vertices and τ = σ̄ at the Odd ones. So u lies on z's W-play: before the cycle node (lower length, contradiction),
    or on the W-cycle. □
- What this means for gen(n) (READING). For an FL run to follow CDAG's order:
  - every CDAG vertex needs an even W-cycle (§2);
  - D must be cyclic, through ODIFF vertices (UP). CDAG's Ξ-edges go down in index, so some W-play must climb in index;
  - the κ-value count must be large enough: #κ-values(v) ≤ Σ_k #κ-values(W-target_k(v)). So vertex m needs W-depth at least
    (m − 1)/log2(deg).
  - If the W-graph and CDAG's Ξ-graph point down in one common order, D is acyclic and the FL run is ≤ n_E (CASC-G). That is
    box 130's suggested embedding in its natural form.

## 4. DATA: what lex-min allows, and what Ξ supplies
- LADDERBF (red/r177/ladderbf.py, exact). Setup:
  - W-ladder: levels 1..d, two Even vertices per level. Option k of a level-l vertex goes through its own gate to vertex k of level l − 1;
    level 1 goes to c_W. Gate indices random, best of the trials.
  - Availability per vertex per step is chosen ADVERSARIALLY (current only, or both options). σ' = the lex-min tree of that arena.
  - The longest chain of σ-changing transitions, computed exactly (state DAG; κ strictly decreases at movers):

| d | Even vertices | trials | longest chain | 2(2^(d+1) − d − 2) |
| --- | --- | --- | --- | --- |
| 2 | 4 | 20 | 8 | 8 |
| 3 | 6 | 20 | 22 | 22 |
| 4 | 8 | 20 | 52 | 52 |
| 5 | 10 | 2 | 84 | 114 |

  - At d ≤ 4 every level-l vertex makes 2^l − 1 moves, the ceiling of the κ-count recursion K(v) ≤ Σ K(targets). So TB alone permits
    exponential FL runs at linear size. Any polynomial bound must use where availability comes from: I_σ, i.e. Ξ.
- The idealised two-face model (red/r177/abs177.py on the si.py engine; red/r177/fastabs.py fast, equal to abs177 on 200 + 200 random
  genomes (with and without fallbacks) and on every champion below: fastver.py, 0 mismatches). Setup:
  - Even vertex x (priority 0) → its gates g (Odd, priority 1).
  - G_W: g → its W-target, one level down, or c_W (top even). All W-values tie, (c_W, ∅, 2·level), so FL holds at every step.
  - G_X: g → β_g (Even, priority ≥ 4, Ξ-only, one per option) → its Ξ-target (any vertex later in a topological order, or c_X).
  - Dynamics = S4a with τ := W-faces and σ̄ := Ξ-faces FIXED: A_j = σ_j ∪ (Ξ-improving in G_X), σ_(j+1) = the S1 optimum of G_W
    restricted to A_j. FB=1 adds the S4c fallback (best Ξ face).
  - Climbs (mutation hill-climbs with restarts over W-targets, Ξ-targets, β ranks and parities, gate indices, start):

| model | d (levels) | width W | deg | Even vertices | best FL run (no fallback) | ceiling (adversarial) | best whole run with S4c fallbacks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fastabs | 2 | 2 | 2 | 4 | 4 | 8 | 8 (4 fallbacks, FL stretch ≤ 2) |
| fastabs | 3 | 2 | 2 | 6 | 7 | 22 | 13 (6 fallbacks, ≤ 3) |
| fastabs | 4 | 2 | 2 | 8 | 10 | 52 | 19 (5, ≤ 5) |
| fastabs | 6 | 2 | 2 | 12 | – | – | 28 (9, ≤ 6) |
| fastabs | 8 | 2 | 2 | 16 | – | – | 35 (10, ≤ 6) |
| fastabs | 3 | 3 | 3 | 9 | 15 | – | – |
| fastabs | 4 | 3 | 3 | 12 | – | – | 41 (9, ≤ 10) |
| fastabs | 6 | 3 | 3 | 18 | – | – | 54 (10, ≤ 8) |
| fastabs | 8 | 3 | 3 | 24 | – | – | 49 (8, ≤ 14) |
| fastabs | 4 | 4 | 4 | 16 | – | – | 57 (9, ≤ 12) |
| abs177 (random W, engine) | 3-6 | – | 2-3 | 8-12 | 8-13 | – | – |
| abs177 ladder (engine) | 4-7 | 2 | 2 | 8-14 | 9-12 | – | – |
| abs177 bidirectional (W down, Ξ up) | 3-6 | 2 | 2 | 6-12 | ≤ 6 | – | – |
| Ξ-target = W-target (same face) | 4 | 2 | 2 | 8 | 3 | – | – |

  - Every climb champion is D-cyclic (dcheck.py). D-acyclic random genomes: 300, CASC-G holds in all (thin: runs ≤ 2).
  - The gap is large: at d = 4, TB permits 52 and Ξ supplied 10. The FL runs found grow about 3d; whole runs with fallbacks ≤ 3.6 n_E.
  - All champions re-run on the si.py engine (abs177, with and without FB): 0 mismatches (fastver.py).

## 5. Why the designs fail (READING) and the stabiliser layer
- Corner symmetry (d = 2 hand designs). To delay the bottom move (the most significant κ digit), a bottom vertex's alternative needs a
  Ξ-face that reads an upper vertex v: an upward D-edge.
  - If v's own faces read the bottom vertex again (a Ξ-cycle), then the non-move at the start and v's later move compare the same
    set: the closing set S = {β of the new face, β of v's face, …}.
  - The first comparison needs S Ξ-worse; the second needs S Ξ-better.
  - Only the terminal context differs, so the band trick must separate them, and the length parity then fails in one of the two
    contexts. This is the same mechanism as R173 PORTAL / R175 ODD-GATE.
  - Without a Ξ-cycle, the vertex last in Ξ-order has a static Ξ preference and moves ≤ deg − 1 times. That starves the vertices that
    read it.
- Realising a two-face option in G. A gate g: τ(g) → W-target side, σ̄(g) → β → Ξ-target side.
  - (τ) I_τ(g) ∌ σ̄(g) depends only on τ (Ξτ is τ against τ̄), so it is a static check. With β even, c_W below every β, and W-plays
    otherwise below c_W, it holds whenever both faces' τ̄-plays end at c_W through the same E-vertices.
  - (σ̄) σ̄(g) must be Odd's best against EVERY σ of the run. With all β even, that is Ξ(W-target) ▷ β_g ⊕ Ξ(Ξ-target) at every state.
  - If that is made automatic (W-targets' own β more relevant than anything on the face), then v's own option β dominates its faces
    and v's Ξ preference becomes static. That contradicts the dynamic preference the climber needs.
  - Gates whose Ξ-face reaches the terminal directly (the top of the Ξ order) cannot satisfy (τ) and (σ̄) together: the comparison
    is static, so σ̄ = τ is forced there. The top of the Ξ order is therefore single-faced, which feeds the "last vertex is static"
    point above.
  - So the real game adds R175 §3 (ii)'s open stabiliser question on top of the idealised gap.

## 6. Verdict, smallest instance, next
- Verdict: no kill. FL runs following gen(n) are impossible at odd W-cycles (FL-IDX). At even W-cycles they need a D-cycle through
  ODIFF gates (CASC-G, UP) and a Ξ-structure that drives TB's lex-min rule. TB allows exponential runs (LADDERBF); no Ξ-structure found
  does, even with τ and σ̄ held fixed by fiat.
- Smallest instance of the obstruction: the 2-wide ladder, d = 2 (4 moving Even vertices, 8 options). TB's ceiling is 8 FL transitions;
  the best idealised Ξ-structure found gives 4 (genome red/r177/out/fa_d2_k2_W2.json). CDAG_6 (box 130) stays the smallest one-player
  witness that rule-free potentials fail.
- CONJECTURE IDEAL-LIN (DATA only): in the idealised two-face model, fallback-free runs are O(n_E). If true, a polynomial FL count
  reduces to (a) this model's bound and (b) corner moves. The proof side should try a potential mixing κ and Ξ.
- Open routes for L-RED: a construction beating 2d at d = 3-4 in the idealised model (that would be the first super-linear FL family,
  still without stabilisers); then stabilisers.

## 7. Files and checks (experiments/red/r177/)
- tbcheck.py (TB on every flat move), runcorp.sh + c_corpus.txt (813 pairs), tbrand.py (random games).
- ladderbf.py (exact ceiling), abs177.py (idealised model on the si.py engine), fastabs.py (fast version), fastver.py (equivalence),
  climbl.py / bidir.py / sameface.py (climbs), dcheck.py + cascg_rand.py (CASC-G on the model), out/ (climb logs, champion genomes).
- The idealised-model genomes (out/*.json) are NOT parity games of an N5 run (two Odd strategies are fixed by fiat), so they are
  not instances in the kill sense; no instance claim is made for them.
- check.sh block «R177»: tbcheck on the two pins, ladderbf d = 3 (22), fastver on the champions, the d = 2 champion's run (4 / 8 with FB).
