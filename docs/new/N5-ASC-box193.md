# Box 193 ASC: the e-set walk of one vertex: first-e decomposition, descending plays, ascents (L-NEW successor 61)
L-NEW successor 61, under D18 / D14 / D1. Lead GO 19:23Z (2026-11-07). Written from 19:2xZ (date -u). Tools: experiments/new/box193/.
Labels: PROVED (lane, unrefereed) / PROVED-CONDITIONAL (on a named premise) / CONJECTURE / DATA (with counter: unit, set, scope) /
DEAD (instance) / READING (not to sign). Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).

## 0. The question and the answer so far (milestone 1)
- Question (Lead brief, box 193): the open core of box 192 is the height of the REALISABLE e-set walk of one vertex on IDEAL-CYC(G)
  (Howard at the movers of Γ(G), Odd's optimal counterstrategy). That is, «no 3-bit counter under E-DOM in any architecture». Asked: a
  proof that lane re-arms are polynomial, or the architecture that escapes the argument.
- Answer so far: no proof of the general case. Proved here:
  - §1 CHAIN-DECOMP (PROVED): a vertex's e-set is its first e-vertex f plus the e-set of f's fixed W-target. So at every state all
    e-sets are chains of one «next-e» forest on the e-vertices.
  - §1 E-MON (PROVED; = box 192 A10, re-proved here from F1, F2 and E-DOM-ALL-d): every vertex's e-set is lex-nondecreasing while its
    cycle node is fixed.
  - §2 DESC-POLY (PROVED): if a vertex's plays visit their e's in decreasing rank throughout an interval with its cycle node fixed, it
    has at most 1 + M(M+1)/2 distinct e-sets there. The bound is tight in the abstract model (exhaustive search, M ≤ 7).
- Why that does not settle it:
  - §3: in the abstract model, CHAIN-DECOMP + E-MON alone allow all 2^M sets, in lex order, when plays visit set bits LOWEST FIRST
    (Friedmann's H1 order). Construction ASC-EXP: DATA, exact simulation for M ≤ 12; no general proof written. So a polynomial bound
    must use Howard's or Odd's choices at ASCENTS: consecutive e's a, b on a play with rank(b) > rank(a).
  - §3 DATA: with at most A ascents per chain, the abstract maximum is exactly 2^M up to M = 2A + 2 and then falls below.
    A = 1: 2, 4, 8, 16, 29, 50, 82 (M 1-7), exactly cubic on M 3-7. A = 2: 64 at M 6, 119 < 128 at M 7.
    CONJECTURE ASC-POLY(A): for each fixed A the abstract maximum is polynomial in M (degree A + 2 in the data).
  - §4 (ascent gates): UP-JUMP (PROVED: an ascent needs a Ξ-edge from a level below lev(a) to a level ≥ lev(a)). Corollary NOUP
    (PROVED): genomes with no strictly upward Ξ-edge (Ξ-cycles inside levels allowed) have polynomial e-set height. ASC-GATE
    (PROVED-CONDITIONAL on [LOC]: at every gate of an ascent segment where Odd takes β, the e-face leads to a better cycle, or reaches b,
    or reaches an e above b before merging).
  - DATA: ascents occur in every instance (max 1-3 per play). So DESC is not met by real runs; the open core moves to the ascents.

## 1. Setting; CHAIN-DECOMP; E-MON
Setting:
- IDEAL-CYC(G), states σ_t, values Ω_t = (Λ, Π, k), the order ⊴, Facts F1-F6 and [LOC]: as in P-N5-XICYC (frozen, RESULTS R118) and
  box 192 §1.
- e-vertices: e_g for each gate g of option (x, k); e_g's only successor is the W-target y_g (a mover of level lev(x) − 1), or c_W at
  level 0.
- Ranks (P-N5-XICYC [DEF]; experiments/new/box189/gamma3.py l. 42-43, 58-59): every e has an even priority above every β-, mover-, gate-,
  cX-, K1- and K2-priority, ordered by (level, gate index). Only c_W, K0 and K3 lie above the e's.
  This is E-DOM-ALL-d (L-RED 54, R217 §10). Checked here from the builder's text, and by DATA:
  edomfail 0. Unit: vertices. Set: the 13 instances of check193.sh. Scope: Γ(G) as built.
- For a vertex v at state t: seq_t(v) := the e-vertices of Π_t(v) in play order; E_t(v) := their set (the «e-part»). For sets of
  e-vertices, S ≤ S′ (lex) iff S = S′ or the most relevant element of S Δ S′ lies in S′.

**Lemma E-MON (PROVED, lane; = box 192 Addendum 10, re-proved).** If Λ_t(v) = Λ_(t+1)(v), then E_t(v) ≤ E_(t+1)(v).
Proof.
- F1: Ω_t(v) ⊴ Ω_(t+1)(v). With equal cycle nodes, either Π_t(v) = Π_(t+1)(v), or the most relevant vertex z of the symmetric difference
  decides: z ∈ Π_(t+1)(v) if z is even, z ∈ Π_t(v) if z is odd.
- c_W, K0 and K3 are never in the symmetric difference:
  - c_W lies on a play only as its cycle node, so it is not in Π;
  - K0 lies on a play only if the play continues K0 → K3 → K2 (K0 → K3 and K3 → K2 frozen; K3's only in-edge is K0 → K3) and ends with
    cycle node K1 or K2. The only edges into K1, K2 come from K3, K2 and K1 (K0 → K1 is not taken: frozen). So both plays pass K0 and K3
    when w ∈ {K1, K2}, and neither does otherwise.
- So if an e-vertex lies in the symmetric difference, z is an e-vertex (E-DOM). It is even, so z ∈ Π_(t+1)(v) and E_t(v) < E_(t+1)(v).
  Otherwise E_t(v) = E_(t+1)(v). ∎

**Lemma CHAIN-DECOMP (PROVED, lane).** Let seq_t(v) = (f, …). Then Λ_t(y_f) = Λ_t(v) and E_t(v) = {f} ∪ E_t(y_f). Hence
seq_t(v) = (f, seq_t(y_f)).
Proof.
- f ∈ Π_t(v), so f is more relevant than w := Λ_t(v). Vertices of the cycle other than w are less relevant than w, so f lies on the
  prefix and is not the cycle node.
- F3: the play from f is f followed by the play from its successor. f is Even and frozen with one successor, y_f (or c_W).
- It is not c_W: then the play would end in c_W's loop, so w = c_W, more relevant than f. So y_f is the W-target mover.
- So the play from y_f is a suffix of the play from v, with the same cycle. Λ_t(y_f) = w, and Π_t(f) = Π_t(y_f) ∪ {f}.
- No e-vertex of Π_t(v) comes before f, by the choice of f. So E_t(v) = E_t(f) = {f} ∪ E_t(y_f). ∎
- Reading: at each state, define next_t(f) := the first element of seq_t(y_f) (or ⊥). Then every seq_t(v) is a path f, next_t(f),
  next²_t(f), … of one forest on the e-vertices (one forest per cycle node w). By E-MON at y_f, the TAIL E_t(y_f) of every e-vertex f is
  lex-nondecreasing while Λ_t(y_f) is fixed (TAIL-MON).
- DATA: decfail 0, tmonfail 0. Units: (state, vertex) pairs for decfail; consecutive state pairs at W-targets for tmonfail.
  Set: the 13 instances of check193.sh (8 frozen L-RED R217 instances in box193/inst, sha1 in inst/SHA1SUMS = L-RED's own sums at
  claude/l-red 476710810; 5 box 192 R-bests); plus the other 12 box 192 R-bests run once (same result). Scope: IDEAL-CYC.
  Tool: asc193.py.

## 2. Theorem DESC-POLY (PROVED, lane)
Statement. Let v be a vertex and I an interval of consecutive states with Λ_t(v) = w for all t ∈ I. Let U_w be the e-vertices more
relevant than w and M_w := |U_w|. Assume (DESC on I): for every t ∈ I, seq_t(v) is strictly decreasing in rank. Then
|{E_t(v) : t ∈ I}| ≤ 1 + M_w(M_w + 1)/2.

Proof.
- Intervals. For an e-vertex x let J_x := {t ∈ I : Λ_t(x) = w}.
  - By F1 and F2 the reward of Λ_t(x) is non-decreasing in t, and strictly increasing at each change of Λ_t(x).
  - So x has cycle node w on an interval of times. J_x is an interval.
  - On J_x, E_t(x) is lex-nondecreasing (E-MON). Since x ∈ E_t(x) on J_x, the tail E_t(x) ∖ {x} is lex-nondecreasing too: removing a
    common element does not change the symmetric difference.
- Chains. For t ∈ I write seq_t(v) = (c_1, …, c_p). By CHAIN-DECOMP applied repeatedly, seq_t(c_i) = (c_i, …, c_p) and Λ_t(c_i) = w.
  Set nx_t(c_i) := c_(i+1) (⊥ for i = p).
- Charging. Let t − 1, t ∈ I with E_(t−1)(v) ≠ E_t(v). Compare the two sequences from the front.
  - Either their first elements differ (event F at t),
  - or there is an x on both sequences with nx_(t−1)(x) ≠ nx_t(x): the last common element of the longest common prefix (event (x, t)).
- Bound on F events. Under DESC, c_1 = top(E_t(v)), the most relevant element. E-MON at v makes top(E_t(v)) non-decreasing in rank: the
  top of a lex-larger set is at least as relevant. So c_1 takes at most M_w + 1 values (⊥ and U_w) along I, in rank order, and there are
  at most M_w F events.
- Bound on (x, t) events. At such t − 1 and t, x lies on v's sequence. So seq(x) is a suffix of a decreasing sequence, hence decreasing,
  and nx(x) = top(E(x) ∖ {x}). That top is non-decreasing in rank on J_x (the tail is lex-nondecreasing), and t − 1, t ∈ J_x.
  - So along the (x, t) events, nx(x) strictly increases in rank among ⊥ and the elements of U_w below x.
  - Let i be x's position in U_w by rank. Then x has at most i − 1 events.
- Total: at most M_w + Σ_(i=1..M_w) (i − 1) = M_w(M_w + 1)/2 changes of E(v) along I. Lex-monotone values never repeat, so there are at
  most 1 + M_w(M_w + 1)/2 distinct values. ∎

Remarks.
- Premises: F1 ([R15a]), F2 ([VJ]), F3, E-DOM-ALL-d (gamma3.py l. 42-59). [LOC] is not used.
- Corollary DESC-ALL (PROVED, lane): if DESC holds on every interval of constant Λ(v), then D_E(v) ≤ (2M + 3)(1 + M(M + 1)/2). The
  intervals are at most 2M + 3, as in box 192 X-GATE (rewards rise strictly; at most 2M + 3 possible cycle nodes).
- Chain of conditionals (READING): DESC-ALL at every vertex + CONJECTURE IN-BOUND ⇒ D(v) polynomial ⇒ (OVT-DV, [LOC]) R_mov polynomial
  ⇒ (R-SPLIT, [LOC]) R polynomial if Σ L_g is polynomial ⇒ (Corollary T3) N5′-xi on Γ3 polynomial.
- Tightness: in the abstract model of §3 with no ascents allowed (A = 0), the exact maximum is 1 + M(M+1)/2 for M = 1-7:
  2, 4, 7, 11, 16, 22, 29. DATA. Unit: distinct hub chains. Set: all runs of CS(M, 0). Scope: abstract. Tools: chain193.py (M ≤ 5,
  check193.sh), dp193.c (M 6, 7; data/cs_dp.txt).
- DESC is NOT met by the real runs: §4 DATA shows ascents in every instance.

## 3. The abstract chain system CS(M, A); Construction ASC-EXP; ascent-limited data
Definition (CS(M, A)).
- Items 1, …, M, with rank = number. A forest is a parent map next: items → items ∪ {⊥}, acyclic. chain(x) := the items on the path
  from x, x included.
- Every chain has at most A ascents (consecutive p, q on it with q > p).
- A run is a sequence of forests such that every chain(x) is lex-nondecreasing.
- The hub is chain(h_t), for an item h_t chosen at each time (or ∅). It is lex-nondecreasing too.
- The quantity is the number of distinct hub chains.
- CS is exactly what §1 gives: CHAIN-DECOMP (one forest) + TAIL-MON / E-MON (monotone chains). Items = e-vertices; the hub = any vertex.
  So any bound proved in CS transfers to IDEAL-CYC. A run of CS need not come from a game.

**Construction ASC-EXP (DATA: verified exactly for M ≤ 10 in check193.sh, M ≤ 12 once).**
- Let S_t be the binary expansion of t = 0, …, 2^M − 1 (bit i = item i). Hub chain = S_t, visited in increasing rank.
- For x ∈ S_t set next(x) := min(S_t ∩ (x, M]) (⊥ if none). Items not in S_t keep their last pointer.
- The run is valid: every item's chain and the hub chain are lex-nondecreasing at every one of the 2^M steps.
- The hub takes all 2^M sets. Tool: ascexp193.py. A general-M proof is not written (sketch: tails of set items are the high part of the
  counter, which never decreases), so for general M this is a CONJECTURE, verified to M = 12.
- READING: the hub play visits the set bits lowest first and climbs: [F09]'s H1 path («starts with the lowest cycle whose bit is set,
  running through all other closed cycles», R217 §11). So CHAIN-DECOMP + E-MON cannot exclude a counter. The obstruction, if any, is in
  Odd's / Howard's choices at the ascents. This is exactly where L-RED's LEAK-ARCH (under H1-H3) found the leak.

DATA (exact maxima of CS(M, A); unit: distinct hub chains; set: all runs; scope: abstract; tools chain193.py, dp193.c, data/cs_dp.txt):

| A \ M | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2 | 4 | 7 | 11 | 16 | 22 | 29 |
| 1 | 2 | 4 | 8 | 16 | 29 | 50 | 82 |
| 2 | 2 | 4 | 8 | 16 | 32 | 64 | 119 |
| 3 | - | - | 8 | 16 | 32 | 64 | not run |
| unlimited (ASC-EXP) | 2 | 4 | 8 | 16 | 32 | 64 | 128 |

- 2^M exactly up to M = 2A + 2, then below: A = 0 from M 3, A = 1 from M 5, A = 2 from M 7.
- A = 1, M 3-7: exactly on (M³ − 7M² + 28M − 32)/2. Five points, four parameters: one point is a test, and it passes. Prediction for
  M = 8: 128. Not run: about 3 h of C here.
- Optimal A = 1 runs (chain193.py on M = 5, read off the DP): the hub chain is a descending LOW run, one ascent, then a descending HIGH
  run. The low part counts in DESC-QUAD fashion, and is re-armed each time the high part increases. That is low (quadratic) × high
  re-arms (linear), consistent with degree 3.
- **CONJECTURE ASC-POLY(A):** for each fixed A, the maximum of CS(M, A) is polynomial in M (degree A + 2 in the data). With DESC-POLY
  (A = 0) as the base case, it would give:
  - in IDEAL-CYC, if every chain has at most A ascents, D_E(v) is polynomial;
  - a superpolynomial e-set walk needs chains with an unbounded number of ascents (≈ M/2 for the full 2^M, in the data).
- Design hint for L-RED (READING): with at most one ascent per chain, no abstract run exceeds the cubic. A superpolynomial e-set walk needs
  hub plays that climb through many set bits (many ascents per play): [F09]'s H1. LEAK-ARCH kills that design only with access edges
  (H2, H3). So the open design question is an H1 hub WITHOUT [F09]'s access edges, i.e. lanes re-armed some other way.

## 4. Ascent gates: UP-JUMP, ASC-GATE
Setting: state t; a vertex v with w := Λ_t(v) less relevant than every e; consecutive a, b in seq_t(v) with rank(b) > rank(a) (an
ascent). P := the play strictly between a and b. a = e_g for an option (x, k) at level ℓ := lev(x).

**Lemma UP-JUMP (PROVED, lane).** P passes a β-face whose Ξ-target is a mover of level ≥ ℓ, entered from a mover of level ≤ ℓ − 1.
Proof.
- ℓ ≥ 1: at level 0 the successor of a is c_W, and the play would have cycle node c_W, more relevant than a.
- So P starts at the mover y_a of level ℓ − 1.
- P contains no e-vertex: every e on the play lies in Π (w is below every e), and b is the next one after a.
- So at every gate of P Odd takes β, and the β-face goes to its Ξ-target mover. It cannot go to u = K0: from K0 the play ends in the
  K-core and never reaches b.
- b = e_(g′) for an option of a mover x′ on P; rank(b) > rank(a) means lev(x′) ≥ ℓ (e-ranks are ordered by level first).
- Along P the level changes only at the β → Ξ-target steps. The first step entering a level ≥ ℓ is the claimed one. ∎
- The proof uses only that e-faces go down one level and β-faces go to their Ξ-targets. It does not need w below every e: for any w, an
  ascent a → b between consecutive e's of Π needs a strictly upward Ξ-edge on the play between them.

**Corollary NOUP (PROVED, lane).** Let G be a genome with no strictly upward Ξ-edge: every Ξ-target xt(x, k) is X or a mover of level
≤ lev(x). Ξ-cycles inside one level are allowed. Then every seq_t(v) is decreasing (UP-JUMP), so DESC holds on every interval. By
DESC-ALL, D_E(v) ≤ (2M + 3)(1 + M(M + 1)/2) for every vertex v.
- So on NOUP genomes the e-set height is polynomial, Ξ-cyclic or not.
- With CONJECTURE IN-BOUND, OVT-DV, R-SPLIT ([LOC]) and Σ L_g polynomial, R on Γ3-Howard would then be polynomial there. That is
  PROVED-CONDITIONAL on those premises, not proved.
- New against R104? R104 needs Ξ-acyclicity. NOUP genomes are Ξ-cyclic in 179 of 300 random samples (DATA below). The conditional
  conclusion is new in the fleet's files as far as I know; the unconditional part is only the e-set height.
- DATA (noup193.py 300 1). Unit: genomes / plays. Set: 300 random NOUP genomes (rand191 shape, d 1-4, w 1-3, degree 2-3, seed 1).
  Scope: IDEAL-CYC. Ξ-cyclic: 179. Max ascents in any play: 0. decfail 0, tmonfail 0. Max D_E per Λ-interval: 3. Least slack to
  1 + M(M + 1)/2: 3.
- Every ascent of a non-NOUP genome needs an upward Ξ-edge, and every Ξ-cycle across levels contains one.

**Lemma ASC-GATE (PROVED-CONDITIONAL on [LOC], lane).** Let h be a gate on P (so σ̄_t(h) = β_h). Then at least one holds:
- (i) Λ_t(e_h) ≠ w, and the reward of Λ_t(e_h) is larger than that of w;
- (ii) b lies on the play from e_h;
- (iii) the play from e_h, before its first vertex on the play from β_h, contains an e-vertex more relevant than b.
Proof.
- [LOC]: Ω_t(β_h) ⊴ Ω_t(e_h).
- If Λ_t(e_h) ≠ w = Λ_t(β_h), the order is decided by the rewards and is strict (F2): (i).
- Otherwise both plays have cycle node w. b lies on the play from β_h.
  - If b is not on the play from e_h, then b is not in the common suffix, so b ∈ B′ (the β-side part before the merge).
  - If (iii) fails, A′ (the e-side part) has no e-vertex more relevant than b. Then L-RED's E-DOM-CHOICE (R217 §11, checked below), with
    u = e_h, v = β_h and ε = b, gives Ω_t(β_h) ▷ Ω_t(e_h). That contradicts [LOC]. ∎
- Check of E-DOM-CHOICE (R217 §11, L-RED 54) before use, line by line: correct.
  - Its MERGE step needs only two plays with the same cycle node: both reach w, and from their first common vertex they coincide
    (positional strategies).
  - Its c_W / K0 / K3 exclusion is the argument written out in E-MON above.
- Meaning (READING): at every gate where an ascending play declines an escape, the declined escape leads to a better cycle (i), or
  climbs at least as high on its own (ii) / (iii).
  - So an ascent is «shadowed» by the alternatives Odd refuses.
  - A proof of ASC-POLY in the game would have to turn this shadowing into a charge on Λ-changes (case i) or on tail growth of the
    e-face's W-target (cases ii, iii). Not done.

DATA (asc193.py; unit as named; scope IDEAL-CYC; set: the 13 check193.sh instances; the other 12 box 192 R-bests run once, same zeros):

| instance | N | T | M (e's) | max ascents / play | ascents (movers) | upfail | gates | (i) | (ii) | (iii) | gfail | max D_E per Λ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rd2_d9 | 18 | 21 | 36 | 3 | 180 | 0 | 448 | 147 | 263 | 38 | 0 | 18 |
| cR_d2_w8_R22 | 16 | 24 | 32 | 3 | 61 | 0 | 117 | 65 | 47 | 5 | 0 | 11 |
| rd3_d7 | 14 | 25 | 37 | 2 | 52 | 0 | 159 | 0 | 153 | 6 | 0 | 12 |
| RS3 (L-RED, 3 bits) | 38 | 13 | 67 | 2 | 10 | 0 | 21 | 21 | 0 | 0 | 0 | 7 |
| RS2_L8M6 | 29 | 17 | 52 | 1 | 1 | 0 | 6 | 6 | 0 | 0 | 0 | 4 |
| FPORT_n3 ([F09] port) | 76 | 16 | 133 | 2 | 816 | 0 | 7344 | 7344 | 0 | 0 | 0 | 4 |
| LEAP_k8 | 37 | 17 | 67 | 2 | 208 | 0 | 1338 | 1338 | 0 | 0 | 0 | 18 |
| CLR_k8s16 (climb) | 53 | 28 | 99 | 2 | 297 | 0 | 3038 | 2829 | 133 | 76 | 0 | 15 |

- «ascents (movers)» counts ascents in movers' plays with Λ below every e (the lemma's setting), per (state, mover, ascent).
- In L-RED's hand-built designs every declined escape at an ascent gate is case (i): the escape leads to a different, better cycle.
  The random R-bests use (ii) / (iii) mostly.

## 5. Next
1. ASC-POLY(1) in CS: prove the cubic (low-run × high re-arm) by a two-level version of the DESC-POLY charging. Then A general, by
   induction on the descending runs.
2. In the game: case (i) of ASC-GATE charges a declined escape to a better cycle node at e_h. Bound how often an ascent's segment can
   change while the cycle node of every declined escape stays fixed.
3. For L-RED (via the Lead): a design needs an H1-type hub (many ascents per play) with lanes re-armed without access edges. The
   abstract runs (M ≤ 7) need chains with ≥ (M − 2)/2 ascents for all 2^M sets.
