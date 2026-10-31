# N5-CORE-SYNTH (box 104 (b), L-NEW successor 40's parking note): what remains of G-N5-TIME inside a W-run, as one statement: XI-CH-POLY. Every per-W-run route tried in boxes 84-104 is either an equivalent face of it or DEAD with an instance
L-NEW successor 40 (Opus 5.5), D14 / D18, Lead reading L40. Lead 23:41Z: «(b) … a short synthesis …: what exactly remains after R94-R95 +
SETTLE/SRC + boxes 84-103 + R135-R150, as one statement. Then park with FINAL.» Written 2026-10-30 23:5xZ (date -u).
- Working note, unrefereed. Labels: PROVED (landed / lane) / CONJECTURE / DEAD / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Scope: what I opened this session. I did NOT re-derive the across-W-run counts (RESULTS R90 CUT-RED's B*, REP*, SC*, O*; R94's phase
  reductions). §3 only quotes them, and the Lead owns that reading.

## 1. The one statement (inside a W-run)
- XI-CH-POLY: there is a polynomial p such that, in every W-run F of every N5 run on every game, every vertex c has ΞCH_F(c) ≤ p(n).
  ΞCH_F(c) counts the transitions of F changing Ξ(c).
- Equivalent (LANDED, RESULTS R95 Corollary WRUN-EQ, line L-5): WRUN-POLY ⇔ XI-CH-POLY ⇔ P*-POLY ⇔ DEEP_k-POLY ⇔ R*-POLY ∧ FL-POLY ⇔
  ALT-POLY ∧ FREE-POLY ⇔ R3-POLY ∧ TIE-POLY ⇔ R*-POLY ∧ [P-INT] ⇔ SB-POLY ∧ R°-POLY ∧ FL-POLY.
- Further faces proved this session (PROVED, lane, unrefereed):
  - HEAD-RED′ (L-SI box 53; P-N5-SETTLE): ⇔ CN, own-node flips and Ξ-changes at U ∪ τ(Odd) all polynomial.
  - PAY (box 98): |F| ≤ (m_E − n_E) + RETT_F.
  - CASCADE-EQ, with FRESH-ROOT (boxes 99-100): ⇔ CASC-POLY, the returns rooted at one fresh Even entry.
  - DEPTH-SUB (box 103): root depth D ≤ (n − 1)(R*_F + 1) + FL_F. Redundant with WRUN-EQ.

## 2. What the residual looks like (DATA, the mechanisms seen)
- Quadratic W-runs (sbq2, obs, latew; L-RED R127 / R138 / R145):
  - one Even clock vertex makes K fresh ticks (out-degree K + 1, period m + 3);
  - each tick re-opens every observer once (≈ 3m returns);
  - all returns are FREE (box 84 class); no head order ever recurs (box 98).
- Order / type recurrence (gate_K, pp_K): pure edge consumption (no Even edge is re-entered), paid by m_E (box 98).
- Deep relays (topfix_N): a rotating Even triple, one transition back per step, root depth 6N − 11, width 1 (boxes 100, 103; box 96's
  stubborn triple).
- Feedback (cedge_n32, L-RED R150): a time-varying loop of plays ({7, 20, 26}) returns one X 4 times under one root (box 104 (a)).
- No super-polynomial W-run is known. The largest growth seen is quadratic (K·m). No counter (unbounded depth × width ≥ 2 per level) has
  been built: L-RED's ARENA-MAX / SETTLE obstacles stopped every attempt so far (R140, R148-hxs).

## 3. The other half of G-N5-TIME (quoted, not re-derived)
- RESULTS R90 (CUT-RED, GAPS line-11 UPDATE 2026-10-30 05:17Z): T ≤ 2n(n−1) + (n(n−1)+1)·(m_E·[1 + 2B* + (B*+1)·K] + SC* + O*), with
  K := n(n−1) + (n(n−1)+1)(n−1)(m_E + REP* + 1). So G-N5-TIME ⇔ B*, REP*, SC* and O* are polynomial.
  - REP* is the per-W-run REPEAT late adoptions, an R* face.
- READING (mine; the Lead should check it against R90 / R94):
  - the W-run side of R90 is XI-CH-POLY's R*-face;
  - the across-W-run side (B*: fallbacks and τ-changes per λ-run; SC*, O*) is bounded on 𝒞^kO by R61 / box 94 kO-RED (O(n^{2k+3}) W-runs);
  - it is open in general.
- So, as one statement: G-N5-TIME ⇐ XI-CH-POLY ∧ (across-W-run counts of R90 polynomial). On 𝒞^kO the second conjunct holds (box 94), so
  there G-N5-TIME ⇔ XI-CH-POLY (box 94 kO-RED).

## 4. Dead ends of this session (each with its instance; details in the box notes and notes/L-NEW.md)
- ORDER-DET U-form: n5s_maxph_0 (box 97).
- NO-REPEAT: thetaA_n7. SB ≤ f(order-set size): gate_K16 → K64 (box 97).
- Head-order returns as the bottleneck: refuted by data. The quadratic families have none (box 98).
- CASCADE-LIN: L-RED R148, cascl_K4_m8_N100.
- Root depth O(1): topfix_N (box 100). Box 99's «depth ≤ 2» was a tool bug.
- NARROW: L-RED R149, narrow_n10 and casctf_n10_N210.
- Once per root: obs_K12_m24. Edge O(1) per root: topfix_n10. Left-target injection: pftheta34_n32 (box 101).
- Overtake once per root, and the pair injection: pftheta34_n32 (box 102).
- Depth ≤ f(distinct chain vertices): topfix_N. Chain nodes always W-changing: u23sw64_n32 (box 103).
- CASC-EDGE: L-RED R150, cedge_n32.
- Self-fed split: cedge_n32. Self-fed ⇒ W(X) change: tog6b_n32 (box 104).

## 5. What I would try next (READING, for successor 41 or the Lead)
- The cedge loop is the first instance where one root re-opens one X more than deg X times. Its object is the UNION OF PLAY GRAPHS over a
  root's window. A lemma «a root's wave traverses each loop of that union O(1) times» would give CASC-POLY. L-RED's growth question is
  whether cedge's loop can be nested (a counter).
- If cedge nests, W-runs are super-polynomial and N5 dies on step 4. If it cannot, the obstruction (probably ARENA-MAX: S4a picks Even's
  arena optimum against τ, which damps re-circulation) is the lemma to prove.
- Either way the next decisive object is L-RED's attempt to nest cedge.

## DONE / FINDINGS / NEEDS
- DONE: this note (parking synthesis).
- FINDINGS: the W-run residual is exactly XI-CH-POLY. All tried per-W-run routes either reduce to it or are DEAD with instances (§4). The
  decisive open question is whether cedge's loop nests (§5).
- NEEDS: none from the owner. Lead: route «nest cedge_n32» to L-RED as the decisive test.
