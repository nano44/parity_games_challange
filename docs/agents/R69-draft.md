# Draft RESULTS R69 (Lead, 2026-10-26 13:03Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C78 (rev. 2026-10-26 13:19Z: C78 E-1..E-3, N-1, N-3, N-4) — LANDED in RESULTS Results 2026-10-26 13:34Z (CHECKER C78 Add. 1 978791e1 PASS), after R68

### R69 [refereed-only] N5 on EVERY game, inside one phase: a change of Ξ at an Odd choice vertex (a ρ event) needs an Even switch on an exit path from Q (ROOT); at a terminal on no honest cycle, a ρ event that is not caused on its own route is relayed from another terminal of its class (ROUTE-RELAY), never with one Odd choice vertex per class (SELF-FREE); per class, with the exits included, unchanged exit paths and exits keep κ (ROOT-C, corrected form); on an interval with no fallback and σ̄|Q, Ξ|Q fixed, N5 runs on two fixed one-player games (STATIC); and a relay flip between two terminals q1, q2 needs a switch on q1's old exit path, overlapping exit paths, or a strict rise of κ(q2) by at least the weight of an Odd-unattractive cycle C (FLIP, N1 ∨ N2 ∨ N3); when C's top lies above c (and, if it lies on q2's exit path, that path is intact at t1), q2's path set changes at a rank ≥ that top (N3-LEVEL) (2026-10-26) — structural lemmas for N5 beyond one Odd choice vertex (no count: the number of flips and of ρ events per phase is not bounded here; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C78.md, checker PENDING)
- Object (packet P-N5-FLIP, added at l-si 7ea3d8cf, pinned trunk d67fdb87, unchanged during review): docs/si/P-N5-FLIP-box18.md, sha1
  96a7e088c2175f71ab1aef2577d6139f80a4efff (L-SI successor 14, Opus 5.5). The referees' notes and repairs are collected by the lane in
  docs/si/P-N5-FLIP-fixes-box18.md (l-si b5d3d321, sha1 93a65e1b7e1df4a1d19a16c1f5ebb794e1d4331b, L-SI successor 15: G-FLIP-1..3 with the
  referees' repair texts, FLIP-N1..N4, N-FLIP-1..4; 23 quotes checked by script); on trunk; repairs only.
  Setting (every game): phases as in RESULTS R38 (a); Q := the Odd vertices of out-degree ≥ 2; classes, U_c, κ, κwt_c and ρ events as in
  RESULTS R56 and R61; for q ∈ Q and y ∈ succ(q), the Q-EXIT PATH of y at s is the play from y in G_{σ_s} up to and including the first vertex
  in Q or repeated; for q ∈ Q_c, the EXIT of y ∈ succ(q) ∩ U_c is the first vertex of Q_c ∪ {c} on y's honest play, and its CLASS EXIT PATH
  the part strictly before it; a ρ event at q is ROUTE if some such y has a different class exit path or exit at t and t + 1, RELAY
  otherwise. A FLIP is (q1, q2, t1 < t2) in one phase with par_{t1}(q1) = q2 and par_{t2}(q2) = q1, exit paths p1 := p_{t1}(q1), p2 :=
  p_{t2}(q2), closed walk C = q1·p1·q2·p2.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: RESULTS R38 (a), R56 (setting,
  (d) κ-Y-FORM_D, named also in ROUTE-RELAY's premise line, FLIP-N1), R57 (a) and the standing SPEC premise 1E-N3 in its two forms (P1:
  S1's σ̄ is Odd's pointwise optimum in G_σ; P2: S4a's step is Even's optimum in its arena), R62 (d) WM-G's premise line, R15 (a), (d) via
  (VJ) ((SG)), R61 (a), (e). P1 only: ROOT, ROUTE-RELAY, SELF-FREE, ROOT-C, FLIP (b); P1 and (SG): FLIP (a), (c), N3-LEVEL, and the necessary condition (from (a)-(c)); STATIC uses P2
  only (N-FLIP-1, REFEREE-2; accepted by REFEREE):
  (a) Lemma ROOT: if at an in-phase transition t → t + 1 every Q-exit path is the same at t and t + 1, then Ξ_t = Ξ_{t+1} on Reach_t(Q);
      so every transition carrying a ρ event switches some Even vertex on a Q-exit path.
  (b) Lemma ROUTE-RELAY: for q ∈ Q_c on no honest cycle at t and t + 1, a RELAY event at q has a SOURCE: an exit e ∉ {q, c} with κ_t(e) ≠
      κ_{t+1}(e), or with e's honest play avoiding q at exactly one of t, t + 1. Corollary SELF-FREE: if Q_c = {q}, every such ρ event at q is
      ROUTE.
  (c) Lemma ROOT-C, corrected form, SIGNED WITH GAPS G-FLIP-1 (= ROOTC-2) and G-FLIP-2 (= ROOTC-1), both closed (both referees; the packet's literal form NOT SIGNED: FALSE): if at an in-phase transition every class exit path AND EXIT
      of every q′ ∈ Q_c (from every y ∈ succ(q′) ∩ U_c) is the same at t and t + 1, then κ_t(q) = κ_{t+1}(q) for every q ∈ Q_c; so every
      transition with a ρ event at a terminal of class c changes a class exit path or exit of class c. As written in the packet (exit paths
      only), ROOT-C is FALSE: an Even last vertex can switch exits without changing its path (witnesses n4_thch_0, sha1 77018c63, found by
      both referees, and REFEREE's rootc_lit_n5, sha1 602e6db6). Its proof's step "each walk is the play of a positional Odd strategy with
      cycle node c" is false when a walk leaves c's honest cycle at an Odd vertex on it (G-FLIP-2 = ROOTC-1, both referees; witnesses
      leanT_N6 and best_tog_83); the conclusion stands by REFEREE-2's repair, the Bellman inequality B(e, y): κ_s(e) ⪯ κwt(e) + κwt(p_y) +
      κ_s(e′) along the walk's steps, with REFEREE's equivalent LOCAL form κ_s(e) ⪯ κwt(e) + κ_s(y) as a remark (P1 only; the two are the same inequality by additivity, both referees; both referees accept either).
  (d) Lemma STATIC: on a ρ-FREE INTERVAL I (a maximal run of in-phase transitions with no fallback and Ξ|Q, σ̄|Q constant), σ̄_k = σ̄_I on all
      Odd vertices and τ_k = τ_I, so I is a run of "improve in G_{σ̄_I}, choose by G_{τ_I}" on two fixed one-player games ("Ξ|Q constant" is part of the cut and not used in the proof, REFEREE).
  (e) Lemma FLIP: (a) FLIP-COST: κ_{t2}(q2) ⪰ κ_{t1}(q2) + wt(C); (b) FLIP-1: if p1 is intact at t2, the cycle that q1's play reaches in
      G_{σ_{t2}} when q1 re-chooses σ̄_{t1}(q1) has a node w with rew(w) > rew(c); (c) Corollary: if moreover p1 ∩ p2 = ∅, that cycle is C,
      wt(C) ≻ 0, and κ(q2) rises strictly between t1 and t2 by at least wt(C). NECESSARY CONDITION at every flip: (N1) an Even vertex of p1
      switches between t1 and t2, or (N2) p1 ∩ p2 ≠ ∅, or (N3) κ(q2) rises strictly between t1 and t2 by at least wt(C), C an
      Odd-unattractive cycle through q1 and q2.
  (f) Lemma N3-LEVEL, SIGNED WITH GAP G-FLIP-3 (minor; REFEREE-2, accepted by REFEREE): for a flip with p1 ∩ p2 = ∅, with h the
      highest-ranked vertex of C, rank(h) > rank(c) and h even (and, if h ∈ p2, p2 intact at t1), q2's path set changes between t1 and t2 at
      a rank ≥ rank(h). The packet's parenthesis "(both hold when p1 is intact at t2, by (c))" does not follow: (c) gives only the
      disjunction "rank(h) > rank(c) with h even, or rank(h) < rank(c) with c odd"; it is unproved, not shown false (the second alternative
      occurs in neither referee's data), and is replaced by that disjunction; the lemma under its explicit hypotheses is unaffected.
- Not signed (packet §7, §8): CONJECTURE FRZ-RHO; ROOT-C's strong form (all relays chain to a route event; DATA); the READINGs (in
  particular that N3 flips of a pair are at most 2^{#ranks ≥ top(C)}); the data. The flip type "C below an odd c" left open by G-FLIP-3 is
  OPEN.
- Honest limits: (i) Structural lemmas: no count of flips, ρ events or phases is given; N1 flips (switches on the old exit path) are not
  charged here, and in the OPEN case "C below an odd c" (G-FLIP-3) N3's rise is a pure length rise, by at least |C| (fixes R3). (ii) N3-LEVEL's sharpness pin leanT_N6 is reproduced by REFEREE (its
  three equalities) but not by REFEREE-2 (no multi-state phase from its starts; it sees equality 80 times elsewhere). (iii) Lane work after
  the packet (L-SI 15's CHOSEN and RELAY-CHAIN, L-RED 21's N3-CHAIN in R87) is not part of this entry.
- Data (DATA, not proof): REFEREE (successor 14, own engine; lane code not run): 0 failures of every signed item with ROOT-C in its
  corrected form; lib41 1,101 runs, 5,365 phases, 1,002 flips, 12 N3-LEVEL checks; random games n 5-24 (12,000 runs); pp_K12 with its start,
  60 flips, all N3, 60 N3-LEVEL checks; ROOT-C's min formula in 105k+ checks and the LOCAL inequality in 462k+; controls: FLIP-COST with
  wt(C) doubled fails 55 times, strict N3-LEVEL fails 3 times on leanT_N6. REFEREE-2 (successor 16, own flip_check.py with its own play
  values and walks; lane code not run): 17,245 N5 runs, 13,876 ρ events, 0 violations of every signed check; ROOT-C's exits form 0
  failures, the walk-form conclusion 10,993 checks; on its 𝒞^1O set every event is ROUTE (SELF-FREE); mutations root, cost and lev bite.
- Signatures: REFEREE docs/referee/R-N5-FLIP.md (referee 8317a435, §C 72db1b18, successor 14): ROOT, ROUTE-RELAY, SELF-FREE, STATIC, FLIP
  (a)-(c), the necessary condition SIGNED; ROOT-C as written NOT SIGNED (ROOTC-2), corrected form SIGNED WITH GAP ROOTC-1, closed by the
  repair; N3-LEVEL SIGNED WITH GAP G-FLIP-3 (in its §C, accepting REFEREE-2's finding); notes FLIP-N1..N4. REFEREE-2
  docs/referee-2/R2-N5-FLIP.md (referee-2 e9044674, §C 75b8b52a, successor 16): the same items SIGN; ROOT-C SIGN WITH GAPS G-FLIP-1, G-FLIP-2; in its §C, adopting REFEREE's wording: as written NOT SIGNED (false), corrected form SIGNED WITH GAP ROOTC-1 = G-FLIP-2 closed (REFEREE's §C in turn accepts REFEREE-2's single line as the joint verdict);
  N3-LEVEL SIGN WITH GAP G-FLIP-3; notes N-FLIP-1..4. §C (both): no disagreement on any signed lemma; joint gaps G-FLIP-1 = ROOTC-2
  (statement; found by both), G-FLIP-2 = ROOTC-1 (proof step; found by both; equivalent repairs), G-FLIP-3 (parenthesis; REFEREE-2 only),
  all minor and closed by the fixes file; notes, the union of FLIP-N1..N4 and N-FLIP-1..4; both under the standing premise 1E-N3 (P1, P2).
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas; no running-time bound). GAPS G-N5-TIME: open.
