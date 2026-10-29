# T41b: S4a vs the fixed best response σ^c_τ, split by L-SI's FROZEN W-PHASES (does "leaving c" happen inside them?)
L-LIT successor 2 (Opus 5.5), D18. Lead's message 13:47Z: «T41b: the same table per FROZEN W-PHASE, using L-SI's definitions and tools in
claude/l-si docs/si/N5-FRZ-box29.md §0 and experiments/si/frz/, read only. Report MISS / AWAY / SBR per frozen W-phase, and whether "leaving
c" happens inside frozen W-phases or only across their cuts (λ_W-changes, fallbacks, σ̄-changes).» Written 2026-10-29 from 13:50Z (date -u).
Working note; all counts DATA, nothing signed. Not a TARGET.md claim; G-N5-TIME stays OPEN. Definitions as in T41 §0.

## 0. Method (docs/lit/T41b-frozen-target-check.py, sha1 69dfa4ac…)
- Phase P (λ_Ξ, τ constant; R38 (a)); target c = σ^c_τ, fixed on P (T41 §0).
- Each in-phase transition t → t + 1 gets ONE kind, in box 29 §0's order: FB (S4c fallback), LW (non-fallback, changes λ_W), SB (non-fallback,
  keeps λ_W, changes σ̄), FZ (none: inside a frozen W-phase). The frozen W-phases are the maximal FZ runs; the cut rule is copied from
  experiments/si/frz/fwphase.py fwphases() (claude/l-si 4e928f11, read only). Check: the frozen W-phase counts equal box 29 §4's exactly
  (alt_all pinned starts 1,125; lib41 864; experiments/si 655).
- Per Even switch: MISS (σ_{t+1}(v) ≠ c(v)) and AWAY (σ_t(v) = c(v): leaves c), tallied by the kind of its transition. Per frozen W-phase F
  and switching vertex v: SW_F, AWAY_F, SBR_F (switches up to the first landing on c(v) inside F), NEVER_F (no landing on c in F).

## 1. Families
| instance | transitions FZ / LW / SB / FB | switches FZ / LW | AWAY FZ / LW | frozen W-phases | per frozen W-phase: max SW_F / max AWAY_F / max SBR_F (vertex, F, \|F\|) |
| --- | --- | --- | --- | --- | --- |
| runquad_K8_m30_n192 = s3quad_K8_m30 | 0 / 263 / 0 / 0 | 0 / 481 | 0 / 240 | 0 | — (every transition changes λ_W, box 29 §3) |
| topfix n 3 (hntop_n3) | 49 / 8 / 0 / 0 | 231 / 75 | 52 / 40 | 4 | 12 / 5 / 7 (d1_3: SW_F 12, AWAY_F 5 in F = [23, 41], \|F\| 18) |
| topfix n 4 | 79 / 12 / 0 / 0 | 476 / 147 | 118 / 74 | 5 | 16 / 7 / 11 (d1_4 in [45, 69], \|F\| 24) |
| topfix n 6 | 157 / 20 / 0 / 0 | 1,359 / 357 | 372 / 169 | 7 | 24 / 11 / 19 (d1_6 in [107, 143], \|F\| 36) |
| topfix n 8 (hntop_n8) | 259 / 28 / 0 / 0 | 2,926 / 655 | 842 / 300 | 9 | 32 / 15 / 27 (d1_8 in [193, 241], \|F\| 48) |
| topfix n 10 | 385 / 36 / 0 / 0 | 5,369 / 1,041 | 1,592 / 467 | 11 | 40 / 19 / 35 (d1_10 in [303, 363], \|F\| 60) |
| topfix n 12 | 535 / 44 / 0 / 0 | 8,880 / 1,515 | 2,686 / 670 | 13 | 48 / 23 / 43 (d1_12 in [437, 509], \|F\| 72) |
- DATA, exact for n = 3, 4, 6, 8, 10, 12 (topfix has no fallbacks and no σ̄-changes): 4n − 4 λ_W-changing transitions, n + 1 frozen W-phases;
  inside the last frozen W-phase (length 6n) d1_n switches 4n times and LEAVES c(d1_n) 2n − 1 times, reaching c at its 2nd switch (SBR_F 2).
  The largest SBR_F, 4n − 5, is another vertex's climb (AWAY_F 1). About 80% of all AWAY switches are FZ (2,686 of 3,356 at n 12).
- So on topfix "leaving c" happens INSIDE frozen W-phases, not only across cuts: d1_n's n² + 2n − 2 departures in one phase (T41) are
  ≤ 2n − 1 per frozen W-phase times n + 1 frozen W-phases plus the λ_W-cut transitions.
- runquad / s3quad: all 240 departures are at λ_W-changing transitions; there is no frozen W-phase to look inside.

## 2. Library and L-SI's FW-BF corpus
| corpus | transitions FZ / LW / SB / FB | switches FZ / LW / SB / FB | MISS FZ / LW / SB / FB | AWAY FZ / LW / SB / FB | frozen W-phases | (v, F) pairs: NEVER_F / SBR_F > 1 / AWAY_F > 0 | max SW_F / AWAY_F / SBR_F |
| --- | --- | --- | --- | --- | --- | --- | --- |
| alt_all, pinned starts (413 games) | 4,742 / 283 / 2,328 / 731 | 8,207 / 540 / 6,278 / 1,929 | 3,318 / 190 / 2,718 / 984 | 2,008 / 99 / 1,669 / 718 | 1,125 | 2,299 / 561 / 1,999 of 7,146 | 48 / 2 / 48 (ladderd0_k48_n156: one climb, SW = SBR = 48, AWAY 0; AWAY 2: lend82_n32) |
| lib41 (349) | 3,587 / 214 / 1,630 / 673 | 6,167 / 400 / 3,714 / 1,571 | 2,785 / 142 / 1,773 / 814 | 1,708 / 58 / 1,245 / 588 | 864 | 1,897 / 472 / 1,683 of 5,203 | 14 / 4 / 5 (sc24: v 2, F = [0, 20], SW_F 14, AWAY_F 4) |
| experiments/si (276; dlmm_ML_L6 skipped, start format, as in box 29) | 3,319 / 337 / 1,752 / 450 | 5,446 / 1,071 / 4,106 / 901 | 2,244 / 447 / 2,110 / 363 | 1,467 / 220 / 1,195 / 226 | 655 | 1,541 / 410 / 1,441 of 4,688 | 14 / 4 / 12 (sw_sc24_s1: AWAY_F 4; ll41_k: SBR_F 12, a climb) |
- Departures from c occur at every kind of transition: FZ 45-48% of all AWAY switches (2,008 / 4,494; 1,708 / 3,599; 1,467 / 3,108), SB
  (σ̄-changes) 35-38%, FB 7-16%, LW 2-7%. So in the library too, leaving c is not confined to the cuts.
- Inside one frozen W-phase leaving is rare and short: AWAY_F ≤ 2 (alt_all), ≤ 4 (lib41, experiments/si; both maxima on sc24-type games). 32-37% of (vertex, frozen W-phase) pairs end the frozen W-phase without having landed on c.

## 3. Reading (not signed)
- For FW-BF (box 29 §4) the relevant scale is per frozen W-phase. There, departures from c are O(n) on the only family where they are large
  (topfix: 2n − 1 for one vertex in a frozen W-phase of length 6n) and ≤ 4 in the library. That is consistent with FW-BF (≤ n − 1 W-changing
  transitions per frozen W-phase) and gives no counter-signal: a vertex can leave its target within a frozen W-phase, but only O(n) times
  in all data.
- The Θ(n²) per-phase departures of topfix come from the n + 1 frozen W-phases (one per λ_W wave, 4n − 4 λ_W-cut transitions), i.e. from the
  number of frozen W-phases per phase, which W-SPLIT bounds by FB + LWCH + SBCH′ + 1 with LWCH ≤ n(n − 1)(FB + 1) (CN-W). On topfix FB = SBCH′ = 0
  and LWCH = 4n − 4, so the phase is (4n − 4) + Σ |F| ≤ (4n − 4) + (n + 1)·L* (DATA L* = 6n).
- As in T41: an edge-level "toward c" potential is not monotone even inside a frozen W-phase (topfix AWAY_F = 2n − 1); progress must be
  counted in W.

## DONE / FINDINGS / NEEDS
- DONE: this note; docs/lit/T41b-frozen-target-check.py (reads L-SI's experiments/si/root/common.py and experiments/new/box21/n5x.py; cut rule
  copied from experiments/si/frz/fwphase.py, read only); runs on runquad, s3quad, topfix n 3, 4, 6, 8, 10, 12, alt_all, lib41, experiments/si.
  Logs in the session scratchpad t41b/ (not committed).
- FINDINGS:
  - Leaving c happens INSIDE frozen W-phases (topfix: ~80% of departures; library: 45-48%), not only at cuts.
  - Per frozen W-phase it is O(n) on topfix (d1_n: AWAY_F = 2n − 1 in a frozen W-phase of 6n transitions; exact n = 3..12) and ≤ 4 in the library.
  - Topfix's Θ(n²) per-phase count = (n + 1) frozen W-phases × O(n): it enters W-SPLIT through the number of frozen W-phases (4n − 4 λ_W cuts).
  - runquad has no frozen W-phase (all 240 departures at λ_W changes).
- NEEDS: none from the owner.
