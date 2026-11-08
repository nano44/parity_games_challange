# Box 89: MULTIPLY on D_U at a bit's waiting hub, SET side (L-SI successor 46; Lead 15:27Z 2026-11-08)
Written 2026-11-08 (date -u in the commit). Labels: PROVED (lane) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD (instance) / READING.
Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).
Tools: experiments/si/box89/ (du89.py = D_U at each real bit's w; climb89.py = climb on D_U at w; check89.sh, wired). Also box88's leap88.py
(two edge cases fixed: b = ∅ and a = b at an event; the latter is now counted as «f2fail» and printed only when nonzero, so box 88's
outputs are unchanged) and nest88.py; L-NEW's asc197.py at claude/l-new f98e93ee (fixed alternation counter), run read-only from a scratch
extract. Scope of every run: box81/ref idealcyc (IDEAL-CYC Howard, [E-LEV]), cap 3000; T3 from asc197's Γ3 run (equal to T on every row).

## 0. Answer (decision owed: does D_U at w grow super-linearly in the tower height?)
- NO on everything measured. No candidate against ALT-POLY. PARTIAL box: the DESIGNED tie-decided-carry gadget was NOT built (§3 says
  why the design is blocked and what it would need); the measurable step was climbs whose mutations include downward (carry) routes.
- The exact obstruction to the QUESTION as posed is elementary: **D_U,I(w) ≤ |I| + 1 ≤ T3 + 1** (PROVED, trivially: one value per state).
  So «D_U at w super-linear» IS «T super-linear» on the same family; the climbs below push D_U(w) up to T (DU21_h4: 21 of T = 24) without
  raising T. The real target is T, i.e. L-RED's (a).
- Mechanism on MIRROR (DATA, trace §2): the U-projected e-set of w_1 contains ONLY SET e-vertices of the bits and mirrors on w_1's route
  (lane e-faces have dummy W-targets, so Odd never takes them). It is a configuration of set bits along a route (BIN's «route to the next
  set bit», L-RED R225 §2) and changes ADDITIVELY: D_U(w_1) = 2 / 5 / 8 / 12 at h = 2-5 (+3 to +4 per level).
- A ≤ 5 on every new instance (asc197 f98e93ee); the earlier 6s (NK6_cl21, HP5t) are unchanged by the counter fix.

## 1. DATA (unit = genome; counters du89 (D_U per maximal constant-node interval, max over I), nest88 (N2 / switch-depth), asc197 (A, T3))
| instance | h | N + M | T = T3 | D_U(w_1) | max_l D_U(w_l) | A | N2 / switch-depth |
| --- | --- | --- | --- | --- | --- | --- | --- |
| HP2_mup (box 84) | 2 | 109 | 11 | 2 | 2 | 2 | 0 / 0 |
| HP3_mup | 3 | 215 | 17 | 5 | 5 | 4 | 1 / 1 |
| HP3t (box 88) | 3 | 215 | 17 | 5 | 5 | 4 | 1 / 1 |
| DU9_h3 (climb89 seed 2893 from HP3t, 1500 iterations) | 3 | 215 | 18 | 9 | 9 | 5 | 13 / 3 |
| HP4_mup | 4 | 537 | 37 | 8 | 8 | 4 | 5 / 2 |
| HP4t (box 88) | 4 | 639 | 24 | 9 | 9 | 5 | 6 / 2 |
| DU21_h4 (climb89 seed 2894 from HP4t, 600 iterations) | 4 | 639 | 24 | 21 | 21 (w_3: 18) | 5 | 48 / 8 |
| HP5_mup | 5 | 877 | 43 | 12 | 12 | 5 | 11 / 2 |
| HP5t (box 88) | 5 | 1039 | 71 | 14 | 14 | 6 | 13 / 2 |
- Fit: on the MIRROR towers D_U(w_1) is linear in h (2, 5, 8, 12). The climbs raise it at fixed size by making w's set change at almost
  every step (DU21_h4: D = 21 of 25 states) and do NOT raise T (24 → 24; 17 → 18). So no growth in the only quantity that matters.
- leap88 (ALL) on the climb bests: DU21_h4 maxk 4, maxdepth 3, maxev 5; DU9_h3 maxk 2, maxev 5; chargefail 0, ascfail 0. f2fail 1 / 4:
  events where a_t = b_t, i.e. units outside F2's hypotheses (PRIV / NODE); NEST-CHARGE does not claim them.
- FINDING for L-RED 60's NEST-POLY (weak form «switch-depth ≤ c»): DU21_h4 has switch-depth 8 and N2 48 at T 24 (L-RED 60's data: ≤ 3).
  The depth is bounded by T here, so this refutes nothing polynomial, only the constant 3 as an empirical ceiling.
- Frozen: box89/inst/DU9_h3.json, DU21_h4.json (+ names), sha1 in box89/pins.sha1.

## 2. The trace (HP4_mup, w_1 = W-target of B_1's SET; U-projection at rank(e_SET(B_1)))
states 0 / 4 / 23 / 25 / 33 / 34 / 35 / 36: ∅, {M2, M3}, {B4}, {M2, B4}, {M2, M4}, {B3, M4}, {M3, M4}, {M2, M3, M4} (SET e-vertices).
Each change is a flip of one SET mover on the route or a re-route; no value pattern repeats after a higher change (no replay).

## 3. Why the designed multiply was not built, and what it needs (READING)
- A multiply at w_l needs every change of the High (the part of w_l's set at levels > l + 1) to reach the two compared plays of B_(l+1) at
  DIFFERENT times (a lag), so that each High value yields an OFF and an ON of B_(l+1) (CX4's race, made at a SET bit), and w_l's route to
  pass B_(l+1) and then the High. Then D(w_l) ≈ 2·D(w_(l+1)).
- That race needs the High to HOLD each value for at least the lag (L-RED R225 §5 READING). Feed-forward, the holds must double per level,
  so the delay lanes grow like 2^h and T stays polynomial in N (Ξ-acyclic genomes: ACYC-LIN, box 81, PROVED: T ≤ N).
- The only escape is a CARRY: the High waits for the low race to finish. By CARRY-TIE (box 88 §3, PROVED) a carry must be a Π_r-tied
  choice at a Howard switch, decided by lower data. Tie decisions are everywhere (box 88), so CARRY-TIE does not forbid it; but I have no
  construction in which a tie-decided switch at level l + 2 waits for the race at level l + 1 AND then changes the High (a tied switch
  changes nothing at ranks ≥ r by definition; it must change the set seen one level down only). This is the open design step.
- CONJECTURE (READING; the SET-side form of L-RED's ADD / NEST-POLY): on IDEAL-CYC under [E-LEV], max_l D_U(w_l) ≤ poly(N + M) for every
  genome; equivalent here to T polynomial (D_U ≤ T + 1, and T ≤ poly(Σ D) by EQUIV). Strongest DATA: the table above (h ≤ 5, T ≤ 71).
