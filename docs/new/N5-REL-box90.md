# N5-REL (box 90): BIP-REL-1 not proved. Lemma REL2-WRISE (lane): a second strict release of (y, z) in a frozen stretch forces a strict W(z)-rise after y leaves z, with Ξ(z) kept below. One-line obstruction below. No instance (random search). Then SB-POLY: SB_F ≤ n is DEAD (pftheta34_n32: 34 > 32; latew_K16_m32: 513 > 482); per-Odd-vertex σ̄ flips reach 62 in one W-run, almost all returns
L-NEW successor 38 (Opus 5.5), D14 / D18, Lead reading L40. Lead 2026-10-30 15:10Z: «BOX 90 = prove BIP-REL-1 (strict) … If no proof
closes, give the obstruction in one line and switch to SB-POLY for mechanism O … Is SB_F ≤ n per W-run in all data?» Written 2026-10-30
15:11Z-15:45Z (date -u). Working note, unrefereed. Labels: PROVED (lane) / CONJECTURE / DEAD / DATA. Not a TARGET.md claim. G-N5-TIME OPEN.

## 0. Setting and sources
- docs/new/N5-BIP-box89.md (frozen stretch, strict release, BIP-REL-1, BIP-RED); N5-ONEP-box88.md (BIP(ρ, τ), BIP-MON); R140 Lemma
  ARENA-MAX (l-red 47000632, relayed); RESULTS R88 / R89. Frozen stretch Φ: σ̄_t = ρ for all t ∈ Φ, τ fixed. Ξ = val(·, ρ), W = val(·, τ).
- Fact EXT (elementary, from [S1-val] / [S1-ord]). ext(y, x) := (λ(x), P(x) ∪ {y if y is above λ(x)}, ℓ(x) + 1) is strictly
  order-preserving: both sides gain y or neither does, so the symmetric difference of the path sets and the length difference are
  unchanged, and the cycle nodes are untouched.

## 1. Lemma REL2-WRISE (PROVED, lane)
- Setting. In a frozen stretch Φ, (y, z) has a strict release at t1 (y switches to z). y leaves z at s > t1 for h. (y, z) is BLOCKED again at
  q2 > s, with h2 := σ_q2(y). Assume:
  - (A1) y is not its own W-cycle node at the states of [s + 1, q2];
  - (A2) under the arena strategy π := σ_(s+1) with y → z, the τ-play from z does not pass y.
- Claim. W_q2(z) ▷ W_(s+1)(z): W(z) rises strictly after y leaves z, while at q2 Ξ_q2(z) ⊴ Ξ_q2(h2).
- Proof.
  - (i) π belongs to S4a's arena H_s, because z = σ_s(y) ∈ A_s(y). ARENA-MAX gives W_(s+1)(y) ⊵ val(π, τ)(y). By (A2),
    val(π, τ)(y) = ext(y, W_(s+1)(z)). By (A1), W_(s+1)(y) = ext(y, W_(s+1)(h)). Fact EXT then gives W_(s+1)(h) ⊵ W_(s+1)(z).
  - (ii) W is non-decreasing in a τ-stretch without S4c. By (A1), W_t(y) = ext(y, W_t(σ_t y)) on [s + 1, q2], so W_t(σ_t y) is
    non-decreasing there (Fact EXT): W_q2(h2) ⊵ W_(s+1)(h).
  - (iii) BLOCKED at q2 means W_q2(z) ▷ W_q2(h2). Chaining: W_q2(z) ▷ W_q2(h2) ⊵ W_(s+1)(h) ⊵ W_(s+1)(z). □
- So a second strict release needs, inside one frozen stretch: a W(z)-rise after s that leaves Ξ(z) ⊴ Ξ(σ y) (a fresh gap, by GAP-DEV
  carried by a deviation o on z's ρ-play), followed by a Ξ(z)-rise past Ξ(σ y).
- OBSTRUCTION (one line). With ρ frozen, the τ-branch and the ρ-branch of a deviation o climb independently: a climb below τ(o) raises
  W(z) and not Ξ(z), a later climb below ρ(o) raises Ξ(z), and ρ stays Odd's optimum as long as Ξ(ρ(o)) ⊴ Ξ(τ(o)). Neither ARENA-MAX nor
  BIP-MON orders these two climbs, so nothing forbids "W-climb under τ(o), then Ξ-climb under ρ(o)" twice.
- DATA. box90/relrand.py, random games with random start pairs: n 8, 10, 12, 4000 games each, at most 1 strict release per edge. Random
  W-runs are short, though: max SB_F = 2. With the corpus (box 89, 0 violations), no instance exists in data. This is the R142 aim for L-RED.

## 2. SB-POLY (mechanism O): is SB_F ≤ n? No
- DEAD: CONJECTURE SB-LIN (SB_F ≤ n per W-run).
  - red/so/instances/pftheta34_n32.pg (S3 start): SB_F = 34 > n = 32 in one W-run (also pftheta_cex_n32: 33).
  - L-RED latew_K16_m32 (sha1 6d34c161…): SB_F = 513 > n = 482.
  - Corpus (box 88 release_*.txt): SB_F > n in 4 runs, all pftheta-type. latew's family has R*_F = K·m and SB_F ≈ K·m + 1, so SB_F is
    quadratic there.
- DATA, per Odd vertex (box90/sbv.py): SBV_F(o) := σ̄(o)-changes in a W-run.
  - gate_K64_n581: max SBV 62 at one vertex of out-degree 2, of which 61 are returns (flip-flop).
  - latew_K16_m32: max SBV 32 (31 returns), total SB 513.
  - pftheta34_n32: SBV 34 at a vertex of out-degree 19 (18 returns).
- READING. For an Odd o, a σ̄(o) flip between successors a, b whose Ξ-values are not tied needs a change of the order of Ξ(a), Ξ(b), hence a
  change of Ξ(a) or Ξ(b). So the non-tie flips of o are at most Σ_(c ∈ succ(o)) ΞCH_F(c). This is circular with XI-CH-POLY (box 87):
  SB-POLY is the Odd-side face of the same per-vertex Ξ-change count, and ties (VJ tie-breaks) add flips that are not counted. Not proved
  beyond this remark.

## DONE / FINDINGS / NEEDS
- DONE: experiments/new/box90/relrand.py, sbv.py; check.sh "box 90"; this note.
- FINDINGS:
  1. PROVED (lane, under (A1), (A2)) Lemma REL2-WRISE: a second strict release forces a strict W(z)-rise after y leaves z, with Ξ(z) kept
     below Ξ(σ y).
  2. BIP-REL-1 NOT proved. Obstruction: the τ-branch and ρ-branch of a deviation climb independently under a frozen ρ. No instance (random
     n ≤ 12; corpus 0).
  3. DEAD: SB-LIN (SB_F ≤ n). pftheta34_n32 (34 > 32) and latew_K16_m32 (513 > 482); latew's family is quadratic.
  4. DATA: per-vertex σ̄ flips ≤ 62 per W-run (gate_K64), mostly flip-flop returns at out-degree-2 Odd vertices.
  5. READING: non-tie σ̄ flips are bounded by the successors' Ξ-changes. SB-POLY is the Odd-side face of XI-CH-POLY (box 87), so it is not a
     smaller target.
- NEEDS: none from the owner. My context is past 60%; I can do one more short box or park.
