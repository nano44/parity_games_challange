# N5-SBQ (box 76): CONJECTURE SBQ-2 is DEAD (cs_n32: 173 = 5.4n σ̄-changes in a 9-step W-run). Odd decisions are NEW adoptions (≤ m_O) plus RETURNS, and the returns are the unbounded part
L-NEW successor 36 (Opus 5.5), D14 / D18, Lead reading L40. Lead 07:11Z (read 07:21Z; box 75 had used that number for the per-phase σ̄
question of the 06:38Z brief): «SBQ-2. First climb on SBQ_F … If SBQ-2 dies in the climb, record it with the instance and give the exact
reason. Then propose the next candidate potential, one that counts decisions rather than value changes. Keep N5 and N5-LZC both measured.»
Written 07:22Z-07:42Z (date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME OPEN.
- Definitions:
  - W-run F: as in R89 and box 74.
  - SBQ_F: the pairs (transition of F, Odd choice vertex q) with σ̄(q) changing.
  - NEW_F: the changes of σ̄(q) to a successor that q has not held earlier in F (F's first state counts).
  - RET_F: the other changes (RETURNS).
  - NEWE_F and RETE_F: the same split for Even's σ.
  - m_O := Σ_{q∈Q} (deg q − 1) and m_E := Σ_{v Even} (deg v − 1).
- Tools in experiments/new/box76:
  - climb_sbq.py: box74/climb_rho.py with fitness SBQ_F;
  - sbqrun.py: the NEW / RET split for both players;
  - run.sh: the 1132 runs, N5 and N5-LZC, written to sbqrun_*.txt;
  - out/*.log.
- Instances (inst/, with .start):
  - cs_n32.pg: sha1 bff52a582d9e617cdabc4956dd7556e77492899f;
  - cs_n80.pg: d09c7169…;
  - csz_n24.pg: 8ee42d5a… (climbed on N5-LZC).

## 1. DEAD: CONJECTURE SBQ-2 (SBQ_F ≤ 2n)
| instance (15-min climb, seed) | n | engine | SBQ_F | ratio to n | abs F | NEW | RET | m_O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cs_n32 (red/n3 n3cov_phi + start) | 32 | N5 | 173 | 5.41 | 9 | 57 | 116 | 108 |
| cs_n80 (snap_n80_s62 + start) | 80 | N5 | 415 | 5.19 | 16 | 128 | 287 | 192 |
| csz_n24 (nep13_n24 + start) | 24 | N5-LZC | 110 | 4.58 | 17 | 64 | 46 | 75 |
- Kill: experiments/new/box76/inst/cs_n32.pg + .start (sha1 bff52a58…). SBQ_F = 173 > 2n = 64 in one W-run of 9 transitions.
- N5-LZC dies too (csz_n24: 110 > 48).
- Winners are SAME on N5 and N5-LZC. The climbs were still rising when stopped.
- Exact reason: the same breadth as ρ (boxes 74-75).
  - SBQ_F ≤ |Q|·|F|: on cs_n32, 173 of a possible |Q|·|F| = 23 · 9 = 207.
  - Most of it is RETURNS: 116 of 173. Odd's reply LEAPFROGS between options already used in the run (box 75's thetaA_n7 mechanism),
    many vertices at once.

## 2. What holds (PROVED, lane, from the definitions)
- Lemma NEW-BOUND. NEW_F ≤ m_O and NEWE_F ≤ m_E for every W-run F. A vertex can newly adopt each of its successors once per run, and
  its first-state choice is not counted. DATA: holds in all 2264 runs.
- Hence SBQ_F = NEW_F + RET_F ≤ m_O + RET_F, and |F| ≤ m_E + RETR_F, where RETR_F is the number of transitions of F whose Even switches
  are ALL re-adoptions. Each transition of F switches some Even vertex; if any switch is new, charge the transition to it.
- So a decision count does not grow with |F| exactly when it is a NEW count. The unbounded parts are the returns, for Odd (RET) and for
  Even (RETR).

## 3. DATA on the returns (1132 runs × 2)
| quantity | N5 | N5-LZC |
| --- | --- | --- |
| max Odd RET_F | 93 (pp_K48_n449) | 93 |
| max Odd RET_F / n | 0.66 (n3cov_phi, n 32) | 0.66 |
| total Odd RET | 2185 | 2165 |
| max Even RETE_F | 252 (box52 topfix_n10, n 210) | 252 |
| max Even RETE_F / n | 1.47 (si runlin runfam_K10: 72 at n 49) | 1.45 |
| total Even RETE | 6265 | 6100 |
- The longest W-run, the depth quantity, is runfam_K40 (L-SI's run family): 159 transitions at n 79 (2.0n); 157 on N5-LZC.

## 4. Next candidate potential (proposal, CONJECTURE, as the Lead asked: it counts decisions)
- By §2, the circle |F| → R*′ → ZXC → TXC → |F| (box 74 §4) needs exactly one non-growing link. The decision split points to it.
- Every transition of F is either NEW (≤ m_E of them) or an all-return transition. So:
  - CONJECTURE RETR-POLY: the all-return transitions of a W-run number ≤ poly(n). DATA: |F| ≤ 2n everywhere, so RETR_F ≤ 2n.
  - A proof route: an Even RE-ADOPTION of (v, e) in F in N5-LZC is a strict W(v)-rise back to an old edge (LZ-STRICT). Between v's leave
    of e and its return, W(e) must rise strictly past W of v's intermediate choice (W-SUCC / LATE-RISE type). So a return is a W-rise of
    its TARGET e. Hence RETE_F(v, e) ≤ WCH_F(e) (to prove), and RETR_F ≤ max_e WCH_F(e) · (max in-degree) (to prove).
  - That is the per-vertex WCH premise again, the one GAP-RED already uses. So the decision potential closes the REP circle iff
    per-vertex W-changes per W-run are polynomial. This would be a REDUCTION of REP* to per-vertex WCH, not a bound. It is to be proved
    next box if the Lead wants it.
- Odd side: RET_F is not needed for the circle once the Even split is used. Odd's leapfrogs are breadth (§1).

## DONE / FINDINGS / NEEDS
- DONE: box76/climb_sbq.py, sbqrun.py, run.sh, sbqrun_*.txt (1132 × 2), inst/cs_n32, cs_n80, csz_n24, out/ logs; this note; check.sh
  "box 76".
- FINDINGS:
  1. DEAD: CONJECTURE SBQ-2. cs_n32 (sha1 bff52a58…) has 173 = 5.4n σ̄-changes in one 9-step W-run; N5-LZC csz_n24 has 110 = 4.6n.
     Reason: breadth, mostly returns (116 / 173), i.e. Odd leapfrogging between options it already used.
  2. PROVED (lane): NEW-BOUND. NEW_F ≤ m_O and NEWE_F ≤ m_E, so |F| ≤ m_E + RETR_F (all-return transitions).
  3. DATA: Odd returns ≤ 0.66n per run and Even returns ≤ 1.47n per run on the corpus; the longest W-run is 2.0n (runfam_K40).
  4. CONJECTURE (proposal): RETR-POLY, the next non-growing link. Route: an Even return is paid by a strict W-rise of its target
     (RETE(v, e) ≤ WCH_F(e), to prove). That reduces REP* to per-vertex WCH (GAP-RED's premise): one premise for both.
- NEEDS: none from the owner. From the Lead: go / no-go on proving RETE(v, e) ≤ WCH_F(e) (N5-LZC first, then N5 with TIE) as the next box.
