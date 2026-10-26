# R2-N5-FBK: second-referee check of packet P-N5-FBK (L-NEW box 44: ROUTE-k, SAT-k, Theorem FB-kT, Corollary FB-kO, Lemma ALT and its N_ep corollary; conditional on RESULTS R56 and P-N5-2T's PFZ-q, DIR). REFEREE-2 (successor 14), written 2026-10-26 04:5xZ-05:0xZ (date -u)
Signature: (Opus 5.5, D15). Lead's order 04:55Z (its stamp).
Object: docs/new/P-N5-FBK-box44.md, `git show 5d723af6:docs/new/P-N5-FBK-box44.md | sha1sum` -> afd7c65a265053531171b66294811bbd9a801dd2
(= the Lead's pin; = my tree), 114 lines (L-NEW successor 23, frozen at l-new 9dd499d3). No fixes file.
Background read: RESULTS R56 (whole entry), R54 (e), R15 (a); P-N5-2T (sha1 fcb91130, my R2-N5-2T 8f43432b); the FBRED packet §0-§1.2.
Independence: no docs/referee/ FBK file (`git ls-tree --name-only` of docs/referee/ on trunk and origin/claude/referee, filtered for fbk:
empty at 04:5xZ); none opened. The lane's experiments/new/box44/altcheck.py was not run or imported.
Tools (own code, docs/referee-2/R2-N5-FBK/): fbk_check.py (on R2-N5-2T/tt_check.py and succ. 13's Runner / fbred_check.Ctx), run_all.sh,
logs/, instances/fb17_k3_P66.pg (sha1 712645de…), witness.lst.
Labels: PROVED (L-NEW 23), every game, CONDITIONAL on RESULTS R56 (landed) and P-N5-2T's PFZ-q and DIR (signed by me in R2-N5-2T; REFEREE's
report on 2T not yet out). A bound on in-phase fallbacks per phase: not a running-time bound, not a TARGET.md claim. G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | notes |
| --- | --- | --- |
| §1 Lemma ROUTE-k | SIGN | — |
| §2 Lemma SAT-k | SIGN (conditional on 2T's PFZ-q) | N-FBK-4 (hypothesis t > g_{w_c} unused) |
| §3 Theorem FB-kT | SIGN (conditional on R56, 2T's PFZ-q and DIR) | outer count and depth recursion checked (§3 below); N-FBK-2 |
| §3 Corollary FB-kO, per-phase bound | SIGN (conditional) | — |
| §3 Corollary FB-kO, whole-run sentence "O(n^{2k+1}) for fixed k" | SIGN for k ≥ 2 only; FALSE as stated at k = 1 | G-FBK-1 (minor; repair stated) |
| §4 Lemma ALT | SIGN | N-FBK-3 ("≥" is (M2κ); the content is "equality only at a tie") |
| §4 Corollary (N_ep) | SIGN | — |
| §5 | not signed (as briefed) | §5.2 ALT data reproduced exactly by my own engine |
One minor gap, G-FBK-1 (one sentence; the per-phase theorem and corollary are unaffected). No (P).
Inherited gaps (the Lead's item): NONE. P-N5-2T's PFZ-q and DIR have no gap (R2-N5-2T §2, §4). Neither proof uses |Q_c| ≤ 2: PFZ-q is per
terminal; DIR's routing step ("y is the first vertex of q's play, which meets c before any other vertex of Q_c, so y ∉ Q") holds for any
m_c. So both apply verbatim with m_c > 2, as FBK uses them.
TARGET.md diff: no TARGET.md §1 or §2 object is claimed.

## 1. Premises and quotes
- R56 (a), (b), (d), (f) as cited ✓ (texts as in R2-N5-2T §1; (d)'s Y^q_t definition is R56 (d)'s "with Y^q_t := {y ∈ succ(q) ∩ U_c : y's
  honest play at t avoids q}" ✓). R54 (e) "phases ≤ n(n − 1) + ∏_i deg(o_i)" ✓. P-N5-2T cited by sha1 fcb91130 per its Citation form line ✓.
- N-FBK-1 (wording): §0 lists "(YB as used there)" among R56 (a)'s facts. R56 (a) has no (YB): (YB_q) is P-N5-2T's own lemma (N-2T-2), and
  FBK uses it only through 2T's DIR. Harmless, since FBK is conditional on DIR; cite (YB_q) as P-N5-2T §2.
- N-FBK-2 (wording): step 1 of FB-kT ("equal tuples ⟺ one Q-run") needs (INJ) (κ constant ⟺ Ξ constant), which §0 does not list; it is
  in R56 (a).

## 2. ROUTE-k and SAT-k: SIGN
- ROUTE-k ✓. par_t(q) exists for a non-direct q (its play reaches c, on its cycle, and meets another vertex of Q_c first). Along a chain
  every vertex is non-direct (it has a parent). A cycle q = p_0 → … → p_r = q puts p_1, …, p_r on q's play in order (positional: from p_i
  on, q's play is p_i's), so q's play revisits q: q is on its own honest cycle, hence direct: contradiction. Acyclic ⇒ the chain's
  vertices are distinct terminals of Q_c, so depth ≤ m_c − 1 ✓. Statewise.
- SAT-k ✓. y := σ̄_t(q); y's play = rest of q's play, avoids q, meets p first among Q_c and before c. y = p: direct ✓. Otherwise y ∉ T
  (y ≠ c; y ∉ Q_c; the only cycle node in U_c is c) ✓. "≤": p is the first vertex of T ∩ U_c on y's play, so (SP′) makes the prefix simple;
  its other vertices are in U_c ∖ T, Even edges σ_t's, Odd forced: a path of G_c^p; (Aκ) ✓. "≥": PFZ-q (2T §2) for the terminal p, Θ = Θ_p,
  z = y ∈ U_c ∖ T, j = w_c, t > f^{Θ_p}_{w_c}; simple paths of G_c^p have ≤ w_c edges; κ_Θ(p) = κ_t(p) ✓. |S_{q,p}| ≤ d_q ✓.
  - N-FBK-4: the hypothesis t > g_{w_c} is not used by the proof (only the p-run saturation is). It is harmless (FB-kT has it anyway).

## 3. Theorem FB-kT: SIGN (the Lead's items)
- Outer count (sum over terminals of distinct monotone tuples) ✓. With (INJ), Ξ(q) constant ⟺ κ(q) constant; by (M2κ) every coordinate
  is non-decreasing over the phase, so equal tuples at k_i < k_{i′} force the tuple constant in between (one Q-run), and conversely;
  N_late = #distinct tuples (sources, FBRED-N1). A coordinate that changes takes a value it never had (monotone), so each change of tuple
  creates a NEW value in at least one coordinate; there are Σ_q (V_q − 1) new values in all; N_late ≤ 1 + Σ_q (V_q − 1) ✓. Cycle nodes
  in Q are constant ✓. (This sum over terminals is finer than 2T's per-class product, and for k = 2 gives the same order.)
- Depth recursion for V_q ✓.
  - h = 0: DIR at k_i (k_i > g_{n−1} ≥ g_{w_c}); |A_q| ≤ d_q + w_c ≤ D_c ✓.
  - h ≥ 1: at an index i where q has depth h, p := par_{k_i}(q) has depth h − 1 (ROUTE-k chain) ✓. Fix (p, α): the block {i : x_i(p) = α}
    is an interval, all its sources in one p-run Θ ✓; after its first w_c indices, k_i > f^Θ_{w_c} ✓, so SAT-k at k_i (for the indices
    where par(q) = p) gives x_i(q) ∈ S_{q,p} + α, ≤ d_q values; the first w_c indices give ≤ w_c values; so ≤ w_c + d_q ≤ D_c values per
    (p, α) ✓. The α's used are values of x(p) at indices where p has depth h − 1, so ≤ V_{p,h−1} of them ✓. V_{q,h} ≤ Σ_{p ≠ q} D_c·V_{p,h−1} ✓.
  - Induction: max_q V_{q,h} ≤ (m_c − 1)·D_c·max_p V_{p,h−1} ≤ D_c((m_c − 1)D_c)^h ✓; h ≤ m_c − 1 ✓; V_q ≤ Σ_h V_{q,h} ≤ m_c·D_c·((m_c − 1)D_c)^{m_c−1}
    (each term ≤ the last; m_c = 1 gives D_c with 0⁰ = 1) ✓. D_c ≤ 2|U_c| − 1 ≤ 2n ✓.
  - The model obstruction of §5.1 (not signed) is consistent with this: the recursion is a product over depth, and only the outer step is
    a sum.
- Corollary FB-kO, per phase ✓: Σ_c m_c ≤ k; N_late ≤ 1 + k·V_max with V_max ≤ k·2n·(2(k − 1)n)^{k−1}; f ≤ 1 + (n − 1)(1 + N_late) =
  O(k²(k − 1)^{k−1}2^k n^{k+1}) ⊆ O(k^{k+1}2^k n^{k+1}) ✓. Start-free (per phase; inductions inside runs) ✓.
- G-FBK-1 (minor gap, one sentence): "With R54 (e) (phases ≤ n(n − 1) + n^k), the in-phase fallbacks of a whole run are O(n^{2k+1}) for fixed
  k." The product is (n(n − 1) + n^k)·O(n^{k+1}) = O(n^{k+3} + n^{2k+1}), which is O(n^{2k+1}) only for k ≥ 2. At k = 1 it is O(n⁴), not
  O(n³). Repair: "O(n^{max(k+3, 2k+1)}), i.e. O(n^{2k+1}) for fixed k ≥ 2" (the packet's §5.3 already restricts to k ≥ 2; on 𝒞^1O R48 is the
  sharper landed form). No other statement depends on that sentence.

## 4. Lemma ALT and the N_ep corollary: SIGN
- ALT ✓. Clean: q on no honest cycle at t and t + 1, y2's play at t avoids q. (Aκ) at t + 1: κ_{t+1}(q) = κwt_c(q) + κ_{t+1}(y2), y2 ∈ U_c
  (the packet cites κ-Y-FORM_D there; (Aκ) suffices). (M2κ): κ_{t+1}(y2) ≥ κ_t(y2). y2 ∈ Y^q_t, so κ-Y-FORM_D at t (q on no cycle at t)
  gives κ_t(q) = κwt_c(q) + min_{Y^q_t} κ_t ≤ κwt_c(q) + κ_t(y2); and the min is κ_t(y1) by (Aκ) at t ✓. Equality forces both
  inequalities to be equalities: the tie ✓.
  - N-FBK-3: κ_{t+1}(q) ≥ κ_t(q) is already (M2κ) at every in-phase transition; ALT's content is that a clean change of σ̄(q) is STRICT
    unless it is a tie.
- N_ep corollary ✓: epochs = 1 + #in-phase transitions changing σ̄|Q; each such transition is charged to one q whose σ̄ changes, which is
  a cycle node (cyc_q), non-clean (nc_q), a clean tie (tie_q), or clean strict, in which case κ(q), hence Ξ(q), changes (ρ_q) ✓.

## 5. DATA (fbk_check.py; own definitions; S3 start (#0) and random starts)
| set | runs | phases | ROUTE-k (max depth, max m_c) | SAT-k (at depth 1 / 2) | best SAT-k closeness | ALT clean strict / clean equal (all ties) / non-clean / cycle node | NEP | violations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41.txt × 2 | 824 | 4,791 | 135,945 (118, 233: tcL_N12) | 0 | −2 | 2,844 / 124 / 97 / 2 | 4,791 | 0 |
| R2-N5-KW/files.lst × 2 (𝒞^1O) | 1,006 | 4,158 | — (m_c ≤ 1) | — | — | 3,173 / 131 / 47 / 3 | 4,158 | 0 |
| lib2o_noref.lst × 3 | 123 | 370 | 1,334 (1, 2) | 0 | −5 | 64 / 0 / 0 / 0 | 370 | 0 |
| box-43/44 × 5 | 50 | 284 | 1,934 (5, 6) | 0 | −5 | 67 / 1 / 1 / 0 | 284 | 0 |
| random 𝒞^kO n 4-12 | 20,000 | 49,359 | 99,220 (5, 10) | 0 | −1 | 232 / 35 / 32 / 23 | 49,359 | 0 |
| UNIONS box-43/44 ⊎ k3 (chain class q3 → q2 → q1, \|U_c\| 10), 2 priorities × 3 starts | 60 | 332 | 4,320 | 76 (38 / 38) | +8 | 108 / 3 / 1 / 0 | 332 | 0 |
| UNIONS ⊎ g5 (R2-N5-2T's gadget) | 60 | 329 | 3,689 | 58 (58 / 0) | +11 | 91 / 2 / 0 / 0 | 329 | 0 |
| instances/fb17_k3_P66.pg (S3) | 1 | 5 | 150 (2, 3) | 26 (13 / 13) | +8 | 7 / 0 / 0 / 0 | 5 | 0 |
- ALT reproduction: from the S3 start only (logs/mut_altstrict_lib41.txt, 1 run per lib41 file) my engine finds 1,910 clean strict, 75
  clean ties, 65 non-clean, 1 at a cycle node — exactly the packet's §5.2 counts (lane's altcheck.py not run). Every clean equality is a tie
  (0 ALT violations); the control altstrict (ALT asked strict always) fails exactly on the 75 ties.
- SAT-k's hypothesis is never met on natural instances (best −1 random, −2 lib41); it is met on constructed unions (as for SAT-2,
  R2-N5-2T N-2T-6), at depth 1 AND depth 2 of the routing chain. Controls on the k3 unions: satk0 (no saturation) fails 4 times, shift (α :=
  (0, 0)) fails 76 / 76: the saturation and the parent's value both matter.
- ROUTE-k holds at depth up to 118 (tcL_N12, a class with 233 terminals): no routing cycle in 246,592 checks (the sets above).
- Not reached: FB-kT's late regime (index ≥ n) in any sample; my strengthened counter (indices ≥ 1 + max w_c, which step 2 also supports)
  is reached only trivially (≤ 67 phases, natural data, small counts). FB-kT and FB-kO rest on their proofs.
- Reproduce: `sh docs/referee-2/R2-N5-FBK/run_all.sh` (≈ 45 s); `FK_MUT=satk0|shift|altstrict` for the controls.

## 6. Notes
- G-FBK-1 (minor gap): the whole-run sentence of Corollary FB-kO is false at k = 1 (O(n⁴), not O(n³)); true for k ≥ 2. Repair as in §3.
- N-FBK-1: (YB) is P-N5-2T's (YB_q), not an R56 fact. N-FBK-2: (INJ) used in step 1, not listed.
- N-FBK-3: ALT's "≥" is (M2κ); its content is strictness off ties. N-FBK-4: SAT-k's t > g_{w_c} is unused.
- Inherited from P-N5-2T: nothing open (PFZ-q, DIR signed without gap; both hold for any m_c).
- DATA: ALT counts reproduced exactly; SAT-k met only by constructed games (depth 1 and 2); late regime unreached.
