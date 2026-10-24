# N5 on o-acyclic one-Odd-choice games is polynomial: (STAT) closed (box 24; READING, unrefereed)
L-NEW successor 8 (Opus 5.5, D15). Lead GO 2026-10-24 03:05Z; argument found and checked 03:00-03:08Z; reported to the Lead 03:09Z
(date -u), before this write-up.
Status:
- A polynomial bound on N5 on a SUBCLASS that is polynomial by other means, in the same sense as RESULTS R17. It is not a
  TARGET.md claim, and gauntlet step 4 for N5 is not passed.
- READING with a complete proof sketch; not refereed; NOT landed (D1).
- Depends on L-RED's Proposition X (docs/red/R58-n5-width.md §9, unrefereed), on premise (P), and on RESULTS R17. G-N5-TIME stays
  OPEN.
- (P) is VJ00 Lemma 5.8 "1 ⇒ 2" ("no improving edge ⇒ optimal"). It is the same premise as R15 G-N5T-3 and R58's Theorem W, and
  is used here only on the one-player game G[X].

## Statement
Let G be a parity game in which exactly one Odd vertex o has out-degree d > 1, and o lies on no cycle of the game graph
("o-acyclic 𝒞^1O"). Let:
- X := the vertices with no path to o, and Y := V \ X;
- m_X := the number of edges inside X;
- σ = Even's strategy and τ = Odd's (only τ(o) is a choice).
Then N5 (docs/new/N5-ssi-global.md SPEC S1-S5), from ANY start pair, makes fewer than
    (C_X + d) · (B + 1) iterations,
where C_X < (|X|² − |X| + 1)(|X| + m_X) and B < (n² − n + 1)(n + m).

## Proof (READING)
Notation.
- Ξ = Even's honest valuation; θ = Ξ(o); W = V_{σ,τ}, the play values against τ; w = W(o).
- A transition k → k+1 is PURE if σ|X and τ are unchanged.

0. Two facts used throughout.
   - o lies on no cycle, so every successor of o is in X.
   - X is closed under successors and has no Odd choice.
1. Prop X (L-RED): the distinct values of σ|X along N5 form N5's run on G[X], which takes fewer than C_X steps. The X-part of every
   S4a step is G[X]'s S4a step at σ|X, by the locality of S1's procedure (R58 §9 step 1). τ changes at most d − 1 times
   (RESULTS R15 (c); box 21 §3.4). So there are at most C_X + d − 1 non-pure transitions.
2. Lemma 1. At a pure transition from state k, σ_k|X has G[X]'s optimal valuation.
   - G[X]'s S4a step is null at σ|X, since σ|X did not change and no global fallback touched X.
   - Case Iσ|X = ∅: σ|X has no improving edge, so it is optimal by (P).
   - Case Iσ|X ≠ ∅: the arena optimum returns σ|X. For every improving (x, z), (F1) gives val_σ(x) ⪰ val_ρ̂(x) with
     ρ̂ = σ[x → z]. R17's case analysis (N5-phase-bound-box10.md §2, Case B: B1, and B2 with D ≠ ∅ or top(Z) ≠ x) contradicts
     each case except B2 with D = ∅ and top(Z) = x. So every improving edge is value-flat at x's own cycle node.
   - Switching flat edges leaves every valuation unchanged and only shrinks improving sets (R17 Theorem PH proof, last
     paragraph). After at most m_X such switches none remains. So the current valuation is that of a strategy with no improving
     edge, which is optimal by (P). □
3. Lemma 2. At a pure transition from state k, θ_k = w_k.
   - For an exit e of o (e ∈ X), Odd's honest valuation Ξ^d_τ(e), read in G's order (Lemma R), is U_τ(e) = max over σ' of
     V_{σ',τ}(e) (Lemma S (a)). Plays from e stay in X, where Odd has no choice, so this is G[X]'s optimal value at e. By
     Lemma 1 it equals the current value Ξ_k(e).
   - Let a := σ̄(o) and b := τ(o). Then θ = o ⊕ Ξ(a), w = o ⊕ Ξ(b), and θ ⊴ w.
   - If θ ◁ w, then Ξ(a) ◁ Ξ(b) (the prefix by o is strictly monotone, since the paths from exits avoid o). So in Odd's honest
     order a beats b, i.e. (o, a) ∈ Iτ (S2 on G^d, Lemma R).
   - S4b then runs. Odd's arena optimum against σ_k is pointwise optimal (R17 (F1) in the dual). Exit a is in the arena and gives
     o a strictly better value for Odd than b, so τ_{k+1}(o) ≠ b. The transition is not pure, a contradiction. □
4. Lemma 3. At a pure transition from state k, Ξ_k = W_k at every vertex.
   - A vertex whose σ-path avoids o meets no Odd choice, so its two plays coincide.
   - A vertex v whose σ-path reaches o has both plays equal to π_v (inside Y, o excluded) followed by o's continuation (inside X,
     via a or via b).
   - The two continuations have equal valuations (Lemma 2), so the same cycle node, path set and length. π_v is disjoint from
     both, so the valuations of v agree. □
5. Hence a pure transition from state k is exactly an N5 step of the one-player game G_{τ_k} (Odd fixed to τ_k):
   - the gate Iσ_k equals G_{τ_k}'s improving set (Lemma 3);
   - S4a is the same computation (the arena optimum against τ_k);
   - S4b produced τ_k again;
   - S4c fires on G exactly when S4a is null, which is when it fires on G_{τ_k}, with the same rule and keys (Ξ = W).
   - Iσ_k ≠ ∅: otherwise the iteration would move τ.
   So a maximal run of pure transitions is a segment of N5's run on the one-player game G_{τ}. RESULTS R17 Corollary 2 bounds
   such a run by (n² − n + 1)(n + m). Its proof (Lemma P, Theorem PH, the phase count) starts from an arbitrary strategy, so it
   applies to a segment. □
6. Counting. Pure blocks are separated by non-pure transitions, so there are at most C_X + d − 1 separators and at most C_X + d
   blocks:
       #iterations ≤ (C_X + d − 1) + (C_X + d)·B < (C_X + d)(B + 1). □

## Checks (DATA; experiments/new/box22/statcheck.py)
L1 is "θ = w at every pure state", L2 is "Ξ = W at every vertex there", and L3 is "every maximal pure block equals the N5 run on
G_τ from its first σ".
- Canonical runs: 1,352 random o-acyclic 𝒞^1O games (n 5..18, with forced Odd vertices). 81 pure states, 74 blocks;
  0 failures of L1, L2, L3.
- Random start pairs: 1,417 games. 103 pure states, 95 blocks; 0 failures.
- Climbed instances: statY_12 (7 pure states, one block of 7) and the climbY n 20 / 28 bests; 0 failures.
- Negative control (o on a cycle): fts_best16 (box 21). L1 and L2 fail at 24 of 28 pure states, and L3 fails. The hypothesis
  is necessary for the argument as written.
- Consistent with box 22: 0 blocks with θ ◁ w in 6,000 random o-acyclic games (statprobe.py).
- Random games give short blocks (max 3), so the DATA tests the lemmas, not the bound's tightness.

## What it does not do
- The o-CYCLIC case is untouched. There exits route back through o, X may be empty (fts_best16, L-RED's frz24), Lemma 1 has no
  analogue, and the σ̄ laps of box 21 §3.4 occur.
- Box 22's (SEG-1O) and (CH-1O) remain OPEN there.
- The proof uses no per-path invariant. It shows that on o-acyclic games the throttle θ ◁ w cannot survive a pure step, which is
  why the I1-I4 failures (box 22) do not matter here: i4_hand's deadlock lives on NON-pure steps (its lane is in X).
- Dependencies to referee: Prop X (L-RED), Lemmas R and S (box 21, mine), Lemma 1's flat case (it uses R17's Case-B analysis at
  an arbitrary state), and (P).
