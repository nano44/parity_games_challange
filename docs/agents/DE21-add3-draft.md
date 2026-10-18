# Draft RESULTS DE21 ADDENDUM 3 (Lead, 2026-10-18 10:15Z by date -u) — HELD for CHECKER (successor needed; CHECKER at ~725k)

ADDENDUM 3 (2026-10-18, fixed d): the DE21 kills hold at d = 3. Source: L-ALG succ. 9, docs/alg/GAP-A-M.md §26a-§26d, l-alg
9b86244. lagflat7(D) := lagfam(D) with ids renumbered by (original priority, id), then priority classes merged to {0, 1, 2}
(experiments/alg/fixd_lagcollapse.py D flat7). Instances experiments/alg/instances/lagflat7_d3_D{4,8,16}.pg (sha1 45de9d933756,
60f2df733ffa, 67b2d56b32c6).
- Lead re-run (2026-10-18 ~10:10Z, detached checkout of l-alg 9b86244, pinned Oink @ 8fbf0a7, unmodified dtl_stealdepth.py with
  RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0): regeneration of D = 8 byte-identical; Oink `--dtl --no-single --no-wcwc --no-loops`
  12 / 15 / 23 searches (even 11/14/22, odd 1) at D = 4 / 8 / 16, solution verified (37/57/97 strategies), winners equal to
  `--zlk`; re-steal depth STABLE order 4 / 8 / 16 (max k 3 / 5 / 9); OINK order 4 / 0 / 0 (max k 3 / 0 / 0).
- Consequence: under L26 (a failure under either order datum refutes a statement about A_DTL) the stable order alone makes
  (STEAL-DEPTH_{f(d)}) false for every function f, already at d = 3; by L-ALG's measurement the same holds for (EXIT_{f(d)})
  (max exits D/2 + 1; not re-run by the Lead). Fixing d bounds the call depth of A_DTL (DTL-proof §3(c)) but none of the
  per-context constants. In the Oink order the depth collapses at D ≥ 6-12 because std::sort is unstable on large
  equal-priority classes (the §21b effect); an Oink-order-robust variant is open (routed to L-RED).
- Not a running-time kill: searches grow linearly in D; every total stays polynomial, as for lagfam.
- (rev. 10:32Z) All-distinct priorities as well (L-ALG succ. 9, GAP-A-M §27a, l-alg 6266da9): lagdist(D) := lagfam(D) with
  priorities refined to pairwise distinct (order and parity kept, ties broken by id); instances
  experiments/alg/instances/lagdist_D4.pg (af9b429696a0), _D8 (215e9ce202dd), _D12 (66855da1a880). With no ties the stable and
  Oink orders coincide. Lead re-run (detached l-alg 6266da9): Oink 12 / 16 searches at D = 4 / 8, verified (37/57
  strategies), winners equal to `--zlk`; unmodified dtl_stealdepth.py re-steal depth 4 / 8 (max k 3 / 5) in BOTH orders. So
  (STEAL-DEPTH_c) is false in both order data on games with all-distinct priorities; the relay needs only a total order of
  the region tops. D = 12 not re-run by the Lead.
