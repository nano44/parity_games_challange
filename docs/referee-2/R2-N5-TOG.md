# R2-N5-TOG: second-referee check of packet P-N5-TOG (L-NEW box 35: L-MONO, Z-COUNT, TOGGLE, TOGGLE-COUNT, X-SN-PHASE, RESTARTS). REFEREE-2 (successor 7), 2026-10-25 09:47Z (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-TOG (Lead 08:41Z). Object docs/new/P-N5-TOG-box35.md, sha1 7dfda8c88a0e9b752156f4faec726d8dccc20ccb.
I checked it with `git show d3daae1:… | sha1sum` and on my tree. The pin is trunk d3daae1.
Background read: RESULTS R15 (a); P-N5-L2 (my R2-N5-L2: X-RUN′, H2-STICK, H3-CONST signed) and P-N5-FRZ (my R2-N5-FRZ, both referees);
R30 (c), (d); SPEC S1-S5.
Independence: no REFEREE report on this packet is on my tree, and I read none. I did not run or import togz.py, fbtau.py, fbtclimb.py,
dlclimb.py or any REFEREE probe. Lane .pg files are inputs only.
Tools: docs/referee-2/R2-N5-TOG/ (own code on my R2-N5-FRZ/frz_check.py): tog_check.py, tog_climb.py, xsn_exit_probe.py, run_all.sh,
logs/, climb/, totals_logs.txt, totals_climb.txt. Every game asserts exactly one Odd vertex with out-degree > 1. Phase key (λ_Ξ, τ).
Labels (D18 / L40): the packet's PROVED (L-NEW succ. 15) label is its own. §7 is not signed, as briefed. Nothing here is a running-time
bound, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §0 fact (F) | SIGN | — |
| §1 Lemma L-MONO | SIGN | — |
| §2 Lemma Z-COUNT | SIGN | — |
| §3 Theorem TOGGLE | SIGN | — |
| §4 Corollary TOGGLE-COUNT | SIGN | — |
| §5 Corollary X-SN-PHASE | SIGN WITH GAPS | G-TOG-1 (accounting; the FRZ-3 pattern again). X_SN (R30 (c)) counts S4a crossings starting at states with c_w = c_θ. That includes the transition from each run's SN-prefix end, which X-RUN′ (a) does not count ("both ends in P"). The proof sums X-RUN′ (a) and so omits up to f + 1 crossings per phase. The stated bound survives by X-RUN's slack (below). The case OCCURS in data: 310 batch / 246,038 climb crossings. N-TOG-1 (citation): X-RUN′ is P-N5-L2 §7, not "§11" |
| §6 Corollary RESTARTS | SIGN | — |
| §7 | not signed (as briefed) | My L2 report found the §7 fallback restart independently (j5_n16); the lane's fbrestart_cex_n12/n24 reproduce in my N5 |
No statement is NOT SIGNED. No counterexample in 31,434 batch runs and 1,753,992 climb runs (4 climbs).

## 1. (F), L-MONO, Z-COUNT: SIGN
- (F). c is the most relevant vertex of its cycle, so along the cycle P = ∅ and the length is the distance. For x ≠ c with λ(x) = c, (V1)
  holds, and x is added to P only if x beats c. ✓
- L-MONO.
  - Ξ_k(next_k c) = (c, ∅, L_k − 1).
  - Unchanged successor (this includes Odd c ≠ o): (M) at the same vertex on the same cycle gives L_{k+1} ≤ L_k for even c.
  - Changed successor (c, z) ∈ Iσ_k (§0's arena / fallback fact; R15 (d)): Ξ_{k+1}(z) ⊵ Ξ_k(z) ▷ (c, ∅, L_k − 1), so L_{k+1} < L_k.
  - Odd c reverses the order. L takes values in [1, n], hence ≤ n − 1 changes. ✓
- Z-COUNT. For v ∈ U the cycle node c is fixed. The signed weight is non-decreasing and injective, and weight(∅) = 0, so the ∅-states form
  an interval. On it the length is monotone, so each v changes ≤ n + 1 times. ✓
- DATA: every state of every phase with c ≠ o was checked against (F) on c's cycle. L-MONO: 24,039 / 2,295,437 transitions, with
  931 / 1,314,465 next(c)-changes, each strict. Z: the interval and monotone length per v; max Z-changes per phase 44 (batch).
  0 failures.

## 2. TOGGLE and TOGGLE-COUNT: SIGN
- C (c's cycle at the ¬H1 end a) contains o, because o's own honest cycle has top λ(o) = c.
- Z_a = Z_b pins Ξ_b = Ξ_a = (c, ∅, d(x)) on C: λ is a phase constant, and Z holds both the ∅ flag and the length.
- Step 1 for x ∈ C ∖ {c, o}: (F) at b gives Ξ_b(next_b x) = (c, ∅, d(x) − 1), since x is below c and so adds nothing to P.
  - Drop: a new successor x′ would need Ξ_k(x′) ▷ Ξ_k(σ_k x), and both are (c, ∅, d(x) − 1).
  - Regain: Ξ_k(y) ▷ (c, ∅, d(x) − 1) ⊵ Ξ_{k+1}(y) contradicts (M).
  - ✓
- Step 2: with next(c) unchanged, c's H_b-play runs along C and meets o before returning to c. λ_b(c) = c makes that walk a cycle, so o
  is on an honest cycle, against H1 at b. ✓
- Count: every toggle changes Z or σ(c), so toggles ≤ |U|(n + 1) + n − 1. Drops and regains alternate. If c = o, ¬H1 holds at every
  state, so there are no toggles. ✓
- DATA:
  - toggles: 507 (batch), 1,209,937 (climbs);
  - toggles with Z unchanged: 266 / 979,032, every one with next(c) changed at an Even c, and Step 1 (next unchanged on C ∖ {c, o})
    checked at each;
  - 23 / 57,040 toggles at fallbacks;
  - per phase at most 3 toggles, 2 drops, 4 σ(c)-changes (climbs);
  - 1,701 / 10,820 phases with c = o have no toggle.
  - 0 failures.

## 3. X-SN-PHASE: SIGN WITH GAPS (G-TOG-1, N-TOG-1)
- The sum: a phase has ≤ f + 1 maximal fallback-free runs Q, and Σ_Q t_Q ≤ T (§4; toggles in different runs are different transitions).
- G-TOG-1.
  - X_SN := the S4a crossings at states with c_w = c_θ (R30 (c)). In a run Q these are the crossings with both ends in its SN prefix P,
    PLUS possibly the S4a transition from P's last state, whose start has c_w = c_θ. X-RUN′ (a) bounds only the first kind. This is the
    same boundary transition as FRZ-3 / G-FRZ-1 (where it mattered for REL_Q).
  - So the proof as written gives X_SN ≤ 13(d_o + 1)n³(f + 1 + T) + T + (f + 1).
  - The stated bound still holds. X-RUN's proof (my R2-N5-FRZ §6) gives each (h)-run ≤ (n − 1) + 6(d_o + 1)n² + 6(d_o + 1)n³ ≤
    13(d_o + 1)n³ − 1. So in X-RUN′ (a), C_P + 1 ≤ 13(d_o + 1)n³(t_Q + 1) + t_Q, and summing gives the packet's bound exactly.
  - One sentence fixes it.
  - DATA (it occurs):
    - batch: 310 of 11,378 X_SN crossings are at the transition leaving an SN prefix;
    - climbs: 246,038 of 1,460,118.
    - Example: experiments/n5-exhaustive/instances/b6_xl2_n32.pg (sha1 909c7371…), my N5 deterministic, run 1, S4a 28 → 29.
      - At 28: H1, H2, H3. At 29: H1, ¬H2, ¬H3.
      - {2, 13, 18} enter R; c_θ = 11 and c_w(29) = 8.
      - xsn_exit_probe.py reproduces it.
    - All such crossings in my data are entries (0 leaves; R2-N5-FRZ §6).
    - The per-phase bound held everywhere (max X_SN 75 per phase).
- N-TOG-1 (citation): §0 and §5 cite "P-N5-L2 §11"; X-RUN′ is §7 of P-N5-L2 (sha1 cbea0739). The §11 is presumably the work-log
  numbering of N5-REL-box34.
- Premise status: X-RUN′ is signed by me (R2-N5-L2, 388caf6c) and rests on FRZ (both referees, with FRZ-1..3). REFEREE's L2 report is
  pending, so X-SN-PHASE inherits that pending status.

## 4. RESTARTS: SIGN
- H3-CONST: with an (h) state in the phase, H3 holds at every H2 state. So a restart k → k+1 starts from ¬H1, which makes it a toggle, or
  from H1 ∧ ¬H2.
- From H1 ∧ ¬H2 the step cannot be S4a (H2-STICK), and cannot be an Odd fallback (τ constant), so it is an Even fallback.
  - The phase's first (h)-run adds 1, giving ≤ 1 + T + f. ✓
  - H2-STICK needs H1 at s, which holds here.
- DATA:
  - restarts: 338 / 750,897 by toggle and 6 / 80,401 from H1 ∧ ¬H2, every one at an Even fallback (0 at S4a steps), at most 3 (h)-runs
    per phase. 0 failures.
  - The lane's fbrestart_cex_n12 (35223b6c…) and fbrestart_cex_n24 (a0aacfba…) show the fallback restart in my N5 (1 and 2 restarts).
    My R2-N5-L2 §8 found the same phenomenon independently on j5_n16.

## 5. §7 (not signed): DATA
- onerun_cex_n32 (sha1 70832fcb…) in my N5 (--rand, 4 runs): 1 drop per phase. The lane's 2 drops is a SPEC run, which I did not re-run.
- Climbs reach 2 drops per phase in my variant.
- DROP-LEN: not checked (optional after §4).

## 6. DATA (DATA, not proof). Commands from docs/referee-2/R2-N5-TOG/
- N5: my own (R2-N5-FRZ/frz_check.run_n5). S4a takes any pointwise arena optimum (deterministic, or --rand), and S4c is as in SPEC. Final
  regions equal Oink zlk's on all 234 LIB files (R2-N5-FRZ §10).
- run_all.sh 600 (logs/, climb/, totals_logs.txt, totals_climb.txt):
  - 238 files: LIB (experiments/new/box34/lib.txt) ∪ box34/instances ∪ box35/instances, × 3 starts × {det, --rand}; random 𝒞^1O
    6 × 5,000 at n 4-14 (2 of them --rand).
  - Batch: 31,434 runs, 65,824 transitions, 2,508 fallbacks, 7,599 phases, 484 logs, all OK.
  - Climbs: tog ×4 (random n 5-12, onerun_cex_n32, fbrestart_cex_n12, random n 8-16); 438,498 evaluations, 1,753,992 runs,
    4,286,312 transitions, 0 violations.

## 7. Fixes-file lines
- G-TOG-1: §5: "X_SN also counts the S4a transition from each SN prefix's last state, which X-RUN′ (a) does not ('both ends in P').
  X-RUN's proof gives ≤ 13(d_o + 1)n³ − 1 per (h)-run, so in X-RUN′ C_P + 1 ≤ 13(d_o + 1)n³(t_Q + 1) + t_Q, and the stated per-phase
  bound holds."
- N-TOG-1: §0, §5: "P-N5-L2 §11" → "P-N5-L2 §7".

Signed: REFEREE-2 successor 7 (Opus 5.5, D15).

## Addendum A (2026-10-25 10:04Z by date -u): attribution of G-TOG-1's DATA (Lead 10:06Z, after L-RED 16's SPEC re-run)
- The counts in §3 (310 batch, 246,038 climb crossings at the transition leaving an SN prefix) and the example (b6_xl2_n32 28 → 29,
  "at 29: H1, ¬H2, ¬H3") come from MY N5 ONLY, whose S4a takes another arena optimum. On b6_xl2_n32 my trace diverges from SPEC.
  - L-RED 16 reports the SPEC trace there: 87 iterations / 10 fallbacks, H2 everywhere, c_w = c_θ = 11 at states 1-87, 0 exit crossings.
  - I reproduce exactly that with xsn_exit_spec.py: 87 / 10, 0 exit crossings.
- SPEC witnesses exist. xsn_exit_spec.py takes the state sequence from experiments/new/n5.py (read-only, through my lane's
  R2-N5-RE/re_check.n5_spec, SPEC S3 start), and all checks are my own analysis.
  - On the 238 TOG batch files it finds 19 S4a crossings at the transition leaving an SN prefix, one per file (logs/xsn_exit_spec_lib.txt).
  - Named witness: experiments/n5-exhaustive/instances/b4_cyc6_0.pg (sha1 748e7d51…). SPEC trace 2 iterations / 0 fallbacks.
  - At the S4a step 0 → 1, H1, H2, H3 at 0 become H1, ¬H2, ¬H3 at 1, and {2, 4, 5, 10} enter R.
  - X_SN counts this crossing (its start has c_w = c_θ). X-RUN′ (a) does not, since its end is outside P.
- G-TOG-1's verdict and repair are unchanged. It is a proof gap whichever trace is used, and the stated bound holds by X-RUN's slack.
  Corrected DATA line for the record: "occurs on the SPEC trace (19 library files, e.g. b4_cyc6_0 0 → 1) and in my N5 (310 batch /
  246,038 climb)".

## §C. Comparison with REFEREE (docs/referee/R-N5-TOG.md, referee fff6e62). REFEREE-2 successor 7, 2026-10-25 10:32Z (date -u)
I opened R-N5-TOG.md only after my report (faabe716) and Addendum A (16d27d1c) were pushed. Signature (Opus 5.5, D15).

### C.1 Verdicts
| statement | REFEREE | REFEREE-2 | joint |
| --- | --- | --- | --- |
| L-MONO, Z-COUNT, TOGGLE, TOGGLE-COUNT | SIGNED | SIGN | signed by both |
| X-SN-PHASE | SIGNED WITH GAPS TOG-1, TOG-2 | SIGN WITH GAPS G-TOG-1 (N-TOG-1) | signed by both with the same two items |
| RESTARTS | SIGNED | SIGN | signed by both |
| §7 | not signed | not signed | — |
No verdict differs. Neither referee has a counterexample.

### C.2 Item by item
- TOG-1 = G-TOG-1: the same accounting gap (X_SN counts the S4a crossing out of each SN prefix, which X-RUN′ (a) does not), found
  independently. It is closed the same way, by the slack in X-RUN°'s per-run count: ≤ 13(d_o + 1)n³ − 1.
  - REFEREE's fixes line spells out the per-run sum. I adopt it as the joint line.
  - DATA, both referees: it occurs.
    - REFEREE, SPEC trace: 26 library, 62 + 26 random.
    - Me, SPEC trace via n5.py for attribution (Addendum A): 19 library files, e.g. b4_cyc6_0 0 → 1.
    - Me, my own N5: 310 batch, 246,038 climb.
    - The SPEC counts differ by file set (272 against 238 files).
- TOG-2 = N-TOG-1: "P-N5-L2 §11" → "§7". REFEREE's line also names Lemma X-RUN° (fixes2 §2), which is better. Adopted.
- REFEREE-only notes, accepted:
  - (i) §7's DROP-LEN line is out of date: FALSE by droplen_cex_n12 (R-N5-L2 §8). It is not signed text.
  - (ii) RESTARTS' fallback branch has only the lane's instances on the SPEC trace. My j5_n16 (own N5) and the fbrestart instances,
    which reproduce in my N5, add the same branch.
- Data agree: toggles far below T in both reports (max 6 / 3 in my climbs per phase); every toggle with Z unchanged moved σ(c) at an Even c.

### C.3 Joint gap map (one fixes-file line per row)
| row | REFEREE | REFEREE-2 | kind / status | fixes-file line |
| --- | --- | --- | --- | --- |
| 1 | TOG-1 | G-TOG-1 | accounting, closed by the line; occurs on the SPEC trace | REFEREE's TOG-1 line (§5, after "Summing:": "X_SN also counts the crossing from P(Q)'s last state … ≤ 13(d_o + 1)n³(t_Q + 1) crossings at SN states, and the stated bound holds") |
| 2 | TOG-2 | N-TOG-1 | citation | §0 table and §5: "P-N5-L2 §11" → "P-N5-L2 §7 (X-RUN′; Lemma X-RUN° in P-N5-L2-fixes2 §2)" |

### C.4 Joint label (D18/L40)
- PROVED (L-NEW successor 15; REFEREE and REFEREE-2, Opus 5.5, D15), on 𝒞^1O inside a (λ_Ξ, τ) phase, pending CHECKER:
  - L-MONO, Z-COUNT, TOGGLE, TOGGLE-COUNT, RESTARTS;
  - X-SN-PHASE (rows 1-2; premise X-RUN′ / R32).
- FALSE (DATA): DROP-LEN and its per-run form; "a fallback at H1 ∧ ¬H2 never takes τ(o) out of R".
- OPEN: (L1), f ↔ X, K, G-N5-TIME.
- Not a TARGET.md claim.

Signed: REFEREE-2 successor 7 (Opus 5.5, D15).
