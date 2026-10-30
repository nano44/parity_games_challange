# N5-ONEP (box 88): one W-run against the one-player τ-arena. NO-DEV (lane): if Odd's optimal reply gives Ξ = W at every state, |F| ≤ n − 1. σ̄ breaks the one-player picture in two separate ways (DATA): (O) σ̄ moves every transition and releases are Odd re-routings (latew, R138); (B) σ̄ is FROZEN at ρ ≠ τ and |F| > n − 1 anyway (obs_K12_m24, R139), so N5 inside a W-run is a "two-fixed-Odd-strategies" process (BIP). BIP-POLY is the cleanest open sub-target
L-NEW successor 38 (Opus 5.5), D14 / D18, Lead reading L40. Lead 2026-10-30 13:57Z (re-aim of box 87, taken as box 88): «bound |F| for
one W-run directly, using what N5 has and switch-all lacks: (i) τ fixed inside the W-run; (ii) S4a's arena optimum …; (iii) GP*'s W-change
structure … State exactly where σ̄ (Odd's optimal reply, which can change while τ is fixed) breaks the one-player picture.» Written
2026-10-30 14:02Z-14:40Z (date -u). Working note, unrefereed. Labels: PROVED (lane) / CONJECTURE / DATA / READING. Not a TARGET.md claim.
G-N5-TIME OPEN.

## 0. Sources and setting
- RESULTS R88 (BLOCKED, R*_T, GP*, Corollary FW-R*: «F has at most (n−1)(R*_T+1) W-changing transitions»), R89 (W-run, GP*-RUN,
  LATE-RISE); SPEC S1-S4 (σ̄ = Odd's pointwise-optimal counterstrategy to σ; S2 offers; S4a arena optimum against τ); boxes 85 (FREE-RED),
  86 (GAP-DEV), 87 (LEVEL-RED). L-RED R138 (l-red 5374e0a5, pin latew_K16_m32, sha1 6d34c161…), R139 (l-red 9326f166, pin obs_K12_m24,
  sha1 7df541fb…), R137 (fx family, regenerated as in box 87 §0). L-RED's R140 (the Friedmann port) was not yet pushed at 14:40Z, so (ii)
  is not yet checked against it.
- In a W-run F: τ is fixed, W_t = val(σ_t, τ) is Even's valuation in the ONE-PLAYER arena G_τ, Ξ_t = val(σ_t, σ̄_t). The offers Iσ_t are
  judged by Ξ_t; the step σ_(t+1) is the W-optimum (against τ) of the arena H_t = σ_t ∪ Iσ_t.

## 1. Lemma NO-DEV (PROVED, lane): the one-player picture holds exactly when Ξ = W, and then |F| ≤ n − 1
- Statement. If Ξ_t = W_t at every state t of a W-run F (for instance, if σ̄_t = τ at every Odd vertex for every t), then R*_F = 0,
  FL_F = 0 and |F| ≤ n − 1.
- Proof. A blocked edge needs a target with Ξ ◁ W (box 86 GAP-DEV), so there is none, and R*_F = 0. By R88 FW-R* (on W-runs by R89
  GP*-RUN), at most n − 1 transitions of F change W. Every transition of F switches some Even y along an edge of Iσ_t. A switched vertex
  strictly improves its Ξ (the standard improvement lemma the SPEC's Termination paragraph uses), so W_(t+1)(y) = Ξ_(t+1)(y) ▷ Ξ_t(y) = W_t(y).
  Hence every transition changes W, FL_F = 0, and |F| ≤ n − 1. □
- READING. With Ξ = W, S4a is one-player optimisation in G_τ restricted to the offered edges, and GP*'s Bellman-Ford rounds finish within
  n − 1 steps. Everything beyond n − 1 comes from Ξ ≠ W, i.e. (GAP-DEV) from Odd deviations σ̄ ≠ τ that poison targets.

## 2. Where σ̄ breaks it: two separate mechanisms (DATA, box88/release.py)
- Per late adoption (release of a blocked edge (y, z)), compare z's (σ_q, σ̄_q)-play at the last block state q with σ̄ at the release:
  ODD if some Odd vertex of that play changed σ̄ (Odd re-routed), EVEN otherwise (only Even switches on the poisoned play lifted Ξ(z));
  POISON-KEPT if every deviation (σ̄ ≠ τ) on that play is unchanged. SB_F := transitions where σ̄ changes somewhere.

  | instance | n | |F| | R*_F | SB_F | late adoptions | ODD | EVEN (poison kept) |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | latew_K16_m32 (R138) | 482 | 560 | 512 | 513 | 513 | 480 | 33 (33) |
  | obs_K12_m24 (R139) | 272 | 324 | 24 | 1 | 25 | 0 | 25 (25) |
  | fx K = 4, m = 8 / 16 / 32 (R137) | 98 / 130 / 194 | 44 / 76 / 140 | 8 | 1 | 9 | 0 | 9 (9) |
  | fx K = 2 / 8, m = 8 | 70 / 154 | 22 / 88 | 4 / 16 | 1 | 5 / 17 | 0 | 5 / 17 |
  | gate_K16_n197 | 197 | 23 | 16 | 16 | 18 | 3 | 15 (15) |
  | corpus (1132 runs, release_*.txt) | ≤ 581 | ≤ 159 | ≤ 64 | ≤ 64 | 2,607 | 1,704 | 903 (951 kept in all) |

- Mechanism (O), "σ̄ moves" (latew). σ̄ changes at 513 of 560 transitions, and 94% of releases are Odd re-routings. This is a genuinely
  two-player clock inside a W-run: τ is fixed, and Odd's optimal reply to the moving σ walks.
- Mechanism (B), "σ̄ frozen" (obs, fx). σ̄ changes ONCE in the whole W-run (SB_F = 1, the deviation set changes once). All releases are
  Even-side with the poison kept. Yet obs_K12_m24 has |F| = 324 > n − 1 = 271. So the excess over the one-player bound arises with Odd's
  reply FIXED at some ρ ≠ τ. The run is then the process below.
- Definition BIP(ρ, τ) ("bi-one-player"): Even strategies σ_t; offers Iρ_t := {(y, z) : val(σ_t, ρ)(z) ▷ val(σ_t, ρ)(σ_t y)}; step σ_(t+1) :=
  the val(·, τ)-optimum of σ_t ∪ Iρ_t (S4a's rule). On any stretch of a W-run where σ̄_t ≡ ρ, N5 IS BIP(ρ, τ) (immediate from S2, S4a). Both
  valuations are one-player: Even against a fixed Odd strategy.
- Lemma BIP-MON (PROVED, lane). In BIP(ρ, τ), val(σ_t, ρ) and val(σ_t, τ) are both non-decreasing in t.
  Proof: σ_(t+1) applies a subset of ρ-improving switches, and the improvement lemma holds for a fixed Odd strategy (one-player arena G_ρ).
  σ_(t+1) is the τ-optimum of an arena containing σ_t. □
- So the exact break, as asked:
  - (a) σ̄ ≠ τ creates poison (GAP-DEV), and the poison filters S4a's arena. That alone, with σ̄ never moving, already gives |F| > n − 1
    (mechanism B, obs_K12_m24).
  - (b) σ̄ moving with σ adds Odd-side releases (mechanism O, latew).
  - Neither (i) τ fixed, (ii) the arena optimum, nor (iii) GP* stops (a). GP* bounds each release-to-release epoch by n − 1, and BIP-MON
    makes both potentials monotone, but nothing bounds the number of Even-side releases.

## 3. CONJECTURE BIP-POLY and what it would give
- CONJECTURE BIP-POLY: every BIP(ρ, τ) run (any game, any two Odd strategies, any start) has at most p(n) steps.
- Status: OPEN. Data: obs_K12_m24's frozen-σ̄ W-run, 324 steps at n 272 (1.19n). The fx family's frozen-σ̄ runs have |F| < n. No
  super-linear BIP run is known to me. (R139's ΞCH = Km + K + 1 ≤ |F| on the obs family says |F| grows at least like K·m there; I did not
  check SB on its larger pins.)
- READING (D18, shortest paths × SI). BIP is a label-correcting process in G_ρ whose relaxation order is chosen by an optimiser in a
  second arena G_τ. Label-correcting methods with an arbitrary node-selection order are reported to be exponential in the worst case
  (Johnson, JACM 20(3):385-388, 1973; Kershenbaum; Shier-Witzgall: NOT OPENED, bibliographic records only; the Bertsekas SLF PDF I fetched
  was a scanned image with no extractable text). If such a lower bound transfers, BIP-POLY must use S4a's optimum (ii), not only
  monotonicity. That is the lemma candidate the Lead names. L-LIT request: open Johnson 1973 or a textbook statement.
- What BIP-POLY would cover: mechanism (B) completely. With it, the W-run residual would be the Odd-side releases of mechanism (O), i.e.
  σ̄'s motion while τ is fixed (count SB_F, 513 on latew).

## DONE / FINDINGS / NEEDS
- DONE: experiments/new/box88/release.py, run.sh, release_*.txt (corpus); check.sh "box 88"; this note.
- FINDINGS:
  1. PROVED (lane) Lemma NO-DEV: Ξ = W along a W-run ⇒ R*_F = FL_F = 0 and |F| ≤ n − 1 (the one-player picture holds exactly there).
  2. DATA: two mechanisms. (O) latew_K16_m32: σ̄ changes at 513/560 transitions, and 480/513 releases are Odd re-routings. (B) obs_K12_m24:
     σ̄ changes once, all 25 releases are Even-side with the poison kept, |F| = 324 > n − 1. Corpus: 1,704 ODD / 903 EVEN releases.
  3. PROVED (lane) BIP-MON; the definition of BIP(ρ, τ) (N5 on frozen-σ̄ stretches). CONJECTURE BIP-POLY OPEN. Exact break: the poison
     (σ̄ ≠ τ) filters S4a's arena even with σ̄ frozen. (i)-(iii) bound each epoch by n − 1 but not the number of Even-side releases.
  4. (ii) vs Friedmann: not checked (R140 not pushed yet).
- NEEDS: none from the owner. Lead: BIP(ρ, τ) is a self-contained two-fixed-strategy process that L-RED can attack in isolation (no σ̄
  dynamics). L-LIT: open a label-correcting worst-case source (Johnson 1973 or similar).
