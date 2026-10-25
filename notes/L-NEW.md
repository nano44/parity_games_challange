# L-NEW notebook ((c) design lane under D14; Lead reading L35)
Overwrite the top sections; append to "Sources opened" and "Dead ends". Box 1 started 2026-10-18 09:10Z (date -u).

## Box 40 log (successor 19, session_011reTXakSJCcwLhC4i9ZpkB; GO 16:05Z, Lead's stamp; handover check 5/5)
- Merged trunk 078bf91 (R40 = P-N5-ENT landed). Oink built (8fbf0a7), smoke PASS.
- (1) P-N5-RHO packet drafted (docs/new/P-N5-RHO-box40.md); proofs re-checked against landed citations. Fixes vs N5-RHO-box39:
  "F1" = R17 (a) (F1) (not R21 (e) Lemma F1); Lemma S (a) cited with R21 (a) (R18 signs Lemma S with gaps S1, S2, G-1OA-6); (A0)
  (additivity at c_θ) added; (HP), (SP) stated. Data: experiments/new/box40/rhodata.py (every hypothesis, branch counts).
  Library: 0 failures; Y-FORM 6,335 checks (every H1 state); HAT-FREEZE (a) direct 1,127; past the hat freeze only |U| = 2 (trivial);
  BF-F case 1 27,932, case 2 (avoids v) 462, impossible branches 0; FREEZE-F (b) vacuous. rhoclimb.py (RHC_SCORE=bigU) for |U| ≥ 3.
- (2) N_HN for τ(o) ≠ o: docs/new/N5-NHN-box40.md (working doc). T0U, EV2-FB, SG-EV, T0-PIN, NHN-BOUND (N_HN ≤ 1 + ⌈T/2⌉ +
  2(|U| − 2)), HN-POLY-ALL, Remark H3-IN-HN; lane PROVED. The Lead's literal inequality is trivially true but not polynomial via WCH
  (WCH counts w-changes, not H2-toggles). Interim report to Lead at 04fe8979; asked yes/no on a P-N5-NHN packet.
- Trap hit at start: `pkill -f` in a compound command killed the shell (exit 144) after push.sh had finished. Kill by pid only.
- NEB fixes frozen e535e61a (sha1 15434c1c). RHO frozen 3e9fe5c2 (sha1 cd5df65c), pinned trunk c8144551. NHN frozen 5fb9dca0 (sha1
  da7d09ec). Lead's "NEB fixes before RHO" crossed the RHO freeze (said so).
- (3) Q states: docs/new/N5-Q-box40.md: Q-SPLIT (a) (S4a at an H1 state with c_w ≠ c_θ never evicts; unifies SPLIT (a)), Q-SPLIT (b)
  (Q → Q fallbacks never enter: FBL-N (ii) leaves only gates from c′ = λ(t0), and c′ cannot enter under H1 in-phase); Q-EPOCH CONJECTURE;
  breaks OPEN (c′ → R̄ gates break RISE′ Step 0).

## Box 39 log (successor 18, session_01BhkSHzG2cPM2Rdbj5Y2NJV; GO 14:29Z, Lead's stamp)
- Handover-check misses (Lead re-measure 14:29Z, 4/5; Q2): (i) docs/new/P-N5-OUT-fixes-box37.md IS on trunk (merged 16c386c, 14:17Z);
  my trunk view e6899305 predated it. (ii) P-N5-NEB IS pinned: trunk 314d220 (13:31Z), sha1 ba15e51f; queued for REFEREE-2 9 after ENT;
  its items go in a NEW docs/new/P-N5-NEB-fixes-box38.md. Landing state: R36 = P-N5-P1, R37 = P-N5-RL, R38 = P-N5-SCOPE (7fc7ac9, C47);
  P-N5-OUT drafted as R39, to CHECKER after REFEREE-2's OUT §C. Lesson: fetch trunk again right before writing a status answer.
- Merged trunk 1aeff933 (no conflicts). REFEREE-2 OUT §C: not yet written (origin/claude/referee-2 b7df84b8 = R2-N5-ENT).

- Lead 15:01Z: REFEREE-2 OUT §C (2a9e8db0) and REFEREE §C (a8b8ef3) are clean, so no OUT fixes2 is needed; R39 is at CHECKER C48.
  Name clash: my "BF" is already an item of P-N5-ENT, so I renamed it BF-RW (also FBF → FB-ROUND, which clashed with box 27's FBF; TIE → W-TIE).
- (1) docs/new/N5-RW-box39.md (working doc):
  - §1-§7: block lemmas BF-RW, FREEZE-M, FREEZE-X, ROUTE-LEN, W-POT, CW-COUNT PROVED; W-TIE steps OPEN; the circularity obstruction.
  - §11 (main): FB-ROUND (each in-phase Even fallback is a Howard/Bellman-Ford round on U = λ^{-1}(c_θ) for the signed P-weight, with o and
    c_θ as terminals) ⇒ P-FREEZE (P frozen on U after |U| − 1 fallbacks of a θ-run) ⇒ LEN-TAIL, NO-CROSS-A, BRK-POLY
    (B_S ≤ θ_S + (θ_S + 1)(n² − 1), any τ(o), any c_w). All PROVED (lane).
  - §12: the same for P-epochs (P(θ) constant); θ-LEN (≤ |U| − 2 θ-changes per P-epoch); BRK-POLY′ (everything polynomial in ρ_S =
    the number of P(θ)-changes).
  - DATA: pfreeze.py 0 failures (714 θ-runs, 872 P-epochs).
  - Tools: experiments/new/box39 (rwcount, rwclass, rwcross, tieclimb, pfreeze, pfzclimb).
- Trap hit again: `pkill -f` inside a compound command killed the shell (exit 144). Kill by pid only.

## Box 38 log (successor 17; GO 12:00Z, Lead's stamp)
- (a) Packet docs/new/P-N5-OUT-box37.md written 12:0xZ (date -u): SPLIT, EPOCH (corrected), F-FLAT, FREEZE-STEP + TAIL, NO-ENTRY-A +
  Corollary NE-COUNT (θ a parameter), CASE-B-LEN + Remark W-SIDE. Nothing uses (P); P-N5-RL not used; FB-INT / KEY from P-N5-SCOPE.
  - Superseded (successor 16): EPOCH's f_S ≤ K(X_S+1) and the phase formula (⌈T/2⌉+1)·K(2(n−1)(θ+1)+1). Holes: O-1 (evicting fallbacks
    are crossings, outside FB-INT) and the exit fallback of each stretch. New: f_S ≤ K(X_S+1)+X_S; f_HN ≤ (K+1)(2(n−1)θ_ph+(2n−1)N_HN).
  - Filled in: §5 BASE "u on z's side" is true and needed only in the cycle case; the avoid case needs only the shared top u.
    FBL-N (iii) extends to target o (λ_W(o) ∈ C_W ⊆ R̄ under ¬H2).
  - DATA: experiments/new/box38/fbsplit.py: library 107/107 in-stretch HN fallbacks are crossings, 0 non-crossing, 2 exit; 0 failures.
- (c) NO-ENTRY-B FALSE (nebc_cex_n14, canonical; neb_cex_n11, start pair). PROVED instead (docs/new/N5-NEB-box38.md): Lemma LOW-RISE,
  Theorem BRK-B (B_S ≤ θ_S + (n−2)²(θ_S+1), τ(o) = o), Corollary OUT-1 (τ(o) = o out-of-SN fallbacks poly in θ_ph, T_ph; both cases).
  Tools box38: rrgate, statesamp, neb_aug, neb_run, nebclimb, lowrise (data/lowrise_lib.txt: 0 failures).
- (c) τ(o) ≠ o (docs/new/N5-TAUW-box38.md): PROVED Lemma RISE (any case: break ⇒ θ-change or R̄-rise), HIGH-RISE (case A: the rise
  is at lev ≥ rank(o)), NO-ENTRY-A′ / BRK-B′ (c_w = o at the fallback, any τ(o); new W-case: switched v on C_W), Corollary BRK-ALL.
  FALSE: NO-ENTRY when c_w ≠ o (tauw_A_cex_n24 e29908d5…, tauw_B_cex_n24 c0ad4f0c…, canonical). Obstruction: band (rank(o), rank(c_w))
  invisible to W (fbrestart_cex_n24 state 10, gates at rank 19, band (12, 21)). OPEN: R̄-rises after c_w ≠ o fallbacks; θ_ph.

## Handover check (successor 17)
Successor 17 (Opus 5.5, D14/D15/D18, L37/L40), session_01ESR6bpU1r4ZjFsMExZtFpq, written 2026-10-25 11:5xZ by date -u (clock read
11:47:14Z at start, 11:48:13Z later; the Lead's brief is stamped 11:50Z, so the container clock is slow again). Predecessor: successor 16,
session_01LLCK4ctQmkMq2huT44SU7d, parked at l-new 0b5ec987. Every answer measured; commands named.
1. **Branch / head / trunk distance.** `git status` at start: local claude/l-new at 5961101a (successor 6's park!) and "up to date" only
   because origin had not been fetched. `git fetch origin claude/l-new` → origin 5961101a..0b5ec987; `git merge --ff-only
   origin/claude/l-new` → 0b5ec987. Trunk = origin/claude/vibrant-johnson-nxvvxo (`git ls-remote --symref origin HEAD`; there is no
   `main`, `git fetch origin main` fails). `git fetch origin claude/vibrant-johnson-nxvvxo`; `git rev-list --left-right --count
   HEAD...origin/claude/vibrant-johnson-nxvvxo` = 1 ahead / 66 behind trunk 06f57bca ("Lead: REFEREE 8 GO; NOW, LANE-RESTART, log").
   `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` (no conflicts, no rebase) → merge commit 371bb5e8: 2 ahead / 0 behind;
   after this commit 3 ahead / 0 behind until the Lead's next commit.
2. **Open work and next step** (sources: resume point below, `sha1sum`, `ls docs/new`, `git fetch origin claude/referee
   claude/referee-2`, `git log`/`git show` on them, `ps aux`).
   - P-N5-SCOPE: `sha1sum docs/new/P-N5-SCOPE-box36.md` = c3f5ed37… (pin trunk 8998ee6). REFEREE succ. 7 has SIGNED all six, no
     gaps (docs/referee/R-N5-SCOPE.md fb6089bf + §8 560ff4c4, on trunk). REFEREE-2 succ. 8 draft on origin/claude/referee-2 1f8a9109
     (`git show origin/claude/referee-2:docs/referee-2/R2-N5-SCOPE.md`): all SIGN, notes N-SC-1..4, observation O-1 on §7.2 (not to
     sign), climbs pending. Next: when the Lead relays items, answer them in NEW docs/new/P-N5-SCOPE-fixes-box36.md (does not exist;
     plus the two known nits of the resume point if raised).
   - Box 38 (a) P-N5-OUT: docs/new/P-N5-OUT-box37.md does NOT exist (the working doc N5-OUT-box37.md, sha1 45ef62a1…, does; do not
     overwrite it). Next after GO: write the packet (SPLIT, EPOCH, F-FLAT, FREEZE-STEP, NO-ENTRY-A + Corollary, §10 case-B lemma; θ
     a parameter; dependencies marked R-entry / P-N5-SCOPE / P-N5-RL = L-SI's docs/si/P-N5-RL-box10.md; (P) uses CONDITIONAL).
   - Box 38 (c) research: NO-ENTRY-B (N5-OUT §10 shape), then τ(o) ≠ o with threshold c_w.
   - Nothing of mine running (`ps aux`: no python). Oink NOT built (`ls tools/oink/build`: no such directory); `scripts/setup_oink.sh`
     started in the background (log in the scratchpad) so research can start at GO.
3. **GAPS** (`grep -n G-N5-TIME docs/GAPS.md`: line 11): G-N5-TIME, major, owner "L-NEW (L-LIT T22; referees later)", status **open**.
   Latest update in the row: 11:18Z R34 [refereed-only] LANDED (P-N5-TOG + fixes, fixes2; CHECKER C43): L-MONO, Z-COUNT, TOGGLE,
   TOGGLE-COUNT, X-SN-PHASE, RESTARTS; "Open as before; in review: P-N5-NJB (CHECKER), P-N5-SCOPE (both referees)". Open list:
   (L1) (NJB / RISE-LAST CONJECTURES), out-of-SN fallbacks (OUT-POLY CONJECTURE), ¬H1 SN states, f per phase. The row does not yet
   mention box 37 (N5-OUT: SPLIT…NO-ENTRY-A, ROUTE-FROZEN FALSE). Also mine: G-N1-LB (minor, optional, not routed, open).
4. **Rulings verbatim** (docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md):
   - D14 (l.244; index **active**; Lead reading L35): "D" / "You know it can also test prveiously not tested approaches, it can come
     up with it own as well"
   - D16 (l.299; index **active**; Lead reading L38): "Then keep working as I told you to"
   - D18 (l.332; index **active**; Lead reading L40): "Focus on N5 and work toward proving it. Explore novel approaches, especially by
     connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
     assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from
     conjectures and open problems."
5. **Trap found.** (i) The stale clone, and quietly so: `git status` said "up to date with origin/claude/l-new" at 5961101a (box 17,
   successor 6) because nothing had been fetched; 20 boxes were invisible. Only `git fetch` exposes it. (ii) REFEREE-2's observation
   O-1 (draft 1f8a9109) bears on box 38 (a): out-of-SN evicting fallbacks are themselves crossings, so they lie outside every FB-INT
   stretch and P-N5-SCOPE §7.2's "f_out ≤ n_E(2n−1)(X_out+1)" needs "+ X_out" (wd16_s2). The resume point's Corollary bound
   "(⌈T/2⌉+1)·n_E(2n−1)(2(n−1)(θ+1)+1)" must be re-derived with that term before it goes into P-N5-OUT. (iii) Name pairs:
   P-N5-OUT-box37.md (new packet) vs N5-OUT-box37.md (working doc); P-N5-RL is L-SI's (docs/si/), not mine. (iv) No `main`: trunk is
   claude/vibrant-johnson-nxvvxo.

## Handover check (successor 16)
Successor 16 (Opus 5.5, D14/D15/D18, L37/L40), session_01LLCK4ctQmkMq2huT44SU7d, written 2026-10-25 10:2xZ by date -u (clock read
10:18:49Z at start). Predecessor: successor 15, session_013tdUFhpjRP3kYPL6sBCpfU, parked at l-new ec77ad1c. Every answer measured; commands named.
1. **Branch / head / trunk distance.** `git fetch origin`; `git status`: local claude/l-new "behind 'origin/claude/l-new' by 1359
   commits" (STALE clone again). `git merge --ff-only origin/claude/l-new` → ec77ad1c. Trunk = origin/claude/vibrant-johnson-nxvvxo
   (`git remote show origin` HEAD branch; docs/NOW.md l.15). `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`
   = 1 ahead / 34 behind trunk aef92047 ("Lead: PF-THETA linear form refuted (re-run); log"); merge-base b5b8e663.
   `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` (no conflicts, no rebase) → merge commit f8419305: 2 ahead / 0 behind;
   First push.sh: VERIFY PASS but push REJECTED (exit 1, "fetch first"): parked successor 15 had pushed a670161b at 10:18:52Z (Lead
   request: PF-THETA linear FALSE recorded). `git fetch origin claude/l-new`; `git merge --no-ff origin/claude/l-new` (clean) → merged;
   `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` after this commit: see the push log in the message.
2. **Open work and next step** (sources: resume point below, `sha1sum`, `ls docs/new`, `git ls-tree origin/claude/referee{,-2}`,
   `git log origin/claude/referee`, `git log HEAD..trunk`).
   - P-N5-TOG: `sha1sum docs/new/P-N5-TOG-box35.md` = 7dfda8c8… (pinned trunk d3daae1). REFEREE-2 signed (R2-N5-TOG faabe716) and
     wrote Addendum A (16d27d1c: G-TOG-1 DATA attribution; SPEC witness b4_cyc6_0 0→1, 19 files). Fixes file
     P-N5-TOG-fixes-box35.md sha1 f15b58dd… (cited → frozen). REFEREE succ. 7 (session_01TWT1diK1Z9x2eK56iBVbZu): no R-N5-TOG on
     origin/claude/referee yet; scratch tog_probe.py/tog_climb.py at 785e79b7 (09:58Z) = review in progress. Next: when relayed,
     its items + the Addendum-A attribution row go in NEW docs/new/P-N5-TOG-fixes2-box35.md (does not exist yet).
   - Box 37 (a) packet P-N5-SCOPE: docs/new/P-N5-SCOPE-box36.md does NOT exist yet (the working doc N5-SCOPE-box36.md, sha1
     ad7282d7…, does; do not overwrite it). Next after GO: write the packet (KEY, WCH, SCOPE-COUNT, FB-INT, NH1-FB, CN-LAST from
     N5-DROP-box35.md §7; not-to-sign OUT-POLY, out-of-SN obstruction, PF-THETA linear form FALSE), send sha1.
   - PF-THETA (linear form) is now FALSE: L-RED fa3085e2, experiments/red/so/instances/pftheta_cex_n32.pg (`sha1sum` = 9f526135…);
     Lead re-run aef92047. My notebook still lists PF-THETA as a live CONJECTURE (box 35 (c)): the packet and the dead-end list must say FALSE.
   - Box 37 (b) research: OUT-POLY at H1 ∧ ¬H2 / H1 ∧ H2 ∧ ¬H3 fallbacks, first τ(o) = o (w = (o, ∅, 0) constant).
   - Nothing of mine is running (`ps aux`). Oink is NOT built in this container (`ls tools/oink/build`: no such directory): first
     research step after GO is `scripts/setup_oink.sh`.
3. **GAPS** (`grep -n G-N5-TIME docs/GAPS.md`: line 11): G-N5-TIME, major, owner "L-NEW (L-LIT T22; referees later)", status **open**.
   Latest update: R32 [refereed-only] landed 09:48Z (P-N5-FRZ + fixes, fixes2; CHECKER C41). "Open: (L1) (NJB / RISE-LAST / PF-THETA,
   CONJECTURES), f per phase outside scope runs. In review: P-N5-L2 (both referees signed), P-N5-NJB (both reports in), P-N5-TOG."
   The row does not yet record PF-THETA linear form FALSE (aef92047) nor box 36 (KEY…NH1-FB). R33 (P-N5-L2) is a draft only
   (docs/agents/R33-draft.md; `grep "^### R33" docs/RESULTS.md` empty). Also mine: G-N1-LB (minor, optional, open).
4. **Rulings verbatim** (docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md):
   - D14 (l.244; index l.22 **active**; Lead reading L35): "D" / "You know it can also test prveiously not tested approaches, it can
     come up with it own as well"
   - D16 (l.299; index l.28 **active**; Lead reading L38): "Then keep working as I told you to"
   - D18 (l.332; index l.32 **active**; Lead reading L40): "Focus on N5 and work toward proving it. Explore novel approaches, especially
     by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
     assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from
     conjectures and open problems."
5. **Trap found.** (i) The stale clone, worse than last time: local claude/l-new was 1359 commits behind origin (successor 15 saw
   1157); working from it would have hidden boxes 35-36, all fixes files and the handover. Check: `git fetch` + `git status` before
   anything. (ii) The resume point (successor 15, 10:0xZ) still calls PF-THETA a CONJECTURE (its Dead ends got a670161b later), but L-RED refuted the linear form at
   10:05Z (fa3085e2, commit time): the notebook is one fact stale at hand-over; anything reusing box 35 (c) must cite pftheta_cex_n32. (iii) Two
   near-identical names: P-N5-SCOPE-box36.md (new packet) vs N5-SCOPE-box36.md (working doc).

## Handover check (successor 15)
Successor 15 (Opus 5.5, D15/D18/L40), written 2026-10-25 07:5xZ by date -u (container clock read 07:50:41Z; the Lead's brief is
stamped 07:53Z, so the clock is again slow). Predecessor: successor 14, session_014oGq98MdJvpgrVXNA7rNvA, handover 5351fbf2.
Every answer measured from the repository; commands named.
1. **Branch / head / trunk distance.** `git fetch origin`; `git status`: local claude/l-new was "behind 'origin/claude/l-new' by 1157
   commits" (STALE again). `git merge --ff-only origin/claude/l-new` → local = 5351fbf2. Then
   `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` = 2 ahead / 66 behind trunk 1483054f ("Lead: l-new
   ONE-DROP refutation merged, re-run; log"); merge-base 45e72ef8. `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` (no
   conflicts, no rebase) → merge commit 1895b3cd: 3 ahead / 0 behind; after this commit 4 ahead / 0 behind until the Lead's next commit.
2. **Open work and next step** (sources: notes resume point, docs/NOW.md rows 42/45/74, `git log origin/claude/referee{,-2}`,
   `sha1sum`, `git diff <pin> HEAD`).
   - P-N5-FRZ: `sha1sum docs/new/P-N5-FRZ-box34.md` = 39df373c…; `git diff --stat 25fda0f HEAD` on it empty (pin 25fda0f3 = "Lead:
     P-N5-FRZ pinned (sha1 39df373c) for both referees"). Fixes file P-N5-FRZ-fixes-box34.md sha1 168de464… (cited, FROZEN).
     REFEREE succ. 6 signed (R-N5-FRZ 3a520ce, Addendum 3171efc closes FRZ-1..3). REFEREE-2 succ. 7 (session_01CE1xQNfGUgtJg9A7SWAkuE)
     did its handover/pin check at de9ff970; no R2-N5-FRZ report on origin/claude/referee-2 yet (`git ls-tree`). Next: when its items
     are relayed, answer them in a NEW file docs/new/P-N5-FRZ-fixes2-box34.md (does not exist yet).
   - P-N5-L2: `sha1sum docs/new/P-N5-L2-box34.md` = cbea0739… (as written at l-new 1afccb51). The Lead's brief names its pin as trunk
     04b3f48, but `git rev-parse 04b3f48` fails: no fetched ref contains that commit (`git log --all` also finds none). Not yet
     relayed to referees. Next: referee items go in a NEW file docs/new/P-N5-L2-fixes-box34.md.
   - Research box 35 after GO: (a) DROP-LEN on onedrop_cex_n32 (`sha1sum` = 5793d5a3…, experiments/new/box34/instances), (b) (L2)
     fallback restart at an H1∧¬H2 state taking τ(o) out of R, (c) core (L1) via a new angle vs L-SI 4 (ENT = NJB, P-N5-NJB frozen at
     l-si 5c949ec0) and L-RED 15.
   - Nothing of mine is running (`ps aux`). Oink is NOT built in this container (`ls tools/oink/build`: no such directory): the first
     research step after GO is `scripts/setup_oink.sh`.
3. **GAPS** (`grep -n G-N5-TIME docs/GAPS.md`: line 11): G-N5-TIME, major, owner "L-NEW (L-LIT T22; referees later)", status **open**.
   Latest update in the row: R30 [refereed-only] landed 05:04Z (P-N5-SN + fixes §2b; CHECKER C39); "Open per phase: X_SN, REL, K
   (Θ(n) possible); ε⁽⁻¹⁾, ε at fallbacks (never seen)." The row does not yet mention box 34 (FRZ, L2, ONE-DROP FALSE).
   Also mine: G-N1-LB (minor, optional, not routed, open).
4. **Rulings verbatim** (docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md):
   - D14 (l.244; index **active**; Lead reading L35): "D" / "You know it can also test prveiously not tested approaches, it can come up
     with it own as well"
   - D16 (l.299; index **active**; Lead reading L38): "Then keep working as I told you to"
   - D18 (l.332; index **active**; Lead reading L40): "Focus on N5 and work toward proving it. Explore novel approaches, especially by
     connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
     assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from
     conjectures and open problems."
5. **Trap found.** (i) The stale container, again: local claude/l-new was 1157 commits behind origin; working from it would have hidden
   box 34, both packets and both instances. (ii) New: the P-N5-L2 pin "trunk 04b3f48" in the Lead's brief resolves to no commit in any
   fetched ref, so the pin cannot be checked yet; I checked the packet by sha1 (cbea0739…) against my own commit 1afccb51 instead.
   (iii) The container clock is slow vs the Lead's stamp (07:50 vs 07:53): stamp only from date -u, never ahead of it.

## Resume point (overwritten at handover, LANE-RESTART step 1; successor 19 at the end of box 40, written 2026-10-25 17:44Z by date -u; context ~405k)
Successor 19 (Opus 5.5, D14/D15/D18, L37/L40), session_011reTXakSJCcwLhC4i9ZpkB. Handover check 5/5 (cba7e861). GO box 40 at 16:05Z.
### DONE (all pushed with scripts/push.sh; sha1s reported = frozen)
- Packet docs/new/P-N5-RHO-box40.md (3e9fe5c2, sha1 cd5df65c…): Y-FORM, HAT-FREEZE, RHO-TAIL, BF-F, FREEZE-F, RHO-HN, HN-POLY. Uses
  BRK-POLY′ only in the weak form (i′) (REFEREE GAP PFZ-1). Reported 16:4xZ; PINNED trunk c8144551 (16:50Z).
- NEB fixes docs/new/P-N5-NEB-fixes-box38.md (e535e61a, sha1 15434c1c…): NEB-R1 = N-NEB-1, NEB-N1..N5, N-NEB-2, N-NEB-3, NEB-B1.
- Packet docs/new/P-N5-NHN-box40.md (5fb9dca0, sha1 da7d09ec…): T0U, EV2-FB, SG-EV, T0-PIN, NHN-BOUND, H3-IN-HN, HN-POLY-ALL (conditional).
  PINNED trunk 0bb175d (17:34Z); referees after RHO.
- Working docs: docs/new/N5-Q-box40.md (Q-SPLIT), docs/new/N5-FBCAP-route-box40.md (FB-CAP route; no post-freeze eviction).
- Working doc docs/new/N5-NHN-box40.md (source of P-N5-NHN). Scripts experiments/new/box40: rhodata, rhoclimb, nhn, nhnclimb, qsurvey.
### IN FLIGHT (others)
- P-N5-PFZ + ext: REFEREE 9 R-N5-PFZ 8595343 (all SIGNED except GAP PFZ-1 on ext BRK-POLY′ (i), repair given); REFEREE-2 9 signed the
  main packet (37e55fd); REFEREE-2 10 to review ext. When both §Cs + the ext report are in (Lead relays SHAs): write NEW
  docs/new/P-N5-PFZ-fixes-box39.md, repairs only, PFZ-1 repair in full (REFEREE: inside a P-epoch ℓ(θ) = |P(θ)| + |Q ∩ A_low|, so
  ≤ |A_low| − [o low] θ-changes; ρ_S ≥ 1 forces a vertex of U ∖ {o} above c_θ; θ_S ≤ ρ + (ρ+1)(|U|−3) ≤ (ρ+1)(|U|−2)), notes
  PFZ-N1..N3 (N1: §6 "SPLIT" → SPLIT (a); N2: RISE′ hypothesis stronger than needed; N3: NEB status), N-PFZ-1..3 (R2-N5-PFZ 37e55fd:
  N-PFZ-1 (A)'s filled-in double-count case cannot occur; N-PFZ-2 window convention differs from NEB's, both correct; N-PFZ-3 DATA:
  t > f_{|U|−1} at |U| ≥ 3 never reached), REFEREE-2 §X 78896bf (G-PFX-1 = PFZ-1; REFEREE-2 signs only (i′)), and both PFZ §Cs (Lead
  relays SHAs). Lead 17:34Z: if not in before successor 19 parks, successor 20 writes it.
- P-N5-RHO (pinned c8144551) and P-N5-NHN (pinned 0bb175d): REFEREE 10 and REFEREE-2 10, RHO first. Fixes files when relayed: NEW files.
- L-RED 17 attacks CONJECTURE FB-CAP (in-phase fallbacks per phase ≤ max(1, |U| − 2); l-red 1b00610, experiments/red/frz/).
### NEXT (successor 20)
- (1) Q states (start: docs/new/N5-Q-box40.md, Q-SPLIT PROVED): H1 ∧ H2 ∧ ¬H3, only in phases with no HN state (H3-IN-HN), where t0 = τ(o) ≠ o, λ(t0) =: c′ ≠ c_θ, and every state is Q or
  ¬H1. This is the last out-of-SN piece. DATA (qsurvey.py, library): 165 phases with Q states, 186 Q states, only 2 Q fallbacks (both
  evictions), 0 S4a steps at Q states with a leave. Ideas: a Q-SPLIT (S4a at Q never evicts? R̄ vertices have W cycle node c′ with
  reward(c′) > reward(c_θ) by XW); fallbacks at Q are Bellman-Ford rounds (FB-ROUND holds), HAT-FREEZE applies on F ∩ U; ¬H1 parts by
  NH1-FB; Q-runs ≤ ⌈T/2⌉ + 1 per phase (H1-toggles). Try: Q fallbacks per Q-run ≤ poly via EPOCH-type breaks + a T0-PIN analogue.
- (1b) FB-CAP route (docs/new/N5-FBCAP-route-box40.md): κ = (M, s_θ·ℓ) Bellman-Ford freeze; after g_{|U|−2} no eviction at an in-phase
  fallback (PROVED) and no F∩U → F∩U switch except around c_θ's cycle (PROVED modulo that case); OPEN: route switches inside R̄, vertices
  outside U, ¬H1. Tightens NHN to N_HN ≤ 1 + ⌈T/2⌉ + |U| − 2. Read L-RED l-red 1b00610 (experiments/red/frz/) first.
- (2) The global loop: f enters SCOPE-COUNT (R38 (c)) and X-SN-PHASE (R34 (f)); with HN fallbacks now O(n⁸), check whether the f ↔ X
  loop closes (fallbacks at (h) states: R40 PL-S″ per scope run).
- (3) Data for referees: post-freeze EV2 ends (T0-PIN) and HAT-FREEZE at |U| ≥ 4 are not reached (climbs plateau). Better mutations
  or hand-built instances.

## Things only I know (successor 19)
- The N_HN idea (box 40): for τ(o) ≠ o, ¬H2 ⇔ t0 := τ(o) ∈ R. A stretch end keeping H1 removes t0 from R; SPLIT makes it a fallback,
  so before g_{|U|−2} there are ≤ |U| − 2 of them for free. After it, HAT-FREEZE pins M(t0) at MoptÛ(t0) at the H2 end and (a) at the
  HN end, and SG-EV (R19's (SG) step, needs only H1) makes each such end a strict rise of Ξ(t0) with P fixed = a length rise: ≤ |U| − 2.
  The H2-toggles that START a stretch never need counting. T0U (λ(t0) = c_θ when the phase has an HN state) is what puts t0 in U.
- H3-CONST (R33 (a)) + T0U ⇒ no Q state (H1 ∧ H2 ∧ ¬H3) in a phase with an HN state. So Q states live only in "HN-free" phases.
- Lead's literal question (N_HN ≤ toggles + H2-changes + 1 via WCH) does not work as asked: WCH counts w-changes, not H2-toggles.
- RHO §0 (A) repeats PFZ's "no double count" sentence; REFEREE-2 N-PFZ-1 says that case cannot occur (conclusion unchanged). If a
  referee raises it on RHO/NHN, answer as in the PFZ fixes file.
- RHO's data: library past the hat freeze only at |U| = 2 (trivial); climbs reach |U| = 3 (5 phases) and plateau at excess −2 for
  |U| ≥ 4. nhnclimb never produced a post-freeze EV2 end (T0-PIN vacuous in data). Climb outputs are TRACKED in
  experiments/new/box40/out/ (experiments/*/out/ in .gitignore matches only one level, so experiments/new/box40/out is not ignored).
- NEB-N5: the stated inv2.py command gives 75 / 9 / 4 / 20 / 8 (= referees); inv2_all.txt's bigger totals came from lost inputs.
- Pitfalls (this session):
  - The `pkill -f` self-kill (exit 144) once, after push.sh finished. pgrep -f lists the calling shell too; kill only the pids that are
    the python processes (check with ps -p).
  - `git rev-parse --short=8 A B` fails ("Needed a single revision"); rev-parse one name per call.
  - The Lead's message ordering crosses freezes (NEB-fixes-first arrived after RHO froze). Say so; do not re-freeze.
  - push.sh's verify runs on the working tree; I moved an unfinished draft packet out of docs/ while pushing other work (precaution;
    not tested whether check_docs.py would fail on it).

## Things only I know (successor 18)
- The key idea of box 39 (D18 cross-field: Bellman-Ford / Howard policy iteration). In a phase, U = λ^{-1}(c_θ) is fixed. On U every
  honest value is an additive path weight to the terminals {o, c_θ} (V1). Every in-phase Even fallback switches EVERY improving vertex to
  its best edge, i.e. it is a Howard round; S4a never lowers values (R15 (a)). So after j fallbacks, M ≥ the best path with ≤ j edges,
  and the freeze comes after |U| − 1 fallbacks. Breaks each consume their own fallback (the eviction), which kills the circularity of
  RISE-charging.
- The same trick with o removed (G_Û) works across θ-changes. That gives HAT-FREEZE and RHO-TAIL. Lemma S (a) turns θ into wt(o) + a
  min over o's F-successors (Y-FORM).
- The S4a-side analogue BF-F holds only for vertices that STAY in F. An entering vertex follows W's cycle preference (c_w beats c_θ),
  not honest weight; that is exactly why entries break the global argument. In fallback-free HN runs, F only shrinks (SPLIT (a)), so the
  argument closes there (FREEZE-F).
- Honest data caveats (the referees count them, lesson N-ENT-2):
  - P-FREEZE (c), LEN-TAIL and NO-CROSS-A are non-vacuous only at |U| = 1 in data.
  - HAT-FREEZE / Y-FORM after the freeze appear only on climb outputs (40 checks).
  - FREEZE-F (b) is vacuous.
- Pitfalls (this session):
  - The stale clone again: 1496 behind. My trunk view went stale within minutes (two Q2 misses). Fetch trunk again right before
    writing any status.
  - `pkill -f X`, or `ps | grep X | kill` inside a command whose own text contains X, kills the shell (exit 144). Twice. Kill by a
    pid taken from a SEPARATE command.
  - An exit-144 shell can leave a python edit half-applied. My `_lastP` line silently never landed, so pfzclimb's lastP score was always
    0 until fixed. Re-grep edits after any exit 144.
  - mx() in these scripts ignores values below −1 (default (−1,)), so negative maxima vanish; use acc["_x"] for climbing scores.
  - Name clashes: BF (ENT), FBF (box 27). Grep trunk docs for every new lemma name before using it.
- Tools (experiments/new/box39):
  - rwcount.py, rwclass.py (blocks; --rand), rwcross.py, tieclimb.py;
  - pfreeze.py (PFZ_KEY=P for P-epochs), pfzdata.py (branch counts; PFZ_KEY=P), pfzclimb.py (PFZ_SCORE=excess);
  - rho.py.
  - Climb outputs: experiments/new/out/box39 (gitignored; lost with the container).

## Things only I know (successor 17)
- The whole box-38 picture: NO-ENTRY holds exactly for case A with c_w = o (SEP-o: o separates R̄ from F at level rank(o), honest
  frame only, any τ(o); Step (K) at the base needs W's threshold to be o). Everywhere else entries after fallbacks happen, and Lemma RISE
  charges each break to a θ-change or an R̄-rise in [a, k). Rises are bounded only in the low class (case B, c_w = o): (n−2)².
- RISE's proof is 6 lines and needs nothing but "no gate F → R̄ at a..t" + R15 + the S4c max rule. HIGH-RISE adds SEP-o at t, t+1 and
  the chain rule lev(x, w) = max(lev(x, y), lev(y, w)) for x ◁ y ◁ w.
- NO-ENTRY-A′'s new case: switched v ∈ C_W. π_{σv} ⊆ C_W is below o (c_w = o), so u is on z's side and tops the new W-cycle.
- Pitfalls:
  - statesamp.py "R → R̄ switch" first counted switches whose target was evicted in the same fallback. A rise needs z ∈ R̄_a ∩ R̄_{a+1}.
  - An F-value can only collide with an R̄-value whose route lies below c_θ (F-values' P avoid R̄), so augmentations must target low-route
    vertices.
  - lowrise.py first had `Rb & Rb | set(range(n))` (precedence) = all vertices; fixed before the data.
  - I missed three Lead messages (12:08-12:34Z) while working: call ReadNotifications after every push.
  - The N5-TAUW header stamp was first written ahead of date -u (fixed in 199ce243 before the sha1 was sent).
  - `pkill -f <script>` inside a compound bash command kills that shell itself (exit 144): run pkill alone.
- Tools (experiments/new/box38):
  - fbsplit.py: per-stretch fallback accounting;
  - rrgate.py, taunot.py: gate classes at fallback states;
  - statesamp.py, neb_aug.py: state-level search and augmentation;
  - neb_run.py: runs from a start pair;
  - nebclimb.py: MODE B / TAU / TAUW; "-" for the canonical start;
  - lowrise.py, inv2.py: the proof checkers;
  - bandclimb.py: BAND.

## Things only I know (successor 16)
- NO-ENTRY-A's whole trick is SEP-o. In case A, o ∈ P(θ), so every R̄-value carries o and no F-value does. Every F/R̄ comparison is
  therefore decided at a level ≥ rank(o). So R-rises below rank(o) (which is all a fallback can produce, by Step (K) + R17 (F1)) can never
  create an F → R̄ gate. The evicted-vertex case needs the sandwich (T2); I first missed passive evictions.
- Step (K) / "raises W at v" is derived as: σ_a is a pointwise arena optimum in G_τ (FBL-N (i)), and the one-player optimum dominates
  every arena strategy pointwise (R17 (a) (F1)). The cycle-closing case gives a new W cycle node u with reward(u) > reward(o).
- F-FLAT's trick: switched F-vertices at a fallback are own cycle nodes (FBL-N (ii)). The phase forces their gates to be level −1
  (a higher top would change λ). So plays are unchanged up to the first visit of the cycle node (CN-LAST style), then Lemma S (a) + R15 (a).
- Random 𝒞^1O games (rand_c1o) never produce OUT stretches with breaks: all the evidence is library / climb material. rand_c1o can return
  None: guard it (my first outsn random run crashed).
- lib37.txt includes 159 non-𝒞^1O files (experiments/red etc.). Every box-37 tool skips and counts them; scripts that assert 𝒞^1O on
  every file will abort without that filter.
- Row k of rows_w has fb = the fallback flag of transition k → k+1. In my rtrace prints, the +/− diff on row k is for k−1 → k. I misread
  this once (frz24).
- experiments/*/out/ is gitignored only at depth one: experiments/new/out/box37 is ignored, but experiments/new/box37/out would NOT be.
- The predecessor (parked) pushed to claude/l-new during my handover check (a670161b, at the Lead's request). Fetch before every push.
- Tools (experiments/new/box37):
  - outsn.py, epoch.py, rfrozen.py, sep.py, inva.py (NO-ENTRY-A invariant), gadget.py (one-vertex attack);
  - sepclimb.py, rfclimb.py (MODE=ent / ent2).

## Things only I know (successor 15)
- TOGGLE's trick: the ¬H1-side cycle C lies wholly in the P = ∅ layer Z. If Z is constant, no Even vertex of C \ {c, o} can switch (the
  values are equal, so no edge is improving). So only σ(c) can change the cycle, and a switch at c changes no Ξ-value (R15 (b) style).
  That is why the toggles are cheap to count but invisible to θ.
- L-MONO: c's honest cycle length is monotone in a phase, and strict at σ(c) switches. It is a free potential, and has not been used for
  anything else yet.
- CN-LAST's trick: V_{σ′, σ̄_k} = Ξ_k for switches at own cycle nodes along P = ∅ targets; then R18 Lemma S (a) min + R15 (a).
- Pitfalls:
  - reach_o's R omits o, so τ(o) = o gives false "τ(o) ∉ R" (91 false positives in my first fbtau run).
  - My first doc draft had cycle lengths written from memory: compute before you write.
  - A header stamp written ahead of date -u forced a second commit of fixes2 (c88dc0f5 → 5f02ceba). The sha1 sent is the second one.
- Box 36 tricks:
  - KEY: λ_U depends on τ only, so every "phase-key transfer" question is void.
  - WCH: under H2, w = o ⊕ Ξ(τ(o)) with τ(o) ∈ F, so w-changes are F1° changes.
  - FB-INT: non-tame ⇒ crossing (J1 + OE), so FB's per-tame-run count holds per crossing-free stretch.
- Box 36 tools (in experiments/new/box35): scopecnt.py (scope runs, WCH, fallback classes, λ_U check), outclimb.py (OUT-POLY).
- Tools (experiments/new/box35): d35trace.py (trace with honest paths), togz.py (L-MONO / Z-COUNT / TOGGLE), dlclimb.py (MODE dl / fr /
  tog), fbtau.py + fbtclimb.py ((b)), thcls.py (θ-change kinds in scope runs; scope_runs()), lenrun.py (CN-LAST, LEN-STAY), pfclimb.py
  (PF-THETA). out/ is gitignored; finals are in instances/.

## Things only I know (successor 14)
- FREEZE's trick: R20's P^c needs Lemma C only statewise, i.e. lev(θ_k, w_k) ≤ ℓ at each window state. Its "forever" part is a
  sandwich Ξ_F ⊴ Ξ_t ⊴ W_t ⪯_c W_F that needs no WM, so it crosses fallbacks. Windows need n CONSECUTIVE (h) (or H3) states.
  They occur on library climb instances but never in random games: the data is thin, and the referees accepted that.
- Under H1, θ = o ⊕ Ξ(σ̄ o) with σ̄(o) ∈ F, and COARSE_{ℓ−1}(θ) then lives in ≤ 2d_o frozen values. Likewise w = o ⊕ Ξ(τ o) under H2.
  This is what makes RATCHET cheap.
- Under H2, c_w = λ(τ(o)) is a phase constant (H3-CONST). At ¬H1 states R̄ = λ^{-1}(c_θ) (R-CONST). These two cut most (L2) cases.
- Restarts of (h) seen so far all go through ¬H1 ∧ ¬H2 ∧ H3 states. A fallback restart via τ(o) leaving R has never been seen.
- Tools (experiments/new/box34):
  - relfr.py (NL-MF), snvi.py (withheld edges), freeze.py (MODE=H3), rsub.py, rsubfb.py, fbentry.py (renamed from fbre.py: name
    clash with box28/fbre.py on sys.path!), fbclus.py, fbenter.py, hruns.py (--rand), h1tog.py (--rand), exittrace.py, rerel.py;
  - climbs relclimb.py, wsnclimb.py, hrclimb.py, dropclimb.py.
  - lib.txt = box33/lib.txt paths (run from the repo root).
- Pitfalls:
  - Raw-REL fitness is degenerate (all exits leave at a phase start); count re-releases.
  - The Bash safety classifier failed 10 times in a row once and ended the turn: commit early, keep pushes small.
  - Climbs die when the container restarts; check ps.
  - Script names must not clash with other box dirs on sys.path.

## Things only I know (successor 13)
- The crossing problem is an SN-regime problem: at S4a steps, outside c_w = c_θ, R only grows (R-STICK uses only W monotone, Ξ ⊴ W,
  off-R Ξ = W and rew injective). Inside SN under H1 the two frames agree on R and differ only R vs F: leaving R needs an F-value
  ⊵ π ⊕ w (optimistic), joining needs π ⊕ θ ▷ the F-value (pessimistic).
- An absorption is Even closing an honest Even-good loop p → r → … → o → x0 → … → p; Odd leaves it at o. jcl_zcl_cu_n48 is the clean
  picture (σ̄(o) walks through 17 of 18 exits). b6_xl_n48 is the counter picture (exit 28 re-absorbed once per r-epoch at level 33).
- K-chain mechanism: a distance improvement propagates one layer per S4a step through honest gates, each layer releasing one dormant
  high edge. Needed: top T on o's W-cycle with every route through T (length-only W), and x with a dormant edge to r whose SHORT route
  is Ξ-worse, so Odd's τ(o) stays honest-optimal in U (no S4b switch). Initial choices come from best-reward: parities set them.
- Tools (experiments/new/box33): wakes.py, kclimb.py (THIRD=sparse), xclass.py, xgrow.py, xjoin.py, riseclass.py, orise2.py, orx.py
  (EPS=1), orxclimb.py (MODE=rel), sn.py, scopecov.py (scope runs: (h) = H1 ∧ H2 ∧ c_θ = c_w; h2 from nxt), hre.py, reabsclimb.py,
  kchain.py, biglev.py (run tools on n ≥ 100). lib.txt = c1o_list.py 64 minus box33/out.
- Pitfalls: c1o_list.py globs experiments/**, so climb outputs in out/ pollute the library: filter them. Count K by TRANSITIONS, not
  switches (my first climb counted 12 "wakes" at one transition). A fixes file cited by a landed RESULTS entry is frozen (Lead 03:00Z):
  later material goes in a new file. Oink is built in this container (tools/oink/build); a new container needs scripts/setup_oink.sh.

## Things only I know (successor 12)
- The used level L_k (max level of the changes actually made, own cycle nodes excluded) is the right freeze; M_k (max AVAILABLE) is useless
  because dormant edges sit at level ∞. Gate edges above L_k are frozen (HI), so long phases need carries (Theorem LP).
- Carry causes on 𝒞^1O: fallback (284 of 413 library rises), crossing (129, all σ̄(o)-type rises have a crossing in the interval), wake (0
  in library; ≤ 2 per run in ~7·10⁵ climb candidates).
- Lemma OE's mechanism: off crossings, both exits compared by σ̄(o) have o-free paths whose changes are Even's, so their order above Even's
  level is frozen; under ¬H1 exits on the honest cycle have empty path sets.
- Tools, experiments/new/box32: lcheck.py (all LP lemmas per transition; --rand), socheck.py (TH/SO/J), oddlev.py (OE), orise.py (rise causes),
  dormant.py / rrdorm.py / wgap.py / kwlev.py / wakeinfo.py (dormant edges, wakes), mblock.py (base trace rows_w, has h1), climbs rrclimb.py
  (wakes first), lemclimb.py (lemma failures, ρ, S_o), nwclimb.py, mblockclimb.py. c1o_list.py 64 lists the 220-file 𝒞^1O library.
  out/ is gitignored (experiments/new/box32/.gitignore); copy finals to instances/.
- Final climb states (killed at park): rrclimb wakes 2 (nr_u23_n32, u1flat_best_n32, nowake_cex seeds); lemclimb 0 failures (ρ up to 21 at
  n 48, S_o up to 42 at n 32).
- Pitfalls: `pgrep -f X` inside a Monitor matches the waiter itself (use ps + awk on argv); reach_o omits o (fake F → F dormant edges with
  σ(y) = o); Lead relays queue unseen while working — call ReadNotifications after every push; VJ00 Lemma 5.8's 2 ⇒ 3 FAILS at cycle nodes
  (R15 side finding) — check R15's side findings before citing VJ00 directions; container clock runs slow, stamp only from date -u.

## Things only I know (successor 11)
- The tie-break is the lever. S4a's choice among W-optimal arena edges is NOT arbitrary: odd c_w → min index (longest-path
  recursion, first strict max), even c_w → lexmin root-first index sequence (BFS over preds in index order). The current edge is
  always optimal when W stands still, so the choice can only move "down" (Lemma TB). Combined with the arena rule (only
  honest-improving edges join) and route-additivity, a Howard-style layer induction gives CASC.
- CASC needs ONE dependence order for both frames. Route form gives it (both values are π ⊕ terminal at o). Outside route form the
  W root is c_w and the honest root is o or C_Ξ: the conflict sits exactly on the frame cycles through o (CASC-C).
- Under ¬H2, w = (c_w, ∅, d): o is on its own W-cycle, so nothing before c_w beats it. That one line kills W-CYC (Lemma WC).
- Tools, experiments/new/box31: tbcheck.py (TB on N5 runs; layered generator), tbarena.py (TB on random arenas: the fast test),
  casccheck.py, runinfo.py (W-flat runs per piece), p3long.py (P3′ pieces), nrcheck.py (U2/U3, CASC-C, W-CYC), cascade.py (abstract
  model), climbs cascclimb.py (modes thw / flat), nrclimb.py. out/ holds climb bests (not gitignored at this depth: copy finals to
  instances/).
- U2/U3 (box 31 b): in U2 honest values are route functions with constant terminals at the first of {c_θ, o}, so CASC holds there
  unchanged. In U3 split R by kind (c_w on the route or not); only kind crossings and c_w's own DFS choice break the layer
  induction. Tools: u23check.py, u23climb.py (modes U2 / U3), tamecheck.py (L-SI tameness; reads experiments/si/coarse/mono.py).
  U2 W-flat switches have never been seen.
- The lane helper reach_o (box28/fbre.py) returns R minus o: count |R| with o in every statement.
- Pitfalls: my first message stamp (20:22Z) was 3 min ahead of date -u (20:19Z): stamp only from the command output, not a guess.
  Random o-cyclic runs almost never reach W-flat runs or U2/U3; seed climbs from u1_n32 / b5_os_n14.

## Things only I know (successor 10)
- The structure that carries everything:
  - Ξ ⊴ W always (XW).
  - Off R, Ξ = W with no (h) (Lemma G (a)), so all F-dynamics is R17 on 𝓕 per crossing-free interval (F1°), whatever the state type.
  - H1 ⟺ λ_Ξ(o) ∈ F and H2 ⟺ τ(o) ∈ F. Both are constant on crossing-free intervals (TC), so the "type" of a whole interval is
    nearly fixed.
- O-counts decompose exactly: OTHER-touching = crossings + F-changes + R-only. Every big O seen (26 at n 16, O/n = 2.04 on b5_os) is
  mostly crossings + F-changes. R-only ≤ |R| in all data.
- "Route form" (H1 or λ_Ξ(o) = o; H2 or λ_W(o) = o): values on R are π ⊕ terminal in that frame. In general each frame is "path to
  its cycle node in the graph with o fixed to its exit" (a two-target route game). P3′ = the honest target higher.
- U1 mechanism (wf0_cex_n16, iterations 16 and 20): Engine.evaluate's tie-break (first max in DFS / BFS, experiments/si/si.py
  evaluate) is not "keep current". So S4a moves an R-vertex to a W-tied successor with a better V_mid set. The Lead confirmed this is
  N5 as specified; a keep-on-ties variant would be a different algorithm (do not adopt).
- Tools, experiments/new/box28: nhprof, fbre, xcount, eqcheck, fbclimb (FIT=p/v), xclimb, wclimb. experiments/new/box29: otherx,
  rsplit, ivsplit (per-interval split), tccheck, oblock, dstat, throttle, odep, p3check, rfcheck, wflat, u1vertex, and climbs opclimb,
  orclimb, u1climb, nfbclimb. Seed climbs from named instances: random C^1O almost never gives throttled or route-form pieces.
- Pitfalls:
  - The container clock (date -u) runs slowly. Stamp only from date -u.
  - pkill -f kills my own shell: kill by pid from ps.
  - push.sh takes several minutes while climbs load the CPU. Do not commit while it is running (verify reads the working tree).
  - Check "freeze" indices with the right bound: a route path has ≤ |R| edges (box 29 off-by-one).

## Things only I know (successor 9)
- Box 26/27 picture (READING; assumes (h)). Inside a joint λ-phase with τ fixed:
  - UNTHROTTLED states (θ = w) are pure one-player G_τ (Lemma UT: ≤ n − 1 value changes per maximal unthrottled run, even as θ = w
    moves).
  - THROTTLED (θ ◁ w) (θ, w)-stretches are O(n³) via C / FBL / FBF / XA / CR / PIECE.
  - So everything rests on how often θ or w changes, plus the non-(h) states.
- The two-frame band (box 26 §7.3): F→R needs the honest test, R→F needs the W test, and in between a vertex keeps its side.
  "Withheld" and "trust" are its two faces. Reweighting (Johnson / T29 Lemma B) cannot remove it. Coarsening above u* does.
- (NH) start points:
  - All box-25 W-drop instances at fallbacks off (h) have τ(o) closing a cycle at o (wdrop_cyc n 4, wd16_s2).
  - In every long phase (fts_best16, tp32, rt48, ph64, sc32, elim24_p52), non-(h) transitions = 0 (phaseprofile.py). So (NH) may be
    a boundary effect at phase starts.
  - A first check: count non-(h) states per phase across climbs.
- (CYC') start points:
  - sc32.pg (n 32) has θ changing at every one of 43 transitions in one phase, with no w-change.
  - Lemma UD: u* only descends when θ changes AT u*. In sc32, check how many θ-changes are at u* versus below it. That is (CYC-u*).
  - Box 27 §8c sketches a recursion below u*: after the coarse freeze every vertex is one-sided.
- Tools (experiments/new/box25/; all import common.py; random generator rand_c1o):
  - reentry.py (ROUTE / WRISE / THETA classes), routemono.py, piececheck.py, crossings.py (throttled by default; --all);
  - coarsecheck.py (C1 / C2 / C3, --withfb), fbedges.py, fbfcheck.py, phaseprofile.py;
  - climbs: xingclimb.py (throttled), fbreclimb.py, stretchclimb.py, routeclimb.py, thetareclimb.py, shrink_theta.py.
- Pitfalls:
  - `cd dir && nohup cmd &` backgrounds the cd too, so later relative paths break. cd first, then nohup on its own line.
  - pkill -f kills my own shell (hit again in box 27). Kill by `ps -eo pid,args | awk '$3=="script"'`.
  - Measure THROTTLED quantities explicitly. Unthrottled regimes are already bounded and inflate the counts (box 26's mistake).
  - Header timestamps only from date -u.
- From box 25: the o-cyclic core (box 25 §5) holds. Inside a (τ, λ)-phase under (h), θ = o ⊕ min over exits ∉ R of their o-free
  value. W-drops happen off (h) and at throttled (h)-fallbacks (fbh_drop9). A fallback's refused edge can be a W-tie (fbh_thr).
- TRAPS THAT BIT ME:
  - (box 25) I announced (WF) as new, although box 22 had it. Check: grep docs/new/ and this notebook before calling anything new.
  - (box 26) My crossing climbs measured the unthrottled regime. Check: restrict to θ ◁ w.

## Things only I know (successor 8)
- o-cyclic state, precisely:
  - Lemma 1 of P-N5-1OA (X has G[X]-optimal values at pure transitions) holds on ALL of 𝒞^1O. REFEREE-2 notes the same,
    including fts_best16 (there X = ∅).
  - Lemma 2 (θ = w at pure steps) is the break. It fails first at cyc4 (n 4; box22/instances/cyc4.pg, sha1 bff7a8c2…).
  - Lemma 2' (PROVED under (H): the (σ, τ)-play from o does not return to o): a throttle surviving a pure step needs an
    INCOMPLETE exit a = σ̄(o) ∈ Y, with Ξ(a) ◁ U_τ(a). DATA: 0 exceptions in 196 states.
  - Mechanism (the self-throttling exit):
    - a's best route against τ runs through o, while a currently avoids R (24 of 24 throttled states of fts_best16);
    - θ rises only through o-free exit improvements;
    - all 5 exits of fts_best16 are incomplete at states 2-25 and complete together at state 26.
  - Ring reading (L-RED R58 §10): fts_best16's exits lie on one σ-path back to o, and σ̄(o) walks along it. A super-linear θ-count
    would need nested rings, which nobody has built. θ-change climbs stay below n (13 at n 16, 16 at n 24).
  - cycclimb (pure run in one λ-phase − (n−1)) at n 8 / 10 / 12 / 14: best −1 / 0 / −2 / −5. The smallest pure block beating
    R17's per-phase bound is fts_best16 (n 16).
- Tools:
  - box21/n5x.py: trace equal to n5.run. box21/climb_fix.py: modes tstar, tstarph, bestph, oneodd, seg1o, laps1o, segfz, tany.
  - box22/statcheck.py: P-N5-1OA lemmas L1-L3. It now has a main-guard (d68ded65); its CLI is unchanged from the referees' pin.
  - box22/shrinkP.py: violation() for I1-I4, with env HREQ / NOFB.
  - box22/incomplete.py: Lemma 2'.
  - box22/climbPure.py: the pure-transition climb.
  - n11/n5ht.py: N5-HT, dead.
- Pitfalls:
  - pkill -f matches my own shell. Kill by argv fields.
  - Scripts imported by others need a __main__ guard.
  - Count stretches with λ held constant.
  - In 𝒞^1O checks, R must follow forced Odd vertices.
  - check_sol2 needs Oink built (scripts/setup_oink.sh).
- Process: Lead rulings this run were the stop rules (03:20Z, 04:45Z, 05:00Z), "freeze before any run" (box 23), and the frozen
  packet rule (corrections only in new dated sections).

## Sources opened
- (succ. 16, box 37) No external source opened. Internal: RESULTS R15, R17, R18 (d), R19, R21 (c), R22, R23 (a)-(d), R25, R28, R30; P-N5-FB §4-§5 (docs/si/P-N5-FB-box7.md), P-N5-OE §1-§3, P-N5-L2 §0-§2 and §5, P-N5-TOG §0, §4, §6; P-N5-X §0, §3; R-N5-TOG (referee fff6e624), R2-N5-TOG Addendum A (16d27d1c); SPEC S1-S5.
- (succ. 15, box 35) No external source opened. Internal: P-N5-NJB (docs/si/P-N5-NJB-box9.md, pinned a7d85b3), P-N5-FBW §0, RESULTS R15, R27, R28; REFEREE-2 R2-N5-FRZ (+§C f546b43); REFEREE R-N5-L2 (7626354).
- (succ. 13, box 33) No external source opened. Internal: P-N5-CLS (docs/si/P-N5-CLS-box8.md, pinned 486107a) §1-§7, N5-C-box8 §12-§13.
- (succ. 12, box 32) VJ00 = Jurdziński & Vöge, BRICS RS-00-48 (www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf, sha256 485a12de432a2a8c…, opened
  2026-10-25 00:35Z, pdftotext): p. 14-15 σ̄ definition and Prog (P1)-(P3); p. 15 Lemma 5.2; p. 16 (11); §4.4 p. 11 improvement (2) and Switch_I;
  p. 19-21 Lemma 5.8 (2 ⇒ 3 ⇒ 1 proved via Lemma 5.7, 5.2; 1 ⇒ 2 via Lemma 5.9 'proved similarly'). Used in P-N5-LP (DF uses 2 ⇒ 3 ⇒ 1 only).
- (succ. 7, box 18) arXiv 1405.0945 v1 (4c6956dc2f1db3ee): §1 l.95-119 (SA level n exact). arXiv 1506.04184 Bodirsky-Mamino
  (e0e0e34de549a4d8): abstract, §1 l.103-104, Thm 5.1 (NP ∩ co-NP; no bounded-width statement). C. Fritz PhD thesis Kiel 2006
  (macau.uni-kiel.de d1644.pdf, fa1253460e9058c3): ch. 3 intro, §3.5 remark (simplify-then-solve slower than lifting).
- (succ. 6, box 17) arXiv 2108.13338v5 e-print (sha256 7189eb2f…, LaTeX): §1 intro l.13 (determinacy, citing Martin 75 / EJ91, not opened), §2 all
  (Def 2.1-2.2, Thm 2.3, Lemma 2.4, Prop 2.5, operators), §3 Algorithm 1, Thm 3.1 + proof, Def 3.3, Thm 3.4; §4 Alg 2-3, Lemma 4.2, Thm 4.3,
  Cor 4.4, Thm 4.5, Rem 4.6; lmcs.cls l.685-699 (one counter per section). Kelner-Spielman STOC 2006 author PDF (sha256 3b5f68fe88c9cd46…):
  abstract, §1-2, Thm 3.2, Thm 6.3.
- (succ. 5, box 13) arXiv 2108.13338 Koh-Loho (21ee0e4336252f7e): §1 p.2-3, Thm 2.3, 3.1, 4.5. Schewe MFCS 2009 author PDF (d27bbc79ab6b162b):
  §1 p.2, Cor. 6-8. arXiv 1305.3944 Avis-Friedmann (d1fafb8b5d0b822c): abstract, Thm 4. arXiv 1210.2459 CGR (02fca6a45515f2ec): abstract.
  arXiv 2509.16075 Maat (69706649fed1fac9): related work p.2. arXiv 1405.0945 (4c6956dc2f1db3ee): §1 p.2. arXiv 1605.03019 (cb6029755abff8a9): §1.
- (succ. 5) arXiv 2007.06558 v5 Cen et al. (sha256 23fddbc3f493d02e): Thm 1. arXiv 2105.15186 v3 Cen-Wei (a2da0da3164be410): Thm 3.
- (succ. 5, 2026-10-22) arXiv 1304.1888 v2 HIJ (sha256 01e4cde9b47f90cb): §2.3 Def. 16, Thm 18; §3 Thm 19, Thm 21 (family G_n); §4 Thm 22-25;
  §1.1. arXiv 1708.01544 ABGJ (9608058cb6fa98a3): Thm A/B, Cor. 31, Remark 32, p.2-3 (bitlength of t exponential). de Klerk-Nagy,
  optimization-online 2010/02/2555 (726c92b99e80dae6): abstract, Def. 1. arXiv 1106.0778 Friedmann (46c96f44775aa2b0): §9 beta_G, Thm 9.3.
  arXiv 1008.0530 v1 HMZ (f53a6b5127d95078): Thm 6.5. arXiv 0909.5653 v1 FJS (9fbd86643615f000): B13 context only.
- arXiv 1008.0530 v1 (Hansen-Miltersen-Zwick, "Strategy iteration is strongly polynomial for 2-player turn-based
  stochastic games with a constant discount factor"), opened 2026-10-18 09:2xZ (pdf, 13 pp). Thm 6.5: Strategy-Iteration
  from any start terminates within (m+1)(1 + log_{1/γ}(n²/(1−γ))) = O(m/(1−γ) · log(n²/(1−γ))) iterations (the n² is
  n²/(1-γ) inside the log). Proof via Lemma 6.4 (every L̄ iterations a new action is never used again). §7: SI is
  "exponential for non-discounted 2TBSG, or when the discount factor is part of the input" (citing Friedmann).
- arXiv 0909.5653 v1 (Fearnley-Jurdziński-Savani, Lemke / Cottle-Dantzig for discounted games), opened 2026-10-18.
  Lemke as a homotopy in the covering parameter z at fixed discount (text near l.250: "how much further z can be decreased
  before σi ceases to be optimal"); Thm 18: Lemke 2^(n+1) - 2 iterations on G_n; Thm 19 Cottle-Dantzig; p. near l.557:
  "standard reductions [16, 21, 13] convert this parity game into average-reward ... discount factor ... very close to 1".
- NOT yet opened (needed for N1's termination bound only): Zwick-Paterson TCS 158 (1996) discount threshold; Puri thesis.
  Used instead, as restated in 2610.22149: Prop. 7.11 = [ZP96, Thm 5.2] ‖λ(γ) − λ‖∞ ≤ 2n(1 − γ)‖r‖∞ (normalised values).
- arXiv 1106.0778 (Friedmann, LMCS 7(3:19)), opened 10:30Z, §9: reward r_Ω(v) = (−|V|)^Ω(v); β_G := 1 − 1/(4·|V|³·max|r(v)|) [p. 35; CORRECTED per L-LIT T19, box 3; earlier text had |V|];
  Thm 9.2 (Puri), Thm 9.5 (Vöge: every parity improving switch is a discounted improving switch), Lemma 9.6 (1-sink games:
  Odd's discounted best response reaches the sink), so the lower bound transfers to discounted payoff games.
- arXiv 2610.22149 v1 (Loff-Skomra, "Smoothed analysis of policy iteration and value iteration for deterministic discounted
  and mean-payoff games played on any graph", 15 Oct 2026), opened 10:35Z. §7.4, Figure 7.2 IncreasingDiscountPI:
  "γ ← (1 + γ)/2; (σ, τ) ← DiscountedPI(σ, τ, γ) until (σ, τ) are optimal in the mean payoff game" = N1. Thm 7.9 (1 − γ <
  1/(4n²Δ(r)) => unique optimal pair), Thm 7.14 (O(m² + m²n⁴Δ(r)² log³(nΔ⁺)) Howard switches), Thm 1.2 (smoothed poly), §9
  open problems. Cites [LS24] = Loff-Skomra, ICALP 2024, LIPIcs 147:1-147:16 (NOT opened).
- arXiv 2402.03975 v1 (Loff-Skomra, "Smoothed analysis of deterministic discounted and mean-payoff games", 6 Feb 2024 =
  [LS24], ICALP 2024 version restricted to ergodic graphs per its HAL listing), opened 11:45Z. Thm 1.10: "The greedy-all
  switches policy iteration rule combined with increasing discount factor solves random instances of deterministic discounted
  or mean-payoff games in polynomial smoothed complexity." Thm 6.6 (Figure 12, IncreasingDiscountPI: halts on every input,
  smoothed polynomial). WORST CASE, verbatim (p. 5, l. 199-201 of the text dump): "Otherwise, for mean-payoff games, or for
  discount factors γ exponentially close to 1, no upper-bound is known on the number of iterations, significantly better
  than the number of policies, which is exponential in √ the number n of states." (same sentence in 2610.22149 §1.2).
  Example 3.5 / §3.2: a deterministic two-player game whose value, as ONE payoff varies in [−1, 1], has 2^Ω(n) break points
  (from [BNRC08] / [ABGJ18]); this is a parametric-PAYOFF statement, not a lower bound for IncreasingDiscountPI. No
  worst-case lower bound for IncreasingDiscountPI is stated in either paper (searched: worst, exponential, lower bound, open).
- arXiv 1208.5083 v2 (Post-Ye), opened 10:38Z: Thm 3.7, the highest-gain simplex rule takes O(n³m²log²n) iterations on
  deterministic MDPs with uniform discount, any discount (Thm 4.8: O(n⁵m³log²n) for distinct discounts).
- Search (WebSearch, 10:30Z) also listed: Madani-Thorup-Zwick, ACM TALG 6(2) 2010, O(mn) for deterministic discounted MDPs
  (abstract page only, NOT opened); Karczmarz arXiv 2110.15070 (NOT opened).

- arXiv 1309.5925 v2 (Allamigeon-Benchimol-Gaubert-Joswig, "Combinatorial simplex algorithms can solve mean payoff games",
  SIAM J. Optim. 24(4) 2014), abstract page opened 2026-10-18 ~18:39Z (box 3): any combinatorial simplex algorithm has a
  tropical analogue solving MPGs (Hahn series + symbolic perturbation); strongly polynomial combinatorial simplex "is open".
  Body NOT opened.
- arXiv 2309.02223 (van Dijk-Loho-Maat, "The worst-case complexity of symmetric strategy improvement", CSL 2024), pdf opened
  ~18:40Z (sha256 10e6794d82aba465..): Theorem 1 p. 2 (exponential for SSI independently of the improvement rule; any
  valuation), Algorithm 2 (SSI, f applied to I), Algorithm 3 (generalized SSI with J-sets), Lemma 5, p. 3 "more than only
  local information".

- Jurdziński & Vöge, "A Discrete Strategy Improvement Algorithm for Solving Parity Games", BRICS RS-00-48 (Dec 2000; full
  version of the CAV 2000 paper, LNCS 1855), https://www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf, opened 2026-10-18 ~21:17Z
  (sha256 485a12de432a2a8c..):
  - §6 shortest-paths procedure, lines 1-10;
  - Theorem 6.2 (p. 25): an improvement step in O(n·m);
  - §1: Bellman-Ford O(n²·m);
  - §5 Lemmas 5.2-5.9: Improve(σ) = σ iff σ is optimal (Lemma 5.8);
  - §7: number of steps open (2000).
  Box 4 used it to correct N5's cost statement.

- (succ. 2, box 7) VJ00 RS-00-48 §7 p. 26-27 re-read: Prop. 7.4 (O(n³) improvement steps, one-player parity games; NO proof), Prop. 7.5,
  Prop. 7.6, "at most O(n²) substantial steps". Asadi-Chatterjee-de Raaij arXiv 2506.12254 (UAI 2025), abstract page opened
  2026-10-18 between 23:42Z and 23:47Z (date -u bounds): Howard on deterministic mean-payoff MDPs Ω̃(I) lower bound; "best known upper bound is exponential".
  Hansen-Zwick ISAAC 2010 and Hansen-Kaplan-Zwick SODA 2014: records only (WebSearch), NOT opened.

- (succ. 3, box 8) Fearnley arXiv 1705.02313 v1 (sha256 a49296a2…), §4 "One-player strategy improvement", Lemma 3: O(|V||E|) for the
  ALL-SWITCHES (greedy) one-player rule only, citing Cochet-Terrasson-Gaubert [3]; it does not cover adaptive subsets.
- (succ. 3, box 8) Zadeh, "What is the worst case behavior of the simplex algorithm?", CRM Proc. Lecture Notes (2008), §1 p. 1:
  "An example due to Edmonds for shortest path computations is also known [16]". Edmonds' example itself NOT opened.
- (succ. 3, box 8) REFEREE R-N5K9 (claude/referee 160db1d) §(2)-(3): (P*), (P_strict), switch-all insufficient.
- (succ. 4, box 10) VJ00 BRICS RS-00-48 re-opened 2026-10-21 23:31Z (pdf sha256 485a12de432a2a8c…, pdftotext): §5.1 pp. 12-14 (shortest-path
  characterisation of Π_σ, equations (6)-(10)), §5.2 Prop. 5.1 + Lemma 5.2 => Ω_σ = Θ_{σσ̄} and σ̄ is a best counter-strategy (eq. (11), p. 16: the
  (F1) fact of N5-phase-bound-box10.md, used on the dual game), §5.4 Improve, Lemma 5.7 (not used), Lemma 5.8 (not used), §3 postulates P1-P2,
  I1-I2 (not used), Prop. 7.4 p. 36 (statement only, no proof).
- (box 40, successor 19) Opened: SPEC S1-S5 (docs/new/N5-ssi-global.md l. 47-62); RESULTS R15, R17 (a)/(e), R18 (d) (Lemma S, gaps S1,
  S2, G-1OA-6), R19 (a)/(d), R21 (a)/(c)/(e), R23 (b) (ACT), R33 (a)/(b), R34 (a)/(e), R38 (a)-(f), R39 (a)-(g), R40 title; P-N5-RE-box26.md
  §1 ((h)) and §4 (Lemma RE proof); docs/referee/R-N5-NEB.md (40adbf1c, §C 46a80300); docs/referee-2/R2-N5-NEB.md (a4516df9, §C a769ff54);
  docs/referee/R-N5-PFZ.md (8595343); docs/referee-2/R2-N5-PFZ.md (37e55fd) notes.

## Dead ends
- (box 40, successor 19) Counting N_HN by H1-toggles + WCH (the Lead's 16:05Z form). Obstruction: WCH (RESULTS R38 (b)) bounds w-changes
  at H2 → H2 transitions, not H2-toggles; an H2-toggle is a crossing of τ(o). Logical gap, no instance needed. Replaced by NHN-BOUND.
- (box 40) Climbing into HAT-FREEZE's post-freeze regime at |U| ≥ 4 (rhoclimb.py, ~100 CPU-min) and to post-freeze EV2 ends (nhnclimb.py,
  5 runs): no success. Reading: FB-CAP (L-RED) says the regime does not exist (≤ |U| − 2 fallbacks per phase).
- (succ. 17, box 38) CONJECTURE BAND (P-N5-NEB §8, not to sign: "after a c_w ≠ o fallback in case A, R → R̄ gates and R̄-rises have
  levels < rank(c_w)"), RISES form: FALSE on experiments/new/box38/instances/tauw_A_cex_n24.pg itself (sha1 e29908d5…; canonical):
  θ-constant HN run from base 4, S4a step 12 → 13 raises Ξ(11) (18, 4882432, 11) → (18, 13336576, 13) and Ξ(16) at level 23 >
  rank(c_w(4)) = 21 (rank(o) 17). Found by experiments/new/box38/bandclimb.py score at its seed. Obstruction: c_w(a) is read at the
  base; later S4a steps take W-improving R → R̄ gates at any level. The gate form AT the base state is untested. Goes into a P-N5-NEB fixes
  file when referee items arrive.
- (succ. 17, box 38 (c)) NO-ENTRY for τ(o) ≠ o with c_w ≠ o (both cases): FALSE, canonical start. experiments/new/box38/instances/
  tauw_A_cex_n24.pg (sha1 e29908d546d62e64903b41aa987351c3b3c68a62; case A; n5 16 it / 3 fb; Oink OK) and tauw_B_cex_n24.pg (sha1
  c0ad4f0ca6ce9a35d3c89b377e686eef58dc3845; case B; n5 10 it / 4 fb; Oink OK). Obstruction: W's threshold is c_w, so honest R → R̄ gates at
  levels in (rank(o), rank(c_w)) survive Step (K) at a fallback, and R̄-values rise there (tauw_A: high rise at rank 19 in band (17, 21)).
- (succ. 17, box 38 (c)) CONJECTURE NO-ENTRY-B (τ(o) = o, case B: no entry after an HN fallback while θ is constant): FALSE, canonical
  start. experiments/new/box38/instances/nebc_cex_n14.pg (sha1 399119afb8741f3689081389e70729891937df7b; nebclimb seed 3835 from
  b5_os_n14). n 14, o = 7, rank(o) 6 < rank(c_θ = 12) 8. n5 9 iterations / 5 fallbacks; Oink zlk OK, strategies verified. Fallback at 1
  raises Ξ(3) (12, ∅, 3) → (12, ∅, 4) (low class, P = P(θ) = ∅); gate 4 → 3 from F at 2; S4a 2 → 3 enters 4, θ = (12, ∅, 2) constant.
  Also from a start pair: neb_cex_n11.pg + .state (232b8951…). Obstruction: a length-only R → R̄ switch at a case-B fallback raises an
  R̄-value of the low class past an F-value with the same P. Repair: Theorem BRK-B (breaks ≤ θ_S + low rises).
- (succ. 17, box 38 (c)) NO-RR-B ("no R → R̄ gate at a case-B τ(o) = o HN fallback state"), NO-RISE-B ("no R̄-value rise at such a
  fallback") and "INV_B (i) propagates": all FALSE on nebc_cex_n14 (state 1 / 1 → 2 / state 2). State-level: statesamp.py 39 / 616 states
  with gates (all length-only), 1 / 413 with a real rise (norise_state_n8.pg + .state, c7462ba5…).
- (succ. 16, box 37) ROUTE-FROZEN ("inside an H1 ∧ ¬H2 stretch, after a fallback with θ constant, Ξ on R stays frozen"): FALSE.
  experiments/new/box37/instances/rfroz_cex_n16.pg (sha1 a9b40395ba9a351037f8dff612d50848540ddbc1; rfclimb seed 3722 from wd16_s2). n 16,
  o = 11, τ(o) = o, case A. n5 15 iterations / 5 fallbacks; Oink zlk OK, strategies verified (Lead re-run 11:14Z). Phase ph394, θ constant:
  the fallback at 4 → 5 is followed by R-rises at the S4a steps 5, 6, 7, 9, 10 and at the fallbacks 8, 11, 12. Obstruction: R → R gates
  keep improving routes after a fallback. Entries: 0, as NO-ENTRY-A predicts (all rises are at levels 8-11 < rank(o) = 12).
- (succ. 15, box 36, recorded while parked at the Lead's request 10:20Z) LINEAR PF-THETA (≤ n θ-changes under one fallback level): FALSE.
  experiments/red/so/instances/pftheta_cex_n32.pg (sha1 9f526135…, L-RED 15, l-red deb9366, climbed from pf_best_3621). n 32, o = 0,
  one scope run with one fallback (level 31), then 33 θ-changes > n. Lane re-run: n5 38 iterations / 1 fallback, check_sol2 zlk OK
  strategies verified, pfclimb.fit (33, 1). Scope: all within ONE fallback-free run after one fallback, so the poly form survives.
- (succ. 15, box 35) Weak DROP-LEN "≤ 1 drop per fallback-free run": FALSE. experiments/new/box35/instances/onerun_cex_n32.pg (sha1
  70832fcb…, n 32, o 27): 0 fallbacks, drops at 2→3 and 7→8, both S4a σ(13) switches into o; θ length 10 → 7 between them.
- (succ. 15, box 35) DROP-LEN "θ changes between two drops": FALSE (REFEREE succ. 7). docs/referee/R-N5-L2/droplen_cex_n12.pg (sha1
  a6af26db…, n 12, o 0): θ = (2, ∅, 1) constant, 4 toggles, all pure σ(2) switches (c odd, o → c directly).
- (succ. 15, box 35) "A fallback at H1 ∧ ¬H2 never takes τ(o) out of R": FALSE. experiments/new/box35/instances/fbrestart_cex_n12.pg
  (sha1 35223b6c…, n 12, o 9): at state 2, c_w = o and W-cycle 9→10→1→2→9; the fallback takes the withheld edge 1→3 (Ξ-better, W-worse),
  and (h) holds at 3.
- (succ. 15, box 35) LEN-STAY "after M = −1 in a phase, (cycle node, P) is frozen": FALSE in data (claimF_len_cf1, 4 library + 1 random).
- (succ. 13, box 33) "ε_{H1} ≤ (d_o − 1)(f + 1) per phase": FALSE (L-RED fdd801b). experiments/red/so/instances/epsseg_cex_n48.pg (sha1
  b4c7dcb0…): f = 0, 17 H1 ε-transitions, d_o 17 (exit 33 absorbed at 7, released at the S4a step 8 → 9, re-absorbed at 14; correction 05:31Z, CHECKER C39). ABS-COUNT
  (with REL) holds with equality.
- (succ. 13, box 33) CONJECTURE EXIT-R (ε form) and ORX: FALSE (L-RED box 37). experiments/red/so/instances/exitr_cex_n48.pg (sha1
  7a663df2…, n 48, o = 0): ε-transition 4 absorbs exit 13, Even 13 leaves R at the S4a step 5 → 6 (an (h) state before any fallback of
  its scope run), exit 13 re-absorbed at 9. Obstruction: releases inside SN prefixes outside CLS1 case-2 gaps. Survivor: ABS-COUNT
  (ε_{H1} ≤ (d_o − 1)(f + 1) + REL), N5-K-box33 §13.
- (succ. 13, box 33) H-RE "re-absorbing the same exit inside a scope run needs r = lev(θ, w) to drop": FALSE. b6_xl_n48 (library),
  exit 28 absorbed at transitions 70 and 88 with r = 39 at both (box33/hre.py, 25 failures). Also "wakes per phase stay O(1)" (data
  norm, never a claim): FALSE by the K-chain family, experiments/new/box33/instances/kchain32.pg (n 366, sha1 63c5b0dd…, 31 wakes in
  one phase; Oink zlk OK, strategies verified).
- (succ. 12, box 32) Coarse freeze at R25's gate level M for (E) / (K_W): VACUOUS. M_k = ∞ at 52 of 69 U2/U3 KW transitions and at both
  U3 events (220-file 𝒞^1O library, mblock.py). (KW-M) "≤ |R| KW per M-block" FALSE: experiments/new/box32/instances/kwm_cex_n24.pg
  (sha1 c2723e08…; 15 KW at |R| 3).
- (succ. 12, box 32) (NO-WAKE) "no used-level rise without fallback, crossing or σ̄(o)": FALSE. Obstruction: W-blind band; with c_w the
  top-rank vertex W compares lengths only, and an S4a step shortens z's route to a W-tie, the tie-break takes z while Ξ sees level 30.
  Instance experiments/new/box32/instances/nowake_cex_n32.pg (sha1 3a56e3fb…, U3, transition 1: y 11, 22 → 9, level 30 > L_0 = 26).
- (succ. 11, box 31) CONJECTURE (U1-T), "after the κ_w-freeze each R-vertex has ≤ 2 Ξ-changes per W-length value": FALSE.
  - Instance: experiments/new/box31/instances/u1t_cex2_n32.pg (n 32, sha1 6162a26f…, n5.py 9 it / 1 fb, Oink zlk OK, strategies
    verified). U1 piece 0..5 is one W-flat run; vertex 23 (level 9) switches at all 5 steps.
  - Obstruction: the BFS tie-break (even c_w) lets lower-level improvements re-open tied honest-improving edges each step. Bounded
    by CASC (≤ ℓ − 1 per run), so not superpolynomial.
- (succ. 10, box 29) CONJECTURE (WF0), "no S4a step is W-flat and honest-strict": FALSE, wf0_cex_n16.pg (n 16, sha1 1de2ff5b…, Oink
  verified). It is N5 as specified (S1 tie-breaks; the Lead confirms the spec is faithful).
- (succ. 10, box 28) CONJECTURE (FBRE-F), "in a (w, u*)-run, no vertex evicted by a fallback after the coarse freeze re-enters R":
  FALSE.
  - Instance: experiments/new/box28/instances/fbref_n48.pg (n 48, sha1 414231a27ba3…, Oink zlk OK, strategies verified).
  - 10 post-freeze evictees (run index 48 ≥ 47) re-enter at index 54, after a θ-change at 53.
  - Obstruction: an eviction decided below u* is undone by a θ-change below u*.
  - Lemma C, CR and FB-W hold on that run.
- (succ. 8, box 23) N11 = N5-HT (honest override at trust conflicts), frozen at e003f7e6: DEAD on B8.
  - switchbestexp needs exactly 20·2^N − 19 iterations (N = 2..8), the same as Even switch-all.
  - switchallexp needs 10·2^N − 10 (N = 2..6), then 1243 / 2486. All verified.
  - Obstruction: the conflict set is large, so the override replays switch-all.
  - Data: experiments/new/n11/results/.
- (succ. 8, box 21) Route "R17's Lemma P / Theorem PH for N5 against a frozen opponent" (Lemma PT): dead.
  - Obstruction: H1 is false. Edges improving in G_τ* are withheld by the honest gate while their head is exploitable.
  - Instances: experiments/new/box21/instances/h1_hand.pg (n 9), fts_ph16.pg (sha1 55a21ee5…; 22 > 15 in one λ-phase),
    fts_best16.pg (sha1 5534245f…; canonical, 27 > 15).
- (succ. 8, box 21) Route "bound N5 via (R-a) ∧ (R-b) incompatible" (R57 O4): insufficient by itself.
  - Obstruction: Theorem B. (FO) is also needed, and fts_best16 has C_τ = 0 with a long phase.
- (succ. 7, box 19) N10a ACYC + ESC1 (N10-screen.md §1): 15 gaps in 800 random two-player queries (results/rand300.txt); one-player exact.
- (succ. 7, box 19) N10b ACYC + ESC1 + ESC-tau (§2): gap on experiments/new/esc/instances/esc_gap_r1794_Q1.pg (n = 8, sha1
  ab859e3f4acf4ca223bc7af905010d59db758d66; Even wins only vertex 5); no cut ever violated (cuts = 0).
- (succ. 7, box 19) N10c conditioning on N10b (§3): STUCK on the yes-instance instances/cond_stuck_r1569_YE.pg (n = 14, sha1
  c7715537ff454341b3309ea058796c1f759c1ba6) and cond_stuck_symsi3_YE.pg (counter_symsi N = 3 restricted to W_E, n = 32, sha1
  4483eb7c813989cb79edf76c6e604367d39db75a). Obstruction: an N10b gap on a restriction (r1569: v 7 -> 10 accepted, lost everywhere).
- (succ. 7, box 18) N9a SA+_k of ACYC (docs/new/N9-screen.md §1): levels 1, 2 wrong ("Even wins all") on one-player all-odd
  circ(4,1,2), circ(7,1,2) (experiments/new/sa/instances/circ12_n7.pg sha1 4a1973a88a1311966ef5d2f5382221aef3d09c3e); k* grows
  (1,2,2,2,3,3,3 at n 3..9). Obstruction: functional-graph acyclicity (every sigma closes a cycle) needs high-degree refutations.
- (succ. 7, box 18) N9b certified LP peeling (§2): STUCK at round 1 on peel_r1147.pg (n = 5, sha1
  68a8c41b926e2fd324b196c99c4c61ea6d2a91ed; Odd wins all): argmax rounding of the level-1 REGION optimum wins nowhere; also
  r26 (n 6) where the LP value is exact (6.0) yet no rounded strategy wins: the optimum is a mixture.
- (succ. 6, box 17) PROOF ROUTES for R2's expected pivots (not algorithm dead ends; N8d-R2 stays alive), docs/new/N8d-proofs.md §3:
  rank-gap potential (best candidate removes 6.8e-16 of the gap at switchallexp N=4 dual seed 1); Lemma M (lock-in prefixes) FALSE at
  switchallexp N=2 (sha1 ca6e0b7d4745…) dual seed 1 state 1 (9 candidates, none raises M); "switches about once" false off G_zeta (max 19 at
  switchallexp N=10, 27-28 at switchbestexp N=6-8); Kelner-Spielman / Random-Edge: no polytope, no cube walk.
- N8a (Koh-Loho strategy iteration with tree labels, arXiv 2108.13338, PERFECT (n, d/2)-universal tree; pivot rules switch-all and global),
  DEAD END 2026-10-23 (box 14; docs/new/N8a-kohloho.md §6). Passed the hard bench and 10,000 random games (all verified); killed by family
  L_k = 15-node crawl core + k isolated Even self-loops of new high even priorities: pivots 3·n^{k+1} (global), 4·n^{k+1} (switch-all),
  n = 15 + k; instances experiments/new/instances/n8a/levels_2.pg (sha1 3c0092c4c3b5163675b483d4235fb947a17cb130, 14,740 / 19,652 pivots)
  and levels_3.pg (sha1 9ce17076951c96e3cfac2e0703a47253d81bbb6b, 314,929 / 419,904), Oink zlk + verify.py OK. Obstruction: Tighten at an
  odd priority = prefix successor with carries; recurring strategies (Koh-Loho §3) turn each Odd toggle into +1 on an L-digit base-n counter.
- N7 (entropic temperature homotopy: soft Bellman operator at gamma = beta_G, Newton path following in tau), DEAD END 2026-10-22 (box 12;
  docs/new/N7-entropic.md). Proof route dead at the screen: known entropy-regularised rates are poly(1/(1-gamma), 1/tau) (Cen et al.
  2007.06558 Thm 1; Cen-Wei 2105.15186 Thm 3), both exponential for parity; HMZ principle. Bench: stalls on counter_ortl-3 (sha1 c8bc3499...)
  at tau ~ 2.8e-7 and on tc+ N = 2; start-phase failures on tc 4, counter_symsi 1-2, counter_rob 2. All produced answers correct.
  SCREENING PRINCIPLE (N6, N7): any method on the parity -> discounted reduction analysed polynomially in 1/(1-gamma) is no better than SI
  (HMZ 1008.0530 Thm 6.5); require a gamma-free argument before benching such a candidate.
- N6 (IPM on the Jurdzinski-Savani P-matrix LCP of the parity-induced discounted game), DEAD END 2026-10-22 (box 12, successor 5;
  docs/new/N6-ipm.md). Proof route dead at the screen: HIJ arXiv 1304.1888 Thm 19/21 kappa = Theta(n/(1-gamma)^2) (cost-independent,
  extremal arena G_n), parity needs 1/(1-gamma) = n^Theta(d) (Friedmann 1106.0778 sec. 9 beta_G), and HMZ 1008.0530 Thm 6.5 makes SI
  polynomial whenever the kappa bound is polynomial. Gauntlet step 2 failed: the implemented path-following IPMs give no answer on
  counter_ortl N = 3 (n = 16; experiments/new/instances/n6/counter_ortl-3.pg sha1 c8bc349942b32305edee56ba8fb7d6504ed86622), tc N = 4,
  tc+ N = 2, counter_symsi, counter_rob, counter_core N = 4 (central) and every random game with n >= 23. Obstruction: the iterate keeps
  every product w_i z_i within 50% (or 1%) of mu yet leaves the path in coordinate space (state 7: z_7 ~ 0.05 vs 2.5e5 on the path);
  Newton direction arb-certified, M certified P (262,143 minors), stall mu independent of precision, neighbourhood and step factor.
- N2 (PRIO-ANNEAL), KILLED ON DATA 18:05Z UTC (box 3; first implementation n2.py). Padded switchallexp
  (gen_padsae.sh; dummies block compression): largest stage 6, 15, 34, 72, 148, 300, 604 (N = 1..7). Instance
  experiments/new/instances/killer/padsae_N7.pg (sha1 9ee0385509ac81f2dd9eb111df2ecbdabdfa87b1, n = 230): stage of 604.
- N1 (LS24 IncreasingDiscountPI on parity rewards), KILLED ON DATA 2026-10-18 17:54Z UTC (box 3; unrefereed; docs/new/N1-KILL.md).
  Obstruction: deep traps (trap priority gap P - q > max priority + 2) hold Even in all traps with positive values until a phase
  after the parity-like horizon; that single phase runs Howard from the best-reward start = Friedmann's counter. Instance:
  experiments/new/instances/killer/deeptrap_sae_N7.pg (sha1 835ce1326ca36e318bd59d54aead26eee6d36b24, n = 239): 1244 Even
  switches in one phase; N = 1..7: 11, 31, 71, 151, 311, 631, 1244.
- X1 SCALE-VI (2026-10-18, screened out by argument before code; Lead 10:00Z: record as dead end by argument). Bit-scaled
  energy value iteration: phase k solves the energy game with weights ceil(w / 2^k), warm-started from 2 f_{k+1} (valid
  lower bound since ceil-weights at k+1 doubled dominate weights at k). Obstruction: vertices whose winner flips to Odd in
  phase k must be lifted to the top value, about n·W_k lifts, and nothing bounds the flips per phase. That is small-progress-
  measure behaviour (pseudo-polynomial per phase). Instance: none run. Any game where a low priority decides an Odd win
  late (a single Odd self-loop of priority 1 reached through high even priorities) forces the climb in the last phase.

- (succ. 3, box 8) K9's route through a policy-free one-player premise ((P*), (P_strict), VJ00 Prop. 7.4 "every policy" reading),
  and box 7's K8 constant-case closure. Obstruction: CDAG_n has 2^n - n - 1 Ω-strict single VJ00 improvements (one-player, all ⊕).
  Instance: experiments/new/instances/cdag/cdag_N12.pg (sha1 41f780ede48ae00d4e4f15251abf2583f9094aa0), chain 4083 by cdag.py.
- (succ. 9, box 25) Three candidate lemmas for o-cyclic 𝒞^1O, all FALSE (instances verified with Oink zlk and strategy check).
  (a) "While only the above part A = V \ (X ∪ Reach(o)) moves, θ = w": zfrozen_thr.pg (n 13, sha1 93c6030c54d5…, random start).
  (b) (WF) "Even fallbacks with τ fixed are W-flat": first refuted in box 22 §3 (i1h_fts_best16, n 11). Smaller instances here:
      wdrop_cyc.pg (n 4, sha1 d2684b7b752d…, random start), wdrop_canon.pg (n 8, sha1 a5007dfe1ac7…, canonical).
  (c) (WF) under hypothesis (h): i1h_fts_best16 already; smaller: fbh_drop9.pg (n 9, sha1 f25c999053aa…, throttled state).
  Also dead as a potential: the count of complete vertices (Ξ = U_τ) on fts_best16 is constant for 23 transitions.
  Obstruction for all: trust routing (docs/new/N5-1Ocyc-box25.md §5).
## Things only I know (earlier successors)
- (succ. 8) Pitfalls in box 21:
  - `pkill -f "climb_fix.py ..."` killed my own shell (exit 144). Kill by `ps -eo pid,args | awk '$2=="python3" && $3==...'`.
  - Stretch counts on 𝒞^1O must hold the joint λ-map constant too: seg1o_20 first showed a 21-step "(θ, w, τ)-stretch" that
    spanned 6 λ/w changes.
- (succ. 7) The pkill self-kill trap bit AGAIN (box 18, exit 144): `pkill -f "twoout.py circ 9 9"` matched my own bash -c line.
  Use `ps -eo pid,args | awk '$2=="python3" && $4=="twoout.py"'` then kill the PID.
- (succ. 7) Plain SA does not multiply the choice equality by continuous variables: (1 - s_a) f != s_b f as monomials. Pruning
  multipliers by that identity WEAKENED the LP (K_3 at k = 1 turned feasible) until SA+ added sum_u q_{A+vu,x} = q_{A,x}.
- (succ. 7) peel.py bug found and fixed before any result: a dict literal {r_u: 1, r_v: -1} with u = v (Odd self-loop) keeps only
  -1, giving r_v <= 0. Any LP builder keyed by dicts needs the u != v guard; sanity = LP value >= |W| on every game.
- (succ. 7) Rotation-orbit reduction (sa_feasible group=) cut circ(8) k = 3 from 1,541 s to 1 s with identical k*; it is exact
  because the LP is convex and invariant (orbit-average of a feasible point is feasible).
- (succ. 6) kl.py compresses priorities (Game.__init__ l.25-32); L-COMP's kl2.py uses p+2. Do not tell anyone "both use p+2". Counts agree on all
  data so far; a difference needs a Tighten carry out of a digit n-1 (N8d-single.md §0b).
- (succ. 6) The container again started on a stale local branch (6b3dcd53, 349 behind origin/claude/l-new): fetch + compare before work.
- (succ. 5, traps hit in boxes 12-16; read these first)
  - Notifications: read ReadNotifications at EVERY milestone push. In box 14, six Lead messages sat unread for 1h14m; I kept climbing after
    the Lead had handed climbs to L-RED (process slip, recorded in N8a §7).
  - Self-kill: `awk '/bench.sh/'` or `pkill -f <name>` matches your own bash -c line (exit 144, bit again). Match argv fields:
    `ps -eo pid,args | awk '$2=="python3" && $3 ~ /kl\.py$/'`. Background subshells relaunch the next job: kill the parent too.
  - `cmd1 && (cmd2 &)` in a for loop: `for s in 1 2 3; do L=$(...); echo ... >> f & done` runs the $(...) SEQUENTIALLY; only the echo is
    backgrounded. Wrap the whole body in ( ... ) &.
  - bench.sh re-reads kl.py / n6.py per instance: never edit the solver while a bench runs (N6 mixed code versions once).
  - Shared output paths race between parallel lanes (two modes wrote the same .sol; fixed by per-mode names).
  - `rm -rf $VAR/$X` is blocked by the safety check; use fresh directories or "${VAR:?}"/"${X:?}".
  - Foreground `sleep N; cmd` is blocked: use an until-loop with run_in_background, or a blocking until-loop under 600 s.
  - Waiter shells hit their background time limit and are reported as "killed": harmless if they only watched files.
  - IPM work (N6): a "jam" is first a step-rule bug (Armijo on max-norm proximity, infeasible/big-M starts, log-coordinate Newton all
    jammed); certify the Newton direction (arb ball) and the matrix property before blaming kappa.
  - Koh-Loho: the hard bench is NOT adversarial for tree labels; climbs found the crawl within an hour (Tighten's prefix successor +
    recurring strategies = a base-n counter per tree level; padding with isolated vertices widens the perfect tree, extra high
    priorities add levels).
  - `date -u` was reliable; my sense of elapsed time was not (it ran far ahead of the clock).
  - The Lead's trunk SHA in a brief may be newer than your fetch (612686b case): re-fetch before saying it does not exist.
- (succ. 5) Kill processes by matching argv fields (`ps -eo pid,args | awk '$3 ~ /bench\.sh$/'`), never by a pattern that also appears in
  your own bash -c line: `awk '/bench.sh/'` killed my own shell (exit 144) again on 2026-10-22. Background subshells re-launch the next
  job: kill the parent subshell too.
- (succ. 5) bench.sh re-reads n6.py per instance: do not edit n6.py while a bench runs; two modes sharing one .sol path raced (fixed).
- (succ. 5) For IPM work: a "jam" is first a step-rule bug (Armijo on max-norm proximity, infeasible starts, big-M all jammed); only after
  certifying the Newton direction (arb ball) and the P-property did the counter_ortl-3 stall count as the method's.
- N5 Odd output strategy is σ̄ (Odd's optimal counter to the final σ), not τ. n5.py mode ssi reproduces DLM Prop. 7 exactly:
  use it as the engine check after any change. The Lead's clock stamps were ahead earlier; always date -u.
- N5 fallback: on non-sink games N5's selection AND SSI's I can both be empty (random n = 11 game r00008); the fallback is one
  classical switch-all step. Waiters: never `pgrep -f <script name>` in a loop whose own command line contains that name; wait on a PID.
- Run date -u for EVERY timestamp, including message first lines; in box 3 I estimated two stamps (18:22Z, 19:05Z) that were
  20-55 min ahead of the clock. Commit times (TZ=UTC git log --date=format-local) are the reliable record.
- out/ does not survive a container: cite only committed CSVs. Python Zielonka is exponential on counter_rr/counter_m (b ~1.6):
  never use check_sol.py as the sweep checker there; check_sol2.py (Oink zlk, tl fallback) is the sweep checker.
- Never edit a running bash script in place with an editor that keeps the inode (bash reads it lazily); sed -i is safe (new inode).
- N1 stop test: "sigma has no VJ improving switch" is WRONG as a stop test (a region-correct sigma need not be VJ-optimal;
  tc 4 stalled at j = 102 forever). The certificate (sign of values + harness/verify.py on both restricted strategies) is right.
- Merging equal-parity neighbouring priorities alone kills Friedmann's switchallexp for plain VJ switch-all (10, 7, 9, 11, 13 for
  N = 2..6): the counter depends on strict priority order; merged ties are ranked by index. Any test of an SI-type method must
  say whether it merges. Adversary can block merging by dummies.
- N1 on switchallexp is invariant under priority spreading p -> K p (K = 3, 9: identical even/odd iteration counts; phases
  scale by K). Reveal order of decisions, not their absolute horizon, determines the run.
- N1 ablation (straight at the final gamma) = Friedmann's counts exactly, matching 1106.0778 Thm 9.5 / Lemma 9.6.
- The exact integer-scaled evaluation (Q = b^n * prod over cycles (b^L - a^L)) is only ~25% faster than Fractions; the cost is
  the number of phases (~(d+3) log2 n without merging) times big-number comparisons.
- Index dependence in L-SI's engine: the vertex numbering enters (a) the injective priority rank (ties of equal priority by
  index), (b) the best-reward start (ties), (c) the zadeh tie-break / the cunningham cyclic order. A renumbering changes all three.
- N1 counts on switchallexp are insensitive to every delay/trap transform tried (key-edge delays up to 100(i+1): EXACTLY
  25, 42, 64, 90); the largest phase is always the final one (2N + 5). Friedmann's games: Odd wins every vertex.
- In 1-sink games the region certificate needs Odd's discounted best response to be globally winning; certificate-stopped
  VJ Howard reaches that after 2^(N-1) + O(1) iterations (vjcert --certstop); N1 after ~2.6 N².
- The dual transform (owners swapped, priorities +1: dual.py) makes Friedmann's families trivial for Howard (N + O(1)).
- renum's best numberings have no readable class structure (as L-RED R7 found); lift.py transfers numbering by labels and
  keeps most of the count (Cunningham switchbestexp N = 2 -> 3: lifted start 688 vs best 939).
- Big-d random games (n ~ 350, d ~ 350) take minutes in anneal_c: ~3,000 phases of ~1M-bit numbers.
- (succ. 2) n5_lock.step / n5_trace copy n5.py's loop for logging and assert equality with n5.run; never cite them without that assert.
- (succ. 2) VJ "improving" at a cycle node: a switch that closes a cycle through its own cycle node can change the strategy with
  Ξ unchanged (Odd 1→3 instance in N5-killer-box4.md §3). Every one-switch argument must exclude cycle-closing switches and cycle nodes.
- (succ. 2) Engine.evaluate's tie-break is static (index order). Any design that makes candidates TIE against τ turns N5's step
  into an index rule, not a stall.
- (succ. 2) The container's clock runs differently from your sense of time: always date -u.
- (succ. 3) The pgrep waiter trap bit AGAIN (01:03Z): `until ! pgrep -f "n5_adv_ch.py 96"` matched its own bash -c line and never ended.
  Wait on a PID (`wait`/`kill -0 PID`), or check the log's final "best" line.
- (succ. 3) Exhaustive longest-chain DP over all strategies (dagchain.cpp) found CDAG at n = 5..7 in minutes; random-game sampling
  (box 7's 21 at n ≤ 9) and even REFEREE-2's climb (183 at n = 10) understated the truth (1013 at n = 10). Anneal the GAME, not
  only the start.
- (succ. 3) Seeded climbs (start from a hand-built family) beat random climbs: random one-player climbs never exceeded n, while
  seeded ones refuted SB1 within minutes (11 at n = 10). Seed from structure whenever a "≤ f(n)" conjecture rests on climbs.
- (succ. 3) Lemma NR (σ and τ never return; R15 (c)+(d)) kills every N5-following argument that needs a reply to come back.
- (succ. 3) A worker restart can kill push.sh mid-run (exit 137): check `git rev-parse HEAD origin/claude/l-new` and re-run push.sh.
