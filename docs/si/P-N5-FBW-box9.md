# Referee packet P-N5-FBW: fallback gates and the Ξ/W gap; fallback levels along a whole scope run; the per-level count (box 9)
L-SI successor 4 (Opus 5.5, D18/L40). Written 2026-10-25 05:45Z (date -u), at the Lead's request (05:28Z). Frozen at its commit:
corrections go in a fixes file, never here.
- Self-contained: definitions, statements, full proofs, the location of every dependency, the data and the scripts that produce it.
- Source text: docs/si/N5-C-box9.md §2, §3 (lane write-up, l-si 2d097630). Where they differ, this packet governs.
- Status: L-SI successor 4's proofs, unrefereed. Labels: PROVED (L-SI succ. 4), CONJECTURE, OPEN, DATA.
  - §1 (Lemma FBW) holds on EVERY game.
  - §2-§6 are on 𝒞^1O: exactly one Odd vertex o with out-degree > 1; every script asserts it.
- These are lemmas about the candidate N5. They are not a running-time bound, not a TARGET.md claim, and not a step-4 pass.
  G-N5-TIME stays OPEN.
- Statements:
  - §1 Lemma FBW; §2 Corollary FBW-S and Theorem CLS2;
  - §3 Lemma FLAT-ALL; §4 Lemma STRETCH; §5 Theorem PL and Corollary PL-S.
- §6 is NOT TO SIGN (conjectures and open items). §7: data.

## 0. Objects and dependencies (only landed RESULTS)
- N5 and its steps S4a (arena step), S4b, S4c (fallback): as specified in docs/new/N5-ssi-global.md (SPEC S1-S5; RESULTS R15).
  - An S4c fallback fires exactly when S4a returns σ_k and S4b returns τ_k. Even switches if Iσ_k ≠ ∅, otherwise Odd.
  - Code: experiments/new/n5.py; experiments/si/coarse/mono.py states(), which asserts equality with n5.run.
- Ξ_k, H_k, gates Iσ_k (Ξ_k-improving Even edges), the gate level lev(Ξ_k σ_k y, Ξ_k z), M_k := the max gate level, lev, COARSE_L,
  (C1)-(C4): as in RESULTS R25 (P-N5-FB §0-§1). ⊥ < −1 < 0 < … < n − 1 < ∞ are the level values.
- (C5), (C6), (C7), Fact R, Lemma CLU: RESULTS R29 (a). Lemma TRANSFER: R29 (b). Lemma CN: R29 (d). NL: R29 (e). CLS1 and its
  proof's (A_j) chain: R29 (f).
- W_k := V_{σ_k,τ_k}, the play valuation of the (σ_k, τ_k)-play, with the engine's convention (experiments/si/si.py l.68-75, l.78ff.):
  - key(c, P, d) = (rew(c), weight(P), d if c is odd else −d);
  - a cycle node c has value (c, ∅, 0);
  - a non-cycle-node v has V(v) = v ⊕ V(next v), where v ⊕ (c, P, d) := (c, P ∪ {v : rank v > rank c}, d + 1).
  - Rewards: rew(c) = +pp(c) for even c and −pp(c) for odd c, pp = 2·rank + parity, injective. Path weights are signed sums over
    distinct ranks, ordered by the top differing rank.
  - Ξ_k obeys the same (P2) on H_k (VJ00 BRICS RS-00-48 Lemma 5.2; ENG-1 of R25).
- Premise P-OPT (signed). The arena A(σ_k) is the set of Even strategies choosing σ_k(v) or a gate target at each Even v; with τ_k
  fixed it is a one-player game.
  - R17 (a) (F1): the optimum of a one-player game dominates every strategy of that game pointwise.
  - R18 (d) Lemma S (c): S4a's Even step computes that optimum over A(σ_k) against τ_k.
  - At an S4c fallback that computation returned σ_k. Hence V_{σ′,τ_k} ⊴ W_k pointwise for every σ′ ∈ A(σ_k).
  - G-1OA-6 (R18) does not apply. It says that the strategy S4c then installs is not the arena optimum; P-OPT is about the state k
    itself, where the optimum is σ_k.
- 𝒞^1O objects (R19-R23, R29 §0):
  - θ_k := Ξ_k(o), w_k := W_k(o);
  - R̄_k := {o} ∪ {v : v's (σ_k, τ_k)-play reaches o}, R_k := R̄_k ∖ {o}, F_k := V ∖ R̄_k;
  - H1 (o on no honest cycle), H2 (o on no W-cycle), H3 (same cycle node for θ and w), (h) := H1 ∧ H2 ∧ H3;
  - r_k := lev(θ_k, w_k). THR: (h) and θ ◁ w (r ≥ 0: u* ≠ none; r = −1: u* = none). EQ: (h) and θ = w (r = ⊥).
  - PHASE: λ_Ξ and τ constant. SCOPE RUN S: a maximal run of in-phase transitions with (h) at k, H2 at k+1 and w_{k+1} = w_k
    (R29 §0). Inside a phase τ is constant, so every in-scope fallback is an Even fallback.
- Other signed results used:
  - R15 (a) Ξ_k ⊴ Ξ_{k+1}; R15 (d) σ_{k+1}(v) ∈ {σ_k(v)} ∪ Iσ_k(v).
  - R18 (d) Lemma S (a): Ξ_k(v) = min over Odd strategies τ′ of V_{σ_k,τ′}(v), pointwise.
  - R19 (a) Lemma G: off R̄, Ξ = W; under (h), on R, Ξ = π ⊕ θ and W = π ⊕ w with π the route to o. R29 (a) CLU's proof shows that
    (C7) applies to π.
  - R20 (b) Lemma FBL (u* ≠ none, strong form): at such a fallback state there is no F→R̄ and no R→R̄ gate edge; the fallback switches
    only R → F edges and flat cycle-node switches.
  - R25 (b) TAME, (c) MONO, (d) Theorem FB and its step (2) (each tail switches to its best target, whose level is the max over its
    gates), (e) OFF (v ∉ R̄_{k+1} ⇒ COARSE_{M_k}(Ξ_{k+1} v) = COARSE_{M_k}(Ξ_k v)) and CAP-1.
  - R28 (a) Lemma U-loc.
  - R30 (a) Lemma OR, (b) TC-SPLIT, (h) ABS-L (relevant changes, E_k, O_k, ε-transition O_k > E_k, absorption: as in R30).
- b_k(y) := Ξ_k(σ_k y) for Even y. It is ⊴-non-decreasing in k: σ moves along gates (R15 (d)) and Ξ is monotone (R15 (a)).

## 1. Lemma FBW (PROVED; every game)
Let k be an S4c fallback at which Even switches. For a gate (y, z) at k put
- u := σ_k(y), ℓ := lev(Ξ_k u, Ξ_k z), δ := max(lev(Ξ_k u, W_k u), lev(Ξ_k z, W_k z)).
Then:
- (a) ℓ ≤ max(δ, −1);
- (b) if ℓ = −1 > δ, then y is its own W_k-cycle node and its own Ξ_k-cycle node.
Proof. Suppose ℓ > δ; then δ < ∞.
- Step 1: the gate is W-improving at level ℓ.
  - COARSE_δ(Ξ x) = COARSE_δ(W x) for x ∈ {u, z} by (C2); for δ = ⊥ the values are equal.
  - Ξ z ▷ Ξ u with level ℓ > δ gives COARSE_δ(Ξ z) ▷_δ COARSE_δ(Ξ u), strictly ((C1), (C2)).
  - Hence COARSE_δ(W z) ▷_δ COARSE_δ(W u), so W z ▷ W u ((C1), (C3)). For L′ ≥ δ the COARSE_{L′} values of Ξ and W agree at u and
    z, so lev(W u, W z) = ℓ.
- Step 2: σ′ := σ_k[y ↦ z] ∈ A(σ_k) strictly improves y, outside one case. Write V := W_k and V′ := V_{σ′,τ_k}. All plays are lassos.
  Let c be the cycle node of V(y).
  - (a) z's σ_k-play avoids y. It is also z's σ′-play, so V′(y) = y ⊕ V(z).
    - If y is a cycle node: V(y) = (y, ∅, 0), and V(u) has cycle node y. V(z) has a different cycle node c_z (its play avoids y).
      So V z ▷ V u forces rew(c_z) > rew(y), and V′(y) ▷ V(y).
    - Otherwise V(y) = y ⊕ V(u). y lies in neither P(V z) (z's play avoids y) nor P(V u) (if u's play visits y, then y is on its
      cycle, of rank < rank c). So y ⊕ · keeps the strict order: V′(y) ▷ V(y).
  - (b1) z's play visits y, and y is not on its own cycle. Let q_1 … q_m be z's play before y; none of them is on y's cycle.
    - V(z) = q_1 ⊕ … ⊕ q_m ⊕ y ⊕ V(u), all with cycle node c.
    - The new play from y is the cycle C = (y, q_1, …, q_m), so V′(y) = (t, ∅, ·) with t := the top of C.
    - Put D′ := {v ∈ C : rank v > rank c}. Then P(V z) = P(V u) ⊔ D′.
    - If D′ ≠ ∅: V z ▷ V u means D′'s top is even. That top is t, of rank > rank c, so rew(t) = pp(t) > |rew(c)|.
    - If D′ = ∅: the improvement is length-only (longer), so c is odd. Then rank t < rank c gives rew(t) > −pp(c) = rew(c).
    - In both cases V′(y) ▷ V(y).
  - (b2) y lies on its own cycle C_y with top c (possibly y = c). Then u ∈ C_y and P(V u) = ∅.
    - z's play p_0 = z, …, p_a = e first meets C_y at e and then runs along C_y to y. P(V z) = {p_i : i < a, rank p_i > rank c}.
    - The new cycle is C = (y, p_0, …, e, then C_y from e to y).
    - If P(V z) ≠ ∅: its top is even, and it is the top t of C (all other vertices of C have rank < rank t). As in (b1),
      V′(y) ▷ V(y).
    - If P(V z) = ∅ and c ∉ C: then e lies strictly after c and before y on C_y, so dist(e, c) > dist(u, c) and V z is longer than
      V u. The improvement makes c odd, rank t < rank c, and V′(y) ▷ V(y).
    - If P(V z) = ∅, c ∈ C and y ≠ c: V′(y) = (c, ∅, 1 + a + dist_{C_y}(e, c)) and V(y) = (c, ∅, 1 + dist(u, c)). V(z) has length
      a + dist(e, c) and V(u) has length dist(u, c). The parity rule that makes V z ▷ V u gives V′(y) ▷ V(y).
    - If P(V z) = ∅ and y = c: V′(y) = (c, ∅, 0) = V(y). This is the only case without a strict improvement. Here y is its own
      cycle node and lev(V u, V z) = −1.
- Step 3. Outside that case, V′(y) ▷ W_k(y) with σ′ ∈ A(σ_k), against P-OPT. So ℓ > δ forces the case: ℓ = lev(W u, W z) = −1
  (Step 1), and y is its own W-cycle node. With δ < −1, Ξ u = W u, so y is also its own Ξ-cycle node. □

## 2. Corollary FBW-S and Theorem CLS2 (PROVED; 𝒞^1O)
**Corollary FBW-S.** At an in-phase S4c fallback k with (h) at k, every gate has level ≤ max(r_k, −1).
- So M_k ≤ −1 at EQ states and at THR states with u* = none.
- At EQ every gate is a length-only switch at a cycle node.
- Proof: k is an Even fallback (τ is constant in a phase). δ ≤ max_v lev(Ξ_k v, W_k v).
  - Off R̄_k, Ξ = W (Lemma G).
  - On R_k, lev(π_v ⊕ θ_k, π_v ⊕ w_k) = r_k by (C7) (as in CLU's proof, R29 (a)). At o the level is r_k.
  - Apply FBW. □
**Theorem CLS2.** Along a scope run S, the fallback levels form a non-increasing sequence, and M_k ≤ max(r_k, −1) at each of them.
- Proof: by Fact R, the fallbacks with r ≥ 0 (THR, u* ≠ none) come first, and CLS1 orders them.
  - Every later fallback has r ≤ −1, so M = −1 by FBW-S. Gate levels are ≥ −1, since gates are strict.
  - −1 is ≤ every earlier level. □
- Consequence: R29 §7's OPEN item (H-EQ) is closed, and its (H-KIND) is not needed.

## 3. Lemma FLAT-ALL (PROVED; 𝒞^1O)
Let k be a fallback of a scope run with M := M_k ≥ 0 and (h) at k and k+1. Then:
- (i) F_k ⊆ F_{k+1}, and every v ∈ R̄_{k+1} lies in R̄_k with the same route to o;
- (ii) COARSE_M(θ_{k+1}) = COARSE_M(θ_k);
- (iii) COARSE_M(Ξ_{k+1} v) = COARSE_M(Ξ_k v) for every vertex v;
- (iv) M_{k+1} ≤ M.
Proof.
- By FBW-S, r_k ≥ M ≥ 0, so k is THR with u* ≠ none. By FBL the switched edges are R → F edges and flat cycle-node switches.
- (i)
  - A switched cycle node y′ keeps λ(y′) = y′ (phase), so its new play is a cycle through y′. That cycle does not contain o:
    otherwise it would be o's W-cycle at k+1, against H2.
  - An F_k vertex's play contains only F_k vertices. The switches among them are cycle-node switches (cycles without o), so the
    play stays off o.
  - A play that reaches o at k+1 meets no switched vertex: an R-tail continues into F_k, and a cycle node stays on its cycle. So
    the play is the same as at k.
- (ii) If λ(o) = o, θ is constant. Otherwise let x0 := σ̄_k(o). x0 ∈ F_k (H1), and θ_k = o ⊕ Ξ_k(x0) by (P2).
  - By (i), x0 ∈ F_{k+1}, so its H_{k+1}-play avoids o.
  - Lemma S (a), with Odd choosing x0 at o, gives θ_{k+1} ⊴ o ⊕ Ξ_{k+1}(x0). R15 (a) gives θ_k ⊴ θ_{k+1}.
  - OFF gives COARSE_M(Ξ_{k+1} x0) = COARSE_M(Ξ_k x0). (C7) carries this through o ⊕, since o lies on neither path.
  - The sandwich and (C1), (C3) give the claim.
- (iii) Off R̄_{k+1}, use OFF. On R̄_{k+1}, use Lemma G (b) at k and k+1 with the same route ((i)), (C7) and (ii).
- (iv) TRANSFER with (iii): a gate at k+1 of level > M would be a gate at k of level > M_k. □

## 4. Lemma STRETCH (PROVED; 𝒞^1O)
Let M ≥ 0. Let [s, e] be consecutive states of a scope run S such that, for every v, COARSE_M(Ξ_t v) is the same for all t ∈ [s, e].
Then each Even y is a LEVEL-M TAIL (a tail with max gate level M = M_k) at most once among the fallbacks k of S with s ≤ k < e.
Proof.
- (1) COARSE_M(b_t(y)) is constant on [s, e].
  - Suppose y switches at t along a gate of level > M. If y is not a cycle node, COARSE_M(Ξ(y)) changes at t → t+1 ((P2), (C7)),
    which the hypothesis excludes. If y is a cycle node, the level is −1 (CN).
  - A switch along a gate of level ≤ M lands on a target with the same COARSE_M (and that value is constant in t).
- (2) Fix a COARSE_M value κ with cycle node c, and let v_M be the vertex of rank M. Only rank M > rank c matters: otherwise no level-M
  difference exists. For values a with COARSE_M(a) = κ, put β(a) := good if v_M ∈ P(a) and v_M is even, or v_M ∉ P(a) and v_M is
  odd; else bad. Among such values, ⊴ is decided by β first ((C1) at level M − 1).
- (3) Let y be a level-M tail at k. Then b_k(y) is bad, and its best target z (R25 FB step (2)) has Ξ_k(z) good.
  - b_{k+1}(y) = Ξ_{k+1}(z) ⊵ Ξ_k(z), with the same COARSE_M. So it is good.
  - b is non-decreasing and its COARSE_M is constant on [k+1, e], so b stays good there.
  - A level-M gate at y needs b bad. So y is not a level-M tail at any later fallback k′ < e. □

## 5. Theorem PL and Corollary PL-S (PROVED; 𝒞^1O)
Setting. Let S be a scope run and M ≥ 0. The BLOCK is the set of fallbacks of S at level M, written f_1 < … < f_N. They are consecutive
among the fallbacks of S (CLS2). An interval (f_i, f_{i+1}) is DIRTY if COARSE_M(Ξ) changes at some vertex at a transition inside it.
**Theorem PL.**
- (a) N ≤ n_E·(1 + D_M), where D_M := #dirty intervals.
- (b) Let j be the first transition of a dirty interval at which COARSE_M(Ξ) changes. Then:
  - j is an S4a step with O_j > M ≥ E_j (an ε-transition);
  - lev(θ_j, θ_{j+1}) = O_j > M;
  - j is an absorption: σ̄_j(o) = x0 ∈ F_j ∩ R_{j+1}.
- (c) If r_t > M for all t ∈ [f_1, f_N], then D_M ≤ (d_o − 1) + REL_M, with d_o := |succ(o)| and REL_M := #exits of o leaving R at
  f_1, …, f_{N−1}. Hence N ≤ n_E·(d_o + REL_M).
Proof.
- (a) For i < N, S continues after f_i, so (h) holds at f_i + 1, and FLAT-ALL (iii) applies at f_i. So no fallback transition of the
  block changes COARSE_M(Ξ).
  - [f_1, f_N] therefore splits into at most 1 + D_M runs of constant COARSE_M(Ξ), cut only inside dirty intervals.
  - Every fallback of the block has a level-M tail (R25 FB step (2)). By STRETCH each Even vertex is one at most once per run.
- (b) M_{f_i+1} ≤ M by FLAT-ALL (iv). While COARSE_M(Ξ) is unchanged, M_t ≤ M persists by TRANSFER. So M_j ≤ M.
  - Every relevant Even change at j has level ≤ M_j ≤ M (R15 (d)), and the interval contains no fallback, so j is an S4a step.
  - U-loc with L = M freezes COARSE_M at every vertex whose H_{j+1}-path before its cycle node has no relevant change above M. A
    change therefore needs the relevant σ̄(o) change with O_j > M ≥ E_j.
  - Lemma OR (c) / TC-SPLIT give lev(θ_j, θ_{j+1}) = O_j. Lemma OR (a)-(b), with H1 at j (scope), give the absorption.
- (c) Under r > M, CLS1's proof gives (A_t) for L = M at every state of each interval (R29 (f)). NL (ii) gives no leave at the S4a
  steps of an interval.
  - By ABS-L, the absorbed exits of an interval are distinct and stay in R until the interval's end.
  - Let N_x := #exits of o in R. Each absorption raises N_x by 1. N_x falls only at the block's fallbacks, by REL_M in total.
    Under H1, σ̄(o) ∈ F, so N_x ≤ d_o − 1.
  - Each dirty interval contains its own first absorption (b). So D_M ≤ (d_o − 1) + REL_M. □
**Corollary PL-S.** If every block of S has r > M on it, then the fallbacks of S at levels ≥ 0 number at most
n_E·Σ_M (d_o + REL_M) ≤ n_E·(n·d_o + REL(S)), with REL(S) := #exit releases at fallbacks of S.
- Proof: the blocks are disjoint and there are at most n levels. □
- Compare R25 (d) Theorem FB: per phase ≤ n_E(2n − 1)(J + 1) + J, where levels reset at every non-tame transition. Here, by CLS2,
  levels never reset along a scope run.

## 6. NOT TO SIGN: conjectures, data findings, open items
- CONJECTURE NJB: no COARSE_M change (equivalently, by PL (b), no absorption above M) happens strictly inside a level-M block.
  - NJB gives D_M = 0, so ≤ n_E fallbacks per level and ≤ n·n_E fallbacks of level ≥ 0 per scope run (the second half of R29's
    (CL-S)).
- CONJECTURE NJ-INT (implies NJB): between consecutive fallbacks k0 < k of a scope run with r > L := M_{k0} on (k0, k], θ does not
  change above L. ABS-L is vacuous in all data (REFEREE-2, P-N5-SN fixes §4: 583 / 0).
- Lemma ABS-O (box 9 §3b; lane, not offered here) is a true but vacuous route to NJB: every block has M ≥ rank o when rank o > rank c.
- OPEN: blocks on which r drops to M (PL (c) does not apply; PL (a)-(b) do); fallbacks at level −1 (by FBW-S, in scope these are
  EQ / u* = none fallbacks or THR fallbacks of level −1); REL(S) itself.
- DATA FINDING: in-scope THR fallbacks with u* = none: 0 in every sample (by FBW-S they would have M ≤ −1).

## 7. Data (DATA, not proof; scripts in experiments/si/coarse/, logs in experiments/si/coarse/logs/box9/, in this packet's commit)
- Sets: NAMED = experiments/si/coarse/named.txt (53) + experiments/si/coarse/instances/*.pg (12 pinned bests); LIB = the 234 files of
  experiments/new/box33/lib.txt (first column); RANDOM = fbw.py --random 901 1500 4 14 and 902 4000 4 20 (general games). Every run is
  asserted equal to n5.py run().
- fbw.py (§1-§2): FBW (a), (b), Step 1 (W-improving at the same level), P-OPT (arena optimum re-computed = σ_k), in-scope consequences.
  - Even fallbacks / gates: NAMED 272 / 837, LIB 694 / 2,384, RANDOM 141 / 156. 0 failures.
  - In-scope fallbacks: NAMED 252 THR (u* ≠ none) + 4 EQ; LIB 526 + 8 EQ; RANDOM 5 EQ; 0 THR with u* = none.
- reltrace.py (§3-§5; NAMED / LIB): 75 / 169 blocks, 252 / 526 block fallbacks, 0 failures in each row.
  - FB-FLAT (FLAT-ALL (iii) in b-form): 252 / 526.
  - Lemma PL (a) bound: checked on every block.
  - Inside blocks: COARSE_M changes (B) 0, gates above M 0, θ-changes above M 0, tail repeats 0 (max_rep 1).
  - NJ-INT intervals: 185 / 377, 0 θ-changes above L.
  - Releases of exits at block fallbacks: 371 / 499.
  - Blocks with r > M throughout: 69 / 156.
- Climbs (jclimb.py, 30 min each, seeds 9101-9104): JMODE=HEQ from x32_rand64 and obr_n32; JMODE=REP from jcl_x32_nest40 and
  rel_j7_n48. Results:
  - 0 violations of any checked statement. HEQ reached 1 in-scope EQ fallback and 0 with u* = none. REP reached 0 tail repeats and 0
    θ-changes above M inside blocks.
  - Bests pinned in experiments/si/coarse/instances/box9/. Each re-verified with xing/reverify.sh (n5.py; Oink zlk OK, strategies
    verified):
    - cl9_heq_b (n 32, sha1 7535a99c, 29 iterations / 27 fallbacks);
    - cl9_rep_a (n 40, 9d31fb39, 40 / 33);
    - cl9_rep_b (n 48, 8efbbc9e, 45 / 37; one level block of 37 fallbacks, each with fresh tails).
  - On these three: fbw 97 fallbacks / 99 gates, 0 failures; reltrace 3 blocks, B = 0 (logs/box9/*_climb.txt).
