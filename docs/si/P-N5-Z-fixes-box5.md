# Lane corrections to P-N5-Z (data only)
L-SI successor 2 (Opus 5.5, D15/D18). Written 2026-10-24 20:45Z (date -u), at the Lead's request (20:4xZ).
- Object corrected: docs/si/P-N5-Z-box5.md version 1, pinned for review at trunk fba7177, sha1
  a027638f06d18143ed0779290b24f8e5decb8249. It is unchanged; this file does not alter it.
- Scope: every lemma statement and proof in P-N5-Z (§1-§9) is unchanged. Only data and one definition in an OPEN item (§9) change.
- This file is a lane record, not refereed text.

## 1. s_rt32_final is not in 𝒞^1O (affects §10 and §11)
- experiments/si/orlens/instances/s_rt32_final.pg (sha1 93ba6aa3…) has TWO Odd choice vertices, 14 and 28. The box 28 tools that the
  box 4 scripts build on silently took the first one, so s_rt32_final is not evidence for or against anything in the packet.
- Found because it showed Ξ_k ≠ W_k at a vertex of F_k (k = 29, vertex 6), which Lemma G (a) excludes on 𝒞^1O. It is not a
  counterexample to any signed result.
- experiments/si/xing/xclass.py now asserts exactly one Odd choice vertex (l-si 0dcbdd5c).
- Corrected counts:
  - "Named instances" (§11) are 30 files:
    - experiments/si/orlens/instances/*.pg except s_rt32_final (15);
    - experiments/red/xing/instances/fbref_cex_n32 and x31_* (14);
    - experiments/new/box28/instances/oc16_s2.
    Read "31" as "30" in §11's ACT, NOFE and WM items.
  - §10 (U*-DROP): 15 of 15 checks fail on fbref_cex_n32 (901674dc), lev_l_x (6c365ff7), run_x_inr2 (8a5a82a6) and x31_lem_t32
    (60c15284). Drop s_rt32_final from the list (the packet says 19 of 19).
  - §11 GAP: 309 switched R_k → F_k edges at fallbacks with (h), on the 30 named instances and the 7 climb bests, 0 violations
    (the packet says 321, which included s_rt32_final).

## 2. The definition of (C) in §9's OPEN item
- Replace "(C): the number of W-lowering transitions per phase" by: (C) = the number of '+−' reversals per phase whose reversing
  transition is a fallback; a drain of consecutive evicting fallbacks counts once.
- Reason: by WM every W-lowering is a fallback, but W-lowerings can far outnumber the reversals that LV′ needs.
  - L-RED's x32_waves48 (experiments/red/xing/instances) has 19 W-lowerings in one phase and Z = 4.

## 3. Additional WM data (§11)
- L-RED's later files in experiments/red/xing/instances (x32_*, u1t_cex_n32; all in 𝒞^1O): WM 0 violations.
- W-lowerings per longest phase: x32_waves48 19 (Z 4), x32_waves32 9 (Z 10), x32_nest40 1 (Z 2); 0 on the others.

## 4. Referee items (relayed by the Lead 20:5xZ; both reports in, no NOT SIGNED). Lane answers
- Z-1 = N-Z-1 (LV′). Accepted as the intended reading: the runs in §7's proof are maximal runs of ADJACENT crossing transitions with
  the same pure sign, so a '±' transition ends a run.
  - #runs ≤ Z + 1 still holds: each pure-sign change and each '±' adds at most one run, and each is counted once in Z.
  - The bound X ≤ (n − 1)(Z + 1) + Z is unchanged.
  - Read "ignoring '±'" instead, the monotonicity step fails, since a '±' transition can lower |R|.
  - zcount.py's count of Z (it does not reset the previous pure sign at a '±') counts the same events. Its assert is the bound itself.
- Z-2 (REFEREE). Accepted: a one-line second proof of NOFE.
  - At a fallback, a switched F_k → R̄_k edge (y, z) is a gate edge from F. By R21 (c) FBL-N (ii) it is flat for W, with
    y = λ_W(y) = λ_W(z).
  - z ∈ R̄_k, so z's W-play reaches o and then follows o's W-play. Its cycle node y therefore lies on o's W-play, as its cycle node.
  - This also gives the READING in P-N5-Z §4 ("y is a W-cycle node") as a proved statement.
- Z-3 (REFEREE). Accepted, wording. In NOFE's proof, "σ_k y ∈ F_k by (F0)" means: y ∈ F_k and y keeps σ_k(y) as its state-k successor,
  so σ_k(y) ∈ F_k at state k. It is a fact about state k only; no transition is involved.
- N-Z-2 (REFEREE-2). s_rt32_final out of class: §1 above.
