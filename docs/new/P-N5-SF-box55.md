# Packet P-N5-SF (box 55): N5-SF terminates, its two one-sided runs decouple, and its length is polynomial iff SBC (Odd's best-reply changes) is
L-NEW successor 33 (Opus 5.5), D14 / D18, Lead reading L40. Lead's brief 2026-10-29 15:19Z, BOX 55 (1): «Freeze SF-TERM, DECOUPLE and SF-RED
as a referee packet docs/new/P-N5-SF-box55.md. Define every symbol from SPEC / RESULTS, name every premise (R15, R17), add a pinned check
and a quote check. Message me the one-line RESULTS statement it adds BEFORE freezing.» Written 2026-10-29 from 15:28Z (date -u).
FROZEN at push: later text goes into a fixes file (P-N5-SF-fixes-box55.md).
What this is and is not, plainly:
- It is a REDUCTION for a VARIANT of N5. It bounds N5-SF's iteration count by a polynomial times SBC, and SBC by twice the count. It does
  NOT bound SBC. CONJECTURE SF-POLY (SBC polynomial) is OPEN.
- Not about N5 itself (G-N5-TIME untouched), not a TARGET.md claim, no running-time bound, not a gauntlet pass (§5 of this file).
- Source: docs/new/N5-SF-box54.md §1-§2 at l-new 56a42d4f (L-NEW successor 32, working note). This packet governs; it changes one
  constant there (n + m → n + m + 1, §3 Remark 1) and adds the converse (Theorem SF-RED (c)).
Labels: PROVED (L-NEW 33, unrefereed) / DATA / CONJECTURE / OPEN / DEAD.

## Proposed RESULTS line (as sent to the Lead 15:27:39Z, verbatim)
"N5-SF (SPEC S1-S5 with S4a's opponent τ replaced by Odd's best reply σ̄(σ), S4b mirrored) terminates (Lemma SF-TERM; R15 (c), (d)); its
sequence of distinct σ depends on σ_0 alone and that of τ on τ_0 alone (Lemma DECOUPLE); and its iteration count I satisfies SBC/2 ≤ I <
(n + m + 1)(2(n² − n + 1) + SBC), SBC = the σ-changes at which σ̄(σ) changes plus the mirror (Theorem SF-RED; R15 (a), (c), (d), R17 (c),
(e)): a reduction, polynomial iff SBC is; CONJECTURE SF-POLY (SBC polynomial) OPEN; output correctness as N5's (rests on G-N5T-3)."

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §2 | Lemma SF-TERM (termination; the stop is S5's) | PROVED (to sign) |
| §2 | Lemma DECOUPLE (the distinct-σ sequence is the orbit of a τ-free map F; mirror for τ) | PROVED (to sign) |
| §3 | Lemma ONE-PLAYER (on a σ̄-constant stretch, F is N5's step on G_σ̄) | PROVED (to sign) |
| §3 | Theorem SF-RED (a) stretch bound, (b) upper bound, (c) converse | PROVED (to sign) |
| §3 | Remarks 1-2 (the sharper constant n + m; what SF-RED does not use) | READING (not to sign) |
| §4 | the pinned check, corpus data | DATA (not to sign) |
| §5 | SF-POLY; output correctness; gauntlet status | CONJECTURE (open) / premise outside / status (not to sign) |
Premises (LANDED; quoted at trunk 305cc8be; checked by experiments/new/box49/quotecheck3.py, §4):
- SPEC S1, injective priorities: [Q docs/new/N5-ssi-global.md@305cc8be:27] «injective priorities: rank(v) = position of v in V sorted by (Ω(v), v); p'(v) = 2·rank(v) + (Ω(v) mod 2).»
- SPEC S1, the order: [Q docs/new/N5-ssi-global.md@305cc8be:30] «order (better for Even): compare reward of c (p'(c) if even, −p'(c) if odd); then P by the signed weight»
- SPEC S1, Ξσ: [Q docs/new/N5-ssi-global.md@305cc8be:32] «Ξσ = valuation of every vertex under σ and Odd's OPTIMAL counterstrategy σ̄ (minimising this order at every vertex at once).»
- SPEC S1, Odd's side: [Q docs/new/N5-ssi-global.md@305cc8be:45-46] «Odd's side: everything on the DUAL game G^d (owner swapped, Ω + 1); τ is an "Even" strategy of G^d; Ξτ, τ̄ (= Even's optimal counterstrategy to τ, as a G^d-Odd strategy), Iτ computed there.»
- SPEC S2: [Q docs/new/N5-ssi-global.md@305cc8be:47] «S2 Improving edges: Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than Ξσ(σ(v))}; Iτ the same on G^d for τ.»
- SPEC S4: [Q docs/new/N5-ssi-global.md@305cc8be:50] «S4 Iteration (one iteration = one pass with Iσ ∪ Iτ ≠ ∅; both steps computed from the SAME (σ, τ), applied together)»
- SPEC S4a: [Q docs/new/N5-ssi-global.md@305cc8be:51-53] «a. If Iσ ≠ ∅: A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v. Arena H: Even v keeps only edges to A(v); Odd v keeps only the edge to τ(v). σ_new = Odd's optimal counterstrategy (S1 procedure) in the dual of H to the dual-Even strategy τ, read as an Even strategy of G.»
- SPEC S4c: [Q docs/new/N5-ssi-global.md@305cc8be:56-57] «c. FALLBACK, if σ_new = σ and τ_new = τ: if Iσ ≠ ∅, for every Even v with an improving edge set σ_new(v) = the w with (v, w) ∈ Iσ maximising (Ξσ(w), w) (best valuation, ties: larger index); otherwise do the same for Odd on Iτ with G^d's valuations. Count it.»
- SPEC S4c, FIX 3: [Q docs/new/N5-ssi-global.md@305cc8be:88] «FIX 3 (S4c, A7). In a fallback iteration with Iσ ≠ ∅ only σ changes (τ_new = τ)»
- SPEC S5: [Q docs/new/N5-ssi-global.md@305cc8be:59] «S5 Stop when Iσ = Iτ = ∅. Output: Even wins v iff the cycle node of Ξσ(v) has even Ω»
- RESULTS R15 (a): [Q docs/RESULTS.md@305cc8be:631] «(a) Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}.»
- RESULTS R15 (c): [Q docs/RESULTS.md@305cc8be:637-639] «≺ is a strict partial order on strategies and every non-empty switch of improvements goes strictly up in ≺. Consequence: no strategy repeats in any VJ00 strategy-improvement run with any non-empty selection rule»
- RESULTS R15 (d): [Q docs/RESULTS.md@305cc8be:641-642] «Iσ depends on σ alone (Ωσ is against ⊖'s optimal reply, not against τ).»
- RESULTS R15, limit (iii): [Q docs/RESULTS.md@305cc8be:649] «(iii) G-N5T-3 (outside the packet): N5's output correctness at S5 rests on VJ00 Lemma 5.8 "1 ⇒ 2"»
- RESULTS R17, setting: [Q docs/RESULTS.md@305cc8be:733-736] «Setting: H a one-player game (one player has out-degree 1 everywhere), injective priorities, VJ00 valuation Ω = (cycle node, P, length) with VJ00's order; switch-best: ρ_{k+1} = an optimal strategy of the arena H_k in which every vertex x may use {ρ_k(x)} ∪ I_k(x) (VJ00 improving edges, §4.4 eq. (2)); λ-phase = a maximal run of steps in which no vertex changes its cycle node.»
- RESULTS R17 (c): [Q docs/RESULTS.md@305cc8be:743-744] «(c) Theorem PH: in a λ-phase, after n − 1 steps every further in-phase step is value-flat, and there are fewer than m such steps; so a phase has fewer than n + m steps.»
- RESULTS R17 (e): [Q docs/RESULTS.md@305cc8be:747-748] «(e) Corollary 2: on a game in which one player has out-degree 1 everywhere, N5's step for the other player is switch-best, N5's fallback (S4c) fires only in the value-flat situation and then leaves no improving edge»
Notation bridge (not a premise): RESULTS writes Ωσ for VJ00's valuation of σ against the optimal reply; SPEC S1 writes Ξσ for the same
object (R15's Object line: [Q docs/RESULTS.md@305cc8be:628] «Notation as there: Ωσ = (Λσ, Πσ)»). I write Ξσ throughout, ⊴ / ◁ for SPEC S1's order pointwise.

## 0. Definitions
- G = (V, E, Ω, owner) as in SPEC; n := |V|, m := |E|; Even = owner 0, Odd = owner 1. G^d := the dual (SPEC S1, «Odd's side»). Even
  strategies σ (one successor per Even vertex), Odd strategies τ. p', reward, the order on valuations: SPEC S1. Priorities are made
  injective by p' (S1), so distinct vertices have distinct rewards.
- σ̄(σ) := Odd's optimal counterstrategy to σ computed by SPEC S1's procedure (a deterministic function of (G, σ): all list orders are
  fixed by S1). Ξσ := the valuation of every vertex under (σ, σ̄(σ)) (S1). Iσ := Even's improving edges (S2). λ_Ξ(σ) := the map
  v ↦ (cycle node of Ξσ(v)). Mirror: τ̄(τ), Ξτ, Iτ, λ_Ξ(τ) on G^d (S1, S2).
- N5-SF := SPEC S1-S5 with exactly two changes:
  - S4a′: as S4a, except that in the arena H every Odd v keeps only the edge to σ̄(σ)(v) (not τ(v)), and σ_new is Odd's optimal
    counterstrategy (S1 procedure) in the dual of H to the dual-Even strategy σ̄(σ), read as an Even strategy of G.
  - S4b′: as S4b, except that every Even v of H′ keeps only the edge to τ̄(τ)(v), and τ_new is Odd's optimal counterstrategy (S1, on H′)
    to τ̄(τ).
  S4c (with FIX 3), S4d, S5 and the iteration count (S4) are unchanged. Implementation: experiments/new/box54/n5sf.py, function step(),
  default MODE (it differs from experiments/new/box21/n5x.py step() only in the two opponent arguments, oppE / oppO).
- A(σ) := S4a′'s σ_new when Iσ ≠ ∅ (the arena optimum against σ̄(σ)). For Iσ ≠ ∅ put F(σ) := A(σ) if A(σ) ≠ σ, and otherwise
  F(σ) := σ with every Even v that has an improving edge switched to S4c's choice (argmax of (Ξσ(w), w) over (v, w) ∈ Iσ). F(σ) is
  undefined when Iσ = ∅. The mirror map F^d on Odd strategies uses A^d(τ) (S4b′) and S4c's Odd branch.
- The run: states (σ_k, τ_k), k = 0..I, I = the number of iterations (S4). The distinct-σ sequence σ^(0), σ^(1), …, σ^(p) := (σ_k) with
  consecutive repetitions removed; #σ := p + 1. Likewise τ^(0), …, τ^(q), #τ := q + 1.
- G_σ̄ for an Odd strategy σ̄: G with every Odd vertex v cut to the single edge (v, σ̄(v)); a one-player game in R17's sense (Odd has
  out-degree 1 everywhere), with n vertices and at most m edges. G^d_τ̄ likewise on G^d.
- SBC_σ := #{j < p : σ̄(σ^(j+1)) ≠ σ̄(σ^(j))}; LAM_σ := #{j < p : λ_Ξ(σ^(j+1)) ≠ λ_Ξ(σ^(j))}. SBC_τ, LAM_τ the mirror (τ̄, G^d).
  SBC := SBC_σ + SBC_τ.
- A stretch: a maximal interval [a, b] of indices of the distinct-σ sequence on which σ̄(σ^(j)) and λ_Ξ(σ^(j)) are constant.

## 2. Termination and decoupling (PROVED)
Lemma SF-TERM. Every run of N5-SF stops, after I ≤ (#σ − 1) + (#τ − 1) iterations, at a state with Iσ = Iτ = ∅, and outputs S5's output.
Proof. (i) Each change of σ is a non-empty switch of improvements. In an iteration with Iσ ≠ ∅, S4a′'s arena gives every Even v only
σ(v) and the targets of Iσ(v), so σ_new differs from σ only at vertices v where σ_new(v) ∈ Iσ(v), one edge per vertex. S4c's Even
branch also picks one edge of Iσ(v) per vertex. With Iσ = ∅, S4a′ sets σ_new = σ (SPEC S4a «Else σ_new = σ»), and S4c's Even branch
needs Iσ ≠ ∅. So whenever σ changes, σ_next = Switch_J(σ) with J := {(v, σ_next(v)) : σ_next(v) ≠ σ(v)}, ∅ ≠ J ⊆ Iσ, and J has at most
one edge per vertex (unambiguous, VJ00 §4.4). The same holds for τ on G^d. (ii) By R15 (c) every such change goes strictly up in ≺
(on G for σ, on G^d for τ), and ≺ is a strict partial order; so a σ-value, once left, never recurs, and the same for τ. Hence the
number of iterations that change σ is #σ − 1, and those that change τ number #τ − 1. (iii) Every iteration changes σ or τ: an iteration
has Iσ ∪ Iτ ≠ ∅ (S4); if σ_new = σ and τ_new = τ, S4c switches a non-empty set of improving edges of σ (if Iσ ≠ ∅) or of τ. So
I ≤ (#σ − 1) + (#τ − 1), which is finite (finitely many strategies). (iv) The loop stops only by S5 (Iσ = Iτ = ∅), and S5 is unchanged,
so the output is S5's output on the final σ. □
(The CORRECTNESS of that output is not claimed here; it rests on the same premise as N5's, §5.)
Lemma DECOUPLE. σ^(j+1) = F(σ^(j)) for every j < p, and Iσ^(p) = ∅. So the distinct-σ sequence is σ_0, F(σ_0), F(F(σ_0)), …, up to the
first strategy with no improving edge, and it does not depend on τ_0. The mirror holds for τ with F^d and τ_0.
Proof. Iσ, Ξσ and σ̄(σ) are functions of σ (R15 (d): «Iσ depends on σ alone»; S1's procedure is deterministic), so A(σ) and F(σ) are
functions of σ; τ enters neither. Take an iteration from (σ, τ) in which σ changes. Then Iσ ≠ ∅ by (i) above. Either A(σ) ≠ σ: then
σ_new = A(σ) = F(σ), S4c does not fire, and S4d sets σ := F(σ). Or A(σ) = σ: then σ changes only through S4c's Even branch, which by
FIX 3 sets σ to F(σ). So each change of σ maps the current σ to F(σ), i.e. σ^(j+1) = F(σ^(j)). At the stop Iσ = ∅ (SF-TERM), and σ is
constant from the first state with Iσ = ∅ on (no change is possible by (i)); that state carries σ^(p). The mirror: Iτ, Ξτ, τ̄(τ)
are functions of τ, S4b′ and S4c's Odd branch read only them, and an Odd change in S4c happens only when Iσ = ∅, which affects WHEN τ
changes, not to WHAT. □
Consequence (timing only). τ_0 changes only the iterations at which σ stalls (σ_new = σ while τ moves); I depends on both starts,
#σ only on σ_0 and #τ only on τ_0.

## 3. The reduction (PROVED)
Lemma ONE-PLAYER. Let σ be an Even strategy with Iσ ≠ ∅, σ̄ := σ̄(σ), and G_σ̄ as in §0. Then:
(a) the valuation of σ in G_σ̄ (SPEC S1 on G_σ̄) equals Ξσ, and the improving set of σ in G_σ̄ equals Iσ;
(b) F(σ) equals N5's iteration (SPEC S4a + S4c) on G_σ̄ from (σ, τ := σ̄), restricted to σ.
Proof. (a) In G_σ̄ Odd has exactly one strategy, σ̄, so it is Odd's optimal counterstrategy to σ there and the valuation of σ in G_σ̄
is the valuation of the play pair (σ, σ̄), i.e. Ξσ (a valuation depends only on the plays, and the plays from every vertex under
(σ, σ̄) are the same in G and in G_σ̄). The Even vertices and their edges are the same in G and G_σ̄, so S2 gives the same set. (b) N5's
S4a on G_σ̄ with τ = σ̄ builds the same arena H as S4a′ on G (the same A(v) by (a); Odd v keeps σ̄(v) in both) and applies the same S1
procedure, so it returns A(σ). In G_σ̄ Odd's improving set is empty (every Odd vertex has one successor), so τ_new = τ, and N5's S4c
fires exactly when A(σ) = σ, with the same choice (by (a), the same Iσ and Ξσ). □
Theorem SF-RED. (a) Every stretch [a, b] has b − a ≤ n + m, and at most n − 1 of its transitions change Ξ.
(b) #σ − 1 < (n + m + 1)(1 + LAM_σ + SBC_σ), LAM_σ ≤ n(n − 1); the mirror for τ. Hence
    I < (n + m + 1)(2(n² − n + 1) + SBC).
(c) Conversely SBC_σ ≤ #σ − 1 and SBC_τ ≤ #τ − 1, so SBC ≤ 2I. N5-SF makes polynomially many iterations on a class of games iff SBC
    is polynomially bounded there.
Proof. (a) On [a, b] put σ̄ := σ̄(σ^(a)) = σ̄(σ^(j)) for all j ∈ [a, b]. By Lemma DECOUPLE and Lemma ONE-PLAYER (b), σ^(a), …, σ^(b) are
consecutive states of N5's run on the one-player game G_σ̄ started at (σ^(a), σ̄), and by ONE-PLAYER (a) their valuations there are
Ξσ^(a), …, Ξσ^(b). λ_Ξ is constant on [a, b], so these b − a transitions lie in one λ-phase of that run (R17's definition: no vertex
changes its cycle node). Each is an S4a step, which is a switch-best step (R17 (e): «N5's step for the other player is switch-best»),
or an S4c step. By R17 (e) an S4c step «leaves no improving edge» on G_σ̄, so N5's run on G_σ̄ has no step after it: there is at most
one S4c step, and it is the last transition of [a, b]. R17 (c) gives fewer than n + m′ ≤ n + m switch-best steps in a λ-phase (m′ the
edge count of G_σ̄), at most n − 1 of them value-changing. So b − a ≤ (n + m − 1) + 1 = n + m. The S4c step is value-flat (R17 (e):
«fires only in the value-flat situation»), so at most n − 1 transitions change Ξ.
(b) The stretches partition {0, …, p}. A boundary between consecutive stretches is a j with σ̄ or λ_Ξ changing from σ^(j) to σ^(j+1),
so there are at most LAM_σ + SBC_σ boundaries and at most S := 1 + LAM_σ + SBC_σ stretches. Then #σ − 1 = Σ_stretches (b − a) +
(S − 1) ≤ S(n + m) + S − 1 < S(n + m + 1). LAM_σ: each σ-change is Switch_J(σ) with J non-empty and unambiguous (SF-TERM (i)), so
Ξσ ⊴ Ξ_{Switch_J(σ)} pointwise (R15 (a)). The order compares the reward of the cycle node first (SPEC S1), so for every vertex v the
reward of λ_Ξ(v) never decreases along the sequence, and a change of λ_Ξ(v) strictly increases it (equal rewards mean the same vertex,
p' being injective). There are n vertices, so each v changes its cycle node at most n − 1 times, and each j counted in LAM_σ changes
some vertex's: LAM_σ ≤ n(n − 1). The same holds on G^d (n vertices, m edges). By SF-TERM, I ≤ (#σ − 1) + (#τ − 1) <
(n + m + 1)(2 + LAM_σ + LAM_τ + SBC) ≤ (n + m + 1)(2(n² − n + 1) + SBC).
(c) Each j counted in SBC_σ is a transition j → j + 1 of the distinct-σ sequence, so SBC_σ ≤ p = #σ − 1; mirror for τ. Each σ-change
and each τ-change happens in its own iteration of the run, so #σ − 1 ≤ I and #τ − 1 ≤ I. The equivalence follows from (b) and (c),
since 2(n + m + 1)(n² − n + 1) is a polynomial. □
Remark 1 (READING, not to sign). The working note states b − a < n + m. That needs R17's PROOF: Theorem PH's count of value-flat steps
(«at most Σ_x (deg(x) − 1) < m flat steps», docs/new/N5-phase-bound-box10.md, frozen §§1-3) also covers an S4c step, which switches each
value-flat x to a strictly better successor value. The signed statements give the n + m above; the difference is one per stretch.
Remark 2 (not to sign). SF-RED uses R15 (a), (c), (d) and R17 (c), (e) as signed, and SPEC. It uses no lemma about N5's two-player
phases (none of R80-R84, no REL-SPLIT), and nothing about σ̄ beyond its being a function of σ. It does not rest on G-N5T-3.

## 4. DATA (not to sign) and the pinned check
- Checker experiments/new/box55/pcheck.py GAME [START] (imports box54/n5sf.py and box21/n5x.py read-only). Per side (Even on G; Odd on
  G^d) it flags: ORB_V (the run's distinct-σ sequence ≠ the τ-free orbit of F, computed without τ); TAU_V (a second run from the same
  σ_0 and τ_0 := each Odd vertex's last successor gives another distinct-σ sequence; mirror: same τ_0, other σ_0); IMP_V (Iσ or Ξσ on G
  ≠ those of σ on G_σ̄); RED_V (F(σ^(j)) ≠ n5x.step on G_σ̄ with τ := σ̄, at EVERY j, not only inside stretches); MON_V (Ξ goes down);
  SEG_V (a stretch with ≥ n + m transitions or > n − 1 value-changing ones; the box-54 sharper form); LAM_V; TOT_V (#σ − 1 ≥
  (n + m)(1 + LAM + SBC), again the sharper form); REP_V (a repeated state). CHECK PASS iff none fired. Sequences are compared on the
  player's own vertices (red/n3/instances/n3cov_lean.start sets SIGMA0 47:18 on an Odd vertex, which S1 ignores; the first checker
  version flagged TAU_V there).
- Control: MUT=1 computes the orbit with τ's CURRENT value as Odd's arena strategy (N5's S4a) instead of σ̄(σ); ORB_V must then fire.
| corpus (log) | games | CHECK PASS | violations | timeouts |
| --- | --- | --- | --- | --- |
| alt_all, pinned starts (box55/pc_alt.txt) | 413 | 413 | 0 | 0 |
| sicorpus, pinned starts (box55/pc_si.txt) | 277 entries | 276 | 0 | 0 (1 not run: experiments/si/instances/dlmm_ML_L6.start has no TAU0 line, n5x.start_pair raises; box 54's 276 is the same set) |
| box 54 families (box54/fam.lst; box55/pc_fam.txt): pivot_demo + dual, runquad K3 / K8 (+ dual), s3quad, topfix N = 3..10 + cmp, dualised hntop, DLC d = 2..4, runfam K10 / K40 | 20 | 20 | 0 | 0 |
| hard families (box55/hard.lst; box55/pc_hard.txt): switchbestexp N = 1..8, switchallexp N = 1..6, box54/out/hf (Oink M1 generators, PGSolver port) | 73 | 73 | 0 | 0 |
- Pinned check: experiments/new/check.sh, block "Box 55" (run by scripts/verify.sh). Expected output line:
  «box 55 P-N5-SF: pcheck PASS on n3all_maxph_0 (fallback), switchbestexp_2 (SBC 4), n3cov_lean (LAM 4, SBC 11), MUT bites; quotes PASS: PASS».
  Expected ROW lines: n3all_maxph_0 (+ .start) «ROW E_ n 3 m 6 values 3 orbit 3 SBC 1 LAM 1 SEG 2 SEGMAX 1»; switchbestexp_2
  «ROW E_ n 60 m 130 values 59 orbit 59 SBC 4 LAM 0 SEG 5 SEGMAX 18»; n3cov_lean (+ .start) «ROW E_ n 48 m 128 values 29 orbit 29 SBC 11
  LAM 4 SEG 12 SEGMAX 6» and «ROW O_ n 48 m 128 values 6 orbit 6 SBC 3 LAM 5 SEG 6 SEGMAX 0»; MUT=1 on switchbestexp_2 prints «E_ORB_V».
- Quote check: `python3 -I experiments/new/box49/quotecheck3.py docs/new/P-N5-SF-box55.md` prints QUOTES PASS (quotes=18 bad=0);
  `--mut` must fail. Both are pinned in check.sh with this file's sha1.

## 5. Not to sign
- CONJECTURE SF-POLY: SBC is polynomially bounded on every game. OPEN. With SF-RED (c) it is EQUIVALENT to N5-SF being polynomial, so it
  is not an easier statement; it only names where the cost sits. DATA (N5-SF-box54.md §3): SBC ≤ 1.17n on the library, ≤ 16 on the M1
  families; on PGSolver's switchbestexp N = 1..16 SBC = 1, 4, 11, 26, 49, 56, 60, 75, 92, 97, …, 138, 179, 232 (0.57n at N = 16).
  The proof attempt and its obstruction: docs/new/N5-SBC-box55.md.
- Output correctness: S5 on the final σ, as in N5; it rests on VJ00 Lemma 5.8 "1 ⇒ 2" (RESULTS R15 limit (iii), G-N5T-3), not
  re-derived here. DATA: every N5-SF output in box 54's runs agrees with N5's regions (WIN PASS) and has no improving edge (OPT PASS).
- Gauntlet status (TARGET.md §5) for N5-SF: docs/new/N5-SF-gauntlet-box55.md. N5-SF has passed no gauntlet step in full.
