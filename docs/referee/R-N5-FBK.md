# R-N5-FBK: REFEREE report on packet P-N5-FBK (L-NEW box 44: ROUTE-k, SAT-k, Theorem FB-kT, Corollary FB-kO; Lemma ALT and the N_ep reduction)
Referee: REFEREE (successor 12, session_01KNDBjZvPFLaNjEdCmEWBcN), Opus 5.5 (owner ruling D15).
- Routing: the Lead's messages of 04:55Z and 05:01Z (Lead's stamps).
- Object: docs/new/P-N5-FBK-box44.md at trunk 5d723af6, sha1 afd7c65a265053531171b66294811bbd9a801dd2 (checked with
  `git show 5d723af6:docs/new/P-N5-FBK-box44.md | sha1sum`; identical on my tree), 114 lines, frozen at l-new 9dd499d3. Read together
  with its fixes file docs/new/P-N5-FBK-fixes-box44.md, sha1 79ad8597b2eb54f56b65718baa89d69b90543a68 (l-new 399e8ec6; checked).
  Author: L-NEW successor 23.
- Written 2026-10-26T05:05Z-05:18Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ FBK file on my tree; none opened. No lane code run (experiments/new/box44/altcheck.py).
  REFEREE-2's published 2T witnesses (docs/referee-2/R2-N5-2T/instances/, read after my own 2T report and §C) are used as INPUT games
  only. D1.
- Conditional on: RESULTS R56 (landed) and P-N5-2T's PFZ-q and DIR (sha1 fcb91130; my R-N5-2T and §C: signed by both referees, conditional
  on R56; not yet landed when I wrote this).
- Tool: scratch/fbk_probe.py (own engine; any game). Logs scratch/fbk_logs/ (run_all.sh).

## Verdicts (CONDITIONAL on RESULTS R56 and P-N5-2T's PFZ-q, DIR)
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | Lemma ROUTE-k (par_t has no cycle; depth ≤ m_c − 1) | SIGNED |
| §2 | Lemma SAT-k (κ_t(q) ∈ S_{q,p} + κ_t(p), \|S_{q,p}\| ≤ d_q) | SIGNED (FBK-N1: its hypothesis t > g_{w_c} is not used) |
| §3 | Theorem FB-kT (N_late ≤ 1 + Σ_q (V_q − 1), V_q ≤ Σ_h D_c((m_c − 1)D_c)^h; f ≤ 1 + (n − 1)(1 + N_late)) | SIGNED |
| §3 | Corollary FB-kO, per phase: N_late ≤ 1 + k·2n·k·(2(k − 1)n)^{k−1}, f = O(k^{k+1}2^k n^{k+1}) | SIGNED |
| §3 | Corollary FB-kO, last sentence: "the in-phase fallbacks of a whole run are O(n^{2k+1}) for fixed k" | SIGNED WITH GAP FBK-1 (false as derived for k = 1; repair below) |
| §4 | Lemma ALT and its N_ep corollary | SIGNED (FBK-N2: the "≥" half is (M2κ); the content is the equality case) |
| §5 | obstruction, data, missing pieces | not signed (as briefed) |
| fixes | verbatim quotes of P-N5-2T PFZ-q (l.85-88), DIR (l.121), A_q (l.115), DIRECT (l.53-54) | CHECKED: verbatim (script, whitespace-normalised); no signed statement changes |
One gap, FBK-1, with a one-line repair; it touches only the whole-run clause. Notes FBK-N1, FBK-N2, FBK-N3 (DATA). Not a running-time bound
(crossings and transitions per phase given f stay OPEN on 𝒞^kO, §5.3). Not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. ROUTE-k
- par_t(q) is defined for q not direct: q is not on its own cycle, and its play (which reaches c) meets some vertex of Q_c ∖ {q} before c ✓.
- A cycle q = p_0 → p_1 → … → p_r = q: p_1 is on q's play; from p_1 on, q's play is p_1's play (positional), which meets p_2; and so on, so q's
  play meets q again, i.e. q lies on the cycle of its own play, so q is direct: contradiction ✓. Hence the relation is a forest on the
  non-direct terminals, every chain ends at a direct one, and a chain of distinct terminals has ≤ m_c − 1 steps ✓.
- VERDICT: SIGNED.

## 2. SAT-k
- y := σ̄_t(q) ∈ U_c ((Aκ)); y's play is q's play minus q and avoids q (q not on its cycle), so its first vertex of Q_c is p, before c ✓.
  y = p: direct ✓. Otherwise y ∉ T: y ≠ c (p precedes c), y ∉ Q_c (p is first), and T ∩ U_c = {c} ∪ Q_c ✓.
- "≤": the prefix of y's play to its first vertex of T ∩ U_c, which is p, is simple ((SP′)), avoids T ∖ {p}, has Even edges σ_t and forced
  Odd vertices: a path of G_c^p; (Aκ) along it ✓. "≥": PFZ-q (P-N5-2T §2, quoted verbatim in the fixes file) for the terminal p, z = y ∈
  U_c ∖ T, Θ = Θ_p, j = w_c: t ∈ Θ_p, t > f^{Θ_p}_{w_c}; simple paths of G_c^p have < |U_c| vertices, so ≤ w_c edges ✓. So κ_t(y) =
  κopt^p(y) + κ_t(p) and κ_t(q) ∈ S_{q,p} + κ_t(p) ✓. |S_{q,p}| ≤ d_q (one value per successor) ✓.
- FBK-N1: the hypothesis t > g_{w_c} is never used (PFZ-q needs only the p-run index). Harmless; FB-kT supplies it anyway.
- VERDICT: SIGNED.

## 3. Theorem FB-kT and Corollary FB-kO
- Step 1 (outer count) ✓: as P-N5-2T's FB-2T step 1 (my R-N5-2T §5): coordinates non-decreasing ((M2κ)), equal tuples ⇔ one Q-run, N_late =
  #distinct tuples; each change of tuple raises some coordinate to a new value, and coordinate q has V_q values, so ≤ V_q − 1 raises ✓.
  Cycle nodes in Q contribute 0 ✓.
- Step 2 (values by depth) ✓. Every k_i > g_{n−1} ≥ g_{w_c} ✓. h = 0: DIR (P-N5-2T §4, verbatim in the fixes file) at k_i ⇒ x_i(q) ∈ A_q,
  V_{q,0} ≤ d_q + w_c ≤ D_c ✓. h ≥ 1: p := par_{k_i}(q) has depth h − 1 (depth is 1 + the parent's) ✓. For a value α of x(p), the indices
  with x(p) = α are consecutive among the late indices and their sources lie in one p-run Θ ((M2κ)) ✓; after the first w_c of them, k_i >
  f^Θ_{w_c} (≥ w_c fallbacks of Θ with earlier sources) ✓, so SAT-k gives x_i(q) ∈ S_{q,p} + α. So per (p, α): ≤ w_c + d_q ≤ D_c distinct
  values of x(q) ✓; the α's are values of x(p) at indices where p has depth h − 1: ≤ V_{p,h−1} ✓. V_{q,h} ≤ Σ_{p ≠ q} D_c·V_{p,h−1} ✓
  (m_c − 1 terms), and by induction max_q V_{q,h} ≤ D_c((m_c − 1)D_c)^h ✓; h ≤ m_c − 1 (ROUTE-k) ✓.
- Step 3 ✓: V_q ≤ Σ_h V_{q,h} ≤ m_c·D_c·((m_c − 1)D_c)^{m_c − 1} (for m_c = 1, read 0^0 = 1: V_q ≤ D_c) ✓. D_c ≤ (n) + (n − 1) < 2n ✓.
- FB-kO per phase ✓: Σ_c m_c ≤ k, m_c ≤ k, and the per-terminal bound is increasing in m_c, so N_late ≤ 1 + k·k·2n·(2(k − 1)n)^{k−1} ✓;
  f ≤ 1 + (n − 1)(1 + N_late) (R56 (f)) = O(k²·2^k·(k − 1)^{k−1}·n^{k+1}) ⊆ O(k^{k+1}2^k n^{k+1}) ✓. k = 2 agrees with FB-2T's order ✓.
- FBK-1 (GAP; the corollary's last sentence). "With R54 (e) (phases ≤ n(n − 1) + ∏_q deg(q) ≤ n(n − 1) + n^k), the in-phase fallbacks of a
  whole run are O(n^{2k+1}) for fixed k." The derivation gives (n(n − 1) + n^k)·O(n^{k+1}) = O(n^{max(2,k)+k+1}). That is O(n^{2k+1}) for
  k ≥ 2, but O(n⁴), not O(n³), for k = 1 (the corollary is stated for every k; on 𝒞^1O, R47 / R48 give the same n² phases × n² fallbacks).
  Exact arithmetic of the stated bound: run-total / n^{2k+1} = 19.9, 200, 2,000 at n = 10, 100, 1,000 for k = 1, and ≈ 32 (k = 2), ≈ 288
  (k = 3) at every n. Repair: "O(n^{k+1}·(n² + n^k)), i.e. O(n^{2k+1}) for fixed k ≥ 2 and O(n⁴) for k = 1". No other statement uses the
  sentence; the per-phase bounds are unaffected.
- Start-freeness ✓ (per phase; R56's statements per phase; ROUTE-k statewise; SAT-k / PFZ-q run-internal).
- VERDICT: FB-kT SIGNED; FB-kO SIGNED, its whole-run clause WITH GAP FBK-1.

## 4. Lemma ALT and the N_ep corollary
- κ_{t+1}(q) = κwt_c(q) + κ_{t+1}(y2) ((Aκ) at t + 1; the packet cites κ-Y-FORM_D, which also gives it) ✓; κ_{t+1}(y2) ≥ κ_t(y2) ((M2κ),
  y2 ∈ U_c) ✓; y2 ∈ Y^q_t (clean: y2's play at t avoids q; y2 ∈ succ(q) ∩ U_c), so κ-Y-FORM_D at t (q on no honest cycle at t) gives κ_t(y2) ≥
  min_{Y^q_t} κ_t = κ_t(y1) = κ_t(q) − κwt_c(q) ✓. Equality throughout ⇔ the tie ✓.
- FBK-N2: the inequality κ_{t+1}(q) ≥ κ_t(q) is already (M2κ); ALT's content is that equality forces a tie. The clean hypothesis "q on no
  honest cycle at t + 1" is not used. Both harmless.
- N_ep corollary ✓: an epoch ends only at a transition changing some σ̄(q), q ∈ Q; each such change is a cycle-node change (cyc_q), a
  non-clean change (nc_q), a clean change with Ξ(q) changing (≤ ρ_q, since ALT's equality case is the only way Ξ(q) stays), or a clean tie
  (tie_q) ✓. So N_ep ≤ 1 + Σ_q (ρ_q + tie_q + nc_q + cyc_q) ✓.
- VERDICT: ALT and the corollary SIGNED.

## 5. Fixes file
- Quotes checked by script against docs/si/P-N5-2T-box16.md (sha1 fcb91130): PFZ-q statement = l.85-88, DIR statement = l.121, A_q = l.115,
  DIRECT = l.53-54, all verbatim (whitespace-normalised) ✓. §3's "how FBK uses them" matches FBK §2 "≥" and §3 step 2 h = 0 ✓. No signed
  statement changes ✓.

## 6. Data (DATA, not proof; scratch/fbk_probe.py, own engine; logs scratch/fbk_logs/)
Checks: ROUTE (acyclic parent relation, depth ≤ m_c − 1, every state and class), SATK (every non-direct q with its parent's run saturated;
the packet's extra t > g_{w_c} NOT imposed, counted as SATK_g), ALT (every in-phase σ̄(q) change: clean ⇒ no drop, equality ⇒ tie), NEP
(N_ep corollary), FBKT (phases with a late fallback). Mutation FBK_MUT=1: S_{q,p} shifted.
| set | runs | phases | ROUTE (max depth) | SATK | ALT changes (clean strict / ties / non-clean) | max epochs | FBKT | failures |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41, n ≤ 64 (367 games), S3 + 6 random | 2,569 | 12,620 | 104,418 (15) | 0 | 7,061 (6,619 / 362 / 80) | 50 | 0 | 0 |
| lib2o.txt (lane list, input only; 43 𝒞^2O), PATHN 24, S3 + 6 random | 301 | 870 | 3,650 (1) | 0 | 146 (146 / 0 / 0) | 8 | 0 | 0 |
| 2,000 random 𝒞^3O, n 4-12, seed 62, S3 + 2 random | 6,000 | 15,360 | 36,757 (2) | 0 | 78 (56 / 9 / 13) | 3 | 0 | 0 |
| 2,000 random 𝒞^4O, n 5-12, seed 63, S3 + 2 random | 6,000 | 16,144 | 53,268 (3) | 0 | 69 (47 / 9 / 13) | 3 | 0 | 0 |
| REFEREE-2's 2T witnesses (4 constructed unions, n 35-39), PATHN 40, S3 | 4 | 20 | 450 (1) | 37 (all also with t > g_{w_c}) | 28 (28 / 0 / 0) | 8 | 0 | 0 |
| MUTATION (S_{q,p} shifted), same witnesses | 4 | 20 | — | 37 | — | — | — | 37 SATK failures (control bites) |
- FBK-N3 (DATA): ROUTE-k and ALT are exercised (depth up to 15 on lib41's many-terminal classes; 7,354 σ̄(q) changes on the natural sets). SAT-k's saturation
  hypothesis is met only on the constructed witnesses (37 checks, depth-1 chains q′ → q; the mutation fails all 37); FB-kT's late count
  is never reached (as the packet says, §5.2). FB-kT and FB-kO rest on their proofs.
- Reproduce (from docs/referee/scratch): `sh fbk_logs/run_all.sh`; `PATHN=40 python3 -I fbk_probe.py ../../../docs/referee-2/R2-N5-2T/instances/*.pg`
  (and with FBK_MUT=1).

## 7. Notes for the fixes file
- FBK-1 (gap, one line): Corollary FB-kO's whole-run clause: "O(n^{k+1}(n² + n^k)), i.e. O(n^{2k+1}) for fixed k ≥ 2, O(n⁴) for k = 1".
- FBK-N1: SAT-k's hypothesis t > g_{w_c} is unused (optional).
- FBK-N2: ALT's "≥" is (M2κ); the clean clause "no honest cycle at t + 1" is unused (optional).
- FBK-N3: DATA.

## §C. Comparison with REFEREE-2 (REFEREE successor 12; written 2026-10-26T05:25Z by date -u; (Opus 5.5, D15))
- Routing: the FBK report pattern (§C after both reports; the Lead's 05:05Z note that REFEREE-2's FBK report was pushed). Objects: this
  report (c7fa8d5e; §1-§7 above unchanged) and docs/referee-2/R2-N5-FBK.md with its Addendum A (referee-2 5ad79417 on origin/claude/referee-2,
  successor 14), opened after c7fa8d5e was pushed. Same pinned text (sha1 afd7c65a…) and fixes file (79ad8597).

### C.1 Verdicts side by side
| § | statement | REFEREE (c7fa8d5e) | REFEREE-2 (R2-N5-FBK + Addendum A) | joint |
| --- | --- | --- | --- | --- |
| §1 | ROUTE-k | SIGNED | SIGN | signed |
| §2 | SAT-k | SIGNED (FBK-N1) | SIGN (N-FBK-4) | signed (cond. 2T PFZ-q) |
| §3 | Theorem FB-kT | SIGNED | SIGN (N-FBK-2) | signed (cond. R56, 2T) |
| §3 | FB-kO per phase | SIGNED | SIGN | signed |
| §3 | FB-kO whole-run sentence | SIGNED WITH GAP FBK-1 (false as derived at k = 1) | SIGN for k ≥ 2 only; G-FBK-1 | SAME GAP, found independently; repairs equivalent |
| §4 | ALT, N_ep corollary | SIGNED (FBK-N2) | SIGN (N-FBK-3) | signed |
| fixes | quotes of 2T | verbatim (script) | verbatim (script, Addendum A) | checked by both |
No disagreement. One joint gap, FBK-1 = G-FBK-1.

### C.2 Joint gap / note map
| REFEREE | REFEREE-2 | relation | joint status |
| --- | --- | --- | --- |
| FBK-1 (whole run (n(n − 1) + n^k)·O(n^{k+1}) is O(n⁴) at k = 1; repair "O(n^{k+1}(n² + n^k))") | G-FBK-1 (same; repair "O(n^{max(k+3, 2k+1)})") | SAME gap; the two repairs are the same bound | fixes file: either wording |
| FBK-N1 (SAT-k's t > g_{w_c} unused) | N-FBK-4 (same) | SAME | optional |
| FBK-N2 (ALT's "≥" is (M2κ); "no cycle at t + 1" unused) | N-FBK-3 (same first half) | SAME (our second half is extra) | optional |
| — | N-FBK-1 (§0 lists "(YB as used there)" under R56 (a); R56 (a) has no (YB): it is P-N5-2T's (YB_q), used only through DIR) | ACCEPTED; MISSED by us. Confirmed: FBK l.18 vs R56 (a)'s list (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′) | fixes file: cite (YB_q) as P-N5-2T §2 |
| — | N-FBK-2 (FB-kT step 1 needs (INJ), not listed in FBK §0) | ACCEPTED; MISSED by us (my §3 step 1 took the 2T argument, which names (INJ)). Confirmed: FBK §0's R56 (a) list omits (INJ) | fixes file: add (INJ) |
| §1 premise note (DIR for any m_c; my R-N5-2T 2T-N2) | "Inherited gaps: NONE … PFZ-q and DIR … hold for any m_c" | SAME | — |
| FBK-N3 (DATA: SAT-k met only on constructed witnesses; late regime unreached) | §5 (same; SAT-k met at depth 1 and 2 on unions; controls satk0, shift bite) | SAME; R2 went further (depth 2). Cross-checked below | DATA |

### C.3 Data cross-checks on my engine (this §C)
- R2's depth-2 witness docs/referee-2/R2-N5-FBK/instances/fb17_k3_P66.pg (sha1 712645de, checked; n 42, so PATHN 50): SATK 26 checks, max
  routing depth 2, 0 failures — the same 26 as R2's row (13 / 13). With R2's 2T witnesses (37), SAT-k is now exercised on two engines at depth
  1 and 2. (fbk_logs/r2_k3_witness_s3.txt)
- ALT from the S3 start on ALL of lib41 (n ≤ 64: fbk_logs/lib41_s3only.txt; the 45 games with n > 64: fbk_logs/lib41_big_s3only.txt, MAXN
  1000): clean strict 1,714 + 196 = 1,910; clean ties 75 + 0 = 75; non-clean 19 + 46 = 65 — exactly the packet's §5.2 counts and R2's
  reproduction (1,910 / 75 / 65; the one cycle-node change is not in my ALT_changes counter). Max routing depth 118 (tcL_N12), the same as
  R2's. 0 failures.
| item | REFEREE | REFEREE-2 | agree? |
| --- | --- | --- | --- |
| ALT on lib41, S3 | 1,910 / 75 / 65 | 1,910 / 75 / 65 (/ 1 cycle node) | YES, exactly |
| ROUTE-k max depth | 118 (S3, big games) | 118 (tcL_N12, 233 terminals) | YES |
| SAT-k | 37 (2T witnesses) + 26 (k3 witness) | 76 + 58 (unions) + 26 (k3 witness) | YES (26 = 26) |
| FB-kT late regime | never reached | never reached | YES |

### C.4 Joint state (for the Lead and CHECKER)
- All to-sign items signed by both, conditional on R56 and P-N5-2T's PFZ-q, DIR; the whole-run sentence of FB-kO with the joint gap FBK-1 =
  G-FBK-1 (true for k ≥ 2; O(n⁴) at k = 1).
- Fixes file: FBK-1 repair; N-FBK-1 ((YB_q) is 2T's); N-FBK-2 (add (INJ)); optional FBK-N1 = N-FBK-4, FBK-N2 ⊇ N-FBK-3.
