# Box 217 (D18): QUIET-KEY as a one-player question — N5's key rule on a fixed one-player game (the quiet sub-window of box 216), a faithful one-player simulator, and a kill attempt by climbing one-player instances (STATEMENT first; OPEN; not a bound; G-N5-TIME stays OPEN; not M3, not M4)
L-NEW successor 76 (session_01V5yGRXFkFRGsbtdAPyKqXN), D1 / D14 / D18 / D21. STATEMENT written 2026-11-13 from 08:35Z (date -u), before
any run. Lead 08:31Z: «BOX 217 is APPROVED, re-framed as follows. Statement first.»; «(1) State QUIET-KEY as a ONE-PLAYER statement»;
«(2) The decisive DATA is NOT a closed form in d on the 5 towers»; «search directly in the ONE-PLAYER setting»; «Compare with Howard
(≤ 12 here) and with the seq rule as controls. Any growth claim needs a fit with residuals.»; «(3) … Do not cite anything unopened.»;
«(4) If (2) finds a one-player family with super-polynomial key-rule runs, report it to me before anything else.»
Labels: STATEMENT / OPEN (QUIET-KEY-1P), PROVED lane (the reduction §2 from landed lemmas), DATA (§4, not to sign).

## 0. Why one-player, and where the towers sit
Box 216 §7: on the five towers N5's key run before its first fallback has Q = 0, no gate flip, Σ_v (D^tot_E(v) − 1) = 0: ONE quiet
sub-window with G_C, faces and boundary constant (N5 30 to 299 steps; Howard 8 to 12). The towers are Ξ-acyclic, and there the
one-player game is explicit by landed results: [Q R122] «every optimal counterstrategy of Odd takes the β-face at every gate, and no play
from a non-e vertex contains an e-vertex» (Lemma BETA-ACYC, Ξ-acyclic genomes), and box 213's KEY-TAU (CANDIDATE) gives N5's choice.

## 1. The one-player model 1P(G) (definitions, as the simulator computes them)
Data: a genome G (RESULTS R104) whose Ξ-graph is acyclic: movers x = 0..N−1 with levels lev(x); each option k of x has a W-target
wt(x, k) (a mover of level lev(x) − 1, none at level 0), a Ξ-target xt(x, k) (a mover or the exit), a β-vertex b(x, k) of priority
6 + 2·br + bp (distinct, R104), and a gate number g(x, k) (distinct).
- States: s = (s(x))_x, one option per mover; start s_0 = G's start (S3 on Γ3 picks it: the start option's pad has priority 2, the
  others 0, box 189 gamma3.py).
- Ξ-value of option (x, k) under s (the [VJ] value of x's pad for that option, with Odd on the β-face by R122): follow
  x →k β(x, k) → xt(x, k) →s … to the exit; P := the set of β-vertices on that path; Ξ_s(x, k) := (weight(P), 5·hops), weight the
  si.Engine signed sum (+2^rank for even, −2^rank for odd priority; ranks by priority), compared lexicographically, longer better (the
  common cycle node K1 is odd, priority 5, below every β). The common suffix (pb, K0, pA, K3, K2, r, K1) adds the same to every value.
- A_s(x) := {s(x)} ∪ {k : Ξ_s(x, k) strictly better than Ξ_s(x, s(x))} (SPEC S2, S4a).
- KEY rule (KEY-TAU (i), box 213): s′ is computed level by level from level 0: s′(x) := the k ∈ A_s(x) with the least
  key_s′(x, k) := key_s′(wt, s′(wt)) ++ (ε(x, k)) (root-first tuple; (ε(x, k)) at level 0), compared lexicographically; ε(x, k) := the vertex
  index of e_(x,k) in the game N5 runs on (R241, L-RED 69: keys read by the e-index are numbering-free; box 189's Γ3 numbers the e-vertices in
  gate order, so there ε orders options as g(x, k) does). CORRECTED 08:41Z by date -u (Lead 08:40Z) from «g(x, k)»: the numbering is part of the input,
  chosen by the adversary, and the climb mutates it (gate swaps = e-order swaps on box 189's builder).
- A step s → s′; the key run stops at the first s with s′ = s (where N5 would fall back) or with no improving option at all.
  T_key(G) := its number of steps.
- Controls on the same model: HOWARD s′(x) := the Ξ_s-best option (unique: distinct β sets have distinct weights); SEQ: the key rule's
  s′ applied at the least-index mover where it differs.

## 2. Statement
**REDUCTION (PROVED lane, CONDITIONAL on KEY-TAU (i) and [IMP3]).** For every Ξ-acyclic genome G, N5's run on Γ3(G) from S3 up to its
first fallback, read at the movers, is the key run of 1P(G); so T_key(Γ3(G)) = T_key(1P(G)). Proof: R122 BETA-ACYC fixes Odd at every
gate on the β-face, so the Ξσ-value of a mover pad is Ξ_s of §1 (play x, m, g, pβ, β, xt, …: five vertices per hop; pads, gates and movers
lie below K1's priority 5 and are not in Π; K0, K3 are on every play); A_s is SPEC S4a's; KEY-TAU (i) gives the choice; [IMP3] and G-2
(box 213, PROVED lane: one window) give that nothing else moves. ∎ The simulator is checked against N5 itself (§4 (a)), so the DATA does
not rest on this proof.
**QUIET-KEY-1P (OPEN).** There is a polynomial p with T_key(1P(G)) ≤ p(N + M) for every Ξ-acyclic genome G.
- It is the one-player form of QUIET-KEY (box 216 §1.4) on Ξ-acyclic genomes, where by box 213's G-2 the whole key run is one window;
  and it is O1 itself, by the REDUCTION
  ([Q docs/new/N5-RFLEVEL-box212.md@d50ec578] «a generalised O1 (O1 is the Ξ-acyclic case, where the whole run is one window»). So QUIET-KEY-1P is not weaker than O1: it IS O1, in a
  model where one step costs O(N·M) instead of a Γ3 valuation.
- What it would give with LOUD-RF (box 216 §1.4): nothing beyond O1 for Ξ-cyclic genomes. QUIET-KEY for Ξ-cyclic genomes needs the same
  bound on every quiet sub-window (G_C fixed, boundary fixed, Ξ-cycles possible inside C); this box tests only the acyclic case.
**Kill criterion.** A family G_n of Ξ-acyclic genomes with T_key(1P(G_n)) super-polynomial in N + M (a fit with residuals on a constructed
or climbed sequence, then the simulator's numbers re-checked by N5 itself on Γ3 at the sizes where that is feasible) kills QUIET-KEY-1P,
hence O1 and O1′ (the towers become a family). Reported to the Lead before anything else (Lead's point (4)).
**Literature (point (3)).** Post-Ye arXiv:1208.5083 v2 (opened by successor 74; Thm 3.7, 4.8): Dantzig's rule, single switch, discounted
deterministic MDPs; not this rule, not this value order. Hansen-Kaplan-Zwick: NOT opened, not cited. Nothing else cited.

## 3. Plan (statement first; nothing run before this text)
- (a) Faithfulness: one217.py builds 1P(G) and runs KEY, HOWARD, SEQ. Must-0 mism: on every Ξ-acyclic genome checked, the KEY run's mover
  states differ from N5's (box 215 keyside215.states: n5v spec on Γ3, mover_state) at some step, or the lengths differ. Sets: the 5 towers,
  eg195 «acyc» random genomes (600), and every climbed record. Control: a deliberately wrong key (gate numbers permuted, as box 215's
  KS_CTRL=1) must give mism > 0.
- (b) Climb: hill-climbing on Ξ-acyclic genomes at fixed (N, degree 2) for N = 4, 6, …, 40: mutations of wt, xt (keeping acyclicity),
  br / bp, gate order and start; objective T_key(1P); records saved as JSON with sha1. Controls on each record: HOWARD and SEQ step counts.
- (c) Growth: for each N, the best T_key found; fits of log T vs log N (polynomial) and log T vs N (exponential) with residuals; no claim
  from a fit alone (climbs give lower bounds on max T, not the max).
- (d) Every record with T_key above the towers' size-matched value re-checked by N5 on Γ3 (mism 0 required).

## 4. DATA
(to be filled; nothing run yet)

## 5. TRACK A (proof attempt; Lead 09:08Z relaying the owner: «So put everything into trying solving it today»). STATEMENT, written
## 2026-11-13 09:11Z by date -u; labels per item; all for 1P(G), G Ξ-acyclic, any degree D, keys ε (R241 form)
Notation: K(x) := the set of keys of x (root-first W-paths from x to level 0, one ε per level: |K(x)| = Σ_k |K(wt(x, k))|, |K| = D at level
0); PΞ(x) := the set of Ξ-paths from x (one option per visited mover, to the exit); μ_t(x) := key_(s_t)(x, s_t(x)) (x's own key);
V_t(x) := Ξ_(s_t)(x, s_t(x)) (x's own Ξ-value); sw(x) := #switches of x in the key run.
- **A1 MONO-1P (PROVED lane).** μ_(t+1)(x) ≤ μ_t(x) and V_(t+1)(x) ≥ V_t(x) for every x, t; both strict when x switches at t. Proof. μ: by
  induction on the level; s_t(x) ∈ A_t(x), so μ_(t+1)(x) = min over A_t(x) of key_(s_(t+1)) ≤ key_(s_(t+1))(x, s_t(x)) = μ_(t+1)(wt(x, s_t(x)))
  ++ ε ≤ μ_t(wt(x, s_t(x))) ++ ε = μ_t(x) (induction at level − 1; level 0: the key is (ε), fixed); options of x have distinct last
  entries, so the argmin is unique and a switch makes the inequality strict. V: values are additive pairs (weight, hops) along a path
  and the lexicographic order is translation-invariant; in topological order of the Ξ-DAG (targets first), V_(t+1)(x) = β + V_(t+1)(xt′) ≥
  β + V_t(xt′) = Ξ_t(x, k′) ≥ V_t(x), the first by induction, the second because k′ ∈ A_t(x); strict when k′ ≠ s_t(x) (strictly better). ∎
  (This is KEY-TAU (ii) and F1 / STRICT restated inside 1P, proved there directly.)
- **A2 SWITCH-BOUND (PROVED lane).** sw(x) ≤ min(|K(x)|, |PΞ(x)|) − 1, hence T_key ≤ Σ_x (min(|K(x)|, |PΞ(x)|) − 1) ≤ N·(D^(1 + min_x-wise(lev(x),
  hΞ(x))) − 1)-type bounds; in particular T_key ≤ N·D^(1 + c·log N) = poly(N) on every Ξ-acyclic genome in which every mover has W-level ≤
  c·log N OR Ξ-height ≤ c·log N (D fixed). Proof: A1; μ(x) ∈ K(x) and V(x) takes values among the |PΞ(x)| path values (distinct sets
  give distinct weights), both strictly monotone at switches. ∎ So an exponential T needs movers that are DEEP IN BOTH graphs.
- **A3 PAIR-1P (PROVED lane).** A degree-2 mover whose two options have the same W-target, or the same Ξ-target (exit included), switches
  at most once: its key order (fixed last entries ε) resp. its Ξ-order (fixed β weights on a common V) never flips, and a second switch
  needs both orders reversed (§2 / box 216 JOINT). ∎
- **A4 HEREDITY (PROVED lane).** Say μ(y) ENUMERATES if it takes every value of K(y) during the run. If sw(x) = |K(x)| − 1 (x switches through
  every key), then μ(x) enumerates and, for every option k of x, μ(wt(x, k)) enumerates (while x holds k, μ(x) = μ(wt(x, k)) ++ ε(x, k), and
  every key of K(x) with last entry ε(x, k) is visited). And every one of x's |K(x)| − 1 switches flips x's Ξ-order (A3's argument at degree
  2): XF_x ≥ |K(x)| − 2, so V of x's two Ξ-targets change Ω(|K(x)|) times in total. ∎
- **A5 TIGHTNESS (DATA, out of box 217's tools; not a proof).** On the towers A2's key part is EXACT at the bottom levels: per level ℓ, the
  largest sw over level-ℓ movers vs |K| − 1 is 1/1, 3/3, 7/7, 15/15, 31/31, 63/63 (H6, levels 0-5) and up to 127/127 at level 6 (HIT7);
  above that the levels switch far below their key bound (HIT7 L7-L27: 33/255, 62/511, 96/1023, 32/2047, …, 1/2^28 − 1). Every
  fully-switching mover has fully-switching W-targets (12 on HIT7, 10 on H6; heredity counter 0, as A4 requires). The Ξ part is slack
  (|PΞ| = 3,195 to 11,791 for the fully-switching movers). So the towers are: k = 6, 7 bottom levels of FULL key enumeration (T ≥ 2^(k+1)),
  fuelled by d − k ≈ 3k upper levels.
- **A6 WHERE A POLYNOMIAL ARGUMENT FAILS (the exact step).** Nothing in A1-A4, KEY-TAU, XFLIP or JOINT bounds the ENUMERATION DEPTH
  k(G) := the largest k such that some mover of level k − 1 has sw = |K| − 1 (more generally: sw ≥ |K|^c). A2 is tight at k (HIT7: 127
  = |K| − 1 at level 6), so any polynomial bound must prove k(G) = O(log N), i.e. that full enumeration over k levels costs 2^Ω(k)
  fuel levels (or movers). The towers say the opposite trend so far: (k, d) = (4, 20) RECF4, (5, 20) H5, (6, 24) H6, (7, 28) HIT7, about
  three or four fuel levels per enumerated level. [CORRECTED 10:03Z by date -u, see A6′: the earlier text listed «(4, 20) DBL4» (wrong:
  DBL4 has k = 0 under this definition) and claimed «QUIET-KEY-1P ⟺ k(G) = O(log N)» (wrong direction: only ⇒ is proved).]
  A super-polynomial family = an infinite family with k(G) ≥ c·d^ε; L-LOWER L18's level-8 attempt is k = 8.
- **A6′ CORRECTION (Lead 10:03Z, relaying L-COMP 22 BOX 47 and L-RED 69's enum243.py; written 10:03Z by date -u).**
  (1) DBL4: its level-0 movers never switch (sw 0, |K| = 2), and at levels l = 1-4 its top movers switch 2^l − 1 = |K|/2 − 1 times (L-COMP 22,
  checked with one217.py; my own A5 run agrees: sw 15 at level 4, |K| 32). So DBL4 has k(G) = 0 as A6 defines k (full enumeration,
  sw = |K| − 1) and is a HALF enumeration (sw = |K|/2 − 1); L-RED 69's «DBL4 = 4» is a different (half-enumeration) count. A5's table rows
  are for H6 / HIT7 and are unchanged; the false entry was A6's «(4, 20) DBL4», now «(4, 20) RECF4» (RECF4: k = 4, sw 15 = |K| − 1 at
  level 3 and 30 at level 4).
  (2) What A2 actually proves. T ≤ N·max_x sw(x) and max_x sw(x) ≤ T, so QUIET-KEY-1P ⟺ SW-POLY: every mover switches at most poly(N + M)
  times. For c ∈ (0, 1] let k_c(G) := 1 + the largest W-level of a mover with sw(x) ≥ |K(x)|^c (0 if none; k_1 is A6's k; at c = 3/4 DBL4's
  level-4 movers qualify: sw 15 ≥ 32^(3/4) ≈ 13.5). Then QUIET-KEY-1P ⇒ k_c(G) = O((log N)/c) for every
  c (a mover of level l with sw ≥ 2^(c(l+1)) needs 2^(c·k_c) ≤ poly). The converse is NOT proved: sw could be super-polynomial while
  sw(x) < |K(x)|^c for every c (e.g. sw ≈ 2^√l). So ENUM-LOG (k = k_1 = O(log N)) is a NECESSARY condition for QUIET-KEY-1P, not a
  reformulation; the statement whose proof would give QUIET-KEY-1P is SW-POLY itself, and A2-POLY is the only sufficient condition proved.
  The kill side is unchanged: a family with k_c ≥ c′·d^ε for some fixed c is super-polynomial (it has a mover with ≥ 2^(c·k_c) switches).
- Next for track A: (a) an exact characterisation of what a level-k full enumeration demands of the Ξ side (A4 gives XF_x ≥ |K(x)| − 2 at
  the top enumerating mover; the Ξ-flips must come from switches of movers on x's Ξ-paths, which are themselves bounded by A2 — a
  counting argument between the two potentials is the candidate route to ENUM-LOG); (b) DATA: k(G) and fuel per level on every climbed
  record (track B).

## 6. TRACK A, referee unit (Lead 09:15Z: «write them as a referee-ready unit, with proofs in full and premises quoted»; written
## 2026-11-13 09:17Z by date -u). Labels: A1-A4 PROVED (lane, unrefereed) as statements about the model 1P(G) of §1; A2's corollary for
## N5 itself is CONDITIONAL on §2's REDUCTION (KEY-TAU (i), [IMP3]). Scope: G Ξ-acyclic, the key run up to its stop (N5: pre-fallback), D fixed.
### 6.1 Premises (all inside the model; nothing landed is used by A1-A4)
- The model 1P(G) exactly as §1 defines it: movers x with levels lev(x); every option (x, k) has a W-target wt(x, k) of level lev(x) − 1
  (none at level 0), a Ξ-target xt(x, k) (a mover or the exit; the Ξ-graph is acyclic), a β-vertex with a weight ω(x, k) = ±2^(rank) (sign
  by the parity of its priority; ranks distinct), and an index ε(x, k) (distinct over all options). c(x, k) := (ω(x, k), 1).
- Values: V_s(exit) := (0, 0); Ξ_s(x, k) := c(x, k) + V_s(xt(x, k)); V_s(x) := Ξ_s(x, s(x)); pairs add coordinatewise and are compared
  lexicographically (larger better). [This is the signed-weight comparison of si.Engine (its docstring: «M < N in Friedmann's set order iff
  weight(M) < weight(N)») on a path's β-set, then path length; that 1P equals N5 is §2 / §4 (a), not used here.]
- Keys: key_s(x, k) := (ε(x, k)) if lev(x) = 0, else key_s(wt(x, k), s(wt(x, k))) ++ (ε(x, k)); μ_s(x) := key_s(x, s(x)); tuples of one
  length (lev(x) + 1) compared lexicographically.
- A_s(x) := {s(x)} ∪ {k : Ξ_s(x, k) > Ξ_s(x, s(x))}. KEY step s → s′: by increasing level, s′(x) := argmin over k ∈ A_s(x) of key_s′(x, k)
  (key_s′ at x uses s′ only at lower levels, already fixed). Run: s_0 = G's start; stop at the first t with s_(t+1) = s_t.
- Counts: sw(x) := #{t : s_(t+1)(x) ≠ s_t(x)}; T := the number of steps; K(x) := the set of keys key_s(x, ·) over all states s and options;
  PΞ(x) := the set of Ξ-paths from x (a choice of one option at x and at every mover the path then visits, to the exit).
### 6.2 Statements and proofs
**Lemma 0 (facts).** (a) Distinct options of one mover have distinct keys (last entries differ); |K(x)| = Σ_k |K(wt(x, k))| (level 0: D),
so |K(x)| ≤ D^(lev(x) + 1). (b) Distinct Ξ-paths from x have distinct β-sets, hence distinct values; |PΞ(x)| ≤ D^(hΞ(x) + 1), hΞ(x) the
length of the longest Ξ-path from x counted in movers after x. (c) No two options of one mover have equal Ξ_s (b, applied at x).
Proof. (a) A key of x is the sequence of ε's of a W-path from x to level 0 (induction on the level), and the ε's are distinct, so distinct
W-paths give distinct keys; count by the first option. (b) Two different Ξ-paths from x first differ at some mover y, choosing options
k ≠ k′ there; the β of (y, k) is on the first path and not on the second: the second leaves y by k′ and, the Ξ-graph being acyclic, never
returns to y. Different β-sets have different signed weights (the most relevant differing rank decides the sign of the difference). ∎
**A1 MONO-1P.** For every mover x and step t: V_(t+1)(x) ≥ V_t(x) and μ_(t+1)(x) ≤ μ_t(x); both strict if s_(t+1)(x) ≠ s_t(x).
Proof. V, by induction along the Ξ-DAG, targets first. Let k′ := s_(t+1)(x), y′ := xt(x, k′). By induction (or y′ = exit) V_(t+1)(y′) ≥ V_t(y′),
so V_(t+1)(x) = c(x, k′) + V_(t+1)(y′) ≥ c(x, k′) + V_t(y′) = Ξ_t(x, k′) (the lexicographic order on pairs is invariant under adding a pair).
k′ ∈ A_t(x), so Ξ_t(x, k′) ≥ Ξ_t(x, s_t(x)) = V_t(x), strictly if k′ ≠ s_t(x) (definition of A_t). μ, by induction on the level. Let
k := s_t(x) ∈ A_t(x). μ_(t+1)(x) = min over A_t(x) of key_(s_(t+1))(x, ·) ≤ key_(s_(t+1))(x, k). At level 0 that is (ε(x, k)) = μ_t(x). At
level ≥ 1, with w := wt(x, k): key_(s_(t+1))(x, k) = μ_(t+1)(w) ++ (ε(x, k)) ≤ μ_t(w) ++ (ε(x, k)) = μ_t(x), by induction (tuples of one
length; appending one entry keeps ≤). If s_(t+1)(x) ≠ k, the minimum is attained only at s_(t+1)(x) (Lemma 0 (a)), so the first inequality
is strict. ∎
**A2 SWITCH-BOUND.** sw(x) ≤ min(|K(x)|, |PΞ(x)|) − 1 for every mover x, and T ≤ Σ_x (min(|K(x)|, |PΞ(x)|) − 1).
Proof. By A1, along the run μ(x) is non-increasing in K(x) and strictly decreasing at every switch of x, so x's switches are at most
|K(x)| − 1; and V(x) is non-decreasing among the values of PΞ(x) (Lemma 0 (b)) and strictly increasing at every switch, so they are at most
|PΞ(x)| − 1. Every step switches at least one mover (otherwise s_(t+1) = s_t and the run stops), so T ≤ Σ_x sw(x). ∎
**Corollary A2-POLY.** If D is fixed and every mover x has min(lev(x), hΞ(x)) ≤ c·log2 N, then T ≤ N·D^(1 + c·log2 N) = D·N^(1 + c·log2 D).
For N5 itself (CONDITIONAL on §2's REDUCTION: KEY-TAU (i), [IMP3]): the same bound holds for the number of iterations of N5 from S3 on Γ3(G)
before its first fallback, for every Ξ-acyclic genome G with that property. Not claimed: anything after the first fallback; Ξ-cyclic G.
**A3 PAIR-1P.** Let x have degree 2, options a, b. (i) If wt(x, a) = wt(x, b), then sw(x) ≤ 1. (ii) If xt(x, a) = xt(x, b) (the exit
included), then sw(x) ≤ 1, under ANY rule with s_(t+1)(x) ∈ A_t(x).
Proof. (i) key_s(x, a) − key_s(x, b) differ only in the last entry, so their order is the same at every state. A move to k ∈ {a, b} at t
needs k to be the key-least option of A_t(x) ⊆ {a, b}, in particular key-less than the other one if both are in A_t(x); a move from a to b
needs b ∈ A_t(x), and then key(b) < key(a); a later move back to a would need key(a) < key(b). (ii) Ξ_s(x, a) − Ξ_s(x, b) = c(x, a) − c(x, b)
at every state (common V term), so the Ξ-order is constant; a move from a to b needs Ξ(b) > Ξ(a), a move back the reverse. ∎
**A4 HEREDITY.** If sw(x) = |K(x)| − 1 then (i) μ(x) takes every value of K(x) and every change of μ(x) is a switch of x; (ii) for every
option k of x, μ(wt(x, k)) takes every value of K(wt(x, k)); (iii) if D = 2, x's Ξ-order (of its two options) alternates at least
|K(x)| − 2 times (XF_x ≥ |K(x)| − 2).
Proof. (i) A1: |K(x)| − 1 strict decreases inside a set of |K(x)| values visit all of them, and there is no room for a decrease without a
switch. (ii) When μ(x) = κ ++ (ε(x, k)), x holds k (Lemma 0 (a): the last entry names the option) and μ(wt(x, k)) = κ; every κ ∈
K(wt(x, k)) occurs (i). (iii) Box 216 §2 (XFLIP, proved for N5's moves; in 1P the same proof: every move of x goes to a strictly Ξ-better
option, the two options alternate, Lemma 0 (c) excludes ties): moves(x) ≤ 1 + XF_x. ∎
### 6.3 What the unit does not do
No bound on the enumeration depth k(G) (§5 A6); no statement for Ξ-cyclic genomes or after the first fallback; A2-POLY's class is a
restriction on the genome (log depth in W or in Ξ), not on N5. Related landed structure on 2-wide ladders: RESULTS R120 (P-TOWER-FUEL:
MOVE, DOUBLE-EQ, PULSE-NEST, GAP-NEST, DOMINANCE-FREEZE, CROSS-ECONOMY), stated in R104's IDEAL model; A1-A4 do not use it.

## 7. TRACK A, step 2: the Ξ-flip supply (Lead 09:15Z (3): «the Ξ-flip supply argument (A4 against A2's Ξ side) toward ENUM-LOG,
## statement first»). Written 2026-11-13 09:19Z by date -u.
**A7 FLIP-SUPPLY (PROVED lane; 1P, degree-2 mover x with Ξ-targets y_a, y_b).** XF_x ≤ #{t ≥ 1 : some mover on the Ξ-path of y_a or of y_b
under s_(t−1) switches at step t} ≤ Σ_(z ∈ Ξdesc(x)) sw(z), Ξdesc(x) the movers reachable from x in the Ξ-graph. Hence (XFLIP)
sw(x) ≤ 1 + Σ_(z ∈ Ξdesc(x)) sw(z).
Proof. Ξ_s(x, a) − Ξ_s(x, b) = c(x, a) − c(x, b) + V_s(y_a) − V_s(y_b); there are no ties (Lemma 0 (c)), so an alternation of the order at
state t needs V(y_a) or V(y_b) to differ between some earlier state and t, hence to change at some step; V_s(y) depends only on s at the
movers of y's Ξ-path under s, and a step that switches none of them leaves the path and the value unchanged. ∎
**A7′ what it gives against A4, and why COUNTING CANNOT PROVE ENUM-LOG (PROVED lane).** For the top mover x of a full block (level k − 1,
D = 2), A4 (iii) and A7 give Σ_(z ∈ Ξdesc(x)) sw(z) ≥ 2^k − 2. But the two level-(k − 2) movers of a full ladder block switch 2^(k−1) − 1
times each, i.e. exactly 2^k − 2 together: a block whose level-ℓ movers take their Ξ-targets one level down could supply every needed
flip from inside, with zero slack. So no argument that only counts switches (A2, A4, A7) can bound k(G): an ENUM-LOG proof must use the
TIMING and ORDER of the flips (as RESULTS R120's PULSE-NEST, GAP-NEST and DOMINANCE-FREEZE do), not their number.
**DATA (box 217 tools; not a proof).**
- Where the towers' supply comes from (unit: switches at step t of movers on the current Ξ-paths of the top full mover's two Ξ-targets,
  by W-level; whole run): H6 (top full mover 10, level 5, sw 63, Ξ-targets 11 (level 5, its PAIR PARTNER) and 8 (level 4)): level 0: 1,
  4: 31, 5: 63, 6: 32, 12-18: 12; HIT7 (mover 12, level 6, sw 127, Ξ-targets 33 (level 16) and 11 (level 5)): levels 2: 4, 5: 63, 6: 118,
  7: 16, 9: 56, 10: 31, 12-24: 58. So most of the supply is INTERNAL to the full block (the partner at the same level and the level below),
  the rest from the upper «fuel» levels (R120's CROSS-ECONOMY setting).
- The naive self-fuelling shape DIES: ladders with Ξ-target = W-target on every option (a switch below improves the same option in key AND
  in Ξ): climbs (objective (k(G), T), 30,000 proposals, d 3-10, two seeds) give T = d and k = 1 on every record; 20,000 random such ladders
  (d 2-9): no mover switches more than twice. CONJECTURE XTW-2 (untested beyond this): on Ξ = W ladders every mover switches at most twice.
  Free Ξ-targets on the same climbs: k ≤ 2, T ≤ 18 at d ≤ 10 (the climber is weak; the towers reach k = 7 at d = 28 by L-LOWER's recipes).
**Next (statement first, then data):** the timing form. R120's PULSE-NEST gives, inside a doubling stack, PULSE, GAP ≥ h − j; A7's supply is
consumed at specific steps (one flip per switch of the partner / level below). The candidate lemma: in a full block of depth k, the
supply steps of level ℓ must fall inside the windows R120 reserves, which forces at least f(k − ℓ) fuel switches per window from outside
the block; ENUM-LOG would follow if f grows exponentially, and fails if a construction keeps f constant. Not yet stated as a lemma.

### 6.4 The crux named by REFEREE-2 40's pre-read (claude/referee-2 dbedf93c, docs/referee-2/R2-key-preread.md §5; relayed by the Lead
### 09:44Z): where 1P(G) gets A_t. Answer: option (a), a rule on 1P(G)'s own state, PROVED equal to SPEC's A_t at the movers. Written
### 2026-11-13 09:44Z by date -u.
[Q docs/referee-2/R2-key-preread.md@dbedf93c] «A reduction «N5's run = 1P(G)'s key run» must say where 1P(G) gets A_t.» 1P(G)'s A_s(x) is
computed from 1P(G)'s own state s by §1 / §6.1 (Ξ_s from the Ξ-DAG and the β weights; no oracle). The bridge to Γ3:
**Lemma BRIDGE (PROVED lane; premises R122 BETA-ACYC, R117's Γ3 / standard states, [VJ]).** Let G be Ξ-acyclic and σ a standard state of
Γ3(G) whose mover part is s. Then for every mover x and options k, k′: Ξσ(m_(x,k)) ▷ Ξσ(m_(x,k′)) iff Ξ_s(x, k) > Ξ_s(x, k′). Hence SPEC S4a's
A(x) = {σ(x)} ∪ {w : (x, w) ∈ Iσ} is, read through the mover pads, 1P(G)'s A_s(x).
Proof. (1) [Q R122] «every optimal counterstrategy of Odd takes the β-face at every gate» (BETA-ACYC; its hypothesis «every Even strategy
that agrees with the stated start off the movers (transported through the pads on Γ3)» holds at standard states). So the play of
(σ, σ̄) from m_(x,k) is m_(x,k) → g → pβ → β(x,k) → then xt(x,k)'s own play if xt(x,k) is a mover, else pb → K0 → pA → K3 → K2 → r → K1 →
s → K1 (R117's Γ3 edges; σ̄(K2) = r by LOC-K2-3, R125). It never enters a pe pad, so it contains no e-vertex (an e-vertex's only in-edge is
from its pe pad, [Γ3]). (2) Every such play ends in the cycle K1 → s → K1 with cycle node K1 (priority 5), the same for all options. The
vertices of the play more relevant than K1 are its β-vertices (priority ≥ 6) and K0, K3 (on every such play); pads, gates, movers, pb, pA,
K2, r, s have priority ≤ 3 ([DEF], R125's (R)). So Ξσ(m_(x,k)) = (K1, {β's of the Ξ-path of (x, k) under s} ∪ {K0, K3}, ℓ) with
ℓ an increasing affine function of the number of movers on the path (five vertices per hop: m, g, pβ, β, the next mover;
  the exit tail is the same for every option): [VJ] compares equal cycle nodes by the signed rank-weight of the
symmetric difference of the Π-sets (K0, K3 cancel), then, K1 being odd, prefers the LONGER path. That is §6.1's order on (ω-sum, hops). ∎
- DATA for the same claim, state by state: §4 (a) (mism 0 on the 5 towers, on 23 renumbered towers, on 200 random Ξ-acyclic genomes).
**What the REDUCTION then needs, and nothing more:** KEY-TAU (i) for the choice (CANDIDATE, box 213; R2 pre-read: re-derived with no gap;
L-RED 69 R241: survives) with keys read by e-vertex index; [STD]/[IMP3] that N5 changes nothing but movers before its first fallback
(box 212 §6, lane). Pin: the numbering is the input game's; 1P(G) takes ε(x, k) := the vertex index of e_(x,k) in that game (one217.py
--numb / --renum build it from L-RED's renumbering; on box 189's Γ3 ε orders options as G["gate"]). Scope: Γ3(G), G Ξ-acyclic, N5 from S3,
states before the first fallback.
**«= O1», corrected:** §2's sentence «it is O1 itself» means O1 as box 212 §6 uses the name (N5's key run on Ξ-acyclic genomes, one window).
An identification with R104's IDEAL model (R104 / R118 vocabulary) is NOT proved here; DATA only: L-COMP box 29 measured R104's L(G) equal
to N5's T on the four towers it ran (claude/l-comp, experiments/comp/box29/README.md, «my simulator (box27/sim.py) gives L(G) = 136, 209,
67, 30 on them (= the Lead's T)»), and one217.py's key T equals N5's T on the same towers.
