# REFEREE-2 handover check (successor 41, session_01V5yGRZX8GpZ4VDaJbszYWA; effort xhigh per D24, under D1 / D21 / D25; model as in the Lead's roster; 2026-11-13T11:57Z by date -u)
1. Branch claude/referee-2. Trap check at 11:30Z (fetch --unshallow + fetch + checkout + merge --ff-only): `git branch --show-current` =
   claude/referee-2, HEAD = origin/claude/referee-2 = 4657952d (EARLY START: successor 40's handover commit not yet on origin; nothing
   committed while waiting). abd629d7 landed on origin at 11:56:26Z (git ls-remote); `git merge --ff-only`: HEAD = origin/claude/referee-2
   = abd629d7 (before this commit). vs trunk claude/vibrant-johnson-nxvvxo 5d7aab0f (fetched 11:56Z): 9 ahead / 483 behind, merge-base
   0f2606da (10 ahead with this commit). No trunk merge (L55 withdrawn; L56): trunk files are read with `git show`.
   Clock: date -u against the Date header of a raw.githubusercontent.com response at 11:30:37Z: skew 0 s.
2. Open work (successor 40's HANDOVER, abd629d7, «OPEN / NEXT for successor 41», and the Lead's brief of 2026-11-13):
   1. Addendum 3 of docs/referee-2/R2-key-preread.md: pre-read of box 217 §6 (Lemma 0, A1-A4, A2-POLY, §6.4 Lemma BRIDGE) and §7 (A7
      FLIP-SUPPLY, A7′) at claude/l-new a143d406 (docs/new/N5-QUIETKEY-box217.md sha1 7753bf3b…, 236 lines; it contains b0e03795 and §5
      A6′). State: every statement re-derived on paper; own engine (r2onep.py lineage, r2end primitives) written in the scratchpad with
      named must-0 counters and firing controls, second-scale runs only (no commit, no long job). Next step after «go»: copy the engine
      and its outputs into docs/referee-2/R2-key/, write the addendum (verdict per item with the exact line of any gap), commit, push.
   2. Any lane KILL of N5 on Ξ-acyclic genomes (a family with growing enumeration depth) or PROOF of SW-POLY comes to me first. Next
      step: none until routed; then for a kill: rebuild the family from its written rule, run N5 itself (n5v spec, and my r2end engine)
      on Γ3 at every size the budget allows, check every output against Zielonka, fit with residuals; for a proof: find the gap.
   3. Full second review when the Lead freezes a packet (P-N5-KEY1P or the kill packet). Next step: none until frozen. docs/referee/ on
      the same object is read only after my own report is committed.
   4. STANDBY A: any item CHECKER routes back on R128 / R129 / R130. Next step: none until routed (byte-test form of the addenda).
3. GAPS rows: none owned by REFEREE-2 (docs/GAPS.md at trunk 5d7aab0f: 0 rows with REFEREE-2 in the owner column, by awk on column 3).
4. Rulings (status from docs/DECISIONS-INDEX.md at trunk 5d7aab0f; text verbatim from docs/DECISIONS.md there, lines 7, 8, 333, 541):
   - D1 (active): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's
     own, as wrong until it passes the gauntlet below.» and «Never downgrade the referee to save money.»
   - D18 (active): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of
     mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them
     briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
   - D25 (active): «So put everything into trying solving it today» (Lead reading L58, active: the whole fleet works on box 217's
     question today, either answer taken; D1's standard of proof unchanged). With it D21 (active; Lead readings L51, L58: maximum effort
     until 2026-11-14 10:05Z) and D24 (active): «do xhigh». If my turn fails on a limit I resume from notes/REFEREE-2.md when woken.
5. Trap (bit successor 40 at its handover, ~10:1xZ to 11:27Z today): a container restart killed the running push.sh, so the handover
   commit abd629d7 was not on origin when this session started; a commit made on 4657952d would have forked the branch. Check now:
   before every commit `git fetch origin claude/referee-2` and HEAD = origin/claude/referee-2 (or strictly ahead of it by my own
   commits); `pgrep -f "bash scripts/push.sh"` before any push; push only as a tracked background task (2-hour timeout, output to a
   file, `echo exit $?`, no pipe, no `&`); after any restart: `git ls-remote origin claude/referee-2` against HEAD and re-run the push
   if they differ. Standing traps kept: quoted heredocs only (<<'EOF'; the date goes in with sed; `git diff --cached | grep -c
   '^+commit '` must be 0); no file created under docs/ while push.sh verifies (scratchpad first, copy after the push exits).
