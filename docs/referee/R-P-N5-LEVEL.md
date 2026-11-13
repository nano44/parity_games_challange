# R-P-N5-LEVEL: first referee report on packet P-N5-LEVEL (L-NEW successors 72-73; box 208 + Addenda A, B)
REFEREE successor 34 (D1; the Lead's «go» 20:04Z, item B). Date -u at writing of §1-§2: 2026-11-12T21:05Z. Written section by section;
§0 (verdicts) comes last. This is a SIGNATURE review of the frozen packet, separate from my lane's pre-reads.
- Prior work of this lane, disclosed: R-box208-preread.md (successor 32, claude/referee 7524342b; gap G-P6 and its repair, which the
  packet uses as PR-1 and credits under L41) and R-box209-preread.md (successor 33; box 209 is NOT in this packet). I re-derived every
  proof below from the frozen text, not from those reports. The packet's step «Odd answers σ_(s′+1) by σ̄_s» originates in this lane
  (REFEREE 32): I checked it afresh in §2.5 as a step of the frozen text.
- Not read before my verdict: docs/referee-2/ on P-N5-LEVEL; L-RED 66 R235, L-RED-B B1, L-COMP 19 BOX 43 records beyond the one item
  the packet cites as DATA (BOX 43 README item 1 (b), opened only to check that DATA clause, §4).

## 1. Objects and premises
### 1.1 Objects (measured with git, not copied)
- Packet: claude/l-new 1e6df4990efeb31dd3800a543b61f721b209f80a (an ancestor of origin/claude/l-new 069c888b, checked);
  docs/new/P-N5-LEVEL.md sha1 7c956df443cfddbf23bfbaa18a26a98369b176ec, 65,874 B, 575 lines.
- Proposed line: docs/new/P-N5-LEVEL-line-L1.txt at 1e6df499, sha1 28565b3c60fe8167f4b660c83fa27c00cd7b4fe9, 7,239 B, one line, 0 «|»,
  84 «(» = 84 «)».
- Pins: experiments/new/box211/level.pins at 1e6df499: 101 non-DOCS pins, every one equal (sha1 of each file in `git archive 1e6df499
  experiments/new experiments/si experiments/harness`; 0 absent, 0 different). The five DOCS pins are the packet, its source note, L-1
  and the two landed packet files of §1.2.
- Landed record used: trunk 68c8d293 (the packet's pinned trunk) and current trunk 7fa6aff4; RESULTS.md's last entry is R127 at both.

### 1.2 Landed premises, quoted by my own script
- scratch/level_quotes.py (mine; not the lane's quotes211.py): every outermost «…» of every bullet carrying a mark [Q X] is looked up in
  the source X names (an R-id: that entry of docs/RESULTS.md; P-N5-QN / P-N5-XICYC: the packet file; TARGET: TARGET.md), whitespace
  normalised. Logs level_logs/quotes_68c8d293.out and quotes_7fa6aff4.out: **25 bullets, 44 quotes, 44 found in the tagged source,
  0 missing**, at both trunks. docs/new/P-N5-QN.md sha1 97254bd2… and docs/new/P-N5-XICYC.md sha1 149e2414… at both trunks, equal to the
  packet's pins.
- Scopes read in the landed entries themselves (RESULTS.md at 68c8d293):
  - R118 (c) DOM: «[IDEAL-CYC, every genome]»; (e)'s reason: Λ moves only to strictly larger reward; (i) BR-SEG-G: «[any parity game,
    Howard from any σ_0, under H0]», proof of record STRICT-G and PATH-G («No DOM is used in §5 or §6.»).
  - R121: premises R104 [DEF], R118 (a), (b), (e); HYPOTHESIS [E-LEV] «only for §6 UP-JUMP, UP-B and NOUP»; E-MON is not under it.
  - R123: «for every genome G»: CN2 (every positional pair), B-ONLY, NO-TIE, LOC-GATE, LOC-K2; [OPT] in its premise clause.
  - R126 QUIET-N: in the entry's scope «for every genome G (Ξ-cycles and Ξ self-loops allowed)», «every maximal window of quiet steps
    has at most N steps»; the Ξ-feedback number defined there. No hypothesis is attached to QUIET-N ([E-LEV] is for GATE-FLIP (b) only).
- So every premise of «To sign» is a landed R-id item with a scope covering every genome's IDEAL-CYC run (BR-SEG-G: every parity game),
  except the readings, §1.3.

### 1.3 The readings (D1), (D3), (D4)
- They are quoted from the packet FILE landed as R126 (P-N5-QN.md §1), not from R126's RESULTS line (which names «RESULTS R104's
  definitions of the genome and of Γ(G) only, including that the Odd vertices with a choice are the gates and K2» and none of D1-D4).
  I re-derived each from R104's own line, which lists every vertex with its out-edges: movers → their gates; gate → {e, β}; β → {Ξ-target,
  u} or {u}; e → {W-target} or {c_W}; c_X «an unused even self-loop»; c_W self-loop; core K0 → {K1, K3}, K1 → {K0, K1}, K2 → {K1, K2},
  K3 → {K1, K2}. (D1): the only edge into e_g is from g (no other vertex lists an e-vertex as a successor). (D3): the only edges from
  outside the core into it are β → u = K0. (D4): no vertex other than c_X lists c_X. All three hold. Γ(G) for Ξ-cyclic genomes is R118
  (a)'s IDEAL-CYC(G) («ANY genome G (Ξ-cycles allowed)») with the same vertex and edge lists. FINDING: none (premise status: R104 [DEF]).

## 2. Proofs, each step re-derived from the frozen text
### 2.1 Class facts (K1)-(K5): CORRECT, no gap
- (K1): R118 (e)'s reason (Λ only to strictly larger reward) and E-MON (E does not fall while Λ is fixed). Correct.
- (K2), on triples (PR-5 N-a applied): Λ ≠ Λ′ gives (VJ-1) and c < c′. Λ = Λ′, E ≠ E′: z (top of Π Δ Π′) is at least as relevant as
  z_E (top of E Δ E′ ⊆ Π Δ Π′); if z ≠ z_E then by E-DOM z ∈ {e-vertex, c_W, K0, K3}; not an e-vertex (it would be in E Δ E′ above
  z_E); not c_W (a cycle node, in no Π); not K0, K3 (with Λ = Λ′ both plays enter the core, at K0 by (D3), and then K0, K3 ∈ both Π,
  or neither does). So z = z_E, even; Θ ◁ Θ′ and (VJ-2) put z ∈ Π′: E <lex E′. The hypothesis «plays of vertices outside the core» is
  what makes the K0 / K3 step valid (a core vertex's own Π is not of that form). Correct.
- (K3): (a) trivial; (b) an e-vertex on its own cycle would have Λ at least as relevant as itself, against B-ONLY (it is not excepted:
  its successor is not c_W, else it is not on a cycle); (c) Π_t(v) = Π_t(s_t(v)) ∪ ({v} if more relevant than Λ) for v ≠ Λ_t(v), and
  for v = Λ_t(v) both E-sets are empty (note N-1: Π_t(s_t(v)) is then empty, not only free of e-vertices); (d) B-ONLY puts e above
  Λ_t(e), (b) puts e off the cycle; (e) c_W, c_X loops; e → c_W: Π = ∅ since only K0, K3 are above c_W; core: K0 → K3 → K2 frozen
  (R104 start), K2 → K1 (LOC-K2), K1 loop; (c_W, ∅) largest because c_W has the largest reward among the possible cycle nodes (K0, K3
  are never cycle nodes) and Π = ∅ there. Correct.
- (K4): NO-TIE then LOC-GATE give Ω_t(a) ◁ Ω_t(b) for the chosen face a; both faces are outside the core, so (K2) gives class(a) ≤
  class(b); class(g) = class(a) by (K3 c). The added clause «the face σ̄_t(g) has that class» is exactly this. Correct.
- (K5): DOM; x has priority 0 and Λ_t(y) priority ≥ 2 (CN2), so ext adds nothing to Π and keeps Λ; (K2) for the triple ext(x, Ω_t(y))
  (the cycle node and Π-set of the play of the gate y, a vertex outside the core) and the value of x at t + 1. Correct.

### 2.2 Lemma LEVEL (L1)-(L5): CORRECT, no gap
- (L1): the bookkeeping is right; a stall at t = b − 1 is impossible (it would give class_b(v) < class_b(v)), consistent with «LAG_(t+1)
  ≠ ∅» at a stall.
- (L2): K-vertices, c_W, c_X, e → c_W and β → u never lag ((K3 c, e)); an e-vertex with a mover successor w either does not lag (w
  does not) or has class > class_t(w) ≥ m_t (it is not in FRONT). Correct.
- (L3): classes do not rise along a play ((K3 c, d, e)), so every lagging vertex of the play from v ∈ FRONT_t is in FRONT_t. The cycle is
  K1's loop, c_W's loop, or a mover / gate / β cycle (no e-vertex by (K3 b), no core vertex, no c_X by (D4)). All-lagging cycle: its
  node c is a β-vertex (CN2) and every vertex has class (c, ∅): (β). Otherwise a lagging z with a non-lagging successor y exists; z is
  not a gate ((K4) at b gives class_b(z) ≤ class_b(y) = class_t(y) = class_t(z)), not a β (frozen successor), not an e-vertex or core
  vertex (L2): z is a mover and m_t = class_b(σ_t(z)): (α). Correct.
- (L4): the map s. Mover z: class_t(σ_b(z)) ≤ class_(t+1)(z) (K5) = m_t (the stall) < class_b(z) = class_b(σ_b(z)) (K3 c at b): σ_b(z)
  lags with class m_t. Gate g: its chosen face r has class m_t; r not lagging would make g not lag ((K4) at b, (K1)); so r ∈ FRONT_t
  and r = β_g (L2). β_g: its mover successor y has class m_t at t and class_b(β_g) ≠ m_t at b. Every s-cycle passes mover → σ_b-gate →
  β-face → Ξ-target. Correct; the stall is used only in the mover case, as the packet says.
- (L5): m_t ∈ {class_b(gate)} ∪ {(c, ∅) : c a β-vertex} (2M values; M under (α) everywhere) and 1 ≤ |FRONT_t| ≤ N + 2M (L2). Correct.

### 2.3 Counting (C1)-(C4) and Theorems WIN, R-INT, R-HEIGHT, K1-TCYC, FVS-TCYC: CORRECT, no gap
- (C2): a step inside an interval of constant Φ is a stall and a step that changes Φ is not ((L1) both ways); the non-stall steps on
  [a, b′] are exactly q. (C4): LAG_(b′) = ∅ gives class_(b′) = class_b, and (K1) squeezes every class on [b′, b]; the b − b′ steps are
  quiet and lie in one maximal quiet window, so **(C4) uses landed R126 QUIET-N** (scope §1.2) for b − b′ ≤ N. Correct.
- WIN: no vertex of S lags on [a, b]; a stall before b′ would give (L4)'s all-lagging Ξ-cycle, which S meets; case (β) gives an
  all-lagging Ξ-cycle the same way (mover → chosen gate → β-face → Ξ-target is an Ξ-edge); so b′ − a = q ≤ M(N + 2M) by (C1) under (α),
  and b − b′ ≤ N by (C4). R-INT is WIN with S = {R}. R-HEIGHT: a change of class(R) at t → t + 1 puts R in LAG_t; at a stall R would
  lie on (L4)'s Ξ-cycle, inside FRONT_t, where nothing changes class; so it is one of the q ≤ P non-stall steps, and none happens after
  b′. K1-TCYC: on each plateau (C3)'s Ξ-cycle contains R, so class(R) is constant there and WIN on the plateau gives ≤ A. FVS-TCYC:
  W(S) recursion with x ∈ F_0 on the plateau's Ξ-cycle, x ∉ S (it lags, S does not), S ∪ {x} constant on the plateau; w_k ≤ A ≤ P + N;
  the induction step P(X + 1) + N ≤ X(P + 1) for X ≥ P + N. All correct; none uses §7.

### 2.4 Lemma PLATEAU (P1)-(P5): CORRECT, no gap; (P4) is used on a plateau only
- (P1): a vertex of Y either lags (then it is in J with class m throughout, (L1)) or does not (then its class is its class at b, and
  by (K1) constant from u to b); outside Y the class is > m at u and stays so. (P2): classes do not rise along a play. (P3): (K5) at
  s < v and (P1); u < v makes such an s exist.
- (P4): cases (1), (2) are (K4) with the classes frozen by (P1). Case (3): e_g → c_W would give class (c_W, ∅), which is **strictly
  above m because m is the class of a lagging vertex** (class_u(x) = m < class_b(x) ≤ (c_W, ∅)), so e_g ∉ Y; hence e_g's successor is a
  mover, e_g ∈ E_s(e_g) = E_s(β_g), the play of β_g passes e_g, enters it from g only (D1), so σ̄_s(g) = e_g at every s. Correct.
- **The Lead's check (L-FORMAL's finding).** With Y := all vertices (no plateau, no lagging class m), a gate whose two faces both have
  class (c_W, ∅) (e_g → c_W, β_g's play ending in c_W) is not settled by case (3)'s argument: both values have Λ = c_W and Π = ∅, and
  Odd's choice is decided by the third component (length). I searched the frozen text for every use of (P4) or of «σ̄ constant»: (P4)
  is used only in (P5), inside one plateau [u, v] with u < v and reference b, where m is a lagging class. (L3) and (L4) use (K4) and
  (L2), never (P4); §6 does not use §7; Odd's moves while classes stand still outside a plateau are handled by landed QUIET-N in (C4),
  not by (P4). FINDING: no step relies on (P4) outside a plateau. The §9 bullet «(P4): Odd's choice at a gate of Y is constant on a
  plateau» says the same.
- (P5): H on Y; a mover of Y keeps all its gates (P3); every other vertex of Y keeps s_u(x), constant on [u, v] by (P4), LOC-K2 and the
  freeze (c_W is never in Y: its class is the largest); H is a parity game in which only the movers of Y choose; the plays of Y under
  (σ_s, σ̄_s) stay in Y (P2) and use H's edges, so Ω_s on Y is H's value under σ_s|Y and Odd's only strategy; the IDEAL-CYC step at a
  mover of Y compares exactly H's values of its H-successors with the same keep-if-best rule. «H's Howard step is the step at EVERY Even
  vertex of H» is stated (PR-2). Note N-2: H's priorities are Γ(G)'s, not compressed to {0, …, |Y|}; R118 (i) is stated for «any parity
  game» and the VJ order (VJ-1), (VJ-2) depends only on the relevance order and parities, which H inherits; no gap.

### 2.5 (P6), (P7): CORRECT, no gap (PR-1 and PR-2 applied)
- (P6), claim for s′ ∈ [s, b] (s the step with no mover of Y switching, u ≤ s ≤ v): (A) at s′ + 1: x kept σ_s(x) at s → s + 1, so by
  R118 (a)'s rule σ_s(x) = σ_(s+1)(x) is a ⊴-largest gate under Ω_s (the rule always moves to a ⊴-largest successor); the gates of x are
  in Y with Ω_(s′) = Ω_s there (B), so x keeps it at s′ → s′ + 1. (B) at s′ + 1: Odd answers σ_(s′+1) by **σ̄_s** (a positional Odd
  strategy of the whole game); the play from x ∈ Y under (σ_s, σ̄_s) stays in Y — this is (P2) **at the plateau state s ∈ [u, v]**, the
  only state where (P2) is used — and visits only movers of Y (equal choices by (A)), frozen Even vertices and Odd vertices (σ̄_s), so
  it is the same play under (σ_(s′+1), σ̄_s), value Ω_s(x); [OPT] at s′ + 1 gives Ω_(s′+1)(x) ⊴ Ω_s(x); F1 at the run step s′ → s′ + 1
  (s′ < b ≤ T) gives ⊵ Ω_(s′)(x) = Ω_s(x). At s′ = b the vertices of J ⊆ Y have their class of state s, against J = FRONT_s. Correct.
  The G-P6 trap of my lane's pre-read («the play of state s′ stays in Y» used after the plateau) is gone: no state outside [u, v] is
  given a (P1)-(P4) property.
- (P7): the steps u → … → v change σ on Y (P6), keep every Λ on Y ((P1): Λ is part of the class) and Odd's choice (none in H): p-steps of
  a Howard run of H started at σ_u|Y (BR-SEG-G allows any σ_0 and any choice among several best non-current successors). H0 for every
  step of every Howard run of H: a step switches a vertex with a choice, a mover of Y, and a mover is never a cycle node under a
  positional pair of H, because such a pair extends to a positional pair of IDEAL-CYC(G) with the same plays from Y (non-movers of Y keep
  their IDEAL-CYC successors, which are legal for the frozen Even vertices and for Odd) and CN2 covers every positional pair. This is
  the H0 point my lane's successor 33 asked for (only movers choose in H): applied. Then R118 (i) (a): v − u ≤ n_E(H) ≤ N + 2M + 5.
  Correct. One proof of record (PR-2); the Lean theorems are named as lane-level only.

### 2.6 Theorem ALL-TCYC and its «Consequences»: CORRECT
- b = T: T ≤ q + Σ (v_i − u_i) + N ≤ P + P(N + 2M + 5) + N. R, Q and D^tot(v) − 1 each count steps of the run, so each is ≤ T_CYC.
- The arithmetic «against K1-TCYC and FVS-TCYC» (not to sign) re-done: A + 1 ≤ N + 2M + 6 iff M(N + 2M) ≤ 2M + 5 (false for M ≥ 2);
  (P + N)(P + 1) ≥ P(N + 2M + 6) + N iff P ≥ 2M + 5 (true for M ≥ 2); M = 1, N = 1: P = 6, A = 4, values 55 / 31 / 49. Correct. Note
  N-3: «N ≤ M, every mover having an option» is a property of genomes the remark uses without a quote; it is not to sign.

### 2.7 The genome-only steps (§9; READING, not to sign): named and correct
- The packet names each step where the genome's shape is used: (K2), (K3 b, d) from B-ONLY and E-DOM; (K1) from E-MON and R118 (e);
  (K4) from NO-TIE, LOC-GATE; (K5) from DOM with CN2; QUIET-N in (C4); (P4) case (3) from (D1); Odd's choices are gates and K2 ((L2),
  (L4)). This matches what my lane's pre-read listed (s32 §7, §9). It also matches the §9 DATA: on Friedmann's G_2 the failing step is
  (K2) inside (K5), at an odd vertex above an escape, which E-DOM excludes (§4, item 4).
- Note N-4: the class order's totality does not need B-ONLY (reward is a rank, injective on vertices); the packet's extra argument
  (distinct priorities of the possible cycle nodes) is what makes the tools' «reward = priority of Λ» a faithful encoding. No gap.

## 3. Replay with my lane's own code (no lane code; written from box 208's statements, which the packet's statements equal or weaken)
- Tool: scratch/box208_replay.py (my lane, successor 32; own Γ(G) builder and IDEAL-CYC Howard run xicyc_replay.howard, own VJ engine
  xicyc_vj, generator end_replay.gen; 36 must-be-0 counters k1 … tb, units in its header; controls c_k4, c_k5, ch1-ch5, c_S, c_Y). It
  tests (K2) on pairs of values (the packet's triple form is used only in (K5), whose counter k5 is the conclusion) and the (P5) / (P7)
  objects with H built and valued on its own (p5v, p5h). Re-run by me now, new seeds (driver scratch/box208_logs/s34_run.sh; logs
  box208_logs/s34_*.out):
  | set | genomes | 36 must-be-0 counters | descriptive |
  | --- | --- | --- | --- |
  | gen rand 3410 / deep 3410 / wide 3410 / acyc 3410 / selfl 3410 | 5 × 2,000 | all 0 | max T 8 / 9 / 7 / 4 / 9 |
  | gen rand 3401 | 300 | all 0 | max T 7 |
  | files: the packet's frozen genomes (box202-207 inst, the three DEAD_SEG2P of R118 (m); from `git archive 1e6df499`) | 82 | all 0 | max T 199, max Φ values 199, plateaus 75 (longest 13) |
  | mut 3420 (≤ 6 mutations) of MWR4_2 and CW4_n (the two bases of the longest plateaus in §11) | 600 | all 0 | max T 33, plateaus 75 (longest 27) |
  Controls fire on every set with stalls (c_k4, c_k5, ch1-ch5, c_S, c_Y > 0; ch3v 0 as designed). Runtime 2 min 33 s in all.
- What this does and does not show: DATA, short runs (T ≤ 199); it tests every step of the proofs state by state on these runs and not
  the constants. A plateau of 27 steps among my mutants is one step longer than the packet's «no plateau longer than 26 steps» for the
  lane's sets; it is far below N + 2M + 5 there and changes nothing (that clause is about the lane's sets).

## 4. DATA rule (L43; «every DATA clause names its counter»), clause by clause, against the frozen outputs (scratch/level_data.py, mine; log level_logs/data.out)
1. §11 level208.py: the 16 counters are named with units in the tool's header (pinned 40828775…) and in §11. My parser: sum 0 on
   level208_records (25), level208_corpus (53), the seven random sets (2,000 + 6 × 500 = 5,000), the eight mut208 sets (8 × 250 = 2,000),
   own208_records / own208_corpus (25 / 53; T equal to the first engine's on 78 of 78, my comparison); the g3 sets 0 (DATA, Γ3, not
   claimed). Controls: level208_ctrl1 fires winstall 7, 1 (2 of 4 genomes), ctrl1_rand winstall + wbeta 50, ctrl2 198. MEETS.
2. §11 plat208.py: p1, pclos, p2, p3, p4, p5 named with units; sum 0 on records 25, corpus 53, rand 6 × 600 = 3,600, mut 2 × 600 =
   1,200 (my parser reads the «genomes» / «samples» fields); control fires (pclos 210, p5 1). MEETS.
3. §11 rv208.py: «49 must-0 counters» named in rv208.py's header (pinned 7916cdf0…; I counted 49 names); the output prints a counter
   only when it is not 0, and no VIOLATION line. My parser: no must-0 name with a non-zero value in rv208_frozen (81), rv208_mut (480),
   rv208_rand (3,300); the control prints 13 of them non-zero. MEETS in the packet; in the line the 49 names are given by reference to
   the tool only (LO-1, optional).
4. §9 G_N: counter k5 with its unit and set, cited from L-COMP 19 BOX 43 (claude/l-comp a6cce717, README.md sha1 db74c155…, equal to the
   packet's pin prefix). I opened that README's item 1 (b): G_1 «none: all 23 are 0», G_2 k5 = 38, «N = 2, step 5 → 6: (K5) fails at the
   mover g2 and its successor f2», run lengths 8 … 2,294, q 3 … 80, longest plateau 2 … 574: as the packet says. In the packet MEETS; in
   the line the counter is called «the counter of (K5)», without its name or file (LT-2).
5. «No run tests the constants» (§11 head; PR-4): my parser gives most Φ values **199 on MW32_2** (level208_corpus.out; N 300, M 657,
   P = 2·657·(300 + 1,314) = **2,120,796**) and longest plateau **26** (level208.py platmax on mut208_MWR4_2_s2086.out; rv208.py platmax
   on the CW4_n rows of rv208_mut_s2094.out); plat208's maxlen is at most 25. The packet's §11 says so with the instance; **the line's
   clause names no instance, tool, unit or file** («at most 199 values of Φ in a run, where P = 2,120,796, and no plateau longer than 26
   steps»). Landed R127's line gives the form for the same kind of clause («every run is short (T3 ≤ 199; unit: states of the HOW3 run,
   max over the 28 frozen instances, split199.out T3; 199 on MW32_2)»). REQUIRED: LT-1.
6. Independent replays: «every fail counter 0, their counters in their own outputs, cited, not re-run» — the landed form of R126 / R127
   («… in their own pinned outputs, cited, not re-run»). MEETS (precedent); nothing asked.
7. Every other number in the line is a count of genomes / runs of the sets above; each checked in items 1-3.

## 5. Line L-1 against «To sign»
- Statements: each clause of L-1 is the packet's statement or a weaker summary of it, with the same quantifiers and scope: (K1)-(K5)
  (K3 without (b), (e); K4 without the face clause), LEVEL ((L1), (L4) without σ̄_t(g_i) = β_(g_i), (L5) without the (α) refinement; (L2),
  (L3) omitted), WIN, R-INT (without the loud-prefix clause), R-HEIGHT, K1-TCYC, FVS-TCYC, PLATEAU, ALL-TCYC. Nothing in L-1 says more
  than a signed statement. The «Consequences» bullet of ALL-TCYC (a «To sign» row) is not in L-1 (LO-2, optional: without it the landed
  line does not record the bound on R118's R or on D^tot, which the packet's §13 names as what a signed ALL-TCYC would change).
- Premise sentence: matches «To sign» and §1; the claim «the class facts, LEVEL, WIN, R-INT, R-HEIGHT, K1-TCYC and FVS-TCYC use neither
  PLATEAU nor F1, [OPT], (D1) or BR-SEG-G» is true of the packet's proofs (F1 and [OPT] are used only in (P6); (D1) only in (P4); landed
  lemmas carry their own premises).
- Scope tail: «Howard all-switch with Even, the maximiser, improving, switch-best with keep-if-best», «single-switch rules and other
  rules are not covered», the genome-only steps named, «nothing is proved on Γ3, for N5′-xi, for N5 or for other games», not M4 / M3,
  not a step-4 pass, G-N5-TIME OPEN: both Lead caveats (ALL-SWITCH only; MAXIMISER improves) are in the statement. L41 credit for the
  (P6) step to REFEREE 32 with L-RED-B's independent G-1: present.
- REQUIRED (strings; each old string occurs exactly once in L-1, checked by scratch/level_l1fix.py; apply in this order; log
  level_logs/l1fix.out):
  - LT-1 (L43, §4 item 5): «no run tests the constants: at most 199 values of Φ in a run, where P = 2,120,796, and no plateau longer
    than 26 steps» → «no run tests the constants: at most 199 values of Φ in a run (unit: values of Φ with reference b = T;
    level208.py's phivals, largest over the level208.py sets above; 199 on MW32_2, out/level208_corpus.out, where P = 2,120,796) and no
    plateau longer than 26 steps (unit: steps; level208.py's platmax and rv208.py's platmax, largest over the sets above; 26 on mutants
    of MWR4_2, out/mut208_MWR4_2_s2086.out, and of CW4_n, out/rv208_mut_s2094.out)»
  - LT-2 (L43, §4 item 4): «the counter of (K5) is 0 on G_1 and first fires on G_2 at the step 5 → 6» → «L-COMP's counter k5 of (K5)
    (experiments/comp/box43/README.md item 1 (b), column k5) is 0 on G_1 and first fires on G_2 at the step 5 → 6»
  - LT-3 (Lean citation form, §7): «L-FORMAL's lane-level Lean theorems Genome.k1, Genome.k2, Genome.k3, Genome.k5, level_count, plateau
    and brsegG (claude/l-formal f74d38a4)» → «L-FORMAL's theorems PG.Genome.k1, PG.Genome.k2, PG.Genome.k3, PG.Genome.k5,
    PG.level_count, PG.plateau and PG.brsegG, Lean-checked (lane) on L-FORMAL's transcription, not through CHECKER (claude/l-formal
    f74d38a4)»
  - Whitespace: each string is one line; one space wherever this file wraps a line inside a string. Result of my script on L-1:
    sha1 **389645a2a646522a8fb57f05dba4458695ac74f2**, 7,706 B, one line, 0 «|», 89 «(» = 89 «)». A lane-built L-2 by script may
    differ from it only by the lane's own optional changes, which then need a byte test.
- OPTIONAL (the Lead's call): LO-1, after «the 49 must-0 counters of rv208.py»: add «(named in its header; a counter that is 0 is not
  printed)». LO-2: add ALL-TCYC's «Consequences» (R, Q and D^tot(v) − 1 are at most P(N + 2M + 6) + N) to the ALL-TCYC clause.
- Verdict on L-1: **does NOT match yet**: LT-1..LT-3 required; no statement changes.

## 6. TARGET.md diff: CLEAN
- The packet's [Q TARGET] quotes (§2 M4; §4's first bullet) occur verbatim in TARGET.md (§1.2). No statement is about W_E / W_O or an
  algorithm for parity games; every statement is a count of steps of one improvement rule on IDEAL-CYC(G) for genomes. TARGET.md §4
  («Polynomial only on a restricted class …») applies; not M4, not presented as M3 (§7e's novelty check not done, as the packet says),
  not a step-4 pass, G-N5-TIME OPEN. The line's TARGET sentence says the same. Nothing to change.

## 7. Lean citations
- The packet cites Lean only as lane-level and never as a premise: §3 (Genome.k1, k2, k3, k5), §4 (level_count), §7 (brsegG, plateau),
  each «Lean-checked (lane)» with claude/l-formal f74d38a4, and the INDEX's «K4Statement … NOT PROVED» is reported. I checked at f74d38a4
  (`git grep`): theorem k1, k5 (GenomeK15.lean, namespace PG.Genome), k2 (GenomeK2.lean), k3 (GenomeK3.lean), level_count
  (LevelCount.lean), plateau (Plateau.lean), brsegG (Corollaries.lean l. 108); INDEX.md l. 42 «K4Statement (GenomeClass) | NOT PROVED»;
  no line with sorry / admit / axiom in lean/ at f74d38a4. My lane's referee build of f74d38a4 (successor 33; logs
  scratch/box209_logs/lean_*.out; NOT CHECKER's exact-commit run): «Build completed successfully (3179 jobs).», and PG.Genome.k1, k2,
  k3, k5, PG.level_count, PG.plateau, PG.brsegG each «depends on axioms: [propext, Classical.choice, Quot.sound]». So the citations
  are accurate as «Lean-checked (lane)»; the line's wording is fixed by LT-3. The packet's body writes «Genome.k1» for PG.Genome.k1
  (note N-5; body text, not landing text).

## 0. Verdicts (REFEREE successor 34; date -u at writing: see the commit). First of two referee signatures; REFEREE-2 not read.
| § | statement | verdict |
| --- | --- | --- |
| §3 | Class facts (K1)-(K5) ((K2) on triples; (K4) with the face clause; (K3 e) with «largest class») | **SIGN** |
| §4 | Lemma LEVEL (L1)-(L5) | **SIGN** |
| §5 | Counting (C1)-(C4) ((C4) by landed R126 QUIET-N) | **SIGN** |
| §6 | Theorem WIN | **SIGN** |
| §6 | Corollary R-INT | **SIGN** |
| §6 | Theorem R-HEIGHT | **SIGN** |
| §6 | Theorem K1-TCYC | **SIGN** |
| §6 | Theorem FVS-TCYC | **SIGN** |
| §7 | Lemma PLATEAU (P1)-(P7) ((P6) with the σ̄_s step, REFEREE 32's under L41; (P7) by landed R118 (i) (a) with H0 checked; (P4) on a plateau only) | **SIGN** |
| §8 | Theorem ALL-TCYC with its «Consequences» | **SIGN** |
| §8-§14 | READING / DATA rows (not to sign) | checked: §2.6-§2.7, §4, §6 |
- Scope of every signature, as the packet states it: Howard ALL-SWITCH strategy improvement with Even, the MAXIMISER, improving
  (switch-best, keep-if-best) and VJ values, on IDEAL-CYC(G) of RESULTS R118 (a), for every genome G of R104 (Ξ-cycles and Ξ self-loops
  allowed), states 0, …, T_CYC of that run. Not N5, not N5′-xi (on or off Γ3), not other rules or games, not M4, not M3, not a gauntlet
  step-4 pass; G-N5-TIME stays OPEN.
- Gaps: **none in the statements or proofs.** Premises: landed R-ids only (R104 [DEF] with (D1), (D3), (D4) re-derived from R104's own
  line, §1.3; R15 (a); R118 (a), (b) F1, (c) DOM, (e)'s reason, (i) BR-SEG-G (a); R121 E-MON, E-DOM; R123 CN2, B-ONLY, NO-TIE, LOC-GATE,
  LOC-K2, [OPT] (R122's wording); R126 QUIET-N and the Ξ-feedback number); no lane lemma, no Lean theorem.
- The Lead's particular checks: (C4) uses landed R126 QUIET-N: YES (§2.3). A step relying on (P4) outside a plateau: NONE (§2.4).
  PR-1, PR-2, PR-3, PR-4, PR-5 (N-a applied; N-b as remark SHARP, not claimed), PR-6 (one packet): applied. Successor 33's three points:
  H0 on every step of H's run (§2.5), (P2)-type citations through (K3 e) for e-vertices with successor c_W ((L3), (P2)), Lean as
  «Lean-checked (lane)» (§7): applied in the packet; the line's Lean wording needs LT-3.
- Notes (no change asked): N-1 (K3 c), N-2 (H's priorities), N-3 (§8's N ≤ M), N-4 (class order), N-5 (Lean names in the body).
- **Line L-1 (sha1 28565b3c…): does NOT match yet.** Required: LT-1 (L43: the «no run tests the constants» clause names instance,
  tool, unit and file), LT-2 (L43: the G_N counter named k5 with its file), LT-3 (Lean citation form); my result on L-1:
  sha1 389645a2a646522a8fb57f05dba4458695ac74f2 (§5). Optional LO-1, LO-2 (the Lead's call). No statement, label or proof changes, so a
  fixes entry with a line L-2 by script needs a byte test only, not a re-sign.

## Erratum (REFEREE successor 34, 2026-11-12T22:12Z by date -u)
- The header's «Date -u at writing of §1-§2: 2026-11-12T21:05Z» was typed, not taken from date -u; the date -u outputs around that
  writing read 21:01Z and 21:04Z. The notebook's «written 2026-11-12T21:06Z by date -u» (commit 4c8d6c4f) has the same fault. No
  content changes.

## §8. Fixes entry 1 and line L-2 (REFEREE successor 34; date -u at writing 2026-11-13T00:02Z; the Lead's 00:03Z byte test)
- Objects (git): claude/l-new 366a38abb8832d616c908c48b73b7280580fcef6 (an ancestor of origin/claude/l-new, checked);
  docs/new/P-N5-LEVEL-line-L2.txt sha1 d18125ed1c62f8ad20396d9f94eac8bdbc624cf4, 7,970 B; docs/new/P-N5-LEVEL-fixes.md sha1
  43891337f77cc3f3cfd830d6acfb06e569ddc8d7 (entry 1, line-only). The report the lane pins, R-P-N5-LEVEL.md at 4c8d6c4f, has sha1
  374a1ba06f845ab9376f78b5ef82d24a3e4d2fc5 (measured).
- Byte test (scratch/level_l2test.py; log level_logs/l2test.out): L-1 (28565b3c, asserted) + my LT-1..LT-3 (the strings of my
  level_l1fix.py, read from that file) gives **389645a2a646522a8fb57f05dba4458695ac74f2** = my §5 L-1′; then REFEREE-2's R-1 and R-2,
  parsed by my script from R2-P-N5-LEVEL.md at claude/referee-2 43824abc §5.4 (wraps joined with one space), each old string once
  (stages 7afc25c8…, 1ba96bd2…); then my LO-1 as «the 49 must-0 counters of rv208.py» → that string + « (named in its header; a
  counter that is 0 is not printed)» (old once). Result: sha1 **d18125ed1c62f8ad20396d9f94eac8bdbc624cf4**, 7,970 B, one line, 0 «|»,
  93 «(» = 93 «)»; `cmp` with the lane's L-2: **EQUAL**. Nothing else changed.
- Meaning:
  - LT-1..LT-3: my strings, verbatim (the stage equals my L-1′).
  - R-1 = my LO-2 point: «…, and so are the number R of steps at which σ̄ changes, the number Q of loud steps and D^tot(v) − 1 for
    every vertex v (D^tot as in RESULTS R126)» states exactly the signed «Consequences» of ALL-TCYC (§2.6), with D^tot by R126's
    definition (landed: «D^tot(v) := the number of distinct classes of v over the run»). Correct.
  - LO-1: inserted in the form I asked for; the two parentheticals in a row read correctly.
  - R-2: «through NO-TIE and LOC-GATE in (K4), through DOM with CN2 in (K5) and in PLATEAU's H0»: true of the proofs ((K4) uses
    NO-TIE and LOC-GATE; (P7)'s H0 uses CN2). Note N-L2 (no change asked): H0 uses CN2 only, not DOM; the phrase is meant as
    «DOM with CN2 in (K5), and CN2 in PLATEAU's H0». It sits in the descriptive tail, not in a statement.
- Fixes entry 1: line-only, as it says; it records both referees' SIGN with the right report sha1s and lists each string with the
  Lead's ruling. Its note on «REFEREE 34's N-L1»: N-L1 is my note on P-N5-GATE (R-P-N5-GATE.md §L, the lamch columns), not on this
  packet; the lane's reading (this report's N-1..N-5) is the right set for P-N5-LEVEL. No change asked.
- Verdict: fixes entry 1 CORRECT. **Line L-2 MATCHES** (L-1 + exactly LT-1..LT-3, R-1, R-2, LO-1; sha1 d18125ed…). Statements and
  labels as in §0: every statement SIGN.
