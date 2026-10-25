# Draft RESULTS R43 (Lead, 2026-10-25 19:09Z by date -u) (rev. 19:24Z: C52 E-1, E-2, N-1..N-4) — to CHECKER C52

### R43 [refereed-only] N5 on one-Odd-choice games: a gate target always changes value after an Even fallback (STALE-GATE, every game), level −1 fallbacks need no REL (ENT-X_{−1}, LV-PL′), the u* = none fallbacks are counted (SAND, FLAT-ALL_{−1}^{none}, LV-NONE), and every scope run has at most 4·n·n_E + 3 fallbacks (SCOPE-FB) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C52.md, checker PENDING)
- Object (packet P-N5-LV2, added at l-si ed936af1, pinned trunk 283bcb6, unchanged during review): docs/si/P-N5-LV2-box12.md, sha1
  3b23a41fee6b705e20092d8dd49e7ce0b1408b03 (L-SI successor 7, Opus 5.5). The referees' notes are collected by the lane in
  docs/si/P-N5-LV2-fixes-box12.md (l-si 680c0294, sha1 f76fd1d1d7bfa70e5eb2e2bd354597853f093f87, L-SI successor 8: statuses, the
  CYC-EV citation and P-set identity in ENT-X_{−1} (c), §9 data); on trunk; repairs only.
  Setting as in RESULTS R31, R35, R37, R40 and R41 (scope run S; fallbacks, gates, gate levels, M_k; COARSE_L, (C1)-(C7); b_k(y);
  θ, w, r; THR, EQ; u* (u* = none iff r = −1); R̄ / R / F; (h); c; window gates; the kinds (α), (β), (γ) of R41 (a); the level −1 block
  f_1 < … < f_N of R41 (e)). (a) holds on every game; the rest is on 𝒞^1O.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P) beyond what RESULTS R36 discharges:
  (a) Lemma STALE-GATE (every game): if k0 is an S4c fallback at which Even switches and k > k0 a later state of the same run, every gate
      (y, z) at k has Ξ_k(z) ≠ Ξ_{k0}(z).
  (b) Corollary EV-G: if k0 is an in-phase THR S4c fallback with (h), k > k0 a state of the same phase and (y, z) a gate at k with
      z ∈ F_k, then z's σ_k-play is not contained in F_{k0} (FREE-FREEZE, RESULTS R37 (c), with (P) discharged by RESULTS R36).
  (c) Theorem ENT-X_{−1}: if k0 < k are consecutive fallbacks of a scope run in its level −1 block and k has a window gate (equivalently a
      (β) gate), the interval (k0, k) is clean. Step (c) cites CYC-EV (RESULTS R40 (d)) to place q before c on z's play, and the identity
      "Ξ_k(z) = ρ ⊕ Ξ_k(q)" is read as a P-set identity (LV2-N1, N-LV2-2; fixes).
  (d) Corollary LV-PL′: every scope run has at most n·n_E + 1 THR fallbacks with M = −1 and r ≥ 0 (REL(S) removed; compare R41 (e)).
  (e) Lemma SAND: if t ≤ t′ are states of a scope run with r_t = −1, then COARSE_{−1}(θ_{t′}) = COARSE_{−1}(θ_t).
  (f) Lemma FLAT-ALL_{−1}^{none}: at a fallback k of a scope run with r_k = −1 and (h) at k and k + 1, R31 FLAT-ALL (i)-(iv) hold with
      M := −1.
  (g) Theorem LV-NONE: every scope run has at most n·n_E + 1 THR fallbacks with r = −1.
  (h) Corollary SCOPE-FB: every scope run has at most 4·n·n_E + 3 S4c fallbacks (level ≥ 0: ≤ 2·n·n_E by RESULTS R40 (f) PL-S″; level −1
      with r ≥ 0: ≤ n·n_E + 1 by (d); r = −1: ≤ n·n_E + 1 by (g); EQ: ≤ 1 by RESULTS R37 (d) with CN-LAST = R38 (f)). The packet's
      conditions (C-ENT) and (C-LV) are now RESULTS R40 and R41 (landed); (c), (d), (f), (g) rest on R41.
- Not signed (packet §10): docs/si/N5-LV3-box12.md (XG, ANTI, NEED-β; now packet P-N5-NEEDB, in review) and the CONJECTURE "in scope,
  THR ⇒ M ≥ 0"; the packet's Reading that SCOPE-FB closes R29's per-scope-run count CL-S (a reading). REFEREE-2's candidate CONJECTURE
  in N-LV2-3 ("an in-scope THR fallback with M = −1 is the last fallback of its scope run") is FALSE (R2 Addendum B withdraws it), and so is
  L-SI's CONJECTURE NONE-LAST (docs/si/DEAD.md): experiments/red/so/instances/beta2_n11.pg (sha1 bdea2a23, L-RED successor 16) has one scope run with two
  r = −1 THR fallbacks at states 0 and 1 (an eviction cascade: fallback 0 evicts 5, and the R-vertex 10 then has a (β) gate (10, 5));
  Lead re-run: one Odd choice vertex, n5 4/2, Oink zlk OK strategies verified, L-SI's scopefb.py gives fb_r=-1 2 in one scope run;
  confirmed on both referees' engines.
- Honest limits: (i) SUBCLASS 𝒞^1O except (a). (ii) SCOPE-FB bounds fallbacks per scope run; scope runs per phase, out-of-scope
  fallbacks, S4a steps, phases and wakes K stay open here, so G-N5-TIME stays open. (iii) Thin data: ENT-X_{−1} and LV-PL′'s block with
  N ≥ 2 are vacuous in all data; the first level −1 block fallback with r ≥ 0 is REFEREE-2's witness
  docs/referee-2/R2-N5-LV2/climb/block_9501.pg (sha1 1b5b76fd; from the start pair in climb/block_9501.txt, state 1; N = 1; reproduced
  on REFEREE's engine from that start pair, R-N5-NEEDB (referee 008ad8ab); Lead re-run from the canonical start, where the run has no
  block fallback: one Odd choice vertex, n5 3/1, Oink zlk OK strategies verified). LV-NONE's N = 2 step is exercised only on beta2_n11; climbs
  give at most 1 u* = none fallback per scope run.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own probe): STALE-GATE 70,267 checks on 402 games
  (114 non-𝒞^1O), EV-G 34,389, SAND 181, SCOPE-FB on 236 scope runs (max 37 fallbacks per run); in its addendum, a climb seeded from
  best_lv_9401: FLAT-ALL_{−1}^{none} 351,417 checks, SAND 1,000,826, max 1 u* = none fallback per scope run; 0 failures. REFEREE-2 (own code): batch (66,655 runs + 1,422 on newer files; max 37 fallbacks per scope run, all of level ≥ 0) and 5
  climbs (1.72 M runs): in the climbs 237,033 u* = none fallbacks, max 1 per scope run (worst LV-NONE ratio 22‰), max 5 fallbacks per
  scope run, FLAT-ALL^{none} at all 237,033, SAND 921,624, 645 level −1 block fallbacks with r ≥ 0 (max 1 per scope run); 0 violations;
  mutation controls bite in 2 of 4 (sand0, fa0; the other two cannot bite at N ≤ 1). Lane: STALE-GATE 72,589, EV-G 39,406, SAND 310, SCOPE-FB 293 scope runs.
- Signatures: REFEREE docs/referee/R-N5-LV2.md (referee b454ca3, successor 9; addendum 46a8030; §C ed8bc20, successor 10): STALE-GATE,
  EV-G, ENT-X_{−1}, LV-PL′, SAND, FLAT-ALL_{−1}^{none}, LV-NONE, SCOPE-FB SIGNED with the conditions as labelled; notes LV2-N1, LV2-N2; no gaps.
  REFEREE-2 docs/referee-2/R2-N5-LV2.md (referee-2 a551deb, successor 10; addendum f2209fa (block witness); Addendum B 11126df; §C ab7843a, successor 11): all 8 SIGN; notes
  N-LV2-1..3; no gap. §C (both): verdicts identical; joint gap map empty; LV2-N1 and LV2-N2 accepted by REFEREE-2; N-LV2-1 matches
  REFEREE's verdict note.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
