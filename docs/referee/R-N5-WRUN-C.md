# R-N5-WRUN-C: REFEREE §C on P-N5-WRUN: cross-map against REFEREE-2 (R2-N5-WRUN, claude/referee-2 a281189a) and the joint gap map
Referee: REFEREE (successor 20), Opus 5.5 (D15).
- The Lead gave the §C word at 17:24Z (read 17:32Z by date -u). I opened docs/referee-2/R2-N5-WRUN.md @ a281189a (176 lines) only after that
  word, and after my report R-N5-WRUN.md (8c0b2e69, Addendum 1 a3aa5b68) was pushed.
- REFEREE-2 reviewed line revision L-1 (l-new 02a12a10, sha1 d92521f7…), which already carries my first-report items. I word-diffed L-1
  against the frozen line 0faa5b80 here (§3).

## 1. Cross-map
| item | REFEREE (R-N5-WRUN) | REFEREE-2 (R2-N5-WRUN) | joint reading |
| --- | --- | --- | --- |
| XI-RUN, WRUN-EQ E1-E13 | SIGNED | SIGNED | agree. Both: E10 vacuous (BIP-REL-1 DEAD). REFEREE-2 reproduced the kill (rel2_R2_n82); I did not |
| WAIT-CYCLE′, DEAD-CYCLE, CHARGE | SIGNED (for the §4.1 definition) | SIGNED | agree. Both re-derived Claim A, Cases 1-3, and the final ρ′ step |
| E0-BOUND, TRIPLE-RED, RET-ΞRISE, FREE-RED | SIGNED | SIGNED | agree |
| GAP-DEV, ΞCH-PCH, RSTAR-PCH | SIGNED | SIGNED | agree (same arithmetic n² − 1 + n·PCH) |
| LEX-SIGN, PREFIX-MON, LEVEL-RED | SIGNED | SIGNED | agree (same three cases at the top differing rank) |
| BIP, BIP-MON, NO-DEV (corrected) | SIGNED; correction right | SIGNED; N-3 correction accurate | agree. REFEREE-2 adds that at an FL transition all switched vertices keep Ξ and are own cycle nodes (SW-KEEP): consistent |
| BIP-RED | SIGNED | SIGNED | agree; unconditional, since [SUB] is signed by both |
| [SUB] | SIGNED independently (§9.1, before opening SUB-check.md) | author (a11c2868) | two signatures |
| REL2-WRISE | SIGNED; N2: = landed R91 LATE-W | SIGNED; the L-1 parenthesis «a special case of R91 LATE-W» is correct (q2 ≥ s + 2) | agree. REFEREE-2's q2 ≥ s + 2 remark makes LATE-W's «later state» explicit |
| INT-XCH⁰; FL-INT inside E7 | SIGNED | SIGNED | agree |
| Fact EXT | WRUN-N1: needs y in neither path set | N-1: FALSE as worded, instance x = (c, {y}, ℓ), x′ = (c, ∅, ℓ) | same finding. REFEREE-2's instance is the clean form; every use satisfies the hypothesis |
| [P-INT] scope (E7 ⇒) | WRUN-N3 | (reviewed L-1, where it is fixed) | applied in L-1 («of every W-run») |
| R3-POLY undefined in the packet body | not raised | N-2 | agree; packet erratum (the line defines it) |
| line: block definition (WAIT-CYCLE′ FALSE as worded in 0faa5b80; n-4 instance) | G-WRUN-1 | (reviewed L-1, where it is fixed) | closed by L-1 (§3) |
| line: k free in LEVEL-RED | WRUN-L1 | (fixed in L-1) | closed by L-1 |
| line: term order unbound | WRUN-L2 | (fixed in L-1; REFEREE-2 checked the six comparisons) | closed by L-1 |
| line: «one-way» wording | WRUN-N4 | (fixed in L-1) | closed |
| line: «strict release» unbound in REL2-WRISE | I called it «acceptable» (defined only implicitly by R°_Φ) | L-1 REQUIRED | I agree with REFEREE-2: the term is used as a hypothesis and never defined in the line. My leniency was the miss. REQUIRED for L-2 |
| line: τ unbound in GAP-DEV «σ̄_q(o) ≠ τ(o)» and BIP-MON «val(σ_t, τ)» | MISSED | L-2 (precision) | agree; τ_q / the W-run's τ. I make it required for consistency with FIXD L-3 (τ → τ_t) |
| line: «[P-INT] := for a polynomial p, …» | MISSED | L-3 (precision) | agree: «there is a polynomial p such that …» |
| line: RSTAR-PCH Σ_{(y, z)} over Even edges | MISSED | L-4 | agree |
| line: REG = not E0, explicit | not raised | L-5 | agree (precision) |
| DATA | n ≤ 100 run set + 3 large pins, 0 violations; pins match; NO-DEV max 55 | full corpus 1132 runs, 0 violations; REG / E0 / FREE = 1,005 / 0 / 5,260 (= packet); NO-DEV max 58 (topfix_n10, n > 100); WAIT 286k blocks | consistent. The differences come from run sets: my MAXN 100 skipped 73 games, topfix_n10 among them |

## 2. Joint gap map
- Packet items to sign (§3-§11): EMPTY on both sides. Nothing FALSE.
- Packet errata (not signed items): Fact EXT's hypothesis (REFEREE WRUN-N1 = REFEREE-2 N-1); R3-POLY's definition in the body (N-2); [P-INT]
  scope at l. 108 (WRUN-N3); E10 vacuous (BIP-REL-1 DEAD).
- Line:
  - G-WRUN-1, WRUN-L1, WRUN-L2 and WRUN-N4 are closed by L-1.
  - Required for L-2: REFEREE-2's L-1 («strict release» unbound) and L-2 (τ in GAP-DEV and BIP-MON).
  - Precision: L-3 ([P-INT] quantifier), L-4 (Even edges), L-5 (REG explicit).

## 3. L-1 (02a12a10, sha1 d92521f7c7ffa28e0ebafeb1f8aeca3d3258b82f) against my notes
- Word-diff against 0faa5b80. The changed tokens:
  - label «revision L-1»;
  - R91 premises plus «LATE-W»;
  - the block «a self-routed block of (X, g) at state t: … improving, g ≠ σ_t(X), … its vertices before X (the route) pairwise distinct and,
    when X lies on the cycle of its own (σ_t, σ̄_t)-play, avoiding that cycle» (G-WRUN-1);
  - «and, for every k ≥ 1,» for DEEP (WRUN-L1);
  - [P-INT] «for a polynomial p, … of every W-run» (WRUN-N3; REFEREE-2 L-3 asks for «there is»);
  - PREFIX-MON: «for every k ≥ 1: while the cycle node of Ξ(v) is fixed», the terms «in decreasing rank, each … ordered by (r, +) above
    (r′, +) iff r > r′, every (r, +) above NONE above every (r′, −), and (r, −) below (r′, −) iff r > r′» (WRUN-L1, WRUN-L2; it matches §7.2);
  - REL2-WRISE «(a special case of RESULTS R91 Lemma LATE-W, which needs neither (A2) nor the frozen stretch)» (WRUN-N2);
  - «proved in one direction only» (WRUN-N4);
  - «CONJECTURE BIP-REL-1 is DEAD (L-RED R143, rel2_R2_n82, l-red 717f407a)» (Addendum 1).
- G-WRUN-1 check: my instance wc_line_cex.pg is excluded by «g ≠ σ_t(X)» (there g = σ_0(X)), and also by the cycle-avoidance clause. With
  the L-1 definition my probe's MUT 0 finds 0 recurrences.
- Verdict on L-1: every item of mine is applied correctly, and nothing else changed. L-1 does NOT yet match, only because of REFEREE-2's
  required L-1 and L-2 (§2). I will word-diff L-2 when it is frozen.

## 4. Line revision L-2 (l-new 85c12579, docs/new/P-N5-WRUN-box92-line-L2.txt, sha1 8ab101e5c8b38caf504d64237034534b0fd0afd1; fixes sha1 a14403f28c5322cc75f8dc96b615b814c56a9a64)
- Word-diff against L-1 (d92521f7). The changed tokens are exactly REFEREE-2's L-1 to L-5:
  - «(that is, not E0)» and «REG (not E0)» (L-5);
  - «there is a polynomial p such that» (L-3);
  - «at a state q of a W-run», «τ_q(o)» (L-2);
  - «(y, z) Even edge» (L-4);
  - «on a frozen stretch of a W-run with σ̄ ≡ ρ and τ_t ≡ τ (the W-run's Odd strategy)» (L-2);
  - «if (y, z) is adopted at a transition of a frozen stretch Φ at which it had been blocked at an earlier state of Φ (a strict release),
    … in Φ» (L-1).
  Each is correct against the packet. Nothing else changed.
- Strict symbol test, second pass clause by clause («is every quantifier's range the packet's?»). This finds two binding defects that were
  already present in 0faa5b80 and L-1. REFEREE-2 (on L-1) and I (on 0faa5b80) both passed them. Both are REQUIRED.
  - WRUN-L3 (REQUIRED): F and the vertices are unquantified in six clauses. The parenthesis defines quantities «for a W-run F», but these
    clauses use F (and X, g, z, v) with no quantifier:
    - «E0_F(X, g) ≤ n, and |F| ≤ m_E + Σ RET_F ≤ …» (TRIPLE-RED);
    - «RET_F(X, g) ≤ ΞCH_F(g) and FREE_F(X, g) ≤ RET_F(X, g) ≤ |F| ≤ …» (RET-ΞRISE, FREE-RED);
    - «ΞCH_F(z) ≤ n(n + 1 + PCH_F(z)) and R*_F ≤ …» (ΞCH-PCH, RSTAR-PCH). Here z is bound only as «a target z of an edge blocked at a state
      q» from GAP-DEV's half, which would wrongly restrict ΞCH-PCH to blocked targets. The packet's §6.2 holds «for every W-run F and
      vertex z»;
    - «while the cycle node of Ξ(v) is fixed … PCH_F(v) ≤ n(2n + 1)^k + DEEP_{k,F}(v)» (PREFIX-MON, LEVEL-RED: v, F and t);
    - «if Ξ_t = W_t at every state of F then …» (NO-DEV);
    - «|F| ≤ SB_F + …» (BIP-RED).
    Fix: one global binder before the claims, e.g. «… ): for every N5 run, every W-run F = [a, b] of it, every Even edge (X, g) and all
    vertices v, z: (Theorem XI-RUN) …». Alternatively put «every W-run F has» / «for every vertex z» into each of the six clauses, as
    XI-RUN's clause already does («every W-run F has …»). This is the K12 pattern («F unbound»).
  - WRUN-L4 (REQUIRED): τ in (A2). REL2-WRISE's «(A2) the τ-play from z under σ_{s+1} with y → z avoiding y»: τ is bound only inside the
    BIP-MON clause («τ_t ≡ τ (the W-run's Odd strategy)»), which is another clause. Fix: «the τ_{s+1}-play» or «the (σ_{s+1}[y → z], τ_s)-play
    from z avoiding y». This is the same kind of item as REFEREE-2's L-2, which L-2 applied to GAP-DEV and BIP-MON.
- Optional: «(Theorem BIP-RED, an implication from [SUB])» may now drop the condition, since [SUB] carries two referee signatures. As an
  implication it is still true.
- Content: unchanged against the packet's §3-§11. The ⇔ chain is E1-E8, the one-direction list is E9 and E13, and BIP-REL-1 is DEAD.
- Verdict on L-2: REQUIRED CHANGES, WRUN-L3 and WRUN-L4 (Opus 5.5, D15). Everything else MATCHES.

## DONE / FINDINGS / NEEDS
- DONE: this §C.
- FINDINGS:
  1. WRUN: both referees SIGN every packet item; the joint gap map for the packet is empty.
  2. Line: my items are closed by L-1. REFEREE-2's «strict release» unbound and τ unbound are required for L-2; I missed both.
  3. Fact EXT: one finding, two forms (N1 / N-1).
- NEEDS: Lead: L-3 with WRUN-L3 (global W-run / vertex binder) and WRUN-L4 (τ in (A2)); I word-diff it. REFEREE-2 should
  re-check WRUN-L3, which both of us passed earlier.
