# N5-RLV (box 52): the reader-proof cut of W-SPLIT. Arena-relevant σ̄-changes SBCH″, measured. It is quadratic in one phase (comparator graft on R109's topfix)
L-NEW successor 32 (Opus 5.5; D14, D18, Lead reading L40). Lead's word 2026-10-29 13:08Z (message to L-NEW): «from L-SI 25's new Theorem
W-SPLIT (lane; claude/l-si 0ec1ea69, docs/si/N5-FRZ-box29.md): |phase| = FB + LWCH + SBCH′ + Σ |frozen W-phases|, where LWCH ≤ n(n−1)(FB+1) and
SBCH′ counts the σ̄-changes in the phase. SBCH′ is open. DATA up to 2.1n, but reader-inflatable (l121reader_n41: 1.8n). Your item: define the
coarser, READER-PROOF cut, i.e. count only σ̄-changes that are ARENA-RELEVANT (that change the arena or W-choice of some Even vertex). Measure
it on the library, L-SI's corpora, and the R106 / R109 families. Then attempt a polynomial bound or a kill.»
This is a working note. It is unrefereed and not frozen, and it is not a TARGET.md claim. G-N5-TIME stays OPEN.
Labels: PROVED (lane) / CONJECTURE / OPEN / DATA / READING / DEAD. Counts are TRANSITIONS.
Tools: experiments/new/box52/ (rlv.py, graft.py, flippair.py, scale.sh). Logs: box52/*.txt. Instances: box52/out/.
Premises (read at claude/l-si 0ec1ea69, now on trunk): W-SPLIT, W-MON, CN-W of docs/si/N5-FRZ-box29.md §1-§2 (L-SI 25, lane-PROVED,
unrefereed). SPEC S1-S5 (docs/new/N5-ssi-global.md).

## 0. Summary
- Definition (§1). The ARENA-FROZEN cut is greedy. A transition t → t + 1 of a phase is cut if it is an S4c fallback (FB) or a non-fallback
  λ_W-change (LWCH), as in W-SPLIT. It is also cut if Iσ(t + 1) ≠ Ifr(t + 1). Here Ifr is S2's improving-edge rule applied to
  val(σ_{t+1}, σ̄_a), the valuation with Odd's reply FROZEN at the reference state a, and a is the state just after the last cut. These
  RLV cuts are counted by SBCH″. Inside a refined frozen W-phase F every source state u has Iσ(u) = Ifr(u). So F is a run of "N5 with σ̄
  frozen at σ̄_a": S4a reads only σ, τ and Iσ.
- Lemma W-SPLIT″ (PROVED, lane; §1). |P| = FB + LWCH + SBCH″ + Σ_F |F|, with SBCH″ ≤ SBCH′ and #F ≤ FB + LWCH + SBCH″ + 1. An Odd vertex that
  is on no Ξ-play from a successor of an Even vertex never causes an RLV cut. In particular a reader (an Odd vertex with no predecessor)
  never does.
- DATA (§2). On 1,170 library / L-SI phases: SBCH″ ≤ 1.825n (nep92_n40: 73 of its 84 σ̄-changes are relevant), against SBCH′ ≤ 2.100n.
  Readers are removed exactly: l121reader_n41 has SBCH′ 74 and SBCH″ 30, and its reader-free original long121_n40 has SBCH′ 33 and SBCH″ 30.
  On non-reader instances most σ̄-changes ARE relevant. CONJECTURE FW-BF and FW-LEN on the refined cut: 0 failures. R106 runquad and R109
  hntop have σ̄ constant on their long phases, so SBCH′ = SBCH″ = 0 there.
- KILL of the linear form (§3, DATA on a scaling family). The COMPARATOR graft adds three vertices to R109's topfix_N: Odd u → {a, b},
  Even z1 → {u, b}, Even z2 → {u, a}, with no edge from an old vertex into them. (a, b) is the pair whose Ξ-order flips most often. On the
  grafted family SBCH″ = 24, 41, 87, 149, 227, 321 in ONE phase at N = 3, 4, 6, 8, 10, 12 (n = 21N + 3). That is exactly 2N² + 3N − 3,
  Θ(n²), while the old run is unchanged. So "SBCH″ = O(n) per phase" is FALSE. Polynomial is untouched: the phase is itself Θ(N²).
- READING (§4). The graft MIRRORS every Ξ-order flip of a same-cycle pair of the host into an arena-relevant σ̄-change. So bounding SBCH″
  polynomially is at least as hard as bounding Ξ-order flips of vertex pairs in a phase. Such flips are at most XR(a) + XR(b), and
  XR (Ξ-changes per vertex per phase) has no polynomial bound (XR-LIN is DEAD, RESULTS R80). SBCH″ is therefore NOT an easier quantity than
  the phase length: on the grafted family SBCH″/|P| → 2/3. I found no polynomial bound and record none.

## 1. Definition and Lemma W-SPLIT″ (PROVED, lane)
Setting: one phase P = [i, j] (λ_Ξ and τ constant; RESULTS R38 (a)), W_t = val(σ_t, τ), Ξ_t = val(σ_t, σ̄_t) (SPEC S1). For an Odd strategy ρ,
val(σ, ρ) is S1's valuation of the (σ, ρ)-plays, and Ifr(σ; ρ) := {(v, w) : v Even, w ≠ σ(v), val(σ, ρ)(w) ▷ val(σ, ρ)(σ(v))} (S2's rule
with ρ in place of σ̄). So Iσ(t) = Ifr(σ_t; σ̄_t).
Cut rule (greedy, left to right). The reference is a := i. For t = i, …, j − 1: the transition t → t + 1 is
(FB) an S4c fallback, or else (LW) a change of λ_W, or else (RLV) a transition with Iσ(t + 1) ≠ Ifr(σ_{t+1}; σ̄_a). After a cut of any of
the three kinds, a := t + 1. The refined frozen W-phases are the maximal runs of uncut transitions. SBCH″ counts the RLV cuts, SBCH′ (L-SI's)
counts the non-fallback, λ_W-keeping transitions that change σ̄, and DEL counts the RLV cuts at which σ̄ does not change.
Lemma W-SPLIT″. (a) |P| = FB + LWCH + SBCH″ + Σ_F |F| and #F ≤ FB + LWCH + SBCH″ + 1.
(b) In a refined frozen W-phase F starting at state a, every state u of F that is the source of a transition of F has
Iσ(u) = Ifr(σ_u; σ̄_a). So F's transitions are the transitions of N5 run with Odd's reply frozen at σ̄_a: S4a's σ_new depends only on
(σ, τ, Iσ), there is no fallback in F, and τ is constant.
(c) SBCH″ ≤ SBCH′.
(d) Let u be an Odd vertex that lies on no (σ_t, ρ)-play from a successor w of an Even vertex of out-degree ≥ 2, for ρ ∈ {σ̄_t, σ̄_a} and t
in P. Then a change of σ̄ at u alone never makes an RLV cut. In particular a reader (no predecessor) never does.
Proof. (a) Every transition is exactly one of FB, LW, RLV or uncut, and the uncut ones are partitioned into the maximal runs F. Between
consecutive cuts there is at most one F. (b) u = a holds trivially (Ifr(σ_a; σ̄_a) = Iσ(a)). Any other source u in F is the target of an
uncut transition u − 1 → u, which by the rule has Iσ(u) = Ifr(σ_u; σ̄_a) with the same reference a. S4c fires only on FB transitions, and τ is
constant on P. (c) Let t → t + 1 be an RLV cut with reference a. If σ̄_{t+1} = σ̄_a, then Ifr(σ_{t+1}; σ̄_a) = Iσ(t + 1) and there is no cut. So
σ̄ changed at some transition in [a, t], none of which is FB or LW, because a is the first state after the last cut. Map the cut to the last
σ̄-changing transition in [a, t]. Distinct RLV cuts have disjoint windows [a, t], so the map is injective into the SBCH′ transitions.
(d) val(σ, ρ)(x) depends on ρ only through ρ on the play from x. Ifr compares valuations of successors w of Even vertices (and of σ(v),
also such a successor). If u is on none of those plays for either ρ, then changing ρ(u) alone changes no compared value. A reader has no
predecessor, so it is on no play from another vertex. □
Check (DATA): ARENA_V, i.e. Iσ(t) equal to Ifr(σ_t; σ̄_t) recomputed with common.wplay, holds at every state of every run below. SPLIT_V ((a)'s
identity) also holds everywhere.

## 2. DATA on the corpora (experiments/new/box52/rlv.py; n5x via common.rows)
Logs: box52/rlv_alt_start.txt (alt_all, pinned starts), rlv_lib41.txt (n5-box18 lib41_n48.lst), rlv_sicorpus.txt / rlv_sicorpus_start.txt
(si/chg/sicorpus.lst, default / pinned starts), rlv_red.txt (R106 / R109 pins).
| corpus | phases | max SBCH′/n | max SBCH″/n (instance: SBCH′ → SBCH″) | max DEL/n | longest refined frozen W-phase / n (WCH″) | ARENA, SPLIT, FWBF2, FWLEN2 |
| --- | --- | --- | --- | --- | --- | --- |
| alt_all, pinned starts | 457 | 2.100 (nep92_n40) | 1.825 (nep92_n40: 84 → 73) | 0.031 | 0.917 (x32_rand48: 44 at n 48) | PASS ×4 |
| lib41 | 368 | 1.531 (lev_l_x) | 1.375 (lev_l_x: 49 → 44) | 0.062 | 0.917 (x32_rand48) | PASS ×4 |
| sicorpus, pinned starts | 345 | 1.805 (l121reader_n41) | 1.375 (lev_l_x) | 0.115 | 0.885 (runfam_K100: 123 at n 139) | PASS ×4 |
| R106 runquad_K3 / K8, R109 hntop_n3 / n8 | 1 + 1 + 2 + 2 | 0 | 0 | 0 | hntop_n8: 48 at n 168 | PASS ×4 |
- Reader-proofness (§1 (d)), on L-SI's reader pair: long121_n40 → l121reader_n41 (+ readers): SBCH′ 33 → 74, SBCH″ 30 → 30.
- runfam_K: the longest refined frozen W-phase is K + 23 against n − 1 = K + 38 (K = 40, 60, 100). CONJECTURE FW-BF's n − 1 is approached up to
  an additive constant.
- FINDING: on instances without readers, 87-91 % of σ̄-changes are relevant (nep92 73/84, lev_l_x 44/49, long121 30/33). The coarser cut
  removes reader inflation and little else.

## 3. A quadratic family for SBCH″ in one phase (DATA; experiments/new/box52/scale.sh)
Construction (box52/graft.py, mode ab). The host is R109's topfix_N (red/seg/hnh1.py N topfix, L-RED's generator; N = 8 reproduces the pin
hntop_n8, same sha1 f71291a3… and start 5ec2d306…). flippair.py picks the pair (a, b) whose Ξ-order flips most often in the longest phase,
among the pairs with the same Ξ cycle node at every state of it. Added: u (Odd, Ω 0) → {a, b}; z1 (Even, Ω 0) → {u, b}; z2 (Even, Ω 0) →
{u, a}. TAU0 gets u ↦ a, SIGMA0 gets z2 ↦ u, and z1 takes S3. On topfix_8 z1 sits on b at every state, and z2 leaves u for a at state 6
and stays there. No old vertex has an edge into {u, z1, z2}.
Why each flip is a cut (the mechanism, READING, checked by the counts below). σ̄(u) is the Ξ-smaller of a and b, and Ξ(u) = ext(min). The true
Ξ(u) is never above the frozen val(σ, σ̄_a)(u) = ext(Ξ(σ̄_a(u))). One observer sees a flip only in one direction: z1 (sitting on b, where its W-choice keeps it) has (z1, u) improving iff ext(Ξ(min)) ▷ Ξ(b). With the Ξ cycle odd (reward −7 on topfix_8's pair; longer is better, ext adds 1) that holds iff b is the
min. So z1 separates true from frozen exactly when the reference choice is a and the true min is b, and z2 covers the reverse. The single
observer variants (modes a, b, q) gave 1 or 7 cuts on hntop_n8, since the reference locks after one cut. With both observers every flip
of σ̄(u) is an RLV cut.
| N | n (graft) | host phase (len) | LWCH | flips of the chosen pair | SBCH′ = SBCH″ (graft) | 2N² + 3N − 3 | SBCH″ / n | refined frozen W-phases (longest) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 66 | [0, 41] (41) | 8 | 30 | 24 | 24 | 0.36 | 9 (1) |
| 4 | 87 | [0, 69] (69) | 12 | 50 | 41 | 41 | 0.47 | 16 (1) |
| 6 | 129 | [0, 143] (143) | 20 | 102 | 87 | 87 | 0.67 | 36 (1) |
| 8 | 171 | [0, 241] (241) | 28 | (161, 162): 170 | 149 | 149 | 0.87 | 64 (1) |
| 10 | 213 | [0, 363] (363) | 36 | (203, 204): 254 | 227 | 227 | 1.07 | 100 (1) |
| 12 | 255 | [0, 509] (509) | 44 | (245, 246): 354 | 321 | 321 | 1.26 | 144 (1) |
- The host's phase and its LWCH are unchanged by the graft (same [i, j], same LWCH). The grafted vertices have no
  in-edge from the host, so the host's plays, Ξ, W, Iσ and σ on the host are the same at every state. That is RESULTS R81 (ii)'s setting,
  read here as DATA: the counts above come from the grafted run itself. ARENA, SPLIT, FWBF2 and FWLEN2 PASS on every graft.
- DEAD: "SBCH″ = O(n) per phase" (and so SBCH′ = O(n), since SBCH″ ≤ SBCH′). Instance: box52/out/topfix_n8_cmp.pg (n 171, sha1 pinned in check.sh) with .start;
  scaling family topfix_N_cmp, SBCH″ = 2N² + 3N − 3 at N = 3, 4, 6, 8, 10, 12. Obstruction: an observed Odd comparator copies a host's
  Ξ-leapfrog. Every refined frozen W-phase has length 1 there, so FW-BF is not what is stressed. The cut count itself is quadratic.

## 4. What this says about a bound (READING; no bound PROVED)
- The graft is a MIRROR. Given any game and any pair (a, b) with the same Ξ cycle node on a phase, the graft turns every flip of the Ξ-order of
  (a, b) that is not at an FB or LW cut into an RLV cut, as long as the observers' W-choices stay put (they did on the whole family).
  So a polynomial bound on SBCH″ would bound the Ξ-order flips of every same-cycle pair. Conversely flips(a, b) ≤ XR(a) + XR(b), and
  RESULTS R83's Count already bounds σ̄-changes by Σ_u XR(u) plus TIE / CYC / THRU terms. So SBCH″ sits between "pairwise Ξ-leapfrogs" and
  "Σ XR". Neither has a polynomial bound in the repo, and XR-LIN is DEAD (RESULTS R80).
- So the reader-proof cut answers the inflation question (readers and unobserved Odd vertices drop out, §1 (d)). It does not make SBCH″
  easier than the phase length. On the grafted topfix family SBCH″ ≈ (2/3)|P|. A route through W-SPLIT″ has to bound SBCH″ with the same
  tools as |P|. My READING is that the next useful cut is not on σ̄ but on Ξ: the per-vertex Ξ P-changes under a fixed top (open after
  TOP-SHAPE, RESULTS R84), since every relevant σ̄-flip here is a Ξ-leapfrog.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box52/ (rlv.py, graft.py, flippair.py, scale.sh; logs rlv_*.txt, scale_*.txt; instances out/topfix_N*.pg,
  .start, _cmp.{pg,start}); check.sh block "Box 52".
- FINDINGS: (1) PROVED (lane) Lemma W-SPLIT″: the arena-frozen cut, with SBCH″ ≤ SBCH′, refined frozen W-phases = σ̄-frozen N5 runs, and
  readers never cut. (2) DATA: SBCH″ ≤ 1.825n on 1,170 phases. Readers are removed exactly (l121reader 74 → 30 = long121's 30). FW-BF and
  FW-LEN on the refined cut: 0 failures. (3) DEAD: SBCH″ (and SBCH′) = O(n) per phase. The comparator graft on topfix_N gives exactly
  2N² + 3N − 3 relevant σ̄-changes in one phase (N = 3, 4, 6, 8, 10, 12). (4) READING: SBCH″ mirrors pairwise Ξ-leapfrogs, so it is no easier than |P|.
  No polynomial bound.
- NEEDS: none from the owner.
