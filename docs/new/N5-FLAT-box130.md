# Box 130 N5-FLAT: counting the roots, i.e. W-flat and weak Even moves per TWO-FIX window (TF-RED's F term)
L-NEW successor 45, 2026-11-01 09:41-10:0xZ (date -u). Lead GO 09:43Z. Code: experiments/new/box130/ (flatcnt.py, runcorp.sh,
c_corpus.txt, pincheck.sh, pincheck.txt, u2flat73_n32_default.start). check.sh block «box 130 FLATCNT». Labels: PROVED (lane), DATA,
READING. «Corner» = a move whose old or new option's play runs through the mover h (box 128 W2).

## 0. Answer
- No polynomial count. The obstruction is exact. A run of consecutive FL transitions (W unchanged everywhere) is a strategy-improvement
  run on the ONE-PLAYER game G_σ̄ restricted to W-tight edges (Lemma FL-RED, §2). Its steps are picked by the S1 procedure's tie-break
  among W-optimal strategies of G_τ.
  - On one-player games, rule-independent potentials (Ξ, or (Ξ, play length)) cannot give a polynomial bound. CDAG_n
    (docs/new/N5-K9-Pstrict-counter.md, this lane, READING with computer check; RESULTS R17 (f) signed it as a reading) has
    2^n − n − 1 Ω-strict single-switch improving steps. Re-checked here: n = 6, 8, 10 give 57, 247, 1,013 steps, each run ending optimal.
  - So any polynomial F must use the RULE: which W-optimal strategy the S1 procedure returns.
  - Smallest instance of the obstruction: CDAG_6 (7 vertices, 22 edges, 57 steps). It is a one-player game, NOT an N5 FL run: embedding
    it needs G_τ to tie all CDAG edges and the procedure's tie-break to follow CDAG's order. That is open, and it is the next L-RED
    question if the Lead wants it.
- The count needs ODIFF ≥ 1. Lemma FL-ODIFF0 (PROVED, lane): in an ODIFF-0 window every non-corner mover's W rises strictly, so FL
  transitions there have only corner movers. DATA: 2 ODIFF-0 FL transitions in the corpus, both corner-only (FL0_NONCORNER 0).
- Flat MOVES are not the right unit. Most ride along with W-strict moves in the same transition (u2flat73_n32: 73 flat moves, 7 FL
  transitions). What TF-RED needs is FL TRANSITIONS: 35 in the whole corpus at ODIFF ≥ 1, at most 8 in a row.

## 1. Corrections to my own predictions (made in this box, before the data)
- I predicted «no non-corner flat moves at ODIFF 0». FALSE: 33 in the corpus. My argument confused times: a move is Ξ-improving at
  state j − 1, flatness is measured at state j, after the other movers.
- I took «Ξ rises strictly at every mover» as standard. It fails at the cycle corner: 6 corpus moves, all with h on its own Ξ-play's
  cycle (XIRISE_CYC 6, XIRISE_VIOL 0).

## 2. PROVED (lane)
- Setting: a fallback-free stretch of a TWO-FIX window (τ and σ̄ constant), standing premise of RESULTS R57 (S4a's σ_j is a pointwise
  optimum of the arena H_{j−1}). FL transition := σ_j ≠ σ_{j−1} and W_j = W_{j−1}.
- Lemma FL-OPT: at an FL transition j, σ_{j−1} is itself a pointwise optimum of H_{j−1}.
  - Proof: val(σ_{j−1}) = W_{j−1} = W_j = val(σ_j), and σ_j is a pointwise optimum of H_{j−1}, which contains σ_{j−1}. ∎
  - So an FL transition happens only because the procedure returns a different optimum. DATA: FLOPT_VIOL 0.
- Lemma FL-TIGHT: in a run of consecutive FL transitions, if v's W-play from σ_j(v) avoids v, then W(σ_j(v)) is the same at every
  state of the run. Hence every chosen option of v lies in T_v := {w : W(w) = c_v}.
  - Proof: W(v) = v·W(σ_j(v)) is constant, and prepending v is injective. ∎
  - DATA: 0 violations; 3 cases with v on its own W-cycle (cw11_n24).
- Lemma FL-RED: a maximal FL run is a sequence of strategy-changing steps on the one-player game G_σ̄^T (Odd fixed to σ̄, non-corner Even v
  restricted to T_v), each step applying a nonempty set of VJ-improving switches of that game.
  - Proof: moves lie in the arena, so they are Ξ-improving. In a TWO-FIX window Ξ is the valuation in G_σ̄ (box 121 TWO-FIX). The
    chosen options lie in T (FL-TIGHT). Improving in G_σ̄ is improving in its restriction (a comparison of values only). ∎
- Lemma FL-ODIFF0: in an ODIFF-0 window (σ̄ = τ, so Ξ = W), a non-corner mover h at j has W_j(h) ▷ W_{j−1}(h). Hence an FL transition
  has only corner movers.
  - Proof: Iσ = IW, so W_{j−1}(new) ▷ W_{j−1}(old). By monotonicity (R17 (a) F1), W_j(new) ⊵ W_{j−1}(new). Prepend h (both plays avoid
    h). ∎
- Partial, DATA otherwise: «a transition whose moves are all flat and non-corner is FL, and every non-corner move of an FL transition is
  flat». Proved for a single mover (switch h between two W-equal options whose plays avoid h: no value changes). For several
  simultaneous movers the plays can change with equal values, so the one-at-a-time argument needs care. DATA: ONLYFLAT_VIOL 0 both ways.

## 3. DATA (813 distinct (game, start) pairs, Erratum E-1; c_corpus.txt; 0 errors)
| quantity | ODIFF 0 windows | ODIFF ≥ 1 windows |
| --- | --- | --- |
| windows / Even moves in stretches | 410 / 8,009 | 883 / 10,827 |
| W-strict / flat / weak moves | 7,971 / 33 / 5 | 10,605 / 214 / 8 |
| corner moves | 238 | 191 |
| FL transitions (W unchanged everywhere) | 2 (corner-only) | 35 |
| longest FL run | 1 (tog6a_n32) | 8 (u23sw64_n32) |
| most flat moves in one window | 8 (x32_rand48) | 73 (u2flat73_n32, n = 32; 7 FL transitions) |
| FL-OPT / FL-TIGHT / XI-RISE violations (non-corner) | 0 / 0 / 0 | 0 / 0 / 0 |
- Pin u2flat73_n32 (sha1 bc1547d42172…, default start written out, 82920dbf9a30…): Oink 8fbf0a7 --zlk and --tl verified, regions agree,
  n5b identical state by state (16 iterations, 5 fallbacks).
- flatcnt.py's FLATTRANS field is an unused counter (always 0); FL is the field to read.

## 4. The Lead's items
- «A potential that ties cannot raise», e.g. lexicographic (Ξ-order, play length) at tied W. Ξ does rise at every non-corner mover, so
  it IS such a potential (up to the corner). Its range is exponential, and CDAG_n shows the climb can use that range on one-player
  games under single switches. Play length adds nothing: CDAG_n's lengths never decide (different paths, different vertex sets).
- S4B-OPT / 1E-N3 with the L45 reading: used only as the standing premise (pointwise optimum), in FL-OPT and FL-RED.
- SETTLE-MON / BRACKET-MON: my box 128 READING stands (they count states).

## 5. Next (Lead decides)
- L-RED: realise CDAG_n's order as an FL run, i.e. a G_τ that ties all CDAG edges, with the S1 tie-break (longest/shortest-path
  recursion, smallest index) choosing CDAG's switches. If the tie-break cannot follow such an order, that structural fact is the
  missing lemma.
- L-NEW: characterise the procedure's choice among W-optimal strategies (it depends only on the arena, FL-OPT). Is it a «canonical
  optimum» whose repeated application converges in poly steps?
