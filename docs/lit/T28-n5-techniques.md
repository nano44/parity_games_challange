# T28: cross-field proof techniques for N5's running time, (CYC) and (TRUST) (L-LIT, 2026-10-24)

Asked by the Lead at 13:20Z (date -u), under owner ruling D18 (docs/DECISIONS.md, verbatim):
> "Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and
> computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed
> without asking me questions. Clearly distinguish proven results from conjectures and open problems."

Scope: no runs, no contact. N5 objects as in:
- docs/agents/N5-STANDDOWN.md;
- docs/new/N5-time-box21.md §1-§3;
- docs/new/N5-1Ocyc-box25.md §5-§6;
- RESULTS R15, R17, R18.

Labels:
- **PROVED** means proved in the cited source, for the source's own objects.
- **CONJECTURE** is any claim that something transfers to N5. No transfer below is proved.
- **READING** is L-LIT interpretation.
- PDF pages unless marked. Ohlmann's thesis: printed page = PDF page − 2. sha256 values are in notes/L-LIT.md.

## 0. The two N5 targets (restated from the lane files, not re-derived)
Setting: o-cyclic 𝒞^1O, a τ-stretch (τ(o) = b) inside one joint λ-phase, the frozen run F_b, hypothesis (h).
- **Gate.** The gate is the improving set of the one-player game G^θ, in which o is a terminal of value θ = Ξ(o).
- **Selection.** Even's selection is the optimum of G^w over the gate, with w = W(o) (box 25 §5 (1), Lemma G of box 21 §3.5).
- **Monotonicity.**
  - θ is non-decreasing in the run (R15 (a) via box 21 Lemma S).
  - W is non-decreasing at arena steps and can DROP at fallbacks (box 25 §3).
- **Trust routing.** A vertex z ∈ R is trust-routed when its o-free route value lies in the window (π_z ⊕ θ, π_z ⊕ w]. Then the
  honest gate offers z's o-free edge and the selection refuses it (box 25 §5 (3)).
- **(CYC):** θ-changes per phase are poly(n).
- **(TRUST):** transitions with a trust event per phase are poly(n).
- Lead reading L40 (2)a splits (TRUST) into three parts:
  - θ-THETA re-entries, ≤ n per θ-change (lane-proved);
  - ROUTE re-entries, a one-player count;
  - (CYC).

## 1. Ranking (expected value for (CYC)/(TRUST); L-LIT estimate)
| rank | technique | field | N5 object | why ranked here |
| --- | --- | --- | --- | --- |
| 1 | strictly-increasing path algebras; junk-route flushing (Daggitt-Griffin; Sobrinho; Griffin-Shepherd-Wilfong) | network routing (BGP theory) | trust routes = routes through o valued at a stale w | a proved n² rate for a mechanism of the same shape; never connected to SI as far as L-LIT found |
| 2 | Post-Ye layered-flux analysis of deterministic MDPs (and the strongly-polynomial PI line) | LP / MDP theory | path progress vs cycle-creation events inside a phase | reward-independent bound for one-player deterministic dynamics; its proof splits exactly as (ROUTE) vs (CYC) |
| 3 | parametric single crossing; parametric shortest-path complexity (Gusfield, Carstensen, Gajjar-Radhakrishnan) | parametric optimization / economics | G^t family; the (θ, w) trust window | turns (TRUST) into counting threshold crossings; also a warning (n^Θ(log n) with edge parameters) |
| 4 | USO face-sink view (Björklund-Sandberg-Vorobyov; violator spaces) | discrete geometry | F_b as jumps to sinks of faces under two orientations | a clean reformulation of the trust deadlock; no polynomial theorem to import |
| 5 | alternating-layer lexicographic potential (GKK, Ohlmann Ch. 10) | mean-payoff games | chains of trust-routed vertices | gives 2^O(depth); polynomial only with a depth bound |
| 6 | tropical arrangements (Akian-Gaubert-Guterman) | tropical geometry | (θ, w) plane cut by n tropical lines | reformulation of rank 3; adds an O(n²) cell count, if the lines were fixed |
| 7 | Davenport-Schinzel lower envelopes (Pettie) | combinatorial geometry | σ̄(o) = argmin over exits; exit laps | needs bounded pairwise crossings, which is the open part |
| 8 | Tarski / supermodular fixed points (EPRY; FPS; Chen-Li) | order theory / game theory | θ as a 1-D monotone lattice walk | query bounds for chosen algorithms; nothing for a fixed dynamic |
| 9 | discounted strongly-polynomial PI (Ye; HMZ; Scherrer; Akian-Gaubert) | MDP / stochastic games | — | every bound carries 1/(1−γ) or a return-time constant; fails on parity (DE25, B21). One hook only: Akian-Gaubert's hub condition |

## 2. Rank 1: path-vector routing algebras
**(i) N5 object.**
- Inside a τ-stretch of a phase, read Even's selection over the gate as a policy-rich Bellman-Ford computation:
  - destinations: the phase's cycle nodes, plus the special node o;
  - node preferences: the VJ order;
  - o "advertises" two values: w to the selection, θ to the gate.
- A trust-routed z holds a route through o whose advertised value w is stale relative to o's honest value θ. In routing terms,
  z holds a junk route.
- L-LIT reading: o's honest value depends on exits whose o-free routes pass z, while z's preference depends on o. This is the
  circular-preference structure that Griffin-Shepherd-Wilfong call a dispute wheel.

**(ii) Sources.**
- **Daggitt-Griffin, "Rate of convergence of increasing path-vector routing protocols", ICNP 2018 (cl.cam.ac.uk/~tgg22, sha256
  376beef0…).**
  - Def. 1-2: routing / path algebra (S, ⊕, F, 0, ∞). Strictly increasing: ∀f, x ≠ ∞ : x < f(x), eq. (3).
  - **Theorem 1 (p.11), PROVED, formalised in Agda:** "For any strictly increasing path algebra ... and network of n nodes then σ
    converges in at most n² iterations from every starting state X".
  - Mechanism, **Lemma 13 (p.11):** "D_{τ+n} = {}". Dangerous junk routes grow in length by one per iteration and are flushed
    within n iterations, because "junk routes capable of interfering with the convergence of this next node can persist for at most
    n iterations before necessarily containing a loop".
  - Lower bound: a family Q_n needs Θ(n²) iterations (§V).
- **Griffin-Shepherd-Wilfong, "The stable paths problem and interdomain routing", IEEE/ACM ToN 2002 (Princeton copy, sha256
  82d4c2a0…).** All PROVED:
  - **Thm V.3 (p.8):** no dispute wheel ⇒ solvable;
  - **Thm V.4 (p.8):** no dispute wheel ⇒ unique solution;
  - **Thm V.9 (p.10):** no dispute wheel ⇒ SPVP is safe (converges).
- **Sobrinho, "An algebraic theory of dynamic network routing", IEEE/ACM ToN 13(5) 2005 (ENS copy, sha256 485afb23…).** Both
  PROVED:
  - **Thm 1 (p.5):** "In a free network, the path-vector protocol converges to local-optimal in-trees";
  - **Thm 2 (p.5):** in a monotonic algebra, a cycle is free iff for every weight some link of the cycle has a label outside a set
    fixed by that weight (the symbols are lost in text extraction);
  - abstract: "Monotonicity implies protocol convergence in every network".
- Daggitt-Griffin, arXiv 2106.01184 v2 (sha256 5a96dd3d…): the asynchronous, formally verified version for the DBF family.

**(iii) If it transfers (CONJECTURE).**
- Suppose N5's in-phase selection dynamics, with o's stale advertisement modelled as a junk route, satisfies a strictly increasing
  path-algebra law on o-free simple routes.
- Then a Lemma-13 analogue holds: a trust route either loops or is flushed within n transitions.
- With Theorem 1's induction (each newly converged node converges after O(n) more iterations), this gives O(n²) transitions per
  τ-stretch per phase.
- That bounds (TRUST) and (CYC) together on 𝒞^1O. Via Theorem B (C_τ ≤ d − 1) and Lemma Φ, it would give a polynomial bound for
  N5 on 𝒞^1O.
- It matches the data envelope: phases ≈ 1.6n (N5-STANDDOWN), and trust events beyond n with phases still ≤ n − 1 (box 25 §6).

**(iv) First obstacle.**
- The VJ path order is NOT increasing. Extending a path by a vertex with a large even priority makes it better for Even, so
  x < f(x) fails.
- L-LIT reading: inside one joint λ-phase the cycle nodes are fixed, and the relevant routes are o-free simple paths into them.
  The first lemma to try: on those routes, ordered by Even's VJ key relative to the phase's fixed cycle node, the extension maps
  are strictly increasing in Daggitt-Griffin's sense, or at least "free" in Sobrinho's sense on every cycle.
- If that lemma fails, use instead the weaker invariant that Lemma 13's proof actually needs: the length of a dangerous route grows
  by one per iteration.
- Second obstacle: Daggitt-Griffin's σ is one synchronous Bellman-Ford step. N5's step is an exact one-player optimum over the
  gate. It is stronger per step, but non-local, so the "fixed node" sets F_t (Def. 3) need re-proving.

## 3. Rank 2: Post-Ye layered flux, and the strongly-polynomial PI literature
**(i) N5 object.**
- F_b inside a phase is a one-player deterministic dynamic. Odd's move is fixed; Even moves in G_τ with parity rewards.
- Under Jurdziński's reduction (weights (−n)^π(v), BARRIERS verification table) it is a deterministic MDP.
- Its events split into path progress (ROUTE re-entries, o-free improvements) and cycle events (λ-changes, which Lemma Φ bounds;
  θ-changes, which are (CYC)).

**(ii) Sources.**
- **Post-Ye, "The simplex method is strongly polynomial for deterministic MDPs", arXiv 1208.5083 v2 (sha256 c51876eb…).** All
  PROVED, for the highest-gain single-switch simplex:
  - **Thm 3.7 (p.9):** "at most O(n³m² log² n) iterations on deterministic" MDPs, with uniform discount, "regardless of the
    discount factor" (abstract);
  - **Lemma 3.4 (p.8):** "Either the algorithm finishes or a new cycle is created after O(n²m log n) iterations";
  - **Lemma 3.6 (p.8):** after O(n log n) new cycles, some action is eliminated (used in Thm 3.7's proof).
  - Measure: "a set of layers in which the values of primal variables must lie" (abstract).
- **Scherrer, arXiv 1306.0386 (sha256 391b6481…).** Thm 1 (Ye 2011), Thm 2 (HMZ 2013), Thm 3-4 (new). **Thm 5 (p.4)** restates
  Post-Ye. The abstract gives Õ(n³m²τ_t τ_r), and Õ(m(n²τ_t + nτ_r)) with a transient/recurrent partition.
- **HMZ arXiv 1008.0530 v1, Thm 6.5** (re-opened T26): strategy iteration, O(m/(1−γ) · log(n/(1−γ))), any start.
- **Akian-Gaubert arXiv 1310.4953 (sha256 ad0cf80f…), Thm 5 (p.9):** PI stops after ≤ (m₁ − n)(1 + ⌊log(1−λ)/log λ⌋)
  iterations, under the bounded-return (spectral) condition (10b). Abstract: "strongly polynomial when restricted to instances with
  bounded first mean return time to a given state".

**(iii) If it transfers (CONJECTURE).**
- A Post-Ye split for F_b: (a) between two θ-changes, path progress finishes within poly(n) transitions (a Lemma 3.4 analogue);
  (b) every O(n log n) θ-changes eliminate one gate edge for the rest of the phase (a Lemma 3.6 analogue).
- Together these give (CYC) ≤ O(m·n log n) per phase, and (TRUST) via L40's split.
- Part (a) is close to R17's Lemma P on o-free paths; the trust deadlock (box 25 §5 (3)) is exactly where it breaks.
- **Akian-Gaubert hook (CONJECTURE):** their condition is a state c that every strategy pair returns to in bounded mean time. On
  N5 this is the hub situation of R58 §12d (i), where "a hub re-root is a one-player move".

**(iv) First obstacle.**
- Post-Ye's potential is LP flux under a single, fixed LP, and their pivot is a highest-gain reduced cost.
- N5's gate is honest (against σ̄), not the LP's improving set. Lemma PT (box 21 §2.6) shows the two differ (131 of 4,504 edges
  on random runs).
- First step: find a parametrised LP family LP(t) whose reduced-cost-positive set at t = θ is N5's gate. Then ask whether
  Lemma 3.4's flux layers survive the change of t at θ-changes.
- The discounted bounds (Ye, HMZ, Scherrer Thm 1-4) are dead on arrival: 1/(1−γ) = n^Θ(d) for parity (BARRIERS B21, DE25).

## 4. Rank 3: parametric single crossing and the (θ, w) window
**(i) N5 object.**
- The family G^t (o a terminal of value t). Box 25 §5 (6), READING: off o's honest continuation, each vertex's optimal choice in
  G^t flips from o-free to through-o at most once as t rises.
- Trust status of z is the position of z's o-free value relative to two thresholds, π_z ⊕ θ and π_z ⊕ w.

**(ii) Sources.**
- **Gajjar-Radhakrishnan, arXiv 1811.05115 v3 (sha256 79208b4f…).** Theorem 1 (p.2), PROVED: planar graphs with linear
  edge-weight parameter λ whose s-t shortest-path cost has n^Ω(log n) pieces.
- §1 (p.2-3) states that Carstensen (1983; not opened) gives the general-graph lower bound, and Gusfield (1980; not opened) the
  n^(log n + O(1)) upper bound.
- Theorem 3: three-parameter linear weights give n^((log n)² + O(log n)) pieces.

**(iii) If it transfers.**
- A parameter that enters only as ONE terminal's value gives each vertex's value one breakpoint in t: min(A_v, B_v + t) in
  additive terms.
- So the n^Θ(log n) phenomenon needs the parameter on many edges. In N5 the parameters θ and w enter only through o, which is
  favourable.
- CONJECTURE (counting): within a τ-stretch of a phase, a trust entry of z needs a change in one of three quantities: θ (monotone),
  w (piecewise monotone, with drops only at fallbacks), or z's o-free value (one-player route progress).
- Hence trust entries ≤ n·(1 + C_θ + C_w) + Σ_z (o-free improvements of z).
- This is a formal version of L40's split, and it says (TRUST) reduces to (CYC) + (FB-1O) + one-player counts.
- It is a CONJECTURE because trustcount.py's definition (z ∈ R_k with an honest-improving edge leaving R_k) also moves with R_k;
  membership changes in R must be added to the count.

**(iv) First obstacle.**
- Single crossing is a statement about OPTIMA of G^t. N5's iterates are not optima, because the selection is restricted to the
  gate.
- Topkis-style monotone comparative statics would need the gate to be monotone in θ in the strong set order, and w to be monotone.
- w is not monotone: there are W-drops at fallbacks (box 25 §3; fbh_drop9, n 9). Topkis / Milgrom-Shannon themselves were NOT
  opened (paywalled); EPRY §5 (below) is the opened bridge to supermodular games.

## 5. Rank 4: unique sink orientations, read as two orientations on one cube
**(i) N5 object.**
- With τ fixed and binary out-degree, Even's strategy cube carries two orientations:
  - O_θ: honest improvement, in G^θ, defining the gate;
  - O_w: values in G^w.
- An arena step jumps to the O_w-sink of the face spanned by O_θ's outgoing directions (box 21 Lemma S (c): σ' maximises
  V_{·,τ} over A(σ)).
- If O_θ = O_w, this is "jump to the sink of the out-face", and R17 bounds it on one-player games. Trust routing is exactly the
  set of directions where the two orientations disagree (READING).

**(ii) Sources.**
- **Björklund-Sandberg-Vorobyov, STACS 2003 (dbai.tuwien.ac.at copy, sha256 b4439e9c…).** Thm 20 (profitability), **Thm 22
  (p.7) stability**: stable strategies are optimal; Thm 23 uniqueness. This is the local-global property behind the USO view.
- **Gärtner-Matoušek-Rüst-Škovroň, arXiv cs/0606087 (sha256 4b66f35d…).** Thm 8 (p.7, the LP-type axioms). **§5 (p.21):** grid
  USOs induce violator spaces.
- **Matoušek, "The number of unique-sink orientations of the hypercube" (KAM series 2003-613, sha256 08cdfcb9…), Thm 1 (p.3):**
  2^Θ(2^d log d) USOs. So generic USO arguments cannot use any compact description.
- Szabó-Welzl FOCS 2001 (O(1.61^n)): NOT opened (no copy found). Abstract lower bounds: BARRIERS B14.

**(iii) If it transfers (CONJECTURE).**
- The question becomes: how many face-sink jumps can alternate between two USOs on the same cube, when one of them (O_θ) changes
  only at θ-changes?
- A bound of poly(n) jumps per change of O_θ would give (TRUST) from (CYC).

**(iv) First obstacle.**
- Every generic USO bound known is exponential (Szabó-Welzl), or an abstract lower bound (B14).
- Any proof must use the game structure (Lemma G's single scalar θ), not the cube.

## 6. Rank 5: alternating-layer lexicographic potentials (GKK)
**(i) N5 object.** Box 25 §5 (5): "the throttle propagates along routes, a chain of trust-routed vertices". Layer i = trust-routed
vertices at blocking depth i.

**(ii) Source.** Ohlmann thesis (sha256 a5c909cb…).
- **Thm 10.4 (printed p.186), PROVED:** if N = N′ and P = P′, the sequence (−|A₁|, |A₂|, −|A₃|, |A₄|, …) "strictly grows
  lexicographically".
- Lemma 10.5 and the O(2^(n/2)) proof (p.189); Thm 10.2 (p.179).

**(iii) If it transfers (CONJECTURE).** A signed lexicographic potential on blocking-depth layers would strictly grow at each
trust event. That bounds (TRUST) by the number of signed layer profiles: 2^O(D) for depth D. It is polynomial if D = O(log n),
which is a register / Strahler-type bound (BARRIERS re-verification table, DJT).

**(iv) First obstacle.** GKK's growth uses N = N′ (the zones are unchanged). The N5 analogue, "R and the exit set unchanged", fails
at every θ-change. Even GKK itself gets only 2^(n/2) from this argument.

## 7. Rank 6: tropical arrangements
**(i) N5 object.** The (θ, w) plane. Each vertex's trust thresholds are tropical lines when route values are fixed.

**(ii) Source.** **Akian-Gaubert-Guterman, arXiv 0912.2462 (sha256 72159bf0…).** The equivalence of tropical polyhedra with mean
payoff games (abstract; §3). **Thm 1.4 (p.4):** tropical independence iff a tropically non-singular n×n submatrix.

**(iii) If it transfers (CONJECTURE).**
- With route values frozen, n tropical lines cut the (θ, w) plane into O(n²) cells.
- A run with θ monotone and w monotone on each of F segments crosses O(n·F) cells.
- That would give (TRUST) ≤ O(n·(1 + FB)) per period of frozen routes.

**(iv) First obstacle.** Route values are not frozen: the lines move with one-player progress, so this is rank 3 again.

## 8. Rank 7: Davenport-Schinzel sequences
**(i) N5 object.** σ̄(o) = argmin over exits e of Ξ(e) (θ = o ⊕ min_e Ξ(e), box 25 §5 (2)). Its sequence of exits inside a phase
can lap (fts_best16: two laps over four exits, box 21 §0).

**(ii) Source.** **Pettie, arXiv 1204.1086 (sha256 3762a763…), Thm 1.2 (p.5), PROVED:** λ₃(n) = 2nα(n) + O(n), with sharp bounds
for every order s.

**(iii) If it transfers (CONJECTURE).** If each pair of exit trajectories k ↦ Ξ_k(e) crosses at most s times per phase, then the
argmin changes ≤ λ_s(#exits), which is near-linear. That bounds the laps.

**(iv) First obstacle.** For non-decreasing step functions, each crossing needs an increase of one of the two. So the crossing count
is bounded only by the route-improvement counts, which DS does not reduce. And θ-changes count value changes of the minimum, not
argmin changes.

## 9. Rank 8: Tarski fixed points and supermodular games
**(i) N5 object.** Box 21 Lemma S: L_σ ⊴ V ⊴ U_τ, with L non-decreasing and U non-increasing. θ is a 1-D monotone walk in a finite
lattice.

**(ii) Sources.** All PROVED:
- **Etessami-Papadimitriou-Rubinstein-Yannakakis, arXiv 1909.03210 (sha256 f03c9ea0…):** Thm 3.2 (p.8) "Tarski ∈ PLS"; Thm 4.1
  (p.13) Ω(log² N) queries in 2-D; §5 supermodular games (Prop. 5.2, Thm 5.4);
- **Fearnley-Pálvölgyi-Savani, arXiv 2010.02618 (sha256 732602f8…):** Thm 15 (p.16) Θ(log² n) in 3-D; O(log^(2⌈k/3⌉) n) in k-D;
- **Chen-Li, arXiv 2202.05913 (sha256 3dc3148e…):** Thm 1 (p.2) O(log^⌈(k+1)/2⌉ n).

**(iii) If it transfers.**
- These are query complexities of algorithms that CHOOSE their queries. N5's trajectory is fixed, so nothing transfers to (CYC)
  as stated.
- The only trivial transfer, a monotone walk taking ≤ height steps, is exponential: VJ valuation lattices have height 2^Θ(n).
- A design spin-off, not N5: bisect θ over its candidate values. That would be a new algorithm (L-SI's territory).

**(iv) First obstacle.** As stated: a fixed dynamic, not a chosen query sequence.

## 10. Rank 9: discounted strongly-polynomial PI
- Ye 2011 (via Scherrer Thm 1), HMZ Thm 6.5 and Scherrer Thm 2-4 all carry a 1/(1−γ) factor.
- Under the parity-to-discounted reduction, 1/(1−γ) = n^Θ(d). This is dead for parity, as in DE25 and BARRIERS B21.
- Akian-Gaubert is γ-free but needs bounded return times (§3 (iii) hook). L-SI covers the algorithmic side (Lead's split).

## 11. Recommendation (READING)
1. Give the rank-1 lemma to L-NEW 9 or a referee lane. Two parts, smallest first:
   - (a) is N5's in-phase selection order on o-free simple routes strictly increasing, or at least Sobrinho-free?
   - (b) if not, does a trust route's length grow by one per transition until it is flushed (Daggitt-Griffin Lemma 13's invariant)?
   - A counterexample to (b) on the box 25 instances (fts_best16, theta_thf16) would kill the rank-1 route at once.
2. In parallel, test rank 2's Lemma-3.4 analogue on data. Between consecutive θ-changes, is the number of transitions ≤ n − 1? This
   is R17's per-stretch bound with no θ-change, i.e. (SEG-1O). Lane data only; no proof.
3. Ranks 3 and 6 are bookkeeping that make L40's decomposition exact. They need no new idea.

No running-time claim is made (D1). G-N5-TIME stays OPEN.
