# N5-SF against the gauntlet (TARGET.md §5): status after box 55. No step passed in full; no polynomial claim
L-NEW successor 33 (Opus 5.5; D14, D18, Lead reading L40). Lead's brief 2026-10-29 15:19Z, BOX 55 (3): «A short gauntlet status for N5-SF
against TARGET.md §5: which steps it has passed, which are open, and which need a referee or Lean. No polynomial claim.»
Owner D1: «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as
wrong until it passes the gauntlet below.» N5-SF is a CANDIDATE, not a claim: its running time is the open CONJECTURE SF-POLY
(docs/new/P-N5-SF-box55.md §5). Object: N5-SF as defined in P-N5-SF §0 (SPEC S1-S5 with S4a′ / S4b′), implementation
experiments/new/box54/n5sf.py.

| step (TARGET.md §5, owner's text) | status | what exists | what is missing | who |
| --- | --- | --- | --- | --- |
| 1. «Exact pseudocode in the lane notebook and one implementation.» | PARTLY MET | Exact definition: SPEC + S4a′ / S4b′ (P-N5-SF §0), copied into notes/L-NEW.md (box 55 log); implementation box54/n5sf.py (default MODE) | D2 change 5: «every implementation also outputs positional strategies, and L-COMP verifies them on every test game». n5sf.py computes S5's strategies but nobody has verified them with experiments/harness/verify.py | L-NEW (output), L-COMP (verify) |
| 2. «agrees with Zielonka on 10,000 random games of varied sizes and on every hard family; runtime growth is plotted and recorded» | OPEN | box 54: final regions equal N5's (WIN PASS) on 413 + 349 + 276 library games, 20 family runs, 59 hard-family runs; N5's regions are themselves checked against Oink zlk in earlier boxes. Growth table on switchbestexp N ≤ 16, H_n n ≤ 12, DLM n ≤ 8 (N5-SF-box54.md §3, §5) | a direct comparison with Zielonka (Oink zlk, or tl where zlk aborts, CLAUDE.md trap) on 10,000 random games; every M1 hard family at the sizes L-COMP uses; a recorded runtime plot; the second implementation follows only after | L-COMP (runs), L-NEW (driver) |
| 3. «A barrier statement: which known lower-bound frameworks it lies outside, and why. L-LIT signs off.» | OPEN | DATA only: N5-SF is not Friedmann's I^glo (diverges at step 22 on H3_F, L-LIT T44 / T45) and is linear on H_n (7n + 49) and DLM; it TRACKS PGSolver's switch-best counts on switchbestexp N = 1..4 (20, 58, 135, 258 vs 23, 61, 137, 289) and then falls away | an identification of the one-sided rule F (P-N5-SF §0; by N5-SBC Proposition NO-TRANSFER, N5-SF from τ* IS F) against the SI literature, and a barrier statement for F against Friedmann's frameworks (sink games, switch-best / switch-all / random-facet constructions); L-LIT sign-off | L-LIT |
| 4. «Written correctness and running-time proofs, double-refereed with every gap listed.» (Lean only if presented as M4) | correctness PARTLY WRITTEN; running time OPEN | Written, lane-proved, to referee: P-N5-SF (SF-TERM, DECOUPLE, ONE-PLAYER, SF-RED). Output correctness at S5 is N5's and rests on G-N5T-3 (VJ00 Lemma 5.8 "1 ⇒ 2", RESULTS R15 limit (iii)), re-derived by no one | REFEREE and REFEREE-2 on P-N5-SF; a proof (or a referee-accepted citation) for G-N5T-3; a running-time proof = a proof of SF-POLY, which is open, with the obstruction of N5-SBC-box55.md §3. Lean (TARGET.md §6) only if this were ever presented as M4 | REFEREE, REFEREE-2; L-FORMAL only if M4 |
| 5. «CHECKER passes on the exact commit, then I am told before anything else happens.» | NOT REACHED | — | steps 1-4 | CHECKER |
- Summary. Passed in full: none. Partly met: step 1 (missing the strategy output and its verification) and the correctness half of
  step 4 (written, not refereed; output correctness inherits G-N5T-3). Open: step 2 (Zielonka on 10,000 random games, hard families,
  plot), step 3 (barrier statement, L-LIT), the running-time half of step 4 (SF-POLY). Needs a referee: P-N5-SF, and G-N5T-3. Needs Lean:
  nothing unless an M4 presentation, which nothing here supports.
- What would make it a dead end (TARGET.md §5: «Failing any step makes it a dead end»): a wrong region or a failed strategy check on any
  test game (step 2), or a family with super-polynomial N5-SF counts (step 4's running time). The live kill target is switch-best-type
  families (N5-SF-box54.md §3; the P-leapfrog of N5-SBC §3); that attack belongs to the adversary lane (D1).
- No polynomial claim is made. The only bound proved is the reduction I < (n + m + 1)(2(n² − n + 1) + SBC), with SBC ≤ 2I.
