# R2-N5-FB: second-referee check of packet P-N5-FB (L-SI box 7: coarse super-solutions, the max gate level, fallbacks per phase). REFEREE-2 (successor 5), 2026-10-24 22:47Z (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-FB (Lead 22:3xZ), pinned at trunk claude/vibrant-johnson-nxvvxo 348393b (an ancestor of my merged tree).
Object: docs/si/P-N5-FB-box7.md, sha1 9ece9994a1251f904935048a605495cd325946e7 (235 lines; checked at the pin and on my tree).
Background read: RESULTS R15, R21, R23; the SPEC (S1-S5, FIX 2-4); si.py l. 28-205; n5.py; docs/si/N5-C-box5.md §6.2 (the (JUMP-EQ) source).
VJ00 opened by me (BRICS RS-00-48, sha256 485a12de…, the file of R15; pp. 12-16 re-read for this packet).
Independence: I have not read docs/referee/R-N5-FB.md. The lane's scripts were only RE-RUN (output to my scratchpad, then diffed against the
committed logs). My checks are my own code.
Tools (docs/referee-2/R2-N5-FB/): fb_check.py (every statement of §2-§5 plus a direct test of (T)), a_check.py (statement A), fb_climb.py,
run_all.sh, totals.py, logs/, climb/.
Labels (D18 / L40): PROVED (L-SI succ. 3) is the packet's label; my verdicts say whether I sign the proof. Nothing here is a running-time bound,
a TARGET.md claim or a step-4 pass. G-N5-TIME and (J-poly) stay OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| (1) §4 Theorem FB | SIGN WITH GAPS | G-FB-1: step (2)'s "M < ∞ by NOINF" needs one line (NOINF bounds only the SWITCHED edge's level; the best-target choice carries it to all of y's gate edges). G-FB-2: step (2) cites R21 (c) FBL-N (i), which is signed on 𝒞^1O only, while §4 is claimed for every game; the fact follows from SPEC S4c + FIX 3 directly. Both CLOSED |
| (1) §4 Corollary | SIGN WITH GAPS | G-FB-3: on general games the W-lowering bullet uses R23 (g) WM beyond its signed scope (𝒞^1O). WM's argument ((F1) in G_τ at S4a steps, τ fixed) holds on every game. CLOSED. The (C) bullet is a 𝒞^1O statement and is fine as cited |
| (2) §2 Claim (T) | SIGN | — |
| (2) §2 COARSE-SI (a) and its converse | SIGN | — |
| (2) §2 COARSE-SI (b) TAME | SIGN | Uses Lemma 5.2 for H_{k+1} built from SPEC's σ̄. That is the R15 code link (DATA, re-checked: Ξ_k = Θ_{H_k} at every state) |
| (2) VJ00 citations by page | correct with one nit | N-FB-1: the Prog definition (P1)-(P3) is on p. 15, not p. 14. σ̄ (p. 14), Lemma 5.2 (p. 15) and (11) (p. 16) are right |
| (3) §3 MONO | SIGN | — |
| (3) §3 NOINF | SIGN | The case split is not needed: λ_k(σ_k y) = λ_k(y) = λ_{k+1}(y) = λ_{k+1}(z) = λ_k(z) by (P1) at k and at k+1. The Consequence needs G-FB-1 |
| (4) §5 J1 | SIGN | — |
| (4) §5 OFF | SIGN | — |
| (4) §5 CAP | SIGN WITH GAPS | G-FB-4: "b minimises Ξ_{k+1} over succ(o) (VJ00 p. 14)" and "the minimality of a" are false for SPEC's σ̄ when o is its own cycle node: there σ̄(o) is FIX 2's DFS choice, which is not always a minimiser (1,228 cases in my batch, all at own-cycle-node Odd vertices). CAP uses only COARSE_M with M ≥ −1, which drops lengths, and the DFS choice is a COARSE_{−1}-minimiser. CLOSED |
| (4) §5 Remark (non-tame ⇒ (NC) fails, cycle through o) | SIGN | One line added: a bad cycle avoiding o would be a cycle of H_{k+1}, whose top is a λ_{k+1} = λ_k fixed point |
| (5) §6 (JUMP-EQ) FALSE | CONFIRMED (DATA) | x31_rx32 (4fe9ec0e), 53 → 54, reproduced with my own code |
| (5) §6 A | PROVED part SIGN; DATA confirmed; OPEN part correctly labelled | L ≤ M_k at tame carries is immediate from the definition of tame; L = M_k at 201 of 201 in-phase evicting fallbacks (my a_check.py) |
| §7 DATA | reproduced byte-identically | All 12 lane logs re-generated from the lane's commands into my scratchpad: identical to the committed logs |
No statement is NOT SIGNED. No counterexample to any statement as used. G-N5-TIME, (J-poly), and A's "L ≥ M_k" stay OPEN.

## 1. VJ00 citations (opened by me)
- Jurdziński & Vöge, BRICS RS-00-48, pdf sha256 485a12de432a2a8c88640b0718bd2042d855fa86d6a82092a0d538fd41ba9e65. Pages below are the
  report's printed page numbers.
- p. 14, §5.2 "Strategy σ̄ for player ⊖": "σ̄(v) = w, such that Ωσ(w) ⊴ Ωσ(u) for all u ∈ succ(v)". ✓ as cited.
- p. 15, "Locally progressive valuation": Prog(Ξ, (v, w)) iff 1. Λ(v) = Λ(w); 2. if Λ(v) ≠ v then Π(v) =_{Λ(v)} Π(w) ⊕ v; 3. if
  Λ(v) = v then Π(v) ≅_{Λ(v)} Π(w) ⊕ v and Π(v) = (∅, 0).
  - The packet cites p. 14 (N-FB-1).
  - Its (P3) keeps only Π(v) = (∅, 0); that is all the packet uses.
- p. 15, Lemma 5.2: "A valuation Ξ is a locally progressive valuation for σ and τ if and only if Ξ = Θστ". The proof (pp. 15-16) shows that
  the cycle's max≤ vertex is Λ. ✓
- p. 16, (11): Ωσ = Θσσ̄, "Hence by definition of Ωσ we get that Θσσ̄ ⊴ Θστ, for all strategies τ". ✓
- Also relevant (used for G-FB-4): p. 14, (9) and (10). At a cycle node ℓ, Πσ(ℓ) ≅_ℓ Πσ(w) ⊕ ℓ for the chosen successor, and
  Πσ(ℓ) ⊴~_ℓ Πσ(u) ⊕ ℓ for all u. Both are comparisons up to length.

## 2. Claim (T) and COARSE-SI
### 2.1 (T): SIGN
- (i) (P1) on H_k-edges, plus the fact that COARSE_L with L < ∞ keeps the cycle node, gives λ_k constant along the H′-play. ✓
- (ii) The cycle top t has λ_k(t) = λ_k(v) = c and λ_k(t) = t, so t = c.
  - p_0..p_{s−1} precede the first visit of c. Cycle vertices other than c lie below c and add nothing to P.
  - So Θ_{H′}(p_i) = p_i ⊕ … ⊕ (c, ∅, 0), exactly. ✓
- (iii) For i < s, p_i ≠ c = λ_k(p_i), so Ξ_k(p_i) = p_i ⊕ Ξ_k(succ_{H_k} p_i) holds EXACTLY in si.py's representation.
  - If p_i is on its H_k-cycle, it comes after c on that cycle, so succ's path to c avoids p_i.
  - (C4) is correct: COARSE_L(u ⊕ x) = (c, (P ∩ V_{>L}) ∪ ({u} if rank u > max(rank c, L))).
  - The downward induction from (P3) at p_s is ✓.
- Mechanical: 306,304 direct (T) instances in the batch (51,126 with H′ ≠ H_k and a value change), and 1,766,872 in the climbs. Each
  uses a random L and a random H′ whose successors keep COARSE_L(Ξ_k) of H_k's. 0 failures. Plays whose cycle top is not a λ_k-fixed
  point are excluded, as the hypothesis requires.
### 2.2 COARSE-SI (a) and the converse: SIGN
- (E) at switched vertices: R15 (d) makes every switch a gate edge, of level ≤ L. ✓
- Ξ_k ⊴ Ξ_{k+1}: R15 (a). Ξ_{k+1} ⊴ V: VJ00 (11) with τ := σ̄_k. ✓
- (C1) holds in all three cases: different cycle nodes; top difference above L; otherwise equal. (C3) holds: rewards are injective and the
  top difference decides. So the coarse sandwich closes. ✓
- Converse: V(t) = (t, ∅, 0) at a bad top t, while λ_k(t) ≠ t, and L < ∞ keeps cycle nodes. ✓
- Mechanical:
  - (a) at every transition where (NC) holds, for both L = M_k and L = the max switched level (they differ in general): 10,246 checks
    (89,233 climbs), 0 failures.
  - The converse at every (NC) failure: 4,826 (19,923), 0 failures.
  - R15 (a) monotonicity and (11) (V ⊵ Ξ_{k+1}) at every transition: 0 failures.
### 2.3 TAME (b): SIGN
- M_k = ∞ and M_k = ⊥ are trivial (Ξ depends on σ only).
- Otherwise (T) with H′ = H_{k+1}:
  - (E) holds at switched Even vertices, at Odd vertices (by the hypothesis), and trivially elsewhere.
  - The cycle tops of H_{k+1} are λ_{k+1}-fixed points by Lemma 5.2, given Ξ_{k+1} = Θ_{H_{k+1}}.
  - λ_{k+1} = λ_k, and Θ_{H_{k+1}} = Ξ_{k+1}. ✓
- Code link. H_{k+1} uses SPEC's σ̄_{k+1}, i.e. si.py's choice, which at an own-cycle-node Odd vertex is FIX 2's DFS choice, not
  VJ00's minimiser (§5.2 below). Lemma 5.2 needs only Ξ = Θ_H for THAT H.
  - This is the R15 code link (G-N5T-1, DATA). I re-checked it: my own play-following of H_k equals si.py's Ξ_k at all 26,724 batch
    states and 52,824+ climb states.
- Mechanical: TAME's hypotheses held at 10,208 transitions (39,444+ in the climbs); tame at every one.

## 3. MONO and NOINF: SIGN
- MONO.
  - u's coarse value equals σ_k y's (gate target of level ≤ M, or unchanged).
  - A coarse-strict (y, z) at k would be a gate edge of level > M_k.
  - Tameness transports the ⊴_M to k+1, the gate at k+1 gives ⊵_M, and (C3) gives equality. ✓ The ⊥ and ∞ cases are ✓.
  - Mechanical: 15,314 tame transitions (106,208 in the climbs; phases or not), 0 rises of M. M rose at 684 non-tame transitions, so the
    tameness hypothesis is needed.
- NOINF. Correct. The two cases collapse into one chain: λ_k(σ_k y) = λ_k(y) [(P1) at k] = λ_{k+1}(y) [phase] = λ_{k+1}(z) [(P1) at k+1]
  = λ_k(z).
- G-FB-1 (the Consequence, used in FB step (2)). NOINF bounds the level of the SWITCHED edge (y, z*). M_k is a max over ALL gate edges.
  - The missing line: suppose a gate edge (y, z) of y had level ∞. Then reward(λ z) > reward(λ σ_k y), since it is strictly better with
    a different cycle node.
  - S4c's z* has Ξ_k(z*) ⊵ Ξ_k(z), so reward(λ z*) ≥ reward(λ z) > reward(λ σ_k y), and (y, z*) has level ∞, against NOINF. CLOSED.
  - Mechanical: 13,757 switches with λ unchanged (156,091 in the climbs), all of level < ∞. 635 in-phase fallbacks (26,060), all with
    M_k < ∞.

## 4. Theorem FB and Corollary
- Step (1):
  - σ_{i+1}(y) ∈ {σ_i y} ∪ gate targets of level ≤ M (R15 (d)).
  - Ξ_{i+1}(σ_{i+1} y) ⊵ Ξ_i(σ_{i+1} y) at level ≤ M (R15 (a); tame).
  - COARSE_M-equality is transitive, so COARSE_M(Ξ(σ y)) is constant and β is ⊴_{M−1}-non-decreasing. ✓
- Step (2):
  - The level of (y, z*) is exactly M: if it were < M, then COARSE_{M−1}(z*) = COARSE_{M−1}(σ_i y) ◁ COARSE_{M−1}(z), against
    Ξ_i(z*) ⊵ Ξ_i(z) by (C1). For M = −1, both levels are −1.
  - The strict rise of β follows. ✓
  - G-FB-1 applies to "M < ∞ by NOINF".
  - G-FB-2: "the fallback is Even's (… R21 (c) FBL-N (i))". R21 is signed in the 𝒞^1O setting, but §4 is claimed for every game.
    - The fact is immediate on any game: an Odd fallback (Iσ = ∅) switches some Odd vertex to an improving edge w ≠ τ(v)
      (SPEC S4c, FIX 3), so τ changes. That is impossible in a phase.
    - Hence Iσ_i ≠ ∅ and the fallback is Even's. CLOSED.
- Step (3):
  - M ≥ 0: with COARSE_M fixed, β is determined by whether the rank-M vertex is in P, so it has ≤ 2 values.
  - M = −1: β moves only in its length ∈ [0, n − 1].
  - So ≤ n_E and ≤ n_E(n − 1) fallbacks per block. ✓
- Step (4):
  - By MONO, each value occurs in at most one block per tame run.
  - ∞ and ⊥ blocks have no fallbacks (G-FB-1; Iσ = ∅).
  - Σ = n·n_E + (n − 1)·n_E = n_E(2n − 1) per run, ≤ J + 1 runs, plus the J non-tame transitions. ✓
- Corollary:
  - W-lowering transitions are fallbacks (WM).
  - (C) reversals are transitions (R23: a reversal is a crossing transition; a drain counts once), so (C) ≤ #fallbacks. ✓
  - G-FB-3: R23 (g) WM is signed on 𝒞^1O. On a general game the same argument holds: in a phase τ is fixed, an S4a step returns an
    arena optimum of G_τ that dominates σ_k (R17 (F1), a one-player statement). CLOSED.
  - Mechanical: "W drops only at fallbacks" holds on general games too (0 failures).
- Mechanical, per phase:
  - Batch: 1,954 phases, 635 in-phase fallbacks, all tame. β is monotone and COARSE_M(Ξ(σ y)) constant in every block. Every tame
    fallback has a strict β-rise. Block caps, per-run caps, FB totals and Corollary totals all hold. No value repeats as a block level
    in a tame run. 0 violations.
  - Climbs (fb_climb.py, 4 seeds from the named set, objective = max fallbacks in one block, J, fallbacks per phase): 9,600 runs,
    113,768 transitions, 26,060 in-phase fallbacks, 0 violations.
  - Max fallbacks in one block: 25 (named) and 15 (climbs).
  - Max J per phase: 3 (batch) and 2 (climbs). My climbs did not reach the lane's post-packet J 9-13. The bound is far from tight in
    all data: n_E(2n − 1) ≥ hundreds against ≤ 25.

## 5. §5 on 𝒞^1O
### 5.1 J1, OFF, the Remark: SIGN
- J1: TAME's contrapositive. On 𝒞^1O every Odd u ≠ o is forced, and in a phase λ_{k+1} = λ_k. So the only way TAME's hypothesis can fail
  is lev(a, b) > M_k (then b ≠ a). M_k ∉ {⊥, ∞} for a non-tame transition. ✓
- OFF:
  - v ∉ R̄_{k+1} means v's H_{k+1}-play avoids o. This is independent of Odd's choices, since o is the only Odd choice.
  - (E) holds along that play (switches have level ≤ M_k; the other Odd vertices are forced).
  - Its cycle top is a λ_{k+1} = λ_k fixed point (Lemma 5.2). (T) applies to v alone. ✓
- Remark: the packet does not say why the bad cycle must pass o. The line: H′ = (σ_{k+1}, σ̄_k) and H_{k+1} differ only at o. A bad
  cycle avoiding o is a cycle of H_{k+1}, whose top is a λ_{k+1} = λ_k fixed point, so it is not bad. ✓
- Mechanical:
  - J1 at 107 in-phase non-tame transitions on 𝒞^1O (2,727 in the climbs).
  - OFF: 118,391 vertex checks (1,946,911).
  - Remark: a bad cycle through o at every non-tame transition.
  - 0 failures.
### 5.2 CAP: SIGN WITH GAPS (G-FB-4)
- The proof uses "b minimises Ξ_{k+1} over succ(o) (VJ00 p. 14)" and "the minimality of a". VJ00's σ̄ is by definition a minimiser.
  SPEC's σ̄ is si.py's, which differs at an Odd vertex that is its own cycle node: there it is FIX 2's DFS choice (the first cycle back
  through lower ranks).
  - Instance: general701 #16, state 2, Odd u = 8 (Ω 4, its own cycle node), succ {1, 6}.
  - σ̄(8) = 1 with Ξ(1) = (8, ∅, 1), while Ξ(6) = (8, ∅, 2) is smaller for Even (even cycle node: longer is worse).
  - So VJ00's minimiser is 6 and SPEC's choice is 1.
  - Batch: 1,228 such vertex-states (232 more in the climbs), all at own-cycle-node Odd vertices. At non-cycle-node Odd vertices
    si.py's σ̄ was a full minimiser in all 111,062 batch cases (DATA).
- Closure: CAP uses the minimality only through COARSE_M with M ≥ −1, and COARSE_{−1} drops lengths.
  - At an own cycle node o, Prog clause 3 on the H-edge (o, b) gives λ(b) = o and Π(b)'s set = ∅ (via Ξ = Θ_H, the code link of §2.3).
  - VJ00 (10) (or optimality of the honest value) gives COARSE_{−1}(Ξ(u)) ⊵ (o, ∅) for every u ∈ succ(o).
  - So the DFS choice is a COARSE_{−1}-minimiser, hence a COARSE_M-minimiser for every M ≥ −1.
  - Both inequalities of CAP's proof hold at the coarse level, which is all that is used: COARSE_M(Ξ_k b) ⊵_M COARSE_M(Ξ_k a), strict by
    J1, and COARSE_M(Ξ_{k+1} e) ⊵_M COARSE_M(Ξ_{k+1} b). CLOSED.
  - DATA: the coarse-minimiser property held at all 1,228 + 232 own-cycle-node cases.
- Context: no in-phase non-tame transition with λ(o) = o occurred in my data (0 of 107 + 2,727). The repair is needed for the proof as
  written, not for any observed case.
- Mechanical: 696 CAP exit checks (34,033 in the climbs), 0 failures.

## 6. §6: (JUMP-EQ) and A
- (JUMP-EQ), as stated in N5-C-box5.md §6.2 ("inside a phase with w constant, if an INR at k → k+1 raises θ at a level above the level of
  the most recent carry, then θ_{k+1} = w"). The lane's jumpeq.py encodes exactly this. FALSE: CONFIRMED with my own code.
  - x31_rx32.pg (sha1 4fe9ec0ea39ea30df855c3738b8e0fdd08e621bc). One Odd choice vertex, o = 0. n5.py: 55 iterations, 3 fallbacks
    (24, 38, 51). check_sol2.py: "zielonka(oink zlk) OK strategies verified".
  - The phase spans states 2-55, and w = (30, …) with key (36, −1040187392, −4) is constant throughout.
  - The last carry before 53 is fallback 51: W-lowering, leaver 21, L = 24 (= M_51).
  - At 53 → 54: σ̄(o) 24 → 31. (NC) fails (my play-following of (σ_54, σ̄_53)). θ's change level is 25 > L.
  - θ_53 key (36, −2146959360, −16) and θ_54 key (36, −2113929216, −4), as the packet says. (h) holds at 54 (my re_check analyse) and
    θ_54 ≠ w_54.
  - At 54 → 55: σ̄(o) → 9 = τ(o) and θ_55 = w.
  - jumpeq.py over the named set: 10 hypothesis cases, 9 with θ_{k+1} = w (re-run, byte-identical log).
- A.
  - PROVED part: at a tame transition every Ξ(v) has lev(Ξ_k v, Ξ_{k+1} v) ≤ M_k (the definition of tame), so L ≤ M_k. ✓
  - DATA (my a_check.py, own code): 201 in-phase evicting fallbacks in the named set, all tame, L = M_k at all 201 (= the lane's
    jump.py).
  - OPEN: "L ≥ M_k" in general, correctly labelled.

## 7. Reproduction and my batch
- The lane's run_all.sh commands, re-run with output to my scratchpad (the lane's log directory left untouched): all 12 logs
  byte-identical to the committed experiments/si/coarse/logs/ (dpot, fb ×5, jump, jumpeq, mono ×3, tame).
- My batch (run_all.sh; logs/totals.txt; 57 logs, all RESULT OK, 0 violations):
  - general games: seeds 731 (3,000, n 4-12) and 732 (1,000, n 12-20);
  - random 𝒞^1O (RC.rand_game, o-cyclic 70%): seeds 733 (3,000, n 6-14) and 734 (1,000, n 14-24);
  - the 53-file named set, S3 start + 4 random starts each, one-o asserted;
  - totals: 8,265 runs, 18,459 transitions, 834 fallbacks, 1,954 phases.
- My run loop is asserted equal to n5.run's (iterations, fallbacks) on every run.

## 8. Gap list
| id | where | status |
| --- | --- | --- |
| G-FB-1 | §3 NOINF Consequence / §4 step (2): "M_k < ∞" from a bound on the switched edge only | CLOSED (best-target line, §3) |
| G-FB-2 | §4 step (2): R21 (c) FBL-N (i) is signed on 𝒞^1O; §4 claims every game | CLOSED (SPEC S4c + FIX 3) |
| G-FB-3 | §4 Corollary: R23 (g) WM is signed on 𝒞^1O | CLOSED ((F1) in G_τ, any game); (C) is 𝒞^1O-only anyway |
| G-FB-4 | §5 CAP: SPEC's σ̄ at an own-cycle-node o is not VJ00's minimiser | CLOSED (coarse minimality suffices; instance §5.2) |
| N-FB-1 | §0: Prog is on VJ00 p. 15 | nit |

## DONE / FINDINGS / NEEDS
DONE (Opus 5.5, D15).
- Report: docs/referee-2/R2-N5-FB.md. Tools: docs/referee-2/R2-N5-FB/.
- Verdicts:
  - Theorem FB: SIGN WITH GAPS (G-FB-1, G-FB-2, closed).
  - Corollary: SIGN WITH GAPS (G-FB-3, closed).
  - (T), COARSE-SI (a) + converse, TAME, MONO, NOINF, J1, OFF, Remark: SIGN.
  - CAP: SIGN WITH GAPS (G-FB-4, closed).
  - (JUMP-EQ) FALSE: confirmed. A: PROVED part signed, DATA confirmed.
  - §7: reproduced byte-identically.
- Evidence:
  - Batch: 8,265 runs; climbs: 9,600 runs; 0 violations.
  - x31_rx32: n5.py 55/3; Oink zlk + check_sol2.py OK.
FINDINGS
- SPEC's σ̄ (FIX 2 DFS) is not VJ00's p. 14 minimiser at own-cycle-node Odd vertices (1,228 cases). CAP survives because it is
  coarse. Any future proof citing "σ̄ minimises Ξ" should say "up to length at cycle nodes".
- §2-§4 are general-game statements, but two cited results (R21 (c), R23 (g)) are signed on 𝒞^1O. Both transfer in one line.
- Data is far from FB's bound (≤ 25 fallbacks per block, J ≤ 3). (J-poly) is untouched.
NEEDS
- Lead: route G-FB-1..4 and N-FB-1 to L-SI's fixes file for P-N5-FB.
- Lead: tell me when REFEREE's R-N5-FB is pushed, for §C.
