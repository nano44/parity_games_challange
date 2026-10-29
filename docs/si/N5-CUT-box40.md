# N5-CUT (box 40): re-entries across cuts. Lemma W-RETURN-G, and the per-pair cut charge B_vc replaced by the FRESH count
L-SI successor 31 (Opus 5.5), D15 / D18, Lead reading L40. Lead's brief 2026-10-29 22:47Z (BOX 40): "the proof side of CONJECTURE
PCH-QUAD-S … (2) Fallbacks and τ-changes per span (G_vc), via R56's ρ and STRETCH-RED's fb_S … Start with (2) if it gives a clean bound
quickly." Working note, unrefereed, not a TARGET.md claim. G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Tool: experiments/si/odd/cuts.py (Even side, plain N5 run, S3 start as in boxes 38-39). Outputs odd/out/cuts_corpus.txt (default
  frame) and odd/out/cuts_corpus_fr.txt (FR=1), 719 games of odd/sbcg.lst, 0 timeouts. Pinned in si/check.sh «box 40».
- Notation as in box 38 / 39: a λ-run R, Even v, target c; leave s → s + 1 (σ_s(v) = c ≠ σ_{s+1}(v)), next re-entry j − 1 → j
  (σ_j(v) = c); the out-window is the states [s + 1, j − 1]. H_t := σ_t ∪ Iσ_t ([S4a]'s arena for Even). W^τ_t := val(σ_t, τ) on G_τ.

## 0. Answer to (2) first (READING, with the arithmetic PROVED lane)
- Box 39's G_vc (pieces of span(v, c) meeting an out-window) is at most B_vc := the transitions inside span(v, c) that are Even S4c
  fallbacks or change τ. The pieces are cut exactly there (§1, Fact CUT).
- Inside a λ-run R every Even fallback is an in-phase fallback (λ_Ξ and τ constant across it), and R's phases are separated by its
  τ-changing transitions. So, with TCH_R := the τ-changing transitions of R and ρ_R := the largest R56 ρ of a phase of R:
  B_vc ≤ TCH_R + (TCH_R + 1)·(1 + (n − 1)(2 + ρ_R))   ([R56] per phase).
- TCH over the whole run is COMPOSE-FREEZE (d)'s count (R89 draft, P-N5-FRAME §2.5): the Odd half, through P^U on unprotected targets.
- So a polynomial G_vc is not an independent lever. It follows from ρ-POLY ∧ the Odd half, and gives nothing those two do not already
  give through STRETCH-RED. There is no clean bound on G_vc from R56 / fb_S alone. This is why §1-§2 shrink the charge instead.

## 1. Lemma W-RETURN-G (PROVED, lane; uses S4a)
- Fact CUT (from SPEC, as in FRAME-τ / SUCC-MON's proofs). Every transition changes σ or τ (R15 (d)). A transition that changes σ is
  either an S4a step (σ_{t+1} = Even's optimum against τ_t in G_{τ_t}|H_t; τ_{t+1} may differ, S4b fires in the same iteration) or an
  Even S4c fallback (then τ_{t+1} = τ_t). An Odd S4c fallback leaves σ unchanged.
- A τ*-PIECE is a maximal run of states [a, b] with τ_t = τ* on it and every transition inside it an S4a step. Its opening boundary
  a − 1 → a (a > 0) is an Even fallback or a τ-changing transition.
- Statement. Let the re-entry j − 1 → j be an S4a step, τ* := τ_{j−1}, [a, j − 1] the τ*-piece containing j − 1, W* := W^{τ*}. Call a
  state q an ANCHOR if max(s, a) ≤ q − 1 ≤ j − 2 and (v, c) ∈ H_{q−1}. If an anchor q exists, v is not its own W*-cycle node at any state
  of [q, j], and W*(c) is constant on [q, j], then W*_j(σ_{j−1} v) = W*_j(c): the re-entry is W*-SILENT.
- Proof. The transitions q − 1 → q, …, j − 1 → j are S4a steps against τ* (all of [q − 1, j − 1] lies in the τ*-piece). Box 37's
  (OPT) = Lemma OPT-OFF and W-MON use only "σ_{t+1} is Even's optimum against τ_t in G_{τ_t}|H_t, and σ_t ⊆ H_t", read in the frame
  τ_t; τ_{t+1} never enters. So they hold for each of these transitions in the frame τ*, including j − 1 → j if τ_j ≠ τ*.
  - W*_q(c) ⊴ W*_q(σ_q v): (OPT) at q, (v, c) ∈ H_{q−1}, v off-cycle at q.
  - W*_q(σ_q v) ⊴ W*_{j−1}(σ_{j−1} v): W-SUCC (box 37 §2) on [q, j − 1].
  - W*_{j−1}(σ_{j−1} v) ⊴ W*_j(σ_{j−1} v): W-MON at j − 1 → j.
  - W*_j(σ_{j−1} v) ⊴ W*_j(c) = W*_j(σ_j v): (OPT) at j with (v, σ_{j−1} v) ∈ σ_{j−1} ⊆ H_{j−1}.
  - The chain starts at W*_q(c) and ends at W*_j(c) = W*_q(c). So every link is an equality. □
- Box 37's W-RETURN is the case q = s + 1 (the leave s itself is an anchor: σ_s(v) = c), τ constant on [s, j]. The new content: the
  anchor may be any later state at which the edge (v, c) is back in the arena, so the charge window need not reach back to the leave,
  and the re-entry transition may change τ.
- Where the premises are needed (DATA, the controls of cuts.py on rise_thin51_n40): an anchor taken before the piece (MUT=nofresh, the
  chain crosses a fallback) fails 16 times; the empty anchor q = j (MUT=off1) fails 92 times. With the stated premises: 0 failures.

## 2. Corollary CUT-CHARGE (PROVED, lane): the per-pair bound with FRESH in place of G_vc
- Classes. Every re-entry of v into c in R is exactly one of:
  - F (at a fallback): the re-entry transition is an Even S4c fallback;
  - FR (FRESH): an S4a re-entry with no anchor;
  - C: an anchor exists (take the smallest q) and v is its own W*-cycle node somewhere on [q, j];
  - P (W-paid): W*(c) changes on [q, j];
  - S (silent): the rest; by Lemma W-RETURN-G, W*_j(σ_{j−1} v) = W*_j(c).
- Statement. ENT_R(v, c) ≤ 1 + FC_R(v, c) + WCH*^span_R(c) + SIL_R(v, c) + CYC_R(v, c), where FC := #F + #FR and WCH*^span_R(c) counts
  the transitions t → t + 1 of span(v, c) at which val(σ_t, τ_t)(c) ≠ val(σ_{t+1}, τ_t)(c) (a change of W(c) read in the frame of t).
- Proof. Consecutive re-entries own the disjoint windows [s + 1, j]; the first entry is the 1. A P re-entry has, inside its own window,
  a transition t → t + 1 (q ≤ t < j) with W*_{t+1}(c) ≠ W*_t(c), and τ_t = τ* there (t ∈ [a, j − 1]). □
- FC ≤ B_vc, and #FR ≤ 1 per τ*-piece and pair:
  - An F re-entry is itself a boundary transition.
  - A FRESH re-entry has a > s: otherwise q − 1 = s is an anchor (s ≤ j − 2 because j − 1 ≥ s + 1). So its window [s + 1, j − 1]
    contains the piece's opening boundary a − 1 → a.
  - The windows are disjoint, so distinct F / FR re-entries of one pair use distinct boundaries.
  - A second re-entry of the same pair in the same piece has its own leave s′ ≥ a as an anchor, so it is never FRESH.
- What a FRESH re-entry is (PROVED, lane, LATE-RISE of R89's packet §3.2): (v, c) ∉ H_t on [a, j − 2] and (v, c) ∈ Iσ_{j−1}. If
  j − 1 > a, then Ξ(c) changes at j − 2 → j − 1 (an ONSET of the edge inside the piece). If j − 1 = a, the edge is taken at the first
  transition after the boundary.
- Comparison with box 39 (READING). Box 39 charged every re-entry whose out-window crosses a cut to that cut (XCUT). CUT-CHARGE charges
  only the anchor-free ones (FR) and those made by the fallback itself (F). An out-window that crosses a cut but has the edge back in
  the arena after the cut is W-charged. The W term is same-frame, so a τ-change does not by itself create a W-change of c.

## 3. DATA (corpus, 719 games, 11,669 re-entries; both frames)
| frame | F (at fallback; at τ-change) | FR (FRESH) | FRESH0 (j − 1 = a) | C | P (W-paid) | S (silent) | VIOL | LRISE_V | XCUT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| default (pieces need τ_j = τ_{j−1}) | 2,363 (1,806 at τ-changing S4a steps) | 4,283 | 503 | 4 | 4,977 | 42 | 0 | 0 | 6,834 |
| FR=1 (§1 as stated) | 557 | 6,031 | 2,209 | 4 | 5,035 | 42 | 0 | 0 | — |
- Lemma W-RETURN-G: 0 failures in both frames. LATE-RISE at FRESH onsets: 0 failures.
- FRESH dominates: 52% of all re-entries are anchor-free (FR=1). The edge (v, c) re-enters the arena after a boundary and is taken
  at once. The S4a filter "keep or take an IMPROVING edge" (Ξ-improving, not W-improving) is what the W-frame cannot see.
- Moving the τ-changing S4a re-entries into the old-τ frame (FR=1) turns 1,806 cut re-entries into 58 W-paid and 1,748 FRESH ones.
- Per pair and λ-run:
  - FC max 4 (b5_os_n40, n 40), largest ratio 0.125 (b5_os_n24);
  - XCUT max 4;
  - B_vc max 25 (njb_reabs65_n48, 0.52n);
  - ENT max 18 (topfix_n10, n 210), largest ratio 0.19 (j5_n16).
  So FC is much smaller than B_vc in data; the cuts that cut a span mostly do not cost an entry.
- rise_thin51_n40 (box 39's kill of PCH^span ≤ WCH^span + O(n)): 8 cut transitions (7 Even fallbacks, 1 τ-change), 125 re-entries =
  14 F + 92 FR + 19 P, 0 silent, FC max 4 per pair.

## 4. CONJECTURE FC-LIN, and composition
- CONJECTURE FC-LIN: FC_R(v, c) ≤ n − 1 for every pair and λ-run. DATA: ≤ 0.125n (4 at n 40); 0 failures.
- Composition (PROVED arithmetic, lane): by CUT-CHARGE, span COMPOSE's sum becomes
  Σ_v SW_R(v) ≤ Σ_{(v, c) ∈ E, ENT_R(v, c) > 0} (1 + FC + WCH*^span(c) + SIL + CYC).
  So G-N5-TIME (Even half per λ-run; the Odd half by the mirror on λ^U-runs) ⇐ FC-LIN (any polynomial) ∧ a polynomial bound on
  min(PCH^span, WCH*^span) per pair (MIN-QUAD in the same-frame W) ∧ SIL, CYC polynomial. Mixing the branches per re-entry is
  allowed: Lemma SPAN's Ξ-charge is valid for every re-entry, so each pair may take whichever of PCH^span or the CUT-CHARGE sum is
  smaller.
- Why FC-LIN is not yet provable (READING). A FRESH re-entry is an arena entry of the edge (v, c), an onset of (v, c) ∈ Iσ (a Ξ-crossing
  of Ξ(c) over Ξ(σ v)). Its count per pair is bounded by the boundaries in the span (≤ B_vc, §0) and by the onsets of the edge; both
  are open. The proof needs a reason why, after a fallback or a τ-change, an Even vertex returns to an edge it left before the
  boundary only O(n) times per λ-run.

## 5. Composition toward G-N5-TIME (one line each)
- §0: G_vc ≤ B_vc ≤ TCH_R + (TCH_R + 1)(1 + (n − 1)(2 + ρ_R)). A polynomial G_vc ⇐ ρ-POLY ∧ the Odd half: no new lever.
- §1: W-RETURN-G frees the W-charge from the cut. It needs only an anchor in the re-entry's own τ*-piece, and works across a τ-change
  at the re-entry.
- §2: per pair, G_vc is replaced by FC (fallback-made + FRESH re-entries). FC ≤ B_vc, ≤ 1 per piece, data ≤ 0.125n.
- §4: G-N5-TIME ⇐ FC-LIN ∧ MIN-QUAD (same-frame W) ∧ SIL / CYC polynomial; the open piece of (2) is FC-LIN.

## DONE / FINDINGS / NEEDS
- DONE: odd/cuts.py; corpus in two frames (odd/out/cuts_corpus.txt, cuts_corpus_fr.txt); si/check.sh «box 40» (two pins and two
  controls that must fire); this note.
- FINDINGS:
  1. READING: G_vc ≤ B_vc ≤ TCH_R + (TCH_R + 1)(1 + (n − 1)(2 + ρ_R)). A polynomial G_vc needs ρ-POLY ∧ the Odd half: no clean
     independent bound.
  2. PROVED (lane): Lemma W-RETURN-G (anchor in the re-entry's own τ*-piece; τ may change at the re-entry).
  3. PROVED (lane): Corollary CUT-CHARGE, ENT ≤ 1 + FC + WCH*^span + SIL + CYC, FC ≤ B_vc and ≤ 1 per piece.
  4. DATA: 52% of re-entries are FRESH; FC ≤ 4 per pair (0.125n) while B_vc reaches 25 (0.52n); 0 failures of W-RETURN-G.
  5. CONJECTURE FC-LIN (FC ≤ n − 1 per pair per λ-run).
- NEEDS: none from the owner.

## Addendum (after L-RED R123, Lead 22:57Z relay): spanobs_K12_m48
- Pin copied read-only from l-red 11ccc5e4's tree (origin/claude/l-red, experiments/red/span/instances/) to
  experiments/si/odd/inst/red/: spanobs_K12_m48.pg sha1 5384eab66ea4, .start sha1 af48ece49891.
- cuts.py with the .start, both frames (DATA): n 346, 612 iterations, 0 cuts, 98 pairs, 1,077 re-entries, ALL W-paid; FC 0, silent 0,
  CYC 0; W-RETURN-G 0 failures; most entries of one pair 12.
- READING: R123's large span counts (span MAT 482, PCH 502) are P-changes of the observer o. They are not re-entries: ENT per pair is
  ≤ 12 and each one is paid by a same-frame W-change. FC-LIN and CUT-CHARGE are untouched; R123 is a family where Lemma SPAN's Ξ-branch
  is the costly one and the W-branch is cheap (R123: WCH 11 on the pair (e, o)).
- R123 (4)'s equivalence (PCH^span ≤ poly ⇔ G-N5-TIME, given Lemma SPAN and R47) applies to FC-LIN's route as well: FC ≤ ENT, so
  FC-LIN carries content only through its linear exponent.
