# L-COMP box 29: N5 end-to-end on Γ3(G) of the tower genomes (Lead 07:08Z). Label: DATA (not a growth claim; G-N5-TIME stays OPEN)
L-COMP successor 10, 2026-11-07 (date -u in the commits).
## Pipeline
- Genomes (ext/): L-LOWER 4's H5_d20_F62 (claude/l-lower; H5 at c45cf2f3 and at 10cac3d9 are the same file, sha1 2204079d), H6_d24_F126 (10cac3d9),
  RECF4_d20_F60, DBL4_d20_F30 (experiments/lower/l4/rec/, read-only copies). Normalised by L-NEW's norm.py (order-preserving relabelling of
  gate indices and β-ranks to 0..M-1) -> inst/*_norm.json; my simulator (box27/sim.py) gives L(G) = 136, 209, 67, 30 on them (= the Lead's T).
- Γ3(G): L-NEW's builder gamma3.py with all pads {K, pe, pb, m}, written by writepg.py (claude/l-new fd1266a5, experiments/new/box189;
  copies in l-new/, run from a git-archive mirror at the original repo path) -> inst/*_g3.pg (+ .start = R104's stated start, not used).
- N5: MY n5b (experiments/n5-second/n5b.py) in SPEC mode from its default start S3 (best reward; n5b.N5.run with no start), run29.py.
  FL runs per RESULTS R104 / P-N5-REACH l. 39 («a maximal set of consecutive non-fallback transitions that keep τ, change σ and keep that
  valuation everywhere», the valuation of the (σ, τ)-play; computed with n5b's SpecSI on the game with σ and τ fixed).
  Bit cost (TARGET.md §3): per state, the largest valuation over all vertices of Even's valuation of σ and the dual valuation of τ;
  |P| = path-set size, dist = path length; bits := (|P| + 2)·⌈log2 n⌉.
- Answers (check29.py, out/check29.txt): Oink 8fbf0a7 `--zlk --verify -w 1` exit 0 «solution verified» on all four; n5b's winning regions =
  Oink zlk's; n5b's strategies pass experiments/harness/verify.py.
## Results (DATA)
| genome | genome sha1 | L(G) | Γ3 .pg sha1 | n | priorities (max) | iterations | fallbacks | FL runs [start, end] = length | FL = L(G) | max P-set size | max dist | max bits | N5 s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H5_d20_F62 | 2204079d | 136 | cb05531e | 610 | 168 (329) | 139 | 1 (transition 137) | [0, 136] = 136 | yes | 21 | 100 | 230 | 9.5 |
| H6_d24_F126 | fb37fec9 | 209 | 12eb2b86 | 730 | 200 (393) | 212 | 1 (transition 210) | [0, 209] = 209 | yes | 26 | 123 | 280 | 20.8 |
| RECF4_d20_F60 | 354b7d44 | 67 | 7e943e4b | 610 | 168 (329) | 70 | 1 (transition 68) | [0, 67] = 67 | yes | 19 | 100 | 210 | 4.9 |
| DBL4_d20_F30 | 43704358 | 30 | 77f41fd8 | 610 | 168 (329) | 33 | 1 (transition 31) | [0, 30] = 30 | yes | 17 | 100 | 190 | 2.1 |
- In every run: exactly ONE FL run, [0, L(G)], and exactly one fallback, at transition L(G) + 1; iterations = L(G) + 3. This is R117's
  REACH3 shape (P-N5-REACH l. 244-246) observed end to end on real .pg files with an independent N5 implementation.
- Bit cost stays small (≤ 280 bits per valuation, P-set size ≤ 26 at n = 730): no big-number effect on these runs.
- Not claimed: anything about growth in d; these are four instances.
## Comparison with L-RED 53 (Lead 07:10Z; read AFTER my runs finished)
- L-RED's n5v (SPEC mode) on the same Γ3 games (claude/l-red 2d5ce1ad r216/out/g3run.txt, as quoted by the Lead): 33 / 70 / 139 / 212
  iterations for DBL4 / RECF4 / H5 / H6 = MY n5b counts above (independent engines: n5b shares no valuation or arena code with n5v).
## N5'-xi (Lead 07:10Z add-on)
- L-NEW's n5bxi.py (claude/l-new 066cd543, sha1 6731655a, unmodified copy in l-new/; it subclasses my n5b and changes one rule), xi29.py,
  out/xi29.txt: DBL4 12 iterations / 1 fallback, RECF4 12 / 1, H5 12 / 1, H6 15 / 1; winning regions = Oink zlk on all four.
  = L-RED's reported 12 / 12 / 12 / 15. Note: n5bxi is L-NEW's own second implementation run here, not a third independent one.

## HIT7 (L-COMP 11, Lead 00:46Z 2026-11-08): N5 end-to-end on Γ3 of the first 7-capped tower (DATA)
- Genome: box30/out/L6_HIT7_F254_d28.txt (sha1 6a3b274d; F(0..6) = 2..254, T 299) -> replay30.py JSON hit7/HIT7_d28_F254.json -> L-NEW
  norm.py -> writepg.py (copies in l-new/, run from a scratch mirror at experiments/new/box189 with experiments/harness linked; the same
  pipeline regenerates inst/H6_d24_F126_g3.pg byte-identical) -> hit7/HIT7_d28_F254_g3.pg = inst/HIT7_d28_F254_g3.pg, sha1 8a360485
  (n 850, 232 priorities, max 457); Γ0 (no pads) hit7/HIT7_d28_F254_g0.pg sha1 3fac56bd.
- run29.py (MY n5b, SPEC, start S3): iterations 302 = L(G) + 3 with L(G) = T = 299; one fallback, at transition 300 = L + 1; one FL run
  [0, 299] = 299 (= L); max |P| 22, max dist 140, max bits 240; 39.6 s. Same REACH3 shape as H5 / H6 / RECF4 / DBL4 above.
- check29.py: Oink 8fbf0a7 --zlk --verify exit 0 «solution verified»; n5b regions == Oink zlk; harness verify.py on n5b's strategies OK.
- Not run: L-RED's n5v (second engine) on this game.
