# N5-FBLIN (box 50): does a fallback force a path-set change or a carry? DATA: no (three mechanisms, instances); FB-LIN stays OPEN
L-NEW successor 31 (Opus 5.5; D14, D18, Lead reading L40). Lead's word 2026-10-29 11:19Z: «(b) Next item: CONJECTURE FB-LIN (f ≤ n fallbacks per
phase; DATA max 0.79n ...). Bring the new tools to bear: your per-phase bound len(P) ≤ Φ_dσ(P)(m) − 1, and L-LIT's Lemma MATCH-Φ (P-N5-MPGS
(A) ...). The question to answer first: does a fallback force a path-set change, or a carry, at a specific vertex? If it does, FB-LIN reduces
to NM. Data before proof, as always.» This is a working note. It is unrefereed and not frozen, and it is not a TARGET.md claim. G-N5-TIME stays OPEN.
Labels: PROVED (lane) / CONJECTURE / OPEN / DATA / DEAD / READING. Tool: experiments/new/box50/fbcarry.py (+ fbwalk.py, the independent
check); logs box50/fbc_alt.txt (default starts), box50/fbc_alt_start.txt (pinned starts).

## 0. Definitions (L-LIT's, P-N5-MPGS (A), claude/l-lit docs/lit/P-N5-MPGS.md §A0)
For a transition t → t + 1 inside a phase and a vertex v (λ(v) = c fixed on the phase), the change of Ξ(v) is one of four kinds:
- NONE: Ξ(v) does not change.
- LEN: same path set, other length.
- MAT: a MATCHED P-change, i.e. a matching of the ranks that leave to the ranks that enter, with w(in) > w(out), covering every even
  rank that leaves and every odd rank that enters (w = ±position in R_c).
- CAR: a P-change that is not matched (a carry).
SW_t := the Even vertices switched at t. An in-phase fallback is a transition t → t + 1 of a phase made by S4c.
The MATCHED test (fbcarry.py) finds two one-sided matchings by augmenting paths. By the Mendelsohn-Dulmage theorem these combine into one matching that covers both sets. CHECK=1 compares the test with L-LIT's
brute force (docs/lit/T33-match-phi-check.py `matched`, copied) on every P-change with |A Δ B| ≤ 7: 30,349 compared, 0 mismatches (fbc_alt.txt).

## 1. DATA (alt_all; engine n5x)
| corpus | in-phase fallbacks | with NO P-change anywhere | with NO carry anywhere | switched vertices at fallbacks: CAR / MAT / LEN / NONE | phases with f ≥ 2 | of those, one vertex carrying at every fallback |
| --- | --- | --- | --- | --- | --- | --- |
| default starts (fbc_alt.txt) | 536 | 27 | 159 | 797 / 459 / 60 / 24 | 55 | 0 |
| pinned starts (fbc_alt_start.txt) | 731 | 33 | 201 | 1,277 / 522 / 100 / 30 | 85 | 4 |
For comparison, the S4a transitions of the same phases (default starts) give switched vertices CAR 5,918 / MAT 4,281 / LEN 581 / NONE 7.
That is a carry share of 55 %, against 59 % at fallbacks. Fallbacks are not special in how often they carry.
When a fallback carries anywhere, a switched vertex carries (376 of 377 such fallbacks, default starts).

## 2. DEAD (the Lead's first question, answered by data)
- «A fallback forces a P-change at some vertex»: DEAD. Two mechanisms, each with an instance checked by two engines (L-SI root/n5bcmp.py: n5b and n5x
  state sequences identical) and by box50/fbwalk.py (it walks the (σ_t, σ̄_t)-plays itself and reads (c, P, ℓ) by S1; it AGREES with
  fbcarry.py's classification at every vertex):
  - FLAT: experiments/n5-exhaustive/instances/b4_n5_other_0.pg (n 5, sha1 6115e60a…, S3 start box50/fbinst/b4_n5_other_0.start), phase
    [0, 2], fallback 1 → 2 switches vertex 4, and Ξ changes at NO vertex (a switch along an honest cycle; this is the instance of box 46's
    dead end "no fallback at a W-honest state").
  - LENGTH-ONLY: experiments/n5-epoch/instances/nep22f_n64.pg (n 64, sha1 d98de59f…, S3 start box50/fbinst/nep22f_n64.start), phase
    [11, 29], fallback 27 → 28 switches 5, 11, 31, 34, 38, 49, 54. Every vertex whose Ξ changes changes its length only.
- «A fallback forces a carry at some vertex»: DEAD. Besides the two above, there is a MATCHED-ONLY mechanism: experiments/n5-exhaustive/instances/b5_o11.pg
  (sha1 db4fe55a…, S3 start box50/fbinst/b5_o11.start), phase [0, 11], fallback 7 → 8 switches 0 and 1. Their changes are matched
  P-changes and no other vertex's Ξ changes. Two engines and fbwalk agree. In the library 132 of 536 fallbacks (default starts) change
  path sets with no carry.
- «One specific vertex carries at every fallback of a phase»: DEAD. 0 of 55 phases with f ≥ 2 (default starts) and 4 of 85 (pinned) have
  such a vertex. On long121_n40 (pinned .start, phase [1, 122], f 8, all fallbacks carry) the best vertex carries at 6 of the 8.
- So FB-LIN does NOT reduce to NM by a per-fallback charge. Obstruction: S4c switches each Even vertex with an improving edge to its
  Ξ-best option. The resulting rise of Ξ at the switched vertex (RISE-SW, RESULTS R80) can sit entirely in the length, can be a matched
  exchange, or can be absent (on an honest cycle).

## 3. What the new tools still give (PROVED (lane), elementary; a REDUCTION with a polynomial, not linear, loss)
- Phase level (P-N5-VC Theorem VC-BOUND (b)): f(P) ≤ len(P) ≤ Φ_dσ(P)(m_σ(P)) − 1. With phase VC ≤ 4 (DATA), this is O(m⁴). True but
  weak, and not specific to fallbacks.
- Per vertex: inside a phase λ is fixed. Inside a block of constant P the order is decided by ℓ alone, and ℓ moves one way (RESULTS R15
  (a)). This is L-SI's elementary step, N5-GRUN §5. So XR_P(v) ≤ PCH_P(v) + (PCH_P(v) + 1)(n − 1), and MATCH-Φ bounds PCH_P(v) by
  (K(K+1)/2)(NM_P(v) + 1) + NM_P(v). Every fallback that is not FLAT changes Ξ at some vertex. By R15 (a), with (d) for S4c, that change is a
  rise, so it is counted in that vertex's XR_P. So f(P) ≤ FLAT(P) + Σ_v XR_P(v), which is polynomial in n and NM_P := max_v NM_P(v),
  of order n·n·n²·NM. This is far from n. READING: since every transition of a phase is counted the same way (R80 PHASE-SW), the bound
  is a phase-length bound, not a fallback bound.

## 3b. Per-phase counts of the fallback kinds, and a per-vertex charge (DATA; fbcarry.py, logs box50/fbc3_alt.txt, fbc3_alt_start.txt)
- Per phase (both start sets): fallbacks with no P-change anywhere ≤ 2; fallbacks with no carry anywhere ≤ 14 (farrise25_n32, phase
  [7, 35], f 25); fallbacks that carry ≤ 37 (rise_fb38_n48, phase [4, 49], f 37, all of them carry). The fallback-rich phases are carry phases.
- Decomposition (elementary): f(P) ≤ NSC(P) + Σ_v SWCAR_P(v). Here SWCAR_P(v) is the number of fallbacks of P at which v is switched
  AND carries, and NSC(P) the number of fallbacks with no such vertex. Then f(P) ≤ NSC(P) + n·max_v SWCAR_P(v), so a constant bound on
  max_v SWCAR_P(v) plus NSC(P) = O(n) would give f = O(n).
- DATA: max_v SWCAR_P(v) ≤ 5 in the library (rise_thin51_n40 vertex 17; long121_n40 vertex 23; nep92/nep94 vertex 36). rise_fb38_n48's 37
  carry fallbacks spread with ≤ 2 per vertex.
- DEAD: "SWCAR ≤ 5" (the library constant). Kill climb box50/vcclimb.py SCOPE=swcar from long121_n40 (pinned .start), step 257:
  box50/out/swc2_vc7.pg (n 56, sha1 f0df2aa9…; .start), phase [2, 69] with f 9, and vertex 53 is the switched carrier at 7 of the 9. Two
  engines agree (n5b = n5x, 70 states). A second climb from rise_thin51_n40 reaches 7 at n 63-64 (out/swc1_vc7.pg). The charge
  concentrates on one vertex rather than spreading. CONJECTURE SWCAR-O(1) stays OPEN only in the weak sense that nothing above 7 was seen.
  It is a per-vertex count of the kind that died before (SW-LIN, XR-LIN), so it is not a promising route.

## 4. OPEN, and what the data suggest next
- FB-LIN (f ≤ n per phase): OPEN. Data max 0.79n (Lead). fb_per_phase_max = 37 in alt_all.
- The three fallback kinds above (FLAT, LEN-only, MATCHED-only) are the cases a per-fallback charge to carries misses. A charge to
  the switched vertex's Ξ-rise would have to bound LEN-rises (≤ n − 1 per P-block per vertex) and matched rises (Φ ≤ K²/2 per vertex
  between carries) per vertex per phase, then show that the fallbacks spread over different vertices. §2's "no common carrier" says
  they do spread, which is the wrong direction for a single-vertex charge.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box50/fbcarry.py, fbwalk.py, fbinst/*.start; logs fbc_alt.txt, fbc_alt_start.txt, fbc2_*.txt, fbc3_*.txt; climbs out/swc1*, out/swc2* (vcclimb.py SCOPE=swcar).
- FINDINGS: (0) §3b: per phase ≤ 2 path-set-free and ≤ 14 carry-free fallbacks; per-vertex switched-carry charge ≤ 5 in the library, 7 after climbs (swc2_vc7, DEAD at 5). (1) DEAD: a fallback forces neither a P-change (FLAT b4_n5_other_0; LENGTH-ONLY nep22f_n64 t 27) nor a carry (MATCHED-ONLY
  b5_o11 t 7), and no vertex carries at every fallback of a phase (0 / 55 and 4 / 85 phases). All three are two-engine. (2) FB-LIN does not
  reduce to NM by a per-fallback charge. The reduction that remains is polynomial and not fallback-specific (§3). (3) Fallbacks carry about
  as often as S4a steps (59 % against 55 % of switched vertices).
- NEEDS: none from the owner.
