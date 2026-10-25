# N5 on 𝒞^1O, box 40 (3): Q states (H1 ∧ H2 ∧ ¬H3) — the last out-of-SN piece. Inside a Q-run, S4a steps never evict and fallbacks never enter (Q-SPLIT); the break count is OPEN (start for successor 20)
L-NEW successor 19 (Opus 5.5, D15/D18), session_011reTXakSJCcwLhC4i9ZpkB. Working doc (not a packet). Written 2026-10-25 17:2xZ by date -u.
- Setting and notation: docs/new/P-N5-RHO-box40.md §0 and docs/new/P-N5-NHN-box40.md §0. A Q STATE has H1 ∧ H2 ∧ ¬H3 (c_w ≠ c_θ). A
  Q-RUN is a maximal run of consecutive Q states of one phase. t0 := τ(o); c′ := λ(t0) (a phase constant).
- Labels: PROVED (L-NEW succ. 19, unrefereed), CONJECTURE, OPEN, DATA.

## 1. Where Q states live (PROVED, from P-N5-NHN §6)
- In a phase with a Q state: t0 ≠ o (τ(o) = o gives ¬H2 everywhere), c′ ≠ c_θ (H3-CONST, RESULTS R33 (a): c_w = c′ at H2 states), the
  phase has NO HN state (H3-IN-HN), so every state is Q or ¬H1. Fallbacks at ¬H1 states: RESULTS R38 (e) NH1-FB. Q-runs per phase:
  ≤ ⌈T/2⌉ + 1 (they are separated by H1-toggles; RESULTS R34 (e)).
- At a Q state: t0 ∈ F (H2), c′ ∉ U (λ(c′) = c′ ≠ c_θ), R̄ ⊆ U ((HP)), W(z) = π_z ⊕ w for z ∈ R̄ with cycle node c′, and
  reward(c_θ) < reward(c′) (XW, RESULTS R21 (a), with distinct cycle nodes).

## 2. Lemma Q-SPLIT (PROVED)
Statement. (a) At an in-phase S4a transition k → k+1 with H1 at k and c_w(k) ≠ c_θ (an HN or a Q state): R_k ⊆ R_{k+1}.
(b) At an in-phase Even fallback k → k+1 from a Q state with H1 at k+1: R̄_{k+1} ⊆ R̄_k.
Proof.
- (a) Let z ∈ R_k. Its (σ_k, τ)-play reaches o and ends on o's W-play's cycle, so W_k(z) has cycle node c_w(k). σ_k is a strategy of S4a's
  arena, so (F1) (RESULTS R17 (a)) gives W_{k+1}(z) ⊵ W_k(z). If z ∈ F_{k+1}, then W_{k+1}(z) = Ξ_{k+1}(z) (G (a), RESULTS R19 (a)), whose
  cycle node is λ(z) = c_θ (z ∈ R_k ⊆ U; λ constant on the phase). XW at k with distinct cycle nodes gives reward(c_θ) < reward(c_w(k)),
  so W_{k+1}(z) ◁ W_k(z), a contradiction. So z ∈ R_{k+1}. (For HN states this re-proves SPLIT (a), RESULTS R39 (a).)
- (b) Suppose R̄ gains a vertex. ACT (i) (RESULTS R23 (b), as restated in P-N5-PFZ §0: "if R̄ gains a vertex, some switched Even
  s ∈ F_k with σ_{k+1}(s) ∈ R̄_k enters") gives such an s, with s ∈ R_{k+1}; by R15 (d), (s, σ_{k+1}(s)) is a gate at k from F_k into
  R̄_k. FBL-N (ii) (RESULTS R21 (c)): a gate (s, z) with s ∈ F_k at an S4c fallback with τ unchanged has s = λ_W(s) and λ_W(z) = s. For
  z ∈ R̄_k, λ_W(z) = c_w(k) = c′, so s = c′. Under H1 at k+1, R_{k+1} ⊆ U ((HP)), so λ(c′) = c_θ; but λ(c′) = c′ ≠ c_θ on the phase.
  Contradiction. □ (ACT (i) wording checked against RESULTS R23 (b).)
- Consequence. Inside a Q-run every crossing is an entry at an S4a step or an eviction at a fallback, as in an HN stretch (SPLIT).

## 3. CONJECTURE Q-EPOCH (transfer of EPOCH)
- EPOCH (RESULTS R39 (b)): per HN stretch X_S ≤ 2(n − 1)(B + 1), f_S ≤ K(X_S + 1) + X_S, from SPLIT and FB-INT. Its proof should use
  only "S4a never evicts, fallbacks never enter" (Q-SPLIT) and FB-INT (every game in 𝒞^1O): CHECK P-N5-OUT §2's proof line by line.
- If it transfers: Q fallbacks per Q-run are polynomial in the breaks B_Q of the run.

## 4. OPEN: breaks in Q-runs
- RISE′ (P-N5-PFZ §5) needs "no gate F → R̄ at the fallback state a" (Step 0). At a Q fallback, FBL-N (ii) leaves exactly the gates from
  c′ into R̄ (W-flat, both W-cycle node c′). They may exist without being taken (c′ switches to its Ξ-best edge). So Step 0 can fail;
  Step 3's "no gate F → R̄ at t" too. Obstruction to check in data: a Q fallback state with a gate c′ → R̄.
- θ, HAT-FREEZE, RHO-TAIL hold on Q states unchanged (they do not use ¬H2); P-FREEZE's post-freeze crossings argument (NO-CROSS-A)
  used SEP-o, which also holds at H1 states. So a BRK-POLY′ analogue may go through once Step 0 is handled.

## 5. DATA (experiments/new/box40/qsurvey.py; P-N5-RHO §8's 412-file list, canonical start)
- 165 phases with Q states, 186 Q states; no Q state in a phase with τ(o) ≠ o and an HN state (H3-IN-HN).
- Q fallbacks: 2 in all (oneodd_c16, one phase), both evictions. S4a steps at Q states with a vertex leaving R: 0 (Q-SPLIT (a)).
  Q entries 6, Q evictions 2. Longest Q-run 13 states. THIN: Q fallbacks are rare in the library; a climb for them is the next tool.
