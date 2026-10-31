# Box 26: XICH_F(v), the core quantity, per W-run of N5 (L-COMP successor 8, last box before parking)
Lead 2026-10-31 04:38Z (D18). Since RESULTS R95, WRUN-POLY ⟺ XI-CH-POLY. XICH_F(v) := the number of transitions of the W-run F at
which Ξ(v) changes. Measured: max_v XICH_F(v) and Σ_v XICH_F(v), against |F| and n, on the corpus and on the pins, and by climbs.
Work 04:50Z-06:3xZ (date -u). Labels: DATA / CONJECTURE / READING. Not a TARGET.md claim; G-N5-TIME open.

## Tool and cross-check
- xich.py: my own count on n5b (SPEC). W-runs as box 23 (R89); Ξ_t is n5b's VJ valuation of σ_t; a change is any change of the
  (cycle node, path set, length) triple. Per W-run: |F|, max_v XICH (and v), Σ_v XICH, and the longest W-constant interval |I|.
- xxich.py vs L-NEW's xirise.py 'xich' (box 85, committed new/box85/xirise_{sbcg,alt}.txt): 1,132 / 1,132 corpus games agree
  (results/xxich.txt).
- Every pin below: xirise.py run unchanged gives the same max XICH.

## 1. Corpus (1,132 runs)
- Max XICH / n: 1.06 on pftheta34_n32 (XICH 34 = |F| = 34: one vertex's Ξ changes at EVERY transition), 1.03 on pftheta_cex_n32,
  0.81 on x31_cu16, 0.73 on pft35_n48.
- Max absolute: 63 on gate_K64_n581 (0.11n), then 50 on pp_K48_n449 and 49 on ladderd0_k48_n156.

## 2. Pins named by the Lead (results/pins.txt)
| pin | n | it | W-runs | max XICH (v) | |F| of that run | Σ_v XICH | |I| | max XICH / n | |F| / n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sbq2_K8_m16 | 261 | 152 | 1 | 136 (260) | 151 | 2,849 | 0 | 0.52 | 0.58 |
| obs_K12_m24 | 272 | 324 | 1 | 301 (247) | 324 | 4,109 | 0 | 1.11 | 1.19 |
| latew_K8_m32 | 370 | 280 | 1 | 17 (218) | 280 | 3,961 | 0 | 0.05 | 0.76 |
| latew_K16_m32 | 482 | 560 | 1 | 33 (330) | 560 | 9,297 | 0 | 0.07 | 1.16 |
| cedge_n32 | 32 | 31 | 2 | 12 (0) | 26 | 164 | 0 | 0.38 | 0.81 |
| ping_n48 | 48 | 37 | 2 | 12 (45) | 31 | 346 | 0 | 0.25 | 0.65 |
| nest_n64 | 64 | 68 | 2 | 21 (20) | 53 | 679 | 0 | 0.33 | 0.83 |
| keych10_n32 | 32 | 22 | 1 | 11 (15) | 19 | 126 | 7 | 0.34 | 0.59 |
| tie_n32 | 32 | 15 | 1 | 12 (15) | 13 | 194 | 7 | 0.38 | 0.41 |
| kr35_n30 (box 24) | 30 | 12 | 2 | 9 (6) | 10 | 161 | 0 | 0.30 | 0.33 |

## 3. The family where max XICH grows faster than linearly (independent reproduction of L-RED R139)
- R139 (docs/red/R139-xich-funnel.md): the Even wave observer on one-world mkr (`OWNER=0 ABOVE=a red/mix/obs2.py` on
  `red/span/mkrw.py K m`). Regenerated here; obs_K12_m24 is byte-identical to the pin (sha1 7df541fb…). Counted with xich.py
  (results/obs_family.txt). One W-run each:

| K | m | n | |F| | max XICH (at the observer) | K·m + K + 1 | Σ_v XICH | max XICH / n | |F| / n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 8 | 96 | 44 | 37 | 37 | 477 | 0.39 | 0.46 |
| 8 | 16 | 184 | 152 | 137 | 137 | 1,845 | 0.74 | 0.83 |
| 12 | 24 | 272 | 324 | 301 | 301 | 4,109 | 1.11 | 1.19 |
| 16 | 32 | 360 | 560 | 529 | 529 | 7,269 | 1.47 | 1.56 |
| 20 | 40 | 448 | 860 | 821 | 821 | 11,325 | 1.83 | 1.92 |

- DATA: max XICH = K·m + K + 1 exactly on all five sizes. That is R139's formula; K20_m40 (n 448) is a new size.
- With m = 2K, n = 22K + 8: max XICH ≈ n²/242. This is QUADRATIC at ONE vertex, and max XICH / n grows linearly in K.
- DATA: Σ_v XICH is ≈ 13.2|F| on this family, against n ≈ 0.52|F| at K 20. So Σ_v XICH grows like n·|F|, cubically in K.
- latew contrasts with it: max XICH = 2K + 1 (17, 33) is linear, while Σ_v XICH is quadratic (R139 §1: spread over many vertices).

## 4. Climbs (climb26.py; fitness (max XICH_F(v) in one W-run, |F|, longest W-constant interval |I|); start pair mutated)
| n | family | budget | steps | max XICH | |F| | |I| | max XICH / n | |F| / n | witness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 16 | fresh | 900 s | 65k | 12 | 13 | 0 | 0.75 | 0.81 | xich12_n16 |
| 32 | fresh | 900 s | 56k | 11 | 11 | 0 | 0.34 | 0.34 | |
| 48 | fresh | 900 s | 15k | 14 | 25 | 0 | 0.29 | 0.52 | |
| 32 | seeded tie_n32 (12) | 1,800 s | 62k | 14 | 15 | 8 | 0.44 | 0.47 | |
| 32 | seeded keych10_n32 (11) | 1,800 s | 58k | 14 | 18 | 8 | 0.44 | 0.56 | xich14_n32 |
| 48 | seeded ping_n48 (12) | 1,800 s | 14k | 31 | 33 | 0 | 0.65 | 0.69 | xich31_n48 |
| 48 | seeded cedge_n32 (12), padded | 1,800 s | 13k | 28 | 31 | 0 | 0.58 | 0.65 | |

- Pins (n5-box23/pin23.py ALL OK: n5 = n5b, Oink zlk, verify, xeng, rstar = xirise; xirise 'xich' equal):
  - xich12_n16 b914a7a8591c…
  - xich14_n32 ecaab74b8e5a…
  - xich31_n48 c4140eb66967…
- On the pinned climb witnesses max XICH / |F| is 0.92, 0.78, 0.94 (12/13, 14/18, 31/33): one vertex's Ξ changes at most transitions
  of its W-run. The fresh n 48 best has 14 / 25 = 0.56.

## 5. Findings
1. DATA: xich.py = xirise.py on 1,132 / 1,132 corpus games and on every pin.
2. DATA: yes, one family has max XICH growing faster than linearly: R139's observer, max XICH = K·m + K + 1 ≈ n²/242. This is reproduced
   independently on 5 sizes up to n 448 (821 = 1.83n). Every other pin and climb has max XICH ≤ 1.11n.
3. DATA: in every W-run measured, max XICH ≤ |F|, which holds by definition. The extremes sit at max XICH ≈ |F|: obs family 0.95|F|,
   pftheta34 1.0|F|, pinned climb witnesses 0.78-0.94|F|. So max XICH and |F| move together, and XI-CH-POLY is the same question as WRUN-POLY (R95 /
   R139 §3).
4. DATA: fresh climbs give max XICH / n 0.29-0.75 (smaller at larger n, budget-limited). Seeded climbs from ping_n48 / cedge_n32 jump
   from 12 to 31 / 28 at n 48.
5. CONJECTURE (data only): no W-run measured here, built or climbed, has max XICH or |F| above quadratic in n. The largest ratio
   |F| / n² found is 0.0043 (obs K20_m40). Whether a W-run can be super-quadratic, nesting the observer funnel, is open. That is the
   construction question (R139 §3, the nesting suggestions of boxes 23 / 104).

## Files
xich.py, xxich.py, climb26.py, check.sh (in verify), instances/ (pins), climbs/ (each climb's best .pg/.start, climbs_end.txt), results/
(xxich.txt, pins.txt, obs_family.txt).
