# Referee packet P-N5-FB: coarse super-solutions, the max gate level, and fallbacks per phase (box 7 lemmas)
L-SI successor 3 (Opus 5.5, D18/L40). Written 2026-10-24 22:1xZ-22:3xZ (date -u), at the Lead's request (21:5xZ).
- Self-contained: definitions, statements, full proofs, the location of every dependency, and the data with the scripts that produce it.
- Source text: docs/si/N5-C-box7.md §1-§6 (lane write-up, l-si 25d16cc8). Where the two differ, this packet governs.
- Status: L-SI successor 3's proofs, unrefereed.
  - §2-§4 hold on EVERY parity game. §5 is on 𝒞^1O.
  - These are lemmas about the candidate N5. They are not a running-time bound, not a TARGET.md claim, and not a step-4 pass.
    G-N5-TIME stays OPEN.
- Labels: PROVED (L-SI succ. 3), DATA, FALSE, CONJECTURE, OPEN.
- Statements:
  - §2 Claim (T) and Lemma COARSE-SI: (a) under (NC), with its converse; (b) TAME;
  - §3 Lemma MONO, Lemma NOINF;
  - §4 Theorem FB and its Corollary;
  - §5 J1, OFF, CAP (𝒞^1O).
  §6: the refuted (JUMP-EQ) and the status of A. §7: data.

## 0. Objects and dependencies
- N5: docs/new/N5-ssi-global.md SPEC S1-S5; code experiments/new/n5.py.
  - S4a (Even's arena step): every Even v uses an edge of {σ_k(v)} ∪ Iσ_k(v).
  - S4c (fallback): it happens iff S4a returns σ_k and S4b returns τ_k. If Iσ_k ≠ ∅, EVERY Even vertex with an Iσ_k edge switches to
    its best one, by (Ξ_k-key, larger index); τ is unchanged (SPEC FIX 3). n5.py lines `if Is:` / `for v in {v for v, _ in Is}: ns[v]
    = max(...)`.
- Gate: (v, z) ∈ Iσ_k iff z ≠ σ_k(v) and Ξ_k(z) ▷ Ξ_k(σ_k v) (si.py `improving`).
- Valuations: Vöge-Jurdziński, BRICS RS-00-48, pdf sha256 485a12de… (the file of R15; opened by L-SI succ. 3 on 2026-10-24 21:35Z
  from www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf). Used by page:
  - p. 14, definition of σ̄: σ̄(v) is a successor w of v with Ω_σ(w) ⊴ Ω_σ(u) for all u ∈ succ(v).
  - p. 14, definition of Prog(Ξ, (v, w)):
    - (P1) Λ(v) = Λ(w);
    - (P2) if Λ(v) ≠ v then Π(v) = Π(w) ⊕ v;
    - (P3) if Λ(v) = v then Π(v) = (∅, 0).
  - p. 15, Lemma 5.2: Ξ is locally progressive for σ and τ iff Ξ = Θ_{στ}. In the proof, the cycle node of a play is the max≤
    (most relevant) vertex of its cycle.
  - p. 16, (11): Ω_σ = Θ_{σσ̄}, "hence … Θ_{σσ̄} ⊴ Θ_{στ}, for all strategies τ".
- Representation (si.py, = VJ00 modulo the cycle node):
  - a valuation is x = (c, P, ℓ): cycle node c; P = the path vertices of rank > rank c; ℓ = the path length;
  - ranks by (priority, index);
  - ⊴ compares reward(c), then P by its top differing rank's parity, then ℓ by c's parity;
  - u ⊕ (c, P, ℓ) := (c, P ∪ ({u} if rank u > rank c), ℓ + 1).
  - Ξ_k := Θ_{σ_k σ̄_k} (honest). λ_k(v) := its cycle node. H_k := the (σ_k, σ̄_k)-graph (one successor per vertex).
- Signed results used:
  - R15 (a) Lemma A: for any non-empty unambiguous set I of improvements, Ω_σ ⊴ Ω_{Switch_I(σ)}. With R15 (d): Ξ_k ⊴ Ξ_{k+1} at every
    N5 iteration.
  - R15 (d): every N5 iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to σ (or leaves σ unchanged). So σ_{k+1}(v) ∈ {σ_k(v)} ∪ Iσ_k(v)
    for every Even v.
  - R21 (c) Lemma FBL-N (i): at an S4c fallback with τ unchanged, the fallback is Even's.
  - R23 (g) Lemma WM: inside a phase every W-decrease is at an S4c fallback. Used only in the Corollary of §4.
- PHASE (§4, §5): a joint λ-phase with τ constant (R21 setting; key (λ_Ξ, λ_U, τ)). Only "λ_Ξ and τ constant" is used.
- 𝒞^1O (§5): exactly one Odd vertex o has out-degree > 1. R̄_k := {o} ∪ {v ≠ o : v's (σ_k, τ_k)-play reaches o}, as in R23.
  - On 𝒞^1O whether a play reaches o does not depend on Odd's choices before o, so R̄_k is also "the v whose H-play, for ANY Odd
    strategy agreeing with the forced edges, reaches o".

## 1. Levels and coarse values (elementary)
- lev(x, y) := ∞ if the cycle nodes differ; else the top rank of P(x) Δ P(y); else −1 if only the lengths differ; ⊥ if x = y.
  Order: ⊥ < −1 < 0 < … < n − 1 < ∞.
- COARSE_L(x) := (c, P ∩ V_{>L}) for −1 ≤ L < ∞, where V_{>L} = the vertices of rank > L. COARSE_∞ is constant; COARSE_⊥(x) := x.
  - ⊴_L compares coarse values by reward(c) and then by the restricted path set.
- (C1) x ⊴ y ⇒ COARSE_L x ⊴_L COARSE_L y.
  - If the cycle nodes differ, the verdict is the same.
  - If the top differing rank r is > L, the coarse comparison has the same top difference.
  - Otherwise the coarse values are equal.
- (C2) COARSE_L x = COARSE_L y ⟺ lev(x, y) ≤ L. (Definition.)
- (C3) ⊴_L is antisymmetric on coarse values (Σ ±2^rank is injective on sets).
- (C4) COARSE_L(u ⊕ x) is a function of u and COARSE_L(x): it is (c, (P ∩ V_{>L}) ∪ ({u} if rank u > max(rank c, L))).
- Gate level of (y, z) ∈ Iσ_k: lev(Ξ_k(σ_k y), Ξ_k(z)). It is ≥ −1, since the gate edge is strict.
- **M_k** := the max gate level at k, or ⊥ if Iσ_k = ∅.
- k → k+1 is **TAME** if COARSE_{M_k}(Ξ_{k+1}) = COARSE_{M_k}(Ξ_k) pointwise.

## 2. Claim (T) and Lemma COARSE-SI (PROVED, L-SI succ. 3)
**(T).** Let L < ∞ and let H′ be a functional graph on V with:
- (E) COARSE_L(Ξ_k(succ_{H′} p)) = COARSE_L(Ξ_k(succ_{H_k} p)) for every vertex p on the H′-play from v;
- every vertex t of that play's cycle that is its top satisfies λ_k(t) = t.
Then COARSE_L(Θ_{H′}(v)) = COARSE_L(Ξ_k(v)). Here Θ_{H′}(v) is the VJ00 play value of v's H′-play: cycle node = top of its cycle;
path = the prefix before the first visit of the cycle node.
Proof.
- Let p_0 = v and p_{i+1} = succ_{H′}(p_i).
- (i) λ_k(p_i) = λ_k(v) =: c for every i.
  - (P1) for Ξ_k on the H_k-edge (p_i, succ_{H_k} p_i) (Lemma 5.2) gives λ_k(p_i) = λ_k(succ_{H_k} p_i).
  - By (E) with L < ∞, the cycle nodes of Ξ_k(succ_{H_k} p_i) and Ξ_k(p_{i+1}) agree. Induction.
- (ii) Let t be the top of the play's cycle. By (i) λ_k(t) = c, and by hypothesis λ_k(t) = t; so t = c.
  - Let s be the first index with p_s = c. Then p_0, …, p_{s−1} are distinct, and Θ_{H′}(p_i) = p_i ⊕ … ⊕ p_{s−1} ⊕ (c, ∅, 0) for
    i ≤ s.
- (iii) For i < s, p_i ≠ c = λ_k(p_i), so (P2) gives Ξ_k(p_i) = p_i ⊕ Ξ_k(succ_{H_k} p_i).
  - By (C4) and (E): COARSE_L(Ξ_k(p_i)) = COARSE_L(p_i ⊕ Ξ_k(p_{i+1})).
  - (P3): Ξ_k(p_s) = (c, ∅, 0).
  - Downward induction on i, with (C4): COARSE_L(Ξ_k(p_i)) = COARSE_L(Θ_{H′}(p_i)). Take i = 0. □

**COARSE-SI (a), general form.** Let L < ∞, and suppose every switched edge (y, σ_{k+1} y) has gate level ≤ L at k (for example
L = M_k). Let H′ be the (σ_{k+1}, σ̄_k)-graph and assume
- (NC) every cycle of H′ has its top t with λ_k(t) = t.
Then COARSE_L(Ξ_{k+1}) = COARSE_L(Ξ_k) pointwise.
Proof.
- H′ differs from H_k only at switched Even vertices.
- At such a vertex, R15 (d) and the hypothesis give (E) via (C2). Elsewhere (E) is trivial.
- (T) gives COARSE_L(V) = COARSE_L(Ξ_k) for V := Θ_{σ_{k+1} σ̄_k}.
- Ξ_k ⊴ Ξ_{k+1} (R15 (a)) ⊴ V (VJ00 (11), applied to σ_{k+1} and the Odd strategy σ̄_k).
- By (C1), COARSE_L(Ξ_k) ⊴_L COARSE_L(Ξ_{k+1}) ⊴_L COARSE_L(V) = COARSE_L(Ξ_k). By (C3) all three are equal. □
**Converse (PROVED).** If L < ∞ and (NC) fails, then COARSE_L(V) ≠ COARSE_L(Ξ_k) at the top t of a bad cycle.
- V(t) has cycle node t, while Ξ_k(t) has cycle node λ_k(t) ≠ t.

**COARSE-SI (b), Lemma TAME.** Suppose λ_{k+1} = λ_k, and every Odd u has lev(Ξ_k(σ̄_k u), Ξ_k(σ̄_{k+1} u)) ≤ M_k. Then
k → k+1 is tame.
Proof.
- If M_k = ∞, there is nothing to show.
- If M_k = ⊥: Iσ_k = ∅, so σ_{k+1} = σ_k (R15 (d)) and Ξ_{k+1} = Ξ_k.
- Otherwise apply (T) with H′ := H_{k+1}.
  - (E) holds:
    - at switched Even vertices by R15 (d) and (C2);
    - at Odd vertices by hypothesis;
    - elsewhere trivially.
  - Every cycle of H_{k+1} has its top t with λ_{k+1}(t) = t (Lemma 5.2), and λ_{k+1} = λ_k.
  - Θ_{H_{k+1}} = Ξ_{k+1}. □
- Note: (b) does not use VJ00 (11) or R15 (a).

## 3. Lemma MONO and Lemma NOINF (PROVED, L-SI succ. 3)
**MONO.** If k → k+1 is tame, then M_{k+1} ≤ M_k.
Proof.
- Write M := M_k. If M = ∞ there is nothing to show; if M = ⊥, Ξ and σ are unchanged and Iσ_{k+1} = ∅. Otherwise:
- Let (y, z) ∈ Iσ_{k+1} and u := σ_{k+1}(y).
- COARSE_M(Ξ_k u) = COARSE_M(Ξ_k σ_k y): u = σ_k y, or u is a gate target at k of level ≤ M (R15 (d), (C2)).
- If COARSE_M(Ξ_k z) ▷_M COARSE_M(Ξ_k u), then Ξ_k(z) ▷ Ξ_k(σ_k y) at a level > M (C1, C2). So (y, z) ∈ Iσ_k has level > M,
  which is impossible. Hence COARSE_M(Ξ_k z) ⊴_M COARSE_M(Ξ_k u).
- Tameness gives COARSE_M(Ξ_{k+1} z) ⊴_M COARSE_M(Ξ_{k+1} u).
- Ξ_{k+1}(z) ▷ Ξ_{k+1}(u) and (C1) give ⊵_M. By (C3) the coarse values are equal, so the level of (y, z) at k+1 is ≤ M. □
- (MONO with L = M_k is box 6's Step 2, PROVED by L-SI succ. 2, docs/si/N5-C-box5.md §6.2.)

**NOINF.** If λ_{k+1} = λ_k and y switches to z at k → k+1, then λ_k(z) = λ_k(σ_k y), i.e. the gate level is < ∞.
Proof. Suppose λ_k(z) ≠ λ_k(σ_k y). Note λ_{k+1}(z) = λ_k(z).
- Case y = λ_{k+1}(y). Then y = λ_k(y), so y is a cycle node at k.
  - (P1) on (y, σ_k y) at k gives λ_k(σ_k y) = y.
  - (P1) on (y, z) at k+1 gives λ_k(z) = λ_{k+1}(z) = y. Contradiction.
- Case y ≠ λ_{k+1}(y). (P1) on (y, z) at k+1 gives λ_{k+1}(y) = λ_k(z).
  - If y = λ_k(y), then λ_{k+1}(y) = y, against the case.
  - Otherwise (P1) at k gives λ_k(y) = λ_k(σ_k y) ≠ λ_k(z) = λ_{k+1}(y), so λ changes. Contradiction. □
- Consequence. At an S4c fallback with λ_{k+1} = λ_k, every vertex with a gate edge switches (§0), so M_k < ∞.

## 4. Theorem FB (PROVED, L-SI succ. 3)
Fix a phase and its transitions k → k+1.
- A TAME RUN is a maximal run of consecutive tame transitions of the phase. A BLOCK is a maximal sub-run with M_k constant.
- For a block of level M and an Even y, put β_k(y) := COARSE_{M−1}(Ξ_k(σ_k y)). For M = −1, COARSE_{−2} means the full value.
- n_E := #Even vertices. J := #non-tame transitions of the phase.
**Theorem FB.** The phase has at most n_E(2n − 1)(J + 1) + J S4c fallback transitions.
Proof.
- (1) Inside a block, for every Even y, β(y) is ⊴_{M−1}-non-decreasing and COARSE_M(Ξ(σ y)) is constant. Take a block transition
  i → i+1.
  - σ_{i+1}(y) is σ_i(y) or a gate target at i (R15 (d)). So Ξ_i(σ_{i+1} y) ⊵ Ξ_i(σ_i y), with level ≤ M.
  - Ξ_{i+1}(σ_{i+1} y) ⊵ Ξ_i(σ_{i+1} y) (R15 (a)), with level ≤ M (tame).
  - Conclude with (C1) and (C2).
- (2) At a fallback i of a block of level M, some y has β_{i+1}(y) ▷ β_i(y).
  - The fallback is Even's (τ unchanged in a phase; R21 (c) FBL-N (i)), so Iσ_i ≠ ∅ and M ≠ ⊥. M < ∞ by NOINF.
  - Pick y with a gate edge (y, z) of level M. S4c sets σ_{i+1}(y) = z*, the best gate target by (key, index). So Ξ_i(z*) ⊵ Ξ_i(z).
  - The level of (y, z*) is M. It is ≤ M by the definition of M. For M ≥ 0, suppose it is < M:
    - then COARSE_{M−1}(Ξ_i z*) = COARSE_{M−1}(Ξ_i σ_i y);
    - but COARSE_{M−1}(Ξ_i z) ▷ COARSE_{M−1}(Ξ_i σ_i y) (C1, C2: lev = M and strict);
    - so Ξ_i(z*) ◁ Ξ_i(z) by (C1). Contradiction.
    For M = −1 the level is −1, because z* ▷ σ_i y and both have level ≤ −1.
  - Hence β_i(y) ◁_{M−1} COARSE_{M−1}(Ξ_i z*) ⊴_{M−1} COARSE_{M−1}(Ξ_{i+1} z*) = β_{i+1}(y), by R15 (a) and (C1).
- (3) Counting inside a block, using (1):
  - M ≥ 0: β(y) ∈ {COARSE_M-value} × {rank-M vertex in or out}, so it has ≤ 2 values and strictly increases at most once;
  - M = −1: β(y) differs only in its length, which lies in {0, …, n − 1}, so it strictly increases at most n − 1 times.
  - By (2) each fallback of the block uses up a strict increase. So a block has ≤ n_E fallbacks (M ≥ 0) or ≤ n_E(n − 1)
    (M = −1).
- (4) By MONO, M is non-increasing along a tame run, so the run has at most one block per value of {∞, n − 1, …, 0, −1, ⊥}.
  - Blocks of value ∞ or ⊥ have no fallback (as in (2)).
  - So a tame run has ≤ n·n_E + (n − 1)n_E = n_E(2n − 1) fallbacks.
  - The phase has ≤ J + 1 tame runs, plus J non-tame transitions. □
**Corollary (PROVED; from FB and R23 (g)).** Inside a phase:
- #W-lowering transitions ≤ n_E(2n − 1)(J + 1) + J;
- the number (C) of '+−' reversals of R whose reversing transition is a fallback (R23 honest limits (ii)) is at most that too.

## 5. Non-tame transitions on 𝒞^1O (PROVED, L-SI succ. 3)
Inside a phase on 𝒞^1O, let k → k+1 be non-tame, and put a := σ̄_k(o), b := σ̄_{k+1}(o).
- **J1.** b ≠ a and lev(Ξ_k a, Ξ_k b) > M_k.
  - Proof: every Odd u ≠ o has one successor, so σ̄_{k+1}(u) = σ̄_k(u).
  - If J1 failed, TAME's hypothesis would hold (λ_{k+1} = λ_k in a phase). □
- **OFF.** At every in-phase transition (tame or not), if v ∉ R̄_{k+1} then COARSE_{M_k}(Ξ_{k+1} v) = COARSE_{M_k}(Ξ_k v).
  - Proof: v's H_{k+1}-play avoids o. Along it, (E) holds:
    - Even vertices by R15 (d);
    - Odd vertices other than o are forced.
  - Its cycle avoids o, and the cycle's top t has λ_k(t) = λ_{k+1}(t) = t.
  - Apply (T) with H′ := H_{k+1}; (T) only uses the play from v. If M_k ∈ {∞, ⊥} the claim is trivial, as in TAME. □
- **CAP.** Every exit e ∈ succ(o) with lev(Ξ_k a, Ξ_k e) ≤ M_k lies in R̄_{k+1}.
  - Proof: b minimises Ξ_{k+1} over succ(o) (VJ00 p. 14), so Ξ_{k+1}(e) ⊵ Ξ_{k+1}(b) ⊵ Ξ_k(b) (R15 (a)).
  - By J1 and the minimality of a, COARSE_M(Ξ_k b) ▷_M COARSE_M(Ξ_k a) = COARSE_M(Ξ_k e).
  - So COARSE_M(Ξ(e)) changes, and OFF gives e ∈ R̄_{k+1}. □
- Remark (PROVED, from §2 (a)): a non-tame transition violates (NC) for (σ_{k+1}, σ̄_k). On 𝒞^1O inside a phase this means a new cycle
  through o, i.e. a is captured (a ∈ R̄_{k+1} also follows from CAP). So non-tame transitions are INRs, but most INRs are tame (§7).

## 6. Refuted (JUMP-EQ); status of A
**(JUMP-EQ) is FALSE (DATA, re-verified instance).**
- The statement (CONJECTURE of L-SI succ. 2, docs/si/N5-C-box5.md §6.2): inside a phase with w constant, if an INR at k → k+1 raises
  θ at a level above the level L of the most recent carry, then θ_{k+1} = w.
  - Here a carry is a W-lowering transition, and L := max over the active leavers y of lev(Ξ_k y, Ξ_{k+1} y).
  - θ := Ξ(o), w := W(o) = the value of o under (σ, τ).
- Instance: experiments/red/xing/instances/x31_rx32.pg (L-RED), sha1 4fe9ec0e. One Odd choice vertex, o = 0 (asserted).
  - experiments/si/xing/reverify.sh: n5.py 55 iterations / 3 fallbacks; zielonka (Oink zlk) OK, strategies verified.
- The case: transition 53 → 54, w constant since the last carry, whose level is L = 24.
  - σ̄(o): 24 → 31 at 53 → 54. This is an INR: (NC) fails.
  - θ rises at level 25 > L. State 54 has (h), and θ_54 ≠ w_54.
  - Keys (reward, signed path weight, ±length): θ_53 = (36, −2146959360, −16), θ_54 = (36, −2113929216, −4),
    w = (36, −1040187392, −4).
  - At 54 → 55, σ̄(o) → 9 = τ(o) and θ_55 = w.
- Script: experiments/si/coarse/jumpeq.py (the statement exactly as above). Over the named set it finds 10 hypothesis cases, 9 with
  θ_{k+1} = w (log §7).
- Theorem FB bounds fallbacks without (JUMP-EQ).
**A ("a carry of level L changes Ξ only at levels ≤ L").**
- PROVED: at a tame carry every Ξ(v) changes only at levels ≤ M_k (definition of tame), and L ≤ M_k.
- DATA: L = M_k at all 201 in-phase evicting fallbacks of the named set (jump.py).
- OPEN: L ≥ M_k in general. A leaver tail with a level-M gate edge, not a cycle node and of rank ≠ M, changes exactly at level M (§4 (2)
  with (P2), (C4)). Not shown: that some level-M gate edge at an evicting fallback has a leaver tail.

## 7. Data (DATA, not proof)
Produced by experiments/si/coarse/run_all.sh. Logs are in experiments/si/coarse/logs/, in this packet's commit.
- Every script re-runs N5 with its own loop and asserts (iterations, fallbacks) = experiments/new/n5.py run().
- NAMED SET: experiments/si/coarse/named.txt, 53 files, each asserted one-Odd-choice:
  - the 30 named in-class instances of P-N5-Z fixes §1;
  - experiments/si/xing/instances/*.pg (12: zcl_*, ccl_*, nofe_cyc_n8);
  - L-RED's x32_*, u1t_*, obr_* (11).
- RANDOM: general games (mono.py / fbcount.py --random; n 4-14). They test §2-§4, which are general-game statements.
- RANDOM 𝒞^1O: experiments/new/box25/common.py rand_c1o (read-only), random starts (fbcount.py --c1o).

| check | where | instances / transitions | violations |
| --- | --- | --- | --- |
| COARSE-SI (a) at NC transitions; converse at NC failures (L < ∞) | mono.py | named 2,011 tr (1,606 NC); random 2 × 1,500 games, 3,379 tr | 0; 0 |
| MONO at NC transitions | mono.py | as above | 0 (M rose 31 / 110 times, all at NC failures) |
| MONO at tame transitions (phases) | tame.py | named 1,830 in-phase tr | 0 |
| FB (i) β monotone, (ii) strict rise at each fallback, (iii) M < ∞, (iv) per-block bound | fbcount.py | named 213 phases, 207 in-phase fallbacks; random 2 × 1,500; random 𝒞^1O 4,285 games | 0 |
| J1 | jump.py | named, 23 non-tame tr | 0 |
| OFF | jump.py | named, 40,704 vertex checks | 0 |
| CAP | jump.py | named, 159 exit checks | 0 |
| L = M_k at evicting fallbacks | jump.py | named, 201 | 0 exceptions |

- Sizes: max fallbacks in one tame block: 25 (ccl_w48_n48, n 48). Max J per phase: 3. NC failures (INRs) in phases: 323. Non-tame: 23.
- After the box, the lane's J-climbs (fitness: max J per phase) reached J 9-13 at n 32-48. Those games are NOT in this packet's data.
  On the four bests, the jumps are runs of consecutive exit jumps with no fallback between them (≤ |succ(o)|) or jumps at states where
  H2 fails. These are open lane work (N5-C-box7.md §9) and not part of the claims here.
