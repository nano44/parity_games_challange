# N5-CARX (box 34): Odd's carries NM^U on class-X options; why d_hntop has 2N² + 5N − 5
L-SI successor 29 (Opus 5.5), D15 / D18, Lead reading L40. Lead's brief 2026-10-29 19:52Z (BOX 34). Working note, unrefereed, not a
TARGET.md claim. G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Tool: experiments/si/odd/carx.py. It reads carries as in R85 / R86 F3 (on G^d), per vertex per λ^U-run; SIDE=E reads Even's Ξ on G.
  --mut flips the tests. Outputs: experiments/si/odd/out/carx_corpus_{O,E}.txt (box59/sbcg.lst; 718 / 716 of 719 games finished
  within 300 s; missing: O mei_h4; E nep90_n40, epsseg_cex_n48). Pinned in check.sh «box 34».

## 1. Where the carries sit (DATA, READING)
- Class X is a property of an EDGE (o, e): e's play never returns to o. NM^U is a property of a VERTEX's valuation.
- By box 33 RE-CHARGE, a re-entry of o into e is paid by a rise of U(e). By box 28 Lemma SW-RISE (Odd side), each switch of o is also
  paid by a rise of U(o) itself.
- So the carries that matter are those of the switching vertices and their options. In d_hntop both are the top-gate vertices of
  Friedmann's H_N: the Odd gate vertices d1_N, d2_N, d3_N (in G^d) and their options d_, a (lane), e.
  - The class-X, carry-charged re-entries on d_hntop_n3 split by label pattern (o → e) as d_ → d_ 49, d_ → a 46, t → r 28, t → t 20,
    d_ → e 17, t → s 16.
- The top vertex is d3_N, with NM^U = 2N² + 5N − 5 (= R111).

## 2. d_hntop explained (DATA, exact on N = 2, 3, 4, 5, 6, 8)
- d3_N's P-set walks up the lane. Each Odd lane switch (τ-change of t_{k+1}) moves it one step, and the step pattern repeats:
  "out a_k; in a_{k+2}, t_{k+2}, t_{k+1}, e_N, d1_N", then "out a_{k+2}, e_N, d1_N; in a_{k+3}, t_{k+3}".
  - Every step is a carry. Odd lane vertices t enter uncovered (against M2), and even outs (e_N) find no heavier partner (against M3).
- A MATCHED change resets the walk ("out a_last, t_last; in c, a_1, t_1"). That splits the run into SWEEPS.
- d3_N has exactly N sweeps. Sweep k has 4k + 3 carries for k < N, and the last has 4N + 2. Σ = 2N(N − 1) + 3(N − 1) + 4N + 2 =
  2N² + 5N − 5.
  - The lane has 6N − 2 vertices a_k. Sweep k covers a prefix that grows by about 6 lane vertices per sweep, with 2 carries per 3 steps.
- So NM^U is quadratic because the number of sweeps (N, one per counter level) times the sweep length (O(N)) is quadratic. Nothing in
  the family is exponential.
- Mirror check: on the original hntop_n3 the Even side (SIDE=E) gives the same sweeps [7, 11, 10] for d3_3.
- No linear per-vertex bound survives this family: NM^U = 2N² + 5N − 5 > n − 1 = 21N − 1 once N ≥ 9 (fit; N = 9 not run).

## 3. Three candidate laws (CONJECTURE / DEAD)
- DEAD: CARRY-CLIMB. "Between consecutive matched P-changes of U(x), the entering top rank of each carry strictly increases."
  - Kill: d_hntop_n2, vertex 4, λ^U-run from 0, t = 7: entering top 38 then 35.
  - It also fails in 43 (Odd) and 187 (Even) corpus games.
- CONJECTURE CARRY-SEG. "Inside a λ-run (λ^U-run), a vertex has at most n − 1 carries between consecutive matched P-changes."
  - DATA: 0 violations on 718 (Odd) + 716 (Even) corpus games and on the 11 dualised families.
  - Longest burst / n: 0.17 on the Odd side (sym_h12_s1, 4 at n 24), 0.46 on the Even side (b5_os_n24, 11 at n 24); 64 at n 168 on
    d_hntop_n8.
- DEAD: SWEEP-GAIN. "R85's Φ, read just after each matched change, strictly increases along the λ-run."
  - Kills: Odd side red/n5inj/instances/wide_h16.pg (sha1 990ecbcf), vertex 2, λ^U-run from 13, t = 23: Φ 18 then 18.
    Even side new/box59/out/fc_3.pg (9af7ca12), vertex 6, t = 23: Φ 155 then 88.
  - It fails in 9 Odd and 119 Even corpus games. It holds on all dualised families.
- Why the pair mattered, and what is left (PROVED, lane; arithmetic):
  - CARRY-SEG and SWEEP-GAIN together would give #MAT ≤ K(K + 1) + 1 (strictly increasing integers in Φ's range), so
    PCH ≤ (K(K + 1) + 2)·n per vertex per λ-run. With R86 (d) that is a polynomial T, with no frame premise.
  - CARRY-SEG alone gives NM ≤ (#MAT + 1)(n − 1). With MATCH-Φ, #MAT ≤ W(1 + NM). The two are circular, so CARRY-SEG alone bounds
    nothing.
  - What the data leave open is a NET-progress law for matched resets that tolerates the Φ falls seen on wide_h16 / fc_3, e.g. a
    potential other than Φ.

## 4. Composition toward G-N5-TIME (one line each)
- §2: d_hntop's NM^U is (sweeps) × (sweep length) = O(N²). It is no obstacle to a polynomial bound, and it kills every linear
  per-vertex bound (N ≥ 9).
- CARRY-SEG (CONJECTURE): carries come in bursts of ≤ n − 1 between matched resets. With it, NM*^U = O(n · #matched resets), so
  G-N5-TIME reduces (with R86, R85) to bounding matched resets per vertex per λ-run. That is the new open target.
- SWEEP-GAIN (DEAD): the reset bound cannot come from R85's Φ alone.

## DONE / FINDINGS / NEEDS
- DONE: experiments/si/odd/carx.py; out/carx_corpus_{O,E}.txt; check.sh «box 34»; this note.
- FINDINGS:
  1. DATA: d_hntop's 2N² + 5N − 5 = N lane sweeps of 4k + 3 carries (last 4N + 2), exact on 6 sizes, mirrored on G.
  2. DEAD: CARRY-CLIMB (d_hntop_n2); SWEEP-GAIN (wide_h16 Odd, fc_3 Even).
  3. CONJECTURE CARRY-SEG: 0 / 1434 corpus runs; it reduces NM to matched resets.
  4. PROVED (lane, arithmetic): CARRY-SEG + SWEEP-GAIN ⇒ PCH = O(n³), but SWEEP-GAIN is dead; CARRY-SEG alone is circular with MATCH-Φ.
- NEEDS: none from the owner.

## 5. Addendum (Lead 20:00Z): is R85's MATCH-Φ per vertex as landed? (READING of RESULTS text; trunk 754810df+, docs/RESULTS.md)
- Per vertex per PHASE: YES, verbatim.
  - R85 (c), RESULTS.md l. 5108-5109: "PCH_𝒫(v) ≤ (K(K+1)/2)(NM_𝒫(v) + 1) + NM_𝒫(v) per vertex per phase, every game"; in the packet's
    words "For every game, vertex v and phase 𝒫: PCH_𝒫(v) ≤ (K(K+1)/2)·(NM_𝒫(v) + 1) + NM_𝒫(v)." The R85 headline (l. 5064) says the
    same: "per vertex per phase, every game, PCH and NM counting v's P-changes and carries in 𝒫".
- Per vertex per λ-run / λ^U-run: signed as a PREMISE that holds, not as a displayed item.
  - R86 (e), l. 5345-5357: the premise is "[MΦ] holds with "phase" replaced by "λ-run" (resp. "λ^U-run" on G^d)". [MΦ] is quoted there
    in per-vertex form: "PCH_𝒫(v) ≤ (K(K+1)/2)·(NM_𝒫(v) + 1) + NM_𝒫(v)", K the number of ranks above rank(λ(v)), NM_𝒫(v) v's carries.
  - Both §6 cells sign that premise as holding: REFEREE "its premise "[MΦ] on λ-runs" HOLDS (… MΦ's proof reads verbatim with c fixed …)";
    REFEREE-2 "The "phase → λ-run" replacement is VALID". The λ^U side: REFEREE §6 "on λ^U-runs it holds for U on G^d …"; REFEREE-2
    §2.5 "MATCH-Φ's proof holds for every parity pattern, so the bound holds (N-C3)".
  - R86's DISPLAYED conclusion is only the max form: "P*_R ≤ (n²/2)(NM*_R + 1) + NM*_R with NM*_R the most carries of one vertex in R".
- Lane reading: the per-vertex λ^U-run form PCH^U_R(e) ≤ (K_e(K_e+1)/2)(NM^U_R(e) + 1) + NM^U_R(e) is what R86 (e)'s signed premise
  says. Citing it per target e is citing that premise, not a new claim. If the Lead wants it displayed, it is a one-line Referee
  strengthening of R86 (e), not a new packet.
- Consequence:
  - R86 (c)'s middle sum is already per target: Σ_{(v, c)} n·(PCH_R(c) + 1), summed over edges (l. 5269 headline).
  - So with L-NEW 35's COMPOSE-FREEZE the Odd term is Σ over unprotected (o, e) of n·(PCH^U_R(e) + 1). Each PCH^U_R(e) is bounded by
    e's own carries.
  - G-N5-TIME's Odd half is then "NM^U_R(e) for targets e of edges that are unprotected at some state". Box 33 (class X 3073 / 3276 on
    d_hntop_n8, 450 / 450 on runquad) says these are mostly class-X targets. §2's d_hntop vertex d3_N is one of them
    (d_ → d_ re-entries).
