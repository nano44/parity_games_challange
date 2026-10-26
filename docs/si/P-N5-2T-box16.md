# Referee packet P-N5-2T: with at most two Odd choice vertices per honest class, the Q-runs holding a late fallback number O(n²), so a phase has O(n³) in-phase fallbacks; on 𝒞^2O this holds in every phase (Theorem FB-2T, Corollary FB-2O)
Author: L-SI successor 11 (Opus 5.5; D15, D18, L37, L40), session_01FchPxfEZ9Fo56WrCZTvnXS. Written at the Lead's request of 04:04Z
(Lead's stamp). FROZEN at the Lead's freeze word of 04:19Z (Lead's stamp), after RESULTS R56 (P-N5-FBRED) landed at trunk eb81356c
(CHECKER C65, checker b911ecce). Repairs go to a NEW fixes file. Stamp: the commit (date -u). Source: docs/si/N5-2O-box16.md (lane note; this packet governs).
- Labels (D18 / L40): PROVED (L-SI 11, unrefereed) / READING / DATA. D1: wrong until checked.
- CONDITIONAL on RESULTS R56: every statement rests on R56 (packet P-N5-FBRED, docs/new/P-N5-FBRED-box44.md, sha1
  11b15455f70d439c93a48d7e82fcdc14ef73854d, l-new 3732ab55; fixes docs/new/P-N5-FBRED-fixes-box44.md, sha1
  05c249433431f7e147272ad689c0a7815b7a5b71, l-new 2742f3e9), LANDED at trunk eb81356c. R56 is quoted from its landed text below.
- Citation form (for packets that cite this one, e.g. L-NEW's P-N5-FBK): PFZ-q (§2) and DIR (§4) are to be cited exactly as stated
  there, by this file's sha1.
- Scope:
  - Every statement is about one phase of the candidate N5 (SPEC S1-S5 with FIX 1-4, docs/new/N5-ssi-global.md), on ANY game.
  - Theorem FB-2T is for phases in which every honest class holds at most two Odd choice vertices besides its cycle node. Every phase
    of every run on 𝒞^2O (exactly two Odd choice vertices) is such a phase; so is every phase on 𝒞^1O.
  - It bounds in-phase fallbacks only. It is NOT a running-time bound for N5 on any class, not a TARGET.md claim, and not a gauntlet
    pass. G-N5-TIME stays OPEN.

## 0. What to sign
| § | statement | label | to sign |
| --- | --- | --- | --- |
| §2 | (YB_q): a terminal on its own honest cycle has P = ∅ and length in [1, \|U_c\| − 1] | PROVED | yes |
| §2 | Lemma PFZ-q: FBRED's κ-PFZ_D holds on q-runs, where only κ(q) is constant | PROVED | yes |
| §3 | Lemma ROUTE-2: of two terminals of a class, at every state one is direct | PROVED | yes |
| §4 | Lemma DIR: late, a direct terminal's κ lies in A_q, of size ≤ d_q + \|U_c\| − 1 | PROVED | yes |
| §4 | Lemma SAT-2: late and saturated in q's run, the other terminal's κ lies in V_{q′}(κ(q)), of size ≤ d_{q′} + \|U_c\| − 1 | PROVED | yes |
| §5 | Theorem FB-2T: under (2T), N_late ≤ 1 + Σ_c (N_c − 1), with N_c = O(n²) | PROVED | yes |
| §5 | Corollary FB-2O: on 𝒞^2O every phase has f ≤ 1 + (n − 1)(1 + 12n²) | PROVED | yes |
| §6 | what else a 𝒞^2O bound needs; more than two terminals | READING | no |
| §7 | DATA (experiments/si/fb2o/) | DATA | no |

## 1. Setting, and the FBRED statements used (verbatim where quoted)
- Phase: a maximal run of states with (λ, τ) constant (RESULTS R38 (a) KEY). In-phase transitions are S4a steps or Even S4c fallbacks.
  - g_1 < g_2 < … are the in-phase fallbacks. As in FBRED and FBP, g_j also denotes the SOURCE state of the j-th fallback, and "t > g_j"
    compares states.
  - A fallback k → k+1 belongs to the run containing its source k (FBRED-N1). For a run Θ of states, f^Θ_j is the source of the j-th
    fallback whose source lies in Θ.
- FBRED §0 (every game), quoted:
  - "Q := the Odd vertices of out-degree ≥ 2 (Odd choice vertices)";
  - "C := the honest cycle nodes of the phase (λ is constant on a phase, so C and the classes below are constant)";
  - "T := C ∪ Q (TERMINALS), and for c ∈ C the HONEST CLASS U_c := λ^{-1}(c)";
  - κ_t(z) := (signed weight of P(Ξ_t z), s_c·ℓ(Ξ_t z)), with s_c := +1 if Ω(c) is odd and −1 if even;
  - wt_c(v) := sgn(v)·2^rank(v) if rank(v) > rank(c), else 0; κwt_c(v) := (wt_c(v), s_c).
  Sums of κ values and κwt's are ARITHMETIC (componentwise integer addition).
  - Graphs: "G_c := U_c ∖ (Q ∖ {c}) with c a sink, Even vertices keeping their edges inside, Odd vertices (all forced there) their edge
    if inside. For q ∈ Q ∩ U_c, q ≠ c: G_c^q := U_c ∖ (T ∖ {q}) … with q a sink, same rules."
  - κopt_c(z) := max{κwt_c(p ∖ {c}) : p a simple path of G_c from z to c}. κopt^q(z) := max{κwt_c(p ∖ {q}) : p a simple path of G_c^q
    from z to q} (FBRED §3.3). A max over an empty set is undefined.
  - Q-run: "a maximal run of consecutive states of the phase with Ξ(q) constant for every q ∈ Q".
- This packet's notation:
  - TERMINALS OF A CLASS: Q_c := (Q ∩ U_c) ∖ {c}.
  - q-RUN (q ∈ Q_c): a maximal run of states of the phase with Ξ(q) constant. By (INJ) and (M2κ) below, it is a maximal run with κ(q)
    constant.
  - DIRECT: q ∈ Q_c is direct at t if q lies on its own honest cycle at t, or its honest play at t visits c before any other vertex of
    Q_c.
  - d_q := |succ(q) ∩ U_c|; w_c := |U_c| − 1; Cyc_c := {(0, s_c·ℓ) : 1 ≤ ℓ ≤ |U_c| − 1}.
  - Hypothesis (2T) for a phase: |Q_c| ≤ 2 for every class.
- RESULTS R56 (a), facts used, signed on every game: "Facts (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′) per honest class, and
  κ-FB-ROUND_D (FBP §0.3, §1 with c for c_θ)". As stated in the packet (FBRED §1.1, "FBP §0.3 with c for c_θ"):
  - (Aκ): for z ∈ U_c ∖ {c}, next_t(z) ∈ U_c and κ_t(z) = κwt_c(z) + κ_t(next_t z), with next_t := σ_t at Even vertices and σ̄_t at
    Odd ones;
  - (M2κ): κ_t(z) ≤ κ_{t+1}(z) at every in-phase transition;
  - (INJ): the signed weight is injective on vertex sets;
  - (SP′): "the prefix of z's honest play up to its first visit of T ∩ U_c is simple, since c ∈ T lies on the cycle".
- R56 (a), (b) lemmas used (R56 (b) quoted from the landed text):
  - κ-FB-ROUND: at an in-phase Even fallback k → k+1, for every Even v ∈ U_c ∖ {c} and every successor x ∈ U_c of v,
    κ_{k+1}(v) ≥ κwt_c(v) + κ_k(x) ("FBP §1 verbatim with U_c, c");
  - κ-HAT-FREEZE_D (a): "for t > g_j, z ∈ U_c ∖ (Q ∖ {c}) and every simple path p of G_c from z to c with ≤ j edges, κ_t(z) ≥
    κwt_c(p ∖ {c})".
- R56 (c), κ-PFZ_D, quoted from the landed text: "(per q ∈ Q ∩ U_c, q ≠ c, Θ a Q_c-run): for t ∈ Θ after the j-th fallback of Θ and every
  simple path p of G_c^q from z to q with ≤ j edges, κ_t(z) ≥ κwt_c(p ∖ {q}) + κ_t(q); stated for z ∈ (U_c ∖ T) ∪ {q}". PFZ-q (§2)
  re-proves it on q-runs.
- R56 (f), Theorem FB-RED late form, quoted from the landed text: "f ≤ 1 + (n − 1) + (n − 1)·N_late, with N_late := the Q-runs of the
  phase holding a fallback g_j, j ≥ n". It is signed as a REDUCTION in ρ. FB-2T bounds N_late, so FB-RED's late form plus FB-2T gives
  an unconditional bound on f under (2T).

## 2. (YB_q) and Lemma PFZ-q (PROVED, every game)
### (YB_q)
Statement. If q ∈ Q_c lies on its own honest cycle at t, then P(Ξ_t q) = ∅ and 1 ≤ ℓ(Ξ_t q) ≤ |U_c| − 1. So κ_t(q) ∈ Cyc_c.
Proof. This is FBP §0.3 (YB) with q for o. (FBRED's step table, §4, reads it as surviving, but it is not in FBRED's signed text.)
- q's honest cycle has cycle node λ_t(q) = c, which is the top of that cycle.
- P(Ξ_t q) consists of the vertices of q's play before c with rank > rank(c). Those vertices lie on the cycle, below its top c, so there
  are none.
- q ≠ c, so ℓ(Ξ_t q) ≥ 1 is the length of q's play up to c. That play is a simple path in U_c ((SP′), (Aκ)), so ℓ ≤ |U_c| − 1. □
### Lemma PFZ-q
Statement. Let q ∈ Q_c and let Θ be a q-run, with κ_Θ(q) the value of κ(q) on Θ. Let j ≥ 0, and let t ∈ Θ with t > f^Θ_j (any t ∈ Θ if
j = 0). Let z ∈ (U_c ∖ T) ∪ {q}, and let p be a simple path of G_c^q from z to q with ≤ j edges. Then
κ_t(z) ≥ κwt_c(p ∖ {q}) + κ_Θ(q).
This is FBRED κ-PFZ_D with "Q_c-run" weakened to "q-run", and with the range of N-FBRED-1.
Proof. Induction on j.
- Base j = 0: p = (q), z = q, and the claim is κ_t(q) ≥ κ_Θ(q), an equality on Θ.
- Step j − 1 → j: if z = q, as in the base. Otherwise p = z·p′, where x, the second vertex, is q or lies in U_c ∖ T (G_c^q has no other
  terminal), and p′ is a simple path of G_c^q from x to q with ≤ j − 1 edges.
  - z Odd: z is not the sink and G_c^q drops Q ∖ {q}, so z is forced and x = next_t(z). (Aκ) gives κ_t(z) = κwt_c(z) + κ_t(x). The
    hypothesis at t (t > f^Θ_j > f^Θ_{j−1}) gives κ_t(x) ≥ κwt_c(p′ ∖ {q}) + κ_Θ(q).
  - z Even: let k := f^Θ_j < t, so k ∈ Θ.
    - The hypothesis at k (k ∈ Θ, k > f^Θ_{j−1}, any k if j = 1) gives κ_k(x) ≥ κwt_c(p′ ∖ {q}) + κ_Θ(q).
    - κ-FB-ROUND at k gives κ_{k+1}(z) ≥ κwt_c(z) + κ_k(x).
    - (M2κ) from k + 1 to t gives κ_t(z) ≥ κ_{k+1}(z).
  Both cases give the claim at t. □
- What changed against κ-PFZ_D: the proof reads κ of a terminal only at x = q, on states of Θ (t, or k ∈ Θ). Constancy of the other
  terminals of Q_c is never used. FBRED §1.2 calls this proof "FBP §1 verbatim", and FBP's κ-PFZ proof is the same induction with o for q.

## 3. Lemma ROUTE-2 (PROVED, every game)
Statement. If Q_c = {q, q′} with q ≠ q′, then at every state t of the phase, q or q′ is direct.
Proof.
- Suppose q is not direct: q is not on its honest cycle, and its honest play visits q′ before c.
- Honest plays are positional. So from its first visit of q′ on, q's play is q′'s honest play.
- If q′'s play visited q, q's play would visit q again, and q would lie on the cycle of its own play. That is excluded. So q′'s play
  never visits q.
- q′'s play reaches c: by (Aκ) it stays in U_c, and it ends in a cycle whose cycle node, c, lies on it. So q′ is on its own honest
  cycle, or it visits c before q. In both cases q′ is direct. □

## 4. Lemma DIR and Lemma SAT-2 (PROVED, every game)
Value sets, for q ∈ Q_c and a value α:
- A_q := {κwt_c(q) + κopt_c(y) : y ∈ succ(q) ∩ U_c ∖ Q, κopt_c(y) defined} ∪ {κwt_c(q) : c ∈ succ(q)} ∪ Cyc_c. So |A_q| ≤ d_q + w_c.
- If Q_c = {q, q′}: V_{q′}(α) := {κwt_c(q′) + β_y(α) : y ∈ succ(q′) ∩ U_c, y ≠ q′, β_y(α) defined} ∪ Cyc_c, where
  - β_q(α) := α and β_c(α) := (0, 0);
  - for y ∉ T, β_y(α) := the larger of κopt_c(y) and κopt^q(y) + α, over those that are defined.
  So |V_{q′}(α)| ≤ d_{q′} + w_c.
### Lemma DIR
Statement. Let t > g_{|U_c|−1}, and let q ∈ Q_c be direct at t. Then κ_t(q) ∈ A_q.
Proof.
- If q is on its honest cycle, (YB_q).
- Otherwise put y := next_t(q) = σ̄_t(q). (Aκ) gives y ∈ U_c and κ_t(q) = κwt_c(q) + κ_t(y). y ≠ q, because q is not on its cycle. y's
  honest play is the rest of q's play, so it visits c before any vertex of Q_c.
  - y = c: κ_t(y) = (0, 0) (cycle node value (c, ∅, 0)).
  - y ≠ c: y ∉ Q, so y is a vertex of G_c.
    - "≤": by (SP′), the prefix of y's play up to its first vertex of T ∩ U_c, which is c, is a simple path. Its vertices lie in
      U_c ∖ Q. Its Even edges are σ_t's, and its Odd vertices are forced. So it is a path of G_c, and (Aκ) along it gives
      κ_t(y) = κwt_c(prefix ∖ {c}) ≤ κopt_c(y).
    - "≥": simple paths of G_c have ≤ |U_c| − 1 edges, so κ-HAT-FREEZE_D (a) with j = |U_c| − 1 gives κ_t(y) ≥ κopt_c(y).
  - So κ_t(q) ∈ A_q. □
- Note: only the prefix of y's play up to c is used. Terminals on c's cycle after c do not matter.
### Lemma SAT-2
Statement. Let Q_c = {q, q′}, let Θ be a q-run, and let t ∈ Θ with t > g_{|U_c|−1} and t > f^Θ_{|U_c|−1}.
Then κ_t(q′) ∈ V_{q′}(κ_Θ(q)).
Proof.
- If q′ is on its honest cycle: (YB_q) for q′.
- Otherwise y := next_t(q′) ∈ U_c, κ_t(q′) = κwt_c(q′) + κ_t(y) by (Aκ), and y's play avoids q′.
  - y = q: κ_t(y) = κ_Θ(q).
  - y = c: κ_t(y) = (0, 0).
  - y ∉ T:
    - "≤": by (SP′), the prefix of y's play up to its first vertex e of T ∩ U_c is a simple path, and e ∈ {q, c} because q′ is not
      visited. Its vertices other than e lie in U_c ∖ T, its Even edges are σ_t's, and its Odd vertices are forced. (Aκ) along the
      prefix gives:
      - if e = c, it is a path of G_c, and κ_t(y) = κwt_c(prefix ∖ {c}) ≤ κopt_c(y);
      - if e = q, it is a path of G_c^q, and κ_t(y) = κwt_c(prefix ∖ {q}) + κ_t(q) ≤ κopt^q(y) + κ_Θ(q).
    - "≥":
      - when κopt_c(y) is defined, κ-HAT-FREEZE_D (a) gives κ_t(y) ≥ κopt_c(y);
      - when κopt^q(y) is defined, PFZ-q with j = |U_c| − 1 gives κ_t(y) ≥ κopt^q(y) + κ_Θ(q) (simple paths of G_c^q have
        ≤ |U_c| − 1 edges; t ∈ Θ, t > f^Θ_{|U_c|−1}).
    - κ_t(y) is at most the defined bound of its own route and at least every defined bound. So κ_t(y) = β_y(κ_Θ(q)). □

## 5. Theorem FB-2T and Corollary FB-2O (PROVED, every game; CONDITIONAL on RESULTS R56)
### Theorem FB-2T
Statement. In a phase with (2T), let N_late be R56 (f)'s count. Then
    N_late ≤ 1 + Σ_c (N_c − 1), the sum over classes with Q_c ≠ ∅, where
- for Q_c = {q}: N_c := |A_q| ≤ d_q + w_c;
- for Q_c = {q, q′}: N_c := |A_q|·(w_c + max_α |V_{q′}(α)|) + |A_{q′}|·(w_c + max_α |V_q(α)|) ≤ 2(d + w_c)(d + 2w_c), with
  d := max(d_q, d_{q′}).
Proof.
1. Late fallbacks and tuples.
   - Let k_1 < k_2 < … be the source states of the fallbacks g_j with j ≥ n. Each k_i > g_{n−1} ≥ g_{|U_c|−1} for every class, since
     |U_c| ≤ n.
   - Let x_i := (κ_{k_i}(q))_{q ∈ Q}. A vertex of Q is a terminal of its class or a cycle node c, and κ(c) = (0, 0) is constant.
   - By (INJ) and (M2κ), every coordinate is non-decreasing along the phase. So two late fallbacks lie in one Q-run iff x is equal at
     them, and N_late is the number of distinct x_i.
   - A coordinatewise non-decreasing sequence has 1 + (number of change indices) distinct terms. Each change index changes some
     class's sub-tuple, and class c's sub-tuple changes N′_c − 1 times, where N′_c is the number of its distinct values.
     So N_late ≤ 1 + Σ_c (N′_c − 1), and it suffices to show N′_c ≤ N_c.
2. Q_c = {q}. q is always direct, since there is no other terminal. By DIR at k_i, κ_{k_i}(q) ∈ A_q.
3. Q_c = {q, q′}. Put a_i := κ_{k_i}(q) and b_i := κ_{k_i}(q′). By ROUTE-2 and DIR, a_i ∈ A_q or b_i ∈ A_{q′} for every i.
   - Fix α ∈ A_q and let I_α := {i : a_i = α}. By (M2κ) the indices of I_α are consecutive, and their source states lie in one q-run Θ_α.
   - Let i ∈ I_α come after the first w_c elements of I_α. Those w_c elements are fallbacks of Θ_α with sources before k_i, so
     k_i > f^{Θ_α}_{w_c}. SAT-2 then gives b_i ∈ V_{q′}(α).
   - So the pairs with a = α number ≤ w_c + |V_{q′}(α)|, and the pairs with a ∈ A_q number ≤ |A_q|·(w_c + max_α |V_{q′}(α)|).
   - The pairs with b ∈ A_{q′} are bounded the same way, with q and q′ exchanged. Every pair is of at least one of the two kinds.
   - Sizes: |A_q| ≤ d_q + w_c and |V_{q′}(α)| ≤ d_{q′} + w_c. □
### Corollary FB-2O
Statement. On 𝒞^2O (exactly two Odd choice vertices q1, q2), every phase of every N5 run, from every start pair, satisfies
    f ≤ 1 + (n − 1)(1 + N_late) ≤ 1 + (n − 1)(1 + 12n²) = O(n³).
Proof. Every phase satisfies (2T), since |Q| = 2. FB-RED's late form (R56 (f)) gives f ≤ 1 + (n − 1)(1 + N_late). Cases for N_late:
- q1, q2 are the two terminals of one class: N_late ≤ N_c ≤ 2(n + n − 1)(n + 2n − 2) = 12n² − 14n + 4 < 12n² (d ≤ n, w_c ≤ n − 1);
- they are terminals of two classes: N_late ≤ 1 + (|A_{q1}| − 1) + (|A_{q2}| − 1) ≤ 4n;
- one of them is the cycle node of its class: its κ is constant, and N_late ≤ |A_q| ≤ 2n − 1 for the other.
Start-freeness: R56's statements are per phase of any run. (YB_q), ROUTE-2 and DIR are statewise. PFZ-q and SAT-2 are inductions
inside a q-run, with base its first state. Nothing uses the start pair or the history before the phase. □
- With RESULTS R54 (e) (Φ-kO: at most n(n − 1) + d_{q1}·d_{q2} phases), a run on 𝒞^2O has O(n² · d_{q1} d_{q2} · n³) in-phase fallbacks.
  This is a count of fallbacks, not of iterations.
- On 𝒞^1O (Q = {o}): N_late ≤ |A_o| ≤ d_o + |U| − 1, which is R48's THETA-AFTER count up to its index convention.

## 6. Not to sign (READING)
- For a polynomial iteration bound for N5 on 𝒞^2O, the 𝒞^1O chain (RESULTS R51: phases × (T per phase given f), with f bounded) needs
  two more pieces:
  - crossings X per phase in set form (an R-STICK_D for R_D);
  - transitions per phase given f (an analogue of R50 (h)).
  R55 (P-N5-GD) gives G_D, F1°_D and Wo_D. Both pieces are OPEN, and neither is claimed here.
- More than two terminals per class (OPEN):
  - ROUTE-2 generalises to "the terminal routing at a state is acyclic";
  - DIR holds for bottom terminals;
  - SAT-2 holds one level up from a saturated run.
  Nesting the pair count over a routing chain of depth h multiplies h value sets, giving (d + 2n)^h. That is polynomial only for
  bounded h: FBRED §5's nesting shape.
- ρ (every Ξ(Q)-change of a phase) is not bounded here and is not needed for f. Its fallback-free part is inside T per phase.

## 7. DATA (DATA, not proof): experiments/si/fb2o/
- Checker: own fb2o.py. It runs N5 via experiments/new/box21/n5x.py step() (read-only import). Every κ is ARITHMETIC, and κopt is a brute
  force over simple paths, so n is small.
- Per phase it checks PFZ-q (at every state of every q-run, for every j up to that state's fallback count), ROUTE-2, DIR, SAT-2 and
  FB-2T's pair count.
- Games: experiments/si/fb2o/lib2o.txt, the 43 repository .pg files with exactly two Odd choice vertices and n ≤ 40.
| set | phases | max f / phase | PFZ-q (viol.) | ROUTE-2 (viol.) | DIR (viol.) | SAT-2 | FB-2T count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lib2o.txt | 129 | 17 | 2,298 (0) | 304 (0) | 1 (0) | 0 checks | 0 checks |
- Mutation control (MUT=1: PFZ with j + 2 edges; DIR, SAT without Cyc_c): PFZ fails 11 times, as it should.
- Thin data, stated plainly: the late regime is essentially never reached. DIR is checked once, and SAT-2 and FB-2T not at all.
  - Climbs (climb2o.py) did not reach it either: on fallbacks in one phase, 6 random starts stay at 1 and 2 library starts reach 4 and 12;
    on DIR + SAT hits, 12 library starts reach at most 1.
  - So DIR, SAT-2 and FB-2T rest on their proofs, like FBRED's late form (N-FBRED-4).
- Trap, recorded: a checker that composes the path value with S1's ⊕ (set union) instead of arithmetic κ sums reports false PFZ
  violations: 60 on experiments/new/box21/instances/fts_best24.pg. The lemma's sums count a vertex twice when it lies on p and in
  P(Ξ(q)). The arithmetic checker reports 0.
- Reproduce, from experiments/si/fb2o (≈ 3 s each):
  - `python3 -I fb2o.py --list lib2o.txt` → "… PFZ_n=2298 PFZ_V=0 … FB2O PASS";
  - `MUT=1 python3 -I fb2o.py --list lib2o.txt` → "FB2O FAIL".
