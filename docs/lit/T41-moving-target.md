# T41: N5's S4a against the FIXED full best response σ^c_τ, per phase (the "moving target" of T40 §1, §8, measured)
L-LIT successor 2 (Opus 5.5), D18, Lead reading L40. Lead's message 13:08Z: «T41: do the §8 measurement yourself ... Per τ-fixed phase,
compare S4a's choice at switching vertices with the fixed full best response σ^c_τ: how often σ_{t+1}(v) ≠ σ^c_τ(v), how often v later
reaches σ^c_τ(v), and the number of switches per vertex before it does. Use runquad, s3quad, the R109 topfix family, the library, and L-SI's
FW-BF corpus.» Written 2026-10-29 from 13:15Z (date -u). Working note, unrefereed. All counts here are DATA; nothing is signed. Not a
TARGET.md claim; G-N5-TIME stays OPEN.
Read first, as asked: claude/l-si docs/si/N5-FRZ-box29.md (d6d681dc). Its Lemma W-MON (§1) is the same statement as T40 §8's W-MONO,
proved by L-SI independently; B-DOM (T40 §8) is its proof step. Nothing below depends on T40 beyond the definitions.

## 0. What is measured (docs/lit/T41-target-check.py, sha1 in the push message)
- Phase P = [i, j]: a maximal run with λ_Ξ and τ constant (R38 (a); L-SI's common.phases, the same cut as T40 and box 29). τ is fixed on P
  (the script asserts it).
- Target c := σ^c_τ, Even's optimal counterstrategy to τ in the FULL game G: S1's procedure on G^d (Ed.evaluate(τ)), i.e. exactly what S4a
  computes, but on all edges instead of the arena H_t. c is constant on P; W^c := the value of the (c, τ)-plays, pointwise maximal in G_τ.
  This is STV's target (T40 §1): with τ fixed, STV's symmetric SI only ever switches v to c(v), so ≤ 1 switch per vertex.
- Per switch of an Even vertex v at t → t + 1 (σ_t(v) ≠ σ_{t+1}(v)):
  MISS = σ_{t+1}(v) ≠ c(v); of a MISS, AVAIL = c(v) was in the arena H_t(v) = {σ_t(v)} ∪ Iσ_t(v) (S4a did not take it) or UNAVAIL;
  AWAY = the switch leaves c(v) (σ_t(v) = c(v)); VMISS = W_{t+1}(v) ◁ W^c(v) (the switch does not reach the target's value).
- Per switching vertex v and phase: REACH (σ(v) = c(v) after some switch of v), NEVER (not), END (σ_j(v) = c(v)), LEAVE (v starts P at c(v)
  and switches away), SBR = v's switches up to and including the first one that lands on c(v) (REACH vertices), SW = all its switches in P.
- Per phase: WEND_EQ = Even vertices with W_j(v) = W^c(v) at P's last state (of EV_PH = Even vertices summed over phases).
- Fallback (S4c) switches are counted in SW and MISS and reported apart (sw_fb, miss_fb).

## 1. Families
| instance (n) | phases with switches | Even switches (fb) | MISS (AVAIL / UNAVAIL) | VMISS | switching vertices: REACH / NEVER / END / LEAVE | SBR max | SW max (vertex) | AWAY (max per vertex) | WEND_EQ / EV_PH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| runquad_K8_m30_n192 (R106 pin) | 1 | 481 (0) | 254 (254 / 0) | 464 | 47 / 0 / 17 / 30 | 8 | 15 (v 102; SBR 2, not at c at the end) | 240 (8) | 18 / 50 |
| s3quad_K8_m30 (R107, n 479) | 1 | 481 (0) | 254 (254 / 0) | 464 | 47 / 0 / 17 / 30 | 8 | 15 | 240 (8) | 18 / 50 |
| topfix n 3 (hntop_n3, n 63) | 2 | 306 (0) | 180 (100 / 80) | 282 | 51 / 5 / 49 / 15 | 7 | 28 (d1_3) | 92 (13) | 37 / 72 |
| topfix n 4 (n 84) | 2 | 623 (0) | 383 (204 / 179) | 590 | 71 / 6 / 69 / 21 | 11 | 47 | 192 (22) | 49 / 96 |
| topfix n 6 (n 126) | 2 | 1,716 (0) | 1,099 (561 / 538) | 1,665 | 111 / 8 / 109 / 33 | 19 | 97 | 541 (46) | 73 / 144 |
| topfix n 8 (hntop_n8, n 168; hntop_n8_s3 identical) | 2 | 3,581 (0) | 2,335 (1,170 / 1,165) | 3,512 | 151 / 10 / 149 / 45 | 27 | 163 | 1,142 (78) | 97 / 192 |
| topfix n 10 (n 210) | 2 | 6,410 (0) | 4,219 (2,095 / 2,124) | 6,323 | 191 / 12 / 189 / 57 | 35 | 245 | 2,059 (118) | 121 / 240 |
| topfix n 12 (n 252) | 2 | 10,395 (0) | 6,879 (3,400 / 3,479) | 10,290 | 231 / 14 / 229 / 69 | 43 | 343 (v 243 = d1_12; SBR 2, at c at the end) | 3,356 (166) | 145 / 288 |
Topfix n 4, 6, 10, 12 were generated with L-RED's experiments/red/seg/hnh1.py N topfix (sha1 518e0952…, read only; regenerating n 8 gives
the pinned hntop_n8.pg/.start byte for byte); .pg sha1: n4 32a613e0…, n6 6241405f…, n10 4b65d3dc…, n12 a08c2c1d….
- DATA (exact for n = 3, 4, 6, 8, 10, 12): the most-switching vertex is d1_n with SW = 2n² + 5n − 5 (= R109's count) in ONE phase, of which
  AWAY = n² + 2n − 2 switches LEAVE its target c(d1_n) = d2_n. Its SBR is 2: it reaches the target at its second switch and then leaves and
  re-enters it n² + 2n − 2 times, ending at it. SBR max over vertices = 4n − 5; NEVER = n + 2 vertices.
- What d1_n does (topfix n 3, phase [0, 41], σ(d1_3) step by step): d2_3 a3 a3 d2_3 a6 a6 d2_3 a15 c c d2_3 a3 a3 d2_3 a6 a6 d2_3 a9 a9
  d2_3 a12 a12 d2_3 a15 c c d2_3 a3 … a15 a15 d2_3. Every departure goes from the target d2_3 into the deceleration lane, which is the
  target edge's alternative while d2_3/d3_3 do not close the gate; d2_3 is in the arena throughout (σ_t(d1) = d2 is always kept), so these
  are AVAIL-type departures: S4a's W-optimum over H_t is not c on the gate while the rest of the gate is not at c.
- runquad / s3quad: every MISS had c(v) in the arena (254 / 254); all 47 switching vertices reach c, 30 of them start at c and leave it,
  and only 17 are at c when the phase ends; 464 of 481 switches stay W-below W^c, and at the end only 18 of 50 Even vertices have W^c.

## 2. Library and L-SI's FW-BF corpus (the three corpora of box 29 §4)
| corpus | games | phases with switches | Even switches (fb) | MISS (fb) | MISS: AVAIL / UNAVAIL | VMISS | vertices: REACH / NEVER / END / LEAVE / SBR > 1 | SBR max | SW max | AWAY (max) | WEND_EQ / EV_PH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alt_all, pinned starts (experiments/si/root/logs/alt_all.lst) | 413 | 457 | 16,954 (1,929) | 7,210 (984) = 42.5% | 5,233 / 1,977 | 12,055 = 71.1% | 6,902 / 406 / 6,765 / 1,515 / 2,043 of 7,308 | 48 (ladderd0_k48_n156) | 48 (ladderd0_k48_n156, n 156) | 4,494 (6, nep76_n40) | 11,718 / 16,552 |
| lib41 (experiments/n5-box18/results/lib41_n48.lst) | 349 | 368 | 11,852 (1,571) | 5,514 (814) = 46.5% | 4,094 / 1,420 | 8,862 = 74.8% | 4,265 / 404 / 4,151 / 1,412 / 1,837 of 4,669 | 7 (fbref_n48) | 14 (sc24, n 24) | 3,599 (6, j4_n40) | 5,416 / 8,767 |
| experiments/si (experiments/si/chg/sicorpus.lst) | 276 (+1 skipped: dlmm_ML_L6, start file in another format, as in box 29) | 345 | 11,524 (901) | 5,164 (363) = 44.8% | 3,913 / 1,251 | 8,587 = 74.5% | 4,841 / 654 / 4,779 / 1,527 / 1,860 of 5,495 | 12 (dl42, n 48) | 27 (swlin_kill_n26, n 26: 1.04n) | 3,108 (7, sw_lend2_s5) | 7,753 / 12,351 |
- 42-47% of S4a's switches do not go to c(v), and 71-75% do not reach W^c(v); in 73-76% of the misses c(v) was in the arena. 88-94% of
  switching vertices reach c(v) inside the phase, most at their first switch (SBR > 1 for 30-43% of the reaching vertices); 6-12% never do.
- Leaving the target is common but short in the library: AWAY ≤ 7 per vertex per phase on all three corpora (vs n² + 2n − 2 on topfix).
  The library maximum of SW (48 on ladderd0_k48_n156) is a single climb (vertex 50: SBR = SW = 48, one rung per switch, reaching c at the end, as in
  box 29 §5's ladder), not a back-and-forth.

## 3. Reading (not signed)
- The fixed target is reached fast; the length comes from LEAVING it. In every set measured, SBR is small relative to SW except for ladder
  climbs, and the two large families split cleanly: runquad (σ̄ constant, |D| = 32) has 30 of 47 vertices leaving c, and topfix has one vertex
  leaving c n² + 2n − 2 times in one phase while its target edge stays in the arena. So a per-vertex bound cannot come from "S4a moves toward
  c": c(v) is optimal only jointly with c on the other vertices, and S4a, optimising over the arena where the other vertices are not yet at c,
  can prefer another edge at v. This is T40 §1's "moving target" in numbers.
- Contrast (T40 §1, PROVED there): STV's symmetric SI, which may only switch v to c(v), changes each vertex at most once per τ-fixed stretch.
  On topfix (I_τ = ∅ at every state, R109) that rule would make ≤ |V_0| Even switches per phase where N5 makes 9,495 at n 12.
- For L-SI's W-SPLIT / FW-BF: W-MON makes W_t(v) non-decreasing on S4a transitions and bounded by W^c(v), and WEND_EQ shows the phases end with
  W below W^c at 29-38% of Even vertices in the libraries (and 64% on runquad). A potential of the form Σ_v (distance of W_t(v) to W^c(v)) can
  only fall at S4a transitions, but AWAY switches show the edge-level distance to c does not; any FW-BF proof that charges switches to
  progress toward c must charge in VALUE (W), not in edges.
- OPEN (a measurement, not done): the same table per FROZEN W-phase (box 29 §0) instead of per phase, to see whether AWAY survives inside
  frozen W-phases or is cut by λ_W changes (topfix: 0 fallbacks, so its phases are W-SPLIT's LWCH + SBCH′ + frozen pieces).

## DONE / FINDINGS / NEEDS
- DONE: this note; docs/lit/T41-target-check.py (reads experiments/si/root/common.py, experiments/new/box21/n5x.py read-only); runs on runquad,
  s3quad, topfix n 3, 4, 6, 8 (and the S3 pin), 10, 12, alt_all (413), lib41 (349), experiments/si (276). Logs in the session scratchpad
  t41/ (not committed; each line re-runs in seconds to minutes).
- FINDINGS:
  - 42-47% of S4a's switches miss the fixed full best response c = σ^c_τ; 73-76% of misses had c(v) in the arena; 71-75% of switches stay
    W-below W^c (libraries; runquad 53% / 100% / 96%).
  - 88-94% of switching vertices reach c(v) in the phase, mostly at once; the long counts come from LEAVING c: topfix d1_n leaves its target
    n² + 2n − 2 times in one phase (SW = 2n² + 5n − 5, SBR = 2; exact n = 3..12); runquad: 30 of 47 vertices leave c. Library AWAY ≤ 7.
  - A per-vertex argument "toward c" is dead on topfix; progress must be measured in W (W-MON), not in edges.
- NEEDS: none from the owner. Lead: the per-frozen-W-phase split (§3, OPEN) if L-SI wants it.
