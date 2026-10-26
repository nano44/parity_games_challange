# Draft RESULTS R73 (Lead, 2026-10-26 18:10Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C82

### R73 [refereed-only] N5 on EVERY game: after an in-phase fallback, every configuration C finds its honest level LEV_C at least min(LEV_C(t) + 1, n − 1) at each of its later C-states (Lemma RET-FB), so a configuration has at most 2n² − n epochs per phase besides its fallback-free returns R⁰_C (Corollary VIS) and N_ep ≤ NCONF·(2n² − n) + R⁰ (Theorem EP-C); a fallback from a saturated C-state ends the phase or is followed by no further C-state of the phase (Lemma SAT-FB), so at most one saturated fallback per configuration and f ≤ n·|𝒞_f(P)| per phase (Corollary SAT-FB1, Theorem FB-C′); and N_ep ≤ (4n² − 3n) + N_1 + NCONF_{≥2}·(2n² − n) + R⁰_{≥2}, with N_1 bounded only as an implication from (Στ) (Corollary EP-ASM) (2026-10-26) — a REDUCTION of the epoch count N_ep to four open quantities X_dir, X_big, NCONF_{≥2}, R⁰_{≥2} (none bounded here; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C82.md, checker PENDING)
- Object (packet P-N5-EPC, added at l-new 81ab0b72, pinned trunk e57ba8cb, quote base f4562054, unchanged during review):
  docs/new/P-N5-EPC-box48.md, sha1 9f48ded742d7f44bbf82ae8ec9e0e88c46457700 (L-NEW successor 27, Opus 5.5). The referees' notes are collected
  by the lane in docs/new/P-N5-EPC-fixes-box48.md (l-new c6a5d467, sha1 174aedd5de766a3f69a90c70cf2bfc1601956763, L-NEW successor 29: R1-R6 for
  EPC-N1..N3 and N-EPC-1..3; remarks for N-EPC-4, EPC-N4 = N-EPC-5; §5 DATA on non-flat saturated fallbacks; 41 quotes checked by script); on
  trunk; repairs only, no signed statement changes.
  Setting (every game): as in RESULTS R71 (N5 = SPEC S1-S5; Ξ_k the value of the honest play; phases (RESULTS R38 (a)); λ; value(r); f; Q;
  configurations C = σ̄|Q, C-states, H_C, LEV_C, B_C, 𝒞_f(P)); LEV_C ≥ 0 at every state of the phase (fixes R1 = EPC-N1, as in R71's setting).
  An EPOCH is a maximal run of the phase with σ̄|Q constant (RESULTS R64), N_ep its number, D_E := {q ∈ Q : σ̄_E(q) ≠ τ(q)}, and D_C := {q ∈ Q :
  C(q) ≠ τ(q)} for a configuration (fixes R5 = N-EPC-2); NCONF(P) := the distinct configurations of P's states, NCONF_{≥2}(P) := those with
  |D_C| ≥ 2. For a configuration C with epochs E_1 < … < E_V (V = V_C), a RETURN is a pair (i, i + 1); R⁰_C := its returns (i, i + 1) with no in-phase fallback source in [s_i, s_{i+1}) and LEV_C(s_i) ≤ n − 2 (s_i the first state of E_i);
  R⁰ := Σ_C R⁰_C, R⁰_{≥2} := Σ_{|D_C| ≥ 2} R⁰_C; REV(S) := (epoch starts in S) − (distinct configurations among them), per maximal
  fallback-free run S.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S2, S4a ("Else σ_new = σ."),
  S4b, S4c, S5, FIX 3; the standing premise 1E-N3 (P1) with RESULTS R57 (a) (VJ); RESULTS R15 (a), (d) ((MON)); R17 (a) (V1), (V2), R17 (b)
  Lemma P's Case A with Ω := Ξ_t (RESULTS R70's Q-A, YES by both); R38 (a); R64 (the epoch); RESULTS R70 (FB-RISE (a)'s items 2-3,
  HON-0-FF (b), REC-1-FF (c)); RESULTS R68 (X_dir, X_big, T*_Q, (Στ)); RESULTS R71 (a), (b) (FB-RISE_C, SAT_C). The packet's §1 restates
  FB-RISE_C and SAT_C with their proofs; both referees signed the restatement as identical to RESULTS R71 (a), (b), and it is not re-landed
  here. SAT-FB's last step reads S4a / S4b / S4c / S5 and FIX 3 directly; the packet's citation of R68's HON-FB (iv) is a cross-reference only
  (fixes R6 = N-EPC-3, both referees):
  (a) Lemma RET-FB: if t → t + 1 is an in-phase S4c fallback of P, then for EVERY configuration C and every C-state s ≥ t + 1 of P,
      LEV_C(s) ≥ min(LEV_C(t) + 1, n − 1). The induction is on |r| at the fixed C-state s, and only its Odd branch calls the hypothesis
      (fixes R2 = EPC-N2); its Even step holds in every frame H_C at once (N-EPC-4, REFEREE-2; accepted by REFEREE).
  (b) Corollary VIS: per phase and configuration, V_C ≤ 2n² − n + R⁰_C (returns of kind (a), after saturation, ≤ 2n(n − 1); of kind (b) ≤ n − 1).
  (c) Theorem EP-C: N_ep(P) ≤ NCONF(P)·(2n² − n) + R⁰(P), and R⁰ ≤ Σ_S REV(S) over the ≤ f + 1 fallback-free runs S of P.
  (d) Lemma SAT-FB: if an in-phase fallback has a saturated C-state source t, then t + 1 is the last state of P or P has no C-state after t,
      by SAT_C (b), S2 and S4c's (Ξ_t(w), w)-maximum (a Ξ-flat fallback leaves Iσ_{t+1} = ∅) and S4a / S4b / S4c / S5. Corollary SAT-FB1: per
      phase and configuration, at most one in-phase fallback has a saturated C-state source. Theorem FB-C′: f ≤ n·|𝒞_f(P)| per phase; hence
      f ≤ n·N_ep (implying RESULTS R60 (c)), f ≤ n·Δ^k on 𝒞^kO with maximum out-degree Δ, and f ≤ n(1 + m) when every |D_k| ≤ 1 (with RESULTS
      R71 (d)'s counts). FB-C′'s proof stands without REFEREE's FBC-N3 route (no R15 (b), no R38 (f) CN-LAST): both referees, in answer to
      the Lead's question; FBC-N3 (REFEREE's note on R71) reaches the same conclusion by another route.
  (e) Corollary EP-ASM: N_ep(P) ≤ (4n² − 3n) + (1 + 4n² − 3n + X_dir + X_big)(T*_Q + 2) + NCONF_{≥2}(P)·(2n² − n) + R⁰_{≥2}(P), signed as an
      assembly, its second term (the |D_E| = 1 epochs N_1, by RESULTS R70 REC-1-FF (c)) signed AS AN IMPLICATION from (Στ). Term by term
      (REFEREE §4, both): 4n² − 3n bounds N_0 unconditionally (R70 HON-0-FF (b)); the N_1 term is an implication, with T*_Q (RESULTS R51 (a))
      polynomial but very large and X_dir, X_big OPEN; the factor 2n² − n is proved (VIS) and NCONF_{≥2} is OPEN; R⁰_{≥2} is OPEN. The packet's
      statement line should name these four open terms (fixes R3 = EPC-N3).
  (f) Remark: (D changes) + 1 ≤ N_ep (τ fixed on the phase).
- Not signed (packet §6): the data, the OPEN items and the READINGs, including CONJECTURE SAT-1 (no C-epoch after a saturated C-state, which
  would make VIS's kind (a) zero; SAT-FB1 bounds saturated fallbacks, not epochs: EPC-N4). The packet's §5 DEAD item ("a fallback from a saturated
  C-state is flat and ends the phase") is CONFIRMED DEAD by both referees on their own runs (rho3_253_n32; cond_stuck_symsi3_YE).
- Honest limits: (i) A REDUCTION: EP-C and EP-ASM bound N_ep only in terms of NCONF_{≥2}, R⁰_{≥2}, X_dir, X_big (and premise (Στ) for N_1); none
  is bounded here, on any class. (ii) VIS's kind-(a) term 2n(n − 1) is never exercised: no return after saturation occurs in either referee's
  data (EPC-N4 = N-EPC-5); REFEREE-2's "VIS without R⁰" control does not bite. (iii) Fallback-free returns are most returns (REFEREE-2: R⁰ 729 of
  its 1,340 returns, N-EPC-6; REFEREE: 124 of 155 at n ≤ 20, 272 of 370 at n ≤ 34): R⁰ is exactly the term left open. (iv) Over-budget
  configurations: REFEREE-2 1,102 (phases containing one skipped for EP-C / EP-ASM); REFEREE 144 UNK phases in its n ≤ 34 row; the n = 40
  lane instances were checked at depth cap 16, decided checks only. (v) Non-flat saturated fallbacks: REFEREE sees 5 of 236 (n ≤ 20) and 11 of
  178 (n ≤ 34) in its library, REFEREE-2 none in its library (0 of 43) but 25 of 25 on its named instances; the instance lists differ (DATA,
  fixes §5; both §Cs).
- Data (DATA, not proof): REFEREE (successor 15, own epc_probe.py, exact LEV_C for every configuration visited, with a path budget; lane code
  not run): 20,753 runs (the library at n ≤ 20 and n ≤ 34, 3,000 random games with ≤ 8 Odd choice vertices, rho3_253_n32 at 32 starts, and
  long121_n40, nep90_n40, nep76_n40 at depth cap 16); RET-FB checked at every later C-state for every configuration; 0 failures of every
  check; reproduces long121 (N_ep 37, NCONF 14), nep90 (90, 48), nep76 (76, 40); mutations MUT=1 (RET-FB + 2) 247 + 82 on long121, MUT=2 (RET-FB
  at non-C states) 251, MUT=3 (the DEAD guess) 1 + 7 failures. REFEREE-2 (successor 17, own epc_check.py with a deep mode; lane code not run):
  21,753 runs (named instances, lib41, its 503 𝒞^1O files, random games with 2, 4 and all Odd choice vertices); RET-FB 25,065 checks (10,200
  across configurations), its Even step 7,126, VIS on 1,340 returns, EP-C on 59,553 phases, SAT-FB / SAT-FB1 on 713 saturated fallbacks,
  Iσ_{t+1} = ∅ and "last state" at all 734 Ξ-flat fallbacks; 0 violations; same three reproductions; controls plus2 609, nonC 11,424, last
  21 failures, noR0 0 (does not bite).
- Signatures: REFEREE docs/referee/R-N5-EPC.md (referee a52feb43, data addendum 58fd9535, §C cd4795f8, successor 15): every item SIGNED, EP-ASM
  as an assembly with its second term as an implication, §5 DEAD CONFIRMED, no gap; FB-C′ stands without FBC-N3; notes EPC-N1..N4. REFEREE-2
  docs/referee-2/R2-N5-EPC.md (referee-2 62b72f6e, §C c4975512, successor 17): every item SIGN, EP-ASM likewise, DEAD CONFIRMED, no gap; the
  same answer on FB-C′; notes N-EPC-1..6. §C (both): verdicts identical; joint gap map empty; EPC-N4 = N-EPC-5; EPC-N3 compatible with N-EPC-6;
  N-EPC-1..4 accepted by REFEREE; EPC-N1..N4 accepted by REFEREE-2; the non-flat saturated fallback counts differ by instance list only;
  nothing open. Both under the standing premise 1E-N3 (P1) and RESULTS R70's Q-A.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (per-phase reductions; no running-time bound). GAPS G-N5-TIME: open.
