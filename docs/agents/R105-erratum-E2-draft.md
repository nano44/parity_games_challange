# Draft RESULTS Erratum E-2 (Lead; first fill 2026-11-04T10:15:43Z by date -u; to CHECKER) — three definition binders (rev. 1 for C119 Add. 1) in RESULTS R105's title line

Placement: directly after «**Erratum E-1**»'s block and before «## Dead ends» in docs/RESULTS.md. Erratum block = the lines between the
two markers below (not landed: this header and the markers).
Sources:
- RESULTS R105 title line, docs/RESULTS.md l. 10155 (landed 2026-11-04 02:59Z, 91c1464f; CHECKER C116 e85c3bb2, Add. 1 49f85ffc).
- Packet P-IDEAL-RED, claude/l-new 0ebddcf5 docs/new/P-IDEAL-RED.md (sha1 06f2c18609e355a1e62c138c420bd49dc401cae4): §4 l. 118-119
  («For 2 ≤ t ≤ T, step t is CHAINED iff h_(t−1) lies on the chain of (h_t, s_t(h_t)) under s_(t−2) (as a mover other» «than h_t),
  and UNCHAINED otherwise.»); §7 l. 161 («RANK_t := 1 + |{x ∈ S(s_(t−1)) : π(x) > π(y_t)}|.»).
- REFEREE successor 23, claude/referee 685a47de docs/referee/R-P-IDEAL-M2.md l. 172-181 (R105-E1, R105-E2).
- REFEREE-2 successor 27, claude/referee-2 0254976d docs/referee-2/R2-R105-chained.md (71 lines) with R2-R105-chained/chained_check.py
  and diff_n2.json (sha1 0c2cdc9fe30721f2fdb06527649b0733928d714f): instance, Q1-Q3 data.
---BEGIN ERRATUM BLOCK---
**Erratum E-2** (not a result; <DATE> <HH:MM>Z by date -u; Lead; three definitions in RESULTS R105's title line):
- What is wrong: RESULTS R105's title line (l. 10155) states three definitions more loosely than the signed packet P-IDEAL-RED
  (claude/l-new 0ebddcf5, sha1 06f2c186…), whose statements both referees signed. (E2a) CHAIN-BACK's parenthesis «(h_(t−1) lies on
  the chain under s_(t−2) of the option h_t takes)» omits the packet's «(as a mover other than h_t)» (§4 l. 118-119); R105's body item (f) (l. 10229-10230: «a step t ∈ [2, T] is
  CHAINED iff h_(t−1) lies on the chain of (h_t, s_t(h_t)) under» «s_(t−2)») omits it too. (E2b) TOP-MONO's
  «RANK_t := 1 + #(unstable movers above y_t before the step)» leaves «above» unanchored; the packet counts unstable x with
  π(x) > π(y_t) (§7 l. 161). (E2c) KEYFLIP's «moves(x)» is used without its binder; the packet defines moves(x) as the number of steps t
  with x ∈ Mv_t (§0 l. 59).
- Found by: REFEREE-2 successor 27 (claude/referee-2 e01175f6, R2-P-IDEAL-M2.md findings) and confirmed by REFEREE successor 23
  (claude/referee 685a47de, R-P-IDEAL-M2.md l. 172-181, R105-E1 and R105-E2), who had MATCHED the line; CHECKER C116 did not catch it.
- Effect of (E2a), measured (REFEREE-2 27, claude/referee-2 0254976d, R2-R105-chained.md; DATA, not a signature): under the line's
  reading a step with h_(t−1) = h_t counts as chained, and CHAIN-BACK (i) «π(h_t) < π(h_(t−1))» is false at every such step (35,116
  steps; first instance diff_n2: degree 3, N 2, T 2, step t = 2). No such step exists at degree ≤ 2 (REFEREE-2's argument by XI-NEW, checked by CHECKER C119; 0 in the data). The
  bound T ≤ N (1 + U′) with U′ counted under the line's reading had 0 failures on 926,555 runs (equality reached, never exceeded), but
  it is NOT PROVED under that reading, and neither are U-EQ's (⇐) direction, RANK-BOUND, INTERVAL-RESTRICT and RECURSION as functions
  of U′: their signed proofs use the packet's U.
- Correction: read R105's CHAIN-BACK parenthesis (title line) and body item (f) with the packet's binder: the parenthesis as «(h_(t−1) lies on the chain under s_(t−2) of the option h_t takes, as a mover
  other than h_t)», and U, U-EQ, RANK-BOUND, INTERVAL-* and RECURSION with that U. Read KEYFLIP's moves(x) as the number of steps that move x. Read TOP-MONO's RANK_t in the title line as «1 + #(unstable movers
  with π above π(y_t) before the step)» (body item (l), l. 10248, already anchors it: «above π(y_t)»). These are the packet's definitions; the signatures (REFEREE 23 a71540d5 / d8f25ef2 /
  0d2fef9f; REFEREE-2 26 2f9b6f5c / ca757330 / f81c6e57) are on the packet's statements, so every signed statement of R105 stands
  as read with the correction.
- Unaffected: R105's other definitions (REFEREE re-read them: 685a47de l. 186-187; CHECKER C119 §3 diffed them against P-IDEAL-RED); RESULTS R106
  (its premises are R105's ENC and LOCAL (b) only); P-IDEAL-M2, whose line states U with the phrase. No title, GAPS line or
  Dead-ends row changes. R105's heading text and its UPDATE on GAPS l. 11 (which repeats both clauses) stay as landed (the heading equals the
  MATCHED line L-2); this erratum governs their reading.
- Lesson (Lead): a line MATCH checks every definition in the line against the packet's definitions, not only the claims; added to the
  referee and CHECKER briefs from now on.
---END ERRATUM BLOCK---
