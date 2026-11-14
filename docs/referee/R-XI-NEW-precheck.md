# R-XI-NEW pre-check: R178 Lemma XI-NEW against R104's IDEAL-ACYC model
REFEREE successor 23 (Opus 5.5, D15), 2026-11-03T20:01Z by date -u. This is a PRE-CHECK of a lane lemma (Lead brief, STEP 1), NOT
a signature. P-IDEAL-RED is not frozen yet. When it carries XI-NEW, the packet's own text is refereed again in R-P-IDEAL-RED.md.
I did not read docs/referee-2/.

Object: docs/red/R178-ideal.md §1-§2 on origin/claude/l-red. Last commit touching the file: e03b15a6. Branch head read: 20d3c025.
File sha1 (git show | sha1sum): 7870ad02. Model of record: docs/RESULTS.md R104 (P-N5-REALIZE; the IDEAL model, Ξ-graph ACYCLIC).
XI-NEW is not in docs/RESULTS.md (grep: no hit), so it is a lane lemma, labelled «PROVED, lane».

## Verdict
- IDEAL part (statement, steps 1-3): SOUND on R104's model. It is exact once the indexing and the key are read as R104 states them
  (§1 below). There is no gap in the logic. Two notes are optional, for the packet's text: XI-P1 and XI-P2.
- Consequence (i): SOUND.
- Consequence (ii): SOUND on R104's model (Ξ-acyclic). One gap: XI-G1. «Ξ is monotone» is used but not proved in R178. I give the proof
  in §3 (4 lines); the packet must carry it, or a landed citation.
- Consequence (iii) («D acyclic gives CASC-G (R177) again: E ≤ height»): NOT CHECKED. It rests on R177, which is not landed. D is
  not defined in R178. A packet using (iii) carries its proof.
- «Real N5» half of the statement: NOT A PROOF at referee standard (XI-G2). It lies outside R104's model. A packet must not use it
  unless it carries a full proof.

## 1. The statement in R104's terms (exactness)
- Run: s_0 = the start, s_1, …, s_L. L = L(G) is R104's step count: «the run stops when nothing is available or nothing changes».
- A_j(x) = {s_j(x)} ∪ {k : Ξ_(s_j)(x, k) ▷ Ξ_(s_j)(x, s_j(x))}.
  - This is R104's «its current option and the options with a strictly better Ξ-value». Availability is read at the OLD state s_j.
- s_(j+1)(x) = the option of A_j(x) with the lexicographically least key.
  - key_(j+1)(x, k) = the gate indices of the chain of W-targets under the NEW state s_(j+1), lowest level first, ending in g(x, k).
- XI-NEW (IDEAL): for every t with 2 ≤ t ≤ L, let h be a mover of least lev among {x : s_t(x) ≠ s_(t−1)(x)}, and let w = s_t(h).
  Then w ∉ A_(t−2)(h).
- R178's «fallback-free run» corresponds to R104's steps 1..L(G).
  - R104's run stops where N5 would fall back (S4c), so every step t ≤ L is a fallback-free IDEAL step.
  - With R178's FB=1 continuation the statement does not apply across a fallback. It is not claimed there.
- XI-P1 (optional, wording): R178 §1 writes «σ_(j+1) = the S1 optimum … equal to TB's lex-min tree». The proof needs the R104 form:
  keys are read under the NEW state, level by level.
  - That form is well-defined because a key at level ℓ reads only s_(j+1) at levels < ℓ.
  - The packet should quote R104's wording, not R178's.

## 2. Proof check (IDEAL, steps 1-3)
1. Every key of an option (h, k) reads s only at movers on the W-target chain. Those have lev < lev(h) (W-target of level lev − 1).
   - No mover of lev < lev(h) moves at step t, by the choice of h. So s_t = s_(t−1) on all of them, and key_t(h, k) = key_(t−1)(h, k)
     for every k.
   - At lev(h) = 0 the key is (g(h, k)) alone, and the step is vacuous. Correct.
2. Let o = s_(t−1)(h). R104's step moves EVERY mover (also one that stays) to the key_(t−1)-least option of A_(t−2)(h). So o is that
   option.
   - Every key ends in its own gate index, and R104 makes gate indices distinct. So the keys of distinct options of h are distinct, and
     the order is strict.
   - h moves at step t, so w ≠ o. If w ∈ A_(t−2)(h), then key_(t−1)(w) > key_(t−1)(o).
3. o = s_(t−1)(h) ∈ A_(t−1)(h) (the current option is always available), and w = s_t(h) is the key_t-least option there. So
   key_t(w) < key_t(o).
   - Step 1 transports this to key_(t−1)(w) < key_(t−1)(o). That contradicts step 2. □
- The proof uses neither Ξ's structure nor acyclicity. It uses only: A_j(x) ∋ s_j(x); argmin of a strict key; keys reading only
  lower levels.
- XI-P2 (optional): say so in the packet. «Least» means least lev among the vertices that move at step t. When several movers tie, the
  claim holds for each of them.

## 3. Consequences
- (i) For each step t ≥ 2, the least-level mover h_t gives an event (t, h_t, w_t) with w_t ∉ A_(t−2)(h_t). The map t ↦ event is
  injective, so L ≤ 1 + E. SOUND.
  - Wording note: w ∉ A_(t−2)(h) also says w ≠ s_(t−2)(h). §0's «not Ξ-better than its current one at t − 2» should say «not in
    A_(t−2)(h)».
- (ii) Chain of inequalities. Write F_j(k) := Ξ_(s_j)(h, k).
  - F_(t−2)(w) ⊴ F_(t−2)(s_(t−2)h), since w ∉ A_(t−2)(h). Ξ is a total order on h's options: the β-sets differ, because each set
    contains its own option's distinct β, and in the acyclic case a chain never returns to h.
  - F_(t−2)(s_(t−2)h) ⊴ F_(t−2)(s_(t−1)h), since s_(t−1)(h) ∈ A_(t−2)(h).
  - F_(t−2)(s_(t−1)h) ⊴ F_(t−1)(s_(t−1)h), by MONOTONICITY (below).
  - F_(t−1)(s_(t−1)h) ◁ F_(t−1)(w), since w ∈ A_(t−1)(h) and w ≠ s_(t−1)(h).
  - Hence F_(t−2)(w) ◁ F_(t−1)(w): a strict rise. Equal chains give equal values, so some mover on w's Ξ-chain under s_(t−2) moved at
    step t − 1. SOUND, given monotonicity.
- XI-G1 (GAP, closable). Monotonicity is asserted («Ξ is monotone, and h only moves upward») but not proved in R178. Proof on R104's
  model:
  - Claim: for every mover y, V_(j+1)(y) ⊵ V_j(y), where V_j(y) = Ξ_(s_j)(y, s_j(y)).
  - Induct along the Ξ-graph's topological order, from the sinks (Ξ-target X) back.
  - Ξ_(s)(y, k) = {β_(y,k)} ∪ V_s(xt(y, k)), or {β_(y,k)} when xt = X. In the acyclic case β_(y,k) lies in neither union operand.
  - So adding the same fresh β to two sets keeps their order: the symmetric difference is unchanged.
  - Then V_(j+1)(y) = Ξ_(s_(j+1))(y, s_(j+1)y) ⊵ Ξ_(s_j)(y, s_(j+1)y) by induction, and Ξ_(s_j)(y, s_(j+1)y) ⊵ V_j(y) because
    s_(j+1)(y) ∈ A_j(y).
  - The same argument gives F_(j+1)(k) ⊵ F_j(k) for every option. □
  - Acyclicity is used here. For Ξ-cyclic genomes, which R104 does not cover, this proof does not apply.
- (iii) NOT CHECKED (R177 not landed; «D» undefined in R178).

## 4. «Real N5» half (XI-G2, outside R104)
- R178's real-game «remarks» are not a proof.
- In a real FL run, R24 (b)'s choice rule picks the key-least among options TIED under W′ (Lead reading L46), not among all of
  A_(t−2)(h).
  - Step 2 then needs: w ∈ A_(t−2)(h) ⇒ w tied at step t − 1. The remarks do not show this.
  - The key also differs at odd W′-cycle nodes (smallest index).
- Corners are excluded, but the W-length grading that step 1 needs («prefixes have smaller W-length») is asserted, not derived.
- A packet that uses the real half must carry a full proof. R104 (Theorem REALIZE) already transports IDEAL-ACYC runs, so the IDEAL half
  is enough for IDEAL-ACYC statements.

## 5. Own DATA (docs/referee/scratch/xinew_probe.py, written from R104's text only; logs in xinew_logs/)
- What the probe does:
  - generates random acyclic IDEAL genomes and runs R104's step;
  - checks XI-NEW at every least-level mover for every t ≥ 2;
  - checks monotonicity of every option's Ξ-value between consecutive states, and the strict rise of (ii).
- Results:
  - MUT 0 (R104), small genomes, seed 1: 3,000 genomes, 236 checked steps, 0 violations.
  - MUT 0, BIG=1, seeds 2-4: 4,500 genomes, 1,925 checked steps (L up to 5), 0 violations, 0 monotonicity failures, 0 missing rises.
  - Controls bite.
    - MUT 1 (keys read the OLD state): 203 violations (small) and 206 violations (BIG).
    - MUT 2 (current option not kept in A): 1,484 violations.
- Limits:
  - Random genomes give short runs (L ≤ 5).
  - I did not run the lane's champions (r178/out/*.json; L 17-64), because I have no reader for their format.
  - The proof (§2) is the evidence, and the DATA is a sanity check only.

## Notes for P-IDEAL-RED (for the packet author, via the Lead)
- XI-G1: carry the monotonicity proof (§3), or cite a landed item for it.
- XI-G2: use the IDEAL half only, or carry a full real-N5 proof.
- (iii): carry its proof if it is used.
- XI-P1: quote R104's key («under the new state»).
- XI-P2: «least» = least lev among the vertices that move at step t, with any tied mover allowed.
- §3 (i) wording: say «not in A_(t−2)(h)».
