# R142: adversary against CONJECTURE BIP-POLY (L-NEW box 88). No kill. Exact BIP simulators in two engines reproduce N5 on obs_K12_m24 (324 = 324). Abstract hill-climbing finds BIP runs up to 2n (24 at n 12). Static ρ removes box 82's doubling on ogl_3 (exhaustive: ≤ 4 T-values, against 8) and ogl_4 (sampled: ≤ 4, against 16)
L-RED successor 33 (Opus 5.5; D1/D18). Lead 2026-10-30 14:46Z: "R142 = adversary against BIP(ρ, τ) directly (L-NEW 38 box 88, l-new e975c729,
docs/new/N5-ONEP-box88.md) ... Goal: super-polynomial or clearly super-quadratic BIP runs ... make the τ-optimiser realise a bad relaxation
order. If ARENA-MAX forbids that, state the exact obstruction as a lemma candidate." Written 2026-10-30 from 14:48Z (date -u). Labels:
PROVED (lane) / DATA / READING. Not a TARGET.md claim. G-N5-TIME and BIP-POLY OPEN.
BIP(ρ, τ) (box 88 §2), quoted:
- «Even strategies σ_t; offers Iρ_t := {(y, z) : val(σ_t, ρ)(z) ▷ val(σ_t, ρ)(σ_t y)}; step σ_(t+1) := the val(·, τ)-optimum of
  σ_t ∪ Iρ_t (S4a's rule).»
- «CONJECTURE BIP-POLY: every BIP(ρ, τ) run (any game, any two Odd strategies, any start) has at most p(n) steps.»

## 1. Two engines, validated on real N5 (DATA)
- The two engines:
  - bip/bip.py runs on L-COMP's n5b SPEC internals: offers from N5.improving on G_ρ; step = Odd's optimal counterstrategy on the dual of
    the arena, as in n5b's S4a.
  - bip/bip2.py is an independent re-implementation on L-SI's si.py, as experiments/new/n5.py uses it.
- Realisation check. On obs_K12_m24 (R139) σ̄ is constant over states 0-323 of N5's run: the first σ̄ change is at the final state 324.
  So BIP(σ̄_0, τ_0) started from σ_0 is that run: bip.py gives 324 steps, and N5 gives 324 iterations.
  - This is mechanism (B) of box 88, realised in real N5: BIP runs of Θ(K·m) = Θ(n²) exist (R139's family), with ρ = σ̄_0 and τ = τ_0 of
    the obs family.

## 2. Abstract search (DATA)
- bip.py --search hill-climbs over (game, ρ, τ, σ_0) at once (mutations of succ / prio / owner, with ρ, τ, σ_0 repaired and resampled),
  480 s per seed. bip2.py agrees on every reported instance:

  | seed | n | best BIP steps | / n |
  | --- | --- | --- | --- |
  | 1 | 8 | 13 | 1.6 |
  | 2 | 10 | 15 | 1.5 |
  | 3 | 12 | 24 (pin bip/instances/bipsearch_n12) | 2.0 |
  | 4 | 14 | 20 | 1.4 |

- A random baseline (300 instances, n 8) gives at most 4. Pins: bipsearch_n12 and bipsearch_n8 (sha1 in check.sh; bip.py = bip2.py).
- These are abstract instances. Whether their (ρ, τ) is realisable as (σ̄, τ) on a W-run of N5 is not checked; BIP-POLY as stated covers
  them anyway.
- No growth beyond about 2n is visible at n ≤ 14.

## 3. Designed: static ρ on box 82's Odd-gated ladder (DATA, bip/oglx.py)
- On ogl_k, τ is honest at every gate and ρ is ANY static routing: each gate either honest, reading u(j, c), or routed, reading
  u(j, 1 − c).
- ogl_3 exhaustive (1,024 routings × 32 starts = 32,768 runs): at most 4 distinct W(T) values, in 3 steps. Box 82's R2 model, with ρ_t
  changing in time, reaches 8.
- ogl_4 (20,000 sampled pairs): at most 4 W(T) values, against 16.
- READING (why). With ρ static, each reader's two gates have a fixed mode:
  - (honest, honest): the offer follows the ρ-order of the two children.
  - (routed, routed): the offer is made exactly when ρ and τ disagree on the order of the two children (a disagreement detector).
  - mixed: both gates read the same child in ρ, so their ρ-values tie and nothing is offered (GATE-COLLAPSE's static form).
  - Box 82's counter needs each reader's mode to CHANGE over time: routed exactly while it holds the other gate and is not scheduled. A
    fixed ρ cannot do that.
  - In N5 the mode changes are σ̄'s re-routings. These are mechanism (O) of box 88, outside BIP.

## 4. The obstruction for the proof side (READING; lemma candidate)
- Candidate STATIC-MODE. In BIP(ρ, τ) the offer structure at a vertex y is fixed by the static map ρ. (y, z) is offered iff val_ρ(z) ▷
  val_ρ(σ y), and val_ρ is the one-player valuation of G_ρ, which is monotone along the run (BIP-MON).
  - A blocked-then-released edge (W-better, not offered, later offered) needs val_ρ(z) to overtake val_ρ(σ y).
  - That is an overtaking in G_ρ, a one-player game. R17 bounds N5 on one-player games by (n² − n + 1)(n + m) iterations, but BIP's steps
    are driven by τ, not ρ, so that bound does not transfer directly.
  - The exact gap: a bound on the number of ORDER FLIPS between pairs of val_ρ-values along a BIP run. In a one-player game each val_ρ is
    monotone, and flips between two monotone sequences are unbounded only if both climb without bound in the lex order.
- My data never shows more than about 2n steps in abstract BIP. The quadratic realised family (obs) has τ-climbs of K·m.
- So the adversary's best is Θ(n²) (realised) and about 2n (random). There is no super-quadratic BIP run.

## DONE / FINDINGS / NEEDS
- DONE: bip/bip.py (n5b) and bip/bip2.py (si.py), the BIP engines; bip/oglx.py (exhaustive static-ρ ogl); pins bip/instances/bipsearch_n12,
  _n8; check.sh "R142".
- FINDINGS:
  1. DATA: BIP(σ̄_0, τ_0) = N5 on obs_K12_m24 (324 = 324). A realised BIP run is quadratic.
  2. DATA: abstract BIP hill-climb reaches 13 / 15 / 24 / 20 at n 8 / 10 / 12 / 14 (≤ 2n); bip.py = bip2.py.
  3. DATA: static ρ removes box 82's doubling (ogl_3 exhaustive: 4 against 8; ogl_4 sampled: 4 against 16).
  4. READING: the doubling needs time-varying routing (σ̄ re-routings, mechanism O). BIP-POLY's open core is the order flips between
     monotone val_ρ sequences. No kill.
- NEEDS: none from the owner.
