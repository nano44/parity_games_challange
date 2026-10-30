# R-N5-FIXD: REFEREE report on packet P-N5-FIXD (L-NEW box 91): FIX-DEPTH, FIXD-MON, PHASE-RED with FLATTR; PHASE-RED′ under FLAT-SW
Referee: REFEREE (successor 20), Opus 5.5 (D15). Lead brief 2026-10-30 (session start 15:46Z by date -u). REFEREE-2 reviews independently.
- Object and pin: docs/new/P-N5-FIXD-box91.md at claude/l-new 5027c17c, `git show 5027c17c:<path> | sha1sum` =
  2050e167a300c676d54178cdc34ccf2daec87036 (89 lines). Line file docs/new/P-N5-FIXD-box91-line.txt sha1
  ba09dd261d5c885441845e09104f5e60bf0a81ed. Both equal the Lead's figures (Lead 15:58Z) and the freeze commit message.
- Runs 2026-10-30T15:49Z-16:01Z; report written from 15:58Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independence: I opened no docs/referee-2/ file for this packet.
- Premises opened: RESULTS R15 (a), (b), (d) (l. 624 ff.); R38 (a) (Remark KEY, l. 1825); R57 (standing SPEC premise); R93 (a) (Fact REW, Fact
  LEX, COMMON PREFIX, l. 7031-7036); SPEC docs/new/N5-ssi-global.md S1 (injective ranks, l. 27-31); the R93 object
  P-N5-WCH-box79.md @ 2ad78f51 (sha1 31caa72e, §2.1 l. 119-128). Sources box 77 / box 79 notes (working notes; the packet governs).
- Quotes: the [LEX] quote fragments are verbatim in P-N5-WCH-box79.md (the R93 object, sha1 31caa72e, unchanged on trunk). The [R15] (a), (d)
  fragments are verbatim in RESULTS R15. I checked them mechanically: «…» split at «…», whitespace-normalised. The two Lead quotes in l. 2-5
  are messages and cannot be checked against any file.
- Scope (D1): a REDUCTION for N5 on every game. Phase length is reduced to FLATTR_P, which is unbounded here. G-N5-TIME stays OPEN. Not a
  TARGET.md claim.

## Verdicts
| § | item | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| 1 | setting, premises, MON | CHECKED. MON is R15 (a) applied at every σ-changing transition (R15 (d): I ⊆ Iσ, one edge per vertex), and is trivial at the others. Ξ_σ = Ωσ is the standing SPEC premise of R57, which the line must carry (FIXD-N2) |
| 2 | Definition FIX-DEPTH; Lemma FIXD-MON | SIGNED |
| 3 | Theorem PHASE-RED (i), (ii), combined | SIGNED |
| 4 | Corollary PHASE-RED′ (the implication from FLAT-SW) | SIGNED |
| 4 | CONJECTURE FLAT-SW (packet: not to sign) | Not signed as a packet item. I PROVE it here (Theorem SW-KEEP, §4b), so PHASE-RED′ holds unconditionally. This is a REFEREE proof and needs REFEREE-2's independent check before anyone uses it |
| 5 | DATA, DEAD, READING | not signed. Pins re-run with my own engine: all MATCH (§5). One mislabel: «6568 of 16183 Ξ-changing» should read «of 16183 in-phase transitions» (FIXD-N3) |
| — | RESULTS line (ba09dd26) | MATCHES §2-§4 and claims nothing more. The strict symbol test finds ONE free symbol: k in the PHASE-RED′ clause (FIXD-N1). The standing premise is missing (FIXD-N2). Citation form (FIXD-N4) |
No gap in §2-§4. Nothing FALSE. Notes FIXD-N1..N4.

## 2. FIX-DEPTH and FIXD-MON
- CS is injective on values:
  - rew is injective (R93 (a) Fact REW, from injective ranks), so CS's first coordinate fixes c;
  - the s_r ≠ 0 coordinates fix the path set;
  - ℓ̂ fixes ℓ once c is known.
  So "DEPTH = n + 2 iff Ξ_t(v) = fin(v)" holds, DEPTH ∈ [0, n + 2] and K ∈ [0, n(n + 2)].
- FIXD-MON ✓:
  - MON along t, …, t′, …, b gives Ξ_t(v) ⊴ Ξ_{t′}(v) ⊴ fin(v);
  - COMMON PREFIX (signed in R93 (a)) carries the first DEPTH_t(v) coordinates to Ξ_{t′}(v).
  - I re-derived COMMON PREFIX myself. The direction of ℓ̂ depends only on c, which lies in the prefix whenever L ≥ 1; for L = 0 there is
    nothing to prove.
- The Remark (holds whatever kind each transition is) ✓: inside a phase τ is constant, and σ either changes by Switch_I or does not change.

## 3. PHASE-RED
- (i) ✓. K is a non-decreasing integer with K_a ≥ 0 and K_b = n(n + 2), so at most n(n + 2) transitions raise it. Every other
  Ξ-changing transition is FLATTR by definition. The equivalence "K unchanged iff no DEPTH changes" ✓ follows from FIXD-MON per vertex.
- (ii) ✓.
  - R15 (d) bounds consecutive iterations that leave both Ωσ and Ωτ unchanged.
  - Ωτ is a function of τ (R38 (a) KEY; SPEC S1 "Odd's side"), and τ is constant in a phase.
  - The CH_P transitions cut the remaining |P| − CH_P transitions into at most CH_P + 1 blocks, each of length ≤ 4n(n − 1).
  - So |P| ≤ CH_P + 4n(n − 1)(CH_P + 1) ≤ (4n(n − 1) + 1)(CH_P + 1).
- |P| = b − a counts transitions with both states in P. This matches the counts I re-ran (§5).

## 4. PHASE-RED′
- The implication ✓. The chosen x is counted in FLATSW_P(x), and distinct transitions give distinct pairs (x, k). So FLATTR_P ≤ Σ_x FLATSW_P(x).
- Note: in a FLATTR transition no DEPTH changes, so every Ξ(x)-change counted in FLATSW is a flat change. The line's definition is the
  packet's §4 definition, verbatim.

## 4b. Theorem SW-KEEP (REFEREE proof; FLAT-SW follows)
Premises: R15 (a) (Lemma A) and the standing SPEC premise of R57 (S1's σ̄_σ realises the pointwise optimum: Ξ_σ ⊴ val(σ, π) for every
positional Odd π). Values are (c, Q, ℓ). x ⊕ (c, Q, ℓ) := (c, Q ∪ {x if rank x > rank c}, ℓ + 1). ⊴ is total and antisymmetric on values
(CS is injective).
- Fact F (play valuations of a positional pair). Suppose Even x is not its own cycle node. Then val(x) = x ⊕ val(σ(x)), and x is not in
  val(σ(x))'s path set: the play from σ(x) reaches the cycle node before it could revisit x. If x is its own cycle node, then
  val(x) = (x, ∅, 0) and val(σ(x)) = (x, ∅, ℓ): σ(x) lies on x's cycle, and the cycle's other vertices rank below x.
- Theorem SW-KEEP. Let I be a non-empty set of Ξ_σ-improving edges with at most one edge per vertex, σ′ := Switch_I(σ), and S the set of
  switched vertices. If Ξ_σ′(x) = Ξ_σ(x) for every x ∈ S, then Ξ_σ′ = Ξ_σ. Moreover, every x ∈ S with Ξ_σ′(x) = Ξ_σ(x) is its own cycle node
  under both σ and σ′.
- Proof.
  (1) Take x ∈ S with Ξ_σ′(x) = Ξ_σ(x). Put d := σ(x), e := σ′(x); then Ξ_σ(d) ◁ Ξ_σ(e), since the edge is improving. "x is its own cycle
      node" means that the first component of its value is x. Three cases:
      - (1a) Exactly one state. Say x is its own cycle node under one strategy and not under the other. Then the first components of
        Ξ_σ(x) and Ξ_σ′(x) are x and some c ≠ x, so Ξ_σ′(x) ≠ Ξ_σ(x), against the choice of x. This covers both orders, σ and σ′.
      - (1b) Neither state. By F,
      x ⊕ Ξ_σ(d) = x ⊕ Ξ_σ′(e), with the same cycle node on both sides and x in neither path set. x ⊕ · is injective there, so
      Ξ_σ′(e) = Ξ_σ(d) ◁ Ξ_σ(e) ⊴ Ξ_σ′(e) (by R15 (a)), a contradiction.
      - (1c) Both states. This is the only remaining case, and then Ξ_σ(x) = Ξ_σ′(x) = (x, ∅, 0).
  (2) By F, Ξ_σ(d) = (x, ∅, ℓ_d) and Ξ_σ′(e) = (x, ∅, ℓ′). These two sandwich Ξ_σ(e), and their CS agree on the first n + 1 coordinates. By
      COMMON PREFIX, Ξ_σ(e) = (x, ∅, ℓ_e). So π_e, the (σ, σ̄_σ)-play from e, reaches x through vertices that rank below x. It meets no
      x′ ∈ S \ {x}: otherwise x′'s play is a suffix of π_e with cycle node x ≠ x′, which contradicts (1) for x′.
  (3) Let Y be the valuation of the (σ′, σ̄_σ)-plays, and v a vertex with (σ, σ̄_σ)-play π.
      - If π avoids S, it is also v's (σ′, σ̄_σ)-play, so Y(v) = Ξ_σ(v).
      - Otherwise let x be the first vertex of S on π, and p the part of π before x. p uses no switched vertex, and no vertex of x's old cycle
        is switched (by (1), such a vertex would have cycle node x). Under σ the play goes on around x's cycle, so
        Ξ_σ(v) = (x, Q(p), |p|). Under σ′ it closes x → e → π_e → x, which is unchanged by (2) and has x as its top vertex. So
        Y(v) = (x, Q(p), |p|).
      Hence Y = Ξ_σ.
  (4) Ξ_σ′ ⊴ Y pointwise (optimality against σ′), and Ξ_σ ⊴ Ξ_σ′ (R15 (a)). So Ξ_σ′ = Ξ_σ. □
- Corollary FLAT-SW (the packet's CONJECTURE). It holds on every N5 run, and the same proof covers N5-LZC.
  - Ξ depends on σ alone, so a Ξ-changing transition changes σ.
  - By R15 (d), σ_{k+1} = Switch_I(σ_k) with ∅ ≠ I ⊆ Iσ_k and one edge per vertex. In N5-LZC, a switched vertex takes σ*(v) ≠ σ_t(v), which
    is an Iσ_t edge.
  - SW-KEEP then gives a switched x with Ξ_{k+1}(x) ≠ Ξ_k(x) at EVERY Ξ-changing transition, not only at those counted in FLATTR_P.
  So PHASE-RED′ holds unconditionally:
  |P| ≤ (4n(n − 1) + 1)(n(n + 2) + Σ_x FLATSW_P(x) + 1).
- This is the converse direction to R15 (b) (Lemma B): if Ω does not change, every switch is a length-only switch at a cycle node. Here,
  if every switched vertex keeps its value, then Ω does not change.
- Controls (§5): fsw_strong.py counts the strong form at every τ-constant σ-changing transition. It found 0 violations. Every kept switched x
  was its own cycle node at both states: 0 cases on its cycle but not its node, 0 off-cycle cases. This is what (1) predicts.
- Status: a REFEREE proof, not a lane claim. It needs REFEREE-2's independent check before the Lead uses it in a RESULTS line.

## 5. Controls and pins (own engine; docs/referee/scratch/, `python3 -I`)
- fixd_probe.py (rl_engine; N5-LZC through wch_probe's one-line patch) checks:
  - XM: Ξ_t ⊴ Ξ_{t+1} ⊴ fin;
  - KM: FIXD-MON per vertex;
  - ST: the R15 (d) stall bound;
  - PR1/PR2/PR3: PHASE-RED's three inequalities (PR3 is FLATTR ≤ Σ_v FLAT);
  - PRp: PHASE-RED′;
  - SW: FLAT-SW.
- Mutations: MUT 1 (reference Ξ_a instead of fin) bites KM 69 and PR3 1 on nep92_n40. MUT 3 (drop n(n + 2)) bites PR2 2. MUT 4 (FLAT-SW only
  through x with an Even old successor) bites SW 1. MUT 2 (stall bound n) never bites: the largest stall seen is 2.
- Pins (all MATCH):
  - nep92_n40 + .start (sha1 ce224ec3…): FLAT(v0) = 66 in a 92-transition phase [6, 98]; FLATTR 73; FSW 73; flat switches ≤ 8 per vertex.
  - returns_ph64: max FLATTR 91.
  - returns_rt64: max FLATSW_P(x) 14 (returns_rt48 ties).
  - nep94_n48: max FLAT 69 (box 77).
- Corpus (box 77's run set: sbcg.lst 719 with the best-reward start; alt_all.lst 413 with the listed start, if any; N5 and N5-LZC):
  - 1132 × 2 runs (per-run files concatenated into fixd_logs/sbcg.txt and alt.txt, then deleted; the per-run grep kept GAME, RC, the counts,
    STAT and every *_V line), every one RC 0, and ZERO violation lines of XM, KM, ST, PR1, PR2, PR3, PRp
    or SW in either engine.
  - N5: 15275 in-phase transitions; 15210 Ξ-changing; 8750 with a K-rise; FLATTR 6460, all with a flat Even switch (FSW 6460).
  - N5-LZC: 14979; 14928; 8592; FLATTR 6336 = FSW.
  - Maxima (both engines): FLATTR per phase 91 (returns_ph64); FLAT_P(v) 69 (nep94_n48); FLATSW_P(x) 14 (returns_rt48 and returns_rt64);
    the longest Ξ-unchanged stall is 2 transitions.
  - SW-KEEP strong form (fsw_strong.py over the 719 distinct games, best-reward start plus sibling .start, both engines; fixd_logs/strong_sum.txt): 27586 τ-constant transitions, 27504 of them Ξ-changing; 0 STRONG
    violations. 96 switched vertices kept Ξ, all of them own cycle nodes (keep_cyc 0, keep_OFF 0); no maxit.
- Run-set note: my aggregate totals are a few percent below the lane's (6503 FLATTR; 16183 transitions). I did not reconcile this. The
  per-instance pins match exactly.

## 6. RESULTS line (ba09dd26): diff against §2-§4 and the strict symbol test
- Content: the three claims are the packet's §2-§4 statements verbatim in substance, and the line claims nothing more. "(K_t ∈ [0, n(n + 2)])"
  ✓. The suffix "a REDUCTION … not a TARGET.md claim" ✓.
- Tokens and their binders:
  - n, run, state, transition, Ξ_t, σ̄_t, λ_Ξ, ⊴ ◁ ⊵ ▷, P = [a, b], |P|, CS (via R93), DEPTH_t(v), K_t, CH_P, FLATTR_P, switched, FLATSW_P(x),
    "Even": all bound in the parenthesis.
  - σ_t, τ_t: through SPEC S1-S5 and "states (σ_t, τ_t)", as in R93's line ✓.
  - 4n(n − 1): R15 (d) ✓.
- FIXD-N1 (FREE SYMBOL). In «(Corollary PHASE-RED′, an implication) if every transition counted in FLATTR_P … has a switched Even vertex x with
  Ξ_{k+1}(x) ≠ Ξ_k(x)», k has no binder. The only earlier k is local to the definition «x is switched at k if …». Fix: «if every transition
  k → k + 1 counted in FLATTR_P (any phase P of any N5 run) has an Even vertex x switched at k with Ξ_{k+1}(x) ≠ Ξ_k(x)».
- FIXD-N2 (missing standing premise). Every N5 line since R88 carries «under the standing SPEC premise of RESULTS R57» (R92, R93 verbatim).
  MON, and hence FIXD-MON, uses R15 (a) for Ωσ together with Ξ_σ = Ωσ, i.e. S1's counterstrategy realises the pointwise optimum. Without the
  premise the line is formally wider than its proof. Fix: add «under the standing SPEC premise of RESULTS R57» after «(SPEC S1-S5». This is a
  disclosure, not a widening. If SW-KEEP is used later, it rests on the same premise.
- FIXD-N3 (DATA label, §5, not to sign): «Flat transitions 6568 of 16183 Ξ-changing». Box 79's own table gives
  16183 = 9615 K-rise + 6503 FLATTR + 65 Ξ-flat, so 16183 counts all in-phase transitions, and 6568 = 6503 + 65 counts those without a K-rise.
  Read «of 16183 in-phase transitions».
- FIXD-N4 (citation). «R93 (Fact LEX)» should read «R93 (a) (Fact LEX, COMMON PREFIX)»: the proof uses COMMON PREFIX, and (a) is the RESULTS
  item label. «R38 (a)» for the phase definition follows the landed R93 line's usage ✓.
- Second pass, clause by clause, on quantifier ranges:
  - «for states t ≤ t′ of a phase P and every vertex v» = §2 ✓.
  - «every phase P» in PHASE-RED and in PHASE-RED′'s conclusion = phases of every N5 run on every game (title «N5 on EVERY game») ✓.
  - The hypothesis «(any phase P of any N5 run)» = the packet's FLAT-SW ✓.
  - FLATSW_P(x) is restricted to FLATTR_P transitions in the line exactly as in §4 ✓.
- Verdict: MATCHES once FIXD-N1 and FIXD-N2 are applied. FIXD-N3 and FIXD-N4 are wording only.

## DONE / FINDINGS / NEEDS
- DONE: this report; fixd_probe.py, fsw_strong.py, fixd_logs/ (run.sh, per-run outputs).
- FINDINGS:
  1. FIXD-MON SIGNED; PHASE-RED SIGNED; PHASE-RED′ (the implication) SIGNED. No gap, nothing FALSE.
  2. FLAT-SW is PROVED by REFEREE (Theorem SW-KEEP), so PHASE-RED′ holds unconditionally. It needs REFEREE-2's check.
  3. Line: one free symbol, k (FIXD-N1); missing R57 standing premise (FIXD-N2); DATA label (FIXD-N3); citation (FIXD-N4).
  4. Pins reproduced with my own engine: 66 / 73 / 8 on nep92_n40; 91; 14; 69.
- NEEDS: Lead: send FIXD-N1 and FIXD-N2 to L-NEW 39 for docs/new/P-N5-FIXD-fixes-box91.md; route SW-KEEP to REFEREE-2 for an independent check; decide whether the
  line states PHASE-RED′ unconditionally (citing SW-KEEP) once REFEREE-2 signs it.
