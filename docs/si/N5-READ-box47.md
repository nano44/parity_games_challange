# N5-READ (box 47): reader chains. Lemma READ-CHARGE (proved); chains are Θ(n) deep (runfam_K40: 73 at n 79), so a depth-bounded recursion over the reader graph gives no polynomial bound
L-SI successor 31 (Opus 5.5), D15 / D18, Lead reading L40. Lead 2026-10-30 00:52Z: «L-RED R127 … reads "depth ADDS along a reader chain; it
amplifies only via breadth". Try to turn that into a lemma: if c's W-play passes through v, then WCH(c) ≤ switches(v) + (the rest of the
play's changes). That gives a recursion over the reader graph. Poly follows if reader chains have bounded length or the graph has a usable
rank. State where reader cycles break it.» Working note, unrefereed. G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Tool: experiments/si/odd/readch.py (W-runs as in L-NEW's box64/late.py). Output odd/out/readch_corpus.txt (719 games). Pinned in
  si/check.sh «box 47».

## 1. Lemma READ-CHARGE (PROVED, lane)
- Setting: a transition t → t + 1 with τ_{t+1} = τ_t = τ (inside a W-run, or any τ-constant transition). W_t(c) := val(σ_t, τ)(c).
- Statement: if W_{t+1}(c) ≠ W_t(c), then some Even x on c's (σ_t, τ)-play switches at t (σ_{t+1}(x) ≠ σ_t(x)).
- Proof: if no Even vertex of c's (σ_t, τ)-play switches, and Odd vertices follow the same τ, the (σ_{t+1}, τ)-play from c is the same
  sequence of vertices, so its [S1-val] triple is the same. □
- Corollary (the Lead's form; PROVED, lane): if v lies on c's play during a stretch Q of a W-run and the prefix c … v of the play does not
  change on Q, then WCH_Q(c) ≤ WCH_Q(v) + #(transitions of Q at which a vertex of the prefix switches) + #(transitions at which the prefix
  stops reaching v). Proof: at a transition where neither the prefix nor the suffix from v changes, W(c) = prefix ⊕ W(v) is unchanged
  (READ-CHARGE applied to the prefix and to v's play).
- The recursion it gives: WCH(c) ≤ Σ_{x ever on c's play} SW(x), and SW(x) = Σ_w ENT(x, w) ≤ Σ_w (1 + WCH(w) + SIL + CYC) (W-ENT, box 37),
  with w on x's play after the switch, i.e. downstream of c again.

## 2. DATA: the chains are long
- Chain: a W-change of c at t has CAUSES (the switching Even x on c's old or new play; READ-CHARGE: at least one; RC_V = 0 everywhere);
  a cause x → w has SOURCE = the last W-change of w before t in the W-run (none: a ROOT); DEPTH = 1 + max over causes of the source's depth.
| instance | n | W-changes (vertex, transition) | roots | max depth |
| --- | --- | --- | --- | --- |
| runfam_K40 | 79 | 343 | 8 | 73 |
| hntop_n8 (.start) | 168 | 5,543 | 1,436 | 48 |
| hntop_n4 (.start) | 84 | 895 | 334 | 24 |
| fc_8 | 210 | 1,485 | 447 | 52 |
| latew_K20_m32 (.start) | 538 | 8,639 | 6,453 | 33 |
| corpus (719 games) | | | | max 73 (runfam_K40); depth ≤ n − 1 in every game |
- hntop_N: depth 6N = the longest W-run (box 41), so each W-run is one chain. latew: shallow (33) but broad (6,453 roots).

## 3. Verdicts (READING)
- "Reader chains have bounded length": DEAD as a route. Depth reaches 0.92n (runfam_K40, 73 at n 79), and grows with N on hntop (6N).
- CONJECTURE READ-DEPTH: chain depth ≤ n − 1 per W-run. DATA: 0 failures (corpus, hntop_2..8, latew). Its likely source is GP*'s wave
  (FW-R*'s charging follows a simple play of ≤ n − 1 edges), but a W-change's causes need not lie on one simple path, so this is not proved.
- Where reader cycles break it. The relation "x lies on c's play" is cyclic on the cycle part of a play: every vertex of a W-cycle reads every
  other. So there is no static rank (priority, attractor depth, λ_W order) that decreases along all reader edges. The recursion is
  well-founded only through time (sources are strictly earlier transitions), and then its depth is the W-run's chain depth, Θ(n) above.
- Why depth n does not give a polynomial. The recursion is additive in depth but multiplicative in breadth: WCH(c) ≤ Σ_x Σ_w (1 + WCH(w)),
  with up to m_E terms per level, so a depth-d unfolding gives m_E^d. With d up to n − 1 that is exponential. A polynomial bound needs either
  depth O(1) (false here) or a per-level sharing argument (each source W-change counted for O(1) readers), which latew's breadth (6,453 roots,
  570 repeats from one W-run) shows is not free.
- This agrees with L-RED R127 («depth ADDS along a reader chain; it amplifies only via breadth»): depth Θ(n) is additive and harmless only if
  the breadth at each level is charged once.

## 4. Composition toward G-N5-TIME
- §1: READ-CHARGE is a correct accounting step (PROVED, lane) but gives only m_E^depth. [P-REP] / [P-LATE] stay OPEN. CONJECTURE READ-DEPTH
  with a sharing lemma ("each W-change of w is the source of O(poly) W-changes per level") would give WCH ≤ poly·n per W-run.

## DONE / FINDINGS / NEEDS
- DONE: odd/readch.py; corpus; si/check.sh «box 47»; this note.
- FINDINGS: 1. PROVED (lane) READ-CHARGE and the prefix corollary. 2. DATA: chain depth up to 0.92n, ≤ n − 1 everywhere (CONJECTURE
  READ-DEPTH). 3. READING: no static rank (W-cycles read each other); depth-bounded recursion is m_E^depth; a sharing lemma is what is missing.
- NEEDS: none from the owner.

## Addendum: sharing, measured (DATA, 4 instances; readch.py FANOUT / FANOUTW)
- FANOUT := the most W-changes (c, t) that use one source W-change (w, t′) (w changed at t′ and not again before t); FANOUTW := the most
  that use the W-changes of one transition t′.
| instance | n | FANOUT | FANOUTW |
| --- | --- | --- | --- |
| runfam_K40 | 79 | 242 | 242 |
| so_th_n32 | 32 | 15 | 24 |
| hntop_n8 (.start) | 168 | 33 | 66 |
| latew_K20_m32 (.start) | 538 | 102 | 2,344 |
- One source W-change feeds up to 3n later W-changes (runfam_K40: 242 at n 79), because it stays the "last W-change of w" for every later
  reader of w until w changes again. So "each source is used O(1) times" is false. A sharing lemma would have to count per (reader, source)
  pair, which is ≤ n per source and transition, and is again the breadth term. No proof; READING only.
