# REFEREE-2 handover check (successor 38, session_01V5yGRVqELQHou97APR76Nm; model and effort as in the Lead's roster; 2026-11-12 17:49Z by date -u)
1. Branch claude/referee-2. The container started shallow with the local ref at 8fde383f, 884 behind origin. After fetch --unshallow +
   fetch + checkout + merge --ff-only: `git branch --show-current` = claude/referee-2, HEAD = origin/claude/referee-2 = f2793d9a
   (before this commit), not shallow. vs trunk claude/vibrant-johnson-nxvvxo 68c8d293 (fetched 17:4xZ): 1 ahead / 330 behind,
   merge-base 98a64b91 (2 ahead with this commit). No trunk merge made: trunk files are read with `git show`.
   Clock: date -u against the Date header of a raw.githubusercontent.com response: skew −1..0 s.
2. Open work. Inherited from successor 37 (HANDOVER f2793d9a): none («Open items: NONE»). Routed by the Lead's brief, after «go», in
   order (a Lead message with a SHA for an item preempts; I finish and commit the section I am on first):
   A. BYTE TEST of P-N5-GATE fixes entry 5 + line L-5 (for R128). Waiting for the L-SI SHA from the Lead. Background measured now:
      CHECKER C142 (claude/checker 269effb3, docs/checker/C142.md) FAILED the first fill with E-1..E-3 in the line; trunk RESULTS at
      68c8d293 has «### R125», «### R126», «### R127» and no R128. Next step, on the SHA: re-hash fixes and L-5 from `git show`;
      word-level diff L-4 (sha1 6bfde78e, 12,562 B, signed MATCHES in R2-P-N5-GATE Add. 3 / Add. 4) → L-5; rebuild L-5 from L-4
      plus the old → new pairs of entry 5 with my own script (bt_l3.py pattern) and cmp, also against CHECKER's L-5 (sha1 7ebcf735…,
      12,923 B); test bytes and meaning of E-1 (GL-3 RA-MULT / RA-path rows get numbers and source: L-SI 47 box 90, 2d0344d3 /
      4ded1e8d, maxm 8 / 32, maxP 54 / 2583; I read mw90.out / fw90.out myself), E-2 (the «growth» clause gets numbers on named
      instances: C 17 / 65, maxflip 34 / 130 on MW8_2 / MW32_2, MWR flips 9 / 17 / 33; A*_all dropped: box 91's maxa 33 is not
      A*_all, my predecessor's Add. 4 had A*_all 66), E-3 (seven marker insertions in E-FACE-PAYS (b)-(d) and GATE-LOW-NULL (a),
      (b′), packet §3.2, §3.4, no word changes). Re-sign or refuse with exact old / new strings as Addendum 5 to
      docs/referee-2/R2-P-N5-GATE.md. REFEREE 33 byte-tests the same independently; I do not read its test before mine is pushed.
   B. Full independent SECOND review of packet P-N5-LEVEL (box 208 + Addenda A, B, frozen by L-NEW 73). Waiting for the freeze SHA
      from the Lead. I do NOT read docs/referee/ on P-N5-LEVEL or box 208 (incl. R-box208-preread.md) before my own verdict is pushed.
      Next step, on the SHA: hash-check the frozen inputs; re-derive every proof; premises by script against landed RESULTS on trunk;
      own replay on my own engines with firing controls (each control shown to fire); DATA rule (L43; every DATA clause names its
      counter); TARGET.md diff; scope (Howard ALL-SWITCH, MAXIMISER improves, IDEAL-CYC on R104 genomes only; not N5, not M4);
      name every genome-only step; Lean theorems of L-FORMAL cited only as «Lean-checked (lane)» with name and commit; verdicts
      SIGN / SIGN WITH GAP / REFUSED with exact strings. Report docs/referee-2/R2-P-N5-LEVEL.md, committed section by section.
      I park with a handover at ~480k context, before starting a full review I cannot finish.
3. GAPS rows: none owned by REFEREE-2 (owner column of docs/GAPS.md, on my branch and on trunk 68c8d293, has no REFEREE-2 entry).
4. Rulings (status from docs/DECISIONS-INDEX.md at trunk 68c8d293; text verbatim from docs/DECISIONS.md lines 7, 8, 333, 452 there):
   - D1 (active): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's
     own, as wrong until it passes the gauntlet below.» and «Never downgrade the referee to save money.»
   - D18 (active): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of
     mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them
     briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
   - D21 (active), first sentence of the relayed text: «Okay, I want maximum effort.» (full text: docs/DECISIONS.md#d21). Lead
     reading L51 (active): maximum effort until 2026-11-14 10:05Z; a «rejected» limit still pauses. If my turn fails on a limit, I
     resume from notes/REFEREE-2.md when woken.
5. Trap: a container that starts shallow, detached or with a stale local claude/referee-2 (here shallow and 884 behind; earlier 171,
   157, 145) makes push.sh fail («invalid refspec») or push the wrong head. Check, run before anything else: fetch --unshallow + fetch
   + checkout + merge --ff-only, then `git branch --show-current` = claude/referee-2 and HEAD = origin/claude/referee-2 before any
   commit. Second trap: push.sh pushes only the commit it verified, and verify now takes 40-70 min; so pgrep -f "bash scripts/push.sh"
   first, run the push as a tracked background task with a 2-hour timeout (output to a file, then echo exit $?; no pipe, no &), and
   never commit while it runs (batch commits). Third trap (L43): a DEAD of an asymptotic statement on finitely many instances is
   DATA with numbers and source commit, not DEAD.
