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

## Entry 2 (2026-10-30 16:34Z by date -u): REFEREE-2 successor 23 report R2-N5-FIXD (claude/referee-2 4a960ef9, docs/referee-2/R2-N5-FIXD.md): §2, §3, §4 SIGNED, no gap; line notes L-1, L-2 (required), L-3 (optional); DATA notes N-1, N-2. Lead 16:34Z: «Add fixes entry 2 and a revision L-2 of the line … PHASE-RED′ stays conditional in L-2.»
(REFEREE-2's note labels L-1, L-2, L-3 are written R2-L-1 … below, to keep them apart from this file's line revisions L-1, L-2.)
### R2-L-1 (REFEREE-2, verbatim, R2-N5-FIXD.md l. 56-59)
> - **L-1 (REQUIRED).** In Corollary PHASE-RED′ the hypothesis reads «if every transition counted in FLATTR_P (any phase P of any N5 run) has
>   a switched Even vertex x with Ξ_{k+1}(x) ≠ Ξ_k(x)»: k is not bound in that clause, and «switched» is defined only «at k». Fix: «if every
>   transition k → k + 1 counted in FLATTR_P (any phase P of any N5 run) has an Even vertex x switched at k with Ξ_{k+1}(x) ≠ Ξ_k(x)». (The
>   packet's own §4 text has «k → k + 1»; only the line dropped it.)
- Already applied in line L-1 (entry 1, FIXD-N1; same fix text). L-2 keeps it.
### R2-L-2 (REFEREE-2, verbatim, l. 60-62)
> - **L-2 (REQUIRED).** In the same clause P is bound inside the parenthesis of the hypothesis («any phase P of any N5 run»), and the
>   conclusion «then FLATTR_P ≤ Σ_{x Even} FLATSW_P(x) and |P| ≤ …» uses P outside that scope. Fix: «then every phase P has FLATTR_P ≤ … and
>   |P| ≤ …» (as in packet §4: «then for every phase P»). Same pattern as the clause-scope binders of earlier lines (handover note).
- Applied in L-2: «then every phase P has FLATTR_P ≤ Σ_{x Even} FLATSW_P(x) and |P| ≤ (4n(n − 1) + 1)·(n(n + 2) + Σ_{x Even} FLATSW_P(x) + 1)».
### R2-L-3 (REFEREE-2, verbatim, l. 63-65; optional)
> - L-3 (precision, optional). τ appears only as «(λ_Ξ, τ) constant»; «τ_t» would match «states (σ_t, τ_t)». The words «Odd's optimal
>   counterstrategy σ̄_t» could cite «(minimising the SPEC S1 order at every vertex at once)» as SPEC does; the R91-R93 lines use the same
>   short form, so I do not require it.
- Applied in L-2 (unambiguous: the phase is a run of states t, and τ_t is the line's own symbol): «(a maximal run of consecutive states
  a, …, b with (λ_Ξ, τ_t) constant)». The σ̄_t wording is left as is (REFEREE-2 does not require it).
### N-1 (REFEREE-2, verbatim, l. 86-89)
> - N-1 (DATA). experiments/red/n3/instances/comp54_n80.start sets σ(11) = 51, but vertex 11's only edge is 11 → 11 (comp54_n80.pg l. «11 134
>   1 11;»). The lane's tools ran N5 from this non-strategy (55 iterations, K-rise 22, FLATTR 32); it is not an N5 run of the game. From the
>   default start: 11 iterations, K-rise 3, FLATTR 4. Corrected N5 corpus totals: K-rise 9596, FLATTR 6475 (lane 9615, 6503); FLAT-SW 0
>   exceptions either way. (REFEREE-2 succ. 22 found the same invalid start file during LATEP.)
- Erratum to packet §5 (DATA, not signed): the comp54_n80 run in the box 77 / 79 corpus started from a non-strategy, so it is not an N5 run.
  Corrected N5 corpus totals (REFEREE-2): K-rise 9596, FLATTR 6475 (packet: 9615, 6503); FLAT-SW 0 exceptions either way. The line cites
  no corpus totals (checked: neither L-1 nor L-2 contains 6503, 9615, 16183 or 6568), so no line change. experiments/red/n3/ is L-RED's;
  I do not edit the start file.
### N-2 (REFEREE-2, verbatim, l. 90-92)
> - N-2 (DATA wording, §5 l. 75). «Flat transitions 6568 of 16183 Ξ-changing»: 16183 = K-rise 9615 + FLATTR 6503 + 65 Ξ-unchanged in-phase
>   transitions, i.e. ALL in-phase transitions, and 6568 = FLATTR + those 65. The Ξ-changing transitions are 16118 (lane, with comp54) /
>   16071 (valid runs). Not signed material; for the fixes file.
- Erratum to packet §5 (with entry 1's FIXD-N3): read «6568 of 16183 in-phase transitions (K-rise 9615 + FLATTR 6503 + 65 Ξ-unchanged);
  Ξ-changing transitions 16118 (16071 on valid runs, i.e. without comp54_n80)».
### Not applied: PHASE-RED′ stays an IMPLICATION from CONJECTURE FLAT-SW (Lead 16:34Z: the referees cross-check REFEREE's SW-KEEP and
REFEREE-2's OWN-based proof; if both pass, L-3 makes it unconditional on the Lead's word).
### Revised line L-2 (also stored as docs/new/P-N5-FIXD-box91-line-L2.txt; sha1 in the commit message and the Lead report)
### R?? [proposed, P-N5-FIXD, revision L-2] N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57; premises RESULTS R15 (a), (d), R38 (a) and R93 (a) (Fact LEX, COMMON PREFIX); a run is the sequence of states (σ_t, τ_t); a transition is written t → t + 1 (states t, t + 1); n the number of vertices of the game; Ξ_t := Ξ_{σ_t} (SPEC S1: the valuation of every vertex under σ_t and Odd's optimal counterstrategy σ̄_t), λ_Ξ its cycle-node map; ⊴, ◁, ⊵, ▷ the SPEC S1 order (better for Even) and its strict and reverse forms; a phase P = [a, b] as in RESULTS R38 (a) (a maximal run of consecutive states a, …, b with (λ_Ξ, τ_t) constant), |P| := b − a its transitions; CS(x) the coordinate sequence of a value x of RESULTS R93 Fact LEX (reward of the cycle node; for each rank r from n − 1 down to 0, +1, −1 or 0 as the vertex of rank r is in the path set with even priority, with odd priority, or not; length, negated when the cycle node has even priority), in which the SPEC S1 order is lexicographic; for a phase P = [a, b], a state t ∈ P and a vertex v, DEPTH_t(v) := the length of the longest common prefix of CS(Ξ_t(v)) and CS(Ξ_b(v)) (n + 2 iff Ξ_t(v) = Ξ_b(v)) and K_t := Σ_v DEPTH_t(v) ∈ [0, n(n + 2)]; CH_P := the transitions of P at which Ξ changes at some vertex; FLATTR_P := the transitions of P at which Ξ changes at some vertex and K does not change; an Even vertex x is switched at k if σ_{k+1}(x) ≠ σ_k(x); FLATSW_P(x) := the transitions k → k + 1 counted in FLATTR_P at which the Even vertex x is switched and Ξ_{k+1}(x) ≠ Ξ_k(x)): (Lemma FIXD-MON) for states t ≤ t′ of a phase P and every vertex v, DEPTH_{t′}(v) ≥ DEPTH_t(v), so K is non-decreasing inside every phase; (Theorem PHASE-RED) every phase P has |P| ≤ (4n(n − 1) + 1)·(CH_P + 1) and CH_P ≤ n(n + 2) + FLATTR_P, so |P| ≤ (4n(n − 1) + 1)·(n(n + 2) + FLATTR_P + 1); and (Corollary PHASE-RED′, an implication) if every transition k → k + 1 counted in FLATTR_P (any phase P of any N5 run) has an Even vertex x switched at k with Ξ_{k+1}(x) ≠ Ξ_k(x) (CONJECTURE FLAT-SW, not proved here), then every phase P has FLATTR_P ≤ Σ_{x Even} FLATSW_P(x) and |P| ≤ (4n(n − 1) + 1)·(n(n + 2) + Σ_{x Even} FLATSW_P(x) + 1) (2026-10-30) — a REDUCTION (FLATTR_P and FLATSW_P are not bounded here; FLAT-SW is a conjecture; G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim)

## Entry 3 (2026-10-30 16:59Z by date -u): FLAT-SW proved (Theorem SW-KEEP, signed by both referees); REFEREE-2 withdraws N-1. Lead 16:59Z: «GO for FIXD fixes entry 3 and line revision L-3 = L-2 with PHASE-RED′ made UNCONDITIONAL … Record the N-1 withdrawal as a correction of entry 2's erratum … Bind every symbol.»
### Theorem SW-KEEP (REFEREE successor 20, verbatim, R-N5-FIXD.md §4b, l. 57-95, claude/referee 2c9d8040) — proof of record for FLAT-SW
> ## 4b. Theorem SW-KEEP (REFEREE proof; FLAT-SW follows)
> Premises: R15 (a) (Lemma A) and the standing SPEC premise of R57 (S1's σ̄_σ realises the pointwise optimum: Ξ_σ ⊴ val(σ, π) for every
> positional Odd π). Values are (c, Q, ℓ). x ⊕ (c, Q, ℓ) := (c, Q ∪ {x if rank x > rank c}, ℓ + 1). ⊴ is total and antisymmetric on values
> (CS is injective).
> - Fact F (play valuations of a positional pair). Suppose Even x is not its own cycle node. Then val(x) = x ⊕ val(σ(x)), and x is not in
>   val(σ(x))'s path set: the play from σ(x) reaches the cycle node before it could revisit x. If x is its own cycle node, then
>   val(x) = (x, ∅, 0) and val(σ(x)) = (x, ∅, ℓ): σ(x) lies on x's cycle, and the cycle's other vertices rank below x.
> - Theorem SW-KEEP. Let I be a non-empty set of Ξ_σ-improving edges with at most one edge per vertex, σ′ := Switch_I(σ), and S the set of
>   switched vertices. If Ξ_σ′(x) = Ξ_σ(x) for every x ∈ S, then Ξ_σ′ = Ξ_σ. Moreover, every x ∈ S with Ξ_σ′(x) = Ξ_σ(x) is its own cycle node
>   under both σ and σ′.
> - Proof.
>   (1) Take x ∈ S with Ξ_σ′(x) = Ξ_σ(x). Put d := σ(x), e := σ′(x); then Ξ_σ(d) ◁ Ξ_σ(e), since the edge is improving. "x is its own cycle
>       node" means that the first component of its value is x. Three cases:
>       - (1a) Exactly one state. Say x is its own cycle node under one strategy and not under the other. Then the first components of
>         Ξ_σ(x) and Ξ_σ′(x) are x and some c ≠ x, so Ξ_σ′(x) ≠ Ξ_σ(x), against the choice of x. This covers both orders, σ and σ′.
>       - (1b) Neither state. By F,
>       x ⊕ Ξ_σ(d) = x ⊕ Ξ_σ′(e), with the same cycle node on both sides and x in neither path set. x ⊕ · is injective there, so
>       Ξ_σ′(e) = Ξ_σ(d) ◁ Ξ_σ(e) ⊴ Ξ_σ′(e) (by R15 (a)), a contradiction.
>       - (1c) Both states. This is the only remaining case, and then Ξ_σ(x) = Ξ_σ′(x) = (x, ∅, 0).
>   (2) By F, Ξ_σ(d) = (x, ∅, ℓ_d) and Ξ_σ′(e) = (x, ∅, ℓ′). These two sandwich Ξ_σ(e), and their CS agree on the first n + 1 coordinates. By
>       COMMON PREFIX, Ξ_σ(e) = (x, ∅, ℓ_e). So π_e, the (σ, σ̄_σ)-play from e, reaches x through vertices that rank below x. It meets no
>       x′ ∈ S \ {x}: otherwise x′'s play is a suffix of π_e with cycle node x ≠ x′, which contradicts (1) for x′.
>   (3) Let Y be the valuation of the (σ′, σ̄_σ)-plays, and v a vertex with (σ, σ̄_σ)-play π.
>       - If π avoids S, it is also v's (σ′, σ̄_σ)-play, so Y(v) = Ξ_σ(v).
>       - Otherwise let x be the first vertex of S on π, and p the part of π before x. p uses no switched vertex, and no vertex of x's old cycle
>         is switched (by (1), such a vertex would have cycle node x). Under σ the play goes on around x's cycle, so
>         Ξ_σ(v) = (x, Q(p), |p|). Under σ′ it closes x → e → π_e → x, which is unchanged by (2) and has x as its top vertex. So
>         Y(v) = (x, Q(p), |p|).
>       Hence Y = Ξ_σ.
>   (4) Ξ_σ′ ⊴ Y pointwise (optimality against σ′), and Ξ_σ ⊴ Ξ_σ′ (R15 (a)). So Ξ_σ′ = Ξ_σ. □
> - Corollary FLAT-SW (the packet's CONJECTURE). It holds on every N5 run, and the same proof covers N5-LZC.
>   - Ξ depends on σ alone, so a Ξ-changing transition changes σ.
>   - By R15 (d), σ_{k+1} = Switch_I(σ_k) with ∅ ≠ I ⊆ Iσ_k and one edge per vertex. In N5-LZC, a switched vertex takes σ*(v) ≠ σ_t(v), which
>     is an Iσ_t edge.
>   - SW-KEEP then gives a switched x with Ξ_{k+1}(x) ≠ Ξ_k(x) at EVERY Ξ-changing transition, not only at those counted in FLATTR_P.
>   So PHASE-RED′ holds unconditionally:
>   |P| ≤ (4n(n − 1) + 1)(n(n + 2) + Σ_x FLATSW_P(x) + 1).
> - This is the converse direction to R15 (b) (Lemma B): if Ω does not change, every switch is a length-only switch at a cycle node. Here,
>   if every switched vertex keeps its value, then Ω does not change.
### REFEREE-2's signature (verbatim, R2-N5-FIXD-C.md §C.4 l. 58-60 and §C.5 l. 88-93, claude/referee-2 73d44f3b)
> ## C.4 Theorem SW-KEEP (REFEREE §4b): SIGNED (Opus 5.5, D15)
> Checked step by step from REFEREE's text, against R15 (a), the R57 standing premise (Ξ_σ ⊴ val(σ, π) for every positional Odd π), [LEX] /
> COMMON PREFIX, and the definition of a play value.
> …
> ## C.5 Lead reading for FLAT-SW (Lead 16:34Z)
> Lead reading, quoted: «it counts as two-referee signed if EACH referee signs at least one proof the other also signs. You sign SW-KEEP, and
> REFEREE checks your OWN-based proof (report §5).» My half is done: SW-KEEP SIGNED (C.4). For the revised line I propose citing SW-KEEP as the
> proof of record. It needs no phase hypothesis and no reading of S1's procedure, and the premises it uses are those the line already carries
> after FIXD-N2. Lemma OWN can stand as a second proof once REFEREE has checked it.
> 
- (The Lead's message cites «R2-N5-FIXD-C §3»; the section in the file is headed «## C.4 Theorem SW-KEEP (REFEREE §4b): SIGNED». L-3 cites §C.4.)
- Status change: CONJECTURE FLAT-SW (packet §4) → Theorem FLAT-SW, two-referee proved, with SW-KEEP (a REFEREE-originated proof, not the lane's)
  as the proof of record. Packet §4's «FLAT-SW itself NOT to sign» is superseded. Premises as in SW-KEEP: R15 (a), (d), the standing SPEC
  premise of R57, R93 (a) (COMMON PREFIX). SW-KEEP covers every Ξ-changing transition, not only FLATTR_P ones.
### Correction of entry 2's N-1 erratum (REFEREE-2, verbatim, R2-N5-FIXD-C.md §C.2 l. 34-40)
> - **Correction of my N-1** (R2-N5-FIXD.md §4). comp54_n80.start does give the non-edge 11 → 51 at the FORCED vertex 11 (its only edge is
>   11 → 11). REFEREE's parse_start replaces a forced vertex's move by its only edge (with a NOTE), and so runs a valid N5 run. Re-run here
>   with the start file minus «11:51» (vertex 11 forced to 11): 55 iterations, K-rise 22, FLATTR 32, exactly the lane's numbers. The lane's
>   n5x.start_pair copies 11 → 51 literally, but its counts equal those of the repaired run. So the lane's totals 9615 / 6503 ARE the
>   totals of valid runs (the repaired start). My 9596 / 6475 came from my tool skipping the whole start file and using the default start.
>   N-1 is withdrawn as a data correction. What remains is a note: the start file should be repaired at vertex 11, and the lane's reader
>   should validate starts.
- Entry 2's N-1 erratum is VOID: the «corrected totals K-rise 9596, FLATTR 6475» are withdrawn; the packet's totals K-rise 9615, FLATTR 6503
  stand (valid runs from the repaired comp54_n80 start). Entry 2's N-2 erratum («6568 of 16183 in-phase transitions») stands, but its
  «16071 on valid runs» figure came from the withdrawn N-1 run set and is void with it; 16118 Ξ-changing transitions stands.
- Remaining notes (no line change): experiments/red/n3/instances/comp54_n80.start sets the forced vertex 11 to 51; L-RED owns that file, and I
  do not edit it (Lead to route the repair). experiments/new/box21/n5x.py start_pair copies start moves without validation; a validating
  reader is a lane TODO, not done in this entry.
### Revised line L-3 (= L-2 with PHASE-RED′ unconditional; also stored as docs/new/P-N5-FIXD-box91-line-L3.txt; sha1 in the commit message and the Lead report)
- Changes from L-2: the heading tag; the clause «(Corollary PHASE-RED′, an implication) if every transition … (CONJECTURE FLAT-SW, not proved
  here), then …» is replaced by «(Theorem FLAT-SW, proof of record Theorem SW-KEEP (…)) every transition k → k + 1 of every N5 run at which Ξ
  changes at some vertex, … has an Even vertex x switched at k with Ξ_{k+1}(x) ≠ Ξ_k(x); and (Corollary PHASE-RED′) every phase P has …»; the
  status parenthesis says FLAT-SW is proved by SW-KEEP. Symbols: k, x, «switched at k», FLATTR_P, FLATSW_P, phase P are bound earlier in the line
  (unchanged from L-2); R15 (a), (d), R57's premise and R93 (a) are in its premise list.
### R?? [proposed, P-N5-FIXD, revision L-3] N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57; premises RESULTS R15 (a), (d), R38 (a) and R93 (a) (Fact LEX, COMMON PREFIX); a run is the sequence of states (σ_t, τ_t); a transition is written t → t + 1 (states t, t + 1); n the number of vertices of the game; Ξ_t := Ξ_{σ_t} (SPEC S1: the valuation of every vertex under σ_t and Odd's optimal counterstrategy σ̄_t), λ_Ξ its cycle-node map; ⊴, ◁, ⊵, ▷ the SPEC S1 order (better for Even) and its strict and reverse forms; a phase P = [a, b] as in RESULTS R38 (a) (a maximal run of consecutive states a, …, b with (λ_Ξ, τ_t) constant), |P| := b − a its transitions; CS(x) the coordinate sequence of a value x of RESULTS R93 Fact LEX (reward of the cycle node; for each rank r from n − 1 down to 0, +1, −1 or 0 as the vertex of rank r is in the path set with even priority, with odd priority, or not; length, negated when the cycle node has even priority), in which the SPEC S1 order is lexicographic; for a phase P = [a, b], a state t ∈ P and a vertex v, DEPTH_t(v) := the length of the longest common prefix of CS(Ξ_t(v)) and CS(Ξ_b(v)) (n + 2 iff Ξ_t(v) = Ξ_b(v)) and K_t := Σ_v DEPTH_t(v) ∈ [0, n(n + 2)]; CH_P := the transitions of P at which Ξ changes at some vertex; FLATTR_P := the transitions of P at which Ξ changes at some vertex and K does not change; an Even vertex x is switched at k if σ_{k+1}(x) ≠ σ_k(x); FLATSW_P(x) := the transitions k → k + 1 counted in FLATTR_P at which the Even vertex x is switched and Ξ_{k+1}(x) ≠ Ξ_k(x)): (Lemma FIXD-MON) for states t ≤ t′ of a phase P and every vertex v, DEPTH_{t′}(v) ≥ DEPTH_t(v), so K is non-decreasing inside every phase; (Theorem PHASE-RED) every phase P has |P| ≤ (4n(n − 1) + 1)·(CH_P + 1) and CH_P ≤ n(n + 2) + FLATTR_P, so |P| ≤ (4n(n − 1) + 1)·(n(n + 2) + FLATTR_P + 1); and (Theorem FLAT-SW, proof of record Theorem SW-KEEP (REFEREE R-N5-FIXD §4b, claude/referee 2c9d8040; signed by REFEREE-2 R2-N5-FIXD-C §C.4, claude/referee-2 73d44f3b), from RESULTS R15 (a), (d), the standing SPEC premise of RESULTS R57 and R93 (a)) every transition k → k + 1 of every N5 run at which Ξ changes at some vertex, in particular every transition counted in FLATTR_P for any phase P, has an Even vertex x switched at k with Ξ_{k+1}(x) ≠ Ξ_k(x); and (Corollary PHASE-RED′) every phase P has FLATTR_P ≤ Σ_{x Even} FLATSW_P(x) and |P| ≤ (4n(n − 1) + 1)·(n(n + 2) + Σ_{x Even} FLATSW_P(x) + 1) (2026-10-30) — a REDUCTION (FLATTR_P and FLATSW_P are not bounded here; FLAT-SW is proved by a referee-originated proof, SW-KEEP, signed by both referees; G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim)
