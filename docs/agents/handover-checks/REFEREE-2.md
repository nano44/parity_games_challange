# REFEREE-2 handover check (successor 37, Opus 5.5 under D1/D18/D20; 2026-11-11 23:15Z by date -u)
1. Branch claude/referee-2. At start: fetch --unshallow + fetch + checkout + ff-only (local ref was 171 behind origin; fast-forwarded);
   `git branch --show-current` = claude/referee-2, HEAD = origin/claude/referee-2 = 50408dc8. vs trunk claude/vibrant-johnson-nxvvxo
   86f62c26: 16 ahead / 248 behind (merge-base 63a3cf87). No trunk merge made (not needed for my items).
2. Open work, after «go», in order (a byte-test SHA from the Lead preempts: finish and commit the current section first):
   A. Byte test of P-N5-SPLIT fixes entry 2 + line L-1 (L-NEW 69 writing; SHA from the Lead, not yet sent) against R-1..R-6 of
      docs/referee-2/R2-P-N5-SPLIT.md (991296c9 final, c708c968 Add. 1): R-1 (LEX-Λ) only on non-core vertices (pads), never the false
      «a play passes K0 iff it passes K3 iff its cycle node is in the closed core»; R-2 «CONDITIONAL on RESULTS R125 (P-N5-CHAIN)»;
      R-3 [E-LEV] on ASC-WIT / ASC-ROOT only; R-4 SPLIT-COUNT a reduction, «G-N5-TIME stays OPEN»; R-5 DATA rule (units, conditions,
      constants; split199.py); R-6 = REFEREE's SP-2 citation form. Bytes and meaning → R2-P-N5-SPLIT.md Addendum 2. Waiting for SHA.
   B. Full independent second review of P-N5-GATE (L-SI): claude/l-si FROZEN 4066f579, docs/si/P-N5-GATE.md sha1 f3a584e6… (25,604 B);
      fixes 1-2 at 9c0349b1 (entry 1 = L-RED 63 G1-G6; entry 2 IDEAL-CYC PROVISO, premise R123 B-ONLY); line L-2 (sha1 c0f2007d…,
      10,295 B). Next step: hash-check the frozen inputs, re-derive every statement's proof, premises by script (r2q.py pattern), Γ3 vs
      IDEAL-CYC scope, own replay with firing controls, DATA rule on L-2, TARGET.md diff, verdicts with exact old/new strings.
      Report docs/referee-2/R2-P-N5-GATE.md section by section; docs/referee/R-P-N5-GATE.md (REFEREE 31) read only after my verdict.
   C. Then the second review of P-N5-BONLY3 (claude/l-si FROZEN 681bfccf, sha1 a6baa60b…, 13,288 B) when the Lead routes it.
3. GAPS rows: none owned by REFEREE-2 (docs/GAPS.md owner column has no REFEREE-2 entry).
4. Rulings (DECISIONS-INDEX status; text verbatim from docs/DECISIONS.md lines 7, 8, 333):
   - D1 (active): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's
     own, as wrong until it passes the gauntlet below.»
   - D1 (active): «Never downgrade the referee to save money.»
   - D18 (active): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of
     mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them
     briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
   (D20, active, sets pace: «We have reset the weekly usage, so we can again work faster no?»)
5. Trap: a container starting with a stale local claude/referee-2 (here 171 behind; earlier 157, 145) makes push.sh fail or push the
   wrong head. Check: fetch --unshallow + fetch + checkout + merge --ff-only, then `git branch --show-current` = claude/referee-2 and
   HEAD = origin/claude/referee-2 before any commit. Second trap (predecessor): a single-process sweep buffers all output and dies in
   a fleet stall; run one process per chunk with a TOTAL-line checkpoint.
