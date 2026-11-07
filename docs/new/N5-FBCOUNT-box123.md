# N5-FBCOUNT (box 123): fallbacks inside TWO-FIX windows: where they act (proved), what is not a potential (DEAD), and the count that survives (DATA)
- L-NEW successor 44 (Opus 5.5), D14 / D18. Lead GO 2026-11-01 03:45Z: «GO for (b) first …: the fallback count for TWO-FIX. Test whether
  the W-vector after each fallback is never repeated (a potential), and how FB grows with n on b5_os / returns / farrise25.»
- Definitions as in boxes 121-122 (docs/new/N5-TWOFIX-box122.md): TWO-FIX window, ODIFF set O, D_j := the vertices whose (σ_j, σ̄)-play
  visits O, W (G_τ) and Ξ (G_σ̄), FB := the window's S4c fallbacks. XO := the window transitions at which Ξ changes at a vertex of O.
- Tools: experiments/new/box123/fbcount.py (one line per window with FB ≥ 1); runcorp.sh (→ f_sbcg.txt, f_alt.txt); pincheck.sh
  (→ pincheck.txt).
- No literature is cited here. L-LIT T64's findings reach this lane through the Lead's 03:45Z message only (no source opened by me).

## 0. Answer
- The W-vector right after a fallback never repeats inside a window (DATA: 250 windows with fallbacks, 0 repeats). This is injectivity
  into an exponential set, so it is NOT a potential. W-vectors do repeat among all window states (46 windows).
- PROVED (lane), §1: fallbacks act only on D.
  - FB-DISJ: at a fallback, Is_j ∩ IW_j = ∅.
  - FB-D: every switched edge touches D_j.
  - DROP-D: W falls only on D_j ∪ D_(j+1). DATA: 3,562 / 3,562 W-drops.
- DEAD (§2): «between consecutive fallbacks, |{Ξ ≠ W}| after the fallback strictly falls unless Ξ changes at an O-vertex in between».
  frz24 (red/n5inj/instances/frz24.pg with frz24.start): ODIFF 1, two fallbacks, gap 18 → 18, no Ξ(O) change. 15 such pairs in 9 windows.
- DATA that survives: FB ≤ (XO + 1)·n in all 250 windows. The largest FB / (XO + 1) is 34 at n = 48 (rise_fb38_n48: one window of 34
  fallbacks with XO = 0; the gap falls by 1 at almost every fallback).
- FB versus n (the Lead's question):
  - Only b5_os is a size-indexed family here: n 12 … 40 gives FB 4 / 6 / 7 / 7 / 7 / 8 / 8 / 9.
  - returns_rt32 / rt48 / rt64 / ph64, farrise25_n32 and rise_fb38_n48 are search-found single instances (L-RED notes), not families:
    FB 4 / 14 / 14 / 15, 28 at n = 32, 34 at n = 48.
  - So the data cannot tell polynomial growth from slow exponential growth. The question goes to L-RED (b).

## 1. Lemmas (PROVED, lane)
- Setting: a TWO-FIX window, a fallback transition j → j + 1 of it.
- Lemma FB-DISJ: Is_j ∩ IW_j = ∅ and Is_j ≠ ∅.
  - Proof.
    - The transition is an S4c fallback, and τ is fixed, so S4a returned σ_j: σ_j is a pointwise optimum of G_τ's arena {σ_j} ∪ Is_j.
    - If (y, z) ∈ Is_j ∩ IW_j, then the switch σ_j[y ↦ z] lies in the arena and strictly raises W somewhere (RESULTS R15 (a) on the
      one-player game G_τ).
    - The arena optimum dominates every arena strategy pointwise (RESULTS R17 (a) (F2)), so its W differs from W_j and the optimum is not
      σ_j. That is a contradiction.
    - Is_j ≠ ∅: S4c's Even branch fires only with Is ≠ ∅, and its Odd branch would change τ. ∎
- Lemma FB-D: every edge (y, z) switched at the fallback has z ∈ D_j or σ_j(y) ∈ D_j.
  - Proof: S4c switches only edges of Is_j. If neither z nor σ_j(y) lies in D_j, then Ξ_j = W_j at both (box 122 GAP-D). So
    (y, z) ∈ Is_j would give (y, z) ∈ IW_j, which FB-DISJ excludes. ∎
- Lemma DROP-D: at any transition j → j + 1 of a TWO-FIX window, W falls only at vertices of D_j ∪ D_(j+1).
  - Proof: outside D_j ∪ D_(j+1), Ξ = W at both states (GAP-D), and Ξ is non-decreasing (RESULTS R18 (d) Lemma S (b), whose proof uses no
    𝒞^1O hypothesis). ∎
  - With box 122 W-MON-RUN, every W-drop is at a fallback and inside D.
- DATA: fallback switches with y ∈ D_j: 1,758 of 1,800. The rest have z ∈ D_j. W-drops in D_j ∪ D_(j+1): 3,562 of 3,562.

## 2. DEAD: gap descent between fallbacks
- Statement killed: «in a TWO-FIX window, for consecutive fallbacks f < f′ with no transition j, f ≤ j < f′, changing Ξ at a vertex
  of O, |{Ξ ≠ W}| at state f′ + 1 is smaller than at state f + 1».
- Instance: red/n5inj/instances/frz24.pg (sha1 f50c434b731a…) with frz24.start (c150c50b241c…), window [13, 30], ODIFF 1, FB 2, gap
  after the fallbacks 18 and 18, XO = 1 elsewhere in the window.
- Checked: Oink 8fbf0a7 --zlk and --tl «solution verified»; regions AGREE; n5b identical (39 iterations, 4 fallbacks)
  (box123/pincheck.txt).
- Corpus: 15 of 449 consecutive-fallback pairs violate it, in 9 windows (frz24, lend27_n24, lend107_n32, lend39f_n32, lend55_n32,
  lend9_n8, lend82_n32, lend72_n48; frz24 both with and without its start file). Every b5_os and returns instance satisfies it.
- The unconditional form (no XO clause) fails more often: 51 pairs. The resets in b5_os_n40 and farrise25_n32 coincide with Ξ(o) changes.

## 3. DATA (box123/f_*.txt; distinct (game, start, window); L-SI box 53's corpus)
- 250 windows with ≥ 1 fallback. By ODIFF: 0: 34, 1: 148, 2: 31, 3: 20, 4: 7, ≥ 5: 10.
- Post-fallback W-vectors: no repeat in any window (REPWF 0). All-state W-vectors repeat in 46 windows (REPW > 0).
- The peaks (W just before each fallback) and troughs (just after) are not pointwise monotone. b5_os_n40: 8 / 7 of 8 consecutive pairs
  fail.
- FB ≤ (XO + 1)·n: 0 violations; largest FB / (XO + 1) = 34 (rise_fb38_n48, n = 48). XO ≤ 16 in ODIFF-1 windows.
- rise_fb38_n48 (red/so/instances, 98ba3601be92…, default start box123/inst/rise_fb38_n48_default.start 5f12daa3d103…): window [14, 49] has
  34 fallbacks with 35 switches, each dropping W at exactly one D-vertex. The gap falls 36 → 2, mostly by 1 per fallback. Pinned: Oink
  --zlk / --tl verified, AGREE, n5b identical (53 iterations).

## 4. READING (not to sign)
- A fallback is N5 trading W for Ξ inside D: it takes Ξ-improving edges that G_τ considers useless (FB-DISJ), and W drops only there.
- On the long fallback chains (rise_fb38, farrise25) each fallback moves one D-vertex and the gap shrinks by one. A natural count is
  «each fallback settles one more D-vertex into Ξ = W, until Ξ changes on O». frz24 shows it is not literally true; the corpus says the
  exceptions are rare.
- CONJECTURE FB-XO (weak, DATA only): FB ≤ (XO + 1)·n in every TWO-FIX window.
  - With TF-RED and TF-PH (box 122) it would reduce TWO-FIX-POLY to XO (Ξ-changes at O-vertices) and F.
  - XO is a Ξ-change count at a set of ODIFF vertices: XI-CH restricted to O. That is again the core, on a smaller set.
- Next (untested): (a) TF-PH via R17 (b) Lemma P. The Lead relays T64: R17 applies when D = ∅, so only D-vertices need care. That would
  turn TF-PH into a lemma and leave FB-XO and XO.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box123/{fbcount.py, runcorp.sh, f_sbcg.txt, f_alt.txt, pincheck.sh, pincheck.txt,
  inst/rise_fb38_n48_default.start}; check.sh block «box 123».
- FINDINGS:
  - FB-DISJ, FB-D, DROP-D PROVED (lane).
  - Post-fallback W never repeats (DATA), which is not a potential.
  - Gap descent between fallbacks DEAD (frz24).
  - CONJECTURE FB-XO (FB ≤ (XO + 1)·n, 250 / 250).
  - FB versus n: only b5_os is a family (FB 4 → 9 for n 12 → 40).
- NEEDS: Lead: GO on (a) the TF-PH proof; route «FB growth on a generated family» to L-RED with box 121-123's definitions.
