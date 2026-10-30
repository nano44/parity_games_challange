# P-N5-GAP fixes (box 69): answers to REFEREE-2 21 (G-GAP-1, N-GAP-1..7); APPEND-ONLY
L-NEW successor 35 (Opus 5.5), D14 / D18. Lead 2026-10-30 02:00Z: «write a fixes file for P-N5-GAP, append-only … G-GAP-1 gets a repaired
OPT-OFF proof as an H-item. Each N-GAP note gets its own H-item. Add a corrected line as its own H-item, if any wording changes.»
Written from ~02:10Z (date -u).
- Packet: docs/new/P-N5-GAP-box69.md, FROZEN at l-new 28ceeadc, sha1 d67f8e04b54d5621ebecf27e7fe7151ce57793cd (unchanged; re-measured).
- Report: REFEREE-2 21, docs/referee-2/R2-N5-GAP.md at claude/referee-2 aee8971e. REFEREE 19's notes will follow as later H-items.
- Status: H1 repairs a proof step (G-GAP-1); the statement of OPT-OFF is unchanged. H2-H8 are clarifications or DATA corrections. H9 is
  the corrected RESULTS line. No signed statement changes.

## H1 (G-GAP-1): repaired proof of Lemma OPT-OFF (§2.4)
Statement unchanged: H a one-player game of Even (Odd fixed), ρ an optimal strategy of H, v Even and not its own Ω_ρ-cycle node, (v, c) an
edge of H; then Ω_ρ(c) ⊴ Ω_ρ(ρ(v)).
Defect (REFEREE-2 §2): Case 2 assumed that c's play meets v before v's cycle node u. The case "v lies on u's cycle and c's play reaches u
before v" (u ∈ π) breaks «Ω_ρ(c) is |π| + 1 longer» and (ii)'s parity step. Instance: REFEREE-2's case2u_inst.pg (n 3).
Repaired proof. Suppose Ω_ρ(c) ▷ Ω_ρ(ρ v). Put u := the cycle node of Ω_ρ(v) and ρ′ := ρ[v → c], a strategy of H; [F1] gives Ω_ρ ⊵ Ω_ρ′.
Split by the ρ-PATH from c to its own cycle node u_c := λ_ρ(c) (the play up to the first visit of u_c).
- Case 1: that path avoids v.
  - (1a) v is not on u_c's cycle. Then the whole ρ-play from c avoids v, the ρ′-play from v is v followed by it, and Ω_ρ′(v) = v ⊕ Ω_ρ(c).
    Also Ω_ρ(v) = v ⊕ Ω_ρ(ρ v) [V1]. Both paths to their cycle nodes avoid v (N-GAP-2's wording). [V2] strict gives Ω_ρ′(v) ▷ Ω_ρ(v),
    against [F1].
  - (1b) v is on u_c's cycle. Then u = λ_ρ(v) = u_c, and v is less relevant than u (u is its cycle's most relevant vertex, v ≠ u). Let
    S := {y on c's path to u (excluding u) : y more relevant than u}.
    - Ω_ρ(ρ v): ρv's path to u runs along the cycle, so its path set is ∅.
    - Ω_ρ(c) has path set S, and Ω_ρ(c) ▷ Ω_ρ(ρ v).
    - The ρ′-play from v is the cycle Z = v, c, …, u, …, v (c's path to u, then u's cycle arc back to v). Its vertices more relevant than u
      are exactly S.
    - If S ≠ ∅: Ω_ρ(c) ▷ Ω_ρ(ρ v) with equal cycle nodes forces max S even. max S is Z's top, so Ω_ρ′(v) has an even cycle node more
      relevant than u, with a greater reward: Ω_ρ′(v) ▷ Ω_ρ(v), against [F1].
    - If S = ∅: Z's top is u, and Ω_ρ′(v) = (u, ∅, 1 + |c's path to u|) = v ⊕ Ω_ρ(c), while Ω_ρ(v) = v ⊕ Ω_ρ(ρ v) [V1]. Both paths to u avoid
      v. [V2] strict: Ω_ρ′(v) ▷ Ω_ρ(v), against [F1].
- Case 2: that path visits v. Then u_c = u, and c's path to u is π, v, then v's path to u, with π := the part before the first v. π does not
  contain u (the path stops at its first u, which comes after v). π is disjoint from ρv's PATH to u:
  - if v is not on u's cycle, a common vertex would make c's play follow v's play from there, and that play never visits v;
  - if v is on u's cycle, π can contain only cycle vertices on the arc from u to v, and ρv's path to u is the other arc.
  So the packet's Case 2 computation holds verbatim:
  - S := {y ∈ π ∪ {v} : y more relevant than u};
  - Ω_ρ(c) and Ω_ρ(ρ v) share u and differ in their path sets exactly by S;
  - Ω_ρ(c) is |π| + 1 longer;
  - the ρ′-play from v is the cycle Z := v, π, which does not contain u.
  Sub-cases (i) S ≠ ∅ and (ii) S = ∅ (then u is odd, and every vertex of Z is less relevant than u) are as in the packet. □
- This is REFEREE-2's repair (split by the path to the cycle node), written out. REFEREE-2's data: 0 violations of the statement in 65,486
  one-player and 647,486 run checks.

## H2 (N-GAP-1): the standing premise, named
XW uses RESULTS R57 (a) (VJ): σ̄ is the pointwise minimum over Odd's replies. W-MON, FB-W, and the uses of OPT-OFF in W-SUCC and LATE-W use the
standing SPEC premise of RESULTS R57 (1E-N3; as in R88, R89 FR-N1 and P-N5-CUT): S1's procedure realises the pointwise optimum. For S4a this
means σ_new is the pointwise optimum of the one-player arena H_t, realised by plays. Read §1's [S4a] and §2.2-§2.5 with this premise named.
The code link G-N5T-1 is used by no proof.

## H3 (N-GAP-2): OPT-OFF Case 1 wording
«Both plays avoid v» → «both paths to the cycle node avoid v» ([V1]). When v lies on its own cycle, ρv's play returns to v, but [V1] gives
the path condition that [V2] needs. Folded into H1's (1a).

## H4 (N-GAP-3): LATE-PIECE's CL, window fixed
In §3.2, read CL_Q(v, c) as: the re-blocked late adoptions u → u + 1 (other than the first) whose window [s + 1, t′] contains some state at
which v is its own W-cycle node. Here s → s + 1 is the latest leave of c by v with s + 1 ≤ u, and t′ := the EARLIEST state of [s + 1, u] at
which (v, c) is blocked. The proof is unchanged: it works for any fixed choice of t′, and the count depends on the choice.

## H5 (N-GAP-4): §5's bullet overstated
§5's bullet «CONJECTURE FB-LIN (≤ n in-phase fallbacks per phase) and any polynomial form of it follow from …» is too strong for FB-LIN
itself. Read: polynomial bounds per phase on Σ_v WCH^S4a_P(v) and ZF_P give a POLYNOMIAL form of FB-LIN. FB-LIN itself (≤ n) would need,
for example, RO_P + ZF_P ≤ n − |Z_a|. Theorem GAP-RED and the RESULTS line are unaffected: the line never claimed FB-LIN.

## H6 (N-GAP-5): "Z-FLAT" lists consequences
Lemma Z-FLAT (§4.3) states consequences of Z_{k+1} = Z_k, not a characterisation (it has no converse). Read its title as "Lemma Z-FLAT
(consequences)". box 68's note calls it a characterisation; that word is withdrawn there too, as a READING.

## H7 (N-GAP-6): relation to P-N5-CUT
P-N5-GAP's OPT-OFF is P-N5-CUT's OPT-OFF (ii) in general one-player form. CUT's three-case proof is complete; GAP's two-case proof needed
H1's split. The Lead may route one shared statement and proof for both packets. Nothing here depends on CUT's file.

## H8 (N-GAP-7): DATA, an invalid start file
- §6's DATA ran experiments/red/n3/instances/comp54_n80 with its start file (via experiments/si/root/logs/alt_all.lst). That start file sets
  τ(11) = 51, but vertex 11 is Odd with the single successor 11: a NON-EDGE. That run is not an N5 run.
- The file is L-RED's (red/), so I do not edit it. It is QUARANTINED in my tree: experiments/new/box67/energy.py and box68/zflat.py now
  reject a start pair with a non-edge («INVALID-START comp54_n80.pg non-edges [(11, 51)]», exit 2).
- Corrected counts, with comp54 removed (they match REFEREE-2's):
  - box 68 / §6: 782 in-phase fallbacks (was 788); 8,442 re-openings (was 8,532), all with a W-rise; ZF 56, GAP-MON 0, SW-IN 0: unchanged.
  - box 67 (alt_all only): 725 in-phase fallbacks (was 731). FBUP becomes E1 532, E2 408, E3 56, E4 679, E5 55, E6 298; SAUP 1207, 2930,
    2424, 469, 2413, 1102. The DEAD verdicts and lend9_n8 are unchanged.
  - box 70: comp54 had no S or C re-entry; S 42, C 4 and S-not-GXC 0 are unchanged.
- Trap noted (the same one as P-N5-CORE successor 19's trap 1): validate start files before trusting a run.

## H9: the corrected RESULTS line
docs/new/P-N5-GAP-box69-line-H9.txt (sha1 28b7e5506a5419181c9bca8b316694c3cd21ccb3) is the proposal f1c5c5d5 with exactly two changes.
`git diff --no-index --word-diff` shows only these:
- (i) N-GAP-1: «N5 on EVERY game (SPEC S1-S5; » → «N5 on EVERY game (SPEC S1-S5, under the standing SPEC premise of RESULTS R57 (1E-N3: S1's
  procedure realises the pointwise optimum; for S4a, σ_new is the pointwise optimum of the one-player arena H_t); ».
- (ii) N-GAP-3: CL's gloss «CL_Q(v, c) those whose leave-to-block window has v as its own W-cycle node» → «CL_Q(v, c) those, other than the
  first, whose window [s + 1, t′] — u → u + 1 the adoption, s → s + 1 the latest leave of c by v with s + 1 ≤ u, t′ the earliest state of
  [s + 1, u] at which (v, c) is blocked — contains some state at which v is its own W-cycle node».
- Checked against §3.2 (with H4) and §1-§2 (with H2). Nothing else changes; the scope tail is unchanged.

## DONE / FINDINGS / NEEDS
- DONE: this file; P-N5-GAP-box69-line-H9.txt; start validation in box67/energy.py and box68/zflat.py.
- FINDINGS: G-GAP-1 repaired (H1); 7 notes answered; DATA corrected for comp54's invalid start (H8); one corrected line (H9).
- NEEDS: none from the owner.

## Answers to REFEREE 19 (docs/referee/R-N5-GAP.md at claude/referee cd1c29d6), appended 2026-10-30 ~02:20Z (date -u)
## H10 (G-GAP-1 / GAP-R1): which repair, checked against both texts
- H1 uses REFEREE-2's split (by the ρ-PATH from c to its cycle node). REFEREE 19's GAP-R1 splits the packet's Case 2 into (2a) u ∉ π (the
  packet's text) and (2b) u ∈ π.
- They coincide.
  - (2b) u ∈ π means that c's play reaches u before v. So c's path to its cycle node avoids v, and v lies on u's cycle: H1's (1b).
  - (2a) is H1's Case 2.
  - REFEREE 19's (2b)(i) (S′ ≠ ∅: max S′ is Z's top) is H1's (1b) with S ≠ ∅ (S′ = S, the vertices of c's path to u above u).
  - REFEREE 19's (2b)(ii) (S′ = ∅: Ω_ρ′(v) = (u, ∅, 1 + ℓ_c) = v ⊕ Ω_ρ(c), Ω_ρ(v) = v ⊕ Ω_ρ(ρ v), ⊕ preserves the strict order) is H1's (1b)
    with S = ∅, word for word up to notation (ℓ_c = |c's path to u|).
- Per REFEREE 19's note, "Ω_ρ(c) is |π| + 1 longer" is dropped for (2b) = (1b). H1 states it only in Case 2 = (2a).
- Both referees' data: 0 violations of the statement (REFEREE 19: 436,677 pairs, 11,948 in (2b); REFEREE-2: 65,486 + 647,486 checks).
## H11 (GAP-N1): standing premise
As H2, with REFEREE 19's wording: XW, FB-W and W-MON rest on S1's procedure returning a pointwise optimum that realises Ξ (RESULTS R57 (a)
(VJ), R17 (a) (F1)). The packet named [F1] and R21 (a) but not R57 (a); read §2.1-§2.3 with R57 (a) added. DATA rests on G-N5T-1 (code = SPEC).
## H12 (GAP-N2): [V2] across two strategy pairs
SW-IN (§4.2) applies [V2] to Ξ_k(σ_k v) and Ξ_{k+1}(w), the values of two DIFFERENT strategy pairs (states k and k + 1). Sentence to add:
[V2] is a statement about triples. For any triples a ⊴ b (strictly a ◁ b) with v ∉ P(a), P(b) and v the cycle node of neither, v ⊕ a ⊴ v ⊕ b
(strictly ◁). The same term is added to both signed weights and 1 to both lengths. Which plays produced a and b does not matter. The path
condition ([V1] at k for σ_k v, at k + 1 for w) supplies "v ∉ P" and "v not the cycle node". The same reading covers SIL-Z-type uses.
## H13 (GAP-N3): Z-FLAT lists consequences
= H6 (REFEREE-2's N-GAP-5). Title read as "Lemma Z-FLAT (consequences)"; item (d) is the definition Z_{k+1} = Z_k.
## H14 (GAP-L1..L3): the COMPLETE corrected RESULTS line
- docs/new/P-N5-GAP-box69-line-H14.txt, sha1 a9e8bcae1d6caec7cded179ead78f1cfedf756f9. It is H9's line (28b7e550…) plus exactly these
  additions (`git diff --no-index --word-diff=porcelain` shows only them):
  - GAP-L3 and GAP-L1, after the standing-premise clause: «premises RESULTS R15 (a), (d), R17 (a) (F1) with R57 (a) (VJ), R21 (a), R38 (a), R88;
    Ξ_t := Ξ_{σ_t} (SPEC S1); »
  - GAP-L2, in the OPT-OFF clause: «an optimal strategy ρ of a one-player game has» → «for a one-player game of Even (Odd fixed), a
    pointwise-optimal Even strategy ρ (R17 (a) (F1)) with Ω_ρ its [S1-val] valuation has».
- Relative to the proposal f1c5c5d5, the H14 line carries H9 (i) (R57 standing premise), H9 (ii) (CL's fixed window) and GAP-L1..L3.
- REFEREE 19 remarks that the proposal's CL omits "other than the first", a superset with the bound still true. H9 restores the packet's
  "other than the first". Either reading is a true statement; H14 keeps the packet's.
- Checked word by word against the packet §1-§5 with H1-H13. The scope tail is unchanged. This is the line to land, superseding H9's.
## H15: DATA and the comp54 start file (summary for the Lead)
= H8. Corrected counts 782 in-phase fallbacks and 8,442 re-openings (box 68 / packet §6; matches REFEREE-2), box 67 725 fallbacks.
comp54_n80.start (L-RED's file, τ(11) = 51 a non-edge) is NOT edited. It is quarantined in L-NEW's tools (box67/energy.py, box68/zflat.py
refuse non-edge starts).
