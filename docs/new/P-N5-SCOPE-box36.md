# Referee packet P-N5-SCOPE: the phase key (Remark KEY), w-changes under H2 (WCH), scope runs per phase (SCOPE-COUNT), fallbacks between crossings (FB-INT, NH1-FB), and the own-cycle-node level −1 fallback (CN-LAST) (box 36)
L-NEW successor 16 (Opus 5.5, D15/D18), session_01LLCK4ctQmkMq2huT44SU7d. Written 2026-10-25 10:4xZ by date -u (clock 10:42:43Z), at the
Lead's GO for box 37 (10:34Z, Lead's stamp). Frozen at this commit: corrections go in a fixes file, never here.
- Self-contained. It gives the definitions, the statements, full proofs, the location and status of every dependency, the data, and the
  scripts that produce the data.
- Source texts:
  - docs/new/N5-SCOPE-box36.md §1-§7 (sha1 7496a2c3…, as of l-new a670161b), for KEY, WCH, SCOPE-COUNT, FB-INT, NH1-FB and the open part;
  - docs/new/N5-DROP-box35.md §7 (sha1 e3a4e7be…), for CN-LAST.
  Where they differ, this packet governs. The proofs are successor 15's. This successor checked them line by line against the cited
  statements, and filled in steps the working text left implicit; each such step is marked "(filled in)".
- Labels (D18/L40): PROVED (L-NEW succ. 15, unrefereed), CONJECTURE, FALSE, OPEN, DATA.
- Scope of the claims:
  - every statement is about the candidate N5, inside a phase;
  - CN-LAST and Remark KEY hold on every game; WCH, SCOPE-COUNT, FB-INT and NH1-FB are on 𝒞^1O.
  - Nothing here is a running-time bound for N5, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.
- What to sign:
  - §1-§6 are to be signed.
  - §7 is NOT TO SIGN. It holds the open out-of-SN fallbacks, the exact obstruction, CONJECTURE OUT-POLY, and the dead end "linear PF-THETA".
  - §8 is data.
- Citation correction against the source. N5-SCOPE-box36.md §3 cites R-CONST as "P-N5-L2 §11". This is the same slip as TOG-2 / N-TOG-1.
  R-CONST is P-N5-L2 §5 (it will be RESULTS R33 (e); draft in docs/agents/R33-draft.md).

## 0. Objects, notation and dependencies
- N5 is as specified in docs/new/N5-ssi-global.md, SPEC S1-S5.
  - S4a is Even's arena step and S4b Odd's.
  - S4c is the fallback. If Iσ ≠ ∅, EVERY Even v with an improving edge sets σ(v) to the w with (v, w) ∈ Iσ that maximises (Ξσ(w), w);
    ties go to the larger index (FIX 3: τ unchanged). Otherwise Odd does the same on Iτ.
  - S5: stop when Iσ = Iτ = ∅.
- Valuations x = (c, P, ℓ) and Even's order ⊴ / ◁ are VJ00's (SPEC S1). The order compares:
  - first, the cycle-node reward;
  - then P, by the injective signed weight Σ_{u∈P} ±2^rank(u), with weight(∅) = 0;
  - then the length: shorter is better for Even if Ω(c) is even, longer if Ω(c) is odd.
- lev(a, b) is the level at which a and b first differ. Level −1 means the same cycle node and the same P, with a different length.
  COARSE_L, (C1)-(C7) are as in R25 / R27.
- Honest frame:
  - Ξ_k := Ξ_{σ_k}, Even's valuation of σ_k against Odd's optimal counterstrategy σ̄_k (SPEC S1);
  - H_k is the (σ_k, σ̄_k)-graph; next_k(v) := σ_k(v) for Even v and σ̄_k(v) for Odd v;
  - λ_k(v) := the cycle node of Ξ_k(v); a cycle node c has Ξ(c) = (c, ∅, 0).
- Odd's side (SPEC S1, "Odd's side"):
  - U_k := Ξ^d_{τ_k}, the valuation of τ_k on the dual game G^d against τ̄_k, Even's optimal counterstrategy to τ_k;
  - λ_U is its cycle-node map.
- 𝒞^1O: exactly one Odd vertex o has out-degree > 1, so τ is determined by τ(o).
  - W_k := the value of the (σ_k, τ)-play, in the one-player game G_τ.
  - θ := Ξ(o), w := W(o).
- Sets (P-N5-FRZ §0, pinned 25fda0f; = R19 / R21 setting):
  - R_k := {v ≠ o : v's (σ_k, τ)-play reaches o};
  - R̄_k := R_k ∪ {o};
  - F_k := V ∖ R̄_k, so o ∉ F_k and |F_k| ≤ n − 1.
  - A CROSSING is an in-phase transition with R_{k+1} ≠ R_k. X := #crossings of the phase. A CROSSING-FREE INTERVAL is a maximal run of
    states of a phase with R constant (R22).
- PHASE (R27 / R28; P-N5-SN §0): a maximal run of consecutive states with λ_Ξ and τ constant. A JOINT λ-PHASE (R21, P-N5-X §0) is one with
  λ_Ξ, λ_U and τ constant. "A transition of the phase" has both ends in the phase (R25 FB-2).
- Within a phase:
  - c_θ := λ(o) is constant. U := λ^{-1}(c_θ) is constant too (it is also written U in P-N5-L2 / P-N5-TOG; it is unrelated to the
    valuation U_k above).
  - c_w := λ_W(o), the cycle node of w.
  - H1: o lies on no honest cycle. H2: o lies on no W-cycle. H3: c_w = c_θ. (h) := H1 ∧ H2 ∧ H3.
  - An H1-TOGGLE is a transition at which H1 changes; a DROP is one from H1 to ¬H1.
- T := the number of H1-toggles of the phase, f := its number of S4c fallback transitions, n_E := #Even vertices.
- A SCOPE RUN (R29 §0) is a maximal run of in-phase transitions k → k+1 with (h) at k, H2 at k+1 and w_{k+1} = w_k. An (h)-RUN is a
  maximal run of consecutive (h) states of the phase.
- M_k := the max gate-edge level at k. A transition is TAME if COARSE_{M_k}(Ξ) is unchanged across it. J := #non-tame transitions.
  A TAME RUN is a maximal run of consecutive tame transitions of the phase (R25).

### Dependencies (statement used / where it lives / status)
| tag | statement used | location | status |
| --- | --- | --- | --- |
| R15 (a) | Ξ_k ⊴ Ξ_{k+1} at every transition (VJ00 Lemma 5.7 on the unambiguous switch set), fallbacks included | RESULTS R15 (a) | LANDED |
| R15 (d) | σ_{k+1}(v) ∈ {σ_k(v)} ∪ Iσ_k(v); every N5 iteration changes σ or τ | RESULTS R15 (d) | LANDED |
| S (a) | Ξ_σ = L_σ is the pointwise minimum of V_{σ,τ′} over Odd's strategies τ′ (VJ00 (11)) | RESULTS R18 (d), Lemma S (a) (docs/new/N5-time-box21.md §2.2) | LANDED |
| G (a) | off R̄, Ξ = W, with no (h) needed | RESULTS R19 (a) Lemma G | LANDED |
| F1° | on a crossing-free interval (OTHER states included), Ξ changes at some vertex of F at ≤ max(0, |F| − 1) transitions | RESULTS R22 (a) | LANDED (joint λ-phase key; see §1) |
| TC (i) | H2 ⟺ τ(o) ∈ F (statewise; constant on a crossing-free interval) | RESULTS R22 (b) | LANDED |
| FB | per tame run ≤ n_E(2n − 1) fallbacks (proof of Theorem FB, steps (1)-(4)); hence ≤ n_E(2n − 1)(J + 1) + J per phase | RESULTS R25 (d); proof in docs/si/P-N5-FB-box7.md §4 (sha1 9ece9994…) | LANDED |
| J1 | a non-tame transition switches σ̄(o) at a level > M_k | RESULTS R25 (e); P-N5-FB §5 | LANDED |
| OE / OX (ii) | no crossing ⇒ O_k ≤ E_k; every non-tame transition is a crossing (OX (ii)'s proof) | RESULTS R28 (b), (c) (ii); proof in docs/new/P-N5-OE-box32.md §2-§3 (sha1 adeccd89…) | LANDED |
| R-CONST | at every ¬H1 state of a phase, R̄_k = U | docs/new/P-N5-L2-box34.md §5 (sha1 cbea0739…; signed by both referees) | IN LANDING (RESULTS R33 (e) draft, CHECKER C42) |
| (F) | if x lies on the cycle of c's H_k-play and λ_k(c) = c, then Ξ_k(x) = (c, ∅, dist_k(x → c)); if x ≠ c has λ_k(x) = c, then Ξ_k(x) = x ⊕ Ξ_k(next_k x) | docs/new/P-N5-TOG-box35.md §0 (sha1 7dfda8c8…) | P-N5-TOG, IN REVIEW (signed by REFEREE-2 faabe716; REFEREE fff6e624 uses it in its §0) |
| TOGGLE-COUNT | T ≤ |U|(n + 1) + n − 1 ≤ n² + 2n − 1; drops ≤ ⌈T/2⌉; T = 0 if c_θ = o | P-N5-TOG §4 | P-N5-TOG, IN REVIEW (SIGNED by both referees) |
| RESTARTS | (h)-runs per phase ≤ 1 + T + f | P-N5-TOG §6 (premises H2-STICK, H3-CONST from P-N5-L2 §1-§2; H3H2 from RESULTS R30 (d)) | P-N5-TOG, IN REVIEW (SIGNED by both); premises IN LANDING (R33) / LANDED (R30) |
| (V1) | if λ(v) ≠ v then the value of v is v ⊕ (value of its successor on the play) | VJ00 BRICS RS-00-48 §4.2, as used in R17 / R20; the same fact as (F)'s second clause, on any one-player graph | VJ00 (source opened by the lane and both referees, R15) |

- Item → dependencies:
  | item | depends on |
  | --- | --- |
  | §1 Remark KEY | SPEC S1 only |
  | §2 Lemma WCH | (V1), G (a), TC (i), F1°, KEY |
  | §3 Corollary SCOPE-COUNT | WCH, RESTARTS (P-N5-TOG) |
  | §4 Lemma FB-INT | FB, J1, OE / OX (ii), R15 (d), KEY |
  | §5 Corollary NH1-FB | FB-INT, R-CONST (P-N5-L2), TOGGLE-COUNT (P-N5-TOG) |
  | §6 Lemma CN-LAST | SPEC S4c / S4a / S4b / S5, (F) (P-N5-TOG §0), S (a), R15 (a) |

## 1. Remark KEY (PROVED, L-NEW succ. 15; every game)
Statement. λ_U, the cycle-node map of U_k = Ξ^d_{τ_k}, is a function of τ_k alone. Hence on every run of states with τ constant, λ_U is
constant. A (λ_Ξ, τ)-phase is therefore exactly a joint λ-phase (λ_Ξ, λ_U, τ), and every result signed on joint λ-phases with τ constant
holds verbatim on (λ_Ξ, τ)-phases.
Proof.
- By SPEC S1, Odd's side: Ξ^d_τ and τ̄ are computed on G^d from τ, read as G^d's Even strategy, by the deterministic S1 procedure. The input
  is G^d and τ; σ does not enter. So U_k and λ_U are functions of τ_k.
- Any run with τ constant therefore has λ_U constant. So "λ_Ξ and τ constant" and "λ_Ξ, λ_U and τ constant" pick out the same maximal runs. □
- Use in this packet: F1° and TC (R22) and FB / J1 (R25) are signed on joint λ-phases with τ constant, and apply here by KEY. R28 / R31
  each argued this transfer case by case (N-OE-3; the NL note in R32 (SUB)); KEY makes those arguments one line.
- DATA: scopecnt.py checks λ_U at every transition with τ(o) unchanged. It found 0 changes in 1,419 library phases and 39,777 random
  phases (§8).

## 2. Lemma WCH (PROVED, L-NEW succ. 15; 𝒞^1O)
Statement. Let k → k+1 be a transition of a phase, with H2 at k and at k+1, and w_k ≠ w_{k+1}. Then either k → k+1 is a crossing, or
Ξ_k(t0) ≠ Ξ_{k+1}(t0) for t0 := τ(o) ∈ F_k = F_{k+1}. Hence such transitions number ≤ (n − 2)(X + 1) + X per phase.
Proof.
- t0 is the same vertex at k and k+1, since τ is constant in a phase.
- (filled in) TC (i), statewise.
  - Suppose t0 ∈ R̄_k. Then t0's (σ_k, τ)-play reaches o, and o's play is o followed by t0's, so o lies on a W-cycle (this includes t0 = o).
  - Conversely, if t0 ∈ F_k, then t0's play avoids o, and o is not on the cycle it ends in.
  - So H2 ⟺ t0 ∈ F_k.
- Under H2, o is not a cycle node of W (o is on no W-cycle). By (V1) in G_τ, w = W(o) = o ⊕ W(t0).
- t0 ∈ F, and off R̄, W = Ξ (G (a)). So w_k = o ⊕ Ξ_k(t0) and w_{k+1} = o ⊕ Ξ_{k+1}(t0).
- So w is a function of Ξ(t0). If Ξ_k(t0) = Ξ_{k+1}(t0), then w_k = w_{k+1}. Hence w_k ≠ w_{k+1} forces Ξ_k(t0) ≠ Ξ_{k+1}(t0).
- Count. Suppose the transition is not a crossing. Then R_k = R_{k+1}, so it lies inside one crossing-free interval I, and t0 ∈ F (F is
  constant on I).
  - By F1° (on (λ_Ξ, τ)-phases by KEY), at most max(0, |F| − 1) ≤ n − 2 transitions of I change Ξ at a vertex of F.
  - A phase with X crossings has ≤ X + 1 crossing-free intervals, and the crossings themselves add ≤ X. □

## 3. Corollary SCOPE-COUNT (PROVED, L-NEW succ. 15; 𝒞^1O; uses RESTARTS from P-N5-TOG)
Statement. The scope runs of a phase number ≤ #(h)-runs + #WCH ≤ (1 + T + f) + (n − 2)(X + 1) + X.
Here #WCH counts the transitions of §2: H2 at both ends, w changing.
Proof.
- Let a scope run start with the transition k → k+1. Then (h) holds at k.
- (filled in) Distinct scope runs start at distinct k. Two scope runs are disjoint maximal runs of transitions, so their first
  transitions differ.
- Case 1: k is the first state of its (h)-run. Each (h)-run has one first state, so this case gives ≤ #(h)-runs scope runs.
- Case 2: k − 1 is a state of the phase with (h).
  - Then k − 1 → k is an in-phase transition with (h) at k − 1 and H2 at k, since (h) at k gives H2 at k.
  - By maximality of the scope run, k − 1 → k is not in a scope run. The only failing clause is w_k = w_{k−1}, so w_{k−1} ≠ w_k.
  - (h) at k − 1 gives H2 at k − 1, so k − 1 → k is a WCH transition.
  - The map from case-2 scope runs to their WCH transition k − 1 → k is injective.
- (h)-runs ≤ 1 + T + f by RESTARTS (P-N5-TOG §6). With §2, the bound follows. □

## 4. Lemma FB-INT (PROVED, L-NEW succ. 15; 𝒞^1O)
Statement. Inside a phase, let Q be a maximal run of consecutive transitions, none of which is a crossing. Then Q contains
≤ n_E(2n − 1) S4c fallback transitions.
Proof.
- Every non-tame transition of a phase is a crossing. This is the proof of R28 (c) (ii) (docs/new/P-N5-OE-box32.md §3 (ii)):
  - by J1, a non-tame transition switches σ̄(o) at a level > M_k;
  - that change is relevant (P-N5-LP §4 step 3: an own-cycle-node change of σ̄(o) leaves the transition tame), so O_k > M_k;
  - Even switches go along Iσ (R15 (d)), to edges of gate level ≤ M_k, so E_k ≤ M_k < O_k;
  - by OE (R28 (b)), a transition without a crossing has O_k ≤ E_k; so the transition is a crossing.
- So every transition of Q is tame, and Q lies inside one tame run.
- FB's proof (P-N5-FB §4, steps (1)-(4)) bounds the S4c fallback transitions of any one tame run by n_E(2n − 1):
  - step (3): a block of level M ≥ 0 has ≤ n_E fallbacks, and a block of level −1 has ≤ n_E(n − 1);
  - step (4): one block per level value along a tame run (MONO), and none at ∞ or ⊥.
- Q has at most that many. □
- Remark. This is the per-run form of R25 Theorem FB. The phase total n_E(2n − 1)(J + 1) + J is FB's union over the ≤ J + 1 tame runs.
  FB-INT replaces "tame run" by "crossing-free stretch", which is coarser and is what the counts below need.

## 5. Corollary NH1-FB (PROVED, L-NEW succ. 15; 𝒞^1O; uses R-CONST from P-N5-L2 and TOGGLE-COUNT from P-N5-TOG)
Statement. The S4c fallback transitions k → k+1 of a phase with ¬H1 at k number ≤ n_E(2n − 1)(⌈T/2⌉ + 1) + T ≤ poly(n). The bound has
no X term and no f term.
Proof.
- Case A: ¬H1 at k and at k+1.
  - The transition lies inside a maximal run S of consecutive ¬H1 states of the phase.
  - By R-CONST, R̄ = U at every state of S, so no transition inside S is a crossing.
  - So the transitions inside S lie in one maximal crossing-free run Q, and FB-INT gives them ≤ n_E(2n − 1) fallbacks.
  - (filled in) Count of the runs S. Every maximal ¬H1 run except possibly the first state's begins with a drop. Drops ≤ ⌈T/2⌉
    (TOGGLE-COUNT), so there are ≤ ⌈T/2⌉ + 1 runs S.
  - If c_θ = o, then ¬H1 holds at every state, T = 0, and there is one run.
- Case B: ¬H1 at k and H1 at k+1. The transition is an H1-toggle, and there are ≤ T of these.
- With T ≤ n² + 2n − 1 (TOGGLE-COUNT) the total is poly(n). □

## 6. Lemma CN-LAST (PROVED, L-NEW succ. 15; every game)
Statement. Let k → k+1 be an S4c fallback at which Even switches (Iσ_k ≠ ∅), and suppose every gate (y, z) ∈ Iσ_k has λ_k(y) = y and
lev(Ξ_k(σ_k y), Ξ_k(z)) = −1. Then:
- (i) Ξ_{k+1} = Ξ_k;
- (ii) Iσ_{k+1} = ∅;
- (iii) k + 1 is the last state of its phase: the next iteration changes τ, or N5 stops (S5).
So a phase has at most one such fallback, and it is the phase's last transition.
Proof.
- Setup.
  - S4c switches exactly the gate tails, which are own cycle nodes c_1, …, c_p (pairwise distinct). It sends each c_i to z_i, its best
    gate target by (Ξ_k, index).
  - By (F), with λ_k(c_i) = c_i: Ξ_k(σ_k c_i) = (c_i, ∅, L_i − 1), where L_i is the length of c_i's honest cycle.
  - Level −1 gives Ξ_k(z_i) = (c_i, ∅, d_i), with d_i strictly better than L_i − 1 for Even.
  - So z_i's H_k-play reaches c_i.
  - It meets no other c_j first. c_j's H_k-play is its own cycle, topped by c_j, so passing c_j would give z_i the cycle node c_j ≠ c_i.
  - All vertices on z_i's path to c_i are less relevant than c_i, since P = ∅.
- (i) Let σ′ := σ_{k+1}, and σ̄ := σ̄_k. Compare the (σ′, σ̄)-plays with the (σ_k, σ̄)-plays. σ′ and σ_k differ only at c_1, …, c_p.
  - A play that meets no c_i is unchanged.
  - Now take a play that meets some c_i first at c_i.
    - It agrees with the old play up to c_i, because no switched vertex lies before c_i.
    - (filled in) After c_i it runs c_i → z_i → … → c_i, along z_i's old path. That path meets no c_j (Setup), so σ′ = σ_k on it.
    - The resulting cycle is topped by c_i (Setup). The old play was on c_i's old cycle, also topped by c_i.
    - A value counts the cycle node, P and the length up to the first visit of the cycle node. All three are read on the common prefix,
      so the value is the same.
  - Hence V_{σ′, σ̄} = Ξ_k pointwise.
  - Ξ_{k+1} is the pointwise minimum over Odd's strategies (S (a)), so Ξ_{k+1} ⊴ V_{σ′, σ̄} = Ξ_k.
  - R15 (a) gives Ξ_k ⊴ Ξ_{k+1}. Hence Ξ_{k+1} = Ξ_k.
- (ii) Iσ_{k+1} is empty at every Even vertex.
  - Take an Even vertex that is not switched.
    - (filled in) S4c switches every Even vertex with an improving edge, so this vertex had Iσ_k(v) = ∅.
    - σ(v) and Ξ are unchanged, by (i). So Iσ_{k+1}(v) = Iσ_k(v) = ∅.
  - Take c_i, and suppose (c_i, w) ∈ Iσ_{k+1}.
    - Then Ξ_k(w) = Ξ_{k+1}(w) ▷ Ξ_{k+1}(z_i) = Ξ_k(z_i) ▷ Ξ_k(σ_k c_i).
    - So w ≠ σ_k(c_i) and (c_i, w) ∈ Iσ_k, with a value strictly above z_i's. This contradicts the choice of z_i.
- (iii) Iσ_{k+1} = ∅, so S4a does nothing at k + 1. There are three cases:
  - Iτ_{k+1} = ∅: N5 stops (S5).
  - S4b returns a new τ: τ changes.
  - S4b returns τ unchanged: σ is unchanged too, so the S4c fallback runs. It is Odd's, since Iσ = ∅, and sets τ(v) to an improving
    target: τ changes.
  - τ is part of the phase key, so k + 1 is the last state of the phase. □
- Remark. The converse direction is R15 (b): a switch set that leaves Ω unchanged consists of length-only switches at cycle nodes. CN-LAST
  is the forward direction for the S4c switch set, together with its consequence for N5's control flow.
- Consequence for the open count (READING). The level −1 fallbacks of a phase are ≤ 1 + (level −1 fallbacks with a gate at a non-cycle
  node). The second term has 1 case in all data (§7.3).

## 7. NOT TO SIGN: the out-of-SN fallbacks (OPEN), CONJECTURE OUT-POLY, and the dead end "linear PF-THETA" (FALSE)
### 7.1 Classification of in-phase fallbacks (DATA, scopecnt.py)
| kind | library | random (20,000 games, n 4-14, seed 3561) | counted by |
| --- | --- | --- | --- |
| IN (inside a scope run) | 898 | 334 | (L1) scope-run machinery: NJB / MINSET (L-SI, L-RED); OPEN |
| ¬H1 at k (NH1) | 11 | 338 | §5, PROVED |
| H1 ∧ ¬H2 at k | 107 | 0 | OPEN (§7.2) |
| OTHER, H1 ∧ H2 ∧ ¬H3 at k | 2 | 0 | OPEN (§7.2) |
| END: (h) at k, ¬H2 at k+1 | 4 | 29 | k is the last state of its (h)-run: ≤ #(h)-runs ≤ 1 + T + f (RESTARTS) |
| END: (h) at k, w changes | 0 | 0 | a WCH transition: ≤ (n − 2)(X + 1) + X (§2) |

### 7.2 The out-of-SN fallbacks: exact obstruction (OPEN)
- The states. Fallbacks at H1 ∧ ¬H2 states and at OTHER states (H1 ∧ H2 ∧ ¬H3).
  - In both, c_w ≠ c_θ. Under H1 ∧ ¬H2, c_w ∈ R̄ (o is on its W-cycle), while c_θ ∈ F (R30 (d), proof of H3H2). OTHER is ¬H3 by definition.
  - So these states are outside the SN regime (c_w = c_θ).
- The loop (READING). Outside SN, R only grows at S4a steps (R30 (c) R-STICK), and fallbacks can evict. FB-INT gives ≤ n_E(2n − 1) such fallbacks
  per crossing-free stretch, so
  - f_out ≤ n_E(2n − 1)(X_out + 1), and
  - X_out ≤ (n − 1)(f_out + 1) + f_out (SN-PREFIX type count per fallback-free run).
  This is the f ↔ X loop of (L1) again, without (h). So u*, NL, CLS1, MINSET and NJB do not apply.
- EXACT OBSTRUCTION. FB's per-tame-run count resets at every crossing. In this regime, crossings are only re-entries after fallback
  evictions. Nothing proved charges an eviction-then-re-entry pair to a monotone quantity.
- The cleanest case is τ(o) = o, which covers 91 of the 104 H1 ∧ ¬H2 fallbacks in box 35's survey (fbtau.py). There w = (o, ∅, 0) is
  constant, so the W frame is a fixed-target "reach o" game, played against "reach c_θ" in the honest frame.
- DATA: wd16_s2 (experiments/new/box25/instances/wd16_s2.pg, sha1 b71ddf0f…, n 16, τ(o) = o) has 12 such fallbacks in one phase, with
  X = 12 and T = 0. Random games: none.

### 7.3 Level −1 fallbacks with a non-cycle-node gate (OPEN)
- What is proved:
  - FB step (3): ≤ n_E(n − 1) per level −1 block, hence per tame run, and by FB-INT per crossing-free stretch;
  - CN-LAST (§6): the own-cycle-node case.
- The only example is experiments/new/box28/out/oc12_s1.pg (sha1 43ec8f09…; n 12; n5 10 iterations / 1 fallback; Oink zlk OK, strategies
  verified). At k = 6:
  - states 5-7 have M = −1, with length-only gates at non-cycle nodes (0 → 7, then 7 → 8); their cycle node 1 is odd;
  - all are ¬H1 states, so §5 counts them.
- A per-scope-run count would need that a level −1 block is not re-entered after a crossing. The same reset as in §7.2 blocks it.

### 7.4 CONJECTURE OUT-POLY (DATA only)
- Statement: the fallbacks at H1 ∧ ¬H2 and OTHER states of a phase are poly(n).
- Climbs (outclimb.py, 25 min each; fitness = (max out-of-SN fallbacks in one phase, crossings in that phase)):
  - seed 3631 from wd16_s2: (12, 12) → (12, 21) after 386,754 mutations;
  - seed 3632 from wd12_s1 (experiments/new/box25/instances/wd12_s1.pg, sha1 500a10ef…): (7, 7) → (7, 13) after 683,765 mutations.
- Only the crossings grew. This is weak evidence for a linear constant. The climb bests are in out/ (gitignored) and were not copied, since
  they show no new maximum.

### 7.5 DEAD END: "linear PF-THETA" (≤ n θ-changes under one fallback level) is FALSE (DATA, verified)
- Instance: experiments/red/so/instances/pftheta_cex_n32.pg (sha1 9f526135e272fabcb38c1cc24a99a4418717f7ed). L-RED 15 found it
  (l-red fa3085e2, climbed from pf_best_3621); the Lead re-ran it (trunk aef92047).
- n 32, o = 0. One scope run with one fallback (level 31), then 33 θ-changes > n = 32.
- Re-runs:
  - successor 15: n5.py n5 38 iterations / 1 fallback; check_sol2.py "zielonka(oink zlk) OK strategies verified"; pfclimb.fit (33, 1);
  - this successor: n5.py n5 38 / 1; check_sol2.py OK; scopecnt.py (one Odd choice vertex asserted): at most 1 (h)-run and 1 scope run per phase.
- Exact obstruction: only the constant dies. All 33 changes are in ONE fallback-free run. There, by successor 15's READING, X-RUN (R32) plus
  R27 TH (≤ n θ-changes per crossing-free interval) already give poly(n).
- The poly form of PF-THETA (N5-DROP-box35.md §8) is untouched; it stays a CONJECTURE.

### 7.6 Where the open items sit in the phase count (READING)
- With KEY, WCH, SCOPE-COUNT, FB-INT and NH1-FB:
  f per phase ≤ (in-scope f) + (out-of-SN f) + poly(n)(1 + T) + #scope runs.
- In that sum, (in-scope f) is (L1), (out-of-SN f) is §7.2, T is poly(n) (P-N5-TOG), and #scope runs is ≤ poly(n)(1 + T + f + X) (§3).
- G-N5-TIME stays OPEN.

## 8. Data (DATA, not proof)
- Every script asserts exactly one Odd vertex of out-degree > 1.
- Scripts, in experiments/new/box35 (sha1):
  - scopecnt.py (8ddf96b1…): checks SCOPE-COUNT, WCH and RESTARTS, KEY's λ_U check, the fallback classes of §7.1, and NH1-FB's count;
  - lenrun.py (c50c4ebc…): CN-LAST (i)-(iii) counters CNLAST_*, and LEN-STAY;
  - outclimb.py (1f975c7c…): OUT-POLY climbs.
- Logs (committed):
  - data/scopecnt_lib.txt (7e957149…): library + box34/box35 instances + experiments/red + experiments/si/coarse + docs/referee/R-N5-L2
    instances; 1,419 phases;
  - data/scopecnt_rand.txt (41eaa74a…): seed 3561, 39,777 phases;
  - data/lenrun_lib.txt (c94a8072…) and data/lenrun_rand.txt (7ebbd3f0…): random seed 3553.
- Results:
  - 0 failures of SCOPE-COUNT, WCH and RESTARTS.
  - Max per phase, library: 5 scope runs (so_th_n32); 4 (h)-runs (tog6a_n32); 20 WCH at n 24 with X = 2 (sc24), against the bound
    22·3 + 2 = 68.
  - Max per phase, random: 2 scope runs, 1 (h)-run, 2 WCH.
  - NH1-FB: library 11, random 338, 0 above the bound.
  - CN-LAST: level −1 Even fallbacks are 25 in the library (24 with only own-cycle-node gates) and 680 random (all 680). 0 failures of (i)
    or (ii), and the phase never continues past k + 1.
  - LEN-STAY FALSE: 4 library cases (first claimF_len_cf1) and 1 random case.
- Re-runs by this successor (pinned Oink 8fbf0a7 built by scripts/setup_oink.sh; experiments/new/check_sol2.py):

  | file | sha1 | n | n5 iterations / fallbacks | Oink zlk |
  | --- | --- | --- | --- | --- |
  | wd16_s2 | b71ddf0f… | 16 | 19 / 14 | OK, strategies verified |
  | wd12_s1 | 500a10ef… | 12 | 8 / 7 | OK, strategies verified |
  | pftheta_cex_n32 | 9f526135… | 32 | 38 / 1 | OK, strategies verified |
  | oc12_s1 | 43ec8f09… | 12 | 10 / 1 | OK, strategies verified |

  scopecnt.py on these four files reproduces max_out_of_scope_fb_phase (12, n 16, X 12, T 0, wd16_s2).
- Thin spots:
  - out-of-SN fallbacks occur only on library / climb instances, never at random;
  - CN-LAST's hypothesis has one-sided data (705 cases, all own-cycle-node but one);
  - WCH is far from tight (20 vs 68).

## 9. Labels (D18/L40)
- PROVED (L-NEW succ. 15, unrefereed; checked and partly filled in by succ. 16):
  - Remark KEY and CN-LAST, on every game;
  - WCH, SCOPE-COUNT, FB-INT and NH1-FB, on 𝒞^1O inside a phase.
- Premises in review / landing: P-N5-TOG ((F), TOGGLE-COUNT, RESTARTS; signed by both referees, not landed); P-N5-L2 (R-CONST; R33 draft).
- OPEN: out-of-SN fallbacks (§7.2), the level −1 residue (§7.3), (L1), G-N5-TIME.
- CONJECTURE: OUT-POLY; PF-THETA (poly form).
- FALSE: PF-THETA linear form (pftheta_cex_n32); LEN-STAY.
- TARGET.md diff: none of these statements is a TARGET.md section 1-2 claim. The packet uses TARGET.md's objects (parity game, max-parity,
  N5 as an algorithm on them) and changes none of them.
