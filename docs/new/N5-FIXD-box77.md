# N5-FIXD (box 77): a non-growing (σ, σ̄) pair potential FIX-DEPTH (range n(n+2), monotone) reduces phase length to per-vertex DEAD-BRANCH climbs FLAT; FLAT-LIN is DEAD (nep92_n40: 66 = 1.65n)
L-NEW successor 36 (Opus 5.5), D14 / D18, Lead reading L40. Lead 07:23Z (read 07:54Z): «BOX 76: a (σ, σ̄) PAIR potential for phase length, i.e.
your box-75 obstruction turned around … a polynomial-range coarsening of the pair's state that still strictly increases at every transition
of a phase, or at least once per bounded number of transitions. Test each candidate against thetaA_n7, cr_n80 and snap_n80_s62 … check
every candidate against [the box-74 reading]». Box 76 had already been used for SBQ-2 (the 07:11Z brief), so this is box 77. Written
07:55Z-08:15Z (date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME OPEN.
- Also in this push: the L-RED R133 hazard fix (Lead 07:34Z). box72/n5lz.py cached its W-engine in a module dict keyed by τ only, so two
  games in one process got wrong runs. The cache now lives on the game object (g.__dict__["_n5lz_wc"]). One-game-per-process drivers
  (every box 72-77 tool) were unaffected. check.sh passes unchanged.
- Tools in experiments/new/box77:
  - fixdepth.py: FIX-DEPTH, its monotonicity check, flat transitions and stalls, FLAT per (v, phase);
  - climb_flat.py: hill climb on max FLAT_P(v);
  - run.sh: the 1132 runs, N5 and N5-LZC, written to fixd_*.txt;
  - out/*.log.
- Instances (inst/, with .start): cf_n80.pg sha1 4b708b06…, cfl_n24.pg ae682d6b….

## 1. The candidate: FIX-DEPTH (PROVED, lane)
- Definition. Fix a phase P = [a, b] and let fin := Ξ_b. For a state t of P and a vertex v, DEPTH_t(v) is the number of leading
  coordinates of Ξ_t(v) that equal fin(v), in the [S1-ord] coordinate sequence: cycle reward, then P-bits from rank n − 1 down, then signed
  length. DEPTH is n + 2 if the two are equal. K_t := Σ_v DEPTH_t(v) ∈ [0, n(n + 2)].
- It is a function of the PAIR (σ_t, σ̄_t) through Ξ_t, with the phase's end value as a fixed reference. That is box 75's obstruction
  turned around, as asked.
- Lemma FIXD-MON. K never decreases inside a phase.
  - Proof. By [R15], Ξ_t(v) ⊴ Ξ_{t′}(v) ⊴ fin(v) for t ≤ t′ in P. In a lexicographic order every element of [x, y] carries the common
    prefix of x and y (box 73 LEVEL-MON).
  - So DEPTH_{t′}(v) ≥ DEPTH_t(v). □
  - DATA: 0 decreases in 1132 + 1132 runs.
- It is NON-GROWING: its range n(n + 2) does not depend on |P|. So it is a legitimate closing link in the sense of box 74 §4.

## 2. Theorem PHASE-RED (PROVED, lane; N5, and N5-LZC by box 73 §4 (a))
- Statement. For every phase P: |P| ≤ (4n(n − 1) + 1)·(CH_P + 1) and CH_P ≤ n(n + 2) + Σ_v FLAT_P(v), where:
  - CH_P := the transitions of P at which Ξ changes somewhere;
  - FLAT_P(v) := the transitions of P at which Ξ(v) changes but DEPTH(v) does not (a DEAD-BRANCH climb). Ξ(v) moves inside the subtree
    below its lcp with fin(v), and that subtree is wholly overtaken later by the jump at the first differing coordinate.
- Proof.
  - A Ξ-changing transition either raises K (at most n(n + 2) such transitions, by §1) or changes Ξ only at vertices whose DEPTH stays.
    Charge the latter to one such vertex: a FLAT event.
  - Between Ξ-changing transitions, Ξ (= Ωσ) is unchanged, and τ is fixed in the phase. By [Q RESULTS R15 (d)] «at most 4n(n−1)
    consecutive N5 iterations leave both Ωσ and Ωτ unchanged», there are at most 4n(n − 1) such transitions in a row. Here Ωτ is
    unchanged because τ is. □
- So phase length is polynomial iff Σ_v FLAT_P(v) is (up to the factor 4n(n − 1) + 1).
- FLAT is a per-vertex DEPTH quantity, a count of moves of one vertex, not the breadth that killed ρ / SBQ (boxes 74-76).

## 3. Tests (DATA; the Lead's three instances, plus L-SI's long run family)
| instance | phase length | K-strict | flat transitions | longest stall | max FLAT_P(v) |
| --- | --- | --- | --- | --- | --- |
| thetaA_n7 + start (n 7) | 3 | 3 | 0 | 0 | 0 |
| cr_n80 (box 74) | 20 | 6 | 14 | 14 | 18 (v 4) |
| snap_n80_s62 + start | 100 | 23 | 77 | 36 | 66 (v 17) |
| runfam_K40 (n 79) | 159 | 98 | 61 | 61 | 6 |
- On thetaA_n7, K rises at every transition; it survives the instance that killed every σ̄-only potential.
- On cr_n80 / snap_n80, K stalls for up to 36 transitions. On runfam the stalls are long (61) but are spread over many vertices (FLAT ≤ 6
  each).
- Corpus (1132 × N5 and N5-LZC):
  - flat transitions 6568 of 16183 (N5) and 6430 of 15884 (N5-LZC);
  - max stall 91 (red/n5inj returns_ph64, n 64);
  - max FLAT_P(v) 69 (nep94_n48), with max ratio 1.65n.
- Climbs on max FLAT_P(v), 15 min each:
  - cf_n80 (seed snap_n80_s62): 78 (0.98n);
  - cfl_n24 (seed nep13_n24): 27 (1.13n).
  Both are below the corpus maximum ratio.

## 4. DEAD and the exact obstruction
- K strictly increasing at every transition (or once per O(1) transitions) is DEAD: snap_n80_s62 stalls 36 consecutive transitions, and
  returns_ph64 stalls 91.
- CONJECTURE FLAT-LIN (FLAT_P(v) ≤ n) is DEAD on the corpus. Kill: experiments/n5-epoch/instances/nep92_n40.pg + .start (sha1
  ce224ec31e56e18103290d4aac81a9f225f76bfc): vertex 0 has 66 = 1.65n dead-branch climbs in one 92-transition phase. Same on N5-LZC.
- Obstruction. A dead-branch climb is a strict Ξ-rise of v inside the subtree below its lcp with fin(v). The values there form a lex
  sub-order of exponential size: a counter.
  - Recursing FIX-DEPTH inside the subtree (end-of-segment value as the new reference) gives a nested potential with ≤ n + 2 levels.
    That is the binary-counter bound (n + 2)^{levels}, not a polynomial.
  - So no PER-VERTEX lcp potential closes FLAT. A bound on FLAT must charge a dead-branch climb of v to OTHER vertices, e.g. through the
    inheritance chain of box 72 TXC-SRC: a flat climb of v inherited from σ(v) / σ̄(v) is a flat or depth event downstream.
  - Untested: CONJECTURE FLAT-SRC, every flat climb of v is inherited along a chain from a source that is a DEPTH event (K-rise) of
    another vertex or an Even switch. If each source feeds O(n) flat climbs, then Σ FLAT ≤ O(n)·(K-range + switches), and the remaining
    count is Even's switches, i.e. the per-vertex decision count of box 76 again.

## DONE / FINDINGS / NEEDS
- DONE:
  - box77/fixdepth.py, climb_flat.py, run.sh; fixd_*.txt (1132 × 2); inst/cf_n80, cfl_n24; out/ logs;
  - box72/n5lz.py cache fix (R133 hazard);
  - this note; check.sh "box 77" (pins nep92_n40).
- FINDINGS:
  1. PROVED (lane): FIX-DEPTH, a pair potential of range n(n + 2), monotone in every phase (FIXD-MON; DATA 0 decreases). It survives
     thetaA_n7 and rises at every transition there.
  2. PROVED (lane): Theorem PHASE-RED. |P| ≤ (4n(n − 1) + 1)(n(n + 2) + Σ_v FLAT_P(v) + 1) (R15 (d) for Ξ-flat steps). Phase length is
     reduced to per-vertex dead-branch climbs, a depth count, not breadth.
  3. DEAD: "K rises every O(1) transitions" (stalls 36 on snap_n80_s62, 91 on returns_ph64). DEAD: FLAT-LIN (nep92_n40, sha1 ce224ec3…:
     66 = 1.65n at one vertex, one phase).
  4. Obstruction: dead-branch climbs are lex counters; any per-vertex recursion is a counter. A bound must charge across vertices
     (CONJECTURE FLAT-SRC, untested).
  5. R133 hazard fixed in box72/n5lz.py.
- NEEDS: none from the owner. From the Lead: next box FLAT-SRC (measure the inheritance sources of dead-branch climbs), or another. Context
  is about 380k of 550k, so one more box, then I park.
