# N5′-xi: gauntlet paperwork (TARGET.md §5 steps 1-3, partial) — CANDIDATE, not a claim; G-N5-TIME unaffected
L-NEW successor 58 (Opus 5.5), D1 / D14 / D18. Lead 2026-11-07 04:00Z: «hand it to L-RED 52 as an ADVERSARY target … It stays a
CANDIDATE under D1. Meanwhile, you continue on the gauntlet's paperwork side (TARGET.md §5), without claiming anything: (1) a second,
independent implementation … (2) the barrier statement … (3) per-iteration cost at bit cost … (4) a note».
Status: CANDIDATE (D1: «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the
fleet's own, as wrong until it passes the gauntlet below.»). Nothing here claims a polynomial bound. G-N5-TIME is unaffected. L-RED 52
holds N5′-xi as an adversary target. Labels: PROVED (lane, unrefereed) / DATA / READING / AWAITING (not done).

## 1. Exact pseudocode (gauntlet step 1)
N5′-xi = SPEC S1-S5 (docs/new/N5-ssi-global.md «SPEC (EXACT)», with FIX 1-4, Q1-Q4) with ONE rule changed, inserted after S4a:
- S4a′. If Iσ ≠ ∅: compute σ_new and the arena values W* exactly as SPEC S4a (S1's procedure on the dual of H; W*(v) is the valuation
  the procedure assigns to v there). Then, for every Even v with |A(v)| ≥ 2 whose W*-cycle node is not v itself:
  TIE(v) := {w ∈ A(v) : W*(v) = v ⊕ W*(w)}, with v ⊕ (c, P, ℓ) := (c, P ∪ {v} if rank(v) > rank(c) else P, ℓ + 1);
  if TIE(v) ≠ ∅, set σ_new(v) := the element of TIE(v) that is best for Even under Ξσ (SPEC S1's order, the valuation of the CURRENT
  σ); ties by «w = SPEC's σ_new(v)» first, then by the larger index. Every other vertex keeps SPEC's σ_new.
- S4b, S4c (fallback, decided on the modified σ_new), S4d, S5 and the start S3: unchanged.
- Implementation 1: experiments/new/box190/n5v.py mode «xi» (SPEC engine si.py Engine via box21 n5x; S4a′ in step()).
- Implementation 2: experiments/new/box190/n5bxi.py (L-COMP's n5b.py SPEC mode, valuations from pgsolver_si.py, a PGSolver port; no
  code shared with implementation 1 below the arena; S4a′ re-implemented on n5b's (cycle node, frozenset P, length) valuations and its
  order nvo). History: implementation 2's first version had the Ξσ comparison inverted (it picked the Ξ-WORST tied option); found by the
  cross-check on REC_d10_tower (3 vs 6 iterations) and fixed before the runs below.

## 2. Correctness and termination (PROVED, lane; from SPEC and landed RESULTS)
- σ_new(v) ∈ TIE(v) ⊆ A(v) = {σ(v)} ∪ Iσ(v). So every iteration still applies Switch_I with I ⊆ Iσ to σ (and S4b to τ). RESULTS R15 (d)
  («N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and changes at
  least one of them … Hence no (σ, τ) state repeats and N5 terminates») applies verbatim: an iteration with σ_new = σ and τ_new = τ is
  a fallback (S4c, unchanged), which changes σ or τ.
- At the stop Iσ = Iτ = ∅, and S5 computes the output from the final σ alone. RESULTS R57 (b) Lemma OUT-G (l. 2909-2916) is stated for
  ANY such σ: «if σ is a positional Even strategy with Iσ = ∅, λ(v) is the cycle node of Ξσ(v), W := {v : Ω(λ(v)) even} and σ̄ is S1's
  Odd counterstrategy at σ, then W = W_E(G), V ∖ W = W_O(G), σ wins for Even from every v ∈ W … σ̄ wins for Odd from every v ∉ W …». So
  N5′-xi's S5 output is correct under the same standing premise (R57 (b): «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus
  SPEC conformance»), with no reference to how the run reached σ.
- Not claimed: that σ_new is still a pointwise optimum of H. No argument above needs it.

## 3. Per-iteration bit cost (gauntlet step 4, cost part; PROVED, lane)
RESULTS R57 (c) Lemma BIT-G: «With valuations stored as (a vertex, an n-bit path-set vector indexed by rank, a length ≤ n), compared by
cycle-node reward, then the top differing bit, then length (SPEC S1, Q1), one N5 iteration and the final output step cost
O(n³(n + m)) word operations on O(log(n + m))-bit words and O(n)-bit vectors on every parity game; no big integers.» S4a′ adds, per Even
v and per w ∈ A(v): one ⊕ (an OR of one bit into an n-bit vector, a length + 1) and one equality test of two valuations, O(n) bit
operations; then a maximum over TIE(v) under Ξσ, O(|A(v)|) comparisons of valuations already computed in the same iteration, O(n) bit
operations each. In total O(m·n) extra bit operations per iteration, with no new big integers: BIT-G holds for N5′-xi with the same
bound O(n³(n + m)) (the extra term is lower order). The valuations W* are the S4a S1-call output that BIT-G already counts.
- Consequence (READING): a polynomial ITERATION bound for N5′-xi would give a polynomial running time at bit cost (TARGET.md §3). No
  iteration bound is known.

## 4. Gauntlet step 2: two implementations agree (DATA; experiments/new/box190/xcheck190.py, out/xcheck.txt)
Per game: (iterations, fallbacks, regions) equal between implementations 1 and 2; regions equal to harness Zielonka; both strategy
outputs pass harness verify.check (positional strategies of both players, D2 change 5).
- C14 Γ3 (P-N5-REACH corpus on the S3-padded games): «XCHECK C14 Gamma3: agree+correct 14/14, iterations [8, 8, 6, 6, 10, 8, 8, 10,
  6, 8, 7, 11, 12, 9]» (unit = games).
- Random: harness gen.random_game, seeds 1..10,000, n 1..40 (as gauntlet190.py): «XCHECK random seeds 1..10000: agree+correct
  10000/10000, max iterations 13» (unit = games).
- Families: 15/15 families, every N run agrees and is correct: switchbestexp, switchallexp, friedmannsubexp, fearnleysubexp,
  recursiveladder N 1..7 (7/7 each); tc N 1..12 (12/12); tc+ N 1..9 (9/9); counter_m, counter_symsi, counter_rr, counter_dp,
  counter_core, counter_qpt, counter_ortl, counter_rob N 1..10 (10/10 each). In total 133 family games plus the 10,014 above (unit = games).
- Runtime growth: experiments/new/box190/out/xi_growth.png (iterations vs n, log n axis, from implementation 1, equal to implementation 2's
  counts on every game above; plot190.py).
- First-implementation-only data (box 190): 10,000 random games 0 wrong; 15 families correct; iteration counts equal to N5's on every
  family except tc. Runtime growth recorded as iteration counts per N (DETOWER §3); the growth over N is linear on every family run
  (e.g. counter_symsi 7, 13, 25, 22, 31, 37, 42, 48, 49, 55 for N = 1..10; counter_rob 3, 5, 7, 10, 13, 16, 19, 22, 25, 28; switchbestexp
  20, 32, 41, 47, 55, 62, 68). Plot: out/xi_growth.png.

## 5. Barrier statement (gauntlet step 3; DRAFT for L-LIT, who signs it off. READING except where labelled)
- Evaded, PROVED (lane, on P-N5-REACH, signed by both referees, not yet landed): the fleet's tower route (R104 REALIZE / P-N5-REACH
  REACH3 on IDEAL-ACYC genomes). On Γ3(G) from S3, N5′-xi runs the IDEAL-XI rule (box 190 §2.3), whose run length is at most the Ξ-height
  H ≤ N (box 190 §2.2, PROVED). Why: the tower needs a mover's choice among W-tied options to depend on OTHER movers' current states (the
  root-first key); S4a′ makes that choice depend only on Ξσ, which on an acyclic Ξ-structure settles bottom-up.
- Not evaded by construction, data only (READING): the classical strategy-improvement lower-bound families in the fleet's corpus,
  experiments/hard-families/families.py: PGSolver ports switchallexp, switchbestexp, friedmannsubexp, fearnleysubexp,
  recursiveladder, and Oink counter_symsi («Matthew Maat's counterexample to Schewe et al's symmetric strategy improvement»,
  counter_symsi.cpp:23, as quoted in families.py). On all of them N5′-xi's counts EQUAL N5's (W-ties do not occur, or do not change the
  choice), and both grow linearly in N on the sizes run. So N5′-xi evades them exactly as far as N5 does. Why that is (two-sided
  improvement; S4a's one-player arena optimum instead of single switches) is the N5 barrier question, not a new one. The literature
  statements behind these families (Friedmann; Friedmann-Hansen-Zwick; Fearnley; Maat) are NOT opened by me: AWAITING L-LIT, and no
  theorem of theirs is cited here.
- Cannot obviously evade (READING; targets handed to L-RED 52):
  (i) every lower bound for N5 whose runs never meet a W-tie with ≥ 2 Ξ-different options: there N5′-xi = N5 step for step;
  (ii) IDEAL-type gadgets with Ξ-CYCLES (outside R104 / P-N5-REACH's scope), where Ξ-best choices can chase each other;
  (iii) gadgets in which the W-faces are not all tied, so that S4a's arena optimum (not the tie rule) carries the dynamics;
  (iv) gadgets that make Ξσ itself W-dependent (Odd's reply at a gate switching faces), the mechanism R104 excludes by Lemma SBAR.

## 6. What is missing before N5′-xi could count (TARGET.md §5)
- Step 2: done on this lane's sets (two implementations, 10,000 random games, 15 families, plot). L-COMP has not reviewed
  implementation 2; larger N for the families is not run.
- Step 3: L-LIT's sign-off on §5 with opened sources.
- Step 4: no running-time proof exists; correctness (§2) and per-iteration cost (§3) are lane proofs, unrefereed; no Lean.
- Step 5: none.
- Adversary: L-RED 52 (Lead 04:00Z).
