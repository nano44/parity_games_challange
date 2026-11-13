# REFEREE-2 handover check (successor 42, session_01V5yGRZt3cYejaeDH2kG1gc; effort xhigh per D24, under D1 / D18 / D25 / D26; model as in the Lead's roster; 2026-11-13T15:57Z by date -u)
1. Branch claude/referee-2. Trap check at 15:56Z (fetch --unshallow + fetch + checkout + merge --ff-only; the local checkout was 15
   commits behind and fast-forwarded): `git branch --show-current` = claude/referee-2, HEAD = origin/claude/referee-2 = da20a307
   (successor 41's Addendum 1 commit; before this commit). vs trunk claude/vibrant-johnson-nxvvxo 38f4a6a0 (fetched 15:57Z): 15 ahead /
   487 behind, merge-base 0f2606da (16 ahead with this commit). No trunk merge (L56): trunk files are read with `git show`.
   Clock: date -u against the Date header of a raw.githubusercontent.com response at 15:56:38Z: skew 0 s.
   `pgrep -f "bash scripts/push.sh"` at 15:56Z: nothing running.
2. Open work (successor 41's HANDOVER at da20a307 and the Lead's brief of 15:55Z), in order:
   1. FIXES-FILE CHECK of P-N5-EXP (claude/l-red-b 350d84eb, docs/red-b/P-N5-EXP.md sha1 c0449b17…, FROZEN): (a) entries 2-5 of
      docs/red-b/P-N5-EXP-fixes.md against my lane's items G-1, M-1, W-1, W-2, D-1 and Addendum 1; (b) the L41 cross-signature: sign or
      refuse LEMMA′ (the first referee's form, restated in entry 4) independently, with my lane's engine (r2exp.py lineage), named
      must-0 counters and a firing control (the lemma as frozen must fail at (j, a, t) = (1, 1, 2^k − 1)), and the concordance claim
      «PREFIX FORM = LEMMA′ at τ_0 = T»; (c) frozen guard (packet sha1 unchanged, fixes file append-only). State at 15:57Z: the fixes
      commit 24f4d436 is NOT on origin (origin/claude/l-red-b = f755b8a4, which holds entry 1 only). Next step: re-read my lane's
      R2-P-N5-EXP.md §2.4 and Addendum 1, prepare the engine in the scratchpad (no commit), wait for `git ls-remote`, then write
      Addendum 2 of R2-P-N5-EXP.md, commit, push, compare ls-remote, send the SHA.
   2. AGREEMENT NOTE with the first referee's report (docs/referee/R-P-N5-EXP.md, REFEREE 36): NOT opened; next step: open it only
      after item 1 is committed, then list agreement and difference by item number.
   3. If context allows: referee box 108's Lemma STEP (32-class table) and MOVE (claude/l-si 8c062914, docs/si/box108-gk-proof.md) as
      the second derivation of EXP-IDEAL (b): «checked» per lemma or the gap. Not needed for the landing.
   4. DEFERRED (Lead 14:19Z, repeated 15:55Z): the second review of P-N5-KEY1P. Standby A (R128-R130 items from CHECKER): none routed.
3. GAPS rows: none owned by REFEREE-2 (docs/GAPS.md at trunk 38f4a6a0: 0 rows with REFEREE-2 in the owner column, by awk on column 3).
4. Rulings (status from docs/DECISIONS-INDEX.md at trunk 38f4a6a0; text verbatim from docs/DECISIONS.md there, lines 7, 8, 333, 541):
   - D1 (active): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's
     own, as wrong until it passes the gauntlet below.» and «Never downgrade the referee to save money.»
   - D18 (active): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of
     mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them
     briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
   - D25 (active): «So put everything into trying solving it today» (Lead readings L58 / L59, active: D1's standard of proof
     unchanged). With it D24 (active): «do xhigh», and D26 (active; DECISIONS.md line 567): «I hit my usage limit while you were
     working, but it has reset now. Please continue from where you left off.» (Lead reading L60, active). If my turn fails on a limit
     I resume from notes/REFEREE-2.md when woken.
   Also binding on item 1 (b): L41 (active, Lead reading): a referee-originated proof counts as two-referee signed when its author
   signs it and the other referee independently signs it.
5. Trap (bit this lane today): scripts/push.sh can print exit 0 after «RPC failed; HTTP 503» with origin unchanged (Lead 13:10Z), and a
   container restart killed successor 40's running push, so a handover commit was missing from origin when its successor started.
   Check now: before every commit `git fetch origin claude/referee-2` and HEAD = origin/claude/referee-2 (or strictly ahead of it by
   my own commits); `pgrep -f "bash scripts/push.sh"` before any push; push only as a tracked background task (2-hour timeout, output
   to a file, `echo exit $?`, no pipe, no `&`); after every push and after any restart compare `git ls-remote origin
   claude/referee-2` with the local SHA and re-run the push if they differ; no commit while a push runs. Standing traps kept: SHAs
   quoted only from git output in a step after the commit; python run from the repo writes __pycache__ under docs/referee-2/ (remove
   before commit); no file created under docs/ while push.sh verifies (scratchpad first, copy after the push exits); docs/referee/ on
   an object is opened only after my own report on it is committed (for P-N5-EXP: after Addendum 2).
