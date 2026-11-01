# P-N5-S4B fixes (append-only; the frozen packet docs/si/P-N5-S4B-box63.md, sha1 f1b65da522d927406a403ae5d023bb48ac73d022, is never edited)
L-SI successor 38. Started 2026-11-01 from 04:1xZ (date -u; see commit), after the Lead's 04:13Z message.

## F0. Status of the packet
- Both referees SIGNED Lemma S4B-OPT and Corollary S4B-KEEP with no gap:
  - REFEREE 22, docs/referee/R-N5-S4B.md (claude/referee 062cd7345): «| 2 | Lemma S4B-OPT | **SIGNED** (precision S4B-P1) |», «| 3 |
    Corollary S4B-KEEP | **SIGNED** (precision S4B-P2) |», «| 5 | RESULTS line | **REQUIRED S4B-L1** (attribution of the quantified
    1E-N3 form) and **S4B-L2** (DATA counts include 319 repeated list lines; §5) |».
  - REFEREE-2 25, docs/referee-2/R2-N5-S4B.md (claude/referee-2 1b9ef2e10): «| §2 | Lemma S4B-OPT … | **SIGNED** |», «| §3 | Corollary
    S4B-KEEP … | **SIGNED** |», «No gap. The premise is 1E-N3 alone, read as in §2 below.»
- The Lead reports Lead reading L45 (docs/DECISIONS.md, being pushed by the Lead at the time of writing): L42's S4b restriction is lifted.
- Changes: the RESULTS line only (line L-1, entries 1-2). Entries 3-5 record the optional precisions. The packet's §4 counts are
  superseded by entry 2.

## 1. S4B-L1 (REFEREE, REQUIRED): attribution of the quantified 1E-N3 form
- REFEREE §5, quoted: «The line writes "under the standing SPEC premise of RESULTS R57 (1E-N3: for every finite game graph G* …"».
  That is a quantified form R57 does not state … Fix: cite R57 (b)'s words ("that S1's procedure realises an optimal σ̄ is VJ00 §6 plus
  SPEC conformance"), and introduce the G*-form with the Lead reading that lifts L42».
- Fix (line L-1):
  - The premise clause now quotes R57 (b) verbatim from docs/RESULTS.md l. 2915-2916: «that S1's procedure realises an optimal σ̄ is
    VJ00 §6 plus SPEC conformance».
  - The G*-form follows it as «read on every game input of S1's procedure (Lead reading L45, lifting L42's S4b restriction)».
  - The N-1E-1 quote is kept, now as the setting of VJ00 and of S1 rather than as REFEREE-2's signed scope of R57.

## 2. S4B-L2 (REFEREE, REQUIRED): the DATA counts include repeated list lines
- REFEREE §5, quoted: «The list has 1,132 LINES, 813 distinct (319 exact repeats, 719 distinct games). The counts sum the repeats. …
  Fix: either de-duplicate and give the distinct counts (lane file: 5,726 states, 5,058 enumerated, 668 not, 213,311 strategies, 29 Odd
  fallbacks), or say "1,132 list lines (813 distinct …), counted with repeats". The same change applies to the packet's §4.»
- Re-derived from my own file, experiments/si/anc58/s4bopt_corpus.txt, keeping the first occurrence of each distinct argument line
  (check.sh «P-N5-S4B L-1» recomputes it):
  - 813 distinct game/start lines (719 distinct games);
  - 5,726 states with I_τ ≠ ∅; 5,058 enumerated, 668 not enumerated (more than 1,024 arena strategies);
  - 213,311 strategies compared, OPTV 0;
  - τ_(k+1) = τ_new at 5,697 states, and the other 29 are the Odd fallbacks;
  - S4a control: 11,326 states enumerated, S4AV 0.
  - These agree with REFEREE's figures.
- Fix (line L-1): the DATA clause states the distinct counts and says how the list was counted.
- The packet's §4 now reads (superseding its 7,772 / 6,719 / 1,053 / 290,345 / 36 / 16,430, which summed the repeats): the figures
  just above. The mutation-control figures (lcount2_n23 215, sym_h8_s1 677) are per instance and unaffected.

## 3. S4B-P1 (REFEREE, optional)
- Quoted: «the proof's (iv) cites S4c, S4d and FIX 3, and (iii) cites S1's value definition. These are SPEC text, not premises. "under
  1E-N3 alone" means "no premise other than 1E-N3", which is accurate.»
- Accepted. The packet's §1 lists S4b / S4c / S4d / FIX 3 under «premises (landed labels only)». Read them as SPEC text. The only premise
  is 1E-N3. The line now writes «(SPEC text S4c, S4d, FIX 3)».

## 4. S4B-P2 (REFEREE, optional)
- Quoted: «cite SPEC S2 ("w ≠ σ(v)", the same on G^d for τ) for "w ≠ τ_k(v)"».
- Accepted. In the proof of Corollary S4B-KEEP (packet §3), «an improving w ≠ τ_k(v)» rests on SPEC S2's «w ≠ σ(v)», read on G^d for τ.
  No line change: the line does not restate that step.

## 5. P-1 (REFEREE-2, optional)
- Quoted: «N-1E-1 was written about G. The step "the procedure's requirement is likewise scoped to every finite game graph, including
  arenas H′_k" is the reading confirmed here, not a sentence of N-1E-1. … would be exact if it added "and confirmed for arena inputs in
  docs/referee-2/R2-N5-S4B.md §2"».
- Accepted. Line L-1 adds «confirmed for arena inputs in docs/referee-2/R2-N5-S4B.md §2».

## Line L-1
- docs/si/P-N5-S4B-line-L1.txt (one line, no heading marker), replacing docs/si/P-N5-S4B-line.txt (f8559b5e). Its sha1 and the full
  word-diff go to the Lead.
