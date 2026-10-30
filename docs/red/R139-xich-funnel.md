# R139: ΞCH at ONE vertex is quadratic inside one W-run. R120's wave observer on one-world mkr is the funnel: ΞCH_F(obs) = K·m + K + 1, all of it path-set changes (529 = 1.47n at n 360). But ΞCH_F(v) ≤ |F|, so XI-CH-POLY is again EQUIVALENT to polynomial W-runs (given FL). No kill
L-RED successor 33 (Opus 5.5; D1/D18). Lead 2026-10-30 13:34Z: "R139 = adversary against XI-CH-POLY ... make ΞCH_F(v) at ONE vertex
super-linear inside ONE W-run ... (1) Measure ΞCH per vertex on your quadratic families ... spread ... or concentrated? (2) Try to
concentrate it ... a single funnel vertex upstream of the fan. (3) If concentration fails, state the exact obstruction". Written
2026-10-30 from 13:36Z (date -u). Labels: PROVED (lane) / DATA / READING. Not a TARGET.md claim. G-N5-TIME OPEN.
- ΞCH_F(v): the transitions of the W-run F at which Ξ(v) changes, as in L-NEW box 86's pch.py (l-new 584e6e19): LCH (cycle node), PCH (path
  set, λ fixed), LEN (length only); XICH = their sum.
- Counters:
  - L-NEW's box86/pch.py and box85/xirise.py, run unchanged from a worktree;
  - L-RED's zxc/zxc.py (R134);
  - L-RED's new xich/xichc.py (n5b SPEC valuations, independent of n5x).

## 1. Step (1): spread or concentrated? (DATA)
- latew_K16_m32 (R138, R*_F = 512): max ΞCH per vertex = 33 (xirise.py), so max ΞCH ≈ 2m + 1. Spread: the quadratic R*_F sits over
  many late adopters, each with a linear count.
- fx_K8_m32 (R137): max ΞCH = 137 at one observer (pch.py; PCH 137, LCH 0, LEN 0). Concentrated: K·m/2 + K + 1, because each of the two
  observers reads half the reactors.

## 2. Step (2): the funnel exists. R120's Even wave observer on mkrw (mix/obs2.py OWNER=0 ABOVE=a on span/mkrw.py K m)
- The observer obs (Even, priority 0) has edges y_j → r_j to every reactor, so its σ̄-play is the newest flipped reactor's play. Every wave
  step therefore changes obs's path set: obs is upstream of the whole fan.
- DATA (one W-run each; zxc.py, pch.py, xirise.py and xichc.py agree where run):

  | K | m | n | |F| | ΞCH_F(obs) | PCH | LCH | LEN | ΞCH / n |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | 4 | 8 | 96 | 44 | 37 | – | – | – | 0.39 |
  | 8 | 16 | 184 | 152 | 137 | 137 | 0 | 0 | 0.74 |
  | 12 | 24 (pin) | 272 | 324 | 301 | – | – | – | 1.11 |
  | 16 | 32 | 360 | 560 | 529 | 529 | 0 | 0 | 1.47 |

- ΞCH_F(obs) = K·m + K + 1 exactly, which is about 0.94|F|. With m = 2K and n ≈ 22K + 8, that is ≈ n²/242: quadratic at one vertex.
  Every change is a pure path-set change. W changes at each of them too (TXC 0; WCH = ΞCH in xirise).
- L-LIT T52's data maximum (63, gate_K64) understated this.
- Pin xich/instances/obs_K12_m24 (n 272, ΞCH 301): sha1 in check.sh, xeng identical, Oink zlk OK with strategies verified.

## 3. Step (3): why it stops at quadratic (PROVED, lane; immediate)
- ΞCH_F(v) counts transitions of F, so ΞCH_F(v) ≤ |F|.
- Conversely, by L-NEW box 86 Theorem RSTAR-PCH (R*_F ≤ m_E n (n + 1 + P*_F)) and box 85 FREE-RED (|F| ≤ (n − 1)(R*_F + 1) + FL_F):
  |F| ≤ poly(n) · (1 + max_v ΞCH_F(v)) + FL_F.
  These are L-NEW lane statements, as stated there; P*_F ≤ max_z PCH_F(z) ≤ max_z ΞCH_F(z).
- So XI-CH-POLY ∧ FL-POLY ⇔ polynomial W-runs. The funnel realises the upper end, ΞCH ≈ 0.94|F| at one vertex.
- Per-vertex Ξ-monotonicity is therefore no obstruction to concentration. The only cap is the W-run length.
- Exact statement for L-NEW 38's box 87 (READING): no lemma of the form "per-vertex ΞCH ≤ (something linear) × (per-vertex monotonicity)"
  can hold. A polynomial bound on ΞCH must bound |F|. The four lanes' targets (P*, ZFL, XI-CH-POLY, R*-POLY) are all polynomially
  equivalent to G-N5-TIME on W-runs.

## DONE / FINDINGS / NEEDS
- DONE: xich/xichc.py (second counter); pin xich/instances/obs_K12_m24; check.sh "R139".
- FINDINGS:
  1. DATA: latew is spread (max ΞCH 33). fx and obs are concentrated.
  2. DATA: ΞCH_F(obs) = K·m + K + 1 at ONE vertex in ONE W-run (529 = 1.47n at n 360), quadratic, pure PCH. The funnel is R120's
     observer.
  3. PROVED (lane, immediate): ΞCH_F(v) ≤ |F|. With L-NEW's RSTAR-PCH and FREE-RED, XI-CH-POLY ∧ FL-POLY ⇔ polynomial W-runs. No new
     obstruction exists below the run length, and there is no kill.
- NEEDS: none from the owner. Lead: tell L-NEW 38 box 87 that concentration is free (ΞCH ≈ 0.94|F|), so any ΞCH bound is a W-run bound.
