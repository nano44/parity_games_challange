# R2-NOTE-E3: REFEREE-2 sign-off on the draft RESULTS Note E-3 (R110's CONDITIONAL DEAD SC-ISO, its premise now RESULTS R112)
REFEREE-2 successor 28 (Opus 5.5, D12/D20). Written 2026-11-06 12:13Z (date -u). Asked by the Lead 11:45Z (its stamp).

## Object
- Trunk claude/vibrant-johnson-nxvvxo 82a5f384: docs/agents/R110-note-E3-draft.md sha1 4a64b0d5085586dff9366de93dafa7de7a5d52a2,
  147 lines (note block l. 74-105). docs/RESULTS.md at 82a5f384: sha1 70407ce7…, 12,730 lines, which is the RESULTS the draft measured
  (R110 l. 11323, R112 l. 11909, Erratum E-2 l. 12165, «## Dead ends» l. 12193). Re-hashed: match.

## Verdict: **SIGN, with one required word change (E3-W1)** (Opus 5.5, D12)
- Ruling on my predecessor's «RESULTS must keep that wording. The item must not be cited as an unconditional DEAD.» (REFEREE-2 27,
  R2-P-IDEAL-FLIP.md l. 85): that ruling bound the label while G-FLIP-1 was open, i.e. while the premise was a single-encoding,
  unrefereed, unlanded SAT result (l. 82). The same report named what closes it (l. 86-88): (a) an independent encoding over all of
  𝓛^R_3, every start, ISO or not, and (b) a referee check of that encoding against R104. Both are now met and landed as RESULTS R112:
  L-COMP's cnf.py; encoding audit R2-T3R-audit.md; my R2-P-TR3.md with Add. 1-2; the other referee's report; CHECKER C123.
  - So yes: a landed R112 changes the ruling. The DEAD may be cited as DEAD, carrying R112's machine trust base.
  - The first half of the old ruling still holds and the note respects it: R110's wording (heading, GAPS UPDATE) stays as landed, and
    only its reading changes through a separately landed item, as R110's Honest limits (iii) allow.
- The logic (checked): R110 (g) signs «SC-ISO at d = 4 ⇒ T^R(3) ≥ 9» unconditionally (the instance iso_d4_st9: 6 + 3 = 9 steps outside
  the moves of 0 and 1, which my predecessor recomputed with their own simulator). R112 gives T^R(3) ≤ 8 for the SAME T^R(3) (below). So
  SC-ISO fails at d = 4, hence the lane conjecture «for every d ≥ 3 …» is false. ✓
- Definition diff, done by me on RESULTS at 82a5f384 (not by reading the draft's diffE3.out):
  - R110's definition text (from «𝓦_d the genomes …» to «… T^R(d) ≤ T*(d))», inside R110's «on acyclic Ξ-graphs, with …») occurs
    verbatim in R112's body, together with the frame «on acyclic Ξ-graphs, with» (Python substring test: True).
  - R112's title cites «RESULTS R110's definitions of 𝓛^R_d and T^R(d) only»; d = 3 (levels 0, 1, 2); «all acyclic Ξ-data, β's,
    gates and starts, ISO not assumed»; «T^R(d) the largest number of steps over 𝓛^R_d and all starts».
  - R110's SC-ISO quote ends «… is at most T^R(d − 1)» with the same symbol, defined over ALL of 𝓛^R_(d−1): not ISO-only (SC-ISO's ISO
    restriction is on the d-level genome only). R112 does not assume ISO, so it bounds exactly that quantity.
  - The draft's 12 aspects (model, definition by citation, T^R text, d, levels, acyclicity, wiring, starts, ISO, steps = R104's L(G),
    SC-ISO's symbol, premise = R112's first clause): I find each equal. The gloss differences the draft lists (𝓦_d omitted, «W-convention»,
    «all acyclic Ξ-data», the T*(d) remark) abbreviate the text; none changes the class or the quantity. ✓
- Quotes: all 17 outermost guillemet quotes of the note block are verbatim (wrap-normalised substring test) in RESULTS at 82a5f384 or in
  R2-P-IDEAL-FLIP.md at dc622d03, with «…» splits; 0 not found. ✓
- Other claims of the block: «the heading equals the MATCHED line L-3» is my predecessor's L-3 byte test (8fde383f). «xcnf.py not used»
  is right: the premise is discharged by R112's statement, not by an encoding. «No GAPS line or Dead-ends row» follows the E-2 and C118
  §5 precedents. ✓

## Required word change
- E3-W1 (the citation form, so that the old ruling's concern stays met): in «What it rests on», replace «The DEAD is unconditional within
  RESULTS and exactly as strong as R112.» by «The DEAD needs no premise outside RESULTS and is exactly as strong as R112's machine
  statement; it is cited as «DEAD (with RESULTS R112's machine trust base)», not as a hand-proved DEAD.»
  - Why: «unconditional» on its own is the word my predecessor ruled out. The DEAD is now free of any premise outside RESULTS, but it is
    not a hand proof. The citation should carry that every time, not only in this note.
- Optional: F-2's label «Note E-3» is fine (nothing in R110 is wrong, so «Erratum» would mislabel it).

## Sign-off line for the block
- «REFEREE-2 <referee-2>» may be filled with this file's push commit. My statement for it: R110 (g)'s implication together with RESULTS
  R112 gives the DEAD, and R112's T^R(3) is R110's.
