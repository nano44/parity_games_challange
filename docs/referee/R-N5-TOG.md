# R-N5-TOG: REFEREE report on packet P-N5-TOG (box 35: L-MONO, Z-COUNT, TOGGLE, TOGGLE-COUNT, X-SN-PHASE, RESTARTS)
Referee: REFEREE (successor 7, session_01TWT1diK1Z9x2eK56iBVbZu), Opus 5.5 (owner ruling D15, Lead reading L37). Packet P-N5-TOG: the Lead's
message of 2026-10-25 09:47Z (Lead's stamp). Object docs/new/P-N5-TOG-box35.md at pinned trunk d3daae1, sha1
7dfda8c88a0e9b752156f4faec726d8dccc20ccb (checked: `git show d3daae1:docs/new/P-N5-TOG-box35.md | sha1sum`, 139 lines). Author L-NEW
successor 15. Written 2026-10-25 10:19Z onward by date -u.
Every verdict is labelled (Opus 5.5, D15). Labels (D18/L40): PROVED (by whom) / CONJECTURE / OPEN. Independent of REFEREE-2:
docs/referee-2/R2-N5-TOG.md not read.
Premises from my own lane:
- R-N5-L2 (X-RUN′, H2-STICK with L2-1, H3-CONST), signed by both referees, §C at ce241061 (corrected from 5e85c706, which is the NJB §C; CHECKER N-2).
- R-N5-FRZ (X-RUN, X-RUN°'s source), signed by both, at CHECKER as R32.

## Verdicts
| statement | lane label | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 Lemma L-MONO | PROVED (L-NEW succ. 15) | SIGNED |
| §2 Lemma Z-COUNT | PROVED | SIGNED |
| §3 Theorem TOGGLE | PROVED | SIGNED |
| §4 Corollary TOGGLE-COUNT | PROVED | SIGNED |
| §5 Corollary X-SN-PHASE | PROVED given X-RUN′ | SIGNED WITH GAPS TOG-1 and TOG-2. Premise X-RUN′ (P-N5-L2, both referees) and through it R32 |
| §6 Corollary RESTARTS | PROVED given H2-STICK, H3-CONST, H3H2 | SIGNED (premises signed by both referees; H2-STICK with L2-1) |
| §7 DROP-LEN, dead ends, OPEN | not to sign | not signed. onerun_cex_n32, fbrestart_cex_n12, fbrestart_cex_n24 re-run (§7) |

The two gaps:
- TOG-1 (accounting). X_SN counts S4a crossings at states with c_w = c_θ, which includes the crossing from each run's last SN state
  out of its prefix. X-RUN′ (a) counts only crossings with both ends in the prefix. The stated bound survives by the slack inside
  X-RUN°'s count, but the proof must say so. Data: 26 library and 88 random such crossings.
- TOG-2 (citation): "P-N5-L2 §11" should read "P-N5-L2 §7" (X-RUN′, with X-RUN° from fixes2 e343d74e).

Fixes-file lines (one per gap):
- TOG-1 (§5): after "Summing:", insert "X_SN also counts the crossing from P(Q)'s last state, if any (≤ 1 per run). Each H1 run of P(Q)
  has ≤ (n − 1) + 6(d_o + 1)n² + 6(d_o + 1)n³ ≤ 13(d_o + 1)n³ − 1 crossings (Lemma X-RUN°'s count, P-N5-L2-fixes2 §2, P-N5-FRZ §6). So
  run Q contributes ≤ (t_Q + 1)(13(d_o + 1)n³ − 1) + t_Q + 1 ≤ 13(d_o + 1)n³(t_Q + 1) crossings at SN states, and the stated bound
  holds."
- TOG-2 (§0 table and §5): "P-N5-L2 §11" → "P-N5-L2 §7 (X-RUN′; Lemma X-RUN° in P-N5-L2-fixes2 §2)".

## 0. Setting and citations
- Phase = (λ_Ξ, τ) constant, c := λ(o), U := λ^{-1}(c).
- (M) = R15 (a): Ξ_k ⊴ Ξ_{k+1} at every transition, fallbacks included.
- "σ_{k+1}(v) ∈ {σ_k(v)} ∪ Iσ_k(v)" = R15 (d), at every transition (the S4a arena; the S4c fallback switches along Iσ; an Odd fallback
  leaves σ unchanged).
- §1-§4 use only these, the phase key and 𝒞^1O. Nothing from FRZ or L2.
- The order convention matches si.py (key (rew(c), weight(P), ±length), shorter better under an even cycle node). (F) is VJ00 (V1) plus
  "c is the top of its own cycle".
- Tools (docs/referee/scratch/, own code, `python3 -I`; own trace = n5.run; 𝒞^1O asserted on every game):
  - tog_probe.py: every check named below, per phase.
  - tog_climb.py: fitness = max H1-toggles in one phase; every improvement is re-run through tog_probe.
  - l2_oink.py.
  - No lane script is imported (togz.py, fbtau.py, fbtclimb.py, dlclimb.py not run); lane instances are inputs only.
- Library = every experiments/**/*.pg in 𝒞^1O with n ≤ 64 at referee head (272 files).

## 1. L-MONO (SIGNED)
- λ_k(c) = c (phase), so c's H_k-play is a cycle through c, of length L_k. By (F), Ξ_k(next_k c) = (c, ∅, L_k − 1); for L_k = 1 this is
  Ξ(c).
- next(c) unchanged (every Odd c ≠ o; c ≠ o by hypothesis): x lies on c's cycle at k+1, so Ξ_{k+1}(x) = (c, ∅, L_{k+1} − 1) ⊵
  Ξ_k(x) = (c, ∅, L_k − 1). Equal cycle node and P, so the length order applies.
- σ(c) switches to z: (c, z) ∈ Iσ_k (R15 (d)), so Ξ_k(z) ▷ (c, ∅, L_k − 1). z lies on c's new cycle, and (M) gives Ξ_{k+1}(z) ⊵ Ξ_k(z),
  so the inequality is strict.
- L ∈ [1, n] and it is strictly monotone at every change, so there are ≤ n − 1 changes. Correct.
- The Remark (a switch at c changes no Ξ value) is correct: plays are evaluated up to their first visit of the cycle node c.
- DATA (LMONO): 0 failures; at most 3 σ(c)-changes per phase (library), 4 on the packet instances, 2 random.

## 2. Z-COUNT (SIGNED)
- For v ∈ U the cycle node is c throughout. (M) makes weight(P(Ξ v)) non-decreasing, and weight is injective with weight(∅) = 0, so
  the P = ∅ states form an interval.
- On that interval the length is monotone in [0, n − 1].
- ≤ 2 membership changes plus ≤ n − 1 length changes per v, and every Z-change changes some v. Correct.
- DATA (ZC): per-v interval and monotone length, 0 failures; at most 44 Z-changes per phase (library, x32_rand48-type phases), against the
  bound |U|(n + 1).

## 3. TOGGLE (SIGNED)
- a = the ¬H1 end, b = the H1 end. At a, o lies on its own honest cycle, whose node is λ(o) = c, so that cycle is c's cycle C, and
  o ∈ C, o ≠ c.
- (F) gives Ξ_a(x) = (c, ∅, d(x)) on C. Z_a = Z_b then forces Ξ_b(x) = Ξ_a(x) on C: the pair (x, d(x)) ∈ Z_b, and the cycle node is c
  by the phase.
- Step 1, x ∈ C ∖ {c, o}:
  - (F) at b, which needs λ_b(x) = c ≠ x, gives Ξ_b(next_b x) = (c, ∅, d(x) − 1).
  - Drop case (a = k+1): a switch σ_{k+1}(x) = x′ would need Ξ_k(x′) ▷ Ξ_k(σ_k x). Both equal (c, ∅, d(x) − 1); x′ ∈ C, so Ξ_b(x′) is
    pinned. Contradiction.
  - Regain case (a = k): a switch to y needs Ξ_k(y) ▷ Ξ_k(x′) = (c, ∅, d(x) − 1), but (M) gives Ξ_k(y) ⊴ Ξ_{k+1}(y) =
    Ξ_b(next_b x) = (c, ∅, d(x) − 1). Contradiction.
  - Odd x ≠ o is forced.
  - Both directions correct.
- Step 2: with next_b(c) = next_a(c), c's H_b-play follows C until o (which precedes the return to c on C). λ_b(c) = c makes that play
  a cycle through c, so o is on an honest cycle at b: ¬H1 at b, a contradiction.
  - C has ≥ 2 vertices (o ≠ c ∈ C), so the self-loop corner cannot occur.
  - Odd c ≠ o is forced, so c ∈ V_E.
  - Correct.
- DATA (TOG): every in-phase toggle with Z unchanged switches next(c), with c Even.
  - Library: 29 toggles (Z same with c switched 14; Z changed 15, of which c switched 8). Random: 329 + 132. Climbs: §8.
  - 0 failures. 11 + 115 + 54 of the toggles are at fallbacks.
  - c = o phases (119 library, 19,364 + 14,134 random) have no toggle.

## 4. TOGGLE-COUNT (SIGNED)
- §3: every toggle changes Z (≤ |U|(n + 1) transitions) or σ(c) (≤ n − 1).
- Drops and regains alternate along the phase, so drops ≤ ⌈T/2⌉.
- c = o: ¬H1 throughout.
- T ≤ n² + 2n − 1 since |U| ≤ n. Correct.
- DATA (TC): max toggles per phase 6 (library), 2 (random), 5 (climbs), 4 on droplen_cex_n12. Max drops 3 / 1 / 2. All far below T.
  0 failures.

## 5. X-SN-PHASE (SIGNED WITH GAPS TOG-1, TOG-2)
- The sum over ≤ f + 1 fallback-free runs with Σ_Q t_Q ≤ T (§4; the t_Q count toggles inside disjoint prefixes) is correct for the
  quantity X-RUN′ bounds: crossings with both ends in P(Q).
- TOG-1:
  - X_SN (R30 (c): S4a crossings at states with c_w = c_θ) also counts the transition from P(Q)'s last state when it is a crossing.
    That is FRZ-3's transition again.
  - It occurs: XSN_cross_out_of_P = 26 (library), 62 + 26 (random).
  - With only X-RUN′'s stated bound, the sum would gain + (f + 1). The stated bound is still true, because each H1 run's count in
    X-RUN°'s proof is ≤ (n − 1) + 6(d_o + 1)n² + 6(d_o + 1)n³ ≤ 13(d_o + 1)n³ − 1. The slack is 7(d_o + 1)n³ − 6(d_o + 1)n² − n + 1 ≥ 1
    for n ≥ 1.
  - That slack absorbs the extra transition (fixes line above).
- TOG-2: the packet cites "P-N5-L2 §11" twice. P-N5-L2 has §0-§9, and X-RUN′ is §7.
- DATA (XSN): max X_SN per phase 91 (library), 3 (random); the bound is never approached. 0 failures.

## 6. RESTARTS (SIGNED)
- The phase has an (h) state (otherwise there are no runs to count), so H3-CONST gives H3 at every H2 state.
- So a non-(h) state k before an (h) state k+1 has ¬H1, or H1 ∧ ¬H2.
- ¬H1 at k with (h) at k+1 is a toggle.
- H1 ∧ ¬H2 at k: H2-STICK (with L2-1) excludes an S4a step. An Odd fallback changes τ and leaves the phase. So it is an Even S4c fallback.
- The first run may start at the phase's first state: + 1. Correct.
- DATA (RS):
  - library: 16 restarts, 14 by toggle and 2 by an Even fallback from H1 ∧ ¬H2 (the fbrestart instances);
  - random: 281 + 118, all by toggle;
  - every restart classified; at most 4 (h)-runs per phase; 0 failures.

## 7. Not to sign: re-runs
- l2_oink.py (Oink `--zlk -v` exit 0, verified, regions agree; own trace = n5.run; one Odd choice vertex asserted):
  - onerun_cex_n32.pg (sha1 70832fcb…): 8 iterations, 0 fallbacks, two drops in one phase (tog_probe: max 2 drops);
  - fbrestart_cex_n12.pg (35223b6c…): 5 / 2;
  - fbrestart_cex_n24.pg (a0aacfba…): 23 / 3.
  - On the three files and pf_best_3621-3623: 2 restarts by an Even fallback from H1 ∧ ¬H2, as the packet says.
  - The "≤ 1 drop per fallback-free run" dead end is also refuted by my droplen_cex_n12 (R-N5-L2 §8), which the packet does not cite.
    Not a gap, since §7 is not signed.
- DROP-LEN: FALSE (R-N5-L2 §8, droplen_cex_n12; fixes 7a110bca §2). The packet's §7 still lists it as a CONJECTURE that "holds in every
  instance seen". That line is out of date, not a gap in a signed statement.

## 8. DATA summary (DATA, not proof)
| run | games | phases | toggles | max toggles / drops per phase | failures |
| --- | --- | --- | --- | --- | --- |
| packet instances + droplen_cex_n12 | 7 | 29 | 8 | 4 / 2 | 0 |
| library (272 files) | 272 | 1,107 | 29 | 6 / 3 | 0 |
| rand 𝒞^1O n 4-14 seed 7701 | 30,000 | 58,127 | 329 | 2 / 1 | 0 |
| randb (back-edges into o) seed 7702 | 15,000 | 32,056 | 132 | 2 / 1 | 0 |
| climbs tog_climb.py (seed 81 random n 5-12, 1,766,277 steps; seed 82 from droplen_cex_n12, 917,912 steps; 20 min each) | 714 improvements re-checked | — | — | 5 / — | 0 |

- Thin spots:
  - Toggle counts are tiny (≤ 6 per phase) against T ≈ n², so the bounds are not approached.
  - RESTARTS' fallback branch has only the lane's instances (2 restarts).
  - X-SN-PHASE inherits X-RUN′'s unexercised parts (R-N5-L2 §4.2, R-N5-FRZ §C).

## 9. Labels after this report (D18/L40)
- PROVED (L-NEW successor 15; signed by REFEREE (Opus 5.5, D15), second referee pending), on 𝒞^1O inside a (λ_Ξ, τ) phase:
  - L-MONO, Z-COUNT, TOGGLE, TOGGLE-COUNT, RESTARTS;
  - X-SN-PHASE (TOG-1, TOG-2; premise X-RUN′ / R32).
- FALSE (DATA): DROP-LEN, "≤ 1 drop per fallback-free run", "a fallback at H1 ∧ ¬H2 never takes τ(o) out of R".
- OPEN: (L1), f ↔ X, K, G-N5-TIME.
- Not a TARGET.md claim; the TARGET.md diff is empty.

Signed: REFEREE successor 7 (Opus 5.5, D15).

## §C. Comparison with REFEREE-2 (docs/referee-2/R2-N5-TOG.md, referee-2 faabe71 + Addendum A 16d27d1, on trunk). REFEREE successor 7, written 2026-10-25 10:33Z by date -u
Signature (Opus 5.5, D15). I opened R2-N5-TOG only after my report (fff6e624) was pushed. Also read: L-NEW's fixes file
docs/new/P-N5-TOG-fixes-box35.md (l-new b5b8e66, on trunk), sha1 f15b58dddf232d810fab277010e29ae5187d382d (checked with sha1sum).

### C.1 Verdicts
| statement | REFEREE | REFEREE-2 | joint |
| --- | --- | --- | --- |
| (F) | checked inside §1-§3 (no separate row) | SIGN | signed by both |
| L-MONO, Z-COUNT, TOGGLE, TOGGLE-COUNT, RESTARTS | SIGNED | SIGN | signed by both |
| X-SN-PHASE | SIGNED WITH GAPS TOG-1, TOG-2 | SIGN WITH GAPS G-TOG-1, N-TOG-1 | signed by both; TOG-1 = G-TOG-1, TOG-2 = N-TOG-1 |
| §7 | not signed | not signed | — |
- No verdict differs. Both gaps were found independently, with the same repair.

### C.2 Item by item
- TOG-1 = G-TOG-1 (X_SN also counts the S4a crossing from each SN prefix's last state; the bound survives by the slack inside X-RUN°'s
  count).
  - My fixes line gives per run ≤ (t_Q + 1)(13(d_o + 1)n³ − 1) + t_Q + 1 = 13(d_o + 1)n³(t_Q + 1). REFEREE-2's line and the fixes file
    give ≤ 13(d_o + 1)n³(t_Q + 1) + t_Q.
  - Both are valid and both sum to the stated bound. The fixes file's §1 carries the full arithmetic, which I re-checked:
    7(d_o + 1)n³ − 6(d_o + 1)n² − n + 1 ≥ d_o + 1 for n ≥ 1. CLOSED.
- TOG-2 = N-TOG-1 ("§11" → "§7"; §11 was N5-REL-box34's numbering). The fixes file carries it. CLOSED.
- DATA attribution, as the Lead asked:
  - My counts come from MY OWN TRACE: u1_probe.trace, the n5.py loop recorded, asserted equal to n5.run's iteration and fallback
    counts on every game. That is the SPEC trace.
  - My "26 library" is 26 S4a crossings out of an SN prefix in 26 library files, one per file. The files include b4_cyc6_0, b4_n4all_cyc3_0,
    b5_n5_cyc4_0, n4_thch_0, epsseg_cex_n16/n48, exitr_cex_n16/n48, so_th_n32 and zcl_rx_n32. This equals L-RED 16's 26 files.
  - REFEREE-2's SPEC count of 19 is over its 238-file TOG batch set; my library is 272 files.
  - My "88 random" (62 + 26) is likewise from my SPEC trace on rand / randb.
  - REFEREE-2's 310 / 246,038 come from its own N5 with other S4a optima (Addendum A). That is a different trace, and the statements
    agree.
- (F) as its own row (REFEREE-2 only): I checked (F) at each use (L-MONO, TOGGLE Step 1). No difference.
- Data agree. In all data of both referees: TOGGLE's "Z unchanged ⇒ next(c) changes at an Even c" holds every time, and the counts are far
  below T. REFEREE-2's climbs reached at most 3 toggles per phase in its variant, mine 5 (SPEC), and the library 6.
- My §7 note (DROP-LEN listed as a CONJECTURE although FALSE): the Lead records it in the R-entry. No row needed.

### C.3 Joint gap map (one fixes-file line per row)
| row | REFEREE | REFEREE-2 | kind / status | fixes-file line |
| --- | --- | --- | --- | --- |
| 1 | TOG-1 | G-TOG-1 | accounting, closed (occurs on the SPEC trace: 26 library files) | §5: fixes f15b58dd §1 (C_P + 1 ≤ 13(d_o + 1)n³(t_Q + 1) + t_Q via X-RUN°'s count ≤ 13(d_o + 1)n³ − 1 per (h)-run) |
| 2 | TOG-2 | N-TOG-1 | citation, closed | §0, §5: "P-N5-L2 §11" → "P-N5-L2 §7" (fixes f15b58dd §1) |

### C.4 Joint label (D18/L40)
- PROVED (L-NEW successor 15; REFEREE and REFEREE-2, Opus 5.5, D15), on 𝒞^1O inside a (λ_Ξ, τ) phase, pending CHECKER:
  - (F), L-MONO, Z-COUNT, TOGGLE, TOGGLE-COUNT;
  - RESTARTS (premises H2-STICK, H3-CONST: P-N5-L2, both referees);
  - X-SN-PHASE (rows 1-2; premise X-RUN′, hence R32).
- FALSE (DATA): DROP-LEN, "≤ 1 drop per fallback-free run", "a fallback at H1 ∧ ¬H2 never takes τ(o) out of R".
- OPEN: (L1), f ↔ X, K, G-N5-TIME.
- Not a TARGET.md claim; the TARGET.md diff is empty.

Signed: REFEREE successor 7 (Opus 5.5, D15).
