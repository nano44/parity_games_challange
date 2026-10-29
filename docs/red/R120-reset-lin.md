# R120: CONJECTURE RESET-LIN is false. An observer on R106's mkr makes K(m − 1) MATCHED P-changes in one λ-run at n = 7m + 7 (m = 4K): 1008 > n = 455 at K = 16, Θ(n²). Two engines state by state, two independent counters, Oink. DATA; reader inflation, the σ-run is mkr's
L-RED successor 30 (Opus 5.5; D1/D18; Lead 20:29Z: "your sharpest target is now a family with super-linear matched resets per vertex
per λ-run (kills RESET-LIN)"). Written 2026-10-29 from 20:50Z (date -u). Labels: DATA / READING / DEAD / OPEN. Not a TARGET.md claim.
Target: L-SI 29, claude/l-si 88a953f5, docs/si/N5-RESET-box35.md §2: "CONJECTURE RESET-LIN: for every N5 run, every vertex x and every
λ-run R (λ^U-run on G^d for Odd), #MAT_R(x) ≤ n." MATCHED is RESULTS R85's definition (M1)-(M3). Corpus data: max #MAT / n = 0.75.

## 1. The family (DATA)
- Base: experiments/red/seg/mkr.py K m (R106, unchanged), from its designed start. Its run is one λ-run: Ξσ's cycle-node map stays
  constant, and every Ξ-play ends at z. Even's reactors r_1..r_m flip one per transition, in a wave down the chain, about K times
  (2 waves per pivot cycle; R106 §2).
- Observer (experiments/red/mix/obs2.py):
  - Odd vertex o, priority 0, no in-edges, with edges to y_1..y_m.
  - y_j is Odd with a single successor r_j and priority q_j = Z − 1 + 2j: even, just above z's priority Z, increasing in j. Every
    original priority above Z is shifted by 2m + 2, which keeps parities and the order.
- Why it counts (READING, checked in the trace below). Ξσ(o) is Odd's minimum over {q_j} ⊕ Ξσ(r_j).
  - Inside a wave the flipped reactors have the higher value, so the minimum is the unflipped reactor of smallest q_j, i.e. the next
    one to flip.
  - Each wave step moves o's P-set by "out y_j, in y_(j+1)": an even rank out, a higher even rank in. That is MATCHED.
  - At each wave end the whole wave's change shows (a carry or a matched reset).
- o and the y_j reach no other vertex, so neither σ's run nor anyone else's valuation changes. On every member the run has the same
  state count as mkr's.
- Trace, K = 4, m = 16, vertex o:
  - t 2-16: in y_(j+1), out y_j (15 steps);
  - t 17: in Bq1, a16 … a1, out Bqp0 (wave end);
  - t 19: in Bqp1, y1, out Bq1, a16 … a1, y16;
  - t 21-29: y_j → y_(j+1) again.
- Counts (matc.py: n5b SPEC, MATCHED per R85 via two one-sided matchings, Mendelsohn-Dulmage):
  | K | m | n | iterations | λ-runs | max #MAT (vertex o) | #MAT / n | fit K(m − 1) |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | 4 | 16 | 119 | 76 | 2 | 60 | 0.504 | 60 |
  | 8 | 32 | 231 | 280 | 2 | 248 | 1.074 | 248 |
  | 12 | 48 | 343 | 612 | 2 | 564 | 1.644 | 564 |
  | 16 | 64 | 455 | 1072 | 2 | 1008 | 2.215 | 1008 |
  - The second λ-run is the final state only.
  - Also runquad_K8_m30_n192 + observer: n 223, #MAT 232 > 223.
  - With m = 4K: #MAT = 4K² − K = Θ(n²) (n = 28K + 7). RESET-LIN fails from K = 8 on.
- Checks:
  - Second engine: seg/xeng.py (L-NEW's n5.py driver on L-SI's si.py valuations). State sequences are IDENTICAL to n5b's at K = 4
    (77 states) and K = 8 (281). K = 12, 16: addendum.
  - Independent counter: L-NEW's box21 n5x engine + L-SI's compose.matched (the functions L-SI's carx.py uses; scratch wrapper,
    SIDE=E form). #MAT at o = 60 / 248 / 564 at K = 4 / 8 / 12, equal.
  - Oink: n5b's solution checked by experiments/new/check_sol2.py: "zielonka(oink zlk) OK strategies verified" at K = 4, 8, 12.
    K = 16: addendum.
  - Odd mirror: ctl/dualize.py of K = 8. SIDE=O (Ξτ on G^d) gives #MAT^U = 248 at n 231, so the λ^U-run form fails too.
- Pins (experiments/red/mix/instances/, sha1 first 12):
  - wobs_K8_m32.pg ec3fb888367e, .start 13075ecab4ec;
  - wobs_K16_m64.pg 6e60c326d94d, .start cf2a38638173;
  - d_wobs_K8_m32.pg 0abcf35e80d0, .start 92ef2c5b6662.
- check.sh gate: mkr.py 8 32 + obs2.py regenerates wobs_K8_m32 byte for byte; matc.py on K = 4 gives max #MAT 60.

## 2. What dies, what stays (READING)
- DEAD as stated: RESET-LIN (#MAT_R(x) ≤ n per vertex per λ-run), on both sides.
- It dies by READER INFLATION: o observes a run it does not affect. So a per-vertex matched count can be made as large as the run
  itself (#MAT(o) = K(m − 1) against T = K(m + 3) + O(1) transitions here). Any surviving per-vertex law must therefore allow #MAT ≈ T,
  and so it is as strong as a bound on T. This matches NOW.md's standing reading that per-vertex counts are reader-inflatable.
- Not touched:
  - CARRY-SEG. The observer has K + O(1) carries, at wave ends, between long matched stretches.
  - PCH-QUAD (PCH_R(x) ≤ n² + n). Here PCH(o) ≤ T = O(K·m) < n² / 100.
  - The implication CARRY-SEG + RESET-LIN ⇒ O(n⁶ m) (arithmetic). It is unaffected but now has a false premise.
  - The weaker form "#MAT ≤ poly(n)" holds here, because T is polynomial on mkr.
- For the G-N5-TIME composition (R86 (d), (e)'s per-vertex premise): per-vertex P-change bounds must hold for observers too, so they
  hold only when T itself is bounded. A useful replacement must count something an observer cannot inflate, e.g. P-changes of the
  vertices whose own strategy switches (box 28 SW-RISE charges each switch to a rise of the switching vertex) or of the targets of
  switching edges. OPEN which such restriction keeps R86's arithmetic.

## DONE / FINDINGS / NEEDS
- DONE: mix/matc.py (#MAT / NM per vertex per λ-run from R85's text), mix/obs2.py (wave observer), pins, check.sh gate, two engines,
  two counters, Oink, Odd mirror.
- FINDINGS:
  1. DATA: observer #MAT = K(m − 1) in one λ-run; 1008 > n = 455 at K = 16, Θ(n²). RESET-LIN DEAD (both sides).
  2. READING: the kill is reader inflation; per-vertex matched counts are bounded only by T, so RESET-LIN-type laws need a restriction
     to vertices an observer cannot be (switching vertices or switch targets).
- NEEDS: none from the owner.
