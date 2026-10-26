# R-N5-FLIP: REFEREE report on packet P-N5-FLIP-box18 (L-SI box 18: ROOT, ROUTE-RELAY, SELF-FREE, ROOT-C, STATIC, FLIP, N3-LEVEL; every game, inside one phase)
Referee: REFEREE (successor 14, session_011gcqhgkUNYoFY7xCryrLff), Opus 5.5 (owner ruling D15). FIRST referee (Lead brief 11:58Z). Context at writing: about 380k tokens.
- Object: docs/si/P-N5-FLIP-box18.md, sha1 96a7e088c2175f71ab1aef2577d6139f80a4efff (checked on the tree, `git show 7ea3d8cf:… | sha1sum`
  (l-si freeze) and `git show d67fdb87:… | sha1sum` (trunk pin); identical), 157 lines. Author: L-SI successor 14.
- Written 2026-10-26T12:00Z-12:08Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ FLIP file exists on my tree or on origin/claude/referee-2 at my fetches (`ls docs/referee-2 |
  grep -ic flip` = 0; `git ls-tree --name-only origin/claude/referee-2 docs/referee-2/ | grep -ic flip` = 0, same turns as the fetches). No
  lane code run (experiments/si/rund/*.py, quotecheck.py not executed or imported). D1.
- Premises read against their text: SPEC S1-S5 (docs/new/N5-ssi-global.md); RESULTS R15 (a), (d); R38 (a) KEY; R56 (setting l. 2832-2846 and
  (d) κ-Y-FORM_D with its "≤ half uses R18 (d) Lemma S (a)" line, at 6f9451e3); R57 (a) (VJ) and the 1E-N3 line; R61 (a), (e) (context);
  R62 WM-G line.
- Quotes: all 10 «…» re-checked by my own script scratch/flip_quotes.py (not the lane's quotecheck.py): QUOTES 10, FAILED 0
  (scratch/flip_logs/quotes.txt); each cited line range lies in the RESULTS entry the packet names (R15, R15, R38, R56, R56, R57, R57, R61,
  R61, R62 at 6f9451e3).
- Tools: scratch/flip_probe.py (own engine rl_engine = SPEC from the text; checks every item per phase, plus ROOT-C's proof claims MINW / REAL
  and my repair LOCAL; controls MUT=1 (FLIP (a) with wt(C) doubled), MUT=2 (N3-LEVEL strict)); witness inputs scratch/flip_inputs/; logs
  scratch/flip_logs/.

## Verdicts
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | additivity (used in §3, §6) | CORRECT (proof step; checked) |
| §2 | Lemma ROOT (P1) | SIGNED |
| §3 | Lemma ROUTE-RELAY (P1; R56 (d)) | SIGNED |
| §3 | Corollary SELF-FREE | SIGNED |
| §4 | Lemma ROOT-C (P1) | AS WRITTEN: NOT SIGNED (FALSE; gap ROOTC-2, witness rootc_lit_n5). SIGNED WITH GAPS in the corrected form "every class exit path AND EXIT … is the same ⇒ κ equal on Q_c" (its corollary: "changes a class exit path or an exit of class c"); proof gap ROOTC-1 (a false sentence in (≤)), closed by the referee-written repair in §4 below |
| §5 | Lemma STATIC (P1, P2) | SIGNED |
| §6 | Lemma FLIP (a) FLIP-COST (P1, (SG)) | SIGNED |
| §6 | FLIP (b) FLIP-1 (P1) | SIGNED |
| §6 | FLIP (c) Corollary (P1, (SG)) | SIGNED |
| §6 | necessary condition N1 ∨ N2 ∨ N3 | SIGNED |
| §6 | Lemma N3-LEVEL (P1, (SG)) | SIGNED |
| §1 | per-item premise lists | COMPLETE (§7 below), with one naming note (FLIP-N1) |
| §7, §8 | FRZ-RHO, ROOT-C strong form, READINGs, DATA | not signed (as briefed) |
Gaps: ROOTC-2 (statement, minor: a missing "or exit"; the proof proves the corrected form), ROOTC-1 (proof step, minor, closed here).
Notes FLIP-N1..N4. Structural lemmas only: nothing here bounds ρ, N_ep, a phase or N5's running time; not a TARGET.md claim; G-N5-TIME
stays OPEN.

## 1. Setting and additivity
- Classes U_c = λ^{-1}(c) are fixed in a phase; inside U_c, Ξ's order is κ's (same cycle node; then signed weight; then length with
  s_c = +1 for odd c (longer better for Even), −1 for even c) ✓.
- Additivity ✓. The honest play is a functional-graph play, so z's play is r followed by e's play; a vertex common to r and e's play before c
  would make the play cycle without c, against λ(z) = c. Then P(Ξ z) = (r above c) ⊔ P(Ξ e), ℓ(Ξ z) = |r| + ℓ(Ξ e), and κ sums. Probe ADD:
  0 failures in 783,000+ checks.

## 2. ROOT ✓
Reach_s(Q) is closed under all successors in G_{σ_s} (a Q-vertex's successors start its exit paths; a non-final path vertex's unique
successor is the next one; the final vertex is in Q or repeats an earlier one). Equal exit paths ⇒ equal Reach and equal out-edges on it
(every Even vertex of Reach ∖ Q has its σ-edge on a path). P1 makes Ξ_s(v) the pointwise minimum over Odd's positional strategies; every
play from v ∈ Reach stays in Reach, so the minimum is that of the subgame G_{σ_s}[Reach], the same at t and t + 1. The consequence: a ρ
event at q ∈ Reach_t(Q) forces a differing exit path; the first difference along it is at a vertex whose successor changed, which is an Even
vertex (forced Odd edges are fixed, Q-vertices end paths) ✓. (The lemma needs no "in-phase"; harmless.)

## 3. ROUTE-RELAY, SELF-FREE ✓
(i) c's play is c's cycle and q is on no honest cycle, so it avoids q; κ(c) = (0, 0). (ii) without a source, "e's play avoids q" is the same
at t, t + 1, and a class exit path never contains q (q ∈ Q_c ends it), so Y^q_t = Y^q_{t+1} (exit q ⇒ y ∉ Y^q both times; self-loop y = q
likewise). (iii) additivity with equal paths and κ(e). (iv) R56 (d) holds at t and t + 1 (q ∈ Q_c on no honest cycle at both), so κ(q) is
equal: no ρ event. SELF-FREE: exits lie in {q, c} ✓.

## 4. ROOT-C: statement gap ROOTC-2, proof gap ROOTC-1, and the repair
- ROOTC-2 (statement). §3 defines the CLASS EXIT PATH as "the part strictly before" the exit, and ROUTE-RELAY accordingly says "a different
  class exit path OR EXIT". ROOT-C's hypothesis names only the paths. A switch at the last vertex of a class exit path changes the exit and
  keeps the path. Witness (own engine; scratch/flip_inputs/rootc_lit_n5.pg sha1 602e6db6a3d0b0c934cd440cba69d34c7a38f390, start
  rootc_lit_n5.start sha1 796b8d5e622d59150d451ecbfcfa6c157573eb56): n = 5, priorities [4, 2, 1, 6, 5], owners [E, E, O, O, O], edges
  0 → {1, 2, 4}, 1 → {2, 4}, 2 → {1, 4}, 3 → {0, 1}, 4 → {1}; start σ = (0 → 2, 1 → 4), τ = (2 → 4, 3 → 1, 4 → 1). Transition 0 → 1 (S4a,
  in-phase: every λ = 4, τ fixed) switches σ(1): 4 → 2. Class c = 4 (cycle 4 → 1 → 4 at state 0), Q_c = {2, 3}. Every class exit path is the
  same vertex sequence ([1] from y = 1 for q′ = 2, 3; [0] from y = 0; [] from y = 4), but y = 1's exit moves from c to 2; and Ξ(3) goes
  (4, {3}, 2) → (4, {3}, 3) (path set {3}, the priority-6 vertex; length 2 → 3): κ_0(3) ≠ κ_1(3), a ρ event at 3 with no class exit path changed. So ROOT-C and its "So …" sentence are FALSE as
  written. In data the literal hypothesis without the exit condition holds with a κ change in 26 of 30 lib41 cases (first: experiments/n5-exhaustive/instances/n4_thch_0.pg (sha1 77018c63…), S3 start, state 0, class 1: y = 2 keeps path [2], exit 1 → 0) and 10 of 64 random cases; the corrected hypothesis (path and exit) holds with κ equal in all 7,036 + 773 + 843 cases (ROOTC: 0 failures).
  The proof's last line ("Π_t(q) = Π_{t+1}(q) as walks with weights (equal paths …)") needs the exits too: with them it is right.
- ROOTC-1 (proof, (≤)). "Hence each walk is the play from q of a positional Odd strategy in G_{σ_s} (choose y_i at e_i), with cycle node c"
  is FALSE when the walk leaves c's honest cycle at a vertex e_i on that cycle: after reaching c the play runs along c's cycle to e_i and then
  along the walk again, and that cycle's top can be an even vertex above c. Witness: experiments/red/tcpert/instances/leanT_N6.pg (sha1
  f037844a…, the packet's own §8 instance), S3 start, state 3, class c = 7 (odd), q = 4 on c's honest cycle [7, 4]; the walk 4 → 26 → 18 →
  … → 27 → 7 ∈ Π_3(4) is realised by a play whose cycle has top 44 (even, rank 44 > rank 7). In data such walks are common (probe REAL:
  2,422 lib41 walks, 3,504 / 1,632 random). The min formula κ_s(q) = min Π_s(q) itself holds in every check (MINW: 0 failures in 105,000+
  states × terminals), and so does ROOT-C's corrected statement.
- Repair (referee-written; P1 only). LOCAL: for every s, e ∈ Q_c and y ∈ succ(e) ∩ U_c, κ_s(e) ⪯ κwt_c(e) + κ_s(y). Proof: τ′ := σ̄_s[e ↦ y].
  (1) y's honest play avoids e: the τ′-play from e is e then y's play, value e ⊕ Ξ_s(y) with cycle node c; P1 gives Ξ_s(e) ⊴ it. (2) y's play
  meets e before c: y's play = (path π to e) · e's play, so κwt(e) + κ_s(y) = κwt(Z) + κ_s(e) with Z := e · π a cycle missing c; the
  τ′-play from e is Z, so by P1 rew(top Z) > rew(c): top above c and even (Σ wt_c(Z) > 0) or below c with c odd (weight 0, s_c·|Z| > 0);
  κwt(Z) ≻ 0. (3) y's play reaches c first and e lies on c's cycle: the τ′-cycle is e · (y's path to c) · (arc c → e); if its top is c, the value
  is e ⊕ Ξ_s(y) as in (1); otherwise its top w has rank > rank(c) (the arc and e are below c), P1 forces w even, w lies on y's path to c and
  is the top of P(Ξ_s y), so κ_s(y) has positive weight while κ_s(e) has weight 0 (e on c's cycle) and wt_c(e) = 0: strict. Then (≤) by
  induction from the end of a walk q = e_0, …, e_j = c: κ(w_i) = κwt(e_i) + κwt(p(y_i)) + κ(w_{i+1}) ⪰ κwt(e_i) + κwt(p(y_i)) + κ_s(e_{i+1})
  = κwt(e_i) + κ_s(y_i) (additivity) ⪰ κ_s(e_i) (LOCAL); κ_s(c) = (0, 0). (≥) is the packet's. Probe LOCAL: 0 failures in 460,000+ checks.
- So ROOT-C with "path and exit" is SIGNED with ROOTC-1 closed by this repair; it uses P1 only (the repair adds nothing beyond P1 and
  additivity).

## 5. STATIC ✓
σ̄|Q is constant on I by definition; Odd vertices outside Q have one edge; τ is fixed on the phase. Iσ_k is S2's set read from Ξ_k =
V_{σ_k, σ̄_I}; every transition of I is an in-phase non-fallback, so σ_{k+1} is S4a's output, Even's pointwise arena optimum against τ_I (P2).
Nearly definitional; "Ξ|Q constant" is part of the cut, not used in the proof ✓.

## 6. FLIP and N3-LEVEL ✓
- (a): par_{t1}(q1) = q2 ≠ q1, so q1's honest play at t1 is q1 · y1 · p1 · q2 · (q2's play), first meeting Q_c ∪ {c} at q2; additivity at t1
  and at t2; (SG) gives κ_{t2}(q1) ⪰ κ_{t1}(q1) (same class, t1 < t2 in one phase); substitution in the ordered group Z × Z ✓.
- (b): with p1 intact, the σ̄′-play from q1 runs y1, p1, q2, p2 back to q1 and stays among {q1, q2} ∪ p1 ∪ p2 ∌ c; its cycle Z has a top w ≠ c,
  and P1 with λ(q1) = c and injective rewards gives rew(w) > rew(c) ✓. (This is the correct use of a cycle top that the ROOT-C proof missed.)
- (c): p1, p2 simple (parts of plays), disjoint, and q1, q2 outside them: C is a simple cycle, Z = C. rew(h) > rew(c): rank(h) > rank(c)
  forces h even (an odd vertex above c has the smaller reward whatever c's parity); rank(h) < rank(c) forces c odd (every lower vertex has
  smaller reward than an even c). Then wt(C) ≻ 0 and (a) ✓.
- N1 ∨ N2 ∨ N3: the contrapositive of (c) with (a) ✓ (p1 not intact means an Even vertex of p1 has another successor at t2; forced Odd edges
  never change).
- N3-LEVEL: I re-did the four cases. (no cycle) and the decomposition (each part restricted to ranks above c) ✓; h = q1 and h ∈ p2 (with p2
  intact at t1) by the no-cycle argument ✓; h ∈ p1 and h = q2 via (SG): the top differing rank L′ of P(Ξ_{t1} q1) Δ P(Ξ_{t2} q1) cannot be
  rank(h) since the even h lies in the t1 set and the t2 set must be the heavier, so L′ > rank(h), and above rank(h) X_s agrees with
  P(Ξ_s q1) ✓. p1 ∩ p2 = ∅ makes C simple and h unique ✓.

## 7. Premise lists (per item; checked complete)
- ROOT: P1; nothing else (valuations of a play are definitional). ROUTE-RELAY: P1, R56 (d) (landed; its "≤" half is Lemma S (a) = P1), the
  phase (λ fixed), additivity. SELF-FREE: ROUTE-RELAY. ROOT-C: P1 (+ additivity in my repair). FLIP (b): P1. STATIC: P1, P2, SPEC S2/S4.
  FLIP (a), (c), N3-LEVEL: P1, (SG), additivity. (SG): R15 (a), (d) via (VJ) under P1 — the switches are Switch_I with I ⊆ Iσ (unambiguous:
  one edge per vertex) ✓. Each list is complete. FLIP-N1: ROUTE-RELAY's line "P1 only" should name R56 (d) as a used landed lemma (it is
  quoted under "Cited landed lemmas", so this is naming only).

## 8. Data (own engine; DATA, not proof)
All checks: own engine, 0 failures of every signed item (ROOT-C in its corrected form) in every sample. Starts S3 + 2 random unless stated.
| sample | runs | phases | transitions (ρ) | ROOT / ROOT2 | ROUTE / RELAY (RR), SF | ROOT-C corrected / literal κ-changes | flips (N1 / N2 / N3), FB / FC, N3-LEVEL (equalities) | STATIC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41 (n ≤ 64; 45 skipped) | 1,101 | 5,365 | 12,093 (3,786) | 7,026 / 3,786 | 3,943 / 356 (356), 3,497 | 7,036 / 26 of 30 | 1,002 (982 / 98 / 40), 20 / 20, 12 (3) | 1,767 |
| random 𝒞^kO, k 1-5, n 5-12, seed 1418 | 9,000 | 22,983 | 1,263 (191) | 313 / 191 | 214 / 31 (31), 87 | 773 / 10 of 64 | 6 (0 / 0 / 6), 6 / 6, 4 (4) | 711 |
| random 𝒞^kO, k 1-6, n 13-24, seed 1419 | 3,000 | 9,646 | 1,102 (251) | 358 / 251 | 313 / 62 (62), 76 | 843 / — | 3 (0 / 0 / 3), 3 / 3, 1 (1) | 604 |
| frz40, leanT_N6 (12 random starts) | 26 | — | — | — | — | — | 560 (544 / 196 / 56), 16 / 16, 4 (3) | — |
| pp_K12_n161 (sha1 8808ba5d…) + its start, and S3 | 2 | 5 | 36 (17) | 19 / 17 | 25 / 15 (15) | 19 / — | 60 (0 / 0 / 60), 60 / 60, 60 (0) | 3 |
- Proof-step checks: additivity ADD 783,000+ checks; ROOT-C's min formula MINW 105,000+ (state, terminal) pairs (classes with |Q_c| ≤ 7 / 5),
  0 failures; REAL (walks whose positional play has a cycle node ≠ c, ROOTC-1) 2,422 / 3,504 / 1,632; LOCAL (my repair) 462,000+, 0 failures.
- Controls (each bites): MUT=1 (FLIP (a) with wt(C) doubled) on leanT_N6 + frz40: FA 55 failures; MUT=2 (N3-LEVEL strict) on leanT_N6: 3
  failures, the packet's three equalities (§8 "MUT=2 (strict) fails on leanT_N6 (3 equalities)" reproduced on my engine). The literal ROOT-C
  test is itself the discriminating control for ROOTC-2.
- Agreement with the packet's §8 where comparable: lib41 N3-LEVEL checks 12 (packet: 12); frz40 flips are N1 and pp_K12's are N3 (intact,
  strict rise) on my engine too; ALLRELAY / FRZ-RHO not checked (not to sign).
- STATIC's arena-optimality check is a necessary-condition test (no arena edge improves W at a vertex off its W-cycle), not a full optimum
  check; 0 failures.

## 9. Notes
- FLIP-N1 (§1 premise line): ROUTE-RELAY / SELF-FREE use R56 (d) (landed, quoted in §1); the per-item line "P1 only" is about standing
  premises; name R56 (d) there too.
- FLIP-N2 (§4 proof): the walk-simplicity sentence ("a repeated vertex has the same successor both times, so the walk would cycle without
  reaching c") is loose — the precise reason is that a repeated non-terminal vertex has a deterministic continuation to the same exit, which
  would repeat an e_i; harmless (and not needed by the repair, which works for every walk).
- FLIP-N3 (§2): ROOT's hypothesis "in-phase" is not used; the lemma holds at every transition.
- FLIP-N4 (§6 N3-LEVEL): the decomposition "X_{t2} = {q2} ∪ p2 ∪ P(Ξ_{t2} q1)" should read "the vertices of {q2} ∪ p2 above c, ⊔ P(Ξ_{t2} q1)";
  the packet's parenthesis "(disjoint, above c; …)" says so, but only after the formula.

## §C. Comparison with REFEREE-2 (R2-N5-FLIP, claude/referee-2 e9044674, docs/referee-2/R2-N5-FLIP.md sha1 7b691f21…), written 2026-10-26T12:19Z by date -u
Opened only after my report was pushed (8317a435) and the Lead's message of 12:17Z (Lead's stamp). REFEREE-2 wrote at 12:10Z with 0 FLIP
files on origin/claude/referee (its independence line).
### C.1 Verdicts, item by item
| item | REFEREE (8317a435) | REFEREE-2 (e9044674) | |
| --- | --- | --- | --- |
| ROOT, ROUTE-RELAY, SELF-FREE, FLIP (a), (b), (c), N1 ∨ N2 ∨ N3 | SIGNED | SIGN | same |
| STATIC | SIGNED (P1, P2 listed) | SIGN, N-FLIP-1: only P2 is used | same verdict; N-FLIP-1 ACCEPTED (my §5 also calls the P1 sentence a remark: "Ξ_k is the play value by definition") |
| ROOT-C | as written NOT SIGNED (FALSE, ROOTC-2); corrected form ("path and exit") SIGNED WITH proof gap ROOTC-1, closed by my repair | SIGN WITH GAPS G-FLIP-1 (statement; literal form FALSE) and G-FLIP-2 (proof step FALSE; repaired) | same substance: both say the literal statement is false and the "path and exit" form is proved after a repair; the difference is only the label (mine splits "as written" and "corrected"); I accept REFEREE-2's single line "SIGN WITH GAPS G-FLIP-1, G-FLIP-2" as the joint verdict, reading G-FLIP-1 as "the signed statement is the exits form" |
| N3-LEVEL | SIGNED (no gap) | SIGN WITH GAP G-FLIP-3 (the parenthesis "(both hold when p1 is intact at t2, by (c))" does not follow from (c)) | REFEREE-2 only; ACCEPTED, I MISSED it (C.3). Joint: SIGN WITH GAP G-FLIP-3 (minor; the lemma under its explicit hypotheses is correct) |
| quotes | 10/10 (own script, entries attributed) | 10/10 VERBATIM (own script) | same |
| premise lists | complete; FLIP-N1 (name R56 (d)) | complete, STATIC over-complete (N-FLIP-1); R56 (d)'s "≤" = Lemma S (a) | same |
### C.2 The ROOT-C gaps and the two repairs
- ROOTC-2 = G-FLIP-1 (same gap). Witnesses: REFEREE-2 n4_thch_0 from S3 (sha1 77018c63…); mine the same instance and state (my first lib41
  example, report §4) plus the hand-checked rootc_lit_n5 (+ start). Counts differ only by unit and starts (REFEREE-2: transitions; mine:
  (transition, class) cases). Joint repair: "class exit path AND EXIT" in the hypothesis and "changes a class exit path or exit" in the
  consequence (both referees, word for word the same fix).
- ROOTC-1 = G-FLIP-2 (same gap). Witnesses: REFEREE-2 best_tog_83 (sha1 01788acf…, S3, state 1, q = 9 on c's cycle); mine leanT_N6 (S3,
  state 3, q = 4 on c's cycle [7, 4]). Same mechanism: the walk leaves c's honest cycle at a Q_c vertex on it, and the positional
  realisation closes a cycle with an even top above c.
- The two repairs are THE SAME INEQUALITY in two forms. Mine, LOCAL(e, y): κ_s(e) ⪯ κwt(e) + κ_s(y). REFEREE-2's B(e, y): κ_s(e) ⪯ κwt(e) +
  κwt(p_y) + κ_s(e′) for exit e′ ≠ e. By additivity κ_s(y) = κwt(p_y) + κ_s(e′) (y's play is p_y then e′'s play), so B = LOCAL for every y
  whose exit is not e, which is every step of a walk in Π_s(q) (the e_i are distinct). The case splits match: my (1) "y's play avoids e" /
  (2) "meets e before c" / (3) "reaches c first, e on c's cycle" are REFEREE-2's (1) / (2, before c) / (2, after c, node c or not). Both use
  P1 only, both conclude by backward induction along the walk with κ_s(c) = (0, 0). I re-read REFEREE-2's case (2) against mine: its
  "the right side equals κ_s(e) + wt(Z)" is my κwt(e) + κ_s(y) = κwt(Z) + κ_s(e); its "after c" case is my (3). EACH SUFFICES.
- Which text for the fixes file: B(e, y) (REFEREE-2's form), because it is stated on the walk's own steps (e, p_y, e′) and slots into the
  packet's (≤) line without the extra additivity step; my LOCAL may be added as a one-line remark (it is B before additivity, and also covers
  y with exit e, which no walk uses). Either text closes the gap; there is no disagreement.
### C.3 G-FLIP-3 (settled)
- I re-read §6: N3-LEVEL's hypotheses state "rank(h) > rank(c) and h even" explicitly; the parenthesis then claims "(both hold when p1 is
  intact at t2, by (c))". (c) proves rew(h) > rew(c), which splits into (rank h > rank c, h even) OR (rank h < rank c, c odd) — my own §6
  derivation of (c) states exactly this disjunction, and I did not carry it to the parenthesis. So the parenthesis is UNPROVED; REFEREE-2 is
  right. It is not shown FALSE: no flip with p1 intact, p1 ∩ p2 = ∅ and C below an odd c occurs in REFEREE-2's 908 cases, nor in mine
  (FC_LOWBRANCH = 0 of 83: lib41 20, random seed 1420 3, pp_K12 60; logs flip_logs/*_v3.txt). Verdict: N3-LEVEL SIGNED WITH GAP G-FLIP-3 (minor, a remark in parentheses; the lemma's conclusion under its
  stated hypotheses is unaffected). Joint repair: REFEREE-2's sentence "(by (c), when p1 is intact at t2 either this holds or C lies below
  an odd c; the lemma treats the former)".
### C.4 Notes
| note | REFEREE | REFEREE-2 | outcome |
| --- | --- | --- | --- |
| STATIC uses P2 only | (§5 remark) | N-FLIP-1 | same in substance; accepted |
| quotes verbatim | §0 | N-FLIP-2 | same |
| class exit paths defined per y, independent of §3's "no honest cycle" qualifier | — | N-FLIP-3 | REFEREE-2 only; agreed (my probe computes them that way) |
| data thin where the gaps sit | — (my data rows) | N-FLIP-4 | REFEREE-2 only; agreed (equality lev = rank(h) is common in its data, 80; mine 3 + 4 + 1) |
| ROUTE-RELAY should name R56 (d) | FLIP-N1 | (in its premise column) | same |
| walk-simplicity sentence loose | FLIP-N2 | "CORRECT" | REFEREE only (wording; no disagreement on correctness) |
| ROOT does not need "in-phase" | FLIP-N3 | "fallbacks included" | REFEREE only (remark) |
| N3-LEVEL decomposition wording | FLIP-N4 | "restricted to V_{>c}" | same reading; REFEREE only as a note |
### C.5 Data comparison (both own engines, 0 violations of every signed check, ROOT-C in the exits form)
- lib41: mine 1,101 runs / 1,002 flips (982 N1 / 98 N2 / 40 N3) / 12 N3-LEVEL checks; REFEREE-2 1,230 runs / 883 flips (716 / 49 / 167) /
  164 checks (its pp/frz set adds 871 flips). Differences come from starts (S3 + 2 random each, different seeds; REFEREE-2 excludes referee
  games). Both: N3-LEVEL equality occurs (sharp); both strict-mutation controls bite; both "2·wt(C)" controls bite.
- ROOT-C: both find the literal form failing in data (REFEREE-2 80 lib41 transitions; mine 26 lib41 cases), the exits form never; both find
  non-realisable walks common (REFEREE-2 RC_POS 60 / 1 / 410; mine REAL 2,422 / 3,504 / 1,632, counting walks) and the min formula always true.
### C.6 Joint gap map
| joint gap | REFEREE | REFEREE-2 | severity / status |
| --- | --- | --- | --- |
| G-FLIP-1 (ROOT-C statement omits exits; literal form FALSE) | ROOTC-2 | G-FLIP-1 | minor (wording, but a false statement as written); repair: "path and exit" in hypothesis and consequence; signed in that form |
| G-FLIP-2 (ROOT-C (≤): positional-realisation sentence FALSE) | ROOTC-1 | G-FLIP-2 | minor; CLOSED by the referee repair B(e, y) (= LOCAL); P1 only |
| G-FLIP-3 (N3-LEVEL parenthesis unproved) | missed (accepted here) | G-FLIP-3 | minor; repair: REFEREE-2's sentence; no witness either way |
Joint verdicts: ROOT, ROUTE-RELAY, SELF-FREE, STATIC, FLIP (a)-(c), N1 ∨ N2 ∨ N3 SIGNED; ROOT-C SIGNED WITH GAPS G-FLIP-1, G-FLIP-2 (in
the exits form, with the repair); N3-LEVEL SIGNED WITH GAP G-FLIP-3. Notes for L-SI 15's fixes file: N-FLIP-1..4, FLIP-N1..N4. Both
(Opus 5.5, D15).
