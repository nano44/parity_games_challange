# Handover check: L-COMP (successor 4, Opus 5.5; written 2026-10-25T04:44Z by date -u)
Every answer measured from the repository at the time of writing, not recalled from notes/L-COMP.md.
Successor of session_01BmytANWGKiHZhXK9QC2rB2 (successor 3, parked 04:35Z after box 7 handover 9e53a0e1). Previous answers are in git history of this file.

## 1. Branch, head, distance to trunk
- Branch `claude/l-comp`. Local head at start was 298d2dc6, 679 commits BEHIND origin/claude/l-comp (stale container, again); working
  tree clean, so fast-forwarded to origin/claude/l-comp = 9e53a0e1 ("box 7 handover"; 298d2dc6 is its ancestor).
- Trunk `origin/claude/vibrant-johnson-nxvvxo` fetched: a9fc3c97 ("Lead: SN fixes final + L-COMP park merged; R30 draft for C39; NOW").
  `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` = 0 ahead / 17 behind; merge-base 9e53a0e1
  (trunk merged it at 565e428f). Fast-forwarded to trunk (no rebase, no merge commit needed): head a9fc3c97, 0 / 0; 1 ahead after this file's commit.
- Container: Oink not built (tools/oink/build absent); no python jobs running; no .tasks caches (results/box7/*.tasks/ absent).

## 2. Open work and the next step of each
- Box 7 rows not done (predecessor's runs were in ITS container; unreachable, caches lost):
  (a) box7.py n 5 subset quarters 3-4 (--offset 2, --offset 3; same command as the Q1-Q2 JSONs' "options" field), ~2 h each from zero.
  (b) box7w.py n 5 subset quarters 2-4 (--offset 1/2/3). Present on trunk: box7 n 4 canonical, n 4 all starts, n 5 Q1 (every4), Q2 (every4_off1);
      box7w n 4 canonical, n 4 all starts, n 5 Q1.
  Next step after GO: scripts/setup_oink.sh (check_instance gate), read the options field of the Q1/Q2 JSONs to reproduce the exact
  command, launch (a) and (b) with --jobs within the core budget, fill README rows Q234ROW / W5ROW.
- Then (orientation from the brief, not started): add R28 OE / OX, R29 OFFGATE / CN / NL / CLS1, R30 R-STICK / SN-PREFIX / LEAVE / ABS-COUNT′
  checks to the exact small-n tables using the referees' / lanes' checkers unmodified (first step: locate each checker; R30 is a draft
  (docs/agents/R30-draft.md) awaiting CHECKER C39). Report maxima J, K, S_o, X_SN, REL as DATA.
- Parked/low: sat-hard cells, counter_qpt growth class (no step unless routed).

## 3. docs/GAPS.md rows owned by L-COMP
None. `grep -n -i l-comp docs/GAPS.md` on a9fc3c97 hits only G-N5-TERM (closed; owner L-NEW, "L-COMP checks runs"). My tables feed G-N5-TIME
(owner L-NEW, open; open core per phase on o-cyclic 𝒞^1O: X (≡ Z) and K (wakes); R28/R29 landed, P-N5-SN in landing as R30).

## 4. Three owner rulings that most constrain this lane (verbatim; status from docs/DECISIONS-INDEX.md on a9fc3c97)
1. D18 (active), docs/DECISIONS.md:333:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
   Constraint (L40): exhaustive small-n tables for N5; every line labelled DATA / CONJECTURE / OPEN / READING, never PROVED by me; no owner questions.
2. D2 change 5 (D2 active), docs/DECISIONS.md:27:
   > 5. Gauntlet addition: every implementation also outputs positional strategies, and L-COMP verifies them on every
   (continues "test game."; TARGET.md §5). Constraint: any reported instance passes check_instance.py (n5b, Oink zlk, verify.py strategies).
3. D1 (active), docs/DECISIONS.md:6:
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   and DECISIONS.md:7:
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   Constraint: results only via scripts/push.sh and send_message to the Lead; any violation of a landed lemma goes to the Lead at once, checked first.

## 5. One trap that bit this lane, and the check that now prevents it
Trap: stale container / lost gitignored state. This container started 679 commits behind its own branch, and box 7's resumable .tasks caches
(gitignored) did not survive the session change, so "resumable" runs restart from zero. Check: git fetch + rev-parse/is-ancestor before any work
(done above); counts are taken only from pushed JSONs under results/box7/ (their "options" field pins the command), never from a remembered
partial run; a quarter is reported only when its JSON has tasks_done = all tasks.
Carried over: one phase key only (phaseprofile's (λσ, λτ, τ(o))), named in every table header.
