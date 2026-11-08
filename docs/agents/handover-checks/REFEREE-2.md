# REFEREE-2 handover check (successor 33, Opus 5.5 under D1/D18/D20; 2026-11-08 04:58Z by date -u)
1. Branch claude/referee-2. At start: fetch --unshallow + fetch + checkout + ff-only (local ref was 134 behind; fast-forwarded);
   `git branch --show-current` = claude/referee-2, HEAD = origin/claude/referee-2 = 98b9622b. vs trunk claude/vibrant-johnson-nxvvxo
   4aaba7d5: 3 ahead / 40 behind (merge-base 6c937bc6). No trunk merge made (not needed for my items).
2. Open work, after «go», in order:
   A. Byte test gating R121: P-N5-ASC line L-4 = L-3 (0012d671 at claude/l-new a2512364; successor 32's Add. 4: MATCHES) + REFEREE 28's
      R5 (docs/referee/R-P-N5-ASC.md §E, claude/referee 013f821b): old «(Lemma CHAIN-DECOMP) if the first e-vertex on v's play is f,
      then» -> new «(Lemma CHAIN-DECOMP) if seq_t(v) = (f, …), i.e. the first e-vertex on v's play is f and f ∈ Π_t(v), then».
      Predicted sha1 4017305a…, 5,198 B. Waiting for the L-4 SHA from the Lead. Next step: script L-3 + R5 (old once in L-3, new once
      in L-4, nothing else changed), hash, read R5's meaning against packet l. 80; write Addendum 5 to docs/referee-2/R2-P-N5-ASC.md.
   B. Full independent second review of P-N5-QUIET (L-NEW 62/63): claude/l-new frozen 9329859d, docs/new/P-N5-QUIET.md sha1 066dfc7d…
      20,022 B; fixes entry 1 d9c49489; L-1 df0d2a25 (sha1 62de9075…, 4,600 B); pins experiments/new/box194/quiet.pins. Next step:
      re-hash, re-derive LOC-GATE, CN2, LOC-K2, QUIET + T-QUIET (layered Bellman-Ford window bound; tie case vs NO-TIE), UP-T
      (under [E-LEV]), ASC-T, B-ONLY, NO-TIE; premise quotes by script ([OPT] source for pointwise optimality of σ̄_t); Γ3 scope for
      N5′-xi; own-engine DATA replay; DATA rule per clause of L-1; TARGET.md diff. Report docs/referee-2/R2-P-N5-QUIET.md;
      docs/referee/R-P-N5-QUIET.md read only after my verdict is on origin. L-RED R221 is context, not a signature.
3. GAPS rows owned by REFEREE-2: none. docs/GAPS.md names REFEREE-2 only in notes of closed rows (G-Bthr, G-K5, G-DOM); G-N5-TIME owner
   is «L-NEW (L-LIT T22; referees later)», open.
4. D1 (active, DECISIONS-INDEX row D1; DECISIONS.md l. 7-8): «A claimed polynomial algorithm is far more likely to be wrong than right.
   Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.» «Never downgrade the referee to save
   money.»
   D18 (active; DECISIONS.md l. 333): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from
   areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them
   briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
   D20 (active; DECISIONS.md l. 423): «We have reset the weekly usage, so we can again work faster no?» (Lead reading L48 active).
5. Trap: a DATA clause can be weaker than its words in two places, the counter's condition (P-N5-ASC upfail) and the cited tool
   (P-ACYC L-2 cited pacyc81.py for a τ test only fix1/pacyc81t.py makes). Check: for every DATA clause read the counter's condition line
   by line against the lemma AND confirm the cited script is the one that computes it, on a git archive of the frozen SHA.
   Also (this start): stale local branch 134 behind; the fetch/checkout/ff-only sequence plus `git branch --show-current` before push.
