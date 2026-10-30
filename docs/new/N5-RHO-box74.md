# N5-RHO (box 74): ρ per W-run is BREADTH. It nearly saturates |Q|·|F| (cr_n80: 698 = 8.7n in one 15-step W-run), so the depth count is the W-run length, and the ρ / R*′ / ZXC chain closes as a circle with gain > 1
L-NEW successor 36 (Opus 5.5), D14 / D18, Lead reading L40. Lead 2026-10-30 06:08Z: «Decision, BOX 73: ρ per W-run (the REP route) … aim at ρ per W-run ≤ poly,
ideally from the Odd side's own one-player structure inside a W-run … An obstruction with an instance is a result.» That brief crossed my
FBO box, which was done as box 73 under the 05:40Z brief. So this is box 74. Written 06:33Z-06:52Z (date -u). Working note, unrefereed,
not a TARGET.md claim. G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Definitions:
  - W-run F: as in R89 / L-SI's tied.py. τ is fixed, there is no S4c, σ changes, and λ_W is fixed.
  - ρ_F: the pairs (transition s of F, Odd choice vertex q) with Ξ_{s+1}(q) ≠ Ξ_s(q). This is R56's ρ, read per W-run.
  - ρ_F(q): ρ_F at one vertex q.
  - |F|: the number of transitions of F.
  - Q: the Odd vertices of out-degree ≥ 2.
- Landed statements found (Lead's step 1):
  - RESULTS R56 (FB-RED, a reduction in ρ; honest limit «ρ per phase is not bounded (max ρ 218 in one phase, tcL_N10, n 350)»);
  - R89 (h) GP*-RUN «F has at most (n − 1)(R*_T + 1) W-changing transitions»;
  - R89 (i) R*-RISE.
  - Kill attempts: docs/red/R76-late-fallbacks.md («ρ = 144 in one phase at n 32 … Large ρ does not turn into fallbacks»);
    docs/red/R126-cut-premises.md (BA kill = FB-LIN / ρ-POLY kill).
  - No ρ-POLY kill exists.
- L-SI source opened: l-si 7dd85b02 docs/si/N5-LATEP-box51.md, items:
  - §2 Corollary FW-R*′ «Every W-run F has WCH ≤ (n − 1)(R*′_T(F) + 1)»;
  - §3 Lemma GAP-CLIMB «LATE′ adoptions of F number at most Σ_z d_E(z)·ZXC_F(z)»;
  - §4 «ZXC_F(z) = TXC_F(z) + WZ_F(z) … WZ_F(z) ≤ WCH_F(z)».
  These are lane-PROVED there, not landed.
- Tools in experiments/new/box74:
  - rho.py: ρ per W-run, length, W-flat transitions, σ̄-changes at Q;
  - climb_rho.py: hill climb on max ρ_F;
  - run.sh: the 1132-run corpus, N5 and N5-LZC, written to rho_*.txt;
  - out/*.log.
- Instances (inst/, with .start):
  - cr_n24.pg: sha1 87be1b412220ebbd55fa84fa27bf005c924a0116;
  - cr_n80.pg: 66d6d8a9…;
  - crz_n80.pg: 7fb981f1… (climbed on N5-LZC).

## 1. DATA first
- Corpus (1132 runs, N5 and N5-LZC):
  - Max ρ_F is 301 (snap_n80_s62, n 80: a 14-transition W-run, |Q| 36).
  - Max ρ_F(q) is 63 (gate_K64_n581, n 581, |Q| 5). On that family ρ_F(q) = K − 1 = 15 / 63 for K = 16 / 64: linear.
  - Max |F| is 159 (runfam_K40, n 79, |Q| 1, ρ 7).
  - W-flat transitions in a W-run: N5 ≤ 8 (u23sw64_n32); N5-LZC 0 everywhere (LZ-STRICT).
- Hill climbs (15 min each, fitness (max ρ_F, |F|)):
  | instance | n | engine | max ρ_F | ratio to n | |F| | abs Q | abs Q · |F| | max ρ_F(q) |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | cr_n24 | 24 | N5 | 162 | 6.75 | 17 | 10 | 170 | 17 |
  | cr_n80 | 80 | N5 | 698 | 8.73 | 15 | 47 | 705 | 15 |
  | crz_n80 | 80 | N5-LZC | 629 | 7.86 | 14 | 45 | 630 | 14 |
  - The climbs were still rising when stopped. Winners are SAME on N5 and N5-LZC.
  - In every climbed W-run, ρ_F is within 1 % of |Q|·|F|: (almost) every Odd choice vertex changes Ξ at (almost) every transition.

## 2. DEAD: ρ linear per W-run
- "ρ_F ≤ c·n per W-run" (any fixed c ≤ 8) is DEAD. The kill is experiments/new/box74/inst/cr_n80.pg + .start (sha1 66d6d8a9…): ρ_F = 698
  = 8.7n in one W-run of 15 transitions.
- Exact obstruction: ρ counts (vertex, transition) pairs, i.e. BREADTH. With |Q| = Θ(n) choice vertices all moving at each step,
  ρ_F = Θ(n·|F|). As for FBO in box 73, this says nothing about long runs.

## 3. What does hold (PROVED, lane)
- Lemma RHO-LEN (trivial, N5 and N5-LZC). ρ_F(q) ≤ |F| and ρ_F ≤ |Q|·|F| for every W-run F.
- Lemma LZ-RUN (N5-LZC; premise [OPT-H] of R88's W-MON, which N5-LZC meets by LZ-OPT).
  - Statement. Every transition of a W-run of N5-LZC changes W. Hence |F| ≤ (n − 1)(R*_T + 1) (R89 (h)) and
    ρ_F ≤ |Q|·(n − 1)(R*_T + 1).
  - Proof. A W-run transition has no S4c and σ_{t+1} ≠ σ_t, so it is an S4a step that switches some Even v. LZ-STRICT (box 72) gives
    W_{t+1}(v) ▷ W_t(v). Then apply R89 (h).
  - Dependency: R89 (h) is signed for N5. Its proof uses «τ constant, no S4c fallback, λ_W constant and [S4a]» (R89 (h)), with [S4a] read
    as "an optimum of H". ASSUMPTION OPT-ONLY (box 72) is needed for the transfer to N5-LZC. Under OPT-ONLY, LZ-RUN holds.
- For N5: |F| ≤ (n − 1)(R*_T + 1) + FLAT_F, FLAT_F := the W-flat transitions of F. At a FLAT transition every switched vertex is a
  TIE event (Lemma TIE), so FLAT_F ≤ TIE_F. So ρ_F ≤ |Q|·((n − 1)(R*_T + 1) + TIE_F).
- So ρ per W-run is polynomial iff the W-run length is (up to the factor |Q| and, for N5, TIE). The depth count behind the REP route is
  |F|, R89's object, not ρ.

## 4. The circle (READING, built from lane-PROVED and landed pieces)
- For N5-LZC under OPT-ONLY the chain reads:
  - |F| ≤ (n − 1)(R*′_T + 1) (L-SI FW-R*′; R*′ ≤ R*);
  - R*′_T ≤ LATE′_F ≤ Σ_z d_E(z)·ZXC_F(z) (L-SI GAP-CLIMB);
  - ZXC_F(z) = TXC_F(z) + WZ_F(z) ≤ TXC_F(z) + WCH_F(z) (L-SI §4);
  - TXC_F(z) ≤ ρ_F + CYC_F (box 72 TXC-RHO, TIE = 0).
- Sharper: one source per (z, transition), so TXC_F(z) ≤ |F| and ZXC_F(z) ≤ |F|. Each link is ≤ |F|, and the chain returns
  |F| ≤ (n − 1)(1 + m_E·|F|): gain (n − 1)·m_E > 1.
- Obstruction: every link charges a W-run transition to a (vertex, transition) event of the same run. No link has gain < 1, so the chain
  cannot close by itself.
- A closing needs one link that charges a step of F to something outside F, or to a potential that does not grow with |F|:
  - an amortised Odd-side potential (σ̄'s one-player optimality in G_σ: σ̄ only improves for Odd as σ rises? DATA: σ̄-changes at Q per
    W-run ≤ 73 at n 80 on the corpus and 58 on cr_n80; not proved monotone);
  - or a per-run bound on WCH_F(z).
  Neither is proved here.
- The Lead's "Odd side's one-player structure" idea, tested on the data:
  - On cr_n80, ρ = 698, but the σ̄-changes at Q are only 58. Most Ξ-changes at Odd choice vertices are inherited (σ̄(q) unchanged, the
    value of σ̄(q) rises), not Odd decisions.
  - So the Odd-side DECISION count (σ̄ changes, at most 58 here) is the small, candidate-polynomial quantity, and ρ over-counts it by
    inheritance.
  - SBQ_F := the σ̄-changes at Odd choice vertices per W-run. DATA:
    | instance | SBQ_F | n |
    | --- | --- | --- |
    | pp_K48_n449 (corpus max) | 101 | 449 |
    | snap_n80_s62 | 73 | 80 |
    | cr_n80 | 58 | 80 |
    | n3cov_phi (corpus, S3 start) | 42 | 32 |
    | cr_n24 | 32 | 24 |
  - "SBQ ≤ n" is DEAD on the corpus itself: experiments/red/n3/instances/n3cov_phi.pg (sha1 50d416db…), 42 > 32, ratio 1.31; cr_n24 has
    1.33. CONJECTURE SBQ-2 (OPEN): SBQ_F ≤ 2n. It was not climbed for; the next box should climb on it.

## DONE / FINDINGS / NEEDS
- DONE: box74/rho.py, climb_rho.py, run.sh, rho_*.txt (1132 × 2), inst/cr_n24, cr_n80, crz_n80, out/ logs; this note; check.sh "box 74".
- FINDINGS:
  1. DATA / DEAD: ρ per W-run is breadth. cr_n80 (sha1 66d6d8a9…) has ρ_F = 698 = 8.7n in one 15-transition W-run, 99 % of |Q|·|F|. No
     linear bound holds. Per q, ρ_F(q) ≤ |F| ≤ 17 in climbs, and 63 on gate_K64 (linear in K).
  2. PROVED (lane): RHO-LEN (ρ_F ≤ |Q|·|F|), and LZ-RUN (N5-LZC, under OPT-ONLY): every W-run transition changes W, so
     |F| ≤ (n − 1)(R*_T + 1) and ρ_F ≤ |Q|(n − 1)(R*_T + 1). For N5 add TIE_F.
  3. READING, the exact obstruction: the REP-route chain |F| → R*′ → ZXC → TXC → |F| closes with gain (n − 1)m_E, so it is a circle,
     not a bound. Every link charges a run step to an event of the same run.
  4. DATA / CONJECTURE: the Odd decision count (σ̄-changes at Q per W-run) is much smaller than ρ (58 vs 698 on cr_n80). "SBQ ≤ n" is
     DEAD (n3cov_phi 42 > 32; cr_n24 32 > 24); CONJECTURE SBQ-2 (≤ 2n) is OPEN.
- NEEDS: none from the owner. From the Lead: whether to climb / attack SBQ-2 (the Odd-decision count) next, or to go back to FBO-type /
  TIE work.
