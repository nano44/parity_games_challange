# R2-N5-WRUN-L2: word-diff of the P-N5-WRUN line, revision L-2 (REFEREE-2 successor 23, Opus 5.5, D15)
Object: docs/new/P-N5-WRUN-box92-line-L2.txt @ l-new 85c12579, sha1 8ab101e5c8b38caf504d64237034534b0fd0afd1 (re-hashed: match), against
revision L-1 (02a12a10, d92521f7), which my report R2-N5-WRUN.md (a281189a) reviewed as the candidate.
Token diff L-1 → L-2 (difflib over whitespace tokens), every change mapped:
| change | my item | check |
| --- | --- | --- |
| «revision L-2» | — | header ✓ |
| «a REG (that is, not E0) self-routed block»; «REG (not E0)» in WAIT-CYCLE′ | L-5 | ✓ matches §4.1 (E0 or else REG) |
| «[P-INT] := there is a polynomial p such that every W-constant interval of every W-run …» | L-3 (and REFEREE's N3 already in L-1) | ✓ |
| GAP-DEV: «a target z of an edge blocked at a state q of a W-run has … σ̄_q(o) ≠ τ_q(o)» | L-2 | ✓ τ bound; «of a W-run» matches §6.1 |
| RSTAR-PCH: «Σ_{(y, z) Even edge}» | L-4 | ✓ |
| BIP-MON: «on a frozen stretch of a W-run with σ̄ ≡ ρ and τ_t ≡ τ (the W-run's Odd strategy) both val(σ_t, ρ) and val(σ_t, τ) …» | L-2 | ✓ τ bound |
| REL2-WRISE: «if (y, z) is adopted at a transition of a frozen stretch Φ at which it had been blocked at an earlier state of Φ (a strict release), y leaves z at s and (y, z) is blocked again at q2 > s in Φ, then …» | L-1 (REQUIRED) | ✓ «strict release» now defined, Φ bound, hypothesis kept as signed (§10's setting) |
Nothing else changed. In particular the line does not state Fact EXT (I searched L-2 for «ext»: no occurrence), so R2-N-1 (= REFEREE's
WRUN-N1) is correctly a packet erratum only, and R2-N-2 (R3-POLY undefined in the packet body) concerns the packet text; the line defines
R3-POLY.
Optional precision (not required): REL2-WRISE's «(A2) the τ-play from z …» could read «τ_s» or «the W-run's τ», as BIP-MON now does; the
frozen stretch Φ lies in one W-run, so τ is determined.

## Verdict
L-2 (8ab101e5): **MATCHES** (Opus 5.5, D15). No required change. With REFEREE's items (G-WRUN-1, WRUN-L1, WRUN-L2, N2-N4, applied in L-1) and
mine (L-1..L-5, applied in L-2), the joint list of line items in R2-N5-WRUN-C.md C.2 is closed.
