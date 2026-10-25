# N5 box 12, part 3 (L-SI successor 7): THR fallbacks with u* = none (r = −1): at most n·n_E + 1 per scope run
L-SI successor 7 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~15:10Z (date -u). Lead GO 14:18Z, box 12, item (1)(a): "the
u* = none fallbacks". Lane write-up, unrefereed; offered as a packet on request (with N5-LV4).
- Labels: PROVED (L-SI succ. 7); PROVED CONDITIONAL on X; CONJECTURE; OPEN; DATA; READING.
- Everything is on 𝒞^1O. Not a running-time bound, not a TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN.
- Result in one paragraph.
  - At r = −1, θ is sandwiched below w at level −1. So COARSE_{−1}(θ) is frozen for the rest of the scope run (Lemma SAND), and no
    "rise" can happen.
  - FLAT-ALL's proof needs u* ≠ none (FBL) only in its part (i). At r = −1, LV-SHAPE and (h) at k + 1 do the same job
    (Lemma FLAT-ALL_{−1}^{none}).
  - Then P-N5-LV's PL_{−1} (b) argument shows that COARSE_{−1}(Ξ) never changes between the first and last r = −1 fallbacks.
  - STRETCH_{−1} gives at most n·n_E + 1 such fallbacks per scope run (Theorem LV-NONE).
  - With N5-LV4's LV-PL′, P-N5-ENT's PL-S″ and R37's EQ-END, every scope run has at most 4·n·n_E + 3 S4c fallbacks (Corollary SCOPE-FB,
    CONDITIONAL; §4).

## 0. Objects and dependencies
- As in P-N5-LV §0 (sha1 d0d797f0) and N5-LV4-box12.md §0.
- LANDED, used:
  - R15 (a), (d); R21 (a) XW (θ ⊴ w);
  - R28 (a) U-loc (any game, inside a phase); R29 (a) Fact R, (C5)-(C7); R29 (b) TRANSFER; R29 (d) CN;
  - R30 (a)-(b) Lemma OR, TC-SPLIT;
  - R31 FBW-S (fallback level ≤ r), FB step (2) (R25 (d)), FLAT-ALL's proof (P-N5-FBW §3);
  - R25 (e) OFF; R18 (d) Lemma S (a); R19 (a) Lemma G;
  - R37 (d) EQ-END.
- IN REVIEW, used: P-N5-LV §1 LV-SHAPE (it covers r = −1), §3 STRETCH_{−1}, §4 PL_{−1} (b)'s proof.
- THE NONE PART of a scope run S: its THR fallbacks with r = −1 (u* = none), g_1 < … < g_N.
  - By FBW-S each has M = −1 (the fallback level is at most r).
  - By Fact R, r is non-increasing along S. So every state of [g_1, g_N] has r = −1: r ≤ −1 after g_1, and r ≥ r_{g_N} = −1 before g_N.
  - In particular, every S4c fallback of S inside [g_1, g_N] is one of the g_i (an EQ state has r = ⊥).

## 1. Lemma SAND (PROVED, L-SI succ. 7)
If t ≤ t′ are states of a scope run S with r_t = −1, then COARSE_{−1}(θ_{t′}) = COARSE_{−1}(θ_t).
- Proof. θ_t ⊴ θ_{t′} (R15 (a)), and θ_{t′} ⊴ w_{t′} = w_t (XW; w is constant on S). If θ_t ◁ θ_{t′}, then (C5) gives
  lev(θ_t, θ_{t′}) ≤ lev(θ_t, w_t) = r_t = −1. So the COARSE_{−1} values are equal (C2). □
- (This is Fact R's proof, read at r = −1.)

## 2. Lemma FLAT-ALL_{−1}^{none} (PROVED, L-SI succ. 7, CONDITIONAL on LV-SHAPE)
Let k be a fallback of a scope run with r_k = −1 (so M_k = −1), and (h) at k and k + 1. Then R31 FLAT-ALL (i)-(iv) hold with M := −1:
- (i) F_k ⊆ F_{k+1}, and every v ∈ R̄_{k+1} lies in R̄_k with the same route;
- (ii) COARSE_{−1}(θ_{k+1}) = COARSE_{−1}(θ_k);
- (iii) COARSE_{−1}(Ξ_{k+1} v) = COARSE_{−1}(Ξ_k v) for every v;
- (iv) M_{k+1} ≤ −1.
Proof.
- The switched edges. Each tail switches along a gate (R15 (d)). By LV-SHAPE (setting (LV), which includes r = −1) each gate is:
  - (α) F → F at the tail's own cycle node; or
  - (γ) F → R̄ at the tail y = c; or
  - (β) R → F.
- (i) R31's proof, with one change for (γ).
  - A switched cycle node y′ (kinds (α), (γ)) keeps λ(y′) = y′ (phase), so its H_{k+1}-play is a cycle through y′.
    - If that cycle contained o, o would lie on an honest cycle at k + 1, against H1 at k + 1.
    - So the cycle avoids o. The (σ_{k+1}, τ)-play from y′ follows it (they differ only at o), so y′ ∈ F_{k+1}.
    - For (γ) this is the new point: the target z lies in R̄_k, but y′'s new play avoids o anyway.
  - An F_k vertex's play under σ_{k+1}:
    - it follows σ_k inside F_k (F_k is closed under σ_k) until it meets a switched cycle node;
    - from there it follows that node's cycle, which avoids o;
    - (β) tails are in R_k, so they are not met.
    So F_k ⊆ F_{k+1}.
  - A play that reaches o at k + 1 meets no switched vertex:
    - after a (β) tail it continues in F_k, whose plays avoid o;
    - after a switched cycle node it stays on that node's cycle, which avoids o.
    So it is the same play as at k.
- (ii)-(iv) R31's proof verbatim. It uses (i), H1, Lemma S (a), R15 (a), OFF at level M_k = −1, (C7), (C1), (C3), Lemma G (b) at k and
  k + 1 with the same route, and TRANSFER. None of these uses u* ≠ none. (ii) also follows from SAND. □

## 3. Theorem LV-NONE (PROVED, L-SI succ. 7, CONDITIONAL on P-N5-LV §1, §3)
Every scope run S has at most n·n_E + 1 THR fallbacks with r = −1 (u* = none).
Proof. Let g_1 < … < g_N be those fallbacks (§0). If N ≤ 1 there is nothing to show.
- (1) COARSE_{−1}(Ξ_t v) is the same for every t ∈ [g_1, g_{N−1} + 1] and every v. Induction along the states.
  - At each g_i with i < N: FLAT-ALL_{−1}^{none} (iii). (h) holds at g_i + 1 because S continues after g_i (its next transition is in S).
    Also M_{g_i+1} ≤ −1 by (iv).
  - At an S4a step j ∈ (g_i, g_{i+1}): suppose COARSE_{−1}(Ξ) is unchanged on [g_i + 1, j]. This is P-N5-LV PL_{−1} (b)'s argument:
    - M_j ≤ −1 (TRANSFER from M_{g_i+1} ≤ −1);
    - every relevant Even change at j has level ≤ −1 (R15 (d)), so E_j ≤ −1;
    - U-loc with L = −1 (R28 (a): any game, inside a phase) freezes COARSE_{−1}(Ξ v) unless v's path before λ(v) carries a relevant change
      of level > −1. So a change at j needs the relevant σ̄(o) change with O_j > −1 ≥ E_j;
    - then j is an ε-transition, and Lemma OR (c) / TC-SPLIT give lev(θ_j, θ_{j+1}) = O_j ≥ 0.
    - But r_j = −1 (§0), so SAND gives lev(θ_j, θ_{j+1}) ≤ −1. Contradiction. So COARSE_{−1}(Ξ_{j+1}) = COARSE_{−1}(Ξ_j).
  - Every fallback strictly inside [g_1, g_N] is some g_i (§0).
- (2) Each g_i has a level −1 tail (FB step (2): M = −1 is attained by a switched edge).
  - STRETCH_{−1} (P-N5-LV §3) on [g_1, g_{N−1} + 1] bounds the fallbacks g_1, …, g_{N−1} by n·n_E.
  - Its proof uses only the constant COARSE_{−1}, CN (R29 (d)), (P2), (C7), R15 (a), (d) and FB step (2). There is no r hypothesis.
- So N ≤ n·n_E + 1. □
- Note. Neither NL nor FBL is used. The missing "NL at L = −1" (P-N5-LV §5 (i)) is not needed: SAND makes every θ-change at r = −1 a
  length change, and U-loc + TC-SPLIT show that only a θ-change of level ≥ 0 could move COARSE_{−1}(Ξ).

## 4. Corollary SCOPE-FB (PROVED CONDITIONAL; L-SI succ. 7)
Every scope run has at most 4·n·n_E + 3 S4c fallbacks. They are THR or EQ, since (h) holds at every source state of S. By kind:
- level ≥ 0: ≤ 2·n·n_E. This is PL-S″ (P-N5-ENT §5): REFEREE signed it CONDITIONAL ON (P), (P) is R36, and R2-N5-ENT is pending.
  - Unconditionally, R35 PL-S′ gives n_E·(n·d_o + REL(S)).
- level −1 with r ≥ 0: ≤ n·n_E + 1 (N5-LV4 LV-PL′, CONDITIONAL on P-N5-LV §1-§4);
- r = −1: ≤ n·n_E + 1 (LV-NONE, CONDITIONAL on P-N5-LV §1, §3);
- EQ: ≤ 1 (R37 (d) EQ-END: after the first state with θ = w, at most one fallback).
- These classes are disjoint, and they cover every fallback of S:
  - a THR fallback has r ≥ 0 or r = −1;
  - if r ≥ 0, its level is ≥ 0 or −1.
- READING (Lead to rule): this closes the per-scope-run fallback count (R29's CL-S) up to the reviews named above. G-N5-TIME still needs
  the rest: scope runs per phase (R38 SCOPE-COUNT: polynomial in (T, f, X)), out-of-scope fallbacks, S4a steps, phases, and X.

## 5. DATA
- THR fallbacks with r = −1 in scope: 0 in all data (P-N5-LV §6; experiments/si/lv/logs/corpus_*.txt, perturbed start pairs included).
  So LV-NONE and FLAT-ALL_{−1}^{none} have vacuous hypotheses in data and rest on the proofs.
- OPEN, outside this note: an instance with an in-scope u* = none fallback at all. It would be a useful seed for L-RED: the fallback must
  have only (α), (β), (γ) gates, all of level −1 (LV-SHAPE).
