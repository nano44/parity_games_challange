# N5 beyond 𝒞^1O: ledger, first obstruction, routes (box 43)
L-NEW successor 22 (Opus 5.5), D14 / D18, Lead reading L40; Lead's brief 21:22Z, GO 21:55Z (Lead's stamps). Written from
2026-10-25 22:25Z (date -u). Working doc, not a packet, unrefereed. Labels: PROVED / CONJECTURE / OPEN / DATA / READING.
TARGET.md diff: nothing here is a claim of TARGET.md §1. No polynomial bound for N5 is proved, on 𝒞^1O or beyond. G-N5-TIME open.

## 0. Setting and classes
N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md. States (σ_k, τ_k); Ξ_k, λ_k (Even's valuation, its cycle-node map); U_k, λ^U_k (Odd's
valuation of τ_k on G^d, its cycle-node map). Joint λ-run: (λ, λ^U) constant (R47). Phase: (λ, τ) constant (R38 (a) KEY: = joint
λ-phase). A choice vertex is a vertex of out-degree ≥ 2.
- 𝒞^kO: exactly k Odd choice vertices o_1..o_k (any number of Even ones). 𝒞^1O is the class of R17-R47.
- 𝒞^1E: exactly one Even choice vertex e (any number of Odd choice vertices). The mirror class of 𝒞^1O.
- FRONTIER 𝒞^{≥2E,≥2O}: at least two choice vertices for each player. By §1 this is where "beyond 𝒞^1O" is really open.
- N5^OF: N5 with S4c changed to "Odd falls back first": if I_τ ≠ ∅, switch-all for Odd on I_τ (σ unchanged), else Even's S4c. Every
  other step as in N5.

## 1. Results
### 1.1 Lemma DUAL (PROVED, every game; from the SPEC)
For every game G and start pair (σ_0, τ_0): the N5 run on G from (σ_0, τ_0) and the N5^OF run on G^d from (τ_0, σ_0) are mirror
images: state k of one is state k of the other with the two strategies exchanged. (G^d = n5.py's dual: owners swapped, Ω + 1; G^d's
Even strategy is G's τ.) Consequently the N5 run on G^d from (τ_0, σ_0) is the mirror of the N5 run on G up to and including the
source state of the first TWO-SIDED fallback (S4c with I_σ ≠ ∅ and I_τ ≠ ∅), and the whole run if there is none.
Proof. (i) Engine invariance: (G^d)^d is G with Ω + 2. SPEC S1 uses Ω only through rank (order of (Ω(v), v)) and Ω mod 2, both
unchanged by + 2, and owners are back; so every S1 output (valuations, optimal counterstrategies, tie-breaks) on (G^d)^d equals the
one on G, and the same holds for every restricted arena of S4 (their duals are the corresponding arenas with Ω + 2).
(ii) S2: G^d-Even's improving set for τ is computed on G^d = N5's I_τ; G^d-Odd's improving set for σ is computed on (G^d)^d, = I_σ
by (i). (iii) S4a on G^d computes G^d-Even's new strategy as "Odd's optimal counterstrategy in the dual of the arena where G^d-Even's
v keeps {τ(v)} ∪ I_τ(v) and G^d-Odd is fixed to σ, against σ"; that dual is, by (i), N5's S4b arena H′ (with Ω + 2), so the result is
N5's τ_new. Symmetrically S4b on G^d gives N5's σ_new. (iv) S3 is stated as "the same rule on G^d" for Odd, so it is mirror-symmetric
(only used when no start is given). (v) S5's stop rule (I_σ = I_τ = ∅) is symmetric. (vi) S4c: N5 on G falls back for G's Even when
I_σ ≠ ∅; N5^OF on G^d falls back for G^d's Odd (= G's Even) when its improving set (= I_σ) is non-empty, with the same switch-all
and the same tie-break "(valuation, larger index)" on the same valuations by (i); when I_σ = ∅ both fall back for G's Odd on I_τ.
So every step agrees; induction on k. The second sentence: N5 and N5^OF on G^d differ only at a two-sided fallback. ∎
DATA (experiments/new/box43/mirror.py, n5x.step = n5.py's loop): lib41 (412 runs, 15 with two-sided fallbacks, 54 such fallbacks
by dblfb.py) and 3,000 random C^kO games (k = 1..4, n 4-14): N5 on G = mirror of N5^OF on G^d in 3,412 / 3,412 runs; N5 on G^d
first differs from the mirror exactly one step after the first two-sided fallback, 0 violations. dualsym.py: 1,999 / 2,000 random
runs mirror N5 itself; the one difference follows a fallback.

### 1.2 Corollary 1E (PROVED)
On 𝒞^1E with Even choice vertex e (d_e := deg(e)): (a) σ changes at most d_e − 1 times along any N5 run (σ is fixed by σ(e) and the
σ's are a strict ≺_G-chain, R15 (c), (d)); (b) the run splits into at most n(n − 1) + d_e maximal runs with (λ^U, σ) constant ("dual
phases"; λ^U changes ≤ n(n − 1) times, R47 Lemma Φ (b)-(c)). (Direct; this is Corollary Φ-1O read through DUAL.)

### 1.3 Theorem MIRROR (PROVED; the implication, not the bound)
Let L(n) be a bound on the number of transitions inside the FIRST phase of the N5 run from an arbitrary start pair, over all 𝒞^1O
games with n vertices. Then N5 on every 𝒞^1E game with n vertices, from every start pair, makes at most (n(n − 1) + d_e)(L(n) + 1)
iterations.
Proof. N5 on G ∈ 𝒞^1E is the mirror of N5^OF on G^d ∈ 𝒞^1O (DUAL). (1) Phases of the N5^OF run (G^d's (λ, τ) constant, i.e. G's
(λ^U, σ)) number at most n(n − 1) + d_e: N5^OF applies a non-empty set of improving switches to σ and/or τ at every iteration, so
R15 (c), (d) and R47 Lemma Φ hold for it verbatim (their proofs use only that property). (2) N5 is memoryless (the next state is a
function of the current one, SPEC S4). Take a phase of the N5^OF run starting at state x. Until its first two-sided fallback it
coincides with the N5 run from x; at a two-sided fallback N5^OF switches G^d's Odd strategy (on 𝒞^1O that is a τ-change of G^d, a
phase boundary). So the phase is a prefix of the first phase of the N5 run from x and has at most L(n) transitions. ∎
- Hypothesis to check (READING): the fleet's 𝒞^1O per-phase lemmas are stated for "a phase of an N5 run". By memorylessness a bound
  for every phase of every run from every start pair IS a bound L(n); a bound proved only for runs from the S3 start is not. R18 says
  "from any start"; for the other items the referees should confirm that no proof uses the start pair (I found none in the items I read).
  grep of RESULTS R17-R47 for "start" (22:27Z): R18 states "any start pair"; no item restricts its setting to the S3 start; the
  referees' data for R28-R47 used 3 named starts plus random starts.
- Scope: 𝒞^1E contains games with arbitrarily many Odd choice vertices. So whatever the 𝒞^1O program proves for phase length
  transfers to a class with unboundedly many Odd choice vertices. Still CONDITIONAL in content: L(n) is not proved polynomial
  (G-N5-TIME on 𝒞^1O: FBPOLY in review, FX, K open).

### 1.4 Corollary Φ-kO (PROVED, every game)
Distinct τ's along an N5 run ≤ ∏_i deg(o_i) (no τ repeats, R15 (c), (d) on G^d), so phases ≤ n(n − 1) + ∏_i deg(o_i). Mirror: dual
phases ≤ n(n − 1) + ∏ over Even choice vertices of deg. On 𝒞^kO with k fixed, phases ≤ n(n − 1) + n^k: POLYNOMIAL for fixed k, so on
𝒞^kO (k fixed) N5 is polynomial iff phase length is. The per-vertex sharpening "τ(o_i) changes ≤ deg(o_i) − 1" is FALSE (§3, DATA).

### 1.5 Lemma ENDGAME (PROVED, every game; small)
If I_σ = ∅ at state k then σ_j = σ_k for all j ≥ k (I_σ depends on σ alone, R15 (d); S4a then keeps σ; S4c with I_σ = ∅ changes τ
only). Mirror: if I_τ = ∅ at k, τ is constant from k on.

## 2. Ledger (item 1): which landed lemma uses "o is the only Odd choice vertex"
Full table (252 rows, R15-R47 + FBPOLY, FX, KW15, KW42, NH42): docs/new/N5-MULTI-ledger-box43.md (READING; provenance stated there).
Verdicts: V verbatim; V1P one-player lemma (true on G_τ, G[X] of any game); I per-Odd-vertex index; S set form only (o replaced by the
disagreement set D_k := {Odd u : σ̄_k(u) ≠ τ_k(u)}, R by R_D := vertices whose (σ_k, τ_k)-play meets D_k); F fails as proved; FI
fails by inheritance; U unclear.
| verdict | RESULTS R15-R47 | packets (FBPOLY, FX, KW15, KW42, NH42) |
| --- | --- | --- |
| V | 42 | 7 |
| V1P | 7 | 0 |
| I | 9 | 1 |
| S | 12 | 0 |
| F | 35 | 11 |
| FI | 80 | 17 |
| U | 31 | 0 |
Survive verbatim on every game (READING; those marked "every game"/"any game" in RESULTS are PROVED there): R15 (all); R18 Lemma R,
Lemma S; R21 XW, EQ, FBL-N (i); R23 (K), WM, LV′; R24 Lemma R, TB; R25 (T), COARSE-SI, TAME, MONO, NOINF, Theorem FB; R27 U, HI, UL,
GR, NU, Theorem LP; R28 U-loc; R29 TRANSFER, CN; R31 P-OPT, FBW; R34 (F), Z-COUNT; R38 KEY, CN-LAST; R43 STALE-GATE; R44 FB-ROUND (κ
form, any cycle-node class); R47 Lemma Φ; KW15 W-ONCE; KW42 WLAG, PAR.
The four roots of every F (READING; each confirmed by me at the cited line):
1. (HP) honest play = (σ, τ)-play until the first visit of o (P-N5-FBPOLY l.100-102; NH42 l.89 "σ̄ = τ off o"). On general games
   they agree only until the first vertex of D_k, and D_k moves with σ inside a phase (τ fixed). Breaks Lemma G (b), TC, H3H2,
   H2-STICK, R-CONST, Fact 0, T0U (b), CN-ONLY.
2. (RT) one route terminal: Ξ = π ⊕ θ, W = π ⊕ w on R (RESULTS l.844, R19 (a) Lemma G (b)). Breaks R20 C, PIECE, P3′, BAND, NL,
   LEAVE, FBW-S, R-SAME, CASC/U1, CASC-U2, Fact A (KW15), ABOVE-h, KW-FREEZE, Lemma SW.
3. (FO) "Odd vertices other than o are forced" inside a proof step (KW42 l.115; G_U's forced Odd edges, RESULTS l.2170). Breaks NF,
   OE, OR, TC-SPLIT, H1-DROP, TOGGLE, HAT-FREEZE, P-FREEZE, EXIT-SWITCH, H-PATH.
4. (TD) τ is fixed by τ(o) (RESULTS l.802 R18 (c), l.2342 Φ-1O (a)). On general games only "no τ repeat" survives (§1.4).
Consequence (READING): FB-POLY, FX, Theorem NH, both K notes, HN-POLY-ALL, SCOPE-FB, X-SN-PHASE, TOGGLE-COUNT are at most FI on the
frontier; on 𝒞^1E all of them transfer by §1.3 (as bounds on phases of N5^OF on G^d, through memorylessness).
Per-Odd-vertex survivors (I, READING): ACT, Fact R, H1-INT (a)/(c), SAND, T0U (a), J1 (existential: a non-tame transition switches
σ̄ at SOME o_i above M_k, from TAME), CAP per o_i (given OFF in S form), Y-FORM / κ-Y-FORM / MINSET (a) as a repair (Y_t := successors
of o_i in U whose honest play avoids o_i; τ′ := σ̄_t except τ′(o_i) = y; then Lemma S (a)). The per-vertex form of Φ-1O (a) is FALSE
(§3). Set-form survivors (S, READING, unchecked by anyone): G (a), Wo, FBL-N (ii), F1° (every change of D_k counted as a crossing),
GAP, OFF, DF′, OFFGATE, R-STICK first sentence, H3-CONST, WCH, R18 Prop X (X := no path to any Odd choice vertex).

## 3. First obstruction (item 2; all DATA)
Tools: experiments/new/box43/ (README). Starts: best-reward (SPEC S3) unless stated. Instances checked with n5.py + check_sol2.py
("zielonka(oink zlk) OK strategies verified", Oink 8fbf0a7).
### 3.1 Exhaustive (canonical form of L-COMP's exh.py)
| table | games / runs | max it | max T | max TJ | max phase | max f / phase | RET (all) | RETN | TX |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 𝒞^2O n 3, canonical | 3,840 | 1 | 1 | 1 | 0 | 0 | 0 | - | 0 |
| 𝒞^2O n 3, all start pairs | 3,840 / 29,160 | 3 | 3 | 2 | 1 | 1 | 84 | - | 0 |
| 𝒞^2O n 4, canonical | 4,193,376 | 3 | 3 | 2 | 2 | 1 | 10,224 | 0 | 0 |
| frontier 𝒞^{≥2E,2O} n 4, canonical, no forced Odd | 1,405,536 | 3 | 3 | 2 | 2 | 1 | 4,704 | 0 | 0 |
RET = some τ(o_i) returns to an earlier value; RETN = the same with o_i not its own λ^U cycle node before and after (excludes the
own-cycle-node length switches of R15 (b) / R38 CN-LAST); TX = T > Σ_i (deg(o_i) − 1). Comparison: L-COMP's 𝒞^1O n 4 canonical table
(experiments/n5-exhaustive/README.md): max it 3, max in-phase 2. So at n ≤ 4 no 𝒞^1O-polynomial quantity is larger on 𝒞^2O; every
return at n ≤ 4 is an own-cycle-node switch. Files: experiments/new/box43/results/.
### 3.2 The first obstruction: per-Odd-vertex τ counts (Φ-1O (a) per o_i)
- instances/ret2_n7.pg (sha1 8a354f5704c6e18d62d50cc467794f5a2b78738d; n 7, Odd choice 1, 3, both degree 2; iterations 2, fallback 0):
  τ(1): 3 → 0 → 3, non-own-cycle-node. Mechanism: simultaneity. S4b best-responds to the OLD σ (1 → 0 → 4 → 5 → cycle {5, 6}), and
  S4a cuts that route in the same iteration (4 → 4); then 1 → 3 joins the cycle 1 ↔ 3 that 3 → 1 created. The game is in 𝒞^1E
  (only Even choice vertex 4), so by DUAL this is the mirror of an ordinary σ(e)-return on a 𝒞^1O game: harmless for running time.
- instances/tx2_n8.pg (sha1 c0f7b214e4e50720ea2d3082b181959f4aaa9f86; FRONTIER: Even choice 4, 6; Odd choice 1, 3 of degree 2;
  iterations 3, fallback 0): τ = (3,2) → (0,2) → (0,1) → (3,1), all four joint strategies, T = 3 = ∏deg − 1 > Σ(deg − 1) = 2; Even idle
  after iteration 1 (I_σ = ∅, ENDGAME), so iterations 2-3 are pure Odd improvement: 1 → 3 is improving only after 3 → 1.
  Reported to the Lead 22:05Z (l-new eb273ebc).
- instances/retf_n6.pg (sha1 8b936bfbc78d3d16ab17ed7bfedf1f7db05da73d; FRONTIER: Even choice 4, 5; Odd choice 0 (degree 3), 1;
  iterations 3, fallback 0): τ(0): 2 → 1 → 5 → 1, a non-own-cycle-node return (λ^U(0) = 3 throughout); τ(0) changes 3 > deg(0) − 1
  = 2. Mechanism: simultaneity again (S4b best-responds to the old σ(5) = 5, S4a switches 5 → 4 in the same iteration).
- So: the first one-Odd use to break on the frontier is (TD), per Odd vertex: smallest found n 6 (retf_n6; greedy shrink from a
  climb at n ≤ 6); exhaustive n 4 has none (RETN 0, TX 0); n 5 not exhausted (climbs at n ≤ 5, 2 × 15,000 steps: none).
### 3.3 Growth search (climbs, experiments/new/box43/climb.py; n ≤ 12-20, 15,000-40,000 steps each)
| objective | k = 1 | k = 2 | k = 3 | k = 4 | k = 5 |
| --- | --- | --- | --- | --- | --- |
| T, Odd choice degree 2 (bound ∏deg − 1 = 2^k − 1) | - | 3 (n 12) | 4 (n 12; 4 at n 20) | 6 (n 20) | 5 (n 12) |
| longest phase (degree 2, n ≤ 16) | 6 | 13 | 10 | - | - |
The k = 2 phase of 13 (n 16) is a Bellman-Ford chain: λ ≡ 0 after τ settles, one length switch per step (≤ n − 1). No growth faster
than linear in n was found in any measure; T stays far below 2^k − 1 for k ≥ 3. lib41's 135 frontier games (hard families: tc, tc+,
counter_*; |D_k| up to 106): D_k changes at most 5 times inside a phase (𝒞^1O games of lib41: 10). DATA only; small n.
### 3.4 Open in this section
Whether n 5 has a RETN or TX instance (n 5 is too large for exhaustive enumeration in Python here); a growing family. Both
mechanisms seen (stale-σ simultaneity; Odd-internal improvement after Even stops) give one extra τ-change per instance; no
composition of them into a family was found.

### 3.5 Do 𝒞^1O ∪ 𝒞^1E contain the known hard families? NO (DATA, Lead's ask 23:02Z)
experiments/new/box43/famcount.py (Oink 8fbf0a7 generators; PGSolver ports in experiments/hard-families/pgsolver_port.py), N = 2, 4, 8,
results/famcount_N2_4_8.txt. Choice vertices (out-degree ≥ 2), Even / Odd:
| family | N 2 | N 4 | N 8 | class |
| --- | --- | --- | --- | --- |
| tc | 6 / 7 | 25 / 26 | 99 / 100 | frontier |
| tc+ | 6 / 6 | 40 / 40 | 288 / 288 | frontier |
| counter_symsi | 9 / 9 | 17 / 17 | 33 / 33 | frontier |
| counter_rr | 4 / 4 | 8 / 8 | 16 / 16 | frontier |
| counter_dp | 2 / 3 | 4 / 5 | 8 / 9 | frontier |
| counter_m | 3 / 3 | 6 / 6 | 12 / 12 | frontier |
| counter_core | 4 / 5 | 8 / 9 | 16 / 17 | frontier |
| counter_rob | 13 / 12 | 38 / 35 | 124 / 117 | frontier |
| counter_ortl | 4 / 1 | 8 / 1 | 16 / 1 | 𝒞^1O |
| counter_qpt | 1 / 0 | 3 / 0 | 7 / 0 | one-player (no Odd choice; N 2 is also 𝒞^1E) |
| switchallexp (Friedmann, PGSolver port) | 22 / 2 | 40 / 4 | 76 / 8 | frontier (Odd choice = N) |
| switchbestexp (Friedmann, PGSolver port) | 38 / 2 | 70 / 4 | 134 / 8 | frontier (Odd choice = N) |
| recursiveladder | 4 / 5 | 9 / 10 | 19 / 20 | frontier |
So only counter_ortl (𝒞^1O) and counter_qpt (one-player, R17) lie in 𝒞^1O ∪ 𝒞^1E. Every family on which classic strategy improvement
is exponential in the fleet's bench (switchallexp, switchbestexp) and every other Oink counter family is frontier, with both choice
counts growing in N. Friedmann's two families have exactly N Odd choice vertices, all of out-degree 2 (checked at N = 8): by Φ-kO their phase count is ≤ n(n − 1) + 2^N, so
Φ-kO alone says nothing useful there. (N5 itself is linear on all of them: experiments/new/n5/per_family_summary.txt.)

## 4. Routes (item 3)
### 4.1 Route MIRROR (mine; PROVED as an implication, §1.3)
Covers 𝒞^1O ∪ 𝒞^1E with one proof program. Cross-field reading (D18): the game-theoretic duality G ↔ G^d acts on N5 as an exact
symmetry broken only by S4c's tie rule (Even falls back first); this is the same situation as a self-dual pivoting method in LP whose
primal/dual symmetry is broken only by its tie rule, and the fix is the same: prove bounds for the rule family closed under the
symmetry (here N5 and N5^OF). READING, no literature claim.
Next step: (a) referees check §1.1-§1.3 (short); (b) confirm the "from any start pair" hypothesis for the 𝒞^1O per-phase items.
### 4.2 The Lead's product route, evaluated
"Each o_i's τ-change as a phase boundary of a product of 𝒞^1O runs": the product bound is §1.4 (phases ≤ n(n − 1) + ∏deg(o_i),
polynomial for fixed k). The sum form (τ-changes ≤ Σ(deg(o_i) − 1), i.e. independent 𝒞^1O clocks) is FALSE (tx2_n8). Inside a phase,
the 𝒞^1O analysis does not split into k copies: D_k moves inside a phase with τ fixed, because σ̄ depends on σ (ledger root HP). So
the product route gives 𝒞^kO for FIXED k only, and only if the per-phase lemmas survive in S form (CONJECTURE below).
### 4.3 Route Δ for the frontier (CONJECTURE / OPEN)
Replace o by the disagreement set D_k and R by R_D. CONJECTURE Δ1: the ledger's S rows hold with (o, R) := (D_k, R_D) and with
"crossing" := a transition where R_D or D_k changes. CONJECTURE Δ2 (the new count): inside one phase, D_k changes at most poly(n)
times. DATA: lib41 frontier ≤ 5 per phase, random frontier ≤ 1; climb for D-changes per phase running (cl5, k = 3, n ≤ 16: 3 so far).
On 𝒞^1O D_k ⊆ {o} and its changes are crossings, so Δ2 generalises the crossing count X (FX). OPEN: (RT) has no S form (several
terminals with different (Ξ, W) pairs), so the route-form lemmas (R19 (b), R20, R22 (c), R24, R26, CLS, KW) need a multi-terminal
replacement; I have none.

## 5. Status
PROVED: DUAL, Corollary 1E, Theorem MIRROR (implication), Φ-kO, ENDGAME. DATA: §3 tables and instances; mirror checks. READING:
ledger rows; the "any start" hypothesis. CONJECTURE: Δ1, Δ2. OPEN: polynomial phase length on 𝒞^1O (hence on 𝒞^1E), the frontier.
