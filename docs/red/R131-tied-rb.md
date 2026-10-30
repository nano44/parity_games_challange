# R131: CONJECTURE TIED-RB (L-SI box 50 §6) is false. One W-run carries (K − 1)(m − 2) untied re-blocked REPEATs: 98 at n 270, 210 at n 382. The release of each is a switch on the shared prefix of the target's W-play and Ξ-play, so its Ξ-climb is never tied. DATA (two counters, two engines, Oink) + READING
L-RED successor 32 (Opus 5.5; D1/D18). Lead 2026-10-30 05:28Z, target (B): "CONJECTURE TIED-RB: every REPEAT re-blocked after its leave
has a TIED Ξ-climb of its target z (Ξ(z) rises while W(z) is fixed). Data: 574/574. Find a counterexample, an untied re-blocked REPEAT,
or report the obstruction." Written 2026-10-30 from 06:35Z (date -u). Labels: DEAD / DATA / READING. Not a TARGET.md claim; G-N5-TIME OPEN.

## 1. Definitions used (box 50 §6, l-si 4fb0bfba, read only)
- W-run: τ constant, σ moves, no S4c fallback, λ_W constant. (y, z) BLOCKED at a state: W(z) ▷ W(σ y) and (y, z) ∉ Iσ.
- LATE adoption: adoption of an edge blocked at an earlier state of the W-run. REPEAT: a late adoption of an edge late-adopted before in
  the same W-run. k = y's last leave of z, u = the REPEAT's transition.
- RE-BLOCKED: (y, z) blocked at some state of [k + 1, u]. TIED: some transition s ∈ [k, u − 1] with Ξ_{s+1}(z) ▷ Ξ_s(z) and
  W_{s+1}(z) = W_s(z).

## 2. The family (tree/mktied.py K m; sha1 in the pin's vrun file)
- Base: span/mkrw.py K m with LATE=1 (R127: mkr in one W-world, late adopters v_J → {d_J, c_J}, c_J Odd → {r_J honest, yh_J τ}).
- Gadget, for J = 2 .. m − 1:
  - y_J (Even, priority 132) → {v_J (start), z_J};
  - z_J (Even, priority 20) → {a_(J+1), c_(J+1)} (start: the engine's "best" initial choice).
- How it was found: a random gadget search on mkrw K 3 m 4 (2 to 5 new vertices wired to existing ones, random priorities). The hit was
  y → {v2, z}, z → {a4, C3, c4}. It was then simplified (C3 dropped) and copied to every J (offset 1).
- TARGET=odd: y_J → {v_J, o_J}, o_J (Odd, priority 22, single successor z_J). The target o_J never switches; same counts.
- ONE=1: the first hit, at the end of the run (K 2, m 4, one REPEAT y → r_2 released by the final Ξ = W collapse). Kept only as the first
  witness. The family above has its untied REPEATs in the middle of the run.

## 3. DATA (one W-run each: τ constant, 0 fallbacks)
| K | m | n | iterations | REP | re-blocked | tied | untied re-blocked |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 8 | 134 | 45 | 36 | 36 | 18 | 18 |
| 8 | 8 | 190 | 89 | 84 | 84 | 42 | 42 |
| 8 | 16 | 270 | 153 | 196 | 196 | 98 | 98 |
| 16 | 16 | 382 | 305 | 420 | 420 | 210 | 210 |
| 4 | 8 (TARGET=odd) | 140 | 45 | 36 | 36 | 18 | 18 |
| 8 | 16 (TARGET=odd) | 284 | 153 | 196 | 196 | 98 | 98 |
- Fit: untied re-blocked = (K − 1)(m − 2), exactly half of the REPEATs. The other half are the base family's tied REPEATs of (v_J, c_J).
- Two counters agree on every row:
  - tied.py = L-SI box 50 at l-si 4fb0bfba (worktree, read only), on L-NEW's n5x step;
  - tree/tiedc.py = my recount on L-COMP's n5b SPEC trace and n5b's valuations, written from the definitions in §1, not from tied.py.
- Pin tree/instances/tiedrb_K8_m16.pg / .start. tree/vrun_tiedrb_K8_m16.txt: n5b SPEC 153 iterations, 0 fallbacks; n5.py 153, 0; state
  sequences identical (seg/xeng.py); n5b's solution Oink zlk OK, strategies verified.
- Box-50 tools on the pin: windag.py RT 128, REP 196, X 0, BETA 14, INDEG 2, NPATH 14, LONG 15, TOKSH 1, EPATH 1. repchain.py (in tree,
  box 44): parF 98, parS 98, parR 0, causal maxdepth 1, LDEC_V 98, MAXWD 15.
- check.sh gate: K 4 m 8 gives 18 untied re-blocked REPEATs (tiedc.py); the pin regenerates.

## 4. Anatomy of one REPEAT (K 4, m 8, (y_3, z_3), leave k = 11, adoption u = 16)
- 11 → 12 (h's step): y_3 leaves z_3 for v_3.
- 12 → 13: z_3 switches a_4 → c_4. Its W rises (c_4's τ-route yh_4 → h, at the new level); its Ξ rises too. Now
  W(z_3) ▷ W(v_3) but Ξ(z_3) ◁ Ξ(v_3): (y_3, z_3) is BLOCKED at states 13 to 15.
- 15 → 16: the wave has reached r_3, so W(a_4) has risen, and z_3 switches c_4 → a_4. W(z_3) changes and Ξ(z_3) rises above Ξ(v_3).
- 16 → 17: y_3 re-adopts z_3, a REPEAT.
- Every Ξ-climb of z_3 on [11, 15] is z_3's own switch. A switch at z_3 moves its W-play too, so none of them is tied.

## 5. READING
- DEAD: CONJECTURE TIED-RB, by a factor of Θ(n²) per W-run, not by an edge case.
- Exact mechanism: the climb that releases the gate happens on the SHARED PREFIX of z's W-play and Ξ-play: at z itself, or (TARGET=odd)
  at a switcher below z before the two plays diverge. The base family's tied climbs happen after the divergence: c_J's honest branch
  r_J is not on its τ-play.
- So the "target does not switch" repair is also dead (TARGET=odd). The repair that the data still allows is: TIED-RB for releases whose
  climb lies strictly after the divergence of z's two plays. That is close to a tautology, and it leaves out exactly the REPEATs above.
- What this means for box 50 §5's positive route: these untied REPEATs are released by a W-change of z (the switch on the shared
  prefix). Theorem CIRCLE (c) charges them to an (edge, W-change) token, so they are back inside the circle. A GXC-type charge (Ξ-climbs
  with W fixed) cannot pay them.
- Also off in this family: box 50 §5's causal-chain reading. The causal parent of each untied REPEAT is the target's own switch
  (repchain LDEC_V 98: l(x) = l(z), not <). And the window DAG is no longer a forest (INDEG 2), though NPATH is only 14.
- G-N5-TIME is not touched: REP is quadratic (420 at n 382), inside the R127 envelope.

## DONE / FINDINGS / NEEDS
- DONE: tree/mktied.py (family, TARGET=odd and ONE=1 variants), tree/tiedc.py (second counter), tree/tiedlib.py (importable counter for
  search), tree/gb.py (named builder and tracer); pin tiedrb_K8_m16 + vrun (two engines, Oink); check.sh gate; this note.
- FINDINGS:
  1. DEAD: CONJECTURE TIED-RB. There are (K − 1)(m − 2) untied re-blocked REPEATs in one W-run (210 at n 382). Two counters and two
     engines agree, and Oink checks the solution.
  2. READING: the release climb lies on the shared prefix of z's W-play and Ξ-play, so it is a W-change of z. These REPEATs are paid
     only by (edge, W-change) tokens, which puts them back in the circle. An Odd, never-switching target fails the same way.
  3. DATA: on this family, box 50 §5's LDEC reading fails (LDEC_V 98) and the window DAG has INDEG 2.
- NEEDS: none from the owner.
