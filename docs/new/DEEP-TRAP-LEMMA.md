# Deep-trap lemma: statement and proof sketch (L-NEW box 3, 2026-10-18; UNREFEREED; for REFEREE-2 with the N1 kill)

Purpose: make the N1 kill (docs/new/N1-KILL.md) and the discount-homotopy obstruction (docs/new/N3-blackwell-path.md, last
section) checkable on paper. Sources (opened by L-NEW, notes/L-NEW.md "Sources opened"): Friedmann, arXiv 1106.0778 (LMCS 7(3:19))
§9: rewards r(v) = (−|V|)^Ω(v), β_G = 1 − 1/(4|V| max|r|), Thm 9.5 (Vöge: for γ ≥ β_G every parity improving switch is a
discounted improving switch), Lemma 9.6 (1-sink games). Loff-Skomra arXiv 2610.22149 Fig. 7.2 (IncreasingDiscountPI), Thm 7.9.
Hansen-Miltersen-Zwick arXiv 1008.0530 Thm 6.5.

## Setting
G = (V, E, Ω) a parity game, |V| = n, priorities ≤ B (B even). E2 = Even vertices with ≥ 2 successors. The deep-trap game
G' adds for every v ∈ E2 two Odd vertices t_v, c_v and edges v → t_v → c_v → c_v, Ω(t_v) = P = B + 2 + 2k (even),
Ω(c_v) = q = B + 1 (odd). n' = |V(G')| ≤ 3n. Rewards r(u) = (−n')^Ω(u) (N1's choice: base = number of vertices).
Discount γ = 1 − 1/H. Values x(u) = discounted payoff of the pair's play from u (anneal.cpp computes these exactly).

## Lemma (DEEP-TRAP)
Let D := P − q = 2k + 1.
(a) Winners: G' and G have the same winner on every vertex of V; t_v, c_v are won by Odd. (A play that enters a trap stays on
    c_v forever, top priority q odd; Even's other options are those of G.)
(b) Holding phase: if H ≤ n'^D / 4, then in the discounted optimum of G' every v ∈ E2 plays t_v, and x(v) > 0 for every v ∈ E2.
(c) Release phase: if H ≥ 4·n'^D, then no v ∈ E2 plays t_v in the discounted optimum, and every Even switch in Howard's run on
    G' at γ is an Even switch on G (trap edges are never improving).
(d) Parity-like after release: if moreover D ≥ B + 3 (k ≥ B/2 + 1), then every γ with H ≥ n'^D satisfies γ ≥ β_G for G with
    rewards (−n')^Ω, so (Vöge, 1106.0778 Thm 9.5) Howard's improving switches on G at γ are the parity (VJ) improving switches.
(e) Consequence for N1: N1's phases with H_j ≤ n'^D/4 make no Even switch after the first phase (Even stays in the traps; the
    certificate cannot fire: Even's values are positive while Odd wins every vertex of V in switchallexp). The first phase j* with
    H_j ≥ 4 n'^D (at most 4 phases after the holding range, since H doubles) starts from σ = all traps and runs Howard to the
    discounted optimum on G at a parity-like discount: the VJ switch-all sequence on G from σ_1 := Howard's first step from all
    traps, up to the at most 3 phases inside the window n'^D/4 < H_j < 4 n'^D.

## Proof sketch (gaps listed below)
(b) x(c_v) = r(c_v)·H = −n'^q H; x(t_v) = n'^P − γ n'^q H ≥ n'^P − n'^q H ≥ (3/4) n'^P when H ≤ n'^D/4. Any play of G' that
    does not enter a trap collects |reward| ≤ n'^B per step, so its value is ≤ n'^B·H ≤ n'^(B+D)/4 < n'^P/4 (since P = q + D = B + 1 + D > B + D). A real option of v leads either to a play avoiding traps (value < n'^P/4) or, through
    other Even vertices, into a trap after ≥ 1 step: value ≤ n'^B·(steps) + γ^steps·x(t_w) < x(t_v) unless it gains more than
    the discount loss, which is impossible since all trap values are equal and γ < 1 (the trap at v is reached with zero delay).
    [Gap 1: write the inequality chain with γ^s ≤ γ for s ≥ 1 and n'^B·s·... explicitly.] Positivity: x(v) = r(v) + γ x(t_v) > 0.
(c) For H ≥ 4 n'^D: x(t_v) = n'^P − γ n'^q H ≤ n'^P − (1/2) n'^q·4 n'^D = −n'^P (for γ ≥ 1/2). Every real option has
    value ≥ −n'^B·H·(1 + o(1)) − (traps entered later, ≥ x(t_w))... [Gap 2: a real option can also lead into another trap; then
    its value is ≥ γ^s x(t_w) > x(t_v) because x(t_w) = x(t_v) < 0 and γ^s < 1. For options avoiding traps the bound
    −n'^B H > −n'^P needs H < n'^(P−B) = n'^(D+1): so (c) as stated holds for 4n'^D ≤ H < n'^(D+1); for larger H use
    x(t_v) ≤ −n'^q H/2 < −n'^B H.] Hence trap edges are never improving and never optimal once released.
(d) β_G for G with base n' (≥ n): 1 − β_G = 1/(4 n'·n'^B) is reached at H = 4 n'^(B+1) ≤ n'^D when D ≥ B + 3 and n' ≥ 4.
    Thm 9.5 is stated for base |V(G)|; base n' > |V(G)| only increases the separation between priorities. [Gap 3: check that
    1106.0778 §9's proof uses only base ≥ |V|.]
(e) Follows from (b)-(d) and the schedule H_j = 2^j. [Gap 4: the window phases n'^D/4 < H_j < 4n'^D may already switch some
    traps; data: none (nonzero lists a single phase).]

## What the lemma does NOT prove (stated as DATA)
The length of the VJ switch-all run on switchallexp from σ_1 (the first Howard step from all traps). Measured (pinned instances,
N = 1..7): N1 makes 11, 31, 71, 151, 311, 631, 1244 Even switches in that one phase; plain VJ switch-all from all traps on the same
games: 13, 33, 73 (N = 1..3), i.e. Friedmann's count + 3 (box 1: 33, 73, 153, 313, 633, 1246 on alltrap). A proof needs:
σ_1 is a strategy from which Friedmann's switch-all lower bound applies (his σ_0, or a state of his counter at value ≤ c).
[Gap 5: identify σ_1 with Friedmann's initial strategy on switchallexp, using 1106.0778's description of σ_0. Evidence: box 1
measured that plain VJ from all traps equals VJ from PGSolver's best-reward start (alltrap.py docstring: "best-reward start = all
traps"), and the M1 bench (experiments/hard-families/switchallexp) confirms Friedmann's doubling from that start.]

## Generalisation used in the N3 obstruction
Nothing above uses N1's schedule except "H doubles": any method that follows the discounted optimum in γ meets, at the release
(between n'^D/4 and 4n'^D), a change from "all traps" to the parity-like optimum of G, all trap edges changing sign together.
n3grid.cpp confirms one change of the optimal pair along the whole grid (N = 1..5).
