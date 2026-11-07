# T63: dynamic BFS / lex-min path trees under insertions, potential proofs finer than the top coordinate, and FEEDBACK in the known lower bounds, against R97 SRC-COUNT, KEY-MON / INS and the A-potential
L-LIT successor T59-T63 (Opus 5.5), D18; un-parked by the Lead 2026-10-31 08:12Z for this one box. Written 2026-10-31 08:12Z-08:40Z
(date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME stays OPEN.
Inputs, as the Lead states them (not re-read beyond the brief):
- landed: RESULTS R96, R97 (SRC-COUNT |F| ≤ E^S + (E^S + 1)(n − 1 + m_C));
- lane: KEY-MON (lex keys monotone at fixed W; tie returns ≤ 1 + INS), k-SOURCE, and the A-potential A := Σ_v lcp(CS Ξ(v), CS W(v)).
Labels as in T59: PROVED (source) / PROVED (L-LIT, elementary) / READING / OPEN / NOT FOUND.

## Summary
- (a) Dynamic BFS.
  - The Even-Shiloach tree, and its incremental twin, bounds the work by LEVEL changes: each vertex's level is monotone and changes at
    most n times, O(mn) in total.
  - The parent inside a level is arbitrary in these structures. No opened source bounds how often a lexicographically minimal path
    (or lex-min parent) changes. NOT FOUND, after a short search.
  - Elementary transfer (PROVED, L-LIT): under insertions only, the lex-min BFS key of a vertex at a fixed level is a function of the
    current graph, so it changes at most once per insertion. Per vertex: ≤ (level changes ≤ n) + INS.
  - That is the lane's «tie returns ≤ 1 + INS» shape; the literature adds no amortisation beyond it. A single insertion can change the
    key of every descendant, so INS stays the quantity to bound.
- (b) Potentials finer than the top coordinate.
  - Ye, HMZ, Scherrer, Post-Ye and Zhong-Ye all use NUMERIC gaps, sums over all coordinates. They see every coordinate, not just the
    first difference.
  - In N5's canonical embedding these gaps are dominated by the top rank. T59 measured them on fx: BLOCK-RATIO 2^(2K), the gap falls by
    n² only at the last transition (WINC = |F|). DEAD as a route (T59).
  - The lcp potential A is blind below the first difference; the numeric gap is swamped by it. They fail in opposite directions.
  - The only scale-free ingredient that worked in the literature is Zhong-Ye's ratio argument (7.2)-(7.5): the step must capture a
    1/poly fraction of the REFERENCE's largest residual. T59 Lemma DZ-W states exactly what a finer potential would have to supply
    (BLOCK-RATIO); fx violates it.
- (c) FEEDBACK. In Friedmann's G_n the feedback is explicit: an Even switch closes cycle i, and Odd's best reply at e_i flips d_i → h_i
  (LMCS Lemma 6.1 p.10, «by moving to d_i, the player 1 node hides …»).
  - In N5, inside a W-run, the same arrow lands on σ̄ (τ is fixed), and through Ξ on Iσ: it opens or blocks Even edges. That is the
    Ξ-blocked-closure mechanism of R140 DECEL-RED.
  - Fearnley's MDPs have no player 2; the feedback is replaced by a probabilistic action (Prop. 4).
  - van Dijk-Loho-Maat's feedback is two-sided («distracted»).
  - Mei's exact best reply cancels a 2-cycle per pivot.
  - §3 gives each mechanism and what L-RED 37 must realise.

## 1. (a) Dynamic BFS / shortest-path trees under insertions
- Sources OPENED (scratchpad t63):
  - Henzinger-Krinninger-Nanongkai, arXiv 1308.0776 (663740ad…), §2 p.18-19.
    - The ES-tree: «introduced by Even and Shiloach … [ES81]».
    - The charging: «the contribution of a node v to the running time … is deg_Gi(v) times its level change».
    - Lemma 2.10 (King [Kin99]): an exact decremental SSSP structure up to depth R_d, with total update time
      O(φ_k(G) + t_SP + Σ_i Σ_v deg_Gi(v)(min(R_d, ℓ_i(v)) − min(R_d, ℓ_(i−1)(v)))).
  - Nanongkai, ADFOCS 2018 lecture slides «4 Deeper Discussions» (conferences.mpi-inf.mpg.de; 376ce8ed…), slide 42: «Theorem
    [Even-Shiloach JACM'81, Dinitz'71] A BFS tree can be maintained with O(mn) total time for m edge insertions»; slides 41-48 (every node
    keeps its level; a node sends deg(v) messages when its level decreases).
- NOT OPENED: Even-Shiloach JACM 28 (1981) and King FOCS 1999 themselves (cited through the two items above). No search hit for
  dynamic LEXICOGRAPHIC BFS or lex-min path trees. NOT FOUND (one search; not claimed absent from the literature).
- Hypotheses of the ES bound: unweighted (or integer-weighted) graph, ONE kind of update (insertions only, or deletions only), levels
  monotone, and the cost charged to level changes ≤ depth per vertex.
- Lemma LEXINS (PROVED, L-LIT, elementary).
  - Setting: a graph under edge insertions only, with BFS levels from a root and the key of a vertex := the lexicographically least
    level path. Between two insertions the key is constant, since it is a function of the graph.
  - Hence each vertex's key changes ≤ (number of insertions) times; together with level changes, ≤ n + INS. Keys only decrease while the
    level is fixed.
- Transfer to N5 (READING). Inside a W-constant interval, S1's EVEN branch is a plain BFS first-in tree of the reverse W-tight arena (T54
  LEX-BFS, T55). Arena changes are insertions and deletions, so the one-kind hypothesis of ES fails unless KEY-MON's insertions-only
  regime holds.
  - Where it holds, LEXINS is the lane's tie-return bound.
  - The quantity left open is INS, the insertions into the W-tight arena. ES charges levels, not insertions, and gives nothing for INS.
- One insertion can change the lex key of all its descendants (READING; standard). So no per-insertion amortisation below Θ(n) is
  possible without structure.

## 2. (b) Potentials finer than the value's top coordinate
- Opened in T58 / T59 (sha256 in notes): Ye MOR 2011 Lemma 4.1-4.2, Thm 4.1; HMZ 1008.0530 Lemma 5.3-5.5, 6.1-6.4; Scherrer 1306.0386
  Lemma 8, 13, Thm 3-4; Post-Ye 1208.5083 Lemma 3.1-3.6; Zhong-Ye 2609.40147 Thm 7.1, (7.2)-(7.6).
| source | potential | what it sees | hypothesis that makes it decrease geometrically | N5 (T58 / T59) |
| --- | --- | --- | --- | --- |
| Ye Lemma 4.1 | c^T x^π − z* (primal gap) | all coordinates, weighted by flux ∈ [1, m/(1−γ)] | Dantzig / Howard rule + discount γ | no γ; Ξ ordinal |
| HMZ Lemma 5.5, 6.4 | ‖v^k − v*‖ | all coordinates | SI step ≥ one Bellman step (Lemma 5.3) + γ | C-DISC (T59 §4.1) needs GREEDY-IN; fails at blocked edges |
| Post-Ye Lemma 3.2, 3.5; Zhong-Ye (7.4) | Σ_s (V^{πT}(s) − V^{πt}(s)), undiscounted | all coordinates, path flux < N | the step captures the LARGEST residual (Dantzig), factor 1 − 1/N² | DZ-W (T59 §4.2): needs BLOCK-RATIO_K; fx: K = 2^(2K), WINC = \|F\| |
| Scherrer Lemma 8 | none (combinatorial) | new cycle within n | deterministic Howard | = R17-type (one player) |
| lane A-potential (Lead brief) | Σ_v lcp(CS Ξ, CS W) | first differing coordinate only | – | blind below the first difference (lane) |
- READING. The numeric gaps are not blind, but in the 2^rank embedding the top coordinate's weight dominates them. That is why they
  fail on fx (T59 §4.3).
- So a finer potential must weigh coordinates WITHOUT the 2^rank scale (ordinal, like A) and still see below the first difference.
- No opened source has such a potential for an arena-optimum rule. The literature's polynomial potentials are scale-free only through
  the ratio «step ≥ 1/poly of the largest reference residual». T59's BLOCK-RATIO is its exact N5 form, and it is false on fx.

## 3. (c) FEEDBACK from a player-1 switch into player 2's best reply
| construction (opened) | the switch | the feedback | its role in the counter | inside one N5 W-run |
| --- | --- | --- | --- | --- |
| Friedmann G_n (LMCS 1106.0778 Lemma 6.1 p.10; §6.1) | Even closes simple cycle i (σ(d_i) = e_i) | Odd's best reply at e_i flips d_i → h_i. While open, «by moving to d_i, the player 1 node hides the fact that there is a highly profitable node on the other side» | the bit's profit appears only through Odd's forced exit; the lane delays it | τ fixed, so the flip is of σ̄. It changes Ξ, hence Iσ: a closure is hidden from S2 (blocked) until σ̄ flips. R140: S4a's arena optimum still closes every W-better cycle in the arena at once, so the delay must come from Ξ-blocking |
| Friedmann H_n (§8.2 pp.28-29) | two of three stubborn-cycle edges leave, one enters | as above, with one cycle edge always non-improving | the closure is never inside the arena (Ξ-blocked) | the exact DECEL-RED shape (T59 §3.2); N5 stops it (HW ≤ 3 on switchbestexp N = 4-8, T59) |
| Fearnley MDP (1003.3418 Prop. 2, 4 p.6) | b_i switches to a_i | no player 2; the probabilistic a_i has appeal < Val(b_i) + 1 while unchosen, but Val(g_i) once chosen | hidden profit without an opponent | not a two-player feedback; ruled out by an arena optimum (T59) |
| van Dijk-Loho-Maat (2309.02223 p.3, pp.11-12) | either player | both are «distracted by the other player's strategy»; the counterstrategy to a bad strategy is bad | recursion G_(j−1) solved twice | symmetric-SI specific; N5 runs these in 1-13 iterations (T37) |
| Mei (2610.27386; T31) | a Dantzig single switch | the exact best reply cancels a 2-cycle per pivot | one joint λ-phase counter | T31; single-switch rule, not S4a |
- What L-RED 37 must realise (READING; the shape only, no construction).
  - An Even selector switch inside the W-run makes an Odd vertex deviate (σ̄ ≠ τ) or re-target. That changes Ξ at a head, which moves a
    W-better Even edge OUT of Iσ (re-blocks it) or INTO Iσ (releases it), in counter order.
  - Each release must be a Ξ-blocked late adoption: R140 DECEL-RED, R*_F ≥ 2^N/(n − 1) for an exponential counter.
  - Friedmann's G_n has the arrow (switch → best-reply flip → hidden or unhidden profit) but needs a non-optimising Even rule. H_n has the
    blocked closures but loses to N5 (DATA).
  - None of the opened constructions is a one-W-run feedback counter under an arena-optimum rule against a FIXED τ. NOT FOUND in the
    literature; it is the open construction.

## DONE / FINDINGS / NEEDS
- DONE: this note; notes/L-LIT.md (sources, resume point; parked).
- FINDINGS:
  1. (a) ES / incremental BFS bound only level changes (≤ n per vertex, O(mn) total; HKN 1308.0776 Lemma 2.10 p.19; Nanongkai ADFOCS'18
     slide 42). No opened source counts lex-min path changes (NOT FOUND). PROVED (elementary) LEXINS: key changes per vertex ≤ n + INS
     under insertions only. INS stays open.
  2. (b) Every opened strongly polynomial potential is a numeric gap over all coordinates. In N5's 2^rank embedding it is dominated by
     the top rank (T59 DEAD on fx). The lcp potential is the opposite (blind below). The literature's only scale-free device is the ratio
     condition, false on fx (T59 BLOCK-RATIO).
  3. (c) FEEDBACK = Friedmann LMCS Lemma 6.1: an Even closure flips Odd's best reply and unhides profit. In a W-run it acts on σ̄ → Ξ →
     Iσ (blocked closures, DECEL-RED). H_n realises blocked closures but N5 stops it. No one-W-run feedback counter exists in the
     literature.
- NEEDS: none from the owner (optional: Even-Shiloach JACM 1981, King FOCS 1999 originals).
