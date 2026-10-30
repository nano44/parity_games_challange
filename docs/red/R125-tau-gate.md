# R125: route (A), the bounded try. A main chain whose hops wait for a shared second chain (mk3f.py) dies on τ-stability: Odd moves every gate to its honest option in the first two transitions and never moves it back, and the run is mkr's to the iteration. READING: the gate's W-signal must read the previous hop, so Even's best reply from the signal route reaches everything the honest option reaches, plus a good marker. Odd's U then never prefers the signal route, so a τ-tick can open a gate but never re-close it. OPEN; the lane parks here
L-RED successor 31 (Opus 5.5; D1/D18; Lead 2026-10-29 23:35Z: "Go for (A), τ-ticks, as one bounded try. A reused gate re-closes at a
phase boundary, the only place W can fall ... Stop at the first clear obstruction, write it down precisely"). Written 2026-10-29 from
23:45Z (date -u). Labels: DATA / READING / OPEN. Not a TARGET.md claim; G-N5-TIME OPEN.

## 1. The design (experiments/red/span/mk3f.py K m P; built on mkr.py; nothing climbed)
- Goal: λ-run ≈ K·m·P. Each main hop r_(j−1) -> r_j waits for a full wave of a SHARED bidirectional chain s_1..s_P (as mkrb, R124).
- Chain-2 sources (they re-arm on their own, R124 §3): Even observers o_odd, o_even -> y_k (Odd, even marker q_k) -> r_k over odd and
  even k. Hop j − 1 (odd) lifts o_odd, a down-wave runs to s_P, hop j − 1 (even) lifts o_even, an up-wave runs to s_1.
- Gate j ≥ 4, W-thresholded (not Ξ-thresholded as in R108's mk3):
  - a_j (Odd) -> {r_(j−1) honest, c_j τ}, c_j -> s_P (j even) or s_1 (j odd). W(a_j) carries q_(j−1) once chain 2 has delivered hop
    j − 1, and q_(j−2) before.
  - b_j (Odd) -> {h′ honest, β_j τ}, β_j (Even) -> {g_j -> h′, k_j (even marker t_j, q_(j−2) < t_j < q_(j−1)) -> r_3}. During the
    h-wave W(b_j) = t_j ⊕ (h's world). At the h′-step β_j moves to h′, so W(b_j) follows h′ and r_j flips back. β_j returns to the
    h-side only after hop 3, so the observers can re-arm first (both moves are W rises inside the phase).
  - This avoids R108 §4: the threshold is in W and both sides are in h's world, so the honest values of the chain are untouched.
- Bands above z: BA < gb < A2 (chain-2 markers) < q/t < ladder.

## 2. DATA: it collapses at once (n5b SPEC; seg/tr.py trace)
| K | m | P | n | iterations | mkr.py K m (no gates, no chain 2) |
| --- | --- | --- | --- | --- | --- |
| 2 | 8 | 4 | 96 | 22 | 22 |
| 2 | 8 | 8 | 108 | 22 | 22 |
| 3 | 8 | 8 | 120 | 33 | 33 |
| 3 | 12 | 12 | 164 | 45 | 45 |
- Trace (K 2, m 8, P 4):
  - Transition 0: τ a4: c4 -> r3, a6, a8 likewise; τ b4..b8: β_j -> h′.
  - Transition 1: τ a5: c5 -> r4, a7 likewise.
  - These are the only τ-changes in the run. Every gate is then the plain mkr link, and the iteration count equals mkr's at every row,
    whatever P is.
- So the τ-ticks occur, but they OPEN the gates, once, at the start. Nothing re-closes them.

## 3. READING: why Odd cannot re-close (and at first sight never keeps) a reused W-gate
- Frame: Odd moves τ(x) from option A to option B only if (x, B) ∈ I_τ (U-improving for Odd: U(B) ◁ U(A), Even scale) and S4b picks it.
  U is Even's best reply against τ; Ξ ⊴ W ⊴ U pointwise.
- Gate requirements at a_j:
  - (H) honesty: Ξ(c_j) ⊵ Ξ(r_(j−1)), so that the main chain's Ξ order is r_(j−1)'s;
  - (S) stability, or re-closing by a τ-tick: U(c_j) ⊴ U(r_(j−1));
  - (D) decision: W(a_j) vs W(b_j) decided at the hop-information rank (q_(j−1) vs t_j). So every higher rank on the two W-plays must
    lie on both.
- (I) Information: W(c_j) must change when hop j − 1 has been delivered. So c_j's W-play reads a vertex whose W follows r_(j−1). In
  mk3f that is the observer's choice y_(j−1) -> r_(j−1). The observers' re-arming (R124 §3) needs y_k's play to pass through r_k: a stale
  y_(m−1) must be W-below a fresh y_1 at the start of a cycle.
- Then Even's best reply from c_j can follow c_j -> chain 2 -> o -> y_(j−1) -> r_(j−1) and continue exactly as Even's best reply from
  r_(j−1) does (o and the s_k are Even, y_k is single-successor). The prefix carries the good even marker q_(j−1), above the BA and A2
  markers. So U(c_j) ⊳ U(r_(j−1)) at EVERY state, and (S) fails permanently. (a_j, r_(j−1)) is in I_τ from the start. It is W-better for
  Odd too: W(c_j) has the same good prefix over W(r_(j−1)). S4b takes it at once, and τ can never return to c_j.
- The ways out each break another requirement:
  - Cycle-node separation (mkr's own τ-stability device: honest escapes reach a better loop): r_(j−1)'s better loop is reachable from
    c_j through the same prefix. Fails.
  - An odd marker ω above the hop band on c_j's prefix (so the prefix is net-bad for U):
    - on a vertex of the Ξ-play (y_k -> ω_k -> r_k): Ξ(c_j) drops below Ξ(r_(j−1)) at the same ladder level, so (H) fails;
    - off the Ξ-play but on the W-play: then by (D) it must also lie on b_j's W-play. A W-play continues uniquely after a common vertex,
      so the hop information after ω is shared by a_j and b_j. With ω_(j−1) placed between y_(j−1) and r_(j−1), the ω's must decrease
      in j for (D) before completion. But ω_(j−1) on y_(j−1)'s single route is on o's Ξ-play, so this is the first case again.
  - Taking the information from o's CHOICE only (y_k with τ -> a world source E, W(o) = q_(σ o) ⊕ W(E), not through r_k): (S) can then
    hold via cycle nodes. But the observers cannot re-arm in W: W(y_1) and W(y_(m−1)) differ only by q, so o stays at y_(m−1) after the
    first cycle (R124 §3 needs the stale world on y_(m−1)'s play).
- This is the same death as R108 §5's mk3 v1 ("dies first on τ-stability"), now with the reason located. A REUSED gate needs a signal
  route that reads the previous hop AND that Odd's U rates below the honest route. Reading the hop gives Even's best reply the honest
  route's continuation plus the reader's marker. NOT a proof: it is argued for observer-type signals (the only reusable sub-clock found,
  R124 §3), and assumes (D).

## 4. Resume point (OPEN, for a successor; the lane parks)
- (A′) A signal that reads hop j − 1 through an ODD reader whose τ blocks Even's best reply (U) but whose σ̄ (Ξ) and W-play still pass:
  W uses τ too, so this needs W and U to differ at an Even vertex on the route, where σ differs from Even's best reply against τ.
  That is a "permanent support" in R113 §3 (i)'s sense. Not tried.
- (B) length thresholds and (C) digit-parity worlds (R108 §6): untouched.
- RUN-QUAD / PCH-QUAD-S: no kill; best λ-run ≈ n²/77 (R124).

## DONE / FINDINGS / NEEDS
- DONE: span/mk3f.py, the trace, this note. No pin: the instance reduces to mkr.
- FINDINGS:
  1. DATA: mk3f's gates collapse in transitions 0-1 (τ to the honest options); the iterations equal mkr's at every row.
  2. READING: a reused W-gate fed by an observer is never U-stable. The reader's play gives Even's best reply the honest option's
     continuation plus a good marker. So Odd's τ-ticks open such gates (once) and never re-close them.
  3. OPEN: (A′) a U-blocking reader with a permanent support; (B); (C).
- NEEDS: none from the owner.
