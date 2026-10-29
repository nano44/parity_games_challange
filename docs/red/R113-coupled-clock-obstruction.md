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

## DONE / FINDINGS / NEEDS
- DONE: this note (no new instance; the R112 traces satisfy (A)).
- FINDINGS:
  1. READING: each side's menu is autonomous; coupling is only through W, i.e. pivot-rule control (as R110).
  2. READING under (A), (B): τ-released steps lower W at the released vertex; a leapfrog reactor chain needs its sources' W to rise at
     every followed step; so an Even reactor clock cannot be driven by Odd-released pivots (and dually). The "two-sided mkr" of R112 §4
     is DEAD as designed (the holder ladder must decrease, the reactors need it to increase).
  3. OPEN: break (B) (separate W-sources behind not-best-reply Odd a_j, b_j) or (A) (simultaneous changes on one play).
- NEEDS: none from the owner.
