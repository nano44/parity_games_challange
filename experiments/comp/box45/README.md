# L-COMP BOX 45 (successor 21; Lead «go» 20:30Z 2026-11-12 for the queued items (a), (b) after BOX 44): a depth TAIL cannot inflate; the per-gate quiet-flip maximum. All DATA.
Nothing here is a TARGET.md claim, an M3 / M4 statement, a bound or a gauntlet step. N5′-xi stays a CANDIDATE (D1); G-N5-TIME stays OPEN.
Every result below is DATA ON THE NAMED SETS ONLY: no number here is claimed for all genomes. Every number names its counter (unit, set,
scope) and is copied from a generated table: out/sum45_a.out and out/sum45_b.out are sum45.py's output on out/ (sha1 of sum45.py and of both
tables in out/SHA1SUMS); README.md is README.src.md with those two tables inserted (mk45.py).
Engine (both items): MY Γ3 engine box34/own34.py (N5′-xi from S3 on Γ3(G), [E-LEV], states 0..T3 before the first fallback; Odd's σ̄_t by my
n5b SpecSI) with box 100's TWO-CROSS charging as in box41/deep41.py. Second engines: L-RED 65's HOW3 (claude/l-red 59daaef2
experiments/red/r232/how3_232.py, read-only, loop of L-SI's cross100.py, claude/l-si 23d39400) and fast37 (C, box 37).

**Correction (two wrong readings, recorded, not erased).** (1) My 23:55Z message to the Lead said «depthNS = 0 on EVERY flip». That was a
misreading of deepNS (flips with depthNS > 3) and of one row's dmax as the maximum. (2) My 00:46Z correction then listed «dmaxNS 2 on DSALT6/7/9,
DHIB18_2805, DWT20_2803, C7_NM105»; that list came from a grep matching dmaxNS 1 OR 2. The exact values are in the table below: max depthNS
= 2 on ONE genome (DSALT9_n416), 1 on eight. Since then every number is copied from sum45.py's tables.

## Item (a): a depth notion TAIL cannot inflate (deep45.py)
- Definition (mine, stated in deep45.py's header). A flip of gate g at t → t+1 is charged to the change Ω_t(a) → Ω_(t+1)(a) of the face a it
  leaves (box 100 §2). P_t(a) := the play from a under (σ_t, σ̄_t), stopped at the first visit of λ = Λ_t(a). For a Λ-quiet change let z be the
  most relevant element of Π_t Δ Π_(t+1) and ABOVE := {u ∈ Π_t(a) : rk(u) > rk(z)} (all of Π_t for a length-only change; rk = (priority, index)).
  depth100 := |ABOVE| (box 100 §3, = deep41's depth); **depthNS := |ABOVE minus the vertices in the common suffix of P_t(a) and P_(t+1)(a)|**;
  depthMID := |ABOVE minus the common prefix and the common suffix|. Λ changes: −1. Self-check counter pimis (must be 0): Π ⊆ the play, the
  play reaches λ without a repeat.
- Why TAIL cannot inflate it (argument sketch, not a lemma): TAIL_h (box43/tail43.py) appends the same chain to the END of every sink-ending
  play; on a Λ-quiet sink-ending change both plays end with that chain, so the chain lies in the common suffix.
- DATA, TAIL invariance flip by flip (deep45.py --tail; out/tail45.out; unit = flip of a gate of G, states 0..T3): on 8 pairs (G, TAIL_2(G))
  — MWR4/8/16/32_2 → TMWR4/8/16/32, C6G8_n54 → TC6G8, BEST_C300_r34 → TREC, DHIB26_2804 → TDHIB26, RWX_n95 → TRWX (box45/inst, tail43.py
  h = 2) — T3 equal, the same set of flips, depthNS changed on 0 flips, depthMID on 0, while depth100 changed on 13 / 25 / 49 / 97 / 54 / 61 /
  145 / 64 flips. Controls (CTRL=1: suffix not removed) fire: MWR8_2 25 flips changed, DHIB26_2804 145.
- DATA, the counts on the frozen sets (out/deep45_{mine,lnew,fam,big,rand}.out; table by sum45.py a; unit = flip, scope = every gate,
  whole run, states 0..T3; «> 3» = depth above c = 3; Int = internal gates of their SCC after t0, box 100 §4):
| set | contents | genome runs | flips | Λ-quiet flips | max depth100 (genome) | deep100 (> 3) | Int100 | max depthNS | deepNS (> 3) | IntNS | max depthMID | unm | pimis |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mine | box40/inst ∪ box39/inst ∪ box41/inst | 61 | 4377 | 3716 | 32 (CW32_own.json) | 1262 | 1206 | 1 | 0 | 0 | 1 | 0 | 0 |
| lnew | L-NEW's 25 records (MWR8_2, MWR16_2 run in «mine») + CWRQ4_n, CWRQ16_n + its 53 corpus (311bbf81) | 78 | 3369 | 2859 | 18 (CW16_n.json) | 591 | 404 | 2 | 0 | 0 | 2 | 0 | 0 |
| fam | box42 CL0/8/16/30, box43 D18_k4/8/16, D10_k16, D80_k16, DHIB26_k0, TMWR4/8/16, TC6G8, TREC, TDHIB26, box45 TRWX | 17 | 4172 | 3947 | 12 (TREC.json) | 1447 | 1386 | 1 | 0 | 0 | 1 | 0 | 0 |
| big | box42 CL45, CL90; box43 D10_k32/k64, D18_k32, D80_k32/k64, TMWR32 | 8 | 6654 | 6549 | 6 (D10_k32.json) | 2281 | 2249 | 0 | 0 | 0 | 0 | 0 | 0 |
| rand | random genomes, rand43.rgen (rand45.py) | 1100 | 3940 | 1328 | 7 (rand_s4512_nm160_px0.3_64) | 14 | 12 | 1 | 0 | 0 | 1 | 0 | 0 |

Total over the sets above: 1264 genome runs, 22512 flips.

Genome runs with max depthNS = 1: 13 (fam: TRWX.json; lnew: C7_NM105_4438ea3e.json, DHIB18_2805.json, DSALT6_n108.json, DSALT7_n108.json, DWT20_2803.json, ROUTELOW_n21.json, RWX_n95.json; mine: DHIB18_2805.json, DWT20_2803.json, RWX_n95.json; rand: rand_s4511_nm60_px0.3_46, rand_s4512_nm160_px0.3_2).

Genomes with max depthNS = 2 (none higher):
- DSALT9_n416.json (set lnew, N + M 1217): claude/l-new 311bbf81 experiments/new/box202/inst/DSALT9_n416.json, sha1 da3308b524e2b00861a880e8f9bfdc2cd652555f; depth100 max 6, T3 30
- READING (DATA, these sets only; not a bound): on every genome run here, the elements of Π more relevant than the top difference z lie in the
  common END of the two plays, except on 11 distinct genomes, where 1 (10 genomes, listed above; DHIB18_2805, DWT20_2803, RWX_n95 occur in
  two sets) or 2 (DSALT9_n416) of them do not. So box 100's depth is, on these data, almost
  entirely the shared end of the two plays: the part TAIL can lengthen at will. A depth notion that discounts that shared end leaves every
  flip shallow (deepNS = 0 at c = 3), so DEEP-type counts measured this way are 0 here and the open quantity is the Λ-quiet flip count itself
  (as box 43's reading 2 said), item (b).

## Item (b): the per-gate Λ-quiet flip maximum beyond linear? (climb45.py, qsec45.py)
- Counter (unit = flip; scope = one gate, whole run, states 0..T3): qmax := max over gates of Λ-quiet flips (a flip whose face a keeps Λ).
  Climb score: QP := max over gates of (flips − lamch) from fast37 (a lower bound on that gate's quiet flips); every new global best re-measured
  exactly by deep45.census (qmax) with fast37 / own34 T3 agreement; ALERT if they disagree or qmax < QP (0 ALERT lines in out/climb45_B*.log).
  In a best's file name «T<k>» is QP, not T3 (climb44's naming kept).
- Climbs (3 bands, 4 restarts × 400 steps each, seeds gen37(n) and MWR(n) at n = 3, 6, 9, RNG seeds 4541-4543; out/climb45_B*.log):
| band | seeds (QP at N + M) | best (QP = text-engine qmax, N + M, ratio) | T3 | evals | file |
| --- | --- | --- | --- | --- | --- |
| 1 | seed_MWR_3.json 7 at 116; seed_gen37_3.json 14 at 116 | 15, 109, 0.1376 | 16 | 1477 | out/climb45/BEST_B1_T15_NM109_d4cf0e34.json |
| 2 | seed_MWR_6.json 13 at 203; seed_gen37_6.json 26 at 203 | 29, 192, 0.1510 | 31 | 1508 | out/climb45/BEST_B2_T29_NM192_cf2a32c9.json |
| 3 | seed_MWR_9.json 19 at 290; seed_gen37_9.json 38 at 290 | 38, 275, 0.1382 | 43 | 1518 | out/climb45/BEST_B3_T38_NM275_703bb6b4.json |

Second engine (qsec45.py on L-RED 65's HOW3, out/qsec45.out): (qmax, T3) equal to mine on 48 of 48 genomes.

| family member | N + M | qmax (HOW3) | max flips of one gate | T3 | mine (qmax, T3) |
| --- | --- | --- | --- | --- | --- |
| CW4_n.json | 157 | 11 | 11 | 30 | (11, 30) |
| CW8_n.json | 303 | 37 | 37 | 59 | (37, 59) |
| CW16_n.json | 643 | 91 | 91 | 114 | (91, 114) |
| MWR4_2.json | 145 | 9 | 9 | 30 | (9, 30) |
| MWR8_2.json | 261 | 17 | 17 | 54 | (17, 54) |
| MWR16_2.json | 493 | 33 | 33 | 102 | (33, 102) |
| MW4_2.json | 145 | 18 | 18 | 31 | (18, 31) |
| MW8_2.json | 261 | 34 | 34 | 55 | (34, 55) |
| MW16_2.json | 493 | 66 | 66 | 103 | (66, 103) |
| MW32_2.json | 957 | 130 | 130 | 199 | (130, 199) |
- READING (DATA, these sets only): the best ratio qmax / (N + M) does not rise with size: 0.1376 at N + M 109, 0.1510 at 192, 0.1382 at 275,
  near the seed family gen37's 4/29 = 0.138. The frozen families: MW(n) qmax = 4n + 2 at N + M 29n + 29 (n = 4, 8, 16, 32); MWR(n) 2n + 1;
  CW(n) = carry206(MWR(n)) (L-NEW box 206): N + M = n²/2 + 30.5n + 27 exactly at n = 4, 8, 16, 32 (157, 303, 643, 1515; CW32_own from box 39
  is that n = 32 member) while qmax = 11, 37, 91, 201 (about 7n), so its ratio 0.070, 0.122, 0.142, 0.133 peaks and falls; D-, CL- families
  constant (15, 5). Nothing beyond linear in N + M was found; a growth exponent above 1 is NOT identified.

## Files
deep45.py (item (a) counters; --tail mode), rand45.py, run45a.sh (tail | frozen | big | rand); climb45.py (copy of box44/climb44.py with the
QP score and deep45 re-measurement), run45b.sh (bands 1-3), qsec45.py + run45c.sh (second engine); sum45.py (tables), mk45.py (this README).
inst/: TRWX.json (TAIL_2(RWX_n95)), seeds; out/: every output, out/climb45/ every global best, out/SHA1SUMS.
Slips: run45a.sh was edited (rand phase added) while an instance ran (the old instance read the new file's tail: one syntax error after its frozen phase had finished (phase exit 2), no row lost or duplicated; the tail phase's closing echo prints the last pair's file because the loop's «set --» overwrites $1, cosmetic); two message timestamps
«00:5xZ» were not from date -u; the two wrong readings above.
