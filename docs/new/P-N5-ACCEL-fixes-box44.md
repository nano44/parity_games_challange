# P-N5-ACCEL fixes (box 44 packet): the referees' notes, written out
L-NEW successor 24 (Opus 5.5, D14/D18, L40). Written 2026-10-26 05:40Z by date -u, at the Lead's GO of 05:39Z (Lead's stamp), step 2 (a):
"repairs only, frozen". FROZEN at push; its sha1 is reported to the Lead.
- Object: packet docs/new/P-N5-ACCEL-box44.md, sha1 301f0be0fa2b2240bba59b347dfbee8426b8dba3 (l-new e9eaaaaf; re-measured on my tree).
  The packet is NOT edited; this file is its correction layer, a record of the reports, not refereed text. No signed statement changes.
- Sources (by branch SHA):
  - REFEREE: docs/referee/R-N5-ACCEL.md (referee a19cdff7, successor 12): §1, ACCEL (a)-(c), EPOCH (a)-(c) SIGNED, no gap; notes ACCEL-N1..N3.
    §C (referee 09b5dbf5; 906247c6 touches R-N5-2T only): no disagreement, no gap; N-ACC-2 ACCEPTED ("Not noted by us").
  - REFEREE-2: docs/referee-2/R2-N5-ACCEL.md (referee-2 f0e82d8a, successor 13): all SIGN, no gap; notes N-ACC-1..3.
    §C (referee-2 5ad79417, successor 14): identical verdicts; ACCEL-N1's in-phase (SG) proof checked and accepted; ACCEL-N2 accepted;
    nothing open.
- Signed scope: §1 (facts, κ-FB-ROUND, CN-ONLY_D), Lemma ACCEL (a)-(c), Lemma EPOCH (a)-(c), every game. §4 not signed. Neither lemma is a
  polynomial bound (|K_c(z)| and N_ep can be exponential). Not a TARGET.md claim; G-N5-TIME stays open.

## 1. Lines (no gap; notes only)
| note(s) | where in the packet | line to read with the packet |
| --- | --- | --- |
| N-ACC-2 (REFEREE-2; ACCEPTED by REFEREE §C C.2, which had missed it) | §3 Lemma EPOCH (a), after "Hence for t ∈ E with t > e_{n−1}: κ_t = opt_E on every class" | Add the per-class form: for every class c and t ∈ E with t > e_{\|U_c\|−1}: κ_t = opt_E on U_c (so Ξ is constant on U_c on that part of E). Proof: (a)'s lower bound at j = \|U_c\| − 1 covers every simple path of G_E[U_c] (≤ \|U_c\| − 1 edges), and (a)'s upper bound holds at every t ∈ E; the two meet on U_c ((INJ) and the fixed cycle node c turn κ into Ξ, as in (a)). Unlike the global freeze, this form IS reached in data (REFEREE-2: 18,251 checks outside the climbs, 38,213 in them; 56,464 in all; 0 violations). |
| ACCEL-N1 (REFEREE) = N-ACC-1 (REFEREE-2); identical on scope per both §Cs | §2 proof of (b), "((SG), R19 (d); S4a and S4c switch along gates)" | (SG) is landed "on all games, not only 𝒞^1O" in RESULTS R19 (d) (proof of Lemma RE), and its proof uses only R15 (a), the gate, (V1) and strict (V2): no one-Odd step. Optional self-contained in-phase proof (REFEREE §2, checked by REFEREE-2 §C): a switched Even y moves to a gate target z (S4a's arena A(y) = {σ(y)} ∪ {w : (y, w) ∈ Iσ}; S4c: the best gate target), so Ξ_L(z) ▷ Ξ_L(σ_L y); λ(y) = c ≠ y is constant on the phase, so (Aκ) at L and L + 1 puts σ_L(y), z in U_c and gives κ_{L+1}(y) = κwt_c(y) + κ_{L+1}(z) ≥ κwt_c(y) + κ_L(z) > κwt_c(y) + κ_L(σ_L y) = κ_L(y) ((M2κ), (M1κ)). |
| ACCEL-N2 (REFEREE; accepted by REFEREE-2 §C) | §3 proof of (b), "leaves Ξ = Ω_σ unchanged" | One clause: SPEC's Ξσ (the valuation against Odd's optimal counterstrategy) is VJ00's Ω_σ on every game, by (VJ) (VJ00 §4.3 and (11)), signed by both referees on P-N5-1E (docs/si/P-N5-1E-box16.md §2; REFEREE-2 R2-N5-1E §2, N-1E-1; REFEREE R-N5-1E §1, 1E-N2); RESULTS R57 when P-N5-1E lands (CHECKER C66). So R15 (d), stated for Ω_σ and Ω_τ, applies. |
| ACCEL-N3 (REFEREE) = N-ACC-3 (REFEREE-2) | §3 (a) freeze conclusion, (b); §4 data | DATA: the global frozen regime (an epoch with ≥ n − 1 in-phase fallbacks) is VACUOUS in all data. REFEREE: EPB hypothesis met 0 times (lib41 n ≤ 64, box-43/44 instances, 2,000 random). REFEREE-2: best epoch 1 short in the library (n 3), 2 short after four climbs aimed at it (47,996 runs). EPOCH (a)'s global freeze and (b) rest on their proofs; EPOCH (a)'s two inequalities, (c), ACCEL (a)-(c) and (SG) are exercised (0 violations); the per-class freeze (N-ACC-2) is exercised. |

## 2. DATA accepted from the reports (not proof)
- REFEREE CN_switch: 410 switches of Even cycle nodes, none raises κ ((A0κ)); so (SG)'s hypothesis λ(y) ≠ y cannot be dropped, and ACCEL (b)
  rightly does not count those transitions (accepted by REFEREE-2 §C).
- σ̄|Q repeats inside a phase (§4): REFEREE re-ran lap_n6_s1_110421 (σ̄(2) = 0, 4, 0); REFEREE-2 finds repeats in 203 lib41 phases (3 starts)
  and 187 phases of its 𝒞^1O files (the packet's 91 phases are S3 only). Max epochs in one phase: 50 (lev_l_x.pg), 53 (rise_thin51_n40).

## 3. Status lines
- Both referees: no NOT SIGNED item, no gap. Nothing in this file changes a signed statement; N-ACC-2 adds a consequence, proved above
  from the signed (a).
