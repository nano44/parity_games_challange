# P-N5-XEP fixes (box 44 packet): the referees' notes, written out
L-NEW successor 24 (Opus 5.5, D14/D18, L40). Written 2026-10-26 06:21Z by date -u, on the Lead's WORD of 06:17Z (Lead's stamp): "write
docs/new/P-N5-XEP-fixes-box44.md, repairs only, and freeze it." FROZEN at push; its sha1 is reported to the Lead.
- Object: packet docs/new/P-N5-XEP-box44.md, sha1 237dd5eb31f60f19ef70099dc9351532e88b56f8 (l-new a4fa94b0; pinned trunk 8460897d). The
  packet is NOT edited; this file is its correction layer, a record of the reports, not refereed text. No signed statement changes.
- Sources (by branch SHA):
  - REFEREE: docs/referee/R-N5-XEP.md (referee 62f4bd2c, successor 12): R-STICK_D, SN-PREFIX_D (a)-(c), D-EPOCH, X-EP and its ALT form SIGNED,
    no gap; notes XEP-N1..N3. §C (referee ead5fdb3): no disagreement; N-XEP-2 ACCEPTED.
  - REFEREE-2: docs/referee-2/R2-N5-XEP.md (referee-2 fd43a69f, successor 14): all SIGN, no gap; the "With ALT" line signed as an inequality,
    its last clause a READING; notes N-XEP-1, N-XEP-2. §C (referee-2 b7b04fad): identical verdicts; REFEREE's extension of XEP-N1 to X-EP's n²
    term ACCEPTED; nothing open.
- Signed scope: R-STICK_D, SN-PREFIX_D (a)-(c), D-EPOCH (every game); X-EP (every game, CONDITIONAL on P-N5-ACCEL EPOCH (b)), a REDUCTION with
  the residual X_SN^pre OPEN; the "With ALT" line as an inequality, CONDITIONAL on P-N5-FBK ALT (both now signed by both referees). Not a
  running-time bound; not a TARGET.md claim; G-N5-TIME stays open.

## 1. Lines (no gap; notes only)
| note(s) | where in the packet | line to read with the packet |
| --- | --- | --- |
| XEP-N1 (REFEREE) = N-XEP-1 (REFEREE-2), found independently; REFEREE-2 §C accepts REFEREE's extension to X-EP | §1 R-STICK_D ("every split v ∈ R_D(s)"); §2 SN-PREFIX_D (b), (c); §4 X-EP | Optional sharpening; the packet's weaker statements are true as written. By R55 G_D (a) (Ξ_s = W_s on F_D(s), no hypothesis), every split vertex lies in R_D(s), so R-STICK_D's hypothesis "v ∈ R_D(s)" is automatic. Hence at an S4a transition no split vertex changes R_D-membership at all (it is already in, and does not leave); SN-PREFIX_D (b) holds with "at most once" replaced by "never"; every crossing at an S4a transition has a membership-changing vertex unsplit at its source. So §2 (c) sharpens to X_D ≤ f + X_SN^D, and in X-EP the n·n term per epoch (≤ n crossings with only split changers in each of ≤ n S4a runs) is 0: X_D ≤ (N_ep − 1) + N_ep·(n + 4n(n − 1)) + Σ_E X_SN^pre(E). |
| N-XEP-2 (REFEREE-2; ACCEPTED by REFEREE §C) | §4, the "With ALT" line, last clause: "every crossing outside the residual is charged to the quantity that also bounds fallbacks (R56 (f) Theorem FB-RED)" | The inequality X_D = O(n²)·(1 + ρ + ties + non-clean + cycle-node changes) + Σ_E X_SN^pre(E) is signed, conditional on P-N5-FBK's ALT (and P-N5-ACCEL's EPOCH (b), through X-EP). The clause is a READING: R56 (f) bounds f by ρ alone, while ties, non-clean changes and cycle-node changes are extra quantities. |
| XEP-N2 (REFEREE; REFEREE-2 §1 the same by a second route) | §0 Premises, "R23 (g) Lemma WM … game-general" | Both referees agree that WM's proof is game-general: REFEREE via docs/si/P-N5-Z-box5.md §8 (S4a's σ_{k+1} maximises V_{·,τ_k} over the arena by R18 (d) Lemma S (c), and σ_k lies in the arena); REFEREE-2 via the WM proof "transferred to every game by (F1) in G_τ", with XW = (VJ) at τ′ := τ_k (signed on every game in P-N5-1E, RESULTS R57). A landing note may record it. |

## 2. DATA accepted from the reports (not proof)
- XEP-N3 (REFEREE; REFEREE-2 §5 the same): EPOCH (b)'s term is VACUOUS in data: no epoch reaches n − 1 fallbacks ("after freeze" = 0 in every
  sample; REFEREE-2's best −1).
- lib41 from the S3 start: 3,222 crossings = 1,269 at epoch boundaries + 1,833 X_SN^pre + 120 with only split changers, reproduced exactly on
  both referees' engines (and equal to the packet's §5 figures). All 120 split-only crossings are fallback transitions (REFEREE, lib41 S3);
  REFEREE-2: 178 split-only crossings on lib41 × 3, all at fallbacks; 0 changes after the unsplit prefix in every sample; X_D ≤ f + X_SN^D
  everywhere.
- Controls (REFEREE-2, lib41 × 3): rstick_all (R-STICK asked of unsplit vertices too) fails 6,444 times; xsn0 (X_D ≤ f without X_SN^D) fails
  607 times. qc_toggle.pg (sha1 27850ecc…) re-run on REFEREE's engine exactly as the packet states.

## 3. Status lines
- Both referees: no NOT SIGNED item, no gap. Nothing in this file changes a signed statement; XEP-N1 adds a sharper consequence, proved above
  from the landed R55 (a).
