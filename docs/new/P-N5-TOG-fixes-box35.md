# P-N5-TOG fixes file (box 35)
L-NEW successor 15 (Opus 5.5, D15/D18). Written 2026-10-25 09:5xZ by date -u, at the Lead's request (09:55Z). It answers the referee
reports on packet docs/new/P-N5-TOG-box35.md (pinned trunk d3daae1, sha1 7dfda8c88a0e9b752156f4faec726d8dccc20ccb; never edited). This
file is a record of the repairs: the packet stays the object, and these lines replace or extend the named lines.
- REFEREE-2: docs/referee-2/R2-N5-TOG.md (referee-2 faabe71). It signs (F), L-MONO, Z-COUNT, TOGGLE, TOGGLE-COUNT and RESTARTS, and signs
  X-SN-PHASE with gap G-TOG-1 and note N-TOG-1. REFEREE: pending.

## 1. REFEREE-2 items (both accepted)
- G-TOG-1 (§5 Corollary X-SN-PHASE; accounting, the FRZ-3 / G-FRZ-1 pattern; it OCCURS in data).
  - The gap: X_SN (R30 (c)) counts the S4a crossings that START at c_w = c_θ states. In a fallback-free run Q these are:
    - the crossings with both ends in Q's SN prefix P, which X-RUN′ (a) bounds;
    - possibly the one S4a transition from P's last state. Its start has c_w = c_θ; its end does not.
    The packet's sum used X-RUN′ (a) only, so as written it omits up to one crossing per run, i.e. up to f + 1 per phase.
  - Corrected accounting (replaces the second bullet of §5).
    - X-RUN's proof (P-N5-FRZ §6 with fixes 168de464 FRZ-3; REFEREE-2 R2-N5-FRZ §6) bounds the crossings with both ends in one run of
      consecutive (h) states of Q by (n − 1) + 6(d_o + 1)n² + 6(d_o + 1)n³ ≤ 13(d_o + 1)n³ − 1, for n ≥ 1 and d_o ≥ 0.
      - Check: 13(d_o + 1)n³ − [(n − 1) + 6(d_o + 1)n² + 6(d_o + 1)n³] = 7(d_o + 1)n³ − 6(d_o + 1)n² − n + 1 ≥ d_o + 1 ≥ 1.
    - In X-RUN′ (a) the SN prefix P has ≤ t_Q + 1 H1 runs, each of that form (P-N5-L2-fixes2 §2, Lemma X-RUN°). ¬H1 runs have no crossing
      (R-CONST), and the transitions between runs are the t_Q toggles. So the crossings starting in P, the boundary transition included, are
      C_P + 1 ≤ (t_Q + 1)(13(d_o + 1)n³ − 1) + t_Q + 1 ≤ 13(d_o + 1)n³(t_Q + 1) + t_Q.
    - Summing over the ≤ f + 1 runs of the phase, with Σ_Q t_Q ≤ T (§4): X_SN ≤ 13(d_o + 1)n³(f + 1 + T) + T. This is the packet's bound,
      unchanged.
  - REFEREE-2's line, adopted: "X_SN also counts the S4a transition from each SN prefix's last state, which X-RUN′ (a) does not ('both ends
    in P'). X-RUN's proof gives ≤ 13(d_o + 1)n³ − 1 per (h)-run, so in X-RUN′ C_P + 1 ≤ 13(d_o + 1)n³(t_Q + 1) + t_Q, and the stated
    per-phase bound holds."
  - DATA (REFEREE-2):
    - 310 of 11,378 batch X_SN crossings and 246,038 of 1,460,118 climb crossings are such boundary transitions, all of them entries.
    - Example: experiments/n5-exhaustive/instances/b6_xl2_n32.pg, run 1, S4a 28 → 29: {2, 13, 18} enter R, c_θ = 11, c_w(29) = 8.
- N-TOG-1 (§0 and §5; citation). Replace "P-N5-L2 §11" with "P-N5-L2 §7" (X-RUN′ is §7 of the packet P-N5-L2, sha1 cbea0739).
  - "§11" was the section number of N5-REL-box34.md, the work-log source.

## 2. Labels after REFEREE-2 (REFEREE pending)
- Signed by REFEREE-2: (F), L-MONO, Z-COUNT, TOGGLE, TOGGLE-COUNT, RESTARTS; X-SN-PHASE with G-TOG-1 (closed by §1).
- X-SN-PHASE and RESTARTS inherit the status of their P-N5-L2 premises (REFEREE-2 signed P-N5-L2 at 388caf6; REFEREE signed it at 7626354).
- Not to sign: §7. G-N5-TIME stays OPEN.
