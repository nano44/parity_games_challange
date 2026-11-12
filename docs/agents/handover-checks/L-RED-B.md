# Handover check: L-RED-B successor 2 (second adversary lane; model and effort: see the roster in docs/NOW.md; D1 / D18 / D21, Lead reading L51; written 2026-11-12 18:20Z by date -u)
Every answer is measured from the repository at the time above (commands named), not recalled. Predecessor: L-RED-B session 1, handover
commit 9e8796cc (notes/L-RED-B.md «SESSION 1 HANDOVER», docs/red-b/B1-box208.md), both read in full.
Trap check on entry: `git branch --show-current` -> claude/l-red-b; HEAD = origin/claude/l-red-b; clock skew against the Date header of
a raw.githubusercontent.com response: 0-1 s (local 18:16:30Z, header 18:16:31Z).

## 1. Branch, head, distance to trunk
- `git branch --show-current` -> claude/l-red-b.
- `git rev-parse HEAD origin/claude/l-red-b` -> both 9e8796cce2bc80089276fdd193b835572e33f00f (before this file's commit).
- Trunk `git rev-parse origin/claude/vibrant-johnson-nxvvxo` -> 68c8d29339d5945efe6878a7e4cfc9d6a1611d48.
  `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 4 ahead, 22 behind; merge-base
  471aba45214c9b4009332ef1d498dd5dbc42f3cb. I do not merge trunk (no instruction to; my inputs are read by `git show <ref>:<path>`).
- Read-only refs fetched (`git rev-parse`): origin/claude/l-new 5ca65a0a65d86d139126c0d4621ef3532b97e972, origin/claude/l-si
  a9ea60b96a55a0917c0e3e5ff4bd73ca8332ea15, origin/claude/l-red 5eca1c32837b9330e8fd52f1b31d51b0f6d04ca8, origin/claude/l-comp
  de9271580ed80490170bc6c8e0d2ffc7ed2c4538.
- Files I own: docs/red-b/, experiments/red-b/, notes/L-RED-B.md, this file. Nothing else is edited.

## 2. Open work and the next step of each
- B1 (box 208): CLOSED by the predecessor (NO KILL; write-up gap G-1 in PLATEAU (P6) step (ii), repaired by the lane). Nothing owed.
  `pgrep -f "bash scripts/push.sh"` -> no process; no CPU job running; `git status --short` -> clean.
- B2 (box 209, NOT opened by the predecessor, NOT opened by me yet beyond measuring it). Object, measured here:
  claude/l-new 3f8960998427db1f67daab4d7fdab210344643cc docs/new/N5-LEVEL3-box209.md, sha1 943568034d3b46ccf85558d9957ae8d52d8ace93
  (356 lines), and the same file at 311bbf81faa525eda9c09ad15d0b0d170a2c25e9 (Addendum A), sha1
  147c889b53695933a6703a70f6ec192c16cc6d04 (377 lines; `git diff --stat` 3f896099..311bbf81: +21 lines in that file).
  Next steps, in order (after «go»):
  1. Read the box and Addendum A; re-quote its premises by script (requote.py) from trunk docs/RESULTS.md (R117, R104, R118, R121, R124,
     R125, R15 (a)); read R117's definition of Γ3 in its landed packet and quote the lines my builder implements.
  2. Own Γ3 builder on top of eng.py (pads from R117 + box 209 §1, by line), own HOW3 run (N5′-xi from S3 up to its first fallback, as the
     box defines it), validated against brute force over all Odd strategies on small genomes and against a naive play walk. The lane's
     gamma3.py is not imported. A second, structurally different run of N5′-xi / N5 for N5XI-G3's count (SPEC lines quoted).
  3. Port lev.py / press.py: must-0 counters for LEVEL3 (Φ values ≤ P3 = 2M(N + 4M)), PLATEAU3 (plateau and final tail ≤ n_E3 =
     N + 6M + 9), T3-ALL (T3 ≤ P3(n_E3 + 1) + n_E3), N5XI-G3 (iterations = T3 + 3), every premise fact used ((K2′) / (K0′) at the pads
     pb_g, (L2′) at pe_g, (P4) case (3), (D1′), NO-TIE3, the tie-rule step); each counter with a control that must fire.
  4. Attacks: exhaustive small genomes as in B1, random strata, mutants, climbs on T3 / bound and on plateau length, every tie-breaking
     branch (ties.py); find exactly where E-DOM (or CORE-ABOVE) is used and whether that use is valid on Γ3; exact VJ ties.
  5. Verdict per lemma (SURVIVES / GAP / KILL with a frozen instance, sha1, numbers) in docs/red-b/B2-box209.md, then to the Lead.
  Independence: I do not read L-SI's box 209 replay (claude/l-si 925577fe, box 103 Addendum B), L-COMP's, L-RED's or any referee's
  report on box 209 before my verdict is sent.
- B3 (GUIDE-RULE, a kill attempt on N5 itself; after B2 or in its idle CPU time): hill-climb N5 (SPEC; SPEC lines quoted before any
  count is reported) iterations over guided wrappers Wg(H, s0, ρ0) and variants whose frozen faces disagree with Odd's true reply; score
  = iterations / |V| and growth along a parametrised family; every best re-run on a second engine + Zielonka, frozen with sha1. Inputs to
  read first: claude/l-si 26704e01 (box 104 freeze: Lemma WRAP, guided wrappers) and its Addenda (01900837), tools
  experiments/si/box104/guide104.py, free104.py, climb104.py (`git ls-tree` on origin/claude/l-si finds these three; gscan104.py and
  glo104.py are not at a9ea60b9: «in its next pushes» per the brief). A family with clearly super-polynomial growth on two engines goes
  to the Lead at once as a CANDIDATE KILL for two referees, nothing more.

## 3. docs/GAPS.md rows
- Owned: none.
- Worked against: G-N5-TIME (docs/GAPS.md line 11: severity major, owner «L-NEW (L-LIT T22; referees later)», status **open**; the row
  is 205,943 characters; its last sentence: «G-N5-TIME stays open.»). Box 209 is a lane CANDIDATE; none of its statements is in the row.

## 4. Owner rulings, verbatim
- D1 (docs/DECISIONS.md line 7; DECISIONS-INDEX line 5, status **active**):
  > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
- D18 (docs/DECISIONS.md line 333; DECISIONS-INDEX line 32, status **active**):
  > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
- D21 (docs/DECISIONS.md lines 451-454; DECISIONS-INDEX line 46, status **active**), relayed text, verbatim:
  > Okay, I want maximum effort. I want to use 200% usage in 3 days. There is fable 5.2 as well, use that too in dpeth everywhere where it seems fitting, use fable 5.2 at hard or xhigh. SO yes, 200% uage under 2 days.
  Direct confirmation in the Lead session, verbatim: «I confrim tge stuff». Lead reading L51 (a reading, not the owner's words):
  maximum effort until 2026-11-14 10:05Z; a «rejected» limit still pauses, so I resume from the notebook when woken.
- The brief says the second adversary was approved by the owner on 2026-11-12. I have not seen the owner's words for that approval;
  the Lead holds them.

## 5. One trap that bit this lane before, and the check that now prevents it
- Trap (notes/L-RED-B.md «Things only I know»; commits fbb6a062 → 0510c800): the root .gitignore line 4 `experiments/*/out/` ignores
  outputs, so the first B1 commit went out without its evidence. Measured now: `git check-ignore -v experiments/red-b/out/x.out` ->
  `.gitignore:4:experiments/*/out/`; `experiments/red-b/work/` is ignored by the lane's own .gitignore (scratch for running jobs).
  Check: outputs that are evidence go to experiments/red-b/data/ and are pinned in data/SHA1SUMS (check.sh verifies the pins inside the
  gate); before every commit `git status --short --ignored experiments/red-b` and `git check-ignore -v` on each file a report cites.
- Second trap, standing (CLAUDE.md, Traps): «A "counterexample" from an unfaithful implementation is not a counterexample: the referee
  checks pseudocode against the paper first.» The Γ3 / HOW3 engine will be new, so a violation it reports is first a suspect bug: before
  any KILL verdict I quote the definition lines the engine implements, re-derive the instance by brute force over all Odd strategies and
  on a second engine, and freeze it with its sha1. The mirror trap holds too: zero violations on short runs test the logic, not the bound.
- Found today, small: `rev` on docs/GAPS.md line 11 (205,943 characters, multi-byte) hangs; I read that row with python instead.

## 6. State at this commit
- No CPU job started. No long job starts before the Lead's «go». This commit is pushed by `bash scripts/push.sh` as a tracked background
  task (2-hour timeout, output redirected to a file, exit code printed); I do not commit while it runs.
