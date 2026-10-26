# X_dir on the 2-Odd-choice game G^{u,u′}, and what 𝒞^2O would need (box 47)
L-NEW successor 26 (Opus 5.5), D14 / D18, Lead reading L40; Lead's GO 10:57Z (Lead's stamp): "(1) X_dir, then (2) HON-FF, as queued".
Written 2026-10-26 11:10Z onward (date -u). Working doc, unrefereed. Not a TARGET.md claim; G-N5-TIME stays open.
Labels: PROVED (L-NEW 26, unrefereed) / IMPLICATION / CONJECTURE / OPEN / DATA / READING / DEAD.
Builds on docs/new/N5-REC1-box46.md (§2 u-runs, §3 REC-1: X_dir, X_big) and docs/new/P-N5-HON-box46.md (frozen, sha1 07f8e767…; not edited).
Read first: docs/si/N5-RUND-box17.md §22 (L-SI 14: Lemmas ROOT, ROUTE-RELAY, SELF-FREE; the re-thaw loop (O2)).

## Summary
| § | item | label |
| --- | --- | --- |
| §1 | Lemma RESTRICT_U, Corollary REPRO_U for any U ⊆ Q (states with D_k ⊆ U run as N5^τ on G^U ∈ 𝒞^{|U|}O); every X_dir transition lies in one {u, u′}-run | PROVED (every game) |
| §1 | S1's counterstrategy on G^U can differ from σ̄_k (6 cases, always at a vertex that is its own cycle node), so D-sets and epochs are G's, not G^U's | DATA (instance sbmis_n12) |
| §2 | Lemma STAY: if no Even vertex on v's honest play at k switches, Ξ is constant along that play at k → k+1 and the play stays Odd-optimal; Corollary ROOT_v (every value change at v has an Even switch on v's own honest play), Corollary CHOICE (a σ̄(q) change without such a switch is a choice between optimal plays) | PROVED (every game, every transition) |
| §3 | Corollary XD-CAUSE (at an X_dir transition {u} → {u′}, each of u, u′ changes either at a tie or because an Even vertex on its own honest play switches); Corollary XD-ρ (X_dir ≤ the ρ_u events plus the flat exits) | PROVED; the count is R61 (f)'s, localised |
| §4 | the 𝒞^2O ledger: a phase on 𝒞^2O is polynomial if ρ_{q1}, ρ_{q2}, ALT's residuals and the |D| = 2 epoch lengths are | IMPLICATION (from landed R58, R61, R64, R65 and lane HON, REC-1) |
| §4 | ρ_q ≤ (n − 1)·π_q + π_q − 1 per phase, π_q := the distinct path sets of Ξ(q) in the phase | PROVED (elementary) |
| §5 | CONJECTURE XD-1 (at most one X_dir per {u, u′}-run): FALSE, pp2_n19 (a 𝒞^2O ping-pong {1} → {0} → {1}, from S3); "X_dir is a start-up transient before the first W-honest state": FALSE as a rule (xdhon_n13) | DEAD (instances) |
| §6 | data | DATA |
| §7 | how this meets L-SI §22 and L-RED's ping-pong gadget | READING |

## 0. Setting (every game)
As docs/new/N5-REC1-box46.md §0: N5 = SPEC S1-S5 (FIX 1-4, Q1-Q4); state k = (σ_k, τ_k); σ̄_k = S1's Odd counterstrategy to σ_k; Ξ_k =
V_{σ_k,σ̄_k}; W_k = V_{σ_k,τ_k}; λ = Ξ's cycle-node map; a phase P = a maximal run with (λ, τ) constant (RESULTS R38 (a)); Q = the Odd vertices
of out-degree ≥ 2; D_k = {q ∈ Q : σ̄_k(q) ≠ τ(q)}; X_dir(P) = the in-phase transitions k → k + 1 with |D_k| = |D_{k+1}| = 1, D_k ≠ D_{k+1}.
The HONEST PLAY of v at k: the play from v under (σ_k, σ̄_k), a lasso; its value is Ξ_k(v) (a value depends only on the play). N5^τ = SPEC with
S4b replaced by S4b^τ (RESULTS R64 setting). ρ_q(P) = the transitions of P that change Ξ(q) (RESULTS R61 (f)).
- For U ⊆ Q: G^U := G with every Odd v ∉ U cut to its edge τ(v); every u ∈ U keeps ALL its edges. So G^U ∈ 𝒞^{|U|}O. G^{u} is N5-REC1 §2's
  G^u; RESULTS R64's G′_E is G^{D_E} with each u ∈ D_E cut further to {τ(u), σ̄_E(u)}. A U-RUN of P: a maximal run of consecutive states of P
  with D_k ⊆ U.

## 1. Lemma RESTRICT_U and Corollary REPRO_U (PROVED, every game)
Lemma RESTRICT_U. For every state k of a phase P with D_k ⊆ U, statements (i)-(iv) of RESULTS R64 (a) RESTRICT_E hold with G′_E replaced by G^U.
Proof. R64 (a)'s proof (docs/new/P-N5-EPR-box45.md §1) verbatim. Its only use of the epoch is in (i): "σ̄_E is an Odd strategy of G′_E and
σ̄_k = σ̄_E". Here σ̄_k is an Odd strategy of G^U: σ̄_k(v) = τ(v) for v ∈ Q ∖ U (D_k ⊆ U), Odd vertices outside Q have one successor, and every
u ∈ U keeps all its edges. (ii)-(iv) use only that G^U's edges are G's, that every τ(v) is an edge of G^U, and (i). □
Corollary REPRO_U. Let J = (x, …, y) be a U-run of P and y′ := y + 1 if y → y + 1 is in-phase, else y′ := y. Then N5^τ on G^U from (σ_x, τ)
passes through (σ_x, τ), …, (σ_{y′}, τ), with the same fallback / non-fallback type at each transition as N5 on G, Ξ^{G^U} = Ξ at every
state of J, and x, …, y lie in one phase of that N5^τ run (the last transition may leave it: RESULTS R64's repair EPR-1).
Proof. R64 (b)'s induction verbatim, with RESTRICT_U at each state of J in place of RESTRICT_E. □
- For U = {u} this is N5-REC1 §2 (RESTRICT_u, REPRO_u). For U = {u, u′}: every X_dir transition k → k + 1 with D_k = {u}, D_{k+1} = {u′} has
  both ends in one {u, u′}-run (D_k, D_{k+1} ⊆ {u, u′}), so it is a transition of one N5^τ phase on the 2-Odd-choice game G^{u,u′}, exactly
  (states, values, fallback types). This is the Lead's "X_dir is exact on G^{u,u′}".
- What REPRO_U does NOT carry (DATA): S1's counterstrategy σ̄′_k on G^U need not equal σ̄_k. RESTRICT_E (i) proves Ξ′ = Ξ, not σ̄′ = σ̄ (R64
  does not claim it either). xd2.py (§6) finds 6 U-runs with σ̄′ ≠ σ̄ (SB_V) on the random sample; in all 6 the differing vertex is its own
  cycle node, whose choice is FIX 2's DFS choice and depends on the edges of other Odd vertices. Pinned:
  experiments/new/box47/instances/sbmis_n12.pg (sha1 d56d48259a6a81be786a47957efb560369da9fc5), S3 start, state 0: D = {0, 7}, vertex 0 is its
  own cycle node (Ξ(0) = (0, ∅, 0)), σ̄(0) = 6 on G and 3 on G^{0,7}, τ(0) = 9; Ξ equal. In 3 of the 6, the restricted D′_k ≠ D_k (σ̄′ = τ at
  that vertex). So the D-sets, epochs and X_dir are read on G; the restricted run carries states and values only. Nothing in §2-§4 uses σ̄′.

## 2. Lemma STAY and its corollaries (PROVED, every game, every transition of N5)
Lemma STAY. Let k → k + 1 be any transition of N5, v any vertex, π the honest play of v at k. If σ_{k+1}(w) = σ_k(w) for every Even vertex w on
π, then (i) Ξ_{k+1}(x) = Ξ_k(x) for every vertex x on π, and (ii) π is an optimal Odd play from v at k + 1: it is the play of (σ_{k+1}, σ̄_k) from
v, and its value is Ξ_{k+1}(v).
Premises (LANDED): RESULTS R18 (d) Lemma S (a) (S1's valuation is the pointwise ⊴-least over Odd strategies; signed on every game, R57 (a)), and
Ξ non-decreasing along a run (RESULTS R15 (a), as used in N5-REC1 §1 step 0); the order on valuations is total and antisymmetric on triples
(R64 (a)'s proof of (i)).
Proof. For x on π, the honest play of x at k is the part of π from x on (positional strategies). Every Even vertex on it lies on π, so it keeps
its successor at k + 1, and the play of (σ_{k+1}, σ̄_k) from x is the same lasso. Its value depends only on the play: V_{σ_{k+1},σ̄_k}(x) = Ξ_k(x).
Lemma S (a) at k + 1 (σ̄_k is an Odd strategy of G): Ξ_{k+1}(x) ⊴ V_{σ_{k+1},σ̄_k}(x) = Ξ_k(x). Monotonicity: Ξ_{k+1}(x) ⊵ Ξ_k(x). So
Ξ_{k+1}(x) = Ξ_k(x), which is (i); and the value of π at k + 1 equals the optimum Ξ_{k+1}(v), which is (ii). □
Corollary ROOT_v. Every transition that changes Ξ(v) switches some Even vertex on v's honest play at k. (Contrapositive of (i) at x = v.)
- Against L-SI's Lemma ROOT (docs/si/N5-RUND-box17.md §22.3): ROOT says a ρ-transition changes SOME Q-exit path; ROOT_v names the place: an
  Even vertex on the changed vertex's OWN current honest play, for every vertex, with no closure argument. Both are the same fact (Odd's
  optimal play survives unless Even breaks it); ROOT_v is the per-vertex form. (READING: neither bounds anything by itself.)
Corollary CHOICE. If σ̄_{k+1}(q) ≠ σ̄_k(q) and no Even vertex on q's honest play π at k switches, then Ξ is constant along π and π remains an
optimal Odd play from q at k + 1: the change of σ̄(q) is a choice between two optimal plays (a TIE CHANGE in this sense). □ (STAY (ii).)
- Relation to RESULTS R61 (e) Lemma ALT: ALT says a clean change of σ̄(q) strictly raises κ(q) unless tied. CHOICE is the converse localisation:
  a change with no Even switch on q's play is a tie in the play sense above. (ALT's TIE is defined by κ-values; CHOICE's by plays. I do not
  claim they coincide.)

## 3. X_dir: causes and a count (PROVED; the count is R61 (f)'s, localised)
Corollary XD-CAUSE. At every X_dir transition k → k + 1 with D_k = {u}, D_{k+1} = {u′}: (exit side) σ̄(u) moves from y ≠ τ(u) to τ(u); either
an Even vertex on u's honest play at k (through y) switches, or the move is a tie change (CHOICE). (Entry side) σ̄(u′) moves from τ(u′) to
y′ ≠ τ(u′); either an Even vertex on u′'s honest play at k (through τ(u′)) switches, or the move is a tie change. □ (CHOICE at u and at u′.)
Corollary XD-ρ. For every phase P: X_dir(P) ≤ Σ_{u ∈ Q} ρ_u^exit(P) + FLAT(P), where ρ_u^exit counts the transitions at which u leaves D and
Ξ(u) changes, and FLAT the X_dir transitions at which the leaving vertex keeps its value. Each counted ρ event has an Even switch on u's honest
play at k (ROOT_u). □ (Each X_dir transition has exactly one leaving vertex u.)
- READING: X_dir is not an independent quantity. Every X_dir transition is an epoch boundary, so X_dir ≤ N_ep − 1 ≤ Σ_q (ρ_q + tie_q + nc_q +
  cyc_q) by RESULTS R61 (f); XD-ρ is the part of that bound that X_dir uses, at the leaving vertex. By REPRO_U, ρ_u and ρ_{u′} inside a
  {u, u′}-run are the ρ counts of one N5^τ phase on G^{u,u′} ∈ 𝒞^2O (Ξ′ = Ξ). So the X_dir question IS the 2-Odd-choice ρ question, inside
  U-runs; what this does NOT give is a bound on the number of U-runs per phase.
- DATA (§6): on all 38 X_dir transitions in the samples, the entry side has an Even switch on τ(u′)'s honest play (SCH 38/38: no tie entry);
  the exit side changes Ξ(u) in 33 (RHO_U), with 4 TIE_U (Ξ_k(τ(u)) = Ξ_k(y)).

## 4. What 𝒞^2O would need (IMPLICATION; a ledger)
Setting: N5 on a game with Q = {q1, q2}. Per phase P, split the states by |D_k| ∈ {0, 1, 2}: S_0, S_1, S_2.
- f (in-phase fallbacks): ≤ 1 + (n − 1)(1 + 12n²) = O(n³) (RESULTS R58 Corollary FB-2O; landed, conditional on R56, landed).
- S_0 ≤ f_in + 4n² − 3n (Lemma HON + HON′, P-N5-HON-box46 / N5-REC1 §1, §1a; signed by REFEREE-2 16, REFEREE 14 pending).
- S_1 ≤ (1 + f + 4n² − 3n + X_dir + X_big)(T*_Q + 2) (Theorem REC-1 (c), N5-REC1 §3, an IMPLICATION from (Στ); (Στ) holds at audit strength since
  RESULTS R65 (GAPS 09:56Z)). T*_Q = T*(G^{q_i}) = O(m·Δ²·n¹¹) (N5-REC1 §2 size reading).
- X_dir + X_big ≤ N_ep − 1 ≤ Σ_{q ∈ {q1, q2}} (ρ_q + tie_q + nc_q + cyc_q) (RESULTS R61 (f), landed).
- S_2: Σ over the epochs with D_E = {q1, q2} of their states; each such epoch has len(E) ≤ 1 + the in-phase transitions of one N5^τ phase on
  G′_E ∈ 𝒞^2O (RESULTS R64 (d) EP-k). G′_E is again a 𝒞^2O game (with deg q_i = 2): EP-k is self-referential here; nothing reduces it.
So on 𝒞^2O, every phase is polynomial in n, m if the following three are (IMPLICATION, from the items above):
  (N1) ρ_{q1}, ρ_{q2} per phase; (N2) ALT's residuals tie_q, nc_q, cyc_q per phase; (N3) len(E) for epochs with D_E = Q (the "both deviate" kernel).
(N1) is L-SI's open question (§22.6) at m_c ≤ 2. Two sub-cases:
- q1, q2 in different honest classes of the phase (classes are phase-constant: λ is): each class has m_c ≤ 1, so every ρ event is a ROUTE event
  (SELF-FREE, §22.4). READING: the 𝒞^1O chain (R45, R48, R50) bounds route values with constant terminals; whether it transfers per class is OPEN
  (S4a's W-arena can cross classes at split states, so the classes do not decouple for Even's moves).
- q1, q2 in one class (Q_c = {q1, q2}): ROUTE-2 (R58 (c)) makes one of them direct at every state; the relay graph is acyclic at each state but
  can flip over the phase (frz40, §22.5): this is the re-thaw loop (O2). All 38 X_dir in the data are of this sub-case (SAME 38/38).
A bound that does hold (PROVED, elementary): in a phase, ρ_q ≤ (n − 1)·π_q + (π_q − 1), where π_q := the number of distinct path sets taken by
Ξ(q) in the phase. Proof: in a phase λ(q) is fixed; Ξ(q) = (λ(q), P, ℓ) is non-decreasing; while P is constant only ℓ ∈ {0, …, n − 1} can move,
and monotonically, so at most n − 1 changes per path set; the path set changes at most π_q − 1 times (a non-decreasing sequence that returns to
an earlier path set would have to be constant in between, the order comparing P before ℓ). □ So (N1) is equivalent, up to a factor n, to a bound
on the number of PATH-SET changes of Ξ(q) per phase. The pp2_n19 ping-pong (§5) is length-only (π_q = 1): it costs nothing in this ledger.

## 5. DEAD (instances)
(i) CONJECTURE XD-1 ("every {u, u′}-run holds at most one X_dir transition", my working hypothesis at 11:0xZ, written only in ppclimb.py's
  docstring; it would have made X_dir ≤ the number of {u, u′}-runs). FALSE:
  experiments/new/box47/instances/pp2_n19.pg (sha1 97b5b13212f9df0afc4f69e8c7663bac434d2cfb), a 𝒞^2O game (Q = {0, 1}), S3 start: phase [1, 3]
  (cycle node 9, path sets empty), D = {1} at state 1, {0} at state 2, {1} at state 3: two X_dir transitions in one {0, 1}-run, no fallback,
  no relay (A2U = 0; both terminals direct at all four states). Values change in path LENGTH only (cycle node 9 has even priority 24: shorter
  is better for Even): Ξ(0) (9, ∅, 8) → (9, ∅, 6) → (9, ∅, 5). Built by ppclimb.py (seed 94, from box46's xdir2_n17) and cut to G^{0,1} at
  state 1 with mkpp2.py; also with its start file instances/pp2_n19.start (sha1 c56f01694a0fcad1e2711f8fa028389a8f8f0a5c; phase [0, 2]).
  Obstruction: nothing forces the leaving and entering vertex to differ from the previous X_dir; each X_dir only needs an Even switch on
  each terminal's own play (XD-CAUSE), and two such switches in a row are cheap. What survives: XD-ρ; the ping-pong is paid by ρ (here
  length-only, π = 1).
(ii) The reading "X_dir is a start-up transient" (N5-REC1 §5, predecessor's DATA reading) as a RULE "no X_dir after the phase's first W-honest
  state": FALSE. experiments/new/box47/instances/xdhon_n13.pg (sha1 9d2d9ca2e8727b64af581b3691fc1dc70d0f7bf4), S3: state 0 is W-honest with
  D = {12} (a tie deviation: Ξ(12) = W(12) = (4, ∅, 3), σ̄(12) = 0, τ(12) = 5), state 1 has D = {1}: an X_dir at a W-honest source, flat at u = 12.
  6 of 38 X_dir have a W-honest state at or before k (HB); in all 6, k is the phase's first state and is itself W-honest. The weaker
  reading (X_dir sits at the start of its phase: POS ≤ 2 in all 38) is still DATA only.

## 6. DATA (experiments/new/box47/, run from that directory; outputs in out/)
xd2.py: every X_dir transition and every U-run (|U| = 2) holding an X_dir or a state with D = U; REPRO_U checked (REP_V: σ, τ, fallback type
through the run's last in-phase transition; XI_V: Ξ; SB_V: σ̄); MUT=1 drops u′ from U and bites (SB_V 2, XI_V 1 on xdir2_n17).
| sample | runs | phases | X_dir | U-runs checked | REP_V | XI_V | SB_V | SAME | SCH | RHO_U | TIE_U | A2U | VIA | HB | POS max | max X_dir in a U-run | max D = U states in a U-run |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41 (n ≤ 64), S3 + 2 random, seed 7 | 1,101 | 5,377 | 1 | 40 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 2 | 1 | 38 |
| random 3,000 𝒞^kO (k 2-4, n 5-18, gseed 111), S3 + 4 random, seed 8 | 15,000 | 40,203 | 15 | 98 | 0 | 0 | 6 | 15 | 15 | 13 | 1 | 5 | 1 | 2 | 1 | 1 | 3 |
| random 3,000 𝒞^kO (n 6-24, gseed 222), S3 + 4 random, seed 9 | 15,000 | 42,777 | 22 | 141 | 0 | 0 | 0 | 22 | 22 | 19 | 3 | 8 | 2 | 4 | 1 | 1 | 3 |
Columns: SAME λ(u) = λ(u′); SCH an Even switch on τ(u′)'s honest play at k; RHO_U Ξ(u) changes; TIE_U Ξ_k(τ(u)) = Ξ_k(σ̄_k(u)); A2U τ(u′)'s honest
play at k passes u (a relay of u's change, §22's sense); VIA u's honest play at k + 1 passes u′; HB a W-honest state at or before k in the
phase; POS k minus the phase's first state. Outputs out/xd2_lib41_k2.txt, out/xd2_rand3000.txt, out/xd2_rand3000b.txt (one line per X_dir).
- ppclimb.py (climb on (max X_dir in one U-run, max X_dir in one phase, max D = U states in a U-run, total), S3 start; out/ppclimb_*.txt): random
  𝒞^2O n ≤ 14 / ≤ 20, 𝒞^3O n ≤ 18 (seeds 91-93): (0, 0, 0, 0), (1, 1, 0, 1), (0, 0, 0, 0); seeded from xdir2_n17 (seed 94): (2, 2, 0, 2) =
  pp2_n19's parent; seeded from pp2_n19, n ≤ 30 / 40 / 60 (seeds 101-103, 3,000-4,000 steps): (2, 2, 0, 2), (2, 2, 1, 2), (2, 2, 0, 2). No growth
  beyond 2 X_dir per phase.

## 7. READING: how this meets L-SI §22 and L-RED's ping-pong gadget
- X_dir is a 2-terminal phenomenon, exact on G^{u,u′} (§1), and every X_dir in the data has both terminals in one honest class (SAME 38/38): it
  lives in L-SI's m_c = 2 setting. But the one ping-pong found (pp2_n19) is NOT a relay cycle: both terminals are direct throughout and no
  terminal's play passes the other. So "X_dir ping-pong" and "relay-cycle re-thaw" are different mechanisms; the first is paid by ρ at the
  leaving vertex (XD-ρ), the second is the open part of ρ itself.
- For L-RED's 𝒞^2O ping-pong gadget: pp2_n19 (n 19) is a 2-Odd-choice seed with a length-only ping-pong. By §4's elementary bound, a family
  that only repeats length-only ping-pongs is paid within n per path set; a family that hurts must change PATH SETS of Ξ(q) many times per
  phase (π_q large), which is where R45-type freezing (constant terminals) breaks with m_c = 2 (§22.5 (O2)).
- Next (OPEN): (N1) per sub-case; a count of path-set changes of Ξ(q) per phase when Q_c = {q1, q2}, using ROUTE-2 (one terminal direct at
  each state) and DIR (R58 (d): a direct terminal's κ lies in A_q, |A_q| ≤ d_q + w_c, after the class's first |U_c| − 1 fallbacks).
