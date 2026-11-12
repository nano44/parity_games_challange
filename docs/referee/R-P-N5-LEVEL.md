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

