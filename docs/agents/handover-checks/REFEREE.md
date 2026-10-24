# Handover check: REFEREE

## successor (2026-10-17T12:45Z; Opus 5.5 under D12/L33; predecessor session_01W3Z4peJy1bngBmMVdJ1f6K parked at ~550k)
Every answer measured from the repository at the time of writing (commands given), not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee`. The container's local branch was STALE (5ed56c5, 1517 behind); after `git fetch origin claude/referee`
  and `git merge --ff-only origin/claude/referee`: HEAD = origin/claude/referee = ca03021.
- `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...origin/claude/referee` -> 13 behind, 0 ahead
  (trunk 44af920); ca03021 is an ancestor of trunk, so all REFEREE work is on trunk. This file's commit adds one ahead.

### 2. Open work and next step of each
- Nothing in flight (predecessor parked 12:38Z after R-P5). Next step: wait for the Lead's next packet.
- Open items I hold from the predecessor's reports (each waits on a packet; I do not start them unasked):
  (ACYC) (R-STEP5); G-e1/G-DOM (R-P4 §22e: first difference in a Dom tattr); (CTX), (DIRTY)/(FALL) (R-P4/R-P5 §22e);
  (SPP) (R-PROVED2, (SPP) => bound only); the (α) shape (R-P3, SKETCH); GAP-A beyond round r (R-P3).
  Next step of each: re-derive against dtl.cpp @ 8fbf0a7 when the Lead routes the L-ALG proof or a REFEREE-2 comparison.
- Before the first packet: rebuild Oink (scripts/setup_oink.sh; tools/ is gitignored).

### 3. docs/GAPS.md rows relevant to me (trunk 44af920)
- GAP-A blocker, L-ALG, open: (SPP) DATA only; phases <= D+2 and (SPP) => O(n^10(m+n^2)) signed (R-PROVED2).
- GAP-C blocker, L-ALG, open: KT frame given (ACYC) (RESULTS R4, signed R-STEP5); single-search progress statements dead (DE13, DE15).
- G-S5-6 major, L-ALG, open: (ACYC). DATA only.
- G-DOM major, L-ALG, open: (e* ∉ Dom) = my R-P4 G-e1. DATA only.
- G-STR major, closed (trunk d8a4e19): STR-DET signed by both referees (my R-P5). Note: GAPS.md on claude/referee (ca03021)
  still shows G-STR open; trunk is the truth.
- Closed rows I signed: G-FDL, G-Bthr, G-K5 (K5'' with Dep(Str)).

### 4. Three owner rulings that most constrain me (verbatim), with DECISIONS-INDEX status
1. D12 (index: active; Lead reading L33 active):
   > WE can run referees on opus too temperoraly
   (L33: until the Fable reset 2026-10-21 21:00Z; two independent referees; every signature labelled "(Opus 5.5, D12)".)
2. D1 (index: active):
   > Never downgrade the referee to save money.
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
3. D1 (index: active):
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (notebook Lessons; R-P3 (a) and G-STR): set-level arguments about what a ψ-play or an extraction does missed strategy-level
  effects; R-P3's G-a1/G-a2 step was wrong (old tangle vertices keep their region strategy, dtl.cpp 169) and was REJECTED after
  REFEREE-2's configuration. Check: for every vertex a proof step touches, name the line that wrote str (89 / 171 / 73) before
  signing; and no signature before re-reading the cited code lines myself.
- Also this session: the local branch was 1517 commits stale; check `git rev-parse HEAD origin/claude/referee` equal before any work.

## successor 2 (2026-10-18T22:48Z by date -u; Opus 5.5 under D12/L33; predecessor session_01M28EFY9Ysyqj67kXt3YSje parked 01:26Z)
Measured from the repository at the time of writing, not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee`. Local branch was STALE again (5ed56c5, 1947 behind origin). After `git fetch origin claude/referee
  claude/vibrant-johnson-nxvvxo` and `git merge --ff-only origin/claude/referee`: HEAD = origin/claude/referee = 563d46c.
- `git rev-list --left-right --count origin/claude/referee...origin/claude/vibrant-johnson-nxvvxo` -> 0 ahead, 411 behind
  (trunk c2b1848). Trunk merged with `git merge --no-edit` (fast-forward: referee had no commits off trunk; no history rewritten):
  HEAD = c2b1848, 0 ahead / 0 behind. This file's commit adds one ahead.

### 2. Open work and next step of each
- In flight: none. Routed, waiting for GO: packet P-N5T (docs/new/G-N5-TERM-reading.md at trunk 812ecba; Lemmas A, B, Theorem;
  output docs/referee/R-N5T.md). Next step after GO: open VJ00 (BRICS RS-00-48) myself, check Lemma 5.2, 5.7, Prop. 6.1 and the
  5.8 direction against the text, then re-derive Lemma B and the φ potential against N5's spec S1-S5.
- Carried from the predecessor (each waits on a Lead packet; not started unasked): wording fixes routed to L-ALG (G9-b1, G10-a1
  V=∅ convention, N11-a1/G11-a1 cites); GAP-A joint state (CTX⁺) ∧ (FIRED⁺-R), DATA only.
- Before running probes: rebuild Oink (scripts/setup_oink.sh; tools/ is gitignored) so the gate's smoke step runs.

### 3. docs/GAPS.md rows relevant to my packet (trunk c2b1848)
- G-N5-TERM, major, owner L-NEW (L-COMP checks runs), OPEN: "N5 SSI-GLOBAL terminates (gauntlet step 4, correctness)". The SPEC
  sentence "each iteration strictly improves σ or τ in Ξ" is FALSE as written (Odd switch closing a cycle changes τ with Ξτ
  unchanged; l-new 655af60/7039eb5); lexicographic repair proposed, not proved. DATA: no repeated (σ, τ) state in any run.
  Also open for step 4: the running-time bound (no route proposed).
- Standing rows from the DTL packets (GAP-A, GAP-C, G-S5-6, G-DOM) are unchanged and not part of P-N5T.

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D12 (index: active; Lead reading L33 active):
   > WE can run referees on opus too temperoraly
2. D1 (index: active):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
3. D14 (index: active; Lead reading L35 active), which created the lane whose claim P-N5T checks:
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well
   (L35 (3) keeps D1's "wrong until it passes the gauntlet" and bit cost for L-NEW's approaches.)

### 5. One trap that bit this lane, and the check that prevents it
- Trap: the container's local claude/referee was stale at every restart (1517 behind on 10-17, 1947 behind today); work on it
  would review an old tree and push a diverged branch. Check: `git fetch` both branches, `git rev-parse HEAD origin/claude/referee`
  must be equal before anything else, then merge trunk with a merge (never rebase).
- Proof-level trap (R-P3, G-STR): set-level arguments missed strategy-level effects. For P-N5T this means: for every switch the
  reading claims raises (Ω, φ), name which player's strategy changed and which node's valuation component moved.

## successor 5 (2026-10-24T21:04Z by date -u; Opus 5.5 under D15/L37, label "(Opus 5.5, D15)"; predecessor successor 4, handover bbd3e7b2)
Measured from the repository at the time of writing, not recalled.

### 1. Branch, head, distance to trunk
- Branch `claude/referee`. Local branch was STALE (73b46eb8, 2 behind origin). After `git fetch origin claude/referee
  claude/vibrant-johnson-nxvvxo` and `git merge --ff-only origin/claude/referee`: HEAD = origin/claude/referee = bbd3e7b2.
- `git rev-list --left-right --count origin/claude/referee...origin/claude/vibrant-johnson-nxvvxo` -> 2 ahead, 0 behind
  (trunk 27f5d2e2 = merge-base). The 2 ahead: dcee2233 (R-N5-Z §C) and bbd3e7b2 (notebook handover). This file's commit adds one ahead.

### 2. Open work and next step of each
- In flight: none. Routed, waiting for GO: packet P-N5-U1, object docs/new/P-N5-U1-box31.md at pin eee0d8a (an ancestor of trunk
  and of HEAD; `git show eee0d8a:docs/new/P-N5-U1-box31.md | sha1sum` = eb90788d2949050f316ed983fa56c34d7a1dd9c7, 200 lines: matches the brief).
  Report: fresh docs/referee/R-N5-U1.md. Next step after GO, in the brief's order: §4 Theorem U1 (with the κ_w-freeze and the
  transferred P3-1 repair), §3 CASC, §2 TB against N5 spec S1 and experiments/si/si.py, §1 Lemma R (open VJ00 myself, cite section),
  §5 Lemma WC, §6 (NH') reduction (READING; signed inputs only). Instances u1t_cex_n32.pg (63dfd785) and u1t_cex2_n32.pg (6162a26f),
  re-run with experiments/new/n5.py, Oink zlk, check_sol2.py; a probe that asserts exactly one Odd vertex with out-degree > 1.
- All earlier packets (R19-R22, P-N5-Z) are signed with §C done (notebook table); nothing else open.
- Before running probes: rebuild Oink (scripts/setup_oink.sh; tools/ is gitignored).

### 3. docs/GAPS.md rows relevant to me (trunk 27f5d2e2)
- REFEREE owns no row. The row my packets feed: G-N5-TIME, major, owner L-NEW ("referees later"), OPEN. Its last update (20:36Z):
  RESULTS R22 landed; open per phase: X (≡ Z up to n, P-N5-Z under review), ROI in U1-U3, W-CYC; "(U1-T) FALSE as stated
  (u1t_cex_n32)". P-N5-U1 is the U1 repair of that.
- G-N5-TERM closed (RESULTS R15, signed by me and REFEREE-2 under D12). DTL rows GAP-A, GAP-C, G-S5-6 open but paused (D18/L40).

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md), with DECISIONS-INDEX status
1. D1 (index: active; full text docs/decisions/D001-launch-brief.md lines 25, 49):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D15 (index: active; Lead reading L37 active: referees on Opus 5.5, label "(Opus 5.5, D15)"):
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
3. D18 (index: active; Lead reading L40 active: labels PROVED (by whom) / CONJECTURE / OPEN, ASSUMPTION lines):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.

### 5. One trap that bit this lane, and the check that prevents it
- Trap (R-N5-Z data appendix; notebook lesson "Glob-based data can pull in out-of-class games"): a glob over instance directories
  pulled s_rt32_final, which is NOT in 𝒞^1O, into a 𝒞^1O check. Check: every probe asserts exactly one Odd vertex with out-degree > 1
  before using an instance (scratch/*_probe.py, via box25 common.odd_choice = first Odd chooser); I keep that assert in the U1 probe.
- Also again this restart: stale local branch (73b46eb8); check `git rev-parse HEAD origin/claude/referee` equal before any work.
