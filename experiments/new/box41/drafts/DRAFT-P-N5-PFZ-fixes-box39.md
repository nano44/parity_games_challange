# Fixes to packets P-N5-PFZ (docs/new/P-N5-PFZ-box39.md, sha1 3c617e06…, pinned trunk 283bcb67) and P-N5-PFZ-ext (docs/new/P-N5-PFZ-ext-box39.md, sha1 b3702b1b…, pinned trunk c61ecc4e): repairs only
L-NEW successor 20 (Opus 5.5, D15/D18), session_018pjn8Y8JRES3YuFDUCAJgM. Written <DATE -u>, after the Lead's relay of all PFZ §Cs
(REFEREE main §C 4859e63, §C-ext ed8bc207; REFEREE-2 §C <SHA>). A record of the referees' items and the lane's repairs; not itself
refereed text. Both packets are frozen and unchanged.
- Reports: REFEREE docs/referee/R-N5-PFZ.md (8595343; main §C 4859e63; §C-ext ed8bc207): P-N5-PFZ all SIGNED; ext: P-FREEZE′, θ-LEN SIGNED,
  BRK-POLY′ (i) SIGNED WITH GAP PFZ-1 + repair, (ii), (iii) SIGNED GIVEN (i). REFEREE-2 docs/referee-2/R2-N5-PFZ.md (37e55fd main; §X
  78896bfc ext; §C <SHA>): main all SIGN (N-PFZ-1..3); ext P-FREEZE′, θ-LEN SIGN; BRK-POLY′ (i) NOT SIGNED as stated (G-PFX-1), (i′) SIGN.

## 1. PFZ-1 = G-PFX-1 (gap in BRK-POLY′ (i)'s proof; repair in full)
- The gap (both referees, independently): the proof bounds θ-changes inside each P-epoch (θ-LEN: ≤ |U| − 2 per epoch) and misses the
  ρ_S transitions that join epochs. As written, the proof gives only (i′) θ_S ≤ ρ_S + (ρ_S + 1)·max(|U| − 2, 0).
- Repair (REFEREE's, re-derived in R-N5-PFZ §C-ext ed8bc207; restated here with the lane's check). Let S be an HN stretch, o ≠ c_θ.
  - Refined θ-LEN. Inside a P-epoch Π (P(θ) constant), c_θ and P(θ) are fixed. Let Q be o's honest path to c_θ, c_θ excluded; it is simple
    in U ((SP)), contains o, and ℓ(θ) = |Q| = |P(θ)| + |Q ∩ A_low|, where A_low := (U ∖ {c_θ}) ∩ {v : rank(v) < rank(c_θ)} and A_high :=
    (U ∖ {c_θ}) ∖ A_low (P(θ) = Q ∩ A_high: the vertices of Q above c_θ). So |Q ∩ A_low| takes at most |A_low| + 1 − [o ∈ A_low] values on Π.
    On Π, θ changes only in ℓ, and ℓ moves monotonically (R15 (a) with c and P fixed: (M1′)'s last component). So Π has at most
    |A_low| − [o ∈ A_low] θ-changes.
  - If ρ_S ≥ 1: P(θ) changes in S. o's membership in P(θ) is fixed (rank(o) vs rank(c_θ) is fixed), so P(θ) ∖ {o} ⊆ A_high ∖ {o} changes,
    hence A_high ∖ {o} ≠ ∅: some u ∈ U ∖ {o, c_θ} lies above c_θ. o is in exactly one of A_low, A_high, and |A_low| + |A_high| = |U| − 1,
    so |A_low| − [o ∈ A_low] ≤ (|U| − 1) − 1 − 1 = |U| − 3.
  - Equivalently (REFEREE-2 11, verdict relayed by the Lead 19:13Z): the per-epoch bound is exactly |A_low| − [o ∈ A_low] =
    |U| − 2 − |A_high ∖ {o}| (as |A_low| + |A_high| = |U| − 1 and o lies in exactly one of them).
  - So θ_S ≤ ρ_S + (ρ_S + 1)(|U| − 3) = (ρ_S + 1)(|U| − 2) − 1 when ρ_S ≥ 1; when ρ_S = 0, θ_S ≤ |U| − 2 by θ-LEN. Both are within
    (i) as stated: θ_S ≤ (ρ_S + 1)·max(|U| − 2, 0). □ (Checked by the lane line by line, <DATE>.)
  - With the repair, (ii)'s middle bound and (iii)'s end constant (ρ_S + 1)(2n − 3) stand as written. Without it (jointly signed today),
    the forms are (i′) and (iii)'s end bound (ρ_S + 1)(2n − 2) (REFEREE-2 §X; REFEREE §C-ext). Landing (i) as stated needs REFEREE-2's
    signature on this repair (REFEREE §C-ext).
- Precision (Lead 18:15Z, REFEREE-2 10's flag): P-N5-RHO quotes PFZ-1's repaired bound as θ_S ≤ (ρ_S + 1)(|U| − 2); the repair gives the
  sharper (ρ_S + 1)(|U| − 2) − 1 for ρ_S ≥ 1. No statement changes: RHO's HN-POLY uses only (i′) (R-N5-RHO).

## 2. Notes (no gap)
| item | where | kind | repair |
| --- | --- | --- | --- |
| PFZ-N1 (REFEREE) | P-N5-PFZ §6 | citation | "SPLIT" for "the eviction is a fallback" means SPLIT (a) (RESULTS R39 (a)). |
| PFZ-N2 (REFEREE) | §5 RISE′ | precision | The hypothesis "no transition of [a, k) is an entry" is stronger than needed; Step 2 derives what is used. |
| PFZ-N3 (REFEREE) | dependency table | status | P-N5-NEB is signed by both referees and LANDED as RESULTS R42 (17:41Z); not a premise. |
| N-PFZ-1 (REFEREE-2) | §1 (A) | wording | The filled-in "no double count" case cannot occur; keep the conclusion, drop the case. (The same sentence in P-N5-RHO §0 (A) and P-N5-FBPOLY §0.3 (Aκ): same note.) |
| N-PFZ-2 (REFEREE-2) | §6 window | convention | §6 uses the LAST eviction before an entry; P-N5-NEB the first eviction after the previous entry. Both are correct for their proofs; say so if the RESULTS entries are merged. |
| N-PFZ-3 (REFEREE-2) | §8 | data | t > f_{|U|−1} at |U| ≥ 3 is never reached (library, climbs): P-FREEZE's freeze point is an upper bound data never approaches. (Consistent with L-RED R71 and P-N5-FBPOLY §8.) |
- §C lines: REFEREE main §C 4859e63 and §C-ext ed8bc207: <summary>. REFEREE-2 §C <SHA>: <summary>.
