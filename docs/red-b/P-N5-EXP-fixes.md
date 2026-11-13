# P-N5-EXP fixes (append-only; the packet docs/red-b/P-N5-EXP.md is never edited after its freeze commit 350d84eb)
L-RED-B successor 5 (session_01V5yGRXFf3kFNfkycCHTnLT). Each entry says what it adds and whether any statement, proof or hypothesis
of the packet changes. Entries carry DATA and answers; a change to a statement or a proof would be an entry of its own, marked so.

## Entry 1 (2026-11-13, drafted 13:0xZ, completed 14:03Z by date -u): extra DATA, no change to any statement, proof or hypothesis
This entry adds six DATA subsections (9.8-9.13) to the packet's §9, one pointer correction and one reproduction erratum (10.E). Nothing in §1-§8, §10, §11
changes; the packet's text is untouched (sha1 c0449b17193f19619f33b366096762dfde27d542 at 350d84eb). The frozen data files
of data/b6b/ are untouched too (SHA1SUMS_b6b is byte-identical); the files this entry adds are pinned in
data/b6b/SHA1SUMS_b6b_fixes1 (checked by experiments/red-b/check.sh).
Pointer correction (no content change): the packet's §9 header says the files are «pinned in data/SHA1SUMS»; the pin file is
experiments/red-b/data/b6b/SHA1SUMS_b6b.

### 9.8 The enabling predicates against the model itself (experiments/red-b/b6enab.py → data/b6b/out/enab.out, enab_ctrl.out)
The packet proves the run from V4 (value-enabling) and K4 (key-enabling), which it derives from MOVE-2 and the static facts. This
check compares those two predicates, computed from the rule's table (the quantities C, E, EY, EY′, D, Z), with what the simulator
computes from R104's definition, at every state and every mover of the real run:
- must-0 counter `venab`, unit (state, mover), set = every state of the key run of G_k and every mover: «x is value-enabled under
  s_t» (V4) differs from |A_(s_t)(x)| = 2 (R104's availability);
- must-0 counter `kenab`, unit (step, mover): «x is key-enabled in the step s_t → s_(t+1)» (K4, read at x's current option with the
  new state below it) differs from «the key of x's other option is the smaller», both keys with s_(t+1) on the lower levels
  (MOVE-2 (b));
- must-0 counter `movd`, unit (step, mover): (value-enabled under s_t) ∧ (key-enabled in the step) differs from «x moves at that
  step».
Result (enab.out), k = 3..12: venab 0, kenab 0, movd 0 on all of them (states 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095).
Controls (enab_ctrl.out): B6E_CTRL=1 (V2's two cases exchanged) → venab 540 and movd 230 on G_6; B6E_CTRL=2 (D_j's two disjuncts
exchanged) → kenab 392 on G_6. Both fire.
Honest notes on this check (they concern the check, not the packet): (1) the first version of b6enab.py read the moving mover's
own option from the NEW state in K4 and reported kenab equal to the number of moves; the predicate of the packet is read at the
CURRENT option with the new state below it, and with that reading every counter is 0. (2) A control that drops V1's «aligned»
case is INERT on this family (along the run that case also evaluates to 0), so the control used for the value side is V2's.

### 9.9 Positional strategies verified (TARGET.md §5, D2 change 5) (experiments/red-b/b6n5.py → data/b6b/out/strat.out, strat_ctrl.out)
TARGET.md's gauntlet asks that «every implementation also outputs positional strategies, and L-COMP verifies them on every test
game» (D2 change 5). For the dead-end record: at N5's stop on Γ3(G_k), engine 1's output (SPEC S5: regions from Ξσ, σ on Even's
region and Odd's optimal counterstrategy on Odd's) is checked by the harness verifier experiments/harness/verify.py `check`.
- must-0 counter `badstrat`, unit (genome), set k = 3..8: the number of complaints of that verifier. Result: 0 on all six
  (strat.out; the games are the same files: the .pg sha1 of each line equals the one in the packet's §9.4).
- Control (strat_ctrl.out): B6N5_CTRL=3 drops the strategy at one vertex of the winner's own region → badstrat 1 on G_4.
  Note on the control's choice: sending ONE choice to another successor is NOT a reliable control on these games, because most
  alternatives are winning too (on Γ3(G_4) only 4 of the 94 single-edge changes are detected by the verifier); dropping an entry
  is detected always.
- Reproduction note: b6n5.py gained this `badstrat` column in THIS entry. The lines pasted in the packet's §9.4 are the output of
  the version frozen at commit 350d84eb (no `badstrat` column); re-running the current version adds `badstrat 0` to each line and
  changes nothing else (checked for k = 3..8: every other field but the two timing columns, and the .pg sha1, are identical).

### 9.10 The run depends on nothing but the ε orders §8 names (experiments/red-b/b6perm.py → data/b6b/out/perm.out, perm_ctrl.out)
§8 lists the gate (ε) comparisons the proof uses (15 of them at k = 4, 45 at k = 9; everything else about the numbering is free).
This check draws RANDOM LINEAR EXTENSIONS of the partial order those comparisons define — a random topological order of the option
set, so the gate indices stay a bijection onto 0..M − 1 and the genome stays a genome of R104's class — and runs the model on each.
- must-0 counter `keep`, unit (relabeling), set 7,050 relabelings over k = 4, 5, 6, 7, 8, 9 (3000, 2000, 1000, 600, 300, 150):
  a relabeling that preserves every listed comparison gives T ≠ 2^k − 2. Result: 0 on all 7,050.
- Reported, not constrained: for each relabeling the script also breaks ONE listed comparison (chosen at random, by swapping those
  two gate numbers) and reports T. About 40% of the broken variants still give 2^k − 2 and the rest fall, as low as T = 3. So the
  list of §8 is SUFFICIENT (that is what the proof needs and what `keep` tests) and is NOT claimed to be minimal: a single
  comparison is often restored by the rest of the order.
- Control (perm_ctrl.out): with one entry of the list read the wrong way round (ε(u_j, o) > ε(v_j, o)), the sampler no longer draws
  the rule's numberings and `keep` fires on all 2,000 (perm_ctrl.out: keep 2000 on G_5).
Reading (not a statement): together with L-RED 70's own 1,200 ε renumberings (relayed by the Lead), this says the family is not an
artefact of one numbering: every numbering that respects the stated orders gives the same run.

### 9.11 R117's own side conditions on these games (experiments/red-b/b6reach.py → data/b6b/out/reach.out, reach_ctrl.out)
Corollary EXP-N5 uses RESULTS R117's Theorem REACH3 as landed. Two lemmas inside R117 are what a referee will want tested on games
of this shape (two options on one W-target, Ξ-target X at positive levels, all parities even, up to 9 movers on a level):
[Q R117] «S3's start pair equal to R104's stated start transported through the pads (Lemma S3-START)» and «no pad is ever a cycle
node or in a P-set (Lemma PAD)».
- must-0 counter `startdiff`, unit (vertex): SPEC's S3 start pair (n5x.start_pair on Γ3(G_k)) differs, at some vertex, from
  R104's stated start transported through the pads (what gamma3.build returns). Result 0 on k = 3..8.
- must-0 counters `padcyc` (unit (state, vertex): the cycle node of a vertex's value is a pad) and `padp` (unit (state, vertex):
  the P-set of a vertex's value contains a pad), over every state of the whole N5 run (10, 18, 34, 66, 130, 258 states; 92 to 452
  pads; every vertex at every state): 0 on k = 3..8.
- must-0 counter `fbpos`: the mover states 0..F are not the model's run, or the first fallback is not at transition L(G) + 1.
  Result 0 on k = 3..8.
- Control (reach_ctrl.out): B6R_CTRL=1 counts the same two quantities for the NON-pad vertices K1 and s instead of the pads:
  padcyc 4,800 on G_4 (K1 is the common cycle node). It fires.
This is DATA about R117's hypotheses on my instances; it is not a re-proof of R117, which is landed and refereed.

### 9.12 N5 itself at k = 12 (b6n5.py as frozen at 350d84eb → data/b6b/out/n5_k12.out; game data/b6b/pg/G_12_g3.pg)
The Lead asked for k = 12 on both engines (12:56Z item 2). The run `bash experiments/red-b/run_b6b.sh R n5 12` ended 13:22:07Z with
exit 0. Its line (n5_k12.out is line 10 of R/out/n5.out; lines 1-9 are byte-equal to the frozen data/b6b/out/n5.out):
`G_12 mode spec ctrl 0 N 92 M 184 n 1390 T1p 4094 F 4094 mism 0 its 4097 fb 1 wrong 0 nonmover 0 its2 4097 fb2 1 wrong2 0 engdiff 0
gdiff 0 pg_sha1 abca645247b284b74b535cb0bb196813e66ce81c secs1 622.3 secs2 944.2`
So at k = 12: n = 1390 = 135·12 − 230; the model's run has 4094 = 2^12 − 2 steps; N5 makes 4097 = 2^12 + 1 iterations on both
engines with its first fallback at transition 4095 = L + 1; every must-0 counter of §9.4 is 0 (mism, wrong, nonmover, wrong2,
engdiff, gdiff). The line has no `badstrat` column because it was made by the b6n5.py of the freeze commit (see 9.9's note).
Not done: fit.out and size.out were not regenerated with this line (the residual against 2^k + 1 at k = 12 is 0 by the line itself).

### 9.13 Other tie rules of engine 1 on the same games (b6n5.py with B6N5_MODE → data/b6b/out/tie.out): DATA, not a statement
Engine 1 (L-NEW's n5v.step, box 190) has four modes; in its own words: [Q n5v] «mode "spec": N5 (box21 n5x.step).»
«mode "idx" : the same TIE broken by the LARGEST vertex index (a different key order).» «mode "seq" : SPEC's sigma_new applied at
ONE Even vertex only (the least index where it differs), others keep sigma.»; mode "xi" is N5′-xi (the packet's §9.4 control).
On Γ3(G_4), Γ3(G_6), Γ3(G_8) (n = 310, 580, 850), iterations to the stop, each with 1 fallback:

| mode | G_4 | G_6 | G_8 |
|---|---|---|---|
| spec (N5) | 17 | 65 | 257 |
| xi (N5′-xi) | 7 | 7 | 7 |
| idx | 7 | 7 | 7 |
| seq | 65 | 154 | 235 |

Must-0 on all 12 rows: wrong 0 (against Zielonka), badstrat 0, gdiff 0. In the rows of modes xi, idx, seq the columns mism and
engdiff are 1 BY CONSTRUCTION (they compare with the model's key run and with engine 2 in mode spec), so they are not counters there.
Reading (not a statement, no growth word): the long run is a property of N5's own S4a key order on these games; three points per
mode identify no growth law for seq («not identified»), and nothing is claimed about any rule but N5.

### 10.E Reproduction erratum for §10: at 350d84eb the runner needs an ABSOLUTE ROOT (found by a clean-clone test, Lead 12:56Z item 5)
§10 writes `bash experiments/red-b/run_b6b.sh R all 11` with R = experiments/red-b/work/b6. Taken literally from the repository root
with the run_b6b.sh of the freeze commit this FAILS: the gen stage changes directory to experiments/red-b before it writes
R/G/G_k.json, so with a relative R every genome file fails with FileNotFoundError, every later stage fails for lack of its input,
and the runner still printed «done» and exited 0. The pinned DATA were made with a ROOT that resolved (cwd = experiments/red-b, ROOT
= work/b6), so no pinned file, statement or proof is affected.
- At 350d84eb use: `bash experiments/red-b/run_b6b.sh "$PWD/experiments/red-b/work/b6" all 11` (an absolute ROOT).
- From this entry's commit on, run_b6b.sh makes ROOT absolute itself, counts a failing stage command and exits 1 if there was one
  (its last line now ends «failures 0» on a clean run). Tested in a clean clone of the branch with a RELATIVE ROOT and archives made
  by §10's commands: gen 6, member 6, lemma 5 exit 0 and member.out is byte-equal to the first four lines of the frozen
  data/b6b/out/member.out; the n5 stage on a ROOT without archives exits 1.
- The instance lines of the dead-end record by one command each (after the archives): `bash experiments/red-b/run_b6b.sh R gen 10`
  then `bash experiments/red-b/run_b6b.sh R n5 10` writes R/out/n5.out with the lines of G_3..G_10 (the smallest instance is
  G_3: data/b6b/pg/G_3_g3.pg, n = 175, 9 iterations). With the b6n5.py of this entry each line carries the extra column
  `badstrat 0` (9.9's note); every other field is that of the frozen lines.
- Clean-clone run with the fixed runner, a relative ROOT and §10's archives (13:55:15Z to 14:02:01Z by date -u; one CPU): `gen 10`
  under 1 s; `n5 3` (G_3 alone, both engines) 0.1 s; `n5 10` 406 s for G_3..G_10 (G_10 alone 97.7 s + 150.1 s); «failures 0» on each.
  The 8 lines (data/b6b/out/n5_clean.out) equal the frozen lines of data/b6b/out/n5.out in every field but the added `badstrat 0`
  and the two timing columns, and the 8 game files are byte-equal to data/b6b/pg/ (G_3_g3.pg sha1
  fca7a52c49e095d297458c2264664b846c442f8b, G_10_g3.pg sha1 615292907463d55cb3156d14914af2a916e5b27e). This also extends 9.9's
  strategy check to k = 9, 10 (badstrat 0).
