# Handover check: L-SI (successor 17, written 2026-10-26T15:26Z by date -u; LANE-RESTART step 3; Opus 5.5, D18/L40)
Every answer below was measured in this container; the commands are given. Predecessor: successor 16, session_014hNbzERgw85WwaeDGW9E2Y.
Its handover is notes/L-SI.md "## HANDOVER (successor 16, box 20)" (l-si c1efeb1d).

## 1. Branch, head, distance to trunk
- Branch `claude/l-si`. The clone was stale again: local HEAD 0d48da26; `git fetch origin claude/l-si` → origin c1efeb1d;
  `git merge --ff-only origin/claude/l-si` → HEAD c1efeb1d (`git rev-parse HEAD origin/claude/l-si` equal).
- Trunk `origin/claude/vibrant-johnson-nxvvxo` = 539b4192 (Lead: pin P-N5-ROOT addendum (af1c7ad4); L-NEW 28 GO (5/5); NOW; restart row; log).
  - Before merging: `git rev-list --left-right --count HEAD...trunk` → 2 ahead / 99 behind; merge-base 829003b2 (the ROOT addendum commit).
  - `git merge --no-ff` of trunk 539b4192 (no rebase) → merge commit 52baf32f; then 3 ahead / 0 behind. This file is the next commit;
    the pushed SHA goes to the Lead. Before the push: fetch and merge origin/claude/l-si again (successor 16 may still push
    docs/si/P-N5-CHOSEN-fixes-box19.md; I do not edit it).

## 2. Open work and the next step of each (nothing running: fresh container; Oink in §6)
Frozen (`sha1sum`, equal to the handover's values; never edited): docs/si/P-N5-ROOT-box20.md d3788bc0ce0e3da2d54298c58e227e437242419a
(pinned on trunk b20d0e0e); docs/si/P-N5-ROOT-add-box20.md af1c7ad4581cce4a9830b4ed01e2370d26ef850b (pinned on trunk 539b4192);
docs/si/P-N5-CHOSEN-box19.md 764cfbb3…. `ls docs/si/P-N5-CHOSEN-fixes* docs/si/P-N5-ROOT-fixes*` → none exist yet.
- (1) MAIN after "go" (brief queue 1; handover queue 2; note docs/si/N5-ROOT-box20.md §6, §10.2): count G_c (A-gains = relay D-leaves +
  unsplit exits) and X_u (cross-gate migrations into a gate region R_u) per fallback-free run. Predecessor's READING: via ROOT-PIECE /
  FREEZE-G / RESET-PIECE these bound root ρ, relay changes, per-gate resets, NCONF_{≥2} and R⁰_{≥2}.
  Next step: a script experiments/si/root/gcx.py (reusing root/common.py, dleave.py, resets.py) that counts G_c and X_u per fallback-free
  run, first on L-RED R90's families (experiments/red/usplit/mkpp.py, mkgate.py; l-red eb64c242 is an ancestor of my head), k fixed and
  the size growing, to see whether G_c / X_u grow linearly like R⁰_{≥2}; then nep90 / nep76; then a bound attempt or a DEAD entry
  with its instance. Warning carried: DEAD box 20 (nep90 phase@4: 32 of 63 root offset resets are Bellman-Ford cascades charged only
  to the root's own ρ).
  - Overlap to clear with the Lead: NOW l.27 shows L-COMP 5 box 14 measuring "G_c, relay changes per fallback-free run on records";
    L-NEW 28 does the relay-change route after FBC / EPC fixes. I count on the R90 families and nep90 / nep76 only unless told otherwise.
- (2) STANDBY: repairs for P-N5-ROOT and its addendum in a NEW file docs/si/P-N5-ROOT-fixes-box20.md, when both referees' reports exist
  (queue after P-N5-EPC; `ls docs/referee docs/referee-2 | grep -i root` → none). One repair per item; quotes via
  experiments/si/rund/quotecheck.py, pinned in check.sh with a --mut control.
- (3) Not mine now: docs/si/P-N5-CHOSEN-fixes-box19.md (successor 16 may push it; I leave it alone).

## 3. docs/GAPS.md rows I own
- None (`git show trunk:docs/GAPS.md | awk -F'|' '$4 ~ /L-SI/'` → empty).
- I work under G-N5-TIME (l.11): major, owner L-NEW, status open; last update 14:38Z (R70, P-N5-HONFF, CHECKER C79): "f, X_dir, X_big
  and |D| ≥ 2 epochs OPEN; general games OPEN." NOW l.11: M4 IN PROGRESS, gauntlet step 4 (G-N5-TIME) OPEN. RESULTS ends at R70.

## 4. The three owner rulings that constrain me most (verbatim from docs/DECISIONS.md at trunk; status from docs/DECISIONS-INDEX.md)
- D18 (DECISIONS.md l.333; index l.32: active): "Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
  where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
  open problems."
  - Lead reading L40 (index l.33: active): L-SI is the OR/MDP lens on N5; labels PROVED / CONJECTURE / OPEN.
- D1 (index l.5: active; DECISIONS.md l.6, full text docs/decisions/D001-launch-brief.md): "Never publish, post, email, submit or
  contact anyone outside the fleet. Anything external is my decision." / "A claimed polynomial algorithm is far more likely to be
  wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below."
- D16 (DECISIONS.md l.300; index l.28: active): "Then keep working as I told you to"

## 5. One trap that bit this lane before, and the check that prevents it
- Trap (box 20, successor 16): experiments/si/root/shrink.py shadowed experiments/new/box21/shrink.py on sys.path, so an import pulled
  the wrong module's helpers.
  - Check: shared helpers live only in experiments/si/root/common.py (first_D, wplay, avoid, wt, M); new scripts get names that do not
    collide (`ls experiments/*/*/<name>.py` before creating one); wplay is cross-checked against box21/h1.py wvals (bffd.py WPLAY_V).
- Still live: stale clone (bit again here: 0d48da26 vs origin c1efeb1d; fetch first, re-fetch and merge before the push); frozen files
  (sha1sum before touching docs/si/P-*); `if grep …; then exit 1; fi` guards with a mutation control per pin; never `git add -A`;
  never pipe scripts/push.sh; never `pkill -f` / `pgrep -f` with a script name; stamp from date -u; «» only around verbatim quotes.

## 6. Oink
- scripts/setup_oink.sh → "oink built at 8fbf0a7" (tc, tc+, counter_*, rngame present), exit 0.

---
# Handover check: L-SI (successor 16, written 2026-10-26T13:40Z by date -u; LANE-RESTART step 3; Opus 5.5, D18/L40)
Every answer below was measured in this container; the commands are given. Predecessor: successor 15, session_017NeJAMbjHE3eoJcsnWhRbw.
Its handover is notes/L-SI.md "## HANDOVER (successor 15, box 19)" (l-si 213bba72).

## 1. Branch, head, distance to trunk
- Branch `claude/l-si`. The clone was stale again: local HEAD 0d48da26; `git fetch origin claude/l-si` → origin 213bba72;
  `git pull origin claude/l-si` (fast-forward) → HEAD 213bba72 (`git rev-parse HEAD origin/claude/l-si` equal).
- Trunk `origin/claude/vibrant-johnson-nxvvxo` = a7c141b8 (Lead: land R69 (FLIP, C78 Add. 1 978791e1) after R68; GAPS/NOW; log).
  - Before merging: `git rev-list --left-right --count HEAD...trunk` → 2 ahead / 59 behind; merge-base b7189738 (the CHOSEN packet commit).
  - `git merge --no-ff` of trunk a7c141b8 (no rebase) → merge commit 023da0fb; then 3 ahead / 0 behind. This file is the next commit;
    the pushed SHA goes to the Lead.

## 2. Open work and the next step of each (nothing running: fresh container; Oink: scripts/setup_oink.sh, result in §6)
Frozen (`sha1sum`, equal to the handover's values; never edited): docs/si/P-N5-CHOSEN-box19.md 764cfbb331a1aaefa819a01d64ee6b7cfbbd7316;
docs/si/P-N5-FLIP-fixes-box18.md 93a65e1b…; docs/si/P-N5-FLIP-box18.md 96a7e088… (FLIP landed as R69).
- (1) STANDBY: P-N5-CHOSEN fixes file docs/si/P-N5-CHOSEN-fixes-box19.md (new file, repairs only), when both referees' reports and §Cs
  exist. None yet: `ls docs/referee docs/referee-2 | grep -i -e chosen -e fbc` → empty; NOW l.42 / l.46: REFEREE 15 and REFEREE-2 17
  "CREATED 13:29Z ...: handover check; then P-N5-FBC, P-N5-CHOSEN". Next step on arrival: one repair per referee item, quotes checked
  with experiments/si/rund/quotecheck.py, pinned in check.sh with a mutation control.
- (2) MAIN after "go" (Lead's brief, handover queue item 2, note §28.2): an FRZ-U / Theorem RUN analogue for the ROOT r of an acyclic
  relay DAG, whose extra W-gates are r's relays and whose values are shifts of κ(r) (R61 (b) SAT-k + Lemma CHOSEN). First step: re-read
  R50 (c) FRZ-U's Claim P^c (docs/si/P-N5-KW-box15.md) and mark each step that uses D = {o}; then test the candidate statement on
  nep76 / nep90 (long-ρ one-gate dynamics around root 0, note §28) before any proof attempt. Inputs via the Lead: L-RED 21's 3n phase
  (long121_n40, |Q| = 3, one ruler level) and L-NEW 27's NCONF counts.
- (3) Older OPEN, Lead's pick only: flips per phase (N1 / N3; L-RED N3-CHAIN input); FRZ-RHO; (R1)-(R3); twin Δ-RT for |D| ≥ 2.

## 3. docs/GAPS.md rows I own
- None (`git show trunk:docs/GAPS.md | awk -F'|' '$4 ~ /L-SI/'` → empty).
- I work under G-N5-TIME (l.11): major, owner L-NEW, status open; last update 13:34Z (R69, P-N5-FLIP, CHECKER C78): "No count: flips
  and ρ events per phase are not bounded here. OPEN as before." NOW l.11: M4 IN PROGRESS, gauntlet step 4 (G-N5-TIME) OPEN.

## 4. The three owner rulings that constrain me most (verbatim from docs/DECISIONS.md at trunk; status from docs/DECISIONS-INDEX.md)
- D18 (DECISIONS.md l.333; index l.32: active): "Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
  where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
  open problems."
  - Lead reading L40 (index l.33: active): L-SI is the OR/MDP lens on N5; labels PROVED / CONJECTURE / OPEN.
- D1 (index l.5: active; DECISIONS.md l.6-7, full text docs/decisions/D001-launch-brief.md): "Never publish, post, email, submit or
  contact anyone outside the fleet. Anything external is my decision." / "A claimed polynomial algorithm is far more likely to be
  wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below."
- D16 (DECISIONS.md l.300; index l.28: active): "Then keep working as I told you to"

## 5. One trap that bit this lane before, and the check that prevents it
- Trap (box 19, successor 15): §27.2 counted "epochs = D changes + 1", which undercounts R61 epochs (σ̄ can change with D the same).
  - Check: epoch counts come only from experiments/si/rund/epcause.py's boundaries (pinned on nep90 in check.sh), never from D alone.
- Still live: stale clone (bit again here: fetch + `git rev-parse HEAD origin/claude/l-si` first, re-fetch before the push); frozen
  files (sha1sum before touching docs/si/P-*); `if grep …; then exit 1; fi` guards with a mutation control per pin; never `git add -A`;
  never pipe scripts/push.sh; stamp from date -u; «» only around verbatim quotes (quotecheck.py).

## 6. Oink
- scripts/setup_oink.sh → "oink built at 8fbf0a7" (tc, tc+, counter_*, rngame present), exit 0.

---
# Handover check: L-SI (successor 15, written 2026-10-26T12:00Z by date -u; LANE-RESTART step 3; Opus 5.5, D18/L40)
Every answer below was measured in this container; the commands are given. Predecessor: successor 14, session_019qFTEd4V6YTCPzEN6Js3ez.
Its handover is notes/L-SI.md "## HANDOVER (successor 14, box 18)" (l-si 8072c86b).

## 1. Branch, head, distance to trunk
- Branch `claude/l-si`. The clone was stale again: local HEAD 0d48da26; `git fetch origin claude/l-si` → origin 8072c86b;
  `git pull origin claude/l-si` (fast-forward) → HEAD 8072c86b (`git rev-parse HEAD origin/claude/l-si` equal).
- Trunk `origin/claude/vibrant-johnson-nxvvxo` = d67fdb87 (Lead: pin P-N5-FLIP (sha1 96a7e088); merges; log).
  - Before merging: `git rev-list --left-right --count HEAD...trunk` → 0 ahead / 18 behind; merge-base 8072c86b (= my head: trunk
    already carries all of l-si).
  - `git merge --no-ff` of trunk d67fdb87 (no rebase) → merge commit 4bc5af1a; then 1 ahead / 0 behind. This file is the next commit;
    the pushed SHA goes to the Lead.

## 2. Open work and the next step of each (nothing running: fresh container; Oink built: scripts/setup_oink.sh → "oink built at 8fbf0a7", exit 0)
Frozen (`sha1sum`, equal to the handover's values; never edited): docs/si/P-N5-FLIP-box18.md 96a7e088c2175f71ab1aef2577d6139f80a4efff
(pinned on trunk d67fdb87); docs/si/P-N5-RUND-fixes-box17.md aa4a3920…; docs/si/P-N5-RUND-box17.md 71e198f3….
- (1) STANDBY: P-N5-FLIP fixes file docs/si/P-N5-FLIP-fixes-box18.md (new file, repairs only), when both referees' reports and §Cs exist.
  None yet: `ls docs/referee docs/referee-2 | grep -i flip` → empty; NOW l.40 / l.43: REFEREE 14 and REFEREE-2 16 "parked light for
  P-N5-FLIP". Next step on arrival: one repair per referee item, quotes checked with experiments/si/rund/quotecheck.py, pinned.
- (2) MAIN after "go": ρ_q per phase for classes with m_c ≥ 2 Odd choice vertices (OPEN). Known (note §22-§25, lane-PROVED, unrefereed):
  ROOT, ROUTE-RELAY, SELF-FREE (m_c = 1 closes), ROOT-C, FLIP (a)-(c) with necessary condition N1 ∨ N2 ∨ N3, N3-LEVEL (sharp).
  Next step: either (a) a per-level ruler count of N3 flips on q2's path set (gives ≤ 2^{#ranks ≥ top(C)} per pair: polynomial only
  when cycle tops are near the class top), or (b) a separate charge for N1 flips (old exit path broken by an Even switch), testing
  L-NEW 26's FB-RISE (an Even fallback is a Ξ Bellman-Ford step) on the fallback-caused N1 flips (frz40). First action: classify every
  flip in the corpus (flipck.py) as N1-by-fallback / N1-by-ordinary-switch / N2 / N3, to see which charge carries the load.
  Coordination via the Lead: L-RED 21 (low-top relay cycles vs N3-LEVEL), L-COMP 5 (growth laws, relay-cycle column).
- (3) Older OPEN, Lead's pick only: FRZ-RHO proof (on R_D); (R1)-(R3), twin Δ-RT for |D| ≥ 2 epochs.

## 3. docs/GAPS.md rows I own
- None (`git show trunk:docs/GAPS.md | awk -F'|' '$4 ~ /L-SI/'` → empty).
- I work under G-N5-TIME (l.11): major, owner L-NEW, status open; last update 11:33Z (R67, P-N5-RUND, CHECKER C76): "No count: the band,
  N_split and U(S) are not bounded. OPEN as before." NOW: M4 IN PROGRESS, gauntlet step 4 (G-N5-TIME) OPEN.

## 4. The three owner rulings that constrain me most (verbatim from docs/DECISIONS.md at trunk; status from docs/DECISIONS-INDEX.md)
- D18 (DECISIONS.md l.333; index l.32: active): "Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
  where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
  open problems."
  - Lead reading L40 (index l.33: active): L-SI is the OR/MDP lens on N5; labels PROVED / CONJECTURE / OPEN.
- D1 (index l.5: active; DECISIONS.md l.6-7, full text docs/decisions/D001-launch-brief.md): "Never publish, post, email, submit or
  contact anyone outside the fleet. Anything external is my decision." / "A claimed polynomial algorithm is far more likely to be
  wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below."
- D16 (DECISIONS.md l.300; index l.28: active): "Then keep working as I told you to"

## 5. One trap that bit this lane before, and the check that prevents it
- Trap (box 18, successor 14): check.sh used `! grep …` as a guard; under `set -e` a negated command never trips, so a pin that should
  fail passed silently. Also flipck.py adds counters alphabetically, so whole-line greps break when a counter is added.
  - Check: guards are written `if grep …; then exit 1; fi`, pins grep single tokens, and every new pin ships with a mutation control
    (MUT / --mut / reversed) that must make it fail (e.g. quotecheck.py --mut, flipck reversed control).
- Still live: stale clone (bit again here: fetch + `git rev-parse HEAD origin/claude/l-si` first, re-fetch before the push); frozen
  files (sha1sum before touching docs/si/P-*); never `git add -A`; never pipe scripts/push.sh; stamp from date -u.

---
# Handover check: L-SI (successor 14, written 2026-10-26T10:08Z by date -u; LANE-RESTART step 3; Opus 5.5, D18/L40)
Every answer below was measured in this container; the commands are given. Predecessor: successor 13, session_018EgSbDTYEVHqL882sCoX7u.
Its handover is notes/L-SI.md "## HANDOVER (successor 13, box 17 cont.)" (l-si ca90fe74).

## 1. Branch, head, distance to trunk
- Branch `claude/l-si`. The clone was stale again: local HEAD 0d48da26; `git fetch origin claude/l-si` → origin ca90fe74;
  `git merge --ff-only origin/claude/l-si` → HEAD ca90fe74 (`git rev-parse HEAD origin/claude/l-si` equal).
- Trunk `origin/claude/vibrant-johnson-nxvvxo` = c69e199e (Lead: log; R65 landed at f7308227).
  - Before merging: `git rev-list --left-right --count HEAD...trunk` → 2 ahead / 7 behind; merge-base 4ff4e1a4.
  - `git merge --no-ff` of trunk c69e199e (no rebase) → merge commit bef09595; then 3 ahead / 0 behind. This file is the next commit; the
    pushed SHA goes to the Lead.

## 2. Open work and the next step of each (nothing running: `pgrep -a python` empty; fresh container)
Frozen: `sha1sum docs/si/P-N5-RUND-box17.md` → 71e198f359cbb321fc0c15e6c28676d4dd046d52 = the handover's value. Not edited, never will be.
- (1) STANDBY: RUND fixes file docs/si/P-N5-RUND-fixes-box17.md (repairs only), when both referees' RUND notes reach me via the Lead.
  None has arrived (no referee RUND file on trunk named in NOW; RUND is third in REFEREE 13's queue after STAU, REC0).
- (2) STANDBY: dead-end records if L-RED kills U-SPLIT, UF-ONCE or PAIR-OC (`grep -i "U-SPLIT\|UF-ONCE\|PAIR-OC" docs/*.md` → none on
  trunk docs). Next step when a kill arrives: reproduce it, record DEAD with instance + obstruction, state the replacement (§18 recursion).
- (3) ACTIVE after "go": the ρ / N_ep line from the L-SI side. Question: a bound on ρ_q per phase in classes with ≥ 2 Odd choice
  vertices. Known (note §20-§21): boundaries ≤ ρ + (epochs − 1) + WG (PROVED, immediate); ruler-pattern level reuse at gates
  (pftheta34 is 𝒞^1O, bounded by R51, not evidence; frz40, 4 Odd choice vertices, ρ_q = 10 < n). First step: ρ_q tables per phase and
  per class on the ≥ 2-Odd-choice corpus (lib41 KMIN=2, frz*, L-RED climbs), with the per-q ruler trace, to see whether the ruler can
  nest across two Odd choice vertices; then a statement (CONJECTURE or proof attempt). Coordination: L-NEW 25 holds N_ep from the epoch
  side (P-N5-HON, REC-1), L-COMP 5 the epoch census: I ask the Lead before any count that overlaps those.
- (4) Older OPEN: (R1), (R2), (R3) ¬(h3_D), twin Δ-RT for |D| ≥ 2 epochs. Packet P-N5-USPLIT only on the Lead's word.

## 3. docs/GAPS.md rows I own
- None (`git show trunk:docs/GAPS.md | awk -F'|' '$4 ~ /L-SI/'` → empty).
- I work under G-N5-TIME (l.11): major, owner L-NEW, status open; last update 09:56Z (R65, P-N5-STAU): "N_ep / ρ and epochs with
  |D_E| ≥ 2 OPEN; general games OPEN." NOW l.2: "NO polynomial bound for N5 on general games is proved."

## 4. The three owner rulings that constrain me most (verbatim from docs/DECISIONS.md at trunk; status from docs/DECISIONS-INDEX.md)
- D18 (DECISIONS.md l.332-333; index l.32: active): "Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
  where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
  open problems."
  - Lead reading L40 (index l.33: active): L-SI is the OR/MDP lens on N5; labels PROVED / CONJECTURE / OPEN.
- D1 (index l.5: active; DECISIONS.md l.3, full text docs/decisions/D001-launch-brief.md): "Never publish, post, email, submit or
  contact anyone outside the fleet. Anything external is my decision." / "A claimed polynomial algorithm is far more likely to be
  wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below."
- D16 (DECISIONS.md l.299-300; index l.28: active): "Then keep working as I told you to"

## 5. One trap that bit this lane before, and the check that prevents it
- Trap (box 17, successor 13 §21): citing an instance as blow-up evidence when its class is already bounded. pftheta34's long gate
  phase (ρ_0 > n, ruler pattern) looked like ρ evidence, but pftheta34 is 𝒞^1O, so R51 bounds it.
  - Check: every ρ / N_ep table first prints the instance's class (number of Odd choice vertices per honest class, 𝒞^1O / 𝒞^1E flag);
    𝒞^1O / 𝒞^1E rows are reported apart and never counted as evidence for ≥ 2-Odd-choice behaviour.
- Still live: stale clone (bit again here: fetch + `git rev-parse HEAD origin/claude/l-si` first, re-fetch before the first push);
  frozen files (sha1sum before touching docs/si/P-*); never `git add -A`; never pipe scripts/push.sh; stamp from date -u.

---
# Handover check: L-SI (successor 13, written 2026-10-26T07:50Z by date -u; LANE-RESTART step 3; Opus 5.5, D18/L40)
Every answer below was measured in this container; the commands are given. Predecessor: successor 12, session_01HYh7NTpb8ZcvdYpgAJiDgy.
Its handover is notes/L-SI.md "## HANDOVER (successor 12, box 17)" with its "UPDATE 07:4xZ" and "NEXT" (l-si ac80b594), plus its final push 0b025b91.

## 1. Branch, head, distance to trunk
- Branch `claude/l-si`. The clone was stale AGAIN: local HEAD 0d48da26; `git fetch origin claude/l-si` → origin ac80b594;
  `git merge --ff-only origin/claude/l-si` → HEAD ac80b594 (`git rev-parse HEAD origin/claude/l-si` equal).
- Trunk `origin/claude/vibrant-johnson-nxvvxo` = c6b763f1 at first fetch, 177b3dbb at the second (the brief's "c6b763f1 or later").
  - Before merging: `git rev-list --left-right --count HEAD...trunk` → 4 ahead / 136 behind; merge-base 47e409bf.
  - `git merge --no-ff` of trunk c6b763f1 (no rebase) → merge commit 1e71b666. My first push was rejected: successor 12 had pushed
    0b025b91 (handover final: Lead 07:36Z queue, box 17 dead ends in the notebook) after my fetch. Merged it (--no-ff, no rebase).
  - Trunk then moved to 177b3dbb (Lead: R62 landed); merged it too (--no-ff). Now `git rev-list --left-right --count HEAD...trunk`
    → 9 ahead / 0 behind (before this file's commit). This file is the next commit; the pushed SHA goes to the Lead.
- R62 / R64: at c6b763f1 RESULTS had R64 but not R62 (NOW said "At CHECKER: R62"); at 177b3dbb R62 (P-N5-H3; CHECKER C71) is in
  RESULTS and GAPS G-N5-TIME has "UPDATE 07:47Z: RESULTS R62 ... LANDED". Both are on trunk now, as the brief says.
- Queue per the notebook's added "Queue (Lead 07:36Z)" (0b025b91): 1. restricted Lemma P / LEVEL-COUNT; 2. twin Δ-RT for |D| ≥ 2
  epochs. Successor 12 agreed: 1 first. That matches the brief's STEP 2.

## 2. Open work and the next step of each (nothing running: `pgrep -a python` empty; fresh container)
Frozen packets: sha1sum of docs/si/P-N5-*.md matches the handover (P-N5-H3 680e4528, P-N5-H3-fixes 5666b4a5, 2T fcb91130 / 8aad9f77,
1E e613db13 / 8f3615bc, FX-fixes 4253d51e, NC 2036e7c8 withdrawn). None is edited.
- (a) Restricted Lemma P, note docs/si/N5-RUND-box17.md §13 (NOT frozen). PROVED (unrefereed): Lemma P^c_ok, Corollary FRZ-OK. DATA
  (okfrz.py): content on pftheta34_n32 (14 frozen full values), coverage 2/24 on frz1_n24 and frz3_n24. Stopping point: "OK on S" is too
  strict. Next step: DATA per run and edge = the last state at which each forbidden edge is forbidden, on the three long (h3_D) runs
  (extend okfrz.py in experiments/si/rund/); then P^c_ok restarted at that state (the P^c_L induction can start at any state of S);
  where an edge stays forbidden while x's play uses it, state the remaining count as N_split in per-vertex form (§11).
- (b) LEVEL-COUNT (count form) is a CONJECTURE (§12; strong form INC DEAD, incdown_n23). Next: attack it via the dynamics, after (a).
  L-RED is running the adversary on it (Lead 07:20Z): I do not duplicate climbs.
- (c) Packet P-N5-RUND-box17 (PIECE_D, SPLIT-RED, TWIN-GAP, OFFSET, MERGE-B, CR-REL from §4, §5, §11, with data tables): a NEW frozen
  file, ONLY on the Lead's word (Lead 07:09Z: fresh referees; "a slightly later, fuller packet is fine").
- OPEN items named in the note: (R1) offset-preserving terminal changes, (R2) offset changes per vertex per stretch_D (≥ Θ(√n) by mkalt,
  ≤ (n − 1) + 2^{B+1}), (R3) ¬(h3_D), (R4) epochs / stretch_D boundaries. L-COMP runs an independent OFFSET / TWIN-GAP checker.

## 3. docs/GAPS.md rows I own
- None (`git show trunk:docs/GAPS.md | awk -F'|' '$4 ~ /L-SI/'` → empty).
- I work under G-N5-TIME (l.11): major, owner L-NEW, status open; updates 07:36Z (R64) and 07:47Z (R62) landed; R64 text: "(Στ) itself (P-N5-STAU, in review),
  N_ep / ρ and |D_E| ≥ 2 epochs OPEN; general games OPEN." NOW l.2: "NO polynomial bound for N5 on general games is proved."

## 4. The three owner rulings that constrain me most (verbatim from docs/DECISIONS.md at trunk; status from docs/DECISIONS-INDEX.md)
- D18 (DECISIONS.md l.333; index l.32: active): "Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
  where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
  open problems."
  - Lead reading L40 (index l.33: active): L-SI is the OR/MDP lens on N5; labels PROVED / CONJECTURE / OPEN.
- D1 (index l.5: active; DECISIONS.md l.6-7, full text docs/decisions/D001-launch-brief.md): "Never publish, post, email, submit or
  contact anyone outside the fleet. Anything external is my decision." / "A claimed polynomial algorithm is far more likely to be
  wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below."
- D16 (DECISIONS.md l.300; index l.28: active): "Then keep working as I told you to"

## 5. One trap that bit this lane before, and the check that prevents it
- Trap (box 17): a freeze statement that is non-vacuous can still be CONTENT-FREE: every known non-vacuous coarse freeze had L = top rank
  (rel.py "content" 0), so it froze nothing a reader cares about. Also (box 16) freezes "constant from state k_0 + n − 1" are vacuous on
  runs with ≤ n states.
  - Check: every freeze checker reports non-vacuous windows AND a "with content" column (non-empty path part, okfrz.py), next to the
    violation count; a mutation control (MUT=1 / MUT=2) must bite before a 0 counts as evidence.
- Still live: stale clone (bit again here: fetch + `git rev-parse HEAD origin/claude/l-si` first); frozen files (sha1sum before touching
  docs/si/P-*); never `git add -A`; never pipe scripts/push.sh; never `pkill -f` a pattern in my own command; stamp from date -u.

---
# Handover check: L-SI (successor 12, written 2026-10-26T06:02Z by date -u; LANE-RESTART step 3; Opus 5.5, D18/L40)
Every answer below was measured in this container; the commands are given. Predecessor: successor 11, session_01FchPxfEZ9Fo56WrCZTvnXS.
Its handover is notes/L-SI.md "## HANDOVER (successor 11, box 16)" (l-si 2d021429).

## 1. Branch, head, distance to trunk
- Branch `claude/l-si`. The clone was stale: local HEAD 0d48da26; `git fetch origin claude/l-si` moved origin 0d48da26 → 2d021429;
  `git merge --ff-only origin/claude/l-si` → HEAD 2d021429; `git merge-base --is-ancestor 2d0214294 HEAD` → true.
- Trunk `origin/claude/vibrant-johnson-nxvvxo` = 5db6da07.
  - Before merging: `git rev-list --left-right --count 2d021429...trunk` → 2 ahead / 6 behind; merge-base 5db6da07 (= trunk head).
  - `git merge --no-ff` of trunk (no rebase) → merge commit b0284ff1, 3 ahead / 0 behind. This file is the next commit; the pushed SHA
    goes to the Lead.

## 2. Open work and the next step of each (nothing running: `pgrep -a python` empty; fresh container)
Frozen packets re-measured with sha1sum: P-N5-H3 680e4528, P-N5-2T fcb91130, P-N5-2T-fixes 8aad9f77, P-N5-1E e613db13,
P-N5-1E-fixes 8f3615bc, P-N5-FX-fixes 4253d51e, P-N5-NC 2036e7c8 (withdrawn unreviewed). All match the handover.
- P-N5-H3 (frozen, in review). REFEREE 12: docs/referee/R-N5-H3.md at referee 7c2d9b49, all SIGNED; notes H3-N1 (WM-G rests on the
  standing SPEC premise), H3-N2 (P^c_L: one step made explicit), H3-N3 (data). REFEREE-2 succ. 14: docs/referee-2/R2-N5-H3.md at
  referee-2 5b251bed (branch head b9a7a1f4), all SIGN, no gap, notes N-H3-1..5. `grep -n '§C'` on both → nothing: no §C yet; neither
  report is on trunk (`git ls-tree trunk docs/referee/ docs/referee-2/ | grep -i h3` → empty).
  - Next step: on the Lead's word after both §Cs, write NEW docs/si/P-N5-H3-fixes-box16.md: H3-N1, H3-N2 (= REFEREE-2's N-NC-3 on the
    void NC; B1 simplicity from x ∉ π), H3-N3, N-H3-1..5, and the 0-BASED reading of "constant from state k_0 + n − 1" (a non-vacuous
    check needs ≥ n + 1 states).
- Research (Lead's pick, after the fixes): ¬(h3_D) KIND-MONO port for twin gates (twin Δ-RT above m*), or RUN_D for twin changes.
  Next step: read N5-2O-T-box16 §8 and the handover NEXT, propose one with reasoning to the Lead before starting.
- P-N5-2T (R58) at CHECKER C67; P-N5-1E = R57 landed. No step for me unless asked.

## 3. docs/GAPS.md rows I own
- None (`git show trunk:docs/GAPS.md | awk -F'|' '$4 ~ /L-SI/'` → empty).
- I work under G-N5-TIME (l.11): major, owner L-NEW, status open. Last update 2026-10-26 05:50Z (R57 landed): "The row stays open: no
  iteration bound on general games; subclass bounds for 𝒞^1O (R51) and 𝒞^1E (R57) are proved." NOW l.2: "NO polynomial bound for N5 on
  general games is proved."

## 4. The three owner rulings that constrain me most (verbatim from docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md)
- D18 (DECISIONS.md l.332-333; index l.32: active): "Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
  where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
  open problems."
  - Lead reading L40 (index l.33: active): L-SI is the OR/MDP lens on N5.
- D1 (index l.5: active; DECISIONS.md l.3-7, full text docs/decisions/D001-launch-brief.md):
  "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
  as wrong until it passes the gauntlet below." / "Never publish, post, email, submit or contact anyone outside the fleet. Anything
  external is my decision."
- D16 (DECISIONS.md l.299-300; index l.28: active): "Then keep working as I told you to"

## 5. One trap that bit this lane before, and the check that prevents it
- Trap (box 16): a freeze-type statement was checked VACUOUSLY. FRZ-U-type freezes are "constant from state k_0 + n − 1" (0-based),
  so a run shorter than n + 1 states tests nothing; most lane runs are shorter than n − 1. And L-COMP's 1-based reading was stronger
  than the proof, so its failure would not have been a counterexample.
  - Check: every freeze checker reports the number of NON-VACUOUS windows (base = i + n − 1, states x > base) next to its violation
    count, and a mutation control (MUT/MUTL) must bite; gdnc.py does both. Also run random START PAIRS, not only the library (TC-W).
- Still live: stale clone (fetch + `rev-parse HEAD origin/claude/l-si` first: it bit again here); frozen files (sha1sum before editing
  docs/si/P-*); ReadNotifications before any freeze; never `git add -A`; never pipe scripts/push.sh; stamp times from date -u.

---
# Handover check: L-SI (successor 11, written 2026-10-26T01:56Z by date -u; LANE-RESTART step 3; Opus 5.5, D18/L40)
Every answer below was measured in this container; the commands are given. Predecessor: successor 10, session_01PBqfsNWMhTPn7yNJ8C18HP.
Its handover is notes/L-SI.md "## HANDOVER (successor 10, box 15)" (l-si 20d3a875); the 1O fixes were frozen after it (90f93566).

## 1. Branch, head, distance to trunk
- Branch `claude/l-si`. `git fetch origin claude/l-si` moved origin 0d48da26 → 278bd489 (stale clone again);
  `git checkout -B claude/l-si origin/claude/l-si`; `git rev-parse HEAD origin/claude/l-si` → both 278bd489.
- Trunk `origin/claude/vibrant-johnson-nxvvxo` = d7d9d7d2 (Lead 01:48Z "R51 rev. (C60 E-1, E-2); merges (R2 FX/NH42/DUAL, ...)").
  - Before merging: `git rev-list --left-right --count HEAD...trunk` → 0 ahead / 27 behind; merge-base 278bd489 (= my head: the Lead
    had already merged all of l-si).
  - `git merge --no-ff` of trunk (no rebase) → merge commit 6be344ce, 1 ahead / 0 behind. This file is the next commit; the pushed SHA
    goes to the Lead.

## 2. Open work and the next step of each (nothing running: `pgrep -a python` empty; fresh container)
Frozen (sha1 sent to the Lead), re-measured with sha1sum on my tree and with `git show trunk:<file> | sha1sum` (identical):
P-N5-1O 2cf5e672, P-N5-1O-fixes 647deab5, P-N5-FX aa227b0b, P-N5-KW-fixes c65f4c1e. N5-FRONTIER-box15 (06cd6c9e, not frozen) is on trunk.
- P-N5-1O (assembly on 𝒞^1O): SIGNED by both (docs/referee/R-N5-1O.md §C, docs/referee-2/R2-N5-1O.md §C on trunk); fixes FROZEN 647deab5.
  RESULTS R51 is NOT landed: `grep '^### R51' RESULTS.md` empty. Lead draft docs/agents/R51-draft.md; CHECKER C60 = FAIL (E-1 start-
  freeness attribution, E-2 honest limits); the Lead revised it at d7d9d7d2. Next step: none for me unless the CHECKER re-check asks.
- P-N5-FX fixes: REFEREE R-N5-FX SIGNED, no gaps, notes FX-N1..N3 (843ba1f8); REFEREE-2 R2-N5-FX SIGNED, no gaps, notes N-FX-1, N-FX-2
  ("with R48 landed, (b) is unconditional") (83a3e8c7). Neither report has a §C yet (`grep -n '§C' ` on both → nothing).
  docs/si/P-N5-FX-fixes-box14.md does not exist. Next step: when the Lead relays both §Cs, write it NEW (FX-N1/N-FX-1 one item:
  "second derivation from R-STICK alone"; FX-N2/N-FX-2: cite R48 (i) (a) repaired + (b), (c), drop "CONDITIONAL"; FX-N3 scope).
- P-N5-1E (new, Lead 01:5xZ, after "go"): N5 on 𝒞^1E (exactly one Even choice vertex) polynomial from any start pair, from R51
  (1O-POLY), P-N5-DUAL (MIRROR; REFEREE SIGNED with wording gap DUAL-1; REFEREE-2 R2-N5-DUAL on trunk) and (H-N5) = R51's start-free
  per-phase bound. Output needs Lemma OUT on every game, PROVED as a lemma to sign (R21 (a) is game-independent per N-1O-4: R18 (d)
  Lemma S (a)). Next step: draft docs/si/P-N5-1E-box16.md (NEW); freeze on the Lead's word after DUAL lands.
- Frontier (successor 10 NEXT 3, Lead's optional item): TC-SWITCH data on L-NEW 22's frontier instances; ≼_D order (N5-FRONTIER §4). Not started.
- I wait for "go"; the order is the Lead's.

## 3. docs/GAPS.md rows I own
- None (`git show trunk:docs/GAPS.md | awk -F'|' '$4 ~ /L-SI/'` → empty).
- I work under G-N5-TIME (l.11): major, owner L-NEW (L-LIT T22; referees later), status open. Last update 2026-10-26 00:38Z (R49, R50
  LANDED; "the assembly ... (P-N5-1O ...) is still to be refereed. Beyond 𝒞^1O: OPEN ... G-N5-TIME stays open."). NOW l.2: "NO polynomial
  bound for N5 is proved."
- G-N5-TERM (l.16): closed (R15).

## 4. The three owner rulings that constrain me most (verbatim from docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md)
- D18 (DECISIONS.md l.332-333; index l.32: active): "Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
  where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
  open problems."
  - Lead reading L40 (index l.33: active): L-SI is the OR/MDP lens on N5.
- D1 (index l.5: active; DECISIONS.md l.3, full text docs/decisions/D001-launch-brief.md):
  "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
  as wrong until it passes the gauntlet below." / "Never publish, post, email, submit or contact anyone outside the fleet. Anything
  external is my decision."
- D16 (DECISIONS.md l.299-300; index l.28: active): "Then keep working as I told you to"

## 5. One trap that bit this lane before, and the check that prevents it
- Trap (box 15): Lead messages crossed successor 10's freezes twice (the K-unit note had to become an addendum; PHI was already done).
  A sha1 sent to the Lead freezes the file, so a crossed relay costs a NEW file and a second referee pass.
  - Check: ReadNotifications, then `git fetch` trunk and `git ls-tree --name-only trunk docs/referee/ docs/referee-2/ docs/checker/ |
    grep <packet>` and `grep -n '§C'` on both reports, immediately before freezing any file and after every push. (Applied here: it is
    how I know FX has no §C yet and that C60 failed R51's first draft.)
- Still live: stale clone (fetch + `rev-parse HEAD origin/claude/l-si` before reading); frozen files (sha1sum + grep notes, NOW before
  editing docs/si/P-* or *-fixes-*); `until ! pgrep -f X` matches its own shell (use `while kill -0 PID`); never `git add -A`; never
  pipe scripts/push.sh; stamp times from date -u in the same command.

---

# Handover check: L-SI (successor 10, written 2026-10-25T19:15Z by date -u; LANE-RESTART step 3; Opus 5.5, D18/L40)
Every answer below was measured in this container; the commands are given. Predecessor: successor 9, session_018jN1MJkw56F58G3qcfcuZA.
Its handover is fe58fbab, notes/L-SI.md "## HANDOVER (successor 9, box 14)".

## 1. Branch, head, distance to trunk
- Branch `claude/l-si`. `git fetch origin claude/l-si` moved origin 0d48da26 → fe58fbab (stale clone again);
  `git checkout -B claude/l-si origin/claude/l-si`; `git rev-parse HEAD origin/claude/l-si` → both fe58fbab.
- Trunk `origin/claude/vibrant-johnson-nxvvxo` = 0ea336ed (Lead 19:09Z "R43 draft (P-N5-LV2) → CHECKER C52").
  - Before merging: `git rev-list --left-right --count HEAD...trunk` → 5 ahead / 37 behind; merge-base 858c7dd5.
    The 5 ahead are succ. 9's 0d04e208, af3a3b5a (P-N5-PHI), 7f76709c (ledger v2), e31e966c (handover), fe58fbab (P-N5-FX).
  - `git merge --no-ff` of trunk (no rebase) → 6 ahead / 0 behind. This file is the next commit; pushed SHA goes to the Lead.

## 2. Open work and the next step of each (nothing running: `pgrep -a python` empty; fresh container)
Frozen (sha1 sent to the Lead), re-measured with sha1sum: P-N5-PHI 35e79ec1, P-N5-FX aa227b0b, N5-LEDGER-v2 8ab27359,
N5-LEDGER (v1) c54e8560, N5-FBPHASE f7aaa624, P-N5-NEEDB 7471aef3 (and every earlier list in this file).
PHI, FX, LEDGER-v2 are NOT on trunk yet (`git show trunk:<file>` empty); FBPHASE, LEDGER v1, NEEDB are, with the same sha1.
- P-N5-NEEDB fixes (succ. 9 NEXT 2): REFEREE succ. 10 report docs/referee/R-N5-NEEDB.md is ON TRUNK (008ad8ab, 18:52Z): all of
  §1-§4.2 SIGNED, no gaps, notes NEEDB-N1 (wording), N2 (precision), N3 (notation), N4 (stronger statement, DATA, no change asked).
  REFEREE-2's R2-N5-NEEDB is not on trunk (REFEREE-2 succ. 11 queue ends "→ NHN → NEEDB", NOW l.42).
  - Next step: when REFEREE-2 reports (or on the Lead's word), write NEW docs/si/P-N5-NEEDB-fixes-box13.md (does not exist) with
    N1-N3 and L-RED R71's INTO wording note (restrict INTO to Iσ_t ≠ ∅ or to fallback states).
- P-N5-PHI (35e79ec1): no referee report on trunk. Next step: Lead routes it; items go to a NEW fixes file.
- P-N5-FX (aa227b0b): Corollary FX X ≤ n(f + X_SN) + n − 1, CONDITIONAL on P-N5-FBPOLY (L-NEW). No report. Next step: same.
- FB-PHASE: lane cross-check of FB-POLY only, not packeted (Lead 18:57Z). Nothing to do unless a referee asks.
- K, the single open count on 𝒞^1O (ledger v2 §3; READING): wakes at U2 / U3 / U23 states, i.e. (E) (kind changes of R-vertices and
  c_w switches per W-flat run of U3 / U23 stretches) and (K_W) (non-fallback W-changes on R). OPEN.
  - Next step, if the Lead routes it: start at HN (U3) states, using BF-F for F-side rounds and SPLIT for R-monotonicity between
    evictions; try an L-MONO analogue for c_w.
- I wait for "go"; the choice among these is the Lead's.

## 3. docs/GAPS.md rows I own
- None (`git show trunk:docs/GAPS.md | grep -n L-SI` → no row with owner L-SI).
- I work under G-N5-TIME (l.11): major, owner L-NEW (L-LIT T22; referees later), status open. Last update 17:41Z (R42 LANDED); open
  list: RW_S, θ_ph / ρ, Q states, scope runs per phase / X, S4a steps, phases. NOW l.2: "NO polynomial bound for N5 is proved."
- G-N5-TERM (l.16): closed (R15).

## 4. The three owner rulings that constrain me most (verbatim from docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md)
- D18 (DECISIONS.md l.333; index l.32: active): "Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
  where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
  open problems."
  - Lead reading L40 (index l.33: active): L-SI is the OR/MDP lens on N5.
- D1 (index l.5: active; DECISIONS.md l.7, full text docs/decisions/D001-launch-brief.md):
  "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
  as wrong until it passes the gauntlet below." / "Never publish, post, email, submit or contact anyone outside the fleet. Anything
  external is my decision."
- D16 (DECISIONS.md l.300; index l.28: active): "Then keep working as I told you to"

## 5. One trap that bit this lane before, and the check that prevents it
- Trap (box 14): crossed work. Lead relayed L-NEW's FB-POLY (18:37Z) while successor 9 was proving FB-PHASE; the second proof cost a
  box segment and was demoted to a cross-check. Same family: a referee report can land on trunk while the notebook still says
  "once both referees report" (R-N5-NEEDB, 18:52Z, found only by this check).
  - Check: ReadNotifications, and `git fetch` trunk + `git ls-tree -r --name-only trunk docs/referee docs/referee-2 docs/new | grep
    <packet>`, before starting any proof or fixes file, and after every push.
- Still live: stale clone (fetch + `rev-parse HEAD origin/claude/l-si` before reading); frozen files (sha1sum + grep notes, NOW,
  LEAD-STATE before editing docs/si/P-* or *-fixes-*); never `git add -A`; never pipe scripts/push.sh; stamp times from date -u in
  the same command.

---

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
