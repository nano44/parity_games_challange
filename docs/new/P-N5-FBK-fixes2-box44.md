# P-N5-FBK fixes, second file (box 44 packet): the referees' gap and notes, written out
L-NEW successor 24 (Opus 5.5, D14/D18, L40). Written 2026-10-26 06:02Z by date -u, on the Lead's WORD of 05:56Z (Lead's stamp): "write
docs/new/P-N5-FBK-fixes2-box44.md now, repairs only, and freeze it." FROZEN at push; its sha1 is reported to the Lead.
- Object: packet docs/new/P-N5-FBK-box44.md, sha1 afd7c65a265053531171b66294811bbd9a801dd2 (l-new 9dd499d3), read with its first fixes file
  docs/new/P-N5-FBK-fixes-box44.md, sha1 79ad8597b2eb54f56b65718baa89d69b90543a68 (l-new 399e8ec6: verbatim quotes of P-N5-2T PFZ-q, DIR;
  checked verbatim by both referees). Neither file is edited; this file is the correction layer for the review, a record of the reports,
  not refereed text.
- Sources (by branch SHA):
  - REFEREE: docs/referee/R-N5-FBK.md (referee c7fa8d5e, successor 12): ROUTE-k, SAT-k, FB-kT, FB-kO per phase, ALT and the N_ep corollary
    SIGNED; FB-kO's whole-run sentence SIGNED WITH GAP FBK-1; notes FBK-N1..N3. §C (referee 0e4ba6ee): no disagreement; one joint gap
    FBK-1 = G-FBK-1; N-FBK-1, N-FBK-2 ACCEPTED (missed by REFEREE).
  - REFEREE-2: docs/referee-2/R2-N5-FBK.md (referee-2 d4cc40d9, successor 14): all SIGN, the whole-run sentence for k ≥ 2 only, gap
    G-FBK-1 (minor); notes N-FBK-1..4. Addendum A (referee-2 5ad79417): the first fixes file's quotes are verbatim. §C (referee-2 9a482c93):
    verdicts identical; one joint gap; FBK-N2's second half ACCEPTED (missed by REFEREE-2).
- Signed scope (both, CONDITIONAL on RESULTS R56 and P-N5-2T's PFZ-q, DIR): Lemma ROUTE-k, Lemma SAT-k, Theorem FB-kT, Corollary FB-kO per
  phase, Lemma ALT and its N_ep corollary, every game. The whole-run sentence of FB-kO is repaired below (§1). Not a running-time bound;
  not a TARGET.md claim; G-N5-TIME stays open.

## 1. The joint gap and its repair
| gap | where in the packet | repaired text |
| --- | --- | --- |
| FBK-1 (REFEREE) = G-FBK-1 (REFEREE-2); the same gap, found independently by both | §3, Corollary FB-kO, last sentence: "With R54 (e) (phases ≤ n(n − 1) + ∏_q deg(q) ≤ n(n − 1) + n^k), the in-phase fallbacks of a whole run are O(n^{2k+1}) for fixed k." | Read: "With R54 (e) (phases ≤ n(n − 1) + ∏_q deg(q) ≤ n(n − 1) + n^k), the in-phase fallbacks of a whole run are O(n^{k+1}(n² + n^k)): O(n^{2k+1}) for fixed k ≥ 2, O(n⁴) for k = 1." Reason: the product (n(n − 1) + n^k)·O(n^{k+1}) is O(n^{k+3} + n^{2k+1}), which is O(n^{2k+1}) only for k ≥ 2 (REFEREE-2's wording O(n^{max(k+3, 2k+1)}) is the same bound). The per-phase bounds (N_late, f = O(n^{k+1}) for fixed k) are unaffected, and no other statement uses the sentence. On 𝒞^1O the landed RESULTS R47 / R48 give the same order. |

## 2. Notes (no gap)
| note(s) | where in the packet | line to read with the packet |
| --- | --- | --- |
| N-FBK-1 (REFEREE-2; ACCEPTED by REFEREE §C) | §0 Premises, LANDED, R56 (a): "facts (Aκ), (M2κ), (SP′), (YB as used there), κ-FB-ROUND_D" | R56 (a) has no (YB). The (YB) meant is (YB_q), P-N5-2T's own lemma (P-N5-2T §2; REFEREE-2 N-2T-2), used by FBK only through P-N5-2T's DIR; cite it there, not under R56. Harmless: FBK is conditional on DIR. |
| N-FBK-2 (REFEREE-2; ACCEPTED by REFEREE §C) | §0 Premises; §3 Theorem FB-kT, proof step 1 ("Two late fallbacks lie in one Q-run iff their tuples … are equal") | Step 1 uses (INJ) (inside a class, κ constant ⟺ Ξ constant), which is in R56 (a) but not in FBK §0's list. Add (INJ) to the R56 (a) facts listed in §0. |
| FBK-N1 (REFEREE) = N-FBK-4 (REFEREE-2) | §2 Lemma SAT-k, hypothesis "Let t > g_{w_c} be a state of the phase" | The hypothesis t > g_{w_c} is not used by the proof (PFZ-q needs only the p-run index t > f^{Θ_p}_{w_c}). Harmless; FB-kT supplies it anyway. Optional. |
| FBK-N2 (REFEREE) ⊇ N-FBK-3 (REFEREE-2); the second half ACCEPTED by REFEREE-2 §C | §4 Lemma ALT: the conclusion κ_{t+1}(q) ≥ κ_t(q), and the CLEAN clause "q lies on no honest cycle at t and at t + 1" | (a) The inequality κ_{t+1}(q) ≥ κ_t(q) is already (M2κ) at every in-phase transition; ALT's content is that a clean change of σ̄(q) is STRICT unless it is a tie. (b) ALT's step at t + 1, κ_{t+1}(q) = κwt_c(q) + κ_{t+1}(y2), is (Aκ) at t + 1 (the proof cites κ-Y-FORM_D, which also gives it), and (Aκ) needs only q ≠ c; so "q on no honest cycle at t + 1" is unused. Both optional. The N_ep corollary is unchanged. |

## 3. DATA accepted from the reports (not proof)
- FBK-N3 (REFEREE; REFEREE-2 §5 the same and further): SAT-k's saturation hypothesis is met only on CONSTRUCTED unions, at routing depth 1 and
  2, on both engines: REFEREE-2's fb17_k3_P66.pg (sha1 712645de…, n 42) gives 26 SAT-k checks (13 at depth 1, 13 at depth 2) on both
  engines; REFEREE 37 + 26 checks, REFEREE-2 76 + 58 + 26; controls bite (REFEREE mutation 37 / 37; REFEREE-2 satk0 4, shift 76 / 76). Never on
  natural instances (best −1 random, −2 lib41).
- ALT counts from the S3 start on lib41: 1,910 clean strict / 75 clean ties / 65 non-clean / 1 at a cycle node, the same on both referees'
  engines and the lane's (altcheck.py); every clean equality is a tie (0 ALT violations).
- ROUTE-k: no routing cycle; routing depth up to 118 (tcL_N12, a class with 233 terminals), on both engines.
- FB-kT's late regime (late index ≥ n) is never reached in any sample: FB-kT and FB-kO rest on their proofs.

## 4. Status lines
- Both referees: one joint gap (FBK-1 = G-FBK-1), repaired in §1; no NOT SIGNED item. Nothing else in this file changes a signed statement.
