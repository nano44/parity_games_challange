# Box 12: epoch census for N5 (L-COMP successor 5, Opus 5.5; Lead GO 2026-10-26 07:57Z)
D18 / L40. Every number here is DATA (not proof). Labels: DATA / READING. Nothing here is a TARGET.md claim; G-N5-TIME stays open.

## Code (L-COMP's own; no other lane's code imported)
- `census.py`: runs N5 with `experiments/n5-second/n5b.py` in SPEC mode (L-COMP's independent implementation, equal to n5.py state by state
  on 22,810 runs, box 9; `fbtrace` hook added 2026-10-26, no effect on the run) and measures, per phase (R38 (a): (λ_Ξ, τ) constant) and per
  epoch (maximal run with σ̄|Q constant): N_ep, ρ = Σ_q ρ_q, the ALT classes (clean strict / tie / non-clean / cycle-node), |D_E|, len(E),
  crossings X_D and X_SN^pre(E). Definitions and the line each comes from are in the script header (RESULTS R60, R61, R63, R64 on trunk e1eabcd0).
- Falsification tests of LANDED statements, every phase: EP0 (R64 (c)), ALT (R61 (e)), NEP (R61 (f), disjoint-class reading = strongest),
  XEP (R63 (d) with the sharpening XEP-N1), SPLIT-RD / SPLIT-STICK (R63 sharpening via R55 (a)), EPOCH (R60 (c)), MONO (R15 (a)),
  D-EPOCH (R63 (c)). A hit prints `VIOLATION`.
- `exhk.py`: exhaustive canonical families (1O = exh.py's C^1O family; 2O = two Odd choice vertices of out-degree 2, Even out-degree 1-2),
  S3 or all start pairs, multiprocessing.
- `climb.py`: hill climbs on (game, start pair) with census.analyse as the scorer (fitness `nep` or `lend2`), sideways moves accepted.
- `named.txt`: the named instance set (lane instances with their start files). `instances/lcount_n23.*`: copies of L-RED's pinned files
  (origin/claude/l-red, experiments/red/h3/instances/; sha1 f86125a0 / 098fca21 / c25786c5 equal to L-RED's), added at the Lead's request.

## Reading choices (READING)
- κ in ALT is read through Ξ: a clean change is STRICT iff Ξ_{t+1}(q) is strictly better than Ξ_t(q) in the VJ order (SI.nvo); TIE as in
  R61 (e) with Ξ-equality. ALT classes are made disjoint in the order cyc (λ(q) = q), nc, tie, strict, so the NEP test is the strongest reading.
- len(E) counts the in-phase transitions whose source lies in E, so it includes an exit transition that stays in the phase (R64). L-NEW's
  P-N5-EPR §5 table reports y − x (both ends in E): its maxima 91 (|D| = 1) and 56 (|D| = 0) on lib41 correspond to my 92 and 56.
- S3 = SPEC's start (n5b default); random start pairs: every vertex of its owner a uniform successor.

## (a)+(b) Census tables (DATA; trunk e1eabcd0 code; 0 violations of EP0 / ALT / NEP / XEP / SPLIT-RD / SPLIT-STICK / EPOCH / MONO / D-EPOCH in every row)
| sample (command) | runs | phases (≥ 2 epochs) | epochs (\|D\| 0 / 1 / ≥2) | ρ | tie / nc / cyc | clean strict | crossings / Σ X_SN^pre | max N_ep | max len(E) \|D\| 0 / 1 / ≥2 | max X_SN^pre(E) \|D\| 1 / ≥2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| named.txt, S3/start + 3 random, seed 12 (`census.py 3 12 --list named.txt`) | 60 | 249 (38) | 86 / 372 / 104 | 734 | 0 / 33 / 0 | 327 | 369 / 186 | 53 | 14 / 36 / 18 | 36 / 15 |
| lib41 (412 games, n ≤ 492), S3 + 2 random, seed 7 (`census.py 2 7 --list ../new/box41/lib41.txt`) | 1,236 | 7,200 (585) | 2,196 / 5,117 / 3,378 | 8,189 | 160 / 142 / 1 | 3,800 | 5,685 / 2,864 | 50 | 56 / 92 / 23 | 69 / 12 |
| 20,000 random C^kO, k 2-6, n 6-20, S3 + 4 random, seed 8 (`census.py 4 8 --rand 20000 6 20 2 6 121`) | 100,000 | 263,090 (1,498) | 107,043 / 67,662 / 89,897 | 3,835 | 199 / 188 / 83 | 1,319 | 1,656 / 242 | 3 | 4 / 3 / 2 | 2 / 1 |
| exhaustive canonical C^2O n 4, S3 (`exhk.py 2O 4`) | 345,600 | 455,010 (276) | 327,372 / 113,652 / 14,262 | 104 | 0 / 0 / 172 | 104 | 324 / 48 | 2 | 2 / 1 / 0 | 1 / 0 |
| exhaustive canonical C^2O n 4, ALL start pairs (`exhk.py 2O 4 --all-starts`) | 3,538,944 | 7,287,738 (27,830) | 3,767,202 / 2,605,482 / 942,884 | 27,122 | 4,068 / 3,152 / 9,640 | 12,512 | 27,492 / 988 | 2 | 2 / 2 / 1 | 1 / 1 |
| canonical C^2O n 5, every 10th game, S3 (`exhk.py 2O 5 --every 10`) | 10,800,000 | 17,167,692 (35,028) | 10,695,408 / 5,584,300 / 923,012 | 29,360 | 4,278 / 1,984 / 15,154 | 14,568 | 47,618 / 13,636 | 2 | 3 / 2 / 1 | 2 / 1 |
- len(E) distributions per |D| class (full histograms): `len_hist` in each results/*.json / *.txt. lib41: |D| = 0: 1,496 epochs of len 0, max 56;
  |D| = 1: 1,811 of len 0, 2,463 of len 1, max 92; |D| ≥ 2: 3,159 of len 0, 182 of len 1, 18 of len ≥ 5, max 23.
- EP-0 (falsification test): max len(E) / (n + m) over D_E = ∅ epochs: 0.29 (lib41, blockph_bp32 S3, len 30, n 36, m 69); 0.20 exhaustive C^2O n 5. Never near the bound.
- ALT / NEP: every clean equality is a tie; NEP tight (slack 0) on 2-epoch phases; the residual tie + nc + cyc per phase is ≤ 28 (lib41), ≤ 17 (named; rho3_253_n32: nc 17).
- Mutation controls (each weakens one bound; must fire): CENSUS_MUT=ep0 9, nep 8, xep 5 violations on named.txt; alt 160 on lib41 (= its 160 ties).
- Engine cross-check on lane instances (S3/start): lap_n6 N_ep 3, so_th_n32 31, lev_l_x 50, rise_thin51_n40 53 (= RESULTS R60 / L-NEW box 45);
  rho3_253_n32 ρ 253 in one phase; xsnpre36_n48 X_SN^pre 36 in one |D| = 1 epoch of len 36; lcount_n23 (start): N_ep 2, |D| ≤ 3, max len 4 (|D| ≥ 2).

## (c) Climbs (DATA; budgets as listed, wall-clock with 4 climbs sharing 4 cores; values are lower bounds that rise with budget)
Command: `climbs.sh 1..4` (each line `climb.py FIT N K SEED --secs S [--seed-pg ...]`); logs results/climb/*.log. Best instances pinned with
`pin.py` (n5.py states = n5b SPEC states, regions = Oink zlk @ 8fbf0a7, verify.py strategies OK) into instances/:
| climb | n | budget | best | pinned instance (sha1) | notes |
| --- | --- | --- | --- | --- | --- |
| nep, random C^2O, seed 1 | 8 | 600 s | N_ep 5 | — | |
| nep, random C^3O, seed 2 | 12 | 600 s | N_ep 9 | — | |
| nep, seed 3 | 16 | 600 s | N_ep 8 | — | |
| nep, seed 4 | 24 | 600 s | N_ep 13 | nep13_n24 (7a6f206d87cf29b47fea25fac72b29c5c370dce6) | ρ 29, tie 1 |
| nep, seed 5 | 32 | 900 s | N_ep 6 | — | |
| nep, seeded lev_l_x (50), seed 6 | 32 | 1,200 s | N_ep 56 (1.75 n) | nep56_n32 (3aa61b2e84036512ca586fa15a67b6fdd2d0aed0) | ρ 91, tie 1, \|Q\| 2 |
| nep, seeded rise_thin51_n40 (53), seed 7 | 40 | 1,200 s | **N_ep 76 (1.90 n)** | nep76_n40 (796ca1334d77522245b77942d5c8776f49599846) | ρ 177, residual 0, \|Q\| 5, phase states [9, 87] |
| lend2, random, seed 11 | 8 | 600 s | len 9 (\|D\| 2) | lend9_n8 (c2d575e8c5dbb55845be64d177fdb400414979bd) | X_SN^pre 2 |
| lend2, seed 12 | 12 | 600 s | len 9 | — | |
| lend2, seed 13 | 16 | 600 s | len 13 (\|D\| 2) | lend13_n16 (1ebf8ead9b4871205b6809a0cd9720d3a0de8e44) | |
| lend2, seed 14 | 24 | 600 s | len 27 (\|D\| 4) | lend27_n24 (556b2048349f79023e842039dac9fc060c40c163) | |
| lend2, seed 15 | 32 | 900 s | len 19 | — | |
| lend2, C^4O, seed 16 | 48 | 900 s | len 15 (\|D\| 7) | lend15_n48 (bcbdc9c13e7fa359d0418130c8f2d1be16e23b96) | |
| lend2, seeded phase2_pk32 (23), seed 17 | 32 | 1,200 s | len 47 (\|D\| 2) | lend47_n32 (ca617b38f4c334619f4cb1c61b85d5fc8b9fbe14) | X_SN^pre 20 |
| lend2, seeded fb17_n32 (18), seed 18 | 32 | 1,200 s | **len 55 (\|D\| 4, 1.72 n)** | lend55_n32 (582b9c9d06adb531e9f1cda4bfd1de4297f8939d) | X_SN^pre 36, epoch states [0, 54] |
- Every pinned instance: census 0 violations; reproduce with `python3 census.py 0 0 instances/NAME.pg:instances/NAME.start`.
- Reading of (c) (READING, not a claim): random starts stay small (N_ep ≤ 13, len ≤ 27 at n ≤ 48); the large values come only from seeding with
  lane instances, and grow with budget (lev_l_x 50 → 56, rise_thin51 53 → 76; |D| ≥ 2 epochs 18 / 23 → 55 / 47). No growth law is claimed.
