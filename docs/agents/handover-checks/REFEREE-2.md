# REFEREE-2 handover check (successor 35, Opus 5.5 under D1/D18/D20; 2026-11-08 09:51Z by date -u)
1. Branch claude/referee-2. At start: fetch --unshallow + fetch + checkout + ff-only (local ref was 145 behind; fast-forwarded);
   `git branch --show-current` = claude/referee-2, HEAD = origin/claude/referee-2 = 0f82f03b. vs trunk claude/vibrant-johnson-nxvvxo
   3906d411: 14 ahead / 49 behind (merge-base 6c937bc6). No trunk merge made (not needed for my items).
2. Open work, after «go», in order (B first when its SHA arrives, it gates P-N5-END's landing):
   B. Byte test of P-N5-END line L-3 (= L-2 e8a8ac51 at 2fcee038 + required L-R1, + optional N-1 / N-2 and REFEREE 29's EL-1 / EL-2):
      when the Lead sends the SHA, check each old string once in L-2, each new string once in L-3, nothing else changed; write
      R2-P-N5-END.md Addendum 2. Waiting for the SHA.
   A. Full independent second review of P-N5-CHAIN (L-NEW 64): claude/l-new FROZEN 93531b03, docs/new/P-N5-CHAIN.md sha1 6e613ba7…,
      38,551 B; L-1 at 71b75424 (docs/new/P-N5-CHAIN-line-L1.txt, sha1 bd152dd9…, 8,124 B); L-2 (fixes entry 1, REFEREE 29's CL-1)
      byte-tested when sent; fixes docs/new/P-N5-CHAIN-fixes.md; pins chain.pins; check.sh block «P-N5-CHAIN». Statements ESC3-ALL,
      W3-ALL, REACH3-ALL; F1/F3/F4′/F5/F6/DOM/STRICT on HOW3; CN2-3, LOC-GATE3, LOC-K2-3, B-ONLY3, NO-TIE3; QUIET3, T-QUIET3; E-MON3,
      CHAIN-DECOMP3, HUB-ASC-G3, UP-JUMP3, UP-B3 ([E-LEV]); Theorem CHAIN3 ([E-LEV], conditional on P-N5-END and P-N5-ASC §4); DEAD
      RUN-TRANSFER. Next step: re-hash on a git archive of 93531b03; re-derive every proof; premise quotes by script (r2q.py adapted);
      own-engine replay (r2end.py / r2quiet.py); DATA rule clause by clause on the line; TARGET.md diff. Report
      docs/referee-2/R2-P-N5-CHAIN.md; docs/referee/R-P-N5-CHAIN.md read only after my verdict is committed. L-RED 58 R223-reach.md,
      R223-q2.md, R224-chain.md are context, not signatures. Not started.
3. GAPS rows owned by REFEREE-2: none. docs/GAPS.md (trunk 3906d411) open rows: GAP-A, GAP-C, G-S5-6, G-NEST, G-N1-LB, G-N5-TIME (owner
   «L-NEW (L-LIT T22; referees later)», open); REFEREE-2 appears only in notes of closed rows.
4. D1 (active, DECISIONS-INDEX row D1; DECISIONS.md l. 7-8): «A claimed polynomial algorithm is far more likely to be wrong than right.
   Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.» «Never downgrade the referee to save
   money.»
   D18 (active; DECISIONS.md l. 333): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from
   areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them
   briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
   D20 (active; DECISIONS.md l. 423): «We have reset the weekly usage, so we can again work faster no?» (Lead reading L48 active).
5. Trap: a line sentence true in the proof's local reading and false on its own (P-N5-END E1's «changes only at a fallback», fixed by
   L-R1). Check: read every line clause as a stand-alone RESULTS claim, and for every DATA clause read the counter's condition,
   constants and loop units against the lemma on a git archive of the frozen SHA. Also (this start, again): stale local branch 145
   behind; fetch/checkout/ff-only plus `git branch --show-current` before every push.
