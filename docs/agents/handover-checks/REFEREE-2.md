# REFEREE-2 handover check (successor 31, Opus 5.5 under D1/D18/D20; 2026-11-07 14:13Z by date -u)
1. Branch claude/referee-2. At start the local ref was stale (cf5157fe, 1,030 behind origin); fetch --unshallow + ff-only to
   origin/claude/referee-2 65df9f94 (HEAD = origin, `git branch --show-current` = claude/referee-2). vs trunk
   claude/vibrant-johnson-nxvvxo 9315f36c: 6 ahead / 259 behind (merge-base 7891ba32). Merged trunk with a merge commit (no rebase)
   -> 82f61753, 7 ahead / 0 behind before this commit.
2. Open work: one item, routed after «go»: full independent review of P-TOWER-FUEL (L-LOWER 5), frozen at claude/l-lower 7f7ff6f5;
   docs/lower/P-TOWER-FUEL.md, line L-1 docs/lower/P-TOWER-FUEL-line-L1.txt (sha1 408470ad…, 3,699 B), check block
   experiments/lower/l5/p_tower_check.py. Next step: re-hash both files at 7f7ff6f5; quote-check every premise (R104, R105 ENC, R110,
   R113 ALIGN) byte-exact against trunk docs/RESULTS.md by script; re-derive MOVE, DOUBLE-EQ (E1)-(E5), PULSE-NEST, GAP-NEST,
   DOMINANCE-FREEZE (a)-(b), CROSS-ECONOMY (i)-(iii); replay I-ROOM G7_best_d28 and I-FUEL SL41_d28 and the §5 counters with my own
   r2moves.py R104 simulator; DATA rule per clause of L-1; TARGET.md diff. Report docs/referee-2/R2-P-TOWER-FUEL.md. docs/referee/ is
   not read for this packet until my verdict is written. Nothing else open (successor 30 handover: «No other open item»).
3. GAPS rows owned by REFEREE-2: none. docs/GAPS.md names REFEREE-2 only in notes of other rows (G-Bthr, G-K5 closed); G-N5-TIME owner
   is «L-NEW (L-LIT T22; referees later)», open.
4. D1 (active, DECISIONS-INDEX row D1; DECISIONS.md l. 7-8): «A claimed polynomial algorithm is far more likely to be wrong than right.
   Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.» «Never downgrade the referee to save
   money.»
   D18 (active; DECISIONS.md l. 333): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from
   areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them
   briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
   D20 (active; DECISIONS.md l. 423): «We have reset the weekly usage, so we can again work faster no?» (Lead reading L48 active).
5. Trap: SHAs typed into a Lead message before reading them from git output (successor 30: 3c1d24ab, 9e3a7fae, 76a6af5c invented), and a
   detached/stale local branch at container start (push.sh exit 128 after VERIFY PASS). Check: `git branch --show-current` prints
   claude/referee-2 before every push; commit, read `git rev-parse HEAD` output, and message the Lead in a LATER step, never in the same
   batch as the commit. Also: every «only» claim measured on every level before it is written (successor 30 N-3).
