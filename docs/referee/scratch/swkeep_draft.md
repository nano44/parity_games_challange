## SW-KEEP (REFEREE successor 20 proof; draft, to go into R-N5-FIXD.md)
Setting. G any game with injective ranks (SPEC S1). For an Even strategy σ, Ξ_σ := Ω_σ (SPEC S1 valuation against Odd's pointwise-optimal
reply σ̄_σ; standing SPEC premise of RESULTS R57: the S1 procedure realises the pointwise optimum, i.e. Ξ_σ(v) ⊴ val(σ, π)(v) for every
positional Odd π and every v). Values are triples (c, Q, ℓ) (cycle node, path set ⊆ {u : rank u > rank c}, length); ⊴ is the SPEC S1 order,
lexicographic in the coordinate sequence of RESULTS R93 (LEVEL-MON) and total on triples (ranks injective). x ⊕ (c, Q, ℓ) := (c, Q ∪
{x if rank x > rank c}, ℓ + 1).

Claim SW-KEEP. Let I be a non-empty set of Ξ_σ-improving edges with at most one edge per vertex, σ′ := Switch_I(σ), S the switched vertices.
If Ξ_σ′(x) = Ξ_σ(x) for every x ∈ S, then Ξ_σ′ = Ξ_σ. Moreover every x ∈ S with Ξ_σ′(x) = Ξ_σ(x) is its own cycle node in both.

Fact F (play valuation). For a positional pair (σ, π) and its play valuation val: if Even x is not its own cycle node, val(x) = x ⊕ val(σ(x)),
and x ∉ path set of val(σ(x)) (the play from σ(x) reaches the cycle node before it could revisit x). If x is its own cycle node,
val(x) = (x, ∅, 0) and val(σ(x)) = (x, ∅, ℓ) for some ℓ (σ(x) lies on x's cycle, all of whose other vertices rank below x).

Proof.
(1) Fix x ∈ S with Ξ_σ′(x) = Ξ_σ(x); d := σ(x), e := σ′(x), Ξ_σ(e) ▷ Ξ_σ(d) (I improving).
    Same cycle node of Ξ(x) in both (the value is the same), so x is its own cycle node in both or in neither.
    Neither: by F, x ⊕ Ξ_σ(d) = Ξ_σ(x) = Ξ_σ′(x) = x ⊕ Ξ_σ′(e); ⊕ by the same x onto triples with the same cycle node and without x in
    the path set is injective, so Ξ_σ′(e) = Ξ_σ(d) ◁ Ξ_σ(e) ⊴ Ξ_σ′(e) (RESULTS R15 (a), Lemma A = VJ00 Lemma 5.7), a contradiction.
    So x is its own cycle node in both: Ξ_σ(x) = Ξ_σ′(x) = (x, ∅, 0).
(2) By F, Ξ_σ(d) = (x, ∅, ℓ_d) and Ξ_σ′(e) = (x, ∅, ℓ′). Ξ_σ(d) ◁ Ξ_σ(e) ⊴ Ξ_σ′(e); in a lexicographic order every element of an interval
    carries the common prefix of its ends (the length coordinate's direction depends only on the first coordinate, which is in the prefix),
    so Ξ_σ(e) = (x, ∅, ℓ_e). Hence the (σ, σ̄_σ)-play π_e from e reaches x, and every vertex on it before x ranks below x.
    π_e meets no x′ ∈ S \ {x}: else x′'s (σ, σ̄_σ)-play is a suffix of π_e, with cycle node x ≠ x′, against (1) for x′.
(3) Y := valuation of the (σ′, σ̄_σ)-plays. Let v be any vertex and π its (σ, σ̄_σ)-play.
    If π meets no vertex of S, π is also v's (σ′, σ̄_σ)-play: Y(v) = Ξ_σ(v).
    Otherwise let x be the first vertex of S on π and p the prefix of π before x. p is unchanged under σ′. Under σ the play continues from x
    on x's cycle (x own cycle node), so Ξ_σ(v) = (x, Q(p), |p|). Under σ′ it continues x → e → π_e → x (unchanged by (2)), a cycle whose other
    vertices rank below x, so Y(v) = (x, Q(p), |p|) = Ξ_σ(v).
(4) Ξ_σ′ ⊴ Y = Ξ_σ pointwise (pointwise optimum against σ′; σ̄_σ is an Odd positional strategy of G) and Ξ_σ ⊴ Ξ_σ′ (R15 (a)).
    ⊴ is total and antisymmetric on triples, so Ξ_σ′ = Ξ_σ. □

Corollary FLAT-SW (box 79's CONJECTURE). Every Ξ-changing N5 (or N5-LZC) transition, in particular every one without a DEPTH rise, has a
switched Even x with Ξ_{k+1}(x) ≠ Ξ_k(x). (A Ξ-changing transition changes σ, since Ξ depends on σ alone; σ_{k+1} = Switch_I(σ_k) with I ⊆ Iσ_k
non-empty, one edge per vertex: RESULTS R15 (d); for N5-LZC the switched vertices take σ*(v), an S4a choice ≠ σ_t(v), hence an Iσ_t edge.)
So PHASE-RED′ holds without the conjecture.
