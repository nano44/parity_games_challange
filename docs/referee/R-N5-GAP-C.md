# R-N5-GAP-C: §C cross-map for P-N5-GAP (REFEREE 19 vs REFEREE-2 21), H1 vs G-GAP-1, H2-H8, H9 line
Referee: REFEREE (successor 19), Opus 5.5 (D15). Lead brief 2026-10-30 02:21Z; written 02:22Z-02:27Z by date -u. Every verdict "(Opus 5.5, D15)".
- My report: docs/referee/R-N5-GAP.md at claude/referee cd1c29d6, pushed BEFORE I opened any REFEREE-2 GAP file.
- REFEREE-2's report: docs/referee-2/R2-N5-GAP.md at claude/referee-2 aee8971e (sha1 84a495d7…, 163 lines), opened 02:21Z after the Lead's word.
- Fixes: docs/new/P-N5-GAP-fixes-box69.md at l-new 15044625, sha1 1e223dc2e08daf88ee40e46421f2d859889230a7; line
  docs/new/P-N5-GAP-box69-line-H9.txt at 15044625, sha1 28b7e5506a5419181c9bca8b316694c3cd21ccb3. Both equal the Lead's figures. Packet
  unchanged (d67f8e04).

## 1. Joint gap map
| item | REFEREE 19 | REFEREE-2 21 | joint |
| --- | --- | --- | --- |
| XW, W-MON, FB-W | SIGNED (premise GAP-N1) | SIGNED (premise N-GAP-1) | SIGNED by both |
| OPT-OFF | statement TRUE; proof gap G-GAP-1; signed with repair GAP-R1 | SIGNED with gap G-GAP-1; repair in its §2.4 | the SAME gap, found independently: Case 2 when v's cycle node u lies on π (v on u's cycle, c's play meets u before v); both: «|π| + 1 longer» and (ii)'s «u is odd … every vertex of Z less relevant than u» fail; both repairs: v ⊕ Ω_ρ(c) vs v ⊕ Ω_ρ(ρ v) with the same cycle node, [V2] strict, against [F1] |
| W-SUCC, LATE-W | SIGNED (given OPT-OFF repaired) | SIGNED (uses OPT-OFF's statement) | SIGNED by both |
| LATE-PIECE | SIGNED | SIGNED (CL's t′ to be fixed: N-GAP-3) | SIGNED by both |
| GAP-MON, SW-IN, Z-FLAT, REOPEN-W, REOPEN-CHARGE | SIGNED | SIGNED | SIGNED by both |
| Theorem GAP-RED | SIGNED (independent of OPT-OFF) | SIGNED | SIGNED by both |
| line f1c5c5d5 | MATCHES after GAP-L1..L3 (definitions only) | MATCHES, precision only (premise; CL window) | MATCHES, no E-item from either |
Gap map = {G-GAP-1} (one proof step, both referees, same configuration, equivalent repairs). Nothing FALSE. No disagreement on any verdict.
- Size of the configuration, two engines: mine 11,948 (v, c) pairs with u ∈ π, 11,781 of them with S = ∅ (alt_all, run states); REFEREE-2
  8,907 (one-player games) and 17,139 (sbcg run states), with S = ∅ and u even 6,957 / 15,355. REFEREE-2 also gives a 3-vertex instance
  (case2u_inst.pg), which I accept by hand: v = 0 on the cycle 0 → 1 → 0, u = 1 even, c = 2, π = (2, 1) ∋ u, Ω(c) = (1, ∅, 1), Ω(ρ v) = (1, ∅, 0).
- Notes map: GAP-N1 = N-GAP-1; GAP-N2 (SW-IN applies [V2] across two strategy pairs) ≈ N-GAP-2 (Case 1 "plays" → "paths"; both are [V2]
  wording); GAP-N3 = N-GAP-5; my GAP-R1 = R2's repair (= N-GAP-6's relation to CUT). REFEREE-2 only: N-GAP-3 (CL depends on the choice of t′; I
  MISSED it, I only flagged "other than the first"), N-GAP-4 (§5's bullet: FB-LIN itself does not follow, only a polynomial form; I MISSED it),
  N-GAP-7 (comp54_n80's start file has a non-edge). On N-GAP-7: my parser repaired that start (a NOTE: «forced vertex 11 → 51; using 11») and ran
  a valid N5 run from the repaired start; so my alt_all counts include comp54 from a DIFFERENT, valid start, not the lane's. No verdict rests on it.
- Data agreement: both find 0 violations of every item; both reproduce nep22f_n64's 10 Z-flat fallbacks and lend9_n8's 3 in-phase fallbacks;
  REFEREE-2's corrected corpus counts (782 in-phase fallbacks, 8,442 re-openings) are the ones H8 adopts. Both controls on the own-cycle
  premise of SW-IN bite (mine 36, REFEREE-2 31 on sbcg).

## 2. H1: does it close G-GAP-1?
YES (Opus 5.5, D15). H1 splits by the ρ-PATH from c to u_c := λ_ρ(c) (not the play). I checked each case.
- (1a) path avoids v, v not on u_c's cycle: the whole play from c avoids v; Ω_ρ′(v) = v ⊕ Ω_ρ(c), Ω_ρ(v) = v ⊕ Ω_ρ(ρ v) [V1]; [V2] strict
  (different cycle nodes allowed) against [F1] ✓.
- (1b) path avoids v, v on u_c's cycle: u = u_c, v below u; ρv runs along the arc to u (P = ∅, and that path avoids v); P(Ω_ρ(c)) = S (the
  cycle vertices are below u); Z = v, c's path, the arc u → v; its vertices above u are exactly S. S ≠ ∅: Ω_ρ(c) ▷ Ω_ρ(ρ v) with equal
  cycle nodes forces weight(S) > 0, i.e. max S even (Fact DELTA), and max S is Z's top: better reward, against [F1] ✓. S = ∅: Z's top is u,
  Ω_ρ′(v) = (u, ∅, 1 + |c's path to u|) = v ⊕ Ω_ρ(c); [V2] strict on two triples with cycle node u and v ∉ P ✓. This sub-case is exactly
  the configuration of G-GAP-1 (my (2b)) and its S = ∅ half is my GAP-R1 verbatim in content.
- Case 2 (path visits v): u_c = u; π (before the first v) excludes u; H1's disjointness argument ✓ (v off u's cycle: a common vertex would
  make c's play follow a play that never visits v; v on u's cycle: π meets the cycle only on the arc (u, v), ρ v's path is the other arc).
  Hence P(Ω_ρ(c)) = S ⊔ P(Ω_ρ(ρ v)), the |π| + 1 length difference, Z = v, π ∌ u: the packet's (i), (ii) are now correct ✓.
- Exhaustive: the path to u_c either avoids v (1a / 1b by v's position) or visits v (2) ✓. G-GAP-1 is CLOSED. With H1, OPT-OFF is SIGNED
  (no longer conditional on my GAP-R1, which H1 contains).

## 3. H2-H8: clarifications only?
| item | content | verdict |
| --- | --- | --- |
| H2 | names R57 (a) (VJ) for XW and R57's standing SPEC premise (1E-N3) for W-MON, FB-W, OPT-OFF's uses; G-N5T-1 for DATA only | clarification (answers GAP-N1 / N-GAP-1). R17 (a) (F1) is already in the packet's [F1] |
| H3 | Case 1 "plays" → "paths to the cycle node" | clarification (folded into H1 (1a)) |
| H4 | CL with t′ := the EARLIEST blocked state of [s + 1, u] | precision: fixes a choice the proof leaves free; any fixed t′ works (LATE-W needs only blocked at t′ and off-cycle on [s + 1, t′]); the bound with this CL is a signed instance. Not a widening |
| H5 | §5's bullet: polynomial bounds give a POLYNOMIAL form of FB-LIN, not FB-LIN (≤ n) | a NARROWING of an unsigned READING bullet; correct (f_P ≤ n would need RO_P + ZF_P ≤ n − |Z_a|) |
| H6 | Z-FLAT = consequences | clarification (GAP-N3 / N-GAP-5) |
| H7 | relation to P-N5-CUT's OPT-OFF (ii) | READING; correct (CUT's Case 3 = H1's (1b)) |
| H8 | DATA correction: comp54_n80's start has a non-edge; counts without it (782, 8,442, 725, …); start validation added | DATA only; the corrected figures equal REFEREE-2's. No signed item uses DATA |
Verdict: H2-H8 are clarifications, a narrowing (H5), a precision (H4) and a DATA correction (H8). None widens a signed statement.

## 4. H9 (line 28b7e550), word by word against f1c5c5d5 and my §8 table
- `git diff --no-index --word-diff` of f1c5c5d5 vs H9: exactly the two changes H9 lists, nothing else (checked).
  - (i) «(SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure realises the pointwise optimum; for S4a, σ_new
    is the pointwise optimum of the one-player arena H_t); » ✓ = H2. It introduces the symbol H_t, which the line does NOT define (GAP-L4,
    new: "H_t := σ_t ∪ Iσ_t, S4a's arena (Odd fixed to τ_t)").
  - (ii) CL: «those, other than the first, whose window [s + 1, t′] — u → u + 1 the adoption, s → s + 1 the latest leave of c by v with
    s + 1 ≤ u, t′ the earliest state of [s + 1, u] at which (v, c) is blocked — contains some state at which v is its own W-cycle node» ✓ =
    §3.2 with H4. This also carries my CL note ("other than the first"), which the Lead's brief listed as missing: it is IN H9.
- Still missing (for H10+):
  - GAP-L1: «Ξ_t := Ξ_{σ_t} (SPEC S1)» (Ξ_t is used in Z_t, XW, GAP-MON, SW-IN, Z-FLAT).
  - GAP-L2: OPT-OFF's clause «an optimal strategy ρ of a one-player game» → «a pointwise-optimal Even strategy ρ (RESULTS R17 (a) (F1)) of a
    one-player game of Even (Odd fixed), Ω_ρ its [S1-val] valuation».
  - GAP-L3: premises not yet named: R15 (a), (d) (Ξ only rises: GAP-MON, SW-IN, REOPEN-W), R17 (a) (F1), R21 (a) (XW). (R38 (a), R57, R88 are
    named.)
  - GAP-L4 (new, from H9 (i)): define H_t.
- Every other symbol of H9 is defined in the line or cited (W_t, Z_t, phase, in-phase, τ-fixed Even fallback, piece, blocked, S4a step,
  WCH_Q, CL_Q, f_P, RO_P, WCH^S4a_P, ZF_P, |Z_a|, n), and every displayed inequality equals the packet's.
- Verdict on H9 (Opus 5.5, D15): MATCHES §2-§5 with H1-H4 and claims nothing more; NOT YET complete by the every-symbol rule: H10+ must add
  GAP-L1, GAP-L2, GAP-L3 and GAP-L4. None is an E-item (no symbol's absence makes a clause false under its natural reading); all are
  definitions or citations.

## 5. Addendum (Lead 02:32Z): fixes H1-H15 (l-new c1aa183d, sha1 955bcea2c5dae4c6016d5f9cfeaa8bae004587e0) and line H14 (sha1 a9e8bcae1d6caec7cded179ead78f1cfedf756f9); written 02:32Z by date -u
- Hashes re-measured: both match. The fixes file is append-only: `git diff 15044625 c1aa183d` adds H10-H15 and changes nothing in H1-H9.
- G-GAP-1: CLOSED via H1, and H10 correctly maps my GAP-R1 onto it. (2b) u ∈ π = H1 (1b), (2a) = H1 Case 2, (2b)(i)/(ii) = (1b) with S ≠ ∅ / S = ∅.
  "|π| + 1 longer" survives only in Case 2 = (2a), where it is true. ✓
- H10-H15 widen nothing. H10 is a mapping. H11 = H2 plus R57 (a). H12 is the triple statement of [V2], which is exactly my GAP-N2: correct, and
  "which plays produced a and b does not matter" is right for the formal ⊕. H13 = H6. H14 is the line. H15 = H8 (DATA).
  With §3: H2-H15 are clarifications, one narrowing (H5), one precision (H4) and DATA (H8 / H15). No signed statement widens.
- H14 against H9, `git diff --no-index --word-diff=porcelain` (mine): exactly two insertions and one replacement.
  - «premises RESULTS R15 (a), (d), R17 (a) (F1) with R57 (a) (VJ), R21 (a), R38 (a), R88; Ξ_t := Ξ_{σ_t} (SPEC S1); »: GAP-L3 ✓ and GAP-L1 ✓.
  - «an optimal strategy ρ of a one-player game has» → «for a one-player game of Even (Odd fixed), a pointwise-optimal Even strategy ρ (R17 (a)
    (F1)) with Ω_ρ its [S1-val] valuation has»: GAP-L2 ✓. The clause reads grammatically in context, which I checked by printing it.
  - CL keeps «other than the first» (the packet's own wording, the one I signed). The Lead's decision is fine; my note was only that the
    00:56Z proposal's omission gave a superset.
- STILL OPEN, one symbol: GAP-L4. H9's standing-premise clause «σ_new is the pointwise optimum of the one-player arena H_t» uses H_t, and no
  clause of H14 defines it. Precision, not an E-item: "for S4a" makes the reading natural. Under the every-symbol rule, add «H_t := S4a's
  arena at t (Even keeps σ_t ∪ Iσ_t, Odd follows τ_t)», or replace «the one-player arena H_t» by «S4a's one-player arena».
- Verdict on H14 (Opus 5.5, D15): it MATCHES §1-§5 with H1-H15 and claims nothing more. GAP-L1, L2 and L3 are present. It is complete once
  GAP-L4 is added: a five-word edit, which I will word-diff check.

## DONE / FINDINGS / NEEDS
- DONE: this §C (R-N5-GAP-C.md).
- FINDINGS: verdicts identical; gap map {G-GAP-1}, found by both with the same configuration; H1 CLOSES it (OPT-OFF now SIGNED outright);
  H2-H8 clarifications / narrowing / precision / DATA only; H9 = f1c5c5d5 + exactly two changes, both correct; H10+ must add GAP-L1..L3 and
  the new GAP-L4 (H_t, introduced by H9 itself). I missed N-GAP-3 and N-GAP-4; recorded.
- NEEDS: Lead: route GAP-L4 (define H_t) to L-NEW; the corrected line SHA for a word-diff check. (§5: H14 carries GAP-L1..L3; G-GAP-1 closed; H2-H15 clean.)

- H16 check (Lead 02:52Z; l-new 996d9a57 docs/new/P-N5-GAP-box69-line-H16.txt sha1 e3a23a9ae8091817576a88ade9d85ea07543719a, fixes sha1 3de5bc3e5b4284c17a87c754fb78d93a214beef8 (append-only: +7 lines vs c1aa183d) re-measured; my own word diff vs H14, written 02:52Z by date -u): H16 = H14 + GAP-L4 exactly («H_t);» → «H_t, H_t := S4a's arena at t (Even keeps σ_t ∪ Iσ_t, Odd follows τ_t));»); every symbol now defined or cited; MATCHES (Opus 5.5, D15).
- H17 check (Lead 04:06Z; l-new f997177d docs/new/P-N5-GAP-box69-line-H17.txt sha1 fa5653705e3f9938fb6732369a7c917e8f1456d8 re-measured; my own word diff H16 → H17, written 04:06Z by date -u): exactly one insertion, «a transition is written k → k + 1 (states k, k + 1); n = |V|; ». Strict symbol test over the whole H17 line: k is now bound. Every other symbol is bound in the line (t, H_t, Ξ_t, W_t, Z_t, ρ, Ω_ρ, v, c, p, q, s, t′, u, Q, WCH_Q, CL_Q, P, a, f_P, RO_P, WCH^S4a_P, ZF_P) or by SPEC S1-S5 / R38 (a) / R88 / R17 (a), with ONE exception: «V» in the new «n = |V|» is not bound. SPEC's input line defines V = {0..n−1}, but that is not S1-S5; L-SI's K15 replaced the same «n = |V|» for this reason. For consistency, write «n the number of vertices of the game». This is a precision, not an E-item. MATCHES otherwise (Opus 5.5, D15).
- H18 check (Lead 04:26Z; l-new 248d9360 docs/new/P-N5-GAP-box69-line-H18.txt sha1 d86446daf3df3d78a364837734a6da56db14a4d6, fixes sha1 6b5f793b8c18efe88a94a0df6991bcbcfc706c62, re-measured; fixes append-only vs f997177d; my own word diff H17 → H18, written 04:27Z by date -u): exactly «n = |V|;» → «n the number of vertices of the game;». With my H17 strict test, every symbol of H18 is now bound. MATCHES (Opus 5.5, D15).
