# Referee report R-P5: Lemma STR-DET (GAP-A-M §22i)

Referee: REFEREE, running on Opus 5.5 under owner ruling D12 (Lead reading L33). Packet: the Lead's message of 12:34Z.
Pin: trunk f920dc2, docs/alg/GAP-A-M.md §22i (line 2156 ff.). Code: dtl.cpp @ 8fbf0a7 ("N" = that line). Written 12:36Z
(date -u). docs/referee-2/R2-P5.md was not read.

## Verdict
| part | verdict (Opus 5.5, D12) | lines checked |
|---|---|---|
| (a) no tangle s lacked fires in an sptl region before π | SIGN WITH GAPS: W-a1 (wording, closed), G-a2 (Case A's justification replaced, closed) | 110-185, 198-202, 477-546, 862-890, 914-955 |
| (b) sptl region computations before π are step-identical, str included | SIGN | 73, 89, 132-137, 169-172, 200-201, 268, 485, 489 |
| (c) same SCCs, W bits; s+1 creates nothing before π | SIGN | 315-379, 385-424, 528-539 |
| (d) no differing tattr ⇒ s+1 is the last search | SIGN | 1068, 1113, 1120 |
STR-DET closes G-STR. With it, the str part of G-h1 and FDL R5 (h) holds as written on the reduced log.

## (a)
- W-a1 (wording, closed). For a region computed at a point ρ < π, s held T_s^ρ, not T_s^π. Tangles in T_s^π \ T_s^ρ are
  present in s+1 at ρ but absent in s, so the statement must exclude every tangle that s lacked AT THAT REGION, i.e.
  T_{s+1} \ T_s^ρ. The proof already covers this: it only uses "t was created by s after the region's point" and splits
  on where that happened. A tangle that s created at a later piece than the firing region is Case A; at the same piece it
  is Case B. A tangle created by s at an earlier piece is in T_s^ρ.
- Case A, context chain: correct. t ⊆ a context after piece P, and by R-PROVED2 §C5 every such context excludes P's Dom
  removal Dom_P(s) (and, after its call returns, the call's whole context). So t ∩ Dom_P(s) = ∅.
- G-a2 (closed). Z_τ ⊆ Dom_P(s) is true, but not by "PREFIX-MONO's absorbed case": that needs the later run to be
  step-ideal, and Dom is not known to be. The direct argument works because Dom's target is X (877-890). Let D_τ be the
  union of Dom's parts for the tops of V* with index ≥ index(τ). Then D_τ is closed under the threshold-pr(τ) rules in R
  (the triggered closure of R-P4 R-a1) with any T ⊆ T_s^{Dom}:
  - A p-vertex u ∈ R \ D_τ with pr(u) ≤ pr(τ) and an edge to w ∈ D_τ: w was popped in the part of a top ρ with
    pr(ρ) ≥ pr(τ) (O1), so at w's pop u is attracted (74, 88).
  - An opponent vertex with all its R-edges in D_τ: at the pop of the last of them, no edge goes to unconsumed R \ X
    (80), so it is attracted.
  - A tangle whose new vertices are in R with priority ≤ pr(τ), whose escapes are in D_τ or outside R, and which has an
    escape in D_τ: at the pop of its last escape, Dom SKIPS every vertex already in X (136, target = X). So a vertex in
    an earlier part does not reject it (this is exactly the X-straddle acceptance), and it fires.
  So D_τ ⊇ Cl_{pr τ}(P(τ⁺) ∪ {τ}) ⊇ Z_τ by (S0) (R-P4 (a)), by induction over the tops with P(τ⁺) ⊆ D_{τ⁺}. Dom runs
  after sptl, with T_s^{Dom} ⊇ T_s^{pass 1}, so D_τ is closed under the smaller rule set too. Hence Z_τ ⊆ Dom_P(s), and
  t's new vertices ⊆ Z_τ ∩ t ⊆ Dom_P(s) ∩ t = ∅. Contradiction.
- Case B: correct.
  - The pass-k regions equal the pass-1 regions as sets: out(s,p1) ⊆ out(s,pk) ⊆ out(s+1,p1) = out(s,p1), by 1.2b with
    the same inputs region by region.
  - Regions of one pass are disjoint (489), so τ′ = τ and t = C_τ (SCC1).
  - Closedness is a set property (73, 515, 519-525), and W[τ] is set at the first closed extraction (529). So t was
    extracted at τ in pass 1.
  - F5: no escape of C_τ lies in Z_τ. Tangles are tried only at escape pops (200-201), and Z_τ is the same set in s+1,
    so t is never tried there.
- Your question: does (a) exclude the 171 case before π? Yes, where it matters. In an sptl region before π, a tangle that
  fires in s+1 but not in s would have to be one s lacked at that point (with an identical state, a tangle s held behaves
  identically, by (b)'s induction), and (a) excludes it. The 171-vs-89 difference CAN still occur in best_vertices regions
  and in −1/Dom attractors, but extraction never reads those str values: F3 holds, since every str read at 268 belongs to
  a region vertex whose str was written in that sptl region (89, 171; 73 only for the top, whose str is reset at 485;
  opponent members are skipped by 73's owner test).

## (b)
- F1 checked: a failing attractTangle writes nothing except tpr[t] = −1 for a tangle with a vertex outside G (132-135).
  Within a phase G is fixed, so a tangle learned inside G′ never hits that line. A zombie tangle answers false whether or
  not it is already flagged.
- New tangles are appended to tin (443), and per (a) they are tried and rejected with no effect.
- So by induction over the pops, each sptl region computation before π executes the same pushes, pops and writes in s
  and s+1, and str agrees on the region (F3). Correct.

## (c)
- Extraction runs on equal (Z, str), so it gives equal SCCs (SCC1) and equal W bits (528-529).
- The dominion test reads the same this->G (333, 347), and s is not the last search, so neither search finds a dominion
  there.
- An SCC that s created is in T_{s+1}, so s+1 skips it as a duplicate (385-424). So s+1 creates nothing before π, and the
  `more` flags agree except for s's repeated pass, which is pure (R2-PROVED2 §13.1, now valid with (b)). Correct.

## (d)
With no differing tattr, (c) holds to the end. s+1 creates no tangle or dominion, search() returns false (1068), and the
player's loop breaks (1113 or 1120). Correct. This settles G-e2: such a transition exists at most once per phase, as the
last one.

## Consequences
- G-STR: CLOSED. The str part of G-h1 is closed. FDL R5 (h): SIGN WITH GAPS (Opus 5.5, D12), all closed. My R-P4 §C
  verdict "conditional on (STR-DET)" is withdrawn.
- §22e: the (STR-DET) term is discharged. The open terms are (CTX), (DIRTY)/(FALL) and G-e1/G-DOM (e* in Dom through an
  X-straddling acceptance), which STR-DET does not touch.

## Findings for the author (one line each)
- W-a1: state (a) for T_{s+1} \ T_s^ρ (ρ = the region's point), not T_s^π.
- G-a2: replace "PREFIX-MONO absorbed case" in Case A by the Dom-closure argument (Dom's target is X, so straddling
  tangles fire, 136).
