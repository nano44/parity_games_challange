# L-RED notebook (independent adversary; Lead brief 2026-10-15 11:30Z, 8 h box)
Owns docs/red/, experiments/red/, this file. Reads other lanes' files, never edits them. Messages only the Lead.

## Resume point
2026-10-15 ~12:55Z (pushed 85a83bf + gate.py commit). Candidate S2a MSF KILLED (docs/red/R1-MSF.md): gated_bland N takes 2^N - 1 MSF iterations on both engines;
Claim F FLAW reported 11:45Z, kill reported 12:20Z (send_message to the Lead). Remaining in the box: push, then (optional) a
generic gate-relabelling transform (any sink game + edge order -> gated game) and a check that the same gadget kills LSF-ranked
variants; wait for the Lead's instructions.

## Queue
1. scripts/verify.sh && git push -u origin claude/l-red (report, engine, family, instances, check.sh).
2. (done) gate.py: generic transform; MSF (reversed labels) and LSF (Bland labels) both 2^N - 1 on G_N.
3. End-of-box message: DONE / FINDINGS / NEEDS.

## Things only I know
- L-SI's branch is read through a detached worktree in the scratchpad (git worktree add <scratch>/lsi origin/claude/l-si);
  experiments/red/xcheck.py --lsi <that path> compares switch sequences with si.py. The worktree is not in the repo.
- vj.py classifies "cycle-creating" by Odd's play (on_play), not by the path bit; its stats line prints cycle-creating /
  escapes / cycle-node changes per run. In a sink game every switch that closes an even 2-cycle is an escape.
- gated_bland: ids sink 0; a_i = 5i-4, b_i = 5i-3, d_i = 5i-2, e_i^a = 5i-1, e_i^b = 5i; b_{N+1} = 5N+1. Gate priorities
  4..4N+2 (even), d_i = 3, underlying shifted by 4N+4. Best-reward start = sigma_0 (e_i^a has the higher even priority).
- Runtime of vj.py msf on gated_bland: N=10 1.3 s, N=12 6.9 s, N=13 17 s (one valuation per switch, no incremental update).
- Oink is built (scripts/setup_oink.sh, ~3 min); MSF on tc/tc+/counter_* via si.py was linear or near-linear (sweep in
  the scratchpad, not pinned: tc N=8 275, tc+ N=10 595; all PGSolver families linear in N).

## Sources opened (arXiv id or DOI, theorem/section)
- Friedmann, "An exponential lower bound for the latest deterministic strategy iteration algorithms", LMCS 7(3:19) 2011,
  arXiv 1106.0778 (PDF opened 2026-10-15 ~11:50Z). Section 3 pp.4-6: play decomposition v1..vk (w1..wl)^omega, node
  valuation (w1, {v_i > w1 : 1 <= i <= k}, k), set order M < N iff max(M delta N) in (N cap V_even) cup (M cap V_odd),
  valuation order (length: e < f worse when u odd, e > f worse when u even), improving edge, Thm 3.2, Thm 3.3.
  Section 5 p.8: 1-sink games, "the path-length component equals the cardinality of the path component". Section 6.1
  pp.9-10: simple cycle (Table 1: d_i Even p_i, e_i Odd p_i+1, h_i exit), Lemma 6.1 (tau(e_i) = h_i when closed; = d_i when
  open and sigma(d_i) prec h_i), Lemma 6.2 (open cycle closes when sigma(d_i) = max D_i prec h_i; "the player 1 node hides
  the fact that there is a highly profitable node on the other side"). Section 6.4 Table 4 (G_n), 6.5 phases (skimmed).
- Disser-Loho-Maat-Mosis, "Lower bounds for ranking-based pivot rules", arXiv 2512.16684 v2 (PDF opened ~12:25Z): Thm 4.3
  (p.13: l-index-based rules need m^omega(1) on sink parity games), Fig. 4.1 (p.14: G_n, priorities a_i 2i+1, b_i 2i+2,
  b_{n+1} 2n+4, Bland numbers 2i / 2i-1, sigma_0 in bold), Lemma 4.4 (p.13: "Strategy improvement with Bland's rule takes
  2^n - 1 iterations to solve the sink parity game G_n with initial strategy sigma_0"; proof by induction, p.14).
- Fleet files: TARGET.md v1.0 sections 2, 3, 5; docs/NOW.md; claude/l-si 95d37d3: docs/si/candidates/S1.md, S2.md,
  docs/si/RESULTS.md, DEAD.md, README.md, experiments/si/si.py, gens.py, families.py, freeze_test.py, adversarial.py,
  notes/L-SI.md; docs/lit/T12-MSF-barriers.md; experiments/harness/pg.py, verify.py, zielonka.py.

## Dead ends
- None yet for the attack. Not pursued: a non-sink killer (the sink-game gate suffices); porting Disser-Mosis D_n with Odd
  gates (T12 section 4) is unnecessary, the Bland counter plus gates is smaller.
