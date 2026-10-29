# N5-DW (box 62): on dwN (fcN + escape-chain repeaters) N5-SF is EXPONENTIAL: F makes I^glo's 19·2^N − 18 steps, σ̄ is a full binary counter, and the cause is LATENCY at every set. Plain N5 is not.
L-NEW successor 34 (Opus 5.5), D14 / D18, Lead reading L40. Lead's heads-up 2026-10-29 18:39Z (L-RED 29's dwN, unpushed). I did not
wait for the push: I REBUILT dwN from the Lead's description and reproduced L-RED's numbers exactly. Written 2026-10-29 from 18:50Z
(date -u). Working note, unrefereed, not a TARGET.md claim. Labels: PROVED (lane) / DATA / READING / CONJECTURE / OPEN / DEAD.
All runs from the SPEC S3 default start. Engines: box54/n5sf.py (N5-SF), box21/n5x.py trace (plain N5, asserted equal to n5.run).

## 0. The family (my rebuild; NOT byte-compared with L-RED's generator, which was not pushed when I wrote this)
- experiments/new/box59/dw.py N. Start from fcN (experiments/red/sf/sbev.py N --drop fc).
- For i = 0..N − 2, add an Even repeater u_i. The edge v_i → r_(i+1) is replaced by v_i → u_i, and u_i → {r_(i+1), v_(i+1)}.
  - For i = N − 2, where v_(N−1) does not exist, u_(N−2) → {r_(N−1), p}. This is my reading of the description.
- u_i gets priority 3 (odd, just above q's 1). Every other priority ≥ 2 is shifted up by 2(N − 1) + 2. So n = 26N + 9.
- sha1 (12): dw_3 67eb4bffcfd1, dw_4 19783274245b, dw_5 f19234a6565c, dw_6 e817c1f19fd9, dw_7 cc4257b82a85.

## 1. DATA
| N | n | N5-SF iterations | 19·2^N − 18 | F steps / I^glo steps (fglo.py) | SBC_σ = SBC_G | 2^(N+1) − N − 2 | max Gflips (= h_0's flips) | plain N5 iterations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 87 | 134 | 134 | 134 / 134 | 11 | 11 | 7 | 41 |
| 4 | 113 | 286 | 286 | 286 / 286 | 26 | 26 | 15 | 47 |
| 5 | 139 | 590 | 590 | 590 / 590 | 57 | 57 | 31 | 55 |
| 6 | 165 | 1198 | 1198 | not run | 120 | 120 | 63 | 62 |
| 7 | 191 | 2414 | 2414 | not run | not run | 247 | | not run |
- The iteration counts equal L-RED 29's reported 134 / 286 / 590 / 1198 / 2414 and I^glo's switchbestexp counts (box 57).
- F and I^glo take the same NUMBER of steps on dw_3..5, but their trajectories differ from step 72 on (fglo.py: first divergence 72,
  DIFFER). So "F = I^glo" holds for the step counts, not state by state.
- σ̄'s flip word is EXACTLY the N-bit binary counter: each increment sets the lowest 0 bit k, then resets k − 1, …, 0 top down
  (box59/dwopen.py, N = 3..5: BINARY). So SBC_σ = SBC_G = 2^(N+1) − N − 2, and every σ̄-change is F-relevant.
- Max Gflips = 2^N − 1 at h_0. That is < n up to N = 7 (127 < 191), and exceeds n at N = 8 (255 > 217, §4).
- Fallbacks 0, LAM 0. N5-SF's output regions on dwN were NOT checked against a reference solver here.

## 2. Mechanism in LATENCY terms (DATA, dwopen.py, N = 3..5: PASS at every set of a bit k ≥ 1)
- On fcN (box 59), only a RECORD gave the lane a one-F-step lead over the escape chain, because only there did the chain need an extra
  hop (z_(k−1) → v_(k−1) after v_(k−1) → r_k). At a re-set the chain was prepared.
- The repeater u_i puts an extra hop on EVERY chain link v_i → u_i → r_(i+1). Its priority (odd, just above q's) makes it worthless
  as an end, so v_i → u_i is not improving until Ξ(u_i) has changed. By Lemma LATENCY (box 59, PROVED) that costs one F-step per link.
- Hence at EVERY set of bit k:
  - the lane carries m_k one step before f_(k−1)'s escape does (dwopen: at the state before cycle k − 1 opens, a_0 has m_k and
    f_(k−1) has not);
  - every escaping lower cycle opens in the gap;
  - all lower bits reset (cascade).
  Unary-with-records (fcN, N²) becomes a full binary counter (2^N).
- The lane walk per re-set gives the 19·2^N leading term: the step count of a binary counter whose increments each cost a lane walk.

## 3. Consequences (labels as stated)
- CONJECTURE SF-POLY: DEAD (DATA N = 3..7; formula 19·2^N − 18 exact on all five). Instance dw_7 (cc4257b82a85, n 191): 2414
  iterations. N5-SF is out as a polynomial candidate, unless dwN's output is wrong. That would not save it: the count stands either way.
- CONJECTURE I-CUBIC (box 61): DEAD on the same instances. dw_7: 2414 ≤ 191³/32 still holds, but 19·2^N outgrows any c·(26N + 9)³
  (N ≥ 14 for c = 1/32).
- CONJECTURE SBCG-QUAD: DEAD in growth (SBC_G = 2^(N+1) − N − 2). CONJECTURE SBC-QP (quasi-polynomial SBC): DEAD too, SBC = 2^(N+1) − N − 2 with n = 26N + 9.
- CONJECTURE PV_G: DEAD, dw_8 (§4): 255 F-relevant flips at h_0 > n = 217.
- What stays PROVED (lane): SF-TERM, DECOUPLE, SF-RED (the frozen packet), SF-RED-G, SF-RED-R (under LOC), Lemmas COUNT, LATENCY,
  DEPTH-COUNT, Theorem DEPTH-BOUND (conditional). All are reductions or counting lemmas. dwN shows that the quantity they reduce to is
  exponential.
- READING. The single frame (Odd's best reply as the arena opponent) is what makes LATENCY bite. With every hop costing one F-step
  against an ALWAYS-fresh opponent, a gadget can always make the lane faster than the escape. Plain N5's two-frame step (Even against
  the current τ, Odd moving at the same time) gives 41, 47, 55, 62 iterations on dw_3..6: about +7 per N, no exponential. N5's stale τ
  is what breaks the race here, the converse of box 57's finding on switchbestexp.

## 4. N = 8 (DATA, box59/dw8_sbcg.txt)
- dw_8 (n 217, m 496, sha1 64f954f37903): 4847 distinct σ, so I = 4846 = 19·2^8 − 18. SBC_G = SBC = 502 = 2^9 − 8 − 2. SEGMAX 57. The
  SF-RED-G bound holds (PASS).
- max Gflips = 255 = 2^8 − 1 at h_0, and 255 > n = 217. CONJECTURE PV_G is DEAD, instance dw_8.

## DONE / FINDINGS / NEEDS
- DONE: box59/dw.py (own rebuild), out/dw_3..8.pg, fglo.py, dwopen.py, dw_iter.txt, dw_sbcg.txt, dw8_sbcg.txt; check.sh "Box 59" pins dwopen on dw_4; plain-N5 counts; this note.
- FINDINGS: (1) DATA: N5-SF on dwN makes exactly 19·2^N − 18 iterations (N = 3..7), L-RED's numbers reproduced independently; σ̄ is a
  full binary counter, all of it F-relevant. (2) The mechanism is Lemma LATENCY at every set, created by the repeater's extra hop.
  (3) DEAD: SF-POLY, I-CUBIC, SBCG-QUAD; PV_G (dw_8: 255 > 217). (4) DATA: plain N5 on dw_3..6 makes 41, 47, 55, 62 iterations.
- NEEDS: none from the owner. Lead: L-RED's dw generator SHA, to byte-compare with mine. Plain N5 on larger dwN is L-RED / REFEREE-2's
  measurement; my 4 points are a cross-check only.
