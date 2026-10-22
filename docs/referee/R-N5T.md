# Referee report R-N5T: termination of N5 SSI-GLOBAL (G-N5-TERM reading)

Referee: REFEREE (successor 2), running on Opus 5.5 under owner ruling D12 (Lead reading L33). Packet P-N5T: the Lead's GO of
22:58Z. Pin: trunk 812ecba, docs/new/G-N5-TERM-reading.md (84 lines; unchanged at trunk c2b1848). Spec: docs/new/N5-ssi-global.md
"Exact pseudocode", SPEC S1-S5, FIX 1-4, Q1-Q4 at 812ecba. Code read: experiments/new/n5.py and experiments/si/si.py at 812ecba.
Written 23:00Z-23:05Z (date -u). docs/referee-2/R2-N5T.md was not read.

Source opened by me: Vöge & Jurdziński, "A Discrete Strategy Improvement Algorithm for Solving Parity Games", BRICS RS-00-48
(Dec 2000), https://www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf, sha256 485a12de432a2a8c88640b0718bd2042d855fa86d6a82092a0d538fd41ba9e65
(the same file L-NEW used). Every lemma, proposition and equation number below was read in that file (§4.1-§6).

## Verdict
| item | verdict (Opus 5.5, D12) |
|---|---|
| §0 instance and the VJ00 Lemma 5.8 observation | CONFIRMED. The instance holds by hand and in my own probe. The gap is in the "2 ⇒ 3" proof, and it also breaks VJ00's postulate I2 and its termination argument P1. The reading does not use the broken direction anywhere (see A0) |
| Lemma A (any non-empty unambiguous subset I of improvements: Ωσ ⊴ Ω_{Switch_I(σ)}) | SIGN. It is VJ00 Lemma 5.7 verbatim: VJ00's Improve operator already allows any non-empty set of improvements (§4.4) |
| Lemma B (flat switch ⇒ length-only switch at a cycle node) | SIGN WITH GAPS: G-B1 (the "=_ℓ" on pairs includes the length; VJ00 defines =_ℓ on sets only; closed below), G-B2 (wording; closed) |
| Theorem (σ ↦ Switch_I(σ) strictly rises in ≺ = (Ω, then φ)) | SIGN |
| Application to N5: both players' steps in one iteration, and the fallback | SIGN WITH GAPS: G-N1 (scope: the theorem applies to n5.py to the extent that si.py computes VJ00's Ωσ; DATA only, my cross-check 0 mismatches), G-N2 (S4a/S4b need the engine to return a choice in A(v) at every vertex; read in code; closed) |
| Side claim: at most O(n²) consecutive flat iterations | SIGN (|φ| ≤ n(n−1)) |
| Overall: N5 (SPEC S1-S5) terminates; G-N5-TERM's termination half | SIGNED WITH GAPS (Opus 5.5, D12). Every gap above is a wording or citation gap, closed in this report. G-N1 is a condition on the code, not on the mathematics |

Not covered (stated plainly): no polynomial or other iteration bound. h(≺) can be exponential. G-N5-TERM's running-time half
stays open, and so does gauntlet step 4 for N5.

## A0. VJ00 checked against the reading's citations
- §4.1 (play values, π, #, (1) PlayValues ⊆ {(v, (B, k)) : B ⊆ V>v}): as the reading uses them. #(P) = |Prefix(P)| = the number
  of steps to the loop value. This is SPEC S1's ℓ.
- §4.2 (Reward, MaxDiff, ≺ on sets, ⊴_ℓ with lengths: ℓ ∈ R− ⇒ k ≤ k′, ℓ ∈ R+ ⇒ k′ ≤ k; ⊴ linear on PlayValues): matches SPEC
  S1 and Q1, with ⊕ = Even, R+ = even p′. si.py key (rew, weight(path), ±ln) is the same order on play values: the weight
  comparison is valid because path ⊆ V>loop (Q1).
- §4.3: ⊴ on Valuations is pointwise; it is a partial order because ⊴ is linear on PlayValues. Ωσ(v) = min_⊴ over σ-plays.
- §4.4: unambiguous I, Switch_I, improvement (2) Ωσ(σ(v)) ◁ Ωσ(w); Improve(σ) = Switch_I(σ) for SOME non-empty set I of
  improvements. So Lemma 5.7 is stated for every non-empty unambiguous subset, not only for a best edge per vertex.
- §4.5: multiset ⊴_ℓ, MaxDiff over \_M, the weak order ⊴̃_ℓ, and ⊕: (B, k) ⊕ v = (B ∪_M {v}, k + 1). As the reading quotes them.
- §5.1 (3), (4), (6)-(10); Prop. 5.1; Lemma 5.2 and (11) Ωσ = Θ_{σσ̄}; Prop. 5.3, 5.4; Lemma 5.5; Lemma 5.7: as cited.
- Prop. 6.1 (§6, the shortest-path procedure: clause 4, "there is no cycle in G(r) containing s"): the reading does not cite it.
  SPEC Q3 cites it for the engine's restricted-graph acyclicity. That concerns only the implementation (G-N1).
- Lemma 5.8, the direction "Improve(σ) ≠ σ ⇒ σ is not a maximum". VJ00 proves it via 2 ⇒ 3: "for some v, the predicate Prog does
  not hold for Ωσ along (v, Improve(σ)(v))". At a cycle node v, Prog's clause 3 compares Π(v) ≅̃_v Π(w) ⊕ v, which ignores
  lengths, so a length-only improvement keeps Prog true. CONFIRMED on the §0 instance (below).
  The same step carries VJ00's I1 and I2 (§5.6: "Immediate from Lemma 5.8") and hence P1's termination claim. The first
  sentence of P2 ("σ maximum ⇒ Improve(σ) = σ") is the broken direction too.
  Does the reading use the broken direction anywhere? NO. Lemma A uses Prop. 5.3, Prop. 5.4 clause 2 and Lemma 5.5. Lemma B uses
  Prop. 5.1, the easy direction of Lemma 5.2 (Θ_{στ} is locally progressive), (11) and (1). The Theorem uses only §4.3. (11)
  rests on Prop. 5.1 and Lemma 5.2, not on 5.8.
  N5's output (S5) uses only "Iσ = ∅ ⇒ Ωσ is locally over-progressive for σ̄ ⇒ (12)". That is VJ00's text under the label
  "1 ⇒ 2"; I read it and it is sound (Prog ⇒ OverProg along σ̄-edges; Prop. 5.10 clause 2 along Even's edges). Correctness of
  the output is not part of this packet; I record only that it does not depend on the broken direction either.
- Prop. 5.4 clause 2 has no proof in VJ00 ("simple facts"). I checked it, since Lemma A depends on it. Λ(v) ≼ Λ(w) ≼ Λ(u). If
  Λ(v) = Λ(u) = ℓ, then Λ(w) = ℓ. Then Π(v) ⊴_ℓ Π(w) ⊕ v, Π(w) ⊴_ℓ Π(u), and ⊕ v is monotone for ⊴_ℓ (same element added on both
  sides, same +1), so Π(v) ⊴_ℓ Π(u) ⊕ v. The clause-3 case is the same with ⊴̃_ℓ, which is coarser. ✓

## §0 instance (by hand, then by probe)
Dual game (⊕ = original Odd; dual priorities 3, 7, 1, 2). Relevance by (priority, index): 2 < 3 < 0 < 1. R+ = {3}, R− = {0, 1, 2}.
⊕ owns only vertex 1 (successors 1, 3).
- τ(1) = 1. Vertex 1 is the most relevant vertex and lies in R−, so Ω(1) = (1, ∅, 0). From 3, ⊖ can reach loop 1 (rank 3,
  R−) or loop 0 (from 0 and 2 only the cycles in {0, 2} are reachable, maximum 0). ⊖ prefers 1 (the lower Reward), so
  Ω(3) = (1, ∅, 1). Ω(0) = (0, ∅, 0) and Ω(2) = (0, ∅, 1).
- (1, 3) is an improvement: same loop 1 ∈ R−, same B = ∅, and 0 < 1, so the longer path is better for ⊕.
- After the switch, the play 1 → 3 → 1 has loop value 1 at position 1: Ω(1) = (1, ∅, 0), and Ω is unchanged everywhere. τ′ has no
  improvement. So τ is a maximum element (both strategies have the same Ω) and Improve(τ) ≠ τ.
- φ goes 0 → 1: only vertex 1 counts (ε = +1, k(τ(1)) goes from k(1) = 0 to k(3) = 1).
Probe output (docs/referee/scratch/n5t_probe.py, VJ00 labels = ranks; original 1 ↦ 3, original 3 ↦ 1): Omega is equal before and
after; improvements {3: [1]} before and {} after; phi 0 -> 1.

## Lemma A
Line by line against VJ00 §5.4:
- Prop. 5.3: Ωσ is locally under-progressive for σ.
- For (v, w) ∈ I: Ωσ(σ(v)) ◁ Ωσ(w). UnderProg(Ωσ, (v, σ(v))) holds by Prop. 5.3 (σ-edges are in Eσ). Prop. 5.4 clause 2 gives
  UnderProg(Ωσ, (v, w)).
- Every other edge of E_{σ⁺} (⊕ vertices outside I keep σ(v); ⊖ vertices keep all their edges) is in Eσ.
- So Ωσ is locally under-progressive for σ⁺, and Lemma 5.5 gives Ωσ ⊴ Ω_{σ⁺}.
The reading is right that 5.7 never uses a best edge. More: VJ00's Improve is already defined for any non-empty set of
improvements, so Lemma A is Lemma 5.7 as stated. SIGN.
DATA (my probe; every non-empty unambiguous subset of improvements of every ⊕-strategy): 0 violations in 83,472 switches.

## Lemma B
Setting: I is unambiguous and non-empty, σ⁺ = Switch_I(σ), and Ω_{σ⁺} = Ωσ =: (Λ, Π).
1. (11) gives Ω_{σ⁺} = Θ_{σ⁺σ̄⁺}. Θ_{στ} is locally progressive for (σ, τ) (Lemma 5.2, the "easy to verify" direction), so
   Prog(Ω, (v, w)) holds for (v, w) ∈ I ⊆ E_{σ⁺σ̄⁺}. ✓
2. Prop. 5.1: Prog(Ω, (v, σ(v))). ✓ (Both statements are about the same function Ω.)
3. Case Λ(v) = ℓ ≠ v. Clause 1 gives Λ(w) = Λ(σ(v)) = ℓ. Clause 2 gives Π(v) =_ℓ Π(w) ⊕ v and Π(v) =_ℓ Π(σ(v)) ⊕ v.
   G-B1 (closed). VJ00 defines =_ℓ only on sets (§4.2: B =_ℓ C iff B ⊴_ℓ C and C ⊴_ℓ B), and ≅̃_ℓ on pairs. On pairs, clause 2's
   =_ℓ must mean ⊴_ℓ in both directions, which forces EQUAL lengths. Otherwise clause 2 would coincide with ≅̃_ℓ, and VJ00's
   own Lemma 5.2 proof would fail: it concludes "Π(v_k) =_ℓ Π(v_k) ⊕ C ... impossible because |C| > 0", which uses the length.
   (6) is also exact on lengths (Π is a shortest-path weight). The reading's cancellation needs this reading of =_ℓ, and should
   say so. It is also directly true of Θ: along a play, Π(v) restricted to V>ℓ equals Π(succ) ⊕ v, and the length is +1.
   Cancellation, re-derived from §4.5:
   - Both sides restrict to V>ℓ first; v is added to both sides or to neither.
   - (B ∪_M {v}) \_M (C ∪_M {v}) = B \_M C, because the multiplicities are max(b + 1 − c − 1, 0) = max(b − c, 0). So MaxDiff,
     and hence ≺, ⊴_ℓ and =_ℓ on the set parts, are unchanged. When B = C, also B ∪_M {v} = C ∪_M {v}.
   - The lengths k + 1 = k′ + 1 give k = k′.
   So Π(w) =_ℓ Π(σ(v)) with equal lengths. Both are play-value path parts with B ⊆ V>ℓ ((1)), so =_ℓ is equality, and
   Ω(w) = Ω(σ(v)). That contradicts Ω(σ(v)) ◁ Ω(w). ✓
   G-B2 (wording, closed). "⊴-equivalent" in the reading is in fact equality here, by (1). Either way it contradicts strictness.
4. Case Λ(v) = v. Clause 1: Λ(w) = Λ(σ(v)) = v. Clause 3: Π(v) = (∅, 0) and (∅, 0) ≅̃_v Π(w) ⊕ v, i.e.
   ∅ =_v (B_w ∪_M {v}) ∩ V>v = B_w ∩ V>v (v ∉ V>v). On sets, mutual ≼ is equality, because exactly one of B ≺ C and C ≺ B holds
   when B ≠ C (MaxDiff lies in R+ or R−). So B_w ∩ V>v = ∅, and by (1) B_w ⊆ V>v, so B_w = ∅. The same holds for σ(v). ✓
5. Same Λ = v, same B = ∅: by §4.2 the comparison is by length alone. For v ∈ R−, Ω(σ(v)) ◁ Ω(w) iff k(σ(v)) < k(w). For v ∈ R+,
   iff k(w) < k(σ(v)). ✓
Focus point "multiset cancellation": correct, as re-derived in 3. SIGN WITH GAPS (G-B1, G-B2; both closed here).
DATA: in my probe, 3,855 of the switches were flat (Ω unchanged). Every switched vertex met all four bullets: 0 violations.

## Theorem
- Definition of φ: φ(σ) = Σ over ⊕-vertices v with Λσ(v) = v of ε(v)·kσ(σ(v)), with ε = +1 on R−, −1 on R+. This is well
  defined: kσ(σ(v)) is the length component of the play value at σ(v), and Λσ(σ(v)) = v by Prop. 5.1 clause 1. It is an integer
  in [−n(n−1), n(n−1)]: at most n terms, each length ≤ n − 1.
- ≺ (Ωσ ◁ Ωσ′, or Ωσ = Ωσ′ and φ(σ) < φ(σ′)) is irreflexive and transitive. I checked all four cases (◁◁, ◁=, =◁, ==).
  ◁◁ needs antisymmetry of pointwise ⊴, which holds because ⊴ is linear on PlayValues. ✓
- Proof step "equal Ω ⇒ the same cycle nodes and the same k": both are read off Ω. The terms differ only where σ⁺(v) ≠ σ(v),
  i.e. at v ∈ I. By Lemma B, each such v is a cycle node and ε(v)·k(w) > ε(v)·k(σ(v)) (R−: k(w) > k(σ(v)); R+: k(w) < k(σ(v))).
  I ≠ ∅, so φ strictly rises. ✓
- Focus point, strategy level (the lane's trap check): in every switch the player who moves is ⊕ (Even on G, Odd on G^d). The
  component that moves is: some Ω value (strict case), or else the length of ⊕'s own successor's value at a ⊕-owned cycle node
  (flat case). No step argues from sets alone. ✓
SIGN. DATA: φ strictly rose on all 3,855 flat switches, 0 violations. Negative control: flipping ε's sign (N5T_FLIP=1) makes
(T) fail on 113 of 113 flat switches. So the check is not vacuous.

## Application to N5 (both players, one iteration, fallback)
- Even's step S4a (n5.py: opt[v] = {σ(v)} ∪ {w : (v, w) ∈ Iσ}; the restricted arena gives Even's v only those edges; ns[v] =
  best[v]): σ_new(v) ∈ A(v). So σ_new = Switch_I(σ) with I = {(v, σ_new(v)) : σ_new(v) ≠ σ(v)} ⊆ Iσ, unambiguous because σ_new is
  a strategy. ✓
  G-N2 (closed by reading the code). This needs the engine to return a choice at every vertex of the restricted arena. SPEC
  FIX 4 says every Odd vertex of R gets one, and FIX 2 covers the cycle node.
- Odd's step S4b: the same on G^d (n5.py: arena with Odd's v restricted to {τ(v)} ∪ Iτ(v); Engine on that arena). Iτ is VJ00's
  improvement set on G^d, with ⊕ = Odd and priorities + 1 (ranks are unchanged, A3). ✓
- Both in one iteration: Iσ depends only on σ (Ωσ is against ⊖'s OPTIMAL counterstrategy, not against τ), and Iτ only on τ.
  The order ≺_G depends only on σ, and ≺_{G^d} only on τ. τ enters S4a only through WHICH subset of Iσ is taken, and the
  theorem holds for every subset. So both steps, computed from the same (σ, τ) and applied together, are each either equality
  or a strict rise in their own order. No cross-interference. ✓
- Fallback S4c: switch-all on Iσ (one target per vertex; an improving w ≠ σ(v) by S2, so σ changes). If Iσ = ∅, the same on Iτ;
  then Iτ ≠ ∅, because an iteration requires Iσ ∪ Iτ ≠ ∅. FIX 3: τ is unchanged when Even falls back. n5.py does exactly this.
  This is a non-empty unambiguous subset, so it is a strict rise. ✓
- "Every iteration changes σ or τ": either S4a or S4b changed something, or the fallback runs. ✓
- No repeated state: if (σ_i, τ_i) = (σ_j, τ_j) with i < j, any strict σ-step in [i, j) gives σ_i ≺ σ_j = σ_i (transitivity
  through the equal steps), which contradicts irreflexivity. The same holds for τ. So no step is strict, which contradicts
  "at least one strict per iteration". ✓
- Bound: #iterations ≤ h(≺_G) + h(≺_{G^d}), with h counting strict steps of the longest chain. ✓ Not polynomial.
- G-N1 (scope; DATA only for the code). The theorem is about SPEC's Ξσ, which S1 defines as Ωσ. For n5.py it holds to the
  extent that si.py's Engine.evaluate computes Ωσ exactly (VJ00 §6, Prop. 6.1; SPEC Q3) and that S2's strict comparison
  (si.py improving(), key > kc) is VJ00's (2). My cross-check (docs/referee/scratch/n5t_engine_xcheck.py; si.py imported
  read-only, compared with my brute force from §4.1-4.3, all σ, G and G^d, 400 random games, n ≤ 6): 22,969 vertex valuations,
  0 mismatches. Engine correctness itself was not in this packet and is not signed here.
- Side claim "consecutive flat iterations are O(n²)": in a flat iteration both Ωσ and Ωτ are fixed. The side that changes raises
  its φ by ≥ 1, and the other side's φ is unchanged. φ and φ^d each lie in [−n(n−1), n(n−1)], so there are at most 4n(n−1)
  consecutive flat iterations. ✓

## Tools (docs/referee/scratch/, run with python3 -I from the repo root)
- n5t_probe.py [games] [nmax] [seed]: written from VJ00 §4.1-4.4 only (no repo imports). Ωσ by brute force over all positional
  ⊖ strategies. Checks (A), (B) and (T) on every non-empty unambiguous subset of improvements of every ⊕-strategy, plus the §0
  instance. Runs: seed 1 (400 games, n ≤ 5): 5,567 switches, 309 flat; seed 2 (1,500, n ≤ 6): 33,660 / 1,616; seed 3 (1,500,
  n ≤ 6): 44,245 / 1,930. All with 0 failures of A, B or T. Totals: 83,472 switches, 3,855 flat, plus the instance. Control:
  N5T_FLIP=1, seed 4: T fails 113/113.
- n5t_engine_xcheck.py: si.py Engine.evaluate against n5t_probe.omega (G-N1).

## Gaps (for GAPS.md)
- G-B1 (Lemma B, closed): state that clause 2's =_ℓ on pairs includes equal lengths (VJ00 Lemma 5.2 proof, (6)). The
  cancellation needs it.
- G-B2 (Lemma B, closed): "⊴-equivalent" is equality here, by (1).
- G-N1 (scope, open as DATA): n5.py's termination = SPEC's termination, given si.py computes VJ00's Ωσ (0 mismatches in 22,969).
- G-N2 (closed): S4a/S4b's σ_new/τ_new take values in A(v) at every vertex (code read; FIX 2, FIX 4).
- Running time: open (outside this packet).

## §C. Comparison with REFEREE-2 (R2-N5T.md, read 23:15Z by date -u, AFTER this report was pushed at 462c8ce; trunk 63b25d1)
Both verdicts: SIGNED WITH GAPS (Opus 5.5, D12). Both use the same source file (sha256 485a12de…).
| item | R-N5T (me) | R2-N5T | comparison |
|---|---|---|---|
| §0 instance, VJ00 5.8 gap | CONFIRMED; also breaks VJ00's I2 and P1 | CONFIRMED (same Ω, φ 0 → 1) | agree |
| Lemma A | SIGN; = Lemma 5.7 as stated; Prop. 5.4 (2) checked by me | CORRECT; = Lemma 5.7 (N2); Prop. 5.4 (2) checked by them | agree, including the unproved-proposition check |
| Lemma B, route to Prog(Ω, (v, w)) | via (11) and the easy direction of Lemma 5.2 | N1: Prop. 5.1 applied to σ⁺ suffices | ACCEPT N1. Prop. 5.1 for σ⁺ gives Prog(Ω_{σ⁺}, ·) on E_{σ⁺σ̄⁺} directly; my route is valid but longer |
| Lemma B, =_ℓ on pairs | G-B1: VJ00 defines =_ℓ only on sets; the pair version with equal lengths is fixed by the Lemma 5.2 proof and (6) | takes it as the equivalence of the preorder E_ℓ on M(V) × N (both length clauses ⇒ k = k′) | agree on the content. Theirs is the natural reading, since E_ℓ is defined on pairs. G-B1 stays a citation note, with no effect |
| Lemma B, contradiction step | G-B2: "⊴-equivalent" is equality, by (1) | "E-equivalent contradicts ◁; no antisymmetry needed"; N3: say "play values (1)" | agree. G-B2 is the same point as N3 |
| Theorem | SIGN; 4-case transitivity | CORRECT; M3 mutant (φ over all ⊕ vertices) also never fails | agree. M3 is consistent with Lemma B: flat switches occur only at cycle nodes |
| N5: both players per iteration | "Iσ depends only on σ; τ only selects the subset" | N4: the same fact, flagged as unstated in the reading | agree. N4 = my bullet. The reading should state it |
| N5: fallback | strict (non-empty switch-all) | the same | agree |
| flat iterations | ≤ 4n(n−1) | ≤ 4n(n−1) | agree, the same constant |
| code link | G-N1: engine valuations, G AND G^d, 22,969 vertex valuations, 0 mismatches (improving() not compared) | G-N5T-1: Even side only, valuations AND improvement sets, 23,943 strategies, 0 mismatches; dual construction not checked | complementary. Together: valuations on both sides plus improvement sets on Even's side. I built G^d my way (prio + 1, owners swapped), which is n5.py's dual() line for line. Remaining open: improving() on the Odd side (same function, other Engine instance). G-N1 = G-N5T-1, DATA |
| scope | no polynomial bound | G-N5T-2 | agree |
| output correctness (S5) | I wrote the "1 ⇒ 2" text is "sound" | G-N5T-3: rests on Lemma 5.9 / Prop. 5.10, which VJ00 does not prove; not re-derived | ACCEPT G-N5T-3, and I correct my A0: I checked the 1 ⇒ 2 text GIVEN Lemma 5.9 and Prop. 5.10, not those two themselves. Outside the packet in both reports; outputs are verified by Oink and verify.py anyway |
| Ω computation in the probe | min over positional ⊖ strategies (uses (11)) | min over all plays (does not use (11)) | theirs is the more independent oracle. Both find 0 failures. Their volume is larger (936,826 switches, 33,103 flat, plus the exhaustive n = 3 class) |

R2's extra finding: VJ00 postulate I1 also fails. CHECKED, CONFIRMED (docs/referee/scratch/n5t_i1.py, my VJ00-only oracle, not
their i1check.py).
- Instance: prio [0, 2, 4], all vertices Even's, succ 0 → {1}, 1 → {0, 1}, 2 → {0, 1}; σ = (0→1, 1→0, 2→0).
  - Ω = [(1,∅,1), (1,∅,0), (1,{2},2)]; improvements {1: [1], 2: [1]}.
  - Switching only (1, 1) leaves Ω unchanged.
  - σ is not a maximum: brute force over all strategies; (2, 1) improves Ω(2) to (1,{2},1).
  - So for I = {(1, 1)}, Improve(σ) ⊑ σ, which violates I1's "Improve(σ) ⋢ σ".
- By hand: vertex 1 ∈ R+ is a cycle node, and the switch is length-only (0 < 1, shorter is better on R+). That is exactly Lemma
  B's shape.
- Exhaustive one-player n = 3 (8 parity maps × 343 successor maps): 2,270 (game, σ, single flat improvement) triples with σ not
  a maximum. R2's 4,272 is not over one-player games only, so the counts are not comparable; both are > 0.
- Consequence (agree with R2 §4): VJ00 §5.6's P1 sentence is unsupported as written, and P2's first step uses the false I2.
  The reading's Theorem (every Switch sequence of non-empty improvement sets is finite) repairs termination. Then "no improvement
  ⇒ maximum" (1 ⇒ 2, given Lemma 5.9 / Prop. 5.10) gives P1. N5's stop rule needs only (12).
- Routing the I1 instance to L-LIT (with the reading's §0 item) is a Lead reading, as R2 says. It is an observation on the BRICS
  report, not checked against CAV 2000, and not claimed new.

Does any gap change my verdict? No.
- G-B1, G-B2, N1-N4: wording or citation.
- G-N2: closed.
- G-N1 = G-N5T-1: a condition on the code. The SPEC-level theorem holds by S1's definition of Ξ.
- G-N5T-2: scope.
- G-N5T-3: outside the packet.
Joint position: the termination half of G-N5-TERM has two referee signatures (REFEREE R-N5T, REFEREE-2 R2-N5T; both (Opus 5.5,
D12), both at 812ecba), with gaps G-B1, G-B2, G-N1 (= G-N5T-1, DATA), G-N2 (closed), G-N5T-2 (scope), G-N5T-3 (outside) and
notes N1-N4.
Suggested reading fixes (L-NEW's file, via the Lead):
- Lemma A = Lemma 5.7;
- Prop. 5.1 instead of (11) and Lemma 5.2 in Lemma B;
- the pair =_ℓ includes length;
- "play values (1)";
- state N4;
- add the I1 instance to §0.
The running-time half stays open.
