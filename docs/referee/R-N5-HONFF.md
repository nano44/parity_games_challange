# R-N5-HONFF: REFEREE report on packet P-N5-HONFF (L-NEW box 47: Lemma FB-RISE, Theorem HON-FF (W-honest states per phase ≤ 4n² − 3n), HON-0-FF, REC-1-FF; every game)
Referee: REFEREE (successor 14, session_011gcqhgkUNYoFY7xCryrLff), Opus 5.5 (owner ruling D15). SECOND referee (Lead brief 12:32Z). Context at writing: about 470k tokens.
- Object: docs/new/P-N5-HONFF-box47.md, sha1 98101d1fe723a570f3c79085b929a456ebb7dff5 (on the tree and `git show 2fca63b8:… | sha1sum` (l-new
  freeze); pin trunk 4a0a8aba, an ancestor of HEAD), 141 lines. Author: L-NEW successor 26.
- Written 2026-10-26T12:35Z-12:39Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ HONFF file on my tree or on origin/claude/referee-2 at any of my fetches (re-listed in the same
  turns; 0 / 0 at 12:39Z). No lane code run (experiments/new/box47/ffdeep.py, quotecheck.py not executed or imported). D1.
- Premises read against their text: SPEC S2, S4c, FIX 3 (docs/new/N5-ssi-global.md); RESULTS R15 (a), (d); R17 (a) (V1)/(V2) and box 10 §2
  Case A (A1, A2); P-N5-HON (my R-N5-HON: steps 0-3, SAT0, HON-0, REC-1 all re-derived there; N-HON-1 accepted in its §C).
- Quotes: all 17 curly-quoted passages of §5 found verbatim (whitespace normalised) in the named files at l-new 0238b1cb, each within 3
  lines of the cited line (my own script; scratch/ff_logs/quotes.txt).
- Tool: scratch/ff_probe.py (own engine rl_engine; exact LEV and LEV_odd by simple-path enumeration in G_τ with a path budget; per phase:
  FB-RISE (a), (b) and its inner step LEV_odd(t) ≥ LEV(h) + 1, HON-FF and the gap rise behind it, HON-0-FF, REC-1-FF (a); the packet's own
  "no Odd term" control; MUT=1 (FB-RISE (b) with + 2)). Logs scratch/ff_logs/.

## Verdicts
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | Lemma FB-RISE (a), general form | SIGNED |
| §1 | Lemma FB-RISE (b), honest form | SIGNED (note HONFF-N1: "SAT0's Odd case" means its proof's Odd-case argument, not the lemma) |
| §2 | Theorem HON-FF: W-honest states per phase ≤ 4n² − 3n | SIGNED |
| §2 | Corollary HON-0-FF (a)-(c) | SIGNED |
| §2 | Corollary REC-1-FF (a) | SIGNED |
| §2 | Corollary REC-1-FF (c), (d) | SIGNED as IMPLICATIONS from (Στ) (at R65's audit strength they hold; signed as stated) |
| Q-A | is Lemma P's Case A valid with Ω := Ξ_t (σ_t, S2's Iσ_t)? | YES (§1 below) |
| §3, §4 | data, OPEN / READING | not signed (as briefed) |
No gap. Notes HONFF-N1..N3. HON-FF removes f from the count of W-honest states only; it bounds no fallback count and no running time; not a
TARGET.md claim; G-N5-TIME stays OPEN.

## 1. Lemma FB-RISE
- Setting ✓: in-phase ⇒ τ kept ⇒ the fallback is Even's (S4c with FIX 3); σ_{t+1}(x) = z*(x), the (Ξ_t(w), w)-maximum of Iσ_t(x), for every x
  with Iσ_t(x) ≠ ∅; λ_{t+1} = λ_t. The |r| = 0 case uses λ(u) = u at t + 1 ✓; for |r| ≥ 1, |r′| ≤ j − 1 ≤ LEV(t) gives Ξ_t(z) ⪰ value(r′) ✓.
- Case 1 (Odd x) ✓: j ≤ LEV_odd(t) and (MON). Nothing about Odd vertices is relaxed by Even's move, which is why the Odd term is there.
- Case 2 (Even x, z ∉ Iσ_t(x)) ✓ via Q-A.
- Case 3 ✓: Ξ_t(z*) ⪰ Ξ_t(z) (z* is the Ξ_t-maximum of Iσ_t(x) ∋ z; the tie-break by index only matters among equal values) ⪰ value(r′);
  (MON) at z*. 3a: λ(x) ≠ x at t + 1, so (V1) for x's honest play at t + 1 (x then z*'s play, z*'s path to λ(x) avoiding x), (V2) with r′
  avoiding x ✓. 3b: x its own cycle node at t + 1, z*'s play returns to x, so λ(z*) = x (in the phase, at t as well) and Ξ_t(z*) has cycle
  node x ≠ u; ⪰ value(r′) forces x better than u ✓.
- Q-A, answered YES. Case A (box 10 §2 l. 32-38) uses: (1) Ω(z) ⪯ Ω(ρ(x)) — here S2's non-improvement for Ξ_t (or z = σ_t(x)); (2) the bound
  Ω(z) ⪰ value(r′) — here LEV(t); (3) (V1) at the Even x for Ω — true for Ξ_t because Ξ_t is the valuation of a single play (the honest one,
  a functional graph), and at an Even x that play steps to σ_t(x), so Ξ_t(x) = x ⊕ Ξ_t(σ_t(x)) with σ_t(x)'s path to λ(x) avoiding x when
  λ(x) ≠ x, and Ξ_t(σ_t(x)) has cycle node x when λ(x) = x; (4) (V2), a property of ⊕ and the order alone. A1's last link "⪯ Ω_{k+1}(x) by
  (F2)" is not part of the inequality value(r) ⪯ Ω(x) and is replaced here by (MON). One-player-ness is used nowhere in Case A (it is used
  in Case B through (F1), which FB-RISE does not call). This matches my SAT0 reading in R-N5-HON §2 (Case A without (F2)).
- (b) ✓. If LEV(h) = n − 1, (MON). Else L := LEV(h) ≤ n − 2 and LEV(t) ≥ L (MON). An Odd x has one edge in G_τ, so r = x → τ(x) → r′;
  W_h(τ(x)) = Ξ_h(τ(x)) ⪰ value(r′) (honest, |r′| ≤ L); the W-cycle nodes at h are λ's; the Odd-case argument of SAT0 (per vertex; it does
  not use SAT0's hypothesis "no W-improving edge", which concerns Even vertices only — HONFF-N1) gives W_h(x) ⪰ value(r), with N-HON-1's
  reading (z's PATH to its cycle node avoids x). So Ξ_t(x) ⪰ Ξ_h(x) = W_h(x) ⪰ value(r): LEV_odd(t) ≥ L + 1, and (a) gives min(L + 1, n − 1) ✓.

## 2. HON-FF and corollaries
- HON-FF ✓. Gaps between consecutive unsaturated honest states: fallback-free ⇒ HON step 1 (signed, with both of its uses of
  fallback-freeness in force); with a fallback at t ∈ [h_i, h_{i+1} − 1] ⇒ FB-RISE (b) at h := h_i ≤ t, then (MON) to h_{i+1}. Every gap rises,
  so s − 1 ≤ n − 2; the saturated part is HON step 3's (R15 (d)); N ≤ 4n² − 3n ✓. The paragraph "What is replaced, exactly" is accurate: a
  gap with a fallback uses neither WM nor the sandwich, only honesty at h_i (Ξ = W, λ_W = λ) — my HON-N3 is answered.
- HON-0-FF ✓ (HON-0's proof; D = ∅ states are honest). REC-1-FF (a) ✓ (f enters REC-1 (a) only through HON-0 (a)); (c), (d) ✓ as
  implications (unchanged structure, EP-1u).
- Against REC-0 (R66): (f + 1)(n + 1) + 4n(n − 1) + 1 − (4n² − 3n) = f(n + 1) + 2 ✓ (re-computed).

## 3. Data (own engine; DATA, not proof; 0 failures of every signed check)
| sample | runs | phases | in-phase fallbacks checked by FB-RISE (a) (non-honest source) | FB-RISE (b) pairs (h, t) | gaps (with an inside fallback) | control "no Odd term" fails (Odd term binding in all) | UNK phases (budget) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| packet's inside-gap instances: ffin4_n24, ffin5_n32, ffin12_n32 (sha1 e1c4043c… / d20ea0f2… / 6bae375b…, with their .start), j10_n24, j7_n32, j8_n32 (S3), BUDGET 3·10⁷ | 9 | 35 | 12 (10) | 45 | 23 (2) | 10 | 7 |
| lib41 games n ≤ 20 (271 skipped), S3 + 2 random | 423 | 1,507 | 170 (142) | 87 | 293 (0 with LEV computed) | 22 | 3 |
| random 𝒞^kO, k 0-4, n 5-12, seed 1447 | 9,000 | 21,587 | 286 (2) | 326 | 141 | 0 | 0 |
- HON-FF, HON-0-FF, REC-1-FF (a) bounds: 0 violations in all 23,129 phases (max 18 W-honest states in a phase).
- Inside-gap fallbacks verified exactly: 10 (FB_inside_gap) on the packet's instances, 1 in lib41 n ≤ 20; all rise (FB-RISE (b) holds at
  every one). The control without the Odd term fails exactly where the packet says (inside fallbacks), always with LEV_odd(t) binding: the
  LEV_odd term of (a) is needed.
- Control MUT=1 (FB-RISE (b) asking LEV(h) + 2) on ffin4_n24 + j10_n24: 5 failures (bites).

## 4. Notes
- HONFF-N1 (§1 (b)): "SAT0's Odd case at h" cites a part of a lemma whose hypothesis (σ_h has no W-improving edge) need not hold at h; what is
  used is the Odd-case step of SAT0's proof, which is per vertex and hypothesis-free. Say "the Odd-case argument of SAT0's proof".
- HONFF-N2 (§0 / §1): LEV_odd quantifies over Odd x but paths through any vertices — as stated; note that LEV(k) ≤ LEV_odd(k) makes (a)'s
  bound min(LEV(t) + 1, LEV_odd(t), n − 1) ≥ LEV(t), so (a) contains (MON)'s "no fall" as a special case (consistent, not an error).
- HONFF-N3 (§5): the cited line numbers are the lines where each quote begins or ends within the cited ranges; all found.

## §C. Comparison with REFEREE-2 (R2-N5-HONFF, claude/referee-2 05e7663c + addendum 1306c31e, sha1 4e44f4d4… at 1306c31e), written 2026-10-26T13:19Z by date -u
Opened only after my report was pushed (cce5ea5e) and the Lead's message of 13:18Z (Lead's stamp).
- Independence (its addendum): REFEREE-2 saw my file NAME in a listing at its push turn and my commit SUBJECT after its push; it did not open
  the file; its report was final before either. Its header "1 at 13:06Z" is the right count (its commit message's "0" is corrected by the
  addendum, without rewriting history). I accept the record; it does not affect either report.
### C.1 Verdicts, item by item
| item | REFEREE (cce5ea5e) | REFEREE-2 (05e7663c) | |
| --- | --- | --- | --- |
| FB-RISE (a), (b) | SIGNED | SIGN | same |
| Theorem HON-FF, HON-0-FF (a)-(c), REC-1-FF (a) | SIGNED | SIGN | same |
| REC-1-FF (c), (d) | SIGNED as implications from (Στ) | SIGN as implications | same |
| Q-A (Case A with Ω := Ξ_t) | YES: (1) non-improvement, (2) LEV bound, (3) (V1) for a single (honest) play, (4) (V2); one-player-ness only in Case B | YES: the same four items, "facts about the VALUE OF A PLAY"; no P1/P2 needed for Case A | same (identical item list) |
| REC-0 difference f(n + 1) + 2 | re-computed | CORRECT | same |
| "What is replaced" / HON-N3 | accurate | right | same |
No disagreement; both: no gap.
### C.2 Notes
| note | REFEREE | REFEREE-2 | outcome |
| --- | --- | --- | --- |
| SAT0's Odd case is used without SAT0's hypothesis | HONFF-N1 (wording: cite the Odd-case argument) | stated in its §1 (b) ("does not use SAT0's hypothesis") | same substance; keep as one wording note |
| XW listed but unused by HON-FF (XW enters P-N5-HON only in HON-FB (iv)) | — | N-HONFF-1 | REFEREE-2 only; ACCEPTED (checked: HON-FF cites HON steps 0-3, SAT0's Odd case, HON-0, REC-1; none uses XW) |
| FB-RISE needs P1 only; P2 enters only through HON step 1 | implicit (my Q-A: Case B / (F1) not called; (MON) only) | N-HONFF-2 | REFEREE-2 only as a note; ACCEPTED |
| data thin where it matters | my §3 (10 inside fallbacks exact, 7 phases UNK) | N-HONFF-3 (5 of 6 gaps exact, j7_n32 UNK even at 1.5·10⁸) | same |
| control without LEV_odd fails | my §3 (10 on the inside-gap instances, 22 lib41 n ≤ 20; Odd term always binding) | N-HONFF-4 (152 lib41) | same |
| LEV ≤ LEV_odd remark; quote line cites | HONFF-N2, N3 | — | REFEREE only (remarks) |
### C.3 Data (both own engines, 0 violations)
Both verify FB-RISE (a), (b) at every exactly-computed inside fallback of the packet's instances (mine 10 + 1 lib41; REFEREE-2 24 across 5 of
6 gaps); both find j7_n32 over budget; both "+2" controls bite (mine 5, REFEREE-2 1); both "no Odd term" controls fail with the Odd term binding.
### C.4 Joint gap map
EMPTY. Joint notes for L-NEW 26's fixes file: N-HONFF-1 (XW unused), N-HONFF-2 (FB-RISE on P1 only), HONFF-N1 (SAT0 Odd-case citation),
N-HONFF-3 / data (j7_n32 still UNK), HONFF-N2, N3 (remarks). Verdicts as in C.1, both (Opus 5.5, D15).
