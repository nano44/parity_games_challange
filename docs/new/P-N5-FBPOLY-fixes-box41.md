# P-N5-FBPOLY fixes (box 41 packet, filed in box 42): the referees' repairs, written out
L-NEW successor 21 (Opus 5.5, D15/D18, L37/L40), session_01YJHHx1t8hvqkDnKzMU2Lfa. Written 2026-10-25 20:59Z by date -u, at the Lead's
request of 20:49Z (Lead's stamp): "GO for two fixes files ... repairs only; do not change any signed statement." Frozen once its sha1 is reported.
- Object: packet docs/new/P-N5-FBPOLY-box41.md, sha1 de244dcd3592b04eca2080a0efe10a7c0b2e5301 (pinned trunk 42d8c3a9). The packet is NOT
  edited; this file is its correction layer. Its own text is a record of the reports, not refereed text.
- Sources:
  - REFEREE: docs/referee/R-N5-FBPOLY.md (referee 3de7cab; §C d6248f7b, merged on trunk 4f94b452): every lemma SIGNED; FB-POLY (a)
    end bound SIGNED WITH GAP FBP-1, (b) SIGNED WITH GAP FBP-2; both repairs stand, unchanged, in its §C; notes FBP-N1..N4.
  - REFEREE-2: docs/referee-2/R2-N5-FBPOLY.md (referee-2 2fef7c4a): all SIGN, no gap; notes N-FBP-1..4. Its §C on FBPOLY is still to
    come (successor 12, after NEEDB). If it adds anything, it goes in a section appended below, not into the lines above it.
- Scope unchanged: lemmas about the candidate N5 on 𝒞^1O. Not a running-time bound, not a TARGET.md claim, not a step-4 pass.
  G-N5-TIME stays OPEN. FB-CAP for |U| ≥ 3 stays OPEN (packet §7).

## One line per note (source, kind, repair text)
| note | source | kind | repair text |
| --- | --- | --- | --- |
| FBP-1 = N-FBP-2 | REFEREE §6 gap (§C: = N-FBP-2); REFEREE-2 §6 note | gap in (a)'s end bound only; the bound is true | In §6 (a), replace "With deg_U(o) ≤ n − 1 and \|U\| ≤ n" by: "THETA-AFTER's V_H ranges over y ∈ succ(o) ∩ Û (κoptÛ is defined on Û only; FBP-N1), so THETA-AFTER holds with \|succ(o) ∩ Û\| in place of deg_U(o). Hence f ≤ 1 + (\|U\| − 2)(\|succ(o) ∩ Û\| + \|U\|) ≤ 1 + (n − 2)(2n − 1), since \|succ(o) ∩ Û\| ≤ \|U\| − 1 ≤ n − 1." Reason: with a self-loop at o and succ(o) ⊇ U = V, deg_U(o) = n (REFEREE-2: 84 of 492 games have a self-loop at o, 3 have succ(o) = V). Alternative accepted by REFEREE: state the end bound as 1 + 2n(n − 2). |
| FBP-N1 | REFEREE §5 | precision (feeds FBP-1) | In §5 THETA-AFTER: "\|V_H\| ≤ \|succ(o) ∩ Û\| ≤ \|U\| − 1", which can be smaller than deg_U(o) = \|succ(o) ∩ U\| when o has a self-loop. The stated bound holds either way. |
| FBP-2 = N-FBP-1 | REFEREE §6 gap (§C: = N-FBP-1); REFEREE-2 §6 note | gap in (b)'s proof only; the statement is true | Add to §6 (b)'s proof: "If o = c_θ and \|U\| = 2, then U = {o, v} and U ∖ T = {v}. At every state of the phase next(v) ∈ U (Aκ) and next(v) ≠ v (a self-loop would make v its own cycle node, while λ(v) = o), so next(v) = o. A switched v would need x*_v ∈ U ∖ {σ_k(v)} = {v}, impossible for the same reason. So S_U = ∅ at every fallback, and (d) gives f ≤ 1." The packet's "U = {o, c_θ}" covers o ≠ c_θ. Data: REFEREE 4 + 19 such phases, REFEREE-2 7,357 (max f 1). |
| FBP-N2 | REFEREE §6 | wording | §0.3 (YB): it uses (SP′) from z = o ∈ T, where "simple up to the first visit of T" is trivial. Add: "the lasso argument in (SP′)'s proof gives that o's honest path to c_θ is simple, which is what (YB) uses." REFEREE-2 reads (SP′)'s proof the same way (§C row). |
| FBP-N3 = N-FBP-3 (scope part) | REFEREE §6; REFEREE-2 §9 | scope | The Remarks' consequences (f removed from SCOPE-COUNT, EPOCH, X-SN-PHASE) are READINGS, not signed. FB-POLY bounds f per phase only. |
| FBP-N4 | REFEREE §8 | data | The per-vertex form of FREEZE-EXIT held at every switched vertex; its hypotheses never occur in the data, so it adds nothing beyond the proof. |
| N-FBP-3 (data part) | REFEREE-2 §9 | data | FREEZE-EXIT / THETA-AFTER hypotheses (fallbacks g_j with j ≥ \|U\| − 1 at \|U\| ≥ 3) are unreached in REFEREE-2's batch (1,484 logs) and climbs (1.92M runs); FX slack reached 0 for kind c_θ in climb 4101 (not saved). REFEREE: unreached in 3.82M climb candidates. Both: a target for L-RED. |
| N-FBP-4 | REFEREE-2 §9 (re-run by REFEREE, §C) | data, against the packet's §7 / §8 sentence | Replace "EXIT-SWITCH's 'loop' kind never occurs in data (0 of 1,544 switched vertices of U ∖ T)" by: "The loop kind occurs for SOME switched vertices: REFEREE-2's climbs found 31, each at a fallback where another switched vertex was of kind c_θ or o, as EXIT-SWITCH proves. Witness docs/referee-2/R2-N5-FBPOLY/climb/loop_4102.pg (sha1 016473b411a63c62260845015025876eba9816af, n 8, o = 2), start σ0 = [3, 1, 1, 2, 5, 1, 2, 1], τ0 = [3, 1, 0, 5, 5, 1, 2, 0], fallback k = 1. REFEREE re-ran it on its own engine: 1 fallback, kinds c_θ 1 and loop 1; with 300 random starts 35 fallbacks, loop 24, 0 failures of EXIT-SWITCH." The packet's lemma (some switched u exits) is unaffected; only the per-vertex 'never' sentence was wrong. |

## Labels after this layer
- With FBP-1 and FBP-2 filed here, REFEREE signs FB-POLY (a) and (b) without a gap (its §C, "Label reconciliation"). REFEREE-2 signed
  everything. So every statement of P-N5-FBPOLY is PROVED (L-NEW succ. 20; REFEREE 10, REFEREE-2 11), with the two repairs above.
- L-NEW (box 42): the loop witness touches nothing in docs/new/N5-KW-box42.md or docs/new/P-N5-NH-box42.md. Neither uses EXIT-SWITCH
  or the per-vertex kinds of P-N5-FBPOLY; they use FB-POLY's bound on f only.
