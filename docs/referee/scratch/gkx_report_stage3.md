## 11. Stage 3 (written @@NOW@@, date -u): comparison with L-SI's independent proof (box 108)
Stage 1 (§0-§9) and stage 2 (§10) are unchanged; no verdict of §0 changes here. Erratum to §10.3: its sentence «box 108 … was not
on origin at this writing» was written at 15:02Z; the file was on origin at my 15:41Z fetch, the minute stage 2 was stamped.
- Object: claude/l-si 8c062914, docs/si/box108-gk-proof.md (461 lines, sha1 31b7c78c9b4941f083b86beb0e0fa513049dce22): «Theorem GK …
  L(G_k) = 2^k − 2 … The state after t IDEAL steps is the closed form c_k(t)», «PROVED (L-SI lane, unrefereed)», written without
  reading claude/l-red-b or docs/referee*/ (its header). Read by me AFTER §0-§9 were on origin (a85626aa) and §10 was committed
  (ea09ae2e): its §0, the rank rule of §1.2, §3 (closed form), §4 (PHASE, INPUT, SIG), §6 (MOVE, the proof of Theorem GK), §7 (the
  orders used). NOT refereed here: it is not my packet; its STEP table (32 transition classes) was not checked row by row.
- Same statement. Theorem GK is EXP-IDEAL (b); Corollary SW is (c) with the same counts and the same total 11·2^(k−2) − 9; the stop
  is «stuck» in both. Box 108 says more about the stop: «exactly v_1, …, v_(k−1) unstable and held»; the packet names v_1 only.
  True on my simulator (counter stopset: the movers with two available options at the final state are exactly v_1..v_(k−1)).
- Same run. My own implementation of c_k(t) from box 108's §3 (positions S0..S11, T0..T6, phases τ_(i+1) = τ_i mod H_i) equals my
  run at every time (counter closed), and the packet's schedule equals the same run (resp, §5), so the two descriptions agree state
  by state for k ≤ 12:
  ```
@@CLOSED@@
  ```
  Dictionary: H_i = P_i = 2^(k−i+1) − 1 (counter HvsP); a middle level's positions S0 → S6 are the response from rest 0 (S1: v; S2:
  F = ȳ to back; S3 at τ = h: B = y to forward, the packet's t_1; S4: u and F′; S5 at τ = 2h: B′, the packet's t_2; S6: e), S6 → S0
  the response from rest 1; T0 → T3 and T3 → T6 are the top unit's (i); A0 → A4 is unit 1's single response.
- Different proof structure, and what it means for E-1 / E-2. Box 108 has no response lemma. It defines the state at every time by
  the closed form and proves, by ONE induction on t, that c_k(t + 1) satisfies R104's step equations at c_k(t) (Lemma STEP: a
  finite table, because a level's inputs are functions of its own phase, Lemma INPUT), then Lemma MOVE (c_k(t + 1) ≠ c_k(t)), which
  is what makes the run continue («it differs from s_t (MOVE), so neither stop applies»). No lemma is applied before its hypothesis
  holds, so the circle of E-2 cannot arise, and «the run reaches s_(t+1)» is proved, not presupposed (E-1). This is the shape of my
  repair LEMMA′ (an induction on time with the step's own s′), reached independently. So the two derivations of L(G_k) = 2^k − 2 are
  independent in structure, and the gap I found in the packet's induction is absent from the second one.
- E-3 from a third side. Box 108 §1.2 states the rule as the Lead relayed it: «the β-rank is the position of (2k + 5 − dep, dl,
  β-id) in increasing lexicographic order». The β-id tie is in the relayed rule and in gk.py; it is missing only from the packet's §3
  text. Box 108 §7 lists «the tie rule by β-id» and «the value 2k + 5 of the wires' class» among the things NOT used, which is what
  my `gen` (revtie_run_differs 0) and `orders` (wire ranks anywhere) measure.
- The orders used. Box 108 §7's table and the packet's §8 agree item by item (ε(v_0, 1) < ε(u_0, 0) < ε(v_0, 0); ε(u_j, ·) < ε(v_j, ·);
  ε(E(j + 1), 1) < ε(wv_j, 0); ε(E(j + 1), 0) < ε(wu_j, 0); ranks depth-major; δ(v_j, ·) > δ(u_j, ·); the two cross inequalities in
  Y_j and in Y′_j; the level-0 chain δ(v_0, 1) > δ(u_0, 0) > δ(v_0, 0)). Two refinements of box 108 that my tests also show: the
  order δ(v_j, ·) > δ(u_j, ·) has no reader at j = k − 1 (my break7 at k = 3: 0 / 20); the wires and u_0 stay put by their ranks OR
  by their gates (the packet's WIRE uses the gates; box 108 uses the ranks and names the gates as the holder).
- What this comparison does not give: a referee's signature of box 108; anything beyond k = 12 by machine.
Result of stage 3: no conflict between the two proofs; the verdicts of §0 stand.
