# REFEREE-2 handover check (successor 32, Opus 5.5 under D1/D18/D20; 2026-11-08 00:15Z by date -u)
1. Branch claude/referee-2. At start: fetch --unshallow + checkout + ff-only; `git branch --show-current` = claude/referee-2, HEAD =
   origin/claude/referee-2 = fcdc16b4 (no stale ref this time). vs trunk claude/vibrant-johnson-nxvvxo 37a4855e: 3 ahead / 126 behind
   (merge-base e72661d0). Merged trunk with a merge commit (no rebase) -> 6146131a, 4 ahead / 0 behind before this commit.
2. Open work, after «go», in order:
   A. P-N5-ASC byte test (predecessor's Add. 2 at fcdc16b4: fixes entry 1 CORRECT, L-1 NOT YET on W-3 and W-4). Waiting for L-NEW 62's
      fixes entry 2 + line L-2 SHA from the Lead. Next step: test W-3's new E-MON unit string occurs once and the old not at all; test
      W-4 (strict condition «lev(nxt[z]) > lev(z's mover)» added to upfail and check193.sh re-run on a git archive, or the clause
      re-worded); DATA rule clause by clause on L-2; Addendum 3 to docs/referee-2/R2-P-N5-ASC.md (MATCHES / does not match).
   B. Full independent second review of P-ACYC (L-SI 43), frozen claude/l-si e3ac4b06; docs/si/P-ACYC.md sha1 0e9edcfd… 16,852 B (not
      6b699f93 as the lane's message said), line L-1 docs/si/P-ACYC-line-L1.txt sha1 bb12deec… 2,085 B; pins box81/pacyc.sha1, check
      box81/check81.sh. Next step: re-hash at e3ac4b06; re-derive BETA-ACYC (Γ and Γ3), LAMBDA-CONST, ACYC-LIN, ACYC-XI (conditional on
      R118 (k)+(l)); FIRST FALLBACK vs SPEC S4/S4c; premise quotes by script; §5 scope; own simulator replay of §6 DATA; DATA rule per
      clause of L-1; TARGET.md diff. Report docs/referee-2/R2-P-ACYC.md; docs/referee/ read only after my verdict is on origin.
3. GAPS rows owned by REFEREE-2: none. docs/GAPS.md names REFEREE-2 only in notes of closed rows (G-Bthr, G-K5, G-DOM); G-N5-TIME owner
   is «L-NEW (L-LIT T22; referees later)», open.
4. D1 (active, DECISIONS-INDEX row D1; DECISIONS.md l. 7-8): «A claimed polynomial algorithm is far more likely to be wrong than right.
   Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.» «Never downgrade the referee to save
   money.»
   D18 (active; DECISIONS.md l. 333): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from
   areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them
   briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
   D20 (active; DECISIONS.md l. 423): «We have reset the weekly usage, so we can again work faster no?» (Lead reading L48 active).
5. Trap: a lane's DATA counter that tests a weaker property than its clause (P-N5-ASC upfail: successor 31's round-1 miss, caught in
   Add. 2 as W-4). Check: read every counter's condition line by line against the lemma (and its loop set, for unit words such as
   tmonunits including c_W) before calling a DATA clause OK. Standing trap too: SHAs typed into a Lead message before reading git output;
   check = commit, read `git rev-parse HEAD`, message in a LATER step.
