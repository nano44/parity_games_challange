# REFEREE-2 handover check (successor 40, session_01V5yGRWQ1pY9BpJ6WvVvBoi; Opus 5.5 per D1 / D21 / L53; 2026-11-13T02:32Z by date -u)
1. Branch claude/referee-2. At start the local claude/referee-2 already equalled origin; after fetch --unshallow + fetch + checkout +
   merge --ff-only («Already up to date»): `git branch --show-current` = claude/referee-2, HEAD = origin/claude/referee-2 = 0f2606da
   (before this commit). vs trunk claude/vibrant-johnson-nxvvxo e8b6abf0 (fetched 02:31Z): 16 ahead / 338 behind, merge-base 98a64b91
   (17 ahead with this commit). No trunk merge made: trunk files are read with `git show`.
   Clock: date -u against the Date header of a raw.githubusercontent.com response at 02:31:55Z: skew 0 s.
2. Open work (from successor 39's HANDOVER 0f2606da: no open items of its own; the Lead's brief adds A-D):
   A. STANDBY: any item CHECKER routes back on R128 / R129 / R130 (P-N5-GATE / P-N5-LEVEL / P-N5-WRAP). Next step: none until routed;
      then the byte-test form of R2-P-N5-LEVEL / R2-P-N5-WRAP Addenda (own rebuild from the earlier line + the fixes pairs, cmp, meaning).
   B. Agreement line for P-N5-WRAP L-2 (my verdict 01e83df5: MATCHES, stays as is). REFEREE 34's byte test claude/referee 32d61d60 is
      NOT yet on origin (origin/claude/referee = 28b95151 at 02:3xZ; «Not a valid object name 32d61d60»). Next step: re-fetch; once it is
      there, read it and add one line «agrees / differs at …» to R2-P-N5-WRAP.md.
   C. PRE-READ of box 212 RF-LEVEL (claude/l-new be167574 is on origin: docs/new/N5-RFLEVEL-box212.md + Addendum A, tools
      experiments/new/box212/). Next step: hash the inputs at be167574; list per statement (RF-A, RF-B, RF-C, RF-D with [IMP3] / [L3],
      the §2 reading, kill criteria) premises (landed or not, by script), proof gaps, genome-only steps, DATA-rule clauses, scope against
      TARGET.md (not N5; RF-D a conditional reduction; G-N5-TIME OPEN); re-derive RF-B (P1)-(P5′) and RF-C's arithmetic myself;
      write docs/referee-2/R2-box212-preread.md. Independence: I do NOT read L-RED's R239 (claude/l-red 2cc894f2, docs/red/
      R239-rflevel.md) until my pre-read is pushed; then an agreement section.
   D. When the Lead routes it (commit to come): Lean SPEC definitions (lean/lemmas/PGLemmas/Spec.lean, SpecGamma3.lean) against SPEC
      (docs/new/N5-ssi-global.md l. 24-127) and si.py l. 78-205, one deviation at a time. Next step: wait for the commit.
3. GAPS rows: none owned by REFEREE-2 (owner column of docs/GAPS.md at trunk e8b6abf0 has no REFEREE-2 entry; «referee-2» occurs
   only in gap texts, e.g. G-S5-6 «32,026 referee-2 runs», G-K5, G-Bthr, G-DOM).
4. Rulings (status from docs/DECISIONS-INDEX.md at trunk e8b6abf0; text verbatim from docs/DECISIONS.md lines 7, 8, 333, 452 there):
   - D1 (active): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's
     own, as wrong until it passes the gauntlet below.» and «Never downgrade the referee to save money.»
   - D18 (active): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of
     mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them
     briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
   - D21 (active), first sentence of the relayed text: «Okay, I want maximum effort.» (full text: docs/DECISIONS.md#d21). Lead readings
     L51 (maximum effort to 2026-11-14 10:05Z), L52 (a limit that has reset is a pause), L53 (this session runs on Opus 5.5, the fleet's
     strongest available model now; D1's «Never downgrade the referee to save money» kept). If my turn fails on a limit, I resume from
     notes/REFEREE-2.md when woken.
5. Trap (bit successor 39 at 00:02Z): an UNQUOTED heredoc (<<EOF, used to expand a date) executed a backquoted «`git show`» and pasted a
   whole commit into R2-P-N5-LEVEL.md l. 413-435 (correction note 2c5695ec). Check now: every heredoc is quoted (<<'EOF'); the date goes
   in with sed afterwards; before commit, «git diff --cached | grep -c '^+commit '» must be 0 and the diff is read.
   Standing trap: a stale / shallow / detached local branch («invalid refspec»): fetch --unshallow + fetch + checkout + ff-only, then
   branch = claude/referee-2 and HEAD = origin before any commit; push.sh only as a tracked task (2-hour timeout, output to a file, echo
   exit $?, pgrep first, never commit while it runs).
