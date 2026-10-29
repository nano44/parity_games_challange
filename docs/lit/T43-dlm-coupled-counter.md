# T43: DLM's coupled Even/Odd counter, the exact step where N5 escapes it, and the design target for a coupled N5 family (for L-RED 27)
L-LIT successor 2 (Opus 5.5), D18. Lead's message 14:15Z: «Extract, with theorem and section numbers: (a) DLM's mutual mechanism ... (b) The
exact step where N5 escapes it ... (c) What a coupled N5 family would need to restore that step, stated as a one-paragraph design target for
L-RED.» Written 2026-10-29 from 14:20Z (date -u). Working note; source facts from the opened paper, N5 facts as DATA (runs below), nothing
signed. Not a TARGET.md claim. Source: van Dijk, Loho, Maat, "The worst-case complexity of symmetric strategy improvement", arXiv 2309.02223 v1
(CSL 2024), pdf sha256 10e6794d82aba465… (re-opened 2026-10-29). Fleet prior work used and checked here: L-NEW box 5 (docs/new/N5-dlm-box5.md,
K6) and T20 (docs/lit/T20-N5-barriers.md).

## (a) DLM's mutual mechanism (§4, family 1 = Table 1 p.9, Fig. 3; Proposition 7 p.10; Observations 8-10 p.10-11; §6 Lemma 12 p.14)
- The rule. SSI (their Algorithm 2, p.7): I ← f((Iσ ∩ {(v, τ̄(v))}) ∪ (Iτ ∩ {(v, σ̄(v))})): a player may switch v only to the opponent-best-reply
  edge, and only if that edge is improving in its own frame (τ̄ = Even's best reply to the CURRENT τ, σ̄ = Odd's best reply to σ).
- The game G_n (Table 1). Even vertices a_1..a_n (priority 2i + 1, ODD), Odd vertices d_1..d_n (priority 2i + 2, EVEN); a_i → {a_1, a_{i+1},
  d_{i+1}}, d_i → {d_1, a_{i+1}, d_{i+1}}; sink a_{n+1} (priority 1), d_{n+1} (priority 2n + 4, the largest even). Start σ_0(a_i) = a_{i+1},
  τ_0(d_i) = d_{i+1}. Even wants the pebble to pass d_{n+1}; Odd wants to avoid it. The optimal strategies differ from the start in ONE edge each
  (σ(a_n) = d_{n+1}, τ(d_n) = a_{n+1}) (p.10).
- The coupling (Observation 8, p.10): «As long as σ(a_j) = a_{j+1}, we have σ̄(d_j) = d_1. Likewise, as long as τ(d_j) = d_{j+1}, we have
  τ̄(a_j) = a_1.» So each player's best reply at level j reads the OTHER player's current choice at level j. Observation 10 (p.11): (a_j, a_1)
  is improving only when the lower levels are at their G_{j−1}-optimal pattern (σ(a_i) = a_{i+1} for i < j − 1, σ(a_{j−1}) = d_j); (d_j, d_1) is
  never improving.
- Which switches carry the bits, and how one level is counted (proof of Proposition 7, p.10-12): the run on G_j is
  1. 2^j − 3 iterations = the whole run on G_{j−1} (levels < j; by Observations 8-10 levels j, j + 1 do not move);
  2. ONE iteration, the only switch (a_j, a_1) (Even: Prof ∩ τ̄ = {this edge} once level j − 1 is optimal);
  3. ONE iteration, the only switch (d_j, a_{j+1}) (Odd), possible because now σ = τ̄ («We have σ = τ̄», p.11);
  4. ONE iteration, the only switch (a_j, d_{j+1}) (Even), possible because now τ = σ̄ (p.11-12);
  5. 2^j − 3 iterations = a fresh run on a copy of G_{j−1}.
  Total 2^(j+1) − 3. The bit of level j is carried by BOTH players in turn: Even's a_j moves twice (a_1, then d_{j+1}) and Odd's d_j once, and each
  of the three single switches is enabled only by the previous switch of the OTHER player (σ = τ̄, then τ = σ̄).
- How resets happen (p.12, "The final 2^j − 3 iterations"): after step 4, «we might as well replace d_j by a sink node of priority 1, and a_j by a
  node with priority 2j + 2 ... But then we have again a copy of G_{j−1} with its respective starting strategies.» No explicit reset switch: the
  lower levels' current (G_{j−1}-optimal) strategies become the START strategies of the transformed lower game, so the lower counter re-counts.
- Rule-independence (Lemma 12, p.14): along these runs every iteration has a single relevant improving move (others are "irrelevant"), so the
  count holds for every improvement rule f inside the SSI candidate set; Theorem 13 (p.15) extends to generalised SSI (Alg. 3, family 2,
  7·2^(n−1) − 5, Proposition 11 p.13). §7 (p.15): players «are distracted by their opponent's (bad) strategy».

## (b) The exact step where N5 escapes (SPEC S4a / S4b vs SSI's candidate set; DATA from runs)
- The step. SSI may switch Even v only to τ̄(v), and only if (v, τ̄(v)) ∈ Iσ. N5's S4a takes Even's W-optimum (against the current τ) over the
  WHOLE arena A_σ(v) = {σ(v)} ∪ Iσ(v) at all Even vertices jointly (S4b dually for Odd, against σ). When τ̄(v) ∉ A_σ(v) — DLM's distraction:
  Observation 8 makes τ̄(a_j) = a_1 while Observation 10 makes (a_j, a_1) non-improving — SSI must keep σ(v); N5 takes the W-best IMPROVING
  alternative. L-NEW box 5 §2 measured exactly this on every state of SSI's runs (dlm1, dlm2, n = 2..5): N5's step never omits a switch SSI
  makes and never switches a vertex differently; it only ADDS switches, at 100% of the distracted vertices (342 Even, 399 Odd vertex-events).
  So the escape is S4a's (and S4b's) joint W-optimum over the improving arena, not GATE-SHUT, not the λ-run structure.
- What the added switches are (this note, L-SI's rows() over L-NEW's experiments/new/dlm_gen.py 1 n, read only; counts = SPEC's reference
  1, 2, 4, 4, 6, 7, …): N5's FIRST iteration on dlm1 switches every a_i to d_{i+1} and every d_i to a_{i+1} at once (n = 3: a1→d2, a2→d3,
  a3→d4 | d1→a2, d2→a3, d3→a4; the same for n = 4, 6). These are the edges SSI takes only at step 4 / step 3 of each level, after 2^j − 3
  iterations of the lower counter. N5 sets every level's final edge in iteration 1, so the recursion never starts; the remaining 3-6 iterations
  are local repairs (n = 6: 7 iterations, 0 fallbacks; one phase of length 1). SSI on the same dlm1 n = 3: 13 = 2^4 − 3 iterations, with the
  distraction failing at Even a2, a3 and Odd d2, d3 in its first iteration (experiments/new/dlm_diag.py, read only).
- Why the jump edge is available to N5. (a_j, d_{j+1}) is Ξ-improving at the start (N5's arena contains it: N5 switches to it), and against
  τ_0 (τ_0(d_i) = d_{i+1}, the d-chain leads to d_{n+1}) it is W-optimal. DLM's level-j lock on that edge is ONLY the distraction (τ̄(a_j) =
  a_1), i.e. it lives in SSI's selection rule, not in the improving set. N5's selection ignores τ̄ and keeps only the improving set.
- Box 5 §3 adds: Odd "blunder" dummies that keep SSI exponential make N5 FASTER (its joint optimum exploits the blunder); K6: a module would need
  a local stall (σ(v) W-optimal in the arena) at every distracted vertex, persistent along SSI's path.

## (c) Design target for a coupled N5 family (one paragraph, for L-RED 27)
DLM's counter is locked in the SELECTION rule (switch only to the opponent's best reply), and N5's selection is the W-optimum over the whole
Ξ-improving arena, so every DLM lock that is not also an improving-set lock is skipped in iteration 1. A coupled N5 counter must therefore put
every lock into the ARENAS: for each level j, the level's final edges (Even's jump, the analogue of (a_j, d_{j+1}), and Odd's, the analogue of
(d_j, a_{j+1})) must be OUTSIDE Iσ (resp. Iτ) — non-improving in N5's improving-set frame (Ξ, against σ̄, for Even's edge; Ξ^d,
against τ̄, for Odd's) — until the lower counter completes, and must enter the improving set exactly then; and at every state, for every vertex whose
switch is not the intended bit, every Ξ-improving alternative must be W-no-better against the opponent's CURRENT strategy than staying (a
local stall in S4a/S4b's frame, which needs the D = {σ̄ ≠ τ} gap on the plays from those alternatives, "optimism-trapped" in L-SI's box 29 §5
sense). Each player's bit move must be enabled by the other's previous move through the improving set (σ̄ or τ̄ changing because the opponent
moved), not through the selection, because N5 computes both steps from the same (σ, τ) and applies them together (SPEC S4) — DLM's
three-iteration hand-off (Even set → Odd follows since σ = τ̄ → Even jumps since τ = σ̄) must become three arena changes in three consecutive
iterations. Resets must again be implicit (the lower levels' current strategies becoming the start of a fresh lower counter), and Odd's
gates must avoid GATE-SHUT's hypotheses (P-N5-MPGS (B): a shut Odd gate with (H1)-(H3) stays shut), e.g. by keeping a cycle node above the gate
((H1) false), as R109's topfix does. Fallbacks must not fire (a fallback is a switch-all step in Ξ and would set several bits at once).

## DONE / FINDINGS / NEEDS
- DONE: this note; runs of N5 (L-SI's experiments/si/root/common.py rows(), i.e. L-NEW's n5x engine) and of SSI (experiments/new/dlm_diag.py)
  on dlm1 n = 3, 4, 6 generated with experiments/new/dlm_gen.py, all read only (scratchpad t43/; not committed). L-COMP's n5b was not re-run:
  box 5 §3 already reports n5.py = n5b spec = n5b orig on dlm1 / dlm2 n = 1..8.
- FINDINGS:
  - DLM's bits are carried by alternating single switches of BOTH players (Prop. 7 steps 2-4), each enabled by the other's last switch through
    the best-reply condition (Obs. 8); resets are implicit relabellings of the lower counter (p.12).
  - N5 escapes at S4a/S4b: the joint W-optimum over the improving arena takes the improving edges SSI withholds (box 5: at 100% of distracted
    vertices). On dlm1 it sets every level's final edge in iteration 1.
  - Design target: all locks in the improving sets (Ξ / Ξ^d), local W-stalls via the D-gap elsewhere, hand-offs as arena changes, implicit
    resets, no fallbacks, Odd gates with (H1) false.
- NEEDS: none from the owner.
