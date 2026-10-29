# N5-PIECECAR (box 50): carries per vertex per phase against σ̄-changes. DATA: they live inside σ̄-frozen pieces (G = 0); what blocks a bound in G; the VC route
L-NEW successor 31 (Opus 5.5; D14, D18, Lead reading L40). Lead's word 2026-10-29 12:01Z: «New proof target: CARRIES PER VERTEX PER PHASE ...
Goal: a polynomial bound on carries (or on Even switches) per phase in terms of n and the number of σ̄-changes in the phase, or a precise
statement of what blocks it. ... Data first: runquad / s3quad (claude/l-red) and the library.» Working note, unrefereed, not frozen. Not a
TARGET.md claim; G-N5-TIME stays OPEN. Labels: PROVED (lane) / CONJECTURE / OPEN / DATA / DEAD / READING.
Tools: experiments/new/box50/piececar.py (carries per vertex per phase and per PIECE), vcrun.py; logs box50/pc_alt.txt, runquad_vc.txt.
Definitions: a PIECE of a phase P is a maximal stretch of its transitions with σ̄ unchanged. The σ̄-changing transitions are the CUTS, and
G(P) is their number. NM_P(v) is the number of carries of P(Ξ v) in P (L-LIT's MPGS (A); box50/fbcarry.py `kind`). CPIECE is the most
carries of one vertex inside one piece.

## 1. DATA
| instance / corpus | phase | G(P) | phase length | max NM_P(v) | max CPIECE | n |
| --- | --- | --- | --- | --- | --- | --- |
| runquad_K3_m4_n54 (L-RED; copy at claude/l-si experiments/si/chg/instances/red/) | [0, 20] | 0 | 20 | 3 | 3 | 54 |
| runquad_K8_m30_n192 (L-RED R106) | [0, 263] | 0 | 263 | 8 | 8 | 192 |
| dlsep_kill_n70 (L-SI chg/instances) | [0, 12] | 8 | 12 | 5 | 1 | 70 |
| alt_all, default starts (pc_alt.txt), 454 phases | b5_os_n24 [0, 49] | 0 | 49 | 11 | 11 | 24 |
|  | b5_os_n28 / n32 / n40 | 0 | 60 / 67 / 77 | 11 / 10 / 11 | same | 28 / 32 / 40 |
|  | xsn91_n48 [3, 115] | 14 | 112 | 18 | 10 | 48 |
| alt_all overall | | ≤ 52 | ≤ 112 | ≤ 31 | ≤ 11 | |
- READING of the table: the largest carry counts per vertex sit INSIDE a single σ̄-frozen piece (G(P) = 0) in runquad and in the library
  family b5_os. So no bound of the form c·(G(P) + 1) holds with c constant, and any bound poly(n)·(G(P) + 1) must already be poly(n) when
  G(P) = 0. DEAD: "a vertex carries O(1) times per piece", by runquad K3 → K8 (3 → 8 = K) and b5_os_n24 (11 in one piece of 49 at n 24).

## 2. What blocks a bound in G (precise; READING built on landed results)
- On a piece, σ̄ is fixed. So Ξ_t is the value of σ_t in the ONE-PLAYER game G_σ̄ (Odd vertices cut to σ̄), and every Even switch is an
  improving switch of G_σ̄ (SPEC S2 with σ̄ fixed). Under switch-best in G_σ̄, RESULTS R17 (b)-(c) would give ≤ n − 1 value-changing steps per
  λ-phase. But N5's step picks the W-optimum against τ (S4a), so it is a different pricing rule. R17's own honest limit (ii) records that Lemma P is FALSE for N5's Even
  moves inside a σ̄-segment (seg_r16, seg_n24) and that the count does not transfer (vc_g25: 26 value-changing moves in one segment-phase
  at n 25). R17 (f) records that for arbitrary single switches the O(n³) statement is false (CDAG_n).
- So the σ̄-frozen case is exactly L-SI's two-LP pricing problem: Ξ (against σ̄) filters the arena, W (against τ) chooses. A bound in G
  needs a statement about that rule which no landed lemma gives. L-SI's COMPOSE reduces the phase to P-changes and carries. MATCH-Φ
  reduces P-changes to carries. INHERIT locates the carries at Even switches. None of them bounds the number of carries made inside one
  σ̄-frozen piece.

## 3. A route that does not depend on G: VC-BOUND per phase (P-N5-VC (b), frozen 21f3285a)
- PROVED (lane, elementary, from P-N5-VC): NM_P(v) ≤ PCH_P(v) ≤ len(P) = |F_σ(P)| − 1 ≤ Φ_dσ(P)(m_σ(P)) − 1 for every vertex v and
  phase P. A carry is a P-change, and a P-change is a transition of P.
- DATA (runquad_vc.txt; L-RED's generator mkr.py at claude/l-red experiments/red/seg/, run from a scratch copy; S-start = its .start):
  | (K, m) | n | phase length | run ENT (= K) | phase VC dσ(P) |
  | --- | --- | --- | --- | --- |
  | (3, 4) | 54 | 20 | 3 | 3 |
  | (6, 12) | 114 | 89 | 6 | 3 |
  | (10, 10) | 156 | 129 | 10 | 3 |
  | (12, 4) | 162 | 83 | 12 | 3 |
  | (16, 4) | 210 | 111 | 16 | 3 |
  | (20, 4) | 258 | 139 | 20 | 3 |
  | runquad_K8_m30_n192 | 192 | 263 | 8 | 3 |
  dlsep_kill_n70: phase VC 2. b5_os family: phase VC ≤ 4 (alt_all maximum, P-N5-VC §3).
- So on the family built to make carries per piece grow, everything that grows (phase length, per-edge re-entries, carries per vertex,
  piece length) grows while the phase VC stays 3. With CONJECTURE VC-N5 in its phase form (dσ(P) ≤ c), the bound above is
  NM_P(v) ≤ Φ_c(m) − 1 = O(m^c), polynomial and independent of G(P).
- Precise statement of the block: a polynomial bound on carries per vertex per phase follows from the phase form of VC-N5, which is OPEN.
  A bound in G(P) alone is impossible with a constant factor (§1) and blocked in general by the σ̄-frozen two-LP pricing case (§2).

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box50/piececar.py; logs pc_alt.txt, runquad_vc.txt.
- FINDINGS: (1) DATA: the largest per-vertex carry counts occur inside σ̄-frozen pieces (G(P) = 0): runquad K3 → K8: 3 → 8; b5_os_n24: 11
  in one piece of 49 transitions at n 24. DEAD: O(1) carries per vertex per piece. (2) Block (READING): the σ̄-frozen case is two-LP pricing
  on the one-player game G_σ̄; R17's Lemma P fails there (its own honest limit (ii)). (3) Route: NM_P(v) ≤ Φ_dσ(P)(m) − 1 (P-N5-VC); the phase VC
  is 3 on all of runquad K = 3..20 while phase length, ENT and NM grow. The open count is the phase form of VC-N5.
- NEEDS: none from the owner.
