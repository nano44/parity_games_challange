# L14: the sink at level j: what is forced, and where the proof stops (BOX L14; L-LOWER successor 13)
Labels: PROVED (lane) / CONJECTURE / DATA / DEAD. Lead «go» 08:33Z 2026-11-09. Every DATA clause names its counter.
Model: the IDEAL model of RESULTS R104 at degree ≤ 2, as simulated by experiments/lower/l6/sim6.py (R104 step, ENC of R105).
Tools: experiments/lower/l14/ (README.md). Target core8 = experiments/lower/l10/out/core8_HIT7.txt (sha1 c6e19673).

## 0. Facts of the model used below (R104 definition; sim6.run lines 57-70)
- (M1) Ξ-graph: an edge y → xt(y, k) for every option (y, k) whose Ξ-target is a mover. It is ACYCLIC (R104's premise for every
  genome considered here, and enforced by every tool: sim6.topo, ann.c, enc32). closure(y) := the movers reachable from y in it;
  y ∉ closure(y).
- (M2) better_y(S) ∈ {0, 1} := the option of y with the larger Ξ-value under S. It depends only on the states of closure(y)
  (R105 LOCAL). The two values never tie (the two options' own β differ; R105 ENC). av_y(S) ⇔ s(y) ≠ better_y(S).
- (M3) Movement at step u (row u−1 → row u), level L ≥ 1: y moves iff av_y(S_(u−1)) and s_(u−1)(y) ≠ c_L(u), where
  c_L(u) := o(L−1)(S_u) (keys read under the NEW row, built level by level). If it moves, s_u(y) = c_L(u) = 1 − s_(u−1)(y).
- (M4) o(l)(S) for l ≥ 1 depends only on the states of pair l and on o(l−1)(S): split pair (a ≠ b): o(l) = [a ≠ o(l−1)];
  joined pair (a = b): o(l) = a gate comparison, a constant given a.
- (M5) On core8 (core gates of levels 0-7 as in core8's definition: C10, C11 and C12 carry them unchanged), o(7)(S_t) alternates at
  every row t = 0, 1, … (DATA, exact; set = rows 0..510; L10 §2a «o(7) changes at every step»; checked again on rows 0-19 of C11's
  clamped run: 0 1 0 1 …). o(7) is a function of the core rows and the core gates, so (M5) holds in EVERY realization of core8 with
  those gates.

## 1. «Reaches none» (PROVED, lane): which acyclicity, which graph, which base property
- Setting. A base genome B (fixed), a mover x (the sink), a set G of movers with x ∉ G. A REWIRING of (B, x, G) is any genome B′
  that has the same Ξ-targets as B on every option of every mover outside G ∪ {x}; the options of x and of G are arbitrary, and
  ranks, signs, gates, starts are arbitrary everywhere. B′ is required to have an acyclic Ξ-graph (M1). This is exactly the class
  of the L13 / pgad3 questions, without pgad3's candidate filter (pgad3's lists are a subset).
- Base property. A_B(x, G) := the movers y ∉ G ∪ {x} that have a Ξ-path y = v0 → v1 → … → vm = x in B with v1, …, v(m−1) ∉ G ∪ {x}.
- Lemma SINK-AVOID. For every rewiring B′ of (B, x, G): closure_B′(x) ∩ A_B(x, G) = ∅, and no mover of closure_B′(x) has any
  member of A_B(x, G) in its closure.
- Proof. Let y ∈ A_B(x, G) with its path v0 … vm. Each edge v(i) → v(i+1) (i < m) is an option of v(i) ∉ G ∪ {x}, so it is
  unchanged in B′, and y reaches x in the Ξ-graph of B′. If y ∈ closure_B′(x), x also reaches y: a cycle in B′'s Ξ-graph,
  contradicting (M1). If z ∈ closure_B′(x) had y ∈ closure_B′(z), then y ∈ closure_B′(x) (closures are transitive). ∎
- How big A is (DATA, exact; l14/mincut.py; counter = helper vertex cut κ(y) := least number of helpers (movers ≥ 16) whose
  removal destroys every Ξ-path from core mover y to x in B; y ∈ A_B(x, G) for EVERY helper set G with |G| < κ(y)):
  | base, sink | κ(y) for core y |
  | --- | --- |
  | C10 (3ef36801), f5 = 11 | 0, 1: 2; 2-5: 4; 6-10: 2; 12, 13: 2; 14, 15: 3 |
  | C11 (c2e925f7), q4 = 8 | 1: 0 (f0 does not reach q4); 0, 11: 1; 3, 5, 7, 9, 10, 12, 14, 15: 2; 13: 3; 2, 4, 6: ∞ (core-only path) |
  | C11, f5 = 11 | 0-9: 0 (pairs 0-4 do not reach f5: L10's cut); 10, 12, 13: 1; 14, 15: 2 |
- Corollary SINK-FLOOR (PROVED, lane; SINK-AVOID + PREF-FUEL of L13 §2). Every rewiring of (B, x, G) that realizes core8 rows
  0..P has |closure(x)| ≥ log2(R_x(P) + 1), and closure(x) avoids A_B(x, G) as above. On the full target (P = 510) a core mover of
  pair j ≤ 6 has R = 2^(j+1) − 1 (L13 §2 DATA), so |closure(x)| ≥ j + 1.
  Instances. C10, x = f5 (j = 5), any helper set |G| ≤ 1: every core mover has κ ≥ 2, so closure(f5) holds no core mover and no
  helper that reaches a core mover; it is a set of ≥ 6 helpers reading no core mover at all. C11, x = q4 (j = 4), |G| ≤ 1:
  closure(q4) ∩ core ⊆ {0, 1, 11}, with ≥ 5 members. This is the «reaches none, size ≥ j + 1» statement, PROVED with c = 1.

## 2. Timing: the key channel (KEY-DELAY, CAUSE: proofs written; DATA check)
- Lemma KEY-DELAY (PROVED, lane; M4, M5). Let L ≥ 9 and r ≥ 1 with o(7) different on rows r−1, r and on rows r, r+1. If
  o(L−1)(S_(r−1)) = o(L−1)(S_r) ≠ o(L−1)(S_(r+1)), then some mover of a pair 8..L−1 moves at step r or at step r+1.
  Proof. Suppose not: rows r−1, r, r+1 carry the same states on pairs 8..L−1; call them P. By (M4), going up from level 7,
  o(L−1) = F_P(o(7)) where F_P is constant if some pair of 8..L−1 is joined in P, and F_P(z) = z ⊕ (a constant) if all are split.
  o(L−1) differs between rows r and r+1, so F_P is not constant, hence a bijection; o(7) differs between rows r−1 and r, so
  o(L−1) differs there too: a contradiction. ∎
- Lemma CAUSE (PROVED, lane; M1-M5). Let y, of level L ≥ 1, move at step u. Let a be the least row such that for every row t in
  [a, u−1], s_t(y) = s_(u−1)(y) and av_y(S_t). Then
  (i) if a ≥ 1, a mover of closure(y) moves at step a;
  (ii) o(L−1)(S_t) = s_(u−1)(y) for every row t in [a+1, u−1], and o(L−1)(S_u) ≠ s_(u−1)(y) (y was BLOCKED at steps a+1..u−1);
  (iii) if a ≤ u−3 and L ≥ 9 (with M5), a mover of a pair 8..L−1 moves at step u−1 or u; if L = 8, a ≥ u−2.
  Proof. (i) At row a−1 either y's state differs (y moved at step a, to better_y(S_(a−1)) by M3; av_y(S_a) says better_y(S_a) ≠
  s_a(y) = better_y(S_(a−1))) or the state is the same and av_y(S_(a−1)) fails (better_y(S_(a−1)) = s ≠ better_y(S_a)). Either
  way better_y changes between rows a−1 and a, so by (M2) a closure mover changes state at step a. (ii) For t in [a, u−2], av_y(S_t)
  holds and y does not move at step t+1, so by (M3) s = c_L(t+1) = o(L−1)(S_(t+1)); at step u it moves, so s ≠ o(L−1)(S_u).
  (iii) If a ≤ u−3, rows u−2 and u−1 lie in [a+1, u−1]: KEY-DELAY with r = u−1. If L = 8, o(7) alternates, so (ii) allows at
  most one blocked row: a ≥ u−2. ∎
- DATA (l14/cause.py; counter = moves of movers of level ≥ 1 in the free sim6 run; violations of (i) and (iii) counted):
  HIT7_lift_d32 (l9/rec, T 299): 1,101 moves, 0 violations ((i) applied 1,083 times, (iii) 45 times). PG_C10_X11_k2_t16 (T 16):
  79 moves, 0. PG_C4_X13_k2_t10 (T 11): 82 moves, 0. The check runs the genome FREE (its own core gates), so (M5) is tested per row.

## 3. The exact place where «size ≥ c·j» stops, and the smallest configuration (item 1 result)
- What closes. «Reaches none»: §1, by acyclicity of the Ξ-graph alone, for helper sets below the cut κ. «Size ≥ j + 1»: PREF-FUEL.
  Together: SINK-FLOOR (c = 1). Nothing stronger follows from Ξ-reach.
- The step that fails. Any argument of the form «the sink's private closure must itself carry the timing, so it must be large»
  needs the closure's moves to be timed by the closure. By CAUSE (ii)-(iii), a closure member y of level L ≥ 9 can sit blocked for
  any number of rows and be released by o(L−1) alone, and o(L−1) is a function of the STATES of pairs 8..L−1 and of o(7) (M4).
  Those pair movers are W-neighbours, not Ξ-neighbours: they need not lie in closure(x), and they may read the core (q7, f7 move
  at every step) through their own Ξ-edges. So a closure that reaches no core mover can still be timed by the core, through the
  helper levels' o-cascade. PREF-FUEL is tight in COUNT for this reason: a closure member with an EMPTY closure moves once, at a
  step that its key chooses. The cost moves from the Ξ-closure to the helper pairs below it; it does not disappear (KEY-DELAY: each
  release after ≥ 2 blocked rows needs a helper move one step before or at the release), but nothing in §1-§2 bounds it below by c·j.
- Smallest configuration showing it: C11, sink q4, first required change. Lemma C11-TIMING (PROVED, lane; scope: any genome whose
  options of q4 (8), f0 (1), h43 (43) have C11's Ξ-targets (q4 → f0, h43; f0 → exit, exit; h43 → exit, f0), acyclic, core gates of
  core8, any other wiring, ranks, signs, gates, starts) that realizes core8 rows 0..14:
  (a) h43 moves exactly once in steps 1..14, at step 13 (row 12 → 13);
  (b) o(20)(S_t) = 1 − b on rows t = 1..12 and o(20)(S_13) = b, where b = better_43, constant on rows 0..253;
  (c) some helper of pairs 8..20 (movers 16..41) moves at step 12 or 13.
  Proof. closure(q4) = {f0, h43}, closure(h43) = {f0}, closure(f0) = ∅. In core8, f0 first moves at step 254, q4 at step 14
  (DATA, exact, from the target file). With C11's core gates q4 is free at pre-states 0..13, required to stay at 1 on 0..12 and to
  move at 13 (l13/reqpref.py: list (0..12, 1), (13, 0)). By (M3) av_q4 is false on rows 0..12 and true on row 13, so better_q4
  changes between rows 12 and 13; by (M2) f0 or h43 changes state at step 13, and f0 does not: h43 moves at step 13. better_43
  depends on s(f0) only, constant b on rows 0..253; h43 moves only to b, and once there it stays: one move, at 13; so
  s(h43) = 1 − b on rows 0..12 and av_43 holds on rows 0..12. CAUSE with u = 13, a = 0 gives (b), and CAUSE (iii) with L = 21
  gives (c). ∎
  Here R_q4(14) = 1, so the count needs one closure move, and the closure {f0, h43} has it. The wall at 14 (L13 §4, Lemma C11-WALL)
  is not a count: it is (b)-(c), a demand on the helper pairs 8..20 to hold o(20) for 12 rows and flip it at row 13. DATA (C11's own
  clamped run, l10/build.fulltraj; counter = rows 0..19): o(20) = 1 on all of them, h43 never moves, and the only helper that moves
  at step 13 is 17 (pair 8). So C11's helper cascade does not deliver the release; L13's pgad3 questions (f5 and ≤ 2 helpers
  rewired) cannot change h43's release time except through the states of pairs 8..20, and they do not.
- Status. Item 1 is CLOSED with c = 1 (SINK-FLOOR) and OPEN beyond it. The open part is exactly: a lower bound on the number of
  helper-pair movers needed to realize a prescribed release pattern of o(L−1) (KEY-DELAY demands), i.e. the tower problem on the
  helper levels, which is CONJECTURE OSC-ROOM of L10 §3c in a sharper form:
  CONJECTURE KEY-ROOM (lane). If a sink of pair j must change at steps t_1 < … < t_R prescribed by core8 (R = 2^(j+1) − 1), then
  the helper pairs below the levels of closure(x) must realize, through KEY-DELAY releases, a pattern needing Ω(j) helper pairs
  that are not shared with the timing of pairs j+1..7. Not proved; HIT7's shared cascade (no sink) is the reason it may be false
  in general, and it is stated only for bases with a sink.
- What this does NOT exclude. Other bases (HIT7-like bases with no sink, §4 of L13), other towers, other targets than core8, helper
  sets at or above κ (§1), and N5 in general: none of §1-§3 bounds an N5 run on any game. All statements are about the IDEAL
  step sequence of genomes against core8 rows.

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. All statements are about
the IDEAL model's step sequence (R104's definition) on degree-≤-2 genomes and core8's rows. Not M3, not a gauntlet step-4 pass,
not a TARGET.md claim.
