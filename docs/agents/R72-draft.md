# Draft RESULTS R72 (Lead, 2026-10-26 15:13Z by date -u; both reports, both §Cs and the fixes file filled (15:38Z by date -u)) — to CHECKER C81

### R72 [refereed-only] N5 on EVERY game, inside one phase: a RELAY ρ event at a terminal q is caused by the exit e of q's CHOSEN option (e ≠ c, e ≠ q): e has a ρ event at the same transition, or e's honest play at t + 1 passes through q (TOG) (Lemma CHOSEN); following chosen exits, every RELAY event chains in at most |Q_c| − 1 steps to a ROUTE or CYC event of its class at the same transition, or to a TOG step (Corollary RELAY-CHAIN), so Σ_{q ∈ Q_c} ρ_q ≤ |Q_c|·(ROUTE_c + CYC_c + TOG_c) per phase (consequence (b)); and once every non-terminal of a class sits at its target value TV_Θ (hypothesis (H)), the class has no Even switch outside its terminals and no ρ event to the end of the phase (Lemma TV-END) (2026-10-26) — structural lemmas for N5 beyond one Odd choice vertex (no count: ROUTE_c, CYC_c, TOG_c and the time to (H) are not bounded here; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C81.md, checker PENDING)
- Object (packet P-N5-CHOSEN, added at l-si b7189738, pinned trunk 9196c318, unchanged during review): docs/si/P-N5-CHOSEN-box19.md, sha1
  764cfbb331a1aaefa819a01d64ee6b7cfbbd7316 (L-SI successor 15, Opus 5.5). The referees' notes are collected by the lane in
  docs/si/P-N5-CHOSEN-fixes-box19.md (l-si d0b94c1f, sha1 2ae6f681c5abecc915f66296cd0c5a3d5fe1c73e, L-SI successor 16: F1-F7 for CHOSEN-N1..N5,
  N-CHOSEN-1..7; 22 quotes checked by script); on trunk; repairs only, no signed statement changes.
  Setting (every game): as in RESULTS R69 (phases as in R38 (a); Q; classes U_c, κ, κwt_c and ρ events as in RESULTS R56 and R61; EXIT and
  CLASS EXIT PATH per y; ROUTE / RELAY as there); Q_c := (Q ∩ U_c) ∖ {c}, T := Q ∪ {c}; a ρ event at q is CYC if q = c or q lies on its honest
  cycle at t or t + 1. The CHOSEN EXIT of q at t is the exit e of y* := σ̄_t(q), p its class exit path. A Q_c-RUN Θ is a maximal run of the phase
  with Ξ(q) constant for every q ∈ Q_c; TV_Θ(z) := max(κopt_c(z), max_{q ∈ Q_c} κopt^q(z) + κ_Θ(q)) for z ∈ U_c ∖ T with RESULTS R56's κopt_c,
  κopt^q (κ_Θ(c) means κ(c) = (0, 0): CHOSEN-N4, REFEREE); (H) at t ∈ Θ: κ_t(z) = TV_Θ(z) for every z ∈ U_c ∖ T.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game, inside one phase, fallbacks included; no item uses (P); premises LANDED:
  RESULTS R15 (a), (d) ((SG) via (VJ), RESULTS R57 (a), under the standing premise 1E-N3, P1; (SW): every Even switch of N5 is to an edge
  of Iσ); R38 (a) KEY; R56 setting line, (d) κ-Y-FORM_D (its "≤" half resting on R18 (d) Lemma S (a), every game), (g) Lemma TV (only for
  when (H) holds); RESULTS R69's setting and additivity (P-N5-FLIP §1, signed as a proof step) and R69 (c) ROOT-C in its corrected form
  ("class exit path AND exit"). CHOSEN's identity κ_t(q) = κwt_c(q) + κ_t(y*) at t is the play decomposition (one-step additivity); R56 (d)
  with P1 is needed only for the "⪯" step at t + 1 (CHOSEN-N1 = N-CHOSEN-4, both referees):
  (a) Lemma CHOSEN: for q ∈ Q_c on no honest cycle at t and t + 1 with a RELAY ρ event at t → t + 1, the chosen exit e satisfies e ≠ c and
      e ≠ q, and either κ_t(e) ≠ κ_{t+1}(e) or e's honest play at t + 1 passes through q (TOG). The packet's statement says only "e ≠ c";
      e ≠ q follows from the same hypothesis and RELAY-CHAIN uses it (N-CHOSEN-2, REFEREE-2; accepted by REFEREE, who had checked it).
  (b) Corollary RELAY-CHAIN: with e_0 := q and e_{i+1} := the chosen exit of e_i while e_i has a RELAY event at t → t + 1, the e_i are distinct
      and the sequence stops after at most |Q_c| − 1 steps at an e_i whose event is ROUTE or CYC, or at a TOG step. Consequences: (a) every
      transition with a ρ event at a terminal of the class carries a ROUTE or CYC event of the class, or a TOG step; (b) per phase,
      Σ_{q ∈ Q_c} ρ_q ≤ |Q_c|·(ROUTE_c + CYC_c + TOG_c), ROUTE and CYC events mapped to themselves (N-CHOSEN-3, REFEREE-2; accepted by REFEREE),
      and since TOG_c counts events, Σ_q ρ_q ≤ |Q_c|(ROUTE_c + CYC_c) + TOG_c also holds (CHOSEN-N3, REFEREE).
  (c) Lemma TV-END: if (H) holds at t ∈ Θ and t → t + 1 is in the phase, no Even vertex of U_c ∖ T switches at t → t + 1, t + 1 ∈ Θ and (H) holds
      at t + 1; hence from t to the phase's end class c has no switch in U_c ∖ T and no ρ event, and Θ lasts to the phase's end. By R56 (g), (H)
      holds at every t after |U_c| − 1 fallbacks of the phase and of a Q-run. REFEREE-2 signed TV-END conditional on ROOT-C's corrected form
      landing (N-CHOSEN-5); R69 (c) landed at trunk a7c141b8 with that wording, and its §C lifts the condition.
- Not signed: consequence (a)'s parenthetical "(This is the stronger, per-event form of ROOT-C's consequence …)", which is not an implication
  (CYC and TOG ends name no changed class exit path) (CHOSEN-N2, REFEREE; REFEREE-2's verdict is on the statement). READING (REFEREE's
  CHOSEN-N2, both §Cs): (a) proves RESULTS R69's not-signed CONJECTURE ROOT-C strong form up to the TOG alternative. Also not signed (packet
  §5): the obstruction map (READING) and the data.
- Honest limits: (i) Structural lemmas: no count; ROUTE_c, CYC_c, TOG_c and the number of transitions before (H) first holds are not bounded
  here; ρ events of the class all occur before (H) (TV-END bounds nothing by itself). (ii) TOG: CHOSEN's second alternative occurs, but in
  both referees' data never alone (the first alternative held at every RELAY event) and no chain ends in a TOG step (CHOSEN-N5 = N-CHOSEN-6,
  first half); the packet's §5 "TOG never occurs" is too strong. (iii) Over-budget classes: REFEREE-2 skipped 2,272 (phase, class) pairs for
  TV-END (κopt over 3·10⁵ paths; tcL_*, pp_K48_n449); REFEREE 122 UNK classes in its §5 rows and 668 in the n ≤ 40 batch.
- Data (DATA, not proof): REFEREE (successor 15, own chosen_probe.py; lane code not run): library n ≤ 24 (2,960 runs; ROUTE / RELAY / CYC
  2,482 / 678 / 92; chains up to 11), random 3,000 games with ≤ 8 and ≤ 12 Odd choice vertices (15,000 runs each), the lane's five
  instances at their starts and with S3, and the n ≤ 40 library batch (e49bf11a: 2,610 runs, 6,364 / 2,027 / 99, 1,485 TV-END checks, chains
  up to 11, ends 2,015 ROUTE / 12 CYC / 0 TOG); 0 failures; TV-END tested at every non-final (H) state, 4,356 checks in the library and random
  rows (2,145 with |Q_c| ≥ 1), so not thin (its §5; N-CHOSEN-6 second half); mutations MUT=1 (σ̄_{t+1}) CHO 5 / CHAIN 3, MUT=2 (TV without
  the q-terms) 24. REFEREE-2 (successor 17, own chosen_check.py; lane code not run): 21,949 runs (the lane's instances, lib2o, lib41, its 503
  𝒞^1O files, random games with 2, 4 and all Odd choice vertices); 6,322 RELAY events, 241 with TOG, first alternative at all of them; chains
  up to 86 (tcL_N12, |Q_c| = 233); 66,816 (class, state) pairs reach (H), 2,955 transitions checked after (H); KADD 2,161,705 and KORD
  2,410,459 self-checks; 0 violations; on its 503 𝒞^1O files 3,781 ROUTE, 68 CYC and 0 RELAY events (N-CHOSEN-7, cross-check of R69 (b)
  SELF-FREE); controls next 740 and noH 12,651 failures. Both reproduce the lane's nep90_n40 (153 / 139) and nep76_n40 (129 / 48) at its
  starts.
- Signatures: REFEREE docs/referee/R-N5-CHOSEN.md (referee b3473114, data e49bf11a, §C d08011be, successor 15): CHOSEN, RELAY-CHAIN, (a)
  (without its parenthetical), (b), TV-END SIGNED, no gap; notes CHOSEN-N1..N5. REFEREE-2 docs/referee-2/R2-N5-CHOSEN.md (referee-2 aab45be6,
  §C bde1ea77, successor 17): the same items SIGN, TV-END conditional on ROOT-C's corrected form, lifted in its §C (R69 (c) at a7c141b8); no
  gap; notes N-CHOSEN-1..7. §C (both): verdicts identical; joint gap map empty; CHOSEN-N1 = N-CHOSEN-4, CHOSEN-N5 = N-CHOSEN-6; CHOSEN-N3 and
  N-CHOSEN-3 compatible wordings of (b)'s count; N-CHOSEN-1, -2, -3, -7 accepted by REFEREE; CHOSEN-N2 accepted by REFEREE-2; N-CHOSEN-5
  closed by R69's landing; nothing open. Both under the standing premise 1E-N3 (P1).
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas; no running-time bound). GAPS G-N5-TIME: open.
