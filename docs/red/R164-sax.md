# R164 depth-3 re-arm: the switch-all counter dies at S4a (W-monotone arena optimum), NOT at the fixed τ (L-RED successor 38)
Started 14:47Z (Lead GO 14:47Z), written ~15:1xZ (date -u), 2026-10-31. Labels: DATA, PROVED (lane, elementary), READING, OPEN.
- Template: L-SI box 58 (l-si cb9a8444, docs/si/N5-ANC-box58.md §5). Classical switch-all SI re-routes one pair 2^N times on
  switchallexp_N while satisfying every lane lemma.
- The Lead's question: which N5 feature kills that counter (S4a's pointwise optimum vs switch-all; τ fixed on a W-run), and can the
  same 2^N re-route be rebuilt inside one N5 W-run?

## Tool: experiments/red/sax/hyb.py (hybrids, si.py engine, best-reward start, both steps from the same (σ, τ) as n5.py)
| mode | Even step | Odd | what it isolates |
| --- | --- | --- | --- |
| sa | switch-all on Iσ (best Ξ target per vertex) | σ̄ (best response) | classical SI |
| n5 | S4a: one-player optimum vs τ over A(v) = {σ(v)} ∪ Iσ(v) | S4b (τ moves) | N5 |
| H1 | switch-all on Iσ | S4b (τ moves) | N5 with S4a replaced by switch-all: does the fixed τ kill the counter? |
| H2 | S4a against σ̄_k (Odd's best response to the current σ) | σ̄ | S4a without a separate τ |
| H3 | S4a against the START τ | frozen | S4a in one W-world, with fallbacks |
| H4 | switch-all restricted to Iσ ∩ (W-improving vs τ) | S4b | W-monotone switch-all |

- Every mode falls back to one switch-all step when nothing changes, as n5.py does.
- The «τ-runs» are maximal stretches with τ constant. They are an upper proxy for W-runs; desc2.py gives the fallback-free W-runs.
- Validation of the n5 mode: hyb n5 = n5.py = n5b SPEC iteration counts on switchallexp N 1-6 (5, 8, 7, 8, 10, 12 = L-NEW's
  switchallexp.csv) and on switchbestexp N 3, 5 (41, 55). Oink zlk regions match n5.py, and n5.py's strategies verify (sb3, sb5,
  sx6).
- Instances: `python3 experiments/hard-families/pgsolver_port.py switchallexp|switchbestexp N`. They are not pinned (generated on the
  fly; the generator is trunk's).

## 0. Answer
- The FIXED τ does NOT kill the switch-all counter. With switch-all for Even and N5's own Odd step (H1), switchallexp_N takes 10, 30, 70,
  150, 310, 630 iterations (= classical SI), and at N = 6, 618 of the 630 sit in ONE τ-run.
  - So the counter runs entirely inside a stretch where τ never moves. «τ fixed on a W-run» is not the property that kills it.
- S4a kills it. Every mode with S4a's arena optimum is fast on switchallexp: n5 12, H2 12, H3 106 at N = 6. So is H4 (36), the
  switch-all variant restricted to W-improving edges.
- PROVED (lane, elementary): S4a is W-MONOTONE. If τ is unchanged, W_(k+1)(v) ⊵ W_k(v) for every v, where W = the valuation of σ against
  the fixed τ.
  - Proof: σ_(k+1) is Even's optimal positional strategy in the one-player arena H (Odd fixed to τ, Even restricted to A(v) ∋ σ_k(v)).
  - An optimal strategy of a one-player game is pointwise at least as good as every strategy of the same arena, and σ_k is one.
  - Both valuations are computed in H. W_k is σ_k's valuation in H, because σ_k uses only edges of H. □
- DATA: the switch-all counter's CARRIES are W-DROPS.
  - In H1, the iterations where some vertex's W (against the current, unchanged τ) strictly DROPS number 3, 9, 23 at N = 3, 4, 5. That is
    about 2^N, the counter's carry rate; vertices dropped: 8, 36, 122.
  - n5 and H4 have 0 drops.
  - READING: switch-all encodes its counter in Ξ (the best-response valuation) and pays each carry with a W-drop against τ. S4a's
    W-monotone optimum cannot take a W-drop, so the encoding is impossible.
- The template therefore cannot be rebuilt inside one N5 W-run AS IS. Its carries are exactly what S4a forbids.
  - A counter inside a W-run must count monotonically in W itself: each carry is a W-INCREASE at a higher bit with re-fixes below (the
    DESC of R162 / R163).
  - fbg does this once per phase (depth 2). Nothing has done it at depth 3.
  - This is a READING about the template, not a proof that W-monotone counters are short. A monotone binary counter is W-monotone too.
- The second Friedmann template, switchbestexp_N, is NOT slow for N5:
  - N5: 20, 32, 41, 47, 55, 62, 68, 77 iterations at N = 1-8. Longest fallback-free W-run |F| = 18, 31, 44, 57 at N = 2, 4, 6, 8
    (= 6.5N + 5, linear, ≈ 0.27n).
  - H2 (S4a vs best response, no τ): 20, 58, 135, 258, 364, 412, 456, 489. It is slower than N5 (here the separate τ helps), but it
    flattens (second differences turn negative), not exponential.
  - H3 (S4a vs the frozen start τ, one W-world with fallbacks 4(N − 1)): 20, 62, 107, 157, 220, 296, 385, 487, with second differences
    → 13. That is QUADRATIC in N, ≈ 6.5N², ≈ 0.011n² at n 210. Not an N5 run (τ frozen, fallbacks).
- DATA, a REAL single-W-world N5 run: start from (best-reward σ, τ*), with τ* = N5's final τ (no Odd improving edge, so τ never moves,
  and no fallbacks; sax/taustar.py).
  - Iterations: 8 and 12 on switchallexp N = 3, 6; 13, 25, 37, 49 on switchbestexp N = 2, 4, 6, 8 (linear, ≈ 0.23n).
  - So H3's quadratic count comes from its non-optimal frozen τ plus switch-all fallbacks, not from S4a in one W-world.
- The search side, |F|/n² growth by climbing (wclimb.py REARM=3, objective the longest W-run): see §2.

## 1. DATA tables
### switchallexp_N (n = 14N + 7); iterations / longest τ-run
| N | sa | n5 | H1 | H2 | H3 (fallbacks) | H4 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 10 / 10 | 5 / 3 | 10 / 5 | 5 / 5 | 5 (0) / 5 | 10 / 5 |
| 2 | 30 / 30 | 8 / 5 | 30 / 22 | 8 / 8 | 14 (4) / 14 | 28 / 20 |
| 3 | 70 / 70 | 7 / 3 | 70 / 61 | 8 / 8 | 28 (8) / 28 | 50 / 41 |
| 4 | 150 / 150 | 8 / 3 | 150 / 140 | 8 / 8 | 49 (12) / 49 | 31 / 21 |
| 5 | 310 / 310 | 10 / 4 | 310 / 299 | 10 / 10 | 75 (16) / 75 | 34 / 23 |
| 6 | 630 / 630 | 12 / 5 | 630 / 618 | 12 / 12 | 106 (20) / 106 | 36 / 24 |

- W-drops (WMON=1; iterations with a drop / vertices): H1 3 / 8, 9 / 36, 23 / 122 at N = 3, 4, 5; n5 and H4 0 / 0.

### switchbestexp_N (n = 25N + 10); iterations
| N | sa | n5 | H1 | H2 | H3 (fallbacks) | H4 | N5 longest W-run \|F\| (desc2) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 21 | 20 | 21 | 20 | 20 (0) | 21 | |
| 2 | 61 | 32 | 61 | 58 | 62 (4) | 39 | 18 |
| 3 | 141 | 41 | 141 | 135 | 107 (8) | 43 | |
| 4 | 301 | 47 | 301 | 258 | 157 (12) | 49 | 31 |
| 5 | 621 | 55 | 621 | 364 | 220 (16) | 68 | |
| 6 | | 62 | | 412 | 296 (20) | | 44 |
| 7 | | 68 | | 456 | 385 (24) | | |
| 8 | | 77 | | 489 | 487 (28) | | 57 |
- H1 = sa again on switchbestexp (the fixed τ does not slow switch-all down).

## 1b. PLAT (Lead 15:46Z, L-SI box 58 §7: equal-swap-key repeat escapes of one (Odd s, old choice x) inside one W-run)
- Tools:
  - L-SI's anc.py (l-si 6370a35f, read-only, run from a git-archive) on N5 runs.
  - sax/ancx.py: anc.py's text with its trace replaced by a hyb.py hybrid run. Its n5 mode reproduces anc.py's own N5 numbers on
    switchallexp_4 (8 iterations, ESCEQ 0, MAXESC_SX 1).
  - sax/platx.py prints the longest plateau with labels.
  - sax/wrise.py checks L-SI's candidate (b), a strict W-rise between re-openings.
- DATA, N5 itself: PLAT ≥ 2, growing with n, in ONE W-run. On fbA_K_m_m2 (R158 design A, fb/mkfb.py; the gates never bind, E2 never
  switches):
  | instance | n | \|F\| (= whole run, one W-run) | MAXESC_SX | MAXPLAT | ESCEQ |
  | --- | --- | --- | --- | --- | --- |
  | fbA_K4_m8_m8 (R158 pin) | 136 | 44 | 4 | 3 | 9 |
  | fbA_K4_m16_m16 | 208 | 76 | 4 | 3 | 21 |
  | fbA_K8_m8_m8 (R164 pin) | 192 | 88 | 8 | 7 | 21 |
  | fbA_K8_m16_m16 | 264 | 152 | 8 | 7 | 49 |
  | fbA_K16_m8_m8 | 304 | 176 | 16 | 15 | 45 |
  - PLAT = K − 1 and MAXESC_SX = K, independent of m and m2.
  - The plateau is the Odd gate a_j (j even): it escapes from its old choice g_j once per pivot round (period m + 3), always at the
    same swap key. On fbA_K8_m8_m8: s = a4, x = g4, escapes at 5, 16, 27, …, 82, all with og (1, 117).
  - PLAT is therefore LINEAR in n: one escape per rung of h's ladder. This kills the data bound «PLAT ≤ 1» (L-SI corpus), but not
    PLAT-POLY.
  - Candidate (b) holds here: on fbA_K4_m8_m8 (s = a4, escapes 5, 16, 27, 38), W(x) and W(x₂) both strictly rise between
    consecutive escapes, and τ is unchanged (wrise.py). The re-openings are paid by the pivot's ladder rises.
  - Faithfulness: xeng identical and Oink OK on fbA_K8_m8_m8, and fbA_K4_m8_m8 is already checked in check.sh (R158).
- DATA, hybrids (anc.py fields inside W-runs; W-runs = τ constant and no fallback):
  | instance | H1 (switch-all, N5 Odd) MAXPLAT / MAXESC_SX | H4 (W-monotone switch-all) | n5 |
  | --- | --- | --- | --- |
  | switchallexp_3 / 5 / 6 | 2 / 3, 14 / 15, 30 / 31 | 1 / 2, 1 / 2, 1 / 2 | 0 / 1, 0 / 0, 0 / 0 |
  | switchbestexp_3 / 4 / 5 / 6 | 2 / 3, 6 / 7, 14 / 15, 30 / 31 | 1 / 2 (all) | 1 / 2 (all) |
  - The escape engine runs INSIDE a fixed-τ run when Even uses switch-all: PLAT 2^(N−1) − 2.
  - Restricting switch-all to W-improving edges (H4) brings PLAT to ≤ 1 on both families, and so does N5.
  - READING: W-monotonicity is the property that kills the exponential plateau on both templates. What it cannot stop is a plateau
    paid by W-rises: fbA's K − 1, one per ladder rung.
- The precise remaining question for a super-polynomial PLAT: a single Odd (s, x) must be re-opened at an equal key once per W-rise of
  x's play, and x's play must take super-polynomially many W-rises. That is again a W-monotone counter (§3): the per-vertex W-chain of
  x must be long. That needs DESC* at depth ≥ 3 (R163).

## 2. Search side (hd/wclimb.py, new REARM=3: objective (longest W-run |F|, −fallbacks); n5b SPEC traces)
- Objective (|F|, −fallbacks), with |F| = the longest fallback-free W-run of the n5b SPEC trace. Mutations as in R160: retarget, add or
  drop an edge, change a priority, change a start choice; the start stays valid. 40 min per climb, timed out (best kept in the log only).
| n | seed (seed \|F\|) | climb seeds | best \|F\| | \|F\|/n | \|F\|/n² |
| --- | --- | --- | --- | --- | --- |
| 32 | w_re3_1 (21) | 1, 3 | 36, 42 | 1.31 | 0.041 |
| 32 | hit_b6a_1 (23) | 2, 4 | 31, 44 | 1.38 | 0.043 |
| 17 | hd_H5 (5) | 11, 12 | (running) | | |
| 47 | hd_H15 (15) | 13, 14 | (running) | | |
- READING: at n ≤ 47, climbing finds |F| of order n (1.3n–1.4n at n 32). This is no evidence of super-quadratic growth: the designed
  quadratic families have |F|/n² ≈ 0.004 only at n ≥ 200, below what a climb at n 32 can separate.
- The climbed games are NOT pinned and were not checked with xeng / Oink (the climb timed out before writing its best). They are data,
  not counterexamples, and claim nothing.

## 3. What the proof side should use (READING; for the Lead / L-SI)
- Name the feature: S4a's W-MONOTONICITY inside a W-run (lemma above), plus its arena optimality.
  - The fixed τ alone is useless: H1 keeps τ fixed for 618 of 630 steps and is exponential.
  - Box 58's barrier lemmas ([R15a], [R57], [PLAY], [IMP]) hold for H1 as well. Any bound has to use «W never drops in a W-run».
  - On switchallexp that property alone (H4) is already enough to kill the counter.
- What remains open: a W-MONOTONE counter. Each vertex's W climbs a chain of 2^Θ(n) values, so monotonicity bounds nothing by itself.
  - The question becomes whether S4a's arena optimum can climb such a chain with nested carries, i.e. the R162 / R163 DESC* at depth ≥ 3
    in the core.
  - fbg does depth 2, with DESC* ≈ |F|. The R158 (A)/(B) obstruction is the only one on record.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/red/sax/hyb.py; hd/wclimb.py REARM=3; check.sh block R164 (hyb n5 = n5.py counts, H1 = sa counts and
  W-drops at N = 3).
- FINDINGS:
  - DATA: the fixed τ does not kill the switch-all counter (H1 exponential, 618/630 in one τ-run).
  - DATA: S4a does kill it (n5, H2, H3 and H4 fast on switchallexp).
  - PROVED (lane, elementary): S4a is W-monotone.
  - DATA: switch-all's carries are W-drops (3, 9, 23 iterations at N = 3-5).
  - DATA: switchbestexp is linear for N5 (|F| = 6.5N + 5); H3 (frozen τ) is quadratic.
  - READING: the template cannot be rebuilt in one W-run as is; the open object is a W-monotone nested counter (depth-3 re-arm).
  - |F|/n² growth: NOT found.
  - DATA (PLAT): N5 has PLAT = K − 1 in one W-run on fbA (linear; pin fbA_K8_m8_m8, PLAT 7); the hybrids show that W-monotone switch-all
    (H4) has PLAT ≤ 1 where switch-all (H1) has 2^(N−1) − 2.
- NEEDS: Lead: route «S4a W-monotonicity» to L-SI as the N5-specific property for the proof side. If wanted: L-LIT to open the source
  for Friedmann's lower bounds for switch-all / switch-best (I cite none here).
