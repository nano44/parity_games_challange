# R2-N5-RE: second-referee check of packet P-N5-RE (L-NEW box 26: Lemmas G, Wo, RM, RE, PIECE on 𝒞^1O). REFEREE-2 (successor 4), 2026-10-24 14:42Z (date -u; first pushed as 3ee7b737 with a wrong stamp 14:50Z, corrected)
Signature: (Opus 5.5, D15). Packet P-N5-RE (Lead 14:20Z), pinned at trunk claude/vibrant-johnson-nxvvxo 52c7261.
Object: docs/new/P-N5-RE-box26.md, sha1 8dba4576950d4888b90d4c0cc86217b9b8fec745 (checked at the pin and in my merged tree; L-NEW
successor 9, unrefereed). Context read: the SPEC docs/new/N5-ssi-global.md (S1-S5); docs/new/N5-phase-bound-box10.md §1-§3 ((V1), (V2),
(F1), Lemma P, Theorem PH); docs/new/N5-time-box21.md §1, §2.3, §3.5; RESULTS R15, R17, R18 as landed; docs/new/N5-reentry-box26.md
§2-§3 (to learn the lane's classes; not used as evidence). These files are identical at the pin and in my tree (empty diff).
Independence: I did not read docs/referee/ before pushing this report. I did not run or import the lane's box25/box26 scripts.
Tools (docs/referee-2/R2-N5-RE/, own code from the definitions): re_check.py, sg_check.py, re_climb.py, dump_nc.py, totals.py,
run_all.sh; logs/ (every run), climb/ (climbs and their final games), nc_fail_n12.pg/.start. §6 gives the numbers.

## Verdicts (Opus 5.5, D15)
| item | verdict | gaps / notes |
| --- | --- | --- |
| (1) Lemma G (a) | SIGN | N-RE-1: (a) needs no (h) |
| (1) Lemma G (b) | SIGN | — |
| (1) Lemma G (c) | SIGN | — |
| (2) Lemma Wo | SIGN | N-RE-2: uses only the W-half of (h) at k and k+1; no phase needed |
| (3) Lemma RM | SIGN | — |
| (4) Lemma RE, as stated (with (NC)) | SIGN WITH GAPS | G-RE-1: step 2, Case NOT (i): the "Caveat" sentence is not justified; G-RE-2: step 3's avoidance sentence is not an argument. Both are closed by §4 (a repaired proof that is shorter and uses no case split) |
| (4) Lemma RE WITHOUT (NC) | SIGN (my proof, §4) | (NC) is not needed: it can be dropped. The "flat leave" of the packet's §6 cannot occur |
| (4) Corollary RE | SIGN WITH GAPS | N-RE-3: the corollary must also assume τ constant on each leave-to-re-entry interval (Lemma RE does); (NC) can be dropped |
| (5) Lemma PIECE | SIGN WITH GAPS | G-RE-3: the count |R| − 1 for the route game 𝓡 is not Theorem PH verbatim (𝓡 has |R| + |K| vertices; PH gives |R| + |K| − 1). Closed in §5 by re-running Lemma P with the base case at o. N-RE-4: θ constant is not needed; the "Consequence (READING)" must say "inside one joint λ-phase" |
Can (NC) be closed? YES. §4 proves Lemma RE's conclusion under (h) at L and E+1, one joint λ-phase and τ constant, with no hypothesis on y.
The step that replaces (NC) is a uniform strict-gain fact (SG): at any N5 transition, an Even vertex that switches and is not its own cycle
node gains strictly. So gap G26-1, in its (NC) residue, is CLOSED (subject to a second signature).
Scope (as the packet says): lemmas about N5 itself on 𝒞^1O, a class that is polynomial by other means. Not a running-time bound, not a
TARGET.md claim, not a step-4 pass; (CYC), (XING), (FB-1O) stay OPEN and G-N5-TIME stays OPEN. TARGET.md diff: no statement here is about
general parity games; nothing to diff against TARGET.md §2.

## 0. Definitions I checked against (from the SPEC and box 10 §1)
- Value (c, P, ℓ) of a play from v: c = the most relevant vertex (highest rank, rank by (Ω, index)) of the cycle reached; P = the vertices
  before the first visit of c that are more relevant than c; ℓ = the number of steps to c. Even's order: reward of c, then the top of the
  symmetric difference of the path sets, then ℓ (longer better iff c is odd). x ⊕ (c, P, ℓ) = (c, P ∪ {x if more relevant than c}, ℓ + 1).
- (V1): if x is not its own cycle node, val(x) = x ⊕ val(succ(x)), and the path of val(succ(x)) avoids x. I re-derived it, because §4
  leans on it in a case the packet avoided: if x lies on the cycle but x ≠ c, the play x, succ(x), …, c reaches c before it returns to x
  (c is on the cycle, and the first return to x closes the cycle). So the path from succ(x) to c avoids x in that case too. ✓
- (V2): a ⊴ b, both paths avoid x (or the cycle nodes differ) ⇒ x ⊕ a ⊴ x ⊕ b, strictly if a ◁ b. ✓ (signed in R17 (a)).
- Ξ_k = Even's honest valuation (against Odd's optimal reply σ̄_k; in 𝒞^1O, the pointwise minimum over Odd's d choices at o); W_k = the
  (σ_k, τ_k)-play values; R15 (a): Ξ_{k+1} ⊵ Ξ_k (signed). Iσ_k = {(v, z) : Ξ_k(z) ▷ Ξ_k(σ_k(v))} (S2). An S4a switch and an S4c switch
  both move v along an edge of Iσ_k (S4a: the arena is {σ_k(v)} ∪ Iσ_k(v); S4c: by definition).
- Joint λ-phase (box 21 §2.3): the cycle-node maps of Ξ and of Odd's dual valuation are constant. (h) at k: neither the honest play nor
  the W-play from o returns to o, and θ_k = Ξ_k(o), w_k = W_k(o) have the same cycle node c.

## 1. Lemma G (a)-(c): SIGN
- (a) For v ∈ F_k the (σ_k, τ_k)-play from v never meets o, the only Odd vertex with a choice. The honest play from v is the same
  sequence of vertices (Odd's other vertices are forced), so Ξ_k(v) = W_k(v). This uses no part of (h) (N-RE-1). ✓
- (b) For v ∈ R_k both plays follow π_v (forced Odd vertices and σ_k; π_v excludes o) and then o's continuation. By (h) neither
  continuation returns to o. Neither meets π_v either, since every vertex of π_v leads to o along the same forced/σ_k edges. Iterating
  (V1) along π_v (no vertex of π_v is on the final cycle, so none is its own cycle node) gives Ξ_k(v) = π_v ⊕ θ_k, W_k(v) = π_v ⊕ w_k. ✓
- (c) With the common cycle node c, π_y ⊕ T = (c, A_y ∪ P(T), |π_y| + ℓ(T)), A_y = {u ∈ π_y : u more relevant than c}, A_y ∩ P(T) = ∅
  (by (b)). The comparison of π_y ⊕ T and π_z ⊕ T sees the same reward, the symmetric difference A_y Δ A_z and the length difference
  |π_y| − |π_z|; none depends on T ∈ {θ_k, w_k}. ✓
- DATA (own code): G (a) 770,554 vertex checks at all states; G (b) 164,560 and G (c) 2,447,720 checks at (h)-states (§6). 0 violations.

## 2. Lemma Wo: SIGN
- b := τ(o) is the same at k and k+1. The W-play from o does not return to o at j = k, k+1 (the W-half of (h)), so b ∈ F_j and o is not
  its own cycle node. (V1): w_j = o ⊕ W_j(b) = o ⊕ Ξ_j(b) (Lemma G (a)). R15 (a): Ξ_{k+1}(b) ⊵ Ξ_k(b). Both paths avoid o (b ∈ F_j), so
  (V2) gives w_{k+1} ⊵ w_k. ✓ N-RE-2: only the W-half of (h) is used, and no phase hypothesis.
- DATA: 19,019 checks at τ-constant transitions with (h) at both ends, 0 decreases (§6).

## 3. Lemma RM: SIGN
- Lemma G (b) at k and k+1 with the same θ, then R15 (a): π^{k+1}_x ⊕ θ = Ξ_{k+1}(x) ⊵ Ξ_k(x) = π^k_x ⊕ θ. Lemma G (c) makes this the
  route order for either terminal. ✓ (The joint phase and τ constant are not used beyond what (h) and θ constant give.)
- DATA: 70,714 checks, 0 route decreases (§6).

## 4. Lemma RE: (NC) is not needed
### 4.1 Where the packet's proof has gaps
- G-RE-1 (step 2, Case NOT (i)). The chain y ⊕ Ξ_{L+1}(z) ⊵ y ⊕ Ξ_L(z) ▷ y ⊕ Ξ_L(σ_L(y)) applies (V2) to Ξ_L(z), so it needs the
  L-path of z to avoid y. The "Caveat" says: if z's L-path passed y, then z ∈ R_L and y's new play would cycle back through y, i.e.
  case (i). The second half does not follow. z's path at L+1 may differ from its path at L (other vertices switch in the same step), so
  y → z at L+1 need not cycle back through y. The configuration did not occur in my data (0 leaves with z's L-path through y), but the
  sentence is not a proof.
- Case (i) and (ii) (the (NC) case). The packet leaves it open and says in §6 that Ξ_{L+1}(y) "may equal Ξ_L(y) if the lengths agree".
  That cannot happen (§4.2). It does occur as a configuration: 31 leaves in my data have (i) and (ii) (all with strict gain), e.g.
  nc_fail_n12.pg (§4.4).
- G-RE-2 (step 3). "The prefix avoids y's new play: otherwise x's new play would pass a prefix vertex twice" is not a contradiction (plays
  may cycle). The avoidance that (V2) needs comes from (V1) instead (§4.2, step 3).
### 4.2 Repaired proof (covers all cases; no (NC))
Hypotheses exactly as in the packet minus (NC): one joint λ-phase containing L, …, E+1; τ constant on it; (h) at L and at E+1.
- Step 1 (as the packet). Some Even vertex of π^L_x switches at L → L+1; let y be the first one along π^L_x from x.
- Step 2 (SG at y). y ∈ R_L, so by (h) at L the honest play from y is π_y, then o's honest continuation, which never returns to o and so
  never meets π_y. Hence y is not on its own final cycle and λ_L(y) = c ≠ y. The phase gives λ_{L+1}(y) = c ≠ y. Let z := σ_{L+1}(y);
  (y, z) ∈ Iσ_L (S4a or S4c), i.e. Ξ_L(z) ▷ Ξ_L(σ_L(y)). Then:
  - Ξ_{L+1}(z) ⊵ Ξ_L(z) (R15 (a)), so Ξ_{L+1}(z) ▷ Ξ_L(σ_L(y)) (transitivity of the order, BEFORE any prefix is applied).
  - The path of Ξ_{L+1}(z) avoids y ((V1) at L+1, y ≠ λ_{L+1}(y); this includes the case where y lies on its new cycle, §0). The path of
    Ξ_L(σ_L(y)) avoids y ((V1) at L).
  - Strict (V2): Ξ_{L+1}(y) = y ⊕ Ξ_{L+1}(z) ▷ y ⊕ Ξ_L(σ_L(y)) = Ξ_L(y). □
  The path of Ξ_L(z) is never used, so neither the Caveat nor the case split (i)/(ii) is needed.
- Step 3 (prefix). Let u be a vertex of π^L_x before y. Its successor s is the same at L and L+1, and u ∈ R_L, so as in step 2,
  λ_L(u) = λ_{L+1}(u) = c ≠ u. (V1) at L and at L+1 give Ξ_j(u) = u ⊕ Ξ_j(s), with paths avoiding u for j = L, L+1. By induction from y
  back to x, Ξ_{L+1}(s) ▷ Ξ_L(s), and strict (V2) gives Ξ_{L+1}(u) ▷ Ξ_L(u). So Ξ_{L+1}(x) ▷ Ξ_L(x). □
- Steps 4-5 (as the packet). R15 (a) from L+1 to E+1. Lemma G (b) at L and at E+1. If θ_{E+1} = θ_L, then
  π^{E+1}_x ⊕ θ_L = Ξ_{E+1}(x) ⊵ Ξ_{L+1}(x) ▷ Ξ_L(x) = π^L_x ⊕ θ_L. □
- What is used: (h) at L (y and the prefix are not their own cycle nodes; Lemma G (b) at L), (h) at E+1 (Lemma G (b)), the phase only at
  L → L+1 (λ_{L+1} = λ_L on π^L_x), τ constant (step 1), R15 (a), (V1), (V2), and S2/S4. θ is non-decreasing at o (R15 (a)), so
  "θ_{E+1} = θ_L" is the same as "θ is constant on [L, E+1]".
### 4.3 The general fact behind it (SG), and why the hypothesis "not its own cycle node" is sharp
(SG) At ANY N5 transition k → k+1, if an Even vertex y switches (σ_{k+1}(y) ≠ σ_k(y)) and λ_k(y) ≠ y, then Ξ_{k+1}(y) ▷ Ξ_k(y).
Proof. If λ_{k+1}(y) ≠ λ_k(y), then Ξ_{k+1}(y) ≠ Ξ_k(y), and R15 (a) makes the change strict. Otherwise λ_{k+1}(y) = λ_k(y) ≠ y, and
step 2 of §4.2 applies word for word. □ No (h), no phase, no τ condition. Data: sg_check.py, 25,283 switches with λ_k(y) ≠ y (own and
SPEC tie-breaks, o-cyclic and arbitrary 𝒞^1O), 0 violations. Control: 6,260 switches at vertices that are their own cycle node, 1,159
of them value-flat. These are the flat cycle-closing switches of R15 (b), so the hypothesis cannot be dropped.
### 4.4 The (NC) configuration exists and is strict (instance)
nc_fail_n12.pg (n = 12; o = 10; start nc_fail_n12.start), from my random stream (seed 2, game 755). At L = 0: x = y = 5, π^0_5 = [5, 1],
c = 0 (priority 11, odd), Ξ_0(5) = (0, ∅, 3): (ii) holds. At L → L+1, 5 → 6 and 0 → 5 (and 9 → 4). At L+1, 5's honest and W play is
5, 6, 7, 3, 0, 5 (a cycle through 5 with top 0): (i) holds. Ξ_1(5) = (0, ∅, 4) ▷ (0, ∅, 3), since c is odd and longer is better. So the
leave is strict, exactly as §4.2 predicts: Ξ_1(6) = (0, ∅, 3) ▷ Ξ_0(1) = (0, ∅, 2). The same leave appears under SPEC tie-breaks
(logs/inst_spec_nc_fail_n12.txt). Reproduce: dump_nc.py 2 755 6 14.

## 5. Lemma PIECE: SIGN WITH GAPS
- Steps 1-3 ✓. Closure of R and F under the stretch's plays is right. 𝓕 = G[F] is a one-player game (every Even vertex of F keeps σ_k(x) ∈ F,
  forced Odd vertices of F point into F, o ∉ F). The gate identities follow from Lemma G (a) (on F) and G (b)-(c) (on R, σ(x) ∈ R).
- Step 4 ✓. For ρ in 𝓕's arena (resp. 𝓡's), the extension by σ_{k+1} on the other part lies in the S4a arena. Its real values equal ρ's
  piece values: F is closed, and on R the terminal is o ⊕ W_{k+1}(b) = w_{k+1} = w. (F1) for the S4a arena then gives the claim. That
  σ_{k+1} maps F into F and R into R is the no-crossing hypothesis.
- G-RE-3 (step 5, the count for 𝓡). 𝓡 has the |R| vertices of R plus the |K| frozen vertices of K, so Theorem PH as stated bounds the
  value-changing steps of 𝓡 by |R| + |K| − 1, not |R| − 1. The sharper count is true. Proof: run Lemma P on 𝓡 with u = c and induct on
  the number L_R of edges of r before o (every path from R to c passes o and then K's fixed path). Base L_R = 0 (x = o): Ω_0(o) =
  value(r), since o's edge and K are fixed. The step is Lemma P's case analysis verbatim, with A2 and the B1 sub-case "x on c's cycle"
  vacuous (c's cycle lies in K). In B2, every alternative contradicts the absence of crossings, as in Theorem PH. L_R ≤ |R| − 1, so after
  |R| − 1 steps no R → R edge is improving except λ-changing ones. A λ-changing one would be taken (F1) and would make some R vertex cycle
  inside R, which is a crossing. So at most |R| − 1 transitions change an R value. For 𝓕, Theorem PH applies verbatim, from any start
  (R17 (e)), inside the joint phase: at most |F| − 1. Under (h), F ∋ τ(o) and R ∋ o are non-empty, so the total is ≤ n − 2. ✓
- N-RE-4: θ constant is not needed (Lemma G (c) at each state suffices); w constant is needed (𝓡's terminal). The "Consequence (READING)"
  drops "inside one joint λ-phase", which step 5 needs for 𝓕. With it the reading is right: (n − 2) per piece plus the crossing and fallback
  transitions themselves give ≤ (n − 1)(#crossings + #fallbacks + 1).
- DATA: 2,836 maximal stretches. Counts checked separately: R ≤ |R| − 1 and F ≤ |F| − 1, the sum ≤ n − 2. Also checked at every step:
  the gate identities of step 3 (76,979 edges) and the arena optimum of each piece (7,664 piece-optima, both pieces). 0 violations. The
  longest piece has 10 value-changing steps (rtt24, theta_tp32). The nearest approach to the bound is 3 below it.

## 6. Mechanical checks (own code; DATA, not proof)
Definitions implemented from §0 only. The honest valuation is the pointwise minimum over o's choices, and a single choice attaining it is
asserted. Odd's valuation is Even's pointwise one-player optimum (switch-all SI to convergence), read in G's order (Lemma R, R18 (d)). My own
N5 (S2-S4) uses RANDOM tie-breaks in the S4a optimum, including random value-preserving re-choices among optima, because the lemmas use only
(F1). In "spec" mode the state sequence comes from n5.py's functions (read-only), and each spec S4a step is checked to be a pointwise arena
optimum by my definitions (6,724 steps, 0 failures). Sanity checks at every state: Ξ ⊴ W ⊴ U (R18 (d)) and R15 (a), 0 failures.
Totals (run_all.sh; numbers from logs/totals.txt, written by totals.py over logs/rand_*.txt and logs/inst_*.txt):
| quantity | count | violations |
| --- | --- | --- |
| runs / transitions / states / (h)-states | 31,827 / 60,225 / 92,052 / 44,273 | — |
| Lemma G (a) / (b) / (c) checks | 770,554 / 164,560 / 2,447,720 | 0 |
| Lemma Wo (τ fixed, (h) at both ends) | 19,019 | 0 |
| Lemma RM (in phase, τ, θ fixed, (h) at both ends) | 70,714 | 0 |
| RE steps 2-3 at every leave (phase, τ fixed, (h) at L), (NC) not assumed | 5,309 leaves (4,278 neither (i) nor (ii); 1,000 (ii) only; 31 (i) and (ii) = (NC) fails; 0 (i) only) | 0 |
| leaves whose z has its L-path through y (the Caveat's case) | 0 | — |
| switched Even y ∈ R_L gains strictly (in phase, (h) at L) | 4,955 | 0 |
| re-entries under Lemma RE's hypotheses | 1,321 (400 with θ unchanged, all strict route improvements; 921 with a θ-change) | 0 |
| PIECE stretches / gate-edge identities / piece optima | 2,836 / 76,979 / 7,664 | 0 |
| SPEC steps checked as arena optima (my definitions) | 6,724 | 0 |
| (SG), sg_check.py (logs/sg_*.txt) | 25,283 switches with λ_k(y) ≠ y | 0 |
- Random games: o-cyclic 𝒞^1O, n 6-16 (o out-degree 2-3; other Odd vertices forced; priorities in 0..n with repeats), random start pairs:
  own tie-breaks seeds 2, 11, 12, 13 (27,000 runs), SPEC seed 21 (4,000 runs).
- Named instances (SPEC from the S3 best-reward start or the instance's .start, and 30 own-tie-break runs from random starts): fts_best16,
  theta_tp32, returns_rt48, returns_ph64, tr20_s4, i1h_fts_best16, thetare_n, thetare_min, oneodd_c24, rtt24, rtt16, fbh_drop9, wdrop_cyc,
  wdrop_canon, my nc_fail_n12, and my climb outputs c12_s54 (300 own runs) and c10_s51. sha1 in logs/instances.sha1.
- θ-unchanged re-entries (the case Lemma RE is about) are rare in random games: 0 in 31,000 random runs. They come from tr20_s4 (3 SPEC, 5 own) and from
  my climb outputs (c12_s54: 32 in 30 own runs, 360 in 300 own runs, 0 under SPEC from the best-reward start); over the climbs themselves another 1,204 (c12_s54 1,074,
  tr20_s61 130), every one checked. All are strict route improvements.
- Negative control: leaves at transitions without (h) or outside the phase. 48,697 such leaves; 3,356 have no strict gain at x, and all 3,356 are at non-(h) states (2,965 in phase, 391 out of phase); 0 at (h)-states.
  At non-(h) states the strict gain fails, so (h) at L is used. Also 4 W-drops at τ-constant transitions without (h) at both ends; 0 with it.
- Climbs (re_climb.py n 10/12/14, 1,200-1,500 steps; two from tr20_s4): every scored run fully checked, 0 violations (climb/*.log).

## 7. Gap list
| id | where | status |
| --- | --- | --- |
| G-RE-1 | RE step 2, Case NOT (i), "Caveat": z's L-path through y does not imply (i) | CLOSED by §4.2 (transitivity before prefix; no use of z's L-path) |
| G-RE-2 | RE step 3, avoidance sentence | CLOSED by §4.2 step 3 ((V1) at L and L+1) |
| (NC) = residue of G26-1 | RE hypothesis | CLOSED: not needed (§4.2); the "flat leave" of the packet's §6 cannot occur (§4.3-4.4) |
| G-RE-3 | PIECE step 5: |R| − 1 is not Theorem PH verbatim | CLOSED by §5 (Lemma P on 𝓡 with base at o) |
| N-RE-1 | G (a) needs no (h) | wording |
| N-RE-2 | Wo uses only the W-half of (h) | wording |
| N-RE-3 | Corollary RE omits "τ constant on each interval" | wording; needed |
| N-RE-4 | PIECE: θ constant not needed; Consequence must say "inside one joint λ-phase" | wording; needed |
| N-RE-5 | (i) does not say which play ("new play": honest or W) | moot after §4.2; in my data the two readings agreed on every leave |

## 8. For the Lead
- Lemma RE holds without (NC). Proposed statement: "Inside one joint λ-phase with τ constant, under (h) at L and at E+1, a re-entry with
  θ_{E+1} = θ_L is a strict route improvement over the last leave." The proof is §4.2, with (SG) of §4.3 as its one new step.
- The packet's claim "Ξ_{L+1}(y) may equal Ξ_L(y)" in §6 is false. L-NEW's §6 bullet on (NC) should be replaced by a pointer to §4.2.
- Nothing here bounds (CYC), (XING) or (FB-1O).
