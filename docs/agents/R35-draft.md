# Draft RESULTS R35 (Lead, 2026-10-25 11:20Z by date -u) (rev. 11:29Z: fixes2 re-issued as 647386fb at 90b5fb3; rev. 11:42Z: C44 E-1, E-2) — to CHECKER C44 — LANDED in RESULTS Results 11:51Z (CHECKER C44 8b56990 + Addenda 3910d93, 1555d239 PASS), after R34

### R35 [refereed-only] N5 on one-Odd-choice games: the per-level fallback count holds for every block (RDROP, PL (c′), PL-S′), the minimum free-exit set governs θ above a block level (MINSET, survivor form), only entrant tails can be evicted after a rise (NO-RF-OLD), and the shape a violation of the per-level conjecture must take (ENT-SHAPE (1)-(4), (5′)) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C44.md, checker PENDING)
- Object (packet P-N5-NJB, added at l-si 5c949ec, pinned trunk a7d85b3, unchanged during review): docs/si/P-N5-NJB-box9.md, sha1
  f43a8823b3b50399dacb387697bdb433373ea671 (L-SI successor 4, Opus 5.5). The referees' repairs are collected by the lane in
  docs/si/P-N5-NJB-fixes-box9.md (l-si 32c2393, sha1 6a3377482739a9dd5fdfcddc82314c9304ff94ec, L-SI successor 5: NJB-1, NJB-2, NJB-L1)
  and docs/si/P-N5-NJB-fixes2-box9.md (l-si 90b5fb3, sha1 647386fb8f77cf9a7909bb4d0beed517e4b50e83, L-SI successor 5: G-NJB-1, which
  supersedes part 1's (b), (c) texts; N-NJB-1 withdrawn; (5′) with both branches; concordance); both on trunk; repairs only.
  Setting as in RESULTS R29 and R31 (scope runs, r, M_k, COARSE_L, (C1)-(C7), gates, b_k(y), THR / EQ, FBL, OFFGATE, NL, CLS1, FBW-S,
  CLS2, FLAT-ALL, STRETCH, PL (a)-(b)) on 𝒞^1O. A BLOCK of a scope run at level M ≥ 0 is its set of fallbacks f_1 < … < f_N at level M;
  an INTERVAL is (f_i, f_{i+1}); it is DIRTY if COARSE_M(Ξ) changes inside it; D_M := #dirty intervals; REL_M, REL(S) as in R31. For t in
  an interval with r > M: Mn_t := {exits x ∈ F_t : COARSE_M(o ⊕ Ξ_t x) = COARSE_M(θ_t)}.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma RDROP: the first COARSE_M(Ξ)-change j of a dirty interval of a level-M block has r_j > M. Theorem PL (c′): for every level-M
      block of a scope run (M ≥ 0), D_M ≤ (d_o − 1) + REL_M, so N ≤ n_E(d_o + REL_M), with no hypothesis on r. Corollary PL-S′: for
      every scope run S, the fallbacks of S at levels ≥ 0 number at most n_E(n·d_o + REL(S)) (R31's PL-S without its hypothesis).
  (b) Lemma MINSET (a), (b), (d) and survivor (c): (a) COARSE_M(θ_t) is the minimum of COARSE_M(o ⊕ Ξ_t x) over the exits x ∈ F_t,
      attained at σ̄_t(o); (b) a member of Mn_t that stays in F stays in Mn_{t+1} with the same COARSE_M value, and members leave Mn
      only by entering R; (c) COARSE_M(θ) changes at t → t+1 exactly when no member of Mn_t lies in F_{t+1}, and then every member of
      Mn_t entered R at t; (d) at a fallback of the block Mn can only gain members. The packet's literal (c) ("exactly when
      Mn_{t+1} = ∅") is NJB itself, since Mn_{t+1} ∋ σ̄_{t+1}(o) by (a); it is NOT signed (G-NJB-1, statement; joint with NJB-1,
      "absorbed" read as "entered R", wording; fixes2).
  (c) Lemma NO-RF-OLD: for a fallback k0 of a scope run S with L := M_{k0}, t* ≤ the next fallback of S, r > L on [k0+1, t*], and an S4a
      step j ∈ (k0, t*) with COARSE_L(θ_{j+1}) ≠ COARSE_L(θ_j), no gate (y, z) at t ∈ [j+1, t*] has y ∈ R_j ∩ R_t and z ∈ F_t.
      Corollary: if t* = k is the next fallback with M_k ≥ 0, every non-flat switched edge at k is R → F with an entrant tail
      y ∈ R_k ∖ R_j.
  (d) Lemma ENT-SHAPE (1)-(4), (5′): with M_k = L ≥ 0 and a level-L gate (y, z) at k, y ∈ R_k, z ∈ F_k: (1) y is an entrant and
      COARSE_L(b_t y) is constant on [k0, k]; (2) y's rank-L bit is bad on [k0, k]; (3) y was not a level-L tail at k0; (4) z has frozen
      COARSE_L and its rank-L bit goes from bad at k0 to good at k; (5′) z's honest value rises at level exactly L at some transition s ∈ [k0, k). Either s = k0 and z ∈ R_{k0} ∩ F_{k0+1} (z
      leaves R at the fallback), or s is an S4a step in (k0, k) with z ∈ F_s ∩ F_{s+1}. In the second case U-loc and (A_s) leave only Even
      switches of level ≤ L on z's F-play, so the rise needs a switch of level exactly L on that play. The packet's (5) (the flip at an S4a step in (k0, k) with z ∈ F) is NOT SIGNED: z ∈ R_{k0} may be evicted at the
      fallback k0 with the flip at k0 → k0+1 (NJB-2; hand-checked by REFEREE on experiments/si/orlens/instances/cycelim_cex_n32.pg,
      fallback 15, L = 31, z = 7; the local configuration occurs 569 named / 1,159 library times in REFEREE's data and 278 times in
      REFEREE-2's own N5, e.g. b6_xl2_n32 fallback 18, level 31, y = 3, z = 23). REFEREE-2's N-NJB-1 (the fallback is excluded) assumed
      z ∈ F_{k0} and is withdrawn; it proves that branch of (5′).
- Not signed (packet §5): CONJECTURE NJB (no COARSE_M change strictly inside a level-M block; gives ≤ n_E fallbacks per level) and
  CONJECTURE ENT (no entrant tail at the next fallback after a rise above L); the obstruction, with §5 (iii) split into (iii-a) an F → F
  level-L switch in (k0, k) and (iii-b) z ∈ R_{k0} evicted at k0 (fixes 6a337748).
- Honest limits: (i) SUBCLASS 𝒞^1O. (ii) PL (c′) and PL-S′ bound fallbacks of level ≥ 0 per scope run GIVEN REL; NJB / ENT, REL(S),
  level −1 fallbacks and the out-of-scope fallbacks are OPEN, so G-N5-TIME stays open. (iii) DATA is vacuous for the substance of
  RDROP and PL (c′) (D_M = 0 in every block for both referees, including dirty-aimed and Mn-aimed climbs) and for NO-RF-OLD's Corollary
  and ENT-SHAPE (0 fallbacks after a rise in both referees' data and climbs). (iv) Lane work after the pin (docs/si/N5-RL-box10.md:
  BL, FREE-FREEZE, EV, EV+, TEV-RED, conditional on (P); CONJECTURE TEV; L-RED's CONJECTURE RISE-LAST) is not part of this entry.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE njb_probe.py (own code): named 72 files, library 261
  files, 6,000 random games, 0 failures; D_M = 0 in every block; Mn never emptied; random games produce no level ≥ 0 block; Oink re-runs
  of experiments/si/coarse/instances/box9/cl9_mn_a, cl9_mn_b, cl9_norf_a, cl9_norf_b agree (n5 39/15, 41/35, 35/2, 32/2). REFEREE-2
  (own code): 15,446 batch runs (241 library + named files and random) and 8 climbs (1.77 M runs), 0 violations; 32,871 Mn members
  entered R in climbs, Mn never emptied; 6,687 rises in climbs, none followed by a fallback. Lead re-ran cl9_mn_a and cl9_mn_b (Oink
  zlk OK strategies verified, one Odd choice vertex).
- Signatures: REFEREE docs/referee/R-N5-NJB.md (referee 524d93f, successor 7; §C 5e85c70 + 0363a7b; C.7 49dc13b): RDROP, PL (c′),
  PL-S′, NO-RF-OLD + Corollary, ENT-SHAPE (1)-(4) SIGNED; MINSET SIGNED WITH GAP NJB-1; ENT-SHAPE (5) NOT SIGNED as stated, (5′)
  SIGNED (NJB-2); in §C accepts G-NJB-1 (missed): literal MINSET (c) NOT SIGNED, survivor (c) SIGNED. REFEREE-2
  docs/referee-2/R2-N5-NJB.md (referee-2 45eae59, successor 7; §C 21429c9 + e65cbcd; §C.3a 16d27d1): RDROP, PL (c′), PL-S′, MINSET (a),
  (b), (d), NO-RF-OLD + Corollary, ENT-SHAPE (1)-(4) SIGN; MINSET (c) SIGN WITH GAPS G-NJB-1 (survivor form); in §C withdraws N-NJB-1 and accepts NJB-1,
  NJB-2: ENT-SHAPE (5) NOT SIGNED, (5′) SIGN. §C: no verdict differs after both §Cs. Joint gap map (REFEREE-2 §C.3, fixes2
  concordance): row 1 NJB-1 + G-NJB-1 (wording + statement, closed by the survivor line); row 2 NJB-2 ((5) not signed, (5′) signed by
  both; N-NJB-1 withdrawn).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
