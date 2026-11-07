# L-SI handover check (successor 43, Opus; written 2026-11-07T21:26Z (date -u); successor 42 = session_01V5yGRWb17CZoo2UVcHAxp8)

1. Branch claude/l-si. Fetched --unshallow; checked out claude/l-si; ff-only: local = origin/claude/l-si = 08340ef2743dfda5578a2af89c2319640de1042d
   at start (`git branch --show-current` = claude/l-si). Before the merge: 6 ahead / 75 behind trunk claude/vibrant-johnson-nxvvxo aea87f1a
   (trunk commit 2026-11-07T20:35Z). Merged trunk by merge commit ece1a3c2: now 7 ahead / 0 behind; merge-base = aea87f1a.
2. Open work:
   (i) BOX 81 (Lead brief, after «go»): BRIDGE between the tower route (N5, R104/R117) and the N5'-xi route (R118, box 193 ASC1).
       Next step: copy an exact N5'-xi runner on Gamma3 (L-NEW box191 idealcyc/subrun191 or the R118 reference) into experiments/si/box81/,
       xcheck on >= 2 instances, then the ascent census (unit play, set all plays of the run, scope stored start) on the library + SL41,
       H5_d20_F62, H6_d24_F126, L6Z_KILL238; deliver docs/si/box81-bridge.md.
   (ii) P-IDEAL-DBL / R119: answer any CHECKER item of the second fill (fixes entry 3 + L-4 by script, as mkL3.py; never edit packet/L-1..L-3).
   (iii) Box 80 core (parked-decider block, 48/127 failing 6-windows): open, not proved. Tower climbs belong to L-COMP 11: do NOT climb.
3. GAPS rows: L-SI owns none (docs/GAPS.md at ece1a3c2: the only L-SI mention is inside G-N5-TIME, owner L-NEW, open). The lane works under G-N5-TIME.
4. Rulings (verbatim, docs/DECISIONS.md; all "active" in docs/DECISIONS-INDEX.md):
   - D18 (l. 333): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and
     computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me
     questions. Clearly distinguish proven results from conjectures and open problems.»
   - D1 (l. 7): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong
     until it passes the gauntlet below.»
   - D14 (l. 245-246): «D» / «You know it can also test prveiously not tested approaches, it can come up with it own as well»
5. Trap: container starts detached / shallow / with a stale local branch, so push.sh fails after VERIFY PASS («invalid refspec»). Check: fetch --unshallow,
   `git branch --show-current` = claude/l-si and HEAD = origin/claude/l-si before work and before every push. Second trap: `pgrep -c push.sh` prints 0 while
   a push runs (process name is bash): use `pgrep -fc scripts/push.sh`; never commit during a push.
