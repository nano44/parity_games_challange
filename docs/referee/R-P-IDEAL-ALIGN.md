# R-P-IDEAL-ALIGN: REFEREE report on P-IDEAL-ALIGN (L-NEW successor 55, box 178)
REFEREE successor 24 (Opus 5.5, D15), 2026-11-06 (date -u in the commit). Independent: I did not open or list docs/referee-2/ on this
packet before this report was pushed.
- Object: claude/l-new cb8e0dca (an ancestor of origin/claude/l-new). Re-measured:
  - docs/new/P-IDEAL-ALIGN.md: sha1 d8acdececb507bfad476341411bddd579fcc5b00, 180 lines;
  - docs/new/P-IDEAL-ALIGN-line-L1.txt: sha1 e46b0417295bfbde7f4cb2d434deed5d0f2e209c, 1 line, 3,055 bytes.
- Premises checked against trunk 4b35e2b0 (RESULTS).

## 0. Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §2 | ALIGN (a), (b), (c) | SIGN |
| §3 | KP-MOVE (a), (b); F0 | SIGN |
| §4 | Theorem PAIR-DOUBLE F(l) ≤ 2F(l − 1) + 2 | SIGN |
| §5 | Corollary MOVES; Corollary T-BOUND T ≤ 2^(d+2) − 2d − 4 on 𝓛^R_d | SIGN |
| §6 | PATH-RISE | SIGN |
| §7 | DATA, exclusions, TARGET diff | not to sign; check.sh block PASS; TARGET diff agreed; optional AL-P1 |
| line | L-1 | NOT YET: REQUIRED AL-L1 (two DATA clauses wider than the tool's counters); optional AL-L2 |

## 1. Premise route
- Byte tests against RESULTS:
  - R105's ENC and MONO: verbatim, the same quotes as in P-IDEAL-KEYS (1 hit each).
  - R110's 𝓛^R_d wording: verbatim (1 hit).
- E-2 does not bear (no CHAINED, RANK_t or KEYFLIP use). moves(x) uses the E2c binder anyway. Correct.
- Not used, correctly:
  - KEYFLIP (KP-MOVE re-proves the one-mover argument);
  - P-IDEAL-KEYS (not landed; PAIR-KF / LADDER are re-proved where needed, as ALIGN (a) and MOVES);
  - every other R105 item.
- No machine premise. The γ(0) ≠ γ(1) bound is machine-only and is EXCLUDED, correctly.

## 2. Proof checks
- ALIGN: SIGN.
  - (a): both options of p, q W-point to the two distinct level-(l − 1) movers. The prefixes differ and decide, so KP = 0 iff b_l(s),
    i.e. KP = c_l(s).
  - (b): (F2) plus «least key under s_t».
  - (c): if s(p) ≠ s(q), the W-targets are {2l − 2, 2l − 1} and ord = [s(p) = c_l(s)]. I checked the orientation: c = 0 iff b iff
    mover 2l − 2 has the smaller key. If s(p) = s(q) = j, the prefixes are equal and the gates decide (γ_l(j)).
- KP-MOVE: SIGN.
  - (a) as ALIGN (b).
  - (b): consecutive moves go to different options (degree 2). By (a), KP differs at s_(t_i) and s_(t_(i+1)). The windows
    (t_i, t_(i+1)] are disjoint.
- F0: SIGN. Level-0 keys are constant gates, so KP is constant and each level-0 mover moves at most once. A (0, 1) flip needs a step
  moving 0 or 1.
- PAIR-DOUBLE: SIGN. I re-derived every step.
  - Alignment w.r.t. c_t: it toggles at b-steps for non-movers, and a moving pair mover lands aligned and was misaligned w.r.t. the
    new c.
  - Φ′(t) = Φ(t − 1) or 2 − Φ(t − 1), and Φ(t) = Φ′(t) − #(Mv_t ∩ {p, q}).
  - ord as a function of (a_p, a_q, c):
    - D-states give a_p;
    - 11 gives γ(c);
    - 00 gives γ(1 − c);
    - at a b-step, 11 ↦ 00 and 00 ↦ 11 keep ord, and only a D-state flips.
  - Hence F(l) ≤ M + B₁.
  - The telescoping is Σ_t #(Mv_t ∩ {p, q}) = Φ(0) − Φ(T) + Σ_b (2 − 2Φ(t − 1)), and M ≤ that sum.
  - h = (2, 1, −2) ≤ 2, and #b-steps = F(l − 1) exactly, since b_l = ord(2l − 2, 2l − 1).
  - So F(l) ≤ 2 + 2F(l − 1). Correct.
- MOVES: SIGN. KP_s(x) = c_l(s) changes iff b_l changes, so KF_x = F(l − 1) exactly. moves ≤ 1 + KF by KP-MOVE.
- T-BOUND: SIGN.
  - F(l) + 2 ≤ 2^(l+2) by induction from F(0) + 2 ≤ 4.
  - T ≤ Σ moves ≤ 2 + Σ_(l=1..d−1) 2(1 + F(l − 1)) = 2d + 2 Σ_(l ≤ d−2) F(l).
  - Σ_(l=0..d−2) (2^(l+2) − 2) = 2^(d+1) − 4 − 2(d − 1), which gives 2^(d+2) − 2d − 4. Recomputed: d = 1, 2, 3, 4 give 2, 8, 22, 52.
- PATH-RISE: SIGN.
  - The current chain of z is a maximal Ξ-path.
  - Two distinct maximal Ξ-paths from z first differ at a common mover y with options k ≠ k′. Each path meets y once (acyclic), so
    their β-sets differ.
  - So cv(z) takes at most P(z) values. By MONO (through ENC) it is non-decreasing, so it rises at most P(z) − 1 times.
- Optional AL-P1 (§5 «Does NOT claim»): «T^R(d) = 2, 4, 8, 13 for d = 1-4 by L-RED's exact data». These are not landed values:
  - T^R(3) = 8 is P-TR3 (signed by me, not landed).
  - T^R(4) = 13 is L-RED's machine result under lane side constraints («L 14 REL+LEM+LAG+KF UNSAT», notes/L-RED.md l. 406;
    docs/red/R197-alt.md l. 34), unrefereed.
  - Label them as lane DATA with their sources. Nothing signed depends on them.

## 3. Independent checks (docs/referee/scratch/align_probe.py, my simulator t3r_sim.py, set order, no ENC; logs align_logs/)
- Coverage: on 𝓛^R_d genomes, every statement:
  - ALIGN (a), (b), (c); F0; PAIR-DOUBLE; MOVES (the KF part at level ≥ 1, the moves bound at every level); T-BOUND (both forms);
  - PATH-RISE: rises of the current Ξ-SET by the R104 order, against P(z) from my own DFS.
- KP-MOVE (a), (b) on the other corpus genomes.
| run set | runs | checks ALIGNA / ALIGNB / ALIGNC / DBL / MOVES_KF / MOVES_MV / PATH / KPMOVE-B | violations |
| --- | --- | --- | --- |
| L-NEW corpus box150-179 at cb8e0dca: 184 𝓛^R genomes (every start if ≤ 64, else stored), 264 others (KP-MOVE only) | 4,246 | 21,922 / 13,433 / 21,922 / 8,489 / 16,978 / 25,470 / 25,470 / 12,057 | 0 |
| 400 random 𝓛^R_d genomes (d 2-6, a third hill-climbed; every start for d ≤ 3, 16 random otherwise) | 10,288 | 54,960 / 28,640 / 54,960 / 26,320 / 52,640 / 73,216 / 73,216 / — | 0 |
- PAIR-DOUBLE equality is reached 132 times (corpus) and 93 times (random). The tightness instance dd_d5_F14 has F(3) = 14 = 2·6 + 2
  (also R-P-IDEAL-KEYS §3).
- Controls fire: «F(l) ≤ F(l − 1) + 1» fails 198 / 103 times, and «rises ≤ P(z) − 2» fails 2,152 / 3,863 times. The bounds are not
  vacuous.
- check.sh block «P-IDEAL-ALIGN» at cb8e0dca (detached worktree): «… PASS». aligncheck.py regenerates aligncheck.out identically
  (fresh run, 0.5 s). All five pins are equal.

## 4. Diff against TARGET.md
- Every statement is inside R104's IDEAL model. The bounds are exponential. Not M3, not M4, not a gauntlet step. G-N5-TIME OPEN.
  Agreed with §7.

## 5. Line L-1
- Shape: one line, 69 «(» / 69 «)», depth never negative, 0 «|», one « — », «2026» once.
- Definitions diffed against §0: T, Mv_t, moves(x) (E2c binder), KP_s, KF_x, flip, F(l), c_l(s), γ_l(j), cv_s and P(z) all MATCH.
- Claims MATCH their signed forms: ALIGN (a)-(c), KP-MOVE, F0, PAIR-DOUBLE, MOVES, T-BOUND and PATH-RISE, with their hypotheses.
- DATA, tested against aligncheck.py's counter code (my rule since C124 E-1: unit and set, not only the §7 words):
  - «PAIR-DOUBLE 0 on 10,648 (run, level ≥ 1) pairs, equality on 44»: runlevels / DBL / dbltight. MATCH.
  - «F0 0 on 5,662 runs» and «T-BOUND 0 on 5,662 runs»: one check per run. MATCH.
  - «PATH-RISE 0 on 32,620 (run, mover) pairs»: runmovers / PATH. MATCH.
  - REQUIRED AL-L1 (C121 / C122 / C124 pattern, DATA wider than its coverage), two clauses:
    - (i) «ALIGN 0 violations on 22,472 (state, level ≥ 1) pairs».
      - (a) and (c) (KPEQ, ORD) are counted on all 22,472 statelevels.
      - (b) (LAND) is tested only at t ≥ 1 («if t and …»): 22,472 − 10,648 = 11,824 pairs. The start states, one per (run, level),
        are excluded.
      - Fix: «ALIGN (a) and (c) 0 violations on 22,472 (state, level ≥ 1) pairs and (b) on the 11,824 of them with t ≥ 1».
    - (ii) «MOVES 0 on 32,620 (run, mover) pairs».
      - The moves bound (MOV) is counted on all 32,620.
      - KF_x = F(l − 1) (KFF) is counted only at level ≥ 1 («if l >= 1 and …»): 32,620 − 2 · 5,662 = 21,296 pairs.
      - Fix: «MOVES 0 on 32,620 (run, mover) pairs for the moves bound and on the 21,296 with level ≥ 1 for KF_x = F(l − 1)».
    - The packet's §7 already separates ALIGN (b) («checked at every step»); the line merged the two counts.
  - KP-MOVE «no separate DATA»: true.
- Optional AL-L2: «improving RESULTS R108's bound T ≤ 3^d − 1 to T ≤ 2^(d+2) − 2d − 4 on 𝓛^R_d» is an improvement only for d ≥ 3. At
  d = 1, 2 the two bounds are equal (2, 8). Say «(strictly for d ≥ 3)».
- Source note «(P-IDEAL-ALIGN, docs/new/P-IDEAL-ALIGN.md; L-NEW successor 55)»: complete now (all proofs in the packet). Once a fixes
  entry exists, it must name the fixes file.
- Verdict: NOT YET (AL-L1).

## DONE / FINDINGS / NEEDS
- DONE: premise byte tests; every proof re-derived; own check with controls on 14,534 runs; check.sh block; TARGET diff; L-1
  definitions / claims / DATA tested against the counter code.
- FINDINGS:
  - All seven statements SIGNED: ALIGN, KP-MOVE, F0, PAIR-DOUBLE, MOVES, T-BOUND and PATH-RISE, with ALIGN (a)-(c) and KP-MOVE (a), (b)
    each signed.
  - L-1 NOT YET: AL-L1, ALIGN (b) and MOVES' KF part counted on fewer pairs than stated.
  - Optional AL-L2 (the R108 «improving» holds for d ≥ 3 only) and AL-P1 (the T^R values are lane DATA).
- NEEDS: L-NEW, via the Lead: line L-2 with AL-L1 (+ optional AL-L2), and a fixes entry if AL-P1 is taken.

## §C (2026-11-06T05:51Z by date -u, successor 24): fixes entry 1 and line L-2
- Object: claude/l-new c787aab1 (an ancestor of origin).
  - docs/new/P-IDEAL-ALIGN-fixes.md: sha1 25b050ee…
  - docs/new/P-IDEAL-ALIGN-line-L2.txt: sha1 cb5f0398…, 3,330 bytes.
  - Unchanged: the packet (d8acdece), L-1 (e46b0417), box178 (aligncheck.py 9335dee7, aligncheck.out b653b01b).
- I know REFEREE-2's items (P-1, P-2) only through the entry.
- F-a (AL-L1): CORRECT. The line numbers quoted from aligncheck.py (52 and 67) and the arithmetic (22,472 − 10,648 = 11,824;
  32,620 − 11,324 = 21,296) are mine and re-measured. The reading note on packet §7 MOVES is right. §7's ALIGN (b) wording («every
  step») was already exact.
- F-b (AL-P1): CORRECT.
  - The T^R values are now labelled lane DATA, unused by any statement.
  - T^R(3) = 8 is P-TR3 (signed, not landed). T^R(4) = 13 is L-RED's result under lane side constraints, with my two sources.
  - T^R(2) = 4 is lane-exact (L-COMP bf2.c, exhaustive; not refereed by me). T^R(1) = 2 is immediate: two level-0 movers, each moving
    at most once (F0).
- F-c (P-1, P-2 = AL-L2): CORRECT.
  - g is §0's gate index.
  - 3^d − 1 and 2^(d+2) − 2d − 4 are 2, 8 at d = 1, 2 and 26 > 22 at d = 3, so the new bound is strictly smaller only from d = 3.
- L-2 byte test (scratch/keys_l2_bytetest.py, the replacements parsed from the fixes file):
  - L-1 + R1..R5, each old string once, gives sha1 cb5f0398…, 3,330 bytes: EQUAL to L-2.
  - Shape: 76 «(» / 76 «)», depth never negative, 0 «|», one line.
  - R1 and R2 are my §5 fix texts verbatim. AL-L1 MET; AL-L2 MET; the source note names the fixes file.
- Verdict:
  - L-2 MATCHES.
  - Fixes entry 1 is CORRECT.
  - All seven statements stay SIGNED. Open items of mine: none.
