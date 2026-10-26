# N5 on 𝒞^2O (two Odd choice vertices): in-phase fallbacks per phase are O(n³), with two terminals per honest class (lane note, box 16)
L-SI successor 11 (Opus 5.5; D15, D18, L37, L40), session_01FchPxfEZ9Fo56WrCZTvnXS. Lead's question of 03:38Z (Lead's stamp): "on 𝒞^2O,
is ρ per phase polynomial?" Written 2026-10-26 03:4xZ onward (date -u; the stamp is the commit). LANE NOTE: not a packet, not frozen.
- Labels (D18 / L40): PROVED (L-SI 11, unrefereed) / CONJECTURE / OPEN / DATA / READING. D1: wrong until checked.
- Scope: the candidate N5 (SPEC S1-S5, docs/new/N5-ssi-global.md) inside one phase. Nothing here is a running-time bound for N5 on any
  class, a TARGET.md claim, or a gauntlet pass. G-N5-TIME stays OPEN.
- Short answer.
  - What FB-RED needs is N_late, the number of Q-runs that hold a LATE fallback. This is not ρ.
  - N_late is polynomial in every phase whose honest classes each hold at most two Odd choice vertices other than the class's cycle node.
    This covers every phase of every run on 𝒞^2O. The bound is N_late ≤ 12n² (Theorem FB-2T).
  - With FB-RED's late form, every phase on 𝒞^2O has f ≤ 1 + (n − 1)(1 + 12n²) = O(n³) in-phase fallbacks (Corollary FB-2O).
  - ρ itself counts every Ξ(Q)-change, including those inside fallback-free stretches. It is NOT bounded here: OPEN, and part of the
    T-per-phase question (§5).
- Premises.
  - P-N5-FBRED (docs/new/P-N5-FBRED-box44.md, L-NEW 23): REFEREE-2 signed; REFEREE §C pending (Lead 03:38Z). Used: §0 setting, §1.1
    facts, κ-FB-ROUND, κ-HAT-FREEZE_D (a), the proof of κ-PFZ_D, Theorem FB-RED late form (§3.2).
  - So this note is CONDITIONAL on FBRED landing.
  - Landed: R15 (a) (via (M2κ)); R54 (e) Φ-kO (phases).

## 0. Setting and notation (FBRED §0, every game)
- Phase: a maximal run with (λ, τ) constant. λ is constant on it, so the honest classes U_c := λ^{-1}(c) (c ∈ C, the honest cycle
  nodes) are constant.
- Q: the Odd vertices of out-degree ≥ 2. For a class U_c, its TERMINALS are Q_c := (Q ∩ U_c) ∖ {c}. T := C ∪ Q.
- g_1 < g_2 < … are the in-phase (Even) fallbacks; g_j denotes the source state of the j-th one, as in FBRED / FBP. For a run Θ of
  states, f^Θ_j is the j-th fallback whose source state lies in Θ.
- κ_t(z) := (signed weight of P(Ξ_t z), s_c·ℓ(Ξ_t z)) for z ∈ U_c, and κwt_c(v) := (wt_c(v), s_c), with arithmetic sums (FBRED §0).
  κopt_c(z) := max κwt_c(p ∖ {c}) over simple paths p of G_c from z to c. κopt^q(z) := max κwt_c(p ∖ {q}) over simple paths p of G_c^q
  from z to q. The graphs G_c := U_c ∖ (Q ∖ {c}) (c a sink) and G_c^q := U_c ∖ (T ∖ {q}) (q a sink) are FBRED §0's. In both, every Odd
  vertex other than the sink is forced.
- Facts used, all FBRED §1.1 on every game:
  - (Aκ): z ∈ U_c ∖ {c} ⇒ next_t(z) ∈ U_c and κ_t(z) = κwt_c(z) + κ_t(next_t z).
  - (M2κ): κ is non-decreasing along a phase.
  - (INJ): Ξ_t(q) is determined by κ_t(q) on the phase.
  - (SP′): the prefix of an honest play from z ∈ U_c ∖ {c} up to its first vertex of T ∩ U_c is a simple path.
  - (YB): q ∈ U_c ∖ {c} on its own honest cycle has P(Ξ_t q) = ∅ and 1 ≤ ℓ ≤ |U_c| − 1.
- A q-RUN (q a terminal): a maximal run of states of the phase with Ξ(q) constant. A Q-RUN: the same with every q ∈ Q (FBRED §0).
  By (M2κ), a q-run is exactly a maximal run with κ(q) constant.
- DIRECT. A terminal q ∈ Q_c is direct at t if q lies on its own honest cycle at t, or if its honest play at t visits c before any
  other terminal of Q_c.
- Cyc_c := {(0, s_c·ℓ) : 1 ≤ ℓ ≤ |U_c| − 1}.
- A_q := {κwt_c(q) + κopt_c(y) : y ∈ succ(q) ∩ U_c ∖ Q, κopt_c(y) defined} ∪ {κwt_c(q) : c ∈ succ(q)} ∪ Cyc_c.
  Then |A_q| ≤ d_q + |U_c| − 1, where d_q := |succ(q) ∩ U_c|.

## 1. Lemma PFZ-q (PROVED, every game): κ-PFZ needs only its own terminal constant
Statement. Let q ∈ Q_c and let Θ be a q-run of a phase. For every j ≥ 0, every t ∈ Θ with t > f^Θ_j (every t ∈ Θ if j = 0), every
z ∈ U_c ∖ T and every simple path p of G_c^q from z to q with ≤ j edges: κ_t(z) ≥ κwt_c(p ∖ {q}) + κ_Θ(q), where κ_Θ(q) is κ(q) on Θ.
Proof. FBRED's κ-PFZ_D is stated for Q_c-runs; its proof (FBRED §1.2: "FBP §1 verbatim"; FBP §1 = docs/new/P-N5-FBPOLY-box41.md, κ-PFZ)
uses the constancy of exactly one value, κ(q) at the relaxing state. Written out, by induction on j:
- Base j = 0: no z ∈ U_c ∖ T is joined to q by a path with 0 edges, so there is nothing to prove.
- Step j − 1 → j: p = z·p′, with x the second vertex of p and p′ a simple path of G_c^q from x to q with ≤ j − 1 edges.
  - The vertex x is either q (then p′ has no edge) or lies in U_c ∖ T, since G_c^q has no other terminal.
  - z Odd: z ∉ Q (it is a non-sink vertex of G_c^q), so x is its forced successor, x = next_t(z). (Aκ) at t gives
    κ_t(z) = κwt_c(z) + κ_t(x). If x = q, κ_t(x) = κ_Θ(q). Otherwise the hypothesis at t (t > f^Θ_j > f^Θ_{j−1}) gives
    κ_t(x) ≥ κwt_c(p′ ∖ {q}) + κ_Θ(q).
  - z Even: k := f^Θ_j < t, with k ∈ Θ.
    - Bound at k: if x = q, κ_k(x) = κ_Θ(q), because k ∈ Θ. Otherwise the hypothesis at k (k ∈ Θ, k > f^Θ_{j−1}) gives
      κ_k(x) ≥ κwt_c(p′ ∖ {q}) + κ_Θ(q).
    - κ-FB-ROUND at k (z Even in U_c ∖ {c}, x ∈ U_c) gives κ_{k+1}(z) ≥ κwt_c(z) + κ_k(x).
    - (M2κ) from k + 1 to t gives κ_t(z) ≥ κ_{k+1}(z).
  The values of the other terminals are never used. □
DATA (§6): 2,298 checks in arithmetic κ, 0 violations. The mutation control (j + 2 edges) fails 11 times.

## 2. Lemma ROUTE-2 (PROVED, every game): of two terminals, one is direct
Statement. If Q_c = {q, q′} with q ≠ q′, then at every state t of the phase, q or q′ is direct.
Proof.
- Suppose q is not direct: q is not on its honest cycle, and its honest play visits q′ before c.
- The honest play is positional, so from its first visit of q′ on, q's play is q′'s honest play.
- If q′'s play visited q, then q's play would visit q a second time, and q would lie on the cycle of its own play. That is excluded.
  So q′'s play never visits q.
- q′'s play reaches c, the cycle node of its class, by (Aκ) and the lasso shape (SP′). So q′ is on its own honest cycle, or it visits
  c before q. In both cases q′ is direct. □

## 3. Lemma DIR and Lemma SAT-2 (PROVED, every game): late value sets
### Lemma DIR
Statement. Let t > g_{|U_c|−1} be a state of the phase, and let q ∈ Q_c be direct at t. Then κ_t(q) ∈ A_q.
Proof.
- If q is on its honest cycle, (YB) gives κ_t(q) ∈ Cyc_c.
- Otherwise put y := next_t(q) = σ̄_t(q). By (Aκ), y ∈ U_c and κ_t(q) = κwt_c(q) + κ_t(y). The honest play of y is the rest of q's play,
  and it visits c before any terminal; y ≠ q, because q is not on its cycle.
  - If y = c: κ_t(y) = (0, 0), and κ_t(q) = κwt_c(q).
  - If y ≠ c: y ∉ Q, so y is a vertex of G_c.
    - "≤": the prefix of y's play up to c is a simple path ((SP′); its first vertex of T ∩ U_c is c). Its vertices lie in U_c ∖ Q, its
      Even edges are σ_t's and its Odd vertices are forced. So it is a path of G_c, and (Aκ) along it gives κ_t(y) = κwt_c(prefix ∖ {c})
      ≤ κopt_c(y).
    - "≥": simple paths of G_c have ≤ |U_c| − 1 edges, so κ-HAT-FREEZE_D (a) at t > g_{|U_c|−1} gives κ_t(y) ≥ κopt_c(y).
    - So κ_t(q) = κwt_c(q) + κopt_c(y) ∈ A_q. □
- Note: FBRED's κ-HAT-FREEZE_D (c) is stated for plays that "avoid Q ∖ {c}". The proof above needs only the prefix up to c, because a
  terminal on c's cycle after c does not change the prefix.
### Lemma SAT-2
Statement. Let Q_c = {q, q′}, let Θ be a q-run, and let t ∈ Θ with t > g_{|U_c|−1} and t > f^Θ_{|U_c|−1}. Then
κ_t(q′) ∈ V_{q′}(κ_Θ(q)), where for a value α:
V_{q′}(α) := {κwt_c(q′) + β_y(α) : y ∈ succ(q′) ∩ U_c, y ≠ q′} ∪ Cyc_c, with
- β_q(α) := α and β_c(α) := (0, 0);
- for y ∉ T: β_y(α) := the larger of κopt_c(y) and κopt^q(y) + α, over those that are defined; y is omitted if neither is.
So |V_{q′}(α)| ≤ d_{q′} + |U_c| − 1.
Proof.
- If q′ is on its honest cycle: Cyc_c, by (YB).
- Otherwise y := next_t(q′) ∈ U_c and κ_t(q′) = κwt_c(q′) + κ_t(y) by (Aκ). y's honest play avoids q′.
  - y = q: κ_t(y) = κ_Θ(q).
  - y = c: κ_t(y) = (0, 0).
  - y ∉ T:
    - "≤": by (SP′), the prefix of y's play up to its first terminal e ∈ {q, c} (q′ is not visited) is a simple path in U_c ∖ T, with
      Even edges σ_t's and Odd vertices forced. If e = c, it is a path of G_c, and κ_t(y) = κwt_c(prefix ∖ {c}) ≤ κopt_c(y). If e = q,
      it is a path of G_c^q, and κ_t(y) = κwt_c(prefix ∖ {q}) + κ_t(q) ≤ κopt^q(y) + κ_Θ(q). Both use (Aκ) along the prefix.
    - "≥": κ-HAT-FREEZE_D (a) at t > g_{|U_c|−1} gives κ_t(y) ≥ κopt_c(y) when it is defined (paths of G_c have ≤ |U_c| − 1 edges).
      PFZ-q at t > f^Θ_{|U_c|−1} gives κ_t(y) ≥ κopt^q(y) + κ_Θ(q) when it is defined (paths of G_c^q have ≤ |U_c| − 1 edges).
    - κ_t(y) is at most the defined bound of its actual route, and at least every defined bound. So κ_t(y) = β_y(κ_Θ(q)). □

## 4. Theorem FB-2T and Corollary FB-2O (PROVED, every game; CONDITIONAL on P-N5-FBRED)
Hypothesis (2T) for a phase: every class has |Q_c| ≤ 2. On 𝒞^2O (|Q| = 2) every phase satisfies (2T); so does every phase on 𝒞^1O.
Statement (Theorem FB-2T). Let N_late be the number of Q-runs of the phase that hold a fallback g_j with j ≥ n (FBRED §3.2). In a phase
with (2T):
    N_late ≤ 1 + Σ_c (N_c − 1),
where the sum is over the classes with Q_c ≠ ∅, w_c := |U_c| − 1, and
- |Q_c| = 1, Q_c = {q}: N_c := |A_q| ≤ d_q + w_c;
- |Q_c| = 2, Q_c = {q, q′}: N_c := |A_q|·(w_c + max_α |V_{q′}(α)|) + |A_{q′}|·(w_c + max_α |V_q(α)|)
  ≤ 2(d + w_c)(d + 2w_c), with d := max(d_q, d_{q′}).
Proof.
1. Late fallbacks and tuples. Let i = 1, 2, … index the late fallbacks g_j (j ≥ n) of the phase, with source states k_1 < k_2 < ….
   Each k_i > g_{n−1} ≥ g_{|U_c|−1} for every class, since |U_c| ≤ n.
   - Let x_i be the tuple (κ_{k_i}(q))_{q ∈ Q}, ordered by class.
   - Two late fallbacks lie in the same Q-run iff x is equal at them: by (M2κ) every coordinate is non-decreasing, so equal values at
     k_i < k_{i′} force constancy in between. So N_late = the number of distinct x_i.
   - A coordinatewise non-decreasing sequence has (number of distinct terms) = 1 + (number of indices where it changes)
     ≤ 1 + Σ_c (indices where the class-c sub-tuple changes) = 1 + Σ_c (N′_c − 1), where N′_c := the number of distinct class-c
     sub-tuples. It remains to show N′_c ≤ N_c.
2. One terminal, Q_c = {q}. q is always direct (no other terminal). By DIR, κ_{k_i}(q) ∈ A_q, so N′_c ≤ |A_q|.
3. Two terminals, Q_c = {q, q′}. Put a_i := κ_{k_i}(q) and b_i := κ_{k_i}(q′).
   - By ROUTE-2, q or q′ is direct at k_i. By DIR, a_i ∈ A_q or b_i ∈ A_{q′}.
   - Pairs with a_i ∈ A_q. Fix α ∈ A_q and let I_α := {i : a_i = α}.
     - By (M2κ) these indices are consecutive, and their source states lie in one q-run Θ_α.
     - For each i ∈ I_α after its first w_c elements, at least w_c fallbacks of Θ_α have source states before k_i (the earlier elements
       of I_α). So k_i > f^{Θ_α}_{w_c}, and SAT-2 gives b_i ∈ V_{q′}(α).
     - So the pairs with a = α number ≤ w_c + |V_{q′}(α)|. Over α ∈ A_q they number ≤ |A_q|(w_c + max_α |V_{q′}(α)|).
   - The pairs with b_i ∈ A_{q′} are bounded the same way, with the roles of q and q′ exchanged. Every pair is of one of the two kinds.
   - |A_q| ≤ d_q + w_c and |V_{q′}(α)| ≤ d_{q′} + w_c. □
Corollary FB-2O. On 𝒞^2O, every phase of every N5 run, from every start pair, has
    f ≤ 1 + (n − 1)(1 + N_late) ≤ 1 + (n − 1)(1 + 12n²) = O(n³)
in-phase fallbacks.
Proof. FB-RED's late form: f ≤ 1 + (n − 1) + (n − 1)·N_late. On 𝒞^2O, Q = {q1, q2}, and:
- if q1, q2 are terminals of one class: N_late ≤ N_c ≤ 2(n + n − 1)(n + 2n − 2) < 12n²;
- if they are terminals of two classes: N_late ≤ 1 + (|A_{q1}| − 1) + (|A_{q2}| − 1) ≤ 4n;
- if one of them is the cycle node of its own class: κ of that vertex is constant ((0, 0)), and the one-terminal bound applies.
Every statement used is per phase and start-free: FBRED's statements are per phase of any run, and ROUTE-2, DIR, SAT-2 and PFZ-q are
statewise or run-internal, with bases at the first state of the window they bound. □
- Remarks.
  - 𝒞^1O is the case |Q| = 1. Then N_late ≤ |A_o| ≤ d_o + |U| − 1, which is R48's THETA-AFTER count up to the index convention.
  - The proof uses (2T) only in ROUTE-2's two-terminal case analysis and in SAT-2's single routed level.

## 5. What else a polynomial bound for N5 on 𝒞^2O needs (READING, with what is landed)
The 𝒞^1O chain (RESULTS R51) multiplies: phases × (transitions per phase given f) × f.
| ingredient | 𝒞^1O source | 𝒞^2O status |
| --- | --- | --- |
| phases per run | R47 (b): n(n − 1) + d_o | LANDED: R54 (e) Φ-kO, n(n − 1) + d_{q1}·d_{q2} |
| in-phase fallbacks f | R48 (i) FB-POLY | THIS NOTE: Corollary FB-2O, O(n³), CONDITIONAL on FBRED (REFEREE §C pending); lane-PROVED, unrefereed |
| crossings X per phase | R30 (c) R-STICK + SN-PREFIX; R34 (f) X-SN-PHASE; R52 | OPEN on 𝒞^2O. Needs R-STICK in set form, with R_D (vertices whose W-play meets D_k) for R. R55 (P-N5-GD, at CHECKER) gives G_D (a) without hypothesis and G_D (b), F1°, Wo under (h_D); R-STICK_D is not among them |
| transitions per phase given f (T) | R50 (h) Corollary PHASE (FRZ-U, KIND-MONO, RUN), R53 | OPEN on 𝒞^2O. R50's Theorem RUN counts Ξ-changes on R per fallback-free run through the single gate o; with D_k ⊆ {q1, q2}, R_D has two entry points and the route freeze (FRZ-U) must hold for both. Not attempted here |
| ρ (all Ξ(Q)-changes) | not needed on 𝒞^1O beyond THETA-AFTER | NOT needed for f (this note). Its fallback-free part is inside T |
- READING: a 𝒞^2O polynomial bound would follow from FB-2O + R54 (e) + a 𝒞^2O analogue of R50 (h) (T per phase polynomial in n, m, f).
  Only the last is open. It contains X and the fallback-free Ξ-changes.
- Beyond two terminals per class (OPEN): ROUTE-2 generalises to "the terminal routing at a state is acyclic". DIR holds for bottom
  terminals, and SAT-2 for a terminal whose next terminal's run is saturated. Iterating the pair count over a routing chain of depth h
  gives products of h value sets, i.e. (d + 2n)^{h} distinct tuples, which is polynomial for bounded h only. That is FBRED §5's nesting
  shape. A count that is polynomial in |Q_c| would need a different argument. CONJECTURE: none stated here.

## 6. DATA (DATA, not proof): experiments/si/fb2o/
Own checker fb2o.py. It runs N5 via experiments/new/box21/n5x.py step (read-only import) and evaluates every quantity in arithmetic κ,
with κopt by brute force over simple paths. Per phase it checks PFZ-q, ROUTE-2, DIR, SAT-2 and FB-2T's pair count. Games: the 43
repository instances with exactly two Odd choice vertices and n ≤ 40 (experiments/si/fb2o/lib2o.txt), plus climbs.
| set | games | phases | max f / phase | PFZ checks (viol.) | ROUTE (viol.) | DIR (viol.) | SAT (viol.) | FB-2T count (viol.) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib2o.txt (43 files) | 43 | 129 | 17 | 2,298 (0) | 304 (0) | 1 (0) | 0 | 0 |
- Mutation control MUT=1 (PFZ with j + 2 edges; DIR / SAT without Cyc_c) on lib2o.txt: PFZ fails 11 times. The check bites.
- A first version of the checker composed values by set union, as S1's ⊕ does. It reported 60 PFZ "violations" on
  experiments/new/box21/instances/fts_best24.pg. The lemma's sums are arithmetic: a vertex on the path and in P(Ξ(q)) counts twice.
  That checker was wrong; the arithmetic version reports 0. The lesson is recorded here: κ-PFZ is a statement about arithmetic κ sums,
  not about play values of the composed walk.
- Thin data: the late regime (≥ |U_c| − 1 fallbacks in one q-run, after g_{|U_c|−1}) is almost never reached: DIR 1 check, SAT 0. So
  DIR, SAT-2 and FB-2T rest on their proofs.
- Climbs (climb2o.py, logs/climb_*.txt). None reached the late regime:
  - objective "fallbacks in one phase": 6 random starts (n 7-12) stay at 1; 2 starts from fts_best24.pg (n 24) reach 4 and 12;
  - objective "DIR + SAT hypothesis hits": 12 library starts, 400 steps each, reach at most 1 hit.
  The regime the theorem acts in is not exercised by any data here.
- Reproduce (from experiments/si/fb2o): `python3 -I fb2o.py --list lib2o.txt` (≈ 3 s) → "games=43 phases=129 FMAX=17 … PFZ_n=2298
  PFZ_V=0 … FB2O PASS"; `MUT=1 python3 -I fb2o.py --list lib2o.txt` → PFZ_V=11, FB2O FAIL.
