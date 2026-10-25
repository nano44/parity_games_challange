# R-N5-RL: REFEREE report on packet P-N5-RL (box 10: BL-FORM, BL, CONF-MONO, FREE-FREEZE, EQ-END, MERGE, EV, EV+, TEV-RED)
Referee: REFEREE (successor 8, session_01YRPeH49wEXXq7vW5qK35Gz), Opus 5.5 (owner ruling D15, Lead reading L37). Packet P-N5-RL: the
Lead's GO of 2026-10-25 11:46Z (Lead's stamp; it reached this session at 11:42Z by this session's clock). Object
docs/si/P-N5-RL-box10.md at pinned trunk 2fb698d, sha1 0a3c70cbf873b2e011a5a00be54d38926f7861f1 (checked:
`git show 2fb698d:docs/si/P-N5-RL-box10.md | sha1sum`; the same at trunk 06f57bca and on origin/claude/l-si). Author L-SI successor 5.
Written 2026-10-25 12:00Z onward by date -u. Every verdict is labelled (Opus 5.5, D15). Independent of REFEREE-2:
docs/referee-2/R2-N5-RL.md not read. D1: every statement treated as wrong until its proof checked.

## Verdicts
| § | statement | packet label | verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| §1 | Lemma R-SAME, Lemma BL-FORM (a)-(c) | PROVED | SIGNED |
| §2 | Lemma BL (a), (d) | PROVED (no (P)) | SIGNED; "no (P)" exact |
| §2 | Lemma BL (b), (c), (e) | PROVED CONDITIONAL on (P) | SIGNED CONDITIONAL ON (P); label exact |
| §3 | Lemma CONF-MONO | PROVED | SIGNED (used nowhere in the packet) |
| §3 | Lemma FREE-FREEZE | PROVED CONDITIONAL on (P), via BL (c) | SIGNED CONDITIONAL ON (P); label exact |
| §4 | Corollary EQ-END | PROVED, CONDITIONAL on CN-LAST | SIGNED CONDITIONAL ON CN-LAST; label exact (no (P)) |
| §5 | Lemma MERGE | PROVED | SIGNED WITH GAP RL-2: for −1 ≤ ℓ < ∞ only. As stated ("ℓ ≥ −1", and ∞ is a level value) (c) fails at ℓ = ∞ (DATA: 202 window gates, inr2_n32) |
| §6 | Proposition EV | PROVED CONDITIONAL on (P), via FREE-FREEZE | SIGNED CONDITIONAL ON (P), WITH RL-4 (citation) |
| §6 | Proposition EV+ | PROVED CONDITIONAL on (P), via EV | SIGNED CONDITIONAL ON (P) |
| §6 | Proposition TEV-RED (1)-(5) | PROVED CONDITIONAL on (P), via FREE-FREEZE | NOT SIGNED as stated (RL-1). TEV-RED′ (the added hypothesis below) SIGNED CONDITIONAL ON (P), WITH RL-3 (wording of (3)) |
| §6 | Consequence (the reduction) | follows from EV+, TEV-RED (5) | NOT SIGNED as stated; it holds when TEV-RED′'s hypothesis holds at t = k (RL-1, RL-3) |
| §7 | TEV, RISE-LAST, NJB / ENT, BL-X | not to sign | not signed. BL-X FALSE confirmed (DATA below) |

Conditions, checked for exactness (task (1)):
- (P), §0: "In a one-player game (Odd has out-degree 1 at every vertex), an Even strategy with no improving edge is optimal: its
  valuation dominates that of every Even strategy, pointwise." This is R18's premise (RESULTS R18 "Honest limits (ii)": "CONDITIONAL
  on (P) for one-player games (G-1OA-4, open by design): VJ00 Lemma 5.8 '1 ⇒ 2'"). R18 used it on G[X], where Odd has no choice:
  the same Even-chooses form. The packet uses it on G_τ (BL (b), Step 2b) and on G_τ[F_k] (BL (c)). Both are one-player games of that
  form: every Odd vertex of G_τ keeps only its τ-edge, and F_k is closed, so every Odd vertex of F_k keeps its unique successor in F_k.
  "Improving" in (P) is with respect to the strategy's own valuation in that game. In G_τ this is the play valuation W, so "no
  W_{σ′}-improving edge" is (P)'s hypothesis. Exact.
- Every use of (P) is labelled. I traced each item:
  - BL (a): Step 0, Step 1 and (C7) only.
  - BL (d): Step 0, Step 1, F1 and (C7).
  - BL-FORM: Lemma G, XW and (C7).
  - MERGE: Lemma G and the definition of the gate level.
  - CONF-MONO: F1 (R17 (a), whose derivation (R17 (g)) does not use VJ00 Lemma 5.8).
  - EQ-END: R15 (a), XW, FBW-S, FBW (b) and CN-LAST.
  - Lemma S (a) and Lemma R (R18 (d)) do not need (P). R18 says so: "the theorem uses (a)-(b) only", and (P) is used "only in
    Lemma 1".
  - None of these items uses (P). Each (P) item reaches (P) only through BL (b) or BL (c).
- CN-LAST (P-N5-SCOPE §6) is used only in EQ-END (iii). Its hypotheses (an Even S4c fallback; every gate has λ(y) = y and level −1) are
  exactly what FBW-S and FBW (b) give at an in-scope EQ fallback:
  - r = ⊥ gives δ = ⊥;
  - ℓ ≤ max(⊥, −1) = −1, and gates are strict, so ℓ = −1 > δ.
  My lane signed CN-LAST in R-N5-SCOPE (fb6089b; §C pending).
- Declared, not a condition: EV, EV+ and TEV-RED use the "Facts used throughout" of §6:
  - OFFGATE, NL (i)-(iii), FLAT-ALL (iii) and FBW-S: landed, R29 / R31;
  - from P-N5-NJB: ENT-SHAPE (4) and the NO-RF-OLD Corollary. Both referees signed these, and they are landing as R35. They are not
    yet in docs/RESULTS.md at trunk 06f57bca.
  - §0 declares them with their status. The labels are exact provided R35 lands with ENT-SHAPE (1)-(4) and NO-RF-OLD + Corollary as
    signed.
  - ENT-SHAPE (5), which my lane did not sign as stated (NJB-2), is not used.
- No condition is used without being declared, beyond RL-1. The missing hypothesis in TEV-RED is not a condition that could be
  declared: the proof does not handle that case.

## 1. §1 R-SAME and BL-FORM: checked
- R-SAME: both values have cycle node c (H3).
  - P(π ⊕ a) = (π ∩ V_{>c}) ⊔ P(a), with P(a) ⊆ {o} ∪ F. For θ: o, then σ̄(o) ∈ F (H1). For w: o, then e* ∈ F (H2).
  - The symmetric difference (π Δ π′) ∩ V_{>c} and the length difference |π| − |π′| do not depend on a. Correct.
- BL-FORM: four cases on (s, u) ∈ {F, R̄}².
  - (F, F): Ξ = W at both. Correct.
  - (R̄, F): W(s) = π_s ⊕ w ⊵ π_s ⊕ θ by (C7) on θ ⊴ w. s = o is included (π_o = ∅). Correct.
  - (R̄, R̄): R-SAME. Correct.
  - (F, R̄): this is (b).
  - (a): v ∈ R would put s on a play to o. Correct.
  - (c): sandwich between two values with cycle node c, and rew decides first. Correct.

## 2. §2 BL: checked, labels exact
- Step 0.
  - Ξτ_k = U_{τ_k} (Lemma S (a) on G^d, Lemma R). U_{τ_k} = max_{σ′} V_{σ′,τ_k} = W* (F1 in G_τ).
  - S2 on G^d: (o, x) ∈ Iτ_k iff W*(x) ◁ W*(e*). Correct, no (P).
- Step 1.
  - τ_new = Odd's optimum in H′. With Lemma S (a) on H′: V(o) ⊴ o ⊕ Ξ_k(x) ◁ w_k = V_{σ_k,τ_k}(o).
  - So τ_new(o) ≠ e*, and S4c does not fire. Correct.
- (a).
  - Under W_k = W*: θ_k = o ⊕ W*(x0) ◁ o ⊕ W*(e*) = w_k.
  - (C7) gives W*(x0) ◁ W*(e*), so (o, x0) ∈ Iτ_k, against Step 1.
  - It uses H1 (λ(o) ≠ o) for (P2) at o, and H2 for w = o ⊕ W(e*). Correct.
- (b), Step 2a.
  - FBW Step 2 (R31) uses only V(z) ▷ V(σ_k y) and σ_k[y ↦ z] ∈ A(σ_k), and the latter needs (y, z) to be a gate.
  - With V := W_k, a W-improving gate is strict except in FBW's case (b2) with y = c and P(V z) = ∅.
  - P-OPT then forces that case. Correct.
- (b), Step 2b.
  - z_i's play reaches c_i through ranks < c_i (P = ∅).
  - It meets no other c_j: c_j's play is its own cycle, so c_j would become z_i's cycle node.
  - Plays first meeting c_i keep (c_i, P, length) read on the common prefix, so W_{σ′} = W_k.
  - At c_i, an improving edge would be a better W_k-improving target than z_i.
  - (P) in G_τ then gives W_k = W*, against (a). Correct.
  - p = 0 is included: σ_k itself has no improving edge.
- (c).
  - G_τ[F_k] is well defined (closure).
  - Its improving edges are W_k-improving edges inside F_k. These are gates (BL-FORM's (F, F) case), hence exceptional.
  - The Step 2b switch, inside F_k, changes no value and leaves none. Then (P) applies in G_τ[F_k]. Correct.
- (d): W*(x) ⊵ W*(e*) ⊵ W_k(e*) ▷ W_k(x) (Step 1 with Step 0, F1, (C7)). Correct, no (P).
- (e).
  - A G_τ-strategy whose x0-play stays in F_k agrees on that play with a strategy of G_τ[F_k]. Extend it by σ_k: it still maps F_k
    into F_k, because the play is closed under its successors.
  - So its value is ⊴ Opt(G_τ[F_k])(x0) = W_k(x0) ◁ W*(x0) ((c), (d)).
  - Odd vertices of F_k cannot leave F_k. Correct.
- "In-phase" is used only to make the fallback Even's (Iσ_k ≠ ∅, τ_{k+1} = τ_k). THR is used in (a) and, through (a), in (b). (c)
  does not use THR, but it is stated in BL's setting and FREE-FREEZE cites it there. Harmless.

## 3. §3 CONF-MONO, FREE-FREEZE: checked
- CONF-MONO: F1 in G_τ[F] applied to an extension of a G_τ[F′]-strategy, which exists because F is closed. Correct. Not used in §4-§6.
- FREE-FREEZE.
  - Ξ_{k0}(z) ⊴ Ξ_t(z) = W_t(z) (R15 (a); Lemma G off R̄_t).
  - σ′ (σ_t on z's play, σ_{k0} elsewhere on F_{k0}) maps F_{k0} into F_{k0}. τ_t = τ_{k0} (one phase).
  - So W_t(z) is σ′'s value in G_τ[F_{k0}], and W_t(z) ⊴ Opt(G_τ[F_{k0}])(z) = W_{k0}(z) = Ξ_{k0}(z) (F1, BL (c) at k0, Lemma G at
    k0, z ∈ F_{k0}). Correct.

## 4. §4 EQ-END: checked
- θ_t ⊴ θ_s ⊴ w_s = w along S.
- At each later fallback of S, the fallback is EQ: (h) at k (k ∈ S) and θ_k = w.
- FBW-S and FBW (b) give CN-LAST's hypotheses (above). CN-LAST (iii) makes k + 1 the last state of the phase. A scope run lies inside
  one phase (it is a run of in-phase transitions), so S ends at k + 1. Correct.
- "Every later state of S is EQ" also holds at S's end state, where only H2 is guaranteed. θ = w gives H3 (the same triple).
  - If o were on its honest cycle, c's σ-path to o (no vertex o before it, and all other vertices agree between the honest and the
    (σ, τ) graphs) would put o on the W-cycle of c = c_w, against H2. So H1 holds too.
  - The packet does not say this. The statement is true; I record it as a remark, not a gap. DATA: 0 scope runs with θ = w whose end
    state fails (h) (EQ_END_NOTH).

## 5. §5 MERGE: RL-2
- Checked for −1 ≤ ℓ < ∞:
  - (a): lev ≤ ℓ gives equal COARSE_ℓ. π ⊆ R_k is disjoint from P(Ξ_k z) ⊆ F_k, and P(θ) ⊆ V_{>c}, so π ∩ H = ∅.
  - (b): o ∈ H would put o in P(θ_k) ∩ H ⊆ P(Ξ_k z).
  - (c): both plays contain c. The H-parts are equal, the prefixes before m are disjoint, and H-vertices are never on the cycle (rank >
    c). Correct.
- RL-2: the statement says "a window gate (y, z) of level ℓ ≥ −1".
  - The level values are ⊥ < −1 < 0 < … < n − 1 < ∞ (P-N5-FBW §0, imported by §0). Gates of level ∞ (z's cycle node ≠ c) are window
    gates of level ≥ −1.
  - For them H = ∅, so (a) and (b) are empty. (c) "let m be the first common vertex" has no referent, and the proof's "both plays end in
    c's cycle" is false.
  - DATA: at (h) states, 50 (NAMED) + 152 (LIB) + 229 (random) window gates have level ∞. In every one of them the plays of z and
    σ̄_k(o) are disjoint.
  - Hand-checked: experiments/si/orlens/instances/inr2_n32.pg, state 0, (h), gate (6, 29).
    - 6 ∈ R and 29 ∈ F.
    - b(6) = (18, ∅, 4), Ξ(29) = (16, {rank 12}, 1), level ∞.
    - The play of 29 is 29 → 16 ↺. The play of x0 = 27 is the cycle 27 → 31 → 18 → 2 → 27. They are disjoint.
- Every use of MERGE (EV, EV+) is at the finite level L ≥ 0, so §6 is unaffected.
- Fix: "level −1 ≤ ℓ < ∞" (equivalently ℓ ≤ n − 1).

## 6. §6 EV, EV+, TEV-RED: RL-1, RL-3, RL-4
- Facts.
  - S lies in one phase. (h) holds at k0, k0 + 1, …, k, because the transitions of these states are in S.
  - THR at k0 and k comes from FBW-S. COARSE_L(θ) strictly increases from k0 to k, by monotonicity and the rise.
  - c is constant on S: w is constant and c = c_w (H3). Correct.
- EV.
  - FREE-FREEZE at (k0, k, z) applies: k0 is an in-phase THR fallback with (h), and k is in the same phase with (h). It contradicts
    ENT-SHAPE (4).
  - The play lies in F_k ⊆ F_{k0+1}.
  - Bookkeeping: ρ ⊆ F_{k0} (it is before the first Ev vertex), π_q ⊆ R_{k0}, and A is on q's play at k. So the three parts are
    disjoint.
  - P(Ξ_k q) ∩ V_{>L} = (π_q ∩ H) ⊔ A follows from NL (i) after k0, FLAT-ALL (iii) across k0, and Lemma G at k0 (q ∈ Ev ⊆ R_{k0},
    q ≠ o).
  - MERGE (a) at L. Correct.
  - Remark (no gap): "Ξ_k(z) = ρ ⊕ Ξ_k(q)" is an identity of triples only if q comes before c on the play. If q lies on the cycle after
    c, only the H-parts agree. Then P(Ξ_k q) = ∅, so A = π_q ∩ H = ∅, and B = ρ ∩ H. The proof uses H-parts only, so EV holds in both
    cases.
- RL-4 (citation): "By ENT-SHAPE (signed), there is a level-L window gate (y, z) at k".
  - ENT-SHAPE assumes such a gate ("Let (y, z) be a level-L gate at k with y ∈ R_k and z ∈ F_k").
  - Its existence is P-N5-NJB §3's Corollary to NO-RF-OLD: the level-L tail of FB step (2), whose best switch has level L ≥ 0, is
    R → F by FBL.
  - Signed (R-N5-NJB 524d93f5). Fix the citation.
- EV+.
  - Case h ∈ ρ: MERGE (c) puts every H-vertex of z's play on the suffix shared with x_k's play, and q follows h.
  - Case h ∈ π_q: h ∈ B ⊆ P(θ_k), h ≠ o, so h is on x_k's play, and h ∈ F_k ∩ R_{k0} ⊆ Ev. Correct.
- TEV-RED (2), (4), (5): correct, given (1).
  - (2): b-form across k0 by FLAT-ALL (iii), in both the tail and the non-tail case. After k0, NL (i) applies through
    Ξ(e) = e ⊕ b(e): e is not a cycle node, since λ(e) = c is constant in the phase and e ∈ R_{k0}.
  - (2): MERGE-type argument for π_{u_e} ∩ H = ∅. o ∉ H.
  - (4): COARSE_L(Ξ_t u_e) = (c, (π′ ∩ H) ∪ B_t) ≠ (c, A) and ⊵ (c, A), so it is ▷ (c, A) = COARSE_L(b_t e).
  - (5): M_k = L. Correct.
- RL-1 (TEV-RED (1); proof gap; NOT SIGNED as stated).
  - The proof says: "Every vertex after e on the play lies in F_t ⊆ F_{k0+1} = F_{k0} ⊔ Ev and is not in Ev, so it lies in F_{k0}."
    From this it concludes that f's play lies in F_{k0} and applies FREE-FREEZE to f.
  - This is valid only if e lies on the prefix of x_t's lasso and no Ev vertex lies on its cycle.
  - If an Ev vertex lies on the cycle (c's cycle C_t at t), then f's play runs around C_t through an Ev vertex. "The last Ev vertex"
    in lasso order is then on C_t, and (1) "f's play lies in F_{k0}" is false. FREE-FREEZE does not apply, and (2)-(5) and the
    Consequence lose their basis.
  - Nothing in the packet, or in the results it cites, excludes Ev ∩ C_t ≠ ∅ for t ∈ (k0, k]:
    - C_{k0+1} ⊆ F_{k0}: FLAT-ALL (i), and FBL forbids F → R̄ gates at k0.
    - Later S4a steps may switch vertices of C_t, including c by length-only cycle-node switches (CN), towards vertices of Ev ⊆ F.
    - NL (i) and FLAT-ALL (iii) force only that such an Ev vertex v has COARSE_L(Ξ_{k0} v) = (c, ∅), i.e. A = ∅ and π_v ∩ H = ∅.
  - That precondition is common. DATA: A = ∅ at 37 of 376 (NAMED) and 95 of 526 (LIB) in-scope fallbacks of level ≥ 0, each with an
    Ev vertex of class (c, ∅).
  - The case itself was not observed. DATA: 0 states with Ev ∩ C_t ≠ ∅ over 732 + 1,353 TEV states, and 0 after 3 × 1,500 s climbs
    aimed at it (§8). Absence in data does not close a proof gap (D1).
  - TEV-RED′ (signed, CONDITIONAL on (P)): TEV-RED with the added hypothesis "no Ev vertex lies on the cycle of x_t's σ_t-play".
    Then e lies on the prefix, the quoted step is valid, and (1)-(5) follow as written (with RL-3).
  - Fix options for L-SI:
    - prove Ev ∩ C_t = ∅ for t ∈ (k0, k] (a new lemma);
    - or carry the hypothesis into TEV-RED (5) and the Consequence;
    - or treat the cycle case separately (there A = ∅, which may help).
- RL-3 (TEV-RED (3); wording).
  - The proof writes Ξ_t(x_t) = (x_t's play up to e) ⊕ Ξ_t(f), with e included. The statement says "B_t = A ⊔ (the H-vertices of x_t's
    play before e)".
  - e ∈ H is not excluded: e ∈ R_{k0}, and COARSE_L(Ξ e) = (c, A ∪ ({e} ∩ H)) at k0 and at t alike.
  - If e ∈ H, (3) as worded is false. The correct form is "up to and including e". The same applies to the Consequence's third
    bullet ("before e").
  - (4) is unaffected: it needs only B_t ⊋ A. DATA: e ∈ H at 0 of 607 meeting states.

## 7. §7 not signed. BL-X FALSE: confirmed
- BL-X fails at 376 − 335 = 41 NAMED fallbacks (packet's 373 + rl_a/b/c, which all satisfy BL-X) and at 4 of 526 LIB fallbacks:
  BL_blocked_on_x0play 335 / 522. These are the packet's counts.

## 8. DATA (DATA, not proof; own code docs/referee/scratch/rl_engine.py + rl_probe.py + rl_oink.py + rl_climb.py; logs scratch/rl_logs/)
- Engine. Own N5 written from SPEC S1-S5 (FIX 1-4, Q1-Q4) only. No lane code is imported (no si.py, n5.py or pg.py). Lane instances
  are read as inputs.
  - Iterations / fallbacks reproduce the packet's on rl_a/b/c: 35/2, 33/2, 30/3.
  - Final regions agree with Oink --zlk (pinned 8fbf0a7) on all 234 LIB and 75 NAMED games (rl_oink.py, logs oink_lib.txt,
    oink_named.txt).
  - Every game is asserted to have exactly one Odd vertex of out-degree > 1.
- Sets: NAMED = experiments/si/coarse/named.txt + coarse/instances/*.pg + instances/box9/*.pg + experiments/si/riselast/instances/*.pg
  (75 games); LIB = experiments/new/box33/lib.txt (234); random 𝒞^1O games (3,000, n 6-24, seed 801).

| check | NAMED | LIB | random | failures |
| --- | --- | --- | --- | --- |
| BL-FORM (a)-(c) + Lemma G form, blocked edges at (h) states | 23,968 edges / 2,345 states | 50,742 / 5,002 | 98 / 3,932 | 0 |
| R-SAME, ordered pairs in R̄ at (h) states | 289,528 | 654,450 | 16,812 | 0 |
| BL (a)-(e) at in-phase THR fallbacks with (h) (W*, Opt(G_τ[F]) by own VJ on the dual) | 376 | 526 | 0 | 0 |
| BL Step 0 (U_τ = W*; (o, x) ∈ Iτ iff W*(x) ◁ W*(e*)) | 1,871 exits | 2,606 | — | 0 |
| BL (d), all deficient free exits | 983 | 1,530 | — | 0 |
| F1 sampled (10 random σ′ per fallback) | 3,760 | 5,260 | — | 0 |
| FREE-FREEZE (k0, t, z) | 93,125 | 177,919 | 0 | 0 |
| EQ-END: scope runs reaching θ = w; fallbacks after | 61; 5 | 156; 8 | 420; 52 | 0 |
| MERGE (a)-(c), window gates of finite level | 4,626 | 11,411 | 362 | 0 |
| MERGE at level ∞ (RL-2): window gates; with disjoint plays | 50; 50 | 152; 152 | 229; 229 | — |
| TEV states (t ∈ (k0, next fb], r > L, (h)); post-rise | 732; 111 | 1,353; 6 | 0 | — |
| x_t's play meets Ev; post-rise | 182; 0 | 425; 0 | — | — |
| TEV-RED (1)-(3) at meeting states (e = last Ev vertex) | 182 | 425 | — | 0 |
| Ev on C_t / on x_t's cycle (RL-1 case) | 0 / 0 | 0 / 0 | — | — |
| A = ∅ at k0 (RL-1 precondition), with an Ev vertex of class (c, ∅) | 37 of 376 | 95 of 526 | — | — |
| e ∈ H (RL-3) | 0 | 0 | — | — |
| ENT setting | 0 | 0 | 0 | — |

- The packet's counts reproduced where they are comparable:
  - FREE-FREEZE: LIB 177,919, the packet's figure exactly; NAMED 91,913 + 1,212 (rl_a/b/c).
  - threv: LIB 425 / 1,353 and 0 / 6, the packet's; NAMED 179 + 3 / 662 + 70.
  - BL fallbacks: 373 + 3 / 526.
- Thin spots, stated plainly:
  - The ENT setting never occurs, and no post-rise state has the threat through Ev. So EV, EV+, TEV-RED (4)-(5) and the
    Consequence have vacuous hypotheses in all data, mine included; they rest on the proofs.
  - TEV-RED (1)-(3) are exercised at 607 states without the rise.
  - Random 𝒞^1O games are vacuous for BL, FREE-FREEZE and TEV.
- Climbs (rl_climb.py; fitness = 1000·[Ev on x_t's cycle] + 100·[Ev on C_t] + 10·[A = ∅] + Σ 1/(1 + dist(Ev → C_t)); 1,500 s each):
  results in §8.1.

### 8.1 Climb results
(added 2026-10-25 12:24Z by date -u)
- Three climbs of 1,500 s, seeds 88001-88003. Starts: zcl_fb1_n32, b6_xl_n32 (A = ∅ at both of its fallbacks) and x32_waves32 (all
  inputs only). 57,605 + 116,920 + 55,167 candidates; every candidate was asserted to be in 𝒞^1O.
- Best fitness 139.5, 142.1 and 120.2. These come from the gradient terms only (Ev vertices draining into C_t, A = ∅). There was 0
  hit with Ev on C_t, and 0 with Ev on x_t's cycle.
- Bests: scratch/rl_climb_out/rlc_best_88001.pg (n 32, sha1 ad0086a7, 41 iterations / 4 fallbacks), rlc_best_88002.pg (cd40c400,
  20 / 2), rlc_best_88003.pg (32002c12, 25 / 1).
  - Own probe: all checks, 0 failures; 24 and 13 TEV states with the threat through Ev, none post-rise.
  - Final regions agree with Oink --zlk on all three.
- Reading: the RL-1 case is not reached by local search from these starts. This is DATA and does not close RL-1; the proof must.

## Fixes-file lines (one per gap; L-SI)
- RL-1 (§6 TEV-RED (1), proof gap): "the last Ev vertex e" and "f's play lies in F_{k0}" need that no Ev vertex lies on the cycle of
  x_t's σ_t-play. Either prove Ev ∩ C_t = ∅ for t ∈ (k0, k], or add that hypothesis to TEV-RED and the Consequence (TEV-RED′), or
  treat the cycle case (where A = ∅) separately.
- RL-2 (§5 MERGE, scope): replace "level ℓ ≥ −1" by "level −1 ≤ ℓ < ∞". At ℓ = ∞, (c) has no common vertex
  (inr2_n32.pg state 0, gate (6, 29)).
- RL-3 (§6 TEV-RED (3) and Consequence bullet 3, wording): "before e" → "up to and including e". e ∈ H is not excluded.
- RL-4 (§6 EV, citation): the existence of the level-L window gate (y, z) at k is P-N5-NJB §3's Corollary to NO-RF-OLD (FB step (2) +
  FBL), not ENT-SHAPE. ENT-SHAPE assumes the gate.

## TARGET.md diff
Not a claim of TARGET.md §2 (M4). These are lemmas about the candidate N5 on 𝒞^1O, a subclass, and the packet says so (header: "not a
running-time bound, not a TARGET.md claim, and not a step-4 pass. G-N5-TIME stays OPEN"). No statement here concerns general parity
games or the running time. G-N5-TIME stays open.

Signed: REFEREE (successor 8) (Opus 5.5, D15).

## Addendum A1 (written 2026-10-25 12:36Z by date -u): L-RED 16's instances (relayed by the Lead 12:27Z, Lead's stamp), and R35
- Inputs only, run through my own probe (rl_probe.py; 𝒞^1O asserted; own engine). These are not L-RED's scripts.
- experiments/red/so/instances/tevlast_cex_n40.pg (sha1 ff1e9cb4):
  - one in-scope THR fallback k0 = 3; 5 TEV states, 2 post-rise.
  - At t = 7 (post-rise) x_t's play meets Ev. The last Ev vertex is e = 15, and e ∈ H.
  - B_t = A ⊔ (the H-vertices before e) ⊔ {e}.
  - So RL-3 OCCURS: TEV-RED (3) as worded ("before e") is false at this state, and "up to and including e" holds. My §6 entry "e ∈ H at
    0 of 607" is superseded by this instance.
  - TEV-RED (1), (2) and (4) hold here (TEVRED4_chk 1, 0 failures). There is no second fallback, so this is not the ENT setting:
    TEV-RED's own hypothesis (a next fallback k with M_k = L) fails. The instance tests the clauses statewise.
  - All other checks: 0 failures.
- experiments/red/so/instances/tev_cex_n40.pg (sha1 17078f78): 16 THR fallbacks, 20 TEV states; all checks 0 failures, e ∈ H 0.
- L-RED's point that "no vertex leaves R in (k0, t]" needs k0 to be the LAST fallback before t:
  - In P-N5-RL §6, k0 < k are consecutive fallbacks of S, and t ∈ (k0, k]. So every t has k0 as its last fallback, and NL (ii) is
    applied only at S4a steps of (k0, k).
  - EV, EV+ and TEV-RED quantify k0 correctly. The point bears on readings of CONJECTURE TEV ("any earlier k0"; L-RED's tev_cex_n40),
    which is §7, not to sign.
- CONJECTURE TEV (§7) FALSE: noted, not my verdict to give (not to sign). It does not change any verdict above.
- R35 (P-N5-NJB) is now landed (trunk 4151e41, per the Lead). So ENT-SHAPE (4) and the NO-RF-OLD Corollary, used in §6, are landed
  premises. The "declared, not landed" remark in the Verdicts section is closed.
- Verdicts unchanged:
  - RL-3 is now realised, not only possible. It remains a wording gap, and its fix is unchanged.
  - RL-1 is unchanged. The Lead reports an unrefereed lane Lemma CYC-EV ("c's cycle at k has no Ev vertex", ENT setting). I will judge
    it when it arrives. As described, it would need to cover every t ∈ (k0, k], not only t = k, to close RL-1 for TEV-RED (1)-(4).

## §C. Comparison with REFEREE-2 (written 2026-10-25 12:46Z by date -u; REFEREE successor 8 (Opus 5.5, D15))
- Compared against: the FINAL docs/referee-2/R2-N5-RL.md at referee-2 30dc5f54, named by the Lead at 12:43Z (Lead's stamp). I read it
  after this report (b7419da0, 257c3d81) and Addendum A1 (38863849) were pushed.
- Same verdict, same labels: BL-FORM, R-SAME, BL (a)-(e), CONF-MONO, FREE-FREEZE, EQ-END, EV, EV+. Both referees find every
  "conditional" label exact. Both agree that EV, EV+ and TEV-RED quantify k0 < k as consecutive fallbacks, so "no leave" holds as
  written.
- Two verdicts differ in label. Reconciled here:

| item | REFEREE (this report) | REFEREE-2 | substance | reconciliation |
| --- | --- | --- | --- | --- |
| §5 MERGE | SIGNED WITH GAP RL-2 (statement scope: "ℓ ≥ −1" includes ℓ = ∞) | SIGN, N-RL-1 (wording: read "plays" in (c) as paths up to the first visit of c) | DIFFERENT points. N-RL-1 is about finite ℓ; I agree with it, and my proof check used H-vertices, which lie before c, so it is equivalent. RL-2 is about ℓ = ∞: R2's own proof line "Both values have the cycle node c" fails there (Ξ(z) has another cycle node, and z's and x0's plays are disjoint: inr2_n32 state 0, gate (6, 29); 50 / 152 / 229 such window gates in my data). R2's 40,974 checked window gates and its (c) argument do not mention ∞ | I keep SIGNED WITH GAP RL-2. Both referees sign MERGE for −1 ≤ ℓ < ∞ (MERGE′), and every use is at finite L. Joint: MERGE′ signed by both; RL-2 (scope) and N-RL-1 (wording) both go to the fixes file. Requested: REFEREE-2's ruling on whether its SIGN covers ℓ = ∞ |
| §6 TEV-RED | NOT SIGNED as stated (RL-1); TEV-RED′ SIGNED CONDITIONAL ON (P), with RL-3 | SIGN CONDITIONAL ON (P) WITH GAPS G-RL-1, G-RL-2 | SAME. G-RL-1 = RL-1: the "last Ev vertex", (1) and (3) are unproved when c's cycle at t meets Ev. R2: "TEV-RED is silent in that case rather than false"; "the Consequence … uses TEV-RED at t = k with no such hypothesis". G-RL-2 = RL-3, with the same instance (tevlast_cex_n40, t = 7, e = 15 ∈ H). R2's fix ("c's honest cycle at t lies in F_{k0}") is equivalent to mine ("no Ev vertex on the cycle of x_t's play"): that cycle is c's cycle, which lies in F_t ⊆ F_{k0} ⊔ Ev | The difference is labelling convention. Under D1 I do not sign a statement whose proof does not cover all of its cases, so I keep NOT SIGNED as stated. Joint state: the literal TEV-RED is unproved in the cycle case (both); TEV-RED′ (with the hypothesis) is signed CONDITIONAL ON (P) by both, with RL-3 = G-RL-2 fixed. The Consequence holds only with the hypothesis at t = k (both). For landing: TEV-RED′, not TEV-RED |

- R2 items I had not raised:
  - N-RL-3: in the EV setting facts, "the top of A Δ B is even and in B" needs A ⊆ B, which only EV gives. From θ_{k0} ◁ θ_k alone
    the top is "even in B or odd in A". Correct, and MISSED by me (my §6 "Facts" said "Correct"). Wording: it is used only after EV.
  - FREE-FREEZE: "(h) at t" is not used. Correct: Lemma G off R̄ needs no (h) (R19 (a)). A note.
  - N-RL-2 = my EV remark (q on the cycle after c; the conclusion holds). Agreed.
- One analytic difference, not a verdict:
  - R2 says the RL-1 case is "reachable in principle: a flat switch of c at k0 into R̄_{k0} whose route is cut by a level −1 R → F
    switch". I read that route as excluded: k0 is THR with u* ≠ none (FBW-S, M ≥ 0), and FBL (R20 (b)) forbids F → R̄ gate edges there.
    So C_{k0+1} ⊆ F_{k0} (my §6). R2's own counter ("c switched into R̄_{k0} at k0": 0 batch, 0 climbs) agrees.
  - On my reading the case needs a later S4a change of c's cycle into Ev. Either way the case is open and unrefuted.
- DATA comparability: R2's counts are on its own N5 (any arena optimum), mine on SPEC traces. Both sets show 0 occurrences of the RL-1
  case (R2: 8,771 batch + 851,022 climb states; mine: 2,085 TEV states + 3 climbs).
- Joint gap map, one fixes-file line each (L-SI, docs/si/P-N5-RL-fixes-box10.md):
  - RL-1 = G-RL-1: TEV-RED and the Consequence need "no Ev vertex on c's cycle at t" (equivalently "c's honest cycle at t lies in
    F_{k0}"), for every t ∈ (k0, k], or a proof of it. The lane's CYC-EV, if it covers every such t, would close it.
  - RL-3 = G-RL-2: TEV-RED (3) and the Consequence: "before e" → "up to and including e" (realised at tevlast_cex_n40).
  - RL-2 (REFEREE only): MERGE scope "−1 ≤ ℓ < ∞".
  - RL-4 (REFEREE only): EV citation, gate existence = the NO-RF-OLD Corollary.
  - N-RL-1, N-RL-2, N-RL-3 (REFEREE-2; I accept all three) and the FREE-FREEZE "(h) at t" note: wording.

## Addendum A2 (written 2026-10-25 12:52Z by date -u; REFEREE successor 8 (Opus 5.5, D15)): the fixes file, Lemma CYC-EV, restricted TEV-RED
- Object: docs/si/P-N5-RL-fixes-box10.md (sha1 ac0274586a3b715d8725bc5226e3b32572edf017, l-si 1f107bfb, on trunk). It cites its proof
  source docs/si/N5-TEV-box11.md (sha1 58a0b3cf…; §0 setting (Σ), §1 FZ, BF, §2 RB, WALK, §3 Step 1′). Both checked by sha1sum. Routed
  by the Lead at 12:49Z (Lead's stamp).
- Read before this addendum: R2-N5-RL (my §C). REFEREE-2's G-RL-1 is the same gap, so this is not an independent first read of the gap.
  The proof check below is my own.

| item | verdict (Opus 5.5, D15) |
| --- | --- |
| Lemma FZ, Lemma BF, Lemma RB, Corollary WALK (a)-(c) (N5-TEV-box11 §1-§2; setting (Σ)) | SIGNED (no (P)) |
| Lemma CYC-EV (ENT setting; no Ev vertex of F_k on C_k) | SIGNED (no (P)) |
| restricted TEV-RED (fixes RL-1 "Replacement statement") | SIGNED CONDITIONAL ON (P), with RL-3's wording; at t = k without extra hypothesis (by CYC-EV), at t < k as TEV-RED′ |
| Consequence (the reduction) | now SIGNED CONDITIONAL ON (P): it uses TEV-RED only at t = k |
| RL-2, RL-3, RL-4 replacement texts | correct; each closes its row |

- FZ:
  - no leave (NL (ii)) at the S4a steps of (k0, k) gives F_k ⊆ F_s;
  - FLAT-ALL (iii) across k0 ((h) at k0 and k0 + 1);
  - NL (i) at each S4a step. Correct.
- BF:
  - Ξ_{k0}(v) = v ⊕ Ξ_{k0}(a) (Lemma G). Ξ_k(v) = v ⊕ b_k(v) by (P2): v ≠ c = λ_k(v), and c ∈ F_{k0}.
  - v is not on the pre-c path of its successor's play (a functional-graph argument, correct).
  - Removing v from both path sets and applying FZ: correct.
- RB.
  - a ≠ σ_k(v): σ_k(v) ∈ F_k and a ∈ R̄_k.
  - Ξ_k(a) ⊵ Ξ_{k0}(a) (R15 (a)), and COARSE_L(Ξ_{k0} a) = COARSE_L(b_k v) (BF).
  - A strict COARSE_L increase would make (v, a) a gate at k of level > L, against M_k ≤ M_{k0} = L (CLS2; k and k0 are fallbacks of
    S). Correct.
  - This is where t = k (a fallback state) is used. At an S4a state t < k no such bound exists. L-SI says so in RL-1 (ii), and
    tevlast_cex_n40 shows the gate (15, 21) of level 33 > L at t = 7.
- WALK.
  - (a): j exists (o ∈ R̄_k). v ∈ F_k ∩ R_{k0}. An Odd v ≠ o with its unique successor in R̄_k would be in R̄_k.
  - (b): RB at v, then Lemma G at k0 and at k. The path part is (π ∩ H) ⊔ (P(θ) ∩ H), because P(·) ⊆ V_{>c} and c is constant on S.
  - (c): π^{k0}_{a_j} ⊆ π^{k0}_{a_1}. Correct.
- CYC-EV.
  - v ∈ Ev ∩ F_k on C_k: then v ≠ c (c ∈ F_{k0}), and Ξ_k(v) = W_k(v) = (c, ∅, ·), since C_k is topped by c.
  - FZ and Lemma G at k0: (π^{k0}_v ∩ H) ⊔ A = ∅. So A = ∅ and v's route is low.
  - WALK (c): B ⊆ A = ∅, against B ≠ A (the rise).
  - It uses (Σ), the rise and (h) at k0, k0 + 1 and k. It does not use M_k = L or (P). C_k is the cycle of x_k's play: x_k ∈ F_k and
    θ_k = o ⊕ Ξ_k(x_k) has cycle node c. Correct.
- Does CYC-EV cover what TEV-RED (1)-(4) need at t = k (my 12:40Z point)? Yes.
  - With no Ev vertex on C_k, every Ev vertex of x_k's play lies on its pre-cycle prefix, which is part of the pre-c path. So "the last
    Ev vertex on the play's prefix before its first visit to c" is the last Ev vertex of the whole play.
  - f's whole play (the rest of the prefix and C_k) avoids Ev, so it lies in F_{k0} (F_k ⊆ F_{k0} ⊔ Ev). (1) follows with FREE-FREEZE
    ((P)).
  - (2)-(5) are as I checked in §6, with (3) in RL-3's form.
  - For t ∈ (k0, k) the replacement keeps the hypothesis (TEV-RED′), which I signed in §6. RL-1 is closed.
- Remark (agreed): CYC-EV also settles EV's "q on the cycle" case at t = k (z's cycle is C_k), so my §6 EV remark and R2's N-RL-2 are
  vacuous in the ENT setting.
- Not reviewed here, and NOT signed by this addendum: N5-TEV-box11.md §3 Theorem ENT-X ("the ENT setting is empty", CONDITIONAL on (P)) and
  §4 Corollaries NJB-A, D1, PL-S″. They are new results, beyond the fixes, and need their own packet. If ENT-X holds, EV, EV+ and
  TEV-RED become vacuous: true, but about an empty setting.
- DATA (own code docs/referee/scratch/cyc_probe.py on rl_engine; logs rl_logs/cyc_named.txt, cyc_lib.txt):

| set | (Σ) pairs | FZ | BF | RB | WALK | failures (FZ, BF, RB, WALK a/b, M_k ≤ L, Ev on C_k) | pairs with a rise |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NAMED (75) | 262 | 6,177 | 515 | 344 | 529 | 0 | 0 |
| LIB (234) | 377 | 10,525 | 1,080 | 578 | 1,121 | 0 | 0 |
| L-RED tev instances + my climb bests (5) | 19 | 482 | 52 | 27 | 53 | 0 | 0 |

- The pair, RB and WALK counts equal the lane's rb.py counts exactly (262 / 344 / 529; 377 / 578 / 1,121).
- Thin spot: no (Σ) pair has a rise, so CYC-EV's hypothesis is vacuous in data. FZ, BF, RB and WALK are non-vacuous; CYC-EV rests on the
  proof.
- Joint status after A2:
  - RL-1 is closed by the fixes file (pending REFEREE-2's view of the same text).
  - RL-2, RL-3 and RL-4 are closed by their replacement texts.
  - The landing label for TEV-RED is the replacement statement, CONDITIONAL ON (P). (P) itself is now P1, signed by both referees,
    pending CHECKER.

## Note on A2 (written 2026-10-25 13:15Z by date -u)
- The Lead's ruling of 12:58Z (Lead's stamp) crossed with A2 (pushed 12:56Z by date -u): CYC-EV is judged in P-N5-ENT, not as an RL
  addendum.
- So, for RL's landing, A2's CYC-EV-based rows are superseded. RL lands with TEV-RED′ and its explicit hypothesis ("no Ev vertex on
  x_t's cycle at t").
- The CYC-EV check itself is in R-N5-ENT.md (55a3f6fb, SIGNED). A2's RL-2..4 text checks stand.
- REFEREE-2's §C (referee-2 88571b0, per the Lead) accepts RL-2 and adopts TEV-RED NOT SIGNED as stated / TEV-RED′ signed. RL and P1 are
  converged.
