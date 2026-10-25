# Referee report R-N5-LP: the used-level freeze and a carry bound for a phase of N5 (box 32)

Referee: REFEREE (successor 5), Opus 5.5 (owner ruling D15, Lead reading L37). Packet P-N5-LP: the Lead's message of 2026-10-25 00:47Z.
Pin: trunk claude/vibrant-johnson-nxvvxo bc42f2c (my HEAD after a merge of trunk). Object: docs/new/P-N5-LP-box32.md, sha1
d2c8121a0089add13c9417080cfb57620f592c88, 202 lines (verified at the pin). L-NEW successor 12.
Context: SPEC S2, S4a-c, FIX 2; RESULTS R15, R17, R19, R24 (incl. G-TB-1), R25 (my R-N5-FB, §C); my predecessor's R-N5T (the VJ00 Lemma
5.8 "2 ⇒ 3" gap). VJ00 opened myself: §5.5 Lemma 5.8 and its proof (pdf pp. 20-22; report pp. 19-21), Lemma 5.2 (p. 15), (11) (p. 16).
docs/referee-2/ was NOT read for this packet. Written 2026-10-25 00:51Z onward by date -u. Every verdict is labelled (Opus 5.5, D15).

## Verdict
| statement | packet label | verdict (Opus 5.5, D15) |
|---|---|---|
| §1 Lemma U (used-level freeze) | PROVED | SIGNED (ENG-1 inherited: Ξ_k = Θ_{H_k}) |
| §1 Lemma HI | PROVED | SIGNED. Its Consequence: SIGNED WITH GAP HI-1 ("M_{k+1} = M_k if M_k > L_k" needs that some level-M_k gate edge sits at a vertex other than a SWITCHED own cycle node; "≤" holds; the Consequence is not used later) |
| §1 Lemma UL | PROVED | SIGNED |
| §1 Lemma GR (a), (b) | PROVED | SIGNED |
| §1 Lemma NU | PROVED | SIGNED |
| §2 Theorem LP (both inequalities) | PROVED | SIGNED |
| §3 Lemma DF | PROVED | **NOT SIGNED: FALSE as stated.** Counterexample docs/referee/R-N5-LP/df_cex.pg (n 11). The failing step is "a maximum has no improvement" (VJ00 Lemma 5.8, 2 ⇒ 3 ⇒ 1), the direction whose gap R-N5T recorded: at an OWN W-cycle node a length-only improvement survives. Restricted form DF′ (y not its own W-cycle node at k+1): SIGNED (§3.2) |
| §3 Lemma BAND | PROVED | SIGNED |
| §3 Lemma WAKE | PROVED | SIGNED WITH GAP W-1: it cites DF; DF′ suffices, because a relevant y in F is not its own W-cycle node (R19 (a)), and for y ∈ R the claim a ∈ R is immediate. CLOSED |
| §4 Corollary LP′ | PROVED | SIGNED (its proof uses wakes only through their definition; the closing remark uses WAKE, which holds via W-1) |
| §5 NO-WAKE FALSE, (KW-M) FALSE; S_o, X, K OPEN | — | not signed (as briefed); nowake_cex_n32 re-run: n5.py 9 / 2, Oink zlk OK, strategies verified |

## 0. Pseudocode against the SPEC
- Used: S2 gate; S4a = one Engine.evaluate on the dual arena (R17 (F1)); S4c fallback (every phase transition changes σ: τ is constant,
  and if S4a/S4b change nothing S4c switches ≥ 1 vertex); FIX 2 (DFS choice at a cycle node). R15 (d) covers S4a and S4c switches.
  PHASE here = λ_Ξ and τ constant (the packet's definition; R25's FB uses only these two, R-N5-FB §C). Correct.
- The relevant-change definition excludes own cycle nodes (Even or Odd). This is exactly what makes Lemma U stronger than R25's TAME
  (M_k → L_k). The FIX-2 choices at own cycle nodes are the ones the DF counterexample exploits.

## 1. §1 and §2
- Lemma U. Step 1 (L_k < ∞): (P1) along H_k and H_{k+1} edges with λ constant in the phase. Correct. Steps 2-4: v's H_{k+1}-path to its
  first visit of c = λ(v); every p_i (i < s) has λ = c ≠ p_i, so a changed out-edge there is a RELEVANT change of level ≤ L_k; (P2) at k and
  k+1, (C4), downward induction from Ξ(c) = (c, ∅, 0) at both states. Correct. The Lead's concern (transfer from TAME): TAME's proof uses
  M_k only as an upper bound on the levels of the edges changed ON THE PATH, and a path before the first visit of c contains no own cycle
  node, so excluding own-cycle-node changes from L_k is sound. Verified line by line. DATA: 0 failures (below).
- Lemma HI. For y not a switched own cycle node: COARSE_L of both ends of (y, z) are unchanged (Lemma U; y's own switch has level ≤ L); a
  level > L and its direction are functions of the two COARSE_L values; the two σ(y) values have level ≤ L. Correct.
  - HI-1 (Consequence). A switched own cycle node y is outside HI. Its gate edges can change. "≤" survives: at k+1, a gate edge (y, z′)
    of level > L relative to z = σ_{k+1}(y) has COARSE_L values as at k, and Ξ_k(z) ▷ Ξ_k(σ_k y). By the ultrametric property its level
    is ≤ max(lev_k(σ_k y, z), lev_k(σ_k y, z′)) ≤ M_k, with z′ gate at k. "=" fails if the only level-M_k gate edges sit at such a y.
    The Consequence is not used by §2-§4. DATA: 0 violations in my runs.
- Lemma UL. Odd case: y ∈ P(Ξ_k(a)) puts a on an H_k-cycle through y with top rank ≥ ℓ > rank c, against (P1). Even case: Lemma U
  (COARSE_ℓ frozen) + R15 (a) keep bit ℓ in Ξ_{k+1}(z), so z lies on an H_{k+1}-cycle through y, against λ constant. Correct.
- Lemma GR. (a): COARSE_ℓ frozen; if bit ℓ moves it is the top difference, and R15 (a) makes the new value ℓ-good. (b): UL gives
  y ≠ u_ℓ; y ⊕ · keeps bit ℓ; (P2) at k and k+1 (λ(y) ≠ y); Ξ_{k+1}(z) ℓ-good by (a). Correct.
- Lemma NU. Ξ constant on an NU run (Lemma U with L = ⊥); every transition switches an Even vertex (τ fixed); at an NU transition only
  own cycle nodes switch, each to a strictly better gate target with Ξ fixed. So ≤ deg(y) − 1 switches per y, Σ ≤ m − n. Correct.
- Theorem LP. First bound: ≤ T_rel + 1 NU runs of ≤ m − n. Second: L-runs strictly decrease between rises over {−1, …, n − 1}, so there
  are ≤ (n + 1)(ρ + 1) runs. A run of value ℓ ≥ 0 adds a NEW vertex to G_ℓ at each non-ε transition (GR (b)), and G_ℓ never loses one
  (GR (a), NU transitions included): ≤ n. A run of value −1 changes only lengths, monotone per vertex: ≤ n(n − 1). Sum. Multiplied out:
  correct.

## 3. §3 on 𝒞^1O
### 3.1 Lemma DF is FALSE as stated
- Instance docs/referee/R-N5-LP/df_cex.pg, sha1 a128663eae53c471f86ea32bfafaf63c05977486, n 11, exactly one Odd vertex with out-degree
  > 1 (o = 1; Odd vertices 3, 8, 9 are forced; asserted). Found by docs/referee/scratch/lp_probe.py (random 𝒞^1O, seed 1001, smallest
  failing game). n5.py: 2 iterations / 1 fallback; check_sol2.py "zielonka(oink zlk) OK strategies verified".
- Transition 0 → 1: an S4a step (no fallback), the same phase (λ_Ξ and τ equal at 0 and 1). Arena at 0 for y = 7 (Even, Ω 9):
  {σ_0(7) = 4} ∪ Iσ_0(7) = {4, 8}. S4a keeps σ_1(7) = 4: 7 is its own cycle node, and FIX 2's DFS choice ignores lengths.
- At state 1: W_1(7) = (7, ∅, 0) (own W-cycle node); Ξ_1(8) = W_1(8) = (7, ∅, 5) and Ξ_1(4) = W_1(4) = (7, ∅, 3). 7 is odd, so a longer
  path is better: (7, 8) is a gate edge at 1. But a = σ_1(7) = 4 ∉ R_1 = {1, 9}. DF claims a ∈ R_1. FALSE.
- The next transition (1 → 2) is the S4c fallback that takes 7 → 8: the length-only improvement that the arena optimum missed.
- The failing step: "σ_{k+1} is a maximum of the arena, so by VJ00 Lemma 5.8 (2 ⇒ 3 ⇒ 1) it has no improvement, so W_{k+1}(z) ⊴ W_{k+1}(a)".
  The contrapositive used ("improvement ⇒ not a maximum") is VJ00's 2 ⇒ 3, whose proof fails at a cycle node: Prog's clause 3 ignores
  lengths (R-N5T, CONFIRMED there; I re-read VJ00's proof, p. 20 report numbering). Here σ_1 is S4a's arena optimum (R17 (F1)), and
  still (7, 8) is a W_1-improving arena edge at 7's own cycle node.
- DATA: DF fails at 96 arena edges in the 228-file library (n ≤ 64; among them the lane's own nowake_cex_n32 and L-RED's x32_rand16,
  x32_rand64, x31_nh_r20, and si/xing nofe_cyc_n8) and at 18 + 56 in random 𝒞^1O runs. Every failure has y its own W-cycle node at k+1.
### 3.2 DF′ (restricted form): SIGNED
- Statement: as DF, with y not its own W-cycle node at k+1.
- Proof: W_{k+1} is the arena optimum's valuation (R17 (F1)). y ≠ λ_W(y) gives W_{k+1}(y) = y ⊕ W_{k+1}(a) (P2). Bellman at an arena
  optimum (R24 G-TB-1 closure, (F1) only): W_{k+1}(y) ⊵ y ⊕ W_{k+1}(z), so W_{k+1}(z) ⊴ W_{k+1}(a).
  - If z's play avoids y, ⊕ y is strictly monotone.
  - If it passes y, the loop y → z → … → y has top t. An even t above the cycle node, or a top below an odd cycle node, would give Even a
    better cycle, against (F1). Otherwise W(z) ◁ W(a) directly (odd t in the path set, or a longer length at an even cycle node).
  - Then the packet's second paragraph (a ∈ F ⇒ Ξ_{k+1}(z) ⊴ W_{k+1}(z) ⊴ W_{k+1}(a) = Ξ_{k+1}(a); R19 (a), VJ00 (11)) runs verbatim.
- DATA: 11,860 + 172 + 3 + 2 edge checks with y not its own W-cycle node (library, nowake_cex_n32, random): DF′ and its first step,
  0 failures.
### 3.3 Lemma BAND: SIGNED
- (R1) on R; θ's and w's paths are disjoint from routes (H1 / λ_Ξ(o) = o; H2 / λ_W(o) = o). The Ξ-difference is (π_z Δ π_a) ∩ V_{>c_θ},
  the W-difference is (π_z Δ π_a) ∩ V_{>c_w}. If the top t has rank > rank c_w, both orders decide alike (in either relative position of
  c_θ, c_w), so W(z) ▷ W(a): excluded. t ≠ c_w (route form). Hence rank c_θ < ℓ < rank c_w and the W path sets agree. Correct.
### 3.4 Lemma WAKE: SIGNED WITH GAP W-1 (closed)
- Carrying the gate edge (y, z) from k′ back to k: across NU transitions y does not switch (it is not an own cycle node) and Ξ is fixed;
  at k Lemma HI (y is not a switched own cycle node). So (y, z) is in the arena of H_{k′−1}, and k′ − 1 → k′ is an S4a step. Correct.
- W-1: the packet then applies DF, which is false in general (§3.1). DF′ applies: y's switch is relevant, so λ_Ξ(y) ≠ y. If y ∈ F_{k′},
  then λ_W(y) = λ_Ξ(y) ≠ y (Ξ = W off R, R19 (a)), so y is not its own W-cycle node. If y ∈ R_{k′} (y ≠ o), y's play passes a, so a ∈ R
  trivially. So a ∈ R. z ∈ R (R constant on [k, k′ + 1]). Route form: y ∈ R \ {o} is not its own W-cycle node (c_w ∈ F ∪ {o}), so DF′'s
  first step gives W_{k′}(z) ⊴ W_{k′}(a), and BAND gives the U1 band. CLOSED.

## 4. Corollary LP′: SIGNED
- ε ≤ S_o (the only Odd choice vertex is o). ρ ≤ 2f + S_o + 2X + K: a fallback or crossing lies in ≤ 2 of the intervals [k, k′]; else an
  Odd-attained rise is a relevant σ̄(o) change, or k′ has a relevant Even switch of level > L_k, which is a wake by definition (no
  fallback, R constant). J ≤ S_o: by J1 a non-tame transition changes σ̄(o) above M_k; if λ(o) = o that change is not relevant, so
  L_k ≤ M_k (Even switches are gate edges, R15 (d)) and Lemma U makes the transition tame; so it is a relevant σ̄(o) change. FB (R25 (d))
  then gives f ≤ n_E(2n − 1)(S_o + 1) + S_o. Theorem LP. O(m·n⁵·(1 + S_o + X + K)). Multiplied out: correct.
- The closing remark ("every wake is an R-changing transition of a U1 piece or a U2/U3/U23 stretch") uses WAKE, valid via W-1.

## 5. Data (DATA, not proof; docs/referee/scratch/lp_probe.py, own code from the packet's definitions, independent of
experiments/new/box32/; trace = the n5.py loop asserted equal to n5.run; 𝒞^1O runs assert exactly one Odd vertex with out-degree > 1)
| run | games | in-phase transitions (relevant / NU) | failures |
|---|---|---|---|
| library: every experiments/**/*.pg in 𝒞^1O with n ≤ 64 | 228 | 5,482 (5,466 / 16); max ρ per phase 14 | U, HI, HI-Consequence, UL, GR (a)/(b), NU, LP (both): 0. DF: 96 (all own W-cycle node); DF′: 0 of 11,860 |
| random 𝒞^1O n 6-20 (seed 1001) / 8-24 (seed 1003) | 1,500 / 3,000 | 521 / 1,305 | all §1-§2 checks 0; DF 18 / 56 (all own W-cycle node); DF′ 0 |
| random general games n 4-12 (seed 1002) | 1,500 | 150 | §1-§2 checks 0 |
| nowake_cex_n32 (sha1 3a56e3fb…) | 1 | 6 | §1-§2 0; DF 1 (own W-cycle node), DF′ 0 of 172 |
- Honest limit: ρ is small in all data (≤ 14), and K = 0 outside the lane's climbs. Theorem LP and Corollary LP′ rest on their proofs.

## Signature
REFEREE (successor 5), Opus 5.5 (D15), 2026-10-25: Lemmas U, HI, UL, GR, NU and Theorem LP SIGNED (HI's Consequence with gap HI-1); Lemma DF
NOT SIGNED, FALSE as stated (df_cex.pg; the VJ00 Lemma 5.8 "2 ⇒ 3" gap); DF′ (y not its own W-cycle node) SIGNED; BAND SIGNED; WAKE SIGNED
WITH GAP W-1 (closed via DF′); Corollary LP′ SIGNED. Labels after two signatures (D18/L40): §1-§2 PROVED on every game in a phase, §3
(with DF′ for DF) and §4 PROVED on 𝒞^1O; DF FALSE. S_o, X, K, G-N5-TIME OPEN.

# Part 2: companion packet P-N5-SO (Lead 01:00Z; one combined review)
Object: docs/new/P-N5-SO-box32.md, sha1 deb5ee4422da3ab7389ce35e4542977927b53886, 54 lines, pinned at trunk 1ef02bb (verified; an ancestor
of my HEAD). L-NEW successor 12. Written 2026-10-25 01:02Z by date -u. docs/referee-2/ NOT read.
## Verdict (Opus 5.5, D15)
| statement | verdict |
|---|---|
| Lemma TH (Θ ≤ (n − 1) + n(X + 1) + X) | SIGNED WITH GAP SO-1 (dependency): the H1 case uses "σ̄_k(o) is a FULL Ξ_k-minimiser when λ(o) ≠ o". That is my R-N5-FB §4.2 case proof (single signature: REFEREE-2's G-FB-4 closure proved only COARSE_{−1} minimality). REFEREE-2 should check it. DATA 0 exceptions (61,968 earlier, plus every state here) |
| Lemma SO (S_o ≤ d_o(Θ + 1); at a relevant change with θ fixed the old choice leaves T) | SIGNED (same dependency SO-1 for "σ̄(o) ∈ T_k") |
| Corollary XJ | SIGNED WITH GAP XJ-1 (arithmetic): with d_o ≤ n and J ≤ S_o ≤ d_o(2n + (n + 1)X) = O(n²(1 + X)), FB gives f = O(n⁴(1 + X)), not O(n³(1 + X)). The stated T = O(m·n⁷(1 + X) + m·n⁵·K) is still correct (LP′'s factor (n + 1)n(n − 1) · f = O(n⁷(1 + X)); the K term is O(m·n³·K), so n⁵ is loose) |
## Checks
- Lemma TH. Crossing θ-changes ≤ X. ¬H1 (crossing-free): θ = (c_θ, ∅, d) (R-1, my R-N5-U23 §3), c_θ fixed in the phase, θ monotone over the
  whole phase (R15 (a)), so the ¬H1-state values of θ are monotone in d: ≤ n − 1 changes. H1: x0 := σ̄_k(o) (full minimiser, SO-1) has
  an honest play avoiding o, which is its (σ_k, τ)-play, so x0 ∈ F; if Ξ(x0) is unchanged, the minimiser chain
  Ξ_{k+1}(x1) ⊴ Ξ_{k+1}(x0) = Ξ_k(x0) ⊴ Ξ_k(x1) ⊴ Ξ_{k+1}(x1) forces θ unchanged ((P2) at o, λ(o) ≠ o). So a θ-change changes Ξ on F:
  ≤ max(0, |F| − 1) per crossing-free interval (F1°), ≤ X + 1 intervals. Correct.
- Lemma SO, the "key frozen" step (checked hardest, as asked).
  - T_k shrinks along a θ-constant run (R15 (a)).
  - σ̄_k(o) is the key-minimum of T_k: this is R24's choice rule in the evaluation of G (o is the optimiser's vertex, not its own cycle
    node), and "fully optimal" ⟺ Ξ(x) = μ (the formal o ⊕ is injective here, because an exit whose play passes o has a longer length).
  - For x ∈ T_k, x's H_k-path to c avoids o (else μ would be longer than itself). Every vertex on it has ONE successor in G_σ (on 𝒞^1O only
    o chooses), and that edge survives the restriction (R24 Lemma R; forced edges always survive). So x's BFS-tree path is this path, and
    its key is its root-first sequence.
  - If a vertex of the path switches, the first one p is Even with λ(p) = c ≠ p, and moves to a strictly better gate target
    (R15 (d)). ⊕ p is strictly monotone there: p is in neither path set, because it is not on its own path prefix. So
    Ξ_{k+1}(p) ▷ Ξ_k(p), the unchanged prefix (P2 at k+1) gives Ξ_{k+1}(x) ▷ μ, and x ∉ T_{k+1}.
  - Hence the paths, and the keys, are unchanged on T_k ∩ T_{k+1}. A switch of c itself does not touch the paths (they end before c).
    Keys of distinct exits differ.
  - So s0 ∈ T_{k+1} stays the key-minimum and σ̄_{k+1}(o) = s0. Each relevant change in a θ-run removes the current choice from T:
    ≤ d_o − 1 per run, Θ + 1 runs, ≤ Θ at θ-changes. In the longest-path mode the key is the index: trivially frozen.
  - VERDICT on the step: correct.
- Corollary XJ: S_o ≤ d_o(Θ + 1) ≤ d_o(2n + (n + 1)X) (multiplied out: (n − 1) + n + 1 = 2n; nX + X). J ≤ S_o (P-N5-LP §4 step 3,
  signed in Part 1). FB, then LP′. XJ-1 as above. The reading "(J-poly), NFB-O and the fallback count follow from (X)" is correct given SO-1.
## Data (docs/referee/scratch/so_probe.py, own code; trace = the n5.py loop asserted equal to n5.run; one Odd choice vertex asserted)
- Library (every experiments/**/*.pg in 𝒞^1O with n ≤ 64: 234 files, 257 phases with λ(o) ≠ o): σ̄(o) a full minimiser at every state, TH
  and SO bounds, "old choice leaves T" (4 relevant changes with θ fixed): 0 failures. Maxima Θ 51, S_o 49 (as the lane reports).
- Random 𝒞^1O n 8-24 (seed 1101, 3,000 runs, 907 phases): 0 failures (6 relevant changes with θ fixed; max Θ, S_o 2).
## Signature (Part 2)
REFEREE (successor 5), Opus 5.5 (D15), 2026-10-25: Lemma TH SIGNED WITH GAP SO-1 (dependency on my single-signed full-minimiser proof);
Lemma SO SIGNED (key-frozen step verified); Corollary XJ SIGNED WITH GAP XJ-1 (f = O(n⁴(1 + X))). G-N5-TIME OPEN; open cores per phase:
X and K.

## §C. Comparison with REFEREE-2 (R2-N5-LP, referee-2 4949d6c; Part 1 = P-N5-LP only)
Written 2026-10-25 01:13Z by date -u, after my report (4957b2cc, Part 2 dcb41198) was pushed and the Lead said R2-N5-LP exists (01:10Z).
No verdict differs: both NOT SIGN Lemma DF (FALSE) with independent counterexamples (mine df_cex.pg n 11, sha1 a128663e; R2's n 5, sha1
0a98e1b7; Lead re-ran both: n5 2/1, Oink OK), both sign DF′, both find the same WAKE and HI-Consequence gaps, and both sign U, UL, GR, NU,
Theorem LP, BAND and Corollary LP′.
- DF′: R2's hypothesis is "y not its own cycle node at k+1" and its proof uses R15 Lemmas A and B with (F1). Mine is "y not its own
  W-cycle node at k+1", proved via R24's G-TB-1 Bellman argument. Both suffice for WAKE: off R, Ξ = W gives λ_W(y) = λ_Ξ(y) (R19 (a)), and
  on R, a ∈ R is immediate. Equivalent where used; route either.
- N-LP-1 (R2 only): MISSED by me, ACCEPTED. Theorem LP step 4's "y ⊕ keeps order and strictness between values of one cycle node" is
  false for set-valued ⊕ in general (R24 TB-1 (b)). It holds where it is used: in a level −1 run all values involved share one path set.
  Wording.
- ENG-1 noted by both under Lemma U.
- Part 2 (P-N5-SO) is mine only; the Lead has moved its second review to my successor.

| statement | REFEREE | REFEREE-2 | joint | fixes-file line (L-NEW) |
|---|---|---|---|---|
| Lemma U | SIGNED (ENG-1) | SIGN (ENG-1) | SIGNED by both | — |
| Lemma HI / Consequence | SIGNED / HI-1 | SIGN / G-LP-2 | HI-1 = G-LP-2 | Consequence: "M_{k+1} ≤ M_k"; equality only if a level-M_k gate edge sits at a non-switched or non-own-cycle-node vertex |
| UL, GR, NU | SIGNED | SIGN | SIGNED by both | — |
| Theorem LP | SIGNED | SIGN (N-LP-1) | SIGNED by both | step 4: "here all values have one path set, so y ⊕ keeps order and strictness" |
| Lemma DF | NOT SIGNED, FALSE | NOT SIGNED, FALSE | FALSE (two counterexamples) | replace DF by DF′ ("y not its own (W-)cycle node at k+1"); drop the VJ00 Lemma 5.8 citation |
| BAND | SIGNED | SIGN | SIGNED by both | — |
| WAKE | W-1 | G-LP-1 | W-1 = G-LP-1, closed | cite DF′; one line on why its y qualifies |
| Corollary LP′ | SIGNED | SIGN | SIGNED by both | — |
