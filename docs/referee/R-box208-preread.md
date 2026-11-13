# R-box208-preread: PRE-PACKET READ (NOT A SIGNATURE) of L-NEW 72's box 208 (Lemma LEVEL, Theorem WIN, R-INT, R-HEIGHT, K1-TCYC, FVS-TCYC; Addendum A: Lemma PLATEAU, Theorem ALL-TCYC)
REFEREE successor 32 (D1 «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the
fleet's own, as wrong until it passes the gauntlet below.»). Date -u at writing: 2026-11-12T14:03Z. Lead 12:54Z item B2.
This is a read to find errors early. It is not a referee signature: nothing is frozen as a packet, every statement of the box is labelled
CANDIDATE by its lane, and a packet review, if one comes, is a separate signature.
Object: claude/l-new 8db300fe3fd8e868e61851a9bff76673146d2f10 (ancestor of origin/claude/l-new, checked), docs/new/N5-LEVEL-box208.md, sha1
55e6538110d379fc695f1f06efbd1d7b3df97494, 57,999 B, 502 lines (= the Lead's brief).
Not read before this verdict: L-RED 66's attack record on this box, docs/referee-2/, L-LIT T66, the lane's tools level208.py / plat208.py
(my counters are written from the document's statements). Read: the document, the landed entries R104, R118, R121, R122, R123, R126 in
trunk docs/RESULTS.md (471aba45), the landed packet P-N5-XICYC (sha1 149e2414…), claude/l-formal 4b376da4's Lean files.

## 0. Verdict
| statement | verdict |
| --- | --- |
| §2 class facts (K1)-(K5) | **no gap found** |
| §3 Lemma LEVEL (L1)-(L5), incl. the step «a stall forces a whole Ξ_(σ_b)-cycle into FRONT_t» (L4) | **no gap found** (§3) |
| §4 counting (C1)-(C4) | **no gap found** |
| §5 Theorem WIN, Corollary R-INT; §6 R-HEIGHT, K1-TCYC, FVS-TCYC | **no gap found**, given LEVEL and landed QUIET-N |
| Addendum A, Lemma PLATEAU (P1)-(P5), (P7) | **no gap found** |
| Addendum A, (P6) | **GAP G-P6 (exact, small, closable in one line)**: step (ii) of the induction uses «the play of state s′ stays in Y» for states s′ after the plateau, where (P2) does not give it. Repair in §5.2: answer with σ̄_s, the plateau state's choice. |
| Addendum A, Theorem ALL-TCYC | follows from LEVEL, (C1)-(C4) and PLATEAU; **no gap found once G-P6 is repaired** |
| (P7) against Lean `brsegG` / `brsegG_noH0` (l-formal 4b376da4) | the sub-game H **meets the hypotheses** (§5.3), with the same two bridges as in R-restrictC-preread §3. The theorems are proved at 4b376da4 and I built them (§5.3). |
| §10 Statement ABS (reading aid) | not read as a verdict; no statement of the box depends on it |
No FALSE statement found; no instance against any step. Own replay with own counters (§6): 36 must-be-0 counters all 0 on the lane's 78
frozen genomes, 26,500 random genomes of eight shapes, 1,200 mutants and 47,028 genomes visited by four hill-climbs; six controls
fire; run lengths equal the lane's on all 78.
What this read does NOT establish: that the bound is right. It says that I re-derived every step and found one small hole. D1 stands:
the claim is a polynomial bound for a model on ALL genomes, the data never come near the constants, and it has had one day of scrutiny.
G-N5-TIME stays OPEN; nothing here is a TARGET.md claim (§8).

## 1. Premises, by my own script
- scratch/box208_quotes.py (every outermost «…» of every bullet marked [Q], located in the landed entries R104, R118, R121, R122, R123,
  R126 at trunk 471aba45; log box208_logs/quotes.out): **19 bullets, 29 quotes, 0 missing**. 28 lie in the entry the bullet names first;
  the 29th («optimal at every vertex at once against σ_t») is in R123's title, as its bullet (l. 424-425) says.
- Scope of each, read in the entries:
  - R118 (a) Howard step, (c) DOM «[IDEAL-CYC, every genome]», (e)'s reason, (i) BR-SEG-G «[any parity game, Howard from any σ_0, under
    H0]»; R118 (b) F1 with F4′.
  - R121 (b) E-MON «[IDEAL-CYC, every genome]»; E-DOM is a [DEF] fact quoted inside it.
  - R123 CN2 (every positional pair), B-ONLY, NO-TIE, LOC-GATE, LOC-K2 (every state of a run of IDEAL-CYC(G), every genome), [OPT].
  - R126 QUIET-N (every genome), the Ξ-feedback number, GATE-CLASS (quoted, not used).
  - The readings (D1) e_g's only in-edge is from g, (D3) the core is entered only at u = K0, (D4) c_X has no in-edge: checked against
    R104's text by my predecessor for P-N5-QN (R-P-N5-QN §1) and again here on the builder (every edge list).
- Every premise is used inside its scope: all statements are about states of one IDEAL-CYC run of one genome, or about positional pairs
  of Γ(G) (CN2 in (P7)).

## 2. The class facts (K1)-(K5): re-derived, no gap found
- (K2) is the hinge. Two triples with the same Λ and different E: the top z of Π Δ Π′ is at least as relevant as the top z_E of E Δ E′, so
  by E-DOM z is an e-vertex, c_W, K0 or K3. c_W is in no Π. For a non-core vertex, K0 and K3 are in Π iff Λ = K1 (the core is entered
  only at K0 and then runs K0 → K3 → K2 → K1 by the freeze and LOC-K2), so they cancel at equal Λ. So z = z_E, even, and the VJ order
  agrees with the lex order on E. Different Λ: the reward decides both orders. So class is a weakly monotone function of the value.
  - Note N-a (wording, optional): (K5) applies (K2) to the triple ext(x, Ω_t(y)), which is not a vertex's value. (K2)'s proof uses only
    (Λ, Π), and ext(x, ·) leaves both unchanged (x has priority 0, CN2), so it applies; say «triples whose (Λ, Π) are those of a
    non-core vertex».
- (K1): from R118 (e)'s reason and E-MON, as written. (It also follows from F1 and (K2) alone.)
- (K3): (a) one play, one cycle. (b) an e-vertex on a cycle would make Λ at least as relevant as an e-vertex, against B-ONLY (its
  successor is then not c_W). (c) for a non-e vertex the path loses only v itself; at v = Λ(v) both E are empty by (b). (d) B-ONLY puts
  e above Λ(e), so e ∈ Π(e), once. (e) the core, c_W, c_X and the e-vertices before c_W are constant.
- (K4): LOC-GATE with NO-TIE, then (K2) on the two faces (non-core), then (K3 (c)).
- (K5): DOM, then (K2) (note N-a).
- Counted directly by my replay (§6): k1, k2 (pairs of non-core vertices at one state, and one vertex at t and t + 1), k3a, k3c, k3d,
  k3e, k4, k5: all 0.

## 3. Lemma LEVEL: re-derived, no gap found
Reference b; LAG_t, m_t, FRONT_t, Φ_t, stall as the document defines them.
- (L1) uses (K1) only: LAG shrinks, m does not fall, at equal m the front shrinks; a stall keeps the whole front lagging at class m, so
  Φ is unchanged; a non-stall step raises some front vertex, so m rises or the front loses it. Correct.
- (L2): constants never lag; an e-vertex e with mover successor w has class_t(e) = (Λ_t(w), {e} ∪ E_t(w)), a function of class_t(w): if
  w does not lag, neither does e; if w lags, w has a strictly lower lagging class than e. Correct.
- (L3): along a play the class does not rise ((K3 (c), (d))), so from a front vertex every vertex of the play is non-lagging or in the
  front. If the whole cycle lags it is a cycle of movers, gates and β-vertices (no e by (K3 (b)), no core vertex, no c_X) with class
  (c, ∅): case (β). Else some lagging z has a non-lagging successor y; z is not a gate ((K4) at b: class_b(z) ≤ class_b(y) =
  class_t(y) = class_t(z)), not a β-vertex (same successor at t and b), not an e-vertex (L2): z is a mover and m_t = class_b(σ_t(z)):
  case (α). Correct.
- (L4), the step the Lead asked about. At a stall define s on FRONT_t:
  - a mover z ↦ w := σ_b(z): class_b(w) = class_b(z) > m_t ((K3 (c)) at b; z lags); class_t(w) ≤ class_(t+1)(z) (K5) = class_t(z) = m_t
    (the stall). So w lags, hence class_t(w) ≥ m_t, hence = m_t: w ∈ FRONT_t. This is the only place the stall is used.
  - a gate g ↦ r := σ̄_t(g): class_t(r) = m_t; if r did not lag, (K4) at b would give class_b(g) ≤ class_b(r) = m_t, so g would not
    lag; so r ∈ FRONT_t, and r ≠ e_g by (L2): r = β_g.
  - a β-vertex ↦ its frozen mover successor y: same class at t and at b, so y ∈ FRONT_t.
  s maps the finite set FRONT_t into itself, so it has a cycle, of the form mover x → gate (x, σ_b(x)) → β-face → mover xt(x, σ_b(x)).
  That is a cycle of Ξ_(σ_b), all of it lagging at class m_t. Each inclusion was re-derived; I found no case missing (a front vertex is
  a mover, a gate or a β with mover successor, by (L2)). Correct.
- (L5): m_t is class_b of one of the M gates or (c, ∅) for one of the M β-vertices; 1 ≤ |FRONT_t| ≤ N + 2M. Correct.
- Counted by my replay with reference b = T and two random reference states per genome: l1 (incl. (C2): exactly q non-stall steps
  before b′), l2, l3, l3v (the VALUE of m_t in both cases, for every witness), l4 (the map s, vertex by vertex), l5: all 0.

## 4. Counting, WIN, R-INT, R-HEIGHT, K1-TCYC, FVS-TCYC: no gap found
- (C1)-(C4): Φ takes each value on one interval; the steps inside an interval are stalls, the steps between intervals are not; after the
  first state b′ with LAG = ∅ no class changes, so those steps are quiet and number at most N by landed QUIET-N. Correct.
- WIN: the vertices of S never lag (their classes are constant on [a, b]); a stall or a case-(β) cycle would be a Ξ-cycle all of whose
  movers lag; S meets it. So b′ − a = q ≤ M(N + 2M) and b − b′ ≤ N. Correct.
- R-INT (k = 1) is WIN with S = {R}. R-HEIGHT: a stall has a Ξ-cycle inside the front, R is on it, and front vertices keep their class
  at a stall; so every change of class(R) is one of the q ≤ P non-stall steps (reference T). K1-TCYC: on a plateau R is in the front and
  keeps its class, so WIN bounds the plateau by A. Correct.
- FVS-TCYC: the recursion w_j ≤ P(w_(j+1) + 1) + N and its solution (P + N)(P + 1)^(k−j) were re-computed (w_k ≤ A ≤ P + N). Correct.
- Arithmetic of the examples re-computed: CW16_n (N 171, M 472): P(A + 1) + N = 554,122,317,291; MW32_2 (N 300, M 657): P = 2,120,796;
  CWRR16_n (N 171, M 487): M(N + 2M) = 557,615. All as printed.
- Counted by my replay: w_stall, w_beta, w_len, w_quiet (every maximal interval of constant classes of S; S = every single feedback vertex
  at k = 1, up to six of them; a minimum pair at k = 2 for N ≤ 80; else a greedy feedback set; S = ∅ at k = 0) and w1..w5 (LEVEL inside
  the interval); rh (R-HEIGHT): all 0.

## 5. Addendum A
### 5.1 (P1)-(P5): no gap found
- (P1): a vertex of Y either lags at u, and is then in the front (class m on the whole plateau), or has its class of state b already.
  A vertex outside Y stays above m by (K1).
- (P2), (P3): classes do not rise along plays; (K5) with (P1) puts every gate of a mover of Y at or below the mover's class, so in Y.
- (P4), each case re-derived: other face outside Y — it stays above m, never chosen (K4). Both in Y with different classes — the chosen
  one is the lower, by LOC-GATE, NO-TIE and (K2), at every state. Equal classes — e_g ∈ E(e_g) = E(β_g), so β_g's play passes e_g, whose
  only in-edge is from g (D1): σ̄(g) = e_g at every state. (An e-vertex of Y has a mover successor: (c_W, ∅) is above every lagging
  class.) K2 by LOC-K2. Correct. The equal-class case is where the genome is used (§7).
- (P5): on [u, v] the plays from Y stay in Y and use H's edges, so Ω_s on Y is H's value under σ_s|Y, and the step at a mover of Y
  compares its gates, all in Y. Counted by my replay with my own VJ engine run on H itself: p5v (values), p5h (each step u ≤ s ≤ v
  legal for H on H's own values): 0.
### 5.2 (P6): GAP G-P6 (exact, small)
- Text (l. 455-456): «(ii) Ω_(s′+1) = Ω_(s′) on Y: Odd may answer σ_(s′+1) by σ̄_(s′) on the gates of Y; then the play from x ∈ Y is the
  play of state s′ (it stays in Y, where σ is unchanged), so by [OPT] Ω_(s′+1)(x) ⊴ Ω_(s′)(x)».
- The induction runs over s ≤ s′ ≤ b, beyond the plateau. For s′ > v nothing proved says that the play of state s′ from a vertex of Y
  stays in Y: (P2) and (P4) are statements about the states u, …, v. The induction hypothesis carries σ_(s′) on Y's movers and Ω_(s′)
  on Y, not σ̄_(s′).
- Repair (one line; I checked it): answer with the PLATEAU state's choice. «Odd may answer σ_(s′+1) by σ̄_s on the Odd vertices of Y. By
  (P2) at state s the play from x ∈ Y under (σ_s, σ̄_s) stays in Y, and σ_(s′+1) = σ_s on the movers of Y, so the play under
  (σ_(s′+1), σ̄_s) is that play, of value Ω_s(x) = Ω_(s′)(x). By [OPT] Ω_(s′+1)(x) ⊴ Ω_(s′)(x); by F1 ⊵.»
  (Alternative: add «σ̄_(s′) = σ̄_s on the Odd vertices of Y» to the induction; it follows from Ω_(s′) = Ω_s on Y, F1 at the other face,
  NO-TIE and LOC-GATE.)
- With the repair (P6) is correct: a step inside the plateau that switches no mover of Y would freeze Y's values up to b, so the front
  would not lag. My replay counts p6 (a step s → s + 1, u ≤ s ≤ v, switching no mover of Y): 0.
### 5.3 (P7) and the Lean theorems
- As written: v − u consecutive p-steps of H's Howard run; H0 by CN2; landed R118 (i) BR-SEG-G (a), stated for any parity game, gives
  v − u ≤ n_E(H). H is a parity game (every vertex of Y has a successor in Y), its Howard step is «every Even vertex», and the Even
  vertices other than movers have one successor, so their step is trivial. Correct.
- Lean (claude/l-formal 4b376da4, ancestor of origin/claude/l-formal; Corollaries.lean sha1 c8f5b435…: l. 52 `theorem brseg :
  BrSegStatement V`, l. 82 `theorem brsegG_noH0`, l. 108 `theorem brsegG : BrSegGStatement V`; Defs.lean b41c937c… and Statements.lean
  aaa3c0c2… are byte-identical to 9dde1527, which R-restrictC-preread §3 compared). The sub-game H against `brsegG`'s hypotheses:
  | Lean hypothesis | in H |
  | --- | --- |
  | `Function.Injective pr` | bridge B-1: pr := SPEC's p′ (2·rank + parity) restricted to Y |
  | Howard at every x ∈ V0, t ∈ [a, a + r) (`HowardAt`) | V0 := the Even vertices of Y; movers by (P5); the others have one successor |
  | F1 pointwise | bridge B-2: landed R15 (a) / R118 (b) F1, on Y's values, which are H's values (P5) |
  | `lam` constant on a, …, a + r | (P1) |
  | τ constant off V0 | Odd has one successor in H |
  | H0: some x ∈ V0 switches, not a cycle node before or after | (P6) with G-P6 repaired; CN2 |
  | conclusion r ≤ V0.card | v − u ≤ n_E(H) ≤ N + 2M + 5 |
  So H meets exactly those hypotheses. `brsegG_noH0` needs only «some x ∈ V0 switches» (P6). `brseg` with Mov := the movers of Y
  (non-movers frozen, the last step v − 1 → v switches a mover) gives the sharper v − u ≤ |movers of Y| ≤ N (note N-b, optional;
  my replay counts it as p7s: 0, and it is attained on tiny genomes).
- Own build (a referee's build, not CHECKER's exact-commit run): `git archive 4b376da4 lean/lemmas` into the scratchpad; Lean v4.35.0 by elan,
  Mathlib cache at the pinned commit 56a00585…; `lake build`: «Build completed successfully (3149 jobs).»; `grep -rnw --include=*.lean -e
  sorry -e admit -e axiom . --exclude-dir=.lake`: no output; `lake env lean Axioms.lean`: `PG.brseg`, `PG.brsegG`, `PG.brsegG_noH0` and
  `PG.lam_gap_sharp` each «depends on axioms: [propext, Classical.choice, Quot.sound]» (box208_logs/lean_build_tail.out, lean_grep.out,
  lean_axioms.out).
### 5.4 ALL-TCYC
- b′ = q + Σ_i (v_i − u_i) ≤ P + P(N + 2M + 5), T − b′ ≤ N. Arithmetic correct. With note N-b: T_CYC ≤ P(N + 1) + N.

## 6. Replay with my own code (scratch/box208_replay.py; logs scratch/box208_logs/)
- Engine: my lane's xicyc_replay.howard (own Γ(G) builder from R104's text, own VJ valuation and best reply, IDEAL-CYC Howard; tie rule:
  keep if best, else the larger index). Counters: mine, written from the document's statements (header of the script), not the lane's
  level208.py / plat208.py, which I did not open. Classes compared by (reward(Λ), e-ranks in decreasing order).
- 36 must-be-0 counters: k1, k2, k3a, k3c, k3d, k3e, k4, k5; l1, l2, l3, l3v, l4, l5, c4 (reference T and two random references);
  w1, w2, w3, w3v, w4, w5, w_stall, w_beta, w_len, w_quiet; rh; p1, p2, p3, p4, p5v, p5h, p6, p7, p7s; tb (T against ALL-TCYC's bound).
- Results (every set: all 36 counters 0):
  | set | genomes | states | max T | stalls (ref. T) / with another class changing | plateaus checked (3 refs) / longest | controls c_k4, c_k5, ch1-ch5, c_S, c_Y |
  | --- | --- | --- | --- | --- | --- | --- |
  | 25 frozen k = 1 records (run208.sh's list) | 25 | 1,036 | 114 | 31 / 0 | 32 / 9 | all fire |
  | 53 corpus genomes (box202/inst) | 53 | 1,699 | 199 | 48 / 23 | 35 / 13 | all fire |
  | own families rand, deep, wide, selfl × 400, seed 3209 | 1,600 | 4,575 | 9 | 132 / 1 | 230 / 3 | all fire |
  | own family acyc × 400, seed 3209 (k = 0) | 400 | 828 | 4 | 0 / 0 | 0 | c_k4 only (nothing lags behind a cycle) |
  | tiny × 20,000, seed 3211 (N ≤ 4) | 20,000 | 34,892 | 6 | 584 / 1 | 1,072 / 2 | all fire |
  | noX × 3,000, seed 3212 (every Ξ-target a mover) | 3,000 | 7,397 | 11 | 169 / 1 | 299 / 3 | all fire |
  | big × 1,500, seed 3213 (4-10 levels, upward Ξ-edges) | 1,500 | 9,134 | 14 | 301 / 1 | 412 / 5 | all fire |
  | 150 mutants of each of 8 frozen genomes, seed 3210 | 1,200 | 29,843 | 33 | 3,505 / 358 | 3,007 / 25 | all fire |
- Adversarial climbs (scratch/box208_climb.py: hill-climb by my own mutations, every counter run on every genome visited; a failing
  genome would be saved): objective T from family rand (seed 41): 9,006 genomes, best T 14; stalls from noX (42): 9,006, best 4; longest
  plateau from big (43): 9,006, best 10; T from tiny (44): 20,010, best 4. Sum of the 36 counters over all 47,028 genomes visited: 0.
  The climbs are weak (the mutations keep N and M), so they widen the sample; they are not an attack of L-RED's strength.
- Instances from `git archive 8db300fe`; `sha1sum -c SHA1SUMS`: box202/inst 53 OK (its 54th line names k1fail_202.json, which lies one
  directory up), box203 10, box204 2, box205 1, box206 14, box207 2 OK.
- Run lengths: my T equals the lane's T (out/level208_records.out, level208_corpus.out at 8db300fe) on all 25 + 53 genomes.
- Both cases of (L3) occur (records n_alpha / n_beta, states with a witness of each, three references): corpus 3,548 / 67; noX
  1,473 / 6,960 (cases_corpus.out, cases_noX.out; their must-be-0 lines equal the first runs').
- Controls: c_k4 (max in place of min in (K4)); c_k5 ((K5) without the time shift); ch1-ch5 (FRONT := the HIGHEST lagging class:
  (L1), (L2), (L3), (L4), (L5) all break); c_S (WIN with S = ∅ on a genome with a Ξ-cycle: stalls appear, 31 on the records, 48 on
  the corpus); c_Y (PLATEAU with Y := the front alone: not closed under plays).
- Limits, stated plainly:
  - No run comes near a constant: the most Φ values is 199 (P = 2,120,796 there); the longest plateau has 25 steps. The data test the
    steps of the proof state by state, not the bound.
  - Exact Howard ties are rare in these runs, so «any tie resolution» rests on the proof (no step uses the tie rule), not on data.
  - One engine (mine) under my counters, plus the lane's two engines under its counters: three engines, two counter codes. Large zero
    counts are DATA, not evidence of the theorem.

## 7. The genome-only steps (what must fail on Friedmann's G_N)
An argument of this shape cannot hold for Howard on every parity game: R118's line records Howard on Friedmann's switchallexp with C = 0
and R = 4, 10, 24, 54, 116, 241 flip steps for N = 2, …, 7. The steps that use a fact true only of Γ(G):
- G-1, (K2) and (K3 (b), (d)), from B-ONLY (R123) and E-DOM ([DEF]): the part of Π that can decide an order above the β-level consists of
  e-vertices only, all EVEN, never on a cycle, and K0 / K3 are a function of Λ. This makes class a monotone image of the value that is
  constant along a play except at an e-vertex, where it rises: «non-negative weights». In a game with odd-priority vertices in that
  part of Π, the class would fall along plays and (L3)'s first sentence fails. The safe choice there is class := Λ (then (K1)-(K4)
  are F1 and Odd's local optimality; my reading), but then:
- G-2, WIN (iii) = landed QUIET-N (R126, from GATE-CLASS), and PLATEAU (P4): Odd does not move while the classes of a gate's faces stand
  still. (P4)'s equal-class case is decided by (D1) «e_g's only in-edge is from g». On switchallexp every Λ is constant (C = 0), so with
  class := Λ the whole run is one quiet window and one plateau, and its 241 flips at N = 7 are exactly Odd moving inside it.
- G-3, (K5), from DOM (R118 (c)): movers have priority 0 and are never cycle nodes (CN2, F6). DOM is false on general games (R118 (i)'s
  note).
- G-4, (L2) / (L4): the only Odd vertices with a choice are gates with two faces (and K2, constant); a front gate's face is its β-face.
So (my reading, not a checked statement) LEVEL's count of non-stall steps would survive with class := Λ in any game where DOM holds,
and it says nothing there (no step is a non-stall step when C = 0); the exponential lives in the plateaus, where the genome facts G-2
enter.

## 8. TARGET.md diff and scope
- The box claims no algorithm, no M3, no M4; its scope line is «IDEAL-CYC on Γ(G) only; not Γ3, not N5′-xi, not M4; G-N5-TIME stays
  OPEN». Correct as a scope: IDEAL-CYC is a model (R118 (a)); the genome games are a restricted family (TARGET.md §4).
- If ALL-TCYC stands it would close R118's «no bound on R is claimed (OPEN)» for IDEAL-CYC only. It does not transfer to Γ3 by itself:
  R118's DATA records Γ3 runs that differ from the IDEAL-CYC run at exact VJ ties, and R125's DEAD RUN-TRANSFER has T3 ≠ T_CYC on RT_n1.
  A Γ3 form is a separate statement with R125's lemmas (not written, as the box says).

## 9. For a packet (what I would test a frozen text against)
- PR-1 (required): G-P6's repair in (P6).
- PR-2 (required): (P7) cites exactly one of: landed R118 (i) BR-SEG-G (a) with H0 checked, or the Lean theorem by name and commit after
  CHECKER; and says that H's Howard step is the step at every Even vertex of H.
- PR-3 (required): premises by R-id as §1 lists them, with the readings (D1), (D3), (D4) cited from R126's packet; no lane lemma
  (Lemma PAID, R-LOCAL, LOUD-SPLIT are not used: confirmed, none appears in a proof).
- PR-4 (required): the DATA clauses say that no run tests the constants, with units as the tools compute them.
- PR-5 (optional): notes N-a ((K2) for triples), N-b (plateau ≤ N by BR-SEG's own form).
- PR-6 (the Lead's call): body and Addendum A as one packet or two. Addendum A makes §6 a corollary with worse constants; WIN, R-INT and
  R-HEIGHT keep their own content.

## 10. Tools and outputs (docs/referee/scratch/)
box208_quotes.py, box208_replay.py; box208_logs/: quotes.out, replay_records.out, replay_corpus.out, replay_gen_{rand,deep,wide,acyc,
selfl,tiny,noX,big}.out, replay_mut.out, cases_corpus.out, cases_noX.out, climb_*.out, climb_best_*.json, lean_build_tail.out, lean_grep.out,
lean_axioms.out; box208_climb.py.
