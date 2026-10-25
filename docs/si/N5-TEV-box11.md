# N5 box 11 (L-SI successor 6): the TEV-RED configuration cannot occur; NJB in the ENT setting, CONDITIONAL on (P)
L-SI successor 6 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~12:55Z (date -u). Lane write-up, unrefereed.
- Labels: PROVED (L-SI succ. 6) = no (P) used; PROVED CONDITIONAL on (P) = uses (P) through P-N5-RL's EV+; CONJECTURE; OPEN; DATA.
- Everything is on 𝒞^1O: exactly one Odd vertex o with out-degree > 1. The script asserts it.
- These are lemmas about the candidate N5. They are not a running-time bound, not a TARGET.md claim, and not a step-4 pass.
  G-N5-TIME stays OPEN.
- Result in one paragraph.
  - Lemma RB (unconditional): between consecutive fallbacks k0 < k of a scope run with L := M_{k0} ≥ 0 and r > L on [k0+1, k], every
    Even vertex that was in R at k0, is free at k, and whose k0-successor a is back in R̄_k, sees no COARSE_L change at a.
  - Walking along a k0-route from a free vertex to the first vertex of R̄_k turns this into a gate of level > L unless the route
    carries a high vertex.
  - Applied to the route of e (the last evicted vertex on the new threat's play), whose route after e is low by TEV-RED (2), this gives
    a gate of level > L at k, against M_k = L.
  - So the one configuration P-N5-RL §6 left open is empty, and NJB holds in the ENT setting, CONDITIONAL on (P).
  - Corollary: D_M ≤ 1 for EVERY block, so every scope run has ≤ 2·n·n_E fallbacks of level ≥ 0 (CONDITIONAL on (P)). This removes
    REL(S) from R35's PL-S′.
  - TEV itself (at every post-rise state) is not proved and is no longer needed for NJB in the ENT setting.

## 0. Objects and dependencies
- Everything in P-N5-RL §0 (docs/si/P-N5-RL-box10.md, sha1 0a3c70cb; in review). This includes P-N5-FBW §0 (R31): N5, S4a / S4c, Ξ, W,
  gates, gate levels, M_k, lev, COARSE_L, (C1)-(C7), b_k(y) := Ξ_k(σ_k y), θ, w, R̄ / R / F, (h), r, THR, phase, scope run S.
  - c := the common cycle node of θ and w along S. H := V_{>max(L, rank c)}. "High" = in H, "low" = disjoint from H.
  - For v ∈ R_s: π_v^s is v's route at s, the vertex SET of v's (σ_s, τ)-play from v (included) up to o (excluded). For Even v,
    π_v^s = {v} ⊔ π_{σ_s v}^s, and π_o^s := ∅.
  - The pre-c path of a play from x: its vertices before the first visit to c. P(Ξ x) consists of its vertices of rank > rank c
    (P-N5-P1 §1, real values).
- Landed results used: R15 (a) (Ξ_k ⊴ Ξ_{k+1}); R19 (a) Lemma G (on R̄_s under (h): Ξ_s(v) = π_v^s ⊕ θ_s, and P(π ⊕ θ) = (π ∩ V_{>c}) ⊔ P(θ));
  R29 (a) Fact R (r non-increasing along S), (c) OFFGATE, (e) NL (i)-(iii); R31 FBW-S, CLS2, FLAT-ALL (i)-(iv), Theorem PL (a)-(b);
  R35 RDROP, ENT-SHAPE (1)-(4).
- In review, used: P-N5-RL (sha1 0a3c70cb) §6 Proposition EV+ (CONDITIONAL on (P)), and the unconditional parts of TEV-RED (1)-(2)
  re-proved below (Steps 2-3 of §3), so only EV+ is imported. EV+ is the ONLY use of (P) here.
- (P) itself: P-N5-P1 (docs/si/P-N5-P1-box10.md, sha1 b98ca794), Lemma P1, PROVED by L-SI succ. 5, unrefereed.
- THE SETTING (Σ). S is a scope run, k0 < k are consecutive fallbacks of S, L := M_{k0} ≥ 0, and r_s > L for every s ∈ [k0+1, k].
  - Facts in (Σ) (all from landed results; listed in P-N5-RL §6 "Facts used throughout"):
    - (Σ1) every transition s → s+1 with k0 < s < k is an in-phase S4a step (consecutive fallbacks; τ constant in a phase);
    - (Σ2) (A_s) holds for L at every s ∈ [k0+1, k] (OFFGATE at k0+1, then NL (iii));
    - (Σ3) no leave (NL (ii)): F_k ⊆ F_s for every s ∈ [k0+1, k]; in particular F_k ⊆ F_{k0+1};
    - (Σ4) M_k ≤ L (CLS2);
    - (Σ5) A := P(θ_{k0}) ∩ H and B := P(θ_k) ∩ H; c ∈ F_{k0} ∩ F_k (c lies on the threat's free play, and c ≠ o by H1).
  - Ev := F_{k0+1} ∖ F_{k0} (the vertices evicted at k0). By (Σ3), Ev ∩ F_k = R_{k0} ∩ F_k.
- THE ENT SETTING: (Σ) with M_k = L and a COARSE_L(θ) change at some S4a step of (k0, k) (a RISE). Then COARSE_L(θ_k) ≠ COARSE_L(θ_{k0})
  (θ is ⊴-monotone by R15 (a); a strict COARSE_L step θ_j ◁_L θ_{j+1} cannot be undone, by (C1) and (C3)), so B ≠ A.

## 1. Lemma FZ and Lemma BF (PROVED, L-SI succ. 6; setting (Σ))
**Lemma FZ (freeze).** If v ∈ F_k, then v ∈ F_s for every s ∈ [k0+1, k], and COARSE_L(Ξ_k v) = COARSE_L(Ξ_{k0} v).
Proof.
- v ∈ F_s by (Σ3).
- Across k0: FLAT-ALL (iii) (M_{k0} = L ≥ 0, (h) at k0 and k0+1, since k0 → k0+1 is a transition of S).
- At each S4a step s → s+1 with k0 < s < k: NL (i), with (h) at s, r_s > L, (A_s) (Σ2), and v ∉ R̄_{s+1}. □
**Lemma BF (b-freeze).** If v is Even, v ∈ R_{k0} ∩ F_k, and a := σ_{k0}(v), then COARSE_L(b_k v) = COARSE_L(Ξ_{k0} a), and both have the
cycle node c.
Proof.
- At k0, v ∈ R_{k0}, so Ξ_{k0}(v) = v ⊕ Ξ_{k0}(a) (Lemma G), with cycle node c.
- At k, Ξ_k(v) has cycle node c (Lemma FZ; COARSE_L keeps the cycle node). v ≠ c, since c ∈ F_{k0} and v ∈ R_{k0}. So (P2) gives
  Ξ_k(v) = v ⊕ b_k(v).
- v is not on the pre-c path of its successor's play, at k0 or at k. Otherwise v's play would return to v before it reaches c; in a
  functional graph v would then lie on a cycle that c is either on (and then c is met before the return to v) or off (and then c is
  never met). Both contradict "cycle node c".
- So, by (C4), for x ∈ {Ξ_{k0}(a), b_k(v)}: P(x) ∩ V_{>L} = (P(Ξ v) ∩ V_{>L}) ∖ {v}, at the matching state.
- Lemma FZ makes the right side the same at k0 and at k. □

## 2. Lemma RB and the walk (PROVED, L-SI succ. 6; setting (Σ))
**Lemma RB.** If v is Even, v ∈ R_{k0} ∩ F_k, and a := σ_{k0}(v) ∈ R̄_k, then COARSE_L(Ξ_k a) = COARSE_L(Ξ_{k0} a).
Proof.
- a ≠ σ_k(v): σ_k(v) ∈ F_k because v ∈ F_k, and a ∈ R̄_k.
- Ξ_k(a) ⊵ Ξ_{k0}(a) (R15 (a)), so COARSE_L(Ξ_k a) ⊵_L COARSE_L(Ξ_{k0} a) = COARSE_L(b_k v) (C1, Lemma BF).
- If the inequality were strict, then Ξ_k(a) ▷ b_k(v) (by (C1) and (C3): Ξ_k a ⊴ b_k v would give the reverse coarse inequality), and
  lev(b_k v, Ξ_k a) > L by (C2). So (v, a) would be a gate at k of level > L, against (Σ4). □
**Corollary WALK.** Let v0 ∈ R_{k0} ∩ F_k, with k0-route v0 = a_0, a_1, …, a_m and a_{m+1} = o. Let j := min{i ≥ 1 : a_i ∈ R̄_k} (it exists,
since o ∈ R̄_k) and v := a_{j−1}. Then:
- (a) v ∈ F_k ∩ R_{k0}, v is Even, and σ_{k0}(v) = a_j;
- (b) (π_{a_j}^k ∩ H) ⊔ B = (π_{a_j}^{k0} ∩ H) ⊔ A   (for a_j = o both routes are empty);
- (c) in particular, if v0's route after v0, π_{a_1}^{k0}, is low, then B ⊆ A.
Proof.
- (a) v ∈ F_k by the choice of j, and v ∈ R_{k0} lies on v0's k0-route. If v were Odd, then v ≠ o and its only successor a_j ∈ R̄_k
  would put v in R̄_k.
- (b) Lemma RB at v. By Lemma G at k0 and at k (both states have (h)), COARSE_L(Ξ a_j) at s ∈ {k0, k} is
  (c, (π_{a_j}^s ∩ V_{>c} ∩ V_{>L}) ⊔ (P(θ_s) ∩ V_{>L})). Since P(·) ⊆ V_{>c}, its path part is (π_{a_j}^s ∩ H) ⊔ (P(θ_s) ∩ H).
- (c) π_{a_j}^{k0} ⊆ π_{a_1}^{k0} for j ≥ 1. If the latter is low, (b) reads (π_{a_j}^k ∩ H) ⊔ B = A. □
- Reading: free vertices evicted at k0 cannot "see" a rise of θ through the part of their old route that comes back to R̄. If that part
  is low, θ cannot have risen at all. Every evicted TAIL y0 of k0 has a low route after y0 (y0's level is ≤ L, as in TEV-RED (2)'s
  computation), so in the ENT setting with A ⊆ B every k0-tail is back in R̄_k.

## 3. Theorem ENT-X (PROVED CONDITIONAL on (P), L-SI succ. 6)
**Theorem ENT-X.** The ENT setting is empty. Equivalently: if k0 < k are consecutive fallbacks of a scope run with M_{k0} = M_k = L ≥ 0 and
r > L on [k0+1, k], then COARSE_L(θ) does not change in (k0, k).
Proof. Suppose the ENT setting holds. Let x_k := σ̄_k(o) ∈ F_k (H1), with pre-c path p_0 = x_k, p_1, …, p_{N−1}, and p_N = c.
- Step 1 [(P), via EV+]. By P-N5-RL Proposition EV+, the σ_k-play of x_k meets Ev.
- Step 1′ [no (P); Lemma CYC-EV]. No vertex of Ev ∩ F_k lies on c's σ_k-cycle C_k. (C_k is the cycle of x_k's play.)
  - Let v ∈ Ev ∩ F_k lie on C_k, v ≠ c (c ∉ Ev, since c ∈ F_{k0}). c tops C_k, so the path from v to c along C_k has no vertex of rank
    > rank c: COARSE_L(Ξ_k v) = (c, ∅).
  - Lemma FZ and Lemma G at k0: COARSE_L(Ξ_{k0} v) = (c, (π_v^{k0} ∩ H) ⊔ A). So A = ∅, and v's whole k0-route is low.
  - B ≠ A = ∅, so B ⊄ A. Corollary WALK (c) from v0 := v gives B ⊆ A. Contradiction.
  - So Ev meets x_k's play on its pre-c path. Let i < N be the LARGEST index with p_i ∈ Ev. Put e := p_i and f := p_{i+1}.
- Step 2 [no (P)]. f ∈ F_{k0} ∩ F_k, and e is Even.
  - f ∈ F_k (it is on x_k's free play) and f ∉ Ev (by the choice of i, or f = c). By (Σ3), F_k ⊆ F_{k0} ⊔ Ev. So f ∈ F_{k0}.
  - If e were Odd, then e ≠ o, and its only successor f would be its k0-successor, which lies in R̄_{k0} since e ∈ R_{k0}.
- Step 3 [no (P); TEV-RED (2) re-proved]. COARSE_L(Ξ_k f) = (c, A), the k0-route of u_e := σ_{k0}(e) is low, and o ∉ H.
  - f ∈ F_k, so Lemma FZ gives COARSE_L(Ξ_k f) = COARSE_L(Ξ_{k0} f). Since f ∈ F_{k0}, P(Ξ_{k0} f) ⊆ F_{k0}.
  - Lemma BF at e: COARSE_L(Ξ_k f) = COARSE_L(b_k e) = COARSE_L(Ξ_{k0} u_e) = (c, (π_{u_e}^{k0} ∩ H) ⊔ A), with A = P(θ_{k0}) ∩ H.
  - So (π_{u_e}^{k0} ∩ H) ⊔ A ⊆ F_{k0}. π_{u_e}^{k0} ⊆ R_{k0} is disjoint from F_{k0}, so π_{u_e}^{k0} ∩ H = ∅. And o ∉ A (o ∉ F_{k0}).
    Since o is the first vertex of θ_{k0}'s play, o ∈ P(θ_{k0}) iff rank o > rank c; so o ∉ A means o ∉ H.
- Step 4 [no (P)]. A ⊆ B, hence B ⊄ A.
  - (P2) along o, p_0, …, p_i (none is the cycle node c): θ_k = o ⊕ p_0 ⊕ … ⊕ p_i ⊕ Ξ_k(f). These vertices are distinct and not on f's
    pre-c path.
  - By (C4) and o ∉ H: B = ({p_0, …, p_i} ∩ H) ⊔ (P(Ξ_k f) ∩ H) = ({p_0, …, p_i} ∩ H) ⊔ A.
  - B ≠ A (ENT setting), so B ⊄ A.
- Step 5 [no (P)]. Contradiction.
  - e ∈ Ev ∩ F_k = R_{k0} ∩ F_k, and its k0-route after e is π_{u_e}^{k0}, low by Step 3.
  - Corollary WALK (c) from v0 := e gives B ⊆ A, against Step 4. □
- Remarks.
  - Steps 1′-5 show more, with no (P): in setting (Σ) with a COARSE_L(θ) change (M_k ≤ L by CLS2; M_k = L not needed), the threat's
    whole σ_k-play at the fallback k avoids Ev (pre-c path by Steps 2-5, cycle by CYC-EV). This is CONJECTURE TEV at the state t = k,
    PROVED (L-SI succ. 6). M_k = L and (P) enter only through EV+ (Step 1), which uses ENT-SHAPE's level-L window gate at k.
  - Lemma CYC-EV (Step 1′) also supplies a detail that P-N5-RL §6 uses without proof: there, "the first (last) Ev vertex" on a play must
    lie on its pre-c path, both for EV's class bookkeeping (Ξ_k(z) = ρ ⊕ Ξ_k(q)) and for TEV-RED (1)-(3). In the ENT setting CYC-EV gives
    this. It belongs in P-N5-RL's fixes file if a referee raises it. Recorded here, not in the frozen packet.
  - The proof does not use FREE-FREEZE's exact equality Ξ_t(f) = Ξ_{k0}(f), only COARSE_L, which is unconditional (Lemma FZ).

## 4. Corollaries (PROVED CONDITIONAL on (P), L-SI succ. 6)
**Corollary NJB-A.** Let (f_i, f_{i+1}) be an interval of a level-M block (M ≥ 0) of a scope run with r > M on [f_i + 1, f_{i+1}]. Then the
interval is clean: COARSE_M(Ξ) does not change inside it.
- Proof. If it were dirty, its first change j is a COARSE_M(θ) change at an S4a step (R31 PL (b)). Then (f_i, f_{i+1}) is the ENT
  setting with L = M, which Theorem ENT-X excludes. □
**Corollary D1.** Every level-M block (M ≥ 0) of a scope run has D_M ≤ 1.
- Proof. Consider the intervals of the block in order. r is non-increasing along S (Fact R).
  - An interval with r > M at all of its states [f_i + 1, f_{i+1}] is clean (NJB-A).
  - An interval with r ≤ M at f_i + 1 is clean, because RDROP puts the first change of a dirty interval at a state with r_j > M.
  - Any other interval has r > M at f_i + 1 and r ≤ M at some later state of it. After that state r ≤ M for the rest of the block.
    So at most one interval is of this kind. □
**Corollary PL-S″.** Every scope run has at most n_E·Σ_M (1 + D_M) ≤ 2·n·n_E fallbacks of level ≥ 0.
- Proof. R31 Theorem PL (a), N ≤ n_E(1 + D_M), per block; blocks are disjoint; there are at most n levels ≥ 0. □
- Compare R35 PL-S′ (signed, unconditional): n_E·(n·d_o + REL(S)). PL-S″ removes REL(S), CONDITIONAL on (P).
- With the per-scope-run counts this does not yet bound G-N5-TIME. What is left for fallbacks inside scope runs: level −1 fallbacks; the
  straddling interval of each block is already counted by D1.

## 5. NOT PROVED here (labels)
- CONJECTURE NJB (full): D_M = 0 for every block. Open only for the one straddling interval of a block (r > M at its start and r = M at its
  end, by FBW-S r_{f_{i+1}} ≥ M). There NL is not available after r reaches M, and Lemma FZ fails as stated. This is successor 5's NEXT 2
  (RISE-LAST "after r ≤ L"). DATA: no rise is ever followed by a fallback (P-N5-RL §8, rlprobe).
- CONJECTURE TEV (L-SI succ. 5): at every post-rise S4a state the threat's play avoids Ev. PROVED at fallback states (§3 Remarks, no (P));
  open at S4a states, and not needed for ENT-X.
  - What the same argument gives at an S4a post-rise state t with r > L on [k0+1, t] (lane reading, not checked by data): if the threat's
    pre-c path meets Ev, then WALK's v carries a gate (v, a) of level > L at t, and then v ∈ R̄_{t+1} unless v lies on e*'s σ_t-play. (The
    switched strategy σ_t[v ↦ a] is in the arena and gives v the value v ⊕ π_a ⊕ w, which is above Ξ_t(v) at a level > L because r > L;
    NL (i) forbids that while v stays free.) So a threat through Ev is absorbed back, one route vertex per step, before the next fallback.
    TEV can thus fail transiently in principle; DATA shows 0 cases.
- OPEN: level −1 fallbacks per scope run; REL(S) is no longer needed for levels ≥ 0 (PL-S″, conditional).
- NOT to be read as: a bound on N5's iterations, a step-4 pass, or a TARGET.md claim.

## 6. DATA (DATA, not proof; experiments/si/tev/rb.py, logs experiments/si/tev/logs/)
- rb.py checks, at every pair of consecutive fallbacks k0 < k of a scope run with L = M_{k0} ≥ 0 and r > L on [k0+1, k]: (RB) Lemma RB,
  (BF) Lemma BF, (WALK) Corollary WALK (a) (the walk's last free vertex is Even), and (Σ4) M_k ≤ L; and counts the ENT setting.
  Runs are asserted equal to n5.py run() (coarse/mono.states), and 𝒞^1O is asserted per game.

| set | pairs (Σ) | RB checks | WALK checks | violations | ENT settings | rises in (Σ) pairs |
| --- | --- | --- | --- | --- | --- | --- |
| NAMED (coarse/named.txt + coarse/instances/*.pg + instances/box9/*.pg + riselast/instances/*.pg) | 262 | 344 | 529 | 0 | 0 | 0 |
| LIB (experiments/new/box33/lib.txt, 234, first column) | 377 | 578 | 1,121 | 0 | 0 | 0 |

- Thin spot: as in P-N5-RL §8, the ENT setting never occurs, so Theorem ENT-X's hypothesis is vacuous in all data. RB, BF and WALK are
  unconditional statements with non-vacuous checks; the theorem rests on the proof.
