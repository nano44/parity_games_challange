# REFEREE-2 notebook (independent second referee)
Rule: do not read docs/referee/ or notes/REFEREE.md before my own report on a claim is pushed.

## Resume point (successor 13, session_01Hjrye27AzEi22tE6LHsM4Y, Opus 5.5 under D15; 2026-10-26 01:1xZ by date -u)
- Handover check a0940b45 (Lead 5/5, GO 00:54Z). Lead queue: P-N5-1O (NEW, top) -> FX (aa227b0b) -> NH42 (93d19be8) -> DUAL (a51f7c30 @ df073cb5).
- P-N5-1O (docs/si/P-N5-1O-box15.md sha1 2cf5e672 @ trunk 291c110d): report docs/referee-2/R2-N5-1O.md: all SIGN, no gap; N-1O-1..6.
  N-1O-1: Lemma OUT step 2 "reward(λ(v)) > 0" false at the rank-0 even cycle node (reward 0); ">= 0" repairs it (reached in data).
  N-1O-2: ITER = O(n^17), packet says O(n^18) (true, loose). N-1O-4: R21 (a) parenthetical general = R18 (d) Lemma S (a). N-1O-5: R32/R33
  chain under R34 (f) read line by line: start-free (discharges R-N5-START's depth caveat).
- Tools R2-N5-1O/onecheck.py (on R2-N5-RE/re_check.py): phases/f/T* per phase, Lemma OUT O1-O6 vs own Zielonka + strategy verifier +
  enumerated strategies; modes random | general | files; ONE_MUT=flip|sbar|early|phi|fb (all bite).
- Read for this packet: docs/referee/R-N5-START.md only (Lead allowed: audit of landed results). R-N5-1O* not opened (not in tree at 01:04Z).
- P-N5-FX (aa227b0b): R2-N5-FX.md all SIGN, no gap; N-FX-1 (FX (a) implied by landed R30 (c)), N-FX-2 (cite R48 repaired; o = c_θ
  case). Tool R2-N5-FX/fx_check.py (FX_MUT=seg|noiii|stick|r30; stick, noiii bite). R-N5-FX.md NOT opened before my push.
- §C 1O 3312144c (identical; OUT-1 = N-1O-1 accepted as closed gap; BIT-N1 accepted; C.4: R34 (b)-(e) line-by-line is mine).
- P-N5-NH-box42 (93d19be8 @ 54ac72e6): R2-N5-NH42.md all SIGN, no gap; N-NH42-1..3. Tool R2-N5-NH42/nh42_check.py (NH_MUT=sw|run|stc|nr;
  run does not bite: no 2 consecutive Ξ-flat transitions in OTHER stretches). R-N5-NH.md / R-N5-NH42.md NOT opened before push.
- P-N5-DUAL (a51f7c30 @ df073cb5): R2-N5-DUAL.md all SIGN (MIRROR (b) as implication), no gap; N-DUAL-1 (wording j vs j+1), N-DUAL-2
  (§2 table coverage), N-DUAL-3 (READING: (H-N5) holds via P-N5-1O, so O(n^17) on C^1E). Tool R2-N5-DUAL/dual_check.py (own N5 loop with
  Odd-first flag; DU_MUT=plain|phi|endg all bite); reproduces lane's lib41 15 runs / 54 two-sided fallbacks. R-N5-DUAL.md NOT opened before push.
- P-N5-GD (b898ff82 @ 3c6f6c16): R2-N5-GD.md all SIGN, no gap; N-GD-1 (R18 (d) Lemma S (c) quoted as iff; only => landed/used),
  N-GD-2 (premise class confirmed, each proof read). Tool R2-N5-GD/gd_check.py (GD_MUT=gda|c2|wo bite, f1 not). No REFEREE GD file at 01:43Z.
- §C GD 6e12b2bc (identical). P-N5-FBRED (11b15455 @ c3f6f2bf): R2-N5-FBRED.md all SIGN, no gap; N-FBRED-1..4 (PFZ range, Y^q
  definition, Lemma S (a) every game CONFIRMED, late regime j >= n NOT reached: data max f-n = -2, climbs -4). Tool R2-N5-FBRED/fbred_check.py.
- §C FBRED a4a642b6 (identical). P-N5-1E (e613db13 @ 7fef9699): R2-N5-1E.md all SIGN, no gap; N-1E-1..5. VJ00 PDF opened
  (brics.dk, sha256 485a12de = R15's): §2, §4.3, §5.2 (11) quotes verified. Tool R2-N5-1E/onee_check.py. R-N5-1E* not opened before push.
- P-N5-VILB (872d4400) and P-N5-ACCEL (301f0be0) @ e7febdc2: R2-N5-VILB.md, R2-N5-ACCEL.md all SIGN, no gap; shared tool
  R2-N5-VILB/va_check.py; EPOCH (a)/(b) global regime NOT reached (data -1, climbs -2); per-class freeze reached and holds.
- Done (was next): P-N5-1E; checks (i) R18 (d) S (a) cited, (ii) '>= 0' repair, (iii) MIRROR (b)+(c) with L(n) = T*(n,n^2,n,n).
- Queue after NH42 (done): DUAL (done) (a51f7c30 @ df073cb5), then GD (docs/new/P-N5-GD-box43.md b898ff82 @ 3c6f6c16).
- Sources (via landed RESULTS, not re-opened): VJ00 BRICS RS-00-48 (sha256 485a12de…, RESULTS R15 object line), p. 16 (11) as quoted in
  P-N5-LP §0 l. 29.

## HANDOVER (successor 12, session_01S8gi5khZfh16sXZ4fcHvZr, Opus 5.5 under D15; written 2026-10-25 23:3xZ by date -u; context ~470k)
Branch claude/referee-2, merged with trunk (--no-ff) before pushes. REFEREE-2 owns no docs/GAPS.md rows. PARKED after this push.
### DONE (every report docs/referee-2/<name>.md; every verdict "(Opus 5.5, D15)")
| item | object (sha1) @ pin | SHA | outcome |
| --- | --- | --- | --- |
| handover check | — | 84d8c8c9 | Lead 5/5 (20:49Z) |
| P-N5-NEEDB | docs/si/P-N5-NEEDB-box13.md 7471aef3 @ e6ee6130 | ef433d32; Addendum A 1a9a0407; §C fafea30e | all SIGN; N-NEEDB-1..5 (N-5: CONJECTURE "in scope, THR => M >= 0" FALSE on block_9501.pg from its pair); §C identical, NEEDB-N1..N4 accepted, C.4 (witness pair) fixed |
| §C FBPOLY | vs R-N5-FBPOLY 3de7cab7 / d6248f7b | 75372604 (+ 6ff47e58) | identical; FBP-1 = N-FBP-2, FBP-2 = N-FBP-1; in RESULTS R48 |
| P-N5-KW | docs/si/P-N5-KW-box15.md c0b0111f + addendum 8d6bfb3c | 8a47fd92 | all SIGN, no gap; N-KW-1..6 (N-KW-3: E-SEG (i) literal count off by e(Q); N-KW-4: RUN (b) sum at r = 1; N-KW-5: freeze delay 39 on kw_n48) |
### IN FLIGHT / NEXT (successor 13), Lead 23:22Z order
1. DONE by successor 12 after the handover (Lead 23:28Z): §C KW in R2-N5-KW.md (KW-1 = N-KW-3, identical; REFEREE's cascb_witness.pg
   reproduced on the spec trace). Also §C NEEDB fafea30e.
2. P-N5-FX (docs/si/P-N5-FX-box14.md, sha1 aa227b0b): not started. docs/referee/R-N5-FX.md EXISTS: do not open before your report.
3. P-N5-NH-box42 (docs/new/P-N5-NH-box42.md, sha1 93d19be8, pinned 54ac72e6), report R2-N5-NH42.md: not started. R-N5-NH.md exists: do
   not open before yours.
4. DUAL (Lead's queue name; not yet pinned to me; ask the Lead for the object).
### Things only I know
- Tools added: R2-N5-NEEDB/ (needb_check.py: XG, ANTI (anti mode for random one-player games), NEEDB at (LV+), OLD-THREAT/FZt, CASEI;
  NB_MUT=nob|anti|otc|otf|xg|b0; needb_climb.py lv|rise; xg_witness.py (rng-free)); R2-N5-KW/ (kw_check.py: all P-N5-KW items and
  PHASE inequalities; KW_MUT=frz0|casc|par; kw_climb.py kw|casc). Both climbs' dump() now saves the pairs evaluate() ran (Addendum A).
- totals.py (both dirs) takes maxima for max_* keys; before the fix it summed them (the KW draft saw fake maxima 3150 / 745).
- (LV+) is reachable only from block_9501's lineage with its start pair (climbs 12001/12004); random seeds reach neither (LV+) nor rises.
- KW: post-freeze kind changes / c_w switches unreached in batch + 160k climb evaluations; CASC-B reached slack 0 (unsaved) and slack 1
  (witness_cascb_13011/13012.pg, reproducible only via the climb's evaluate()).
- Traps this session:
  - The predecessor pushed twice after its handover (2173b54f, f8cb3ef3): fetch + `git log HEAD..origin/claude/referee-2` before push.sh.
  - A repo-wide grep (docs notes) printed LEAD-STATE / RESULTS lines about REFEREE's unreported verdict. Grep only the packet's own dirs.
  - A climb's .txt must hold a start pair VALID on the dumped game (C.4). Witnesses depending on a random optimum must pin σ*.
  - `kill` by a pattern that also occurs in the command's own text (heredoc) kills the calling shell (exit 144). Write scripts with Write.
  - A checker edit while a batch runs: keep checks unchanged, add only RECORD counters.
- Oink was built in this container (20:2xZ); a fresh one must run scripts/setup_oink.sh (~3 min).

## Resume point (successor 12, session_01S8gi5khZfh16sXZ4fcHvZr, Opus 5.5 under D15; 2026-10-25 21:5xZ by date -u)
- Handover check 84d8c8c9 (Lead 5/5, GO 20:49Z). Queue: NEEDB -> §C FBPOLY (REFEREE §C d6248f7b on trunk) -> FX (aa227b0b) -> NH42 (93d19be8,
  report R2-N5-NH42.md). §C PHI done by succ. 11 (f8cb3ef3).
- R2-N5-NEEDB.md: all SIGN, no gap; N-NEEDB-1..5. N-NEEDB-5 FINDING: CONJECTURE "in scope, THR => M >= 0" FALSE on R2-N5-LV2/climb/block_9501.pg
  (its start pair), by N5-LV3 §4's own counterexample shape. N-NEEDB-4: XG reached 7x in climb 12004 (witness_xg_12004.pg).
- Tools R2-N5-NEEDB/ (needb_check.py, needb_climb.py with START = seed's .txt start pair; NB_MUT=nob|anti|otc|otf|xg|b0).
- Independence slip (disclosed in the report): a repo-wide grep printed LEAD-STATE.md l. 1410 / RESULTS R43 lines on REFEREE's R-N5-NEEDB
  after my verdicts were written. Trap: never grep docs/agents/ or RESULTS for an unreported packet; restrict grep to the packet's own dirs.
- §C FBPOLY 75372604 (+ 6ff47e58), in R48. NEEDB Addendum A 1a9a0407 (REFEREE C.4: witness start pairs were the seed's; fixed, xg_witness.py).
- R2-N5-KW (P-N5-KW c0b0111f + addendum 8d6bfb3c): all SIGN; N-KW-1..6. Tools R2-N5-KW/ (kw_check.py, kw_climb.py; KW_MUT=frz0|casc|par).
- Traps (new): totals.py summed max_* keys across files (fixed: maxima); a pattern-kill matched my own shell via heredoc text (write
  scripts with the Write tool, never kill by a pattern that appears in the command); climb dump() must save the pairs evaluate() ran.
- Oink built in this container (20:2xZ).

## HANDOVER (successor 11, session_01VrcXfBuNYKJ3uBUc7ETARQ, Opus 5.5 under D15; written 2026-10-25 20:1xZ by date -u; context ~420k)
Branch claude/referee-2, merged with trunk (--no-ff) before pushes. REFEREE-2 owns no docs/GAPS.md rows. PARKED after this push.
### DONE (every report docs/referee-2/<name>.md; every verdict "(Opus 5.5, D15)")
| item | object (sha1) @ pin | SHA | outcome |
| --- | --- | --- | --- |
| handover check | — | 23e09925 | Lead 5/5 (18:27Z) |
| §C LV2 | vs R-N5-LV2 b454ca3 / 46a8030 / ed8bc207 | ab7843a8 | identical; block witness f2209fa4 supersedes REFEREE's "no saved witness" |
| §C RHO | vs R-N5-RHO 59278313 / 06d6e6d | ab7843a8 | identical; RHO-N2 (R39 (f) is case A only) ACCEPTED, missed by succ. 10 |
| §C PFZ (main + ext) | vs R-N5-PFZ 8595343 / 4859e63 / ed8bc207 | 212f88ec | identical; G-PFX-1 = PFZ-1; BRK-POLY′ (i)-(iii) SIGNED as stated with REFEREE's repair (C.2); data PFZR=1 |
| P-N5-FBPOLY | docs/new/P-N5-FBPOLY-box41.md de244dcd @ 42d8c3a9 | 2fef7c4a | all SIGN; N-FBP-1 ((b) at o = c_θ), N-FBP-2 (deg_U(o) with a self-loop), N-FBP-4 (EXIT loop kind occurs: climb/loop_4102.pg sha1 016473b4) |
| P-N5-PHI | docs/si/P-N5-PHI-box14.md 35e79ec1 @ af3a3b5a | b621f9af | all SIGN; S2 is (b)'s own citation; λ^U checked |
| P-N5-NHN | docs/new/P-N5-NHN-box40.md da7d09ec @ 0bb175d | 04b5c1fd (+ §C in this push) | all SIGN, §7 CONDITIONAL as labelled; N-NHN-1 (= RHO-N2), N-NHN-2; §C vs R-N5-NHN 9bb3f79d: identical, NHN-N2 accepted |
### IN FLIGHT / NEXT (successor 12)
- Queue from the Lead (18:27Z, 18:51Z, 19:18Z): P-N5-NEEDB (docs/si/P-N5-NEEDB-box13.md, sha1 7471aef3, pinned trunk e6ee6130), then
  P-N5-FX (docs/si/P-N5-FX-box14.md, sha1 aa227b0b on trunk, added at fe58fbab; crossings per phase, conditional on FBPOLY). Neither has been started. Independence:
  `ls docs/referee | grep -i 'needb\|N5-FX'` was empty at 20:1xZ.
- PFZ fixes diff: DONE, R2-N5-PFZ §C C.5, ea5cc217. Fixes §1 (3f55bc88) = C.2 in substance, so BRK-POLY′ (i)-(iii) are signed
  unconditionally. This unblocks CHECKER C53 E-1 (R44).
- §C PHI: DONE (R2-N5-PHI.md §C; identical with R-N5-PHI 843ba1f8).
- RESUME POINT (Lead 20:21Z order): P-N5-NEEDB, not started (nothing read beyond its title). Then P-N5-FX. REFEREE's R-N5-FX.md is on
  trunk: do NOT open it before your own R2-N5-FX is pushed. Then P-N5-NH-box42 (Lead 20:12Z:
  docs/new/P-N5-NH-box42.md, sha1 93d19be8, pinned trunk 54ac72e6; report docs/referee-2/R2-N5-NH42.md; Theorem NH:
  (NH′) ⇐ (X) ∧ NFB-O ∧ (E) ∧ (K_W)). That sha1 is the Lead's; re-measure it.
- §C FBPOLY: when REFEREE 10's R-N5-FBPOLY lands.
- Lead NEEDS sent: route N-FBP-1/2 + the loop witness to L-NEW / L-RED.
### Things only I know
- Tools added: R2-N5-PFZ/ (PFZR=1 env in pfzx_check.py: rtlen(), refined θ-LEN, repaired (i); PFZR_MUT=bd|i; run_allr.sh, logs_r/,
  FIT rtl in pfzx_climb.py); R2-N5-FBPOLY/ (fbpoly_check.py: κ-path DFS, EXIT kinds, FX per-vertex bounds, CN, TA, FB; FBP_MUT=fx|ta|fb;
  fbpoly_climb.py FIT frz with dumps frz_hit_ / loop_; files.lst = 492 𝒞^1O files, reused by PHI and NHN); R2-N5-PHI/ (phi_check.py,
  PHI_MUT=ub); R2-N5-NHN/ (nhn_check.py imports R2-N5-RHO/rho_check.py; NHN_MUT=pin1|nhn).
- FBPOLY data: FREEZE-EXIT / THETA-AFTER hypotheses (f ≥ |U| − 1 at |U| ≥ 3) never reached in batch or 1.92 M climb runs; f = |U| − 2
  in 63 batch phases; kind-c_θ FX bound reached with equality in climb 4101 (not saved).
- Traps this session:
  - The predecessor pushed THREE times after its handover (11126df8, eed4efd2, 2fef675c). push.sh was rejected twice. The check
    "fetch + git log HEAD..origin right before push.sh" caught each one.
  - A checker bug of mine (o = c_θ: p_u tested against Û instead of G_U) surfaced only in a climb. A climb violation is first a
    checker suspect: reproduce with the climb's own evaluate(g, o, fit, seed), since inst mode seeds its rng differently.
  - `pgrep -f <pattern>` / `pkill -f <pattern>` match the calling shell's own command line. A wait loop on `pgrep -f run_allr.sh`
    never ended, and a `pkill -f "fbpoly_climb.py frz 410"` killed its own shell. Use `ps aux | grep "[x]yz"`.
  - Sha1s typed from memory into a §C were wrong twice (RHO, NHN). Paste them from `git show <ref>:<path> | sha1sum` output only.
  - `git log -- docs/referee/` subjects carry REFEREE verdicts. For unreported packets, list file names only.
- Oink is built in this container (setup 18:12Z).

## HANDOVER (successor 10, session_012VrKctzqedu9x1gVAMchV7, Opus 5.5 under D15; written 2026-10-25 17:3xZ by date -u; context ~390k)
Branch claude/referee-2, merged with trunk (--no-ff) before each push. REFEREE-2 owns no docs/GAPS.md rows. PARKED after this push
(Lead: hand over at ~450k; parked at ~415k after c2c326c7; the §Cs and NHN are left to successor 11).
### DONE (every report docs/referee-2/<name>.md; every verdict "(Opus 5.5, D15)")
| packet | object (sha1) @ pin | report SHA | §C | outcome |
| --- | --- | --- | --- | --- |
| handover check | — | 5ca9ac38 | — | Lead 5/5 (16:32Z) |
| P-N5-LV2 | docs/si/P-N5-LV2-box12.md 3b23a41f @ 283bcb6 | a551debf | NOT DONE | all SIGN; N-LV2-1 (R36 status), N-LV2-2 (wording, also in R37 (f) EV), N-LV2-3 (DATA) |
| P-N5-PFZ-ext | docs/new/P-N5-PFZ-ext-box39.md b3702b1b @ c61ecc4 | 78896bfc (§X of R2-N5-PFZ.md) | NOT DONE | P-FREEZE′, θ-LEN SIGN; BRK-POLY′ (i) NOT SIGNED as stated, G-PFX-1, (i′) SIGN |
| P-N5-RHO | docs/new/P-N5-RHO-box40.md cd5df65c @ c814455 | 269ae45a | NOT DONE | all SIGN; N-RHO-1 (wording), N-RHO-2 (DATA) |
| LV2 addendum | level −1 block witness (Lead 17:48Z ask) | f2209fa4 | — | R2-N5-LV2/climb/block_9501.pg sha1 1b5b76fd (r 10, M −1, 3 (β) gates; own = SPEC); start pair in block_9501.txt |
### IN FLIGHT / NEXT (successor 11)
- §C PFZ: compare R2-N5-PFZ (successor 9's §1-§6 AND my §X) with REFEREE's R-N5-PFZ (referee 8595343, covers both files per the Lead).
  P-N5-RHO l. 10-11 / 213-214 quotes "REFEREE's GAP PFZ-1" on (i) with a repair "(θ_S ≤ (ρ_S + 1)(|U| − 2))" (the packet's wording):
  check whether REFEREE's PFZ-1 = my G-PFX-1 or a different reading, and diff the repaired statements.
- Lead 17:34Z (its stamp): a551debf + 78896bfc merged to trunk 0bb175d; N-LV2-1..3 routed to L-SI, G-PFX-1 to L-NEW (PFZ fixes file).
  Queue: RHO (done by me) -> §C PFZ (main + ext) vs REFEREE R-N5-PFZ 8595343 + its §C 4859e63, and its ext §C when it lands -> §C LV2
  vs R-N5-LV2 b454ca3 + addendum 46a8030 -> P-N5-NHN (docs/new/P-N5-NHN-box40.md, sha1 da7d09ec, pin trunk 0bb175d) -> §C RHO vs
  REFEREE 10's report when routed.
- Lead 17:56Z (its stamp; read by me 18:09Z): REFEREE 10 on trunk: R-N5-RHO 5927831 (all SIGNED; mine 269ae45a is pushed, so readable);
  PFZ-ext §C ed8bc20 (PFZ-1 = G-PFX-1; REFEREE re-derives a repair proving (i) AS STATED: refined θ-LEN ≤ |A_low| − [o low] per
  P-epoch, and ρ_S ≥ 1 forces a high u ≠ o, so θ_S ≤ (ρ_S+1)(|U|−2) − 1). The Lead asks the PFZ §C to say whether (i) would be signed
  once that repair is in the fixes file: CHECK the refined θ-LEN yourself (pfzx_check.py can count length moves vs |A_low|).
  LV2 §C ed8bc20: N-LV2-3's conjecture FALSE on experiments/red/so/instances/beta2_n11.pg (bdea2a23); I withdrew it in R2-N5-LV2
  Addendum B (eed4efd2) and ran LV-NONE at N = 2 there (0 violations).
- Lead NEEDS sent 17:2xZ: N-LV2-1..3 to L-SI; G-PFX-1 to L-NEW; CONJECTURE "an in-scope THR fallback with M = −1 is the last fallback of its
  scope run" to L-RED.
### Things only I know
- Tools added: R2-N5-LV2/ (lv2_check.py on R2-N5-LV/lv_check + ent_check + out_check; lv2_climb.py FIT none / blk; files_new.lst = 158
  tracked C^1O files newer than R2-N5-OUT's list); R2-N5-PFZ/pfzx_check.py (pfz_check with θ-run -> P-epoch, PFZX_KEY=theta restores;
  θ-LEN, BRK-POLY′, (i′)), pfzx_climb.py FIT brki, filesx.lst (453); R2-N5-RHO/rho_check.py (exact DFS optima, RHON=12), rho_climb.py.
- LV2 data: the u* = none part is reached ONLY from my predecessor's witness lineage (best_lv_9401.pg -> climb/best_none_9501.pg); random-
  seeded "none" climbs reach r = −1 states but no fallback there. 645 level −1 block fallbacks (r ≥ 0) appeared inside climb 9501 and
  were not saved (9505 retry failed). Max 1 per scope run of each M = −1 class in all data.
- PFZ-ext data: (i) as written never exceeded (max excess 0) in 277k HN stretches; G-PFX-1 is a proof gap only.
- RHO data: FREEZE-F (b) vacuous (0 states); post-hat-freeze only at |U| = 3; mutation hatall bites (701), frzb0 does not (M on F ∩ U
  already frozen from s in tested runs).
- Traps this session:
  - The predecessor pushed twice AFTER its handover and after my first fetch (a769ff54, 937535e5): push.sh rejected with "fetch first".
    Re-fetch and `git log HEAD..origin/claude/referee-2` right before every push.sh.
  - My "not on trunk" for 37e55fde was measured against a stale trunk ref (e05382f); the Lead found it on trunk via c74648b. Fetch trunk
    in the same command as the ancestry check.
  - A climb's fitness edited while it runs does not change the running process (9501 ran the old weights); say so in the report.
  - Editing a checker while a batch runs changes later files' runs: keep default behaviour unchanged (only behind MUT flags).
- Oink is built in this container (8fbf0a7).

## HANDOVER (successor 9, session_0163ejRshYhYxVW2CD2XUEB2, Opus 5.5 under D15; written 2026-10-25 16:07Z by date -u; context ~360k)
Branch claude/referee-2, merged with trunk (--no-ff) at each packet. REFEREE-2 owns no docs/GAPS.md rows. PARKED after this commit.
### DONE (every report docs/referee-2/<name>.md; every verdict "(Opus 5.5, D15)")
| packet | object (sha1) @ pin | report SHA | §C SHA | outcome |
| --- | --- | --- | --- | --- |
| handover check | — | ba6fac1b | — | Lead 5/5 |
| P-N5-OUT | docs/new/P-N5-OUT-box37.md 9f032e61 @ 719ce66 | dfcaae67 | 2a9e8db0 | all SIGN; N-OUT-1..4 (fixes 640a5db2 checked); REFEREE identical |
| P-N5-ENT | docs/si/P-N5-ENT-box11.md 4fd22be7 @ 765e893 | b7df84b8 | f33884e6 + addendum cf54523b | 6 SIGN + 4 SIGN COND (P), and R36 lifts (P); N-ENT-1..3; REFEREE identical (§C d6b8aef9) |
| P-N5-NEB | docs/new/P-N5-NEB-box38.md ba15e51f @ 314d220 | a4516df9 | — (REFEREE 9's report pending) | all SIGN; N-NEB-1..3 |
| P-N5-LV | docs/si/P-N5-LV-box11.md d0d797f0 @ 601df6e (+ addendum a15a8871, not to sign) | b1038bea | — | all SIGN (LV-CN, LV-COUNT COND CN-LAST, now R38); N-LV-1..3 (N-LV-3: u* = none (LV) states reachable; witness R2-N5-LV/climb/best_lv_9401.pg) |
| P-N5-PFZ | docs/new/P-N5-PFZ-box39.md 3c617e06 @ 283bcb6 | 37e55fde | — | all SIGN; N-PFZ-1..3 (post-freeze only with |U| <= 2 in all data) |
### IN FLIGHT (updated after the Lead's 15:41Z / 15:59Z messages, which crossed with my handover)
- §Cs DONE since: NEB §C + LV §C in a769ff54 (vs REFEREE 9's R-N5-NEB 40adbf1c and R-N5-LV 8054da2f; identical verdicts; I accepted
  NEB-N1..N3 and LV-N3).
- P-N5-PFZ-ext (docs/new/P-N5-PFZ-ext-box39.md sha1 b3702b1b, pinned c61ecc4; to sign: P-FREEZE′, θ-LEN, BRK-POLY′). NOT started.
  The Lead wants R2-N5-PFZ.md to cover BOTH files: add a section for the ext file. pfz_check.py's theta_run() is the base (key the
  run by P(θ) instead of θ, as PFZ_KEY=P does in the lane's script).
- P-N5-LV2 (docs/si/P-N5-LV2-box12.md sha1 3b23a41f, pinned 283bcb6, l-si ed936af1; pin and l-si sha1 verified by me). NOT started beyond:
  - The Lead asks: check the lane's claim that N-LV-1 / N-LV-2 are not inherited (its lines 60-65).
  - To check first: §4 (iii) (l. 142-143) and §7 (2) (l. 210-211) apply STRETCH_{-1} with e := f_{N-1} + 1. That needs COARSE_{-1}(Xi)
    constant on [f_1, f_{N-1} + 1]; find where LV2 proves it.
  - Statements to sign: STALE-GATE, EV-G, ENT-X_{-1}, LV-PL', SAND, FLAT-ALL_{-1}^{none}, LV-NONE, SCOPE-FB. It depends on P-N5-LV and
    P-N5-ENT (R40).
  - My R2-N5-LV/lv_check.py already reaches u* = none (LV) states in climbs: use it as the base for FLAT-ALL_{-1}^{none} / LV-NONE.
  - The Lead asks: count r = -1 THR in-scope fallbacks PER SCOPE RUN in those climbs, to test LV-NONE (<= n*n_E + 1 per scope run) and
    SCOPE-FB. lv_check.py does not record per-run maxima yet; add an mxu().
- §Cs for NEB, LV and PFZ: when the Lead routes REFEREE 9's reports. Not read yet.
### NEEDS
- Lead: route N-NEB-1..3 and N-PFZ-1..3 to L-NEW, N-LV-1..3 to L-SI, and the u* = none witness to L-RED.
### Things only I know
- Tools added this session (own code; each dir has run_all.sh, run_climbs.sh, logs/, climb/, totals*.txt):
  - R2-N5-OUT/out_check.py: the base. analyse() adds HN and lamW to frz_check.analyse; run_trace(mode) gives own / rand / spec
    (spec = re_check.n5_spec). spec_s3.py reproduces the lane's fbsplit exactly.
  - R2-N5-ENT/ent_check.py ((Sigma)-pairs, blocks), rise_end.py. R2-N5-NEB/neb_check.py (classes by case x c_w x tau(o)).
  - R2-N5-LV/lv_check.py. R2-N5-PFZ/pfz_check.py (U, M_t, G_U, DFS Mopt; PFZN=12 caps |U| for the DFS, and skips are counted).
  - *_climb.py are all ent_climb.py with a fitness; seeds are lane instances (inputs only).
- Recurring traps this session:
  - A HANDOVER section is not the branch head. Check `git log <handover SHA>..origin/claude/referee-2` and ancestry against trunk.
    The predecessor's late push (7ed07fe5) arrived after my first fetch.
  - A totals/summary regex that silently drops keys (counter names with "!"). Use ^([^:]+): (-?\d+)$ and check that every expected class
    shows up.
  - Post-pin lane instances (experiments/new/box38) live in the library. A checker should RECORD what §7 conjectures fail, not count it
    as a violation.
  - "Vacuous in data" must be said per statement: corollaries over all blocks are usually exercised even when the setting is not
    (N-ENT-2).
- Oink is built in this container; a fresh container must run scripts/setup_oink.sh (~3 min).

## Resume point (successor 9, session_0163ejRshYhYxVW2CD2XUEB2, Opus 5.5 under D15; 2026-10-25 13:5xZ by date -u)
- Handover check ba6fac1b (Lead 13:35Z by its stamp: 5/5, GO for R2-N5-OUT then R2-N5-ENT; REFEREE's R-N5-OUT fa08687 / R-N5-ENT 55a3f6f
  are on trunk: NOT to be read before mine are pushed).
- P-N5-OUT (docs/new/P-N5-OUT-box37.md sha1 9f032e61 @ trunk 719ce66): docs/referee-2/R2-N5-OUT.md. All SIGN (SPLIT, EPOCH corrected,
  F-FLAT, FREEZE-STEP + TAIL, NO-ENTRY-A, NE-COUNT, CASE-B-LEN + W-SIDE); notes N-OUT-1 (FBL-N (iii) already has o in R), N-OUT-2 (Step (K)
  cited "inside a phase", BASE needs only FBL-N (i) + F1), N-OUT-3 (stale status), N-OUT-4 (§7 NO-ENTRY-B / τ≠o NO-ENTRY FALSE per lane box 38,
  reproduced in all 3 traces). Tools R2-N5-OUT/ (out_check.py on R2-N5-FRZ; traces own / rand / spec). Batch 66,655 runs, climbs 741,432
  runs, 0 violations. spec_s3.py reproduces the lane's fbsplit numbers exactly. Mutation controls theta / caseB / nohyp all caught.
- R2-N5-OUT pushed dfcaae67 (Lead messaged 13:58Z).
- P-N5-ENT (docs/si/P-N5-ENT-box11.md sha1 4fd22be7 @ 765e893): docs/referee-2/R2-N5-ENT.md. FZ, BF, RB, WALK, CYC-EV, TEV-FB SIGN;
  ENT-X, NJB-A, D1, PL-S″ SIGN CONDITIONAL ON (P) (via EV+). N-ENT-1 (CYC-EV here generalises the RL-fixes CYC-EV), N-ENT-2 (corollaries
  not vacuous: 698 r > M intervals, all clean), N-ENT-3 (stale status). Reachability: 0 (Σ)-pairs with a rise in batch + climbs; every
  rise after a fallback (62 library, 26,665 climb) is followed by NO further fallback of S (DATA record; rise_end.py). Tools R2-N5-ENT/.
- §C OUT 2a9e8db0 (vs REFEREE fa08687 + a8b8ef3; fixes 640a5db2 checked; c_w != o qualification confirmed on all traces); §C ENT f33884e6
  (vs 55a3f6f; identical; tev_cex_n40 counts identical across engines; N-ENT-2 vs REFEREE's "vacuous" wording).
- P-N5-NEB (docs/new/P-N5-NEB-box38.md sha1 ba15e51f @ 314d220): docs/referee-2/R2-N5-NEB.md a4516df9, all SIGN; N-NEB-1..3. Tools R2-N5-NEB/.
- P-N5-LV (docs/si/P-N5-LV-box11.md sha1 d0d797f0 @ 601df6e + addendum a15a8871, not to sign): report docs/referee-2/R2-N5-LV.md in progress;
  all SIGN (LV-CN, LV-COUNT COND CN-LAST); N-LV-1 (FBW-1 H1 vs H2), N-LV-2 (STRETCH k <= e). (LV) setting empty in batch.
- LV climbs reached the (LV) setting with u* = none (r = -1): 173,371 states, LV-SHAPE 0 failures; witness climb/best_lv_9401.pg (SPEC,
  S3 start, state 2). This refutes the packet's §5 DATA line "0 in scope" (N-LV-3), not any signed item.
- NEXT: §Cs for NEB / LV when the Lead routes REFEREE's reports.
- Trap (mine, this session): a totals regex that silently dropped counter names with "!" (NEB). Use ^([^:]+): (-?\d+)$ and check that
  every class you expect appears in the summary.
- Trap: experiments/new/box38 instances (post-pin lane cex of §7 conjectures) are in the library; the checker records them, does not fail.

## Handover check (successor 9, session_0163ejRshYhYxVW2CD2XUEB2, Opus 5.5 under D15/L37; 2026-10-25 13:01Z by date -u)
Predecessor successor 8 session_018vPA5mmjjVjrRV4KqAJfFk (parked). Measured from the repository; commands named.

1. Branch, head, distance to trunk.
   - `git status`, `git log --oneline -3` at container start: local claude/referee-2 at 77f9cf71 (STALE, fourth time; the notebook had no
     successor-8 HANDOVER section).
   - `git fetch origin`; `git rev-parse HEAD origin/claude/referee-2` -> 77f9cf71 vs db9d66a8; `git merge --ff-only origin/claude/referee-2` -> db9d66a8.
   - Trunk = claude/vibrant-johnson-nxvvxo (docs/NOW.md:15). `git fetch origin claude/vibrant-johnson-nxvvxo`;
     `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 2 ahead, 10 behind (trunk 2c3a7677).
     The 2 ahead: d347d8f1 (merge trunk) and db9d66a8 (R2-N5-RL Addendum A), both after the 88571b03 that trunk merged (3e6cd80e).
   - `git merge --no-ff -m ... origin/claude/vibrant-johnson-nxvvxo` -> merge commit bddffda0; count -> 3 ahead, 0 behind. This notebook commit adds one.
2. Open work, next step of each.
   - Successor 8's HANDOVER (12:48Z) says IN FLIGHT: none. Not true of its head: db9d66a8 (12:54Z, after the handover) adds R2-N5-RL
     Addendum A (CYC-EV SIGN; replacement TEV-RED and Consequence SIGN CONDITIONAL ON (P)), read at the Lead's 12:49Z request.
     `git merge-base --is-ancestor db9d66a8 origin/claude/vibrant-johnson-nxvvxo` -> no: Addendum A is NOT on trunk.
     Next step: Lead merges claude/referee-2 (it rides this push).
   - Successor 8's NEEDS (Lead routes RL-1..4 and N-P1-1 to L-SI): Lead's, not mine.
   - Task 1 after GO, P-N5-OUT: `sha1sum docs/new/P-N5-OUT-box37.md` -> 9f032e61…aba; `git show 719ce66:<file> | sha1sum` and
     `git show origin/claude/l-new:<file> | sha1sum` -> same. Next: read packet, P-N5-SCOPE (KEY, FB-INT), SPEC; build R2-N5-OUT/ on
     R2-N5-SCOPE/scope_check.py; write docs/referee-2/R2-N5-OUT.md.
   - Task 2 after GO, P-N5-ENT: `sha1sum docs/si/P-N5-ENT-box11.md` -> 4fd22be7…0d0; same at 765e893 and at origin/claude/l-si.
     Next: read packet, EV+ in P-N5-RL, L-RED tev_cex_n40 / tevlast_cex_n40 (from lane branches if not on trunk); reachability of the
     (Σ) + rise hypotheses; write docs/referee-2/R2-N5-ENT.md. Note: CYC-EV is in the ENT sign list and successor 8 signed a CYC-EV in
     Addendum A (of docs/si/P-N5-RL-fixes-box10.md); I re-check the ENT text on its own and diff the two statements.
   - Independence: `ls docs/referee/ | grep -i 'N5-OUT\|N5-ENT'` and `git ls-tree -r --name-only origin/claude/referee docs/referee |
     grep -i 'N5-OUT\|N5-ENT'` -> empty. Not opened.
   - Oink: `ls tools/oink/build` -> absent; scripts/setup_oink.sh started (13:01Z).
3. GAPS rows. `grep -n 'G-N5-TIME\|REFEREE-2' docs/GAPS.md`: REFEREE-2 owns no row. Relevant: G-N5-TIME | major | L-NEW | open (docs/GAPS.md:11);
   last update R35 (11:51Z): open NJB = ENT (CONJECTURE; lane reductions EV/EV+/TEV-RED = P-N5-RL), REL(S), level −1 fallbacks,
   out-of-scope fallbacks (P-N5-SCOPE; lane NO-ENTRY-A), θ-changes per HN stretch. Task 1 (NO-ENTRY-A, out-of-scope) and task 2
   (ENT) are both on this row's open list.
4. Owner rulings verbatim (docs/DECISIONS.md), status from docs/DECISIONS-INDEX.md (`grep -n` on both):
   - D1 (index line 5: active), DECISIONS.md:7-8:
     > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
     > Never downgrade the referee to save money.
   - D15 (index line 26: active), DECISIONS.md:278:
     > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
   - D18 (index line 32: active), DECISIONS.md:333:
     > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
5. Trap found: a HANDOVER section is not the head. Successor 8's handover (written 12:48Z, "IN FLIGHT: None", committed 88571b03) was
   followed by db9d66a8 (12:54Z) on the same branch; trunk merged only 88571b03. Reading the notebook alone, or trusting trunk to hold
   my branch, would lose Addendum A. Check `git log <handover SHA>..origin/claude/referee-2` and `git merge-base --is-ancestor` against
   trunk, not the handover's own words. (The stale local ref at container start, 77f9cf71, is the same trap one level down.)
   Second instance, same session: my first scripts/push.sh (13:1xZ) got VERIFY PASS and then "! [rejected] (fetch first)". Successor 8
   had pushed 7ed07fe5 (committed 12:57Z, a DONE-table row for Addendum A) after my 13:00Z fetch. `git fetch origin claude/referee-2`;
   `git log HEAD..origin/claude/referee-2` -> 7ed07fe5 only (1 line in this notebook); merged with --no-ff, no conflict. So the
   predecessor's branch can still move during the handover check: re-fetch right before pushing. Correction to item 2: with 7ed07fe5
   the handover table does list Addendum A (db9d66a8); "IN FLIGHT: None" is then true; it is still not on trunk.

## HANDOVER (successor 8, session_018vPA5mmjjVjrRV4KqAJfFk, Opus 5.5 under D15; written 2026-10-25 12:48Z by date -u; context ~460k)
Branch claude/referee-2, merged with trunk at each packet. REFEREE-2 owns no docs/GAPS.md rows. PARKED after this commit.
### DONE (every report docs/referee-2/<name>.md; every verdict "(Opus 5.5, D15)")
| packet | object (sha1) @ pin | report SHA | §C SHA | outcome |
| --- | --- | --- | --- | --- |
| handover check | — | 6eda0134 | — | Lead 5/5 |
| P-N5-SCOPE | docs/new/P-N5-SCOPE-box36.md c3f5ed37 @ 8998ee6 | 6d6e4bcf | fb6fa696 (+ 8655f692 stamp) | all six SIGN; notes N-SC-1..4, O-1 (§7.2 f_out needs + X_out); no verdict differs from REFEREE |
| P-N5-RL | docs/si/P-N5-RL-box10.md 0a3c70cb @ 2fb698d | 30dc5f54 | this commit | after §C: MERGE SIGN WITH GAP RL-2 (ℓ = ∞; my miss); TEV-RED NOT SIGNED as stated (RL-1 = G-RL-1 cycle case; RL-3 = G-RL-2 "up to and including e"); TEV-RED′ SIGN COND (P); Consequence NOT SIGNED as stated; RL-4 citation (NO-RF-OLD Corollary; my miss); rest SIGN / SIGN COND (P) / COND CN-LAST, labels exact |
| P-N5-RL fixes (Addendum A) | docs/si/P-N5-RL-fixes-box10.md ac027458 (l-si 1f107bfb, on trunk) | db9d66a8 | — | CYC-EV SIGN (no (P)); replacement TEV-RED + Consequence SIGN CONDITIONAL ON (P); cycev_probe 836 (Σ) settings 0 failures, ENT case vacuous |
| P-N5-P1 | docs/si/P-N5-P1-box10.md b98ca794 @ 48a8a4c | e036e4c5 | this commit | Lemma B, M, P1, §4 SIGN; no gaps; REFEREE §5 correction accepted (only TEV-RED′ becomes unconditional) |
### IN FLIGHT
None.
### NEEDS
- Lead: route the RL joint fixes lines (R2-N5-RL §C.4: RL-1..4 + my wording notes) and N-P1-1 to L-SI; N-SC-1..4, O-1 already routed to L-NEW 17.
### Things only I know
- Tools added this session (own code; each dir has run_all.sh, logs/, totals*.txt):
  - R2-N5-SCOPE/scope_check.py (on R2-N5-FRZ): KEY, TC, WCH, SCOPE-COUNT, FB-INT (tameness via COARSE_{M_k}), NH1-FB, CN-LAST, §7.1 classes.
    It also has an own GENERAL-game N5 (run_general: honest Ξ = Odd one-player SI pointwise min; U = Even best response; S4b = Odd arena
    optimum), validated by gxcheck.py against Oink (574/574). scope_climb.py (FIT scope / fb / cnl; cnl uses general games, gmutate).
    mklib.py lists tracked experiments/**/*.pg on 𝒞^1O with n ≤ 64 (276-280 files).
  - R2-N5-RL/rl_check.py: BL-FORM, BL (a)-(e) (W* = Even best response, Opt(G_τ[F]) by restricted SI), FREE-FREEZE, MERGE (FINITE levels
    only: `l >= INF: continue`; that is exactly how I missed RL-2), EQ-END, ENT setting + EV/EV+/TEV-RED, CYC probe (c's cycle meets Ev).
    rl_climb.py FIT cyc; tev_probe.py (TEV-RED (3) both forms at every post-rise state, k need not exist).
  - R2-N5-P1/p1_check.py (exhaustive strategies, extended order coded from the packet text), mutation.py.
- Lane instances only on lane branches (not trunk) must be extracted with `git show origin/<branch>:path` into the scratchpad (tevlast_cex_n40
  was on l-red only).
- Recurring traps this session:
  - Plain `git merge` fast-forwards silently when the branch is 0 ahead: use --no-ff.
  - Check each numbered sub-claim against its STATED form, not its proof line (G-RL-2).
  - A statement's quantifier range must be read against the level ORDER it imports: "ℓ ≥ −1" includes ∞ (RL-2). Never let a checker skip
    a case silently; count skipped cases and say so.
  - "Exists-a-last-X" steps on lasso plays need the cycle to avoid X (G-RL-1).
  - A proof gap whose case is not excluded makes the statement NOT SIGNED as stated, with a repaired form signed (D1); not "SIGN WITH GAPS".
  - Citations of a lemma that ASSUMES an object (ENT-SHAPE "Let (y, z) be …") for the object's existence (RL-4).
- Oink built in this container (8fbf0a7); a fresh container must rebuild it (scripts/setup_oink.sh, ~3 min).

## Resume point (successor 8, session_018vPA5mmjjVjrRV4KqAJfFk, Opus 5.5 under D15; 2026-10-25 11:56Z by date -u)
- Handover check 6eda0134 (Lead 11:09Z: 5/5, GO for R2-N5-SCOPE).
- P-N5-SCOPE (docs/new/P-N5-SCOPE-box36.md sha1 c3f5ed37 @ trunk 8998ee6): report docs/referee-2/R2-N5-SCOPE.md. KEY, WCH (N-SC-2),
  SCOPE-COUNT, FB-INT (N-SC-3), NH1-FB (N-SC-4), CN-LAST all SIGN; header citation (R-CONST = P-N5-L2 §5) correct, N-SC-1 stale status.
  O-1 on §7.2 (not signed): evicting fallbacks are crossings, so f_out needs "+ X_out". Tools R2-N5-SCOPE/ (scope_check.py on
  R2-N5-FRZ; own GENERAL N5 run_general for CN-LAST, Oink-validated by gxcheck.py 574/574). 0 violations: 86,517 batch + 5,443,544 climb runs.
- §C SCOPE fb6fa696 (+ stamp 8655f692) vs REFEREE R-N5-SCOPE (fb6089b + 560ff4c): no verdict differs; joint gap map empty.
- P-N5-RL (docs/si/P-N5-RL-box10.md sha1 0a3c70cb @ trunk 2fb698d): docs/referee-2/R2-N5-RL.md. All SIGN, labels exact; BL (b),(c),(e),
  FREE-FREEZE, EV, EV+ conditional on (P); EQ-END on CN-LAST; TEV-RED SIGN CONDITIONAL ON (P) WITH GAPS G-RL-1 (last Ev vertex needs c's
  cycle at t in F_k0; 0 cases in data) and G-RL-2 (3) "before e" -> "up to and including e" (L-RED 16 tevlast_cex_n40, on l-red only,
  reproduced with my N5; I missed it in the draft). Notes N-RL-1..3. ENT setting vacuous in my data. Tools R2-N5-RL/.
- P-N5-P1 (docs/si/P-N5-P1-box10.md sha1 b98ca794 @ trunk 48a8a4c): docs/referee-2/R2-N5-P1.md e036e4c5. Lemma B, M, P1, §4 all SIGN
  (N-P1-1 trivial cases). Tools R2-N5-P1/ (p1_check.py exhaustive strategies; mutation.py: flipped odd rule and CAV coarse order caught).
- NEXT: §C for RL and P1 when the Lead says REFEREE's reports are on trunk (not read before).
- Trap: check each numbered sub-claim against its STATED form, not only its proof line (G-RL-2: the proof wrote "up to e", the statement
  "before e").
- Trap: Iτ is a function of τ alone (n5.py l. 30), so after an Even fallback Iτ_{k+1} = Iτ_k; CN-LAST's τ-change branch needs Iτ_k ≠ ∅
  with S4b keeping τ (rare in batch, common in FIT cnl climbs).

## Handover check (successor 8, Opus 5.5 under D15/L37; 2026-10-25 11:0xZ by date -u)
Predecessor successor 7 session_01CE1xQNfGUgtJg9A7SWAkuE (parked, 8681e3f2). Measured from the repository; commands named.

1. Branch, head, distance to trunk.
   - `git status`, `git log --oneline -1` at container start: local claude/referee-2 at 77f9cf71 (STALE, third time).
   - `git fetch origin`; `git rev-parse HEAD origin/claude/referee-2` -> 77f9cf71 vs 8681e3f2; `git merge --ff-only origin/claude/referee-2` -> 8681e3f2.
   - Trunk = claude/vibrant-johnson-nxvvxo (docs/NOW.md:15). `git fetch origin claude/vibrant-johnson-nxvvxo`;
     `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 0 ahead, 25 behind (trunk 8998ee6d).
   - `git merge --no-ff -m ... origin/claude/vibrant-johnson-nxvvxo` -> merge commit 63ff0909; count -> 1 ahead, 0 behind. This notebook commit adds one.
2. Open work, next step of each.
   - Successor 7's IN FLIGHT: none. Its NEEDS (Lead routes FRZ rows 4-5, NJB rows 1-2, TOG rows 1-2 to lanes): Lead's, not mine.
   - Task after GO: independent review of P-N5-SCOPE. `sha1sum docs/new/P-N5-SCOPE-box36.md` -> c3f5ed3788f0853939d247dbcfb970334c9dcf7d;
     `git show 8998ee6d:docs/new/P-N5-SCOPE-box36.md | sha1sum` and the same at origin/claude/l-new -> same sha1 (pin and lane agree);
     `git log -- <file>` -> one commit 8483279d (L-NEW box 37 (a)). Statements §1 KEY, §2 WCH, §3 SCOPE-COUNT, §4 FB-INT, §5 NH1-FB, §6 CN-LAST; §7 not to sign.
     Next step: read packet + SPEC (docs/new/N5-ssi-global.md) + RESULTS R15, R18, R19, R22, R25, R28, R30-R33 + P-N5-TOG; build
     docs/referee-2/R2-N5-SCOPE/ on R2-N5-TOG/tog_check.py and R2-N5-FRZ/frz_check.py (one-Odd-choice assert on every 𝒞^1O game);
     write docs/referee-2/R2-N5-SCOPE.md.
   - Oink: `ls tools/oink/build` -> absent; must run scripts/setup_oink.sh in this container.
3. GAPS rows. `grep -n 'G-N5-TIME\|REFEREE-2' docs/GAPS.md`: REFEREE-2 owns no row. Relevant: G-N5-TIME | major | L-NEW | open (docs/GAPS.md:11);
   its last update (10:37Z) records R33 landed and "lane (unrefereed) box 36: scope runs per phase and ¬H1 fallbacks polynomial in (T, f, X)";
   that is P-N5-SCOPE (SCOPE-COUNT, NH1-FB). Open there: (L1) (NJB / RISE-LAST), out-of-SN fallbacks (OUT-POLY CONJECTURE), ¬H1 SN states, f per phase.
4. Owner rulings verbatim (docs/DECISIONS.md), status from docs/DECISIONS-INDEX.md (`grep -n` on both):
   - D1 (index line 5: active), DECISIONS.md:7-8:
     > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
     > Never downgrade the referee to save money.
   - D15 (index line 26: active), DECISIONS.md:278:
     > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
   - D18 (index line 32: active), DECISIONS.md:333:
     > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
5. Trap found: "merge trunk with a merge commit" is NOT what a plain `git merge` does here. After the ff to 8681e3f2 the branch was 0 ahead
   of trunk, so `git merge` fast-forwarded silently (HEAD = 8998ee6d, no merge commit). I reset the LOCAL, unpushed ref back to 8681e3f2
   (`git reset --hard 8681e3f2`; nothing pushed was touched) and merged with `--no-ff` (63ff0909). Use `--no-ff` whenever the branch is 0 ahead.
   Also (independence): `git log origin/claude/referee -- docs/referee/R-N5-SCOPE.md` -> empty, and `ls docs/referee/ | grep -i scope` -> empty;
   REFEREE's report does not exist yet. I will not open docs/referee/ or notes/REFEREE.md until R2-N5-SCOPE.md is pushed.

## HANDOVER (successor 7, session_01CE1xQNfGUgtJg9A7SWAkuE, Opus 5.5 under D15; written 2026-10-25 10:33Z by date -u; context ~460k; Lead 10:31Z: PARK)
Branch claude/referee-2, merged with trunk at each packet. REFEREE-2 owns no docs/GAPS.md rows. PARKED after this commit.
### DONE (every report docs/referee-2/<name>.md; every verdict "(Opus 5.5, D15)")
| packet | object (sha1) @ pin | report SHA | §C / addenda SHA | outcome |
| --- | --- | --- | --- | --- |
| handover check | — | 8e3e6188 / de9ff970 | — | Lead 5/5 |
| P-N5-FRZ | docs/new/P-N5-FRZ-box34.md 39df373c @ 25fda0f | 20a73ca1 | §C f546b43c | all SIGN; X-RUN SIGN WITH GAPS G-FRZ-1 (= FRZ-3); N-FRZ-1..4; joint 6-row map; P^c label aligned to REFEREE (FRZ-1/2) |
| P-N5-FBW §C | (successor 6's report 25962855) | — | bc2e7b72 | no verdict differs; FBW-1 CONFIRMED (H1 not H2) |
| P-N5-L2 | docs/new/P-N5-L2-box34.md cbea0739 @ 04b3f48 | 388caf6c | §C 21429c91 | all SIGN; L2-1 = N-L2-1; L2-2 (REFEREE only) accepted; §8 (2) restart occurs (j5_n16) |
| P-N5-NJB | docs/si/P-N5-NJB-box9.md f43a8823 @ a7d85b3 | 45eae593 | §C 21429c91, e65cbcdd, §C.3a 16d27d1c | joint: literal MINSET (c) NOT signed (G-NJB-1, REFEREE accepted), survivor (c) signed; ENT-SHAPE (5) NOT signed (NJB-2; my N-NJB-1 withdrawn, assumed z ∈ F_{k0}), (5′) signed; NJB-1 accepted |
| P-N5-TOG | docs/new/P-N5-TOG-box35.md 7dfda8c8 @ d3daae1 | faabe716 (+881e288a) | Addendum A 16d27d1c; §C (this commit) | all SIGN; X-SN-PHASE SIGN WITH GAPS G-TOG-1 = TOG-1 (occurs on SPEC trace: b4_cyc6_0 0->1), N-TOG-1 = TOG-2; no verdict differs |
### IN FLIGHT
None. Next packet P-N5-SCOPE (L-NEW 16) not ready; successor takes it.
### NEEDS
- Lead: route the joint fixes lines (FRZ rows 4-5 to L-NEW; NJB rows 1-2 to L-SI 5; TOG rows 1-2 to L-NEW 15) if not yet done.
### Things only I know
- Tools added this session (own code, chained on my lane's R2-N5-RE/re_check.py; each dir has run_all.sh, logs/, climb/, totals_*.txt):
  - R2-N5-FRZ/frz_check.py: own N5 run_n5 (S4a = ANY arena optimum: deterministic switch-all SI, or --rand random-subset SI + random
    value-preserving re-choices; S4b Odd pointwise best; S4c as SPEC), analyse() (Xi, W, H1-H3, (h), r, R/Rbar/F, gates, MF), checks for
    FRZ (Fact 0, ARENA, Steps 1-2, P^c exhaustive n <= 10 / sampled, FREEZE, RATCHET, BLOCK, X-RUN sub-counts, SUB). frz_climb.py (mutate,
    ok, dump reused by all later climbs), oink_xcheck.py (468/468 vs Oink zlk), h2need.py. totals.py (shared). FRZ_WINF env = mutation test.
  - R2-N5-L2/l2_check.py (+ l2_climb.py, restart_probe.py); R2-N5-NJB/njb_check.py (scope runs, blocks, MINSET survivor + literal,
    NORF, ENT) (+ njb_climb.py, entp_probe.py); R2-N5-TOG/tog_check.py (+ tog_climb.py, xsn_exit_probe.py, xsn_exit_spec.py);
    R2-N5-FBW/fbw1_probe.py.
  - My N5 differs from SPEC only in S4a's optimum choice: data from it must be attributed as "my N5". SPEC-trace data: only via
    re_check.n5_spec (imports n5.py read-only) and only when the Lead asks (done once, xsn_exit_spec.py, Lead 10:06Z).
- Recurring traps seen this session:
  - The same boundary transition (from an SN prefix's last state) was missed three times by the lanes (FRZ-3, X-RUN′ text, TOG-1): any
    count "with both ends in P" used for releases or X_SN needs +1 per run (closed each time by slack ≥ 1 in X-RUN's count).
  - A statement whose defining set is nonempty by a sibling clause (MINSET (c) vs (a)) can secretly assert the conjecture; read every
    "iff X = ∅" against the clause that makes X nonempty.
  - "No leave" facts start at k0+1, never at the fallback k0 itself (NJB-2; my N-NJB-1 error).
  - Citations of R29 lemmas need the phase-key transfer check ((λ_Ξ, λ_U, τ) -> (λ_Ξ, τ)); I missed it once (FRZ row 6).
  - Literal readings "In a phase: every state k with … at k+1" must be in-phase (L2-2, missed by me).
  - Background jobs > 30 min are killed: give run_in_background a long timeout (5400000).
  - Local branch is stale at container start (77f9cf71 twice): fetch, ff to origin/claude/referee-2, merge trunk.
- Oink built in this container (scripts/setup_oink.sh, 8fbf0a7); a fresh container must rebuild it.

## Handover check (successor 7, session_01CE1xQNfGUgtJg9A7SWAkuE, Opus 5.5 under D15/L37; 2026-10-25 07:00Z by date -u)
Predecessor successor 6 session_01H9qTdDhPBiSG4S7P1SkFjD. Correction at push time: its handover DID land (320e4b9d, seen on a second
`git fetch` when push.sh was rejected); merged below, and its HANDOVER section is the handover.
Measured from the repository (commands named). Written here, not in docs/agents/ (Lead-owned), per the Lead's 07:04Z brief.

1. Branch, head, distance to trunk.
   - `git rev-parse HEAD origin/claude/referee-2` after `git fetch origin claude/referee-2 claude/vibrant-johnson-nxvvxo`:
     local 77f9cf71 (STALE again), origin 25962855 (succ. 6's R2-N5-FBW). `git merge --ff-only origin/claude/referee-2` -> 25962855.
   - `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 2 ahead, 34 behind (trunk b0dd1616).
     Merged trunk with a merge commit ee25bcec -> 3 ahead, 0 behind; this notebook commit adds one more.
2. Open work, next step of each.
   - Task 1 (after GO): independent review of P-N5-FRZ, docs/new/P-N5-FRZ-box34.md. `sha1sum` -> 39df373c17d91f942ad2cb15244cd779ca7abda1
     (matches the pin); last change edbccb69 (`git log -- <file>`); f10d381 is an ancestor of HEAD (`git merge-base --is-ancestor`).
     Pin check: the file is ABSENT at f10d381 (`git cat-file -e f10d381:docs/new/P-N5-FRZ-box34.md` -> 128); f10d381 is an ancestor of
     the trunk pin commit 25fda0f3 ("Lead: P-N5-FRZ pinned"), where the blob equals HEAD's (67a871c7). So the object is at 25fda0f or later.
     Fixes file docs/new/P-N5-FRZ-fixes-box34.md sha1 168de464adab5c56945bc5587f4f0ad3262a1fcd (read only after judging the packet).
     Next step: read the packet + SPEC S1-S5 + RESULTS R17-R30, build R2-N5-FRZ/ on R2-N5-SN/CLS/FBW code (one-Odd-choice assert), run
     packet instances, library sweep, random, climbs on long r <= l (h)-windows; write docs/referee-2/R2-N5-FRZ.md.
   - Task 2 (after FRZ pushed): §C for P-N5-FBW (vs docs/referee/R-N5-FBW.md) and §C for P-N5-FRZ (vs R-N5-FRZ.md + Addendum).
   - Oink was NOT built in this container (`ls tools/oink/build` absent); scripts/setup_oink.sh started.
3. GAPS rows. `grep -n REFEREE-2 docs/GAPS.md`: REFEREE-2 owns none. Relevant: G-N5-TIME | major | L-NEW | open (docs/GAPS.md:11):
   N5 makes polynomially many iterations; P-N5-FRZ (X-RUN: O((d_o+1)n^3) crossings per fallback-free run with an H1 SN prefix) is
   under this row. G-N5-TERM closed (R15).
4. Owner rulings verbatim (docs/DECISIONS.md), index status from docs/DECISIONS-INDEX.md:
   - D1 (index: active), DECISIONS.md:7-8:
     > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
     > Never downgrade the referee to save money.
   - D15 (index: active; L37 active), DECISIONS.md:278:
     > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
   - D18 (index: active; L40 active), DECISIONS.md:333:
     > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
5. Trap found this session: independence exposure. `ls docs/referee/` after the trunk merge shows R-N5-FRZ.md (3a520ce7) and
   R-N5-FBW.md already on my tree, before my FRZ report exists. Check: I do not open docs/referee/R-N5-FRZ.md or notes/REFEREE.md
   until R2-N5-FRZ.md is pushed (only `ls`/`git log` on them so far). Also the container branch was stale again (77f9cf71):
   always compare `git rev-parse HEAD origin/claude/referee-2` after fetch.

## Resume point (successor 7, session_01CE1xQNfGUgtJg9A7SWAkuE, Opus 5.5 under D15; 2026-10-25 08:2xZ by date -u)
- Handover check de9ff970 (Lead 07:13Z: 5/5, GO). Pin of P-N5-FRZ is trunk 25fda0f (not f10d381; Lead confirmed).
- P-N5-FRZ (docs/new/P-N5-FRZ-box34.md sha1 39df373c): report docs/referee-2/R2-N5-FRZ.md. NL-MF, Fact 0, ARENA (N-FRZ-1 citation),
  P^c_l (N-FRZ-2 = REFEREE FRZ-1, N-FRZ-3 = FRZ-2), FREEZE, RATCHET, BLOCK (vacuous in data), SUB SIGN; X-RUN SIGN WITH GAPS G-FRZ-1
  (= FRZ-3, closed; transition leaving P). Fixes file 168de464 read after verdicts. Tools R2-N5-FRZ/ (frz_check.py on R2-N5-RE/re_check.py,
  own N5 with any arena optimum; oink_xcheck 468/468). 0 violations: 16,434 batch runs, 1,485,828 climb runs. No freeze at l in {-1, bot}.
- §C FBW bc2e7b72 (appended to R2-N5-FBW.md): no verdict differs; FBW-1 CONFIRMED (honest cycle, H1 at k+1; my lane's §3 said H2);
  FBW-2 = N-FBW-1. Probe R2-N5-FBW/fbw1_probe.py (thin: 7 random cases).
- §C FRZ (appended to R2-N5-FRZ.md): only the P^c label differs (adopted REFEREE's SIGNED WITH GAPS FRZ-1/2); FRZ-1..3 = N-FRZ-2/3, G-FRZ-1;
  rows 4-5 mine (N-FRZ-1 ARENA citation, N-FRZ-4 definitions); row 6 REFEREE's NL phase-key transfer ACCEPTED (my miss).
  Asked: did REFEREE's 30 BLOCK runs contain any S4a leave?
- Lead 08:41Z: FRZ §C merged; next P-N5-L2, P-N5-NJB, P-N5-TOG, each independent, report + message after each.
- P-N5-L2 (cbea0739 @ 04b3f48): R2-N5-L2.md all SIGN (N-L2-1 tau(o)=o wording, N-L2-2 X-RUN applied to H1 runs, N-L2-3 FREEZE' conclusion
  never exercised). §8 DATA: open item (2) restart of (h) by a fallback OCCURS (j5_n16 --rand, fallback 6->7). Tools R2-N5-L2/.
- P-N5-NJB (f43a8823 @ a7d85b3): R2-N5-NJB.md. All SIGN; MINSET (c) SIGN WITH GAPS G-NJB-1 (literal Mn_{t+1} never empty by (a) =>
  literal (c) = NJB; proof gives survivor form Mn_t ∩ F_{t+1}); N-NJB-1 (ENT-SHAPE (5): fallback k0 does not move Xi(z)). Data: D_M = 0,
  no fallback after a rise (Corollary, ENT-SHAPE vacuous). Tools R2-N5-NJB/.
- P-N5-TOG (7dfda8c8 @ d3daae1): R2-N5-TOG.md. All SIGN; X-SN-PHASE SIGN WITH GAPS G-TOG-1 (SN-prefix exit crossing, occurs: 310 batch;
  bound survives by X-RUN slack); N-TOG-1 (§11 -> §7). Tools R2-N5-TOG/.
- §C L2 (appended to R2-N5-L2.md): no substantive difference; L2-1 = N-L2-1; L2-2 accepted (I missed it: H1-INT (b) in-phase only).
- §C NJB (appended to R2-N5-NJB.md): ENT-SHAPE (5) -> NOT SIGNED as stated (REFEREE NJB-2 right; my N-NJB-1 assumed z ∈ F_{k0}, unproved;
  withdrawn); (5′) signed. MINSET (c): kept G-NJB-1 (literal Mn_{t+1} never empty), asked REFEREE to reconcile; NJB-1 accepted.
- NEXT: §C TOG when REFEREE's TOG report lands; else wait for the Lead.
- Trap: background jobs over 30 min are killed (first climb wave lost its second half). Give run_in_background a long timeout.

## HANDOVER (successor 6, Opus 5.5 under D15; written 2026-10-25 ~06:1xZ; context ~575k; Lead 06:08Z: finish FBW, hand over, park)
Branch claude/referee-2, merged with trunk at each packet pin. REFEREE-2 owns no docs/GAPS.md rows. PARKED.
### DONE (every report is docs/referee-2/<name>.md; every verdict "(Opus 5.5, D15)")
| packet | object (sha1) @ pin | report SHA | §C / addenda SHA | outcome |
| --- | --- | --- | --- | --- |
| handover check | — | 6a27ab9b | — | Lead 5/5 |
| P-N5-OE | docs/new/P-N5-OE-box32.md adeccd89 @ 361d18c | ca6e5bd1 | §C ea6ad672 | U-loc, OE, OX all SIGN (notes N-OE-1..3); R28 |
| P-N5-CLS | docs/si/P-N5-CLS-box8.md 5bbfd872 @ 486107a | ffe10e1b | §C 848839e9 | all SIGN; CLS1 SIGN WITH GAPS (G-CLS-1 citation, closed); R29 |
| P-N5-SN | docs/new/P-N5-SN-box33.md 340d4f29 @ 2c70ef6 | ddbecafc | §A 91d95e84, §C 80d2e457, §B 4c8dcfd0 (fixes §2b at l-new 0883157, e5394445: H1-DROP, H1-KEEP, ABS-COUNT′ SIGN) | all SIGN; ABS-COUNT SIGN WITH GAPS G-SN-1 (closed by §2b except ε⁽⁻¹⁾ and fallback ε) |
| P-N5-FBW | docs/si/P-N5-FBW-box9.md 88337bd6 @ e69772b | 25962855 | §C NOT YET (REFEREE's R-N5-FBW not seen) | P-OPT VALID (G-1OA-6 is about σ_{k+1}); FBW, FBW-S, CLS2, FLAT-ALL, STRETCH (N-FBW-1: "k < e" → "k ≤ e"), PL, PL-S all SIGN |
### IN FLIGHT
- R2-N5-FBW §C: write when the Lead says R-N5-FBW is on trunk (do not read it before; my report 25962855 is pushed).
### NEEDS
- Lead: R-N5-FBW → §C (successor 7 may write it from my report).
- Lead: the fixes file version with §2b (l-new 0883157) and L-RED's epsseg_cex_n16 were NOT on trunk when I reviewed them (§B).
- P-N5-FRZ (docs/new/P-N5-FRZ-box34.md, sha1 39df373c…, pin 25fda0f, L-NEW succ. 14) goes to successor 7 (Lead 06:08Z). Lead's hints:
  climb FREEZE's "through fallbacks" and X-RUN's count hardest.
### Things only I know
- Tools added this session (each dir has run_all.sh, logs/, climb/, totals.py; run from the dir):
  - R2-N5-OE/oe_check.py (U-loc smallest L, OE, CAP-1 full minimiser, OX), oe_climb.py.
  - R2-N5-CLS/cls_check.py (C5-C7 random triples, TRANSFER, CN, OFFGATE, Fact R, CLU, FBL strong form, NL at every admissible L, CLS1 with
    the (A_j) chain); cls_climb.py. cls_check.prefix(E, pi, x) = pi ⊕ x in si.py representation.
  - R2-N5-SN/sn_check.py (OR, TC-SPLIT, R-STICK, SN-PREFIX, H3H2, LEAVE, ABS-COUNT both forms, WK, odd-mode choice rule, ABS-L),
    sn_climb.py; h1_check.py / h1_climb.py (H1-DROP divergence claim, H1-KEEP, ABS-COUNT′).
  - R2-N5-FBW/fbw_check.py (P-OPT by re-running S4a's arena and all single switches, FBW, FBW-S, CLS2, FLAT-ALL, STRETCH with k ≤ e, PL,
    PL-S), fbw_climb.py (FIT=dirty on 𝒞^1O, FIT=fbw on general games with its own mutation).
- Library sweep idiom (≈245-252 files): every experiments/**/*.pg with exactly one Odd vertex of out-degree > 1 (set of successors), n ≤ 64,
  plus named instance dirs at larger n; 3 starts per file. Phase key used throughout: (λ_Ξ, τ).
- Recurring traps seen this session:
  - Counters that only count a sub-case (my first OE tie-move counter counted only E_k = ⊥; corrected in R2-N5-OE §C). Name each
    counter by exactly what it counts.
  - Packet "ends ≤ d_o − 1"-type counting: check what holds at the LAST state of the run (G-SN-1).
  - Citations of FBL at "a stretch of length 1": only the u* ≠ none strong gate form is statewise (G-CLS-1).
  - Fixes-file objects can be on the lane branch but not on trunk: verify the sha1 and say where the object lives.
  - Stamp: take date -u immediately before writing (my 01:34Z message was really 01:37Z).
- Oink is built in this container (scripts/setup_oink.sh); a fresh container must rebuild it.

## Resume point (successor 6, Opus 5.5 under D15; 2026-10-25 01:5xZ by date -u)
- Handover check 6a27ab9b (Lead 01:44Z: 5/5, GO). Lead: P-N5-SO NOT re-reviewed (succ. 5's R2-N5-LP §8 stands).
- P-N5-OE (docs/new/P-N5-OE-box32.md sha1 adeccd89, pin 361d18c): report docs/referee-2/R2-N5-OE.md. U-loc, OE, OX (i)-(v) all SIGN;
  notes N-OE-1 (in-particular sentence vs level-⊥ tie move), N-OE-2 (step 3 one-line reason), N-OE-3 (phase-key transfer of FB/J1/CAP-1/TC).
  Tools R2-N5-OE/ (oe_check.py, oe_climb.py, run_all.sh). 0 violations; CAP-1 non-minimiser at λ(o)=o seen (420), never used by OE.
  §C ea6ad672 vs R-N5-OE (5e98e33 + 696b08c): no disagreement; joint gap map 5 rows (OE-1=N-OE-1, OE-2, OE-3+N-OE-2, N-OE-3, OX-1)
  + note 3.6. Corrections in §C: tie moves 2 library / 5 random (my first counter only had E_k = ⊥); 220 vs 234 = lane run date.
  Lead 02:25Z: review closed, R28 drafted (CHECKER C37). PARKED 02:24Z.
- P-N5-CLS (docs/si/P-N5-CLS-box8.md sha1 5bbfd872, pin 486107a; Lead 02:40Z): report docs/referee-2/R2-N5-CLS.md (02:43Z).
  All SIGN except CLS1 + Corollary SIGN WITH GAPS (G-CLS-1 citation: FBL strong gate form at the state alone, R2-N5-XA §2; closed).
  Notes N-CLS-1 (OFF's honest R̄ = (σ,τ) R̄), N-CLS-2 ((h): θ = w ⟺ EQ). Tools R2-N5-CLS/ (cls_check.py, cls_climb.py). 0 violations.
  §C 848839e9 vs R-N5-CLS (a0b92ec): no disagreement; 5-row gap map (CLS-1, CLS-2, CLS-3 = G-CLS-1, CLS-4, N-CLS-1).
  Lead 03:08Z: review closed (REFEREE 8af6347 adopts my row-3 form); lands as R29 after L-SI's fixes file.
- P-N5-SN (docs/new/P-N5-SN-box33.md sha1 340d4f29, pin 2c70ef6; Lead 03:42Z): report docs/referee-2/R2-N5-SN.md (03:50Z).
  OR, TC-SPLIT, R-STICK, SN-PREFIX, H3H2, LEAVE, WK (N-SN-1) SIGN; ABS-COUNT SIGN WITH GAPS (G-SN-1: proof gives d_o, not d_o − 1, per run;
  fallback ε uncounted per phase; packet form CONJECTURE, 0 excess in data/climbs); ABS-L conditional, met on R29; WM transfer VALID.
  Tools R2-N5-SN/ (sn_check.py, sn_climb.py). §A (L-RED probes: epsseg tight; N = d_o only at a phase exit). §C vs R-N5-SN (59a886d): no
  disagreement; 4-row gap map (SN-1 = G-SN-1 (a), SN-2 = G-SN-1 (b), SN-3 accepted, N-SN-1). Waiting for the Lead. PARKED 03:10Z; next packet when frozen.
- Oink built in this container (setup_oink.sh).

- P-N5-SN §B (fixes §2b, l-new 0883157 e5394445): H1-DROP, H1-KEEP, ABS-COUNT′ SIGN (4c8dcfd0).
- P-N5-FBW (docs/si/P-N5-FBW-box9.md sha1 88337bd6, pin e69772b; Lead 05:53Z): report docs/referee-2/R2-N5-FBW.md (06:05Z). P-OPT VALID
  (G-1OA-6 is about σ_{k+1}); FBW, FBW-S, CLS2, FLAT-ALL, STRETCH (N-FBW-1: k ≤ e), PL, PL-S all SIGN. Tools R2-N5-FBW/. 0 violations;
  PL (b), (c) vacuous (0 dirty intervals). NEXT: §C after REFEREE's R-N5-FBW; then P-N5-FRZ (L-NEW 14).

## HANDOVER (successor 5, session_01VbMVVvPYCY47wY5MbtLG8w, Opus 5.5 under D15; written 2026-10-25 01:23Z by date -u; context ~660k, over the line)
Branch claude/referee-2, merged with trunk at each packet. REFEREE-2 owns no docs/GAPS.md rows. PARKED.

### DONE (every report is docs/referee-2/<name>.md; every verdict labelled "(Opus 5.5, D15)")
| packet | object (sha1) @ pin | report SHA | §C SHA | outcome |
| --- | --- | --- | --- | --- |
| handover check | — | 1b394dfc | — | Lead 5/5 |
| P-N5-U1 | docs/new/P-N5-U1-box31.md eb90788d @ eee0d8a | 28ddf6fa | 3d68a030 (+ stamp cab4e7da) | U1, WC SIGN; CASC SIGN WITH GAPS (C-1..C-3 accepted); TB, R SIGN WITH GAPS (G-TB-1, G-R-1, G-R-2 closed); N-U1-3 closed via R15 (a) in G_τ |
| P-N5-FB | docs/si/P-N5-FB-box7.md 9ece9994 @ 348393b | 7699593d | eb10cf74 | FB, Corollary, CAP SIGN WITH GAPS (G-FB-1..4); rest SIGN; JUMP-EQ FALSE confirmed; adopted REFEREE's full-minimiser proof (CAP-1) |
| P-N5-U23 | docs/new/P-N5-U23-box31.md ee3e5d1e @ 7666336 | 07b22b07 | 5e24010a | CASC-U2 SIGN; CASC-U3 (ii) SIGN WITH GAPS (G-U23-1 = U3-1); READING note N-U23-2 = R-1 (closure accepted); u2flat_n32: CASC-U2 bound attained |
| P-N5-LP | docs/new/P-N5-LP-box32.md d2c8121a @ bc42f2c | 4949d6c9 | caee2aec | DF NOT SIGNED (FALSE; my df_cex.pg n 5); DF′ SIGN; WAKE SIGN WITH GAPS (G-LP-1); HI Consequence unproved (G-LP-2); rest SIGN |
| P-N5-SO | docs/new/P-N5-SO-box32.md deb5ee44 @ 1ef02bb | ba67f410 (R2-N5-LP.md §8) | caee2aec (in the same §C) | TH SIGN; SO SIGN WITH GAPS (G-SO-1); XJ SIGN WITH GAPS (N-SO-2 = XJ-1). NOTE: the Lead's 01:10Z message assigned SO to successor 6, but it reached me (01:19Z) after this review was pushed (01:2xZ). The review exists and stands; the Lead decides whether successor 6 redoes it independently |

### IN FLIGHT
None.

### NEEDS
- Lead: route to the lanes' fixes files: DF → DF′ (proof R2-N5-LP §4.3), G-LP-1, G-LP-2, N-LP-1, G-SO-1, N-SO-1..3 (L-NEW);
  G-U23-1 / N-U23-2 (L-NEW); G-FB-1..4 (L-SI). Decide whether P-N5-SO needs a fresh independent second review.

### Things only I know
- Tools (own code; each directory has run_all.sh, logs/, often climb/, and totals.py):
  - R2-N5-U1/u1_check.py: an instrumented VJ00 procedure (vj_eval) asserted equal to si.py's evaluate; Lemma R checks; TB key-min /
    step-2 checks; pieces; CASC; U1; WC.
    - spec_run() is the SPEC N5 loop with per-transition arena records, cross-checked against re_check.n5_spec.
    - u1_climb.py with FIT=b/c.
  - R2-N5-FB/fb_check.py: general-game and 𝒞^1O N5 runner (run_n5 = n5.py loop, asserted equal to n5.run).
    - analyse() gives Xi, sbar, lam, lamU, H, gate levels gl, M, W, Rbar. lev()/coarse() implement the packet's levels.
    - Also the LINK checks: Ξ = Θ_H, and σ̄ minimiser except at own cycle nodes (FIX 2 DFS).
    - fb_climb.py, a_check.py.
  - R2-N5-U23/u23_check.py (U2/U3/U23 stretches, kinds, events, sub-runs), u23_climb.py, theta_notH1.py, theta_shape.py.
  - R2-N5-LP/lp_check.py (used level L_k, Lemma U/HI/UL/GR/NU, Theorem LP, DF / DF′, BAND, WAKE, LP′), df_probe.py, df_find.py
    (writes instances/df_cex.pg), so_check.py, so_climb.py.
- Library sweep idiom: every experiments/**/*.pg with exactly one Odd choice vertex and n ≤ 64 (about 228-234 files). See
  R2-N5-LP/run_all.sh.
- Never write the lane's experiments/*/logs. When re-running a lane's run_all.sh, redirect into the scratchpad and diff against the
  committed logs (done for P-N5-FB: 12/12 byte-identical).
- Recurring traps:
  - Set-valued ⊕ is NOT monotone when the vertex is in one path set but not the other (TB-1 (b)). Every "⊕ keeps strictness" in a packet
    needs the simple-path / λ-fixed argument.
  - SPEC's σ̄ at an own cycle node is FIX 2's DFS choice, not VJ00's minimiser. VJ00 Lemma 5.8 2 ⇒ 3 ⇒ 1 is FALSE there (R15 side
    finding). Any citation of "maximum ⇒ no improvement" or "σ̄ minimises" needs "not its own cycle node" (DF, CAP-1).
  - R21-R23 results are signed on 𝒞^1O with R22's phase key (λ_Ξ, λ_U, τ). The LP / SO / FB packets use the coarser (λ_Ξ, τ) phase.
    Check each transferred citation.
  - Stamps: take date -u immediately before writing. I wrote one stamp ahead once (R2-N5-U1 §C, fixed in cab4e7da).
- Oink is built in this container (scripts/setup_oink.sh); a fresh container must rebuild it.

## Archive: the notebook before this handover (verbatim)

## Resume point (successor 5, session_01VbMVVvPYCY47wY5MbtLG8w, Opus 5.5 under D15; 2026-10-24 21:47Z by date -u)
- Handover check 1b394dfc (Lead 21:2xZ: 5/5, GO).
- P-N5-U1 (docs/new/P-N5-U1-box31.md sha1 eb90788d…, trunk eee0d8a): report docs/referee-2/R2-N5-U1.md.
  - Verdicts: Theorem U1 SIGN; CASC SIGN; TB SIGN WITH GAPS (G-TB-1: step 2's Bellman inequality when x lies on σ_k(x)'s W*-play;
    closed by an (F1)-only case proof); Lemma R SIGN WITH GAPS (G-R-1: invariant exception x = u; G-R-2: "(c, P)-optimal" form false,
    instance tb_general seed 532 #13 edge 11→13; full-equality form true); WC SIGN; §6 READING correct with N-U1-3 (EQ-state fallbacks
    in ¬H1∧¬H2 intervals feed WC's f_I).
  - VJ00 re-downloaded and opened (sha256 485a12de…): §6 Prop 6.1 clause 1 is existence only.
  - Tools: docs/referee-2/R2-N5-U1/ (u1_check.py, tb_general.py, tb_arena.py, u1_climb.py, totals.py, run_all.sh).
  - Data: batch 11,910 runs + 20,000 arenas; climbs 70,400 runs; 0 violations. Thin spots: K = 0 everywhere, no U1 fallback, CASC never
    tight.
- Oink built in this container (scripts/setup_oink.sh, 8fbf0a7).
- Report pushed 28ddf6fa. §C (21:56Z; 3d68a030) vs REFEREE R-N5-U1 (257fa4c): no disagreement of substance. Accepted C-1/C-2/C-3,
  so CASC is now SIGN WITH GAPS; G-TB-1 = TB-1 (TB-1 (b) corrects my "⊕ monotone" wording); G-R-2 = R-1; R-2 = my VJ00 finding.
  N-U1-3 closed by R15 (a) applied in G_τ at EQ states. Withdrew "§6 uses only signed results". Stamp fix: §C header said 21:58Z,
  true 21:53Z. PARKED.
- P-N5-FB (docs/si/P-N5-FB-box7.md sha1 9ece9994…, trunk 348393b; Lead 22:3xZ): report docs/referee-2/R2-N5-FB.md (22:47Z).
  - FB SIGN WITH GAPS (G-FB-1: M<∞ needs the best-target line; G-FB-2: R21 (c) signed on 𝒞^1O only, transfers via S4c + FIX 3).
  - Corollary SIGN WITH GAPS (G-FB-3: WM signed on 𝒞^1O; (F1) in G_τ transfers it).
  - (T), SI (a) + converse, TAME, MONO, NOINF, J1, OFF, Remark SIGN.
  - CAP SIGN WITH GAPS (G-FB-4: SPEC σ̄ = FIX 2 DFS at own-cycle-node Odd vertices is not VJ00's minimiser, 1,228 cases; coarse
    minimality suffices).
  - (JUMP-EQ) FALSE confirmed at x31_rx32 53→54; A confirmed (201/201).
  - Lane logs reproduced byte-identically.
  - Tools: docs/referee-2/R2-N5-FB/ (fb_check.py, a_check.py, fb_climb.py).
  - §C (22:55Z) vs REFEREE R-N5-FB (eb1ec3c): no disagreement. FB-2 accepted; CAP-1 = G-FB-4, and REFEREE's case split
    (full minimiser at non-cycle nodes, proved) is adopted; G-FB-2/3 mine only. PARKED.
- P-N5-U23 (docs/new/P-N5-U23-box31.md sha1 ee3e5d1e…, trunk 7666336; Lead 23:37Z): report docs/referee-2/R2-N5-U23.md (23:47Z).
  - CASC-U2 + Corollary SIGN; CASC-U3 kinds/events, (i), (iii), Corollary SIGN.
  - (ii) SIGN WITH GAPS (G-U23-1: T = max(L_B − 1, 0); L_B undefined for empty kind B).
  - Note N-U23-2: θ-changes under ¬H1 (5 seen, no F-change) are missing from §3's READING inputs.
  - Data: 0 U2 W-flat switches and 0 kind-B switches anywhere, so those parts are vacuous in data; 34,230 kind-A switches checked.
  - Tools: docs/referee-2/R2-N5-U23/.
  - §C (2026-10-25 00:00Z) vs REFEREE R-N5-U23 (7ffbd9f): no disagreement. U3-1 = G-U23-1 (identical bound); U3-2/U3-3
    accepted; R-1 = N-U23-2, closure (θ = (c_θ, ∅, d), d monotone) re-checked. u2flat_n32: 7 U2 W-flat switches, bound attained, 0 violations. PARKED.
- P-N5-LP (docs/new/P-N5-LP-box32.md sha1 d2c8121a…, trunk bc42f2c; Lead 00:47Z): report docs/referee-2/R2-N5-LP.md (00:56Z).
  - §1 U, HI, UL, GR, NU SIGN (G-LP-2: HI's Consequence unproved, unused); §2 LP SIGN (N-LP-1).
  - §3 DF NOT SIGNED as stated: VJ00 Lemma 5.8 2⇒3⇒1 is false at cycle nodes (R15 side finding); counterexample
    R2-N5-LP/instances/df_cex.pg (n 5, sha1 0a98e1b7). DF′ (λ(y) ≠ y) SIGN via R15 (a)/(b) + F1 + R19 (a).
  - BAND SIGN; WAKE SIGN WITH GAPS (G-LP-1: cite DF′); §4 LP′ SIGN (it uses neither DF nor WAKE).
  - Tools: R2-N5-LP/lp_check.py, df_probe.py, df_find.py. NEXT: §C after REFEREE's report.
- P-N5-SO (docs/new/P-N5-SO-box32.md sha1 deb5ee44…, trunk 1ef02bb; Lead 01:00Z): combined into R2-N5-LP.md §8 (01:15Z).
  - TH SIGN (N-SO-1: F1° on the coarser phase transfers); SO SIGN WITH GAPS (G-SO-1: ⊕ strictness via (SG) + simple prefixes);
    XJ SIGN WITH GAPS (N-SO-2: f = O(d_o n³(1+X))).
  - Climbs 12,000 runs: S_o − d_o(Θ+1) ≤ −1, J − S_o ≤ 0. Tools so_check.py, so_climb.py.

## HANDOVER (successor 4, session_01DDRfmJkBTC5uu5q62T2Dme, Opus 5.5 under D15; written 2026-10-24 21:05Z by date -u; context ~485k)
Branch claude/referee-2, at trunk claude/vibrant-johnson-nxvvxo plus my commits (0 behind / 3 ahead at 21:03Z, before this commit).
REFEREE-2 owns no docs/GAPS.md rows (G-N5-TIME names "referees later").

### DONE (this session; every report is docs/referee-2/<name>.md; every verdict labelled "(Opus 5.5, D15)")
| packet | object (sha1) @ pin | report | report SHA | §C SHA (and later addenda) | outcome | landed |
| --- | --- | --- | --- | --- | --- | --- |
| P-N5-RE | docs/new/P-N5-RE-box26.md 8dba4576 @ 52c7261 | R2-N5-RE | 3ee7b737 (+ stamp c66da44a) | §C dd5aaa2c; §A 9d3f1fb6 | G, Wo, RM SIGN; RE SIGN without (NC) via (SG); PIECE SIGN WITH GAPS (G-RE-3 closed); N-RE-3 withdrawn (§A) | R19 |
| P-N5-XA | docs/new/P-N5-XA-box27.md 832d0da2 @ b70aa59 | R2-N5-XA | 9d3f1fb6 | §C 4df15e63 (+ stamps a8c73512, 99998aad); §C2 38af0dff | C, CR, XA SIGN; FBL SIGN for u*≠none, unproved u*=none (G-XA-1 (b), mine, accepted by REFEREE); FBF SIGN; Corollary SIGN via §C5 | R20 |
| P-N5-X | docs/new/P-N5-X-box28.md b21d2d06 @ afc88b0 | R2-N5-X | 059f492a | §C 3a581a5b | all SIGN; Theorem X SIGN WITH GAPS: G-X-1 = R19 (f) θ-free count (my N-RE-4 was incomplete), closed by Lemma TF / REFEREE X-1; R19 (f) clarification wording is mine (R21 (i)) | R21 |
| P-N5-NH | docs/new/P-N5-NH-box30.md 382c5143 @ c7981ee | R2-N5-NH | 48da84a1 | §C 8621a847 (+ stamp e7578fe6) | TC, F1°, Corollary SIGN; P3′ step 1 SIGN WITH GAPS (G-NH-1 = P3-1, closed); reduction READING ok; withdrew my §1.3 converse (NH-2) | R22 |
| P-N5-Z | docs/si/P-N5-Z-box5.md a027638f @ fba7177 | R2-N5-Z | 1a5854b3 | §C fde04482 | all SIGN; N-Z-1 = Z-1 ('±' breaks runs); N-Z-2 s_rt32_final not 𝒞^1O | pending (fixes docs/si/P-N5-Z-fixes-box5.md) |
| tooling | — | — | 04611c5e | — | every N5 checker asserts exactly one Odd choice vertex | — |

### IN FLIGHT
None. Parked after R2-N5-Z §C (fde04482).

### NEEDS
- Lead: route N-Z-1 and N-Z-2 to docs/si/P-N5-Z-fixes-box5.md (the Lead said it will relay).
- NEXT for my successor: packet P-N5-U1, docs/new/P-N5-U1-box31.md, sha1 eb90788d…, pin trunk eee0d8a. Do not read
  docs/referee/R-N5-U1.md until your own report is pushed.

### Things only I know
- Tools (own code; no lane script imported except n5.py's functions in "spec" mode, which only produce N5's state sequence):
  - docs/referee-2/R2-N5-RE/re_check.py: the base library.
    - Game, play values (c, P, ℓ) by following plays, the VJ00/SPEC S1 key.
    - Ξ = pointwise minimum over o's exits (asserted attained by one exit); U = Even's one-player optimum by switch-all SI.
    - Iσ, Iτ.
    - Own N5 (n5_own) with RANDOM tie-breaks in S4a, plus random value-preserving re-choices among optima (the lemmas use only (F1),
      so they must hold for every optimum).
    - n5_spec: n5.py's step functions, read-only.
    - analyse() gives per-state Ξ, W, U, R (o included), π, (h), θ, w.
    - rand_game builds o-cyclic 𝒞^1O by construction.
    Its siblings: re_climb.py (mutate() is reused by every later climb), re_notau.py, dump_nc.py, totals.py (sums logs; any key with
    "_max" is a max).
  - R2-N5-XA/xa_check.py (coarse order, throttled stretches, FBL/FBF/CR/XA), xa_climb.py, piece_flatfb.py.
  - R2-N5-X/x_check.py (XW, EQ, FBL-N, NF, F1, F2, TF, PIECE θ-free split, Theorem X bounds, (w, u*)-runs, FB-W), dump_tf.py
    (the G-X-1 instance printer; the Lead re-ran it).
  - R2-N5-NH/nh_check.py (F1°, TC, P3′ with the G-NH-1 probe: 𝓡*_w-arena optimum test and single-switch inequality), nh_climb.py.
  - R2-N5-Z/z_check.py (Step (K), ACT, LOOP, NOFE, NOFL-E, GAP, WM, LV′ incl. the literal-run reading, Corollary Z), dbg_k.py.
  - Each directory has a run_all.sh and logs/ (and climb/). Run each script from its own directory.
- The one-o assert (04611c5e). Every inst path now refuses games without exactly one Odd choice vertex. Before that, the inst paths
  silently took the first one.
  - This bit once: s_rt32_final (Odd choices 14, 28) gave 14 false Step (K) "failures" under SPEC.
  - Out-of-class files in the fleet (Lead 20:5xZ): box21 fts_best24/39, fts_g29/43, fts_ph16; si/orlens s_rt32_final; red/n5inj
    bribe_cex_n15, elimn_cex_n48, frz32, frz40, phase2_pk32/48, returns_rt32/64, wide_h16.
- Oink is built in this container only (scripts/setup_oink.sh); a fresh container must rebuild it before check_sol2.py.
- Lessons.
  - Random 𝒞^1O runs are nearly vacuous for the interesting configurations: θ-equal re-entries, throttled fallbacks, P3′ pieces,
    FB-W evictions. Climbs seeded from the lane's instances are what produce them: tr20_s4 and c12_s54 for RE, wf0_cex_n16 for P3′.
    Say so whenever data is thin.
  - Check every "θ free" or "w free" extension at the COUNT level as well as at the gate level. My own N-RE-4 missed that Ξ on R moves
    with θ (G-X-1).
  - Prove a statement about a single switch before trusting a contraction (G-NH-1): contracted games are not faithful when o's
    continuation runs through R (¬H2).
  - Take `date -u` IMMEDIATELY before writing a stamp. I wrote stamps ahead of the clock three times (R2-N5-RE header, R2-N5-XA §C,
    R2-N5-NH §C) and fixed each in a separate commit.
  - Never pipe push.sh. I always redirected it to scratchpad/pushN.log and printed $?.

## Archive: the notebook before this handover (verbatim)

## Resume point
2026-10-24 20:42Z P-N5-Z (docs/si/P-N5-Z-box5.md sha1 a027638f…, trunk fba7177): docs/referee-2/R2-N5-Z.md. All SIGN: LV' (N-Z-1: runs
must be adjacent among crossing transitions; '±' breaks them), Corollary Z (R21 (g) within hypotheses), NOFE strong, ACT, LOOP, NOFL-E, GAP,
WM, Step (K). N-Z-2: s_rt32_final is NOT C^1O (Odd choices 14, 28); my checker falsely "failed" Step (K) on it before I added the C^1O
guard. Tool R2-N5-Z/z_check.py. Context ~470k.
§C (20:55Z) vs REFEREE R-N5-Z (c818ef2/555cbeb): full agreement; Z-1 = N-Z-1; accepted Z-2 (NOFE from FBL-N (ii)) and Z-3;
class question: X/NH never ran on out-of-class files; all checkers assert one Odd choice (04611c5e). PARKED. Next packet P-N5-U1 (eee0d8a).
Earlier:
2026-10-24 19:49Z P-N5-NH (docs/new/P-N5-NH-box30.md sha1 382c5143…, trunk c7981ee): docs/referee-2/R2-N5-NH.md. TC, F1°, P3' steps 2-3,
Corollary SIGN; P3' step 1 SIGN WITH GAPS (G-NH-1: "S4a optimum restricted to R is an R*_w-arena optimum" unjustified under not-H2,
lambda_W(o)=o; closed: CR needs only B1 single-switch inequality; x not on C_W: real = contracted; x on C_W: vacuous, top of pi_z even
above o would move lambda_W). Reduction READING correct. Tools R2-N5-NH/nh_check.py, nh_climb.py. Context ~440k.
§C (20:01Z; stamp corrected from 20:03Z) vs REFEREE R-N5-NH (78d61b1): full agreement; P3-1 = G-NH-1, same proof; accepted sharper count, NH-2 (SG);
withdrew my §1.3 converse (W-change on R need not be a Xi-change at that vertex). PARKED.
Earlier:
2026-10-24 18:34Z P-N5-X (docs/new/P-N5-X-box28.md sha1 b21d2d06…, trunk afc88b0): docs/referee-2/R2-N5-X.md. F1, NF, XW, EQ, FBL-N, F2,
FB-W SIGN; table agree; Theorem X SIGN WITH GAPS: G-X-1 = R19 (f) "theta free" (my N-RE-4) misses Xi-changes on R from theta (fbref_n48
56->57, R={o}); closed by Lemma TF (theta-change under (h) both ends => Xi-change on F, theta = min over F-exits). Amend R19 (f).
FB-W data vacuous. Tool R2-N5-X/x_check.py; Oink built here (setup_oink.sh). Context ~400k. §C (18:43Z) vs REFEREE R-N5-X (53c0c68): full agreement; X-1=G-X-1 (its proof: H1 at k + Lemma S (a) + R15 (a), shorter than TF);
accepted X-2 (F empty), X-3; X-4=N-X-3. R19-note-X1: confirmed with a wording correction (per-part true for routes, false with Xi on R). PARKED.
Earlier:
2026-10-24 15:33Z P-N5-XA (docs/new/P-N5-XA-box27.md sha1 832d0da2…, trunk b70aa59): docs/referee-2/R2-N5-XA.md. §1, Lemma C, CR, XA SIGN;
FBL SIGN WITH GAPS (G-XA-1: F->R case; for u* != none no F->R gate edge at all (flat => P(w)=A_z=0 => theta >= w unless u*=none); u*=none
statement unproved: (c,z), z in R_k minus R_{k+1}, not excluded); FBF SIGN WITH GAPS (G-XA-2 closed, incl. u*=none via (h) at t+1);
CR's B-fallback vacuous (N-XA-1); XA count <= n-1 per vertex (N-XA-2); Corollary reading sound, add R15 (d) runs (N-XA-3). Tool
R2-N5-XA/xa_check.py (on R2-N5-RE/re_check.py). 0 violations; no XA re-entry occurs in data. Also R2-N5-RE §A: tau-constant not needed
(REFEREE §C3 right), N-RE-3 withdrawn (re_notau.py). §C (15:47Z; stamp corrected from 15:50Z) vs REFEREE R-N5-XA (f39972d, trunk e99a586): XA-1=G-XA-1(a); XA-2=G-XA-2, its best-key repair adopted (+ my (h) base);
accepted XA-3, XA-4 (missed); XA-5 accepted, my 'Corollary sound' withdrawn, closure proposed (pieces pass through leave-free fallbacks: sigma_{k+1}
is another arena optimum). DISAGREEMENT: FBL statement for u*=none (mine: z's route can leave in the same fallback; REFEREE: survives). PARKED.
§C2 (16:06Z) vs REFEREE §C (1123baf, trunk 1494ae1): REFEREE accepted G-XA-1(b): disagreement RESOLVED (FBL unproved for u*=none, joint).
Signed REFEREE §C5 = my C.5 (pieces pass flat fallbacks); Corollary SIGNED (u*!=none): O(n^3) vc/crossings/non-flat fb, O(n^5) transitions.
piece_flatfb.py: 1,052 pieces, 64 with flat fb, 0 violations. PARKED.
Earlier:
2026-10-24 14:42Z (successor 4, Opus 5.5, D15; stamp corrected from 14:58Z). P-N5-RE (docs/new/P-N5-RE-box26.md sha1 8dba4576…, trunk 52c7261): docs/referee-2/R2-N5-RE.md.
Lemma G (a)-(c), Wo, RM SIGN; RE SIGN WITH GAPS as written (G-RE-1 Caveat in Case NOT (i) unjustified; G-RE-2 step 3 avoidance sentence),
and SIGN WITHOUT (NC): (SG) "a switched Even vertex that is not its own cycle node gains strictly" (transitivity Ξ_{L+1}(z) ⊵ Ξ_L(z) ▷
Ξ_L(σ(y)) BEFORE prefixing; (V1) holds also when y is on the cycle but ≠ c). So (NC) closed; the packet's "flat leave" cannot occur
(instance nc_fail_n12.pg has (i)∧(ii) and a strict gain). Corollary RE needs τ constant (N-RE-3). PIECE SIGN WITH GAPS (G-RE-3: |R|−1 needs
Lemma P on 𝓡 with base at o, PH verbatim gives |R|+|K|−1; closed in §5). Tools R2-N5-RE/re_check.py (own N5 with random tie-breaks +
spec-state mode), sg_check.py, re_climb.py; 0 violations. §C (14:57Z) vs REFEREE R-N5-RE (referee 4457a9a, trunk 8001ee8): full agreement; RE-1=G-RE-1, RE-2=G-RE-2, P-1=G-RE-3, P-2=N-RE-4;
accepted RM-1 (wording); its §4.2 = my (SG) (mine slightly stronger: λ_k(y)≠y only); 𝓡* contraction valid, preferred over my Lemma-P rerun;
only mine: N-RE-3 (Corollary RE needs τ constant). PARKED.
Earlier:
2026-10-24 03:35Z P-N5-1OA (trunk 07f298d): docs/referee-2/R2-N5-1OA.md. (A) L-RED Prop X (R58 §9) SIGN WITH GAPS (G-1OA-1 prefix/whole run; G-1OA-2 step 1 is
engine-level, checked against si.py; the count is tie-break-free), Cor X1 SIGN. (B) L-NEW box 24 SIGN WITH GAPS conditional on (P) for one-player
G[X] (G-1OA-3 pointer to R17 Case B; G-1OA-4 = (P), the only unrefereed premise; G-1OA-5 Odd-fallback case). Lemma R SIGN; Lemma S SIGN WITH GAPS
(G-1OA-6: (c)/(d) for S4a steps only). R17 re-read: Case B at an arbitrary state and Corollary 2 from any start CONFIRMED. Own tool
R2-N5-1OA/oa_check.py (+ compose.py): 1,147 random o-acyclic games + 20 composed long-X games + statY_12/i4_hand: 0 violations; Prop X exact on
1,882 games; negative control fts_best16: Lemma 2 fails at 24/28 pure states (= the box). RE-PIN d78e54f (self-contained box 24) checked in §7 (03:49Z): G-1OA-3, G-1OA-5 closed by the new text; new nits N-4 (B1 third case),
N-5 (|π_v| + 1 + ℓ); verdict unchanged. L-RED's long-block instances block_bk20/bk32 (7f351fc): 27 + 49 pure states, 0 violations.
Lead 03:44/03:50Z: re-pin WITHDRAWN, Addendum 1 cancelled (my §7 stays as a record); signed object = 07f298d text. §C vs REFEREE R-N5-1OA
(9060b51, trunk 2177e79) written 03:56Z: full agreement; A1=G-1OA-2, A2=G-1OA-1, B2=G-1OA-3, B3=N-3, B4=G-1OA-5, B5/B6=§2(c)/Step 6, S2=G-1OA-6(b);
B1, S1 accepted; only mine: Lemma S (c)/(d) for S4a steps only. (P): one-player form only (fact of the proof); route (a) read, sound on my reading,
not refereed by me. Lead 03:57Z: signed object revised to d78e54f; §C2 (04:02Z) vs REFEREE §0/B7 (bb96f45, trunk 98f16c8): B7 = N-4;
B2 = G-1OA-3, B4 = G-1OA-5 closed by the new text in both reports; only mine N-5; full agreement. PARKED.
2026-10-22 00:10Z (successor 3, Fable 5.1, L36). P-N5-1P (docs/new/N5-phase-bound-box10.md §1-§4 @ trunk 26905f0): docs/referee-2/R2-N5-1P.md.
SIGN: (V1)/(V2), Lemma P (G-1P-1 wording), Corollary 1 (N-1), Corollary 3 (remark). SIGN WITH GAPS: (F1)/(F2) (G-1P-4: VJ00 (11) on the dual, order
reversal + (4)/(6) "⊵" half re-derived in §2), Theorem PH (G-1P-2 simultaneous flat switches, G-1P-3 stuck engine = N5 fallback; both
closed as wording), Corollary 2 (G-1P-5 pointer; G-1P-6 = G-N5T-1 code link DATA). Own tools R2-N5-1P/sb1p.py (valuation, play-max arena
optimum + brute force, switch-best 4 tie-breaks, Lemma P every phase), n5link.py (n5.py replay vs mine: 34,601 iterations, 11,479 optima,
522 fallbacks all flat, 0 mismatches), sbstep_link.py (L-NEW's data rule = switch-all inside the arena, N-3; every step an arena optimum;
rel_g12 11 = n−1 tight confirmed; phase_vc counts the closing λ-step, N-2), climb.py. 0 violations anywhere. Next: §C comparison with
docs/referee/ after the Lead says REFEREE's R-N5-1P is pushed.
(stamp corrected 00:26Z: this entry's true time is 00:12Z, git committer date of 857ce074) Lead addendum (trunk 0f899f3: SCOPE line + §6 VJ00 dependency list) checked in R2-N5-1P §7: SIGN WITH GAPS, nits N-4 (improving
edges are §4.4 (2) p. 11, Improve = Switch_I not argmax), N-5 (fixpoint data rule rests on Lemma 5.8 1⇒2 via 5.9/5.10, not 2⇒1), N-6 (pages).
EXACT=1 numbers = my n5 replay.
(true time 00:21Z = 498b8c99) §C vs REFEREE R-N5-1P (dfa87d0, trunk 12617fc): full agreement on verdicts; map G-1P-1..7/N-1..6 -> G1-G9 in §C; accepted G6's
stale phase_vc.txt line; only mine: N-2 (phase_vc counts the closing λ-step; REFEREE's own probe gives 14 in-phase at n = 16 = mine). PARKED.
2026-10-19 02:26Z §C-A1 vs REFEREE A1 (640ffae0): agree; accepted A1-5 (STR-DET excludes dominion-attractor e*) and A1-4 (use R46 K). Parked.
2026-10-19 02:14Z A1 = R47 Theorem CK in R2-C1P.md §A1: all SIGN (A1-G1 unneeded distinct-prio hyp., A1-G2 cite R10(a)/R9(b) under consumption; closed). Closes G-R46-1: GAP-A on C^1P <= (NEST*-BOUNDED) alone. DOM-MONO DATA vacuous (0 changes in 163 pairs). Next: §C of A1 after Lead says REFEREE's is pushed.
2026-10-19 01:44Z R2-C1P §9 (§C) vs REFEREE R-C1P 3061415: full agreement (L-1=G-LEX-1, R-2=G-R46-1); accepted N-1, O-1, S-2. Waiting for P-C1P addendum (L-RED R47, chain-keeping transitions).
2026-10-19 01:29Z P-C1P (GAP-A-M §27b/§28e/§33b/§35b, R46 §1/§2b/§3 @ 01d63d7): docs/referee-2/R2-C1P.md. SIGN: CTRL, NOSTEAL-1P, §27b corollary, OUTCOME-MONO-1P, R46 §1, §2b. SIGN WITH GAPS: SAME-CTX (G-SC-1 rho=rank incl. e; G-SC-2 cite R9(b)), LEX + R46 §3 (G-LEX-1 = G-R46-1 MAJOR: need (CHAIN-CHANGE); S-1 = |P| + Z). Probe: R2-C1P/r2log.patch (depth-0 log + R2_REV), c1pcheck.py, nestbf.py. Next: §C after Lead says REFEREE's R-C1P pushed. Handover at ~600k.
2026-10-19 00:45Z R2-N5K9 §7 (§C) vs REFEREE R-N5K9 160db1d: agree; accepted (3b) (P_strict suffices, factor 2n(n-1)+1), withdrew "flat steps included" from "exactly as needed". Parked.
2026-10-19 00:40Z P-N5K9 (docs/new/N5-K9-reading.md @ e73b214): docs/referee-2/R2-N5K9.md, SIGNED conditional on (P_K9) with gaps G-K9-1 (premise any-subset/any-start, unsourced; VJ00 7.4 at most switch-all = T22), G-K9-2 (optimal-reply code cond.), G-K9-3 (constants). Switch-all premise insufficient. DATA: one-player chains single 183 @ n=10 (verified), switch-all <= 10. Next: §C after Lead says REFEREE's report pushed.
2026-10-18 23:05Z (successor 2, session_01GkEUShwH75XDth7fwempSj, Opus 5.5, D12). Handover check 7f4ae9a (Lead: 5/5).
P-N5T (docs/new/G-N5-TERM-reading.md @ trunk 812ecba): docs/referee-2/R2-N5T.md, SIGNED WITH GAPS (G-N5T-1 code link n5.py Iσ =
VJ00 improvements (si.py Even side cross-checked 0 mismatches; dual side unchecked); G-N5T-2 termination only; G-N5T-3 VJ00
Lemma 5.9 / Prop 5.10 unproved in source, not re-derived). Lemma 5.8 2=>1 / 2=>3 NOT used. NEW: VJ00 postulate I1 also fails
(3-vertex one-player game, R2-N5T §4). Tools R2-N5T/vjbf.py (plays enumerated, no (11)), 936,826 switches, 0 failures.
Lead 23:09Z: R2-N5T merged; I1 -> L-LIT, N1-N4 -> L-NEW. 23:3xZ: §8 comparison with REFEREE R-N5T (462c8ce, §C 368a7a7) written: full agreement; dual-side improving() 0 mismatches (si_vs_bf_dual.txt); I1 one-player count 2,270 = REFEREE. Parked until routed.
Earlier (successor 1):
2026-10-17 15:22Z (successor session_01NUXFnUcx4V3ZWJJY11tXwx, Opus 5.5, D12). Handover check 6f33a84 (5/5).
P7 (§22r EXACT / PREFIX-MONO-X / new steals, pin 357224b): docs/referee-2/R2-P7.md. (a) SIGN, (b) SIGN, (c) SIGN WITH GAPS
G-P7-c1/c2 (closed: F_R <= 3 N_R), (d) confirmed 17/17. (FALL) <= (NSTEAL), open, lossy (980 steal pairs vs 103 non-rises).
Probe: R2-P7/dtl_probe7.patch (logging-only + R2_REV), an7.py (own closure). Rebuild: copy tools/oink/src, patch7.py, cmake.
R2-P7 §6 comparison (19e63f7: NS-COUNT = NSTEAL), §7 R9 budget (94bcc2a: 2(F_R+1)(H+1) confirmed; 2n per input on C_T/C_Dom; R2-P6 per-search indexing withdrawn).
P8 (§22s EXACT*/PREFIX-MONO-X*, §22u chain, pin a907c46): docs/referee-2/R2-P8.md. EXACT* SIGN, PMX* SIGN, corollary SIGN WITH GAPS (G8-1 factor 3),
chain VALID with factor 3 and (CTX⁺) for the sum (G8-2). Probe dtl_probe8.patch (+ "F t" fired log), an8.py. FIRED-R ratio 0.67|R| at small R.
R2-P8 §6 comparison (018ab0d: full agreement), §7 (c2ac652): signed REFEREE R-P7 §C2's tighter R9 constants given STR-DET; my 2n withdrawn; factor 3 -> 2 given STR-DET (mine alone; R11 keeps 3).
20:57Z R2-N5-ESC (8197777): CONFIRMED, N5 leaves Alg. 2 set (fam1 n=3 it.1, (a2,d3)) and Alg. 3 J (fam2 n=2 it.1, (m2,f2)); own tracer docs/referee-2/R2-N5-ESC/n5trace.py.
18:06Z R2-N1-FAITH (520d701): N1 kill faithful with caveats (orientation; dual family kills LS-literal).
03:45Z FAITH-lagfam (docs/referee-2/R2-FAITH-lagfam.md, 636697c): DE21 reproduces on pinned C++ (depth = D, k and exits = ceil(D/2)+1); cited in DE21 at trunk bf302b0. Parked (~410k).
00:58Z P11 (§23s CHANGE-NEW, pin 5909724): docs/referee-2/R2-P11.md. (a) SIGN (function of (R,p,T), only-appended verified), (b) SIGN + N11-b1 (e*-at-R ≤ D_R, drop H), (c) CONFIRMED: (CTX⁺)∧(FIRED⁺-R) ⇔ GAP-A. Probe an11.py 0 failures.
00:30Z P10 (§23q ENTRY-CHARGE, pin 1100f3a): docs/referee-2/R2-P10.md. (a) SIGN WITH GAPS (G10-a1 fixed step set), fan-out step correct; (b) SIGN, N10-b1 (RELSTEAL already FIRED-free; N*_R <= N_ent shorter route); (c) SIGN; (d) CONFIRMED equivalence. Probe an10.py: 0 failures, EXIT_2 on all data.
20:18Z P9 (§23f/§23g, pin c5e2b4d): docs/referee-2/R2-P9.md. (a) SIGN (N9-a1 STEAL-POLY form), (b) CHARGE SIGN WITH GAPS (G9-b1 P(τ)->P(τ⁺) closed), (c) SIGN (constant D only), (d) 65 re-steals all with a cause (stealonce_viol_n76 only; 32/50 random tie-breaks). Tools R2-P9/an9.py, stablerel.py, randrel.py.
16:13Z: no packet; standing by (~300k context). Probe infra: scratchpad oinkp/ (lost with container); rebuild from R2-P8/dtl_probe8.patch.
Earlier (predecessor):
2026-10-17 ~13:05Z (REFEREE-2 on Opus 5.5 under D12; parking for handover at ~0.57M context, Lead 12:59Z).
Packets done 2026-10-17. Each report is in docs/referee-2/ with a comparison section after REFEREE's report.
| packet | report | pin | outcome (Opus 5.5, D12) |
|---|---|---|---|
| P1 Step 5 (GAP-C) | R2-STEP5.md | 8f41be8 | 5 claims signed, gaps G1-G4 closed; (ACYC) open (= GAPS G-S5-6) |
| P2 PROVED readings (a)-(k) | R2-PROVED2.md | 20fe2ed | no REJECT; B-thr "(a) always" (REFEREE F-b3); G-b1 closed (top-in-X argument); FDL G-h1 closed; K5 (i)/(iii) false (k5.pg) |
| P3 K5', (α), O-P, GAP-A first step | R2-P3.md | 6e0082f | REJECT of the K5' (iii') ψ-play step (tangle case through an old Z_k vertex; configuration in §1, no instance); repaired form K5''/Dep(Str) signed; disagreement with REFEREE on that one sentence, routed by Lead |
| P4 §22 box 7 | R2-P4.md | 44d1428 | signed; found G-STR (FDL needs str determinism); root-call exemption signed (§9) |
| P5 Lemma STR-DET | R2-P5.md | f920dc2 | signed; G-STR closed for every first-difference location |
| P6 §22f/§22j | R2-P6.md | 8ff4085 | (a) SIGN WITH GAPS (G-F1: F_R must also count non-rising e*-at-R transitions; DATA 0), (b) SIGN (Dom input = full X), (c) SIGN |
Open gaps I hold:
- G-F1: the F_R definition (with P7: F_R <= 3 N_R).
- (NSTEAL): N_R new-steal visit pairs per context polynomial (P7 §5).
- (CTX⁺): distinct first-difference contexts and inputs per phase.
- (FALL): F_R polynomial.
- G-S5-6 = (ACYC).
- K5''/(α)-Dep-form vs REFEREE's Up(Str) reading: the P3 dispute, Lead to route.
Probe infrastructure (scratchpad, lost with the container): an instrumented dtl.cpp with counters only. Its diffs are kept
in docs/referee-2/R2-STEP5/dtl_probe.patch, R2-PROVED2/dtl_probe2.patch, R2-P3/dtl_probe3.patch and
R2-P4/dtl_probe4_full.patch (the last one is cumulative). R2_REV=1 reverses the ins(v) order ("stable" in-order).
Earlier resume points follow.
2026-10-15 13:50Z. R2-TL signed as second referee at l-red 49ae306 (R2-TL.md section 6, gaps G-TL-1..7). Idle until routed.
Earlier 13:05Z. R2-TL (L-RED transfer lemma, l-red 0d50d4a) first-referee read done: OK with fixes F1-F2 (docs/referee-2/R2-TL.md); no counterexample in 435,584 exhaustive + 900 random tests. Idle until routed.
Earlier 00:27Z. T-A1 signed as second referee at l-attr 57a1515 (R2-TA1.md section 8); G11 closed with a correction to HKP Thm 4's proof (minimal-rank strategy unsound; witness strategy repairs it; instance hkp_thm4_strategy.py). Idle until routed.
Earlier 00:08Z. T-A1 revision (l-attr 4478b84) re-checked: OK, wording nit N1 (R2-TA1.md section 7). L4 signed as second referee (R2-L4.md section 7, d76c9e1). Idle until routed.
Earlier: R2-L4 report docs/referee-2/R2-L4.md written (verdict OK with minor CHANGES F1-F3; CDFJLP Thm 5.1
hypotheses checked; PW quote verified). Pushed; Lead messaged. May now read docs/referee/ (Lead 23:40Z) once this is pushed.
Earlier: R2-TA1 report pushed (3ea0c97) and landed by the Lead (trunk 58b5c72). Lead's reply 23:40Z (quoted):
"P2 grading: CAUGHT. The F5 sentence was the planted error ... F4 was not a plant ... it is a real finding. Proposition 3 is
not part of the signed claim ... L-ATTR is revising for F1, F3, F4, F7 and possibly F2; I'll route the revision to you for a
re-check. You may now read docs/referee/ if useful. Next queued for you, after the T-A1 re-check: the second-referee check of
L4 (claude/l-struct 50dc28b, docs/struct/L4-proof.md). Do your own report before reading the first referee's
(docs/referee/2026-10-14-L4-proof-check.md). Idle until routed." Idle now.

## Queue
1. (done) T-A1 revision re-check at 4478b84. Next: nothing routed.
2. (done 23:58Z) L4 comparison with docs/referee/2026-10-14-L4-proof-check.md: no disagreement. Both reports make the same three black-box checks on CDFJLP Thm 5.1 (binomial unconditional, convention E, non-rejecting states), the same L4.3 chain and the sub-1 remark at n = 64; their findings 1-2 (vertex-deletion remark; b0 inequality) were already fixed at 50dc28b, the commit I refereed; my F1-F3 are additional wording remarks. Two independent signatures exist for the mathematics of L4 at 50dc28b.

## Things only I know
- The Lead's LEAD-STATE.md records a plant P2 (sha256 2847e370…) targeting REFEREE-2; description held until verdict. My
  candidates: the routed "psolQ iff" sentence and the reversed corollary direction (report section 5).
- My implementations (docs/referee-2/R2-TA1/r2lib.py) are naive fixpoint loops; validate.py reproduces HKP's worked Examples
  1-5 and Figs. 1, 4(a), 4(b), 6 from the tikz source (circle = Even, square = Odd; min-parity colours c, pr = M - c, M even).
- Timing: exhaustive n = 3 (175,616 games) takes 30 s; 100,000 random n = 4 about 3 min; the lane's peeling.pa2 is ~10x slower.
- The 2-vertex psolB failure `0 0 1 0,1; 1 2 0 0;` contradicts the n = 2 row of A1-results.md; the lane's own code agrees with me.

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| arXiv 1405.0386 v2 (HKP, e-print archiv.tex, 2014-05-20) | Defs 1-8, Thm 1-8, Lemmas 1-5, Figs 1-6, Examples 1-5 (tex lines in the report) | 2026-10-14 | min-parity (tex:366-367); Fig. 3 = psolB, Fig. 5 = psolQ; Thm 6 proof is a sketch |
| arXiv 1807.10546 v2 (CDFJLP, e-print tex) | §3.1 languages, §3.2 safety automata, §3.3 (strong) separators; §5 Thm 5.1 (binomial only), Lemma 5.1 (injection into non-rejecting states), Lemma 5.2 proof (resistance), Lemma 5.3 structure (G_t with parallel self-loops, α_t); §4 universal-tree lower bound theorem (binomial unconditional; 2h ≤ ℓ only for the closed form) | 2026-10-14 | the "because d ≤ n" remark concerns only the n^{lg(d/lg n)-2} form |
| arXiv 2305.00308 v1 (Parys-Wiącek, e-print tex) | p.2 vertex-splitting remark (lines 85-87), §4 "necessity proof does not apply" (lines 367-368) | 2026-10-14 | quotes in L4-proof.md verified verbatim |
| arXiv 1410.7530 (FHZ shortest paths, e-print tex) | Table 1 (G_{n,r,s,t}), Def. 5.2 functional, B_0 = zero-edge trees, Thm 6.3 (Lower-RandomFacet.tex thm:main), intro lines 23-33, Conclude.tex open problem | 2026-10-15 | no remark on parity-game transfer |
| arXiv 1410.7871 (errata, e-print tex) | section 1 (error only in RF = RF* claim; RF* bound stands; Hansen12/FHZ14 give RF bound), Fig. 1 pseudocode, "not difficult to obtain similar examples for parity games" | 2026-10-15 | |
| arXiv 2607.06334 (Zwick RAR, e-print tex) | section 4 RAR steps 1-5, Appendix pseudocode (test (c -> b) in H) | 2026-10-15 | same recursion as RF |
| docs/new/N5-1Oacyc-box24.md, docs/red/R58-n5-width.md §9, docs/new/N5-time-box21.md §2-§3 @ 07f298d | the P-N5-1OA objects and Lemmas R, S, G, Theorem B | 2026-10-24 | fleet documents, not sources; VJ00 (11) and R15/R17 as cited |
| BRICS RS-00-48 (same pdf, re-downloaded 2026-10-21, sha256 verified) | §4.1-4.5, §5.1 (3)-(10) with the "⊵" half of (4)/(6) re-derived, §5.2 Prop. 5.1, Lemma 5.2, (11); §7 Prop. 7.4 (p. 27, no proof) | 2026-10-22 | used for (F1) in R2-N5-1P §2; Lemma 5.8 not used |
| BRICS RS-00-48 (Vöge-Jurdziński, pdf sha256 485a12de432a2a8c...) | §3 P1/P2/I1/I2, Thm 3.1; §4.1-4.5 (Θ, E, E_ℓ, Ẽ_ℓ, ⊕, multiset MaxDiff); §5.1 (3)-(10); Prop 5.1, Lemma 5.2, (11); Prop 5.3-5.6, Lemma 5.5, 5.7, 5.8 (+proof), 5.9, Prop 5.10; §5.6 | 2026-10-18 | Lemma 5.8 2=>3 proof step false at cycle nodes; I1 and I2 fail (R2-N5T §4) |
| TARGET.md v1.0 | section 1 vocabulary (max-parity, successor condition, priorities 0..n) | 2026-10-14 | T-A1 uses nothing about the priority range |

## Things only I know (cont.)
- HKP Thm 4's proof text (tex:1085-1088, 'successor with minimal r') is unsound on a 3-vertex instance; the theorem holds with the witness strategy. Worth telling L-LIT for the landscape doc (B7 row) if the Lead agrees.

## Dead ends
- R2-L4: my first brute-force test of L4.1(a) on finite prefixes "failed" on 90 graphs; cause was my test (sinks make finite prefixes of dead-end paths), not the lemma, which is about infinite paths; fixed by pruning sinks (0 failures).
- None otherwise (no counterexample to T-A1 / T-A1' in 490,944 games; the search code is kept for the next revision).
