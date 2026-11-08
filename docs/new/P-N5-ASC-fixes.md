# P-N5-ASC fixes (append-only; the packet docs/new/P-N5-ASC.md stays frozen)

## Fixes entry 1 (L-NEW successor 62; Lead 22:41Z, 22:46Z, 22:48Z: «GO, fixes entry 1, now. One entry»)
- Reports answered:
  - REFEREE 27: docs/referee/R-P-N5-ASC.md at claude/referee 26b2b516 (ALL SIGN; required AS-2, AS-3, AS-D1, AS-D2; optional AS-1, AS-4).
  - REFEREE-2 31: docs/referee-2/R2-P-N5-ASC.md at claude/referee-2 533744a5 (ALL SIGN; required W-1, W-2, D-1, D-2, D-3).
  - L-RED 55 R220: docs/red/R220-asc.md at claude/l-red 68a1f609 (every statement SURVIVES; the [E-LEV] scope item).
- Nothing was REFUSED. The packet (sha1 in asc.pins) is unchanged; where this entry and the packet differ, this entry governs.
- Line: L-1 = docs/new/P-N5-ASC-line-L1.txt (the first line; written by script, with every changed string below applied).

### W-1 (REFEREE-2) = AS-2 + AS-3 (REFEREE 27) + R220's scope item: [E-LEV] is needed for NOUP too. ACCEPTED.
- The three replacements, each old string occurring once in the packet (grep -cF = 1 each, checked by script):
  - §1: «(only for §6 UP-JUMP and UP-B)» → «(only for §6 UP-JUMP, UP-B and NOUP)»;
  - «To sign» table: «UP-JUMP and UP-B under HYPOTHESIS [E-LEV]» → «UP-JUMP, UP-B and NOUP under HYPOTHESIS [E-LEV]»;
  - title: «in particular on genomes with boundedly many upward Ξ-edges (UP-B)» → «in particular, under the e-priority hypothesis
    [E-LEV], on genomes with boundedly many upward Ξ-edges (UP-B)».
- Reason (DATA of others, quoted with their counters; not re-run here):
  - REFEREE-2 control CTRL=elevrev (e-priorities in decreasing level order): «UPB/NOUP fail on 209 of 21,116 plays of U = 0 genomes (up
    to 2 ascents).»; all §3-§5 counters stay 0 under the same control.
  - L-RED R220 (EORD = rev, e-order (−level, gate), still R104's shape): «NOUPC_1 / 2 / 3 have U(G) = 0 and max ascents 2 / 3 / 4, in 120
    / 450 / 280 (t, v) pairs»; witness «NOUPC_1, t 0, v 10»; frozen files claude/l-red 68a1f609 experiments/red/r220/inst/
    NOUPC_{1,2,3}_rev_idealcyc.pg, sha1 82e41194f59fd6c4a4dba6537890dfb797153197, 7ea66452331c4635282cd3a53a35d2a00bd0ef60,
    94db68d5355d8dcf6f9cc50ee251b91b1bb6c060 (L-RED's inst/SHA1SUMS); the run is checked by one route only (L-RED's own.py).
- AS-3: every UP-B / NOUP clause of L-1 carries «under [E-LEV]», and L-1 keeps the scope sentence (D_E,I(v) only, not R, not a running
  time; OVT-DV and IN-BOUND not landed). R220's wording is used for the hypothesis: «the order of Γ(G) as built by
  experiments/new/box189/gamma3.py (and of R104's packet §3.1), not in a landed line».
- §3-§5 (E-MON, CHAIN-DECOMP, SKELETON, HUB-ASC(B), HUB-ASC-G) do not use [E-LEV]; both referees' controls confirm it.

### W-2 (REFEREE-2) = AS-D2 (REFEREE 27): pins. ACCEPTED (add the five).
- experiments/new/box193/asc.pins gains five rows, ../box192/inst/{cR_d2_w8_R22, rd2_d9, rd2_d10, rd3_d7, rf_d5}.json, with the sha1s of
  box192/inst/SHA1SUMS (each checked equal by sha1sum before pinning). §8's claim «sha1 of this packet and of every tool and instance it
  cites» is then true for the instances. The check.sh block «P-N5-ASC» reads asc.pins, so it now checks 27 + 5 + 2 = 34 rows (the two
  more rows: this fixes file and line L-1; the changed asc193.py, check193.sh, check193.out are re-pinned in place).

### D-1 (REFEREE-2) = AS-D1 (REFEREE 27): unit counts. ACCEPTED.
- asc193.py now also prints edomunits, decunits, tmonunits (appended after gfail; no other output changes). The count for upfail is the
  existing «asc» field. Sums over the 13 instances (check193.out):
  - E-DOM part of E-MON's proof: edomfail 0 in 1,892 vertices (units: vertices other than c_W, K0, K3 and the e's);
  - E-MON in its TAIL-MON form: tmonfail 0 in 2,552 (consecutive state pair, W-target or c_W-successor y with Λ(y) fixed) pairs;
  - CHAIN-DECOMP: decfail 0 in 24,818 (state, vertex) pairs with a nonempty e-sequence;
  - UP-JUMP: upfail 0 in 1,956 ascents (the «asc» sum; REFEREE-2's number).
- REFEREE-2's own 46,830 every-vertex E-MON units are its count, not re-run here.

### D-2 (REFEREE-2): «12 instances were run once». ACCEPTED (output committed).
- check193.sh now runs ug193.py on all 13 instances; check193.out holds every line (max ascents ≤ U(G) on all 13: CLR_k8s16 2 ≤ 21,
  FPORT_n2 1 ≤ 4, FPORT_n3 2 ≤ 6, LEAP_k8 2 ≤ 17, RS2 1 ≤ 4, RS2_L8M6 1 ≤ 7, RS3 2 ≤ 6, RSG_K4 1 ≤ 1, cR_d2_w8_R22 3 ≤ 9, rd2_d9 3 ≤ 20,
  rd2_d10 2 ≤ 18, rd3_d7 2 ≤ 17, rf_d5 2 ≤ 8). L-1 states «all 13 instances».

### D-3 (REFEREE-2): M 7 tightness. ACCEPTED (re-run by a check).
- check193.sh now runs chain193.py 6 0 and chain193.py 7 0 (pure Python, 29 s for M 7): «CS(M 7, A 0): max distinct hub chains 29; 2^M
  128; 1 + M(M+1)/2 29». So F_0 tightness M 1-7 is re-run by check193.sh; dp193.c's data/cs_dp.txt is no longer the only source.

### AS-1 (REFEREE 27, optional): F′_0. TAKEN (wording only).
- Corollary HUB-ASC-G's B = 0 case is DESC-POLY on the whole interval I, not §4's proof «word for word» per refined level (that would
  give a factor M² + 3M + 1): τ(x) is monotone on x's active interval, and x is active at both times of each change it is blamed for.
  L-1 says «F′_0 = F_0 (DESC-POLY on the whole interval)».

### AS-4 (REFEREE 27, optional): D_E(v). TAKEN in L-1.
- L-1 defines it: «the number D_E(v) of distinct (Λ_t(v), E_t(v))» over the whole run.

### Not taken (no change asked)
- REFEREE-2 N-1 (levels ≤ M² + 1), N-2 (F in place of F′ inside refined levels): both are sharper constants; the stated ones stay valid.

### Machine checks after this entry
- check193.sh / check193.out: asc193.py's three unit fields; ug193.py on 13 instances; chain193.py M 6 and 7 at A 0. The check.sh block
  «BOX 193 ASC» greps the new rd2_d9 line.
- asc.pins: re-pinned (changed: asc193.py, check193.sh, check193.out; added: the five box192 instances, this fixes file, line L-1).

## Fixes entry 2 (L-NEW successor 62; Lead 00:15Z: «P-N5-ASC fix round 2 … Write fixes entry 2 (append-only) and line L-2 by script»)
- Reports: REFEREE 27 «entry 1 CORRECT and L-1 MATCHES» (claude/referee d4b39be0); REFEREE-2 31 Addendum 2 (claude/referee-2 fcdc16b4,
  docs/referee-2/R2-P-N5-ASC.md): entry 1 CORRECT, «L-1 NOT YET: W-3 and W-4 (DATA rule, wording or counter only; no statement
  changes)». Nothing REFUSED. The packet is unchanged; entry 1 is unchanged; where they differ, this entry governs.
- Line: L-1 (docs/new/P-N5-ASC-line-L1.txt) → L-2 (docs/new/P-N5-ASC-line-L2.txt), written by script. L-2 differs from L-1 by exactly
  two strings, each replaced once: W-3 below, and the source tail «with fixes entry 1» → «with fixes entries 1-2».

### W-3 (REFEREE-2): E-MON unit. ACCEPTED.
- tmonunits counts every successor y of an e-vertex with Λ(y) fixed, c_W included (level-0 e's go to c_W): REFEREE-2 «Σ T = 229 of the
  2,552». Entry 1 already says «W-target or c_W-successor y»; L-1 did not.
- Old (once in L-1): «(consecutive state pair, W-target with Λ fixed) pairs»
- New (in L-2): «(consecutive state pair, W-target or c_W with Λ fixed) pairs»

### W-4 (REFEREE-2): UP-JUMP tested form. ACCEPTED, option (a).
- asc193.py's upfail now also requires the Ξ-step to go STRICTLY up from the β's own mover: a β z on the segment counts only if its
  Ξ-target nxt[z] is a mover with lev(nxt[z]) ≥ la AND lev(nxt[z]) > lev(z's own mover), as UP-JUMP asserts.
- Re-run (check193.sh, 13 instances): upfail 0 in 1,956 ascents (the «asc» sum), so the set is unchanged and L-1's UP-JUMP clause
  stands unchanged in L-2. check193.out is byte-identical (the printed fields did not change); only asc193.py's sha1 changes.
- Second route (REFEREE-2's, not re-run here): full form «0 in 10,751 ascents of all vertices' plays» (r2asc.py,
  docs/referee-2/R2-P-N5-ASC/r2asc_inst.out at claude/referee-2 533744a5).

### Machine checks after this entry
- asc.pins: asc193.py and this fixes file re-pinned; line L-2 added (35 rows). check.sh block «P-N5-ASC» unchanged (it reads asc.pins).

## Fixes entry 3 (L-NEW successor 63; Lead 03:30Z: «P-N5-ASC fix round 3, from CHECKER 21 C135 … Write fixes entry 3 (append-only) and docs/new/P-N5-ASC-line-L3.txt by script»)
- Report: CHECKER 21 C135 (claude/checker 0942e8be, docs/checker/C135.md): FAIL E-1 to E-4, «No statement, proof, definition or DATA
  figure changes; E-3 narrows one clause to its signed form.» All four ACCEPTED as written. The packet is unchanged; entries 1-2 are
  unchanged; where they differ, this entry governs.
- Line: L-2 (docs/new/P-N5-ASC-line-L2.txt) → L-3 (docs/new/P-N5-ASC-line-L3.txt), written by experiments/new/box193/mkl3_193.py from
  C135 §5 byte-for-byte (`git show 0942e8be:docs/checker/C135.md`; wrapped lines joined with one space, as C135 §5 says). The script
  asserts that each old string occurs exactly once in L-2, applies R1-R4 in order, and asserts L-3's sha1 = 0012d6710983ec339be8f5d4e051a205cc9207ba
  (5,154 bytes, one line, 122 «(» / 122 «)», no «|»), C135's target. Result: equal.

### E-1 / R1 (R-B): source note. ACCEPTED.
- Old: «; L-NEW successor 61)» → New: «; L-NEW successors 61-62)». Entry 1 (AS-1, AS-4, W-1, unit counts) and entry 2 are successor 62's.

### E-2 / R2 (R-G, L41, Lead ruling): HUB-ASC-G's B = 0 constant. ACCEPTED.
- Old: «; §3-§5 do not use [E-LEV]; DATA, clause by clause» → New: «; §3-§5 do not use [E-LEV]; the proof of record of HUB-ASC-G's B = 0 case
  (F′_0 = F_0, DESC-POLY on the whole interval) is referee-originated (REFEREE R-P-N5-ASC §3 AS-1, restated in P-N5-ASC's fixes entry 1
  AS-1), signed by both referees; DATA, clause by clause».
- Reason (C135 E-2): the packet's «§4's proof applies word for word» (l. 160) gives a factor M² + 3M + 1 at B = 0; F′_0 = F_0 is AS-1's
  argument (entry 1 AS-1).

### E-3 / R3 (R-R): the READING inside CHAIN-DECOMP's clause. ACCEPTED.
- Old: «so the e-vertices of one Λ-class form one forest whose paths are the sequences seq_t(v)» → New: «hence seq_t(v) = (f, seq_t(y_f))»,
  the lemma's own signed sentence (packet l. 81 «Hence seq_t(v) = (f, seq_t(y_f)).»). The forest reading (packet l. 89-90) stays in the
  entry body as a proof step of HUB-ASC-G; it is not a line clause.

### E-4 / R4 (R-Q): seq_t(v) and «ascent» defined in the line. ACCEPTED.
- Old: «with E_t(v) the set of e-vertices in Π_t(v),» → New: «with seq_t(v) the e-vertices in Π_t(v) in play order, E_t(v) their set, an
  ascent of seq_t(v) a step to a more relevant element,». Packet l. 52-55: «seq_t(v) := the e-vertices that lie in Π_t(v), in the order
  of the play from v under (σ_t, σ̄_t)»; «An ascent of a sequence (c_1, …, c_p) of distinct items is an index i with c_(i+1) more relevant
  than c_i.»

### Machine checks after this entry
- asc.pins: this fixes file re-pinned; line L-3 and mkl3_193.py added (37 rows). check.sh block «P-N5-ASC» unchanged (it reads asc.pins).
- No tool or DATA output changes (check193.out unchanged).

## Fixes entry 4 (L-NEW successor 63; Lead 04:56Z: «P-N5-ASC fix round 4: ONE required string (R5), from REFEREE 28 §E»)
- Report: REFEREE 28, docs/referee/R-P-N5-ASC.md §E at claude/referee 013f821b: L-3 = L-2 + exactly R1-R4 (byte test PASSES), R1-R4
  CORRECT; «L-3 does NOT YET MATCH the packet: R5 is required.» ACCEPTED. The packet is unchanged; entries 1-3 are unchanged; where they
  differ, this entry governs.
- The finding: the line's CHAIN-DECOMP hypothesis «if the first e-vertex on v's play is f» is weaker than the packet's l. 80 «If seq_t(v)
  = (f, …), then …» (which needs f ∈ Π_t(v)) and false as worded: at v = e_g of a level-0 gate the first e-vertex is v itself, its
  successor is c_W (not a mover) and v ∉ Π_t(v). REFEREE's witness: scratch/asc_cd_l0.py, asc_logs/cd_level0.out (RS2 and LEAP_k8, option
  (0, 0)). The signed packet statement is unaffected; the line misstated its hypothesis.
- R5: old «(Lemma CHAIN-DECOMP) if the first e-vertex on v's play is f, then» → new «(Lemma CHAIN-DECOMP) if seq_t(v) = (f, …), i.e. the
  first e-vertex on v's play is f and f ∈ Π_t(v), then».
- Line: L-3 → L-4 (docs/new/P-N5-ASC-line-L4.txt), written by experiments/new/box193/mkl4_193.py: asserts the old string once in L-3 and
  REFEREE's predicted sha1 4017305a34eac21615ba8f172a9b899544d25659 (5,198 B, 125 «(» = 125 «)», one line, no «|»). Result: equal.
- DATA rule: R5 is a statement wording; its witness is REFEREE's asc_cd_l0.py. No tool or DATA output changes.
- asc.pins: this file re-pinned; line L-4 and mkl4_193.py added (39 rows). check.sh block «P-N5-ASC» unchanged.
