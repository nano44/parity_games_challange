# R161: per-pair FUEL in the corpus is re-armed at most once per outer event. FUEL-DESC (L-SI box 56) dies again, 25 times without a reset, on R158's fbg_K4_m6_m24: E2 reactor pairs whose fuel keys alternate between the h- and hp-ladder ranks (two alternating sources, R156's leapfrog), re-routed once per phase (MAXPAIR = K). A SELF-FEEDING pair (z's rises fed by y's own fuel) cannot close: while y sits on z, Ξ(z) does not depend on y (the cycle rule of SPEC S1 plus SI monotonicity); while y sits elsewhere, the z-versus-w comparison at y is decided by z's prefix alone. So a pair's fuel must come from outside the pair, and the counter shape needs an outside source that rises many times per outer event. That is XI-CH-POLY again (no amplification)
L-RED successor 37 (Opus 5.5; D1/D18). Lead 2026-10-31 11:23Z: «Take ONE more box, R161, then park … Grow nep56_n32's single ascent into a pair whose fuel re-arms many times per outer event, by making z's higher digit rise repeatedly. Ideally, z's higher digit is fed back by y's own fuel (a self-feeding pair = a counter). Score fuel events per pair against n with L-SI's srcfuel.py … If the feedback cannot close, give the exact obstruction.» Written 2026-10-31 from 11:25Z (date -u).
- Labels: DATA / READING (with a proof sketch). Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Sources opened:
  - l-si cecbf177: docs/si/N5-GROW-box56.md §4 (FUEL-MONO, FUEL-DESC, nep56_n32 pair (28, 2)) and experiments/si/grow56/srcfuel.py
    (run unchanged from a git archive, PYTHONPATH new/box21:harness:new:si);
  - docs/new/N5-ssi-global.md SPEC S1 (cycle nodes, Odd's choice);
  - RESULTS R153 SW-XI (L-RED lane: switches of u ≤ Σ over its successors of (1 + XICH)).

## 1. DATA: fuel per pair against n (srcfuel.py @ l-si cecbf177)
| instance | n | iterations | W-runs | source events | FUEL | MAXPAIR | KEYTURN | RESET | DESCV | MAXSTRETCH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nep56_n32 (L-SI seed) | 32 | 57 | 4 | 51 | 47 | 2 | 0 | 1 | 1 | 2 |
| src2_K3 (R156) | 285 | 324 | 1 | 24 | 24 | 12 | 0 | 0 | 0 | 12 |
| rcl_K8 (R157) | 289 | 324 | 1 | 24 | 24 | 12 | 0 | 0 | 0 | 12 |
| rcl_K24 (R157) | 321 | 324 | 1 | 24 | 24 | 12 | 0 | 0 | 0 | 12 |
| fbg_K4_m6_m24 (R158) | 178 | 140 | 1 | 32 | 27 | 4 | 25 | 0 | 25 | 4 |
| fbg_K8_m6_m24 (R158) | 234 | 272 | 1 | 64 | 55 | 8 | 25 | 0 | 25 | 8 |
| hit_b6a_1 (l-new) | 32 | 43 | 3 | 11 | 9 | 1 | 0 | 0 | 0 | 1 |
| w_re3_1 (R160) | 32 | 28 | 2 | 8 | 8 | 1 | 0 | 0 | 0 | 1 |
| hd_H40 (R159) | 122 | 40 | 1 | 40 | 39 | 1 | 0 | 0 | 0 | 1 |

- MAXPAIR is the number of outer events in every instance: 12 waves on obs-based builds, K phases on fbg, 1 on the single-wave seeds.
- No pair is re-routed twice inside one outer event.
- fbg_K4_m6_m24: the DESCV pairs are E2 reactors (e.g. (130, 132), (133, 135), (136, 138); srcfuel's first violations show keys
  (1, 150) at k 99, then (1, 177) at k 132). Their fuel keys alternate between the rank class of the h-ladder and that of the hp-ladder
  (E2's selectors ride E1's two roots). That is R156's two-source leapfrog: a reversal paid by the OTHER source's rise, with no reset of
  Ξ(z) at a more significant rank.
- So FUEL-DESC is dead with 25 violations (nep56_n32 has 1), but the reversals give one re-route per phase, not a counter.

## 2. READING: a pair cannot feed itself (the obstruction for «self-feeding»)
Let y be Even with successors z, w, inside a W-run (τ fixed).
- (a) While σ(y) = z, Ξ(z) is independent of y.
  - If y lies on z's Ξ-play, that play is a cycle y → z → … → y.
  - The cycle is closed through an Odd choice o, because W-plays cannot close it: a W-cycle would change λ_W and end the W-run.
  - If the cycle's top priority is even, Odd's optimal counterstrategy σ̄ leaves it at o (S1), so the Ξ-play from z avoids y.
  - If the top priority is odd, Ξ(y) under σ would be that Odd-won cycle, i.e. worse than Ξ before the switch y → z. That contradicts SI
    monotonicity (Ξ_(k+1) ⊵ Ξ_k for switches on improving edges, used in RESULTS R96/R97). So y cannot have switched to z.
- (b) While σ(y) = w and y lies on z's Ξ-play, Ξ(z) = Pref ⊕ Ξ(y) = Pref ⊕ Ξ(w), where Pref is the marker set of the path z → … → o → y.
  - So y's improvement test Ξ(z) ▷ Ξ(w) depends only on Pref (the sign of its top marker). It is the same at every visit unless Pref
    itself changes.
  - This is R159's self-reference (hd_H's gates), which fires once per change of Pref.
- So the rises of Ξ(z) that re-arm (y, z) are changes of Pref or of the part of z's Ξ-play outside y: they come from OUTSIDE the pair.
- A counter at one pair therefore needs an outside source whose Ξ rises many times per outer event.
- By SW-XI (R153: re-routes of y ≤ Σ over its successors of (1 + XICH)), the pair's fuel ≤ 1 + XICH_F(z) + 1 + XICH_F(w). That is
  bounded by the XICH of other vertices, which is R95's XI-CH-POLY again. There is no amplification inside the pair.
- Status: (a) and (b) are short arguments from SPEC S1 and SI monotonicity, given here as a sketch. They are not refereed and not
  lane-PROVED in a separate packet.

## 3. What would still give a counter (open)
- A pair (y, z) whose outside source s rises w times per outer event, where s is itself a pair re-armed by a source rising w′ times
  per its own events.
- This is the recursive leapfrog of R156 (composition (K_b + 1)(1 + WCH(u_b)) per level), with every level fed from below by
  re-armed waves.
- R157 realised one level (passive, capped by |F|); R158 showed the feedback needed to lengthen F binds once per phase; R160 found no
  re-armed wave at depth 3.
- The proof side's corrected FUEL-LEX (L-SI 36) is the natural place to bound it.

## DONE / FINDINGS / NEEDS
- DONE: this note (no new tools; srcfuel.py run unchanged on 9 instances, all pinned elsewhere). SHA: see the commit.
- FINDINGS:
  - DATA: MAXPAIR = the number of outer events on every instance (≤ 12; fbg: K). There is no second re-route of a pair inside one outer
    event.
  - DATA: FUEL-DESC has 25 violations without a reset on fbg_K4_m6_m24 / fbg_K8_m6_m24: two-source alternation, once per phase.
  - READING (sketch): a pair cannot feed itself. While y is on z, Ξ(z) is independent of y; while y is off z, the test depends only on
    z's prefix. So pair fuel is bounded by outside XICH (SW-XI), which is XI-CH-POLY again.
- NEEDS: none.
