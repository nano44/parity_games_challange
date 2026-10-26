# (h3_D) and not (NC) states that stay in-phase (L-COMP box 10 item 2, for L-SI; Lead 2026-10-26 06:48Z)
Source: gdnc_check.rand_ckO random C^kO games (k 2-4, n 5-16, rng seed 5; the box 9b tau-change census). Each .start is the state k
itself, (sigma_k, tau_k): from it the run's first transition k -> k+1 is non-fallback, keeps tau and lambda_Xi (same phase), and (h3_D)
holds while (NC) fails at k (a disagreement gate on its own honest or W-cycle). check_instance OK on all (n5b states equal, regions =
Oink zlk, strategies verified). DATA. Columns: D_k at the start state; whether (NC) holds again at k+1; N5 iterations from the start.
| instance | sha1 | n | D_k | (NC) at k+1 | iterations |
| --- | --- | --- | --- | --- | --- |
| notnc1_n16 | 86c00252160f84954322c1f2cccdadf36cdca400 | 16 | [10] | yes | 1 |
| notnc2_n9 | 23342c45c3857245de443f387ec018a0610c6fb0 | 9 | [3] | yes | 2 |
| notnc3_n16 | 4226af28cf2d923fded26438f2bae36a85f6cb3f | 16 | [6] | no | 1 |
| notnc4_n12 | 257c693267737353d2a7323f7ca5a810045459f8 | 12 | [7, 11] | no | 1 |
| notnc5_n5 | 7e880bd4b9a3b2ab3c36877a82bd87360ebe3026 | 5 | [1] | no | 1 |
| notnc6_n15 | 8bd264f792bbf314cf52da937af16b6206143e4b | 15 | [7] | no | 1 |
| notnc7_n11 | 89f912a5d64fc4179bcc4524ac751b92ae0d5d5d | 11 | [8] | no | 2 |
| notnc8_n15 | 85b8ed1041681c3ebf3b7f934e95865012515421 | 15 | [6] | no | 5 |
Observation (DATA): in 6 of 8 the in-phase step from the not-(NC) state is the run's LAST transition (1 iteration), i.e. the state is one
step from the end of N5; only notnc2, notnc7, notnc8 continue.
