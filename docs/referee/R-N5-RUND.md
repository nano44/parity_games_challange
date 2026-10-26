# R-N5-RUND: REFEREE report on packet P-N5-RUND (L-SI box 17: CR-REL, offsets and TWIN-GAP, PIECE_D / SPLIT-RED, the per-edge schedule of Lemma P, charging; every game)
Referee: REFEREE (successor 13, session_01Nzrjhmm1pgUnEvdgjCBhTv), Opus 5.5 (owner ruling D15). Context at writing: about 400k tokens.
- Routing: the Lead's GO of 09:08Z (Lead's stamp).
- Object: docs/si/P-N5-RUND-box17.md at trunk 94910ed3, sha1 71e198f359cbb321fc0c15e6c28676d4dd046d52 (checked with `git show 94910ed3:… |
  sha1sum` and `git show 762b7243:… | sha1sum`; identical), 211 lines, frozen at l-si 762b7243. Authors: L-SI successors 12 (§2-§4) and 13 (§5, §6).
- Written 2026-10-26T09:10Z-10:06Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ RUND file opened (I used REFEREE-2's R2-N5-H3 start file pftheta34_n32_S3.start as an input
  only). No lane code run (experiments/si/rund/*.py, experiments/new/box21/n5x.py). D1.
- Premises read against their text: RESULTS R62 (a)-(f) as landed (RESULTS l. 3267-3323); P-N5-H3 §5 (P^c_L, CR-D proofs, the object of R62
  (e)); R55 setting (π_v, u(v), (h3_D), M_D) and (a); R25 setting (lev, COARSE_L, (C1)-(C4); docs/si/P-N5-FB-box7.md §1); R17 (a)-(d); R21 (a) XW;
  R57 (VJ) / 1E-N3; SPEC S2, S4a.
- Tool: scratch/rund_probe.py (own engine; every maximal fallback-free in-phase run S of N5 and, for the schedule items, every suffix run;
  every coarse level L ∈ {−1, …, n − 1}; mutation controls MUT=1 (schedule shifted by one state) and MUT=2 (forbidden-ness ignored)).
  Logs scratch/rund_logs/ (run_all.sh).

## Verdicts
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | setting quotes of R62 | CHECKED by script: the four R62 quotes ((setting), (d), (e), (f)) are verbatim; R55 (a), R17 (a) verbatim in their entries; the R19 (d) "quote" is NOT verbatim (RUND-N1) |
| §2 | Lemma CR-REL | SIGNED |
| §3 | Lemma OFFSET (a)-(c) | SIGNED (under (h3_D) on S) |
| §3 | Lemma MERGE-B | SIGNED |
| §3 | Theorem TWIN-GAP (i)-(iii) and its Corollary | SIGNED (under (h3_D) on S) |
| §4 | Lemma PIECE_D (a), (b); Corollary SPLIT-RED | SIGNED |
| §5 | Lemma P^c_sch; Corollary FRZ-SCH; Corollary CHARGE (with its "Consequence") | SIGNED (hypothesis (ii) only) |
| §6 | Fact FZ | SIGNED; it uses exactly the standing premise (σ̄_k pointwise optimal in G_{σ_k}, = XW / (VJ), 1E-N3) plus definitions (RUND-N2) |
| §6 | Lemma UNF; Corollary CHARGE-U | SIGNED (hypothesis (ii) only) |
| §7-§9, READINGs | conjectures, dead ends, data | not signed (as briefed) |
No gap. Notes RUND-N1..N4. Structural, inside one fallback-free run of one phase; nothing here bounds N5's running time on any class
(TWIN-GAP is exponential in the band B; CHARGE-U needs |U(S)|, unbounded here). Not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. §1 setting and quotes
- Script check (normalised whitespace; "…" splits a quote into parts, each must occur): R62 setting, (d) WM-G, (e) P^c_L / CR-D, (f) FRZ-U_H3:
  all parts verbatim in RESULTS R62 ✓. R55 (a) and R17 (a) (F1): verbatim in R55, R17 ✓. Item letters (b) TC-CLASS, (c) C2-H3, (d), (e), (f)
  match R62 ✓. The FORBIDDEN predicate is new and defined in place ✓.
- RUND-N1: "RESULTS R19 (d), the (SG) step: 'Ξ_{L+1}(z) ⊵ Ξ_L(z) at any N5 transition (on all games)'" is not a verbatim quote: R19 (d) has
  "(on all games, not only 𝒞^1O)" and "(Ξ_{L+1}(z) ⊵ Ξ_L(z) ▷ Ξ_L(σ_L y), …)" in one sentence about a switched y. The fact OFFSET (a) uses,
  Ξ_{k+1}(v) ⊵ Ξ_k(v) for every v at every transition, is RESULTS R15 (a) (Ξ non-decreasing along a run, every game). Cite R15 (a); no
  statement changes.

## 2. Lemma CR-REL
- P-N5-H3 §5 (the object of R62 (e)) read line by line. Hypothesis (i) appears once: Case B, first bullet ("By (i), COARSE(Ξ_k(z)) ≻
  COARSE(Ξ_k(a)), so Ξ_k(z) ▷ Ξ_k(σ_k x) by (Cstrict). So (x, z) ∈ Iσ_k"). Case B's hypothesis is Ω^c_k(z) ≻ Ω^c_k(a), i.e. COARSE_L W_k(z)
  ≻_L COARSE_L W_k(a); (i_rel) gives Ξ_k(z) ▷ Ξ_k(a) directly ✓. Cases A1, A2, the B1 / B2 cycle arguments (and R62's B1 sentence) and the
  proof of CR-D (P^c_L at j = n − 1, (MON), (C3)) never read Ξ ✓. (i) ⇒ (i_rel): (i) turns the W-comparison into the same coarse
  Ξ-comparison, then (Cstrict) ✓. VERDICT SIGNED.

## 3. Offsets
- OFFSET (a) ✓. λ_Ξ = λ_W on V is FRZ-U_H3's proof of (ii) (R55 (a) on F_D; TC-CLASS + (h3_D) on R_D), constant since λ_Ξ is constant on the
  phase. With the cycle node fixed, S1's order compares path sets by w first, so Ξ_{k+1} ⊵ Ξ_k (R15 (a); RUND-N1) and W_{k+1} ⊵ W_k (WM-G)
  give non-decreasing s^Ξ, s^W ✓.
- OFFSET (b) ✓. F_D: Ξ = W (R55 (a)). v ∈ R_D, c := λ(v) = λ_W(v), u := u(v), π_v := v's (σ, τ)-path to u, u excluded (R55). If c ∈ π_v, both
  plays share π_v up to u (σ̄ = τ off D_k), so both reach c along the same prefix, and the path set (vertices before c above c) is the same;
  Δ = 0. If c ∉ π_v, R62 (c)'s factorisation P_F(v) = (π_v ∩ V_{>c}) ⊔ P_F(u) in both frames (λ(u) = c by TC-CLASS) and additivity of w give
  Δ(v) = δ(u) ✓.
- OFFSET (c) ✓. δ_k(u) = w(P_W(u)) − w(P_Ξ(u)) = Σ over P_W ∖ P_Ξ minus Σ over P_Ξ ∖ P_W of ±2^r. (h3_D) gives the same cycle node, so the top
  rank of the symmetric difference is lev(Ξ_k(u), W_k(u)) ≤ M_D ≤ L* (lev = −1 or ⊥ means the difference is empty). Ranks ≥ ℓ_S by the
  definition of ℓ_S ✓.
- MERGE-B ✓ (definition of Δ). The R50 Fact B analogy is a remark.
- TWIN-GAP (i) ✓ (s^W rise = s^Ξ rise + d, both ≥ 0). (ii) ✓. From k_0 + n − 1, FRZ-U_H3 at L* (L* ≥ max_S M_D, L* ≥ −1) keeps
  COARSE_{L*}(W(v)) = COARSE_{L*}(Ξ(v)) constant: the cycle node and P ∩ V_{>L*} are fixed in both frames. The remaining part of w ranges
  over sums of ±2^r with r ≤ L*, one vertex per rank, whose range has width Σ_{r ≤ L*} 2^r = 2^{L*+1} − 1 (even ranks give the top, odd ranks the
  bottom). So each monotone score rises by ≤ 2^{L*+1} − 1, their sum by ≤ 2^{L*+2} − 2. Each offset change consumes ≥ |d| ≥ 2^{ℓ_S} of that
  sum (by (i)), and offsets are multiples of 2^{ℓ_S} (c). If L* = −1, U_S = ∅ and there is nothing to count ✓. (iii) ✓. Corollary ✓.
- VERDICT: OFFSET (a)-(c), MERGE-B, TWIN-GAP (i)-(iii) and Corollary SIGNED (under (h3_D) on S, as stated).

## 4. PIECE_D, SPLIT-RED
- (a) ✓. Aligned ⇔ for every Even edge, Ξ-improvement ⇔ W-improvement, so Iσ_k (S2) = G_τ's improving set at σ_k (G_τ's S1 valuation is W_k,
  Odd having one successor). S4a's arena is then R17's switch-best arena on G_τ, and S4a returns a pointwise optimum of it (R18 (d) S (c);
  R17 (d): every pointwise-optimal choice) ✓.
- (b) ✓. B is a run of switch-best on G_τ from its first state, inside one λ-phase of that run (λ_W constant). R17 (c) applies to a run started
  at ANY strategy: Lemma P's base (k = 0) needs only that u is a cycle node at ρ_0 (my R-N5-REC0 §2 reading of the same proof) ✓.
- SPLIT-RED ✓. λ_W is constant on S under (h3_D) (FRZ-U_H3's (ii)); aligned-source blocks ≤ N_split + 1, each ≤ n + m − 1 transitions ✓.
- The bullet "a forbidden edge at L = −1 is a split edge" ✓ (COARSE_{−1} keeps every rank, so ≻_{−1} gives ▷). The withdrawn §11 READING is
  not used by any PROVED item ✓.
- VERDICT: PIECE_D (a), (b), SPLIT-RED SIGNED.

## 5. The schedule
- P^c_sch ✓. Base m = 0 by (ii). Step: r′'s schedule at k − 1 is clean (k − 1 − (m − 1) = k − m ≥ k_0; edge q′ of r′ is looked at state
  (k − 1) − 1 − q′ = k − 1 − (q′ + 1), the state at which r's edge q′ + 1 is looked at) ✓; IH at k − 1 for r′. P^c_L's step from k − 1 to k
  reads the hypothesis at k − 1 only on the first edge (x, z), in Case B (§2 above) ✓; in Case B, z ≠ a (their coarse W-values differ), so
  "not Ξ_{k−1}(z) ▷ Ξ_{k−1}(a)" would make (x, z) forbidden at k − 1, against cleanness (edge 0 is looked at k − 1 − 0) ✓. The transition
  k − 1 → k is an S4a step of S (k − 1 ≥ k − m ≥ k_0) ✓. Odd x falls in Case A (z = τ(x)) and needs no schedule condition ✓.
- FRZ-SCH ✓ (Ω_t(x) = value(r_t) by (ii); P^c_sch at s; (MON) on [s, t]; (C3) antisymmetry). The containment remark (CR-D, CR-REL) ✓.
- CHARGE ✓. Non-clean schedule of r_s at s − 1 means s − 1 − m < k_0 (window) or an Even edge q forbidden at (s − 1) − 1 − q = s − 2 − q,
  which is ≥ s − 1 − m ≥ k_0 when the window case fails ✓. Window: s ≤ k_0 + m ≤ k_0 + n − 1, so ≤ n − 1 values of s ✓. Consequence: a
  forbidden state f serves s ∈ [f + 2, f + 1 + m], ≤ n − 1 values ✓.
- VERDICT: P^c_sch, FRZ-SCH, CHARGE SIGNED (hypothesis (ii) only; neither (i) nor (h3_D) is used, as stated).

## 6. Charging switches
- Fact FZ ✓, and the Lead's question: it uses exactly
  1. Ξ_k ⊴ W_k pointwise: XW (RESULTS R21 (a), game-general = (VJ) of R57 at τ′ := τ_k), i.e. the standing SPEC premise that σ̄_k = S1's
     output attains the pointwise minimum over Odd's strategies in G_{σ_k} (1E-N3); the packet's "(F1) in G_{σ_k}" is the same fact;
  2. totality of ⊴ (rewards injective, signed weights injective on sets, then length), for "not ▷ ⇒ ⊴";
  3. (Cstrict) (from R25's definition of COARSE_L);
  4. the definition of D_k (σ̄_k = τ_k off D_k), for the last sentence.
  Nothing else (no run, phase, S4a or (ii) hypothesis). RUND-N2: cite XW / (VJ) next to "(F1) in G_{σ_k}".
- Lemma UNF ✓. σ_s(r_q) = r_{q+1} (r_q Even on x's W-play at s); r_{q+1} ≠ σ_f(r_q) (forbidden at f needs z ≠ a); k′ := the largest k ∈ [f, s − 1]
  with σ_k(r_q) ≠ r_{q+1} exists and σ_{k′+1}(r_q) = r_{q+1}; k′ → k′ + 1 is an S4a step of S, whose output at r_q lies in {σ_{k′}(r_q)} ∪
  Iσ_{k′}(r_q) (S4a's arena), so the edge is in Iσ_{k′}, i.e. Ξ-improving, hence not forbidden at k′, so k′ ≠ f; s − 1 − f = q + 1 ≤ m ≤ n − 1 ✓.
- Corollary CHARGE-U ✓. The event (k′, e) from UNF is a switch event with e forbidden at f ∈ [k′ − n + 1, k′ − 1] ∩ S; k′ + 1 ≤ s ≤ k′ + n − 1,
  so an event serves ≤ n − 1 values of s; plus ≤ n − 1 window changes ✓. The last bullet is immediate ✓.
- VERDICT: FZ, UNF, CHARGE-U SIGNED.

## 7. Own data (DATA, not signed; scratch/rund_logs/)
Own engine; every maximal fallback-free run S inside a phase of an N5 run, every L ∈ {−1, …, n − 1}; schedule items also on every suffix run
(SUFFIX=1) except lib41 (SUFFIX=0: k_0 = the start of each maximal run; the suffix loops are cubic in |S| and too slow there).
| sample | runs | runs S | checks (selection) | failures |
| --- | --- | --- | --- | --- |
| long runs: frz1/frz2/frz3_n24 (canonical + their .start) and pftheta34_n32 (canonical + R2-N5-H3's S3 start), SUFFIX=1, PSCH off | 8 | 11 | FRZ-SCH 9,880,461 pairs; CHARGE 159,674 changes (112,261 window, 47,413 charged); UNF 57,867; CHARGE-U 169,320; FZ 798; OFFb 6,056; TG-i 397; CR-REL 5; SPLIT 11 | 0 |
| random games n 4-9, k ≤ min(3, n − 1), 6,000 games, seed 21, canonical + 3 random starts, PSCH (exhaustive simple paths) for n ≤ 7 | 24,000 | 3,087 | P^c_sch 62,957; FRZ-SCH 208,333; CHARGE 10,036 (all window); OFFb 44,352; SPLIT 3,037 | 0 |
| lib41 (412 files, 45 with n > 64 skipped; canonical + 2 random starts + 29 given .start pairs), SUFFIX=0, PSCH for n ≤ 7 | 1,130 | 1,572 | FRZ-SCH 67,380,884; CHARGE 757,338 (692,137 window, 65,201 charged); UNF 70,546; CHARGE-U 1,676,596; FZ 85,174; OFFb 337,373; TG-i 22,702; TG 25,074; PIECE-b 11,156; SPLIT 1,076; CR-REL 3; P^c_sch 951 | 0 |
| controls on frz1, frz3: MUT=1 (schedule one state late) / MUT=2 (forbidden-ness ignored) | 4 each | 7 each | FRZ-SCH | 78,800 / 405,240 FAIL (as they must) |
- failures = CRREL, OFFa, OFFb, OFFc, TGi, TGii, TGiii, PIECEb, SPLIT, PSCH, FRZSCH, CHARGE, FZ, UNF, CHU, PREFIX: all 0.
- Maxima: B 19 on the long runs, 44 on lib41 (n ≤ 64); N_v 10 / 19; |U(S)| 7 on the long runs (= the packet's long-run rows) and 23 on lib41.
  My |U| is per level L and includes given starts, so it is not comparable with the packet's lib41 row (6, presumably L = −1).
- Thin: CR-REL's own hypothesis ((i_rel) at every state of a run with ≥ n transitions) held only 3-5 times; P^c_sch's exhaustive check runs
  only on small games (n ≤ 7), where charged changes do not occur; the schedule logic is exercised on the long runs and lib41 through
  FRZ-SCH / CHARGE / UNF.
- Reproduce: scratch/rund_logs/run_all.sh from docs/referee/scratch/.

## 8. Notes (not gaps)
- RUND-N1 (citation, §1 / §3 OFFSET (a)): the R19 (d) "quote" is not verbatim; the fact used is R15 (a).
- RUND-N2 (citation, §6 FZ): name XW (R21 (a)) / (VJ) (R57) for Ξ_k ⊴ W_k, and (Cstrict), totality of ⊴ as the other inputs.
- RUND-N3 (wording, §4 PIECE_D (b)): say that R17 (c) is applied to switch-best started at B's first state (Lemma P's base holds at any start).
- RUND-N4 (wording, §3 TWIN-GAP (ii)): "each rank r contributes at most 2^r" — the bound used is the WIDTH of the range of the low part,
  Σ_{r ≤ L*} 2^r = 2^{L*+1} − 1 (one vertex per rank, signed by parity); say so, since a reader may add the two signs twice.

DONE (REFEREE successor 13, (Opus 5.5, D15)).
