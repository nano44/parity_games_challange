# P-N5-REPD status: FROZEN, NOT REFEREED. Premise WD-BOUNDED DEAD (L-RED R130)
- Packet docs/si/P-N5-REPD-box49.md (frozen at l-si ea45f909, sha1 9f02599c20f887278f2cc87ab81f845c39c5a620) and line file
  docs/si/P-N5-REPD-line.txt (sha1 2f27ea6ac48374058647de54a23f70fdca962df9) stay unchanged.
- Lead 2026-10-30 03:35Z: «P-N5-REPD is NOT routed to the referees. A reduction to a premise already dead buys nothing for G-N5-TIME. GP*-SUB,
  LOC-R* and WIN stay lane-PROVED in your notebook and remain citable later.»
- Why: L-RED R130 (l-red 448a1bf9, docs/red/R130-window-depth.md): CONJECTURE WD-BOUNDED (box 48: window depth D_F ≤ a constant) is DEAD.
  Family wdepth_K4_m64 (span/mkrw.py K m, LATE=2; chained late adopters in one W-run, no fallback, τ constant): D_F = (m − 1)/2 = 7 / 15 / 31 at
  n = 146 / 234 / 410, counted by two counters (my repchain.py at 4b71fcc7, read-only, and L-RED's latec.py on L-COMP's n5b). REP stays
  linear there: REP = (K − 1)(m − 1)/2 (93 at n 410, one REPEAT per window).
- Consequence: Corollary REPD-POLY's premise [P-WD] fails on a growing family, and Theorem REP-DEPTH's Σ_{d ≤ D_F}(n·m_E)^d is exponentially
  loose there (true count linear). The theorem itself stands (lane-PROVED), but it gives no polynomial bound when D_F grows.
- READING (L-RED R130, the Lead): the growth is branching across windows, not depth; a bound must count repeats per window chain additively.
  The per-edge form REP_F(y, z) ≤ WCH_F(z) (P-N5-CUT §6) summed lands back in the WV-R circle (P-N5-CUT §7).
- Still lane-PROVED and citable: GP*-SUB, LOC-R*, Lemma WIN, Theorem REP-DEPTH (P-N5-REPD §2-§5; working notes N5-SUB-box46.md,
  N5-WDEPTH-box48.md).
