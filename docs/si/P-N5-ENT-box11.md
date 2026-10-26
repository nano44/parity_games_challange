# Referee packet P-N5-ENT: the route-back freeze, TEV at fallback states, and NJB in the ENT setting (box 11)
L-SI successor 6 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~12:55Z (date -u), at the Lead's request (12:34Z). Frozen at its
commit: corrections go in a fixes file, never here.
- Self-contained: definitions, statements, full proofs, the status of every dependency, the data and the script.
- Source text: docs/si/N5-TEV-box11.md (lane write-up, l-si 3f08db7, sha1 58a0b3cf). Where they differ, this packet governs.
- Status: L-SI successor 6's proofs, unrefereed. Labels: PROVED (L-SI succ. 6) = no (P); PROVED CONDITIONAL on (P); OPEN; DATA.
  - Everything is on 𝒞^1O: exactly one Odd vertex o with out-degree > 1. The script asserts it.
- These are lemmas about the candidate N5. They are not a running-time bound, not a TARGET.md claim, and not a step-4 pass.
  G-N5-TIME stays OPEN.
- Statements to sign:

| § | statement | label | uses (P) |
| --- | --- | --- | --- |
| §1 | Lemma FZ (freeze) | PROVED | no |
| §1 | Lemma BF (b-freeze) | PROVED | no |
| §2 | Lemma RB (route back) | PROVED | no |
| §2 | Corollary WALK (a)-(c) | PROVED | no |
| §3 | Lemma CYC-EV | PROVED | no |
| §3 | Proposition TEV-FB (TEV at the fallback state k) | PROVED | no |
| §4 | Theorem ENT-X | PROVED CONDITIONAL on (P) | yes, only via P-N5-RL EV+ |
| §5 | Corollaries NJB-A, D1, PL-S″ | PROVED CONDITIONAL on (P) | yes, via ENT-X |

- §6 is NOT TO SIGN: NJB in full (the straddling interval), TEV at S4a states (FALSE as a conjecture; a lane reading only), level −1
  fallbacks. §7: data.

## 0. Objects, dependencies and their status
- Objects: as in P-N5-FBW §0 (docs/si/P-N5-FBW-box9.md, sha1 88337bd6; RESULTS R31): N5, S4a / S4c, Ξ, W, gates (Ξ_k-improving Even
  edges), gate levels, M_k (max gate level), lev, COARSE_L, (C1)-(C7), b_k(y) := Ξ_k(σ_k y), θ := Ξ(o), w := W(o), R̄ / R / F, H1-H3,
  (h), r := lev(θ, w), THR, phase (λ_Ξ and τ constant), scope run S.
  - In a phase, τ is constant; e* := τ(o). Under (h), the threat x_s := σ̄_s(o) ∈ F_s (H1) and e* ∈ F_s (H2).
  - c := the common cycle node of θ and w along S (H3; w is constant on S, so c is constant on S).
  - For L fixed, H := V_{>max(L, rank c)}. "High" means in H; a set is "low" if it is disjoint from H.
  - For v ∈ R_s, the route π_v^s is the vertex SET of v's (σ_s, τ)-play from v (included) up to o (excluded). For Even v ∈ R_s,
    π_v^s = {v} ⊔ π_{σ_s v}^s, and π_o^s := ∅.
  - The pre-c path of a play from x: its vertices before the first visit to c. For a value with cycle node c, P(·) is the set of
    pre-c-path vertices of rank > rank c (real values; P-N5-P1 §1).
- LANDED (RESULTS), used:
  - R15 (a): Ξ_k ⊴ Ξ_{k+1}.
  - R19 (a) Lemma G: off R̄_s, Ξ_s = W_s. Under (h), for v ∈ R̄_s: Ξ_s(v) = π_v^s ⊕ θ_s with π_v^s ⊆ R_s, and P(π ⊕ θ) = (π ∩ V_{>c}) ⊔ P(θ)
    (with o ∈ P(θ) iff rank o > rank c).
  - R29: (a) Fact R (r non-increasing along S); (c) OFFGATE; (e) NL (i)-(iii).
  - R31: FBW-S, CLS2, FLAT-ALL (i)-(iv), Theorem PL (a)-(b).
  - R35: RDROP, the NO-RF-OLD Corollary, ENT-SHAPE (1)-(4).
- IN REVIEW, used: P-N5-RL (docs/si/P-N5-RL-box10.md, sha1 0a3c70cb, pinned trunk 2fb698d), only in §4, through Proposition EV+.
  - REFEREE succ. 8 (docs/referee/R-N5-RL.md, referee b7419da / 257c3d8) signed EV and EV+ CONDITIONAL ON (P), EV with RL-4 (citation).
    It signed MERGE with RL-2 (restricted to −1 ≤ ℓ < ∞, which covers EV / EV+'s use at L ≥ 0), and FREE-FREEZE and BL (c)
    CONDITIONAL ON (P).
  - Fixes: docs/si/P-N5-RL-fixes-box10.md (sha1 ac027458), RL-1 to RL-4.
  - REFEREE-2's report is pending (its items go to P-N5-RL-fixes2-box10.md).
  - EV+'s chain: EV+ ⇐ EV + MERGE (c) at level L; EV ⇐ FREE-FREEZE ⇐ BL (c) ⇐ (P); EV also uses ENT-SHAPE (4) and the NO-RF-OLD
    Corollary (R35).
  - Nothing else from P-N5-RL is used. In particular, TEV-RED is NOT used: its unconditional parts are re-proved here (§3), and RL-1
    does not arise.
- (P), the premise: in a one-player game, an Even strategy with no improving edge is optimal (R18's premise; P-N5-RL §0).
  - It is discharged by P-N5-P1 (docs/si/P-N5-P1-box10.md, sha1 b98ca794, pinned trunk 48a8a4c), Lemma P1, PROVED by L-SI succ. 5,
    unrefereed.
- SETTING (Σ). S is a scope run, k0 < k are CONSECUTIVE fallbacks of S, L := M_{k0} ≥ 0, and r_s > L for every s ∈ [k0+1, k].
  - Ev := F_{k0+1} ∖ F_{k0}, the vertices evicted at k0. A := P(θ_{k0}) ∩ H, B := P(θ_k) ∩ H.
  - A RISE: some S4a step in (k0, k) changes COARSE_L(θ).
  - THE ENT SETTING: (Σ), a rise, and M_k = L. (This is P-N5-RL §6's setting.)
- Facts in (Σ) (each from landed results):
  - (Σ1) Every transition s → s+1 with k0 < s < k is an in-phase S4a step: there is no fallback in (k0, k), and τ is constant.
  - (Σ2) (h) holds at every state of [k0, k] (each is the source of a transition of S), and (A_s) holds for L at every s ∈ [k0+1, k]
    (OFFGATE at k0+1, then NL (iii); R29 (f)'s chain).
  - (Σ3) No leave: NL (ii) at each S4a step of (k0, k) gives R_s ⊆ R̄_{s+1}. Hence F_k ⊆ F_s for every s ∈ [k0+1, k], F_k ⊆ F_{k0+1} =
    F_{k0} ⊔ Ev, and Ev ∩ F_k = R_{k0} ∩ F_k.
  - (Σ4) M_k ≤ L (CLS2: fallback levels are non-increasing along S).
  - (Σ5) c ∈ F_{k0} ∩ F_k: c lies on the threat's free play, and c ≠ o by H1.
  - (Σ6) After a rise, B ≠ A. θ is ⊴-monotone (R15 (a)), so COARSE_L(θ) is ⊴_L-monotone (C1), and a strict step cannot be undone (C3).
    Both values have cycle node c.

## 1. Lemma FZ and Lemma BF (PROVED, L-SI succ. 6; setting (Σ))
**Lemma FZ.** If v ∈ F_k, then v ∈ F_s for every s ∈ [k0+1, k], and COARSE_L(Ξ_k v) = COARSE_L(Ξ_{k0} v).
Proof.
- v ∈ F_s by (Σ3).
- Across k0: FLAT-ALL (iii) with M_{k0} = L ≥ 0 and (h) at k0 and k0 + 1 gives COARSE_L(Ξ_{k0+1} v) = COARSE_L(Ξ_{k0} v).
- At each S4a step s → s+1, k0 < s < k: NL (i) gives COARSE_L(Ξ_{s+1} v) = COARSE_L(Ξ_s v). Its hypotheses are (h) at s, r_s > L, (A_s)
  (Σ2), and v ∉ R̄_{s+1}. □
**Lemma BF.** If v is Even, v ∈ R_{k0} ∩ F_k, and a := σ_{k0}(v), then COARSE_L(b_k v) = COARSE_L(Ξ_{k0} a), and both have cycle node c.
Proof.
- At k0: Ξ_{k0}(v) = v ⊕ Ξ_{k0}(a) (Lemma G), with cycle node c.
- At k: Ξ_k(v) has cycle node c (Lemma FZ; COARSE_L keeps the cycle node). Also v ≠ c, since c ∈ F_{k0} (Σ5) and v ∈ R_{k0}. So (P2)
  gives Ξ_k(v) = v ⊕ b_k(v).
- At either state, v is not on the pre-c path of its successor's play.
  - Otherwise v's play returns to v before it reaches c. In a functional graph, v then lies on a cycle.
  - If c is on that cycle, c is met before the return to v.
  - If c is not on it, c is never met.
  - Both contradict "cycle node c".
- So, by (C4), for x = Ξ_{k0}(a) at k0 and x = b_k(v) at k: P(x) ∩ V_{>L} = (P(Ξ v) ∩ V_{>L}) ∖ {v}, at the matching state.
- Lemma FZ makes the right side the same at k0 and at k. □

## 2. Lemma RB and Corollary WALK (PROVED, L-SI succ. 6; setting (Σ))
**Lemma RB.** If v is Even, v ∈ R_{k0} ∩ F_k, and a := σ_{k0}(v) ∈ R̄_k, then COARSE_L(Ξ_k a) = COARSE_L(Ξ_{k0} a).
Proof.
- (v, a) is an edge with a ≠ σ_k(v): σ_k(v) ∈ F_k because v ∈ F_k, and a ∈ R̄_k.
- Ξ_k(a) ⊵ Ξ_{k0}(a) (R15 (a)), so COARSE_L(Ξ_k a) ⊵_L COARSE_L(Ξ_{k0} a) (C1). The right side equals COARSE_L(b_k v) (Lemma BF).
- Suppose the inequality is strict. Then Ξ_k(a) ▷ b_k(v): otherwise (C1) would give COARSE_L(Ξ_k a) ⊴_L COARSE_L(b_k v), against
  strictness and (C3). And lev(b_k v, Ξ_k a) > L (C2).
- So (v, a) is a gate at k of level > L ≥ M_k (Σ4). That is impossible. □
**Corollary WALK.** Let v0 ∈ R_{k0} ∩ F_k, with k0-route v0 = a_0, a_1, …, a_m and a_{m+1} = o. Let j := min{i ≥ 1 : a_i ∈ R̄_k}, which
exists because o ∈ R̄_k. Put v := a_{j−1}. Then:
- (a) v ∈ R_{k0} ∩ F_k, v is Even, and σ_{k0}(v) = a_j;
- (b) (π_{a_j}^k ∩ H) ⊔ B = (π_{a_j}^{k0} ∩ H) ⊔ A (for a_j = o both routes are empty);
- (c) if v0's route after v0, π_{a_1}^{k0}, is low, then B ⊆ A.
Proof.
- (a) v ∈ F_k by the choice of j. v ∈ R_{k0}, since it lies on v0's k0-route.
  - If v were Odd, then v ≠ o, and its only successor is its k0-successor a_j ∈ R̄_k. That would put v in R̄_k.
  - So v is Even, and its k0-successor is a_j.
- (b) Lemma RB at v gives COARSE_L(Ξ_k a_j) = COARSE_L(Ξ_{k0} a_j).
  - By Lemma G at s ∈ {k0, k}, COARSE_L(Ξ_s a_j) = (c, P(π_{a_j}^s ⊕ θ_s) ∩ V_{>L}).
  - Since P(·) ⊆ V_{>c}, its path part is (π_{a_j}^s ∩ H) ⊔ (P(θ_s) ∩ H).
- (c) π_{a_j}^{k0} ⊆ π_{a_1}^{k0}, since j ≥ 1. If the latter is low, (b) reads (π_{a_j}^k ∩ H) ⊔ B = A. □

## 3. Lemma CYC-EV and Proposition TEV-FB (PROVED, L-SI succ. 6; no (P))
Setting: (Σ) and a rise (so B ≠ A by (Σ6)). M_k = L is NOT assumed: (Σ4) suffices.
**Lemma CYC-EV.** No vertex of Ev ∩ F_k lies on C_k, the σ_k-cycle of c. (C_k is the cycle of x_k's play.)
Proof.
- Let v ∈ Ev ∩ F_k lie on C_k. Then v ≠ c (c ∉ Ev by (Σ5)).
- c tops C_k, so the path from v to c along C_k has no vertex of rank > rank c. Hence COARSE_L(Ξ_k v) = (c, ∅).
- v ∈ Ev ⊆ R_{k0}. Lemma FZ and Lemma G at k0 give COARSE_L(Ξ_{k0} v) = (c, (π_v^{k0} ∩ H) ⊔ A) = (c, ∅). So A = ∅, and v's k0-route is low.
- Corollary WALK (c) from v0 := v gives B ⊆ A = ∅. So B = A, against (Σ6). □
**Proposition TEV-FB.** The σ_k-play of x_k avoids Ev.
Proof. Suppose not. The play is the pre-c path p_0 = x_k, …, p_{N−1}, then c = p_N, then C_k. By CYC-EV, some p_i with i < N lies in Ev.
Let i be the largest such index, e := p_i, and f := p_{i+1}.
- Step 1: f ∈ F_{k0}, and e is Even.
  - f ∈ F_k, and f ∉ Ev: by the choice of i, or because f = c. Since F_k ⊆ F_{k0} ⊔ Ev (Σ3), f ∈ F_{k0}.
  - If e were Odd, then e ≠ o, and its only successor f would be its k0-successor. That lies in R̄_{k0}, because e ∈ R_{k0}.
- Step 2: COARSE_L(Ξ_k f) = (c, A); the k0-route of u_e := σ_{k0}(e) is low; and o ∉ H.
  - Lemma FZ at f: COARSE_L(Ξ_k f) = COARSE_L(Ξ_{k0} f). Since f ∈ F_{k0}, its k0-play avoids o and stays in F_{k0}, so P(Ξ_{k0} f) ⊆ F_{k0}.
  - Lemma BF at e, with b_k(e) = Ξ_k(f): COARSE_L(Ξ_k f) = COARSE_L(Ξ_{k0} u_e) = (c, (π_{u_e}^{k0} ∩ H) ⊔ A).
  - So (π_{u_e}^{k0} ∩ H) ⊔ A ⊆ F_{k0}. π_{u_e}^{k0} ⊆ R_{k0} is disjoint from F_{k0}, so π_{u_e}^{k0} ∩ H = ∅.
  - Also o ∉ A. o is the first vertex of θ_{k0}'s play and is not its cycle node, so o ∈ P(θ_{k0}) iff rank o > rank c. Hence
    o ∉ A means rank o ≤ max(L, rank c), i.e. o ∉ H.
- Step 3: A ⊆ B, so B ⊄ A.
  - None of o, p_0, …, p_i is the cycle node c. By (P2) along them, θ_k = o ⊕ p_0 ⊕ … ⊕ p_i ⊕ Ξ_k(f).
  - By (C4) and o ∉ H: B = ({p_0, …, p_i} ∩ H) ∪ (P(Ξ_k f) ∩ H) = ({p_0, …, p_i} ∩ H) ∪ A.
  - B ≠ A (Σ6), so B ⊄ A.
- Step 4: e ∈ Ev ∩ F_k = R_{k0} ∩ F_k, and its route after e is π_{u_e}^{k0}, low by Step 2. Corollary WALK (c) from v0 := e gives
  B ⊆ A, against Step 3. □
- Reading. This is (the dead) CONJECTURE TEV at the single state t = k, where the fallback forbids gates of level > L (Σ4). At S4a states
  TEV is FALSE (L-RED 16: experiments/red/so/instances/tevlast_cex_n40.pg, sha1 ff1e9cb4, k0 = 3, t = 7, L = 32). There the walk's vertex
  v = 15 carries the gate (15, 21) of level 33 at t = 7 and enters R at 8 (checked by L-SI succ. 6; docs/si/P-N5-RL-fixes-box10.md §7).

## 4. Theorem ENT-X (PROVED CONDITIONAL on (P), L-SI succ. 6)
**Theorem ENT-X.** The ENT setting is empty. Equivalently: if k0 < k are consecutive fallbacks of a scope run with M_{k0} = M_k = L ≥ 0 and
r > L on [k0+1, k], then COARSE_L(θ) does not change in (k0, k).
Proof.
- In the ENT setting, P-N5-RL Proposition EV+ (CONDITIONAL on (P)) says the σ_k-play of x_k meets Ev.
  - Its hypotheses are exactly the ENT setting: S, consecutive k0 < k, M_{k0} = M_k = L ≥ 0, r > L on [k0+1, k], and a rise.
  - Its proof uses the level-L window gate at k (NO-RF-OLD Corollary, RL-4), ENT-SHAPE (4), FREE-FREEZE (P) and MERGE (c) at level L.
- TEV-FB says the same play avoids Ev. Contradiction. □
- Where (P) enters: only through EV+, i.e. FREE-FREEZE ⇐ BL (c) ⇐ (P). Everything in §1-§3 is unconditional.
- Where M_k = L enters: only through EV+ (the window gate of level L at k). For M_k < L, TEV-FB still holds, but nothing places the threat
  in Ev.

## 5. Corollaries (PROVED CONDITIONAL on (P), L-SI succ. 6)
**Corollary NJB-A.** Let (f_i, f_{i+1}) be an interval of a level-M block (M ≥ 0) of a scope run, with r > M on [f_i + 1, f_{i+1}]. Then it
is clean: COARSE_M(Ξ) does not change at any transition inside it.
- Proof. Suppose it is dirty, with first change j. By R31 PL (b), j is an S4a step with lev(θ_j, θ_{j+1}) > M, so a rise. Consecutive
  fallbacks of a block are consecutive fallbacks of S (CLS2), so (f_i, f_{i+1}) is the ENT setting with L = M. ENT-X excludes it. □
**Corollary D1.** Every level-M block (M ≥ 0) of a scope run has D_M ≤ 1 (D_M := the number of dirty intervals, R31).
- Proof. r is non-increasing along S (Fact R). Classify the intervals of the block:
  - r > M at every state of [f_i + 1, f_{i+1}]: clean (NJB-A);
  - r ≤ M at f_i + 1: clean, since RDROP puts the first change of a dirty interval at a state with r_j > M;
  - otherwise, r > M at f_i + 1 and r ≤ M at some later state of the interval (the STRADDLING interval). After that state r ≤ M for the
    rest of the block, so there is at most one such interval. □
**Corollary PL-S″.** Every scope run has at most Σ_{M≥0} n_E·(1 + D_M) ≤ 2·n·n_E fallbacks of level ≥ 0.
- Proof. R31 Theorem PL (a), N ≤ n_E(1 + D_M), applied per block. The blocks are disjoint, and there are at most n levels ≥ 0. □
- Compare R35 PL-S′ (signed, unconditional): n_E·(n·d_o + REL(S)). PL-S″ removes REL(S), CONDITIONAL on (P).

## 6. NOT TO SIGN
- CONJECTURE NJB in full (D_M = 0 for every block). Open only for the straddling interval of a block. Once r reaches M (by FBW-S,
  r_{f_{i+1}} ≥ M, so r = M there), NL is unavailable and Lemma FZ fails as stated.
  - DATA: straddling intervals occur 0 times (experiments/si/tev/straddle.py: NAMED 290 block intervals, LIB 357).
- TEV at S4a states: FALSE as CONJECTURE TEV / TEV-LAST (tev_cex_n40, tevlast_cex_n40; docs/si/DEAD.md).
  - Lane reading, not offered (docs/si/N5-TEV-box11.md §5): at a post-rise S4a state the walk's v carries a gate of level > L. It enters
    R̄ at the next step unless it lies on e*'s σ_t-play.
- OPEN: level −1 fallbacks per scope run; G-N5-TIME.

## 7. DATA (DATA, not proof; experiments/si/tev/rb.py and straddle.py, logs experiments/si/tev/logs/, in commit 3f08db7 / 8c10cbf)
- rb.py runs at every (Σ)-pair (consecutive fallbacks k0 < k of a scope run with L = M_{k0} ≥ 0 and r > L on [k0+1, k]). It checks:
  - Lemma RB at every Even v ∈ R_{k0} ∩ F_k with σ_{k0}(v) ∈ R̄_k;
  - Lemma BF there;
  - Corollary WALK (a) for every v0 ∈ R_{k0} ∩ F_k;
  - (Σ4).
  It also counts rises and ENT settings. Runs are asserted equal to n5.py run() (coarse/mono.states), and 𝒞^1O is asserted per game.

| set | (Σ)-pairs | RB / BF checks | WALK checks | violations | rises in (Σ)-pairs | ENT settings |
| --- | --- | --- | --- | --- | --- | --- |
| NAMED (coarse/named.txt + coarse/instances/*.pg + instances/box9/*.pg + riselast/instances/*.pg) | 262 | 344 | 529 | 0 | 0 | 0 |
| LIB (experiments/new/box33/lib.txt, 234, first column) | 377 | 578 | 1,121 | 0 | 0 | 0 |
| tev_cex_n40 (L-RED, 17078f78) | 15 | 16 | 19 | 0 | 0 | 0 |

- Thin spots, stated plainly:
  - No (Σ)-pair in any data has a rise. So CYC-EV, TEV-FB, ENT-X and its corollaries have vacuous hypotheses everywhere, and they rest on
    the proofs.
  - FZ, BF, RB and WALK (a) are exercised non-vacuously.
- Suggested attack for L-RED: a (Σ)-pair with a rise. By TEV-FB its threat at k avoids Ev; by ENT-X it then needs M_k < L.
