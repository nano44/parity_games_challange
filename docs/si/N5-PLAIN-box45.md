# N5-PLAIN (box 45): the plain-wave lemma is DEAD in transition form (runfam_K40); REP-PLAIN is DEAD on latew_K20_m32
L-SI successor 31 (Opus 5.5), D15 / D18, Lead reading L40. Lead 2026-10-30 01:11Z: «Before the plain-wave lemma: falsify it cheaply on
L-RED's latew family … If "plain-driven W-changes ≤ n−1 per W-run" fails there, it is dead; record it with the instance and do not try to
prove it. If it survives, say why … In either case state REP-PLAIN's status on latew too.» Working note, unrefereed. G-N5-TIME OPEN.
- Tool: experiments/si/odd/repchain.py (box 44) + counters PLAINW (most W-changing transitions with no late adoption at that transition, in
  one W-run) and PLAINV (most W-changes of one vertex at such transitions, in one W-run). Corpus output odd/out/repchain_corpus.txt
  (re-run, 719 games). Instance copied read-only from origin/claude/l-red (l-red e55592d9 tree): odd/inst/red/latew_K20_m32.pg sha1
  063d173c2de7, .start f6ac65607e4d. (latew_K24_m40 is not on l-red's tree; not run.)

## 1. DATA
| instance | n | late | REP | REP parents (REPEAT / FIRST / plain) | depth | PLAINW | PLAINV |
| --- | --- | --- | --- | --- | --- | --- | --- |
| latew_K20_m32 (L-RED, with .start) | 538 | 641 | 570 | 0 / 570 / 0 | 1 | 60 | 39 |
| runfam_K40 (si/runlin, sha1 287a185d6b82) | 79 | 19 | 1 | 0 / 0 / 1 | 1 | 151 | 5 |
| runfam_K10 (sha1 faf218f125d1) | 49 | 19 | 1 | 0 / 0 / 1 | 1 | 85 | 5 |
| corpus (719 games) | | 1,141 | 41 | 0 / 0 / 41 | 1 | max 151 (runfam_K40) | max / n 0.33 (x31_cu24, 8 at n 24) |

## 2. Verdicts
- DEAD: the plain-wave lemma in transition form, "W-changing transitions with no late adoption ≤ n − 1 per W-run". Kill:
  si/runlin/instances/runfam_K40.pg (S3 start), one W-run with 151 such transitions > n − 1 = 78 (runfam_K10: 85 > 48). It survives on
  latew_K20_m32 (60 ≤ 537), so latew is not the kill; the corpus is. Obstruction (READING): GP*'s n − 1 is per wave, and the plain
  switches of one W-run can form many waves, each started by a FIRST late adoption elsewhere (runfam: 19 late adoptions, 1 repeat).
- Per-vertex form "PLAINV ≤ n − 1" survives (≤ 0.33n on the corpus; 39 at n 538 on latew). CONJECTURE only; it does not bound REP,
  because REP per edge is charged to all W-changes of z, including those at late-adoption transitions.
- DEAD on latew_K20_m32: CONJECTURE REP-PLAIN (box 44). All 570 REPEATs there have a FIRST late adoption as the parent of the last
  W-rise of their target (h's K pivot rises are late adoptions, as the Lead guessed). Chain depth is still 1: the parents are FIRST, not
  REPEAT. REP 570 > n = 538 in that game (L-RED R128 owns the REP-LIN verdict; my count is per game, its is per W-run).
- So depth stays 1 everywhere measured, while breadth (one FIRST adoption re-enabling many edges) is what grows. This agrees with L-RED
  R127's reading «depth ADDS along a reader chain; it amplifies only via breadth».

## 3. Composition toward G-N5-TIME
- [P-REP] (P-N5-CUT) stays OPEN. The two candidate routes to it from boxes 44-45 are DEAD: REP-PLAIN (latew), plain-wave transition form
  (runfam_K40). The live structure is depth 1 + breadth: a bound would need "each FIRST late adoption re-enables ≤ p(n) repeats", which
  latew already pushes to Θ(n) per adoption (570 / ~K).

## DONE / FINDINGS / NEEDS
- DONE: repchain.py counters; latew pin copied; corpus re-run; si/check.sh «box 45»; this note.
- FINDINGS: 1. DEAD plain-wave lemma (transition form), runfam_K40 151 > 78. 2. DEAD REP-PLAIN, latew_K20_m32 570 / 570 FIRST parents.
  3. DATA depth 1 everywhere; per-vertex plain form survives (CONJECTURE, not useful for REP).
- NEEDS: none from the owner.
