# Box 213 (D18): KEY-WINDOW — the τ-arena question of box 212's RF-D. (P2^τ) is FALSE on every window with Y ≠ V; RF-D keeps its inequality and loses its window clause (repair (b)); N5's key step on Γ3 is a least-root-first-key descent on the fixed W-graph (KEY-TAU, a consolidation of landed lemmas); G-2 proved from R122 (CANDIDATES and DATA; not a bound for N5; G-N5-TIME stays OPEN)
L-NEW successor 75 (session_01V5yGRWimvjsi2nZhjaevtK), D1 / D14 / D18 / D21. Written 2026-11-13 from 04:10Z (date -u). Box 213 approved by
the Lead (23:26Z; «Go after Addendum A» 00:04Z); first deliverable set by the Lead's brief to successor 75 (item 1 (e)) and the Lead's
03:57Z message: «(1) GAP G-1 is CONFIRMED with DATA … This is your box 213 first deliverable; choose (a) or (b) with reasons, in the
statement you send me. (2) G-2: «O1 = the whole run is one window» is asserted in box 212, not proved. Prove it or relabel it. (3) N-4
…». Statement sent to the Lead 04:05Z before any long run.
Labels: PROVED-lane (my proof, unrefereed), CANDIDATE (lane statement with a proof sketch from landed text, unrefereed), READING (what a
landed text says), DATA (not to sign). Nothing here is a RESULTS entry. Not M3, not M4, not a bound for N5 or N5′-xi; **G-N5-TIME stays
OPEN.**

## 0. Answer
1. **G-1: repair (b), because (a) is false where it can be tested (DATA, §2).** REFEREE-2 40's (a) needs (P2^τ): «τ(g) ∈ Y for every gate
   g ∈ Y». On every window step with Y ≠ V that N5's runs produced (random 4 modes × 300 genomes: 38 steps; frozen set: K1F21_n48,
   DHIB26_2804), some gate of Y has its τ-face outside Y (counter tauclos, 38 of 38 steps; H^τ_Y is never even a game). Saved instances:
   experiments/new/box213/inst/TAUESC_rand2150.json, TAUESC_dense2151.json. So a window is closed in the σ̄-arena (RF-B (P2)) but not in
   the τ-arena that makes N5's choice; no «rule run on a closed one-player sub-game» form exists for N5's windows in either arena. RF-D
   keeps its inequality; its window clause is replaced by what RF-B proves (box 212 Addendum B).
2. **KEY-TAU (CANDIDATE; a consolidation of landed lemmas, §3).** On Γ3(G), before N5's first fallback, the one-player problem behind the
   key rule is fixed: the W-graph (mover x → the target wt of each option's e-vertex; levelled), with every Odd vertex at τ = TAU3. N5's
   step moves every mover to the option of A_t(x) = {σ_t(x)} ∪ Iσ_t(x) with the least ROOT-FIRST KEY (the e-indices of its τ-path to c_W
   read from c_W, compared lexicographically; all such paths of x have one length, R125 W3-ALL). The key μ_t(x) of x's own play is
   non-increasing in t for every mover and strictly decreases at every switch of x. Two value systems, named: the CANDIDATE set A_t comes
   from Ξσ (Odd at σ̄_t); the CHOICE comes from the W-graph (Odd at τ). Not a bound. What is measured (kcount213.py, §5): on the five
   towers the longest key sequence of ONE mover has 15, 31, 63, 127 switches (DBL4, H5, H6, HIT7; RECF4 30) while that mover has
   |K(x)| = 2^20, 2^20, 2^24, 2^28 possible keys (maxK); counter kviol (a mover with more switches than |K(x)| − 1) is 0. No growth law
   in N + M is claimed (O1 is OPEN).
3. **G-2: PROVED-lane (§4).** On every genome with an acyclic Ξ-graph, every class is constant along N5's run on Γ3(G) before its first
   fallback; no vertex lags against the last state, so the run is ONE window, the tail, with Y = V. From R122 BETA-ACYC and LAMBDA-CONST
   (landed) and standard states.
4. **N-4: corrected (§6).** notbest 187 of 6,107 moves on 38 of 86 genomes (not «12»); notebook fixed by script.

## 1. Premises (landed unless marked)
- SPEC docs/new/N5-ssi-global.md (S1 (iv): «if Ω(v) odd, the SHORTEST (BFS from v over predecessors in list order; first discovery sets
  Odd's choice)»; S4a: «σ_new = Odd's optimal counterstrategy (S1 procedure) in the dual of H to the dual-Even strategy τ»).
- [Q R125] R117 (Γ3(G), S3) and TAU3 (P-N5-REACH), as R125 states: «RESULTS R117's entry signs S3-START, PAD, K3 and TAU3 for every genome»;
- [Q docs/new/P-N5-CHAIN.md@7fa6aff4] (R125's object): «In H, Odd plays τ: pe at every gate, K2 → K2.»
- [Q R125] (Lemma ESC3-ALL) «in every standard state Iσ ∋ (K0, K1), every pointwise optimum of S4a's arena agrees with σ off the movers»;
  (Lemma W3-ALL) «in every standard state every option of a level-ℓ mover has arena value (c_W, ∅, 5ℓ + 4), no mover is its own arena cycle
  node and TIE(x) = A(x)».
- [Q R122] (Lemma BETA-ACYC) «for every genome G whose Ξ-graph is acyclic, on Γ(G) or Γ3(G), and every Even strategy that agrees with the stated
  start off the movers (transported through the pads on Γ3), every optimal counterstrategy of Odd takes the β-face at every gate, and no
  play from a non-e vertex contains an e-vertex»; (Lemma LAMBDA-CONST) «every vertex's cycle node is then independent of the movers' choices».
- [Q R24] (a) Lemma R and (b) Lemma TB («(TB-even) c even and W' = W_k on v's σ_k-play from v to (before) c ⇒ the root-first index key pk(v)
  strictly decreases lexicographically»), landed on 𝒞^1O. Not tagged (cited, not quoted): R104 [RULE]; WRAP Remark (3) (P-N5-WRAP, as cited by L-RED R240, claude/l-red
  50fe432a). Credited, not re-proved.
- [Q docs/red-b/B3-guide.md@9bce72fa] L-RED-B 3 FLAT-IDX / hbound (claude/l-red-b, §3): «L-RED-B reading, NOT PROVED».
- [STD] (READING, not re-proved here): N5 from S3 on Γ3(G) visits only standard states before its first fallback: σ off the movers by
  ESC3-ALL (S4a's output is a pointwise optimum, [1E-N3] = R57 (b)), τ by TAU3; box 104's W-FLAT (claude/l-si 26704e01, lane) states it
  for SPEC's rule. DATA: counter tau3 = 0 (§5).
- Box 212 (l-new be167574, docs/new/N5-RFLEVEL-box212.md): RF-A, RF-B, RF-C CANDIDATE, RF-D CONDITIONAL; REFEREE-2 40's pre-read
  (claude/referee-2 8e075239, docs/referee-2/R2-box212-preread.md §5, §7, §9): G-1, G-2, N-4.
- Sources outside the fleet: Post-Ye, arXiv:1208.5083 v2 (opened by successor 74; Thm 3.7, 4.8). Hansen-Kaplan-Zwick: full text NOT
  opened, NOT cited.

## 2. G-1: the τ-arena form of RF-B fails at (P2^τ) (DATA, with the reason)
- The form tested (REFEREE-2 40 §7, repair (a)): H^τ_Y := the movers of Y with A(x) ∩ Y, Odd fixed at τ|Y; (P2^τ) τ(g) ∈ Y for every gate
  g ∈ Y; (P5^τ) N5's step at the movers of Y = the S1 optimum of H^τ_Y.
- Tool experiments/new/box213/key213.py: N5 (box190 n5v.step mode spec) from S3 on Γ3(G) to its first fallback; classes as box 208's
  level208.prep; windows = plat208's plateaus (reference b = T, Y = {x : class_u(x) ≤ m}) and the tail (Y = V). Counters per window step
  s → s + 1: tauclos (Odd o ∈ Y with τ(o) ∉ Y), tauclosg (gates only), undef (H^τ_Y not a game), n5out (N5's σ_(s+1)(x) ∉ Y: RF-B (P2),
  must be 0), keytau / keytauval (where defined: N5 ≠ the optimum of H^τ_Y), keytau_tail (Y = V: must be 0, the tool's self-check),
  keysig (N5 ≠ SPEC run on H_Y with Odd at σ̄_u: REFEREE-2's reading).
- DATA (out/key213_rand.out, out/key213_frozen.out; numbers from the files):
  | set | plateau steps (Y ≠ V) | tauclos (= tauclosg) | undef | n5out | keytau_tail | keysig (movers) |
  | --- | --- | --- | --- | --- | --- | --- |
  | rand (seed 2150, 300) | 4 | 42 | 4 | 0 | 0 | 107 |
  | dense (2151, 300) | 9 | 193 | 9 | 0 | 0 | 152 |
  | deep (2152, 300) | 15 | 447 | 15 | 0 | 0 | 299 |
  | noesc (2153, 300) | 10 | 225 | 10 | 0 | 0 | 89 |
  | frozen + towers (86) | 2 | 101 | 2 | 0 | 0 | 7,848 (towers 7,359; §5) |
  The seeds are box 212's rfd212 seeds; the plateau counts (deep 13, dense 8, noesc 10, rand 4) equal rfd212's «plat» in
  box212/out/rfd212_rand_spec_*.out (an agreement check between the two tools).
- Instances (find213.py regenerates the seeds and saves the first genome with undef > 0): inst/TAUESC_rand2150.json (genome 80 of seed
  2150 rand: T 2, one plateau step, |Y| 43, 6 gates of Y with τ-face outside Y), inst/TAUESC_dense2151.json (genome 44 of seed 2151 dense:
  |Y| 105, 18 gates). Frozen: K1F21_n48 (97 gates on its plateau step), DHIB26_2804 (4).
- The reason (READING): τ = TAU3 sends every gate to pe_g → e_g. RF-B's (P4) puts only the σ̄-chosen face of a gate of Y in Y; when σ̄
  chooses β_g (class ≤ m) and class(e_g) > m, the τ-face leaves Y. So Y is closed under (σ_s, σ̄_s) but not under (σ_s, τ), and N5's
  choice at a mover of Y (the τ-arena optimum, §3) reads keys through vertices outside Y.
- Choice: **(b)**. Reasons: (1) (a) is false on every window step with Y ≠ V in the data, and on the towers (Y = V) it is vacuous;
  (2) even where (a) held it would describe a two-arena rule, not SPEC's key rule, so «a generalised O1» would not follow; (3) (b) is
  exactly what RF-B proves. The wording goes into box 212 as Addendum B (append-only).

## 3. KEY-TAU (CANDIDATE; consolidation)
**Setting.** G any genome; N5 from S3 on Γ3(G); t any state before the first fallback; [STD]. A_t(x) := {σ_t(x)} ∪ {w : (x, w) ∈ Iσ_t}.
X_t := the arena of S4a at t (Even v keeps A_t(v), Odd v keeps τ_t(v)). The W-graph: x → wt(o) for every option o of x (wt(o) = the
successor of o's e-vertex; c_W if wt < 0); a τ-path of x: x → m_o → g_o → pe_o → e_o → wt(o) → … → c_W. KEY of a τ-path: the tuple of
its e-vertices' indices read from c_W; keys of one mover are compared lexicographically (they have one length, below). κ_t(x) := the least
key of a τ-path of x in X_t; μ_t(x) := the key of x's own play under (σ_t, τ_t).
**Statement.** (i) σ_(t+1)(x) = the first option of x's least-key τ-path in X_t, for every mover x. (ii) μ_(t+1)(x) = κ_t(x) ≤ μ_t(x) for
every mover x, with strict inequality whenever σ_(t+1)(x) ≠ σ_t(x). (iii) Hence every mover switches at most |K(x)| − 1 times before the
first fallback, K(x) the set of keys of τ-paths of x in the W-graph, and T_key ≤ Σ_x (|K(x)| − 1).
**Proof sketch (from the premises; to be checked by referees).**
- (i) By [STD] and W3-ALL (landed), every option of a level-ℓ mover has arena value (c_W, ∅, 5ℓ + 4), no mover is its own arena cycle
  node and TIE(x) = A(x): every play of X_t from a mover reaches c_W with an empty P-set and length 5ℓ + 4 (so every key of x has one
  length, and «hdec 0» of §5 is this fact; must-0 counters unreach and hdec), and S4a's choice at x is decided by S1's tie rule alone. In S1 on the dual of X_t, c_W (dual priority odd, the most
  Even-preferred cycle node that is reached; K0 is not a cycle node of X_t: its only arena successor pA leads to K3, more relevant than K0)
  is the first processed cycle node; R (the vertices reaching c_W) contains no vertex more relevant than c_W (K0, K3 do not reach c_W), so
  step (iii) deletes nothing, and step (iv)'s odd branch is a BFS from c_W over predecessors in increasing index; the first discovery sets
  the choice. The predecessors on a τ-path are unique except at movers and e-vertices' targets: pred(e_o) = pe_o, pred(pe_o) = g_o, pred(g_o)
  = m_o, pred(m_o) = x; a mover y's predecessors are the e-vertices with target y and β-vertices with xt = y (dead ends in X_t: a β-vertex's
  only predecessor pβ has none, gates keep τ = pe). So the BFS discovers a mover through its least option by (discovery time of the
  target, index of the e-vertex), i.e. by the least root-first key (R104 [RULE], R24 (a)-(b) in their settings).
- (ii) At t + 1 every mover holds its BFS choice of X_t ((i)), so x's play under (σ_(t+1), τ) is its BFS-tree path of X_t: μ_(t+1)(x) =
  κ_t(x). x's play under (σ_t, τ) is a τ-path in X_t (σ_t(y) ∈ A_t(y) for every y), so κ_t(x) ≤ μ_t(x). If σ_(t+1)(x) ≠ σ_t(x), the two
  paths differ in x's own e-vertex (distinct options have distinct e-vertices), so the keys differ and the inequality is strict. (Not
  «iff»: μ(x) also falls when only a descendant switches.)
- (iii) Each switch of x strictly lowers μ(x) in the finite totally ordered set K(x); every step before the first fallback switches at
  least one mover (W-FLAT / RF-D [IMP3], lane).
**Scope and literature.** (iii) is not a polynomial bound: |K(x)| is the number of τ-paths from x in the levelled W-graph (2^20 to
2^28 on the towers, §5). The key rule is a pivot
rule on a FIXED deterministic one-player problem (the lexicographic least-key path to c_W in the W-graph), but its candidate sets are
supplied by another value system (Ξσ, Odd at σ̄_t), and it moves every mover at once to its restricted optimum. Post-Ye (arXiv:1208.5083
v2, Thm 3.7, 4.8) bound the SINGLE-SWITCH simplex with Dantzig's rule on DISCOUNTED deterministic MDPs (γ < 1 part of the input; «Our
results do not extend to policy iteration»): none of the three features matches, so nothing transfers. Hansen-Kaplan-Zwick: not opened,
not cited. What box 213 contributes beyond R24 / R104 [RULE] / WRAP Remark (3) / FLAT-IDX: the Γ3 statement with the two value systems
named, and the DATA of §5; not a new mechanism.

## 4. G-2 (PROVED-lane)
**Statement.** Let G be a genome whose Ξ-graph (x → xt over all options) is acyclic. Under [STD], along N5's run on Γ3(G) from S3 up to its
first fallback, class_t(v) = class_T(v) for every vertex v and state t. Hence LAG_t = ∅ at every state (reference T), b′ = 0, and the
whole run is one class-frozen window, the tail, with Y = V (box 212 RF-C's tail clause).
**Proof.** Fix a state t. It is standard ([STD]), i.e. it agrees with the stated start off the movers (through the pads), so R122 applies
to it with σ̄_t (an optimal counterstrategy). (1) BETA-ACYC: no play from a non-e vertex contains an e-vertex. On Γ3 the pad pe_g has e_g
as its only successor, so read for every vertex v that is neither an e-vertex nor a pe pad: the e-set of class_t(v) (the e-vertices in
the P-set of v's value) is ∅. (2) LAMBDA-CONST: the cycle node Λ_t(v) of every vertex is independent of the movers' choices; the
non-movers are the same at every standard state; so Λ_t(v) = Λ_T(v). With (1), class_t(v) = (rew(Λ(v)), ∅) = class_T(v) for such v.
(3) For e_g and pe_g: the play is pe_g → e_g → w (w = wt, a mover, or c_W) and then w's play, which by (1) contains no e-vertex; its cycle
node is Λ(w), constant by (2). The e-set of class_t is {e_g} if e_g is more relevant than Λ(w) and ∅ otherwise: the same at t and T. ∎
- Where it is used: box 212's side claim «O1 is the Ξ-acyclic case, where the whole run is one window» (REFEREE-2 40 G-2) becomes this
  statement, under [STD]. RF-D's reduction says nothing on Ξ-acyclic genomes (its window is the whole run).
- DATA (g2_213.py): g2fail (Ξ-acyclic genome with b′ > 0) and g2e (non-empty e-set at a vertex other than an e-vertex or a pe pad) must be
  0; control lagcyc (a Ξ-cyclic genome with b′ > 0) fires (§5).

## 5. DATA (not to sign; experiments/new/box213/, outputs out/, inputs inst/)
Every number below is from the output files (summ213.py prints the sums; out/summ213.txt is pinned, with out/SHA1SUMS and inst/SHA1SUMS).
Sets: FROZEN = box 212's frozen set (81 genomes: run212.sh's ALL list) + the 5 towers (box212/inst) + inst/TAUESC_* (2); RANDOM = eg195.gen
modes rand, dense, deep, noesc (seeds 2150-2153, rfd212's) and acyc (2154), 300 genomes each. Runners run213.sh / run213m.sh: 600 s per
genome, resumable; TIMEOUT lines are listed by summ213.py (none in the frozen keymu213 and key213 runs).
- **G-1 (key213.py).** FROZEN (86 genomes, key213_frozen.out): plateau steps 2 (K1F21_n48, DHIB26_2804), tauclos 101, undef 2; tail steps
  770 (741 on the towers); n5out 0, keytau_tail 0 (must-0); keysig 7,848 in all, 7,359 on the towers. RANDOM (key213_rand.out, 4 modes):
  plateau steps 38, tauclos 907, undef 38, n5out 0, keytau_tail 0. Control KEY_CTRL=1 (Y minus the new successors of the movers that
  switch at the window's first step): n5out fires (check213.out, «ctrlkey»).
- **keysig reconciliation (ks213.py, ks213_towers.out).** Towers: Odd at σ̄_u or σ̄_s gives the same counts (σ̄ never changes on any tower
  state: sbar_changes 0, box 212's tail clause); non-movers keeping A_s (SPEC's arena, key213) gives 178, 1,152, 1,627, 3,923, 479 =
  7,359; non-movers kept at σ_s (H_Y as RF-B defines it, REFEREE-2's reading) gives RECF4 478, total 7,358 = REFEREE-2 40's §7 count.
- **KEY-TAU (keymu213.py).** FROZEN (88 genomes) and RANDOM (5 modes × 300): tau3, kp, kpn, muinc, muflat, mukappa, unreach, hdec all 0;
  switches 6,111 (FROZEN) and 4,500 (RANDOM), every one a same-length lexicographic descent (lexdec = switches; hdec 0 is W3-ALL's
  «one length per level»); longest key 28 (HIT7). Controls (check213.out): KM_MODE=xi (N5′-xi, Howard's tie rule) on DBL4: kp 44, muinc
  91; KM_CTRL=1 (BFS with reversed predecessor order) on DBL4: kp 213.
- **What (iii) measures (kcount213.py, kcount213_towers.out).** Towers DBL4, H5, H6, HIT7, RECF4: T 30, 136, 209, 299, 67; the most switches
  of one mover (maxsw) 15, 31, 63, 127, 30; the most τ-paths of one mover (maxK) 2^20, 2^20, 2^24, 2^28, 2^20; N 40, 40, 48, 56, 40; kviol 0.
  So one mover's key sequence has 2^k − 1 steps on DBL4 (k = 4), H5 (5), H6 (6), HIT7 (7); nothing is claimed about growth in N + M.
- **G-2 (g2_213.py).** RANDOM (g2_213_rand.out): 311 Ξ-acyclic genomes (300 acyc + 8 rand + 3 dense): g2fail 0, g2e 0; control lagcyc
  (Ξ-cyclic genomes with b′ > 0) 204, 221, 265, 209 in the four other modes. FROZEN (g2_213_frozen.out, 88 genomes): the 5 Ξ-acyclic
  ones (the towers) g2fail 0, g2e 0; control lagcyc 70 of the 83 Ξ-cyclic genomes.

## 6. N-4 and the notebook
experiments/new/box213/n4fix213.py reads out/arena213_frozen.out (successor 74's frozen run) and asserts the totals: notbest 187 of 6,107
moves on 38 of 86 genomes (the earlier «on 12 genomes» list summed to 84). With --apply it replaced the two wrong passages of notes/L-NEW.md
(BOX 213 section; dead end «Howard on a subset») by the generated line. REFEREE-2 40's second engine equals the file on all 86.

## 7. Kill criteria (where to attack)
- (K1) kp, kpn, muinc, muflat or mukappa > 0 on any N5 run on Γ3 before its first fallback kills KEY-TAU (i) or (ii) (instance named).
- (K2) tau3 > 0 kills the τ premise of KEY-TAU.
- (K3) g2fail or g2e > 0 on a Ξ-acyclic genome kills G-2 (an error in my reading of R122).
- (K4) A window step with Y ≠ V and tauclos = 0 does not revive repair (a); it would only narrow §2's «every window step».

## 8. Not claimed; TARGET.md diff
No bound for N5 or N5′-xi; T_key may be exponential (towers); RF-D's inequality unchanged, its window clause withdrawn; KEY-TAU is a
reformulation with a monotone potential, not a running-time result. Nothing here is stated in TARGET.md's vocabulary as M3 or M4: the
statements concern N5's run on the genome games Γ3(G) of R117 only. Not M3, not M4. **G-N5-TIME stays OPEN.**
