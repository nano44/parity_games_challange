# R34: (STEALER-MONO) is FALSE on A_DTL under the stable order datum; the run is complete (L-RED box 7, 17:40Z by date -u; produced on Opus 5.5)
Status: DATA, unrefereed. Target: L-ALG's (STEALER-MONO), GAP-A-M §23a (l-alg e2f7e198), relayed by the Lead 17:21Z: "the
region that holds the stealing vertices of a relevant steal never loses a vertex afterwards in that phase" (216/216 in §23a,
Oink order). It would order the relevant steals and prove (STEAL-ONCE*).

## Instance
experiments/red/carry/instances/stealer_viol_n76.pg (n = 76, sha1 714ecc0f6ad42c70bdd10a94e2a1f7fbf1d3f3c4). Found by
dtl_search.py --fitness root, ROOTFIT=stealer (root/rootfit.py), seed 22002, DTL_ORDER=stable, from carry/instances/fall3_n76.pg
(R31), step 148.

## Evidence (re-run)
- L-ALG experiments/alg/dtl_rootmono.py UNMODIFIED (l-alg e2f7e198), RM_EXCL=1 RM_PREF=1 RM_DV=0:
  - DTL_ORDER=stable: "STEALER-MONO (the stealing region never loses vertices later): FAILS" 3, "...: holds" 14;
    "STOLEN-PERM (the stealing vertices stay in the prefix): holds" 17; "RELEVANT new-steal visits per context": max 3, total
    12, 5 transitions, |G'| 76. No INCOMPLETE line.
  - DTL_ORDER=oink: STEALER-MONO holds 1, STOLEN-PERM holds 1; relevant steals max 1, 4 transitions. No INCOMPLETE line.
- Pinned Oink 8fbf0a7 --dtl --no-single --no-wcwc --no-loops -v: 1 dominion, 47 tangles, 7 iterations, solution verified (33
  strategies). Pinned in experiments/red/check.sh (dtl_flipflop n=76 tangles=47 dominions=1 iterations=7).

## Reading (L-RED)
Under the binding Lead reading L22/L26 the frozen DTL statement covers every order datum, so a failure under the stable
datum refutes (STEALER-MONO) as a statement about A_DTL. (STOLEN-PERM) survives on this instance (17/17). Not traced yet:
which region j loses a vertex after its relevant steal, and at which round/top (successor's first item).
