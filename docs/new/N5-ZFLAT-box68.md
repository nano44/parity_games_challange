# N5-ZFLAT (box 68): FB-LIN from GAP-MON. Z-flat fallbacks are Ξ-climbs inside a saturated gap; S4a re-openings are paid by W-rises (the WCH ↔ R* circle)
L-NEW successor 35 (Opus 5.5), D14 / D18, Lead reading L40. Lead's brief 2026-10-30 00:43Z (BOX 68: (1) characterise and bound Z-flat
fallbacks; (2) what an S4a step pays to re-open a gap vertex; no new import). Written from ~00:50Z (date -u). Working note, unrefereed,
not a TARGET.md claim. G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Setting and symbols as in N5-FBENERGY-box67.md: phase = (λ_Ξ, τ) constant (R38 (a)); W := val(σ, τ) on G_τ; Z_t := {v : Ξ_t(v) ≠ W_t(v)};
  Lemma GAP-MON (box 67): at a τ-fixed Even fallback, Z_{k+1} ⊆ Z_k and Ξ, W are frozen outside Z_k.
- Tool: experiments/new/box68/zflat.py; alt_all (413 games, box68/run.sh, zflat_alt.txt) + L-RED's fb38_n48, pl130_n40, long121_n40 with
  starts (zflat_red.txt): 416 games, 788 in-phase fallbacks, 7606 in-phase S4a steps.

## 1. Who moves at a fallback: Lemma SW-IN (PROVED, lane)
Let k → k + 1 be a τ-fixed Even fallback, and let v be switched (σ_{k+1}(v) ≠ σ_k(v)), with v off its own Ξ-cycle at k and at k + 1. Then
Ξ_{k+1}(v) ▷ Ξ_k(v), hence v ∈ Z_k.
Proof.
- S4c sets σ_{k+1}(v) = w with (v, w) ∈ Iσ_k, so Ξ_k(w) ▷ Ξ_k(σ_k v) ([S2]).
- Ξ_{k+1} ⊵ Ξ_k pointwise (R15 (a), (d)).
- With v off-cycle, [V1] / [V2] (R17 (a), the prefix facts, as in P-N5-GP §1) give Ξ_{k+1}(v) = v ⊕ Ξ_{k+1}(w) ⊵ v ⊕ Ξ_k(w) ▷ v ⊕ Ξ_k(σ_k v) = Ξ_k(v).
- By GAP-MON, a vertex outside Z_k keeps its Ξ-value. So v ∈ Z_k. □
DATA: 0 switched off-cycle vertices outside Z_k in 788 fallbacks (SWOUT 0).

## 2. (1) Z-flat fallbacks: characterisation, data, obstruction
- Characterisation (PROVED, lane; GAP-MON + SW-IN). A τ-fixed Even fallback is Z-FLAT iff Z_{k+1} = Z_k. Then:
  - every change of σ, Ξ and W is inside Z_k;
  - every switched off-cycle vertex has a strict Ξ-rise;
  - W only falls (box 21 Lemma W);
  - no vertex of Z_k reaches Ξ_{k+1}(v) = W_{k+1}(v).
  So a Z-flat fallback is a strict Ξ-climb at the switched vertices inside a gap that stays open.
- DATA: 56 of 788 fallbacks are Z-flat. 29 of them leave W unchanged everywhere (W-flat), and 27 lower W inside Z.
- The record, nep22f_n64 (alt_all start), has 10 Z-flat fallbacks in one phase.
  - |Z| = 59 of n = 64 at every one of them: the gap is saturated and never closes.
  - Z's vertices have 1 distinct Ξ cycle node and 2 distinct W cycle nodes.
  - Each fallback switches 1-8 vertices of mixed priorities, raises Ξ at 6-39 vertices, and lowers W at 1-25.
  - So the count is NOT a count of priorities or of cycle-node classes (SCCs) of the gap. It is the number of strict Ξ-climbs that
    Even makes inside a fixed gap with fixed cycle nodes, i.e. path-set / length changes of Ξ.
- Obstruction (READING): in a Z-flat fallback, GAP-MON's energy |Z| is saturated, and the only strict progress is a Ξ-rise inside a
  λ-run. Bounding Z-flat fallbacks per phase is therefore bounding Ξ-rises inside Z (R86's RISE / PCH, the Ξ-route). No new handle.
- Instance: experiments/n5-epoch/instances/nep22f_n64.pg (with its alt_all start) shows the saturated gap. Not a kill of FB-LIN
  (f = 10 < n).

## 3. (2) S4a re-openings: Lemma REOPEN-W (PROVED, lane)
Let k → k + 1 be an in-phase S4a transition (not a fallback; τ_{k+1} = τ_k). If v ∉ Z_k and v ∈ Z_{k+1}, then W_{k+1}(v) ▷ W_k(v).
Proof. W_{k+1} ⊵ W_k pointwise (R88 §2 W-MON; also P-N5-FRAME §3.3, GP*-RUN's first bullet: only "τ constant, not a fallback" is
used). Ξ_{k+1} ⊵ Ξ_k (R15 (a), (d)). If W_{k+1}(v) = W_k(v), then Ξ_{k+1}(v) ⊵ Ξ_k(v) = W_k(v) = W_{k+1}(v) ⊵ Ξ_{k+1}(v) (Lemma XW). So
Ξ_{k+1}(v) = W_{k+1}(v), and v ∉ Z_{k+1}. □
Corollary REOPEN-CHARGE (PROVED, lane). In a phase, the re-openings at S4a steps are at most Σ_v WCH^S4a_phase(v), where WCH^S4a_phase(v)
counts the in-phase S4a transitions at which W(v) changes.
DATA: 8532 re-openings in 7606 S4a steps, every one with a strict W-rise of v (REOPNW 0). Worst phase: 234 re-openings against 746
vertex-W-changes (new/box48/out/qpcclimb/scale/best_qpc_nep90_n40_s62, n 80). Max re-openings per phase / n: 3.33.

## 4. Composition, and where it lands (READING)
- Per phase, by GAP-MON:
  - each fallback either shrinks Z by at least 1 or is Z-flat;
  - Z grows only at S4a steps (re-openings), and at the phase start.
  So f ≤ |Z_start| + (re-openings) + (Z-flat fallbacks) ≤ n + Σ_v WCH^S4a_phase(v) + (Z-flat fallbacks).
- Re-openings are W-changes. Per W-run, W-changing transitions are ≤ (n − 1)(R*_T + 1) (R89 GP*-RUN, from R88 FW-R*), and each changes
  W at ≤ n vertices. A phase splits into W-runs at its fallbacks and λ_W-changes. So the re-opening term sits in the same WCH ↔ R*
  circle that L-SI works on (l-si 7079843d box 42; NOT read for this box, cited only as the Lead relays it).
  - This unifies FB-LIN's (2) with L-SI's (c′): a polynomial bound on per-vertex W-changes per phase (equivalently R* per W-run with
    the W-run count) bounds the re-openings.
- Z-flat fallbacks are Ξ-climbs: the Ξ-route (P*), not the W-circle.
- So FB-LIN ⇐ (WCH per vertex per phase poly, the L-SI circle) ∧ (Ξ-climbs in a saturated gap poly, the Ξ-route).
  - The first is shared with (c′). The second is the residue that is specific to FB-LIN.
  - DATA: the second is small (56 in 416 games; 10 in nep22f_n64). The first is large (8532 re-openings).

## DONE / FINDINGS / NEEDS
- DONE: box68/zflat.py, run.sh, zflat_alt.txt (413), zflat_red.txt (3); check.sh "box 68"; this note.
- FINDINGS:
  (1) PROVED (lane): Lemma SW-IN. A fallback switches only gap vertices, each with a strict Ξ-rise. DATA 0 / 788.
  (2) PROVED (lane): characterisation of Z-flat fallbacks (all change inside Z; Ξ climbs, W falls, no gap closes). DATA 56 / 788.
  On nep22f_n64 the gap is saturated (59 / 64) with 1 Ξ cycle node, so the count is neither priorities nor SCCs. It is the Ξ-route.
  (3) PROVED (lane): Lemma REOPEN-W and Corollary REOPEN-CHARGE. An S4a re-opening needs a strict W-rise of v. DATA 8532 / 8532.
  So re-openings land in the WCH ↔ R* circle, unifying FB-LIN's (2) with (c′).
  (4) READING: FB-LIN ⇐ WCH per vertex per phase poly ∧ Ξ-climbs in a saturated gap poly.
- NEEDS: none from the owner.

## Addendum (2026-10-30, REFEREE-2 N-GAP-5 via P-N5-GAP fixes H6)
- "Characterisation" in §2 and FINDINGS (2) is withdrawn: the items are consequences of Z_{k+1} = Z_k, with no converse.
- DATA correction (N-GAP-7, fixes H8): comp54_n80's start file has a non-edge (11 -> 51); without it, 782 fallbacks and 8,442 re-openings (ZF 56 unchanged).
