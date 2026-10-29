# Draft RESULTS R80 (Lead, 2026-10-29 00:45Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C89 (Lead reviewed 00:51Z by date -u: title date set to the packet's freeze date 2026-10-28; N-CORE-1 kept as Referee strengthening (REFEREE 'ACCEPTED, re-derived', not 'SIGNED')) (rev. 01:10Z by date -u: C89 N-1, N-2) — LANDED in RESULTS Results 2026-10-29 01:25Z (CHECKER C89 Add. 1 3f849b3a PASS), after R79

### R80 [refereed-only] N5 on EVERY game, inside one phase: every transition of a phase changes Even's σ (Lemma EVERY-SWITCH), so a phase P has |P| ≤ Σ_w SW_P(w), |P| the number of TRANSITIONS of P and SW_P(w) the number of those at which σ(w) changes (PHASE-SW; FALSE if |P| counts states); an Even vertex w that switches at a transition t → t + 1 of a phase and lies on no honest cycle at t and at t + 1 strictly raises Ξ(w) (Lemma RISE-SW), so |P| ≤ Σ_w XR_P(w) + #{(w, t) : w switches at t and lies on an honest cycle at t or t + 1}, XR_P(w) the transitions of P at which Ξ(w) changes (its Consequence); a CLEAN change y1 → y2 of σ̄ at an Odd choice vertex u ∈ U_c ∖ {c} of class c, u on no honest cycle at t and at t + 1, gives κ_{t+1}(y1) ⪰ κ_t(y1), strictly unless κ_{t+1}(y1) = κ_{t+1}(y2) (Lemma RISE-GATE-CLEAN; the tie exception is needed, nep22f_n64); a set I of consecutive transitions of one phase has |I| ≤ m_E + NOFRESH(I) (FRESH-RED); and on a global C-interval (RESULTS R76's definition, taken inside one phase) the transitions with a fresh Even edge, with a fresh Odd option and with a strict shrink of some A number at most m_E, Σ_{Odd u} (deg(u) − 1) and Σ_c |A_a(U_c)| ≤ n (FRESH3-COUNT) (2026-10-28) — elementary structural lemmas for N5 (they bound nothing: no count of switches or Ξ-changes per vertex, no NOFRESH and no phase length is bounded; the per-vertex forms SW-LIN and XR-LIN are DEAD; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C89.md, checker PENDING)
- Object (L-SI successor 19, Opus 5.5; frozen, unchanged during review): packet P-N5-CORE, docs/si/P-N5-CORE-box23.md, sha1
  7b66f1bae1a1b675c0fda0af1e5eaabf13f128a0 (l-si freeze 081ae740; quote base 33f43c20; 10 quotes), the §11 PROVED core (C1)-(C6) of
  docs/si/N5-ALT-box23.md. The referees' notes are collected by the lane in docs/si/P-N5-CORE-fixes-box23.md (l-si 5533c58c, sha1
  5f22c9ecd534bcf041f9f0672d842b643faf90e2, L-SI successor 20: F1-F7 for CORE-N1, CORE-N2 (a)-(c), N-CORE-1, CORE-N3 = N-CORE-4, CORE-N4 =
  N-CORE-2, N-CORE-3, and the records N-CORE-5, N-CORE-6, CORE-N5, CORE-N6; 35 quotes checked by script, experiments/si/rund/quotecheck.py
  "quotes=35 bad=0", pinned in experiments/si/check.sh with a shifted-line control that must fail); on trunk; repairs only: F1 adds the
  definition of |P| (CORE-N1), F2 corrects three citations, F4 replaces (C6)'s premise by RESULTS R76's landed definition and states the
  scope, F5 adds a remark (the tie exception is needed), F6 and F7 change no statement. F3 widens (C3) to every N5 transition (N-CORE-1);
  that widening is NOT part of this entry (bullet "Referee strengthening"). The statements below are in the repaired wording otherwise.
  Setting (every game): N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) with FIX 1-4 and the standing premise 1E-N3; state t = (σ_t, τ_t); Ξ_t
  := Ξσ_t, the valuation of σ_t against S1's Odd counterstrategy σ̄_t, Ξ_t(v) the value of v's honest (σ_t, σ̄_t)-play; ▷, ⊵ the S1 order;
  λ := Ξ's cycle-node map. A PHASE: a maximal run of states with λ_Ξ and τ constant (RESULTS R38 (a) KEY: the (λ_Ξ, τ)-phase is the joint
  λ-phase); a transition t → t+1 of a phase P joins two states of P; |P| := the number of transitions of P (pairs t → t+1 of consecutive
  states of P), so a phase with s states has |P| = s − 1 (F1). SW_P(w) := the transitions of P at which σ(w) changes; XR_P(w) := those at
  which Ξ(w) changes. Per honest class c, U_c := λ^{-1}(c); Q := the Odd vertices of out-degree ≥ 2; κ, κwt_c, Y^q_t as in RESULTS R56's
  setting and (d). A σ̄ change y1 := σ̄_t(u) ≠ y2 := σ̄_{t+1}(u) is CLEAN if y2 ∈ Y^u_t and y1 ∈ Y^u_{t+1}. For a set I of consecutive
  transitions of one phase, t → t+1 ∈ I is FRESH if some Even w switches at it to an edge (w, y) that w held at no earlier state of I (the
  first state of I included); NOFRESH(I) := the other transitions of I; m_E := the number of Even edges. GLOBAL C-INTERVAL: RESULTS R76's
  definition (a maximal run of GOOD transitions: for every c, A_{t+1} ⊆ A_t, D_{t+1} = D_t, DD_{t+1} = DD_t and Δ_{t+1}(u) = Δ_t(u) on DD_t;
  transition-local reading), taken inside one phase (R76 takes it inside a fallback-free run S; (C6) holds in both scopes, both referees
  checked both; F4); A_a(U_c) is A of U_c at the interval's first state a.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S1, S2, S4 (a)-(d) with
  FIX 1-4; RESULTS R15 (a) Lemma A and (d) (cited in full, F2 (a): «(d) N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ
  (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and» …; used with τ fixed); RESULTS R17 (a) (V1) for Ξ(v) = v ⊕ Ξ(next v) off v's
  play's cycle (F2 (b)); (SW) "every Even switch of N5 is to an edge of Iσ", as listed among RESULTS R72's landed premises; RESULTS R38 (a)
  KEY (only for the remark that a (λ_Ξ, τ)-phase is a joint λ-phase; τ constant is the phase definition, F2 (c)); RESULTS R56 (a) (Aκ),
  (M1κ), (M2κ) and (d) κ-Y-FORM_D; RESULTS R76 (the global C-interval definition only; CORE-N3 = N-CORE-4, F4):
  (a) (C1) EVERY-SWITCH (§2): at every transition t → t+1 of a phase, σ_{t+1} ≠ σ_t. (τ_{t+1} = τ_t by the definition of a phase; a
      non-fallback iteration changes (σ, τ); an Even fallback moves every Even vertex with an improving edge, to w ≠ σ(v) by S2; an Odd
      fallback changes τ and so cannot occur inside a phase.)
  (b) (C2) PHASE-SW (§2, with F1): for a phase P, |P| ≤ Σ_w SW_P(w), |P| the number of TRANSITIONS of P.
  (c) (C3) RISE-SW (§3, with F2): let t → t+1 be a transition of a phase and w an Even vertex with y := σ_{t+1}(w) ≠ σ_t(w), w on no honest
      cycle at t and at t + 1. Then Ξ_{t+1}(w) ▷ Ξ_t(w). Remark: the order of the steps matters (Ξ_t(y) may be the value of a play through
      w; the proof compares Ξ_{t+1}(y) ▷ Ξ_t(σ_t w), two w-free values with cycle node λ(w), and only then applies w ⊕). Consequence (with
      (b)): |P| ≤ Σ_w XR_P(w) + #{(w, t) : w switches at t and lies on an honest cycle at t or t + 1}.
  (d) (C4) RISE-GATE-CLEAN (§4): let t → t+1 be a transition of a phase, c a class, u ∈ Q ∩ U_c, u ≠ c, on no honest cycle at t and at
      t + 1, with a CLEAN change y1 := σ̄_t(u) ≠ y2 := σ̄_{t+1}(u). Then κ_{t+1}(y1) ⪰ κ_t(y1), strictly unless κ_{t+1}(y1) = κ_{t+1}(y2).
      (Chain κ_t(y1) ⪯ κ_t(y2) ⪯ κ_{t+1}(y2) ⪯ κ_{t+1}(y1) by (Aκ) and κ-Y-FORM_D at t and t + 1 and (M2κ) at y2.) Its two closing
      sentences: ties at t + 1 aside, a clean σ̄ change at u is a strict Ξ-rise of the abandoned option y1 at the same transition ((M1κ));
      each such rise of y1 at t is charged by at most the number of Odd u with σ̄_t(u) = y1. Remark (F5; CORE-N4 = N-CORE-2): the tie
      exception cannot be dropped: nep22f_n64 (sha1 d98de59f…, its .start in experiments/n5-epoch/instances/, sha1 a7ecb00e…), transition
      8 → 9 (a fallback), class 18, gates 9 (57 → 30) and 56 (6 → 1), both clean, all four κ = (0, 4) at t and t + 1 (found independently
      by both referees, two engines).
  (e) (C5) FRESH-RED (§5): for a set I of consecutive transitions of one phase, |I| ≤ m_E + NOFRESH(I) (fresh transitions map injectively
      to fresh Even edges); with (a), the non-fresh transitions of I are exactly those at which every switching Even vertex returns to an
      edge it held before in I.
  (f) (C6) FRESH3-COUNT (§5, with F4): on a global C-interval I = [a, b]: the transitions with a fresh Even edge (in I's scope) number
      ≤ m_E; those at which some Odd vertex moves σ̄ to an option it did not hold at an earlier state of I number ≤ Σ_{Odd u} (deg(u) − 1);
      those with A_{t+1} ⊊ A_t for some class number ≤ Σ_c |A_a(U_c)| ≤ n. (Of goodness only "A non-increasing" is used, REFEREE §4,
      accepted by REFEREE-2.)
- Not signed: (C2) and (C3)'s Consequence with |P| read as the number of STATES of P (the packet's §1 calls a phase a run of states and
  did not define |P|): FALSE, every one-state phase has |P| = 1 > 0 = Σ_w SW_P(w) (CORE-N1; REFEREE: 13,932 of 16,595 phases of lib1140;
  REFEREE-2: 2,098 one-state phases in alt_all); repaired by F1. (C4) without its tie exception ("strictly"): FALSE (nep22f_n64, above).
  The packet's §6 (not to sign, as the packet says): the DATA; the UNCLEAN gate change (N5-ALT §1 RISE-GATE, through Fact CL of P-N5-OFFMONO
  §1); the conjecture FRESH3 (every σ̄-changing in-interval transition has one of (f)'s three events), DEAD (ret14_n48, N5-ALT §3; REFEREE
  reproduces 4 failures of 1,379 in alt_all, CORE-N6); the DEAD per-vertex forms XR-LIN and SW-LIN; the READING on passive readers.
- Referee strengthening (NOT part of this entry; N-CORE-1: in REFEREE-2's (C3) verdict line as an addition, not in REFEREE's verdict table): (C3) RISE-SW at EVERY N5 transition, in a
  phase or not (fixes F3 writes it into (C3)'s statement). REFEREE-2 states and proves it in its report (verdict line of (C3), "Also true at
  every N5 transition, not only in-phase ones (N-CORE-1)"; §3: if the cycle nodes at t and t + 1 differ, the two values compare by the
  cycle node's reward, which w ⊕ does not change; data XC3, 0 failures off-cycle) and calls it in its §C "mine alone; it is an extension and
  changes no verdict"; REFEREE in its §C: "ACCEPTED, re-derived" (steps 1-2 of its §2 hold at every iteration, w-freeness needs only "off
  honest cycles at t and t + 1", same cycle node → step 5, different → reward), not entered as a SIGNED verdict ("Verdicts identical:
  (C1)-(C6) all SIGNED by both"). Also not signed as a bound: m_E − n_E in (e) and (f)'s first count (N-CORE-3; REFEREE "could be m_E − n_E
  ... Not needed"; F6 keeps m_E; REFEREE-2's control X5nE shows it cannot be lowered to n_E, 344 in alt_all).
- Honest limits: (i) It bounds nothing. (b), (c)'s Consequence, (e) and (f) move |P| or |I| onto SW_P, XR_P, the on-cycle switch pairs and
  NOFRESH, none of which is bounded here; (f) counts three events but FRESH3 is DEAD, so some σ̄-changing transitions of a global C-interval
  carry none of them. (ii) READING (Lead): the PROVED (C2)-type bound |P| ≤ Σ_w SW_P(w) is reader-inflatable per vertex: some passive Even
  readers (those that keep the run SAME; not every Even reader does, N5-ALT §12's CORRECTION) raise one vertex's SW, and Σ_w SW_P(w), without
  changing the run (docs/si/N5-ALT-box23.md §12, l-si 3cb6035b, corrected 992e3bb0: on long121_n40's phase [1, 122] the most switches
  of one Even vertex is 12, and an appended Even reader switches 16 times with the run SAME, instance l121ereader_n41); the transition count |P| is intrinsic. CONJECTURE SW-LIN ("in every phase, every Even vertex switches
  ≤ n times") is DEAD (l-si 85709361, swlin_kill_n26: one Even vertex switches 27 > n = 26 in one phase; L-COMP's n5b agrees), and
  CONJECTURE RUN-LIN (every fallback-free run of a phase has ≤ 2n transitions) is DEAD (runfam_K10, n = 49: a fallback-free run of 99 > 2n =
  98 transitions; L-SI 51281c00, docs/si/N5-RUNLIN-box24.md §7 at l-si 90bcc50c; reproduced by REFEREE, docs/referee/R-N5-RUNLIN-kill.md
  c609f779). So (b) and (c)'s Consequence are not completed by a linear per-vertex bound. (iii) Every hypothesis is needed in data:
  (a) fails at phase-leaving transitions (τ-only moves; REFEREE MUT3 4 of 52, e.g. swlin_kill_n26 at its given start, transition 48;
  REFEREE-2 X1 435 / 939 / 2,789 on alt_all / lib41 / random k2); (c)'s off-cycle hypothesis (on-cycle switches without a Ξ(w) rise:
  REFEREE alt_all 73 of 128, lib1140 328 of 615; REFEREE-2 X3cyc 38 / 89 / 328); (d)'s tie exception (nep22f_n64); (e)'s NOFRESH term
  (REFEREE MUT6: 40 failures of |I| ≤ m_E on l121reader_n41, a 121-transition phase, m_E = 103); (f)'s goodness (REFEREE-2 X6A 26 / 34 and
  X6Ax 201 / 472 on alt_all / lib41; REFEREE's MUT4 did not bite on its corpus). (iv) (d) is for CLEAN changes only; the unclean case is not
  claimed (REFEREE-2 saw (d)'s conclusion hold at every unclean change it checked, DATA). (v) NOFRESH is not small over a phase: the packet's
  §6 "≤ 22 per run" holds per fallback-free run (fresh.py's unit; F7, N-CORE-6); over whole phases it reaches 90 (long121_n40 and
  l121ereader_n41 [1, 122], both referees), and 115 in one fallback-free run on the RUN-LIN family (runfam_K40, L-SI's experiments/si/runlin/anatomy.py; fixes F7). Nothing here bounds N5's running time.
- Data (DATA, not proof): REFEREE (successor 17; own scratch/core_probe.py (sha1 be6bb900…) on its engine rl_engine, written from SPEC S1-S5
  + FIX 1-4; lane code not run; 0 failures in every MUT=0 run): alt_all (413 games of root/logs/alt_all.lst, n ≤ 600; 918 runs: given start
  when valid, best-reward, 1 random) 12,937 in-phase transitions, (C3) 27,194 checks, (C4) 4,953 clean / 1,764 unclean / 29 ties at t + 1 /
  2 without a rise, (C5) 98,053 intervals, (C6) 1,891 / 1,874 intervals (phase / fallback-free scope); lib41 (349 games, 698 runs) 9,059
  transitions; lib1140 (1,024 games, 3,072 runs) 22,018 transitions, (C3) 40,019, (C4) 3,195 clean; rand3000 (6,000 runs) and MUT=2 random
  sets (48,000 games, 96,000 runs). Premise checks at every state: (V1), (SW), R15 pointwise monotonicity, (C3)'s steps separately, (Aκ)
  and κ-Y-FORM_D at both ends, (M2κ) at y2, 0 failures. Controls: MUT1 ((C3) demanded of the abandoned option) bites 579 on its 4-instance
  set; MUT2 ((C4) strict) bites 2 (nep22f_n64); MUT3, MUT6 above; MUT4, MUT5 do not bite. REFEREE-2 (successor 19; own
  docs/referee-2/R2-N5-CORE/core_check.py and qcheck.py on its lane's Runner (si.py); lane tools not run; every run 0 violations): alt_all
  (413 runs, given start else S3) 458 phases (its phase count; 2,098 one-state phases besides), 8,048 in-phase transitions (729 fallbacks),
  (C3) 16,825, (C4) 3,071 clean / 1,075 unclean, (C5) 86,519 intervals, (C6) 1,187 (1,172 in GCX's scope S); lib41_noref × 3 starts
  (1,230 runs) 12,135 transitions; named (8 runs) 537; random k2 / kO / k5 (9,000 / 4,500 / 800 runs); RULE=rand (any non-empty subset of
  Iσ, lib41 × 3, 1,230 runs, 14,822 transitions): (C3)-(C5) hold, 0 violations. Engine Ξ equals the play value at every state (ENGXI, 0
  differences). Counts differ from the packet's §6 (alt_all 8,048 against 8,084 in-phase transitions; cause unknown on both sides, no
  violation on either; N-CORE-5) and from REFEREE's (extra starts). CORE-N5: three start files in alt_all.lst (L-RED's comp54_n80,
  n3cov_lean, n3cov_phi under experiments/red/n3/instances/) do not fit their games or are partial; REFEREE skipped or corrected them,
  REFEREE-2 re-ran alt_all with start validation (every count IDENTICAL, 0 violations); L-RED repaired them in R99 (l-red 5e8f0174,
  docs/red/R99-start-erratum.md: every reported count reproduces). No signed statement uses the counts on those games.
- Signatures: REFEREE docs/referee/R-N5-CORE.md (report 9d831869, sha1 0e1480a3709671f395a8813fcafa6e464fd2ffd4 there; §C 8641ae40;
  successor 17): (C1) SIGNED; (C2) SIGNED with |P| the number of TRANSITIONS (CORE-N1; the state reading false); (C3) with its Remark and
  Consequence SIGNED; (C4) with its two closing sentences SIGNED, tie clause needed (CORE-N4); (C5) with its parenthesis SIGNED; (C6) SIGNED
  in either scope (CORE-N3); quotes 10/10; notes CORE-N1..N6; no gap. REFEREE-2 docs/referee-2/R2-N5-CORE.md (report 2ed8d3fb, sha1
  a402d9e71efee5830ad2a853cf7808a1a1ab4402 there; §C b28d1ba9; successor 19): (C1)-(C6) SIGN, quotes 10/10 (shifted control 0/10); notes
  N-CORE-1..6; no gap. INDEPENDENCE: both clean, no exposure on either side (REFEREE re-listed REFEREE-2's paths at 23:00Z, 0 / 0 / 0 CORE
  files before its push; REFEREE-2 ran only a names-only count on docs/referee/ and opened REFEREE's report only after pushing 2ed8d3fb).
  §C (both): verdicts identical, (C1)-(C6) SIGNED by both; joint gap map EMPTY; CORE-N4 = N-CORE-2 found independently on two engines
  (same instance, transition, class, gates and κ); CORE-N3 = N-CORE-4; CORE-N1, CORE-N2 (a) and CORE-N5 ACCEPTED by REFEREE-2 as missed,
  CORE-N2 (b), (c) agreed; N-CORE-1 (re-derived), N-CORE-3, N-CORE-6 and REFEREE-2's controls ACCEPTED by REFEREE; N-CORE-5 no conflict;
  nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (elementary structural lemmas on N5's phases; no running-time bound, no
  algorithm claim). GAPS G-N5-TIME: open.
