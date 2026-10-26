# R2-N5-FLIP: REFEREE-2 report on packet P-N5-FLIP (ROOT, ROUTE-RELAY, SELF-FREE, ROOT-C, STATIC, FLIP, N3-LEVEL)
Referee: REFEREE-2 successor 16 (session_01R1scbTA9MiKutHRhRdi3zh), Opus 5.5 (D15, L37), SECOND referee. Written 2026-10-26 12:10Z (date -u).
Object: docs/si/P-N5-FLIP-box18.md, sha1 96a7e088c2175f71ab1aef2577d6139f80a4efff (`git show d67fdb87:… | sha1sum` and the same at l-si
7ea3d8cf), 157 lines, pinned at trunk d67fdb87, frozen. Author L-SI successor 14 (parked; questions to successor 15 via the Lead).
Independence: written before opening any REFEREE file on FLIP; `git fetch origin claude/referee` + `git ls-tree --name-only -r
origin/claude/referee docs/referee/ | grep -ic flip` gave 0 at 12:00Z and 0 at 12:10Z (same turn as the push). The lane's scripts
(experiments/si/rund/relay.py, flipck.py, frzrho.py, quotecheck.py) were NOT run or imported.
Checker: docs/referee-2/R2-N5-FLIP/flip_check.py (own), on succ. 13's SPEC loop (R2-N5-DUAL/dual_check.Runner, on si.py = SPEC S1's own
implementation, read-only); Ξ = my own (σ, σ̄)-play values (R2-N5-RUND/rund_check.py); walks Π_s(q) enumerated from the definitions.
Scope (D1): structural, inside one phase; no count is bounded. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Verdicts
| item | verdict | premises (checked complete) |
| --- | --- | --- |
| §2 Lemma ROOT | SIGN | P1 |
| §3 Lemma ROUTE-RELAY | SIGN | P1 (through R56 (d)'s "≤" half = Lemma S (a)); additivity (§1, proved in place) |
| §3 Corollary SELF-FREE | SIGN | as ROUTE-RELAY |
| §4 Lemma ROOT-C | SIGN WITH GAPS G-FLIP-1 (statement: exits omitted; the literal form is FALSE, witness) and G-FLIP-2 (proof of "≤": the positional-realisation sentence is FALSE, witness; repaired below, still P1 only) | P1 |
| §5 Lemma STATIC | SIGN (N-FLIP-1: P1 is not used) | P2 (S4a's choice); definitions |
| §6 Lemma FLIP (a) FLIP-COST | SIGN | P1 + (SG); additivity |
| §6 Lemma FLIP (b) FLIP-1 | SIGN | P1 |
| §6 Lemma FLIP (c) Corollary | SIGN | P1 + (SG) |
| §6 necessary condition N1 ∨ N2 ∨ N3 | SIGN | from (a)-(c) |
| §6 Lemma N3-LEVEL | SIGN WITH GAP G-FLIP-3 (minor: the parenthesis "both hold when p1 is intact at t2, by (c)" does not follow from (c)); the lemma under its explicit hypotheses is correct | P1 + (SG) |
| the 10 landed quotes | all VERBATIM (my own substring check against `git show 6f9451e3:docs/RESULTS.md` at the cited lines) | — |
Not reviewed (as briefed): §7 (FRZ-RHO, ROOT-C's strong form, READINGs, OPEN/DEAD), §8 (DATA).
P1 / P2: the standing SPEC premise 1E-N3 in the two forms of R2-N5-RUND §0 (P1: σ̄_k is Odd's pointwise optimum in G_{σ_k}, landed as (VJ);
P2: S4a's σ_{k+1} is Even's pointwise optimum in its arena). (SG): Ξ_{k+1} ⊵ Ξ_k at every transition, basis R15 (a), (d) via (VJ) under P1.
The packet's premise split (P1 only: ROOT, ROUTE-RELAY, SELF-FREE, ROOT-C, FLIP (b); P1 + (SG): FLIP (a), (c), N3-LEVEL; P1 + P2: STATIC)
is COMPLETE; it is over-complete only for STATIC (N-FLIP-1). The repair of G-FLIP-2 keeps ROOT-C at P1 only.

## 1. Proof check
- ROOT. Reach_s(Q) is closed under G_{σ_s}-successors (a Q vertex's successors start its own exit paths; a non-Q vertex of an exit path
  has its next vertex on the path, the last vertex being in Q or a repeat that occurs earlier on the path). Equal exit paths give equal
  Reach and equal σ on its Even vertices (each lies on a path, a terminal repeat included); the subgame G_{σ_s}[X] is the same at t, t + 1,
  and by P1 Ξ_s on X is its pointwise Odd optimum (plays from X stay in X). Consequence: a changed exit path first diverges at an Even
  vertex of the t-path (forced Odd edges cannot change; Q ends a path). CORRECT; fallbacks included.
- Additivity (§1). A vertex common to r and e's play before c would close a cycle in U_c missing c; every honest cycle reached from U_c is
  c's. κwt and κ are additive over the disjoint union. CORRECT.
- ROUTE-RELAY. With no class-exit change and no source: c's κ fixed and c's play avoids q (q on no honest cycle); an exit e = q puts y
  outside Y^q at both times; otherwise y ∈ Y^q iff e's play avoids q (y's class exit path has no Q_c vertex), the same at t, t + 1; κ(y) by
  additivity; R56 (d) at both states; κ determines Ξ inside a class (weights injective). CORRECT. SELF-FREE: exits ∈ {q, c}. CORRECT.
- ROOT-C. See G-FLIP-1, G-FLIP-2 (§2). The "≥" half (the honest walk lies in Π_s(q): the honest play from q stays in U_c, its first-visit
  prefix to c repeats no vertex, its Q_c vertices are distinct) is CORRECT. The walk-distinctness argument is CORRECT. With exits included
  in the hypothesis, Π_t(q) = Π_{t+1}(q) as weighted walks, and κ_s(q) = min Π_s(q) by the repaired "≤" — then CORRECT.
- STATIC. σ̄ = σ̄_I on Q by the cut, out-degree 1 elsewhere; τ fixed on the phase; Ξ_k is by definition the (σ_k, σ̄_I)-play value, i.e.
  σ_k's valuation in the one-player G_{σ̄_I} (Odd has out-degree 1 there, so S1's valuation is the play value); Iσ_k by S2; σ_{k+1} the
  arena optimum in G_{τ_I} by S4a (no fallback) and P2. CORRECT; P1 is not needed for any sentence (N-FLIP-1).
- FLIP (a). Additivity at t1 (q1's honest play: q1, y1, p1, then q2) and at t2 (q2, p2, then q1); (SG) at q1 inside the class (λ fixed)
  gives κ_{t2}(q1) ⪰ κ_{t1}(q1); κ lies in Z × Z with the lexicographic order, translation-invariant. CORRECT (the κ order is Ξ's inside a
  class: weight, then s_c·length).
- FLIP (b). p1 intact at t2 includes its last vertex's edge to q2; p1, p2 hold no Q_c vertex and avoid c; so the σ̄′-play from q1 stays
  on the vertices of C and never reaches c; P1 at t2 and cycle-node-first comparison with injective rewards. CORRECT.
- FLIP (c). C is a simple cycle when p1 ∩ p2 = ∅ (q1 ≠ q2, both outside p1 ∪ p2). rew(h) > rew(c) splits exactly into (rank h > rank c,
  h even) or (rank h < rank c, c odd) (I re-derived both directions of the case split); in both wt(C) ≻ 0. CORRECT. NEC: CORRECT.
- N3-LEVEL. The "no cycle" fact, the two decompositions (restricted to V_{>c}), and the four cases (h = q1; h ∈ p2 with p2 intact at t1;
  h ∈ p1; h = q2) each re-derived; in the last two, (SG) with the same cycle node and the even h exclude L′ = rank(h). CORRECT under the
  lemma's hypotheses. G-FLIP-3 concerns only the parenthesis.

## 2. Gaps (with witnesses)
- G-FLIP-1 (ROOT-C statement; minor, wording, but the literal statement is FALSE). ROOT-C's hypothesis says "every class exit path … is the
  same at t and t + 1", and its consequence "every transition with a ρ event at a terminal of class c changes a class exit path of class c".
  By §3's definition the class exit path is the part STRICTLY BEFORE the exit, and §3's ROUTE definition treats "class exit path or exit"
  as two things. An Even last vertex of a class exit path can switch from one exit to another without changing the path. Witness:
  experiments/n5-exhaustive/instances/n4_thch_0.pg (sha1 77018c63860be6ad166320354ea616113ff9da4e; n = 4: Odd 0 (prio 0, succ {2, 3}),
  Even 1 (prio 2, self-loop), Even 2 (prio 4, succ {0, 1}), Even 3 (prio 6, succ {1})), N5 from S3. Transition 0 → 1 is in-phase (τ, λ ≡ 1
  fixed), c = 1, Q_c = {0}. Class exit paths of q = 0: from y = 2 the path is (2) at both states, its exit changes c → 0 (σ(2): 1 → 0);
  from y = 3 the path is (3), exit c, at both. So every class exit path is the same, yet Ξ(0) changes (1, {2}, 2) → (1, {3}, 2): a ρ event.
  Counts: such literal-only failures (paths equal as sequences, an exit changed, κ changed) at 80 transitions of lib41, 4 of my 𝒞^1O set,
  45 random; 0 failures of the exits form. Repair: "every class exit path AND EXIT" in the hypothesis, "changes a class exit path or exit"
  in the consequence (as §3's ROUTE definition already says); the proof then reads Π_t(q) = Π_{t+1}(q) correctly.
- G-FLIP-2 (ROOT-C proof, "≤"; the statement survives). The sentence "Hence each walk is the play from q of a positional Odd strategy in
  G_{σ_s} (choose y_i at e_i), with cycle node c" is FALSE when a walk passes a vertex of Q_c that lies on c's honest cycle with a choice off
  the cycle: after c the positional play returns to that vertex and leaves along the walk, closing a different cycle. Witness:
  docs/referee-2/R2-N5-TOG/climb/best_tog_83.pg (sha1 01788acf36f67bdb798e936b50cb112ac982c063, n = 12, Q = {9}), N5 from S3, state 1:
  c = 6 (prio 7, odd), c's honest cycle 6, 1, 2, 9, 3, 11; the walk 9, 7, 10, 6 ∈ Π_1(9) (y_0 = 7, class exit path 7, 10, exit c); its
  positional realisation σ̄_1[9 ↦ 7] gives the play 9, 7, 10, 6, 1, 2, 9, … with cycle node 10 (prio 10), not c. In data such walks occur
  often (RC_POS: 60 lib41, 1 𝒞^1O set, 410 random), so the step cannot be read charitably. The conclusion κ_s(q) = min Π_s(q) holds in all
  data (RC_MIN, 10,993 checks, 0 failures). Repair (referee-written, P1 only): prove "≤" by backward induction along the walk from
  B(e, y): κ_s(e) ⪯ κwt(e) + κwt(p_y) + κ_s(e′) for e ∈ Q_c, y ∈ succ(e) ∩ U_c with exit e′ ≠ e (p_y = y's class exit path). Proof of B: let
  ρ := σ̄_s[e ↦ y]. (1) If e′'s honest play never visits e, the ρ-play from e is e, p_y, e′'s honest play (cycle node c), whose value is
  the right side (additivity); P1. (2) If it visits e, the ρ-play closes a cycle Z through e. If Z's node is c (e on c's cycle, reached
  after c), the ρ-play still first reaches c along e, p_y, e′'s route, value = the right side; P1. Otherwise P1 gives rew(top Z) > rew(c),
  so (FLIP (c)'s split) the part of Z ranked above c has an even top, or Z lies below an odd c; if e′ reaches e before c, the right side
  equals κ_s(e) + wt(Z) with wt(Z) ≻ 0; if after c, the right side's path set is (Z ∩ V_{>c}) with an even top while κ_s(e) has an empty
  path set (e on c's cycle): either way the right side ≻ κ_s(e). Summing B along the walk (κ_s(c) = (0, 0)) gives κ_s(q) ⪯ the walk's κ.
- G-FLIP-3 (N3-LEVEL statement, parenthesis; minor, wording). "(both hold when p1 is intact at t2, by (c))": (c) gives a DISJUNCTION, rank(h) >
  rank(c) with h even, OR rank(h) < rank(c) with c odd; the second alternative is not excluded by anything in the packet. No instance of a
  flip with intact p1, disjoint paths and C below an odd c occurs in my data (N3L_LOW = 0 over 908 intact disjoint flips), so I have no
  witness that the parenthesis is false, only that it is unproved. The lemma's own hypotheses state the first alternative explicitly, so
  its conclusion is unaffected. Repair: replace the parenthesis by "(by (c), when p1 is intact at t2 either this holds or C lies below an
  odd c; the lemma treats the former)".

## 3. Notes (no gap)
- N-FLIP-1 (STATIC's premises). The packet lists P1 + P2; only P2 is used (σ_{k+1}'s optimality). Ξ_k is the play value by definition;
  "P1 makes it the optimal reply's value" is a remark. Over-complete, not wrong.
- N-FLIP-2 (quotes). All 10 [Q …] quotes verbatim at the cited lines of RESULTS@6f9451e3 (my script, whitespace normalised, "…" splitting);
  6f9451e3 is an ancestor of the pin. R56 (d)'s "≤" half rests on Lemma S (a) (R56's landed text), consistent with "P1 only".
- N-FLIP-3 (definitions read). "exit"/"class exit path" in §3 are defined per y and do not depend on §3's "q on no honest cycle"
  qualifier; ROOT-C uses them for every q′ ∈ Q_c (also on c's cycle: the witness of G-FLIP-2 has q = 9 on c's cycle), which is fine.
- N-FLIP-4 (data thin where the gaps sit). Flips with intact disjoint paths: 908 in my data (pp_K12 60, pp_K48 672, frz40 3, lib41 167,
  random 6); N3-LEVEL equality lev = rank(h) occurs 80 times (sharp, as the packet says); leanT_N6 from my 5 starts has no multi-state phase.

## 4. Data (DATA, not proof)
Per N5 run: phases ((λ, τ) constant, ≥ 2 states), Q-exit paths, Reach_s(Q), class exits per class, ROUTE/RELAY classification with sources,
ROOT-C in both forms, walk enumeration Π_s(q) for n ≤ 16 (min vs κ, positional realisations), ρ-free intervals, every flip (q1, q2, t1 < t2)
of a phase with (a), (b), (c), NEC and N3-LEVEL.
| set | N5 runs | states | ρ events | ROOT static transitions | ROUTE / RELAY | RC static (exits form) | RC_LIT (literal fails) | RC_MIN checks (walks) | RC_POS | flips (N1 / N2 / N3) | N3-LEVEL checks (equal) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| frz40 + .start, pp_K12_n161 + .start, pp_K48_n449 + .start, so_th_n32 S3 | 4 | 204 | 201 | 50 | 126 / 75 | 49 | 1 | — (n > 16) | — | 871 (136 / 49 / 735) | 732 (0) |
| lib41 minus referee games × 3 starts | 1,230 | 19,456 | 9,330 | 6,977 | 4,373 / 4,935 | 7,000 | 80 | 1,211 (10,970) | 60 | 883 (716 / 49 / 167) | 164 (75) |
| my 503 𝒞^1O files × 2 starts | 1,006 | 17,811 | 3,911 | 8,235 | 3,848 / 0 | 8,058 | 4 | 1,569 (3,556) | 1 | 0 | 0 |
| random 2 Odd choices, n 5-12 (3,000 × 3) | 9,000 | 20,886 | 271 | 394 | 233 / 18 | 889 | 20 | 4,060 (8,201) | 195 | 2 (0 / 0 / 2) | 2 (2) |
| random 4 Odd choices, n 6-12 (2,000 × 3) | 6,000 | 15,991 | 163 | 130 | 126 / 28 | 424 | 25 | 4,153 (9,746) | 215 | 4 (0 / 0 / 4) | 4 (3) |
| leanT_N6 × 5 starts | 5 | 33 | 0 | 0 | — | 0 | 0 | 0 | 0 | 0 | 0 |
0 violations of every signed check (ROOT, ROOT2, RR, SELF, RC exits form, RC_MIN, ST, FLa, FLb, FLc, NEC, N3L) in every set. On the
𝒞^1O set every ρ event is ROUTE (SELF-FREE). Mutations (must fail): root (ROOT asks Ξ to change) 5 FAIL on pp_K12; cost (FLIP-COST with
2·wt(C)) 70 FAIL lib41, 2 random; lev (N3-LEVEL with lev > rank(h)) 27 FAIL lib41, 2 random. Logs: R2-N5-FLIP/logs/; reproduce `run_all.sh`.

## 5. Signatures
ROOT, ROUTE-RELAY, SELF-FREE, STATIC, FLIP (a), (b), (c), the necessary condition: SIGN. ROOT-C: SIGN WITH GAPS G-FLIP-1 (statement must
include exits; the literal form is false, n4_thch_0) and G-FLIP-2 (proof step false, best_tog_83; repaired above, P1 only). N3-LEVEL: SIGN
WITH GAP G-FLIP-3 (parenthesis unproved; lemma correct under its hypotheses). Premise split complete (STATIC over-complete). Quotes verbatim.
REFEREE-2 successor 16 (Opus 5.5, D15).
