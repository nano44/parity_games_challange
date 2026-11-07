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

## Addendum 1 (milestone 2; Lead 20:01Z: M = 8, ASC-POLY(1), case-(i) charge, DEAD «pointer monotone»)
### A1.1 Two DEAD proof routes for ASC-POLY(1) (abstract witnesses; tool dead193.py, in check193.sh)
- **DEAD PTR-MON-HI** («if the part of tail(x) above x is unchanged, next(x) does not move down»: the two-level version of
  DESC-POLY's charging).
  - Witness, CS(3, 1), one valid step: chains before 1: [1], 2: [2], 3: [3, 2]; after 1: [1, 2], 2: [2], 3: [3, 1, 2].
  - tail(3) rises lex from {2} to {1, 2}, its top stays 2, and next(3) drops from 2 to 1. The ascent 1 → 2 lies below x.
  - Counts. Unit: pointer changes with unchanged high part, over all dominance pairs of forests. Set: CS(M, 1). Scope: abstract.
    M 3: 31 changes, 4 decreasing. M 4: 1,200 / 191. M 5: 62,916 / 10,282.
- **DEAD FIXTOP-QUAD** («with the hub's top fixed, at most quadratically many hub chains»).
  - CS(5, 1), exact, per fixed top T = 1-5: 1, 2, 4, 8, 16 = 2^(T−1).
  - Fixing the hub's top alone does not reduce the problem.

### A1.2 Lemma SKELETON (PROVED, abstract; transfers to IDEAL-CYC through CHAIN-DECOMP)
Definitions.
- In CS(M, A) (or IDEAL-CYC with Λ fixed), let τ(x) := top(tail(x)), the most relevant element of chain(x) ∖ {x} (0 if empty).
- By E-MON / lex-monotone tails, τ(x) is non-decreasing in rank for every x. The hub's top is non-decreasing too.
- A LEVEL is a stretch of a run on which τ(x) is constant for every x and the hub's top is constant.
- A run has at most M(M + 1) + 1 levels: each τ(x) changes at most M times, the hub's top at most M times.

Statement. Inside a level, for every item x:
- (a) the τ-path x, τ(x), τ²(x), … (fixed in the level) lies on chain(x), in this order;
- (b) every element z strictly between τ^i(x) and τ^(i+1)(x) on chain(x) has z < τ^(i+1)(x) and τ(z) = τ^(i+1)(x);
- (c) chain(x) has at least as many ascents as it has nonempty segments (b).
So inside a level a chain with at most A ascents is its fixed skeleton plus at most A nonempty segments.

Proof.
- (a): τ(x) ∈ tail(x), so τ(x) lies on chain(x), and chain(τ(x)) is the suffix of chain(x) from τ(x). Induct along the path.
- (b): every element of tail(τ^i(x)) is ≤ its top τ^(i+1)(x). So an element z before τ^(i+1)(x) is below it. And tail(z) ⊆ tail(τ^i(x))
  contains τ^(i+1)(x), so τ(z) = τ^(i+1)(x).
- (c): if the segment is nonempty, the step from its last element (below τ^(i+1)(x)) into τ^(i+1)(x) is an ascent. Distinct segments
  give distinct steps. ∎
- DATA (skel193.py; unit: forests; set: all forests of CS(4, ∞), CS(5, ∞), CS(6, 1), CS(6, 2); scope: abstract): violations 0.

### A1.3 CONJECTURE RECUR (exact data) and what it would give (the implication is PROVED)
- **CONJECTURE RECUR(A):** inside one level, the hub takes at most f_(A−1)(M − 1) distinct chains. Here f_A(M) := the maximum of
  CS(M, A) and f_(−1) := 1.
- DATA (taulin193.py; unit: distinct hub chains inside one level, maximised over level keys; set: all runs; scope: abstract):

| A | M 3 | M 4 | M 5 | M 6 | predicted f_(A−1)(M − 1) |
| --- | --- | --- | --- | --- | --- |
| 0 | - | 1 | 1 | - | 1 |
| 1 | 4 | 7 | 11 | 16 | f_0 = 4, 7, 11, 16 |
| 2 | 4 | 8 | 16 | 29 | f_1 = 4, 8, 16, 29 |

  Equality in every case computed.
- Implication (PROVED): there are at most M(M + 1) + 1 levels (A1.2), and lex-monotone values never repeat across levels. So RECUR(A)
  gives f_A(M) ≤ (M² + M + 1)·f_(A−1)(M − 1), hence f_A(M) ≤ (M² + M + 1)^(A+1). That is ASC-POLY(A) for each fixed A, with
  degree ≤ 2A + 2.
  - The data's degrees are 2 (A = 0) and 3 (A = 1): the bound is loose but polynomial.
- Why RECUR is plausible (READING, from SKELETON): inside a level the skeletons are fixed. Each nonempty segment spends one ascent, and
  its elements z all have τ(z) = the next skeleton node, so a segment is a chain of the sub-forest {z : τ(z) = y} ending at y. A proof
  must show that such a segment walk behaves like CS(M − 1, A − 1).
  - Not done. The difficulty: chain(z) also contains tail(y), which varies inside the level and interleaves in rank with the segment.

### A1.4 ASC-GATE case (i): what it gives (READING plus a corollary)
- Corollary LOCK-(i) (PROVED-CONDITIONAL on [LOC]): if at state t gate h has Λ_t(e_h) ≠ Λ_t(β_h) =: w and σ̄_t(h) = β, then
  σ̄_s(h) = β at every later s with Λ_s(β_h) = w.
  - Proof: F1 at e_h gives reward(Λ_s(e_h)) ≥ reward(Λ_t(e_h)) > reward(w) (F2). So Ω_s(β_h) ◁ Ω_s(e_h), and [LOC] applies. ∎
  - This is EQ-FLIP plus monotone rewards (the X-GATE argument), not a new bound.
- So in L-RED's designs (only case (i) at ascent gates, §4 DATA), every ascent segment runs through gates that are frozen to β for the
  rest of w's interval. The ascent structure there changes only through MOVER switches on the segment, never through Odd.
- A charge of ascents to cycle-node changes would need a bound on mover switches along frozen-gate segments. That is the original problem
  in another form (lanes). Not done. No claim.

## Addendum 2 (milestone 3): RECUR(1) PROVED; hence ASC-POLY(1) PROVED (abstract) and its game form
**Lemma LOW-SHAPE (PROVED, abstract; any forest of CS(M, 1)).** Call x LOW if x < τ(x). For a low x, chain(x) is a strictly
descending run x = d_1 > … > d_k of low items with τ(d_j) = τ(x), followed by τ(x), followed by exactly the τ-path of τ(x). For a
non-low y (τ(y) < y or τ(y) = 0), the τ-path of y is strictly descending.
Proof.
- Every element of tail(x) is ≤ τ(x), and x < τ(x). So the step into τ(x) on chain(x) comes from an element below τ(x): an ascent.
- That is the chain's only ascent (A = 1). So the part before τ(x) is strictly descending, and the part from τ(x) on, chain(τ(x)), has
  no ascent.
- An ascent-free chain has no nonempty segment (SKELETON (c) holds per forest: its proof uses only τ). So chain(τ(x)) is exactly the
  τ-path of τ(x).
- Each d_j lies before τ(x), so tail(d_j) ⊆ tail(x) and contains τ(x): τ(d_j) = τ(x) > d_j.
- For a non-low y, τ(y) < y, and each later τ-step stays below it (SKELETON (b), A1.2). ∎
- DATA (low193.py; unit: forests; set: all forests of CS(4, 1), CS(5, 1), CS(6, 1); scope: abstract): violations 0.

**Theorem RECUR(1) (PROVED, abstract).** Inside one level (A1.2) of a run of CS(M, 1), the hub takes at most 1 + M(M − 1)/2 distinct
chains. That is f_0(M − 1).
Proof.
- Let T be the hub's top in the level and L the set of low items. T ∉ L: chain(T) is contained in a hub chain, so τ(T) < T or
  τ(T) = 0. So |L| ≤ M − 1.
- Shape of the hub chain. Let s be its first item.
  - If s = T: the hub chain is chain(T). Its skeleton is the descending τ-path of T. By SKELETON it carries at most one nonempty segment,
    and that segment's entry into the next skeleton node is the chain's one ascent. So the segment is strictly descending, of low items
    with τ = that node (SKELETON (b)).
  - If s ≠ T: then τ(s) = T > s, so s is low, and by LOW-SHAPE the hub chain is a descending run of low items, then T, then the τ-path
    of T.
  - Either way, hub = P(T) ∪ D, where P(T) is the τ-path of T (fixed in the level) and D (the D-PART) is empty or a strictly descending
    run of low items. Low items are not on P(T), whose nodes are non-low by LOW-SHAPE. So D is disjoint from P(T).
- Monotone parts.
  - The hub is lex-nondecreasing and P(T) is fixed, so D is lex-nondecreasing.
  - So top(D) = the first element of D is non-decreasing in rank (∅ first).
  - For a low w, chain(w) = D(w) ∪ P(τ(w)) at every state of the level (LOW-SHAPE, with τ fixed). So D(w) is lex-nondecreasing.
  - Then so is D(w) ∖ {w}. Its top is w's pointer (∅ when the pointer is τ(w)). So w's pointer is non-decreasing in rank, among ∅ and
    the low items below w.
- Charging. A change of D between consecutive states of the level either changes its first element (at most |L| times: values ∅ and L,
  monotone), or keeps it. In the second case, at the last common element w of the two runs' common prefix, the pointer changes (it
  cannot stay, since the runs then continue identically).
  - w is low; its pointer changes at most |{u ∈ L : u < w}| times in the level.
  - Total changes ≤ |L| + |L|(|L| − 1)/2 = |L|(|L| + 1)/2.
  - Distinct D's (hence hub chains) ≤ 1 + |L|(|L| + 1)/2 ≤ 1 + (M − 1)M/2. ∎
- Agreement with data: equality with the exact maxima 4, 7, 11, 16 at M 3-6 (A1.3).

**Corollary ASC-POLY(1) (PROVED, abstract).** f_1(M) ≤ (M² + M + 1)(1 + M(M − 1)/2).
- Levels ≤ M(M + 1) + 1 (A1.2), and lex-monotone hub values never repeat across levels.
- DATA comparison: f_1 = 2, 4, 8, 16, 29, 50, 82 against the bound 3, 14, 52, 147, 341, 688, 1254 (M 1-7).
- The bound is degree 4; the data's degree is 3. CONJECTURE ASC-POLY(A) for A ≥ 2 stays open; RECUR(A ≥ 2) is DATA only (A1.3).

**Corollary ASC1 (PROVED, lane; the game form).** Let v be a vertex of IDEAL-CYC(G), I an interval of states with Λ_t(v) = w on I, U_w
the e-vertices more relevant than w, M_w := |U_w|. Hypothesis (ASC≤1 on I): at every t ∈ I, every e-vertex x with Λ_t(x) = w has at
most one ascent in seq_t(x), and so does v. Then D_E,I(v) ≤ (M_w² + 3M_w + 1)(1 + M_w(M_w − 1)/2).
Proof.
- Items := U_w. The item x is active at t iff Λ_t(x) = w. Its active times J_x form an interval (§2 proof).
- At each t, the active items' next-e pointers form one forest (CHAIN-DECOMP). Their chains are lex-nondecreasing on J_x (E-MON). The
  hub is v.
- So every statement of SKELETON, LOW-SHAPE and RECUR(1) applies inside a level, where the active set, the τ's of active items and the
  top of E(v) are constant. Every argument there compares states of one level at which the items concerned are active.
- Level count: each item becomes active at most once and inactive at most once (2M_w); each τ(x) changes at most M_w times (M_w²); the
  hub's top at most M_w times. So there are at most M_w² + 3M_w + 1 levels.
- Multiply by RECUR(1)'s 1 + (M_w − 1)M_w/2. ∎
- Premises: F1, F2, F3, E-DOM-ALL-d. [LOC] is not used.
- DATA: the hypothesis holds in rd2_d3, rd2_d4, rd3_d3, rf_d4, RS2, RS2_L8M6, RSG_K4 and FPORT_n2 (max ascents per play 1, §4 table and
  asc193.py lines). It fails in the others (2 or 3).

Reading (status of the open core after milestone 3).
- e-set height is now PROVED polynomial on runs whose plays have at most one ascent (ASC1), and on NOUP genomes (no ascents).
- A superpolynomial e-set walk, hence any superpolynomial R via OVT-DV, needs plays with at least two ascents.
- RECUR(A ≥ 2) is the next target; the data says RECUR(2) holds with equality at M 3-6.

## Addendum 3 (toward RECUR(2)): two more DEAD routes; RECUR(2) stays DATA
- **DEAD RMON-2** (the step that proved RECUR(1), read at A = 2: «inside a level, a low item's part before τ(w) is lex-nondecreasing»).
  - Witness, CS(5, 2), one valid same-level step: chains before 1: [1, 2, 5, 4], 2: [2, 5, 4], 3: [3, 4], 4: [4], 5: [5, 4]; after
    1: [1, 5, 3, 4], 2: [2, 1, 5, 3, 4], 3: [3, 4], 4: [4], 5: [5, 3, 4]. τ = (5, 5, 4, 0, 4) in both.
  - chain(1) rises (3 enters and beats 2), but its part before τ(1) = 5 drops from {1, 2} to {1}. The cause is the one named in A1.3:
    with A = 2, chain(τ(w)) can still change inside a level (5 gains the segment {3} before 4), and it interleaves in rank with w's part.
  - Counts (dead193.py rmon 5). Unit: (same-level dominance pair, low item). Set: CS(5, 2). Scope: abstract. 10,242 checks,
    5 decreases. CS(4, 2): 234 checks, 0 decreases (scratch run).
- **DEAD K-LEVEL collapse** («fixing deeper R95 prefixes (the top K elements of every tail) cuts the ascent budget further»).
  - Exact maxima inside one K-level (klev193.py; unit: distinct hub chains; set: all runs; scope: abstract):
    - A 2, K 2: 4, 8, 16 at M 4, 5, 6;
    - A 2, K 3: 4, 8 at M 5, 6;
    - A 1, K 2: 7, 11 at M 5, 6.
  - That is f_(A−1)(M − K) in every case: deeper prefixes remove ITEMS, not ascents. Only the first level (K = 1) spends an ascent.
  - So R95's k-prefix refinement (polynomially many K-levels for fixed K) cannot by itself give ASC-POLY(2).
- RECUR(2) stays CONJECTURE (equality with f_1(M − 1) at M 3-6, A1.3). A proof must handle a gap's segment whose items see a varying
  tail(τ(w)). In the witness that tail gains a segment of another gap.

## Addendum 4 (milestone 4): Theorem HUB-ASC(B), polynomial for every fixed B; ASC-POLY(A) PROVED (abstract); game forms; Corollary UP-B
RECUR(2) in its exact form (f_1(M − 1) per level) stays DATA; the dead step is RMON-2 (Addendum 3, witness CS(5, 2)). But a coarser
induction avoids that step and proves polynomiality for every fixed number of ascents. Only the HUB's chain is constrained.

Setting.
- A run of CS(M, ∞): forests on items 1..M, every chain lex-nondecreasing.
- A hub h_t whose chain has at most B ascents at every time t of the run.
- The statement must also hold for runs restricted to a subset of times. Restricting a run to a subset of its times gives a run, since
  monotonicity is between any two times.

**Theorem HUB-ASC(B) (PROVED, lane, abstract).** The hub takes at most F_B(M) distinct chains, where F_0(M) := 1 + M(M + 1)/2 and
F_B(M) := (M² + M + 1)(1 + M·F_(B−1)(M)²).
So F_B(M) is a polynomial in M of degree 5·2^B − 3 (2, 7, 17, …) for each fixed B.

Proof (induction on B).
- B = 0 is DESC-POLY's argument (§2), which uses only the hub's chain:
  - an (x, t) event has x on the hub chain at t − 1 and t, so x's chain is a descending suffix and x's pointer is top(tail(x)), which is
    monotone (tails are lex-monotone);
  - the hub's first element is its top, which is monotone.
- B ≥ 1. Levels (A1.2): stretches with every τ(x) and the hub's top T constant. There are at most M² + M + 1 of them. Fix a level. By
  SKELETON (b), (c), which hold in every forest, the hub chain c = chain(s) has one of three shapes:
  - (N) s = T and no nonempty segment: c = P(T), the τ-path of T, fixed in the level.
  - (a) s ≠ T: then τ(s) = T > s. The part of c before T consists of items with τ = T (SKELETON (b)); write it R(s). Then
    c = R(s) ⊔ chain(T), and the step into T is an ascent. Entry y := T, entry item z := s.
  - (c) s = T, with a first nonempty segment after skeleton node y_i: z := next(y_i) has τ(z) = y_(i+1) =: y. Then
    c = {y_0, …, y_i} ⊔ R(z) ⊔ chain(y), where R(z) is the part of chain(z) before y, and the step into y is an ascent.
  - In (a) and (c): c = Fix(y) ⊔ R(z) with Fix(y) := {skeleton nodes of T above y} ∪ chain(y). Both R(z) and chain(y) have at most
    B − 1 ascents (the entry ascent is spent).
- Group the level's times by entry y (at most M values, all on P(T)), and within y by the value of chain(y).
  - (i) At entry-y times, chain(y) is the chain of the constant hub y in the run restricted to those times, and it has ≤ B − 1 ascents.
    By HUB-ASC(B − 1) it takes at most F_(B−1)(M) values.
  - (ii) Fix y and one value C of chain(y). Let Z_y := {w : τ(w) = y, w < y}. For every w ∈ Z_y and every time of the level,
    chain(w) = R(w) ⊔ chain(y) (τ(w) = y lies on chain(w), and everything before it is in Z_y).
    - So at the times where chain(y) = C, every R(w) is lex-nondecreasing: the common part C is removed.
    - The pointers of Z_y (to the next element before y, or ⊥) form a forest on Z_y whose chains are the R(w). So those times carry a run
      of CS(|Z_y|, ∞).
    - The hub restricted to them is Fix(y) ⊔ R(z_t) with Fix(y) constant, so R(z_t) is lex-nondecreasing: a hub of that run with
      ≤ B − 1 ascents.
    - By HUB-ASC(B − 1) there are at most F_(B−1)(|Z_y|) ≤ F_(B−1)(M) distinct hub chains there.
- Per level: at most 1 + M·F_(B−1)(M)·F_(B−1)(M) distinct hub chains. Lex-monotone hub values never repeat across levels, so
  F_B(M) ≤ (M² + M + 1)(1 + M·F_(B−1)(M)²). ∎

Remarks.
- The constraint is on the hub only; other chains are unconstrained. In particular ASC-POLY(A) (CONJECTURE since §3) is now PROVED:
  f_A(M) ≤ F_A(M).
- The bound is far from tight: exact f_1 is cubic, F_1 has degree 7.
- DATA (hubasc193.py; exact maxima with only the hub constrained; unit: distinct hub chains; set: all runs of CS(M, ∞); scope: abstract):
  - B 0: 7, 11, 16 at M 3-5 (= F_0);
  - B 1: 8, 16, 29 at M 3-5;
  - B 2: 32 at M 5.
  These are the same values as f_A with every chain constrained (§3).
- Exact RECUR(2) (f_1(M − 1) per level) stays DATA. HUB-ASC replaces it for polynomiality.

**Corollary HUB-ASC-G (PROVED, lane; game form).** Let v be a vertex of IDEAL-CYC(G) and I an interval with Λ_t(v) = w. If seq_t(v)
has at most B ascents for every t ∈ I, then D_E,I(v) ≤ F′_B(M_w), with F′_0 := 1 + M(M + 1)/2 and
F′_B(M) := (M² + 3M + 1)(1 + M·F′_(B−1)(M)²).
- Proof: as ASC1 (Addendum 2). Items = U_w, active iff Λ_t(x) = w, active times are intervals; one forest per state (CHAIN-DECOMP),
  lex-monotone tails (E-MON). Levels also fix the active set, so there are at most M_w² + 3M_w + 1 of them. Every restricted sub-run in
  the induction lies inside one level, where the active set is constant. ∎
- Premises: F1-F3, E-DOM-ALL-d. [LOC] is not used. No hypothesis on other vertices' plays.

**Corollary UP-B (PROVED, lane).** Let U(G) be the number of strictly upward Ξ-edges of G (options (x, k) whose Ξ-target is a mover of
level > lev(x)). Then every seq_t(v) has at most U(G) ascents, so D_E(v) ≤ (2M + 3)·F′_(U(G))(M) for every vertex v.
- Proof: each ascent's segment (between consecutive e's of Π, on the play's prefix) contains a strictly upward Ξ-edge (UP-JUMP). The
  segments of different ascents are disjoint parts of the prefix. The prefix's vertices are distinct, and each β-vertex has one Ξ-edge.
  So the edges are distinct. Then HUB-ASC-G on each of the ≤ 2M + 3 Λ-intervals. ∎
- So genomes with a bounded number of upward Ξ-edges have polynomial e-set height. NOUP (§4) is U(G) = 0.
- DATA (ug193.py; unit: max ascents over all (state, vertex) plays vs U(G); set: the 8 inst/ files + rd2_d9, rf_d5, rd3_d7,
  cR_d2_w8_R22; scope: IDEAL-CYC): max ascents ≤ U(G) everywhere. E.g. RSG_K4: U 1, max 1. rd2_d9: U 20, max 3.

Reading (status of the open core after milestone 4).
- PROVED (lane): the e-set height D_E(v) is polynomial whenever v's plays have a bounded number of ascents, in particular on genomes with
  boundedly many upward Ξ-edges. The bound is M^(O(2^B)), so quasi-polynomial if B = O(log log M).
- So a superpolynomial e-set walk, hence via OVT-DV + IN-BOUND any superpolynomial R, needs plays whose ascent count grows with the
  genome, i.e. many upward Ξ-edges used on one play. That is the H1 lowest-first hub of ASC-EXP, now forced. With ASC-EXP's own
  construction the count is M − 1.
- Open: (1) IN-BOUND (CONJECTURE); (2) plays with ω(1) ascents. Is there a game run whose hub play climbs through k upward Ξ-edges and
  realises ≫ poly e-sets? LEAK-ARCH kills [F09]'s H1-H3 version. A counter must avoid access edges (H2).
- For L-RED: designs need ascents per play growing with size. A design with a fixed number of upward Ξ-edges, however large the genome,
  cannot give superpolynomial e-set height.
