# REFEREE-2 handover check (successor 39, session_01V5yGRaEeN3dRqjQP5twiRH; model and effort as in the Lead's roster; 2026-11-12 19:58Z by date -u)
1. Branch claude/referee-2. The container's local claude/referee-2 was 887 commits behind origin at start; after fetch --unshallow +
   fetch + checkout + merge --ff-only: `git branch --show-current` = claude/referee-2, HEAD = origin/claude/referee-2 = 0df0fdd8
   (before this commit). vs trunk claude/vibrant-johnson-nxvvxo 7fa6aff4 (fetched 19:57Z): 4 ahead / 332 behind, merge-base 98a64b91
   (5 ahead with this commit). No trunk merge made: trunk files are read with `git show`.
   Clock: date -u against the Date header of a raw.githubusercontent.com response at 19:57:35Z: skew 0 s.
2. Open work (successor 38 was stopped by the Fable weekly limit ~19:38Z with no handover; taken from its «Resume point 2», 0df0fdd8):
   A. R2-P-N5-GATE Addendum 5 is DONE and on origin (0df0fdd8: L-5 l-si 7b0a58ae, sha1 459fd88d MATCHES, re-signed). Remaining: one
      agreement line, ONLY after item B's verdict is pushed: read REFEREE 34's L-5 test on origin/claude/referee (if it exists) and add
      «agrees / differs at …» to R2-P-N5-GATE.md.
   B. Full independent SECOND review of P-N5-LEVEL: claude/l-new 1e6df499, docs/new/P-N5-LEVEL.md (sha1 7c956df4…, 65,874 B, 575
      lines), line docs/new/P-N5-LEVEL-line-L1.txt (sha1 28565b3c…, 7,239 B), quotes pinned at trunk 68c8d293, tools
      experiments/new/box211/. No review text exists yet; prepared tool docs/referee-2/R2-P-N5-LEVEL/r2q.py (render of landed R104,
      R118, R121, R123, R126 at 68c8d293). Next step after «go»: hash-check the frozen inputs; re-derive every proof; premises by script
      against landed RESULTS; own replay with firing controls; DATA rule (L43, each DATA clause names its counter); TARGET.md diff;
      scope (Howard ALL-SWITCH, MAXIMISER improves, IDEAL-CYC on R104 genomes only; not N5, not N5′-xi, not M4); name every
      genome-only step; check (C4) uses landed R126 QUIET-N and no step uses (P4) outside a plateau; L-1 against «To sign»; verdicts
      SIGN / SIGN WITH GAP / REFUSED with exact strings → docs/referee-2/R2-P-N5-LEVEL.md, section by section. REFEREE 34 reviews in
      parallel: I do NOT read docs/referee/ on P-N5-LEVEL or box 208 (incl. R-box208-preread.md) before my verdict is pushed.
3. GAPS rows: none owned by REFEREE-2 (owner column of docs/GAPS.md at trunk 7fa6aff4 has no REFEREE-2 entry; «referee-2» occurs
   only in gap texts, e.g. G-S5-6 «32,026 referee-2 runs»).
4. Rulings (status from docs/DECISIONS-INDEX.md at trunk 7fa6aff4; text verbatim from docs/DECISIONS.md lines 7, 8, 333, 452 there):
   - D1 (active): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's
     own, as wrong until it passes the gauntlet below.» and «Never downgrade the referee to save money.»
   - D18 (active): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of
     mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them
     briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
   - D21 (active), first sentence of the relayed text: «Okay, I want maximum effort.» (full text: docs/DECISIONS.md#d21). Lead readings
     L51 (maximum effort to 2026-11-14 10:05Z), L52 (a limit that has reset is a pause), and per the Lead's brief L53 (Fable weekly
     limit reached until 2026-11-18 21:00Z; this session runs on Opus 5.5; D1's «Never downgrade the referee to save money» kept).
     If my turn fails on a limit, I resume from notes/REFEREE-2.md when woken.
5. Trap: a container that starts with a stale, shallow or detached local claude/referee-2 (here 887 behind; earlier 884, 171, 157)
   makes push.sh fail («invalid refspec») or push the wrong head. Check, run before anything else: fetch --unshallow + fetch + checkout
   + merge --ff-only, then `git branch --show-current` = claude/referee-2 and HEAD = origin/claude/referee-2 before any commit.
   Second trap (bit successor 38 today): a session stopped by a model limit leaves no handover, so I write a resume point into
   notes/REFEREE-2.md at every commit and commit review sections as they are finished. Third: push.sh pushes only the commit it
   verified (40-70 min): pgrep -f "bash scripts/push.sh" first, tracked background task with a 2-hour timeout, output to a file then
   echo exit $?, no pipe, no &, never commit while it runs.
