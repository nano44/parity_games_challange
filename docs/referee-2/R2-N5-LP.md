# R2-N5-LP: second-referee check of packet P-N5-LP (L-NEW box 32: the used-level freeze and a carry bound for a phase of N5). REFEREE-2 (successor 5), 2026-10-25 00:56Z (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-LP (Lead 00:47Z), pinned at trunk claude/vibrant-johnson-nxvvxo bc42f2c (an ancestor of my merged tree).
Object: docs/new/P-N5-LP-box32.md, sha1 d2c8121a0089add13c9417080cfb57620f592c88 (202 lines; checked at the pin and on my tree).
Background: RESULTS R15 (incl. its side finding on VJ00 Lemma 5.8), R17 (F1), R19 (a), R22, R24, R25 (FB, J1; my R2-N5-FB); the SPEC (S1,
S2, S4a-c, FIX 2-4). VJ00 opened by me: BRICS RS-00-48, pdf sha256 485a12de…, report pp. 14-16 and 19-21 re-read for this packet.
Independence: I have not read docs/referee/ for this packet. I did not run or import the lane's box32 scripts (lcheck.py etc.); its two
instances are inputs only.
Tools (docs/referee-2/R2-N5-LP/, own code on my R2-N5-FB/fb_check.py): lp_check.py (every statement of §1-§4), df_probe.py and df_find.py
(Lemma DF as stated), run_all.sh, totals.py, logs/, instances/df_cex.pg. 𝒞^1O probes assert exactly one Odd vertex with out-degree > 1.
Labels (D18 / L40): PROVED (L-NEW) is the packet's label. §5 (NO-WAKE, (KW-M), S_o, X, K) is not to sign. Nothing here is a running-time
bound, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §1 Lemma U | SIGN | Rests on Lemma 5.2 for SPEC's σ̄ (ENG-1 code link, as in R25) |
| §1 Lemma HI | SIGN | Its "Consequence" line is unproved as written: G-LP-2. It is not used later |
| §1 Lemma UL | SIGN | — |
| §1 Lemma GR (a), (b) | SIGN | — |
| §1 Lemma NU | SIGN | — |
| §2 Theorem LP | SIGN | N-LP-1: step 4's "y ⊕ keeps order and strictness between values of one cycle node" is false in general for set-valued ⊕ (R24 TB-1 (b)). It holds where it is used, because in a level −1 run all the values involved have one path set |
| §3 Lemma DF | **NOT SIGNED** as stated | The failing step: "By VJ00 Lemma 5.8 (2 ⇒ 3 ⇒ 1) a maximum has no improvement in its arena". That direction is FALSE at cycle nodes (RESULTS R15 side finding, signed). Counterexample: instances/df_cex.pg (n 5, sha1 0a98e1b7…; §4.2). REPAIRED form DF′ (add "y is not its own cycle node at k+1"): SIGN, with the proof in §4.3 |
| §3 Lemma BAND | SIGN | — |
| §3 Lemma WAKE | SIGN WITH GAPS | G-LP-1: it must cite DF′, not DF. Its y is relevant, hence not its own cycle node, so DF′ applies, and so does DF′ step 1 in the route-form clause (λ_W(y) = c_w ≠ y on R). CLOSED |
| §4 Corollary LP′ | SIGN | It does not use DF or WAKE (K is a count; LP, FB, J1, Lemma U are used) |
| §5 | not signed (as briefed) | NO-WAKE refutation reproduced (§6) |
| VJ00 citations by page | correct pages; one cited statement false | Prog p. 14-15 (the definition is on p. 15), Lemma 5.2 p. 15, (11) p. 16, Lemma 5.8 p. 19-21 (statement p. 19, proof pp. 20-21). Its direction 2 ⇒ 3 ⇒ 1 fails at cycle nodes (§4.1) |

## 1. Pseudocode and dependencies against the SPEC
- Used: SPEC S2 (gate), S4a (one evaluate on the dual of the arena), S4c (fallback switches to gate targets: R15 (d)), FIX 2 (DFS
  choice at a cycle node), "every iteration changes σ or τ".
- The packet's PHASE (λ_Ξ and τ constant) is coarser than R25's key (λ_Ξ, λ_U, τ). My checker uses the packet's definition. That is
  a stronger test of §1-§2, and J1's proof needs only λ_Ξ and τ.
- The DF counterexample (§4.2) is SPEC N5 exactly: n5.py from the S3 start, 2 iterations / 1 fallback; check_sol2.py "zielonka(oink zlk)
  OK strategies verified"; one Odd choice vertex (o = 3).

## 2. §1 Lemmas
- Lemma U.
  - (1) L_k < ∞: (P1) at k and at k+1, plus the phase. This does not even need "relevant".
  - (2)-(4) are Claim (T) with the H_{k+1}-path to the first visit of c. Every changed successor before c is at a vertex with λ = c ≠
    itself, hence a relevant change of level ≤ L_k; own cycle nodes never lie on such a prefix.
  - (P2) is exact in the representation (a non-cycle-node never lies on its own prefix). ✓
  - DATA: 11,595 in-phase transitions, COARSE_{L_k}(Ξ) frozen at every one; L_k < ∞ always; Ξ unchanged at all 376 NU transitions.
- Lemma HI.
  - y is unswitched or switched relevantly, so the COARSE_L values of both ends are the same at k and k+1 (Lemma U, (C2)).
  - Level and direction above L are functions of the two COARSE_L values.
  - σ_k(y) and σ_{k+1}(y) have level ≤ L at both states. ✓
  - DATA: 323,374 vertex checks, 0 failures.
- G-LP-2 (HI's "Consequence: M_{k+1} = M_k if M_k > L_k; M_{k+1} ≤ L_k if M_k = L_k").
  - HI excludes Even vertices that are own cycle nodes and switched. Their switches are not counted in L_k, and their gate edges at k+1
    are measured from the NEW successor.
  - Such switches above L_k are common: 377 of 428 own-cycle-node switches in my batch have level > L_k.
  - So the Consequence does not follow from HI as written. If the only level-M_k gate edges sit at such a vertex, the argument gives
    nothing.
  - DATA: the Consequence held at all 2,472 (M_k > L_k) and 8,240 (M_k = L_k) cases, so it may be true. But it is unproved, and it is
    used nowhere in §2-§4. Either drop it, or restrict it to transitions with no own-cycle-node switch above L_k.
- Lemma UL.
  - Ω(y) odd: y ∈ P(Ξ_k(a)) puts a on an H_k-cycle through y, top ≥ ℓ, against (P1).
  - Ω(y) even: bit ℓ of Ξ_{k+1}(z) cannot drop (Lemma U above ℓ, R15 (a)), so z lies on an H_{k+1}-cycle through y, against the phase. ✓
  - DATA: 10,144 checks, 0 failures.
- Lemma GR.
  - (a) COARSE_ℓ is frozen for L_k ≤ ℓ. A bit-ℓ change is then the top difference, and R15 (a) makes it the good one. ✓
  - (b) UL gives y ≠ u_ℓ, so y ⊕ keeps bit ℓ. a is ℓ-bad, z is ℓ-good, and (a) keeps z good. ✓
  - DATA: (b) at 13,155 attaining Even switches; (a) at every (transition, ℓ, v); 0 failures.
- Lemma NU.
  - Ξ is constant (Lemma U), and τ is constant, so σ changes at every transition.
  - A non-cycle-node switch would be relevant of level ≥ −1, since gate targets are strictly better.
  - Own-cycle-node switches strictly increase Ξ(σ y) with Ξ fixed. ✓
  - DATA: every NU switch is at an own cycle node; max NU run 2 ≤ m − n.

## 3. §2 Theorem LP: SIGN
- Bound 1: ≤ T_rel + 1 NU runs, each ≤ m − n long. ✓
- Steps 2-3.
  - Between rises the run values strictly decrease within {−1, …, n − 1}: ≤ (n + 1)(ρ + 1) runs.
  - In a run of value ℓ ≥ 0, every non-ε transition adds a new vertex to G_ℓ (GR (b)), and G_ℓ never shrinks during the run (GR (a),
    NU included). So ≤ n transitions. ✓
- Step 4 (value −1).
  - COARSE_{−1} (cycle node + full path set) is frozen, so Ξ_k(a), Ξ_k(z) and Ξ_{k+1}(z) all have the same path set. ⊕ y is then
    monotone and strict (length + 1 on all of them).
  - N-LP-1: the packet's general phrase "y ⊕ keeps order and strictness between values of one cycle node" is false for set-valued ⊕
    (R24 TB-1 (b)). It is true here for the reason above.
  - Lengths are monotone in [0, n − 1] (fixed cycle node and path set). ✓
- DATA: both inequalities held on every one of 2,282 phases. Batch maxima: T 110, ρ 14, ε total 600, rises 687.

## 4. §3 on 𝒞^1O
### 4.1 VJ00 Lemma 5.8 (opened, report pp. 19-21)
- Statement (p. 19): "1. strategy σ is not a maximum element in (Strategies⊕, ⊑), 2. Improve(σ) ≠ σ, 3. Improve(σ) ⋢ σ" are equivalent.
- Proof of 2 ⇒ 3 (p. 21): "if Improve(σ) ≠ σ then for some v ∈ M⊕, the predicate Prog does not hold for Ωσ along the edge
  (v, [Improve(σ)](v)). Therefore, by Lemma 5.2 … Ωσ ≠ Θ_{Improve(σ)Improve(σ)}".
- At a cycle node v (Λ(v) = v), Prog's clause 3 (p. 15) only asks Π(v) ≅_{Λ(v)} Π(w) ⊕ v and Π(v) = (∅, 0). ≅ ignores the length, so a
  length-only improvement at v satisfies Prog. The step fails there, and Ω can stay unchanged (R15 (b) Lemma B: exactly these switches
  leave Ω unchanged).
- This is RESULTS R15's signed side finding: "VJ00 … Lemma 5.8's direction 'Improve(σ) ≠ σ ⇒ σ not maximum' … FAIL[S] at cycle nodes".
  Lemma DF cites exactly this direction.
### 4.2 Lemma DF as stated: NOT SIGNED (counterexample)
- instances/df_cex.pg (pgsolver format, sha1 0a98e1b7ad99d007abdd0f1c39387dd0232f656d). Vertices (priority, owner, successors):
  0 (3, E, {4}), 1 (5, E, {0, 3, 4}), 2 (3, E, {0, 4}), 3 (5, O, {3, 4}), 4 (0, E, {2, 3}). One Odd choice vertex o = 3.
  - n5.py: 2 iterations, 1 fallback. check_sol2.py: "zielonka(oink zlk) OK strategies verified".
- SPEC run from the S3 start.
  - State 0: σ = (0→4, 1→4, 2→4, 4→2), τ(o) = 3 (o's self-loop). R_0 = {3}.
  - Vertex 2 (Even, Ω 3 odd) is the top of the cycle 2 → 4 → 2, so it is its own cycle node: Ξ(2) = (2, ∅, 0), Ξ(4) = (2, ∅, 1),
    Ξ(0) = (2, ∅, 2).
  - Iσ_0 = {(1, 0), (2, 0)}, both of level −1 (length only; at an odd cycle node longer is better for Even).
- Transition 0 → 1 is an S4a step inside a phase (λ_Ξ and τ unchanged). The arena at 2 is {4, 0}. FIX 2's DFS choice at the cycle node 2
  keeps a = σ_1(2) = 4.
- At state 1, (2, 0) is still a gate edge (Ξ_1(0) = (2, ∅, 2) ▷ Ξ_1(4) = (2, ∅, 1)), and a = 4 ∈ F_1 = V \ {3}. DF claims a ∈ R_1:
  FALSE.
- Transition 1 → 2 is the S4c fallback that makes this length-only switch, the "stall" the I1 failure predicts.
- Batch DATA: DF as stated fails 176 times in the batch (and 28 in df_probe seed 901). In every failure y is its own cycle node and the
  gate edge has level −1. There are 0 failures with y not its own cycle node (15,746 checks).
### 4.3 DF′ (DF with "λ_{k+1}(y) ≠ y"): SIGN, with this proof
- Suppose a := σ_{k+1}(y) ∈ F_{k+1}. Then y ∈ F_{k+1} (its play passes a). On F, Ξ = W (R19 (a)), so λ_W(y) = λ_Ξ(y) ≠ y.
- σ_{k+1} is a pointwise optimum of the one-player arena H_k against τ (R17 (F1)). Its VJ00 valuation in that arena is W_{k+1}, because
  Odd's vertices have single successors there.
- If W_{k+1}(z) ▷ W_{k+1}(a), the single switch y → z is an improvement in the arena:
  - R15 (a) (Lemma A) gives W′ ⊵ W_{k+1}, and (F1) gives W′ ⊴ W_{k+1}, so W′ = W_{k+1};
  - R15 (b) (Lemma B) then forces λ_W(y) = y, a contradiction.
  - So W_{k+1}(z) ⊴ W_{k+1}(a): this is "no improvement at y", proved without VJ00 Lemma 5.8, for y not its own W-cycle node.
- The packet's second bullet then applies verbatim: Ξ_{k+1}(z) ⊴ W_{k+1}(z) ((XW)) ⊴ W_{k+1}(a) = Ξ_{k+1}(a), against the gate edge. □
- DATA: DF′'s first step ("no improvement" for y with λ_W(y) ≠ y) held at all 15,746 arena-edge checks; DF′ itself never failed.
### 4.4 BAND: SIGN
- On R in route form, the path-set differences are (π_z Δ π_a) restricted above c_θ (honest) and above c_w (W). θ's and w's paths avoid
  routes.
- The top t has rank ℓ > rank c_θ. rank t > rank c_w would give W(z) ▷ W(a). t ≠ c_w, since c_w ∉ routes.
- So ℓ < rank c_w, and every difference vertex lies below c_w. ✓
- DATA: 606 checks, 0 failures.
### 4.5 WAKE: SIGN WITH GAPS (G-LP-1)
- Carrying the gate edge back: y is not its own cycle node, so it does not switch at the NU transitions in between, and Ξ is fixed there.
  HI at k carries the edge to k, so (y, z) is a gate edge on all of [k, k′] and an arena edge at k′ − 1. ✓
- G-LP-1: the next sentence uses DF. It must use DF′ (§4.3), whose extra hypothesis holds because y's switch at k′ is relevant
  (λ(y) ≠ y).
- The route-form clause uses DF's first step ("W_{k′}(z) ⊴ W_{k′}(a)") at a vertex y ∈ R. In route form λ_W(y) = c_w ≠ y, so DF′'s first
  step (§4.3) applies. Then BAND applies. CLOSED.
- z ∈ R: R is constant and y ∈ R_{k′}. ✓
- DATA: 1 wake in my whole batch (nowake_cex_n32, §6), with a, z ∈ R. Not route form (U3), so the U1 clause is not exercised by data.

## 5. §4 Corollary LP′: SIGN
- ε ≤ S_o: o is the only Odd vertex with a choice. ✓
- ρ ≤ 2f + S_o + 2X + K.
  - An interval [k, k′] between consecutive relevant transitions shares only endpoints with its neighbours, so each transition lies in
    ≤ 2 such intervals.
  - Otherwise the rise is either Odd-attained (σ̄(o) relevant) or a wake (no fallback and R constant on [k, k′ + 1], as the definition
    requires). ✓
- J ≤ S_o.
  - J1: a non-tame transition switches σ̄(o) above M_k.
  - If λ(o) = o, that change is not relevant, L_k ≤ M_k (relevant changes are Even gate edges), and Lemma U makes the transition tame:
    a contradiction. So the change is relevant. ✓
- Assembling LP + FB gives the stated T bound and T = O(m·n⁵(1 + S_o + X + K)). ✓
- Neither DF nor WAKE is used. The last bullet (wakes are R-changes of U1 pieces or U2/U3 stretches) is a remark, valid with G-LP-1.
- DATA: ε ≤ S_o, ρ ≤ 2f + S_o + 2X + K, J ≤ S_o and the T bound held on all 1,792 𝒞^1O phases. Max S_o 49, max K 1.

## 6. §5-§6 data reproduced (not signed)
- NO-WAKE FALSE: nowake_cex_n32.pg (sha1 3a56e3fb…), one Odd choice vertex o = 27. n5.py 9 iterations / 2 fallbacks; zlk +
  check_sol2.py OK.
  - In-phase transitions 0, 1 with |R| 30, R constant, ¬H1, ¬H2, c_θ = o (rank 15), c_w = 13 (rank 31).
  - L_0 = 26; at transition 1, y = 11 switches 22 → 9 at level 30 > L_0. That is a wake. The packet's description is confirmed.
- My batch (run_all.sh; logs/totals.txt):
  - general games, seeds 921 (3,000, n 4-12) and 922 (800, n 12-20);
  - random 𝒞^1O, seeds 923 (3,000, n 6-14) and 924 (800, n 14-24);
  - the library: every experiments/**/*.pg with one Odd choice vertex and n ≤ 64 (228 files, S3 start + 2 random starts each);
  - 8,284 runs, 23,863 transitions, 2,282 phases, 11,595 in-phase transitions;
  - 232 logs, all RESULT OK, 0 violations of anything signed above. The DF as-stated failures are counted, not flagged, since DF′ is
    the signed form.

## 7. Gap list
| id | where | status |
| --- | --- | --- |
| DF (NOT SIGNED) | §3 Lemma DF: "a maximum has no improvement" (VJ00 Lemma 5.8 2 ⇒ 3 ⇒ 1) fails at cycle nodes | counterexample instances/df_cex.pg; repaired DF′ (λ(y) ≠ y) signed, proof §4.3 |
| G-LP-1 | §3 WAKE cites DF | CLOSED: cite DF′ (its y is not its own cycle node) |
| G-LP-2 | §1 HI "Consequence" | unproved as written (own-cycle-node switches above L_k: 377 seen); unused; DATA holds |
| N-LP-1 | §2 step 4: "y ⊕ keeps order … one cycle node" | true here (equal path sets), false in general |

## DONE / FINDINGS / NEEDS
DONE (Opus 5.5, D15).
- Report: docs/referee-2/R2-N5-LP.md. Tools: docs/referee-2/R2-N5-LP/.
- Verdicts:
  - §1 U, HI, UL, GR, NU: SIGN.
  - §2 LP: SIGN.
  - §3 DF: NOT SIGNED as stated (counterexample df_cex.pg); DF′ SIGN; BAND SIGN; WAKE SIGN WITH GAPS (G-LP-1).
  - §4 LP′: SIGN.
- Evidence:
  - 8,284 runs; 0 violations of the signed statements.
  - df_cex.pg: n5.py 2/1, zlk + check_sol2.py OK.
FINDINGS
- Lemma DF rests on VJ00 Lemma 5.8's direction that R15 already records as false at cycle nodes. It fails exactly there (176 cases, all
  own-cycle-node length-only edges). The fix is one hypothesis, which WAKE satisfies.
- HI's Consequence is unproved (own-cycle-node switches above L_k are common). It is not used.
- Theorem LP and Corollary LP′ are unaffected: they use neither DF nor the Consequence.
NEEDS
- Lead: route DF → DF′ (with the §4.3 proof), G-LP-1, G-LP-2 and N-LP-1 to L-NEW's fixes file for P-N5-LP.
- Lead: tell me when REFEREE's report is pushed, for §C.

## 8. Companion packet P-N5-SO (one combined review; Lead 01:00Z)
Written 2026-10-25 01:15Z (date -u). Object: docs/new/P-N5-SO-box32.md, sha1 deb5ee4422da3ab7389ce35e4542977927b53886, pinned at trunk 1ef02bb
(ancestor of my tree). L-NEW successor 12. Own code: R2-N5-LP/so_check.py and so_climb.py (on fb_check). Every game asserts one Odd choice
vertex. I have not read docs/referee/ for this packet.
### 8.1 Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| Lemma TH | SIGN | N-SO-1: F1° (R22 (a)) is signed for R22's phase key (λ_Ξ, λ_U, τ) and is used here on intervals of the coarser LP phase (λ_Ξ, τ). Its proof uses only λ_Ξ on F, τ, Lemma G (a), (F1) in G_τ and FBL-N (ii), none of which needs λ_U, so it transfers. DATA: 7,241 + 38,680 intervals of this phase notion, 0 failures |
| Lemma SO | SIGN WITH GAPS | G-SO-1: the frozen-key step justifies two strict increases by "⊕ keeps strictness", which is false for set-valued ⊕ in general (R24 TB-1 (b)). CLOSED: p's strict gain is R19 (d) (SG); along x's unchanged prefix, ⊕ is strictly monotone because the prefix vertices lie in neither path set (paths before c are simple, and a repeat would close a cycle without c, against λ = c in the phase). N-SO-3: "⊕ is injective for a fixed cycle node" is false in general (sets that differ only at o), but true on the exits' values: an exit whose path passes o has value path ⊕ θ, strictly longer than μ |
| Corollary XJ | SIGN WITH GAPS | N-SO-2: "f = O(n³(1 + X))" should read O(d_o·n³(1 + X)) ⊆ O(n⁴(1 + X)), since J ≤ S_o ≤ d_o(2n + (n + 1)X). The T bound O(m·n⁷(1 + X) + m·n⁵·K) is right and already uses n⁴. With that, (J-poly), NFB-O and the fallback count follow from (X) per phase, as the corollary says |
### 8.2 Checks
- Lemma TH.
  - Crossing θ-changes ≤ X (H1 is constant on crossing-free intervals, TC (i)).
  - ¬H1: θ = (c_θ, ∅, d) (R-1). Ξ is monotone and c_θ fixed, so along the whole phase the ¬H1 values form a monotone d-sequence: ≤ n − 1
    changes.
  - H1: x0 = σ̄_k(o) is a full minimiser (R25 CAP-1 closure). x0 ∈ F (its honest play equals its (σ, τ)-play, since o is the only choice).
    The four-term sandwich shows that Ξ(x0) fixed forces θ fixed, so each θ-change is an F-change: ≤ max(0, |F| − 1) per interval
    (F1°), ≤ n(X + 1). ✓
  - DATA: TH bound on every phase. 1,220 + 22,525 H1 cases with x0 ∈ F and Ξ(x0) changed. 58 + 31 ¬H1 changes, all with θ = (c_θ, ∅, d),
    ≤ n − 1 per phase.
- Lemma SO.
  - T (the full minimisers) only shrinks on a θ-run, and μ is fixed (via N-SO-3). ✓
  - The choice is the key-minimum of T: Lemma R; longest-path mode = smallest index, BFS mode = lex-least root-first path (TB step 5). ✓
  - An x ∈ T has an H-path to c that avoids o (length argument) and runs through single-successor vertices; its key is frozen while x
    stays in T (G-SO-1 closure). ✓
  - So a relevant change with θ fixed removes the old choice: ≤ d_o − 1 per run. ✓
  - DATA: 10,841 + 67,456 key-minimum checks; 8,002 + 20,338 frozen-key checks; 19 + 3,896 relevant changes with θ fixed, the old choice
    leaving T every time; T never grew; μ never moved with θ fixed. 0 failures.
- Corollary XJ: S_o ≤ d_o(Θ + 1) ≤ d_o(2n + (n + 1)X); J ≤ S_o (P-N5-LP §4 step 3, signed in §5 above); FB. ✓
  - DATA: J ≤ S_o and the f bound on every phase.
### 8.3 Data and climbs
- Batch (run_so.sh; logs/so_totals.txt):
  - random 𝒞^1O, seeds 931 (3,000) and 932 (800), plus the 228-file one-o library (×3 starts);
  - 4,502 runs, 1,854 phases (1,558 with λ(o) ≠ o);
  - 236 logs, all RESULT OK.
  - Maxima: Θ 51, S_o 49 (lev_l_x, as in the packet), J 18, X 84, f 33.
  - Closest approaches: S_o − d_o(Θ + 1) = −1; J − S_o = 0 (J = S_o is attained).
- Climbs (so_climb.py, 6 × 500 steps, 12,000 fully checked runs): objectives S_o − d_o(Θ + 1), J − S_o, and the number of relevant
  σ̄(o)-changes with θ fixed. Seeds: lev_l_x, jcl_zcl_cu_n48, nowake_cex_n32. 0 violations; best margins −1 and 0, never positive.
- Honest limit: the bounds are loose in d_o and n; the data show neither a growth law nor tightness beyond J = S_o.
### 8.4 Gap list (P-N5-SO)
| id | where | status |
| --- | --- | --- |
| G-SO-1 | Lemma SO, frozen-key step: "⊕ keeps strictness" | CLOSED ((SG) R19 (d) + simple prefixes) |
| N-SO-1 | Lemma TH: F1° on a coarser phase | transfers (proof uses no λ_U); DATA agrees |
| N-SO-2 | Corollary XJ: f = O(n³(1 + X)) | should be O(d_o n³(1 + X)) ⊆ O(n⁴(1 + X)) |
| N-SO-3 | Lemma SO: "⊕ is injective for a fixed cycle node" | false in general; true on exit values (length) |
Combined DONE (P-N5-LP + P-N5-SO): LP §1-§2 and LP′ SIGN; DF NOT SIGNED as stated (df_cex.pg), DF′ SIGN; WAKE SIGN WITH GAPS; TH SIGN; SO
SIGN WITH GAPS (closed); XJ SIGN WITH GAPS (N-SO-2). NEEDS: Lead: route DF′, G-LP-1, G-LP-2, N-LP-1, G-SO-1, N-SO-1..3 to L-NEW's fixes files;
tell me when REFEREE's reports are pushed, for §C.

## §C. Comparison with REFEREE's R-N5-LP (referee 4957b2c, on trunk; read after my reports 4949d6c9 and ba67f410 were pushed)
Written 2026-10-25 01:19Z (date -u). Kept short at the Lead's request. Signature (Opus 5.5, D15).
### C.1 Verdicts: no disagreement of substance
| statement | REFEREE | REFEREE-2 |
| --- | --- | --- |
| LP §1 U, HI, UL, GR, NU; §2 LP | SIGNED (HI Consequence: gap HI-1) | SIGN (HI Consequence: G-LP-2) |
| LP §3 DF | NOT SIGNED, FALSE (own df_cex.pg, n 11) | NOT SIGNED, FALSE (own df_cex.pg, n 5) |
| LP §3 DF′ (y not its own W-cycle node) | SIGNED (Bellman + R24 G-TB-1) | SIGN (R15 (a) + (F1) + R15 (b) Lemma B) |
| LP §3 BAND | SIGNED | SIGN |
| LP §3 WAKE | SIGNED WITH GAP W-1 | SIGN WITH GAPS G-LP-1 |
| LP §4 LP′ | SIGNED | SIGN |
| SO Lemma TH | SIGNED WITH GAP SO-1 | SIGN (N-SO-1) |
| SO Lemma SO | SIGNED | SIGN WITH GAPS G-SO-1 (closed) |
| SO Corollary XJ | SIGNED WITH GAP XJ-1 | SIGN WITH GAPS N-SO-2 |
- DF: same failing step (VJ00 Lemma 5.8, 2 ⇒ 3 ⇒ 1, at own cycle nodes) and same repair. Two independent counterexamples. The two DF′
  proofs differ in route but are both valid: REFEREE's goes through the Bellman inequality, mine through Lemma A/B.
- SO-1: REFEREE asks me to check its full-minimiser proof (σ̄(o) minimises Ξ over succ(o) when λ(o) ≠ o). I did, and adopted it, in
  R2-N5-FB §C.3. So that dependency carries two signatures: CLOSED.
- XJ-1 = N-SO-2 (f = O(n⁴(1 + X))).
- G-SO-1 is mine only. REFEREE's key-frozen check gives the same closure ("⊕ p strictly monotone: p is in neither path set"), so we agree.
### C.2 Joint gap map
| REFEREE | REFEREE-2 | status |
| --- | --- | --- |
| DF FALSE | DF NOT SIGNED (df_cex.pg) | same; DF′ signed by both |
| HI-1 | G-LP-2 | same (Consequence unproved for switched own cycle nodes; unused) |
| W-1 | G-LP-1 | same (WAKE cites DF′); closed |
| — | N-LP-1 | mine only (⊕ order phrase in LP step 4); nit |
| SO-1 | R2-N5-FB §C.3 | closed (two signatures on the full-minimiser proof) |
| XJ-1 | N-SO-2 | same |
| — | G-SO-1, N-SO-1, N-SO-3 | mine only; closed / notes |
Final (Opus 5.5, D15): as in my §§ above. G-N5-TIME OPEN; open cores per phase: X and K.
