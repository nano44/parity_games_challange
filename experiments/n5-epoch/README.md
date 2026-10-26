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

## Add-on (Lead 09:46Z / 10:06Z): CONJECTURE HON-FF (L-NEW 25, docs/new/N5-REC1-box46.md §1a on claude/l-new), IMM / IMM' as validation
Code: `honff.py` (own checker from the doc's §0, §1, §1a, §4; L-NEW's imm.py / hon2.py / ffclimb.py not opened), `levcheck.py` (LEV prune
cross-check), `honclimb.py` + `honclimbs.sh` (climb). LEV = largest j ≤ n − 1 with Ξ_k ⪰ value(r) for every simple G_τ-path r with ≤ j edges to
a cycle node of λ; computed as (shortest beating simple path) − 1: BFS for other cycle nodes, DFS with length pruning and an exact
optimistic-completion prune for c = λ(x); budget 2·10⁶ expansions per state, over budget = UNK (never a pass).
- LEV prune check (`levcheck.py 3000 5`): 7,597 states, prune = no prune = brute force (n ≤ 9): 0 mismatches.
- Validation (DATA): immfail_n14 (db3fc2ca, S3): IMM fails at h = 0 and h = 2 (LEV 3 → 3), both with h + 1 last in its phase, so IMM' holds there;
  immp_cex_n11 (1dd7f585, its start): IMM' FAILS at h = 0 (LEV 1 → 1); exitr_cex_n16: IMM' FAILS on 15 of 40 random starts (`honff.py 40 7 FILE`);
  j10_n24 / j7_n32 / j8_n32 (S3): inside-fallback gaps 1 → 24 (fallback 9, LEV 1 → 4), 1 → 46 (22, 0 → 19), 3 → 50 (22, 29; 2 → 9) = L-NEW §5.
  Copies of L-NEW's instances: instances/immfail_n14.pg, immp_cex_n11.pg/.start (sha1 equal to l-new's).
| sample (command) | runs | phases | W-honest states | gaps: fallback-free / fallback at h (HON-FB) / fallback inside | UNK gaps | HON-FF failures | HON / HON-FB violations | IMM fails (IMM' fails) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| named.txt, S3/start + 3 random, seed 12 (`honff.py 3 12 --list named.txt`) | 60 | 249 | 162 | 62 / 0 / 0 | 8 / 0 / 0 | 0 | 0 / 0 | 0 (0) |
| lib41 n ≤ 64 (367 games), S3 + 2 random, seed 7 (`honff.py 2 7 --list results/honff/lib41_le64.txt`) | 1,101 | 5,377 | 5,607 | 3,380 / 56 / 3 | 789 / 16 / 0 | 0 | 0 / 0 | 5 (3: exitr_cex_n16 R1, so_th_n32 R0, j8_n32 S3) |
| lib41 n > 64 (45 games), --fb-only (`honff.py 2 7 --fb-only --list results/honff/lib41_gt64.txt`) | 135 | 1,841 | 184 | 18 / 3 / 0 | — | 0 | 0 / 0 | not run |
| 20,000 random C^kO, k 2-6, n 6-20, S3 + 4 random, seed 8 (`honff.py 4 8 --rand 20000 6 20 2 6 121`) | 100,000 | 263,090 | 135,044 | 9,529 / 2,136 / 0 | 0 | 0 | 0 / 0 | 13 (0) |
- The lib41 n ≤ 64 row reproduces L-NEW's hon.py counts exactly (1,101 runs, 5,377 phases, FBH 56, 3,380 fallback-free pairs).
- Climbs (`honclimbs.sh A`, `B`; 1,200 s each; fitness (inside-fallback gaps, inside fallbacks, shaping terms); every individual with an
  inside-fallback gap is checked for HON-FF with exact LEV):
| climb | n | best (gaps, inside fallbacks, ...) | inside-fallback gaps checked along the climb (UNK) | HON-FF failures |
| --- | --- | --- | --- | --- |
| random C^3O, seed 21 / C^3O seed 24 / C^4O seed 26 | 16 / 24 / 32 | (0, 0, 0, 13, 0) / (0, 0, 0, 11, 0) / (0, 0, 0, 19, 0) | 0 | 0 |
| seeded j10_n24, seed 22 | 24 | (1, 4, ...) | 20,815 (0) | 0 |
| seeded j7_n32, seed 25 | 32 | (1, 5, ...) | 16,791 (0) | 0 |
| seeded j8_n32, seed 23 | 32 | (1, 12, ...) | 8,639 (2) | 0 |
  Pinned (pin.py: n5.py = n5b states, Oink zlk, verify.py OK): ffin12_n32 (6bae375bc1814acb60e59719cf93aea4b98a54ad): gap 6 → 23 with 12 inside
  fallbacks, LEV 6 → 31 (saturated); ffin5_n32 (d20ea0f2892701ea5fc9f650e9ab4f1eb0ec71fc): gap 3 → 12, 5 inside fallbacks, LEV 4 → 31;
  ffin4_n24 (e1c4043c284125ad572736498efeda7bbbac6e4d): gap 5 → 13, 4 inside fallbacks, LEV 4 → 6.
- Reading (READING): random climbs never produce an inside-fallback gap (as L-NEW's ffclimb); seeded climbs grow the number of fallbacks inside
  one gap (1 → 4, 5, 12), and in every gap seen the level rises, often to saturation (n − 1). HON-FF: 0 failures; the support is now 6 + the
  climbs' 46,245 checked gap instances (near-duplicates along three climbs, not independent).

## Box 13 (Lead GO 10:11Z; seeds 10:23Z; relay column 10:42Z): growth law of N_ep and of |D| >= 2 epoch lengths; rho_q per phase
### (1) Scaling climbs (DATA; `scale.sh` runs every line of `scale_jobs.txt`, 4 at a time; `python3 fit.py` -> results/scale/fit.txt)
Budget = 15 s × n per climb (wall clock, 4 climbs on 4 cores), n ∈ {16, 24, 32, 40, 48, 64}, 3 repeats (seeds 100+10n+r etc.). Fresh: random
C^3O (N_ep) / C^4O (lend) with S3 start. Seeded (padded with Even self-loops to n): N_ep from nep24_n20 (n 24), nep56_n32 (32), L-RED's nep90_n40
(40, 48, 64); lend from lend13_n16 (16), lend27_n24 (24), lend55_n32 (32-64). Exponent b: least squares of log(max) on log(n).
| family | n 16 / 24 / 32 / 40 / 48 / 64: max over 3 repeats | max/n at n 64 | b over per-n maxima | b per repeat (spread) |
| --- | --- | --- | --- | --- |
| N_ep, fresh | 10 / 13 / 7 / 12 / 14 / 22 | 0.34 | 0.47 | -0.10, 0.41, 0.30 |
| N_ep, seeded | — / 27 / 63 / 92 / 94 / 91 | 1.42 (2.30 at n 40) | 1.21 | 1.25, 1.27, 1.23 |
| len(E), \|D_E\| ≥ 2, fresh | 21 / 26 / 39 / 19 / 32 / 21 | 0.33 | 0.02 | -0.35, -0.11, 0.13 |
| len(E), \|D_E\| ≥ 2, seeded | 13 / 29 / 63 / 71 / 72 / 71 | 1.11 (1.97 at n 32) | 1.29 | 1.17, 1.30, 1.23 |
- Steps per climb FALL with n (seeded n 64: ~1,700 (N_ep) / ~3,700 (lend) steps vs ~5,000-28,000 at n ≤ 32; a step's cost grows with n), and
  the seeded values at n ≥ 40 are the seed's value plus a few (nep90 → 91-94; lend55 → 63-72). So the seeded exponents (~1.2-1.3) measure
  the SEEDS' sizes, not a growth law; the fresh exponents (≤ 0.5) say random climbs at this budget find nothing growing. READING: the data do
  not separate polynomial from super-polynomial; no value above 2.6 n was found (max/n² falls with n in every family).
- Budget doubling at n 32 (seeded): N_ep 240 / 480 / 960 / 1,920 s → 56 / 57 / 62 / 59 (from nep56: still ~1.8-1.9 n, not rising
  clearly); |D| ≥ 2 len → 58 / 63 / 62 / 82 (still rising at 1,920 s: 82 = 2.56 n).
- Pinned (pin.py OK: n5.py = n5b states, Oink zlk, verify.py): lend82_n32 (34dedec67b5e379c61d9def40f2d97391d249bd4; epoch len 82, |D| 3,
  X_SN^pre 38), nep94_n48 (3859c268caa9a1f755268c08442876c533c2cda7; N_ep 94), nep92_n40 (ce224ec31e56e18103290d4aac81a9f225f76bfc; N_ep 92 =
  2.30 n), lend72_n48 (2ecc531682eb02aa56961ff3c66330140ee70ef5; len 72, |D| 3), lend39f_n32 (f7053a7cace6f30e1ef0708193a0534e9df8326c; fresh,
  len 39), nep22f_n64 (d98de59fb84821bafc15128fd928c70ea6c71f1d; fresh, N_ep 22). Census on each: 0 violations.
### (2) rho_q per q per phase (`rhotab.py`; results/rho/*.txt): class first on every row
- rhotab.py reimplements the logic of L-SI's experiments/si/rund/relay.py (read, not imported). Cross-check: lib41 with L-SI's start pairs
  (`rhotab.py 0 0 --lsi-starts 4 --nmax 48 --kmin 1 --list ../new/box41/lib41.txt`) gives exactly L-SI's relay_lib41_rs4.txt counts: 1,601 phases,
  5,437 rho transitions, ROUTE_one 5,042, ROUTE_multi 618, RELAY_multi 427, CYC_OR_ONCYCLE 42, 107 phases with relays, CYCG 28, CYC2 23.
  0 violations of ROOT / R_EMPTY / ONE_RELAY.
- Extremes (`rhotab.py 0 0 --rows 2 --list extremes.txt`, `--rows 3 --list extremes13.txt`), longest phase of each; ρ_q as total(Route/reLay/Cyc):
| instance | class | \|Q\| | kq per class | N_ep | ρ | ρ_q | relay graph cycle |
| --- | --- | --- | --- | --- | --- | --- | --- |
| nep94_n48 | 9O | 9 | 11:9 | 94 | 429 | 0:75(R75), 1:67(R32/L35), 44:66(R19/L47), 45:65(R29/L36), 6:52, ... | CYCG 1 (1 ↔ 6) |
| nep92_n40 | 6O | 6 | 11:6 | 92 | 333 | 0:72(R72), 1:64(R39/L25), 25:55, 17:53, 6:51, 8:38 | 0 (all relays toward 0, 1) |
| nep90_n40 (L-RED) | 5O | 5 | 11:5 | 90 | 292 | 0:72(R72), 1:64(R23/L41), 17:70(R10/L60), 6:55, 8:31 | 0 |
| nep76_n40 | 5O | 5 | 11:5 | 76 | 177 | 0:62(R62), 8:47, 1:41, 6:22, 37:5 | 0 |
| nep56_n32 | 2O | 2 | 30:2 | 56 | 91 | 0:48(R48), 20:43(R18/L25) | 0 |
| lev_l_x / rise_thin51 / so_th_n32 / nep24_n20 | 1O | 1 | 1 | 50 / 53 / 31 / 24 | 51 / 60 / 33 / 21 | all ROUTE | — |
| rho3_253_n32 (L-RED) | 12O | 12 | 24:12 | 25 | 253 | 11 terminals with 20-26 each, mostly RELAY | 1 (2-cycles) |
| lend82_n32 | 3O | 3 | 6:3 | 3 | 11 | 12:4, 19:4(R1/L3), 11:3 | 0 |
| lend2_30_n48 (L-RED) | 14O | 14 | 11:14 | 2 | 64 | 14 terminals with 3-5 each, mostly RELAY | 1 |
- 𝒞^1O rows (lev_l_x, rise_thin51, so_th_n32, nep24_n20, lap_n6): every ρ event ROUTE, as L-SI's ONE_RELAY lemma says. No 𝒞^1E game among the
  extremes (1E rows: lib41 has 7 phases with ρ ≤ 1).
- READING on L-SI's question: the N_ep records are driven by a ROUTE-only root terminal (q = 0: 72-75 route events per phase) that the other
  terminals copy by RELAY; their relay graphs are acyclic stars toward the root (nep76, nep90, nep92), and nep94's one 2-cycle (1 ↔ 6) is not
  what makes it long. Relay cycles appear on the ρ-dense, few-epoch phases (rho3_253: ρ 253 with N_ep 25; lend2_30). So in this data the
  growth of ρ_q is NOT driven by relay cycles; it is driven by how often the root's exit routes change.
- lib41 with my starts (`rhotab.py 2 7 --rows 10 --list ../new/box41/lib41.txt`, results/rho/lib41_s3r2.txt): 1,152 phases with ≥ 1 transition,
  max ρ_q: 51 (1O), 10 (classes with ≥ 2 Odd choice vertices); CYCG 96 phases, CYC2 87.
