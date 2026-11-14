# L7: a seventh capped level without the return chain (L-LOWER successor 7, BOX L7)

Box: Lead brief (L-LOWER successor 7; D1 / D14 / D18), GO 2026-11-07 18:45Z. Items: (2) read L-COMP 11's RC-PLATEAU test; (3) BOX L7:
design a seventh capped level with no Ξ-path from q₅ into pair 6 by construction. Written from 19:00Z (date -u).
Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA / DEAD / READING. Every DATA clause names its counter (unit, set, scope).
Nothing here is a result in the sense of CLAUDE.md; G-N5-TIME stays OPEN. Not a TARGET.md claim (§9).

## 0. Model, notation, tools
- Model and notation as docs/lower/L6-supplier.md §0 (R104's IDEAL rules; simulator l6/sim6.py; pair j = movers 2j, 2j + 1;
  c_j = o(j − 1); j-window = maximal run of steps with c_j constant). closure(x) = movers reachable from x by Ξ-edges of either option.
  q₅ = the member of pair 5 that moves second in its 5-windows (DOUBLE-EQ (E5): one member, mover 10, in every genome below).
- 5-window [t₀, t₁) is INNER if no mover of pairs 0-4 moves at a step t₀ < t < t₁.
- Tools (experiments/lower/l7/): ranksolve.py (exact rank/sign feasibility for a fixed wiring and target trajectory, §4), clamp.py
  (clamped completion, ideal pair 6), runstats.py (§2), rcfree.py, ideal.py (§4), xorbrute.py (§5). Frozen copies of L-COMP's
  genomes: l7/rec/LCOMP_*.txt (sha1 in §1).

## 1. L-COMP 11's RC-PLATEAU test, read (item 2; DATA)
- Source: claude/l-comp af466f89 (snapshot 17:50Z), experiments/comp/box30/out/. Frozen genomes (sha1 of the bytes read):
  L6_TEST1_d28.txt c7a32d08b84554808f9c423d92974ee0d83ec1df (= D_l6_TEST.txt), L6Z_TEST1_d28.txt a7cca69a8c88f92e07597b3d6e3f708f8b91e8ab
  (= D_l6z_TEST.txt), L6_BEST_D_l6_d28.txt 43e8b5def35e915ebae3a8e5706f367b75094d91, D_l6z_best.txt
  1ef15c3b3c2596087a9eabbc49264d6d4f5b765d. Lane logs: D_l6 STOPPED 17:41Z (replaced by the gated D_l6g, which has no file in this
  snapshot); D_l6z unit 0 best F(6) 190. L6_BEST (L-COMP's name) is not in the snapshot under that exact name; L6_BEST_D_l6_d28.txt is read.
- Re-run here with two simulators (l6/sim6.py and l5/fev.c, built from source; unit = genome; set = the four files; scope = stored
  start): identical T and F-profile on all four; guard_l6.py 'noreturn' ok on all four (levels 0-5 capped, q₅ = 10, npaths(q₅, pair 6) = 0):
  | genome | T | F(6) |
  | --- | --- | --- |
  | L6_TEST1_d28 | 202 | 117 |
  | L6Z_TEST1_d28 | 258 | 160 |
  | L6_BEST_D_l6_d28 | 200 | 134 |
  | D_l6z_best | 249 | 190 |
- So CONJECTURE RC-PLATEAU (j = 6 role form) SURVIVES this test: every RC-free genome with levels 0-5 capped found so far has
  F(6) ≤ 190 < 222. Not a proof (annealing, not exhaustive). The D_l6g lane is unread (no file yet).

## 2. Two window lemmas and what they say about RC-free towers
- Lemma WINDOW-CAP (PROVED, lane; R104 movement rule). Let l ≥ 1 and [t₀, t₁) an l-window (c_l changes at t₀, is constant on
  t₀, …, t₁ − 1). Then o(l) changes at no more than 2 steps of the window, and at no more than 1 if t₁ − t₀ = 1. Hence
  F(l) ≤ 2·W_l − W¹_l, W_l = number of l-windows, W¹_l = number of l-windows of length 1.
  Proof. o(l) at step t is a function of s_t(2l), s_t(2l + 1) and c_l(t). Inside the window c_l is constant, and each member of pair l
  moves at most once there (it moves only to c_l, and only if it is not there). So o(l) can change only at t₀ and at the steps of
  member moves. If both members move, both sat on ¬c_l at t₀ − 1: the pair was joined, and a joined pair's o(l) is its gate value,
  which does not depend on c_l, so o(l) does not change at t₀; at most 2 changes. Otherwise at most 1 + 1. A length-1 window has one
  step. ∎
- Lemma PULSE-TRIGGER (PROVED, lane; R105 ENC, acyclicity, movement rule). Let j ≥ 1 and [t₀, t₁) a j-window in which both members of
  pair j move, the first at u₁, the second (q) at u₂ > u₁. Then some mover of closure(q) moves at step u₂ − 1 (≥ t₀).
  Proof. q moves at u₂, so pref_q(s_(u₂−1)) = c, c = c_j on the window, and s_(u₂−1)[q] ≠ c. At step u₂ − 1 ≥ u₁ ≥ t₀ the key is c too, q is
  not on c and does not move, so pref_q(s_(u₂−2)) ≠ c. By ENC, pref_q(s) is the sign of the top option of chain_s(q, 0) △ chain_s(q, 1);
  these chains consist of q's two options and options of movers of closure(q), followed along their current states. So s_(u₂−2) and
  s_(u₂−1) differ on closure(q). ∎
- Corollary DECOUPLED (PROVED, lane; from the two lemmas). If closure(q₅) contains no mover of level ≥ 6, then in every INNER 5-window
  in which both members of pair 5 move, PULSE_5 = u₂ − u₁ = 1. (The mover moving at u₂ − 1 is in closure(q₅); if u₂ − 1 > u₁ it moves
  strictly inside the window, so it is not in pair 5 (each member moves once there), not in pairs 0-4 (inner) and not of level ≥ 6.) ∎
  Each such window bounds a 6-window [u₁, u₂) of length 1 whenever both pair-5 moves change c_6, and then WINDOW-CAP costs one flip.
- Corollary GUARD (PROVED, lane). Under guard_l6 'noreturn' (no Ξ-path from q₅ into pair 6), in every inner 5-window with
  PULSE_5 ≥ 2 the mover of closure(q₅) that moves at u₂ − 1 has level ≥ 7. A seventh capped level needs F(6) = 2·127, so by WINDOW-CAP
  every 6-window has length ≥ 2. With levels 0-5 capped every pair-5 move changes c₆ (o(5) changes 126 times; it can change only at
  c₅ changes, where pair 5 is joined and o(5) is its gate value, or at the 126 pair-5 moves, DOUBLE-EQ: one per member per 5-window),
  so u₁ and u₂ bound a 6-window: every inner 5-window needs PULSE_5 ≥ 2 and hence such a level-≥7 trigger. Keys of levels ≥ 7 change inside a 5-window
  only at pair-6 moves or helper moves, so in an RC-free tower the news «pair 6 has finished its first 6-window» can reach q₅ only
  through the key cascade above pair 6 (a helper keyed by o(6) that fires when q₆ joins). READING: that is the RC-free route; the
  climbs use it (below), but in too few windows.
- DATA (runstats.py → runstats.out; unit = 5-window; set = the 63 5-windows of each of SL41_d28, G7_best_d28 and the four L-COMP
  genomes of §1; scope = stored start). In every window with PULSE_5 ≥ 2 the closure(q₅) movers moving at u₂ − 1 include one of level
  ≥ 6; a lower-only trigger occurs 0 times (consistent with PULSE-TRIGGER and the inner/outer split). Inner windows: 40 or 41 per genome.
  | genome | F(6) | inner, PULSE_5 = 1 | inner, PULSE_5 ≥ 2 | 6-windows of length 1 | WINDOW-CAP bound |
  | --- | --- | --- | --- | --- | --- |
  | SL41_d28 (RETURN-CHAIN) | 222 | 0 | 40 | 0 | 254 |
  | G7_best_d28 (RETURN-CHAIN) | 222 | 9 | 32 | 30 | 224 |
  | LCOMP D_l6z_best (RC-free) | 190 | 24 | 17 | 24 | 230 |
  | LCOMP L6Z_TEST1 (RC-free) | 160 | 39 | 1 | 40 | 214 |
  | LCOMP L6_BEST_D_l6 (RC-free) | 134 | 40 | 1 | 68 | 186 |
  | LCOMP L6_TEST1 (RC-free) | 117 | 40 | 0 | 72 | 182 |
  Lemma checks (l7check.py, run by check.sh; unit = (genome, level) and j-window; set = the six genomes, levels 1-7 and windows of
  levels 1-6 with two staggered moves; scope = stored start): WINDOW-CAP 0 violations on 42 pairs, PULSE-TRIGGER 0 violations on 940 windows.
  In the RC-free genomes the inner windows that keep PULSE_5 ≥ 2 use triggers of level 7 (D_l6z_best: lowest trigger level 7 in 31
  of its 39 PULSE_5 ≥ 2 windows) — the key-cascade route above. In SL41 the lowest trigger level is 6 (a pair-6 member: the RETURN-CHAIN) in 47 of 63.

## 3. D18 connection: rank design is decision-list consistency (computational learning theory ↔ strategy-improvement lower bounds)
- Observation (PROVED, lane; R105 ENC). Fix a wiring (xt, gates, start) and a target trajectory s₀, …, s_T. The run reproduces it
  iff at every step t and every mover x whose move is not blocked (level ≥ 1: s_(t−1)[x] ≠ c_x(t); level 0: its gate allows the
  switch), pref_x(s_(t−1)) = s_t[x]. (If x is not blocked, it moves iff it prefers the other option; if blocked, it does not move.)
  By ENC each such condition says: «the top-rank option of Δ = chain(x, 0) △ chain(x, 1) at s_(t−1) has the sign σ», σ fixed per
  element by its side. So rank design for a fixed wiring and trajectory is the consistency problem of a DECISION LIST: order the
  options (a list of tests) and give each a sign (its output) so that every example's first applicable test outputs its label.
- Lemma GREEDY-COMPLETE (PROVED, lane). The greedy that repeatedly takes an option on which all open conditions containing it agree,
  gives it the next highest rank and that sign, and closes those conditions, finds an assignment iff one exists.
  Proof. If it finishes, every condition was closed by its first-picked element, which is its top, with the agreed sign. Conversely
  let (r*, σ*) be an assignment and suppose the greedy is stuck with open set O. Open conditions contain no picked element (a pick
  closes every condition containing it). Let e be the r*-largest element occurring in O; e is the top of every open condition containing
  it, so all of them require σ*(e): e is pickable. Contradiction. ∎
- Tool ranksolve.py (constraints, solve). Validation (ranksolve_SL41.out; unit = genome; scope = stored start): SL41's wiring and
  run give 6,023 conditions; the greedy solves them, and the genome rebuilt with the solved ranks reproduces SL41's trajectory
  exactly (T 290, F identical). So, unlike annealing, a «no» from ranksolve is exact for its (wiring, trajectory) pair, and its
  open set says which movers are pulled both ways.

## 4. Exact tests on SL41 (DATA; unit = genome; scope = stored start; ranks and signs of ALL movers free)
- RC-free realizations of SL41's own trajectory (rcfree.py → rcfree_SL41.out): (a) one of 10:0, 10:1, 55:0, 55:1 re-pointed to any
  mover or exit, acyclic, closure(10) ∩ {12, 13} = ∅: 104 genomes, 0 realize SL41's trajectory; (b) both 10:0 and 10:1 re-pointed:
  2,704 genomes, 0 realize it; mover 10 is in the open set of every one. So F(6) = 222 itself is not available RC-free by re-pointing
  q₅'s options in SL41's wiring.
- The ideal pair 6 on SL41's wiring (ideal.py → ideal_SL41.out). Sanity: clamping movers 0-13 to SL41's own run reproduces it,
  feasible. Target: SL41's pairs 0-5 unchanged, pair 6 doubling (first mover 13 at t₀ + a, second 12 at t₀ + a + b in every 6-window),
  every other mover completed by its own rules (clamp.runclamp). For (a, b) = (0, 1) and (1, 1): target F(0..6) = 2, 6, 14, 30, 62,
  126, 254, but 34 movers of levels 6-24 change trajectory (o(6) changes, and the key cascade carries it up), and the target is
  infeasible: EVERY mover 0-13 has an infeasible own condition set (no ranks at all realize it on SL41's wiring). (a, b) = (0, 2):
  17 movers change, movers 0, 4, 6-13 infeasible alone.
- READING (COUPLING-UP): SL41's capped levels are fuelled by helpers above pair 6 (§2: triggers of levels 6-24), and those helpers are
  clocked by o(6). Making pair 6 double changes their schedule and with it every lower level's fuel, whatever the ranks. A
  perturbation that fixes level 6 must therefore also re-build levels 0-5: this is a mechanism for the plateau of perturbative
  climbs (L6 §7 found the local reasons at level 6 only). A seventh capped level has to be designed with the final helper schedule.

## 5. The top pair needs a «split» detector, and one reader cannot compute XOR (DATA; CONJECTURE)
- Requirement (READING, from the schedule). In the sequential schedule (f_j moves one step after
  each key change, q_j one step after the last move of the higher levels), the first mover of pair 6 must, after each pair-5 move,
  prefer the new c₆ = o(5), which is g₅ XOR [f₅ ≠ q₅]: over the four pair-5 phases AA → BA → BB → AB → AA its preference must follow
  XOR(s_f₅, s_q₅) (the 5-window context w, constant within a 5-window and changing between consecutive ones, distinguishes the halves).
- DATA (xorbrute.py → xorbrute.out; exhaustive; unit = wiring; set = every acyclic wiring under every topological order of a reader x,
  input movers a, b (two live options each) and fixed nodes (one live option); exact feasibility by GREEDY-COMPLETE):
  pure XOR(a, b) with two fixed nodes: 84,000 wirings, 0 realize it. With the context input w (the six visited (w, f₅, q₅) combinations
  of the schedule) and one fixed node: 180,000 wirings, 864 realize it, e.g. x:0 → w, x:1 → a, w:1 → b, a:0 → b.
- CONJECTURE ONE-READ XOR (tested only in the scope above): with the states of all movers other than a, b fixed, no mover's preference
  equals XOR(s_a, s_b) on all four combinations. Consequence (READING): the split detector of a doubling pair needs a context mover whose
  own options point into the pair below (here w:1 → q₅): its wiring then also decides w's own preference, so the detector couples to w's
  fuel. This is the same coupling as §4, seen locally.

## 6. BOX L7 outcome (labels as stated)
- Success criterion (F(6) = 254 with six capped levels below, RC-free by construction, two simulators + xcheck) NOT met: no genome built.
- Exact obstructions found, at instances: (i) COUPLING-UP (§4, SL41_d28 sha1 c1b46c31…): on SL41's wiring the ideal pair 6 is
  infeasible for every lower mover even with all ranks free, because 34 helper trajectories above pair 6 change; (ii) RC-free q₅
  (§2, PROVED): every inner 5-window (40-41 in every genome read) needs a level-≥7 trigger of q₅ firing at u₂ − 1, available only through
  the key cascade above pair 6; the RC-free climbs supply it in at most 17 of 41 (D_l6z_best); (iii) the split detector (§5): XOR is not
  realizable by one reader (DATA, exhaustive in the stated scope), so the top pair needs a context mover wired into pair 5.
- What is built: an exact pipeline for a designed construction — target trajectory (clamp.py) + wiring → ranksolve (exact). Next step
  (not run): write the sequential schedule for pairs 0-7 explicitly (pair 7 = the two o(6)-keyed helpers that tell q₅ «pair 6 done»),
  choose per-mover reading sets from the tables of §5, enumerate the wirings consistent with them, and decide each exactly.
- Design sketch for the RC-free q₅ trigger (READING; hand-derived tables, not run). Pair 7 = (h, h₂), both keyed by o(6); G = g₆,
  N = ¬g₆; pair 5 moves f₅ at u₁, f₆ at u₁ + 1 (reads f₅), q₆ at u₁ + 2. pref(h) = G iff s_f₅ = B (h reads f₅): in a 5-window with key B, h
  sits on N, becomes armed at s_(u₁) and fires to G at u₁ + 2 together with q₆ (o(6) returns to G); in the next 5-window (key A) h fires
  to N at f₆'s move. h₂ is the mirror (pref G iff s_f₅ = A, also reading h). Then q₅'s preference on the visited (s_f₅, s_h, s_h₂) is the
  decision list «h₂ = G → A; else h = G → B; else ¬s_f₅», which moves q₅ at u₁ + 3 in both window types (PULSE_5 = 3) with no Ξ-path into
  pair 6. Untested: the wiring this needs (q₅:B → h₂ → h → f₅) also fixes h's and h₂'s own preferences; the sign of (f₅, A) is pulled
  both ways (q₅ needs +, h₂ needs −) unless the rank order separates them. That is the first input for the ranksolve pipeline.
- RC-PLATEAU: survives L-COMP 11's frozen tests (§1). DECOUPLED and GUARD (§2) are partial explanations, not a proof: they cap F(6)
  only through the count of inner windows without a level-≥7 trigger.

## 7. Files (experiments/lower/l7/)
ranksolve.py, clamp.py, runstats.py, rcfree.py, ideal.py, xorbrute.py, l7check.py (run by check.sh); outputs runstats.out, ranksolve_SL41.out, rcfree_SL41.out,
ideal_SL41.out, xorbrute.out; rec/LCOMP_*.txt (frozen copies, sha1 in §1).

## 8. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class; all are about the IDEAL
model's step sequence (R104's definition) on 𝓛^R_d and its F-profile. Not M3, not a step-4 pass, not a TARGET.md claim.
