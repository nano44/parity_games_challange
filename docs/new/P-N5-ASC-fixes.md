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
