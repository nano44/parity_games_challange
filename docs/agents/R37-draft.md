# Draft RESULTS R37 (Lead, 2026-10-25 13:20Z by date -u) (rev. 13:30Z: Lead ruling 12:58Z applied — CYC-EV lands with P-N5-ENT, not here; addendum 5c29d93d cited) — to CHECKER C46 — LANDED in RESULTS Results 14:01Z (CHECKER C46 2314af84 PASS), after R36

### R37 [refereed-only] N5 on one-Odd-choice games: blocked edges at a fallback (BL-FORM, BL), the confined optimum and the free freeze (CONF-MONO, FREE-FREEZE), the end of a scope run at θ = w (EQ-END), and where a violation of the per-level conjecture must live (EV, EV+, TEV-RED′) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C46.md, checker PENDING)
- Object (packet P-N5-RL, added at l-si 01d69ac, pinned trunk 2fb698d, unchanged during review): docs/si/P-N5-RL-box10.md, sha1
  0a3c70cbf873b2e011a5a00be54d38926f7861f1 (L-SI successor 5, Opus 5.5). The referees' repairs are in docs/si/P-N5-RL-fixes-box10.md
  (l-si 1f107bf, sha1 ac0274586a3b715d8725bc5226e3b32572edf017, L-SI successor 6: RL-1 with Lemma CYC-EV and the replacement TEV-RED,
  RL-2, RL-3, RL-4; this file contains new proof text, signed by both referees in addenda) and docs/si/P-N5-RL-fixes2-box10.md (l-si
  d2701d8, sha1 b3e3cd93f21cb61e019cb975afa428292a75d983, L-SI successor 6: REFEREE-2's items and the concordance) and
  docs/si/P-N5-RL-P1-addendum-box10.md (l-si f5b39de, sha1 5c29d93d54f133edd4a8fb9e43c331067b8c6b2e, L-SI successor 6: the joint
  verdicts; it governs where it differs from the fixes files); all on trunk. By Lead ruling (12:58Z), the CYC-EV text in fixes
  ac027458 is not landed under this entry: CYC-EV is a to-sign item of P-N5-ENT (signed there by REFEREE, R-N5-ENT 55a3f6f).
  Setting as in RESULTS R31 and R35 (𝒞^1O; phase; (h); THR; scope run S; gates and gate levels; M_k; COARSE_L; R̄ / R / F; b_k(y)). G_τ
  is the one-player game "Odd fixed to τ" and G_τ[F] its restriction to a closed F; an Even edge is BLOCKED if it is W-improving and not
  a gate. THE ENT SETTING: S a scope run, k0 < k consecutive fallbacks of S with M_{k0} = M_k = L ≥ 0, r > L on [k0+1, k], and an S4a
  step in (k0, k) that changes COARSE_L(θ) (a RISE); Ev := F_{k0+1} ∖ F_{k0}; A, B := the parts of P(θ_{k0}), P(θ_k) in
  H := V_{>max(L, rank c)}. (P) := for one-player games, a positional Even strategy with no improving edge is optimal (R18's premise
  G-1OA-4; discharged by RESULTS R36).
- Claims signed (both referees "(Opus 5.5, D15)", L37); every "CONDITIONAL on (P)" item is unconditional given RESULTS R36:
  (a) Lemma R-SAME and Lemma BL-FORM: at a state with (h), the order of π ⊕ a against π′ ⊕ a (routes in R) is the same for a ∈ {θ, w};
      every blocked edge (v, u) has σ_k(v) ∈ F_k, u ∈ R̄_k, π_u ⊕ θ_k ⊴ Ξ_k(σ_k v) ◁ π_u ⊕ w_k, and Ξ_k(σ_k v) has cycle node c.
  (b) Lemma BL at an in-phase THR S4c fallback k with (h) (x0 := σ̄_k(o)): (a) σ_k is not optimal in G_τ; (d) x0 is nominally deficient,
      and so is every free exit x with o ⊕ Ξ_k(x) ◁ w_k; and, CONDITIONAL on (P): (b) some Even edge is blocked at k; (c) on F_k,
      W_k = Opt(G_τ[F_k]); (e) every optimal G_τ-play from x0 leaves F_k along an Even edge into R̄_k.
  (c) Lemma CONF-MONO: for closed F′ ⊆ F, Opt(G_τ[F′]) ⊴ Opt(G_τ[F]) on F′. Lemma FREE-FREEZE (CONDITIONAL on (P)): if k0 is an
      in-phase THR S4c fallback with (h), t > k0 a state of the same phase, z ∈ F_t and z's (σ_t, τ)-play lies in F_{k0}, then
      Ξ_t(z) = Ξ_{k0}(z) (the packet's "(h) at t" is not needed).
  (d) Corollary EQ-END (CONDITIONAL on CN-LAST, P-N5-SCOPE §6): if θ_t = w at a state t of a scope run S, every later state of S is EQ,
      and S has at most one S4c fallback after t, the last transition of its phase.
  (e) Lemma MERGE′ (packet: MERGE): for a window gate (y, z) of level −1 ≤ ℓ < ∞ at a state with (h), y's route has no vertex of
      H := V_{>max(ℓ, rank c)}, COARSE_ℓ(Ξ z) = COARSE_ℓ(π ⊕ θ), o ∉ H, and before their first common vertex the σ-plays of z and x0
      contain no vertex of H. The packet's range "ℓ ≥ −1" includes ∞, where it is FALSE: level-∞ window gates with disjoint plays exist,
      e.g. experiments/si/orlens/instances/inr2_n32.pg, state 0, gate (6, 29) (RL-2, both referees).
  (f) In the ENT setting, CONDITIONAL on (P): Proposition EV (the σ_k-play of the level-L gate target z meets Ev; with q its first Ev
      vertex, ρ the play before q and π_q q's route at k0: A ⊆ B and B ∖ A = (ρ ∪ π_q) ∩ H; the window gate exists by RESULTS R35's
      NO-RF-OLD Corollary, RL-4); Proposition EV+ (the σ_k-play of the new threat x_k := σ̄_k(o) also meets Ev).
  (g) Proposition TEV-RED′ (CONDITIONAL on (P)): for t ∈ (k0, k] after the rise with x_t's σ_t-play meeting Ev and NO Ev VERTEX ON
      THAT PLAY'S CYCLE (the added hypothesis, RL-1), with e the last Ev vertex on the play's prefix before its first visit of c, f := σ_t(e), u_e := σ_{k0}(e), B_t := P(θ_t) ∩ H: (1) e is Even, f's play lies in
      F_{k0}, Ξ_t(f) = Ξ_{k0}(f); (2) u_e's route at k0 has no vertex in H and COARSE_L(Ξ_{k0} u_e) = COARSE_L(θ_{k0}); (3) B_t = A ⊔ (the
      H-vertices of x_t's play up to and including e) (RL-3); (4) if u_e ∈ R̄_t, (e, u_e) is a gate of level > L at t; (5) at t = k,
      u_e ∈ Ev ∩ F_k. Consequence (CONDITIONAL on (P), RL-3 wording, WITH the added hypothesis at t = k): if the per-level conjecture fails
      in the ENT setting and no Ev vertex lies on the cycle of the threat's σ_k-play, then at k the threat's play passes an Even e with e and u_e both evicted at k0 and both free at k, e re-routed to a frozen f ∈ F_{k0} of class
      (c, A), and B ∖ A on the threat's play up to and including e.
- Not signed: the packet's TEV-RED as stated (RL-1 = G-RL-1: an Ev vertex may lie on the cycle of x_t's play, and the packet does not
  exclude it; RL-3 = G-RL-2: "before e" is false when e ∈ H, which occurs on experiments/red/so/instances/tevlast_cex_n40.pg at
  k0 = 3, t = 7, e = 15) and its Consequence as stated (without the hypothesis); packet §7: CONJECTURE TEV FALSE in both forms (tev_cex_n40, sha1 17078f78;
  tevlast_cex_n40, sha1 ff1e9cb4; L-RED successor 16; Lead re-run: one Odd choice vertex, n5 27/16 and 11/1, Oink zlk OK strategies
  verified), CONJECTURES RISE-LAST and NJB / ENT, BL-X FALSE (lane data).
- Honest limits: (i) SUBCLASS 𝒞^1O. (ii) EV, EV+, TEV-RED′ (4)-(5) and the Consequence are about the ENT setting, which occurs in NO data
  of either referee or the lane: they are vacuous in data and rest on their proofs. (iii) These results narrow where a violation of the per-level conjecture NJB must live;
  NJB itself and G-N5-TIME stay OPEN. (iv) Lane work after the pin (P-N5-ENT with CYC-EV, N5-STR-box11) is not part of this entry.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE own engine from the SPEC text: 309 library + named
  games, agreeing with Oink zlk on all; FREE-FREEZE 93,125 + 177,919 checks, BL 376 + 526 THR fallbacks, BL-FORM 74,710 blocked edges,
  R-SAME 944k pairs, 0 failures; the lane's climb bests rl_a / rl_b / rl_c reproduced (35/2, 33/2, 30/3); REFEREE-2 own N5: batch 566 logs / 45,680 runs and
  climbs 1,583,748 runs, 0 violations; 168 level-∞ window gates, all with disjoint plays.
- Signatures: REFEREE docs/referee/R-N5-RL.md (referee b7419da, successor 8; climbs 257c3d8; Addendum A1 3886384; §C 5f52510; Addendum
  A2 d104aac on the fixes; 6d480e7 records the Lead ruling: A2's CYC-EV rows superseded for this landing): BL-FORM + R-SAME, BL (a), (d), CONF-MONO SIGNED; BL (b), (c), (e), FREE-FREEZE, EV (RL-4), EV+ SIGNED
  CONDITIONAL ON (P); EQ-END SIGNED CONDITIONAL ON CN-LAST; MERGE SIGNED WITH GAP RL-2; TEV-RED NOT SIGNED as stated, TEV-RED′
  SIGNED CONDITIONAL ON (P) with RL-3; A2's checks of the RL-2..4 texts stand. REFEREE-2 docs/referee-2/R2-N5-RL.md (referee-2 30dc5f5, successor 8; §C 88571b0; Addendum A db9d66a on the fixes): R-SAME,
  BL-FORM, BL (a), (d), CONF-MONO SIGN; BL (b), (c), (e), FREE-FREEZE, EV (N-RL-2, N-RL-3), EV+ SIGN CONDITIONAL ON (P); EQ-END SIGN
  CONDITIONAL ON CN-LAST; in §C MERGE SIGN WITH GAP RL-2 (missed) and TEV-RED NOT SIGNED as stated, TEV-RED′ SIGN CONDITIONAL ON (P);
  (its Addendum A db9d66a also signs CYC-EV, which lands with P-N5-ENT). §C: no verdict differs after both §Cs.
  Joint gap map (both §Cs; fixes2 concordance): RL-1 = G-RL-1 (proof gap; closed by TEV-RED′'s added hypothesis); RL-2
  (with N-RL-1; MERGE range, closed); RL-3 = G-RL-2 (wording, closed); RL-4 (citation, closed); N-RL-2, N-RL-3 and the FREE-FREEZE
  "(h) at t" remark (wording).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
