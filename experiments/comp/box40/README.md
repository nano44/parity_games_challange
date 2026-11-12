# L-COMP BOX 40 (successor 18; Lead 08:42Z 2026-11-12): U-FREE front, box 99's SCC census, ties (G1), SCC-LIN climb. All DATA.
Nothing here is a TARGET.md claim. CONJECTURE SCC-LIN (L-SI box 99) and U-FREE stay OPEN; G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1).
Nothing found with loc/M_C > 1 or H > M_C under any legal tie resolution: nothing to send at once.

## Item 1 COUNTER: scc40.py (MY Γ3 engine box34/own34.py: N5′-xi from S3 on Γ3, [E-LEV], states 0..T3 before the first fallback)
- Written from box 99's TEXT (claude/l-si f65e0fb9, docs/si/box99-ufree.md §1, §2, §4; quoted in the script header), not scc99.py.
  Counters (unit; scope): D(G) SCCs; f(C) (last state t in 1..T3 with σ_(t−1)(x) ≠ σ_t(x) for some x ∈ C); e(C) = max f over ALL SCCs
  reachable from C (C excluded); loc(C) = max(0, f − e); M_C = options of C's movers; locfail [SCC: loc > M_C + 1]; chainfail [genome:
  T3 > max_C F(C), F(C) = loc + 1 + max F(succ)]; ratio = max loc/M_C over SCCs with >= 2 movers (READING of «non-trivial»; matches).
- Note: scc99.py's docstring states its chain bound with «loc(C) + [C switches after e(C)]»; box 99 §2 has «H(C) + 1». I use §2's
  (weaker by at most 1 per SCC); chainfail is 0 under both on every genome here.
- Cross-check (xcheck40.sh; out/scc40_inst26.out, out/xcheck40.log): the 26 frozen instances (copied from claude/l-red 59daaef2
  experiments/red/r232/inst; every sha1 = its SHA1SUMS) against L-SI's out/inst99.out (copied as inst/inst99.out.lsi): N, M, T3, #SCC,
  largest SCC, max loc, ratio, locfail, chainfail: **0 mismatches on 26/26**. Control CTRL=1 (e over DIRECT successors only): locfail
  MW8_2 10, FW8_2 14 (= L-RED R232 §2's control exactly).

## Item 2 TIES (gap G1): ties40.py
- HOW3 on my Γ3 engine (own34 build, S3 start, n5b values with Odd's optimal counterstrategy; non-mover Even frozen). Rule (R125 as quoted
  in R232 §1): a mover with a strictly better successor moves to a ⊴-best one; TIE = >= 2 ⊴-best successors. Every combination of tie
  choices is branched (memoised over states; caps SCAP 20,000 states, PRODCAP 4,096 combinations per state, PCAP 5,000 paths for the
  per-path census). Per genome (unit: genome; scope: the run from S3 to HOW3's fixpoint): T3n (n5v rule = own34), legal (n5v's path is
  HOW3-legal: 1 on EVERY genome below), Hmax / Hmin over resolutions, tie states, paths, and per-path box 99 census (max loc, max ratio,
  HM := max over SCCs of loc(C) − M_C).
  | set (unit genome) | genomes | with ties | Hmax > T3n | by | Hmin < T3n | max HM over all paths | ratio max over paths | capped |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | 26 frozen (L-SI box 99) | 26 | 2 (DWT20_2803, C98_5_5_3) | 0 | — | 0 | −1 | 0.8 | 0 |
  | 300 random k = 1, law A (seed 4002) | 300 | 0 | 0 | — | 0 | −1 | 0.5 | 0 |
  | 300 random k = 1, law B = A with repeated β ranks (seed 4003) | 300 | 0 | 0 | — | 0 | −1 | 0.429 | 0 |
  | L-RED's 400 (rand232 replay, seed 2321; 55 have k = 1) | 400 | 90 (k = 1: 1) | 7 (k = 1: 0) | +1, +1, +1, +1, +2, +2, +3 | 7 | −1 | 0.5 | 0 |
- Law A: box38 samp38's law at random (N, M), N + M <= 60, Ξ-target X with probability 0.6 (uniform Ξ-targets give k = 1 almost never at
  N >= 12), resampled to k = 1. Random law A/B ties: none (equal values need equal (Λ, Π, length) plays through distinct gates).
- L-RED's set reproduced (generator copied from r231/dep231.rgen; replay of r232/rand232.py): my n5v T3 = L-RED's «T3n5v» on r85, r96,
  r238, r271, r296, r327, r363 (3, 6, 11, 5, 5, 6, 9), and L-RED's own-rule T3 (4, 8, 7, 4, 6, 5, 10) lies in my [Hmin, Hmax] on all seven.
  The 7 with Hmax > T3n: r85 (N + M 12: 3 -> 4), r96 (60: 6 -> 8), r173 (60: 6 -> 8), r271 (60: 5 -> 6), r296 (40: 5 -> 6), r363 (100:
  9 -> 10), r369 (48: 3 -> 6); all Ξ-feedback number > 1; max loc over their paths 4, 8, 8, 6, 6, 10, 6, every one below M_C (HM <= −1).
- READING: G1 is real (the max over legal resolutions exceeds the n5v run on 7 / 400 of L-RED's genomes, by <= 3) but small; on every
  genome and every legal path here, loc(C) <= M_C − 1.

## Item 3 CLIMB: climb40.py, band40.sh (score (loc(C_max)/M_C, loc − M_C, T3) on the largest SCC; 1 restart x 200 proposals per stream)
- Second engine on every new best: L-SI's scc99.py (worktree of claude/l-si f65e0fb9, ROOT = git archive of l-new fcba92fc as its
  run99.sh): **29 / 29 frozen bests agree** (T3, #SCC, largest SCC, max loc, ratio, locfail). No k constraint (box 99's SCC-LIN is for
  every genome; READING of the brief).
- Seeds (Lead reading: the brief lists 4 seed kinds for 2 streams per band): A = MWR(n) at the band (MWR4_2 145; MWR9 290, genmw229
  WTGT=R n 9, same pipeline gives MWR4_2's sha1); B = C98_2_2_3 grown to 140 (band 150) and C6G8_n54 grown to 280 (band 300), growth-only
  moves accepted iff the score does not fall. DHIB (N + M 400) lies above both bands and the move set cannot shrink: not used.
  | stream | seed (ratio, loc/M_C, big) | best ratio | loc / M_C | movers in C_max | N + M | T3 | sha1 |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | S150a | MWR4_2 (0.330, 30/91, 44) | 0.5 | 12 / 24 | 12 | 154 | 22 | 4c8bf1d25498 |
  | S150b | C98_2_2_3 grown (0.8, 8/10, 4) | 0.8 (no gain) | 8 / 10 | 4 | 140 | 11 | 4fbcb198c975 |
  | S300a | MWR9 (0.314, 60/191, 89) | 0.5 | 19 / 38 | 19 | 291 | 30 | 69712a2f996a |
  | S300b | C6G8 grown (0.124, 18/145, 50) | 0.139 | 19 / 137 | 51 | 286 | 19 | e1b18d094b87 |
  ALERT (loc/M_C > 1 or loc > M_C on any SCC): 0 in every stream. locfail 0, chainfail 0 on every evaluated genome.
- READING: the score is maximised by SHRINKING C_max (MWR's giant SCC of 44 / 89 movers cut to 12 / 19 movers with 2 options each and
  loc = #movers: ratio 0.5), not by lengthening its run. The giant-SCC runs stay at loc/M_C ≈ 0.31-0.34 (S300a passed 0.335 at 85 movers
  before fragmenting). The largest ratio seen anywhere is C98_2_2_3's 0.8 (4 movers).

## Files
scc40.py, xcheck40.sh, ties40.py, sum40.py, climb40.py (+ box39/mut39.py move set), band40.sh; inst/ (26 frozen = L-RED's SHA1SUMS;
inst/SHA1SUMS.box40 for all inputs incl. seeds); out/. Second engine needs env LSI (worktree claude/l-si f65e0fb9) and LSIROOT (git
archive fcba92fc experiments/new experiments/si/si.py experiments/harness).
