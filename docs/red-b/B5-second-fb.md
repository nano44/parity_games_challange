# B5: SECOND FALLBACK, a kill attempt on N5 (L-RED-B successor 4) — Lemma ONE-FB (k = 1 on every guided wrapper), its direct test, and the search outside the wrappers
Written 2026-11-13 (date -u in the commit). Brief (Lead, this session): «No wrapper has produced k ≥ 2 fallbacks. Design guides /
wrappers that force a SECOND fallback, by construction (read SPEC S4c and box 104 §8 … first, and state why a second fallback is or is
not possible on W-type wrappers before searching) … If a proof shows k ≤ 1 on all W-wrappers, that is a finding: write it as a lemma
(lane, unrefereed) and move to wrappers outside W.» D1 (owner, verbatim): «A claimed polynomial algorithm is far more likely to be
wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.» D18 (owner,
verbatim, excerpt): «Clearly distinguish proven results from conjectures and open problems.»
LABELS: Lemma ONE-FB is an L-RED-B lemma with a written proof, NOT refereed (PROVED here means: proved by this lane, unrefereed). Every
count is DATA. G-N5-TIME stays OPEN. Nothing here is a statement about N5 on games that are not wrappers.

## 1. Objects (sources opened, quoted by line)
- N5 = SPEC S1-S5 + FIX 1-4 of docs/new/N5-ssi-global.md (trunk 65e02855, «## SPEC» l. 24-62, FIX l. 81-93). The lines used:
  S4 «one iteration = one pass with Iσ ∪ Iτ ≠ ∅; both steps computed from the SAME (σ, τ), applied together»; S4a «A(v) = {σ(v)} ∪
  {w : (v, w) ∈ Iσ} for Even v. Arena H: Even v keeps only edges to A(v); Odd v keeps only the edge to τ(v). σ_new = … (Even's one-player
  optimum against τ among "keep or take an improving edge".)»; S4b (the same for τ, only «If Iτ ≠ ∅»); S4c «FALLBACK, if σ_new = σ and
  τ_new = τ: if Iσ ≠ ∅, for every Even v with an improving edge set σ_new(v) = the w with (v, w) ∈ Iσ maximising (Ξσ(w), w) …; otherwise do
  the same for Odd on Iτ»; FIX 3 «In a fallback iteration with Iσ ≠ ∅ only σ changes (τ_new = τ) … Odd falls back only if Iσ = ∅»; S2
  (strict improvement); S3 + FIX 1 (start).
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
Under these facts the τ side is frozen for the whole run, and the core forces the first fallback and then shuts every later one:
τ never changes, so N5 on Wg is a one-sided improvement for Even with arena «best response to the fixed faces»; the first fallback
closes Even's core K0 → K1 → q → K0; two iterations later every valve exits to it; from then on Odd's optimal counterstrategy IS the
fixed τ, Ξσ is the one-player valuation against τ, and in a one-player game an improving edge always improves inside S4a's arena, so
S4a never returns σ unchanged while Iσ ≠ ∅. The proof follows.

**Lemma ONE-FB (L-RED-B, proved here, unrefereed).** Let H be any parity game, s0 a positional Even strategy of H, ρ0 any map of V_O to
targets (as `wrapg` takes it: a vertex of H, or a pair), γ any map of Even edges to vertices of H, copy ∈ {0, 1}, CORE ∈ {high, low},
and Wg = wrapg(H, s0, ρ0, γ, copy). Under [OPT], the run of N5 (SPEC S1-S5, FIX 1-4) from S3 on Wg satisfies:
- (i) τ = τ0 (the guide faces, K2 → K2) at every state, and Iτ = ∅ at every state.
- (ii) Before the first fallback F: σ(K0) = pA, σ(K1) = s, σ(K3) = K2 and (K0, K1) ∈ Iσ at every state; the run has a fallback.
- (iii) Iteration F + 1 is not a fallback and sets σ(K1) = q (with σ(K0) = K1 from F).
- (iv) Iteration F + 2, if the run reaches it, is not a fallback, and after it every valve is at pb.
- (v) At every state from F + 2 on (and from F + 1 on if every valve is at pb there), σ̄ = τ0 at every Odd vertex, and no iteration is a
  fallback.
So k = 1, exactly, on every Wg; and I − F = 2 + (the number of iterations of a ONE-PLAYER run: Even's restricted best response to the
fixed τ0, with Ξσ = the values of (σ, τ0)) whenever the run reaches F + 2.

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
  (v.2) If Iσ ≠ ∅, S4a returns σ_new ≠ σ. Let (v, w) ∈ Iσ and σ' = σ with v switched to w. Apply [F11] Theorem 3.2 (arXiv 1106.0778v2
  = LMCS 7(3:19) 2011, p. 6, opened 2026-11-13, PDF sha1 a63a9293fec00b8078f434bfab3ea1a66e55eaf9; quoted: «Theorem 3.2 ([VJ00]). Let G
  be a parity game, σ be an improvable strategy and IG be an improvement policy. We have Ξσ ◁ ΞIG(σ)», where «Ξ ◁ Ξ′ :⇔ Ξ(v) ⊴ Ξ′(v) for
  all v ∈ V and Ξ ≠ Ξ′» and an improvement policy satisfies «(1) For every node v ∈ V0 it holds that (v, IG(σ)(v)) is an edge in AG,σ»,
  «(2) If σ is improvable then there is a node v ∈ V0 s.t. σ(v) ≺σ IG(σ)(v)») to the ONE-PLAYER parity game Wg[τ0] (Odd's edges cut to
  τ0), where the optimal counterstrategy of every Even strategy is τ0 and, by (v.1), the valuation of σ is Ξσ and its improving edges
  are Iσ; the map «σ ↦ σ'» meets (1) and (2). So Ξσ ◁ Ξσ′ in Wg[τ0]: Ξσ′ ⊵ Ξσ at every vertex and ▷ at some vertex u. σ' lies in S4a's
  arena (w ∈ A(v), Odd at τ0), so the arena's pointwise optimum σ_new [OPT] has val(σ_new, τ0) ⊵ Ξσ′ at every vertex, hence ▷ Ξσ at u:
  σ_new ≠ σ. S4c does not fire.
  (v.3) CLOSED is kept: in S4a's arena the options K1 at K0, q at K1 and pb at a valve give node K0 (the best reward), every alternative
  a node other than K0 (pA → K3 meets K3, odd and on top; s loops at K1; y leads into H against τ0); a pointwise optimum keeps them. S4c
  does not fire (v.2), and τ = τ0 (i).
  From (iii), (iv): the state after F + 2 is CLOSED (or the one after F + 1 already is), and by (v.3) every later state is CLOSED, so by
  (v.2) no iteration after F is a fallback. With (ii), k = 1. ∎
- Remark 1 (what is used of `wrapg`). Only (A1)-(A3) and the core. The guide targets (any ρ0, γ, copied priorities) and H itself are
  arbitrary. The flat W(H, s0) satisfies (A1)-(A3) with c_W in place of the guide targets (its faces end in c_W, which is below K0), so
  ONE-FB re-proves WRAP (v)'s «exactly one fallback» for N5 by another route. CORE = low changes nothing above (only (A2) is used of the
  core's priorities, plus Ω(K2) < Ω(K1) and K3 the top).
- Remark 2 (what ONE-FB says about B4). B4's P1 = I − F on every Wg is 2 plus a one-player run (Even's restricted best response to the
  fixed faces). B4's DATA «2..37 iterations after it» are such one-player runs. A second fallback cannot be forced on any Wg by any guide:
  the climb on k over W-type wrappers is empty by proof, not by search. What bounds the one-player run is a separate question (box 104
  §8 O3 names B*, REP*, SC*, O* of R90; G-N5-TIME's K9 reading bounds runs in terms of best-reply changes, CONDITIONAL); ONE-FB does not
  bound it.
- Remark 3 (where the proof breaks: the routes to k ≥ 2). (A1) fails if an Odd vertex has a second successor that avoids the valves:
  then (i) fails (Even cannot punish that deviation, Iτ may be ≠ ∅, τ may change) and (v.1) fails (σ̄ may differ from τ after the close),
  so S4a can be stuck with Iσ ≠ ∅ after F: a second fallback becomes possible. (A2) fails if a second gadget has a larger even node.
  These are the shapes of §4.
