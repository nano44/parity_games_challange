# P-N5-KW addendum: what K, K_S, (E) and (K_W) count (transitions vs switches)
L-SI successor 10 (Opus 5.5; D15, D18, L37, L40). Written 2026-10-25 21:50Z (date -u), at the Lead's request of 21:46Z (Lead's stamp),
which crossed the packet's freeze. Object: docs/si/P-N5-KW-box15.md, sha1 c0b0111fcc2259e4ed9d43647bc4fa08cec452a5 (l-si bf1ed0f7). The
packet is FROZEN and not edited; this file only fixes the counting units. It adds no new statement and no new proof.
- Source: L-RED 18, docs/red/R72-fx-fbpoly-k.md at l-red 9812efa7 (file sha1 5f982712…), §(2) and §5.

## 1. Definitions used in P-N5-KW (all are TRANSITION counts)
- (K_W), K_S (packet §7, Corollary KW-S): the number of non-fallback TRANSITIONS of the stretch at which W changes at some vertex of R.
  This is R26's K_W (R26 (b), (d): "non-fallback transitions with a W-change on R").
- (E), E(Q) (packet §5 E-SEG (iii)): the number of TRANSITIONS of Q that contain an event, as in R26 (d) ("E transitions containing an
  event"). e(Q), N_B(Q), N_cut(Q) and the c_w-switch count in E-SEG (ii) are also counted in transitions.
  - c_w switches at most once per transition, so for c_w the switch and transition counts agree.
- Theorem RUN, Corollary PHASE: N_Ξ, T_rel, T, N_st, X, Θ, W_ch, S_o, f are all TRANSITION counts, as in the landed results cited.
- K (wakes, packet §7 third bullet): read it as K_t := the number of TRANSITIONS with a wake. The packet's sentence "every wake is a
  relevant transition, so K ≤ T_rel" is exact for K_t.
  - For the switch count K_s := #wake switches (RESULTS R27 setting's "K := #wakes"), each wake is a switch of a distinct Even vertex at
    its transition, so K_s ≤ n_E·K_t ≤ n·K_t ≤ n·T_rel.

## 2. Which landed results use which unit, and the conversion
- RESULTS R27 setting writes "K := #wakes". Its source packet P-N5-LP §3 (sha1 d2c8121a…) defines "K := the number of transitions with
  a wake", and R27 (f)'s bound ρ ≤ 2f + S_o + 2X + K counts rises: one per wake TRANSITION (P-N5-LP §4 step 2). So ρ needs K_t.
  - With K_s in place of K_t the bound stays true, since K_t ≤ K_s, but it is weaker.
- P-N5-KW does NOT use ρ, R27 (f) or R28 (c). Corollary PHASE goes through Theorem LP's first inequality, T ≤ (m − n + 1)(T_rel + 1)
  (R27 (d)), and bounds T_rel directly. So the K-unit question does not touch any statement to sign.
- R26 (b), (d) count K_W and E in transitions, and the packet uses them in that unit.
- Conversion, whenever needed: switches ≤ n_E · transitions (each Even vertex switches at most once per transition).

## 3. DATA from R72 (L-RED 18; DATA, not proof)
- Every wake L-RED saw, in the library and in climbs, is at a ¬H1 ∧ ¬H2 state (its type "U23"), including the K-chain family.
  - R72 notes that docs/new/N5-K-box33.md calls these states U3, but by the H1 test they are ¬H1.
- K_t grows linearly on the K-chain family: K_t = K − 1 = (n − 25)/11. Climbs found no faster growth: best K_t 6 at n 58, 9 at n 124.
- A climb drove K_s to 28 per phase at n 58 with a single wake transition. So K_s and K_t really differ.
- Consistent with P-N5-KW: wakes are relevant transitions, so K_t ≤ T_rel, and T_rel is polynomial given f by Corollary PHASE.
