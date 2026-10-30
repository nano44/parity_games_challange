# SUB-check: premise [SUB] of L-NEW box 89 (REFEREE-2 successor 22, Opus 5.5, D15; one referee's check, not a landing)
Question (Lead 2026-10-30 15:10Z): does landed RESULTS R88's Corollary FW-R*, on W-runs by RESULTS R89 Lemma GP*-RUN, hold verbatim on every
SUB-INTERVAL of a W-run, as docs/new/N5-BIP-box89.md §3 assumes? Box 89 reads [SUB] «with R* counted inside the sub-interval».

## Verdict: TRUE (Opus 5.5, D15)
For every W-run F = [a, b] and every sub-interval F′ = [a′, b′] with a ≤ a′ ≤ b′ ≤ b (consecutive states of F), WCH_{F′} ≤ (n − 1)(R*_T(F′) + 1).
- WCH_{F′} := the transitions t → t + 1 with a′ ≤ t < b′ and W_{t+1} ≠ W_t.
- R*_T(F′) := the transitions τ → τ + 1 of F′ at which some Even y adopts an edge (y, z) that was BLOCKED (R88 §3) at some state
  t ∈ [a′, τ).
- R88's definitions are read with [a′, b′] in place of [a, b]. No added hypothesis is needed.
- The bound with R*_T(F′) implies the bound with R*_T counted on all of F: every late adoption relative to F′ is late relative to F.

## Reasons: every use R88's proofs make of F, checked against F′
I read R88's object docs/si/P-N5-GP-box31.md: §3 Lemma GP* and its proof, l. 84-123; §4 Corollary FW-R* and its proof, l. 143-156. I also
read R89's line (GP*-RUN carries both proofs to W-runs). The proofs use F in exactly these places, and each holds for F′:
1. Every transition k → k + 1 used is inside F, so it is not an S4c fallback and keeps τ. On W-runs this gives W_{k+1} ⊵ W_k (GP*-RUN; the
   W-run form is R90 (b) W-MON′), and [S4a]'s arena H_k ([F1] in Case B). Transitions of F′ are transitions of F.
2. λ_W is constant on F. GP* uses this in the base case (L = 0: W(u) = (u, ∅, 0) for u with λ_W(u) = u), in Case B1′ (ii), B2a and B2b (i),
   (iii) («λ_W(x) changes at k + 1: impossible in F»), and in FW-R* («u = λ_W(x) (constant on F, so u is a cycle node of state a)»). On F′ ⊆ F,
   λ_W is the same constant map, so «cycle node of state a» becomes «cycle node of state a′», the same set.
3. «Unblocked at state k» needs L ≤ k − a and no block at the states k − 1 − i. FW-R* takes k ≥ a + n − 1 and finds the block at t = k − 1 − i
   ≥ k − n + 1 ≥ a. With a′ in place of a, the block is at t ≥ a′, inside F′. The adoption τ ∈ (t, k] lies in F′, so it is late relative
   to F′.
4. The charging (k − τ ≤ i ≤ n − 2; each τ charged by at most n − 1 values of k) and the first n − 1 transitions are counted from a′.
5. Maximality of F appears nowhere. No step refers to a − 1, b + 1, to the endpoints being cut transitions (fallback, τ-change or
   λ_W-change), or to any property of the start state beyond λ_W(u) = u, which holds at every state of F.
- This agrees with L-SI's box 46 Lemma GP*-SUB (docs/si/N5-SUB-box46.md §1). I read it only after writing items 1-5 above. It is unrefereed,
  and this check is the first referee reading of it.

## Mechanical check (DATA)
- Tool: docs/referee-2/R2-SUB/sub_check.py, on my R2-N5-LATEP/latep_check.py state construction (my N5 loop, no lane code).
  - Coverage: every sub-interval of every W-run with ≤ 40 transitions; 400 random sub-intervals of longer W-runs (30 on the pins file).
  - Lateness is read inside the sub-interval. GPB checks the base reading at a′.
- Sets: the lane corpus odd/sbcg.lst (719 games, S3), plus tiedmut_so_th_n32_11, wdepth_K4_m16 (start + S3), so_th_n32 and fc_6.
- Result: 57,726 sub-interval checks, 0 violations of SUB and 0 of GPB.
  - 218 sub-intervals have WCH_{F′} > n − 1, so the bound is not trivially n − 1 there.
  - Maxima: WCH_{F′} 156, R*_T(F′) 31.

## Consequence for box 89
- [SUB] holds as box 89 states it, so it need not be a premise.
- Theorem BIP-RED applies FW-R* to each frozen stretch Φ of F, a sub-interval of F, with R°_Φ counted inside Φ. That use is covered.
  - Box 89 l. 19 defines a STRICT release in Φ as «a late adoption of (y, z) whose blocking state also lies in Φ».
  - Reading «blocking state» as a state t ∈ Φ before the adoption at which (y, z) is BLOCKED, this is exactly a Φ-late adoption.
  - So R°_Φ = R*_T(Φ), and [SUB] gives the stretch bound (n − 1)(R°_Φ + 1) that BIP-RED's proof uses.
  - I checked only this use of [SUB], not the rest of box 89 (BIP-REL-1 is a CONJECTURE there).

## DONE / FINDINGS / NEEDS
- DONE: this file; R2-SUB/sub_check.py.
- FINDINGS: [SUB] TRUE (sub-interval-relative R*_T; no added hypothesis; maximality never used by R88's proofs); 57,726 sub-interval checks,
  0 violations.
- NEEDS: none. Recorded as one referee's check.
