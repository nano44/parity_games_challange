# R-box209-preread: PRE-READ (NOT A SIGNATURE) of L-NEW 72's box 209 (Lemma LEVEL3, Lemma PLATEAU3, Theorem T3-ALL, Corollaries N5XI-G3, FLIPS3) and its Addendum A
REFEREE successor 33 (D1 «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the
fleet's own, as wrong until it passes the gauntlet below.»). Date -u at writing: 2026-11-12T18:35Z. Lead 17:53Z item C.
This is a read to find errors early. It is not a referee signature: nothing is frozen as a packet, every statement of the box is labelled
CANDIDATE by its lane, and a packet review, if one comes, is a separate signature.
Object: claude/l-new 311bbf81 (ancestor of origin/claude/l-new, checked), docs/new/N5-LEVEL3-box209.md, sha1
147c889b53695933a6703a70f6ec192c16cc6d04, 43,451 B, 377 lines (body = 3f896099's file, sha1 94356803…; `git diff` removes 0 lines).
Prior work of this lane, disclosed: R-box208-preread.md (successor 32, 7524342b), the pre-read of the Γ(G) form. I read its report, not
box 208 itself; box 209 redoes every step on Γ3 and I re-derived each from box 209's text.
Not read before this verdict: docs/referee-2/, L-RED's and L-RED-B's records, L-SI's box 103 Addendum B, the lane's tools (level208.py,
plat209.py, struct209.py; my counters are written from the box's statements), box 208, box 210. Read: the box, the landed entries R104,
R117, R118, R121, R123, R124, R125 in docs/RESULTS.md (trunk 68c8d293) where quoted, my lane's xicyc_replay.py (Γ3 builder, HOW3).

## 0. Verdict
| statement | verdict |
| --- | --- |
| §1 premises, [Q] quotes | **21 [Q] bullets, 34 quotes, 0 missing** (scratch/box209_quotes.py, log box209_logs/quotes.out); 33 lie in an entry the bullet names; the 34th is the [OPT] wording, in R122 and not R118: exactly Addendum A (1)'s correction |
| §2 class facts (K0′)-(K5′) | **no gap found** (§1) |
| §3 Lemma LEVEL3 (L1′)-(L5′) | **no gap found** (§2) |
| §4 Lemma PLATEAU3 (i): (P1)-(P7) | **no gap found**; (P6) is in the REPAIRED form (Odd answers with σ̄_s of the plateau state s: G-P6 of R-box208-preread does not recur); wording notes N-1 ((P2)'s citation), N-2 (H0 in (P7)) |
| §4 PLATEAU3 (ii) (the tail; new against box 208) | **no gap found** (§3) |
| §5 Theorem T3-ALL, Corollary N5XI-G3 (with Addendum A (2): under 1E-N3), Corollary FLIPS3 | follow from §2-§4 and landed R125 REACH3-ALL / R124 END-T3; counting re-done; **no gap found** |
| Addendum A (1), (2) | correct (the quote script finds the string in R122 only); (3)-(5) are records, not statements |
No FALSE statement found; no instance against any step. Own replay with own counters (§4): 30 must-be-0 counters all 0 on the lane's
90 frozen genomes (53 + 37), 26,500 random genomes of eight shapes and 1,200 mutants; my T3 equals the lane's maxima on the
frozen sets (199, 114, and 10 / 19 / 21 on the three DEAD_SEG2P genomes).
What this read does NOT establish: that the bound is right. It says that I re-derived every step and found none missing. D1 stands:
the claim is a polynomial bound for N5′-xi on ALL genome games Γ3(G), no run comes near the constants, and it is two days old. It is a
statement about a restricted family (TARGET.md §4): by box 104's Lemma WRAP (R-WRAP-preread.md, also a pre-read) N5′-xi is, on wrappers
of arbitrary games, exactly as slow as Howard's rule, so nothing here points at M4. G-N5-TIME stays OPEN.

## 1. The class facts: re-derived
- (K0′): the core is frozen in HOW3 and σ̄(K2) = r (LOC-K2-3), so the eight values are constant; the core is entered only by pb_g → K0;
  K0, K3 are above K1. So for a vertex outside the core: Λ = K1 ⟺ the play enters the core ⟺ K0 ∈ Π ⟺ K3 ∈ Π; c_W is a self-loop.
- (K2′), the hinge: equal Λ, different E. The top z of Π Δ Π′ is at least as relevant as the top z_E of E Δ E′, so by E-DOM3 it is an
  e-vertex, c_W, K0 or K3; (K0′) excludes the last three; so z = z_E, even, and the VJ order is the class order. It needs both values to
  be values of vertices OUTSIDE the core; every use is such ((K1′), (K4′): faces; (K5′): the triple ext(x, Ω_t(y)) has y's (Λ, Π)
  because a mover is in no Π, CN2-3).
- (K3′): (b) from B-ONLY3 (an e-vertex on a cycle would have Λ at least as relevant as itself; the excepted vertices play into c_W's
  loop); (c), (d), (e) as written. (K4′): LOC-GATE3, NO-TIE3, (K2′). (K5′): DOM on HOW3 (R125's fact list), then (K2′).
- Counted (§4): k0, k1, k2 (same state, t / t + 1, and two random states), k3a, k3c, k3d, k3e, k4, k5: 0.

## 2. LEVEL3: re-derived
- (L1′): as box 208's (L1), from (K1′) only. (L2′): the constants never lag; an e-vertex with mover successor w has a class that is a
  function of w's and lies above it ((K3′ d)), its pad pe_g has e's class; a β with successor pb_g is constant. What is left is the
  five kinds listed.
- (L3′): from a front vertex the play stays in the front or leaves LAG; the leaving vertex z is not an m-pad, pβ or β (one frozen
  successor: class_b(z) = class_b(w) = class_t(w) = class_t(z)), not a gate ((K4′) at b and (K1′) squeeze class_b(z) = class_t(z)); so
  it is a mover and m_t = class_b(σ_t(z)). Otherwise the cycle is in the front, its node has Ω ≥ 3 (CN2-3; c_X is not in the front),
  so it is a β-vertex c with class (c, ∅).
- (L4′): each of the three inclusions of the map s re-derived (mover: (K3′ c) at b, (K5′), the stall; one-successor vertices: (K3′ c)
  at t and b; gate: (K4′) at t and b, then (L2′) excludes pe_g). A cycle of s exists and has the shape mover, m-pad, gate, pβ, β.
- (L5′): at most M classes of m-pads at b and M classes (c, ∅); 1 ≤ |FRONT| ≤ N + 4M.
- Counted: l1 (incl. «exactly as many non-stall steps before b′ as values of Φ»), l2, l3, l3v, l4, l4c (the cycle of (L4′), with its
  shape), l5, c4, for reference T3 and two random references: 0. Both cases of (L3′) occur (table).

## 3. PLATEAU3 and T3-ALL: re-derived
- (P1)-(P3): as written ((P3) needs u < v for the state u; the inequality at s = v follows by constancy).
- (P4): cases (1), (2) by (K4′) and (P1). Case (3), equal classes of both faces: e_g's successor is a mover (else Λ(pe_g) = c_W, while
  pβ_g is not among B-ONLY3's exceptions), e_g ∈ E(pe_g) = E(pβ_g), so pβ_g's play passes e_g, whose only in-edge is from pe_g, whose
  only in-edge is from g ((D1′); true of my builder): σ̄_s(g) = pe_g at every s. Case (3) OCCURS in my runs (table, column «(P4) case
  (3)»), and the counter p4c (σ̄ = pe_g there) is 0.
- (P5): on [u, v] the plays from Y stay in Y and use H's edges; movers of Y have all successors in Y. Counted against my own VJ engine
  run on H itself: p5v (values), p5h (each step legal for Howard on H's own values): 0.
- (P6): the induction runs over s ≤ s′ ≤ b, past the plateau, and carries exactly «σ = σ_s on the movers of Y, Ω = Ω_s on Y». Step (a)
  uses the successors of x being in Y (a fixed set, (P3)) and «keeps a best current one»; step (b) answers σ_(s′+1) with σ̄_s, the
  PLATEAU state's reply, whose plays stay in Y by (P2) at s. No fact is used outside the states it was proved for. Correct.
- (P7): v − u steps of H's Howard run, each switching a mover (P6), with constant cycle nodes on Y (P1) and no Odd choice: p-steps.
- (ii): on [b′, T3] no class changes, so (P4)'s cases (2), (3) fix σ̄ on every gate; H := Γ3(G) with every non-mover at its successor of
  state b′; every step before T3 switches a mover by the definition of T3; BR-SEG-G (a) gives T3 − b′ ≤ n_E3. Counted: t1 (σ̄ changes on
  the tail), t2, and p5v / p5h / p6 on the tail with H := all of Γ3: 0.
- T3-ALL: b′ = Σ over the at most P3 intervals of (stall steps + 1) ≤ P3·(n_E3 + 1); T3 − b′ ≤ n_E3. n_E3 = N + 6M + 9 and
  n = N + 7M + 10 recounted on every game built (counter nE 0). N5XI-G3: REACH3-ALL and END-T3 are landed (R125, R124) and need 1E-N3
  (Addendum A (2)); §2-§4 use of the tie rule only «a ⊴-best successor, keeping a best current one». FLIPS3: D^tot_E(v) is, in R125's
  line, «the number of distinct classes of v over the run», at most T3 + 1.
- Notes (wording; none changes a statement):
  - N-1. (P2) cites (K3′ c, d). For an e-vertex with successor c_W neither applies; there class(e) = class(c_W) = (c_W, ∅) (e is below
    c_W, so e ∉ Π(e)). Add the case, or let (K3′ e) say «equal to (c_W, ∅)».
  - N-2. Landed BR-SEG-G's H0 is a hypothesis on EVERY step of the Howard run it speaks of. For H it holds at every step of H's own run
    (only movers have a choice in H, and a mover is never a cycle node, CN2-3); (P6) is what makes the plateau's steps steps of that
    run. (P7) should say both. With the Lean theorem `PG.brsegG` (hypotheses on the segment only) nothing more is needed; it is
    «Lean-checked (lane)» until CHECKER passes it (my build of claude/l-formal f74d38a4, a referee's build: 3,179 jobs, no sorry / admit /
    axiom line, 46 theorems within [propext, Classical.choice, Quot.sound]; logs box209_logs/lean_*.out).
  - N-3. The Γ3 readings (D1′), (D3′), (D4′) and E-DOM3 are readings of R117 / R104's text, not quoted lines; they hold on my builder
    (written from that text by successor 26). A packet should cite them as P-N5-CHAIN §5 / P-N5-QN §1 do.

## 4. Replay with my own code (scratch/box209_replay.py; logs scratch/box209_logs/; every run `python3 -I`)
- Engine: my lane's xicyc_replay.howard(G, pad = True): own Γ3(G) builder, own VJ valuation and Odd reply, HOW3 with the tie rule «keep if
  best, else the larger index». 30 must-be-0 counters written from box 209's statements (header of the script).
| log | genomes | states | max T3 | sum of the 30 must-0 counters | stalls (reference T3) | plateaus checked, three references | longest tail | (P4) case (3) gates | states with (α) / (β), three references | controls |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| files_box202.out | 53 | 1,699 | 199 | 0 | 48 | 33 (longest 13) | 0 | 3 | 3477 / 64 | c_k4 567,683, c_k5 5,858, ch1 612, ch2 3,144, ch3 1,572, ch4 2,870, ch4c 1,245, ch5 1,572, c_Y 264 |
| files_other.out | 37 | 1,352 | 114 | 0 | 87 | 63 (longest 9) | 4 | 14 | 2397 / 179 | c_k4 306,588, c_k5 5,420, ch1 297, ch2 1,936, ch3 968, ch4 1,697, ch4c 761, ch5 968, c_Y 660, c_l3v 2,397 |
| gen_acyc.out | 400 | 829 | 4 | 0 | 0 | 0 (longest 0) | 4 | 0 | 0 / 0 | c_k4 8,823, c_k5 0, ch1 0, ch2 0, ch3 0, ch4 0, ch4c 0, ch5 0, c_Y 0 |
| gen_big.out | 1,500 | 9,221 | 13 | 0 | 324 | 413 (longest 4) | 7 | 9 | 3349 / 11494 | c_k4 334,797, c_k5 24,920, ch1 570, ch2 12,738, ch3 6,369, ch4 2,773, ch4c 1,408, ch5 6,369, c_Y 486 |
| gen_deep.out | 400 | 1,407 | 8 | 0 | 57 | 80 (longest 3) | 3 | 3 | 875 / 1003 | c_k4 23,365, c_k5 1,303, ch1 67, ch2 1,682, ch3 841, ch4 316, ch4c 157, ch5 841, c_Y 120 |
| gen_noX.out | 3,000 | 7,416 | 9 | 0 | 166 | 302 (longest 3) | 3 | 4 | 1446 / 6515 | c_k4 79,260, c_k5 3,135, ch1 255, ch2 6,442, ch3 3,221, ch4 985, ch4c 501, ch5 3,221, c_Y 152 |
| gen_rand.out | 400 | 1,016 | 7 | 0 | 25 | 41 (longest 2) | 3 | 4 | 546 / 557 | c_k4 10,940, c_k5 581, ch1 35, ch2 870, ch3 435, ch4 150, ch4c 78, ch5 435, c_Y 52 |
| gen_selfl.out | 400 | 1,026 | 8 | 0 | 30 | 50 (longest 3) | 2 | 0 | 608 / 605 | c_k4 10,865, c_k5 710, ch1 55, ch2 934, ch3 467, ch4 152, ch4c 79, ch5 467, c_Y 56 |
| gen_tiny.out | 20,000 | 34,649 | 5 | 0 | 569 | 1071 (longest 2) | 3 | 0 | 9265 / 10577 | c_k4 145,810, c_k5 6,951, ch1 359, ch2 12,304, ch3 6,152, ch4 1,626, ch4c 846, ch5 6,152, c_Y 1,188 |
| gen_wide.out | 400 | 1,063 | 7 | 0 | 33 | 60 (longest 2) | 2 | 1 | 619 / 571 | c_k4 12,542, c_k5 671, ch1 51, ch2 748, ch3 374, ch4 171, ch4c 93, ch5 374, c_Y 81 |
| mut_fixed.out | 1,200 | 29,888 | 33 | 0 | 3125 | 2733 (longest 20) | 26 | 330 | 55629 / 651 | c_k4 2,914,845, c_k5 53,066, ch1 9,180, ch2 47,792, ch3 23,896, ch4 46,447, ch4c 20,884, ch5 23,896, c_Y 50,961 |
| all | 27,790 | 89,566 | | 0 | | | | | | |
- Sets: files_box202 = the 53 corpus genomes (sha1sum -c: 53 OK); files_other = the 37 genome files of box191 / 203-207 inst (the three
  DEAD_SEG2P genomes of R118 (m) and the frozen k = 1 records; sha1sum -c OK for boxes 203-207); gen_* = own generators (end_replay.gen:
  rand, deep, wide, selfl, acyc; box208_replay.own_gen: tiny, noX, big); mut_fixed = 150 mutants of each of eight frozen genomes.
- Controls that fire: c_k4, c_k5, ch1-ch5 with ch4c (FRONT := the highest lagging class), c_Y, c_l3v. The counters k0-k3e, c4, p1, p3-p7,
  t1, t2, tb, nE have NO firing control; ch3v never fires (under that control (α) and (β) both fail first, ch3).
- Limits, stated plainly: no run comes near a constant (longest T3 199 against a bound above 10^10; longest plateau 20 steps (a mutant; 13 on the frozen genomes); longest
  tail 26 steps); exact Howard ties are rare, so «any tie rule» rests on the proof; one engine (mine) under my counters. Large zero
  counts are DATA, not evidence of the theorem.

## 5. The genome-only steps, and scope
- As in R-box208-preread §7: (K2′) / (K3′ b, d) from B-ONLY3 and E-DOM3; (P4) case (3) from (D1′); (K5′) from DOM; Odd's only choices are
  two-faced gates. Friedmann's games violate E-DOM (odd vertices above lower exits); box 104 §5 runs them through N5′-xi.
- TARGET.md diff: no algorithm, M3 or M4 is claimed; the scope line («HOW3(G) on Γ3(G) … Not N5, not another start, not another game,
  not M4; G-N5-TIME stays OPEN») is right. N5XI-G3 would make N5′-xi polynomial on {Γ3(G)}: a restricted class (TARGET.md §4).

## 6. For a packet
- P3-1 (required): N-1, N-2, N-3 in the text; Addendum A (1), (2) folded into §1 and the corollary.
- P3-2 (required): the DATA clauses with the lane's units; the lane's tools were not opened by me (DATA rule to do).
- P3-3 (the Lead's call): one packet with P-N5-LEVEL or a second one; box 209 does not use box 208 as a premise.

## 7. Tools and outputs (docs/referee/scratch/)
box209_replay.py, box209_quotes.py, box209_summ.py, box209_run.sh; box209_logs/: quotes.out, files_box202.out, files_other.out, gen_*.out,
mut_fixed.out, summ.out (the table above), run.log, lean_build_tail.out, lean_grep.out, lean_axioms.out. (mut.out: a first run with wrong
base paths, kept as it failed.)
