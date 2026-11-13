# L-COMP BOX 48 (successor 22; Lead 12:28Z / 13:50Z 2026-11-13): independent check of L-RED-B 5's kill candidate G_k. All DATA.
Nothing here is a TARGET.md claim, a RESULTS entry or a referee signature. The statement under review is L-RED-B's (P-N5-EXP, frozen on
claude/l-red-b 350d84eb per the Lead); this box re-measures it with L-COMP's own generator, games and engines.

## What was run (exact commands, from this directory; env LNEW = archive of claude/l-new a32a588d, LRED = archive of claude/l-red 390e56f6)
1. `python3 -B gk48.py K inst/G_K.json` for K = 3..20 -> out/gen48.out. My generator, written from the rule as relayed by the Lead (not from
   L-RED-B's code). The four check sha1 of json.dumps(G) match the Lead's (G_3 cd3cd7e3…, G_4 7a2218bf…, G_8 d3ad8e2e…, G_10 da29d33e…).
2. `python3 -B run48a.py 3 16`, `python3 -B run48a.py 17 20`, `LRED=… python3 -B run48a.py 3 10 --ideq` -> out/run48a_*.out. The C port of
   1P(G) (box47/bin/one47, checked in BOX 47 = one217.py = n5v spec = IDEAL ideal.traj) with rules key / howard / seq.
3. `LNEW=… python3 -B run48b.py 3 12` -> out/run48b.out (resumable per k). Γ3(G_k) by MY builder box34/own34.build, S3 by own34.standard,
   written to inst/G_K_g3.pg + .start. On that game:
   - n5b --mode spec (experiments/n5-second/n5b.py) runs to the end;
   - its winners are compared with Zielonka (harness zielonka.py, «wrong»), and its strategies go through the harness verifier («verr»);
   - its (iterations, fallbacks) are compared with L-NEW's n5v spec on L-NEW's own Γ3 (box47/replay47.py, «engdiff»);
   - controls: n5b --mode xi (engdiff_ctrl), one flipped Zielonka winner (wrong_ctrl).
4. `bash ../../../scripts/setup_oink.sh` (Oink pinned 8fbf0a7), then `python3 -B oink48.py 3 12` -> out/oink48.out. Oink --tl and --zlk with -v,
   winners against n5b's; control: one flipped n5b winner.

## Results (files and sha1; numbers in the files)
| file | sha1 | content |
| --- | --- | --- |
| out/gen48.out | 41441e41f87a | G_k, k = 3..20: N = 9k − 16, M = 2N, d = k + 1, sha1 of each genome |
| out/run48a_k3_16.out, out/run48a_k17_20.out | 193e8400f26a, 0dfcc0976b8e | C port: T_key = 2^k − 2 exactly for k = 3..20 (1,048,574 at k = 20, N + M 492); max_x sw = 2^(k−2); per-level max sw 1, 1, 2, 4, …; T_howard 4 (k ≥ 4); T_seq 10 … 382 |
| out/run48a_ideq_k3_10.out | 2bc89ec29854 | ideal.traj = C key run state by state, k = 3..10 (ideq 0) |
| out/run48b.out | 6ec008a39c9d | N5 on Γ3(G_k), k = 3..12 (n = 135k − 230 = 175 … 1,390): n5b spec 2^k + 1 iterations, 1 fallback; n5v spec the same (engdiff 0), first fallback at step 2^k − 2; wrong 0, verr 0; controls fire |
| out/oink48.out | 53ce8ce777b7 | Oink --tl and --zlk: verified, winners = n5b's (owrong 0) for k = 3..12; control fires |
| inst/SHA1SUMS | | the genomes (json), games (pg) and S3 starts |

## Reading (DATA, k = 3..12 on the game, 3..20 in the model; not a proof)
On the rule-built family G_k (Ξ-acyclic, degree 2, N + M = 27k − 48):
- N5 (SPEC key rule) from S3 on Γ3(G_k) takes 2^k + 1 iterations: two independent N5 implementations on two independently built games, k = 3..12;
- the model run 1P(G_k) = IDEAL L(G_k) = 2^k − 2 for k = 3..20;
- the winners are correct (Zielonka, Oink tl / zlk, strategy verifier).
Through k = 12 the measured iteration count is exactly 2^k + 1, which grows exponentially in the game size n = 135k − 230. Whether this
is a kill of N5 rests on the referees' reading of R117 and of the family's general-k proof (L-RED-B's P-N5-EXP), not on this box.
