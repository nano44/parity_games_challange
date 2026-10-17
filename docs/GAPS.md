# Gaps and proof obligations (one owner each)
Severity: blocker | major | minor. Status: open | in-progress | closed. Closed rows move to the closed list.

| id | severity | owner | status | claim | gap |
| --- | --- | --- | --- | --- | --- |
| GAP-A | blocker | L-ALG (L-RED attacks) | open | A_DTL makes polynomially many searches (gauntlet step 4, running time) | (SPP) "searches per phase <= \|G'\|" is DATA only (tight: spp_chain_up_n43); phases <= D+2 and (SPP) => O(n^10(m+n^2)) refereed-signed (R-PROVED2 / R2-PROVED2 (g),(k), comparison pending); every per-context and per-phase potential dead (RESULTS DE9-DE12); L32 reassessment |
| GAP-C | blocker | L-ALG (L-RED attacks) | open | A_DTL is complete: W_p(G') nonempty => search(p) learns or finds a dominion (gauntlet step 4) | KT frame: depth-0 P pieces keep KT given (ACYC) (RESULTS R4); DE13 (kin_viol_n29): (K-in), (K-low), (TW), S-LOW-TIGHT and (KT-STEP-first) at an S piece FALSE, so learning inside W_p in the same search cannot be required; the KT chain no longer reaches Lemma K (GAP-C §18r); surviving DATA targets (MEET) 'learns a tangle meeting D or finds a dominion' and (PHASE-IN) 'it or a later same-player search with the same G\' learns inside D', 0 failures on corpus + 1,800+ union searches per order; (PHASE-IN) is equivalent to phase completeness (run() dtl.cpp 1106-1121, search() 1068; L-RED succ. 5, Lead checked), so the only local statement left is (MEET), now L-RED's target |
| G-S5-6 | major | L-ALG | open | (ACYC): the new part of a Dom(prevV) straddle has no tangle-graph cycle | only open hypothesis of R4; DATA 0 failures (32,026 referee-2 runs, L-ALG 4 x 4,000 climb steps) |
| G-K5 | major | L-ALG | open | DTL-proof K5 (i)/(iii) (lowest region closed unless straddling) | FALSE as written (REFEREE-2, docs/referee-2/R2-PROVED2/k5.pg); corrected form in R2-PROVED2 §3 to be imported; meaning of (alpha) depends on it |

## Closed
| id | severity | owner | status | claim | gap |
| --- | --- | --- | --- | --- | --- |
| G1 | major | L-STRUCT | closed | L4 (first referee OK at l-struct 50dc28b, referee 9bf5301; second referee pending): s^V(n,n) >= n^Omega(lg n) (split G_t vertices per out-letter + CDFJLP Lemma 5.1 in V + Lemma 2(a), d ~ sqrt n) | CDFJLP Lemma 5.1 induction not re-derived in V; REFEREE proposed the route, so an independent second referee must sign; novelty: no published vertex-priority lower bound (L-LIT T6); conversion is a PW p.2 remark; independently derived by REFEREE and L-LIT (Claim R) Closed 2026-10-15: two referee signatures (9bf5301, d76c9e1); remaining gap G-L4-1 (Thm 5.1 black box) recorded in RESULTS R1. |

| G-FDL | minor | L-ALG | closed | First-Difference Lemma (GAP-A-M §21d) | G-h1 (sptl repeat loop 870-874) CLOSED by both referees after comparison (R2-PROVED2 §13.1, R-PROVED2 §C): state (ii)/(iii) on the log with repeated sptl passes deleted; closed 2026-10-17 10:30Z; L-ALG to restate; dtl_fdlcheck.py to drop repeated passes |
| G-Bthr | minor | L-ALG | closed | Lemma B-thr (iii) (GAP-C §3) | Closed 2026-10-17 10:10Z by both referees: F-b3 (branch (b) vacuous, B-thr = (a) always, GAP-beta = (beta-a)); REFEREE-2 G-b1 closed R2-PROVED2 §13.2, signed by REFEREE R-PROVED2 §C5 (88d8e4c) |
