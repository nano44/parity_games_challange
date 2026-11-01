# N5-UNBLOCK (box 119): inconsistent steps are NOT paid by released blocked edges; they are fed by fresh Ξ-changes, which is XI-CH again
L-NEW successor 43, 2026-10-31 (date -u: after 23:15Z). Lead brief 23:15Z (BOX 119): charge INC (box 118) to the distinct blocked edges
later used × their unblock events (Ξ-changes of the target at a higher key, FUEL-COUNT's form); test it on the L-RED builds where INC ≈
stretch length; if it holds, say whether it relocates onto XI-CH-POLY or avoids the degree factor of L-SI box 60 (KEY-RETURN).
Labels: DEAD, DATA, READING. No count is bounded here. G-N5-TIME stays OPEN. This is not M3 and not a TARGET.md claim.

## 0. Answer
- Definitions as in box 118 (τ-stretch, G_τ, W, IW_k, Is_k, BL_k := IW_k minus Is_k, INC). A switch (y, z) at k is RELEASED if (y, z) was
  blocked at an earlier transition of the same stretch and not used since. An UNBLOCK event of a blocked edge (y, z) at j: (y, z) ∈ BL_j
  and (y, z) ∈ Is_(j+1).
- DEAD at constant 1 (explicit instance): «every inconsistent transition switches at least one released edge» (so INC ≤ released switches).
  - cp_K4 (n 192): INC 43, released switches 9, and 36 inconsistent transitions switch no released edge.
  - The same on every build (table, §1). The ratio INC / released grows along the families: 4.8 (cp_K4, fbA_K4), 5.1 (fbA_K8), 8.9 (suf_K8),
    15.5 (s3quad_K8_m30). That is DATA, not a proof for every constant.
  - Corpus: 8,736 of 12,433 inconsistent transitions switch no released edge.
- So the brief's charge does not cover INC. Most blocked edges are never used: the W-better move stays blocked, as in R167's restart,
  and N5 advances along OTHER, freshly Ξ-improving edges.
- What does pay the steps (DATA, §2): on every L-RED build, every inconsistent transition with a predecessor in its stretch is FRESH-FED. It
  switches some edge (y, z) that was not in Is_(k−1), so Ξ(z) changed at k − 1 (box 113 NEW-FUEL, in P-N5-ROOT, signed by both referees).
  Corpus: 958 of 12,433 are not fresh-fed (concentrated on L-RED's «returns_*» instances).
- Unblock events (DATA): their cause is always a Ξ-change of the target (6,061 target only, 828 target and source, 0 source only, corpus).
  One target change unblocks ≤ 2 edges on every build (FAN 2) and ≤ 10 in the corpus.
- READING, answering the Lead's question:
  - The per-blocked-edge charge fails before the degree-factor question arises.
  - The charge that does hold on the builds is «step k ↦ a Ξ-change of a target at k − 1». It is injective trivially (one per transition),
    so it avoids the degree factor only trivially.
  - It is the relocation onto XI-CH-POLY again: τ-stretch steps ≤ (not fresh-fed steps) + Σ_z XCH(z). That is landed R95 WRUN-EQ's
    direction, not a new handle.

## 1. Table (box119/unblock.py; red.txt; valid / repaired starts of box 116b / 117)
| instance | n | INC | no released switch | released / distinct edges | max releases of one edge | unblocks (target / both) | not fresh-fed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cp_K4 / fbA_K4_m8_m8 | 192 / 136 | 43 | 36 | 9 / 9 | 1 | 9 / 0 | 0 |
| fbA_K8_m8_m8 | 192 | 87 | 72 | 17 / 17 | 1 | 17 / 0 | 0 |
| suf_K8 | 199 | 151 | 136 | 17 / 17 | 1 | 17 / 0 | 0 |
| s3quad_K8_m30 | 479 | 263 | 248 | 17 / 17 | 1 | 17 / 0 | 0 |
| fbg_K4_m6_m24 / K4_m6_m48 | 178 / 250 | 131 / 227 | 111 / 207 | 109 / 34, 205 / 58 | 4 / 4 | 21 / 88, 21 / 184 | 0 |
| fbg_K8_m6_m24 / K12_m6_m24 | 234 / 290 | 263 / 395 | 223 / 335 | 217 / 42, 325 / 50 | 8 / 12 | 41 / 176, 61 / 264 | 0 |
| fb3_K4_m6_m12_m12 | 215 | 140 | 107 | 79 / 26 | 5 | 35 / 44 | 0 |
| switchbestexp_4 / _6 | 110 / 160 | 7 / 8 | 6 / 6 | 12 / 12, 23 / 23 | 1 | 17 / 0, 34 / 0 | 0 |

- On fbg the released edges recur: max releases of one edge is 4 / 8 / 12 at K = 4 / 8 / 12, i.e. K. They are fbg's gates, re-blocked and
  re-released once per outer step. Even counted with multiplicity, released switches (325) stay below INC (395) on fbg_K12.
- Corpus (1,132 runs): INC 12,433, released switches 6,844 (5,842 distinct edges, max 5 per edge), unblocks 6,889, not fresh-fed 958
  (264 runs; max 15 of 93 on returns_ph64).

## 2. Fresh feeding (DATA; READING)
- «Fresh-fed» at k: some switched edge (y, z) of k → k + 1 is not in Is_(k−1). Box 113's NEW-FUEL (packet P-N5-ROOT, signed by both
  referees) then gives Ξ_(k−1)(z) ≠ Ξ_k(z), for k − 1 in the same W-run.
- On every build all inconsistent transitions are fresh-fed. The climb is a front: each step uses an edge that became Ξ-improving at the
  previous step, while the W-better blocked edges wait.
- This is the P-N5-ROOT / FUEL picture (R^fuel ≤ Σ N_F(y, z) ≤ … HC) seen from the gate side. The quantity that counts is the Ξ-changes
  feeding the front (XI-CH). Blocked edges are bystanders.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box119/ (unblock.py, run.sh; outputs red.txt, u_sbcg.txt, u_alt.txt). No new instance (faithfulness of the
  builds: boxes 116b-118).
- FINDINGS:
  - DEAD at constant 1: INC ≤ released switches (cp_K4: 43 inconsistent, 9 released). The ratio grows to 15.5 on s3quad (DATA).
  - DATA: unblocks are always target-caused, fan ≤ 2 on the builds; every inconsistent step on the builds is fresh-fed (NEW-FUEL).
  - READING: the charge that holds is per target Ξ-change, i.e. XI-CH-POLY again. The degree factor is avoided only trivially.
- NEEDS: Lead: next box.
