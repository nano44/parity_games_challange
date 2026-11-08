# REFEREE-2 handover check (successor 34, Opus 5.5 under D1/D18/D20; 2026-11-08 08:38Z by date -u)
1. Branch claude/referee-2. At start: fetch --unshallow + fetch + checkout + ff-only (local ref was 142 behind; fast-forwarded);
   `git branch --show-current` = claude/referee-2, HEAD = origin/claude/referee-2 = f699a724. vs trunk claude/vibrant-johnson-nxvvxo
   a1decf9a: 11 ahead / 47 behind (merge-base 6c937bc6). No trunk merge made (not needed for my items).
2. Open work, after «go», in order:
   A. Full independent second review of P-N5-END (L-NEW 63/64): claude/l-new frozen 131b4c1c, docs/new/P-N5-END.md sha1 5cae845b…,
      22,967 B; pins experiments/new/box195/end.pins; check.sh blocks «P-N5-END», «BOX 195 END»; fixes entries 1 (a60733b8) and 2
      (2fcee038) in docs/new/P-N5-END-fixes.md; line L-2 at 2fcee038 (docs/new/P-N5-END-line-L2.txt, sha1 e8a8ac51…, 6,988 B; L-1
      superseded). Statements E0, E1, E2-E4, TERM-XI, ENDGAME-3, ENDGAME-3-N5, EXACT-L, END-T3. Next step: re-hash all of it on a git
      archive; re-derive every proof; premise quotes by script ([OPT] = [1E-N3] for SPEC runs); own-engine DATA replay; DATA rule per
      clause of L-2 (counter condition AND cited tool); TARGET.md diff. Report docs/referee-2/R2-P-N5-END.md; docs/referee/R-P-N5-END.md
      read only after my verdict is committed. L-RED 58 R223-end.md is context, not a signature.
   B. Later: second review of P-N5-CHAIN (box 196: REACH3-ALL, Γ3 forms of QUIET / ASC, Theorem CHAIN3) when the Lead sends the SHA.
3. GAPS rows owned by REFEREE-2: none. docs/GAPS.md (trunk a1decf9a) names REFEREE-2 only in notes of closed rows (G-Bthr, G-K5, G-DOM);
   G-N5-TIME owner is «L-NEW (L-LIT T22; referees later)», open.
4. D1 (active, DECISIONS-INDEX row D1; DECISIONS.md l. 7-8): «A claimed polynomial algorithm is far more likely to be wrong than right.
   Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.» «Never downgrade the referee to save
   money.»
   D18 (active; DECISIONS.md l. 333): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from
   areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them
   briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
   D20 (active; DECISIONS.md l. 423): «We have reset the weekly usage, so we can again work faster no?» (Lead reading L48 active).
5. Trap: the DATA rule bit again in P-N5-QUIET: a tool's constants and loop units can make a clause weaker than its words
   (quiet194.py's L carried «+ 1» and counted steps; k2fail tested one conjunct). Check: for every DATA clause read the counter's
   condition, constants and loop units against the lemma AND confirm the cited script computes it, on a git archive of the frozen SHA.
   Also (this start): stale local branch 142 behind; the fetch/checkout/ff-only sequence plus `git branch --show-current` before push.
