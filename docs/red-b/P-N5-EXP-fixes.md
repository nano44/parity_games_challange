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
## Entries 2-5: conventions (L-RED-B successor 6, session_01V5yGRYvwUZTkQxfvG8iXBu; written 2026-11-13 15:49Z by date -u)
These four entries answer the referees item by item, by each referee's own item number (REFEREE 35's pre-check, REFEREE 36's
first review, REFEREE-2 41's second review). The frozen packet is not edited
(`sha1sum docs/red-b/P-N5-EXP.md` → c0449b17193f19619f33b366096762dfde27d542; the frozen pins SHA1SUMS_b6b are byte-identical).
What changes: the STATEMENTS of the RESPONSE LEMMA and of STABLE are replaced by the forms of entry 4 (the mathematics and every
number stay); the LABELS of Corollary EXP-N5 and of the dead-end paragraph are fixed by entry 2; entry 3 adds a corollary; entry 5
is wording and records. Theorem EXP-IDEAL (a)-(c) is unchanged.
Quotes: as in the packet, every guillemet quote that follows a Q-tag is checked verbatim, here by experiments/red-b/b6fixquote.py
(b6quote.py with the sources read by `git show COMMIT:PATH`; output data/b6b/out/quote_fixes.out: 80 tagged quotes in this file, 5 in entry 1 and 75 in entries 2-5, 80 found verbatim, «quotes 80 found 80 notfound 0»; with its control,
every quote spoiled by one letter, quote_fixes_ctrl.out: «quotes 80 found 0 notfound 80»). Labels: FROZEN = docs/red-b/P-N5-EXP.md at 350d84eb; REF2 = REFEREE-2 41's second
review, claude/referee-2 33ff0e98911544cb18545541e4acbe71de84c6e0, docs/referee-2/R2-P-N5-EXP.md (sha1
f63e227e31586d159fad57a6c3ea986cdf644343, 284 lines); PRE = REFEREE 35's pre-check (of the rule as relayed, before the freeze; not a
signature), claude/referee 06ac891df6f6212bac74259863da3105e7fe4341, docs/referee/R-GK-precheck.md (sha1
e2d7c5cb965a960bd0dc5c00d5cd50fc6d368e6f, 371 lines); REF1 = REFEREE 36's first review (stage 1), claude/referee
c881709b78d8e4b2debb72baf2c487156413416f, docs/referee/R-P-N5-EXP.md (sha1 c662d157621671c816ef03726e1649af1b648555, 397 lines);
R117, R124, R57 = trunk 5d7aab0f docs/RESULTS.md (sha1 eecbd798b81ad431d1b753f5a7f92f3c63e56da1, the same file at trunk 6eaf4604),
each restricted to that entry; R104P = trunk 5d7aab0f docs/red/P-N5-REALIZE.md; KEY1P = claude/l-new
44775605 docs/new/P-N5-KEY1P.md (a lane packet, frozen, sha1 f7191623e9ee212fa127c7e4a224f7ab9d689156); LNEW = claude/l-new aa29064d
docs/new/P-N5-KEY1P-after-EXP-draft.md (a lane draft). Line numbers after a label are lines of that source.
New tools: experiments/red-b/b6prefix.py (direct tests), run_b6fix.sh (its runner; no archive needed, about two minutes),
b6fixquote.py; new DATA files in experiments/red-b/data/b6b/out/, pinned in data/b6b/SHA1SUMS_b6b_fixes2 (checked by check.sh).
Also added, not used by these entries: b6n5ck.py, b6n5.py's engine 1 with a checkpoint every 100 iterations (the only resumable
way to run N5 at k = 13; that run was in progress at this commit and is not DATA here).

## Entry 2 (L-RED-B successor 6, 2026-11-13): what is unconditional, what is conditional, what is measured — answers REFEREE-2 41's W-2 and §4, REFEREE 35's P-1 and REFEREE 36's P-1 and E-7
The items, verbatim (REF2 = REFEREE-2 41: W-2, l. 55-59, and its §4, l. 238-255; PRE = REFEREE 35's pre-check: P-1, l. 322-326; REF1
= REFEREE 36: its §2, l. 55-63, its verdict rows l. 20-21, and E-7, l. 281-285).

[Q REF2 l. 55-59] «That sentence is Corollary EXP-N5, which is proved THROUGH R117's Theorem REACH3. R117 is a landed, refereed-only
result with standing premises» «So the sentence is PROVED-CONDITIONAL on R117 as landed, like every line that cites R117; the RESULTS
line should carry «refereed-only, through R117» and not a bare «FALSE».»

[Q REF2 l. 239, 241] «UNCONDITIONAL (mathematics about R104's DEFINITIONS, no theorem used): Theorem EXP-IDEAL (a), (b), (c) with its
lemmas.» «PROVED-CONDITIONAL on RESULTS R117 as landed: Corollary EXP-N5's iteration bound, and with it the Dead-end paragraph»

[Q PRE l. 322-326] «So «N5 from S3 makes at least 2^k − 1 iterations on Γ3(G_k) for every k» can be stated only with R117's premises,
in R117's words; the measured runs (§4) are premise-free DATA (the engines execute SPEC). The packet should say which of the two
each clause is.»

[Q REF1 l. 60-63] «the Corollary (l. 54-60), the title (l. 1) and the dead-end paragraph (l. 61-66) do not repeat them: P-1.» «So:
Corollary EXP-N5 and «FALSE» are CONDITIONAL on R117's premises; for k = 3..12 the iteration counts are also MEASURED, premise-free
(§7).»

[Q REF1 l. 283-285] «the DATA covers k = 3..11; for every k the sentence is landed R57 (b) (Lemma OUT-G: «on every game N5 stops
(R15 (d)) and SPEC S5's output there is correct», under 1E-N3). Say which.»

No statement and no proof of the frozen packet changes; this entry fixes the LABELS and the wording of the dead-end sentence.

**(a) UNCONDITIONAL (R104's DEFINITIONS only).** Theorem EXP-IDEAL (a), (b), (c), with Lemma MEMBER, MOVE-2, V0-V4, K1-K4, WIRE, the
RESPONSE LEMMA and STABLE (both in the form of entry 4), use the definitions quoted in the frozen §1 (the genome, IDEAL-ACYC, the
X-chain and its order, the IDEAL step, L(G)) and nothing else: no theorem of R104 or of any other entry, no SPEC premise, nothing
about N5. They are statements about a finite object, a genome and the step map R104 defines on it. Label: PROVED (lane) until two
referees sign; then refereed-only.

**(a′) A consequence of (a) alone, inside the model.** R104's packet names the polynomial statement about the model:
[Q R104P l. 224] «Let IDEAL-ACYC-POLY mean: there is a polynomial q such that L(G) ≤ q(N + M) for every G ∈ IDEAL-ACYC.»
Theorem EXP-IDEAL (b) refutes it without any premise: L(G_k) = 2^k − 2 and N + M = 27k − 48, and every G_k has all degrees 2. By
(c) the same holds per mover: the movers of unit k − 1 change their option 2^(k−2) times. So the two statements that L-NEW's packet
P-N5-KEY1P (lane; frozen at claude/l-new 44775605, docs/new/P-N5-KEY1P.md, sha1 f7191623e9ee212fa127c7e4a224f7ab9d689156) leaves
open, [Q KEY1P l. 138] «There is a polynomial p with T_key(G) ≤ p(N + M) for every genome G with an acyclic Ξ-graph.» (its
QUIET-KEY-1P) and [Q KEY1P l. 211] «There is a polynomial q with sw(x) ≤ q(N + M) for every genome G with an acyclic Ξ-graph and
every mover x of G.» (its SW-POLY), are false when T_key and sw are read in R104's IDEAL model, as that packet's Lemma IDEAL-1P
reads them (L-NEW's lemma; not used by anything else here). No statement about N5 is involved in (a′).

**(b) PROVED-CONDITIONAL on RESULTS R117's Theorem REACH3 AS LANDED [refereed-only].** Corollary EXP-N5 (frozen §2 l. 54-60, §7 l.
276-282) is (a) put into REACH3; it inherits R117's standing premises and adds none. R117's title line names them:
[Q R117 l. 13362] «with R104's premises as landed (1E-N3 = RESULTS R57 (b) in its two forms; RESULTS R24 (a) Lemma R and R24 (b)'s
choice rule with RESULTS R103's bridge B and (R1) ruling; RESULTS R36 (c) Lemma P1 on the dual game) and RESULTS R15 (d) for
termination only»

R117's entry calls them [1E-N3], [RULE], [VJ-LOC], [TERM], and says what they leave open:
[Q R117 l. 13482-13488, 13543-13544] «R104's three premises as landed, in R104's forms: [1E-N3]» «forms P1 (σ̄, τ̄ pointwise optima)
and P2 (S4a's σ_new a pointwise optimum of H); [RULE]» «[VJ-LOC] (R104 l. 10011-10012, R36 (c) Lemma P1 on the dual game» «[TERM]
RESULTS R15 (d)» «Premises [1E-N3], [RULE], [VJ-LOC] as landed in R104: the correctness of S1's procedure stays SPEC's requirement,
and the code's match to SPEC is DATA (R57 (b))»

REACH3's hypothesis on the genome is [Q R117 l. 13362] «for every G with an ACYCLIC Ξ-graph»; G_k is such a genome by (a) (Lemma
MEMBER, c8), and L(G_k) = 2^k − 2 ≥ 1. Nothing else of R117 is used (not NO-REACH, not Corollary REAL-IDEAL-S3 as a premise, not
SUBDIV).

**(c) The dead-end paragraph (frozen l. 61-71) carries the condition of (b) [W-2].** Its sentences
[Q FROZEN l. 61-63] «The claim "N5 (SPEC S1-S5, default start S3) runs in polynomial time" is FALSE.» «N5 therefore cannot pass
gauntlet step 4 (no running-time proof can exist) and is a dead end as an M4 candidate; G-N5-TIME is answered NO.»

are consequences of Corollary EXP-N5 and are to be READ, here and wherever they are quoted: through RESULTS R117's Theorem REACH3
(refereed-only), under R117's standing premises of (b). In full: under R117's Theorem REACH3 as landed, N5 (SPEC S1-S5) from its
default start S3 makes at least 2^k − 1 iterations on Γ3(G_k), a game with n = 135k − 230 vertices and n + m = 311k − 530 vertices
and edges; so N5 from S3 does not run in polynomial time, cannot pass gauntlet step 4, and G-N5-TIME is answered NO for N5 from S3.
The arithmetic of that paragraph (the sizes; the first k beyond n^c) is unconditional. The Lead's wording of 12:43Z is kept, with
this condition attached.

**(d) MEASURED (DATA): the N5 runs kill nothing by themselves.** The runs of N5 on Γ3(G_k) (frozen §9.4, k = 3..11; entry 1, k = 12;
the other lanes' and the referees' runs) use no premise of R117 as mathematics: an engine runs and its iterations are counted. But
they are runs of implementations of SPEC, and they stop at k = 12: 2^12 + 1 = 4,097 iterations on n = 1,390 vertices (n + m =
3,202), which is above n from k = 11 on (2,049 > 1,255) and above n + m at k = 12, and below n² = 1,932,100. 2^k − 1 exceeds n²
first at k = 23 (frozen §9.5: n = 2,875, 8,388,607 iterations), which no engine here reaches. So no measured run lies beyond an
explicit polynomial bound of degree 2 or more, and the kill rests on the PROOF: (a) with R117 (and R124 for the exact count, entry
3). REFEREE-2 says the same of its own runs:
[Q REF2 l. 248-249] «They are far below every explicit polynomial bound (2^k − 1 < n² until k = 23, where a run would take 8.4
million iterations on 2,875 vertices): no measured instance «beyond an explicit bound» exists or is in reach of these engines. The
kill rests on the proof.»

The DATA's role: to test every step of the proof (must-0 counters with firing controls) and the predictions of R117 and R124 at
k ≤ 12 (the first fallback at iteration L(G_k) + 1 = 2^k − 1; 2^k + 1 iterations; the mover states equal to the model's).

**(e) The sentence on correctness (frozen l. 65-66) [E-7].** The frozen sentence is [Q FROZEN l. 65-66] «N5 is CORRECT on these
games (DATA §9.4: every winner equals Zielonka's); what fails is the polynomial bound.»

For k ≤ 12 this is DATA (frozen §9.4, k = 3..11, and entry 1, k = 12: every winner equals Zielonka's; the referees and L-COMP add
their own solvers, entry 5.8). For EVERY k it is not DATA but landed RESULTS R57 (b), Lemma OUT-G, under the same standing premise
as (b):
[Q R57 l. 2893, 2914-2916] «N5's output at its stop is correct on EVERY parity game (Lemma OUT-G)» «In particular, on every game N5
stops (R15 (d)) and SPEC S5's output there is correct. Standing premise, as in R51 (d): OUT-G concerns SPEC's Ξσ and σ̄; that S1's
procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance, and the code's match to SPEC is DATA (R15 G-N5T-1) (1E-N3 =
N-1E-1).»

So the frozen sentence is to be READ: N5's output on Γ3(G_k) is correct for every k by RESULTS R57 (b), Lemma OUT-G (refereed-only,
under 1E-N3), and for k ≤ 12 this is also measured; what fails is the polynomial bound, not the answer.

## Entry 3 (L-RED-B successor 6, 2026-11-13): Corollary EXP-N5′, the EXACT count, by landed R124 — REFEREE 36's O-1 (optional) and L-NEW 77's note; an addition, not needed for the dead end
[Q REF1 l. 66-67] «The packet does not need it (the lower bound kills). O-1 (optional fixes entry): cite it for the exact count,
with its premises (R117 (f), 1E-N3, SPEC's FIX 1-4 tie-breaks through REACH3's [RULE]).»

Source of the remark: L-NEW 77, claude/l-new aa29064d1, docs/new/P-N5-KEY1P-after-EXP-draft.md l. 13-14 (a draft of that lane):
[Q LNEW l. 13-14] «N5 makes exactly T_key + 3 = 2^k + 1 iterations with one fallback, at transition 2^k − 1 (the exact count of
landed RESULTS R124, Corollary EXACT-L»

R124 was opened at the source for this entry (trunk 5d7aab0f docs/RESULTS.md l. 15371, its title line; all quotes below are from it).

**Corollary EXP-N5′** (PROVED-CONDITIONAL on RESULTS R124's Corollary EXACT-L AS LANDED [refereed-only]; EXACT-L's premise is RESULTS
R117 (f) = Theorem REACH3, so the premises of entry 2 (b) apply, with R124's own, quoted below). For every k ≥ 3, N5 (SPEC S1-S5
with its FIX 1-4 tie-breaks) from S3 on Γ3(G_k) makes EXACTLY L(G_k) + 3 = 2^k + 1 iterations, with exactly one fallback, at
iteration 2^k − 1.

Proof. G_k ∈ IDEAL-ACYC (Lemma MEMBER, c8: the Ξ-graph is acyclic and has no self-loop) and L(G_k) = 2^k − 2 (Theorem EXP-IDEAL
(b)). R124's Corollary EXACT-L and its Theorem ENDGAME-3-N5 say:
[Q R124 l. 15371] «PROVED for G ∈ IDEAL-ACYC» «N5 (SPEC S1-S5 with its FIX 1-4 tie-breaks) from S3 on Γ3(G) makes exactly L(G) + 3
iterations, L(G) the length of G's IDEAL run» «N5′-xi, and N5, from S3 on Γ3(G) have exactly one fallback, at an iteration F ≥ 1,
and exactly F + 2 iterations»

So the count is L(G_k) + 3 = 2^k + 1 and the fallback is iteration F = L(G_k) + 1 = 2^k − 1. ∎

R124's premises, in its words:
[Q R124 l. 15371] «premise RESULTS R117 (f); it uses SPEC's S1 tie-breaks, through REACH3's [RULE] choice: with another
pointwise-optimal S4a choice the identity can fail» «premises, all under the standing SPEC premise 1E-N3 of RESULTS R57 / R104 /
R117» «iterations counted as in SPEC S4»

What EXP-N5′ adds. The frozen Corollary EXP-N5 (at least 2^k − 1 iterations, by R117 alone) stays as frozen and is all the dead end
needs. EXP-N5′ gives the equality, and R124's own consequence clause is the «iff» behind the dead-end wording:
[Q R124 l. 15371] «so on {Γ3(G) : G ∈ IDEAL-ACYC} N5's iteration count is polynomial in n iff L(G) is polynomial in N + M (a
statement about iteration counts; the cost per iteration at bit cost is a separate gauntlet step-4 item)» «it bounds none of F, T3,
L(G) (OPEN)»

Theorem EXP-IDEAL decides the right-hand side of that «iff»: L(G_k) = 2^k − 2 with N + M = 27k − 48, so L(G) is not polynomial in
N + M on IDEAL-ACYC (entry 2 (a′)), and so, by R124, N5's iteration count on R124's class of games is not polynomial in n.

DATA agrees with the exact count at every k run: frozen §9.4 (k = 3..11) and entry 1 (k = 12) have its = its2 = 2^k + 1, fb = fb2 =
1 and F = 2^k − 2 S4a iterations before the fallback (so the fallback is iteration 2^k − 1); REFEREE-2's own engine has the same for
k = 3..11:
[Q REF2 l. 206-207] «the first fallback is transition 2^k − 1 (as REACH3 says: L(G) + 1), N5 makes 2^k + 1 iterations, and its
answer is right.»

## Entry 4 (L-RED-B successor 6, 2026-11-13): the RESPONSE LEMMA RESTATED (one lemma, prefix form: LEMMA′) with CAUSAL, and STABLE in step form — answers REFEREE-2 41's G-1 and REFEREE 36's E-1, E-2, E-4, E-5
The referees' items, verbatim (REF2 = REFEREE-2 41, REF1 = REFEREE 36).

[Q REF2 l. 38-45] «Case (ii) applies the lemma to unit j + 1 before the hypothesis (H2) of that application is known» «So the lemma,
as stated with (H2) on the whole window, cannot be used as a black box inside its own induction step. What the packet's
step-by-step text proves, and what the induction needs, is the PREFIX form of §2.4 (hypothesis and conclusion both cut at a step
τ_0), by an induction on τ_0 inside the downward induction on j. The stated lemma is the case τ_0 = the last step. Fix for the
lane: state the prefix form as the induction hypothesis (text in §2.4).»

[Q REF1 l. 180-188] «If the run has stopped at s_(t−1), (H2) is vacuous and the conclusion is false. INSTANCE, every k ≥ 3: (j, a,
t) = (1, 1, 2^k − 1).» «The lemma means the key input of the STEP, i.e. C_(j−1) under the s′ that the definition computes from
s_(τ−1), whether or not s′ ≠ s; the hypothesis must say so.»

[Q REF1 l. 191-196] «At the point where it is used, that hypothesis is not yet known» «As a black box the lemma cannot be applied
before its hypothesis holds on the whole interval, so the induction as written is circular. The packet's own words («which we
check along the way») describe a step-by-step argument; that argument needs the lemma in a PREFIX form (the moves of the steps t,
…, T follow from the inputs up to T), which is not what is stated.»

[Q REF1 l. 125-129] «K1's C_0(s) = s(v_0) and V1's E_0(s) = s(v_0), and with them every C_j, E_j, EY_j, D_j, Z_j, need s(u_0) = 0»
«Fix: «every wire and u_0 at option 0» (the wire part is needed only for the wording of K2 / K3 / WIRE). The run satisfies it
(WIRE).»

[Q REF1 l. 257-261] «Read under one state it is false: under s_0 unit 1 is at rest 0 with input (0, 0), and v_1 moves in step 1»
«Correct form: «if unit i is at rest b under s, E_(i−1)(s) = b and C_(i−1)(s⁺) = b, then s⁺ = s on unit i». Its two uses (l.
255-256; l. 270-271) are correct with this form, applied level by level from level 0 up.»

**4.0 What changes.** The frozen file is not edited. The frozen STATEMENT of the RESPONSE LEMMA (l. 192-204) is REPLACED by 4.4 and
the frozen statement of STABLE (l. 258) by 4.2; the frozen PROOF text (l. 205-257, 258-262) stays and is read as 4.5 says; Theorem
EXP-IDEAL, its proof (§7, read as 4.6) and every other statement are unchanged. The two referees found the same defect of FORM
independently and wrote the same repair: REFEREE-2 its PREFIX FORM (REF2 §2.4), REFEREE 36 its CAUSAL and LEMMA′ (REF1 §5.3,
referee-originated, L41). This entry is the lane's own repair. It does not write a third form: 4.3 and 4.4 ADOPT REFEREE 36's two
statements word for word, 4.4 shows that REFEREE-2's PREFIX FORM is the same statement, and 4.5 gives the proof in the order both
referees give. Item by item:
- G-1 / E-2: the frozen proof applies the lemma to unit j + 1 [Q FROZEN l. 229] «provided its input stays (1, 1), which we check
  along the way», i.e. with (H2) of unit j + 1 known only up to the step under discussion. 4.4 is the prefix form the induction
  uses and proves.
- E-1: the frozen (H2) is quantified over the τ «that the run reaches»; at t = 2^k − 1 no such τ exists, (H2) is vacuously true,
  (H1) holds for (j, a) = (1, 1) under the last state, and the frozen conclusion «the run reaches s_(t+P_j−1)» is false. In 4.4
  the key hypothesis is about the state s⁺ that the step computes, whether or not the run goes on; it FAILS at that triple (4.4,
  Remark 1).
- E-4: 4.1 (S1) adds u_0 to the standing assumption.
- E-5: 4.2 states STABLE for a step, the key bit under s⁺.

**4.1 Standing assumptions and notation (for the frozen §5-§7 and for this entry).** REFEREE 36's standing paragraph is adopted:
[Q REF1 l. 200-202] «Standing: states with every wire and u_0 at option 0 (E-4). For such a state s that is not «opt», s⁺ := the s′
of R104's step («defined level by level»); for an «opt» state s⁺ := s. The run continues from s iff s⁺ ≠ s, and then the next state
is s⁺. (WIRE's static part: s⁺ again has the wires and u_0 at 0.) U_j := the movers of the units j, …, k − 1.»

- (S1) [E-4] «State» means a state of G_k with every wire AND u_0 at option 0. Only K1's and V1's level-0 clauses (C_0(s) = E_0(s)
  = s(v_0)) use «u_0 at 0». s_0 is such a state and s ↦ s⁺ keeps the property (a wire at 0 and u_0 at 0 are neither value-enabled
  nor key-enabled: WIRE's argument, which is about one step from any state).
- (S2) [E-1; REFEREE-2's W-1] s⁺ is defined for EVERY state, and s⁺ = s exactly when the run stops at s («opt» or «stuck»). The run
  is s_0, s_1 = (s_0)⁺, …, s_L, with L = L(G_k) the least τ with (s_τ)⁺ = s_τ. «Step τ» is the passage s_(τ−1) → s_τ = (s_(τ−1))⁺.
  «The run reaches s_τ» means τ ≤ L. A hypothesis about the key input of step τ is a hypothesis about (s_(τ−1))⁺, which exists
  whether or not the run goes on; so no hypothesis is vacuous at a stopped state.
- (S3) [E-5, G-1 / E-2] In a step s → s⁺ the VALUE bits E_i, EY_i, EY′_i are read under s (the availability sets A_s are defined
  from s), the KEY bits C_i, D_i, Z_i under s⁺ (R104's keys are taken with s′ on the lower levels). The INPUT OF UNIT j IN THE STEP
  s → s⁺ is the pair (C_(j−1)(s⁺), E_(j−1)(s)): its key input and its value input. The frozen «input of unit j under s», (C_(j−1)(s),
  E_(j−1)(s)), stays as the name of two bits of ONE state; it is used in (H1) only.
- (S4) last := t + P_j − 1 for j ≥ 2 and t + P_1 − 2 for j = 1; the WINDOW of a response of unit j that begins at step t is the set
  of steps t, …, last (the steps the frozen (i), (ii) list). The UPPER PART of a state, for a given j, is its restriction to U_j.

**4.2 STABLE (step form; replaces the frozen statement l. 258) [E-5].** Let s be a state, 1 ≤ i ≤ k − 1, b ∈ {0, 1}. If REST_i(b)
holds under s, E_(i−1)(s) = b and C_(i−1)(s⁺) = b, then s⁺ = s on unit i (REFEREE 36's form, quoted above); hence REST_i(b) under
s⁺, C_i(s⁺) = 0 and E_i(s) = 0. Consequently, if in addition REST_m(0) holds under s for every m > i, then s⁺ = s on U_i.
Proof. The frozen proof (l. 258-262), with «key-disabled» read as K4 reads it: u_i, v_i, e_i stand at b = C_(i−1)(s⁺); the observers
are value-disabled under s exactly as written there (Y_i from E_(i−1)(s) = b; Y′_i from EY_i(s) = 1 − b, which REST_i(b) gives by
V2). The pair is aligned at b under s and s⁺, so C_i(s⁺) = 0 (K1) and E_i(s) = [EY_i(s) = b] = [1 − b = b] = 0 (V1). For m = i + 1
the hypotheses hold again with b = 0 (REST_m(0), E_i(s) = 0, C_i(s⁺) = 0): induction on m. ∎
The two frozen uses are step-form uses: l. 255-256 (step t_2 + 1: unit j + 1 is in REST_(j+1)(0) under s_(t_2) with E_j(s_(t_2)) = 0
and C_j(s_(t_2+1)) = 0, the units above at rest 0), and §7 l. 270-271 (s := s_(2^k−2): REST_1(1), E_0(s) = 1, and C_0(s⁺) = 1
because v_0, at option 1, does not move (WIRE); REST_i(0) for i ≥ 2; so with WIRE no mover moves, s⁺ = s).

**4.3 CAUSAL (REFEREE 36's statement, adopted).**
[Q REF1 l. 203-204] «For 1 ≤ j ≤ k − 1 the restriction of s⁺ to U_j is a function of three things only: the restriction of s to U_j,
the bit E_(j−1)(s), and the bit C_(j−1)(s⁺).»

That is: the upper part of s⁺ is a function of the upper part of s and of the input of unit j in the step. REFEREE-2 names the two
facts behind it: [Q REF2 l. 89-90] «(K-loc) no observer is a W-target, so a key depends only on the options of pairs, e's and
wires of lower levels; (V-loc) values are read under the OLD state s.»

Proof (REFEREE 36's argument, REF1 l. 205-209, written out in an order in which every bit used is already fixed). By MOVE-2 a mover with two options
moves iff it is value-enabled under s and key-enabled with s⁺ on the lower levels. Downward induction on j:
 (L1) whether u_j, v_j, e_j move: by their options under s, by EY_j(s), EY′_j(s) (V4), which are functions of s on Y_j, Y′_j and
      of E_(j−1)(s) (V2, V3), and by C_(j−1)(s⁺) (K4);
 (L2) the input of unit j + 1 in the step, (C_j(s⁺), E_j(s)): a function of s⁺(u_j), s⁺(v_j), C_(j−1)(s⁺) (K1) and of s(u_j),
      s(v_j), EY_j(s) (V1); so, by CAUSAL for j + 1, s⁺ is fixed on U_(j+1);
 (L3) whether an observer of Y_j, Y′_j moves: by its option under s, by E_(j−1)(s), resp. EY_j(s) (V4), and by D_j(s⁺), Z_j(s⁺)
      (for j = k − 1: C_(k−1)(s⁺)) (K4), functions of s⁺(E(j + 1)) and C_j(s⁺) (K2, K3).
The order is well-founded by (K-loc) (table: the W-targets are u's, v's, wires and end-followers, never an observer) and (V-loc). ∎

**4.4 RESPONSE LEMMA, restated: LEMMA′ (REFEREE 36's statement, adopted; replaces the frozen statement l. 192-204).**
[Q REF1 l. 219-225] «Let 1 ≤ j ≤ k − 1, a ∈ {0, 1}, c := 1 − a, t ≥ 1, last := t + P_j − 1 for j ≥ 2 and last := t + P_1 − 2 for j = 1,
and let T be an integer with t − 1 ≤ T ≤ last. Suppose the run reaches s_(t−1), (H1) holds under s_(t−1), and (H2′_T) for every τ with
t ≤ τ ≤ T: if the run reaches s_(τ−1), then C_(j−1)((s_(τ−1))⁺) = c; and for every τ with t ≤ τ ≤ T − 1: if the run reaches s_τ, then
E_(j−1)(s_τ) = c. Then the run reaches s_T, each of the steps t, …, T changes a mover, and in the steps t, …, T the movers of U_j move
exactly as the packet's list (i) / (ii) says (with the lemma's F, B, F′, B′, t_1, t_2). For T = last this includes: s_τ(E(j)) = a for
τ < last and E(j) moves to c at step last (j ≥ 2), and REST_j(c), REST_i(0) for i > j under s_last.»

Here (H1) is the frozen (H1) (l. 193), i.e. under s_(t−1): REST_j(a), REST_i(0) for every i > j, and C_(j−1)(s_(t−1)) = E_(j−1)(s_(t−1))
= a. In the words of (S3), (H2′_T) says: the input of unit j is (c, a) in step t and (c, c) in the steps t + 1, …, T. The conclusion
has three parts, called below (R1) the steps t, …, T are the listed ones on U_j; (R2) each of them changes a mover and the run
reaches s_T; (R3) for T = last, the clause on E(j) and the rest states.
REFEREE-2's PREFIX FORM is the same statement with τ_0 = T ≥ t:
[Q REF2 l. 129-132] «PREFIX FORM. Let j, a, c, t, F, B, F′, B′ be as in the packet, last := t + P_j − 1 (t + P_1 − 2 for j = 1), and
assume (H1). Let t ≤ τ_0 ≤ last and assume (H2[τ_0]): for every τ with t ≤ τ ≤ τ_0 the step from s_(τ−1) leaves C_(j−1) = c on the
levels below j (i.e. C_(j−1)(s_τ) = c), and E_(j−1)(s_τ) = c for every τ with t ≤ τ ≤ τ_0 − 1. Then the run reaches s_(τ_0), and in
each step τ ∈ [t, τ_0] the movers of the units j, …, k − 1 that move are exactly those the packet lists for step τ.»

Concordance. Its key clause «the step from s_(τ−1) leaves C_(j−1) = c» is C_(j−1)((s_(τ−1))⁺) = c, LEMMA′'s key clause; its value
clause is LEMMA′'s; its conclusion is (R1), (R2). LEMMA′ says in addition: T = t − 1 (nothing to show), the guards «if the run
reaches», and (R3). The guards cost nothing: by (R2), under (H2′_T) the run reaches every s_τ, τ ≤ T, so each guarded clause is
used. So the two forms are one lemma, with one proof (4.5).
Remark 1 (E-1's instance is excluded). For (j, a, t) = (1, 1, 2^k − 1) and any T ≥ t: the run reaches s_(t−1) = s_L and (H1) holds,
but (s_L)⁺ = s_L has C_0 = 1 = a ≠ c, so (H2′_T) fails at τ = t and LEMMA′ claims nothing. In general, for T ≥ t, (H2′_T) contains
C_(j−1)((s_(t−1))⁺) = c ≠ a = C_(j−1)(s_(t−1)), which forces (s_(t−1))⁺ ≠ s_(t−1): the hypothesis is never vacuous at a stopped state.
The same holds at the triples (j, 0, 2^k − 1), 2 ≤ j ≤ k − 1, where the frozen wording fails in the same way (REFEREE 36 says so too,
REF1 l. 184; 4.7 (2), control 5, lists them).
Remark 2 (what the frozen (H2) asked in addition). For T = last the frozen (H2) also asked for E_(j−1)(s_last) = c, a bit that no
step of the window reads (it holds on the run: 4.7 (1), counter h2last).
Remark 3 (how the lemma is used). Twice: by itself for j + 1 (4.5), and in §7 for j = 1, where (H2′_T) is known for every T
beforehand (4.6).

**4.5 Proof of LEMMA′ (the frozen l. 205-257, in the order of REFEREE-2's §2.4 and of REFEREE 36's proof, REF1 l. 226-239).**
Downward induction on j; inside it, induction on T. T = t − 1: nothing to show. Let t ≤ T ≤ last, assume LEMMA′ for j + 1 (nothing
for j = k − 1) and the claim for T − 1: the run reaches s_(T−1), and s_(t−1), …, s_(T−1) are the listed states on U_j. Step T is to be
decided, i.e. (s_(T−1))⁺ on U_j. By CAUSAL it reads from below exactly C_(j−1)((s_(T−1))⁺) and E_(j−1)(s_(T−1)), which (H2′_T) gives
(the first is c; the second is c, and a for T = t, by (H1)). In the order of (L1)-(L3), which is REFEREE-2's (1)-(4):
 (1) the level-j movers u_j, v_j, e_j: V4 under s_(T−1), K4 with C_(j−1)((s_(T−1))⁺) = c;
 (2) hence C_j((s_(T−1))⁺) (K1) and E_j(s_(T−1)) (V1): these are the bits that (H2′_T) of unit j + 1 asks for, for the inner window
     that contains T (at that window's first step, E_j(s_(T−1)) is part of its (H1));
 (3) LEMMA′ for j + 1 with ITS T equal to OURS: the moves of U_(j+1) in the steps up to T, in particular (s_(T−1))⁺(E(j + 1));
 (4) the observers of unit j: V4 under s_(T−1), K4 with D_j, Z_j under (s_(T−1))⁺ (K2, K3 from (s_(T−1))⁺(E(j + 1)) and C_j((s_(T−1))⁺)).
There is no circle: (3) at step T rests on the inner hypothesis up to T only, and that hypothesis rests on (1) at the steps ≤ T
and on the states up to s_(T−1). The result is the list's step T, which changes a mover; so (s_(T−1))⁺ ≠ s_(T−1), the run reaches
s_T = (s_(T−1))⁺: (R2). The frozen text carries out (1)-(4) step by step:
 Case (i), j = k − 1 (l. 207-217): steps t, t + 1, t + 2; no unit above, so (2), (3) are empty and D_j, Z_j are replaced by C_(k−1).
 Case (ii), j ≤ k − 2 (l. 218-257):
  - the first inner window, steps t, …, t_1, from REST_(j+1)(0). Its (H1) is ours (l. 221-222: (C_j, E_j) = (0, 0) under s_(t−1)).
    Its (H2′_T), C_j((s_(τ−1))⁺) = 1 for t ≤ τ ≤ T and E_j(s_τ) = 1 for t ≤ τ ≤ T − 1, holds for t ≤ T ≤ t_1: v_j moved to c in step t
    and is key-disabled while the key input of unit j is c; u_j is value-disabled while EY_j = c (l. 223, 231-233), which the claim
    for T − 1 and E_(j−1)(s_(T−1)) = c give; so the pair is split with v_j at c = C_(j−1) (K1: C_j = 1), and E_j = 1 under every split
    state (V1). This is what the frozen words [Q FROZEN l. 229] «which we check along the way» stand for.
  - the second inner window, steps t_1 + 1, …, t_2, from REST_(j+1)(1). Its (H1) holds under s_(t_1) (l. 245-246; the pair is still
    split under s_(t_1), and (R3) of the first inner window gives REST_(j+1)(1), REST_i(0) above). Its (H2′_T), C_j((s_(τ−1))⁺) = 0 for
    t_1 + 1 ≤ τ ≤ T and E_j(s_τ) = 0 for t_1 + 1 ≤ τ ≤ T − 1, holds: u_j moved to c in step t_1 + 1, the pair is aligned at c and
    key-disabled while the key input of unit j is c (K1: C_j = 0), and E_j = [EY_j = c] = 0 because Y_j stands at (c, 1 − c) from
    s_(t_1) on (EY_j = a by V2, whatever the input) and does not move while E_(j−1) = c under the previous state (l. 243-245).
  - step t_2 + 1 (j ≥ 2): the units above j by STABLE in step form (4.2), with (R3) of the second inner window, E_j(s_(t_2)) = 0
    and C_j(s_(t_2+1)) = 0.
 (R2) in detail: step t moves v_j; the steps of the two inner windows move a mover by (R2) for j + 1 (case (i): each of the three
 steps moves one); step t_2 + 1 moves e_j. (R3): read off the list at T = last, as in the frozen l. 203-204, 216-217, 256-257. ∎
Where each frozen sentence reads the part below unit j (complete; where the frozen proof cites (H2), it is one of these two bits):
| frozen lines | step τ | key input C_(j−1)((s_(τ−1))⁺), used for | value input E_(j−1)(s_(τ−1)), used for |
| --- | --- | --- | --- |
| 207-210 (i), 220-227 (ii) | t | v_j key-enabled | = a by (H1): neither B nor F value-enabled |
| 210-213 (i), 228-231 (ii) | t + 1 | v_j key-disabled | B (case (i)), F (case (ii)) value-enabled |
| 213-217 (i) | t + 2 | u_j key-enabled | EY_j(s_(t+1)) = a; F value-enabled |
| 231-234 (ii) | t + 2, …, t_1 − 1 | v_j key-disabled | F not value-enabled, EY_j = c (so u_j value-disabled) |
| 235-238 | t_1 | v_j key-disabled | B value-enabled |
| 239-247 | t_1 + 1 | u_j key-enabled | Y_j not value-enabled |
| 248-250 | t_1 + 2, …, t_2 − 1 | pair key-disabled | Y_j not value-enabled |
| 251-253 | t_2 | pair key-disabled | Y_j not value-enabled |
| 254-257 | t_2 + 1 | e_j key-enabled, pair key-disabled | Y_j not value-enabled |

**4.6 §7 with LEMMA′ (no change of substance).** Theorem EXP-IDEAL (b): j = 1, a = 0, t = 1, T = last = 2^k − 2. (H1) under s_0 as
frozen (l. 265-267). (H2′_T) holds for EVERY T: for every state s, s⁺(v_0) = 1 (v_0 at 0 moves to 1, at 1 it stays: WIRE's
argument at one state), so C_0(s⁺) = 1 for every state s of the run, and E_0(s_τ) = s_τ(v_0) = 1 for τ ≥ 1 (K1, V1 with (S1)). So
(R1) gives the list of the whole window, (R2) that the run reaches s_(2^k−2), (R3) the last state REST_1(1), REST_i(0) (i ≥ 2); then
(s_(2^k−2))⁺ = s_(2^k−2) by STABLE in step form (4.2) with WIRE, so L(G_k) = 2^k − 2; the stop is «stuck» as frozen. (c) as frozen.
This is REFEREE 36's derivation (REF1 l. 240-242) and REFEREE-2's (REF2 l. 146-149).

**4.7 DATA: direct tests of 4.2-4.5 (experiments/red-b/b6prefix.py, runner run_b6fix.sh → data/b6b/out/prefix_*.out; not to sign).**
This is this lane's DATA. REFEREE 36 tested CAUSAL and LEMMA′ with its own tools (REF1 l. 210-218, 243-256: counters causal, abs,
resp, all 0, with controls) and REFEREE-2 tested its schedule and hypotheses (REF2 §3.3: resp, rest, inp); theirs, not re-run here.
All order bits are read off the simulator (onep.py): C_i(s) = [key_s(v_i) < key_s(u_i)], E_i(s) = [value_s(v_i) > value_s(u_i)];
the list of (R1) is generated recursively from the frozen (i), (ii). The tool's step is s ↦ s⁺, and it writes s_τ for the τ-th
state of the sequence s_0, (s_0)⁺, ((s_0)⁺)⁺, …, also beyond a stop (where the sequence repeats); so its «C_(j−1)(s_τ) = c» is
LEMMA′'s key clause C_(j−1)((s_(τ−1))⁺) = c, and its τ_0 is LEMMA′'s T. Every counter marked «must 0» is 0 on every line; every
control fires. Unit and set are named per block.

(1) The restated lemma at the windows of the recursion (prefix_run.out). Unit: a response window (j, t, a) of the recursion from
(1, 0, 1) (2^(j−1) windows of unit j; 2^(k−1) − 1 per k), resp. a (window, step) pair; set: the run of G_k, k = 3..14 (16,368
windows, 376,836 pairs). Must 0: h1 = windows whose (H1) fails; h2 = (window, τ) with C_(j−1)(s_τ) ≠ c for a τ of the window or
E_(j−1)(s_τ) ≠ c for a τ before its last step; psched = (window, τ_0) where the moves of the units ≥ j in step τ_0 differ from the
list; empty = (window, τ) where the list names no move. Also h2last = windows with E_(j−1) ≠ c under the window's last state
(Remark 2: 0 too, although the lemma does not need it). So at every place where the proof applies the lemma, its hypotheses hold on
the whole window, and (R1), (R2) hold at every T.
```
G_3 mode run ctrl 0 T 6 windows 3 pairs 12 h1 0 h2 0 h2last 0 psched 0 empty 0
G_4 mode run ctrl 0 T 14 windows 7 pairs 40 h1 0 h2 0 h2last 0 psched 0 empty 0
G_5 mode run ctrl 0 T 30 windows 15 pairs 112 h1 0 h2 0 h2last 0 psched 0 empty 0
G_6 mode run ctrl 0 T 62 windows 31 pairs 288 h1 0 h2 0 h2last 0 psched 0 empty 0
G_7 mode run ctrl 0 T 126 windows 63 pairs 704 h1 0 h2 0 h2last 0 psched 0 empty 0
G_8 mode run ctrl 0 T 254 windows 127 pairs 1664 h1 0 h2 0 h2last 0 psched 0 empty 0
G_9 mode run ctrl 0 T 510 windows 255 pairs 3840 h1 0 h2 0 h2last 0 psched 0 empty 0
G_10 mode run ctrl 0 T 1022 windows 511 pairs 8704 h1 0 h2 0 h2last 0 psched 0 empty 0
G_11 mode run ctrl 0 T 2046 windows 1023 pairs 19456 h1 0 h2 0 h2last 0 psched 0 empty 0
G_12 mode run ctrl 0 T 4094 windows 2047 pairs 43008 h1 0 h2 0 h2last 0 psched 0 empty 0
G_13 mode run ctrl 0 T 8190 windows 4095 pairs 94208 h1 0 h2 0 h2last 0 psched 0 empty 0
G_14 mode run ctrl 0 T 16382 windows 8191 pairs 204800 h1 0 h2 0 h2last 0 psched 0 empty 0
```
Control (the list with the two observers of every pair exchanged; psched must fire):
```
G_5 mode run ctrl 2 T 30 windows 15 pairs 112 h1 0 h2 0 h2last 0 psched 89 empty 0
```

(2) EVERY triple, and the frozen wording as a control [E-1] (prefix_all.out). Unit: a triple (j, a, t), 1 ≤ j ≤ k − 1, a ∈ {0, 1},
1 ≤ t ≤ L + 3 with L = L(G_k) (the output's column T), on the sequence s_0, s_1 = (s_0)⁺, s_2 = (s_1)⁺, … continued beyond the
stop (it then repeats s_L); set: k = 3..12 (163,970 triples). Among the triples
with (H1) under s_(t−1): h1only = those with C_(j−1)(s_t) ≠ c, where (H2′_T) fails for every T ≥ t and LEMMA′ claims nothing
(REFEREE 36's triple (1, 1, 2^k − 1) is one of them); windows = those where (H2′_t) holds. Must 0: aviol = (window, τ ≤ τ_0) where
step τ is not a step of the run (τ > L(G_k)) or the moves of the units ≥ j differ from the list. Result: windows = expected =
2^(k−1) − 1 on every line, i.e. the triples at which LEMMA′ applies with T ≥ t are exactly the windows of the recursion, and aviol 0.
```
G_3 mode all ctrl 0 T 6 triples 36 h1only 6 windows 3 expected 3 steps 12 aviol 0
G_4 mode all ctrl 0 T 14 triples 102 h1only 11 windows 7 expected 7 steps 40 aviol 0
G_5 mode all ctrl 0 T 30 triples 264 h1only 20 windows 15 expected 15 steps 112 aviol 0
G_6 mode all ctrl 0 T 62 triples 650 h1only 37 windows 31 expected 31 steps 288 aviol 0
G_7 mode all ctrl 0 T 126 triples 1548 h1only 70 windows 63 expected 63 steps 704 aviol 0
G_8 mode all ctrl 0 T 254 triples 3598 h1only 135 windows 127 expected 127 steps 1664 aviol 0
G_9 mode all ctrl 0 T 510 triples 8208 h1only 264 windows 255 expected 255 steps 3840 aviol 0
G_10 mode all ctrl 0 T 1022 triples 18450 h1only 521 windows 511 expected 511 steps 8704 aviol 0
G_11 mode all ctrl 0 T 2046 triples 40980 h1only 1034 windows 1023 expected 1023 steps 19456 aviol 0
G_12 mode all ctrl 0 T 4094 triples 90134 h1only 2059 windows 2047 expected 2047 steps 43008 aviol 0
```
Control 5, THE LEMMA AS FROZEN: (H1), and (H2) only over the τ ≤ L «that the run reaches»; demanded: the run reaches the window's
last state and the steps are the listed ones. It fails at exactly k − 1 triples per k: REFEREE 36's (1, 1, 2^k − 1) and the triples
(j, 0, 2^k − 1), 2 ≤ j ≤ k − 1 (under the last state every unit is at rest with its input equal to its rest bit, and no τ of the
window is reached). At every other triple where the frozen hypothesis holds the frozen conclusion holds (frozen_hyp_holds −
frozen_conclusion_fails = 2^(k−1) − 1).
```
G_3 mode all ctrl 5 T 6 frozen_hyp_holds 5 frozen_conclusion_fails 2 at(j,a,t) (1,1,7) (2,0,7)
G_4 mode all ctrl 5 T 14 frozen_hyp_holds 10 frozen_conclusion_fails 3 at(j,a,t) (1,1,15) (2,0,15) (3,0,15)
G_5 mode all ctrl 5 T 30 frozen_hyp_holds 19 frozen_conclusion_fails 4 at(j,a,t) (1,1,31) (2,0,31) (3,0,31) (4,0,31)
G_6 mode all ctrl 5 T 62 frozen_hyp_holds 36 frozen_conclusion_fails 5 at(j,a,t) (1,1,63) (2,0,63) (3,0,63) (4,0,63) (5,0,63)
G_7 mode all ctrl 5 T 126 frozen_hyp_holds 69 frozen_conclusion_fails 6 at(j,a,t) (1,1,127) (2,0,127) (3,0,127) (4,0,127) (5,0,127) (6,0,127)
G_8 mode all ctrl 5 T 254 frozen_hyp_holds 134 frozen_conclusion_fails 7 at(j,a,t) (1,1,255) (2,0,255) (3,0,255) (4,0,255) (5,0,255) (6,0,255) (7,0,255)
```

(3) Off the run (prefix_off.out). Unit: every (t, j, a) of a trajectory with (H1) under its state t − 1 and C_(j−1) = c under its
state t; τ_0 := the largest T of the window for which (H2′_T) holds. Set: 400 start states per (k, seed), k = 4..8, seeds 1, 2,
every wire and u_0 at 0, four kinds, a quarter each (a planted rest with a random part below it; a state of the run with 1-3
movers below a unit flipped; the state before a window of the run with 1-2 movers below unit j − 1 flipped; a splice of two states
of the run), each iterated 2^(k+1) + 8 steps: 42,902 windows, 1,089 of them PROPER (τ_0 before the window's last step: the
hypothesis fails inside the window), 346,644 steps checked. Must 0: pviol = (window, τ ≤ τ_0) where the moves of the units ≥ j
differ from the list.
```
G_4 mode off ctrl 0 seed 1 starts 400 cap 40 windows 853 full 838 proper 15 properlen 15 maxproper 1 steps 3545 pviol 0 byunit 12 222 619
G_4 mode off ctrl 0 seed 2 starts 400 cap 40 windows 898 full 883 proper 15 properlen 15 maxproper 1 steps 3692 pviol 0 byunit 12 224 662
G_5 mode off ctrl 0 seed 1 starts 400 cap 72 windows 1552 full 1502 proper 50 properlen 55 maxproper 2 steps 7949 pviol 0 byunit 12 121 418 1001
G_5 mode off ctrl 0 seed 2 starts 400 cap 72 windows 1567 full 1515 proper 52 properlen 59 maxproper 2 steps 8204 pviol 0 byunit 12 138 418 999
G_6 mode off ctrl 0 seed 1 starts 400 cap 136 windows 2943 full 2838 proper 105 properlen 134 maxproper 3 steps 18214 pviol 0 byunit 2 94 325 791 1731
G_6 mode off ctrl 0 seed 2 starts 400 cap 136 windows 3138 full 3034 proper 104 properlen 122 maxproper 3 steps 20067 pviol 0 byunit 9 110 344 832 1843
G_7 mode off ctrl 0 seed 1 starts 400 cap 264 windows 5529 full 5369 proper 160 properlen 199 maxproper 3 steps 43011 pviol 0 byunit 7 85 270 658 1451 3058
G_7 mode off ctrl 0 seed 2 starts 400 cap 264 windows 5451 full 5283 proper 168 properlen 218 maxproper 3 steps 42287 pviol 0 byunit 4 89 264 656 1438 3000
G_8 mode off ctrl 0 seed 1 starts 400 cap 520 windows 10297 full 10122 proper 175 properlen 240 maxproper 4 steps 98265 pviol 0 byunit 9 81 235 575 1270 2651 5476
G_8 mode off ctrl 0 seed 2 starts 400 cap 520 windows 10674 full 10429 proper 245 properlen 320 maxproper 4 steps 101410 pviol 0 byunit 5 88 257 610 1323 2741 5650
```
Controls (first line: ctrl1 = proper windows where the list is demanded one step beyond τ_0 and fails, which is all of them;
second line: observers exchanged, pviol fires):
```
G_6 mode off ctrl 1 seed 1 starts 400 cap 136 windows 2943 full 2838 proper 105 properlen 134 maxproper 3 steps 18214 pviol 0 ctrl1 105 byunit 2 94 325 791 1731
G_6 mode off ctrl 2 seed 1 starts 400 cap 136 windows 2943 full 2838 proper 105 properlen 134 maxproper 3 steps 18214 pviol 14097 byunit 2 94 325 791 1731
```
Honest note: on sequences s, s⁺, (s⁺)⁺, … the proper prefixes are short (at most 4 steps here). A reading, not a statement: the
part below a unit reads the part above only through the end-follower, so it rarely changes an input in the middle of a window.
Block (4) forces such changes.

(4) The lower part disturbed by hand inside a window (prefix_drive.out). Unit: a window (j, t, a) of the run of G_k, started from
the run's own s_(t−1); z_τ := (z′_(τ−1))⁺, where z′_(τ−1) is z_(τ−1) with 1-3 movers below unit j flipped (never a wire, u_0 or a
mover of the units ≥ j) at a random step d of the window and, after it, at every step with probability 0.2; the inputs are
C_(j−1)(z_τ) and E_(j−1)(z′_(τ−1)); τ_0 := the last step up to which they are c. Set: 2,000 windows per (k, seed), k = 4..10,
seeds 1, 2: 28,000 windows, 16,423 proper, the longest proper prefix 888 steps, 190,500 steps checked. Must 0: dviol
= (window, τ ≤ τ_0) where the moves of the units ≥ j differ from the list. This is not a run of G_k: it tests CAUSAL and 4.5's
reading together (the upper part follows the list for as long as the two bits it reads are c, whatever else happens below).
```
G_4 mode drive ctrl 0 seed 1 tries 2000 h1fail 0 windows 2000 full 744 proper 1256 properlen 4209 maxproper 13 steps 7062 dviol 0 byunit 280 542 1178
G_4 mode drive ctrl 0 seed 2 tries 2000 h1fail 0 windows 2000 full 752 proper 1248 properlen 4455 maxproper 13 steps 7395 dviol 0 byunit 297 564 1139
G_5 mode drive ctrl 0 seed 1 tries 2000 h1fail 0 windows 2000 full 831 proper 1169 properlen 5912 maxproper 29 steps 9410 dviol 0 byunit 117 287 518 1078
G_5 mode drive ctrl 0 seed 2 tries 2000 h1fail 0 windows 2000 full 818 proper 1182 properlen 5512 maxproper 29 steps 9095 dviol 0 byunit 122 248 519 1111
G_6 mode drive ctrl 0 seed 1 tries 2000 h1fail 0 windows 2000 full 873 proper 1127 properlen 7257 maxproper 60 steps 11327 dviol 0 byunit 61 137 256 501 1045
G_6 mode drive ctrl 0 seed 2 tries 2000 h1fail 0 windows 2000 full 852 proper 1148 properlen 7959 maxproper 61 steps 12182 dviol 0 byunit 73 139 244 543 1001
G_7 mode drive ctrl 0 seed 1 tries 2000 h1fail 0 windows 2000 full 859 proper 1141 properlen 9850 maxproper 122 steps 14254 dviol 0 byunit 30 62 142 256 518 992
G_7 mode drive ctrl 0 seed 2 tries 2000 h1fail 0 windows 2000 full 850 proper 1150 properlen 9192 maxproper 113 steps 13374 dviol 0 byunit 24 74 120 256 496 1030
G_8 mode drive ctrl 0 seed 1 tries 2000 h1fail 0 windows 2000 full 840 proper 1160 properlen 12198 maxproper 244 steps 16482 dviol 0 byunit 19 36 63 136 258 499 989
G_8 mode drive ctrl 0 seed 2 tries 2000 h1fail 0 windows 2000 full 800 proper 1200 properlen 13071 maxproper 246 steps 16943 dviol 0 byunit 22 41 61 127 240 502 1007
G_9 mode drive ctrl 0 seed 1 tries 2000 h1fail 0 windows 2000 full 850 proper 1150 properlen 12582 maxproper 452 steps 16996 dviol 0 byunit 5 18 35 58 113 228 530 1013
G_9 mode drive ctrl 0 seed 2 tries 2000 h1fail 0 windows 2000 full 817 proper 1183 properlen 15041 maxproper 457 steps 19304 dviol 0 byunit 7 23 39 65 132 242 505 987
G_10 mode drive ctrl 0 seed 1 tries 2000 h1fail 0 windows 2000 full 849 proper 1151 properlen 14150 maxproper 888 steps 18573 dviol 0 byunit 1 6 19 32 66 123 243 503 1007
G_10 mode drive ctrl 0 seed 2 tries 2000 h1fail 0 windows 2000 full 842 proper 1158 properlen 13597 maxproper 457 steps 18103 dviol 0 byunit 1 6 19 29 63 152 255 502 973
```
Controls (first line: ctrl1 = proper windows where the list is demanded at the first step whose input is not (c, c) and fails,
which is all of them; second line: observers exchanged, dviol fires):
```
G_6 mode drive ctrl 1 seed 1 tries 2000 h1fail 0 windows 2000 full 873 proper 1127 properlen 7257 maxproper 60 steps 11327 dviol 0 ctrl1 1127 byunit 61 137 256 501 1045
G_6 mode drive ctrl 2 seed 1 tries 2000 h1fail 0 windows 2000 full 873 proper 1127 properlen 7257 maxproper 60 steps 11327 dviol 9085 byunit 61 137 256 501 1045
```

(5) CAUSAL (prefix_loc.out). Unit: a random state with every wire and u_0 at 0; for each j, 3,000 states whose upper part is
drawn from a pool of 30 and whose lower part is random. Must 0: loc = states whose triple (upper part of s, E_(j−1)(s),
C_(j−1)(s⁺)) was seen before with a DIFFERENT upper part of s⁺. hits = states whose triple was seen before (the test is not
vacuous): 78,534 of 81,000 states, k = 3..8.
```
G_3 mode loc ctrl 0 seed 1 pool 30 states 6000 keys 110 hits 5890 loc 0
G_4 mode loc ctrl 0 seed 1 pool 30 states 9000 keys 224 hits 8776 loc 0
G_5 mode loc ctrl 0 seed 1 pool 30 states 12000 keys 360 hits 11640 loc 0
G_6 mode loc ctrl 0 seed 1 pool 30 states 15000 keys 480 hits 14520 loc 0
G_7 mode loc ctrl 0 seed 1 pool 30 states 18000 keys 584 hits 17416 loc 0
G_8 mode loc ctrl 0 seed 1 pool 30 states 21000 keys 708 hits 20292 loc 0
```
Controls (the triple without C_(j−1)(s⁺), resp. without E_(j−1)(s); loc must fire):
```
G_5 mode loc ctrl 3 seed 1 pool 30 states 12000 keys 210 hits 11790 loc 3262
G_5 mode loc ctrl 4 seed 1 pool 30 states 12000 keys 180 hits 11820 loc 4262
```

(6) STABLE in step form [E-5] (prefix_stable.out). Unit: (state s, unit i, b) with REST_i(b) under s and E_(i−1)(s) = b; set: 6,000
states per k, k = 3..8 (a third from the run, two thirds random with a planted rest; wires and u_0 at 0). Must 0: stviol = cases
with C_(i−1)(s⁺) = b in which a mover of unit i moves (14,698 cases). The frozen one-state reading on the same states, as the
control: onestate_cases = cases with C_(i−1)(s) = b, onestate_moves = those in which a mover of unit i moves all the same.
```
G_3 mode stable ctrl 0 seed 1 states 6000 cases 2014 stviol 0 onestate_cases 3736 onestate_moves 1808
G_4 mode stable ctrl 0 seed 1 states 6000 cases 2311 stviol 0 onestate_cases 4002 onestate_moves 1775
G_5 mode stable ctrl 0 seed 1 states 6000 cases 2474 stviol 0 onestate_cases 4210 onestate_moves 1820
G_6 mode stable ctrl 0 seed 1 states 6000 cases 2486 stviol 0 onestate_cases 4278 onestate_moves 1871
G_7 mode stable ctrl 0 seed 1 states 6000 cases 2719 stviol 0 onestate_cases 4495 onestate_moves 1856
G_8 mode stable ctrl 0 seed 1 states 6000 cases 2694 stviol 0 onestate_cases 4555 onestate_moves 1937
```

(7) The standing assumption [E-4] (prefix_u0.out). Unit: a random state with every wire at 0; 8,000 per k, k = 3..6. Must 0: c0e0 =
states with u_0 at 0 where C_0(s) ≠ s(v_0) or E_0(s) ≠ s(v_0). Control: c0e0_u0free = the same count with u_0 random (the formulas
fail exactly at u_0 on 1 and v_0 on 0: about a quarter of the states).
```
G_3 mode u0 ctrl 0 seed 1 states 8000 c0e0 0 c0e0_u0free 2013
G_4 mode u0 ctrl 0 seed 1 states 8000 c0e0 0 c0e0_u0free 1972
G_5 mode u0 ctrl 0 seed 1 states 8000 c0e0 0 c0e0_u0free 2124
G_6 mode u0 ctrl 0 seed 1 states 8000 c0e0 0 c0e0_u0free 2021
```
REFEREE 36's own counters for E-4 (its DATA, cited, not re-run): [Q REF1 l. 127-128] «random states with wires at 0 and u_0 FREE: K1
980 / 8,000, V1 731 / 8,000, V4 2,331 / 32,977 failures at k = 4 (and K2, K3, V2, V3); with u_0 at 0 and the wires FREE: 0 failures
of every fact.»

(8) EXHAUSTIVE at k = 3 and k = 4 (prefix_exh.out). Set: EVERY state with every wire and u_0 at option 0: 2^9 = 512 states of G_3,
2^16 = 65,536 states of G_4 (G_4 has every kind of unit: bottom, middle with e and Y′, top). Must 0, each over all these states:
c0e0 (as in (7)); loc = states whose triple (upper part of s, E_(j−1)(s), C_(j−1)(s⁺)) has two different upper parts of s⁺,
summed over j: CAUSAL checked as a FUNCTION on all states (lockeys = the number of triples); stviol = STABLE in step form over
ALL its cases (stcases; onestate_cases / onestate_moves: the frozen reading, the control); pviol = the restated lemma with s in the
role of s_(t−1), for every state s and every (j, a) with (H1) under s and C_(j−1)(s⁺) = c, followed along s ↦ s⁺ up to τ_0 (windows
= full + proper; h1only = the (state, j, a) with (H1) at which C_(j−1)(s⁺) ≠ c).
```
G_3 mode exh ctrl 0 states 512 c0e0 0 loc 0 lockeys 576 stcases 24 stviol 0 onestate_cases 48 onestate_moves 26 h1only 7 windows 11 full 8 proper 3 steps 30 pviol 0
G_4 mode exh ctrl 0 states 65536 c0e0 0 loc 0 lockeys 73792 stcases 3200 stviol 0 onestate_cases 6400 onestate_moves 3424 h1only 839 windows 1227 full 560 proper 667 steps 2428 pviol 0
```
Controls (first line: observers exchanged, pviol fires; second line: CAUSAL's triple without C_(j−1)(s⁺), loc fires):
```
G_4 mode exh ctrl 2 states 65536 c0e0 0 loc 0 lockeys 73792 stcases 3200 stviol 0 onestate_cases 6400 onestate_moves 3424 h1only 839 windows 1227 full 560 proper 667 steps 2428 pviol 1192
G_4 mode exh ctrl 3 states 65536 c0e0 0 loc 31712 lockeys 69664 stcases 3200 stviol 0 onestate_cases 6400 onestate_moves 3424 h1only 839 windows 1227 full 560 proper 667 steps 2428 pviol 0
```

## Entry 5 (L-RED-B successor 6, 2026-11-13): wording and records — answers REFEREE-2 41's M-1, W-1, D-1, REFEREE 35's P-2, M-1, M-2, M-3 (pre-check) and REFEREE 36's E-3, E-6 (with its notes O-2, N-1)
Sources: REF2 l. 46-54, 60; PRE l. 327-337; REF1 l. 94-101, 372 and its notes l. 49-54, 360-361 (labels as in the conventions above).
No statement changes. Each item: the referee's words, then the reading that completes or replaces the frozen words.

**5.1 The rank clause and its tie-break (REFEREE-2 M-1; REFEREE 36 E-3).**
[Q REF2 l. 48-53] «The br key is NOT injective for k ≥ 4: every wv_j has the pairs (−(2k + 5), 1), (−(2k + 5), 0) and every wu_j
the pairs (−(2k + 5), 3), (−(2k + 5), 2), so 4k − 14 options share a key with an earlier one» «Fix: add «ties broken by β-id» to §3
and to c6.»

[Q REF1 l. 95-101] «is not a bijection for k ≥ 4: the options (wv_j, 0), 1 ≤ j ≤ k − 2, all have the pair (−(2k + 5), 1), and likewise
(wv_j, 1), (wu_j, 0), (wu_j, 1)» «The Theorem names gk.py build(k), so G_k is well defined; the TEXT of rule R is not. Fix: add
«ties (wire options only) by β-id» to §3 and to c6. The run does not depend on the tie order: `gen` with the reverse tie order
gives a different genome and the same run (revtie_run_differs 0), and `orders` places the wire ranks anywhere.»

READ the frozen l. 98-99 as: br of the β of (x, o) := the rank, among all options, of the TRIPLE (−depth(x), local δ of (x, o),
β-id of (x, o)), a wire counting as depth 2k + 5; ties of the pair are broken by β-id, the smaller β-id getting the smaller rank.
This is what gk.py does (`order = sorted(rawrk, key=lambda b: (rawrk[b], b))`) and how the genomes of record were written. READ
Lemma MEMBER c6 (frozen l. 114-115) as: br is the rank of that triple, which is injective, hence a bijection onto 0..M − 1. The
ties are exactly these: the options (wv_j, 0), 1 ≤ j ≤ k − 2, share one pair, and so do the options (wv_j, 1); the options
(wu_j, 0), 2 ≤ j ≤ k − 2, share one pair, and so do the options (wu_j, 1); no two other options tie (the table gives distinct δ to the non-wire options of one Ξ-depth). That makes 2(k − 3) +
2(k − 4) = 4k − 14 options that share a pair with an earlier one for k ≥ 4, and none for k = 3.
Harmless for every tie-break: br enters the model only through the order of two faces of ONE mover, decided by the β of largest
rank in the symmetric difference of their X-chains. No Ξ-edge ends at a wire (table: every Ξ-target is a u, v, y, ȳ or X), so the β
of a wire option lies in one X-chain only, the one-element chain of that option; it is compared only with the β of the other option
of the same wire, whose δ differs (1 against 0, 3 against 2). So no availability set, hence no step of the run and no line of V0-V4,
depends on how the ties are broken. REFEREE-2 gives the same reason (its l. 79-81) and tested it:
[Q REF2 l. 170-171] «the run with the br ties broken by DECREASING β-id ≠ the run (M-1) | 0 |» «tied br keys per k = 0, 2, 6, 10,
…, 42 (= 4k − 14 for k ≥ 4)»

(REFEREE-2's counter tiebreak, its §3.1, file exp_main.out; cited, not re-run.)
This lane's own counter: b6prefix.py tie → data/b6b/out/brtie.out, k = 3..14 (tied = options that share the pair with an
earlier one, formula = 4k − 14; member2 = [the br of the variant with every tied block REVERSED is a bijection onto
0..M − 1]; must 0: rundiff = [the variant's run differs state by state from the run]):
```
G_3 mode tie ctrl 0 N 11 tied 0 formula 0 changed 0 member2 1 T 6 T2 6 rundiff 0
G_4 mode tie ctrl 0 N 20 tied 2 formula 2 changed 4 member2 1 T 14 T2 14 rundiff 0
G_5 mode tie ctrl 0 N 29 tied 6 formula 6 changed 8 member2 1 T 30 T2 30 rundiff 0
G_6 mode tie ctrl 0 N 38 tied 10 formula 10 changed 12 member2 1 T 62 T2 62 rundiff 0
G_7 mode tie ctrl 0 N 47 tied 14 formula 14 changed 16 member2 1 T 126 T2 126 rundiff 0
G_8 mode tie ctrl 0 N 56 tied 18 formula 18 changed 20 member2 1 T 254 T2 254 rundiff 0
G_9 mode tie ctrl 0 N 65 tied 22 formula 22 changed 24 member2 1 T 510 T2 510 rundiff 0
G_10 mode tie ctrl 0 N 74 tied 26 formula 26 changed 28 member2 1 T 1022 T2 1022 rundiff 0
G_11 mode tie ctrl 0 N 83 tied 30 formula 30 changed 32 member2 1 T 2046 T2 2046 rundiff 0
G_12 mode tie ctrl 0 N 92 tied 34 formula 34 changed 36 member2 1 T 4094 T2 4094 rundiff 0
G_13 mode tie ctrl 0 N 101 tied 38 formula 38 changed 40 member2 1 T 8190 T2 8190 rundiff 0
G_14 mode tie ctrl 0 N 110 tied 42 formula 42 changed 44 member2 1 T 16382 T2 16382 rundiff 0
```

**5.2 «Step t» (REFEREE-2 W-1).**
[Q REF2 l. 54] «§6 never says that «step t» is the IDEAL step s_(t−1) → s_t; (H1), (H2) and the proof use exactly that reading.»

Said once in entry 4, 4.1 (S2): «step τ» is the passage s_(τ−1) → s_τ = (s_(τ−1))⁺; a mover moves at step τ iff s_τ and s_(τ−1)
differ at it; in that step the value bits are read under s_(τ−1) and the key bits under s_τ (S3).

**5.3 §9.7's placeholder (REFEREE-2 D-1; REFEREE 36 E-6).**
[Q REF2 l. 60] «§9.7 is the unfilled placeholder `QUOTESUMMARY` (l. 530).»

[Q REF1 l. 371-372] «The four untagged citations are verbatim in the sources named; «different options at depth d*» is the packet's
own phrase.» «§9.7 is the literal placeholder `QUOTESUMMARY`.»

The text the placeholder stands for is the summary of b6quote.py's output on the frozen packet, data/b6b/out/quote.out (pinned in
data/b6b/SHA1SUMS_b6b, sha1 b20118000a5456610e9303b0e140a4bc53501a6f; re-run by this session from the archives of the frozen §10:
byte-equal). Pasted from that file (its five source lines and its last line; the 27 lines between them are one FOUND line per
quote):
```
source R104P = P-N5-REALIZE.md sha1 067f06b6c67969adf346621b4a92b253491ab2b9
source R117 = RESULTS.trunk.md sha1 eecbd798b81ad431d1b753f5a7f92f3c63e56da1
source TARGET = TARGET.md sha1 a41d5e1a3d251b1e7c345c159651c08d76ad8165
source CLAUDE = CLAUDE.md sha1 1e990915503030bba02722f621767c4563c83c74
source GAPS = GAPS.trunk.md sha1 3fa61e1cf9ce48ab16ee6102c3ee145a7d7e0491
quotes 27 found 27 notfound 0
```
REFEREE-2's own checker found the same 27 quotes verbatim (its §3.6, l. 219-220) and four untagged quotes, of which one is a
verbatim quote of R104's packet without a tag (the frozen §9.2's sentence on r178 / r187; its l. 221-222): it is found in the
source, so nothing is misquoted; a tag is missing there.

**5.4 Level width (REFEREE 35 P-2).**
[Q PRE l. 327-329] «my rebuild has 9 movers on a level for every k ≥ 6 (levels 4..k − 2: u, v, e, wv, wu, y, yb, yp, ypb); 4, 6, 8
for k = 3, 4, 5. No step of R104 / R117 depends on the width, so nothing follows, but a number in the packet should be the measured
one.»

The frozen packet has both numbers: [Q FROZEN l. 41, 566] «its levels have up to 9 movers» «up to 8 movers on a level»

The first is the value for k ≥ 6, the second (relayed in §11) the value at k = 5. Measured (b6prefix.py width →
data/b6b/out/width.out; widths = the number of movers on the levels 0, …, k): 
```
G_3 mode width N 11 levels 4 widths 2 2 3 4 max 4 sum 11
G_4 mode width N 20 levels 5 widths 2 2 4 6 6 max 6 sum 20
G_5 mode width N 29 levels 6 widths 2 2 4 7 8 6 max 8 sum 29
G_6 mode width N 38 levels 7 widths 2 2 4 7 9 8 6 max 9 sum 38
G_7 mode width N 47 levels 8 widths 2 2 4 7 9 9 8 6 max 9 sum 47
G_8 mode width N 56 levels 9 widths 2 2 4 7 9 9 9 8 6 max 9 sum 56
G_9 mode width N 65 levels 10 widths 2 2 4 7 9 9 9 9 8 6 max 9 sum 65
G_10 mode width N 74 levels 11 widths 2 2 4 7 9 9 9 9 9 8 6 max 9 sum 74
G_11 mode width N 83 levels 12 widths 2 2 4 7 9 9 9 9 9 9 8 6 max 9 sum 83
G_12 mode width N 92 levels 13 widths 2 2 4 7 9 9 9 9 9 9 9 8 6 max 9 sum 92
G_13 mode width N 101 levels 14 widths 2 2 4 7 9 9 9 9 9 9 9 9 8 6 max 9 sum 101
G_14 mode width N 110 levels 15 widths 2 2 4 7 9 9 9 9 9 9 9 9 9 8 6 max 9 sum 110
```
Nothing in the packet's proofs uses the width.

**5.5 Which genome is the member, and which sha1 pins are of which file (REFEREE 35 M-1).**
[Q PRE l. 330-333] «The genome «as generated» (gate = 100·level + eps) is NOT in R104's class (clause 6: a bijection onto 0..M − 1,
and Γ(G)'s gate vertices have index N + gate(x, k)). The member is the order-preservingly renumbered genome; the sha1 pins are of the
raw JSON. Lemma MEMBER should name the renumbered genome as the object, and say that the IDEAL run is unchanged (keys compare gate
values only) and that Γ(G), Γ3(G) are built from the renumbered one.»

The pre-check read the rule as relayed at 12:41Z, before the freeze. The frozen packet already has the renumbered genome as its
object: §3 (l. 96-97) defines gate(x, o) as the RANK of 100·lev(x) + ε, a bijection onto 0..M − 1; Lemma MEMBER c5 is about that
gate; §4's last lines (l. 119-121) and §9.1 record the raw files as DATA only (they fail c5 alone; their normalised copies are
byte-equal to the genomes of record: normdiff 0). For the record, explicitly:
- GENOMES OF RECORD (the members; the rule's output, gk.py build(k)): experiments/red-b/data/b6b/G/G_k.json, k = 3..14. Their sha1s
  are the lines `G/G_k.json` of data/b6b/SHA1SUMS_b6b (G_3 fe5b59464d938730eb8e19afff139d983d2c3946, G_4
  fb96a30fc1b8e5935229cad597b5b38604db7b1b, G_8 b293075ce300b23477f3bb6ad694c6577b2c64d2, G_10
  d63509cd3dc6fc735d1452d02d371243963a40ab).
- RAW FILES (gk.py --raw: gate = 100·level + ε; NOT members, DATA only): experiments/red-b/data/b6b/raw/G_k.json. The four sha1s
  the Lead relayed with the rule at 12:41Z, and against which REFEREE 35, REFEREE-2 41, L-RED 70 and L-COMP 22 rebuilt byte-equal
  (by their own reports), are sha1s of these raw files: G_3 cd3cd7e361dfe16482bbe56eb87d3e3decf9e6af, G_4 7a2218bfa94e37f85b3fc60d874030aeba8ca848, G_8
  d3ad8e2e6f202eb17e66d04dad77de1a33e74eb2, G_10 da29d33ecaf20cb777650729e54acb1dad17cfd9 (lines `raw/G_k.json` of SHA1SUMS_b6b).
- GAMES: experiments/red-b/data/b6b/pg/G_k_g3.pg = Γ3 of the genome of record (b6n5.py reads data/b6b/G/G_k.json); sha1s in
  SHA1SUMS_b6b and in the frozen §9.4's column pg_sha1.
- The IDEAL run of a raw file equals that of its genome of record (same order of gate values, and R104's step compares gate values
  only): frozen §9.1, and independently REFEREE-2's counter rawdiff 0 (its l. 169) and REFEREE 35's RENUM 0 (its l. 85-86).
- The pin file of the frozen data is data/b6b/SHA1SUMS_b6b (50 lines; entry 1's pointer correction); entry 1's files are pinned in
  SHA1SUMS_b6b_fixes1, the files of entries 4-5 in SHA1SUMS_b6b_fixes2; check.sh verifies all three.

**5.6 The mover order the games use (REFEREE 35 M-2).**
[Q PRE l. 334-335] «The file's mover order fixes the mover indices and the option order of the β-vertices in Γ(G_k). By REACH3's
proof these never decide; PERM (4 random mover orders per k, k = 3..6) is DATA for it. The packet's DATA should say which mover
order its games use.»

Every genome file and every game of this packet uses the GENERATOR'S order (gk.py build(k), list `names`): mover index x = 0, 1, …
runs through u_0, v_0; u_1, v_1, …, u_(k−1), v_(k−1); e_2, …, e_(k−2); wv_1, …, wv_(k−2); wu_2, …, wu_(k−2); y_1, ȳ_1, …, y_(k−1),
ȳ_(k−1); y′_2, ȳ′_2, …, y′_(k−2), ȳ′_(k−2) (the frozen l. 100-101). The β-id of option o of mover x is 2x + o. In Γ(G_k) and
Γ3(G_k) the mover vertices are 0, …, N − 1 in this order and the β-vertices follow in option order (x, o), as R104's packet
prescribes; REFEREE-2 compared the nine game files index by index with its own builder after renumbering its β block that way:
[Q REF2 l. 65-66] «then my game EQUALS the lane's instance file index by index for k = 3..11, and N5 on that numbering makes the same
run» «The lane's files are right»

No other mover order was run by this lane; REFEREE 35's PERM is its DATA (cited, not re-run).

**5.7 The JSON fields (REFEREE 35 M-3).**
[Q PRE l. 336-337] ««deg» is the scalar 2 in the JSON and «pi», «cyc» of the older genome files are absent: a loader that expects a
list or the old keys must not be reused silently (mine reads `opts` only).»

A file G_k.json is one JSON object with exactly these keys: N (the number of movers); lev (list, lev[x]); deg (the NUMBER 2, not a
list: every mover has two options); opts (list, opts[x][o] = [wt, xt, b]: W-target, Ξ-target, β-id, with −1 for «none» and for X);
gate (list, gate[x][o]); br (list, br[b]); bp (list, bp[b], all 0); start (list, start[x]). There are no keys pi, cyc or names.
This lane's tools read the files through onep.load and use opts, lev, gate, br, bp, start, N only.

**5.8 The other lanes' DATA named in the frozen §9 header, now with their commits (Lead 12:56Z item 3).** The frozen §9 header (l.
299-305) cites three independent rebuilds as relayed by the Lead, not on origin at that time. They are on origin now; I opened
their summary files today (not their code), and cite their numbers as THEIR DATA, not re-run by this lane:
- L-COMP 22, BOX 48: claude/l-comp dc6d831f7c56943a03070a9d268df2388565b438, experiments/comp/box48/README.md (own generator from
  the relayed rule; a C port of the model: T = 2^k − 2 for k = 3..20; N5 by L-COMP's n5b on its own Γ3 builder: 2^k + 1 iterations,
  one fallback, for k = 3..12; Oink 8fbf0a7 --tl and --zlk verify the winners for k = 3..12).
- L-RED 70, R245: claude/l-red c7ed9b8b6af43c4ae94a5fa15571193bc923eedc (first version 706d1ecc), docs/red/R245-kill-Gk.md (own
  generator; the model on two engines for k = 3..12; N5 on its own SPEC engine n5s237 for k = 3..8; verdict SURVIVES; its own list
  of what it does not establish stands).
- REFEREE 35's pre-check (PRE; not a signature): own simulator, L = 2^k − 2 for k = 3..15; N5 on its own builder and engine, 2^k + 1
  iterations with the fallback at transition 2^k − 1, for k = 3..12; its firing control: with the e-indices in reversed gate order
  the run has 6 iterations for k = 3..6.
- REFEREE 36 (REF1 §3-§7): own generator and model for k = 3..14 (its file gkx.py); N5 on its own genome with that lane's builder
  and engine for k = 3..9; the games that builder makes equal this lane's nine frozen files vertex by vertex (its counter PG 0).
- REFEREE-2 41 (REF2 §3): own generator and model for k = 3..16; N5 on its own engine for k = 3..11, the answer checked by four
  solvers (two Zielonka implementations, Oink zlk and tl).
The frozen §9 header counts three N5 engines and three Γ3 builders; with the referees' own stacks there are now five N5 engines
(n5v, n5b, n5s237, the first referee lane's rl_engine, REFEREE-2's r2end) and five Γ3 builders (gamma3.build, this lane's eng3,
own34.build, the first referee lane's gk_gamma3, REFEREE-2's r2end.build), by the lanes' own reports.

**5.9 Two notes of REFEREE 36, recorded; no change.**
[Q REF1 l. 360-361] «for «δ(v_j, ·) > δ(u_j, ·)» my variants keep only δ(v_j, o) > δ(u_j, 1 − o) (what the split case reads), and the
run is still the same.»

(O-2.) The frozen §8 lists orders that SUFFICE for the proof and does not claim that each is needed (entry 1, 9.10: about 40% of
single violations keep the run). The proof's V1 reads the split case, where v_j at o and u_j at 1 − o are compared: that is the
weaker condition REFEREE 36 names. The rule's table has the stronger one; nothing is changed.
[Q REF1 l. 53-54] «So «DEFINITIONS ONLY (no theorem of R104 is used)» is right; MEMBER c8 (acyclic) comes first and makes the X-chains
finite. No circularity.»

(N-1.) The order that the frozen §1 quotes from R104's packet stands there after the word «Hence» of Fact X; the landed line R104
states the same order as the model's definition. The frozen §1's label DEFINITIONS ONLY stays.

## Entry 6 (L-RED-B successor 6, 2026-11-13, written 16:43Z by date -u): N5 itself at k = 13 on one engine — extra DATA, no change to any statement, proof or hypothesis
The Lead allowed k = 13 only as a tracked, resumable job. b6n5.py runs one k as one process (about 27 + 41 minutes at k = 13 by
the ratio of entry 1's timings), which is longer than a container usually lives; so this entry uses experiments/red-b/b6n5ck.py
(committed with entries 2-5): the same game, the same engine 1 (L-NEW's n5v.step in mode spec, from S3 = n5x.start_pair), the same
counters as b6n5.py, with a checkpoint of (σ, τ, the counters) every 100 iterations and a restart from it; engine 2 (L-COMP's
n5b.py) is NOT run by it, because it is one subprocess without a checkpoint. Files: data/b6b/out/n5_k13.out, n5ck_check.out,
n5ck_ctrl.out, n5ck_resume.out and the game data/b6b/pg/G_13_g3.pg, pinned in data/b6b/SHA1SUMS_b6b_fixes3 (checked by check.sh).

### 9.14 The checkpointed driver against the frozen lines (b6n5ck.py → n5ck_check.out, n5ck_ctrl.out, n5ck_resume.out)
- Must-0 counter `ckdiff`, unit (genome, field), set k = 3..8 × the twelve fields N, M, n, T1p, F, mism, its, fb, wrong, nonmover,
  gdiff, pg_sha1: the field of b6n5ck.py's line differs from the frozen line of data/b6b/out/n5.out. Result: 0 of 72.
```
G_3 mode spec ctrl 0 ck 100 N 11 M 22 n 175 T1p 6 F 6 mism 0 its 9 fb 1 wrong 0 nonmover 0 gdiff 0 pg_sha1 fca7a52c49e095d297458c2264664b846c442f8b secs 0.0 resumes 0
G_4 mode spec ctrl 0 ck 100 N 20 M 40 n 310 T1p 14 F 14 mism 0 its 17 fb 1 wrong 0 nonmover 0 gdiff 0 pg_sha1 4a2e89c57ec82362c128074c8be3344fb3c0da61 secs 0.2 resumes 0
G_5 mode spec ctrl 0 ck 100 N 29 M 58 n 445 T1p 30 F 30 mism 0 its 33 fb 1 wrong 0 nonmover 0 gdiff 0 pg_sha1 f145a99c548d3f5489c0aca1552ed6eb96deafc3 secs 0.7 resumes 0
G_6 mode spec ctrl 0 ck 100 N 38 M 76 n 580 T1p 62 F 62 mism 0 its 65 fb 1 wrong 0 nonmover 0 gdiff 0 pg_sha1 b9fea1092df47c2abfefef85bf18511346da7d71 secs 1.8 resumes 0
G_7 mode spec ctrl 0 ck 100 N 47 M 94 n 715 T1p 126 F 126 mism 0 its 129 fb 1 wrong 0 nonmover 0 gdiff 0 pg_sha1 daa0f243aefaaf8cbdd205283f5fc7ce2f3d0f56 secs 5.8 resumes 0
G_8 mode spec ctrl 0 ck 100 N 56 M 112 n 850 T1p 254 F 254 mism 0 its 257 fb 1 wrong 0 nonmover 0 gdiff 0 pg_sha1 924239d911a4c32a32397a7ed5ab2efdacf02fee secs 16.1 resumes 0
```
- Control (B6N5_CTRL=2: the Zielonka answer flipped at vertex 0; `wrong` must fire):
```
G_4 mode spec ctrl 2 ck 100 N 20 M 40 n 310 T1p 14 F 14 mism 0 its 17 fb 1 wrong 1 nonmover 0 gdiff 0 pg_sha1 4a2e89c57ec82362c128074c8be3344fb3c0da61 secs 0.1 resumes 0
```
- Kill and resume: G_9 with a checkpoint every 50 iterations, the process killed twice by a timeout (after 12 s and after a
  further 14 s) and started a third time. Its line (resumes 2) has the frozen line's values in all twelve fields (513 iterations,
  one fallback, pg_sha1 9cece8a782b6212e06a177c0899422ebac6e3b0b):
```
G_9 mode spec ctrl 0 ck 50 N 65 M 130 n 985 T1p 510 F 510 mism 0 its 513 fb 1 wrong 0 nonmover 0 gdiff 0 pg_sha1 9cece8a782b6212e06a177c0899422ebac6e3b0b secs 43.4 resumes 2
```

### 9.15 N5 at k = 13 (b6n5ck.py → n5_k13.out; game data/b6b/pg/G_13_g3.pg)
Command (from the repository root, R = experiments/red-b/work/b6 with the lnew archive of the frozen §10): `B6N5_CK=100 python3
experiments/red-b/b6n5ck.py R/lnew R/pg13 R/ck experiments/red-b/data/b6b/G/G_13.json`. Started 15:41Z as a tracked background
job, ended 16:13:13Z with exit 0, without a restart (resumes 0). Its line:
```
G_13 mode spec ctrl 0 ck 100 N 101 M 202 n 1525 T1p 8190 F 8190 mism 0 its 8193 fb 1 wrong 0 nonmover 0 gdiff 0 pg_sha1 9d887e3bf2e1fa4912c32ee0a1ec4ed14327bf71 secs 1947.2 resumes 0
```
So at k = 13: n = 1,525 = 135·13 − 230; the model's run has 8,190 = 2^13 − 2 steps; N5 (engine 1) makes 8,193 = 2^13 + 1 iterations
with one fallback, after F = 8,190 S4a iterations (the fallback is iteration 8,191 = 2^13 − 1); N5's mover states before the
fallback are the model's states, one by one (mism 0); every winner equals harness Zielonka's (wrong 0); no non-mover Even vertex
and no τ changes before the fallback (nonmover 0); this lane's Γ3 builder and L-NEW's give the same game (gdiff 0). These are the
values Corollary EXP-N5 (at least 8,191 iterations, through R117) and Corollary EXP-N5′ (exactly 8,193, through R124) give for
k = 13 (entries 2, 3): the DATA agrees with them at one more k.
What this does NOT add: 8,193 iterations on 1,525 vertices is above n + m = 3,513 and below n² = 2,325,625, like every measured
run (entry 2 (d)): the dead end still rests on the proof. Not done at k = 13: engine 2; the strategy verifier of entry 1's 9.9;
fit.out and size.out were not regenerated (the residual against 2^k + 1 at k = 13 is 0 by the line itself). The size of the game,
by b6size.py on the file, with its control (m tested against 176k − 299), data/b6b/out/size_k13.out:
```
G_13_g3.pg ctrl 0 k 13 n 1525 m 1988 sizediff 0
G_13_g3.pg ctrl 1 k 13 n 1525 m 1988 sizediff 1
```

## Entry 7 (L-RED-B successor 7, session_01V5yGRVmUNMkUXGRuVH63B8; 2026-11-13, written 19:09Z by date -u): REFEREE-2 42's items F-1 to F-5 (its Addendum 2: the fixes-file check of entries 1-5 and the L41 cross-signature) and REFEREE 36's stage 4 — two readings of entry 4, one of entry 5, the runner run_b6fix.sh repaired, one label, line L-2; no statement, proof, hypothesis or number changes
Conventions as in «Entries 2-5: conventions» above. New labels: REF2B = REFEREE-2 42's Addendum 2 (the fixes-file check of
entries 1-5 at 24f4d436 and the L41 cross-signature), claude/referee-2 f17a2708de653b306eaedf878f6120d2d0b31e06,
docs/referee-2/R2-P-N5-EXP.md (sha1 7128d83e76c675609af3f74c73cb0015c9de2ef3, 549 lines; Addendum 2 is its l. 321-549); REF1D =
REFEREE 36's report with its stage 4, claude/referee 78515253a74a353a829b435d53f4987a8552989a, docs/referee/R-P-N5-EXP.md (sha1
0ec7d605ffd23b31114cdc328d792261a108ced9, 542 lines; stage 4 is its §12, l. 498-542, commits 577e8df9 and 4cf6e1ff; its first 496
lines are the file at 7ca9c2b4 byte for byte); FIX5 = this file as both referees read it, claude/l-red-b
24f4d436a0fea1f62ae736f20f78ff9e84333a90 (entries 1-5: 829 lines, sha1 9dc9179fb08063cd59de25c5d3e16b0f8c693fbd), so a line number
after FIX5 is a line of the signed text. Where a referee's sentence itself carries a tag and a quotation, the quote here is cut
into the pieces before and after it. Quote check of the whole file: b6fixquote.py → data/b6b/out/quote_fixes7.out (the 80 quotes
of entries 1-5 and the 24 of this entry: «quotes 104 found 104 notfound 0»; control, every quote spoiled by one letter, quote_fixes7_ctrl.out:
«quotes 104 found 0 notfound 104»). The frozen packet is not edited (sha1 c0449b17193f19619f33b366096762dfde27d542) and entries 1-6 are byte for byte
what they were (7.6). REFEREE-2's Addendum 3 (claude/referee-2 e643672d, an agreement note of the two reviews) was read and has
no item for this lane beyond F-1 to F-5.

The verdicts this entry answers.

[Q REF2B l. 344-346] «**P-N5-EXP: SIGNED with fixes entries 1-5.** The signature is §0's, with one correction (§A2.1): the statement
of the RESPONSE LEMMA that I sign is entry 4's 4.4 (LEMMA′), not the frozen l. 192-204; STABLE is signed in 4.2's step form. Every
other row of §0 stands as written. Items F-1 to F-5 are wording and tooling; none of them is a condition of the signature except
the reading F-1.»

[Q REF1D l. 522-524] «**Verdict on entry 4: it closes E-1, E-2, E-4, E-5. RESPONSE LEMMA SIGNED as restated in fixes entry 4 (=
LEMMA′ of §5.3 with CAUSAL and STABLE in step form).** Under L41 the lemma is referee-originated in statement, so it also needs
REFEREE-2's independent signature.»

[Q REF1D l. 537-538] «entry 3's **Corollary EXP-N5′, the STATEMENT, is SIGNED AS PROVED-CONDITIONAL on RESULTS R124 and R117 as
landed**»

Stage 4 raises no new item: it closes E-1, E-2, E-4, E-5 by entry 4, notes P-1, E-7, O-1, E-3 and E-6 as taken up by entries
2, 3 and 5, which it read in part (the word-by-word reading is its successor's stage 5), and leaves entry 3's proof text unread.
Nothing to change.
The second signature that L41 asks for is REFEREE-2's (Lead reading L41: a referee-originated proof needs its author's signature
and the other referee's independent one):

[Q REF2B l. 463-465] «Signature (L41: the statements 4.3 and 4.4 are referee-originated, REFEREE 36's; this is the independent
second signature): **REFEREE-2 signs 4.1 (S1)-(S4), 4.2 STABLE, 4.3 CAUSAL, 4.4 LEMMA′ with their proofs (4.2, 4.3, 4.5) and 4.6,
as printed in docs/red-b/P-N5-EXP-fixes.md at claude/l-red-b 24f4d436 (sha1 9dc9179f…), (R3)'s range read as t − 1 ≤ τ < last
(F-1).**»

**7.1 Clause (R3) of LEMMA′ with its range (F-1; a READING of entry 4.4, the one condition of the second signature).**
[Q REF2B l. 442-444] «**F-1 (reading; inherited from the frozen l. 203).** (R3) says» «with no lower end. Read: for t − 1 ≤ τ <
last. Without the lower end it is false (before the first response of unit j ≥ 2 ends, E(j) is at 0, which is not a when a = 1).
The proof uses and proves the window reading (4.5 (3): σ before t_1, resp. t_2). I sign with it.»

The words in question stand in entry 4.4, inside REFEREE 36's LEMMA′ as adopted, and come from the frozen statement:

[Q FIX5 l. 384-385] «For T = last this includes: s_τ(E(j)) = a for τ < last and E(j) moves to c at step last (j ≥ 2), and
REST_j(c), REST_i(0) for i > j under s_last.»

[Q FROZEN l. 203-204] «for j ≥ 2, s_τ(E(j)) = a for τ < t + P_j − 1 and E(j) moves to c at step t + P_j − 1»

Accepted. Neither wording names the lower end of the range. Clause (R3) of 4.4 is to be READ, there and wherever it is cited:

> (R3) For T = last: if j ≥ 2, then s_τ(E(j)) = a for every τ with t − 1 ≤ τ < last, and E(j) moves to c at step last; and (for
> every j) REST_j(c) and REST_i(0) for every i > j hold under s_last.

This is the clause the proof proves and uses; no step of 4.5 changes.
- Proved: (H1) puts E(j) at a under s_(t−1) (REST_j(a) has e_j at a for 2 ≤ j ≤ k − 2, and u_(k−1) = E(k − 1) at a for j = k − 1),
  and by (R1) at T = last the list moves E(j) exactly once in the window, at its last step (case (i): u_j to c at step t + 2 =
  last; case (ii): e_j to c at step t_2 + 1 = last). So s_τ(E(j)) = a exactly for t − 1 ≤ τ ≤ last − 1, and s_last(E(j)) = c.
- Used: only by the proof for unit j − 1, which reads the end-follower of the unit above inside that unit's own window, i.e. at
  states s_τ with t − 1 ≤ τ ≤ last (4.5 (3)-(4): D and Z of unit j − 1 under (s_(T−1))⁺). The frozen proof's words for these two
  uses are [Q FROZEN l. 229] «with s(E(j + 1)) = 0 before step t_1» and [Q FROZEN l. 248-249] «with s(E(j + 1)) = 1 before step
  t_2»
- Without a lower end the clause is false at every window of a unit j ≥ 2 except that unit's first: the responses of one unit
  alternate between a = 0 and a = 1, and until the previous response of unit j ended, E(j) stood at the present c.

DATA, a direct test of the clause as restated (experiments/red-b/b6e7.py r3 → data/b6b/out/e7_r3.out; no archive needed). Unit: a
response window (j, t, a) of the recursion on the run of G_k, resp. a (window, τ) pair; set: k = 3..14, 16,368 windows, 16,356 of
them with j ≥ 2 (windows2). Must 0: r3in = (window with j ≥ 2, τ) with t − 1 ≤ τ < last and s_τ(E(j)) ≠ a; r3move = windows with
j ≥ 2 where E(j) does not move from a to c exactly at step last; r3rest = windows (every j) where REST_j(c) or a REST_i(0), i > j,
fails under s_last; litdiff = [literal ≠ 2^(k−1) − k]. The firing control is the wording without a lower end: literal = windows
with j ≥ 2 where s_τ(E(j)) ≠ a for some τ < t − 1; it is 2^(k−1) − k on every line (every window of a unit j ≥ 2 but its first),
16,278 of the 16,356 in all.
```
G_3 mode r3 ctrl 0 T 6 windows 3 windows2 2 r3in 0 r3move 0 r3rest 0 literal 1 expected 1 litdiff 0
G_4 mode r3 ctrl 0 T 14 windows 7 windows2 6 r3in 0 r3move 0 r3rest 0 literal 4 expected 4 litdiff 0
G_5 mode r3 ctrl 0 T 30 windows 15 windows2 14 r3in 0 r3move 0 r3rest 0 literal 11 expected 11 litdiff 0
G_6 mode r3 ctrl 0 T 62 windows 31 windows2 30 r3in 0 r3move 0 r3rest 0 literal 26 expected 26 litdiff 0
G_7 mode r3 ctrl 0 T 126 windows 63 windows2 62 r3in 0 r3move 0 r3rest 0 literal 57 expected 57 litdiff 0
G_8 mode r3 ctrl 0 T 254 windows 127 windows2 126 r3in 0 r3move 0 r3rest 0 literal 120 expected 120 litdiff 0
G_9 mode r3 ctrl 0 T 510 windows 255 windows2 254 r3in 0 r3move 0 r3rest 0 literal 247 expected 247 litdiff 0
G_10 mode r3 ctrl 0 T 1022 windows 511 windows2 510 r3in 0 r3move 0 r3rest 0 literal 502 expected 502 litdiff 0
G_11 mode r3 ctrl 0 T 2046 windows 1023 windows2 1022 r3in 0 r3move 0 r3rest 0 literal 1013 expected 1013 litdiff 0
G_12 mode r3 ctrl 0 T 4094 windows 2047 windows2 2046 r3in 0 r3move 0 r3rest 0 literal 2036 expected 2036 litdiff 0
G_13 mode r3 ctrl 0 T 8190 windows 4095 windows2 4094 r3in 0 r3move 0 r3rest 0 literal 4083 expected 4083 litdiff 0
G_14 mode r3 ctrl 0 T 16382 windows 8191 windows2 8190 r3in 0 r3move 0 r3rest 0 literal 8178 expected 8178 litdiff 0
```
Second control (B6E7_CTRL=1: the range one step too long, t − 1 ≤ τ ≤ last; r3in fires once per window with j ≥ 2):
```
G_5 mode r3 ctrl 1 T 30 windows 15 windows2 14 r3in 14 r3move 0 r3rest 0 literal 11 expected 11 litdiff 0
G_6 mode r3 ctrl 1 T 62 windows 31 windows2 30 r3in 30 r3move 0 r3rest 0 literal 26 expected 26 litdiff 0
```
REFEREE-2's own counter for the same reading (its DATA, cited, not re-run): r3_u1, 0 of 4,082 windows for k = 3..12 (REF2B l. 483).

**7.2 Which frozen lines of §6's statement stay in force (F-2; wording of 4.0).**
[Q REF2B l. 445-447] «**F-2 (wording).** 4.0 says the frozen statement l. 192-204 is REPLACED by 4.4, and 4.4 then refers to»
«which are frozen l. 195 and l. 197-202 (and P_j, l. 191). So those lines stay as definitions; what is replaced is the frame (H2)
and the conclusion's first and last sentences.»

The sentence of 4.0: [Q FIX5 l. 314-315] «The frozen STATEMENT of the RESPONSE LEMMA (l. 192-204) is REPLACED by 4.4 and the
frozen statement of STABLE (l. 258) by 4.2»

Accepted: that sentence is too coarse. READ it as the following table of the frozen lines 191-204 of docs/red-b/P-N5-EXP.md:

| frozen line | what it holds | after entry 4 |
| --- | --- | --- |
| 191 | P_(k−1) := 3, P_j := 2·P_(j+1) + 1, so P_j = 2^(k+1−j) − 1 | IN FORCE (a definition; LEMMA′'s «last» is written with it) |
| 192 | the head of the lemma: j, a, c := 1 − a, t ≥ 1 | REPLACED by the first sentence of LEMMA′ (the same j, a, c, t; it adds last and T) |
| 193 | (H1) | IN FORCE, unchanged (4.4 says so) |
| 194 | (H2) | REPLACED by (H2′_T) |
| 195, its first sentence | the names F, B (the observers of Y_j) and F′, B′ (of Y′_j) | IN FORCE (a definition: these are «the lemma's F, B, F′, B′» of LEMMA′) |
| 195 from «Then the run reaches», and 196 | the first sentence of the conclusion | REPLACED by the conclusion of LEMMA′: (R1), (R2) |
| 197 | the list (i) | IN FORCE (a definition: «the packet's list (i)»); claimed for the steps t, …, T only |
| 198-202 | the list (ii), with the definitions of t_1 and t_2, its sentence for j = 1 and its sentence that no mover of unit j moves at any other step | IN FORCE (a definition: «the packet's list (ii)», t_1, t_2); claimed for the steps t, …, T only |
| 203-204 | the last sentence of the conclusion («In both cases: …») | REPLACED by (R2) and by (R3) as read in 7.1 |

The first sentence of l. 195 is [Q FROZEN l. 195] «Let F be the observer of Y_j that is on forward under s_(t−1) and B the other
one; F′, B′ the same for Y′_j.»

In l. 198 and l. 200 the two parentheses about unit j + 1 («from REST_(j+1)(0), to the input (1, 1)» and «from REST_(j+1)(1), to
the input (0, 0)») are descriptions in the frozen one-state vocabulary, not moves of the list; in the words of 4.1 (S3) they are
the (H1) and the (H2′_T) of the two inner windows, which 4.5 proves. The frozen statement of STABLE (l. 258) is replaced by 4.2
as 4.0 says; nothing of it stays as a definition.

**7.3 The parenthesis of 5.1 (F-3; wording).**
[Q REF2B l. 384-385] «**F-3 (wording).** The reason given,» «omits y′_j and ȳ′_j, the Ξ-targets of e_j. The claim it supports,
that no Ξ-edge ends at a wire, is true by the table.»

The sentence of 5.1: [Q FIX5 l. 670] «No Ξ-edge ends at a wire (table: every Ξ-target is a u, v, y, ȳ or X)»

Accepted. READ the parenthesis as: (table: every Ξ-target is a u, v, y, ȳ, y′, ȳ′ or X). The row that was left out is that of the
end-followers, [Q FROZEN l. 87] «| e_j | j | 2 ≤ j ≤ k − 2 | u_(j−1) / v_(j−1) | ȳ′_j / y′_j |»

The sentence itself (no Ξ-edge ends at a wire) and what 5.1 draws from it (the β of a wire option lies in one X-chain only, so
the tie-break of the wire ranks is harmless) stand as written. DATA (b6e7.py xt → data/b6b/out/e7_xt.out). Unit: an option of G_k;
set: k = 3..14. kinds = the kinds of movers that are the Ξ-target of some option (yb, yp, ypb are the tool's names for ȳ, y′, ȳ′);
must 0: wiretgt = options whose Ξ-target is a wire, etgt = options whose Ξ-target is an end-follower e_j, ypdiff = [yptgt ≠
2(k − 3)], yptgt = options whose Ξ-target is a y′_j or ȳ′_j (the two options of each e_j).
```
G_3 mode xt ctrl 0 N 11 kinds u v y yb wiretgt 0 etgt 0 yptgt 0 expected 0 ypdiff 0
G_4 mode xt ctrl 0 N 20 kinds u v y yb yp ypb wiretgt 0 etgt 0 yptgt 2 expected 2 ypdiff 0
G_5 mode xt ctrl 0 N 29 kinds u v y yb yp ypb wiretgt 0 etgt 0 yptgt 4 expected 4 ypdiff 0
G_6 mode xt ctrl 0 N 38 kinds u v y yb yp ypb wiretgt 0 etgt 0 yptgt 6 expected 6 ypdiff 0
G_7 mode xt ctrl 0 N 47 kinds u v y yb yp ypb wiretgt 0 etgt 0 yptgt 8 expected 8 ypdiff 0
G_8 mode xt ctrl 0 N 56 kinds u v y yb yp ypb wiretgt 0 etgt 0 yptgt 10 expected 10 ypdiff 0
G_9 mode xt ctrl 0 N 65 kinds u v y yb yp ypb wiretgt 0 etgt 0 yptgt 12 expected 12 ypdiff 0
G_10 mode xt ctrl 0 N 74 kinds u v y yb yp ypb wiretgt 0 etgt 0 yptgt 14 expected 14 ypdiff 0
G_11 mode xt ctrl 0 N 83 kinds u v y yb yp ypb wiretgt 0 etgt 0 yptgt 16 expected 16 ypdiff 0
G_12 mode xt ctrl 0 N 92 kinds u v y yb yp ypb wiretgt 0 etgt 0 yptgt 18 expected 18 ypdiff 0
G_13 mode xt ctrl 0 N 101 kinds u v y yb yp ypb wiretgt 0 etgt 0 yptgt 20 expected 20 ypdiff 0
G_14 mode xt ctrl 0 N 110 kinds u v y yb yp ypb wiretgt 0 etgt 0 yptgt 22 expected 22 ypdiff 0
```
Control (B6E7_CTRL=2: outside = options whose Ξ-target is a mover outside the list of 5.1's parenthesis as it was written; it
fires for every k ≥ 4, and k = 3 has no e_j):
```
G_3 mode xt ctrl 2 N 11 kinds u v y yb wiretgt 0 etgt 0 yptgt 0 expected 0 ypdiff 0 outside 0
G_4 mode xt ctrl 2 N 20 kinds u v y yb yp ypb wiretgt 0 etgt 0 yptgt 2 expected 2 ypdiff 0 outside 2
G_5 mode xt ctrl 2 N 29 kinds u v y yb yp ypb wiretgt 0 etgt 0 yptgt 4 expected 4 ypdiff 0 outside 4
G_6 mode xt ctrl 2 N 38 kinds u v y yb yp ypb wiretgt 0 etgt 0 yptgt 6 expected 6 ypdiff 0 outside 6
```

**7.4 The runner run_b6fix.sh (F-4; tooling; no DATA changes).**
[Q REF2B l. 395-402] «**F-4 (tooling; the same defect in the NEW runner).** experiments/red-b/run_b6fix.sh, added by 24f4d436 as
the runner of 4.7, 5.1 and 5.4's DATA, has no failure count: with the same failing python3 it prints «run_b6fix exh done», exits 0
and leaves an EMPTY prefix_exh.out (T4). run_b6b.sh got `trap 'fail=1' ERR` and `exit $fail` in entry 1; the new runner did not.»
«Ask: the two lines of run_b6b.sh in run_b6fix.sh; CHECKER should compare the files, not trust the runner's exit code.»

Accepted and reproduced (control C1 below). The repair in this commit does more than the two lines, because the two lines alone
were tested first and are not enough here:
- With only the two lines added to the runner of 24f4d436, a stage whose commands all fail exits 1 but still leaves the empty
  output file (control C2); and in the stage ctrl, whose ten commands run in one subshell, a failing command that is not the last
  one is not seen at all: exit 0, «failures 0», and a prefix_ctrl.out of 14 lines instead of 15 (control C3).
- The runner now tests each command where it runs. A command's output goes to a temporary file and reaches the output file only
  if the command exits 0, so a failure leaves no empty or partial file; the ctrl stage replaces prefix_ctrl.out only if all ten
  control commands exit 0; every failure is counted, the last line ends «failures N», and the runner exits 1 if N > 0; an unknown
  stage exits 2. The two lines of run_b6b.sh are there as well, as a backstop for every other command. The stage commands, their
  arguments and their order are those of 24f4d436.

Tests (experiments/red-b/b6fixtest.sh WORKDIR → data/b6b/out/runfix.out; N1-N7 the runner as it is now, each with its expected
values in the script's header; C1-C3 the controls, on the runner of 24f4d436 read with `git show`; E the full run). Every N line
ends «ok 1», every control «fires 1», and the last line is «b6fixtest failed 0»:
```
N1 stage width all-fail: exit failures files = 1 12 0 ok 1
N2 stage exh failing-python3-on-PATH: exit failures files = 1 2 0 ok 1
N3 stage ctrl all-fail: exit failures files = 1 10 0 ok 1
N4 stage ctrl one-middle-control-fails: exit failures files = 1 1 0 ok 1
N5 unknown stage: exit files = 2 0 ok 1
N6 stage width fail, run, run again: exit; exit cmp; exit cmp = 1 0 0 0 0 ok 1
N7 stage width k=5-fails, then run: exit failures lines G_5-lines; exit lines same-lines-as-pin = 1 1 11 0 0 12 0 ok 1
C1 runner of 24f4d436, stage exh failing-python3-on-PATH: exit files bytes = 0 1 0 fires 1
C2 that runner + the two lines only, stage exh failing-python3-on-PATH: lines-added exit files bytes = 2 1 1 0 fires 1
C3 the two-line variant, stage ctrl one-middle-control-fails: exit failures lines pinned-lines differs = 0 0 14 15 1 fires 1
E run_b6fix.sh every: exit failures files = 0 0 11 ok 1
E prefix_run.out sha1 23a7ccc2f6db4e2e5e3a5dff9f6e16f3ef0b08b0 cmp-with-data 0 sha1-equals-pin 1
E prefix_all.out sha1 effd99c4e29ea98feab55e23c826cb4acc23da1a cmp-with-data 0 sha1-equals-pin 1
E prefix_off.out sha1 a8627151bd6de3be4d558b217fd9e95b2e96afdf cmp-with-data 0 sha1-equals-pin 1
E prefix_drive.out sha1 b1b88237aef2a3a305da5bc202bfd3768ec02e21 cmp-with-data 0 sha1-equals-pin 1
E prefix_loc.out sha1 cd8195db9e0aaa65b9dae51eabd155146992d98d cmp-with-data 0 sha1-equals-pin 1
E prefix_stable.out sha1 f6726881228602576942b3c0bb946e22b3657446 cmp-with-data 0 sha1-equals-pin 1
E prefix_exh.out sha1 70d47b4dfb85776a4c95fa8bd947ef8567a0dc5c cmp-with-data 0 sha1-equals-pin 1
E prefix_u0.out sha1 e1273bd394564c98c3447ae012f965094349f7fb cmp-with-data 0 sha1-equals-pin 1
E brtie.out sha1 1bc769568775b902231df2d782929c42569c07f0 cmp-with-data 0 sha1-equals-pin 1
E width.out sha1 414d23efc7511243fabfa12acadb1a2362bfec76 cmp-with-data 0 sha1-equals-pin 1
E prefix_ctrl.out sha1 4b0bb7cc214098e3041c062ea05b467b771a6a5d cmp-with-data 0 sha1-equals-pin 1
b6fixtest failed 0
```
No DATA changes: the lines E are a full run of the repaired runner (`run_b6fix.sh WORKDIR/every every`, exit 0) whose eleven
output files are byte-equal to the pinned files of entries 4-5 (cmp-with-data 0) and have the sha1s of data/b6b/SHA1SUMS_b6b_fixes2
(sha1-equals-pin 1). The pinned files and that pin file are not touched by this commit. As the referee asks, the comparison of
record is of the files, not of an exit code. check.sh now runs one stage of the runner with a failing interpreter (exit 1 and no
file left expected) and once normally (width.out byte-equal to its pinned file expected).

**7.5 The two sentences of entry 2 (a′) (F-5; a remark, no change asked).**
[Q REF2B l. 368-371] «**F-5 (label inside (a′); no change asked).** (a′) has two sentences of different standing. That
IDEAL-ACYC-POLY is false follows from Theorem EXP-IDEAL (b) alone (L(G_k) = 2^k − 2 against N + M = 27k − 48): unconditional. That
QUIET-KEY-1P and SW-POLY of P-N5-KEY1P are false needs that lane packet's Lemma IDEAL-1P to identify T_key and sw with the IDEAL
model's quantities; the entry says so»

[Q REF2B l. 373-374] «A RESULTS line may carry the first sentence as unconditional and not the second; line L-1 does exactly that.»

Recorded, with the labels made explicit. Entry 2 (a′) holds two statements:
- (i) R104's IDEAL-ACYC-POLY is false: UNCONDITIONAL (Theorem EXP-IDEAL (b); R104's definitions only).
- (ii) QUIET-KEY-1P and SW-POLY of L-NEW's packet P-N5-KEY1P are false: CONDITIONAL on that packet's Lemma IDEAL-1P, which
  identifies its T_key and sw with the IDEAL model's L(G) and option changes. That lemma is L-NEW's; it is not proved, used or
  refereed in this packet, and its second review is deferred by REFEREE-2's own account. The words of entry 2 that carry the
  condition are [Q FIX5 l. 187-188] «when T_key and sw are read in R104's IDEAL model, as that packet's Lemma IDEAL-1P reads them»

The lines L-1 and L-2 carry (i) only; neither names QUIET-KEY-1P, SW-POLY or P-N5-KEY1P.

**7.6 Guards, line L-2, pins (records).**
- FROZEN and APPEND-ONLY guards, now in check.sh (experiments/red-b/b6guard.py; files only, no git): the packet has the sha1 of
  its freeze commit; the fixes file still begins, byte for byte, with its text at each landed stage (entry 1 at 06d399c2: 125
  lines; entries 1-5 at 24f4d436: 829 lines, sha1 9dc9179f…; entries 1-6 at 0c8fdf9e: 881 lines, sha1 43a941eb…; entries 1-7 at
  this entry's commit); line L-1 has its sha1. Its line now is «guard frozen 0 prefix 0 of 4 l1 0»; its control (one letter of
  entry 1 changed in memory) gives «guard frozen 0 prefix 4 of 4 l1 0». Both referees checked the same two properties on 24f4d436
  by their own commands (REF2B l. 342; REF1D l. 504-505).
- LINE L-2: docs/red-b/P-N5-EXP-line-L2.txt, built from line L-1 by experiments/red-b/b6line.py (five named replacements, each old
  text occurring exactly once in L-1; undoing them gives L-1 back byte for byte; L-1 is not edited). Items: REFEREE-2's line notes

  [Q REF2B l. 522-527] «(L-a) the gloss «per unit j a block pair u_j, v_j, an end-follower e_j, two wires wv_j, wu_j and two observer
  pairs Y_j, Y′_j» describes the middle units 2 ≤ j ≤ k − 2 only (unit 1 has no e_1, wu_1, Y′_1; unit k − 1 has no e, wire or
  Y′), and §6's UNIT j does not contain the wires, which the same line then counts separately («u_0 and the wires never»);
  (L-b) R117's premises are paraphrased (R117's title line also has «in its two forms», «Lemma R», «and (R1) ruling», «Lemma P1 on
  the dual game»): quote the parenthesis; (L-c) L41 asks for a scope tail naming the referee-originated statements (CAUSAL and
  LEMMA′, REFEREE 36) with both signatures quoted; the second one is the bold sentence of §A2.3.»

  and the Lead's item L-d (N5 at k = 13 from entry 6 into part (3); every measured run is still below n²). L-a: the gloss now says
  which unit has which movers (units 1 and k − 1: four; the others: seven) and puts u_0, v_0 and the wires outside the units, as
  §3's table and §6's definition of UNIT j have them. L-b: R117's premises in the words of its title line (trunk docs/RESULTS.md
  l. 13362). L-c: the L41 scope tail with REFEREE 36's two verdict sentences (stage 1 and stage 4) and REFEREE-2's signature
  sentence. Nothing else differs from L-1: the status phrase, part (1) with IDEAL-ACYC-POLY, the dead-end clause, the non-claims
  and the closing parenthesis are byte for byte those of L-1 (the closing parenthesis still reads «with fixes entries 1-5», the
  set both referees signed; entry 6 is named where its number enters, and this entry changes no statement). The builder's own
  record (data/b6b/out/line_L2_build.out, its last four lines; line_L2_quotes.out: the four quotations inside L-2 found verbatim
  at their commits; controls line_L2_ctrl.out, line_L2_quotes_ctrl.out fire):
```
L-2 bytes 7267 (with its newline) lines 1 pipes 0 sha1 6e047c676e582484fe8eb87891764e8c1a7d9a18
L-2 brackets ( 79 ) 79 [ 0 ] 0 { 0 } 0 « 6 » 6 balanced 1
L-2 checks failed 0
written docs/red-b/P-N5-EXP-line-L2.txt
```
- PINS: the new files of this entry are pinned in data/b6b/SHA1SUMS_b6b_fixes4 (checked by check.sh); the pin files of the frozen
  packet and of entries 1-6 are unchanged.
