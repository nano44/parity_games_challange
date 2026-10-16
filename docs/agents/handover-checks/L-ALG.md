# Handover check: L-ALG (third successor session, 2026-10-16 08:05Z; LANE-RESTART step 3; produced on Opus 5.5, D8/L27)
Every answer measured from the repository at the time of writing (commands given), not recalled from notes/L-ALG.md.
Successor of session_01Aoj1NEAPu4ibQ3VbNXaXVY (paused by the Fable weekly limit; handover notebook b27211a, last push fe22c7f).
Previous check (session_01Aoj1N..., fa1dec3, Lead 5/5) overwritten.

## 1. Branch, head, distance to trunk
- Branch: `claude/l-alg`, tracking `origin/claude/l-alg`. Local was at 1017502 at container start; `git pull origin claude/l-alg`
  fast-forwarded it to origin. Working tree clean before this file.
- Head: fe22c7f13b201010c0a91d2f52ce827b2e5a11df (fe22c7f, "L-ALG: GAP-A data F11: every piece-0 change comes with a new
  first-call firing ...").
- Trunk `origin/claude/vibrant-johnson-nxvvxo` at 43231d639089b990d96c4c39ba9ca6466608f8ef (43231d6, "D8: owner switches paused
  lanes to Opus 5.5 until Fable reset (L27)").
- `git merge-base HEAD origin/claude/vibrant-johnson-nxvvxo` = fe22c7f = HEAD: the whole lane branch is on trunk.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` = 0 ahead, 389 behind (before this commit).
- `scripts/verify.sh` at fe22c7f in this container (12 s): VERIFY PASS. doc shape PASS; experiment self-checks PASS (the
  "compare ... ['wrong']: FAIL (5 bad)" line is the harness self-test's planted defect, followed by SELFTEST PASS); lean NOT RUN
  (no lean/lakefile); oink smoke NOT RUN (tools/oink/build absent). scripts/setup_oink.sh started in the background at 08:03Z;
  every DTL measurement waits for it.

## 2. Open work and the next step of each
- DTL gauntlet step 4, docs/alg/DTL-proof.md (§0 re-frozen at e144992 by L26, every order datum ω). §6 status table at fe22c7f:
  §1 PROVED; §2.1 soundness + strategies PROVED; §2.2 halting PROVED (exponential bound); §2.3 completeness SKETCH with GAP-C;
  §3 (b)(c)(d) PROVED, (e) PROVED conditional on (a); §3(a) tangle count = GAP-A; §4 idtl PROVED; §7 correspondence unsigned.
  - GAP-A (the task after "go"). PROVED: Lemma W (one extraction per top per search, so tangles ≤ n · searches; DTL-proof.md
    §3(a) line 696, GAP-A-data.md F0) and Lemma 1.5a; so GAP-A ⇔ polynomially many search calls per phase. SKETCH: Lemma P/Q
    (fixed-context monotonicity (M) = L-RED's Claims P, Q; DTL-proof.md line 704) with one open case: a top pruned early and
    re-absorbed through a tangle that later straddles. DATA: (M) 0 violations in ~1,400 recurring contexts; nested contexts are
    not monotone, giving an exponential nested-epoch product bound (GAP-A-data.md §4c); F11 (§4d): every piece-0 change comes
    with a new first-call firing; the CARRY first-difference half is PROVED but adds no bound (piece-0 changes are already
    ≤ n(n+1) by F5), and the Lead's budget candidates (a)(b)(c) each reduce back to GAP-A.
    Next step: (1) close the open case of Lemma P/Q and write (M) as a PROVED lemma; (2) look for a global budget charged by
    every piece-k change (not per context), or write the exact reason none exists; every step PROVED/SKETCH/GAP; message the Lead
    at once on a closed gap or a counter shape. First reads after "go": docs/red/R9-DTL-flipflop.md (read only; on trunk or
    claude/l-red), DTL-proof.md §3(a)/§4b/§5, GAP-A-data.md §4b-§4d.
  - GAP-C (Lemma K, completeness; shapes (α) straddling tangle, (β') duplicate with escapes in removed pieces): no step
    assigned in the Lead's brief of 06:55Z; stays open, untouched until routed.
- T-ALG1 (docs/alg/T-ALG1.md): (a) prose proof unrefereed, deferred by the Lead (11:20Z, 2026-10-15); (c) data only. No step.
- C1-C4: DEAD (docs/alg/DEAD.md); regressions in experiments/alg/check.sh run at every verify. No step.
- IN FLIGHT: only scripts/setup_oink.sh (this container, background, started 08:03Z). The predecessor's climbs (notebook
  "IN FLIGHT") died with its container; their last readings are in GAP-A-data.md. No patched/Debug Oink builds exist here: the
  recipes are notebook "Things only I know" items 1 and 6, 9, 10.

## 3. docs/GAPS.md rows owned by L-ALG
None. `git show origin/claude/vibrant-johnson-nxvvxo:docs/GAPS.md`: the open table is empty; the closed table holds only G1
(owner L-STRUCT). GAP-A and GAP-C are proof gaps in the lane file docs/alg/DTL-proof.md §5, not GAPS.md rows (DTL is a step-4
attempt, not a claim).

## 4. Three owner rulings that most constrain this lane (verbatim; status from trunk docs/DECISIONS-INDEX.md at 43231d6)
1. D1 (active), docs/DECISIONS.md key lines of docs/decisions/D001-launch-brief.md:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   Constraint: DTL stays "wrong" until TARGET.md §5 passes; with GAP-A and GAP-C open nothing in DTL-proof.md is a result; the
   deliverable of the next task is a PROVED lemma, the exact gap, or a counter shape.
2. D5 (active), docs/DECISIONS.md#d5:
   > I want you to believe in yourself and just loo kat the decade old mathematical open questions that has been cracked this year with AI. There are hundreads of examples so dont tell me it is highly unlikely to solve the parity game problem, because it is not
   Lead reading L18: M4 is the fleet's primary aim; reports drop the "M4 unlikely" framing; D1's "treated as wrong" stays.
   Constraint: GAP-A is pursued as a proof target; a "no global budget" outcome must name the mechanism, not a likelihood.
3. D8 (active), docs/DECISIONS.md#d8:
   > I think it is okay if we switch to opus 5.5 until the weekly limit is reset no? They produce very similiar results on the benchmarks
   Lead reading L27: L-ALG and L-RED continue on Opus 5.5 until the Fable reset (2026-10-21 21:00Z); work produced on Opus is
   labelled as such in the notebook; referees are not engaged before the reset; if Opus hits its cap the fleet pauses (D7).
   Constraint: every notebook entry this session says "produced on Opus 5.5"; no step-4 refereeing is requested now.
Also binding, Lead readings (not owner rulings, not counted): L22 (A_DTL = `oink --dtl --no-single --no-wcwc --no-loops`
@ 8fbf0a7, trace 0) and L26 (§0 re-frozen at e144992 for every order datum ω; changes through the Lead and CHECKER).

## 5. One trap that bit this lane, and the check that now prevents it
Trap: a per-top claim measured with the wrong notion of "top". dtl_tangle_family.py names a tangle's top as its
max-(priority, id) vertex, which merges all tops of one priority level; the predecessor reported "31 tangles at one top"
(dtl_pertop31_n18.pg) and "per-top ≤ n FALSE". With true tops read from a Debug trace (experiments/alg/dtl_tops.py) the
maximum is 4 at one top there, ≤ searches everywhere, as Lemma W requires (GAP-A-data.md F2, corrected 00:50Z; notebook
"Things only I know" item 4). Check now: any per-top count comes from dtl_tops.py on a Debug trace and is cross-checked
against Lemma W (count at one top ≤ number of searches); a violation of that bound means the tool is wrong, not the lemma.
DTL-proof.md §5's GAP-A row still says "per-top ≤ n FALSE (31 at n = 18)": that is the per-level count and gets relabelled
at my next DTL-proof.md edit after "go".
Process trap (other lanes, same gate): verify piped into tail loses its exit status; I push only with the literal
`scripts/verify.sh && git push -u origin claude/l-alg` as its own call and read "VERIFY PASS" before reporting a SHA.
