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
@@A@@
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
@@B@@
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
