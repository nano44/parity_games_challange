# Handover check: L-RED-B successor 3 (second adversary lane; Opus 5.5 per the brief, L53; D1 / D18 / D21, Lead readings L51-L53; written 2026-11-12 20:05Z by date -u)
Every answer is measured from the repository at the time above (commands named), not recalled. Predecessors: L-RED-B session 1 (handover
9e8796cc, notes/L-RED-B.md «SESSION 1 HANDOVER», docs/red-b/B1-box208.md) and successor 2 (handover check 977d7ab5 only; stopped by the
Fable weekly limit ~19:38Z). Successor 2's local commit 8d5d8388 is NOT on origin: `git cat-file -t 8d5d8388` -> «fatal: Not a valid
object name». Its B2 / B3 tools (eng3.py, lev3.py, xcheck3.py, n5xi3.py, sweep3.py, climb3.py, run_b2.sh, gw.py, gclimb.py, n5real.py,
gfam.py) and its draft docs/red-b/B2-box209.md are lost; I rebuild what I need. Its smoke readings (relayed by the Lead) are not DATA.
Trap check on entry (20:00Z): the local branch was 1 behind origin; `git merge --ff-only origin/claude/l-red-b` fast-forwarded it;
`git branch --show-current` -> claude/l-red-b; HEAD = origin/claude/l-red-b = 977d7ab5. Clock skew against the Date header of a
raw.githubusercontent.com response: 0 s (local 20:00:37Z, header 20:00:37 GMT).

## 1. Branch, head, distance to trunk
- `git branch --show-current` -> claude/l-red-b.
- `git rev-parse HEAD origin/claude/l-red-b` -> both 977d7ab5387830187795e9a41e0d001bdc26f37d (before this file's commit).
- Trunk `git rev-parse origin/claude/vibrant-johnson-nxvvxo` -> 7fa6aff4aa04054fe063abaa57889591883db014.
  `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 5 ahead, 24 behind; merge-base
  471aba45214c9b4009332ef1d498dd5dbc42f3cb. I do not merge trunk; inputs are read with `git show <ref>:<path>`.
- Read-only refs fetched 20:00Z: origin/claude/l-new 069c888b6d0ab6bc124e32424f50f4372da0a4a1, origin/claude/l-si
  516b68371860623df13db77ecf312693eabb1c6b, origin/claude/l-red 2d290a15b672c9a86caa8ceb49df4adb3b4be510, origin/claude/l-comp
  aa863db51fa9ff1e103940f62168c4b9a0d6ce55.
- Files I own: docs/red-b/, experiments/red-b/, notes/L-RED-B.md, this file.

## 2. Open work and the next step of each
- B1 (box 208): CLOSED by session 1 (no kill; PLATEAU write-up gap G-1 in (P6) step (ii)). Nothing owed.
  `pgrep -af "push.sh|python"` -> nothing; `git status --short` -> clean (before this file).
- B2 (box 209). Object measured here: claude/l-new 3f8960998427db1f67daab4d7fdab210344643cc docs/new/N5-LEVEL3-box209.md, sha1
  943568034d3b46ccf85558d9957ae8d52d8ace93 (356 lines); Addendum A at 311bbf81faa525eda9c09ad15d0b0d170a2c25e9, same file sha1
  147c889b53695933a6703a70f6ec192c16cc6d04 (377 lines). Not read by me yet. Next steps after «go», in order:
  1. Read the box and Addendum A in full; re-quote its premises from trunk docs/RESULTS.md (R117, R104, R118, R121 E-DOM, R124, R125,
     R15 (a)); quote by line the Γ3 definition (R117's packet + box 209 §1) that my builder implements.
  2. Own Γ3 builder (pads pA, s, q, r, pe_g, pβ_g, pb_g, movers m_(x,k)) on session 1's eng.py; own HOW3 run (N5′-xi from S3 to its
     first fallback, as the box defines it); validated by brute force over Odd strategies on small genomes. The lane's gamma3.py is not
     imported. A second, structurally different N5′-xi run for N5XI-G3's count (SPEC lines quoted).
  3. Must-0 counters: LEVEL3 (Φ values ≤ P3 = 2M(N + 4M)), PLATEAU3 (plateau and final tail ≤ n_E3 = N + 6M + 9), T3-ALL
     (T3 ≤ P3(n_E3 + 1) + n_E3), N5XI-G3 (iterations = T3 + 3), and each premise fact the proofs use; each with a control that fires.
  4. Exhaustive small genomes, random strata, mutants, climbs on T3 / bound, every tie branch; locate the use of E-DOM (L-SI 52: N5′-xi
     exponential on F_n with E-DOM dropped) and check it is valid on Γ3.
  5. Verdict per lemma SURVIVES / GAP / KILL in docs/red-b/B2-box209.md, then to the Lead.
  Independence: I do not read L-SI's replay (claude/l-si 925577fe), L-COMP's BOX 44 or REFEREE 33's R-box209-preread.md before my verdict.
- B3 (GUIDE-RULE, kill attempt on N5): after B2. Climb N5 (SPEC, lines quoted) iterations over guided wrappers Wg(H, s0, ρ0) and variants
  whose frozen faces disagree with Odd's true reply; L-SI's tools at claude/l-si 2051a0ee6df5ecc17463a1ce80a9eb65ea9e492a (`git ls-tree`
  finds experiments/si/box104/gscan104.py, glo104.py, guide104.py); score = iterations / |V| and growth over a family; every best on a
  second engine + Zielonka, frozen with sha1. Clearly super-polynomial growth on two engines -> Lead at once as CANDIDATE KILL, nothing more.

## 3. docs/GAPS.md rows
- Owned: none (open table rows 6-11 at trunk 7fa6aff4: GAP-A, GAP-C, G-S5-6, G-NEST, G-N1-LB, G-N5-TIME; none names L-RED-B).
- Worked against: G-N5-TIME (line 11: severity major, owner «L-NEW (L-LIT T22; referees later)», status **open**; 215,460 characters,
  measured with python; it ends «G-N5-TIME stays open.»). Box 209 is a lane candidate, not a row.

## 4. Owner rulings, verbatim
- D1 (docs/DECISIONS.md line 7; DECISIONS-INDEX line 5, status **active**):
  > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
- D18 (docs/DECISIONS.md line 333; DECISIONS-INDEX line 32, status **active**):
  > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
- D21 (docs/DECISIONS.md line 452; DECISIONS-INDEX line 46, status **active**), relayed text, verbatim:
  > Okay, I want maximum effort. I want to use 200% usage in 3 days. There is fable 5.2 as well, use that too in dpeth everywhere where it seems fitting, use fable 5.2 at hard or xhigh. SO yes, 200% uage under 2 days.
  Direct confirmation (line 454): «I confrim tge stuff». Lead reading L51 (not the owner's words): maximum effort until 2026-11-14 10:05Z.
  The brief adds L53 (Fable weekly limit reached, resets 2026-11-18 21:00Z; this session runs on Opus 5.5).
- The owner's approval of a second adversary (2026-11-12, per the brief): `grep -n "L-RED-B\|second adversary"` on trunk
  docs/DECISIONS.md finds nothing; the Lead holds those words.

## 5. One trap that bit this lane before, and the check that now prevents it
- Trap (today, successor 2): work committed locally but never pushed is lost with the container (8d5d8388 is gone). Check: commit and
  push in batches during B2, not only at the end; keep long jobs resumable in experiments/red-b/work/ (ignored by the lane's
  .gitignore line 1) and move evidence to data/ before each commit; `git cat-file -t <sha>` on origin before quoting a SHA as pushed.
- Older trap (session 1, fbb6a062 -> 0510c800): the root .gitignore line 4 `experiments/*/out/` ignores outputs (measured now:
  `git check-ignore -v experiments/red-b/out/x.out` -> `.gitignore:4:experiments/*/out/`). Evidence goes to experiments/red-b/data/,
  pinned in data/SHA1SUMS, checked by check.sh in the gate.
- Standing (CLAUDE.md Traps): a counterexample from an unfaithful implementation is not one; my Γ3 engine is new, so any violation is a
  suspect bug until the definition lines are quoted, the instance re-derived by brute force and on a second engine, and frozen by sha1.

## 6. State at this commit
- No CPU job started; none starts before the Lead's «go». This commit is pushed by `bash scripts/push.sh` as a tracked background task
  (2-hour timeout, output to a file, exit code printed); no commit while it runs.
