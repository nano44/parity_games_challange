# Handover check: L-SI (successor 9, written 2026-10-25T18:12Z by date -u; LANE-RESTART step 3; Opus 5.5, D18/L40)
Every answer below was measured in this container; the commands are given. Predecessor: successor 8, session_013kZp65x9TKU9AqPZdMYGpm.
Its handover is e683a4c0, notes/L-SI.md "## HANDOVER (successor 8, box 13)".

## 1. Branch, head, distance to trunk
- Branch `claude/l-si`. `git fetch origin claude/l-si` moved origin 0d48da26 → e683a4c0 (the local clone was stale at 0d48da26);
  `git checkout -B claude/l-si origin/claude/l-si`; `git rev-parse HEAD origin/claude/l-si` → both e683a4c0.
- Trunk `origin/claude/vibrant-johnson-nxvvxo` = e6ee6130 (Lead 18:06Z "P-N5-NEEDB pinned").
  - Before merging: `git rev-list --left-right --count HEAD...trunk` → 1 ahead / 12 behind; merge-base 680c0294.
    The 1 ahead is e683a4c0 (succ. 8 handover); everything up to 680c0294 is on trunk already.
  - `git merge --no-ff` of trunk (no rebase) → 2 ahead / 0 behind (the handover commit + the merge). This file is the next commit.

## 2. Open work and the next step of each (nothing running: `pgrep -a python` empty; fresh container)
Frozen files, re-measured with sha1sum: P-N5-ENT 4fd22be7, P-N5-LV d0d797f0, LV-addendum a15a8871, LV-fixes b75ab1fc,
P-N5-LV2 3b23a41f, LV2-fixes f76fd1d1, N5-LV2 94ac2469, P-N5-NEEDB 7471aef3, N5-RISE 3b8fea13, N5-A2STAR 2a85601d.
- P-N5-NEEDB (docs/si/P-N5-NEEDB-box13.md, 7471aef3): PINNED on trunk e6ee6130 (`git show trunk:… | sha1sum` = 7471aef3),
  queued for both referees after NHN (LEAD-STATE 18:06Z). To sign: XG, ANTI, NEED-β (all cases incl. A2*), OLD-THREAT, INTO ⇒ no case
  (i) fallback. No referee report yet (no R-N5-NEEDB / R2-N5-NEEDB on trunk).
  - Next step: when reports land, items go to a NEW file docs/si/P-N5-NEEDB-fixes-box13.md (does not exist).
- P-N5-LV: LANDED as RESULTS R41. P-N5-LV2 + fixes (f76fd1d1): REFEREE signed (b454ca3, Add. 46a8030, §C ed8bc207), REFEREE-2 a551deb;
  landing is the Lead's/CHECKER's. Next step: none for me unless a §C item arrives (→ a NEW file).
- Rise question (docs/si/N5-RISE-box13.md):
  - case (i), r > L up to a later fallback: reduced (PROVED, succ. 8, via FBL) to CONJECTURE INTO (425/425 library states). OPEN.
  - case (ii), r ≤ L before the next fallback: OPEN, untouched. L-RED box 41 attacks both (Lead 17:25Z).
  - Next step: a proof attempt of INTO, if the Lead routes it.
- LV-NONE sharpening: DATA max 1 u* = none fallback per scope run in 8 climbs, but beta2_n11 (L-RED) has 2 (eviction cascade).
  CONJECTURE (reading): count ≤ cascade depth (≤ depth of R). Next step: state and try to prove a cascade-depth bound.
- "THR ⇒ M ≥ 0" in scope: OPEN; NEED-β pins the shape a counterexample needs ((β) gates on every reply).
- G-N5-TIME items not this lane's alone: θ_ph, HN stretches for τ(o) ≠ o, OTHER states, REL(S), phases.
- The choice among these is the Lead's (succ. 8 NEXT 2); I wait for "go".

## 3. docs/GAPS.md rows I own
- None (`git show trunk:docs/GAPS.md | grep -n L-SI` → no owner column = L-SI).
- I work under G-N5-TIME (l.11): major, owner L-NEW (L-LIT T22; referees later), status open. NOW l.2: "NO polynomial bound for N5
  is proved."
- G-N5-TERM (l.16): closed (R15).

## 4. The three owner rulings that constrain me most (verbatim from docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md)
- D18 (DECISIONS.md l.332; index l.32: active): "Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
  where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
  open problems."
  - Lead reading L40 (index l.33: active) (2)d: L-SI is the OR/MDP policy-iteration lens on N5.
- D1 (index l.5: active; DECISIONS.md l.3, full text docs/decisions/D001-launch-brief.md l.25, l.96):
  "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
  as wrong until it passes the gauntlet below." / "Never publish, post, email, submit or contact anyone outside the fleet. Anything
  external is my decision."
- D16 (DECISIONS.md l.299; index l.28: active): "Then keep working as I told you to"

## 5. One trap that bit this lane before, and the check that prevents it
- Trap: a stale clone. This container's local claude/l-si was at 0d48da26 (successor 0's box end, Oct 16), ~13 boxes behind origin
  e683a4c0, and `git status` alone would not have shown it before the fetch.
  - Check: `git fetch origin claude/l-si` + `git checkout -B claude/l-si origin/claude/l-si` + `git rev-parse HEAD origin/claude/l-si`
    equal, before reading any notebook. Same again (fetch + merge, never rebase) right before every push.
- Still live: never edit a frozen file. Before touching docs/si/P-* or *-fixes-*, `sha1sum` it and grep notes/L-SI.md, docs/NOW.md and
  docs/agents/LEAD-STATE.md for the sha1; if listed, new text goes in a NEW file.
- From succ. 8: `until ! pgrep -f X` never ends (matches itself), wait with `while kill -0 PID`; absolute paths in multi-line Bash;
  never `git add -A`; never pipe scripts/push.sh (redirect to a file, print $?).

---

# Handover check: L-SI (successor 8, written 2026-10-25T15:36Z by date -u; LANE-RESTART step 3; Opus 5.5, D18/L40)
Every answer below was measured in this container; the commands are given. Predecessor: successor 7, session_01Nosb1KbEcKX2yMZfBES2sA.
Its handover is 0756713c, notes/L-SI.md "## HANDOVER (successor 7, box 12)".

## 1. Branch, head, distance to trunk
- Branch `claude/l-si`. `git fetch origin claude/l-si` moved origin 0d48da26 → 0756713c (stale clone); then
  `git checkout -B claude/l-si origin/claude/l-si`; `git rev-parse HEAD origin/claude/l-si` → both 0756713c.
- Trunk = claude/vibrant-johnson-nxvvxo at 283bcb67 ("Lead: P-N5-PFZ and P-N5-LV2 pinned; referee queues; NOW, log").
  - Before the merge: `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` = 1 ahead / 23 behind;
    merge-base ed936af1 (the P-N5-LV2 commit; only the handover commit 0756713c is not on trunk).
  - `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` (merge commit 77c56476 "L-SI succ. 8: merge trunk 283bcb6") → 2 ahead / 0 behind.
  - First push rejected: successor 7 pushed a6378fc1 (15:34Z, notes NEXT update) after my fetch. Merged --no-ff. The pushed head SHA
    is in the message to the Lead.

## 2. Open work and the next step of each (nothing running; fresh container)
sha1s re-measured with sha1sum on my tree and with `git show <trunk>:<path> | sha1sum`; all match, all FROZEN.
- P-N5-LV2 (docs/si/P-N5-LV2-box12.md, 3b23a41f): pinned at trunk (Lead 15:29Z commit). REFEREE succ. 9 queue: NEB (working), then
  PFZ (3c617e06), LV (d0d797f0 + addendum a15a8871), LV2 (3b23a41f). No R-N5-LV2 / R2-N5-LV2 yet.
  Contents: STALE-GATE, EV-G, ENT-X_{−1}, LV-PL′, SAND, FLAT-ALL_{−1}^{none}, LV-NONE, SCOPE-FB (≤ 4·n·n_E + 3 fallbacks per scope run;
  CONDITIONAL on P-N5-ENT PL-S″, P-N5-LV, N5-LV4). Next step: referee items go to a NEW file docs/si/P-N5-LV2-fixes-box12.md.
- P-N5-LV (d0d797f0 + a15a8871): queued at REFEREE 9 (and REFEREE-2). Next: items to a NEW docs/si/P-N5-LV-fixes-box11.md.
- P-N5-ENT (4fd22be7) + fixes file docs/si/P-N5-ENT-fixes-box11.md (72d052b5): both referees converged (R-N5-ENT §C d6b8aef: R36 lifts
  (P)); G-N5-TIME 15:09Z says "P-N5-ENT converged, landing next" (Lead drafting R40). Next: nothing unless CHECKER asks.
- Lane write-ups (unrefereed except via LV2): N5-LV3 (20ba05d7; NEED-β case A2* OPEN, "THR ⇒ M ≥ 0" CONJECTURE), N5-LV4 (9d1b90f4),
  N5-LV5 (e2cb0703). Next (optional, predecessor NEXT 2): case A2* via ANTI-W on the cycle K′ (first idea, unchecked).
- Research item (Lead 15:34Z, relayed in successor 7's late push a6378fc1, merged here with --no-ff, no rebase): NEED-β case A2*
  (N5-LV3 §3) is approved as the next item. If A2* stalls within ~45 min, switch to the Lead's D18 suggestion: prove unconditionally
  REFEREE-2's DATA observation "after a rise with r > L the scope run has no further fallback" (62 library + 26,665 climb cases), which
  would make ENT-X independent of EV+ and FREE-FREEZE. Next step after "go": A2* via ANTI-W on K′, checked against betasearch.py
  corpus mode; 45-min stall clock from GO.
- Predecessor NEXT 3 (θ_ph, HN stretches for τ(o) ≠ o, OTHER states, REL(S), S4a steps): not this lane's alone; only on Lead routing.

## 3. docs/GAPS.md rows I own
- None. `awk -F'|' '$5 ~ /L-SI/'` over trunk docs/GAPS.md finds no row owned by L-SI.
- The row I work under is G-N5-TIME: major, owner L-NEW, status open. Latest update 15:09Z: R39 [refereed-only] LANDED (P-N5-OUT);
  "Open: θ_ph, HN stretches for τ(o) ≠ o, OTHER states, NJB = ENT (P-N5-ENT converged, landing next), REL(S), level −1. Lane
  (unrefereed): P-FREEZE / BRK-POLY (L-NEW 18), STALE-GATE / LV-PL′ (L-SI 7)."
- G-N5-TERM: closed (R15).

## 4. The three owner rulings that constrain me most (verbatim from docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md)
- D18 (index line 32: active; DECISIONS.md l.333): "Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
  where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
  open problems."
  - Lead reading L40 (index line 33: active): L-SI is the OR/MDP lens on N5.
- D1 (index line 5: active; DECISIONS.md l.6-7):
  - "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
    as wrong until it passes the gauntlet below."
  - "Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision."
- D16 (index line 28: active; DECISIONS.md l.300): "Then keep working as I told you to"

## 5. One trap that bit this lane before, and the check that prevents it
- Trap: a stale clone. This container's `claude/l-si` sat at 0d48da26, three commits behind origin (the box-12 packet and handover were
  missing). Working from it would have re-opened frozen files or missed P-N5-LV2 entirely.
- Check: `git fetch origin claude/l-si`, reset, `git rev-parse HEAD origin/claude/l-si` equal; then sha1sum every frozen file against
  the sha1s in notes/L-SI.md and against trunk (done above: LV2 3b23a41f, ENT-fixes 72d052b5, LV3 20ba05d7, LV4 9d1b90f4,
  LV5 e2cb0703, LV d0d797f0, ENT 4fd22be7 — all match).
- Still live: frozen-once-reported files (new text in NEW files); never `pkill -f` a pattern in one's own command line (exit 144);
  ReadNotifications after every push (successor 7 missed two relays for ~35 min); `git log -- <path>` > 120 s; add files by name;
  fetch and merge (never rebase) before push; token count from the session counter, not an estimate.

---

# Handover check: L-SI (successor 7, written 2026-10-25T13:58Z by date -u; LANE-RESTART step 3; Opus 5.5, D18/L40)
Every answer below was measured in this container; the commands are given. Predecessor: successor 6, session_01WZRciyMqz1LNWwdFoeq2AP.
Its handover is dbef1de6, notes/L-SI.md "## HANDOVER (successor 6, box 11)".

## 1. Branch, head, distance to trunk
- Branch `claude/l-si`. Commands: `git fetch origin claude/l-si`, then `git checkout -B claude/l-si origin/claude/l-si` → head dbef1de6.
  - This container's local branch was already up to date with origin, unlike successors 4-6. The fetch moved origin 0d48da26 → dbef1de6.
- Trunk = claude/vibrant-johnson-nxvvxo at 601df6ed ("Lead: R36 LANDED (P-N5-P1, CHECKER C45 3667fb1c); GAPS; P-N5-LV pinned; NOW, log").
  - Before the merge: `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` = 1 ahead / 55 behind;
    merge-base b7f18feb.
  - `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` (merge commit "L-SI succ. 7: merge trunk 601df6e") → 2 ahead / 0 behind.
  - My first push of this file (2e1a7c29) was rejected: successor 6 had pushed 84974fea at 13:55Z (P-N5-LV addendum).
    `git merge --no-ff origin/claude/l-si` brought it in (no rebase).
  - The second push was rejected too: successor 6's handover update 95fb6d0c (14:01Z) had landed while verify ran (~9 min). Merged it
    the same way. The pushed head SHA is in the message to the Lead.

## 2. Open work and the next step of each (nothing running; fresh container)
The frozen files and their sha1s are re-measured with sha1sum.
- P-N5-ENT (docs/si/P-N5-ENT-box11.md, 4fd22be7):
  - REFEREE succ. 8 report docs/referee/R-N5-ENT.md is on trunk. It signs §1-§3 (FZ, BF, RB, WALK, CYC-EV, TEV-FB). It signs §4-§5
    (ENT-X, NJB-A, D1, PL-S″) CONDITIONAL ON (P). There are no gaps and §6 is not signed.
  - R2-N5-ENT: not on trunk or on origin/claude/referee-2. It is with REFEREE-2 succ. 9 (NOW roster; Lead 13:54Z per successor 6's
    14:01Z update).
  - Since R36 has LANDED (Lemma P1 = (P) for one-player games), the (P) condition should lift once ENT lands. READING, to be confirmed by
    the referees/CHECKER.
  - Next step: any items go to a NEW file docs/si/P-N5-ENT-fixes-box11.md (does not exist).
- P-N5-LV (docs/si/P-N5-LV-box11.md, d0d797f0): pinned on trunk and queued after NEB (NOW). No R-N5-LV / R2-N5-LV yet.
  - Addendum docs/si/P-N5-LV-addendum-box11.md (a15a8871; successor 6, 84974fea; answers Lead 13:51Z) is on trunk too (`git cat-file -e`).
    - It points to the (β) bound already in the packet (PL_{−1} / LV-PL cover (β)-fallbacks with r ≥ 0).
    - It marks the NL= straddle material NOT TO SIGN.
  - Next step: items go to a NEW file docs/si/P-N5-LV-fixes-box11.md.
- Level −1 (successor 6 NEXT 2; Lead's queue 13:54Z, research item 2), OPEN:
  - (a) THR fallbacks with u* = none (r = −1; NL at L = −1 is not available).
  - (b) A length-based ENT-SHAPE, to drop REL(S) from LV-PL ≤ n·n_E·(d_o + REL(S)).
  - (c) Or exclude a (β)-fallback, giving "THR ⇒ M ≥ 0" in scope (P-N5-LV §1/§5).
  - First step: (c) via the N5-LV §3 kill shape, checked against experiments/si/tev/lvm1.py. DATA so far: 1,032 in-scope THR, all M ≥ 0.
- NL= (straddle; N5-STR/STR2) CONJECTURE: off the critical path (Lead agreed). Only if cheap; it buys a factor 2.
- Not started from older successors: two-player VJ00 Lemma 5.8 (R15's G-N5T-3), the remaining half of (P).

## 3. docs/GAPS.md rows I own
- None. L-SI owns no GAPS row.
- The row I work under is G-N5-TIME: major, owner L-NEW, status open.
  - Last update 13:52Z: R36 [refereed-only] LANDED (P-N5-P1 + fixes, addendum §3; CHECKER C45). This discharges R18's premise (P) for
    one-player games only and "Adds no running-time bound. Open as before."
  - "Open as before" (11:51Z update): "NJB = ENT (CONJECTURE; lane reductions EV/EV+/TEV-RED in review as P-N5-RL), REL(S), level −1
    fallbacks, out-of-scope fallbacks (P-N5-SCOPE in review; lane NO-ENTRY-A), θ-changes per HN stretch."
- G-N5-TERM: closed (R15).

## 4. The three owner rulings that constrain me most (verbatim from docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md)
- D18 (index: active): "Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas
  of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them
  briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems."
  - Lead reading L40 (active): L-SI is the OR/MDP lens on N5.
- D1 (index: active; full text docs/decisions/D001-launch-brief.md). Key lines:
  - "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
    as wrong until it passes the gauntlet below."
  - "Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision."
- D16 (index: active): "Then keep working as I told you to"

## 5. One trap that bit this lane before, and the check that prevents it
- Trap: editing a packet or fixes file after its sha1 had already gone to the Lead. Several Lead messages crossed with successor 6's
  files, and referees pin by sha1 (R-N5-ENT checks `git show 765e893:docs/si/P-N5-ENT-box11.md | sha1sum` = 4fd22be7).
- Check: before touching any docs/si/P-* or *-fixes-* file, `sha1sum` it and grep notes/L-SI.md and docs/NOW.md for that sha1. If the
  sha1 is listed, the file is FROZEN and new text goes in a NEW file.
  - Today's frozen list: ENT 4fd22be7, LV d0d797f0, N5-LV 407c5520, N5-LV2 94ac2469, N5-TEV 58a0b3cf, STR c7b9c671, STR2 b6ed9476,
    RL-fixes ac027458, RL-fixes2 b3e3cd93, P1-fixes 83ef83b0, RL-P1-addendum 5c29d93d, LV-addendum a15a8871.
  - This bit me in this very check: my push crossed with successor 6's 13:55Z addendum. Fetch before pushing, and merge, never rebase.
- Still live from successors 5-6:
  - Never `pkill -f <pattern>` from a shell whose own command line contains it (exit 144).
  - `git log -- <path>` takes more than 120 s here.
  - Never `git add -A`; add files by name.
