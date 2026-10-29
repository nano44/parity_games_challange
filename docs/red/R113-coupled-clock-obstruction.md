# R113: why the two-sided mkr clock does not couple at the pivots. A source that a leapfrog reactor chain follows must have its W raised at every step the chain follows; a step released by a τ-change lowers W at the released vertex (R112 rule D). So τ cannot release the pivot steps of an Even reactor clock, and dually σ cannot release Odd's. READING (heuristic; assumptions stated) + OPEN
L-RED successor 27 (Opus 5.5; D1/D15/D18; Lead 13:47Z STEP 1, the COUPLED family; R112 §4 "two-sided clock"). Labels: READING /
OPEN. Not a TARGET.md claim, not a proof. G-N5-TIME stays OPEN.

## 0. Frame (SPEC S2, S4a, S4b; R110)
- Iσ depends on σ only and Iτ on τ only. So each side's MENU is autonomous: τ never creates or removes an Even improving switch, σ
  never an Odd one. Each side's strategy sequence is an improving SI path of its own game; the other side only SELECTS which subset
  of the current menu is taken, and when (S4a: W-optimum against τ; S4b: W-optimum against σ).
- So "coupling" means: each side acts as the pivot-rule controller of the other's strategy improvement (R110), and its control
  signal is W.

## 1. Direction (R112 rule D, restated with its assumption)
- With σ fixed, Odd's S4b step is Odd's joint optimum over {keep} ∪ Iτ, so it lowers W (Even scale) at every vertex, or leaves it.
  With τ fixed, Even's S4a step raises W everywhere.
- Even vertex a is stalled at state t: W_t(keep) ≥ W_t(alt) with alt ∈ Iσ. If the release at t + 1 comes from a τ-change on keep's
  play, and nothing on alt's play changes in between, then W(a) after the switch = W(alt) ≤ W_t(keep) = W(a) before: a net DROP at a.
  A release by a σ-change raises W(alt) instead: a net RISE.
- Assumption (A): "nothing on alt's play changes in between". The two steps of a transition are simultaneous, so (A) can fail;
  every trace in R112 satisfies it.

## 2. The obstruction for leapfrog reactor chains (READING under (A) and (B))
- Setting (mkr, R106 §2): Even reactor r between options a → (towards source h) and b → (towards source h′). A wave towards h needs
  Ξ(h) > Ξ(h′) (menu) AND W(h) > W(h′) (S4a selection); a flip back needs both reversed.
- Assumption (B): the reactor's W-plays pass through its sources (W(a) = W(h), W(b) = W(h′) up to the reactor's own markers). In
  mkr the a_j, b_j are single-successor Odd vertices, so (B) holds.
- Claim: under (A) and (B), a source whose steps are τ-released cannot drive a leapfrog chain for more than one round.
  - Write x_k = W(h) after h's k-th step and y_k = W(h′) after h′'s k-th step. The chain follows h after h's step k + 1 and h′ after
    h′'s step k + 1, so x_{k+1} > y_k and y_{k+1} > x_{k+1}.
  - If h's steps are τ-released (net drops, §1): x_{k+2} < x_{k+1} < y_{k+1}, contradicting x_{k+2} > y_{k+1}.
  - If both sources are τ-released, the same contradiction appears one step earlier (y_{k+1} < y_k < x_{k+1}).
- Concretely for the R112 §4 plan: Even pivots h, h′ released by Odd holders (Odd's reactor wave opens the holder's U-menu, the holder
  drops W on the pivot's keep). The pivot's holder ladder must then DEcrease in W (the pivot keeps the current holder while the next
  options are W-lower: D_1 > D_2 > …), while the reactors need each pivot's W to INcrease. Dead as designed (no instance built: the
  contradiction is in the inequalities, before any game).
- Dually (mirror, R111): an Odd reactor clock cannot follow σ-released Odd pivots.

## 3. What is left open (and where coupling can still enter)
- (i) Break (B): reactors whose honest play goes to the sources (for Ξ) while τ sends their W-play elsewhere, to a separate pair of
  Even-released W-sources that leapfrog in step with the Ξ-sources. This needs a not-best-reply Odd vertex at every a_j, b_j (R112 rule
  S), i.e. permanent supports, as mkr's W-loops are.
- (ii) Break (A): simultaneous σ- and τ-changes on the same plays (every transition applies both steps; R112's chain has one vertex
  per transition, so it never uses this).
- (iii) One-shot cross gates only: τ releases Even vertices that no Even flip-flop has to follow again (R112's a_i are of this kind).
  One-shot gates cost a vertex each, so they give at most O(n) cross-caused events (R112: 2L + 1 τ-changes at n = 8L + 4).
- (iv) Odd flip-flop holders: an Odd vertex on a reactor's keep play that alternately holds and drops, driven by Odd's own U-rises.
  Its re-hold must itself be W-better for Odd against the current σ, so its "hold" W at re-hold time is low; whether this can still
  delay a reactor more than once is OPEN.
- Reading for G-N5-TIME (not a claim): if (A) and (B) could not be broken, every re-usable clock on one side would be driven by that
  side's own rises, and the other side could only add one-shot delays. That would point AGAINST the mutual binary counter of R111 §4,
  i.e. towards a polynomial bound. The obvious next test is (i) or (ii).

## 4. Addendum (2026-10-29 14:47Z, date -u): route (iv′) and why mkr cannot simply be merged with its dual
- A route that respects §2: let Odd delay mkr's W-SINKS instead of the pivots. w_i's keep goes to a one-shot Odd holder χ_i (τ = a new
  Odd loop Λ_i with T′_K < Λ_i < T_i, so W(keep) ≥ W(T_i) and τ(Λ_i) = self stays U-stable through mkr's EQ escape). h cannot take
  C_{i+1} during the hold, because C_{i+1}'s honest value rises only after w_i switches (its Ξ-menu, Even's own). So the net W-drop at
  w_i (rule D) is followed by nobody, and h's step is still a W-rise. Each pivot step then waits for one Odd event.
- The Odd events must come from an Odd clock (Odd pivots + Odd reactors) whose own W-sinks wait for Even events. The obvious Odd clock
  is the dual of mkr. It does not work as a partner (READING, from S1's order, no instance):
  - mkr lives in an Odd-winning region: every Ξ-play ends at z (odd), every U-play in an Odd self-loop. Its dual lives in an
    Even-winning region (z^d and the dual loops have even priority).
  - Valuations compare cycle nodes first. A cross edge from mkr's χ_i into the dual region gives χ_i's alt an Even-winning U-play, so
    alt is never U-improving for Odd; dually a cross edge from a dual holder ψ_i into mkr is never Ξ-improving for Even. The cross gates
    never open.
  - So both clocks must live in the SAME winning region: an Odd clock in an Odd-winning region (equivalently, the dual of an Even
    clock in an Even-winning region). mkr's W-loops rely on z being odd (Odd self-loops of low odd priority beat z for Even), so this
    needs a new clock design, not a relabelling. OPEN; this is the resume point.
- Same-region Odd clock: DONE (DATA). cpl/ewin.py moves mkr into an EVEN-winning region by priorities only (structural < z, now even <
  loops, now even with their order reversed < h, h′ < markers unchanged). On mkr K, m = (3, 4), (6, 24), (8, 30) the run is state by state
  identical (21, 162, 264 iterations). Its dual (ctl/dualize.py) is an Odd clock in an ODD-winning region, the region mkr lives in:
  instances/dewin_runquad_K3_m4 (from runquad_K3_m4_n54): 21 iterations, 21 τ-changes, 0 σ-changes, every Ξ- and U-cycle node over the
  run has odd priority; n5b = n5.py state sequences; Oink zlk OK, both strategies. check.sh gate.
- Next (resume point): mkr ⊎ dewin with one-shot cross holders. The holder's two options must END IN THE SAME CYCLE in the valuation
  that gates it (cycle nodes are compared first; across copies they differ), and its W must fall below the W-sink's loop only at the
  release. So the two copies' loop priorities have to be interleaved by hand against mkr's W-loop schedule. Not done.
- Climb DATA (cpl/search.py, MODE=flip: fitness = min(most switches of one Even vertex, of one Odd vertex) inside one joint λ-run;
  n 12, 16, 20, two seeds each, ≤ 30,000 steps, explicit starts): best 6 / 7 (n 16), 8 / 6 (n 20). cause.py on the n 12 best (Even
  vertex 7 visits 10, 3, 0, 8, 10, 3, 0; Odd vertex 2 visits 8, 11, 5, 8, 0, 8; one joint λ-run, 8 iterations, 0 fallbacks): every
  switch of vertex 7 and all but the last of vertex 2 are MENU switches (the target entered the own side's improving set at that
  state), i.e. driven by the own side's leapfrogging values, not released by the opponent. Not coupled. Bests not pinned.

## DONE / FINDINGS / NEEDS
- DONE: this note (no new instance; the R112 traces satisfy (A)); cpl/cause.py (MENU vs STALL per switch); flip climb (§4).
- FINDINGS:
  1. READING: each side's menu is autonomous; coupling is only through W, i.e. pivot-rule control (as R110).
  2. READING under (A), (B): τ-released steps lower W at the released vertex; a leapfrog reactor chain needs its sources' W to rise at
     every followed step; so an Even reactor clock cannot be driven by Odd-released pivots (and dually). The "two-sided mkr" of R112 §4
     is DEAD as designed (the holder ladder must decrease, the reactors need it to increase).
  3. OPEN: break (B) (separate W-sources behind not-best-reply Odd a_j, b_j) or (A) (simultaneous changes on one play).
  4. READING (§4): Odd may delay mkr's W-sinks (one-shot holders) without breaking §2; but mkr's dual is in the opposite winning
     region, so cross gates between mkr and its dual never open. The partner clock must be built in the same region. OPEN.
- NEEDS: none from the owner.
