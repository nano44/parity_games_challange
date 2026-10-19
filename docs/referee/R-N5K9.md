# Referee report R-N5K9: K9, N5's iteration count bounded by best-reply changes (given (P))

Referee: REFEREE (successor 2), running on Opus 5.5 under owner ruling D12 (Lead reading L33). Packet P-N5K9: the Lead's message of
00:20Z (2026-10-19). Pin: trunk e73b214, docs/new/N5-K9-reading.md (identical at my merge of trunk). Context read:
docs/lit/T22-VJ00-prop74.md (L-LIT), docs/RESULTS.md R15. Written 00:21Z-00:24Z (date -u). docs/referee-2/ was not read.
Source opened by me: VJ00 BRICS RS-00-48 (sha256 485a12de432a2a8c…, the file of R-N5T), §7, printed pp. 25-28. Every quote of
§7 below is from that file.

## Verdict
| item | verdict (Opus 5.5, D12) |
|---|---|
| (1) Derivation of K ≤ (C n³ + 1)(2 + ch_O + ch_E) from (P), (T1), (T2), R15 and the definitions | SIGNED, CONDITIONAL ON (P), WITH GAPS: K9-G1 (code link: the computed σ̄ must be an optimal counter-strategy; DATA, 0 failures), K9-G2 ("O(n³)" → "≤ C n³ for all n": enlarge C; closed), K9-G3 (wording of (P): the policy must be allowed to depend on information outside H; closed by reading "every sequence") |
| (2) (P) stated exactly | below, (P*). Player: the improver ⊕ in a game where every ⊖ vertex has out-degree 1. Policies: ALL, including adaptive ones. Start: any. Steps counted: every strategy change, flat steps INCLUDED (or see (3b)) |
| (3a) Is switch-all only enough? | NO. N5's S4a/S4b moves are not switch-all moves of the one-player game G_c, and their subsets depend on τ, which is outside G_c |
| (3b) Another weaker premise | YES, along the other axis. Counting only Ω-strict steps is enough: (P_strict) gives K ≤ ((C n³ + 1)(2n(n−1) + 1) + 1)(2 + ch_O + ch_E), by R15's φ |
| (4) §6 checks 1-3 | 1 CONFIRMED (math; plus DATA for the computed σ̄); 2 CONFIRMED; 3 NO: (P) as stated (every policy) is not what VJ00 Prop. 7.4 asserts on any reading the text forces; I agree with T22 |
| Overall | SIGNED (conditional on (P*), with gaps K9-G1..G3) (Opus 5.5, D12). K9 is a correct REDUCTION. (P*) itself has no source: T22 STATED ONLY, and the any-policy form is stated nowhere. So K9 gives no bound today |

## (1) The derivation, line by line
Facts used: (T1) and (T2) (R15 (d)); VJ00 (11) Ωσ = Θ_{σσ̄}; the definitions of Ω (§4.3), improvement (§4.4 (2)), Switch_I.
Step 1 (one segment). Let [a, b] be an interval and c an Odd strategy with Θ_{σ_k c} = Ω^G_{σ_k} for every k ∈ [a, b].
- In G_c (each Odd vertex u keeps only (u, c(u))), every ⊕-strategy ρ has exactly one consistent play from each vertex. So the
  min over plays (§4.3) is that play: Ω^{G_c}_ρ = Θ_{ρc}. ✓
- Hence Ω^{G_c}_{σ_k} = Ω^G_{σ_k} for k ∈ [a, b]. ✓ G_c keeps the vertex set, the relevance order and the parities, so the order
  ⊴ is the same.
- Improvements (§4.4 (2)) are defined from the valuation and from ⊕'s edges, and ⊕'s edges are the same in G and G_c. So σ_k has
  the same improvements in both. Only the inclusion "improvement in G ⇒ improvement in G_c" is needed. ✓
- (T1): σ_{k+1} = σ_k, or σ_{k+1} = Switch_I(σ_k) with ∅ ≠ I an unambiguous set of improvements of σ_k (in G, hence in G_c),
  for k, k+1 ∈ [a, b]. With the repetitions deleted, σ_a, …, σ_b is an improvement sequence of the one-player game G_c. By (P),
  #{k ∈ [a, b−1] : σ_{k+1} ≠ σ_k} ≤ C n³. ✓
- Existence of c on a constant-σ̄ interval: c = σ̄_a = σ̄_k for all k ∈ [a, b], and Θ_{σ_k σ̄_k} = Ω_{σ_k} by (11). ✓ This uses
  (11) for the COMPUTED σ̄. That is §6 check 1, below.
Step 2 (segments). The cut points are the k < K with σ̄_{k+1} ≠ σ̄_k on Odd's vertices; there are ch_O of them.
- They split {0, …, K} into exactly 1 + ch_O maximal intervals of constant σ̄. ✓
- An Even move k → k+1 either lies inside one interval (both ends in it), counted by Step 1, or has k a cut point (≤ ch_O). ✓
- So #Even moves ≤ C n³ (1 + ch_O) + ch_O ≤ (C n³ + 1)(1 + ch_O). ✓
Step 3 (Odd). The same on G^d, with τ, τ̄ and G^d_{c′} (dual-⊖ = Even vertices fixed to c′). (11) holds on G^d, which is a
parity game. ✓ #Odd moves ≤ (C n³ + 1)(1 + ch_E).
Step 4. (T2): every iteration is an Even move or an Odd move (or both), so K ≤ #Even + #Odd. ✓ Summing gives the statement.
"Every tie-break / any simultaneous scheme" (§2): only (T1) and (T2) are used. ✓ This holds as long as each player's move is
Switch_I of its own improvements and every iteration moves a side.
Strategy-level check (this lane's trap): in Step 1 the player who moves is Even, in G_c, and the component that matters is the
whole valuation Ω^{G_c} = Ω^G on the segment. The cut is on Odd's computed reply σ̄, not on τ. τ may change freely inside a
segment: it changes which subset Even switches, not which valuation Even's improvements are read from. ✓
K9-G1 (code link; DATA). ch_O is defined from the computed σ̄ (si.py Engine.evaluate). Step 1 needs Θ_{σ_k σ̄_k} = Ω_{σ_k}, i.e.
that si.py's σ̄ is a VJ00-optimal counter-strategy. VJ00's (11) is proved for its own σ̄ (§5.2: a pointwise Ω-minimiser), and
si.py's choice at a cycle node comes from a DFS (SPEC FIX 2), not from a minimiser. Mathematically K9 holds with ch_O counted
over ANY sequence of optimal counter-strategies. For the code's ch_O, my check (docs/referee/scratch/n5k9_sbar.py; G and G^d as
n5.py's dual(); 400 random games, n ≤ 6, every σ: 4,465 strategies, 21,373 vertex plays) found Θ_{σ, σ̄_si} = Ω_σ in every case:
0 failures. DATA, not proof.
K9-G2 (closed). VJ00's "O(n³)" gives C n³ only for n ≥ n₀. For n < n₀, chains are finite (R15 (c)), so enlarging C covers them.
The reading should state (P) as "≤ C n³ for all n ≥ 1".
K9-G3 (closed). Inside a segment, N5's subsets depend on τ_k and on the iteration history, which are outside G_c. So (P) must
bound EVERY sequence, including adaptively chosen ones, not only the runs of a fixed rule on G_c. (P)'s "every sequence
ρ_0, …, ρ_L with ρ_{j+1} = Switch_{I_j}(ρ_j)" says exactly that. The reading should say it, because "policy" in VJ00 (§4.4)
denotes a sequence too, but readers take "policy" as a rule.

## (2) (P) exactly as K9 needs it
(P*) There is C such that for every n ≥ 1, every parity game H on n vertices in which every vertex of the NON-improving player ⊖
has out-degree 1, and every finite sequence ρ_0, ρ_1, …, ρ_L of strategies of the improving player ⊕ with ρ_{j+1} =
Switch_{I_j}(ρ_j), where I_j is ANY non-empty unambiguous set of improvements of ρ_j in H (VJ00 §4.4 (2)), we have L ≤ C n³.
- Player: ⊕, the improver; ⊖ has no choices. This agrees with T22 (i). It is needed for Even on G_c and for Odd on G^d_{c′}.
- Policies: all, adaptive included (K9-G3). Start: any strategy (segments start wherever σ̄ changes).
- Flat steps: INCLUDED. N5's moves can be flat (R15 (b)). REFEREE-2's I1 instance (prio [0,2,4], R15 side finding) is itself a
  one-player ⊕ game with a flat improvement. So a bound that counts only Ω-strict steps does not give (P*) directly. It does give
  K9 with an extra factor, by (3b).

## (3) Would a weaker premise suffice?
(3a) Switch-all only: NO. The reason:
- Inside a segment, Even's moves come from S4a (σ_new = Even's optimum in the arena restricted to {σ(v)} ∪ Iσ(v), against τ_k).
  The switched subset is the set of vertices where that τ_k-dependent optimum leaves σ. In general it is a proper subset of the
  switchable vertices, and its targets need not be the "best" improvements. Only the fallback S4c is a switch-all step.
- τ_k changes inside a segment (Odd moves do not change σ̄). So from G_c's point of view, the subsets form an adaptive selection
  with no fixed rule.
- A theorem about switch-all runs on G_c therefore bounds none of N5's S4a moves. Step 1 needs the bound for the sequence N5
  actually produces, which is (P*). Under the switch-all reading of T22, K9 bounds only the fallback steps, which is nothing
  useful.
- No source gives an any-subset bound (T22 (ii)). VJ00 itself keeps the general any-policy question open (Problem 7.3, p. 27:
  "Are there families of examples of parity games for which there exist strategy improvement policies of super-polynomial
  length?"; for general, not one-player, games).
(3b) Weaker along the flat axis: YES. Let (P_strict) be (P*) with L replaced by the number of j with Ω_{ρ_{j+1}} ≠ Ω_{ρ_j}.
- On a segment, Ω^{G_c} = Ω^G, so "flat" means the same thing in G_c and in G. By R15 (c), every flat step raises φ (computed in
  G_c) by ≥ 1, and |φ| ≤ n(n−1). So any run of consecutive flat steps has length ≤ 2n(n−1).
- A segment with s ≤ C n³ strict steps has at most s + 1 flat runs. So its moves number ≤ s + (s + 1)·2n(n−1) ≤
  (C n³ + 1)(2n(n−1) + 1).
- Then Step 2 gives K ≤ ((C n³ + 1)(2n(n−1) + 1) + 1)(2 + ch_O + ch_E): still polynomial in n times the reply changes.
- This removes T22's burden (iii) (counting T21's flat steps) from the premise. It does not touch the policy axis.

## (4) The reading's §6 checks
1. "Ω^{G_c}_{σ_k} = Ω^G_{σ_k} whenever c is an optimal counter-strategy to σ_k; needs Θ_{σc} = Ω_σ for SOME optimal c".
   CONFIRMED as mathematics (Step 1 above): any c with Θ_{σ_k c} = Ω_{σ_k} for all k in the segment works, computed or not. For
   the code's ch_O the computed σ̄ must be optimal: K9-G1, DATA 0/21,373.
2. Cut count: CONFIRMED. There are 1 + ch_O intervals, ≤ ch_O boundary moves, and #Even ≤ (C n³ + 1)(1 + ch_O).
3. Is (P) what VJ00 Prop. 7.4 asserts? NO, not on any reading the text forces. I read §7 myself:
   - Prop. 7.4 (p. 27): "The discrete strategy improvement algorithm terminates after O(n3) strategy improvement steps for
     one-player parity games." There is no proof.
   - The sentence before it contrasts "the standard policy, i.e., switching all switchable vertices in every strategy
     improvement step" for one-player stochastic games with "our discrete strategy improvement algorithm".
   - Where VJ00 means all policies, it says so: Prop. 7.6, "for which all policies have length O((n/d)^d)". Prop. 7.1 and
     Problem 7.3 speak of "a policy" or "policies" explicitly.
   - Problem 7.7 asks whether the switch-all ("maximal set of improvements") policy is polynomial in general.
   - So "every policy" is one possible reading of "the algorithm" (whose Improve is non-deterministic, §4.4), not a forced one.
     I agree with T22 (ii): the any-subset statement (P*) is stated nowhere; the sources support at most switch-all.
   - "One player" = ⊕ the improver: agree with T22 (b). With ⊖ the only chooser, the algorithm makes zero steps.
   - Also from §7 (p. 27-28): "Note that in every strategy improvement step the current valuation Ωσ strictly improves" is false
     (R15 side finding). So any proof of 7.4 that counts steps through strict improvement has to be repaired for flat steps.
     (3b) shows K9 can absorb that cost.

## DATA (not part of the signature)
- n5k9_sbar.py: K9-G1, above.
- n5k9_longest.py (VJ00-only oracle; one-player games, ⊖ out-degree 1; longest chain over ALL subsets and ALL starts, a longest
  path in the acyclic strategy graph; 60 random games per n):
  | n | 4 | 5 | 6 | 7 |
  |---|---|---|---|---|
  | longest chain | 8 | 14 | 23 | 17 |
  | strict steps | 8 | 13 | 22 | 16 |
  This is of the same order as L-NEW's numbers (5, 9, 9, 16, 21, 14 at n = 4..9). Small n cannot separate n³ from exponential,
  and random games are not adversarial.
- I did not re-run L-NEW's brchanges/k9_sanity tables (§4). They are DATA and not used in the proof.

## Gaps (for GAPS.md)
- K9-G1 (DATA): the computed σ̄ is optimal (Θ_{σσ̄} = Ω_σ). 0 failures in 21,373 vertex plays, G and G^d.
- K9-G2 (closed): "≤ C n³ for all n", by enlarging C.
- K9-G3 (closed): (P) must allow adaptive subset sequences. State it.
- Premise (P*) (OPEN, no source): the any-subset, flat-steps-included one-player bound. (P_strict) suffices instead, with an extra
  O(n²) factor. Switch-all does NOT suffice.
- Not given: any bound on ch_O + ch_E along N5's runs. Gauntlet step 4 for N5 stays open.
