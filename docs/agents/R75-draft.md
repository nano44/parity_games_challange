# Draft RESULTS R75 (Lead, 2026-10-28 21:49Z by date -u; both reports, both §Cs and the fixes file filled) (rev. 21:52Z by date -u: Lead removed an unsourced inference from Honest limit (ii)) (rev. 2026-10-28 22:34Z by date -u: C84 E-1 (a), (b), E-2 (with the reread sentence kept and scoped per phase), N-1, N-2, N-3; N-4 not applied) — to CHECKER C84 — LANDED in RESULTS Results 2026-10-28 22:53Z (CHECKER C84 Add. 1 d756549c PASS), after R74

### R75 [refereed-only] N5 on EVERY game, inside one phase: the κ-offset off(q; p) of an Odd choice vertex q ≠ c to its routing vertex p := par_{t+1}(q) never falls (Lemma OFFSET-MONO for q on no honest cycle at t; Lemma OFFSET-MONO⁺ for every q), so a change of κ(q) is a sum of non-negative level rises along q's chain (Corollary CHAIN-SUM with OFFSET-MONO⁺), and per run J of a phase and class the transitions that change κ(q) number at most Σ_x (|EXIT_x| + Σ_π (v_x(π) − 1)) ≤ Σ_x D·(|EXIT_x| + 1), pieces cut at the exit changes only (Corollary CHAIN-COUNT‴; the cut versions CHAIN-COUNT, CHAIN-COUNT′, CHAIN-COUNT″ hold on their own proofs); an unchanged cycle of c keeps every κ-value, routing vertex and offset on it (Remark Z-CONST); the cycle changes of a class number at most (n − 1)|U_c| + TIE_c + ODDC_c per phase (Lemma ZCH-COUNT); the transitions with an F-touching κ-change number at most 2(n − 1)(|U_c| − 1) per phase (Lemma FT-COUNT), and outside them κ is constant on the path-free vertices and on c's cycle every offset is constant (Remark FT-CONST); and, code-level against si.py e688b963 (= SPEC S1), S1's choice at a path-free Odd vertex is the (κ, tie-break)-minimiser of its options that are path-free or c (Lemma PF-CHOICE), so STRICT_c + TIE_c ≤ 2(n − 1)(|U_c| − 1) (Corollary TIE-CHARGE) (2026-10-26) — structural lemmas and a REDUCTION for N5 (the per-phase, per-class count of κ-changes is reduced to EXIT_x and D, both OPEN; ODDC_c is not bounded; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C84.md, checker PENDING)
- Objects (four packets reviewed as ONE unit, "the OFFMONO unit"; all frozen, unchanged during review; all four on trunk 77f2664e at
  REFEREE-2's review): P-N5-OFFMONO, docs/new/P-N5-OFFMONO-box49.md, sha1 d9705ac6cede9849d68bf9b8d0fc5c54ab6fc3c4 (l-new freeze 1f816370,
  L-NEW successor 28, Opus 5.5); add1 P-N5-OFFMONO-add, docs/new/P-N5-OFFMONO-add-box49.md, sha1 5911aba8fc4e968187523c27b4f48cdc55433b3f
  (freeze b2a78eb1, successor 29); add2 P-N5-OFFMONO-add2, docs/new/P-N5-OFFMONO-add2-box49.md, sha1 f2d123ef6ebbb71408dc25b503b78edc085cbf9a
  (freeze 6ef3dd25, successor 29); add3 P-N5-OFFMONO-add3, docs/new/P-N5-OFFMONO-add3-box49.md, sha1 b7cd0ff103ead10054c8f42f787369710f7feb40
  (freeze 8b7e2e6e, successor 29). The referees' notes are collected by the lane in docs/new/P-N5-OFFMONO-fixes-box49.md (l-new 34d176ab, sha1
  490fc7f3ff31605062ac4239c3387873c06276e9, L-NEW successor 30 as the authors' successor: F1-F14 for OFFMONO-N1..N4, OFFADD-N1..N2,
  ADD2-N1..N4, ADD3-N1..N3, N-OFF-1..9; 76 quotes checked by script, experiments/new/box49/quotecheck3.py "quotes=76 bad=0", pinned in
  experiments/new/check.sh); on trunk; repairs only, no signed statement changes. The statements below are in their repaired wording (F1,
  F2, F4, F5, F6, F7, F8, F9).
  Setting (every game): N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md, sha1 66fde9ef1726602fc0a52ca8d6d6fe8cbbcf110e) with FIX 1-4. A phase P is a
  (λ_Ξ, τ)-phase: λ_Ξ and τ are constant on it by definition; RESULTS R38 (a) Remark KEY (λ_U is a function of τ alone) is what makes these the
  joint λ-phases (N-OFF-1, F1; the packets' "λ constant, R38 (a)" is read so). Fix c, U := U_c := λ^{-1}(c), Q := the Odd vertices of out-degree
  ≥ 2; κ_t(z), s_c, κwt_c as in RESULTS R56's setting line; next_t(z) := σ_t(z) (Even), σ̄_t(z) (Odd); par_t(q) := the first vertex of Q ∖ {q} on
  q's honest play at t strictly before c, else c (q ∈ Q ∩ U ∖ {c}); off_s(q; p) := κ_s(q) − κ_s(p). The (t+1)-CHAIN of q: x_0 := q, x_{i+1} :=
  par_{t+1}(x_i), up to c. For a run J of consecutive in-phase transitions: EXIT_x := those with par_t(x) ≠ par_{t+1}(x); CYC_c := those at which
  some x ∈ Q ∩ U ∖ {c} is on an honest cycle at t; Z_t(c) := c's honest cycle at t as a sequence from c; ZCH_c := those with Z_t(c) ≠ Z_{t+1}(c);
  ZC_c := ZCH_c ∩ CYC_c. F := {(0, s_c·ℓ) : 1 ≤ ℓ ≤ n − 1}; A_t := {z ∈ U_c ∖ {c} : P(Ξ_t z) = ∅} (the PATH-FREE vertices); FT_c := the in-phase
  transitions at which some z ∈ U_c ∖ {c} has κ_t(z) ≠ κ_{t+1}(z) with κ_t(z) ∈ F or κ_{t+1}(z) ∈ F; ZC″_c := CYC_c ∩ ZCH_c ∩ FT_c. An x-PIECE
  (resp. ′, ″, ‴) is a maximal run of consecutive transitions of J none in EXIT_x ∪ CYC_c (resp. EXIT_x ∪ ZC_c, EXIT_x ∪ ZC″_c, EXIT_x);
  par(x) = p is constant on it; v_x(π) := the number of distinct values of off(x; p) on the states of π. Facts used as proof steps, not in the
  packets' to-sign tables: (CYC-ID) x ∈ U is on an honest cycle at t ⇔ x ∈ Z_t(c); (CYC-SHAPE) for v ∈ Z_t(c) ∖ {c}, κ_t(v) = (0, s_c·ℓ),
  1 ≤ ℓ ≤ n − 1; (A-F) z ∈ A_t ⇔ κ_t(z) ∈ F (REFEREE SIGNED them, REFEREE-2 checked them CORRECT; carried here as checked proof steps).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game, inside one phase, fallbacks included; no item uses (P); premises LANDED:
  SPEC S1's order (l. 30-31) and S4c; standing premise 1E-N3 in its form P1 (P-N5-FLIP §1: S1's σ̄ is Odd's pointwise optimum in G_σ; RESULTS
  R57), used through Lemma S (a) by Case L of (a) and Cases L1, L2 of (i) (OFFMONO-N3, F2); RESULTS R18 (d) Lemma S (a), every game by RESULTS
  R57 (a) (VJ); R38 (a) KEY (as read in F1); R56 setting line, (a) (Aκ), (A0κ), (M1κ), (M2κ) (resting on RESULTS R15 (a) Lemma A), (INJ), and
  (d) κ-Y-FORM_D, the minimum attained at σ̄_t(q) by R56 (d) with (Aκ) (N-OFF-4, F10); (SW) "every Even switch of N5 is to an edge of Iσ", as
  listed among RESULTS R72's landed premises. (h) only: SPEC S1 l. 33 names si.py Engine.evaluate (l. 78-205) as exact; si.py sha1
  e688b96327b7fd2770126e20bb00e459c1f18869:
  (a) Lemma OFFSET-MONO (OFFMONO §1): at an in-phase transition t → t + 1, for q ∈ Q ∩ U with q ≠ c and q on no honest cycle at t, and
      p := par_{t+1}(q): off_{t+1}(q; p) ⪰ off_t(q; p). (Step 1: backwards along q's (t+1)-play from y2 := σ̄_{t+1}(q) to p, by (Aκ), (SW), (M1κ);
      Step 2: Case N by κ-Y-FORM_D, Case L by Lemma S (a) and S1's reward order.)
  (b) Corollaries CHAIN-SUM and CHAIN-COUNT (OFFMONO §2): κ_{t+1}(q) − κ_t(q) = Σ_{i=0}^{h} [off_{t+1}(x_i; x_{i+1}) − off_t(x_i; x_{i+1})] over q's
      (t+1)-chain, every term with x_i on no honest cycle at t ⪰ (0, 0). If off(x; p) takes at most D values on every x-piece, the transitions of
      J that change κ(q) number at most |CYC_c| + Σ_{x ∈ Q ∩ U ∖ {c}} D·(|EXIT_x| + |CYC_c| + 1) (a REDUCTION to EXIT_x, CYC_c and D).
  (c) Remark Z-CONST (add1 §1): if Z_t(c) = Z_{t+1}(c), then κ_t(x) = κ_{t+1}(x) for every x on it, and for x ∈ Q on it, x ≠ c, par_t(x) = par_{t+1}(x)
      and off_t(x; par(x)) = off_{t+1}(x; par(x)).
  (d) Corollary CHAIN-COUNT′ (add1 §2): Step A (off_{t+1}(x; p) ⪰ off_t(x; p) at every level of every transition of J not in ZC_c); sum form
      |ZC_c(J)| + Σ_x (|EXIT_x| + Σ_{π′} (v_x(π′) − 1)); stated form, if v_x(π′) ≤ D on every x-piece′: |ZC_c(J)| + Σ_x D·(|EXIT_x| + |ZC_c(J)| + 1).
      Remark (i), repaired (OFFADD-N1, F5): through the SUM form CHAIN-COUNT′ implies CHAIN-COUNT (an x-piece′ is a union of x-pieces glued at
      CYC ∖ ZC transitions, so Σ_{π′}(v_x(π′) − 1) ≤ (D − 1)(#x-pieces) + |CYC_c ∖ ZC_c|); the stated form alone does not.
  (e) Lemma ZCH-COUNT and its Corollary (add1 §3; a REDUCTION in TIE_c, ODDC_c): with N := {v ∈ Z_{t+1}(c) ∖ {c} : next_{t+1}(v) ≠ next_t(v)}, a
      transition of ZCH_c is STRICT (some v ∈ N with κ_{t+1}(v) ≻ κ_t(v)), TIE (not STRICT, N ≠ ∅), CEVEN (N = ∅, c owned by Even) or ODDC (N = ∅,
      c owned by Odd; the owner, not the parity Ω(c): N-OFF-5, F7). Per phase and class |ZCH_c| ≤ (n − 1)|U_c| + TIE_c + ODDC_c; STRICT ≤
      (n − 1)(|U_c| − 1), CEVEN ≤ n − 1; at a TIE every vertex of N is Odd with κ unchanged; at an ODDC c ∈ Q and σ̄(c) changes. Corollary: with
      J = the phase, |ZC_c| ≤ |ZCH_c| ≤ (n − 1)|U_c| + TIE_c + ODDC_c.
  (f) Lemma FT-COUNT and Remark FT-CONST (add2 §1-§2): |FT_c| ≤ 2(n − 1)(|U_c| − 1) per phase and class (sharper, REFEREE's ADD2-N1, checked
      CORRECT by REFEREE-2: at most n F-touching changes per vertex, |FT_c| ≤ n(|U_c| − 1); not needed, the signed bound stands; F9). At an
      in-phase transition not in FT_c: A_t = A_{t+1}; κ_t(z) = κ_{t+1}(z) for every z ∈ A_t ∪ {c}; and for every x ∈ Z_t(c) ∩ Q, x ≠ c, with
      p := par_{t+1}(x), off_{t+1}(x; p) = off_t(x; p) (N-OFF-3, F6). No tie-break of S1 is used.
  (g) Corollary CHAIN-COUNT″ (add2 §3; a REDUCTION to EXIT_x and D): Step A″ (as Step A, outside ZC″_c); sum form |ZC″_c(J)| + Σ_x (|EXIT_x| +
      Σ_{π″} (v_x(π″) − 1)); D form |ZC″_c(J)| + Σ_x D·(|EXIT_x| + |ZC″_c(J)| + 1); |ZC″_c(J)| ≤ min(|CYC_c ∩ ZCH_c|, |FT_c|) ≤ 2(n − 1)(|U_c| − 1);
      so per phase and class κ(q)-changes ≤ 2(n − 1)(|U_c| − 1) + Σ_x D·(|EXIT_x| + 2(n − 1)(|U_c| − 1) + 1).
  (h) CODE-LEVEL, against si.py e688b963 (= SPEC S1): Lemma PF-CHOICE (add2 §4): at a state t, for Odd x ∈ A_t, σ̄_t(x) is the minimiser over y ∈
      succ(x) ∩ (A_t ∪ {c}) of (κ_t(y), tb_t(y)) lexicographically, tb_t(y) := y's index if Ω(c) is even, the index sequence of y's honest play at
      t from c's side if Ω(c) is odd. Corollary TIE-CHARGE: at an in-phase transition not in FT_c, next_{t+1}(z) = next_t(z) for every z ∈ A_t
      (the Even step with x′ := σ_{t+1}(z) ∈ U_c taken from (Aκ) at t + 1: ADD2-N2, F8); every STRICT and TIE transition lies in FT_c, so
      STRICT_c + TIE_c ≤ 2(n − 1)(|U_c| − 1). ODDC_c is not covered (add2 §4's remark, not signed).
  (i) Lemma OFFSET-MONO⁺ (add3 §1), item (a) without the honest-cycle hypothesis: for every q ∈ Q ∩ U_c with q ≠ c and p := par_{t+1}(q),
      off_{t+1}(q; p) ⪰ off_t(q; p). For q on an honest cycle at t (q ∈ Z_t(c), path-free): y2 ≠ q (a self-loop at q would make q its own
      cycle node at t + 1, against λ_Ξ constant on the phase: ADD3-N1, F4); y2's t-play meets q before c (Case L1, OFFSET-MONO's Case L) or after
      c (Case L2: strict when P(Ξ_t y2) ≠ ∅, "L2a", by Lemma S (a) and S1's reward order; by Lemma S (a), (M1κ) and (Aκ) when P(Ξ_t y2) = ∅, "L2b").
  (j) Corollary CHAIN-COUNT‴ (add3 §2; a REDUCTION to EXIT_x and D, both OPEN): for every q ∈ Q ∩ U_c ∖ {c}, the transitions of J that change
      κ(q) number at most Σ_{x ∈ Q ∩ U_c ∖ {c}} (|EXIT_x| + Σ_{x-pieces‴ π} (v_x(π) − 1)); if v_x(π) ≤ D for every x and π, at most Σ_x D·(|EXIT_x| + 1)
      (D ≥ 1 is implicit, a piece has a state; the sum forms are the sharper statements: N-OFF-6, F5).
- Not signed: OFFMONO §3-§5, add1 §4-§7, add2 §5-§7, add3 §3-§4 (READING / DATA / OPEN), as the packets asked; OFFMONO's Remarks (i), (ii)
  (READINGs; (iii) CHECKED by REFEREE); add2 §4's ODDC remark. Joint reading of add3 §3 (N-OFF-2 refined by OFFADD-N1, F5): the cycle cuts are
  no longer needed for the route; as NUMBERS, the stated / D forms of CHAIN-COUNT, CHAIN-COUNT′ and CHAIN-COUNT″ follow from CHAIN-COUNT‴'s sum
  form, the cut SUM forms of CHAIN-COUNT′ and CHAIN-COUNT″ do not (a cut sum bound is below ‴'s in 10 / 12 of 27,395 (q, J) pairs in REFEREE-2's
  data, e.g. tcS8_N9, J = 19..21: 39 against 55); those stand on their own proofs (signed). OFFMONO-N4, OFFADD-N2 and ADD2-N4 (the on-cycle
  CONJECTURE and the necessity of the cuts) are PROVED by add3's OFFSET-MONO⁺ (ADD3-N3 for the first two; REFEREE-2's §C for ADD2-N4; F3); OFFMONO's statement keeps its hypothesis as
  signed.
- Honest limits: (i) A REDUCTION, not a bound: the unit reduces the per-phase, per-class count of κ-changes to EXIT_x (exit changes) and D
  (offset values on a piece); both are OPEN and neither is addressed by the unit. ODDC_c is not bounded; ZCH-COUNT, FT-COUNT and TIE-CHARGE
  are true but no longer on the route (REFEREE-2 §4). Nothing here bounds ρ, N_ep, f, the phases or N5's running time. D is large where it
  matters: max D 69 on nep90_n40's phase against at most 72 κ-changes of one vertex (OFFMONO-N2, F13). (ii) READING (Lead), from L-SI's
  docs/si/N5-ALT-box23.md §8 (l-si 6ec0aa2b): a passive Odd READER (an appended Odd vertex o with no predecessors and edges into one class) can leave N5's run on the old vertices
  unchanged but raise L-SI's per-vertex and cut counts. REFEREE's R-N5-READER (e83fd19d; one referee): the unconditional invariance is FALSE
  (G-READ-1: S4b can move τ(o), splitting phases or cancelling a fallback; counterexample cex_reader.pg); Theorem READER-INV PROVED under (R),
  'τ(o) never moves at a transition at which τ is unchanged on the old vertices', which a dual-optimal start gives on any τ-constant stretch;
  l121reader_n41 reproduced with (R). For l121reader6_n46, (R) was not checked by a referee (READ-N2); L-SI's orcheck.py finds the run SAME
  and the phases equal there (DATA). On
  experiments/si/root/instances/l121reader6_n46.pg (sha1 29d2c84203f97bc247986d0af90778c5194d65a7, start
  7c6897065a63ce81e43c2355ac20980c81a3b515; long121_n40 plus six two-option readers, run on the old 40 vertices SAME) L-SI's exit-change count
  at cuts (its "EXIT_x") goes 23 → 41 (one reader) → 57 (six readers), its C-cuts K 53 → 57 → 73. L-SI's §8 concludes that bounding K(S) or ALT
  polynomially is at least as hard as bounding the phase length; the Lead reads the same for EXIT_x (READING, not proved: that L-SI's count is
  the unit's EXIT_x is not checked here), so the unit's reduction need not make the problem smaller (a phase is τ-constant, so REFEREE's Corollary, a dual-optimal start per
  τ-constant stretch, covers a whole phase: the reading is per phase, the unit's own scope). Related: CONJECTURE XR-LIN ("in every
  phase, every vertex's Ξ changes ≤ 2n times") is DEAD (L-SI, same §8): experiments/si/root/instances/l121reader_n41.pg (sha1
  084da8cd47707b8937ebe30fdfae88d3d988bdaf, start 7ca283c43b7092acc454c5ffc6b1995e3a29bf68), Ξ(o) changes 86 times in the phase [1, 122], > 2n =
  82; reproduced by a second engine (L-COMP experiments/xr-lin/, l-comp eabb3018: n5b SPEC only, run on 0..39 = long121_n40, phases equal,
  86, Oink zlk OK). (iii) Thin spots: Case L2a of (i) is exercised twice, both in REFEREE-2's saved instances docs/referee-2/R2-N5-OFFMONO/l2a/
  (r1814_6302_0.pg sha1 9c575fc9, r1813_619_1.pg sha1 fd6d95a4), strictly, and never in the lane's or REFEREE's data (0 of 9,390); Case L1 once in
  each referee's data (REFEREE: harm_n12_seed412, sha1 5282c3f1; REFEREE-2: once in its lib41 runs), never in the lane's (ADD3-N2 corrected by
  N-OFF-7, F12). The cycle cuts ZC_c, ZC″_c never bite in data (now explained by OFFSET-MONO⁺); FT-COUNT's factor 2 is never needed. (iv) (h) is
  CODE-LEVEL: it holds for si.py at e688b963, which SPEC S1 names as exact; si.py was executed only as the object, never as a checker (ADD2-N3).
- Data (DATA, not proof): REFEREE (successor 15 for OFFMONO and add1, successor 16 for add2 and add3; own engine rl_engine; lane code not run):
  OFFMONO (offmono_probe.py): library n ≤ 40 (870 files, 2,610 runs) 30,635 OFFSET-MONO checks (Case L 117), STEP1 112,498, CHAIN-SUM 34,641;
  3,000 random games (15,000 runs) 7,619; the lane's start files 455 / 390 / 363 (exact), parent changes 53 / 60 / 48 (OFFMONO-N1, F11);
  MUT=1 (p := par_t) 490 of 1,769, MUT=2 (opposite length sign) 1,308, MUT=3 (admit on-cycle q) 0 of 4,006. add1 (zch_probe.py): Z-CONST
  29,793 + 11,601; ZCH STRICT / TIE / CEVEN / ODDC 183 / 8 / 291 / 5 and 331 / 8 / 952 / 13; 806 + 565 ZC checks, 0 offset falls; MUT=1 (no ZC cut)
  0, MUT=2 Step A 1,271, MUT=3 (no EXIT cut) PM 422. add2 (add2_probe.py, 112,872 runs): si.py and rl_engine give the same (Ξ, σ̄) at 75,525
  states; PF-CHOICE at 29,141 pairs on both engines (1,506 κ-tied) plus 39,787 on rl_engine only (2,740 tied); TIE-CHARGE 62,181 checks, all
  1,184 STRICT and 36 TIE transitions in FT_c; ZC″ 1,054 cut checks, 0 falls; at most 7 F-touching changes per vertex per phase; MUT=1
  (reversed tie-break) 568, MUT=2 (FT-CONST asked at FT_c) 1,157 / 1,485 / 330. add3 (add3_probe.py, 103,872 runs): 9,390 on-cycle checks (L1 1,
  L2a 0, L2b 9,389); MUT=1 361 / 1,780, MUT=2 59 / 472. REFEREE-2 (successor 18, own offmono_check.py on its SPEC loop over si.py; lane code
  not run): 23,959 runs, 142,287 (phase, class) pairs; OFFSET-MONO 69,881 checks (Case L 138) and 44,966 more in the thin-spot search;
  OFFSET-MONO⁺ 4,049 (L1 1, L2 4,048 all with P(Ξ_t y2) = ∅) + 13,890 thin-spot (L2a 2, L1 0); CHAIN-SUM 73,930; Z-CONST 38,639; ZCH 1,562
  transitions (STRICT 459, TIE 14, CEVEN 1,060, ODDC 29); FT-COUNT 142,287 / FT-CONST 34,281; PF-CHOICE 315,088 (128,674 with ≥ 2 options);
  CHAIN-COUNT / ′ / ″ / ‴ 27,395 (q, J) pairs per form (cuts CYC 3,181, ZC 729, ZC″ 331), ‴'s sum form tight in 2,857; 0 violations of every
  check; controls bite (opposite sign 2,756; p := par_t 1,358; no EXIT cut 904; tie-break mutations 2,585 / 13,369 / 645), CTL_ft1 0. Both
  reproduce the lane's 455 / 390 / 363 checks and Case L 2 on long121_n40.
- Signatures: REFEREE docs/referee/R-N5-OFFMONO.md (report 04a563d3, successor 15): OFFSET-MONO, CHAIN-SUM, CHAIN-COUNT (as a REDUCTION)
  SIGNED, no gap; notes OFFMONO-N1..N4. R-N5-OFFMONO-add.md (c2a97189, successor 15): (CYC-ID), (CYC-SHAPE), Z-CONST, CHAIN-COUNT′ (Step A,
  both forms), ZCH-COUNT and its Corollary (as a REDUCTION) SIGNED, no gap; notes OFFADD-N1..N2. R-N5-OFFMONO-add2.md (d6e07396, stamp
  ff99f1f5, successor 16): (A-F), FT-COUNT, FT-CONST, CHAIN-COUNT″, PF-CHOICE and TIE-CHARGE (code-level) SIGNED, no gap; notes ADD2-N1..N4.
  R-N5-OFFMONO-add3.md (907e21b9, stamp d1a22e18, successor 16): OFFSET-MONO⁺, CHAIN-COUNT‴ SIGNED, no gap; notes ADD3-N1..N3. Unit §C at the
  end of R-N5-OFFMONO.md (96b2cd9a, successor 16; pointers in the three addendum reports). REFEREE-2 docs/referee-2/R2-N5-OFFMONO.md (report
  4e9a6372, §C c040084a, successor 18): every to-sign item of the four files SIGN, no gap; (CYC-ID), (CYC-SHAPE), (A-F) CORRECT; notes
  N-OFF-1..9. §C (both): verdicts identical; joint gap map EMPTY. N-OFF-1 (KEY's clause is about λ_U) ACCEPTED by REFEREE (F1); OFFMONO-N3
  matches REFEREE-2's premise column (F2); OFFMONO-N4, OFFADD-N2, ADD2-N4 PROVED by add3 (F3); ADD3-N1 agreed (F4); N-OFF-2 refined by
  OFFADD-N1, REFEREE withdrawing its add3 "follow" wording, N-OFF-6 compatible (F5); N-OFF-3, N-OFF-4, N-OFF-5 ACCEPTED by REFEREE (F6, F10,
  F7); ADD2-N2 consistent with REFEREE-2's step (F8); ADD2-N1 accepted by REFEREE-2, CORRECT (F9); OFFMONO-N1 confirmed by REFEREE-2, 53 / 60 / 48
  (F11); ADD3-N2 CORRECTED by N-OFF-7: L2a exercised twice (F12); OFFMONO-N2, N-OFF-8, ADD2-N3 data / method (F13); N-OFF-9 independence
  record (F14); nothing open. Quotes: all verbatim (REFEREE 12 / 15 / 23 / 9; REFEREE-2 55 / 55 after its §C, counting add1 12, add2 22). Both under the standing premise 1E-N3 (P1).
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas and a per-phase reduction; no iteration bound, no algorithm
  claim). GAPS G-N5-TIME: open.
