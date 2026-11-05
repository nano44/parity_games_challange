# Box 164 N5-ENCODE: the encoding (entropy-compression) method applied to IDEAL-ACYC run length — exact translation, the bound it gives (T ≤ μ·|R|), its degenerate form (no entropy is consumed), kills of the injective and constant-bit forms, and one surviving polynomial-strength conjecture REC-2
L-NEW successor 54, 2026-11-05 (date -u: see the commit). Lead brief BOX 164 (D14 / D18): option (a), entropy compression. Labels:
PROVED (lane, unrefereed) / DATA / CONJECTURE / DEAD (with instance) / READING. Model, c-step, forced run, T_k(m), T^R, ISO: packet
P-IDEAL-FLIP §0-§1 (docs/new/P-IDEAL-FLIP.md, frozen 9effea1f; landing as R110). MONO-FLIP: box 163 §1 (docs/new/N5-FLIPXI-box163.md,
PROVED (lane)). Not a TARGET.md claim. No polynomial bound is proved. FLIP-ADD, SLOT-TRADE and G-N5-TIME stay OPEN.

## 0. Answer
- Translation (§1). A run is encoded by its last state and one RECORD per move: (x, ρ), x the mover, ρ the DECISIVE β of the A-set
  comparison that let x move (the largest-rank β of Ξ_(s_(t−1))(x, new) △ Ξ_(s_(t−1))(x, old)). At degree 2 the record plus s_t
  determines s_(t−1) (Lemma REV), so the encoding is injective.
- The bound the framework gives (§2, PROVED (lane), elementary): T ≤ #moves ≤ μ · |R|, μ := the largest number of moves of one run
  carrying the same record, R := the set of possible records. On ISO 𝓛^R_(m+1) in the forced model |R| ≤ 2m · 4m = 8m².
- Why only this form (§2, PROVED (lane)): the Moser–Tardos counting inequality bounds the run by «records of length L» against «random
  bits consumed in L steps». An IDEAL run consumes no random bits (deterministic in (G, s_0)); a forced run consumes ≤ 1 bit per frame
  and only k changes. So the counting inequality is vacuous here and what survives is the charging bound above. Everything rests on μ.
- Kill test (§3): no exact value lies above the bound for any μ ≥ 1 (T^R = 2, 4, 8, 13; T_k(2) = 4, 5, 7, 8, 8, 9; T_∞(2) = 9 are all ≤
  8m² resp. 16(d − 1)² + 2). The translation is consistent. Every T_k value my DP recomputes on the witness files matches the
  table (§5 S3), so the forced-model code is the right one.
- DEAD (§4):
  - injective records (μ = 1) on real runs: iso_d3_6 (sha1 c1ced511), record (3, β11) at steps 1 and 5;
  - REC-0 «μ_0 = 1 with a constant bit»: kf0_d4_t8 (the T_0(3) ≥ 8 witness, sha1 aed4fd15), c = 0, record (5, β8) at frames 3 and 8;
  - REC-K «μ_k ≤ 1 + ⌈k/2⌉»: dies with REC-0 at k = 0;
  - a k-independent μ: finfclimb_m3_mu4_T11 (sha1 8e71f8a7) has μ_k = 1, 2, 2, 3, 3, 3, 4 for k = 0..6 (μ_∞(3) ≥ 4); so the route
    cannot reach T_∞ / INF-ADD;
  - records WITHOUT the key rule (control): on the 2-wide diamond Ξ-DAG the longest single-switch improving path is 8, 22, 52, 114
    (n = 2..5 layers, hill-climbed; = 2^(n+2) − 2n − 4 on these four points, DATA) with μ_free = 8 at n = 4. Any bound on μ must use
    the key rule (same phenomenon as the fleet's CDAG_n, docs/new/N5-K9-Pstrict-counter.md).
- CONJECTURE REC-2 (DATA only, §5): in the forced model with ≤ 2 flips, μ_2(m) ≤ 2 for every m. Data: every screened ISO 𝓛^R genome
  (m ≤ 3) and the m = 4 hill-climbs (interim: μ_2 = 2 at T_2 = 9). If true: T_2(m) ≤ 16m² (PROVED (lane) conditional, §2), hence by
  W-ONLY (d) T ≤ 16(d − 1)² + 2 on ISO 𝓛^R_d. Warning (READING): μ_0 rises from 1 (m = 2) to 2 (m = 3), so μ may grow with m; a
  bounded-by-poly(m) version is EQUIVALENT to T_2 polynomial (μ_2 ≤ #moves ≤ 2m·T_2), so it adds nothing. Only the constant form
  REC-2 has new content, and it is the one to kill or prove.

## 1. Translation: every R104 rule and where it goes (model: P-IDEAL-FLIP §0)
| R104 rule (P-IDEAL-FLIP §0) | in the encoding |
| --- | --- |
| state s picks one option per mover | the encoded object is the sequence s_0, …, s_T |
| A_s(x) = {s(x)} ∪ {k : Ξ_s(x, k) ▷ Ξ_s(x, s(x))} (old state) | the record ρ = decisive β certifies s_t(x) ∈ A_(s_(t−1))(x): ρ is the largest-rank β of P △ Q, P := Ξ_(s_(t−1))(x, s_t(x)), Q := Ξ_(s_(t−1))(x, s_(t−1)(x)); ρ ∈ P iff ρ has even parity |
| keys under the NEW state, level by level; least key in A | NOT in the record. It selects which A-members move. It is the only place a bound on μ can come from (§4 control) |
| stop rule (all A singletons, or s_t = s_(t−1)) | the run ends; every counted step has ≥ 1 move, so T ≤ #moves |
| degree 2 | the new option of a moving mover is its other option: the record (x, ρ) fixes it |
| level 0 under ISO (𝓛^R) | via W-ONLY (P-IDEAL-FLIP §2) the levels ≥ 1 run as a forced run with ≤ 2 flips: records are taken on U only |
- Variant V (kept for comparison, rec.py): ρ_V := the decisive β of V_(s_t)(x) △ V_(s_(t−1))(x) (value change). On the real runs
  screened it has the same multiplicity as ρ except L-RED's grow_top_N15 (degree 3: ρ 4, ρ_V 2) (§5 S1); the text uses ρ.
- Lemma REV (PROVED (lane); IDEAL-ACYC, every mover of degree ≤ 2). For every step t, s_(t−1) is s_t with the movers of Mv_t switched
  to their other option; Mv_t is the set of movers named in the records of step t. So (s_T; records of step T, …, records of step 1)
  determines the whole run. Proof: degree 2 and s_t(x) ≠ s_(t−1)(x) for x ∈ Mv_t, s_t(x) = s_(t−1)(x) otherwise. ∎
- Lemma CHAIN-UP (PROVED (lane); IDEAL-ACYC, any degree; a by-product used to read records). Along a real run or a forced run with any
  bit schedule, for every option (x, k) the set Ξ_(s_t)(x, k) is ⊵-non-decreasing in t. Proof: if xt(x, k) = X it is constant. Else,
  z := xt(x, k): Ξ_(s_t)(x, k) = {β(x, k)} ∪ V_(s_t)(z), β(x, k) is on no chain from z (acyclic), V_(s_t)(z) is ⊵-non-decreasing by
  MONO-FLIP (box 163 §1; each step's movers take options of their old-state A-sets), and (O1) of box 163 §1 gives the claim. ∎
  So x can move away from option k and back only if the OTHER option's chain rose in between; a record recurs only if the decisive β
  left the symmetric difference and came back (example §4 D2).

## 2. The bound, and why the Moser–Tardos form degenerates
- Proposition CHARGE (PROVED (lane)). Let μ(run) := max over records r of #{moves of the run with record r}. Then T ≤ #moves ≤ μ(run) ·
  #{records used}. In the forced model on G ∈ 𝓛^R_(m+1) with ISO, every record is (x, β(y, j)) with x, y ∈ U (U has 2m movers; under
  ISO no chain from a U-option visits level 0), so #records ≤ 2m · 4m = 8m². Hence T_k(m) ≤ μ_k(m) · 8m², μ_k(m) := the sup of μ over
  forced runs with ≤ k flips. Proof: each counted step has a move; each move has one record; group the moves by record. ∎
- Corollary (PROVED (lane), conditional on REC-2): T_2(m) ≤ 16m²; with W-ONLY (d) (P-IDEAL-FLIP §2, signed by both referees, landing
  R110): T ≤ 16(d − 1)² + 2 for every ISO genome of 𝓛^R_d and every start.
- Proposition NO-ENTROPY (PROVED (lane); the precise obstruction to the brief's «far fewer bits» form). The encoding method in the
  Moser–Tardos form bounds Pr[run ≥ L] ≤ #(record sequences of length L) · 2^(−b(L)), b(L) := random bits read in L steps. (i) A real
  IDEAL run reads none: s_t = F_G^t(s_0) for a fixed map F_G, so b(L) = 0 and the inequality reads 1 ≤ #(record sequences): vacuous for
  every L. (ii) A forced run reads the bits c_t, but c_t is not fresh: with ≤ k flips the whole schedule has ≤ 1 + k·⌈log_2(L + 1)⌉
  bits, and the worst case over schedules (T_k is a sup) is again deterministic. (iii) Hence the only usable content of the method on
  this model is an injectivity/multiplicity statement on records — CHARGE — and a bound needs μ = O(poly), which is a statement about
  the dynamics, not about information. Proof of (i)-(ii): definitions (P-IDEAL-FLIP §0-§1). ∎
- Cited method, NOT opened in this box (HYPOTHESIS as a citation, not used in any proof): R. A. Moser, G. Tardos, «A constructive
  proof of the general Lovász Local Lemma», J. ACM 57(2) 2010, Article 11 (DOI 10.1145/1667053.1667060), main theorem. Nothing above depends on it: CHARGE and NO-ENTROPY are proved here.
- READING on option (b) (tropical): Gen.face (box150/check.py) already writes Ξ-values as Σ ±2^rank; a run depends only on the rank
  order and parities. A cell count of the tropical arrangement bounds how many DIFFERENT runs a genome family has as the weights move,
  not the length of one run at one weight vector. Same degeneracy as NO-ENTROPY; not pursued.

## 3. Kill test of the translation against the exact data
| exact value (source) | bound with μ = 1 / μ = 2 | consistent |
| --- | --- | --- |
| T_k(1) = 2, 3 (P-IDEAL-FLIP §5) | 8 / 16 | yes |
| T_k(2) = 4, 5, 7, 8, 8 (k 0-4), 9 (k ≥ 6) (box 162/163, L-COMP 27) | 32 / 64 | yes |
| T_∞(2) = 9 (box 163) | 32 / 64 (μ_∞(2) = 2 measured, §5) | yes |
| T^R(d) = 2, 4, 8, 13 (d 1-4; ISO values ≤ these) | W-ONLY (d): 16(d − 1)² + 2 = 2, 18, 66, 146 at μ = 2 (d ≥ 2) | yes |
- No exact value exceeds the bound, so no step of the translation is refuted. Per instance, #moves ≤ μ · #records used holds by
  definition (rec.py prints both).

## 4. DEAD (instances; files under experiments/new/box164/ unless a path is given)
- D1 injective records on real runs (μ = 1). box160/out/iso_d3_6.json (sha1 c1ced511, 𝓛^R_3, ISO), real run from its start, T = 6:
  record (3, β11) (β11 rank 10, even) at steps 1 and 5 (mover 3: 1→0, 0→1 at step 3 with decisive β7, 1→0 again). Level-0 moves at
  steps 3 and 5. (show.py prints the run.) So μ ≥ 2 on real runs at d = 3.
- D2 REC-0 (constant bit, μ_0 = 1). box162/out/kf0_d4_t8.json (sha1 aed4fd15; the T_0(3) ≥ 8 witness), c = 0, U-start (movers 2-7)
  001101, T_0 = 8 frames: records per frame [(4, β12)], [(7, β8)], [(5, β8), (6, β12)], [(3, β6), (4, β6)], [(5, β14), (7, β14)],
  [(2, β13), (4, β8)], [(7, β8)], [(5, β8)]. (5, β8) at frames 3 and 8, (7, β8) at frames 2 and 7. β8 = β(4, 0) (rank 9, even): mover 4
  leaves option 0 at frame 4 and returns at frame 6, which puts β8 back on the chains 5 → 7 → 4 and 7 → 4 (CHAIN-UP's mechanism).
- D3 REC-K (μ_k ≤ 1 + ⌈k/2⌉): dies at k = 0 by D2 (fkall.sh screen: 6 (file, k) kills, all at k = 0, all m = 3).
- D4 a k-independent μ: out/finfclimb_m3_mu4_T11.json (sha1 8e71f8a7, ISO 𝓛^R_4): (T_k, μ_k) = (3,1) (5,2) (6,2) (7,3) (8,3) (9,3)
  (10,4) (11,4) for k = 0..7 (fk.py). μ grows with the number of flips, so CHARGE cannot bound T_∞.
- D5 (control, no keys) records alone. keyless.py / diamond.py: all 2^N states, an edge for every improving switch (single switches
  for diamond.py; acyclic by MONO-FLIP). Diamond Ξ-DAG (layers 1..n, movers a_i, b_i, both options of a layer-i mover to a_(i+1) resp.
  b_(i+1)), ranks and parities hill-climbed: longest path 8, 22, 52, 114 for n = 2, 3, 4, 5 (out/diamond_n<n>_L<L>.json; n 5 sha1
  3fa80814), μ_free = 1, 4, 8, 8. So the decisive-β record has no bounded multiplicity in the key-free dynamics: the key rule is
  necessary for any CHARGE bound.

## 5. DATA (experiments/new/box164/, logs in log/)
- S1 real runs (rec.py; real IDEAL runs from the file's start): μ ≤ 2 on every degree-2 genome screened — every 𝓛^R file in box160/out,
  box162/out, box163/out and L-RED's degree-2 sets (claude/l-red @ 5f3e89e1 experiments/red/r187/out T_d3..6_W2, A_d4/6_W2_k2);
  μ ≤ 4 on L-RED's degree-3/4 sets (r178/r187 big_*, grow_*, fl_*; e.g. grow_top_N24 N 24, T 64, 119 moves, 106 records, μ 4)
  (log/lred_rec.txt). Hill-climbs on μ (climb.py d 3-6, seeded.py from the d 4 maxima): μ = 2 at best.
- S2 key-free control: random degree-2 acyclic genomes N 4-8 (keyless.py): μ_free ≤ 3, longest paths 10-20; diamond D5.
- S3 forced model (fk.py: exact DP over (U-state, bit, flips left); finf.py: k = ∞). Recomputed T_k equal the known table on the
  witness files (T_0(2) 4, T_1(2) 5, T_2(2) 7, T_3(2) 8, T_8(2) = T_∞(2) 9; T_0(3) 8 on kf0_d4_t8). Screen fkall.sh over 94 ISO 𝓛^R
  files (m ≤ 3) × k 0..8 (log/reck_screen.txt): μ_0 ≤ 2, μ_1 ≤ 2, μ_2 ≤ 2 everywhere; μ_k reaches 3 at k ≥ 3 (kf4_d3_t8: μ_4 = 3) and 4
  at k ≥ 6 (D4).
- S4 REC-2 hill-climbs at m = 4 (fkclimb.py k m; objective (μ_k, T_k)): interim at the commit μ_0 = 2 (T 5), μ_1 = 2 (T 9), μ_2 = 2 (T 9);
  final numbers go into the box report. finf.py climb m 4: μ_∞ ≥ 3 at T_∞ ≥ 16.

## 6. Next (Lead decides)
- Kill side (cheap): a dedicated REC-2 search at m = 4, 5 (fkclimb.py 2 m, many restarts; m 5 = 1024 U-states, fine), and the
  L-RED/L-COMP exact maxima of T_2(3), T^R(4) through fk.py. One instance with μ_2 = 3 kills REC-2.
- Proof side: CHAIN-UP says a record (x, β(z, j)) recurs only after z (or a mover rerouting the chain above z) leaves and re-enters;
  REC-2 needs: with ≤ 2 flips, this happens at most once per record. The natural induction is on the Ξ-depth of z below x combined with
  NOW-ONCE's ratchet (between consecutive moves of x, the key-preferred option of x under the new state changes).
