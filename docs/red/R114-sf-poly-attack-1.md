# R114: CONJECTURE SF-POLY (N5-SF), first attack. switchbestexp's SBC is linear (≈ 12N, 0.47n at N = 24); the two published snare-rule families are linear; I^glo doubles on the same games; N5-SF leaves I^glo's run at 16 of 364 steps, through a stale ESCAPE at an open cycle. DATA + READING; SF-POLY stays OPEN
L-RED successor 28 (Opus 5.5; D1/D18; Lead 15:28Z STEP 1). Written 2026-10-29 from 15:58Z (date -u). Subject: L-NEW's N5-SF
(claude/l-new docs/new/N5-SF-box54.md §1; tool experiments/new/box54/n5sf.py). Labels: DATA / READING / OPEN / DEAD. Not a TARGET.md
claim. Nothing here is super-polynomial. CONJECTURE SF-POLY stays OPEN.

## 0. Engines and checks
- Engine 1: L-NEW's n5sf.py (MODE=x), run read-only from a worktree of origin/claude/l-new.
- Engine 2 (new): experiments/red/sf/sf2.py. Written from the text of N5-SF-box54 §1 (S4a′: Odd fixed to σ̄(σ); S4b′ the mirror;
  S4c/S4d/S5 as SPEC). Its valuations come from L-COMP's PGSolver port (experiments/n5-second/n5b.py → hard-families/pgsolver_si.py),
  not from L-SI's si.py, which n5sf.py uses. `--mode spec` uses n5b's SPEC choice rule; `--mode orig` uses PGSolver's per-vertex
  counterstrategy rule.
- Agreement. On switchbestexp N = 1..5, sf2 gives the same iterations and SBC as L-NEW's table in both modes (20, 58, 135, 258, 364;
  SBC 1, 4, 11, 26, 49), and N = 12 reproduces L-NEW's 684 / SBC 138. Every new family below gives the same iteration count in n5sf.py
  and in sf2 (§2: fsubexp N = 1..6, fearnley N = 2..8 with and without gadgets).
- Correctness: experiments/red/sf/okcheck.sh compares sf2's regions with Oink 8fbf0a7 `--zlk` (falling back to `--tl`) and runs
  harness/verify.py on sf2's strategies. Result REGIONS OK + "strategy verified" on fsx_3, fsx_6, fe_8, feng_8, sbe_4 and fe_4.
- Start: the SPEC S3 default (best reward, both sides) unless stated. §3 also uses PGSolver's own setting (its transformation and
  the last-edge start).
- SBC (as L-NEW defines it) = the σ-changes at which σ̄ changes. "SBC_τ" is the mirror. sf2 also prints LAM, which is 0 everywhere below.

## 1. switchbestexp, larger N (DATA; sf2 spec; S3 start; n5sf.py runs for N = 18, 20, 24 were started at 15:57Z and are still running)
| N | n | sha1 (12) | N5-SF iterations | SBC_σ | SBC_τ | SBC_σ / n |
| --- | --- | --- | --- | --- | --- | --- |
| 12 | 310 | c1444919e1bc | 684 | 138 | 12 | 0.45 |
| 14 | 360 | (L-NEW) | 750 | 179 | | 0.50 |
| 16 | 410 | (L-NEW) | 928 | 232 | | 0.57 |
| 18 | 460 | 798ff17c09a0 | 662 | 215 | 18 | 0.47 |
| 20 | 510 | 065c59ca4d2a | 737 | 266 | 20 | 0.52 |
| 24 | 610 | 26de1b35e17c | 770 | 289 | 24 | 0.47 |
- READING. N = 12 to 24 doubles N, and SBC goes 138 → 289, i.e. it doubles too: about 12N, linear. The iteration count is not even
  monotone (928 at N = 16, 662 at N = 18). L-NEW's "0.45n → 0.57n, still rising" (N ≤ 16) was the steep start. It does not continue.
  My first reading in the 15:38Z message ("≈ 0.9N², quadratic") was wrong: retracted.
- DEAD as a kill target: switchbestexp drives SBC only linearly (DATA to N = 24).

## 2. The published families for snare-based rules (L-LIT T46 §3 item 1), ported (DATA)
- experiments/red/sf/fsubexp.py ports PGSolver d3cd624's friedmannsubexp.ml (90 lines; "Friedmann's Subexponential Lower Bound for
  snare-based rules", the DAM 2013 family per T46) and fearnleysubexp.ml (86 lines; `-nogadget` as in the OCaml), line by line with
  pgsolver_port.SymbolicPG. That SymbolicPG matched the OCaml binary byte for byte on switchbestexp. The new ports have NOT been
  diffed against a binary, because no OCaml toolchain is in this container. Source opened: git clone of github.com/tcsprojects/pgsolver
  at d3cd624.
- N5-SF from the S3 start, sf2 = n5sf.py iteration counts (lnew_small run, 15:5xZ):
  | family | N | n | iterations | SBC_σ |
  | --- | --- | --- | --- | --- |
  | friedmannsubexp | 1..6 | 20, 44, 77, 119, 170, 230 | 4, 8, 11, 14, 18, 23 | 1, 5, 9, 12, 16, 20 |
  | fearnleysubexp | 2, 3, 4, 5, 6, 8 | 38 .. 209 | 6, 9, 12, 15, 18, 24 (= 3N) | ≤ 2N |
  | fearnleysubexp -nogadget | 2, 3, 4, 5, 6, 8 | 31 .. 109 | 6, 9, 12, 15, 18, 24 | |
  sha1 (12): fsx_3 907738682bdb, fsx_6 67408669123c, fe_8 8e259baa798f, feng_8 3f912f81063e.
- DEAD as kill targets from the S3 start: both are linear. One caveat is OPEN: Friedmann's DAM 2013 bound is for a snare-MEMORISING
  rule, which may need its own start and memory. The paper is NOT OPENED (T46), so I cannot say whether some other start would
  revive the family.

## 3. PGSolver's own setting (DATA)
- experiments/red/sf/pgtrans.py applies PGSolver's SI preprocessing (alternating transformation + cheap escape cycles, pgsolver_si.py)
  and sets σ_0 to PGSolver's last-edge start (τ_0 = S3 default; DECOUPLE: Even's distinct-σ sequence does not depend on it).
- switchbestexp' N = 1..6 (n 61 .. 271; tsbe_5 sha1 d8a680151763): N5-SF 22, 60, 137, 260, 366, 414, SBC_σ 1, 4, 11, 26, 49, 56. That is
  the raw game's count + 2. The transformation does not revive the counter.

## 4. Where N5-SF leaves the counter: I^glo vs N5-SF on the same σ (DATA + READING)
- experiments/red/sf/evseq.py builds Even's distinct-σ sequence (DECOUPLE) under two rules from the same σ_0. "sf" is S4a′. "glo" is
  the optimum of the arena game with Odd FREE (I^glo / Schewe in the Ξ frame), computed by switch-all SI inside the arena. Both use n5b
  valuations. The S4c fallback is the same for both.
- I^glo, raw switchbestexp, S3 start: 134, 286, 590, 1198 σ-changes at N = 3..6, with σ̄ changing 10, 24, 54, 116 times along them. It
  doubles. PGSolver's switch-best on the transformed game gives 137, 289, 593, 1201, i.e. these + 3. N5-SF gives 135, 258, 364, 412.
- `evseq.py --shadow` follows N5-SF's run and computes I^glo's step from every σ it visits. On sbe_5 the two steps differ at only 16 of 364
  steps (shadow5 below), and in two ways:
  (a) v_i → r_{i+1} vs v_i → v_{i+1} (upper-selector helpers; 3 steps; harmless).
  (b) 13 steps of the form "sf: x → y, y → l0, g_j keeps h_j; glo: x → w, y → w, g_j → g'_j", at the reset steps right after a bit is set
      (102, 179, 218/219, 252, 291/292, 297, 298, 303, 318/319). N5-SF routes the bit selector to bit 0 and keeps the lower cycles' g-edges
      on the cycle. I^glo routes to the new high bit and opens them.
- Anatomy of (b) at step 218, N = 5 (/tmp debug script, numbers from n5b's Ξ):
  - Bits 0, 1 are set, so σ̄(h0) = m0 and σ̄(h1) = m1 (Odd escapes). Bit 2 has just been set. At 217 f0 moved to c, which OPENS cycle 0.
    But Odd still escapes at h0, because the stay route via c reaches bit 2 and is better for Even.
  - In N5-SF's frame σ̄(h0) = m0 is frozen. Within the arena Even can re-point the route above m0 (z0 → v0 → v1 → … → bit 2). Then
    y → l0 → k0 → h0 → m0 → … collects {m0, m2, m3, …}, which beats the w route {m2, m3, …}. So N5-SF picks x → y → l0.
  - Truly, Odd at h0 then prefers to stay in the open cycle (the escape has become too good for Even). σ̄(h0) flips at 219, as the SBAR
    trace shows.
  - This is T46's Mechanism 2 (escape selection), not a snare closing: an Odd reply that is stale only because Even improved the
    route behind it.
- The damage is indirect. From N5-SF's own state at 219-221, I^glo makes the same moves: f4 → g4, e4 → f4, g4 → h4, so cycle 4 closes
  early (SBAR h4 at 221). So the state is already off the counter after (b) at 218/219. The two-step detour lowers the lane's value
  relative to I^glo's run, and that makes cycle 4's three cycle edges improving one after another. From there the counter skips
  (N = 5: bit 4 set at count 1011; N = 6: bits 4 and 5).
- READING. N5-SF's extra optimism over I^glo appears exactly where an Odd reply is stale behind an improvable route. On this
  family that costs the counter at the first reset above count 11.
- Single-edge-class removals in switchbestexp (sbev.py `--drop` fc / ed / ga / fa) and lane spacing c = 8, 12 (`shift` and `scale`)
  make N5-SF shorter, never longer (N = 4, 5: ≤ 364). Blind lane tuning does not repair it.

## 5. What a kill needs (READING; for the next design step)
- A counter whose reset never leaves an Odd reply stale behind a route that Even can improve within ONE arena step. Equivalently: at
  every visited state, S4a′'s optimum equals I^glo's, except at bit-set steps, where the difference must not change Even's choice.
- Concretely, for switchbestexp-type counters: when a cycle opens, Odd at its centre must stay in the SAME iteration. So the opening
  exit must be worse for Even than the escape route, while it is still improving for Even's cycle node. switchbestexp's f_i → c (into
  the newest bit) violates this.
- OPEN: a family where N5-SF's SBC is super-linear for large n. Best found so far is linear.

## Files
- experiments/red/sf/: sf2.py (second engine), sftrace.py (named trace with σ̄ changes), evseq.py (sf vs glo sequences; --shadow),
  fsubexp.py (friedmannsubexp + fearnleysubexp ports), sbev.py (switchbestexp with lane spacing / edge-class drops; c = 6 selftest =
  pgsolver_port byte for byte), pgtrans.py (PGSolver preprocessing + last-edge start), okcheck.sh (Oink + verify.py).
- check.sh block "R114": sf2 on switchbestexp N = 2 = 58 / SBC 4; fsubexp N = 3 = 11; fearnleysubexp N = 3 = 9; sbev selftest.

## DONE / FINDINGS / NEEDS
- DONE: sf2.py (second engine, exact match with n5sf.py); switchbestexp to N = 24; the friedmannsubexp and fearnleysubexp ports with
  N5-SF runs; PGSolver-setting runs; I^glo-vs-N5-SF shadow on N = 5 with the anatomy of the divergence.
- FINDINGS: (1) DATA: switchbestexp's SBC is linear (≈ 12N; 289 = 0.47n at N = 24). (2) DATA/DEAD: friedmannsubexp and
  fearnleysubexp are linear under N5-SF from S3 (4..23 and 3N). (3) DATA: I^glo doubles on raw switchbestexp (286, 590, 1198), while N5-SF
  agrees with it at 348 of 364 steps on N = 5. The breaking steps are stale escapes behind improvable upper-selector routes (Mechanism 2),
  and they put the lane state where a high cycle closes early. (4) OPEN: SF-POLY.
- NEEDS: none from the owner.
