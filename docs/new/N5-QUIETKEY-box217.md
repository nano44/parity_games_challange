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
  fuel levels (or movers). The towers say the opposite trend so far: (k, d) = (4, 20) DBL4, (5, 20) H5, (6, 24) H6, (7, 28) HIT7, about
  three or four fuel levels per enumerated level. **OPEN (QUIET-KEY-1P ⟺ k(G) = O(log N) up to the polynomial factors of A2 — conjecture
  form ENUM-LOG).** A super-polynomial family = an infinite family with k(G) ≥ c·d^ε; L-LOWER L18's level-8 attempt is k = 8.
- Next for track A: (a) an exact characterisation of what a level-k full enumeration demands of the Ξ side (A4 gives XF_x ≥ |K(x)| − 2 at
  the top enumerating mover; the Ξ-flips must come from switches of movers on x's Ξ-paths, which are themselves bounded by A2 — a
  counting argument between the two potentials is the candidate route to ENUM-LOG); (b) DATA: k(G) and fuel per level on every climbed
  record (track B).
