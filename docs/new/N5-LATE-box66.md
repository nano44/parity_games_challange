# N5-LATE (box 66): late adoptions per edge. A list-update (inversion-potential) import, what it proves, and the boundary obstruction
L-NEW successor 35 (Opus 5.5), D14 / D18, Lead reading L40. Lead's brief 2026-10-30 00:09Z: bound LATE per edge (L-SI's Lemma FRESH-SPLIT,
l-si 94bb55db, docs/si/N5-CUT-box40.md §6) by an argument imported from an area not usually paired with parity games. Written from 00:15Z
(date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Branches fetched at box start: l-si 94bb55db (FRESH-SPLIT), l-red 0393967a (L-RED 31 parked after R125). Read only.
- Tools: experiments/new/box66/latepair.py (own); L-SI's experiments/si/odd/cutsx.py run read-only from a scratch copy (not edited).
- Notation: L-SI box 37 / 40. A PIECE (L-SI's guided stretch / τ*-piece) = a maximal run of states with τ constant whose transitions are
  all S4a steps. W_t := val(σ_t, τ) on G_τ. H_t := σ_t ∪ Iσ_t. BLOCKED at t: W_t(c) ▷ W_t(σ_t v) and (v, c) ∉ Iσ_t (R88). (OPT) = L-SI's
  Lemma OPT-OFF; W-MON = R88 §2; W-SUCC = box 37 §2 (W_t(σ_t v) non-decreasing on an interval of a piece where v is off its own W-cycle).

## 1. The statement aimed at, diffed against FRESH-SPLIT
- FRESH-SPLIT's LATE_R(v, c) = the re-entries of v into c in the λ-run R that are FRESH (no anchor in their piece) and fall in class
  (LATE): W*(c) constant on [a, j], (v, c) blocked at j − 2, v off its own W*-cycle at j − 1 and j.
- Aimed at (T-LATE): for every λ-run R and Even edge (v, c), LATE⁺_R(v, c) ≤ poly(n), where LATE⁺_R(v, c) := the transitions j → j + 1
  of R that are S4a steps with σ_{j+1}(v) = c ≠ σ_j(v) and (v, c) blocked at some earlier state of the same piece (R88's late adoption,
  read on pieces).
- Diff: LATE ⊆ LATE⁺. A FRESH-SPLIT (LATE) re-entry is an S4a step whose edge is blocked at j − 2, in the same piece (j − 2 ≥ a).
  LATE⁺ drops "FRESH", "W*(c) constant" and "v off-cycle". So a bound on LATE⁺ bounds LATE.

## 2. Inside one piece: Lemma LATE-W and Corollary LATE-PIECE (PROVED, lane)
Lemma LATE-W. Let Q be a piece. Let v leave c at s → s + 1 in Q (σ_s(v) = c ≠ σ_{s+1}(v)). Let t′ > s be a state of Q at which (v, c) is
blocked, with v off its own W-cycle at every state of [s + 1, t′]. Then W_{t′}(c) ▷ W_{s+1}(c): W(c) rises strictly between leave and block.
Proof. W_{t′}(c) ▷ W_{t′}(σ_{t′} v) (blocked) ⊵ W_{s+1}(σ_{s+1} v) (W-SUCC on [s + 1, t′]) ⊵ W_{s+1}(c) ((OPT) at s + 1: (v, c) ∈ σ_s ⊆ H_s,
v off-cycle at s + 1). □
- Not to be confused with box 65's DEAD "W-charge" (N5-STRETCH-box64.md §5.4). That one asked for a W-rise of c between the BLOCK and
  the adoption (887 of 1141 have none). LATE-W puts the rise between the previous LEAVE and the block, and it is proved.
Corollary LATE-PIECE. In a piece Q, call a late adoption of (v, c) RE-BLOCKED if (v, c) is blocked at some state after v's previous leave of
c in Q. Then
  #(re-blocked late adoptions of (v, c) in Q) ≤ 1 + WCH_Q(c) + CL_Q(v, c),
with WCH_Q(c) the transitions of Q at which W(c) changes, and CL_Q(v, c) those whose leave-to-block window has v on its own W-cycle.
Proof. Let u_1 < u_2 < … be the re-blocked late adoptions of (v, c) in Q. For i ≥ 2, let s_i be v's leave of c between u_{i−1} and u_i,
and t′_i ∈ (s_i, u_i] a block after it. By LATE-W, W(c) changes in (s_i, t′_i] unless the window has v on-cycle (CL). The windows
(s_i, u_i] are disjoint. □
- Late adoptions that are not re-blocked (their only blocks precede the previous adoption) are ordinary re-entries. They are charged by
  L-SI's W-ENT (box 37 §2): W-paid, silent or CYC. LATE-PIECE's gain over W-ENT: re-blocked late adoptions carry no SIL term.
DATA (latepair.py; 719 games, S3 start, plus mkr and the 8 dual / coupled instances with their start files; 729 games): 1645 late
adoptions; the LATE-W check fired 182 times, 0 violations. Max per (piece, edge): 3 (red/so/instances/so_th_n32). There, cutsx.py counts
38 re-entries, all WPAID, 0 FRESH.

## 3. The import: an inversion potential from online list-update (READING → DEAD as an independent bound)
- Source of the idea: the list-update / move-to-front analysis (Sleator-Tarjan's potential = inversions between two orders). NOT opened
  in this box; it is used only as the template "potential = number of inversions between two orders", not cited for any statement.
- The two orders, per Even v: W (what Even's choice against the fixed τ prefers) and Ξ (what the honest gate admits). A blocked edge (v, c)
  is exactly an INVERSION: W says c beats σ(v), Ξ says it does not. Φ_t := the number of blocked edges at t (≤ m_E).
- What Φ gives (PROVED, lane, by the definitions):
  - A late adoption of (v, c) removes the inversion (v, c): after it, σ(v) = c, and an edge to σ(v) is never blocked.
  - So LATE⁺ ≤ Φ_start + #(inversion creations). Each later late adoption of the same edge needs a re-creation of (v, c).
- Where inversions are created:
  - (a) Inside a piece: by LATE-W, a re-creation of (v, c) after a leave costs a strict W-rise of c (or an on-cycle window). This is
    the W-route: it is charged to WCH(c), the same-frame term already in FRESH-SPLIT's composition.
  - (b) At a piece boundary (an Even S4c fallback or a τ-change): the frame changes. The fallback lowers W (603 of 607 do, box 64 §1.8)
    and a τ-change replaces W^τ by W^{τ′}, so (v, c) can become blocked again with no W-rise of c in any one frame.
- Obstruction (DATA, the instance that kills the import as an independent bound): experiments/n5-exhaustive/instances/b6_xl2_n32.pg
  (sha1 909c737192e3…, n 32, S3 start).
  - latepair.py: one edge is late-adopted 4 times in one λ-run, once in each of 4 pieces; max per (piece, edge) = 1; LATE-W fired once.
  - cutsx.py (FR=1): 10 cuts, all Even fallbacks (CUTRE_T 0); FR_LATE 5; maxFRESHCUT 4.
  - So every repeat comes from a type-(b) re-creation. The potential pays for them only by counting boundaries, i.e. B_vc (L-SI §0).
  - DATA: in 36 of 729 games the max late adoptions per (λ-run, edge) exceeds the max per (piece, edge).
- Verdict: DEAD as a bound on LATE independent of the boundaries. What survives is the exact split (PROVED, lane, LATE-PIECE + the
  potential):
    LATE⁺_R(v, c) ≤ PL_R(v, c) + WCH^pieces_R(c) + CL_R(v, c) + (non-re-blocked ones, charged by W-ENT),
  where PL_R(v, c) := the pieces of R containing a late adoption of (v, c) (≤ 1 + B_vc). For FRESH-SPLIT's own LATE this is sharper:
  FRESH re-entries are ≤ 1 per piece and pair (L-SI §2), so LATE_R(v, c) ≤ PL_R(v, c) ≤ 1 + B_vc with nothing else.
- READING: LATE is not a separate premise of G-N5-TIME. It is the boundary count B_vc restricted to pieces where the edge is re-blocked.
  The remaining lever is the boundaries themselves: Even fallbacks (R56's ρ) and τ-changes (COMPOSE-FREEZE's Odd half).

## 4. The other candidate imports (READING; none measured beyond the remarks)
- Tropical / max-plus LP duality with τ̄ (or σ̄) as a dual certificate. The certificate that defines the gate is σ̄(σ), and inside one
  piece it changes freely (box 64: 2277 σ̄-changes in the 719 longest stretches). A duality argument needs a certificate that moves
  monotonically. Ξ does (R15 (a)), but bounding its rises is the Ξ-route (RISE). No handle found.
- Matroid / submodular exchange. A late adoption is not a single exchange: S4a's arena optimum switches many vertices at once, and
  blocking depends on W and Ξ of two vertices, not on a rank function. No exchange axiom was found to hold. Not pursued.
- Well-quasi-order / Ramsey. These give finiteness, which R15 (c) already gives. A polynomial bound needs a quantitative pattern bound.
  Its natural object here is the sequence of pieces in which (v, c) is re-blocked. That is B_vc again.

## DONE / FINDINGS / NEEDS
- DONE: box66/latepair.py, latepair_all.txt (719), latepair_start.txt (mkr, dual / coupled); cutsx.py run read-only on b6_xl2_n32 and
  so_th_n32; this note.
- FINDINGS:
  (1) PROVED (lane): Lemma LATE-W and Corollary LATE-PIECE. Inside a piece, the repeat re-blocked late adoptions of an edge are W-paid
  (strict W-rise of c between leave and block), with no silent term. DATA: 182 checks, 0 violations.
  (2) DEAD (as an independent bound): the list-update inversion potential. Inversions are re-created for free at piece boundaries.
  Instance b6_xl2_n32: one edge late-adopted 4 times in one λ-run, in 4 pieces separated by Even fallbacks.
  (3) READING: FRESH-SPLIT's LATE_R(v, c) ≤ PL_R(v, c) ≤ 1 + B_vc. So LATE is the boundary count, and the open lever is ρ-POLY (Even
  fallbacks) together with the Odd half (τ-changes).
  (4) READING: tropical duality, matroid exchange and wqo give no handle (§4).
- NEEDS: none from the owner.
