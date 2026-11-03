# P-N5-REALIZE fixes (append-only; the frozen packet 067f06b6 and line 53dd6e9f are never edited)
L-RED. Each entry quotes the referee item, gives the reply and says where the change lands (packet reading here; line text in a
revision file P-N5-REALIZE-line-L<k>.txt). Where an entry and the frozen packet differ, the entry governs.

## Entry 1 (2026-11-02, L-RED successor 45): REFEREE 22 (docs/referee/R-N5-REALIZE.md, claude/referee 05b865e0) and REFEREE-2 26
(docs/referee-2/R2-N5-REALIZE.md, claude/referee-2 bcd43b5a); one revision, line L-1 (docs/red/P-N5-REALIZE-line-L1.txt)
Verdicts: both referees SIGN every to-sign item; no gap in the mathematics. Both used the label «REAL-L1»; here they are named by referee.

### REFEREE 22 items
- REFEREE REAL-L1 (REQUIRED, line). «The line's description of Γ(G) gives priorities and edges but no vertex INDICES … KEY (b) equates them
  with the IDEAL keys only because e-vertices are indexed in gate-index order.» ACCEPTED. The packet has the order (§3.1: «e_g: indices
  N + 2M, … allocated in GATE-INDEX order»); the line lacked it. Line revision L-1 adds the full index layout of §3.1 («movers, gates in
  gate-index order, β-vertices, e-vertices in the order of their gates' gate indices, the unused loop, c_W, K0 to K3 (packet §3.1), on
  which the root-first key comparison depends») and defines top («the least even number at least 2 above every other priority so far»,
  REFEREE 22's optional note). L-1 carries it.
- REFEREE REAL-P1 (optional). «with bridge B is redundant here … The citation of R24 (a) Lemma R + TB steps 1, 3-5 is NOT redundant: it gives
  σ_new(x) is the κ-least element of TIE(x), which no lemma of the packet proves.» ACCEPTED, as a correction of the packet's wording.
  §1 [RULE] («so this packet uses Lemma W (iii), not bridge B's FL hypothesis») and §8 last bullet («bridge B … is not needed in the
  proof») read: Lemma W (iii) supplies bridge B's conclusion (every arena option of a mover is fully W′-optimal), so the bridge-B part
  of the citation is redundant here; the citation of RESULTS R24 (a) Lemma R and R24 (b)'s choice rule (TB proof steps 1, 3-5) is
  ESSENTIAL: it is the only source of «σ_new(x) is the κ-least element of TIE(x)» used in §4 (movers). The line keeps the CF-1 citing
  line unchanged.
- REAL-P2 (optional; REFEREE REAL-P2 and REFEREE-2 P-2). «for L(G) = 0 there is no FL transition, so [0, L] is one FL run should read no FL run.» ACCEPTED. §4 Theorem
  REALIZE and §5 read: if L(G) ≥ 1, [0, L(G)] is one FL run of length L(G); if L(G) = 0, transition 1 is a fallback and there is no FL
  run (the corollary is unaffected: L(G) = 0 needs no bound). Line L-1 says so.
- REFEREE REAL-P3 (optional). «L(G)'s finiteness … Say so in one clause.» ACCEPTED. §2 reads: L(G) is finite because the induction of §4
  realises every IDEAL step that exists as an N5 transition from (σ_0, τ_0), so an infinite IDEAL run would give an infinite N5 run,
  which RESULTS R15 (termination) excludes; this is not circular, since the induction does not assume finiteness.

### REFEREE-2 26 items
- REFEREE-2 REAL-L1 (REQUIRED, line). «The 1E-N3 gloss … is narrower than the proof's use (G-REAL-1). Quote R57 (b) as R102's line does
  … or name both forms.» ACCEPTED. L-1 quotes R57 (b) as R102's landed line does («that S1's procedure realises an optimal σ̄ is VJ00 §6
  plus SPEC conformance», read on every valid input, L45 / R102) and names both forms: P1 (S1's σ̄, and τ̄ on the dual game, are
  pointwise optima) and P2 (S4a's σ_new, S1's output on the dual of its arena, is a pointwise optimum of that arena, before S4c).
- REFEREE-2 REAL-L2 (REQUIRED, line). «compared by the β of largest rank in the symmetric difference and its parity does not say which
  way.» ACCEPTED. L-1: «the option whose set contains that β is the better one if its parity is even and the worse one if odd» (packet
  §2 Fact X; Ω parity = bp).
- G-REAL-1 (minor, CLOSED by landed results; no new proof). «§1 says Premises (named; nothing else is used) and restates [1E-N3] as …
  form P2, restricted to σ_j at non-fallback transitions. The proof uses more»: (a) P1 in SBAR (ii)/(iii), TAU, K (c); (b) P2 and
  [RULE] applied to S4a's σ_new before S4c. ACCEPTED as a correction of §1's wording only. §1 reads: [1E-N3] is RESULTS R57 (b) on every
  valid input (L45, R102), in both forms (P1) S1's σ̄, and τ̄ on G^d, are pointwise optima, and (P2) S4a's σ_new, S1's output on
  dual(H), is a pointwise optimum of H at every transition with Iσ ≠ ∅, before S4c; [RULE]'s «σ_j(x)» reads «σ_new(x) (= σ_j(x) at a
  non-fallback transition)», the (R1) reading landed in RESULTS R103 (TB steps 1, 3-5 describe one S1 call on dual(H)). «Nothing else
  is used» holds with this reading. REFEREE-2 §3 also closes (b) directly from SPEC S4a's text; no change to any lemma.
- REFEREE-2 P-1 (optional, line). ACCEPTED: L-1's start reads «β → its Ξ-target (u when the target is X)».
- REFEREE-2 P-2 (optional, line): with REFEREE REAL-P2 above.
- REFEREE-2 N-2 (note). §7's «L / n ≈ 0.2-0.26» reads 0.177 (big_d3, n 96) to 0.260 (grow_top_N24, n 246), DATA on the 7 champions.
- REFEREE-2 N-1 (note): Lemma TAU and K (c) use no acyclicity; §6's list is right to omit them. Noted.

### Line L-1 (docs/red/P-N5-REALIZE-line-L1.txt): the changes against 53dd6e9f, nothing else
1. 1E-N3 gloss replaced by R57 (b) as quoted in R102's line, with both forms P1, P2 (REFEREE-2 REAL-L1).
2. IDEAL comparison direction stated (REFEREE-2 REAL-L2).
3. c_W's priority «top» defined; vertex-index layout of §3.1 added, e-vertices in the order of their gates' gate indices (REFEREE REAL-L1).
4. Start: «β → its Ξ-target (u when the target is X)» (REFEREE-2 P-1).
5. «so, if L(G) ≥ 1, [0, L(G)] is one FL run … (no FL run if L(G) = 0)» (REAL-P2, both).
6. Date tag «(2026-11-02; revision L-1 2026-11-02)».

## Entry 2 (2026-11-02, L-RED successor 45): REFEREE-2 Addendum 1 (docs/referee-2/R2-N5-REALIZE.md, claude/referee-2 a2070483)
- REFEREE-2 agrees with REFEREE 22 on every verdict and now also REQUIRES REFEREE REAL-L1 (e-index order), with a failing instance (as
  relayed by the Lead 05:31Z): Γ(G) built as the frozen line describes it but with e-indices in REVERSED gate order, on big_d4_k3_W3
  and grow_top_N24, makes the real N5 run leave the IDEAL run (IDEAL 20, KEYB 33, first at state 0, mover x = 2). So REAL-L1 is
  substantive, not cosmetic: Lemma KEY (b) needs the gate-index order of e-indices (packet §3.1). Line L-1 (1d72ee31) already carries it;
  no further line change.
- Joint REQUIRED list, all in L-1: REFEREE REAL-L1, REFEREE-2 REAL-L1, REFEREE-2 REAL-L2 (entry 1). Optional items as in entry 1.

## Entry 3 (2026-11-02, L-RED successor 45): CHECKER C115 (docs/checker/C115.md, claude/checker fbca67cf), line L-2
- E-1 (REQUIRED). «L-1 cites VJ00 Lemma 5.8 «1 ⇒ 2» as «the direction that holds»; RESULTS records it as resting on unproved lemmas»
  (R15 (iii): 5.8 «1 ⇒ 2» «uses VJ00's unproved Lemma 5.9 and Prop. 5.10»; R36 (d): R36 (c) «does NOT discharge the two-player VJ00
  Lemma 5.8»; R57 routes around 5.8). ACCEPTED; my citation was wrong (the R15 side finding concerns the OTHER direction only).
  - [VJ-LOC] (packet §1) is restated: RESULTS R36 (c) Lemma P1 («if σ is a positional Even strategy of a one-player game H with no
    improving edge (no Even edge (x, y) with V_σ(y) ▷ V_σ(σ(x))), then V_σ(v) ⊵ V_σ′(v) for every positional Even strategy σ′ and every
    vertex v»), applied on G^d to Odd's one-player game Γ_σ (Even's choices fixed to σ; Odd = the Even player of G^d).
  - Orientation (Fact DUAL): G^d's order is the reverse of Γ's, so «no Odd-improving edge in Γ's order» (SBAR (i): no Odd v, w with
    φ(w) ◁ φ(ρ(v))) is «no improving edge of the G^d-Even strategy ρ», and P1's conclusion «V_ρ ⊵_(G^d) V_ρ′» is «φ_(σ,ρ) ⊴ φ_(σ,ρ′) in
    Γ's order for every ρ′», i.e. ρ is Odd's pointwise optimum against σ. With [1E-N3] P1 (S1's σ̄ is a pointwise optimum), φ = Ξσ
    follows as in SBAR (ii); SBAR (iii) is unchanged.
  - VJ00's two-player Lemma 5.8 is NOT used anywhere in the packet. No other lemma used [VJ-LOC] (K (d), ESC, TAU use only the
    definition of a pointwise optimum / [1E-N3]; REFEREE-2 §1).
- Notes folded into L-2 (CHECKER, all wording): G-1 bare date «(2026-11-02)» and the source note «docs/red/P-N5-REALIZE.md with its
  fixes entries 1-3, docs/red/P-N5-REALIZE-fixes.md»; G-3 «RESULTS R103's bridge B» and «non-movers included (RESULTS R103's (R1)
  ruling)»; G-2 «a Ξ-target xt(x, k), a mover or the exit X»; G-7 «random Ξ-cyclic genomes do mismatch» moved after «DATA:»; G-10 «L-RED
  R178 champions», «L-RED R188 genomes».
- Line L-2 (docs/red/P-N5-REALIZE-line-L2.txt) = L-1 (1d72ee31) with exactly these changes: (1) the [VJ-LOC] parenthesis replaced by
  «local optimality in a one-player game (RESULTS R36 (c) Lemma P1, applied on the dual game to Odd's one-player game against a fixed σ;
  VJ00's two-player Lemma 5.8 is not used)» (E-1); (2) G-3 (two places); (3) G-2; (4) G-1 (date, source note); (5) G-7; (6) G-10.
  The frozen packet, the frozen line and L-1 are not edited.
