# R-N5-RESTRICT: REFEREE report on packet P-N5-RESTRICT (L-NEW box 48: Lemma RESTRICT_H, Corollary REPRO_H, instances G′_E, G^u, G^{u|J}, G^P)
Referee: REFEREE (successor 16), Opus 5.5 (owner ruling D15). FIRST referee (Lead brief to successor 16, item (4); order of 18:52Z on 26 Oct,
21:05Z on 28 Oct by date -u).
- Object and pin: docs/new/P-N5-RESTRICT-box48.md, sha1 48c63a8e45c0288678805195a91f9c00ee703da9, 116 lines, author L-NEW successor 28: the
  same sha1 on my tree and at the l-new freeze 7e56744a (an ancestor of HEAD). Quote base 08abd9cb.
- Probe and data runs 2026-10-26T18:52Z-19:00Z; report written 2026-10-28T21:22Z-21:27Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ file on RESTRICT on my tree, on trunk or on origin/claude/referee-2 (re-listed in the same
  turn as the fetch; 0 / 0 / 0 at 21:26Z). No lane code run (experiments/new/box48/phrestrict.py, fsrestrict.py, quotecheck2.py, box43/multi.py, box45/eprestrict.py neither
  executed nor imported). D1.
- Premises read against their text: P-N5-EPR-box45 §1-§2 at 08abd9cb (l. 52-82; sha1 8fecca79, unchanged on trunk 9bbd86e4); RESULTS R64 (a),
  (b) with EPR-1 (l. 3215-3232 at 9bbd86e4), R68 (f) (l. 3546-3548); R18 (d) Lemma S (a) with R57 (a); R38 (a); 1E-N3; N5-NCONF-box48 §9 at
  7b5876d8 (CONJECTURE RESTRICT_{u|J}, matched against the instance G^{u|J}).
- Quotes: all 8 curly-quoted EPR passages verbatim at 08abd9cb, and every "l. N" citation of §1 points at the quoted text
  (scratch/fbc_quotes.py; line numbers re-read).
- Tool: scratch/restrict_probe.py (own engine rl_engine for N5; REFEREE successor 12's own N5^τ step epr_probe.n5tau_step, written from
  SPEC with S4b^τ; checks in §4). Logs scratch/restrict_logs/.

## Verdicts (sign-off line per item)
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §0 | ODD CUT, H-admissible, len(J), (P1)-(P3) | CHECKED (definitions; (P1)-(P3) follow) |
| §1 | Lemma RESTRICT_H (i)-(iv) | SIGNED |
| §1 | Corollary REPRO_H, with EPR-1 and the "unless" clause | SIGNED |
| §2 | instances G′_E (= R64), G^u (= R68 (f)), G^{u|J} (= NCONF §9's conjecture, now proved) | SIGNED (admissibility by definition, checked) |
| §2 | instance G^P and its sentence "EVERY PHASE OF N5 ON G IS ONE N5^τ PHASE ON G^P" | SIGNED in the CONTAINMENT reading ("the states of P lie in one N5^τ phase of the run on G^P, state by state, same fallback types"). FALSE in the EQUALITY reading (gap G-RESTRICT-1, minor: wording; witness nep_n12, §2) |
| §3, §4 | data, READINGs, OPEN | not signed. §4's first READING is true but uninformative on its three examples (QP = |Q|, as the brief says; RESTRICT-N2) |
One gap (G-RESTRICT-1, wording; the proved containment is what §4 needs). Notes RESTRICT-N1..N3. Nothing here bounds QP, N5's phases or its
running time; not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. RESTRICT_H and REPRO_H, re-derived (parentheticals checked one by one)
- §0 ✓. (P1) every Odd strategy of H is one of G (succ_H ⊆ succ_G) ✓; (P2) σ̄_k is one of H (admissibility at k; for Odd v ∉ Q it is the only
  successor) ✓; (P3) τ is one of H and Even's lists are G's ✓.
- (i) ✓. Lemma S (a) on G against S1's σ̄′_k on H (P1): Ξ_k ⊴ Ξ′_k. On H against σ̄_k (P2): Ξ′_k ⊴ Ξ_k. "Antisymmetry ... a property of the order,
  not of the game" ✓ (the order is total and antisymmetric on triples, EPR l. 58-59). W: G_τ = H_τ by (P3) ✓. Only (P1)-(P3) AT k are used
  ✓, so σ̄ may change along J ✓.
- (ii) ✓. Iσ reads Ξ and Even's lists ✓. S4a's arena (Even restricted to {σ_k} ∪ Iσ_k, Odd to τ) is the same game by (P3) ✓, and S1 on its
  dual is deterministic ✓. S4c reads Iσ, Ξ and indices ✓.
- (iii) ✓. Odd's dual valuation of τ runs on the graph "Odd keeps only τ, Even keeps all": the same by (P3) ✓. S2 on G^d reads Odd's lists
  (⊆ G's by P1), so Iτ′_k = Iτ_k ∩ E(H) ✓.
- (iv) ✓. Iτ′ ≠ ∅ ⇒ Iτ ≠ ∅ ✓. In-phase on G ⇒ S4b's output on G is τ ✓ (an Odd fallback would change τ). τ is optimal in H′_G (Lemma S (a)) ✓.
  H's arena restricts Odd to a subset containing τ, so τ stays optimal there ✓ ("(iii) and (P3)" ✓).
- "Nothing else about G′_E is used" ✓: every item is a statement at one state k.
- REPRO_H ✓. EPR §2's induction on k ∈ [x, y′ − 1] ⊆ J verbatim ✓.
  - Iσ_k ≠ ∅ on an in-phase transition ✓.
  - S4a's output is the same (ii) ✓.
  - S4b^τ returns τ (by SPEC if Iτ′ = ∅, else by (iv)) ✓.
  - The fallback fires on both or neither, and is Even's on both (ii) ✓.
  - λ′ = λ at x, …, y by (i) at states of J ✓: one N5^τ phase ✓.
  - EPR-1: the last transition y → y′ may leave it ✓.
  - "unless σ̄_{y′} is also an Odd strategy of H (then J ∪ {y′} is H-admissible and y′ is in that phase too)" ✓. y → y′ in-phase on G means
    y′ is in P, so J ∪ {y′} is a run of P. With (P2) at y′ it is admissible, and (i) at y′ gives λ′ = λ.

## 2. The instances, and G-RESTRICT-1
- G′_E ✓ (σ̄_k = σ̄_E on an epoch; v ∉ D_E has σ̄_E(v) = τ(v)). G^u ✓ (D_k ⊆ {u} gives σ̄_k(v) = τ(v) for v ≠ u; u keeps all edges).
  G^{u|J} ✓: on a frozen-side stretch σ̄_k = σ̄_J on Q ∖ {u}, D⁻-vertices keep {τ, σ̄_J}, the others τ, and u everything. Matched word for word
  against N5-NCONF §9's CONJECTURE RESTRICT_{u|J} at 7b5876d8 ("For k ∈ J, RESULTS R64 (a) (i)-(iv) hold with G′_E replaced by G^{u|J} …"):
  the instance proves it.
- G^P ✓ as an instance: P is G^P-admissible by construction; len(P) = y − x "(y → y + 1 leaves P by maximality)" ✓; so REPRO_H reproduces
  every in-phase transition of P with no EPR-1 exit ✓; G^P ∈ 𝒞^{QP}O ✓.
- G-RESTRICT-1 (the bold sentence). REPRO_H proves that the states of P lie in ONE N5^τ phase on G^P. It says nothing about the N5^τ
  transition from y, because y → y + 1 is not an in-phase transition of N5 on G. That transition can stay in the phase.
  - Witness: nep_n12 (experiments/n5-epoch/results/climb/nep_n12.pg, sha1 682f6bf3) at its .start.
  - On G, P = states [0, 1]: τ changes at 1 → 2 (τ(1): 10 → 8, the Odd edge (1, 8)).
  - G^P keeps Odd lists 1: {9, 10}, 6: {3, 5, 7}, 7: {2, 11}, 11: {1, 3, 9}. So (1, 8) ∉ E(G^P), and by RESTRICT_H (iii) Iτ′ = Iτ ∩ E(G^P) does
    not contain it.
  - N5^τ on G^P keeps τ at y = 1 and moves to G's σ_2 with the same λ′ and τ. Its phase holds states 0, 1, 2 ⊋ P.
  - In data, 44 of 4,073 phases extend this way (§4).
  - So the sentence holds as "lies in one N5^τ phase on G^P". It is false as "is exactly one". The containment is the direction §4's
    READING needs: a per-phase count on G^P bounds P's length. Repair: replace "IS ONE" by "LIES IN ONE".

## 3. §4 READING (not signed), as briefed
- "nep90, nep76 and long121 … are N5^τ phases of games with 5, 5 and 3 Odd choice vertices" is true and reproduced: phases of 91 / 78 / 121
  in-phase transitions, QP = 5 / 5 / 3, XDEG = 22 / 24 / 8, exactly the packet's numbers. But the games themselves have |Q| = 5 / 5 / 3, so G^P
  removes no Odd choice vertex there (RESTRICT-N2, as L-NEW 28's N5-NCONF §11 correction says).
- In general G^P does reduce: QP < |Q| in 2,307 of 4,073 phases (most of them in random 𝒞^kO games). The largest QP is 18 (lib, |Q| up to 30).
- The second READING (transfer of R61's 𝒞^kO counts to N5^τ) is stated as unchecked by the packet itself; not examined here.

## 4. Data (own engines; DATA, not proof; 0 failures of every signed check)
Checks (scratch/restrict_probe.py, per phase P of N5 on G): R1-R4 = RESTRICT_H (i)-(iv) at every k ∈ J; REP = REPRO_H over len(J)
transitions (σ, τ and fallback flag); ONEPH = λ′ = λ at the states of J; UNLESS = the "unless" clause when y → y′ is in-phase and σ̄_{y′} ∈
H; EXITLAM = an EPR-1 exit that actually leaves (count); EXT = G^P's N5^τ phase extends past y (count). Families: GP = G^P with J = P; RH =
a random admissible cut between G^P and G (each other Odd edge kept with probability 1/2); GE = G′_E per epoch; GU = G^u per maximal u-run;
GUJ = G^{u|J} per maximal frozen-side u-stretch.
| set (log in restrict_logs/) | N5 runs | phases (in-phase transitions) | R checks GP / RH / GE / GU / GUJ | REP transitions GP / GE / GU / GUJ | UNLESS GE / GUJ | EXITLAM GE / GU / GUJ | EXT (GP) | failures |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib 1,140 files, n ≤ 40 (4 parts), S3 + given + 2 random | 2,739 | 2,368 (18,036) | 20,404 ×3 / 25,667 / 55,229 | 18,036 / 18,036 / 20,991 / 45,109 | 870 / 2,508 | 538 / 397 / 1,674 | 41 | 0 |
| lib41 (experiments/new/box41), n ≤ 64, S3 + 1 random (families GP, RH, GE, GU) | 763 | 742 (9,510) | 10,252 ×3 / 11,155 / — | 9,510 / 9,510 / 9,966 / — | 271 / — | 263 / 30 / — | 3 | 0 |
| random 𝒞^kO, n 6-20, k ≤ 8, seed 481 | 4,500 | 960 (1,102) | 2,062 ×3 / 4,547 / 5,510 | 1,102 / 1,102 / 2,384 / 2,888 | 40 / 107 | 9 / 26 / 39 | 0 | 0 |
| nep90 / nep76 / long121 at their starts | 3 | 3 (290) | 293 ×3 / 46 / 1,221 | 290 / 290 / 33 / 1,208 | 31 / 127 | 0 / 0 / 0 | 0 | 0 |
- Totals: 8,005 N5 runs, 4,073 phases, 28,938 in-phase transitions reproduced on G^P (and on G′_E); 202,408 RESTRICT_H checks over the five
  families; 3,954 "unless" checks; EPR-1 exits that really leave: 2,976 (GE 810, GU 453, GUJ 1,713). Those are not failures; they are what
  EPR-1 allows.
- Control MUT=1 (G^P without (v, σ̄_x(v)) for the first v with σ̄_x(v) ≠ τ(v), so (P2) fails at x) bites. On the three long instances: R1 57,
  R2 34, REP 2 of 3 (nep76, long121; nep90's REP survives, as in the lane's own control: 1 / 0, 1 / 1, 1 / 1). On 400 random games: R1 13,
  R2 4, REP 3, ONEPH 1.

## 5. Notes
- RESTRICT-N1 (= G-RESTRICT-1's repair). "IS ONE N5^τ PHASE ON G^P" → "LIES IN ONE N5^τ PHASE ON G^P"; the phase on G^P can be longer
  (nep_n12; 44 phases).
- RESTRICT-N2 (§4, as briefed). The first READING's examples have QP = |Q| (5 / 5 / 3); G^P reduces nothing there. Say so, or pick examples
  with QP < |Q| (common in random games).
- RESTRICT-N3 (scope). RESTRICT_H is a statement at one state per item; REPRO_H needs admissibility at every state of [x, y′ − 1] and, for the
  last state's phase, at y′. The G^{u|J} instance therefore settles N5-NCONF §9's CONJECTURE RESTRICT_{u|J} in full (both referees will
  need to agree before it lands).

DONE: this report. FINDINGS: RESTRICT_H, REPRO_H and the four instances SIGNED; G-RESTRICT-1 (G^P's "IS ONE phase" true only as
containment); RESTRICT-N2 confirmed. NEEDS: Lead: route G-RESTRICT-1 and RESTRICT-N1..N3 to L-NEW's fixes file; §C against REFEREE-2 on your
word.

## §C. Comparison with REFEREE-2 (written 2026-10-28T23:23Z by date -u, after the Lead's word of 23:21Z; REFEREE-2's report
docs/referee-2/R2-N5-RESTRICT.md, sha1 7c18aed3…, at origin/claude/referee-2 9549e59a; read only after the report above was pushed at c9bdfa68)
Written by REFEREE successor 17, as successor to the author (successor 16). Every verdict is labelled (Opus 5.5, D15).
- Where the file is: the Lead's word says it is on trunk; at my fetch (trunk f86a4145) it is not. I read it at origin/claude/referee-2 9549e59a
  (same sha1 as that branch's head copy).
- Verdicts identical: RESTRICT_H (i)-(iv), REPRO_H (with EPR-1 and the "unless" clause) and the admissibility of the four instances SIGNED by
  both; §4's first READING not signed by either and UNINFORMATIVE on its examples (QP = |Q| = 5 / 5 / 3) by both.
- Joint gap map: {G-RESTRICT-1 = G-R2-RESTRICT-1}. Same sentence ("EVERY PHASE OF N5 ON G IS ONE N5^τ PHASE ON G^P …"), same verdict: true as
  containment, false as equality.
  - Two witnesses, two MECHANISMS, both reproduced on my engine (scratch/restrict_probe.py, sha1 f451e00a…, env ONE=1 adds one-state phases for G^P):
    - nep_n12 (successor 16): the edge of G's τ-move, (1, 8), is not in G^P, so N5^τ cannot make it (phase [0, 1] extends to state 2).
    - nh_r2802 (REFEREE-2; experiments/new/box28/out/nh_r2802.pg.pg, sha1 8652ac82): G^P = G at the one-state phase [0, 0], and the extension
      comes from N5^τ's own S4b^τ rule (τ kept when value-optimal; SPEC's S4b moves it on a tie). REPRODUCED: my probe reports GP_EXT at [0, 0].
      This shows the equality reading fails even with no edge cut, which successor 16's witness did not show.
  - Data difference explained: successor 16's 44 of 4,073 counted multi-state phases only (the probe skipped one-state phases). With one-state
    phases included (ONE=1, lib1140, G^P only; restrict_logs/sc_lib1140_one_part00-03.txt): 186 of 11,527 phase ends extend, all of them
    τ-ends (7,312 τ-ends, 4,215 λ-ends), 0 failures of (i)-(iv), REPRO_H (12,625 runs, 18,036 transitions). REFEREE-2: 176 of 39,385, all τ-ends.
  - JOINT REPAIR: REFEREE-2's wording, which implies successor 16's "LIES IN ONE": "every phase P of N5 on G is the INITIAL SEGMENT, of len(P)
    transitions, of the first N5^τ phase on G^P started at (σ_x, τ)", with the addition below.
- REFEREE-2's parenthesis "Equality holds when P ends by a λ change": an unproved claim in its report (data only). I PROVE it (Opus 5.5, D15):
  let y → y + 1 leave P on G with τ_{y+1} = τ, so λ_{y+1} ≠ λ_y; σ_{y+1} ≠ σ_y (λ depends on σ alone), so Iσ_y ≠ ∅ and N5^τ does not stop at y. N5^τ on G^P steps from y to (σ_{y+1}, τ) with the same fallback type: (ii)
  at y (y ∈ J); S4b's output on G at y is τ (no Odd fallback, τ unchanged), so S4b^τ on G^P keeps τ by (iv)'s argument; S4c fires on both or
  neither. Take v with λ_{y+1}(v) ≠ λ_y(v). R15 (a), (d) give Ξ_{y+1}(v) ⊵ Ξ_y(v), and distinct cycle nodes have distinct rewards, so
  reward(λ_{y+1}(v)) > reward(λ_y(v)). Every Odd strategy of G^P is one of G (P1), so Lemma S (a) (R18 (d)) gives Ξ_{y+1} ⊴ Ξ′_{y+1}, hence
  reward(λ′_{y+1}(v)) ≥ reward(λ_{y+1}(v)) > reward(λ_y(v)) = reward(λ′_y(v)) ((i) at y). So λ′_{y+1} ≠ λ′_y and the N5^τ phase ends at y. □
  Data agree: 0 of 4,215 λ-ends extend (above), 0 of 11,777 in REFEREE-2's. Only τ-ends can extend. Add it to the joint repair:
  "… equal to it when P ends by a λ change".
- The EXPOSURE REFEREE-2 declared, weighed:
  - What it saw before reviewing: the subject line of c9bdfa68, i.e. successor 16's verdicts on ALL items (RESTRICT_H, REPRO_H, instances
    SIGNED), the subject of the gap and the witness name nep_n12. So the exposure is not limited to the G^P finding as its report says: it knew
    the SIGN verdicts too.
  - The SIGNATURES (RESTRICT_H, REPRO_H, instances): each referee re-derived every step line by line (successor 16 independently, REFEREE-2
    after the exposure) and ran its own checker on its own corpus with 0 failures (REFEREE-2: 21,971 runs, a different engine lineage built on
    si.py, which SPEC S1 names as its reference). The proofs are short, one state per item, and every step is checkable by a reader. My
    reading: the two signatures stand, with REFEREE-2's recorded as anchored, not blind.
  - The GAP: a refutation stands on its witnesses, not on agreement between referees. Both witnesses re-check on my own engine, and REFEREE-2's
    witness came from its own library run by a mechanism successor 16 did not find (no edge cut). So G-RESTRICT-1 needs no independent second
    finding to hold. What the exposure costs is only the claim that two referees found it independently: it should be recorded as found by
    REFEREE (successor 16) and CONFIRMED by REFEREE-2 (anchored), with REFEREE-2's own witness nh_r2802.
  - The repair wording and the λ-end equality (proved above) are independent additions by REFEREE-2 and by me; neither depends on the exposure.
- Notes matched:
  - RESTRICT-N1 (repair) = G-R2-RESTRICT-1's repair; superseded by the JOINT REPAIR above.
  - RESTRICT-N2 = N-RESTRICT-2 (first READING uninformative). REFEREE-2 adds XDEG(G) = 24 / 26 / 9 against XDEG(G^P) = 22 / 24 / 8: ACCEPTED.
  - RESTRICT-N3 (G^{u|J} settles N5-NCONF §9's CONJECTURE RESTRICT_{u|J}): REFEREE-2 signs G^{u|J}'s admissibility and RESTRICT_H covers it,
    so both referees' signatures cover that conjecture as an instance. It lands only with the Lead's routing.
  - N-RESTRICT-1 (no EPR-1 exit for G^P): ACCEPTED; same as successor 16's §2 ("no EPR-1 exit").
  - N-RESTRICT-3 (second READING: transfer needs N5^τ counts, and the longer phase): ACCEPTED; successor 16 did not examine it, and with the
    joint repair a bound on N5^τ phase lengths on G^P bounds len(P).
- Nothing else open on RESTRICT. RESTRICT bounds nothing; G-N5-TIME stays OPEN.
