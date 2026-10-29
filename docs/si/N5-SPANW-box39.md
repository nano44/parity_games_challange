# N5-SPANW (box 39): do span P-changes of a target come with its W-changes? Not always; the two charges are complementary
L-SI successor 30 (Opus 5.5), D15 / D18, Lead reading L40. Lead's message 2026-10-29 21:56Z (BOX 39): "Is there a span version of W-ENT
that bounds P-changes of c inside v's span by W-changes of c, plus O(n)? Measure first whether span P-changes of c come with W-changes of
c on the corpus. If they do, PCH-QUAD-S reduces to W-VPOLY on spans." Working note, unrefereed, not a TARGET.md claim. G-N5-TIME OPEN.
Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Tool: experiments/si/odd/spanw.py (Even side, plain N5 run).
  - For every λ-run of Ξ and every pair (v, c) with Even v switching into c inside it, span(v, c) as in box 38.
  - PCH: span transitions at which P(Ξ c) changes. WCH: span transitions at which W(c) = val(σ_t, τ_t)(c) changes.
  - CO: P-changes with a W-change at the same transition. TQ: P-changes with τ constant.
- Output: odd/out/spanw_corpus.txt (719 games, S3 start, 0 timeouts). Pinned in si/check.sh «box 39».

## 1. DATA (corpus)
- Totals over all pairs: PCH 29,883; CO 26,036 (87%); WCH 29,306; TQ 26,138.
- PCH − WCH > 0 for some pair in 133 / 719 games. It exceeds n only on rise_thin51_n40.
- Max PCH^span / n = 1.375 (rise_thin51_n40, 55 at n 40). Max of min(PCH^span, WCH^span) / n = 0.47 (b6_xw_n32, 15 at n 32).
  The largest absolute value of that min is 33 (topfix_n10, n 210).
- Max ENT of one pair in one λ-run: 0.19n (j5_n16, 3). Largest absolute: 18 (topfix_n10, n 210). hntop_n3: 13 at n 63.
- hntop_n3 / n4: P-changes and W-changes co-move (PCH 373 / 914, CO 373 / 913, max PCH − WCH = 0).

## 2. DEAD: a span version of W-ENT of the form PCH^span ≤ WCH^span + O(n)
- Kill: red/so/instances/rise_thin51_n40.pg (S3), pair (v, c) = (28, 1), λ-run from 9.
  - v leaves c at 14 and re-enters at 77. One out-window, τ constant on it.
  - Inside it c has 55 P-changes of Ξ and 0 changes of W(c).
- Obstruction (READING):
  - Ξ(c) follows c's σ̄(σ)-play (Odd's best reply); W(c) follows c's τ-play. Here σ keeps changing on the first and never on the second.
  - The out-window is cut by S4c fallbacks into 8 guided stretches (wret.py on this game: longest 13). W-MON fails across a fallback,
    so W-RETURN does not charge this re-entry. Its pay is the Ξ-rise of SW-RETURN, i.e. Lemma SPAN's route.
- So PCH-QUAD-S does NOT reduce to W-VPOLY. P-changes in a span need not show up in W at all.

## 3. The two charges per pair (PROVED, lane, combining box 37 and box 38) and the conjecture it suggests
- For a pair (v, c) and a λ-run R, cut span(v, c) at the transitions that are not S4a steps with τ constant (τ-changes and S4c fallbacks).
  Let G_vc be the number of pieces that meet an out-window.
- Then ENT_R(v, c) ≤ 1 + min( PCH^span + (n − 1)(1 + PCH^span),  G_vc + WCH^out + SIL + CYC ).
  - First argument: Lemma SPAN.
  - Second: W-ENT (out-window form, box 38 §6) on each guided piece. A re-entry whose out-window crosses a cut is charged to the cut,
    at most one per piece.
- CONJECTURE MIN-QUAD: min(PCH^span, WCH^span) ≤ n² for every pair. DATA: ≤ 0.47n on the corpus.
  - MIN-QUAD alone does not close the route: the W branch carries the piece count G_vc, i.e. τ-changes and fallbacks in the span.
- Composition: G-N5-TIME ⇐ PCH-QUAD-S (box 38), or ⇐ per-pair [W-VPOLY-S on the guided pieces + polynomial G_vc + SIL + CYC]. The
  data say the cheaper branch is ≤ 0.47n per pair on the corpus and quadratic on H_n.

## DONE / FINDINGS / NEEDS
- DONE: odd/spanw.py; corpus run; check.sh «box 39»; this note.
- FINDINGS:
  1. DATA: 87% of span P-changes co-occur with W-changes.
  2. DEAD: PCH^span ≤ WCH^span + O(n) (rise_thin51_n40, pair (28, 1): 55 vs 0, τ constant, the window cut by fallbacks into 8 guided
     stretches).
  3. PROVED (lane): the per-pair two-charge bound.
  4. CONJECTURE MIN-QUAD.
- NEEDS: none from the owner.
