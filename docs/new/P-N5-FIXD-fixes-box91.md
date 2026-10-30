# P-N5-FIXD fixes (box 91; APPEND-ONLY). Frozen packet docs/new/P-N5-FIXD-box91.md (sha1 2050e167…) and line docs/new/P-N5-FIXD-box91-line.txt (sha1 ba09dd26…) at l-new 5027c17c are NOT edited; revisions are given here.
L-NEW successor 39 (Opus 5.5), D14 / D18. Each entry quotes the referee verbatim, then the change. Newest entry last.

## Entry 1 (2026-10-30 16:21Z by date -u): REFEREE successor 20 report R-N5-FIXD (claude/referee 2c9d8040, docs/referee/R-N5-FIXD.md): §2, §3, §4 SIGNED, no gap; line notes FIXD-N1..N4. Lead 16:22Z: «apply the four line notes as a revised line L-1, with its own sha1 … Do NOT yet make PHASE-RED′ unconditional.»
### FIXD-N1 (REFEREE, verbatim, R-N5-FIXD.md l. 136-138)
> - FIXD-N1 (FREE SYMBOL). In «(Corollary PHASE-RED′, an implication) if every transition counted in FLATTR_P … has a switched Even vertex x with
>   Ξ_{k+1}(x) ≠ Ξ_k(x)», k has no binder. The only earlier k is local to the definition «x is switched at k if …». Fix: «if every transition
>   k → k + 1 counted in FLATTR_P (any phase P of any N5 run) has an Even vertex x switched at k with Ξ_{k+1}(x) ≠ Ξ_k(x)».
- Applied in L-1: the PHASE-RED′ clause now reads «if every transition k → k + 1 counted in FLATTR_P (any phase P of any N5 run) has an Even
  vertex x switched at k with Ξ_{k+1}(x) ≠ Ξ_k(x)». The packet's §4 already binds k («every transition k → k + 1 counted in FLATTR_P»).
### FIXD-N2 (REFEREE, verbatim, l. 139-142)
> - FIXD-N2 (missing standing premise). Every N5 line since R88 carries «under the standing SPEC premise of RESULTS R57» (R92, R93 verbatim).
>   MON, and hence FIXD-MON, uses R15 (a) for Ωσ together with Ξ_σ = Ωσ, i.e. S1's counterstrategy realises the pointwise optimum. Without the
>   premise the line is formally wider than its proof. Fix: add «under the standing SPEC premise of RESULTS R57» after «(SPEC S1-S5». This is a
>   disclosure, not a widening. If SW-KEEP is used later, it rests on the same premise.
- Applied in L-1: «(SPEC S1-S5, under the standing SPEC premise of RESULTS R57; premises …». A disclosure; the claims are unchanged.
### FIXD-N3 (REFEREE, verbatim, l. 143-145)
> - FIXD-N3 (DATA label, §5, not to sign): «Flat transitions 6568 of 16183 Ξ-changing». Box 79's own table gives
>   16183 = 9615 K-rise + 6503 FLATTR + 65 Ξ-flat, so 16183 counts all in-phase transitions, and 6568 = 6503 + 65 counts those without a K-rise.
>   Read «of 16183 in-phase transitions».
- Erratum to packet §5 (DATA, not signed; not in the line): read «Flat transitions 6568 of 16183 in-phase transitions» (16183 = 9615 K-rise
  + 6503 FLATTR + 65 Ξ-flat; 6568 = 6503 + 65 without a K-rise). The frozen file is not edited.
### FIXD-N4 (REFEREE, verbatim, l. 146-147)
> - FIXD-N4 (citation). «R93 (Fact LEX)» should read «R93 (a) (Fact LEX, COMMON PREFIX)»: the proof uses COMMON PREFIX, and (a) is the RESULTS
>   item label. «R38 (a)» for the phase definition follows the landed R93 line's usage ✓.
- Applied in L-1: «R93 (Fact LEX)» → «R93 (a) (Fact LEX, COMMON PREFIX)».
### Not applied (Lead 16:22Z): PHASE-RED′ stays an IMPLICATION from CONJECTURE FLAT-SW. REFEREE's Theorem SW-KEEP (report §4b) proves
FLAT-SW but awaits REFEREE-2's independent signature; if signed, L-2 = L-1 with PHASE-RED′ unconditional, citing SW-KEEP as a
referee-originated proof.
### Revised line L-1 (also stored as docs/new/P-N5-FIXD-box91-line-L1.txt; sha1 in the commit message and the Lead report)
### R?? [proposed, P-N5-FIXD, revision L-1] N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57; premises RESULTS R15 (a), (d), R38 (a) and R93 (a) (Fact LEX, COMMON PREFIX); a run is the sequence of states (σ_t, τ_t); a transition is written t → t + 1 (states t, t + 1); n the number of vertices of the game; Ξ_t := Ξ_{σ_t} (SPEC S1: the valuation of every vertex under σ_t and Odd's optimal counterstrategy σ̄_t), λ_Ξ its cycle-node map; ⊴, ◁, ⊵, ▷ the SPEC S1 order (better for Even) and its strict and reverse forms; a phase P = [a, b] as in RESULTS R38 (a) (a maximal run of consecutive states a, …, b with (λ_Ξ, τ) constant), |P| := b − a its transitions; CS(x) the coordinate sequence of a value x of RESULTS R93 Fact LEX (reward of the cycle node; for each rank r from n − 1 down to 0, +1, −1 or 0 as the vertex of rank r is in the path set with even priority, with odd priority, or not; length, negated when the cycle node has even priority), in which the SPEC S1 order is lexicographic; for a phase P = [a, b], a state t ∈ P and a vertex v, DEPTH_t(v) := the length of the longest common prefix of CS(Ξ_t(v)) and CS(Ξ_b(v)) (n + 2 iff Ξ_t(v) = Ξ_b(v)) and K_t := Σ_v DEPTH_t(v) ∈ [0, n(n + 2)]; CH_P := the transitions of P at which Ξ changes at some vertex; FLATTR_P := the transitions of P at which Ξ changes at some vertex and K does not change; an Even vertex x is switched at k if σ_{k+1}(x) ≠ σ_k(x); FLATSW_P(x) := the transitions k → k + 1 counted in FLATTR_P at which the Even vertex x is switched and Ξ_{k+1}(x) ≠ Ξ_k(x)): (Lemma FIXD-MON) for states t ≤ t′ of a phase P and every vertex v, DEPTH_{t′}(v) ≥ DEPTH_t(v), so K is non-decreasing inside every phase; (Theorem PHASE-RED) every phase P has |P| ≤ (4n(n − 1) + 1)·(CH_P + 1) and CH_P ≤ n(n + 2) + FLATTR_P, so |P| ≤ (4n(n − 1) + 1)·(n(n + 2) + FLATTR_P + 1); and (Corollary PHASE-RED′, an implication) if every transition k → k + 1 counted in FLATTR_P (any phase P of any N5 run) has an Even vertex x switched at k with Ξ_{k+1}(x) ≠ Ξ_k(x) (CONJECTURE FLAT-SW, not proved here), then FLATTR_P ≤ Σ_{x Even} FLATSW_P(x) and |P| ≤ (4n(n − 1) + 1)·(n(n + 2) + Σ_{x Even} FLATSW_P(x) + 1) (2026-10-30) — a REDUCTION (FLATTR_P and FLATSW_P are not bounded here; FLAT-SW is a conjecture; G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim)
