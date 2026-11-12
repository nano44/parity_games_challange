# Box 99: U-FREE from the proof side: reduction to one SCC (Lemma SCC-RED), Lemma CAP, CONJECTURE SCC-LIN
L-SI successor 50 (Opus 5.5), D18 / D14 / D1; Lead 2026-11-12 00:04Z («try to turn U-FREE into a lemma from the proof side … state exactly
where Howard's greed blocks an odometer on a hub's e-sets») and 05:09Z. Labels: PROVED (L-SI lane, unrefereed) / CONJECTURE / DATA (unit,
set, scope, counter) / READING. Not a TARGET.md claim; not M3 or M4; not a gauntlet step; G-N5-TIME stays OPEN. L-RED 65 attacks it.

## 0. Answer
- U-FREE is NOT proved. What is proved (lane):
  - Lemma SCC-RED (§2): on N5′-xi's mover phase, T3 ≤ max over chains C_1 → … → C_r of SCCs of the mover graph D(G) of Σ_i (H(C_i) + 1),
    where H(C) is the longest Howard run inside C with every exit of C held constant. This extends L-RED 64's SCC-CHAIN (H = 0 or
    deg − 1 for a single mover) to every SCC.
  - Corollary SCC-RED ⇒ U-FREE: if every SCC C has H(C) ≤ M_C (its own options), then T3 ≤ M + N, i.e. U-FREE (T3 ≤ N + M + 4) holds.
  - Lemma CAP (§3): the value of a mover's option is at most what its β-face observes; a direct reading of LOC-GATE3 (RESULTS R125).
- So U-FREE reduces to CONJECTURE SCC-LIN (§4): Howard inside ONE strongly connected component of D(G), with constant exits, makes at
  most M_C iterations. An odometer on a hub's e-sets would have to live inside one SCC with its exits already final (§5).
- DATA (§4): the measured local length loc(C) never exceeds M_C + 1 (locfail 0) and the chain bound holds (chainfail 0) on 26 frozen
  instances and 600 random genomes; the largest ratio loc(C) / M_C is 0.8 (C98_2_2_3, N 4) and ≤ 0.33 at N + M ≥ 100. Two kinds of long
  run: the MW, FW and Ku families are long through the SCC CHAIN (local length ≤ 2 per SCC; FW8_2: 123 single-mover SCCs, T3 29), so
  SCC-RED alone explains them; the MWR, C6G8, DHIB families run inside ONE giant SCC (MWR16_2: 152 of 156 movers, loc = T3 = 102), and
  there SCC-LIN is the whole content of U-FREE.

## 1. Setting and premises (by R-id)
- RESULTS R125 (P-N5-CHAIN): N5′-xi from S3 on Γ3(G) is a Howard run at the movers (HOW3(G)) until its first fallback at T3 + 1, for every
  genome (REACH3-ALL); non-mover Even vertices are frozen in its states; LOC-GATE3, NO-TIE3 (Odd at a gate plays the strictly ◁-smaller
  face); F1 (values never fall); RESULTS R15 (a) (a switch set of improvements does not lower any value).
- D(G) (L-RED 64, R230 §2): one node per mover; an edge x → y for every option of x with W-target y or Ξ-target y (a mover).
- From a mover x the play under any positional pair visits only movers reachable from x in D(G), their gates, pads, β's and e's, the
  closed core and c_W (R104's edges: a mover's options are its gates; a gate's faces lead to its e (then the W-target) and its β (then
  the Ξ-target, or u)).

## 2. Lemma SCC-RED (PROVED, lane; extends L-RED 64's Lemma SCC-CHAIN, claude/l-red 0e74d179)
- For an SCC C of D(G): exits(C) := the movers outside C reachable by one edge from C. H(C) := the maximum, over all strategies of C's
  movers at the start, of the number of iterations of the Howard run (HOW3's tie rule) of the game in which every mover outside C is
  fixed at an arbitrary strategy that is final for it. f(C) := the last state at which some mover of C switches (0 if none).
- Statement: f(C) ≤ max_(C′ reachable from C, C′ ≠ C) f(C′) + H(C) + 1, hence T3 ≤ max over chains of SCCs of Σ (H(C_i) + 1).
- Proof. Let t0 := max f(C′) over ALL SCCs C′ ≠ C reachable from C (0 if none); from t0 on every mover reachable from C outside C is
  final, by the definition of f. (Direct successors alone do not suffice: a deeper SCC may switch after a direct successor has stopped,
  and its switch can change C's values.) The values of
  C's movers' options at a state t ≥ t0 depend only on the strategies of movers reachable from C (§1), so they are the values of the
  game G_C in which those outside movers are fixed at their final choices. HOW3 switches every mover with a strictly better successor
  to a ⊴-best one, by values that depend only on that game; so the states t0, t0 + 1, … restricted to C form a Howard run of G_C from
  the strategy at t0. It ends within H(C) iterations, after which no mover of C switches. So f(C) ≤ t0 + H(C) (+ 1 for the step at t0
  itself). Chain bound: put F(C) := H(C) + 1 + max_(C′ ∈ succ(C)) F(C′) (0 for an empty max). F does not increase along reachability
  (F(C′) ≥ F(C″) when C″ is reachable from C′), so by induction from the sinks f(C) ≤ max_(reachable C′) F(C′) + H(C) + 1 = F(C), and
  F(C) is a sum of H + 1 over one chain. T3 = max_C f(C). ∎
- Special cases: a single mover without a self-loop has H = 0 or 1 (one switch to its best option, as in SCC-CHAIN); with a Ξ self-loop,
  H ≤ deg − 1 (its values depend on its own choice only; each switch raises V(x), RESULTS R15 (a)). So SCC-CHAIN is SCC-RED with these H.
- Corollary. If H(C) ≤ M_C for every SCC C, then T3 ≤ Σ_C (M_C + 1) ≤ M + N (each mover lies in one SCC; at most N SCCs).

## 3. Lemma CAP (PROVED, lane; L-RED 64's CAP, R230 §4, made precise)
- For a mover x, an option k with gate g_k, e-face pad pe_k and β-face pad pβ_k, at every state t of HOW3(G):
  Ω_t(g_k) = min⊴(Ω_t(pe_k), Ω_t(pβ_k)), so ext(m_(x,k), Ω_t(g_k)) ⊴ ext(m_(x,k), Ω_t(pβ_k)).
- Proof: LOC-GATE3 / NO-TIE3 (RESULTS R125): Odd at g_k plays the strictly ◁-smaller face; the gate's value is its face's value extended
  by g_k, which is in no Π (CN2-3), so the order is kept (F4′). ∎
- Reading: an option can lift x at most to what its β-face observes (β_k, then the Ξ-target's play); x gains its own e-item e_k only when
  the observed β-face play is already ⊵ the e-face play. This is the first half of L-RED 64's blocking argument; SELF-SIGHT and RACE-BUDGET
  stay READINGS (R230 §4), unproved: they need «leader» and «observer» defined for a general SCC.

## 4. CONJECTURE SCC-LIN and its DATA (experiments/si/box99: scc99.py, run99.sh; engine L-NEW gamma3 / n5v at l-new fcba92fc)
- Statement: for every genome G and every SCC C of D(G), H(C) ≤ M_C (Howard inside C with constant exits makes at most as many
  iterations as C has options). By §2 it implies U-FREE (T3 ≤ M + N).
- What is measured: on the actual run (not the maximum over starts), loc(C) := max(0, f(C) − e(C)), e(C) := max f over all SCCs
  reachable from C; locfail := SCCs with loc(C) > M_C + 1; chainfail := genomes with T3 above the SCC-RED chain bound with loc in place of H (a check
  of §2's bookkeeping; must be 0).
- Results (out/inst99.out, out/rand99.out; unit SCC for locfail, genome for chainfail): locfail 0, chainfail 0 on box 91's 11, box 93's 8,
  box 98's 7 climb bests (26) and on 600 random genomes (rand191.rgen, seed 9901). Max loc / M_C over non-trivial SCCs: 0.8 (26 frozen;
  C98_2_2_3), 0.667 (random). Per family: MW8_2 / MW32_2 T3 55 / 199 with 83 / 299 SCCs, max loc 1; FW8_2 / FW16_2 T3 29 / 53, all SCCs
  single movers, max loc 1; Ku_4 / 8 / 16 T3 28 / 52 / 100, max loc 2; MWR4_2 / 8 / 16 T3 30 / 54 / 102 in one SCC of 44 / 80 / 152
  movers, loc = T3, loc / M_C 0.33 / 0.32 / 0.31; C6G8_n54, RWX_n95, DWT20_2803, DHIB26_2804, DHIB18_2805: one SCC of 50-102 movers, loc / M_C
  ≤ 0.12.
- Context DATA from other lanes (quoted, not re-run): L-COMP 17 (claude/l-comp 61d04877, box38): Ttot = T3 + 3 on 376 two-engine runs, U
  0-216; max T3 flat in U (exhaustive at N + M ≤ 8: max T3 0-2 at every U); removing all upward Ξ-edges changes T3 by ≤ 4; a
  U-constrained climb in the band [140, 160] gives T3 33 / 32 / 34 at U ≤ 0 / ≤ 2 / free. L-RED 64 (claude/l-red 0e74d179, R230-odo): the
  hand-built two-source odometer gives T3 ≈ m + k + O(1) (ODO(16, 16): T3 41 at N 36, M 82); its [E-LEV]-violating climbs at U = 2 stay
  linear (5cc17d8d).

## 5. Where Howard's greed blocks an odometer (READING, with what is proved marked)
- PROVED (SCC-RED): any run longer than Σ_chain (M_C + 1) needs an SCC C whose own Howard run, with its exits already final, is longer
  than M_C. So an odometer on a hub's e-sets must run inside one SCC, AFTER everything it observes outside C has stopped moving.
- PROVED (CAP): inside C, a hub's option is capped by its observed β-face play; it can only climb to what some other mover of C already
  shows it.
- READING (L-RED 64's SELF-SIGHT, RACE-BUDGET; not proved): a hub whose observer passes through itself climbs one option per iteration
  without pause, and a reset of a domino needs a rival that pays one of its own options per iteration of the domino. Greed is the point:
  a Howard step moves every mover at once to its best option, so a «stall» would need an option that becomes improving only after a
  delay, and that delay is itself a domino inside the same SCC, paid in options again. No stall that is not paid in options is known.
- The open step, stated exactly: bound the number of Howard iterations of the game G_C (one SCC of D(G), exits constant) by M_C, or by any
  polynomial in M_C. That is SCC-LIN; nothing here proves it.

## 6. Sources opened (this box)
- claude/l-red 0e74d179 docs/red/R230-odo.md (§0-§6); L-COMP 17's box38 summary as relayed by the Lead (02:43Z; not opened here: cited as
  relayed); docs/RESULTS.md R125 (trunk 0753fd71), R15 (a); box 97 / box 98 records.

## Addendum A (L-SI successor 51, 2026-11-12T08:01Z (date -u); append-only, §0-§6 unchanged): GAP G1 (tie rule in H(C)), fixed
- Source: L-RED 65, claude/l-red 59daaef2 docs/red/R232-box99.md §1 «GAP G1 (wording; affects what SCC-LIN must bound)», relayed by the
  Lead 08:01Z. R125's HOW3 is «every mover moving to a ⊴-best successor and keeping a best current one» (R232 §1, quoted from RESULTS
  R125): when the current successor is not best, ANY ⊴-best successor is legal. §2 above defined H(C) with «HOW3's tie rule», which
  names no single rule. DATA (L-RED's, not re-run here): L-RED's own HOW3 engine and n5v differ in T3 by ±1 on 7 of 400 random genomes
  (seed 2321), the four inspected all with tie events.
- Corrected definition (replaces the one in §2 wherever H(C) is used, including §4's CONJECTURE SCC-LIN):
  H(C) := the maximum, over every start strategy of C's movers, every assignment of final strategies to the movers outside C, and every
  HOW3-legal tie resolution at every iteration (each mover whose current successor is not ⊴-best moves to SOME ⊴-best successor; a mover
  whose current successor is ⊴-best keeps it), of the number of iterations of that Howard run of G_C.
- Lemma SCC-RED's proof is unchanged under this definition: the states t0, t0 + 1, … of N5′-xi's run restricted to C are ONE HOW3-legal
  run of G_C (N5′-xi's S4a choice is one legal tie resolution), so their number is ≤ H(C) for the maximum above. The corollary
  (H(C) ≤ M_C for all C ⇒ T3 ≤ M + N) is unchanged. SCC-LIN is now the stronger statement over all legal tie resolutions.
- §4's measured loc(C) is one run (n5v's resolution), a lower bound on H(C); it does not test the tie-maximised H(C).
