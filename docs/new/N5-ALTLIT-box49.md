# N5-ALTLIT (box 49): Friedmann's globally-optimal lower bound and Hansen-Miltersen-Zwick's discounted upper bound, read against ALTERNATION (READING, sources opened)
L-NEW successor 29 (Opus 5.5), D14 / D18, Lead reading L40. Lead's word of 18:36Z (message): "A literature step on the main open count ...
Open the FULL texts ... Then answer, as a READING with the sources opened: (i) ... (ii) ...". Written 2026-10-26 from 18:51Z (date -u).
Labels: READING throughout (no statement here is to be signed); PROVED / OPEN only where marked. Not a TARGET.md claim; G-N5-TIME stays open.
The open count: docs/si/N5-EXIT-box22.md §9 (L-SI successor 18, l-si 196c7e8c, opened): ALT_c(S), the transitions of a λ_W-constant
fallback-free run S of one phase at which σ̄ changes at a gate of class c (with a D or D-direct offset change); OPEN whether it is polynomial.

## 0. Sources (full texts opened; recorded in notes/L-NEW.md "Sources opened")
- [F] O. Friedmann, "An exponential lower bound for the latest deterministic strategy iteration algorithms", Logical Methods in Computer
  Science 7(3:19), 2011, 42 pp.; arXiv 1106.0778 (pdf sha256 46c96f44775aa2b0…). Read: §3 (valuations ϑ = (w1, path set, k), the
  improvement arena A_{G,σ}, Theorem 3.2 [VJ00]), §4 (policies; I^loc; I^glo, Theorem 4.2 [Sch08]; Lemma 4.3 [Vög00] and the remark after
  it), §5 (1-sink games: Sink Existence, Sink Seeking; Lemma 5.1), §6.1 (simple cycles), §6.5 (the counter's four phases, Lemmas 6.8-6.12),
  §8 (I^glo: 8.1 modified deceleration lane, 8.2 stubborn cycles, 8.3 modified cycle gate, 8.4 construction, Theorem 8.4), §9 (Theorem 9.8,
  Corollaries 9.9, 9.10).
- [HMZ] T. D. Hansen, P. B. Miltersen, U. Zwick, "Strategy iteration is strongly polynomial for 2-player turn-based stochastic games with a
  constant discount factor", arXiv 1008.0530v1, 3 Aug 2010, 13 pp. (pdf sha256 f53a6b5127d95078…). Read: §2 (Definitions 2.1-2.7, Theorem
  2.8), §3 (Lemmas 3.1-3.12), §4 (Lemma 4.2, Corollary 4.3, Lemma 4.5), §5 (Lemmas 5.1-5.5), §6 (Lemmas 6.1-6.4, Theorem 6.5), §7.

## 1. What the two papers prove (their statements, paraphrased with numbers)
- [F] Theorem 8.4: the strategy improvement algorithm with the globally optimizing policy I^glo needs at least 2^n improvement steps on H_n
  from ι_{H_n} (Theorem 6.14: the same for I^loc on G_n). I^glo (§4): given σ, σ* = I^glo(σ) is Ξ-optimal among all strategies of the
  improvement arena A_{G,σ} (edges not worse than σ in Ξ_σ), i.e. a one-step lookahead. Valuations Ξ_σ are against player 1's OPTIMAL
  COUNTERSTRATEGY τ_σ (Lemma 3.1 [VJ00]); player 1 never improves a strategy of its own.
- [F] §5: both families are 1-SINK games: one odd sink v* (self-loop, least priority), reachable from all nodes, and "Sink Seeking": for every
  σ reached from ι, the cycle component of Ξ_σ(w) is v* for every node w. So only path components move ("there are only linearly many
  different values for the first and third component while there are exponentially many for the second").
- [F] §6.1 / §8.2: player 1's only real choices are the e_i (one per bit, inside the simple / stubborn cycles); the construction assumes "it
  is more profitable for player 1 to move into the cyclic structure as long as it is not closed". Opening and closing these cycles is how the
  counter counts (§6.5: phase 1 waiting, 2-3 set bit μ_b, 4 reset lower bits; Lemmas 6.8-6.12).
- [F] Corollary 9.9: on a 1-sink parity game, Ξ_σ(v) ≺ Ξ_σ(u) iff the induced discounted game H = IndDPG(IndMPG(G)) ranks the plays the
  same way (R_H). So the parity runs ARE discounted runs, with the discount factor part of the input (Corollary 9.10; [HMZ] §7 says the same).
- [HMZ] Theorem 6.5: strategy iteration (player 1 switches to P1 v, player 2 best-responds) terminates after at most (m + 1)(1 + log_{1/γ}
  (n²/(1 − γ))) = O(m/(1 − γ) · log(n/(1 − γ))) iterations, γ the fixed discount.

## 2. Question (i): does Friedmann's I^glo family need τ or λ to change between its phases? Could it fit inside ONE N5 phase?
- On the Ξ side, NO change is needed: by construction λ_Ξ is constant for the whole run (Sink Seeking, [F] §5 (2)), and [F]'s "phases"
  (§6.5) are sets of player 0 strategies, not changes of anything player 1 owns. So the Ξ-part of an N5 phase boundary is never forced by
  the construction.
- But the family is NOT an N5 run, and nothing in [F] says what N5 does on it:
  - (a) Choice rule. I^glo picks the Ξ-optimal successor (against the best response τ_σ); N5's S4a picks Even's W-optimum in its arena
    against the FIXED τ (SPEC S4a; docs/si/N5-EXIT-box22.md §9 calls S4a "a globally optimal improvement inside an arena", arena by Ξ, choice
    by W). [F]'s Lemmas 6.8-6.12 and §8 are proved for I^loc / I^glo only; they say nothing about W-choices against a fixed τ.
  - (b) Odd's strategy. [F] has no player-1 improvement; N5 improves τ (S4b) and ends the phase when τ changes (R38 (a)). [F] does not
    address whether τ would move on H_n.
  - (c) Where the counting happens. The gadgets count through player 1's best response at e_i flipping as a cycle opens or closes ([F] §8.2).
    In N5 terms that is σ̄ changing at the gate e_i: exactly an ALT event. Inside one N5 phase τ(e_i) is fixed, so the W-play through e_i is
    fixed; σ̄'s flips reach S4a only through the arena Iσ (Ξ-improving edges). So a one-phase embedding of [F]'s mechanism needs the
    alternation to drive the count through the ARENA alone, with a one-player W-choice. Moreover, when a cycle (d_i, e_i) closes with
    τ(e_i) = d_i, the W-play from e_i ends in that cycle, so λ_W changes at e_i; with τ(e_i) = h_i the closing is invisible to W. So within one
    phase, bit events are either λ_W-changes or W-invisible. (READING from [F] §6.1's gadget and the definition of W; not checked on H_n.)
- ANSWER (READING): [F]'s family needs no change of λ_Ξ, and has no τ, so the paper does NOT force it to span many N5 phases; but it also
  does not show that N5 (S4a by W against τ, plus S4b) does anything exponential on it. Whether such a family fits in one N5 phase is OPEN
  and testable: [F] §8.4 gives H_n explicitly (sink x, modified deceleration lane of length 6n − 3, roots r, s, n modified cycle gates with
  stubborn cycles). Proposed DATA step (not done here): build H_n for n = 3..8 from §8.4 and run N5 (SPEC) on it, counting phases, τ changes,
  λ_W changes and ALT per phase.

## 3. Question (ii): where [HMZ] uses the discount, and whether N5's lexicographic order has an analogue
- The discount enters in exactly three places, all quantitative:
  - Lemma 3.10: the flux of any profile sums to x_π e = n/(1 − γ) (geometric series Σ_k γ^k).
  - Lemma 4.2: the value-iteration operator is a γ-contraction in ‖·‖∞; with Lemmas 5.3-5.4 (SI dominated by value iteration) this gives
    Lemma 5.5: ‖v_k − v*‖∞ ≤ γ^k ‖v_0 − v*‖∞ (geometric convergence of SI).
  - Lemma 6.2: ‖v_π″ − v_π‖₁ ≤ n/(1 − γ)·(c_π)_a with a the largest reduced cost (from Lemma 3.12 and 3.10); hence Lemma 6.3:
    ‖v_π′ − v*‖₁ ≥ (1 − γ)/n · ‖v_π″ − v*‖₁ when π′ still uses that action a.
  - The combinatorial core is Lemma 6.4: the action a of σ^k with the largest reduced cost w.r.t. the OPTIMAL profile never appears again
    after L = log_{1/γ}(n²/(1 − γ)) more iterations (Lemma 6.3's lower bound against Lemma 5.5's geometric upper bound). Theorem 6.5 then
    counts: at most m actions are eliminated, one every L iterations.
- What transfers to N5 (READING):
  - The skeleton of Theorem 6.5 is order-only: "every block of L iterations eliminates some action forever" ⇒ ≤ (m + 1)·L iterations. An
    N5 analogue would be a lemma "within L(n) transitions of a phase, some Even edge (or some σ̄-option at a gate) is left and never
    retaken in that phase", with L polynomial. E-ONEWAY / NO-UP (docs/si/N5-EXIT-box22.md §2, §8; conditional on OFFSET-MONO) are
    statements of the "not retaken" kind, but only INSIDE a window where the old exit and its class exit path stay fixed; they are not
    "forever", and nothing chooses WHICH action is eliminated within a bounded time.
  - Lemma 5.1-5.2's monotonicity is N5's (MON) / R15 already.
- What does not transfer:
  - Lemmas 3.10, 4.2, 5.5, 6.2-6.4 need a metric value with a contraction. N5's values are lexicographic (cycle node, signed path weight,
    length); the κ-weights are powers of 2, so "a (1 − γ)/n fraction of the gap" has no meaning, and there is no geometric convergence.
  - [F] Corollary 9.9 shows this is not a technicality: on 1-sink games VJ's lexicographic order IS a discounted order with γ part of the
    input (γ close to 1), and there SI with I^loc or I^glo is exponential (Theorems 6.14, 8.4). So any polynomial bound for N5 must use
    something [HMZ]'s argument does not have: N5-specific structure (the symmetric τ-improvement S4b, the W-choice of S4a, phases), not the
    order alone.
- ANSWER (READING): the discount is used in the flux bound (Lemma 3.10) and the contraction (Lemma 4.2 → 5.5), both feeding the
  elimination Lemma 6.4. N5's lexicographic order has no analogue of either; the γ → 1 limit is where [F] builds exponential runs. What could
  carry over is the counting skeleton (eliminate one action per polynomial block), which would need an UNCONDITIONAL "left forever within L
  steps" lemma for N5; E-ONEWAY / NO-UP are windowed versions of it and do not give the block length.

## 4. What this suggests (READING; not routed)
- The one experiment that settles (i) for this family: N5 on [F]'s H_n (§8.4), counting phases and ALT. If N5 needs one phase per counter
  increment (τ or λ_W changing at each), [F]'s mechanism does not live inside a phase; if a phase holds exponentially many ALT events, that
  is an N5 lower bound candidate for L-RED.
- For an upper bound, the HMZ skeleton points at the statement to look for: an unconditional elimination lemma inside a phase.
