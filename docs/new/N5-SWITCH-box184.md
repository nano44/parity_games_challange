# Box 184 N5-SWITCH: the Ξ-channel cost of a switch — DATA: every non-ISO 𝓛^R_3 run exceeds the ISO frame value T_C(2) by at most 1 (≤ the number Z of switch steps), frozen non-ISO frames never exceed T_0 (RELAY-FREE), and the narrow «renewal through the switched mover» count does not explain the excess; CONJECTURES SWITCH-Z and RELAY-FREE; no proof
L-NEW successor 56, 2026-11-06 (from 14:30Z by date -u; see the commits). Lead brief BOX 184 (14:31Z): bound U(segment after a switch) by
T_0(frozen genome) + f(|P(switch)|), P(switch) = the upper options whose chains pass through the switched level-0 mover; measure the
slack on now1_d3_5 / one_d3_6 / dbl_d3_F6 and the d 4 corpus; prove it or kill it. Premises: box 183 NONISO-FRAME (lane); R110
definitions (T_k, c-step, ISO); the exact T_0/1/2(2) = 4/5/7 (SAT, L-COMP 27 / box 160, lane DATA). Labels as before. Not a TARGET.md
claim. G-N5-TIME stays OPEN.

## 0. Answer
- The literal form is trivially true with f = 0 and says nothing new. By NONISO-FRAME, a segment between switch steps IS a run of
  the frozen genome G_q, so U(segment) ≤ max_start T(G_q). The content lies in comparing with the ISO frame values T_C(d − 1), against
  which runs are measured in R110. Two quantities matter: frozen frames with relays (RELAY-FREE), and the cost of the switch steps
  themselves (SWITCH-Z).
- DATA (box184/switchcost.py, every start of every in-tree 𝓛^R_3 / 𝓛^R_4 file; log/switchcost.txt). Excess := U − T_C(d − 1), with U
  the steps changing the levels ≥ 1 and C the b_0 changes, as in box 183.
  - d = 3 (exact frame values): 3,968 runs (3,072 ISO, 896 non-ISO). Max excess 1, in 4 runs, all non-ISO (dbl_d3_F6@111101 twice,
    now1_d3_5@001110, one_d3_6@110110); ISO runs max excess 0. H-Z (excess ≤ Z, Z = #switch steps): 0 violations. H-P (excess ≤ Σ
    |P(switch)|): 0 violations. H-REN (excess ≤ #movers newly Ξ-unhappy at a switch step through the switched mover's chain): 1
    violation (one_d3_6@110110: movers 4, 5 become Ξ-unhappy at the switch step 3, which also moves 3, but neither one's other option has 0 on
    its chain under s_2, so the REN test does not count them). So the excess is not «one per renewal through 0 / 1».
  - d = 4 (proxy: excess against the LOWER bounds T_C(3) ≥ 8, 10, 12; a positive proxy is not a violation): 16,384 runs; max proxy excess
    1 (6 non-ISO runs, e.g. max_d4_L13@11000101: U 13, C 2, Z 2, Σ|P| 9, REN 1); ISO max 0.
- DATA (box184/relayfree.py; log/relayfree.txt): every non-ISO 𝓛^R_3 / 𝓛^R_4 file, every q ∈ {0, 1}², the frozen genome G_q from every
  start: max T = 4 = T_0(2) over 56 frozen frames at d 3; max T = 8 (= the lower bound of T_0(3)) over 68 at d 4. Static relays (upper
  options pointing to the frozen 0, 1) add nothing in the corpus.
- CONJECTURE RELAY-FREE (lane): for every frozen genome G_q of 𝓛^R_d (any Ξ), max_start T(G_q) ≤ T_0(d − 1).
- CONJECTURE SWITCH-Z (lane): for every run of 𝓛^R_d (any Ξ), U ≤ T_C(d − 1) + Z, with C the b_0 changes and Z ≤ 2 the switch steps.
  With NONISO-FRAME: T^R(d) ≤ T_2(d − 1) + 4. So FLIP-ADD on the ISO frame (T_2(m) ≤ T^R(m) + O(m)) would give T^R(d) ≤ T^R(d − 1) +
  O(d), i.e. T^R(d) = O(d²). SWITCH-Z is the precise statement that the non-ISO channel costs O(1) per switch.
  Kill: one run with excess ≥ Z + 1. At d 3 this is settled by the exact T^N_k(2) query routed to L-RED R213: SWITCH-Z at m = 2 ⇔ the
  exact non-ISO upper maxima are ≤ T_C(2) + Z.
- Why no proof (READING). At a switch step, the Ξ-values of options through 0 / 1 jump (MONO), and the A-sets above change in a way no
  c-step of a single ISO genome reproduces. The excess-1 runs show the switch step itself carrying upper moves that an ISO frame would
  need an extra step for (now1_d3_5 step 1 moves 0 and 4 together; dbl_d3_F6 steps 4 and 6 move 1 with 3 and 0 with 3). A proof would
  have to exhibit an ISO genome and a c-sequence with C changes reproducing every non-ISO segment up to one step per switch. I see no
  such simulation: SWAP (R110) handles the key bit, but there is no Ξ-analogue (an option's β-set cannot absorb the switched mover's β
  without breaking the comparisons of other options that share it; box 183 §0).

## 1. Files (experiments/new/box184/)
- switchcost.py (U, C, Z, Σ|P|, REN, excess per run; H-Z / H-P / H-REN counters at d 3); relayfree.py (frozen frames). Logs in log/.
