# Draft RESULTS DE24 (Lead, 2026-10-19 00:12Z by date -u) — DRAFT, not landed; awaits CHECKER C18 re-diff (rev. 00:27Z: C18 E-1..E-3, N-1, N-2)

- DE24 (2026-10-18): five DATA hypotheses toward GAP-A (A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7) are
  FALSE, each in BOTH order data (L22/L26), each found by L-RED successor 9 (box 14) with graded climbs and checked with L-ALG's
  UNMODIFIED tools; each re-run by the Lead (tools at the cited l-alg commit, detached worktree; pinned Oink verified, regions =
  Oink zlk); L-ALG (author) confirmed that the tools for (a), (b) and the (VR-NEW_all) part of (c) compute the statements as written (GAP-A-M §37, docs/alg/DEAD.md, l-alg ad6cd54 +
  e35b0f2). None is a refereed result; R4-R14 are unaffected. 𝒞^1P = 𝒞_0^dist ∪ 𝒞_1^dist: every vertex of the opponent
  q = 1 − C has exactly one successor, and q's priorities are pairwise distinct (GAP-A-M §27b; the instances here have all
  priorities distinct).
  (a) (XCTX@p0) (GAP-A-M §35a, the hypothesis of §33's 𝒞^1P reduction "GAP-A ⇐ (XCTX@p0) ∧ (CHAIN-CHANGE)"): FALSE on
      𝒞^1P. Instance experiments/red/xctx/instances/xctx_viol_n20.pg (sha1 742ba103cdb77cbb20e8d94e99120331568e84cd; n = 20;
      pinned Oink 6 iterations). Even phase, s2 → s3, p0 = 2: N = {12} is covered by piece_{p0}(s0) at the different context
      G′ \ {13,19,18} (same size 17, same signature (3, 17, 4)). b12_core.py @ l-alg 9ab9a3e, CLASS=1 DIST=1: MODE=xcover max
      covered fraction 1.0 at ((0,0),2,2); MODE=core "CORE-ALL violations 1". docs/red/R42-xctx.md §1 (l-red 8f09538).
  (b) (TREE-PIECE⁺) (GAP-A-M §36a: at every consecutive pair of searches whose call sequences differ, some vertex holds a key
      (v, depth, position, ρ, |R|, |V|) it held at no earlier search of the phase): FALSE in two-player games. Instances
      experiments/red/tpp/instances/tpp_viol_n22.pg (sha1 a5088b091cbddad1b62233335649b8088b7d1089; pinned Oink 5 iterations)
      and tpp_viol_n63.pg (sha1 64d0832859a415f8bda8959f35e55bc9520425d9; 8 iterations). b12_ident.py @ l-alg 5eb1b4b: TREE=1
      "without a new key 1"; tp_score with PLUS=1: n22 (1, 0, 3, 5), n63 (1, 0, 6, 8). Obstruction: at depth 1 the key does not
      determine the call's input (R, X); a different parent subgame X repeats the key. Adding X to the key reintroduces (CTX⁺).
      Cannot occur on 𝒞^1P (L-RED Lemma EMPTY-REC, a reading). docs/red/R43-treepiece.md (l-red 313aaae).
  (c) (VR-NEW_all) (GAP-A-M §32-§33a: every chain-changing transition gives some vertex a new full key (v, ρ_j, j, |R_j|, |V_j|))
      and (FD-WITNESS_all) (a new-key vertex in the piece at j* or j* − 1): FALSE on 𝒞^1P and in general. Instance
      experiments/red/xctx/instances/vrall_viol_n20.pg (sha1 ed50585765541988d42aa4fa2b3d97c0b3bb8401; 𝒞^1P; pinned Oink 5
      iterations). b12_pot.py @ l-alg 5eb1b4b (with and without CLASS=1 DIST=1): "K-v-all violations 1"; b12_fdwit.py: no
      new-key vertex at j* nor at j* − 1 for K-v-rV, K-v-rs, K-v-all; b12_core xcover fraction 1.0. Obstruction: a depth-0
      cross-context cover with nothing new below p0. docs/red/R42-xctx.md §5 (l-red 8a81ce9).
  (d) (NO-PRE-a) (GAP-A-M §28c: "a vertex of a tangle that fired at top τ in round r is never a round-r top above τ at the next
      visit"): FALSE (two-player, tied priorities). Instance experiments/red/nopre/instances/nopre_viol_n20.pg (sha1
      9a93a8e24832a2440206658fc0f4fdca63cb1574; pinned Oink 4 iterations). b12_nopre.py @ l-alg 5eb1b4b scan: "PRECONDITION",
      (pre, near, surv, gap, above) stable (1, 2, 6, 4, 6), oink (1, 1, 5, 4, 5). Found by L-ALG's own climb (b12_nopre.py climb,
      seed 51) from L-ALG's near miss nopre_near_n20. NOSTEAL-1P (distinct q-priorities) untouched. docs/red/R44-nopre-and-growth.md.
  Consequence: every known key-based (local no-repetition) route to GAP-A on 𝒞^1P is closed (R44 §3; GAP-A-M §37;
  docs/alg/DEAD.md); in general games the key statements tried so far ((TREE-PIECE⁺), (VR-NEW_V), (VR-NEW_s), (VR-NEW_all))
  and (NO-PRE-a) are false too. Surviving DATA among the statements attacked in box 14 (R44 §1): (CHAIN-CHANGE) on 𝒞^1P,
  which cannot give super-polynomial growth even if false (R44 §3, a reading); also still open: (TOP-CHAIN@R) on 𝒞^1P
  (GAP-A-STATUS §4) and the R14 hypotheses (CTX⁺), (FIRED⁺-R). These are "proof route dead" results, not lower-bound steps (R44 §3): each counterexample repeats a label
  once in a phase of 3-6 searches; NEST ≤ 2 on these instances; the open question is the global (CTX⁺) count. Pinned in
  experiments/red/check.sh: sha1 of all five instances; checker outputs in both orders except b12_fdwit (unpinned) and
  tpp_viol_n63 (sha1 only).
