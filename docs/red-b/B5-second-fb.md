# B5: SECOND FALLBACK, a kill attempt on N5 (L-RED-B successor 4) — Lemma ONE-FB′ (k ≤ 2 on every guided wrapper; a second fallback is NULL and ends the run), its direct test, and the search outside the wrappers
Written 2026-11-13 (date -u in the commit). Brief (Lead, this session): «No wrapper has produced k ≥ 2 fallbacks. Design guides /
wrappers that force a SECOND fallback, by construction (read SPEC S4c and box 104 §8 … first, and state why a second fallback is or is
not possible on W-type wrappers before searching) … If a proof shows k ≤ 1 on all W-wrappers, that is a finding: write it as a lemma
(lane, unrefereed) and move to wrappers outside W.» D1 (owner, verbatim): «A claimed polynomial algorithm is far more likely to be
wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.» D18 (owner,
verbatim, excerpt): «Clearly distinguish proven results from conjectures and open problems.»
LABELS: Lemma ONE-FB′ is an L-RED-B lemma with a written proof, NOT refereed (PROVED here means: proved by this lane, unrefereed). Every
count is DATA. G-N5-TIME stays OPEN. Nothing here is a statement about N5 on games that are not wrappers.

## 1. Objects (sources opened, quoted by line)
- N5 = SPEC S1-S5 + FIX 1-4 of docs/new/N5-ssi-global.md (trunk 65e02855, «## SPEC» l. 24-62, FIX l. 81-93). The lines used:
  S4 «one iteration = one pass with Iσ ∪ Iτ ≠ ∅; both steps computed from the SAME (σ, τ), applied together»; S4a «A(v) = {σ(v)} ∪
  {w : (v, w) ∈ Iσ} for Even v. Arena H: Even v keeps only edges to A(v); Odd v keeps only the edge to τ(v). σ_new = … (Even's one-player
  optimum against τ among "keep or take an improving edge".)»; S4b (the same for τ, only «If Iτ ≠ ∅»); S4c «FALLBACK, if σ_new = σ and
  τ_new = τ: if Iσ ≠ ∅, for every Even v with an improving edge set σ_new(v) = the w with (v, w) ∈ Iσ maximising (Ξσ(w), w) …; otherwise do
  the same for Odd on Iτ»; FIX 3 «In a fallback iteration with Iσ ≠ ∅ only σ changes (τ_new = τ) … Odd falls back only if Iσ = ∅»; S2
  (strict improvement); S3 + FIX 1 (start).
- SPEC lines BY SCRIPT (`git show 65e02855:docs/new/N5-ssi-global.md` (sha1 66fde9ef1726602fc0a52ca8d6d6fe8cbbcf110e), then
  `sed -n '47p;50,59p;88p'`; pasted unedited by python, not retyped):
    l. 47: S2 Improving edges: Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than Ξσ(σ(v))}; Iτ the same on G^d for τ.
    l. 50: S4 Iteration (one iteration = one pass with Iσ ∪ Iτ ≠ ∅; both steps computed from the SAME (σ, τ), applied together):
    l. 51:   a. If Iσ ≠ ∅: A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v. Arena H: Even v keeps only edges to A(v); Odd v keeps only the edge
    l. 52:      to τ(v). σ_new = Odd's optimal counterstrategy (S1 procedure) in the dual of H to the dual-Even strategy τ, read as an Even
    l. 53:      strategy of G. (Even's one-player optimum against τ among "keep or take an improving edge".) Else σ_new = σ.
    l. 54:   b. If Iτ ≠ ∅: A(v) = {τ(v)} ∪ {w : (v, w) ∈ Iτ} for Odd v. Arena H': Odd v keeps only edges to A(v); Even v only the edge to σ(v).
    l. 55:      τ_new = Odd's optimal counterstrategy (S1 procedure on H', not dual) to σ. Else τ_new = τ.
    l. 56:   c. FALLBACK, if σ_new = σ and τ_new = τ: if Iσ ≠ ∅, for every Even v with an improving edge set σ_new(v) = the w with (v, w) ∈ Iσ
    l. 57:      maximising (Ξσ(w), w) (best valuation, ties: larger index); otherwise do the same for Odd on Iτ with G^d's valuations. Count it.
    l. 58:   d. σ, τ := σ_new, τ_new.
    l. 59: S5 Stop when Iσ = Iτ = ∅. Output: Even wins v iff the cycle node of Ξσ(v) has even Ω; Even's strategy = σ on Even's region; Odd's
    l. 88: FIX 3 (S4c, A7). In a fallback iteration with Iσ ≠ ∅ only σ changes (τ_new = τ); n5.py l. 61-62. Odd falls back only if Iσ = ∅.
- Standing premise 1E-N3 (R57 (b), as box 104 §3 cites it): «S1's σ̄ and τ̄ are pointwise optima, and S4a's σ_new is a pointwise optimum
  of its arena». Used below as [OPT].
- W-type wrappers. The flat wrapper W(H, s0) (box 104 §3, Lemma WRAP (iv)-(v): «The N5 run from S3 has exactly one fallback») and the
  guided wrapper Wg(H, s0, ρ0, γ) of L-SI's experiments/si/box104/gscan104.py `wrapg` (claude/l-si 2051a0ee, l. 16-51; box 104 Addendum
  A.2 for guide104's Wg, γ = ∅), which every B3/B4 wrapper of this lane used. Wg as built by `wrapg` (read line by line):
  - vertices of H with Ω := pr + 6; for an Even edge (v, w): Even pad m (Ω 2 if w = s0(v), else 0) → Odd GATE g (Ω 1) → {pgd (Ω 1) →
    u1 → u2 → γ(v, w) (u2 has Ω pr(γ(v, w)) + 6 if γ(v, w) ≠ w and copy, else 0), pβ (Ω 0) → VALVE b_(v,w)};
  - for an Odd edge (o, w): pads x1 → x2 → x3 → valve b_(o,w); for o ∈ V_O one guide path z1 (Ω 1) → three pads → z → ρ0(o) (z has a
    copied priority when ρ0(o) is a pair (target, via));
  - a VALVE b (Even, Ω 0) → {y (Ω 2) → w, pb (Ω 1) → K0};
  - the core: K0 (Even) → {K1, pA}, pA → K3, K1 (Even) → {q, s}, s → K1, q (Ω 1) → K0, K2 (Odd) → {r, K2}, r → K1, K3 (Even) → {K1, K2};
    CORE = high: Ω(K2) = k2 (the least odd number > every other priority), Ω(K1) = k2 + 2, Ω(K0) = k2 + 3, Ω(K3) = k2 + 4; CORE = low:
    Ω(K0) = t + 2, Ω(K1) = 5, Ω(K2) = 3, Ω(K3) = t + 3 with t the least even number ≥ top + 2.
  - no c_W. Every vertex not named as Odd is Even; every pad has one successor.
- A FALLBACK is an iteration that takes S4c; k = the number of fallbacks of the run from S3; F = the first one.

## 2. Why a second fallback is not possible on W-type wrappers (written before any search)
Three structural facts of Wg (each read off `wrapg`):
- (A1) The Odd vertices of Wg are the gates, the vertices of V_O and K2. Each has exactly ONE successor that does not lead to a valve or
  to r: its guide face (pgd at a gate, z1 at o ∈ V_O; K2 at K2). Every other successor leads, through Even pads with one successor, to
  a valve (pβ → b; x1 → x2 → x3 → b) or to r → K1.
- (A2) K0 has the largest EVEN priority of Wg (only K3, odd, is larger). So a value whose cycle node is K0 is the best value for Even
  and the worst for Odd in SPEC S1's order (reward first).
- (A3) The plays that follow the guide faces at every Odd vertex never enter a valve or the core (Even's vertices of H only lead to
  pads and gates; the faces lead to vertices of H).
Under these facts the τ side is frozen for the whole run, and the core forces the first fallback and then shuts every later one
except a NULL one. τ never changes, so N5 on Wg is a one-sided improvement for Even with arena «best response to the fixed faces».
The first fallback closes Even's core K0 → K1 → q → K0, and two iterations later every valve exits to it. From then on Odd's optimal
counterstrategy IS the fixed τ, and Ξσ is the one-player valuation against τ. In a one-player game, an improving edge whose switch
changes the valuation also moves S4a's arena. The one exception is a NULL edge: (v, w) with v the cycle node of both Ξσ(σ(v)) and
Ξσ(w). Such a switch changes no valuation, so the arena ties and keeps σ, and S4c fires once more, as the last iteration.

**DEAD END (my own first claim, killed by my own test, 2026-11-13 07:10Z).** The draft committed in 2afb3f11 stated, verbatim
(docs/red-b/B5-second-fb.md lines 50-60 at 2afb3f110, pasted by script):
  > **Lemma ONE-FB (L-RED-B, proved here, unrefereed).** Let H be any parity game, s0 a positional Even strategy of H, ρ0 any map of V_O to
  > targets (as `wrapg` takes it: a vertex of H, or a pair), γ any map of Even edges to vertices of H, copy ∈ {0, 1}, CORE ∈ {high, low},
  > and Wg = wrapg(H, s0, ρ0, γ, copy). Under [OPT], the run of N5 (SPEC S1-S5, FIX 1-4) from S3 on Wg satisfies:
  > - (i) τ = τ0 (the guide faces, K2 → K2) at every state, and Iτ = ∅ at every state.
  > - (ii) Before the first fallback F: σ(K0) = pA, σ(K1) = s, σ(K3) = K2 and (K0, K1) ∈ Iσ at every state; the run has a fallback.
  > - (iii) Iteration F + 1 is not a fallback and sets σ(K1) = q (with σ(K0) = K1 from F).
  > - (iv) Iteration F + 2, if the run reaches it, is not a fallback, and after it every valve is at pb.
  > - (v) At every state from F + 2 on (and from F + 1 on if every valve is at pb there), σ̄ = τ0 at every Odd vertex, and no iteration is a
  >   fallback.
  > So k = 1, exactly, on every Wg; and I − F = 2 + (the number of iterations of a ONE-PLAYER run: Even's restricted best response to the
  > fixed τ0, with Ξσ = the values of (σ, τ0)) whenever the run reaches F + 2.
It is FALSE (part (v) and «k = 1, exactly»; (i)-(iv) survive). Instance: experiments/red-b/data/b5/null2_s5101_i313_n3.pg, sha1 8be02077b7ca002df7f91daf547f256b671ead69 (= b5lemma.py rand
seed 5101 item 313, written by experiments/red-b/b5freeze.py, a replay of that generator), H with 3 Even vertices, prio
[0, 2, 1], succ [[2], [0, 2], [1, 2]], s0 [2, 2, 2], γ {(1, 0): 1, (2, 1): 1, (2, 2): 2}, copy 1, CORE high, |Wg| 56. N5 makes 5
iterations with fallbacks at 2 and 5; engine 2 (n5b) agrees; the output is correct. At the state before iteration 5 the state is
CLOSED, σ̄ = τ0, and Iσ = {(1, 28)}. Vertex 1 has Ω 8 and is the cycle node of both its current cycle (value of σ(1) = 37: (1, ∅, 11))
and of the cycle through 28 (value (1, ∅, 5)). The edge is improving by S2 (an even node, the shorter is better), but the switch leaves
Ξ(1) = (1, ∅, 0) and every other value unchanged. Obstruction: proof step (v.2) applied [F11] Theorem 3.2, which as quoted («Ξσ ◁
ΞIG(σ)», strict somewhere) does not hold for this switch in the one-player game Wg[τ0] (L-RED-B reading). Frequency (uncorrected counters; outputs data/b5/old/lemma_rand*_{high,low}.out, pinned): 15 of 1,500
random Wg (n ≤ 10) with CORE high and 12 of 1,500 with CORE low, so 27 of 3,000; with n ≤ 14, 6 of 300 (high) and 5 of 300 (low),
so 11 of 600. Failing step: (v.2). The corrected
statement follows.

**Lemma ONE-FB′ (L-RED-B, proved here, unrefereed).** Call (v, w) ∈ Iσ NULL if v is the cycle node of both Ξσ(σ(v)) and Ξσ(w). Let H be any parity game, s0 a positional Even strategy of H, ρ0 any map of V_O to
targets (as `wrapg` takes it: a vertex of H, or a pair), γ any map of Even edges to vertices of H, copy ∈ {0, 1}, CORE ∈ {high, low},
and Wg = wrapg(H, s0, ρ0, γ, copy). Under [OPT], the run of N5 (SPEC S1-S5, FIX 1-4) from S3 on Wg satisfies:
- (i) τ = τ0 (the guide faces, K2 → K2) at every state, and Iτ = ∅ at every state.
- (ii) Before the first fallback F: σ(K0) = pA, σ(K1) = s, σ(K3) = K2 and (K0, K1) ∈ Iσ at every state; the run has a fallback.
- (iii) Iteration F + 1 is not a fallback and sets σ(K1) = q (with σ(K0) = K1 from F).
- (iv) Iteration F + 2, if the run reaches it, is not a fallback, and after it every valve is at pb.
- (v) At every state from F + 2 on (and from F + 1 on if every valve is at pb there), σ̄ = τ0 at every Odd vertex. An iteration after F
  is a fallback only if every edge of Iσ at its state is NULL. That fallback leaves Ξσ unchanged and empties Iσ, so the run stops after
  it (a NULL fallback, the last iteration).
So k ∈ {1, 2} on every Wg; k = 2 exactly when the run ends with a NULL fallback. I − F = 2 + (the number of iterations of a ONE-PLAYER
run: Even's restricted best response to the fixed τ0, with Ξσ = the values of (σ, τ0)), plus 1 if the run ends with a NULL fallback,
whenever the run reaches F + 2.

**Proof.**
- (S3) S3's pair is the standard state: FIX 1 at the vertices with ≥ 2 successors. v ∈ V_E: its pads, all even, the highest is the Ω-2
  pad of s0(v). Valve: y (Ω 2, even) over pb (Ω 1). Gate: pgd (Ω 1, the highest odd) over pβ (Ω 0). o ∈ V_O: z1 (Ω 1, the only odd
  successor) over its x1's (Ω 0). K0: pA (Ω 0, the only even successor; K1 is odd). K1: s (Ω 0, even) over q (Ω 1). K3: both successors
  odd, the lowest is K2. K2 (Odd's rule): K2 (odd) over r (Ω 0, even). (This is box 104 A.2's «S3 standard True», proved for every wrapg.)
- (i) Iτ = ∅ when τ = τ0. Ξτ is the valuation of τ0 against Even's optimal counterstrategy τ̄, a pointwise optimum [OPT]. Let u be an
  Odd vertex and x ≠ τ0(u) a successor. By (A1) x leads through one-successor pads to a valve or to r. From a valve Even can play pb →
  K0 → K1 → q → K0, from r: K1 → q → K0 → K1; this cycle has node K0. By (A2) every Even strategy that realises it gives x the best
  possible reward, so the pointwise optimum τ̄ gives x a value with node K0 (reward is compared first), the worst value for Odd. Hence x
  is not strictly better for Odd than τ0(u): (u, x) ∉ Iτ. Iτ depends on τ alone (S2 on G^d). With τ = τ0: S4b does nothing (Iτ = ∅);
  S4c changes τ only if Iσ = ∅, and then along Iτ = ∅ (FIX 3), and Iσ = Iτ = ∅ is the stop (S5). So τ stays τ0 at every state. ∎(i)
- (ii) Let a state have σ(K0) = pA, σ(K1) = s, σ(K3) = K2. Values (Ξσ, against σ̄): at K2 Odd compares its loop (node K2) with r → K1 → s
  → K1 (node K1, odd, Ω(K1) > Ω(K2)): σ̄(K2) = r, Ξσ(K2) = (K1, ∅, 2) (no vertex of the path is above K1). Ξσ(K1) = (K1, ∅, 0). Ξσ(pA) =
  (K1, {K3}, 4): K3 (odd, above K1) is in the path set. Ξσ(q) = (K1, {K0, K3}, ·): the top of {K0, K3} is K3, odd.
  So: (K0, K1) ∈ Iσ (the path sets differ by K3, odd: K1 is better); (K1, q) ∉ Iσ (q's path set has K3 on top: worse than s);
  (K3, K1) ∉ Iσ (same node K1, odd, empty path sets: the LONGER is better for Even (S1), and K2's 2 > K1's 0).
  Arena of S4a (Odd fixed at τ0, τ0(K2) = K2): A(K1) = {s}, A(K3) = {K2}, A(K0) = {pA, K1}. Via pA: pA → K3 → K2 → K2 (node K2); via
  K1: K1 → s → K1 (node K1). Both nodes odd, Ω(K2) < Ω(K1): the node K2 has the larger reward, so the pointwise optimum [OPT] keeps
  σ_new(K0) = pA, σ_new(K1) = s, σ_new(K3) = K2. A fallback switches each Even vertex with an improving edge to its (Ξσ, index)-best
  improving edge only, so before F it does not happen, and K1, K3 have no improving edge. By induction from (S3) the claim holds at every
  state before F; (K0, K1) ∈ Iσ there, so the run does not stop before F, and N5 terminates (RESULTS R15), so F exists. At F, S4c sets
  σ(K0) = K1 (its only improving edge) and leaves K1 at s and K3 at K2. ∎(ii)
- (iii) State F: σ(K0) = K1, σ(K1) = s. Ξσ(q) = q → K0 → K1 → s → K1: node K1 with path set {K0} (even, above K1), better for Even than
  Ξσ(s) (empty path set): (K1, q) ∈ Iσ, so Iσ ≠ ∅ and iteration F + 1 runs. In its arena A(K1) ∋ q and A(K0) ∋ K1 = σ(K0): the cycle K1 →
  q → K0 → K1 has node K0, the best reward (A2); via s the node is K1 (odd). The pointwise optimum has σ_new(K1) = q ≠ σ(K1): no fallback.
  At K0 it keeps K1 (via pA the play meets K3, odd, the top priority of Wg, on its cycle or path set whatever K3 does, so pA is worse than
  the K0-cycle). ∎(iii)
- (iv) State F + 1: σ(K0) = K1, σ(K1) = q, the cycle K0 → K1 → q → K0 is closed. For a valve b with σ(b) = y: Ξσ(pb) has node K0 (the play
  pb → K0 → … is all Even). Ξσ(y) = the value of y → w against σ̄; the Odd strategy τ0 gives y a play that never enters a valve or the
  core (A3), so a value with a node outside the core and a priority below Ω(K0); σ̄ is pointwise at most that for Even [OPT], so Ξσ(y) has
  a reward below K0's. So (b, pb) ∈ Iσ at every valve at y, and in the arena (Odd fixed at τ0, which never enters a valve or the core
  from y) the valve's pb-option has node K0 and its y-option a node outside the core: the pointwise optimum puts every valve at pb (and
  keeps the valves already there, and K0, K1 as in (iii)). If some valve was at y, σ_new ≠ σ: no fallback. If none was, the state F + 1
  is already CLOSED (below) and (v) applies to it. ∎(iv)
- (v) Call a state CLOSED if σ(K0) = K1, σ(K1) = q and every valve is at pb. In a CLOSED state:
  (v.1) σ̄ = τ0 at every Odd vertex. At a gate or at o ∈ V_O every successor other than the guide face leads, through one-successor pads,
  to a valve, and every valve now plays pb → K0 → …: a value with node K0, the worst for Odd (A2). The guide face's continuation, with
  Odd playing τ0 afterwards, never enters a valve or the core (A3): a value with another node. σ̄ is a pointwise optimum [OPT], so its value
  at u is not the node-K0 value, so σ̄(u) is the guide face. At K2: its loop (node K2) against r → K1 → q → K0 (node K0): σ̄(K2) = K2 = τ0(K2).
  So Ξσ is the valuation of the pair (σ, τ0), and Iσ is the set of improving edges of σ in the ONE-PLAYER game Wg[τ0] (Odd's edges cut
  to τ0), with the same values.
  (v.2) If Iσ has an edge that is not NULL, S4a returns σ_new ≠ σ. (The first version of this step said «If Iσ ≠ ∅» and cited only
  [F11] Theorem 3.2; that is the step the dead end above kills.) Let (v, w) ∈ Iσ be not NULL and σ' = σ with v switched to w. Direct
  argument in the one-player game Wg[τ0] (every play is determined by σ', resp. σ):
  - If the play from w does not visit v, then Ξσ′(v) is v prefixed to Ξσ(w). If Ξσ(σ(v)) does not have node v, Ξσ(v) is v prefixed
    to Ξσ(σ(v)), and prefixing the same vertex is strictly order-preserving on S1's order, so Ξσ′(v) ▷ Ξσ(v). If Ξσ(σ(v)) has node v,
    then Ξσ(v) = (v, ∅, 0) and Ξσ(w) has a node c ≠ v (its play avoids v), with Ξσ(w) ▷ Ξσ(σ(v)) decided by reward(c) > reward(v). So
    Ξσ′(v), with node c, is ▷ Ξσ(v).
  - If the play from w visits v, it continues as v's play, so Ξσ(w) and Ξσ(σ(v)) have the same node c. As (v, w) is not NULL, c ≠ v.
    The switch closes the cycle C = v → w → … → v. Let D be the set of vertices above c on the segment w … v (v included). Ξσ(w) ▷
    Ξσ(σ(v)) means: either D ≠ ∅ and max D is even, or D = ∅, c is odd, and the w-path is longer. In the first case the top of C is
    max D, even and above c, a better reward than c's. In the second case every vertex of C is below c, and c is odd. The top m of C
    is then either even (reward > 0 > reward(c)) or an odd number below c (a better reward). Either way Ξσ′(v), with node m, ▷ Ξσ(v).
  So σ' gives v a strictly better value against τ0. σ' lies in S4a's arena (w ∈ A(v), Odd at τ0), so the arena's pointwise optimum
  σ_new [OPT] gives v a value ⊵ Ξσ′(v) ▷ Ξσ(v): σ_new ≠ σ. (The prefix fact used: for a vertex x that is not the node of its value, Ξ(x) = x prefixed to Ξ of its
  successor; on a cycle, the successor reaches the node before it returns to x.) S4c does not fire.
  Source note. The first version cited [F11] Theorem 3.2 instead: arXiv 1106.0778v2 = LMCS 7(3:19) 2011, p. 6, opened 2026-11-13, PDF
  sha1 a63a9293fec00b8078f434bfab3ea1a66e55eaf9; quoted «Theorem 3.2 ([VJ00]). Let G be a parity game, σ be an improvable strategy and
  IG be an improvement policy. We have Ξσ ◁ ΞIG(σ)», with «Ξ ◁ Ξ′ :⇔ Ξ(v) ⊴ Ξ′(v) for all v ∈ V and Ξ ≠ Ξ′» and the two conditions «(1) For
  every node v ∈ V0 it holds that (v, IG(σ)(v)) is an edge in AG,σ», «(2) If σ is improvable then there is a node v ∈ V0 s.t. σ(v) ≺σ
  IG(σ)(v)» (pdftotext output lines 240-266; the relation symbols, lost by pdftotext, restored from the definitions next to them).
  With the length rule of its valuation order (p. 5, «assuming we have an even-priority dominating cycle node, it is better to reach the
  cycle fast»), a NULL switch is «improving» under (2), but it leaves Ξ unchanged. The instance of the dead end above is such a switch
  in a one-player game. So the theorem, as quoted, does not cover NULL switches (L-RED-B reading). VJ00 itself was not opened; its
  definitions may exclude the case.
  (v.4) NULL fallback. Let the iteration from a CLOSED state be a fallback. By (v.2) every edge of Iσ is NULL. S4c (FIX 3: only σ
  changes)
  switches every v with an improving edge to its (Ξσ, index)-best successor w_v. Each w_v's play reaches v and stays in v's play. It
  meets no other switching vertex u, because u's play would then reach v, so u would not be the node of its own value. So the switched
  cycles are those of single vertices, each still has node v, and Ξ(v) = (v, ∅, 0) is unchanged. Every other play reaches its old
  node through unchanged edges, so Ξσ is unchanged. Each switched v now sits at its Ξσ-best successor, and no other vertex had an
  improving edge, so Iσ = ∅. With Iτ = ∅ (i), the run stops. So a NULL fallback is the last iteration.
  (v.3) CLOSED is kept: in S4a's arena the options K1 at K0, q at K1 and pb at a valve give node K0 (the best reward), every alternative
  a node other than K0 (pA → K3 meets K3, odd and on top; s loops at K1; y leads into H against τ0); a pointwise optimum keeps them. S4c
  does not fire (v.2), and τ = τ0 (i).
  From (iii), (iv): the state after F + 2 is CLOSED (or the one after F + 1 already is), and by (v.3) every later state is CLOSED. By
  (v.2) an iteration after F falls back only if every edge of Iσ is NULL, and by (v.4) that iteration is the last. With (ii), k ∈ {1, 2}. ∎
- Remark 1 (what is used of `wrapg`). Only (A1)-(A3) and the core. The guide targets (any ρ0, γ, copied priorities) and H itself are
  arbitrary. The flat W(H, s0) satisfies (A1)-(A3) with c_W in place of the guide targets (its faces end in c_W, which is below K0), so
  ONE-FB′ gives k ≤ 2 there by the same route. WRAP (v) claims «exactly one fallback». On W, its faces end in c_W, which is not a vertex of
  H, so the cycles of the one-player run end at c_W and no vertex of V_E is a cycle node: no NULL edge (L-RED-B reading, not checked
  by a run). CORE = low changes nothing above (only (A2) is used of the
  core's priorities, plus Ω(K2) < Ω(K1) and K3 the top).
- Remark 2 (what ONE-FB′ says about B4). B4's P1 = I − F on every Wg is 2 plus a one-player run (Even's restricted best response to the
  fixed faces), plus 1 for a NULL end. B4's DATA «2..37 iterations after it» are such one-player runs. Beyond a NULL end, a second fallback cannot be forced on any Wg by any guide.
  The climb on k over W-type wrappers is empty by proof, not by search (k ≤ 2, and a k = 2 adds one iteration). What bounds the one-player run is a separate question (box 104
  §8 O3 names B*, REP*, SC*, O* of R90; G-N5-TIME's K9 reading bounds runs in terms of best-reply changes, CONDITIONAL); ONE-FB does not
  bound it.
- Remark 3 (where the proof breaks: the routes to k ≥ 2). (A1) fails if an Odd vertex has a second successor that avoids the valves:
  then (i) fails (Even cannot punish that deviation, Iτ may be ≠ ∅, τ may change) and (v.1) fails (σ̄ may differ from τ after the close),
  so S4a can be stuck with Iσ ≠ ∅ after F: a second fallback becomes possible. (A2) fails if a second gadget has a larger even node.
  These are the shapes of §4.

## 3. DATA: the direct test of ONE-FB′ (b5lemma.py; run_b5.sh lemma; outputs data/b5/*.out, pinned in data/SHA1SUMS; 2026-11-13)
N5 = L-NEW's box190/n5v.py mode spec (claude/l-new 069c888b), engine 2 = L-COMP's n5b.py --mode spec (trunk 7fa6aff4), wrappers =
gscan104.wrapg (claude/l-si 2051a0ee), all via git archive (B3-guide.md §6). Unit of every counter: one wrapper. Must-0: tau, itau, k
(k ∉ {1, 2}), pre, f1, f2, post (the corrected form: a fallback after F that is not a NULL fallback, a non-CLOSED state from F + 2 on,
or σ̄ ≠ τ0 at a CLOSED state), wrong (regions ≠ harness Zielonka), engdiff ((I, k) of n5v ≠ n5b's). null2 is DATA (wrappers with a NULL
second fallback).
| inputs | CORE | wrappers | tau itau k pre f1 f2 post wrong engdiff | null2 |
| --- | --- | --- | --- | --- |
| the 52 B3/B4 bests (data/b3, data/b4 state files) | high / low | 52 / 52 | all 0 / all 0 | 0 / 0 |
| own guides: switchallexp n = 2..8, LMCS G_n n = 2..8, H_n n = 1..4 | high / low | 18 / 18 | all 0 / all 0 | 0 / 0 |
| random H (b5lemma rand, seed 5101), 2 ≤ n ≤ 10, random s0, ρ0 (half off-successor), γ (p 0.3), copy | high / low | 1,500 / 1,500 | all 0 / all 0 | 15 / 12 |
| random H (seed 5102), 2 ≤ n ≤ 14 | high / low | 300 / 300 | all 0 / all 0 | 6 / 5 |
Total 3,740 wrappers, every must-0 counter 0; 38 NULL second fallbacks (each the last iteration, Ξ unchanged, only NULL edges).
Controls (each must fire; all fire):
- CTRL=1 (checks made with F + 1 for F; seed 5201, 200 wrappers): pre 200.
- CTRL=2 (CLOSED expects the valves at y; seed 5202, 200 wrappers): f2 200, post 200.
- CTRL=3 (the UNCORRECTED claim «no fallback after F»; seed 5101, the same 1,500 wrappers): post 15 = the 15 NULL wrappers of that row.
- FREE (outside the hypothesis (A1): each Odd vertex of H gets an extra non-valve face with probability 0.7; seed 5203, 500 wrappers):
  tau 256, itau 256, post 123; k = 2 on 2 of 500 (both NULL by the counter), wrong 0, engdiff 0.

## 4. Outside W: second fallbacks by construction (DATA + L-RED-B reading)
- X1 (FREE Odd faces; (A1) fails). An Odd vertex with a second non-valve successor can deviate without meeting a valve. Even cannot
  punish it, so Iτ may be non-empty and τ may change ((i) fails), and after the close σ̄ may differ from τ0 ((v.1) fails). DATA (§3,
  FREE row): τ changes on 256 of 500 wrappers. A second fallback is rare (2 of 500 in that sample, both NULL); the climbs of §5 search
  this class.
- X2 (a disjoint MIRROR core; box 104 §7's «mirror image of the core (owners swapped, priorities + 1)»; b5lemma MIRROR=1). Odd now
  keeps a permanent improving edge in the mirror, (K0′, K1′), which S4b's arena never takes, so Iτ ≠ ∅ throughout. Reading (L-RED-B, the
  mirror image of (ii)-(iv) with FIX 3's priority of Even): Even's run is unchanged up to its end. When Iσ = ∅, S4c makes Odd fall
  back once (the mirror flips). So k = 2 by construction, or k = 3 when Even's run ends with a NULL fallback, which then does not stop
  the run because Iτ ≠ ∅. DATA (data/b5/x2_mirror_rand.out, x2_mirror_states.out): random seed 5204, 500 wrappers: k = 2 on 495,
  k = 3 on 5 (each with two consecutive fallbacks at the end, e.g. [3, 6, 7]); the 52 B3/B4 bests with a mirror: k = 2 on all 52.
  Both engines agree on all 552, 0 wrong. Largest P1 = 40.
- So a second (and third) fallback is easy to force and lengthens the run by a constant. The kill question is the LENGTH after the
  first fallback, not k. The Lead (06:56Z): «Aiming the climbs outside W at P1 / I, not at k, is accepted: k ≥ 2 alone lengthens
  nothing.»
