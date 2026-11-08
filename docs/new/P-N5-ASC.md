# Packet P-N5-ASC (box 193): the e-set height of one vertex on IDEAL-CYC is polynomial when its plays have boundedly many ascents (HUB-ASC-G), in particular on genomes with boundedly many upward Ξ-edges (UP-B)
L-NEW successor 61 (Opus 5.5), D1 / D14 / D18. Lead 2026-11-07 21:44Z: «DECISION: GO, packet P-N5-ASC.» Written from 21:4xZ (date -u).
FROZEN at push. Later text goes to docs/new/P-N5-ASC-fixes.md, append-only. Source, history only: docs/new/N5-ASC-box193.md (box 193,
§1-§4 and Addenda 1-4). This packet carries every proof in full.
Labels: PROVED (L-NEW 61, unrefereed) / HYPOTHESIS (stated in the theorem) / DATA / READING (not to sign).
This packet is NOT a TARGET.md claim and NOT M3. It does not decide G-N5-TIME. N5′-xi stays a CANDIDATE.

## What this packet does NOT give (one sentence, as asked)
It bounds the e-set height D_E,I(v), the number of distinct sets of e-vertices on v's plays while v's cycle node is fixed, and NOT R and NOT
any running time: the step from D_E to R needs OVT-DV ([LOC], L-RED R217 §2) and CONJECTURE IN-BOUND (box 192 Addendum 9), and neither
has landed.

## To sign
| § | statement | label | hypotheses |
| --- | --- | --- | --- |
| §2 | definitions: e-sets, lex order, ascents, the chain system CS(M) | definitions | |
| §3 | Lemma E-MON; Lemma CHAIN-DECOMP | PROVED | every genome, IDEAL-CYC |
| §4 | Lemma SKELETON; Theorem HUB-ASC(B) (abstract; B = 0 is DESC-POLY) | PROVED | any run of CS(M) |
| §5 | Corollary HUB-ASC-G (game form) | PROVED | every genome; hypothesis on v's plays only |
| §6 | Lemma UP-JUMP; Corollary UP-B; Corollary NOUP | PROVED | UP-JUMP and UP-B under HYPOTHESIS [E-LEV] |
| §7-§9 | DATA, machine checks, TARGET diff, limits | DATA / READING (not to sign) | |

## 1. Premises (landed only; quoted by script from trunk claude/vibrant-johnson-nxvvxo 5470cc0c, docs/RESULTS.md, line numbers there)
- [DEF] RESULTS R104 (l. 9864), definitions of the genome and of Γ(G) only:
  - «each with a W-target of level lev(x) − 1 (none at level 0), a Ξ-target xt(x, k), a mover or the exit X»;
  - «Even movers of priority 0; Odd gates of priority 1 with a W-face e and a Ξ-face β»;
  - «β of priority 6 + 2·rank + parity with edges to the Ξ-target and to u, or to u alone»;
  - «e of even priority above every β with one edge to the W-target or to the top even self-loop c_W»;
  - «an unused even self-loop of priority 2; c_W's priority top is the least even number at least 2 above every other priority so far»;
  - «a closed core u = K0 (Even, top + 2) → {K1, K3}, K1 (Even, 5) → {K0, K1}, K2 (Odd, 3) → {K1, K2}, K3 (Even, top + 3) → {K1, K2}»;
  - «with start σ = the genome start at movers, β → its Ξ-target (u when the target is X), K0 → K3, K1 → K1, K3 → K2».
  R104's own text leaves the order among the e-priorities open: «the exact e-priorities to packet §3.1» (l. 10085).
- [XICYC] RESULTS R118 (l. 13607), signed parts used:
  - (a) (l. 13677): IDEAL-CYC(G): «The game is Γ(G) with every Even vertex that is not a mover frozen at its start successor. Odd is
    unrestricted (gates and K2).», Howard steps at the movers, Ω_t, σ̄_t.
  - (b) (l. 13682): «(b) Facts F1-F6 (§3 l. 68-83) with F4 REPLACED by F4′». Used here: F1, F2, F3. They are quoted from the frozen packet
    docs/new/P-N5-XICYC.md (sha1 149e2414), l. 69-74:
    - F1 «Ω_t ⊴ Ω_(t+1) pointwise, for every step t.»;
    - F2 «if Ω(v) ⊴ Ω′(v) and Λ ≠ Λ′, then the reward of Λ′ is strictly larger. Distinct vertices have distinct rewards.»;
    - F3 «let v be a vertex with Λ_t(v) ≠ v. Then Ω_t(v) = ext(v, Ω_t(nx_t(v))), … and ext(v, (Λ, Π, k)) := (Λ, Π ∪ {v if v is more
      relevant than Λ}, k + 1).»
  - (e) (l. 13691): «C ≤ n·(2M + 2).» with its reason «(each vertex's Λ moves only to a vertex of strictly larger reward among at most
    2M + 3 possible cycle nodes)». Used in the per-vertex form: Λ_t(v) takes at most 2M + 3 values, in increasing reward.
- [VJ] values (Λ, Π, k) and the order ⊴, as in R118's premises (VJ00 §4.2 / Friedmann arXiv 1106.0778 §3); P-N5-XICYC §1 l. 29-33. Π is
  the set of play vertices more relevant than Λ (vertices of the cycle other than Λ are less relevant than Λ).
- HYPOTHESIS [E-LEV] (only for §6 UP-JUMP and UP-B): the e-priorities increase with the level of their gate's mover. Formally: lev(x) <
  lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′)). This is how the fleet's builder sets them (experiments/new/box189/gamma3.py l. 43, order
  (level, gate index)). It is NOT in a landed R-id, so it is a hypothesis of those two statements.
- Not used anywhere: [LOC], OVT-DV, IN-BOUND, any L-RED lane lemma, F4/F4′, F5, F6.

## 2. Definitions
- Fix a genome G and a run of IDEAL-CYC(G). For a vertex v and a state t: seq_t(v) := the e-vertices that lie in Π_t(v), in the order of
  the play from v under (σ_t, σ̄_t). E_t(v) := their set (the e-set).
- Lex order on sets of e-vertices: S ≤ S′ iff S = S′ or the most relevant element of S Δ S′ lies in S′.
- An ascent of a sequence (c_1, …, c_p) of distinct items is an index i with c_(i+1) more relevant than c_i.
- For an interval I of states with Λ_t(v) = w for all t ∈ I: U_w := the e-vertices more relevant than w, M_w := |U_w|, and
  D_E,I(v) := |{E_t(v) : t ∈ I}|.
- The chain system CS(M): items 1..M, compared by number («rank»).
  - A forest is a map next: items → items ∪ {⊥} without cycles. chain(x) := the sequence x, next(x), next²(x), … (as a set when compared).
  - A run is a sequence of forests (one per time t in a finite ordered index set) such that, for every item x and times s < t,
    chain_s(x) ≤ chain_t(x) (lex).
  - A hub of a run is a choice h_t ∈ items ∪ {⊥} with chain_s(h_s) ≤ chain_t(h_t) for s < t (chain(⊥) := ∅). Its value at t is chain_t(h_t).
  - A run restricted to any subset of its times is again a run (the conditions are pairwise).

## 3. Two lemmas on IDEAL-CYC
**Lemma E-MON.** If Λ_t(v) = Λ_(t+1)(v), then E_t(v) ≤ E_(t+1)(v).
Proof.
- F1: Ω_t(v) ⊴ Ω_(t+1)(v). With equal cycle node w, [VJ] decides by z, the most relevant vertex of Π_t(v) Δ Π_(t+1)(v) (if there is one):
  z lies in Π_(t+1)(v) if z is even, and in Π_t(v) if z is odd.
- Every vertex more relevant than some e-vertex is an e-vertex, c_W, K0 or K3, by [DEF]: e lies above every β; movers 0, gates 1,
  the unused loop 2, K2 3, K1 5 and β ≥ 6 all lie below every e; c_W lies above every other priority so far, K0 = top + 2, K3 = top + 3.
- c_W, K0 and K3 are never in the symmetric difference:
  - c_W has only its self-loop, so on a play it is the cycle node, never in Π;
  - K0 → K3 and K3 → K2 are frozen in IDEAL-CYC ([XICYC] (a), [DEF] start). The only edge into K3 is from K0. The only edges into K1, K2
    come from K0 (not taken: frozen to K3), K1, K2 and K3. So a play passes K0 iff it passes K3 iff it ends with cycle node K1 or K2.
    Both plays have the same w, so both or neither contain K0 and K3.
- So if some e-vertex lies in the symmetric difference, z is an e-vertex. It is even, so z ∈ Π_(t+1)(v), and E_t(v) < E_(t+1)(v).
  Otherwise the e-sets are equal. ∎

**Lemma CHAIN-DECOMP.** If seq_t(v) = (f, …), then the successor y_f of f is a mover, Λ_t(y_f) = Λ_t(v) and E_t(v) = {f} ∪ E_t(y_f).
Hence seq_t(v) = (f, seq_t(y_f)).
Proof.
- f ∈ Π_t(v) is more relevant than w := Λ_t(v). Cycle vertices other than w are less relevant than w, so f is on the prefix, not the
  cycle node.
- f is Even and frozen with one successor ([DEF]: «one edge to the W-target or to … c_W»). F3: the play from f is f followed by the play
  from y_f.
- y_f ≠ c_W: otherwise the play ends in c_W's loop, so w = c_W, more relevant than f. So y_f is the W-target mover.
- The play from y_f is a suffix of the play from v, so Λ_t(y_f) = w. No e-vertex of Π_t(v) precedes f. So E_t(v) = {f} ∪ E_t(y_f). ∎
Reading: at each state, next_t(f) := the first element of seq_t(y_f) (⊥ if none) defines one forest on the e-vertices with cycle node w,
and every seq_t(v) is a path of it starting at v's first e-vertex.

## 4. The abstract core
For an item x at time t: τ_t(x) := the most relevant element of chain_t(x) ∖ {x} (0 if empty).
- In a run, τ(x) is non-decreasing in rank: the top of a lex-larger set is at least as large.
- A LEVEL of a run with a hub is a maximal set of consecutive times on which every τ(x) and the hub's top are constant. A run has at most
  M² + M + 1 levels: each τ(x) takes at most M values, the hub's top at most M + 1.

**Lemma SKELETON.** In any forest, for every item x and i ≥ 0:
- (a) the τ-path x, τ(x), τ²(x), … lies on chain(x) in this order;
- (b) every element z strictly between τ^i(x) and τ^(i+1)(x) on chain(x) satisfies z < τ^(i+1)(x) and τ(z) = τ^(i+1)(x), and
  τ^(i+2)(x) < τ^(i+1)(x);
- (c) if that stretch (a «segment») is nonempty, the step from its last element into τ^(i+1)(x) is an ascent.
Proof.
- (a): τ(x) ∈ chain(x) ∖ {x}, and chain(τ(x)) is the suffix of chain(x) from τ(x). Induct along the path.
- (b): chain(τ^i(x)) ∖ {τ^i(x)} has top τ^(i+1)(x). So z < τ^(i+1)(x), and the elements after τ^(i+1)(x) are below it, i.e.
  τ^(i+2)(x) < τ^(i+1)(x). Also z's chain is a suffix of chain(τ^i(x)) and contains τ^(i+1)(x), so τ(z) = τ^(i+1)(x).
- (c) is immediate from (b). ∎

**Theorem HUB-ASC(B).** Let F_0(M) := 1 + M(M + 1)/2 and F_B(M) := (M² + M + 1)(1 + M·F_(B−1)(M)²) for B ≥ 1. In any run of CS(M)
with a hub whose value has at most B ascents at every time, the hub takes at most F_B(M) distinct values.
For fixed B, F_B is a polynomial in M of degree 5·2^B − 3.
Proof, by induction on B.
- Every lex-monotone sequence of sets is strictly increasing at each change, so the number of distinct values is 1 + the number of
  changes.
- B = 0 (DESC-POLY). The hub's value is descending, so its first element is its top, which is non-decreasing. It changes at most M times.
  - Otherwise, at a change between consecutive times s < t with the same first element, let x be the last element of the common prefix
    of the two values. Then next_s(x) ≠ next_t(x), and x lies on the hub's value at s and t.
  - There x's chain is a descending suffix, so next(x) = τ(x).
  - τ(x) is non-decreasing in rank over all times and here strictly changes. It takes values in {0} ∪ {items below x}, so x causes at
    most x − 1 such changes.
  - Total changes ≤ M + Σ_x (x − 1) = M(M + 1)/2.
- B ≥ 1. Fix a level, with hub top T. Let the hub's value at a time be c = chain(s), s = h_t. Three shapes:
  - (N) s = T and c has no nonempty segment: c is the τ-path P(T) of T, fixed in the level.
  - (a) s ≠ T: then τ(s) = T > s.
    - By SKELETON (b), the part of c before T consists of items z with τ(z) = T; call it R(s).
    - c = R(s) ⊔ chain(T), and the step into T is an ascent (SKELETON (c), or s → T directly).
    - Entry node y := T, entry item z := s.
  - (c) s = T with a first nonempty segment after the skeleton node y_i:
    - z := next(y_i) has τ(z) = y_(i+1) =: y (SKELETON (b));
    - c = {y_0, …, y_i} ⊔ R(z) ⊔ chain(y), where R(z) := the part of chain(z) before y;
    - the step into y is an ascent (SKELETON (c)).
  - In (a) and (c), c = Fix(y) ⊔ R(z) with Fix(y) := {skeleton nodes of P(T) above y} ∪ chain(y). Since the entry ascent is spent, R(z)
    and chain(y) each have at most B − 1 ascents. y ranges over at most M values, all on P(T) ∪ {T}.
- (i) Fix y. At the level's times with entry node y, chain(y) is the value of the constant hub y in the run restricted to those times.
  It has at most B − 1 ascents there. By HUB-ASC(B − 1) it takes at most F_(B−1)(M) values.
- (ii) Fix y and one value C of chain(y). Let Z_y := {w : τ(w) = y, w < y} (constant in the level).
  - For every w ∈ Z_y and every time of the level, chain(w) = R(w) ⊔ chain(y): τ(w) = y lies on chain(w), and the elements before it
    are in Z_y by SKELETON (b).
  - So at the times with entry node y and chain(y) = C, every R(w), w ∈ Z_y, is lex-nondecreasing: remove the common part C.
  - The maps w ↦ (the element after w on R(w), or ⊥) form forests on Z_y whose chains are the R(w). So these times carry a run of
    CS(|Z_y|) (items Z_y in their rank order).
  - On these times the hub's value is Fix(y) ⊔ R(z_t) with Fix(y) constant. So R(z_t) is lex-nondecreasing: a hub of that run with at
    most B − 1 ascents.
  - By HUB-ASC(B − 1) it takes at most F_(B−1)(|Z_y|) ≤ F_(B−1)(M) values.
- So within a level the hub takes at most 1 + Σ_y F_(B−1)(M)·F_(B−1)(M) ≤ 1 + M·F_(B−1)(M)² values: one for shape (N), then (i) × (ii).
- Lex-monotone values never repeat across levels. Over at most M² + M + 1 levels this gives F_B(M).
- Degree: d_0 = 2 and d_B = 2 + 1 + 2d_(B−1), so d_B = 5·2^B − 3. ∎

## 5. The game form
**Corollary HUB-ASC-G.** Let v be a vertex and I an interval of states of a run of IDEAL-CYC(G), for any genome G, with Λ_t(v) = w for
t ∈ I. If seq_t(v) has at most B ascents for every t ∈ I, then D_E,I(v) ≤ F′_B(M_w). Here F′_0(M) := 1 + M(M + 1)/2 and
F′_B(M) := (M² + 3M + 1)(1 + M·F′_(B−1)(M)²). No hypothesis is made on any other vertex's plays.
Proof.
- Items := U_w in their relevance order. Item x is active at t iff Λ_t(x) = w. Its active times form an interval: by F1 and F2 the
  reward of Λ_t(x) is non-decreasing and strictly increases at each change.
- At each t ∈ I, next_t on the active items is one forest (CHAIN-DECOMP), and every active item's chain is E_t(x) in the order seq_t(x).
  By E-MON, each item's chain is lex-nondecreasing over its active times. The hub is v: its value is seq_t(v) = chain_t(f_t(v)).
- Refine the levels of §4 so that the active set is also constant: each item becomes active at most once and inactive at most once. So
  there are at most M² + 3M + 1 levels.
- Inside one such level the active items form a run of CS(M_w) restricted to those times, and §4's proof applies word for word. Every
  restricted sub-run in it lies inside the level. ∎
- Corollary (whole run): Λ_t(v) takes at most 2M + 3 values ([XICYC] (e)). So if every seq_t(v) has at most B ascents,
  D_E(v) ≤ (2M + 3)·F′_B(M).

## 6. Ascents need upward Ξ-edges
**Lemma UP-JUMP (under [E-LEV]).** Let a, b be consecutive in seq_t(v) with b more relevant than a, and let a = e_(x,k) with
ℓ := lev(x). Then the play from a to b uses a β-vertex whose Ξ-target is a mover of level > the level of the mover it was entered from,
and ≥ ℓ.
Proof.
- ℓ ≥ 1: at level 0 a's successor is c_W and the play would have cycle node c_W, more relevant than a ∈ Π.
- So the play continues at the W-target y_a, a mover of level ℓ − 1 ([DEF]). b = e_(x′,k′) for a mover x′ on the play. By [E-LEV],
  b more relevant than a gives lev(x′) ≥ ℓ.
- Between a and b the play leaves each mover through a gate, to its e-face or its β-face. An e-face goes to a mover one level lower
  ([DEF]). A β-face goes either to u = K0, after which the play stays in the closed core and never reaches b ([DEF]), or to its
  Ξ-target mover.
- So levels change only at e-steps (down by one) and at Ξ-steps. The first step after y_a that reaches a level ≥ ℓ starts at a level
  ≤ ℓ − 1 and goes up, so it is a Ξ-step that goes strictly up. ∎

**Corollary UP-B (under [E-LEV]).** Let U(G) := the number of options (x, k) whose Ξ-target is a mover of level > lev(x). Then every
seq_t(v) has at most U(G) ascents, so D_E(v) ≤ (2M + 3)·F′_(U(G))(M) for every vertex v.
Proof.
- The segments of the play between consecutive e's of Π are disjoint parts of the play's prefix, whose vertices are distinct.
- Each ascent's segment contains a β-vertex whose Ξ-edge goes strictly up (UP-JUMP), and each β-vertex has one Ξ-edge. So distinct
  ascents use distinct upward Ξ-edges.
- Then apply §5. ∎

**Corollary NOUP (under [E-LEV]).** If U(G) = 0 (Ξ-cycles inside one level allowed), every seq_t(v) is descending, and
D_E(v) ≤ (2M + 3)(1 + M(M + 1)/2).

## 7. DATA (not to sign; every clause: unit, set, scope, tool; all tools in experiments/new/box193/, run by check193.sh)
- E-MON, CHAIN-DECOMP, E-DOM part of E-MON's proof: tmonfail 0, decfail 0, edomfail 0.
  - Units: consecutive state pairs at W-targets / (state, vertex) pairs / vertices.
  - Set: 13 instances. 8 frozen L-RED R217 instances in inst/ (sha1 = L-RED's own SHA1SUMS at claude/l-red 476710810: CLR_k8s16,
    FPORT_n2, FPORT_n3, LEAP_k8, RS2, RS2_L8M6, RS3, RSG_K4), plus box192/inst cR_d2_w8_R22, rd2_d9, rd2_d10, rd3_d7, rf_d5.
  - Scope: IDEAL-CYC. Tool: asc193.py.
- UP-JUMP: upfail 0. Unit: ascents in movers' plays with Λ below every e. Same set, scope and tool.
- UP-B: max ascents ≤ U(G) on 4 instances in check193.sh: RSG_K4 1 ≤ 1, RS3 2 ≤ 6, rd2_d9 3 ≤ 20, cR_d2_w8_R22 3 ≤ 9. 12 instances
  were run once. Unit: max ascents over (state, vertex) plays. Scope: IDEAL-CYC. Tool: ug193.py.
- NOUP: 300 random genomes with no strictly upward Ξ-edge; 179 of them Ξ-cyclic; max ascents 0; max D_E per Λ-interval 3. Unit:
  genomes / plays. Set: noup193.py 300 1. Scope: IDEAL-CYC.
- HUB-ASC(B), exact maxima with ONLY the hub constrained, CS(M) unconstrained otherwise: B 0: 11 at M 4 (= F_0); B 1: 16 at M 4, 29 at
  M 5. Unit: distinct hub values. Set: all runs of CS(M). Scope: abstract. Tool: hubasc193.py.
- SKELETON: violations 0. Unit: forests. Set: all forests of CS(4) and CS(5). Scope: abstract. Tool: skel193.py.
- Tightness of B = 0: F_0 is attained for M 1-7 (2, 4, 7, 11, 16, 22, 29). Unit: distinct hub values. Set: all runs. Scope: abstract.
  Tools: chain193.py (M ≤ 5, check193.sh), dp193.c (M 6, 7; data/cs_dp.txt).
- No separate DATA: Theorem HUB-ASC(B) for B ≥ 2 beyond hubasc193.py's B 1 rows; Corollary HUB-ASC-G's constants; the whole-run
  corollary of §5.
- Context, not a clause: with every chain limited to 1 ascent the exact maxima are 2, 4, 8, 16, 29, 50, 82 (M 1-7). F_1 is far from tight.

## 8. Machine checks
- check.sh block «P-N5-ASC»: sha1 of this packet and of every tool and instance it cites, against experiments/new/box193/asc.pins.
- check.sh block «BOX 193 ASC» re-runs check193.sh and diffs it against the committed check193.out. That covers asc193.py, ug193.py,
  hubasc193.py, skel193.py, dead193.py, chain193.py, noup193.py and the inst/ instances.

## 9. TARGET.md diff and limits
- TARGET.md §2 (M4) asks for an algorithm that is polynomial on every parity game. This packet proves no algorithm polynomial.
  - It bounds one quantity (D_E,I(v)) in one model (IDEAL-CYC of R104 / R118 genomes), under a hypothesis on v's plays (§5) or on G
    (§6, plus [E-LEV]).
  - The quantity is not a running time.
  - §4 of TARGET.md: a bound on a restricted class is not M4; the bound here is not even a running-time bound. Not M3.
- Limits:
  - The bound F_B is far from tight (degree 5·2^B − 3 against 2 and 3 in the data for B 0, 1) and super-polynomial if B grows like
    log M.
  - The step to R (OVT-DV, IN-BOUND) is not landed. HUB-ASC-G says nothing about R_mov directly.
  - [E-LEV] is a hypothesis of UP-JUMP, UP-B and NOUP. §3-§5 do not use it.
