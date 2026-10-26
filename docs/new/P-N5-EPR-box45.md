# Packet P-N5-EPR (box 45): an epoch of an N5 phase is a run of N5 on the game restricted to the epoch's Odd choices (RESTRICT_E, REPRO); epochs with no disagreement have ≤ n + m transitions (EP-0); per phase, transitions are the sum of epoch lengths (EP-k); epochs with one disagreement are polynomial under a named premise (EP-1) — every game
L-NEW successor 24 (Opus 5.5), D14 / D18, Lead reading L40; Lead's GO 06:15Z (Lead's stamp): "packet P-N5-EPR, frozen and self-contained.
To sign: RESTRICT_E, REPRO, EP-0 and EP-k (unconditional), plus EP-1 with premise (Στ) named, stated as an implication. Not to sign: the
(Στ) audit (READING) and the data." Written 2026-10-26 06:27Z (date -u). FROZEN at push: later text goes into a fixes file.
Source: docs/new/N5-EPR-box45.md (working doc; this packet governs). Labels: PROVED (L-NEW 24, unrefereed) / IMPLICATION / READING / DATA.
Not a TARGET.md claim. EP-0 and EP-1 bound the transitions of ONE EPOCH; nothing here bounds the number of epochs, so nothing here bounds
N5's running time on any class beyond 𝒞^1O ∪ 𝒞^1E. G-N5-TIME stays open.

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Lemma RESTRICT_E (i)-(iv) | PROVED |
| §2 | Corollary REPRO | PROVED |
| §3 | Corollary EP-0 | PROVED |
| §3 | Corollary EP-k | PROVED (a REDUCTION) |
| §3 | Corollary EP-1: (Στ) ⇒ the stated bound | IMPLICATION (PROVED as an implication; (Στ) is NOT claimed) |
| §4 | the (Στ) audit; Lemma TIE-W (offered, PROVED, not needed by any item above) | READING (audit); TIE-W optional |
| §5 | data, including DIV = 0 | DATA (not to sign) |
| §6 | combination with ALT; what this does not give | READING (not to sign) |
- Premises (all LANDED unless marked):
  - SPEC S1-S5 of docs/new/N5-ssi-global.md (with FIX 1-4, Q1-Q4): S1 (valuations; S1's counterstrategy procedure), S2 (improving edges),
    S4a, S4b, S4c (FIX 3: in an iteration where Even falls back, τ is unchanged; Odd falls back only if Iσ = ∅), S4d.
  - RESULTS R18 (d) Lemma S (a): S1's valuation L_σ is the pointwise minimum of V_{σ,τ′} over Odd's strategies τ′ (VJ00 (11)). Signed under a
    𝒞^1O setting line; both referees CONFIRMED that it holds on every game (RESULTS R56, landing note N-FBRED-3; the same statement is
    signed on every game as (VJ) in RESULTS R57).
  - RESULTS R17 (c), (e) (one-player games: a λ-phase has fewer than n + m switch-best steps; N5's step for Even is switch-best and its
    fallback fires only in the value-flat situation and then leaves no improving edge).
  - RESULTS R38 (a) KEY (a (λ_Ξ, τ)-phase is a joint λ-phase), used only to name the phase.
  - For EP-1 only: RESULTS R48 (i) Theorem FB-POLY, RESULTS R50 (h) Corollary PHASE and RESULTS R51 (a), (b) (the per-phase bound T* and
    start-freeness), read through premise (Στ) (§3).
  - No (P). No (h_D), no hypothesis on |Q|, on τ or on the start pair.

## 0. Setting (every game)
- G = (V, E, Ω, owner), n := |V|, m := |E|, Δ := max out-degree. N5 = SPEC S1-S5. State k = (σ_k, τ_k); σ̄_k := S1's Odd counterstrategy
  to σ_k on G; Ξ_k := S1's valuation of σ_k, which is the play valuation V_{σ_k,σ̄_k}; W_k := V_{σ_k,τ_k} (the valuation of σ_k in G_τ, Odd
  fixed to τ_k); λ := Ξ's cycle-node map. Iσ_k, Iτ_k: SPEC S2 (Iτ on G^d). A PHASE: a maximal run of consecutive states with (λ, τ)
  constant; an IN-PHASE transition has both ends in it. Q := the Odd vertices of out-degree ≥ 2.
- EPOCH: a maximal run E = (x, x + 1, …, y) of consecutive states of a phase on which σ̄|Q is constant (as in P-N5-ACCEL §0). σ̄_E := σ̄_k for
  k ∈ E (constant on E: Odd vertices outside Q have one successor). D_E := {u ∈ Q : σ̄_E(u) ≠ τ(u)} (= D_k for k ∈ E; P-N5-XEP §3).
  len(E) := (y − x) + [1 if y → y + 1 is an in-phase transition, else 0]: the in-phase transitions whose source lies in E.
- The RESTRICTED GAME G′_E: G's vertices, priorities, owners and Even successor lists; every Odd v ∉ D_E has the single successor τ(v); every
  u ∈ D_E has the two successors τ(u) and σ̄_E(u). So G′_E has exactly |D_E| Odd vertices of out-degree > 1, each of out-degree 2;
  n′ = n, m′ ≤ m, Δ′ ≤ Δ; τ and σ̄_E are positional Odd strategies of G′_E. Objects computed by SPEC on G′_E carry a prime (Ξ′, W′, Iσ′, Iτ′).
- N5^τ ("keep τ on ties"): SPEC N5 with S4b replaced by S4b^τ: if Iτ ≠ ∅ and τ is VALUE-OPTIMAL against σ in S4b's arena H′ (that is,
  V_{σ,τ} on H′ equals S1's valuation on H′ against σ, pointwise), then τ_new := τ; otherwise τ_new := SPEC's S4b output. S1, S2, S3,
  S4a, S4c, S4d, S5 are SPEC's. N5^τ differs from N5 only at an iteration where SPEC's S4b output is a τ_new ≠ τ with the same valuation as
  τ (a tie inside S1's procedure on H′). A phase of N5^τ: a maximal run with (λ, τ) constant, as for N5.

## 1. Lemma RESTRICT_E (PROVED, every game)
Let E be an epoch of a phase of N5 on G, with τ, σ̄_E, D := D_E, and let k ∈ E. Then, at the pair (σ_k, τ):
- (i) Ξ′_k = Ξ_k and W′_k = W_k.
- (ii) Iσ′_k = Iσ_k; SPEC S4a's output on G′_E equals its output on G; S4c's Even switch-all on Iσ is the same on G′_E as on G.
- (iii) Odd's dual valuation of τ is the same on G′_E as on G; hence Iτ′_k = Iτ_k ∩ E(G′_E).
- (iv) if k → k+1 is an in-phase transition of N5 on G and Iτ′_k ≠ ∅, then τ is value-optimal against σ_k in S4b's arena H′ of G′_E.
Proof.
- (i) Every Odd strategy of G′_E is one of G (G′_E's edges are G's). Lemma S (a) on G: Ξ_k ⊴ V_{σ_k,τ″} for every Odd strategy τ″ of G, in
  particular for S1's counterstrategy σ̄′_k on G′_E; so Ξ_k ⊴ V_{σ_k,σ̄′_k} = Ξ′_k. Lemma S (a) on G′_E: Ξ′_k ⊴ V_{σ_k,σ̄_E} = Ξ_k, since σ̄_E is
  an Odd strategy of G′_E and σ̄_k = σ̄_E. The order on valuations is total and antisymmetric on triples (rewards are injective, so the cycle
  node is fixed; distinct path sets have distinct signed weights; then the length), so Ξ′_k = Ξ_k. W: G_τ and (G′_E)_τ are the same
  one-player game (every Odd v keeps τ(v), which is an edge of G′_E), so W′_k = W_k.
- (ii) Iσ (S2) is read from Ξ and Even's successor lists, both unchanged by (i). S4a's arena H (Even v restricted to {σ_k(v)} ∪ Iσ_k(v), every
  Odd v to τ(v)) is the same game for G and G′_E, and S1 on its dual is deterministic, so the outputs are equal. S4c's Even switch-all reads
  Iσ, Ξ and vertex indices only.
- (iii) S1 on G^d for τ runs on the graph in which τ's owner (Odd) keeps only τ and Even keeps all its edges: the same graph for G and G′_E.
  So the valuation is the same, and S2 on G^d gives Iτ′_k = {(v, w) ∈ E(G′_E) : v Odd, w ≠ τ(v), improving} = Iτ_k ∩ E(G′_E).
- (iv) By (iii), Iτ′_k ≠ ∅ gives Iτ_k ≠ ∅, so S4b runs on G at k. The transition is in-phase, so τ_{k+1} = τ; an Odd fallback changes τ (S4c),
  so S4b's output on G at k is τ itself (S4d). S4b's output is S1's counterstrategy to σ_k on the arena H′_G (Odd v restricted to
  {τ(v)} ∪ Iτ_k(v), Even fixed to σ_k); by Lemma S (a) on H′_G, V_{σ_k,τ} ⊴ V_{σ_k,τ″} for every Odd strategy τ″ of H′_G. S4b's arena on G′_E
  restricts Odd v to {τ(v)} ∪ Iτ′_k(v) ⊆ {τ(v)} ∪ Iτ_k(v) ((iii)), with Even fixed to σ_k: every Odd strategy of it is one of H′_G, and τ is
  one of them. So V_{σ_k,τ} is the pointwise minimum over that arena's Odd strategies, which is S1's valuation there (Lemma S (a)). □

## 2. Corollary REPRO (PROVED, every game)
Let E = (x, …, y) be an epoch of a phase P of N5 on G, and y′ := x + len(E) (that is, y + 1 if y → y + 1 is in-phase, else y). Then
N5^τ on G′_E from the start pair (σ_x, τ) passes through the pairs (σ_x, τ), (σ_{x+1}, τ), …, (σ_{y′}, τ), with the same fallback / non-fallback
type at each of its len(E) transitions as N5 on G; and all of these states lie in ONE phase of that N5^τ run (λ′ = λ on them, by RESTRICT_E (i)).
Proof. Induction on k ∈ [x, y′ − 1]; the N5^τ run is at (σ_k, τ). The transition k → k+1 of N5 on G is in-phase, so Iσ_k ≠ ∅ (if Iσ_k = ∅,
σ_new = σ_k, and N5 stops or τ changes); by RESTRICT_E (ii) Iσ′_k = Iσ_k ≠ ∅, so N5^τ does not stop. S4a's output on G′_E is G's (RESTRICT_E
(ii)). S4b^τ returns τ: by SPEC if Iτ′_k = ∅, else by RESTRICT_E (iv) and the definition of S4b^τ. So the fallback fires on G′_E iff S4a's
output is σ_k; on G it fires iff S4a's output is σ_k and S4b's output is τ, and the latter holds (in-phase, as in RESTRICT_E (iv)); so the
fallback fires at k on both or on neither. If it fires, it is Even's on both (Iσ ≠ ∅) and switches the same vertices to the same targets
(RESTRICT_E (ii)). So N5^τ moves to (σ_{k+1}, τ). The cycle-node maps agree at every visited pair (RESTRICT_E (i)), so λ′ is constant and τ is
fixed along the visited states: one phase of the N5^τ run. □

## 3. Corollaries EP-0, EP-k, EP-1
- **EP-0 (PROVED, every game).** If D_E = ∅, then len(E) ≤ n + m.
  Proof. G′_E is a one-player game: every Odd vertex has out-degree 1. So Iτ′ = ∅ at every pair (S2 needs w ≠ τ(v)), S4b^τ = S4b, and N5^τ = N5
  on G′_E; REPRO gives len(E) consecutive N5 iterations on G′_E inside one λ-phase. (Here RESTRICT_E (i) is immediate: σ̄_E = τ, so Ξ_k =
  V_{σ_k,τ} = S1's valuation on G′_E, whose only Odd strategy is τ.) By RESULTS R17 (e), N5's Even step on a one-player game is switch-best,
  and its fallback fires only in the value-flat situation and leaves no improving edge, so at most the last transition is a fallback; by
  R17 (c), a λ-phase has fewer than n + m′ switch-best steps. So len(E) ≤ (n + m′ − 1) + 1 ≤ n + m. □
- **EP-k (PROVED, every game; a REDUCTION).** For every phase P of N5 on any game, the number of in-phase transitions of P is Σ_E len(E) over
  the epochs E of P, and for each epoch, len(E) is at most the number of transitions of one phase of an N5^τ run on G′_E ∈ 𝒞^{|D_E|}O (every
  Odd choice vertex of out-degree 2), started at (σ_x, τ).
  Proof. Every in-phase transition has its source in exactly one epoch, so the sum counts each once. The second part is REPRO. □
- **EP-1 (IMPLICATION, every game).** Premise (Στ): RESULTS R48 (i) (Theorem FB-POLY, in the form f ≤ 1 + (n − 2)(2n − 1) ≤ 2n² used by
  R51 (a)) and RESULTS R50 (h) (Corollary PHASE), together with the per-phase statements they cite (R48: R38, R39, R44, R45, R49; R50: R15,
  R17, R18 (d), R19, R21 (a), R22, R23 (g), R24, R26, R27, R30 (c), R34 (e), (f), R38 (a), and their own landed chains), hold for every phase of
  every N5^τ run on every game of 𝒞^1O from every start pair, with "phase of N5" read as "phase of N5^τ".
  Claim: (Στ) ⇒ for every epoch E with D_E = {u}: len(E) ≤ T*(G′_E), where T*(·) is R51 (a)'s per-phase bound (R50 (h)'s bound with f := 2n²)
  evaluated at G′_E's parameters (n, m′ ≤ m, Δ′ ≤ Δ, d_o = 2); in particular len(E) = O(m·Δ·n¹¹).
  Proof. G′_E ∈ 𝒞^1O with o := u and d_o = deg(u) = 2, n′ = n, m′ ≤ m, Δ′ ≤ Δ. By REPRO, E's len(E) transitions are transitions of one phase of
  an N5^τ run on G′_E from the start pair (σ_x, τ) (start pairs are allowed: R51 (b)). Under (Στ), that phase has f ≤ 2n² in-phase fallbacks
  (R48 (i)) and so at most T*(G′_E) transitions (R50 (h) with f := 2n²; its chain is non-decreasing in f, as R51 (a) uses). R50 (h) gives
  T = O(m′·Δ′·d_o·n⁹·(f + n²)), so with d_o = 2 and f ≤ 2n², len(E) = O(m′·Δ′·n¹¹) ⊆ O(m·Δ·n¹¹). □
- Consequence (PROVED from the above): every count that lives inside one epoch is ≤ len(E): its S4a steps, its fallbacks, its crossings
  (P-N5-XEP §0), and in particular X_SN^pre(E) (P-N5-XEP §4), the residual of Lemma X-EP. So X_SN^pre(E) ≤ n + m if D_E = ∅, and, under
  (Στ), X_SN^pre(E) = O(m·Δ·n¹¹) if |D_E| = 1.

## 4. Not to sign: the (Στ) audit (READING) and Lemma TIE-W (offered)
- What (Στ) asks. A phase of N5^τ and a phase of N5 consist of the same kind of transitions (SPEC's S4a step or Even S4c fallback, τ fixed);
  they differ only in WHEN a phase ends: N5 may leave a phase at a τ-tie of S1's procedure on H′, N5^τ does not. The landed per-phase chain
  (R51 (b); docs/referee/R-N5-START.md with its Addendum 1; REFEREE-2 R2-N5-1O §3) consists of statewise facts, per-transition facts and
  inductions over windows. Such a fact transfers to N5^τ unless its proof uses which optimal counterstrategy S1's procedure returns on H′.
- Audit by text search (READING; not a line-by-line read). `grep -n "S4b\|Iτ\|τ_new\|τ-improving\|Odd's step\|S4b returns\|S4b leaves"` over
  docs/new/P-N5-*.md and docs/si/P-N5-*.md (fixes files and P-N5-DUAL, which is not in the per-phase chain, excluded):
  | packet (RESULTS) | use of S4b / Iτ | transfers to N5^τ? |
  | --- | --- | --- |
  | P-N5-RE, XA, X, U1, U23, OUT, NEB, SCOPE §0, FBPOLY §0, RHO §0, Z, FB, FBW, KW (R19-R26, R29, R31, R38, R39, R42, R45, R48, R50) | definitions: "inside a phase S4b returns τ"; "the fallback fires iff S4a returns σ_k and S4b returns τ_k"; "the fallback is Even's" | yes: each holds verbatim with S4b^τ in an N5^τ phase |
  | P-N5-LP §0 (R27) | "every N5 iteration changes σ or τ" | yes |
  | P-N5-SCOPE §6 CN-LAST (iii) (R38 (f)) | at Iσ_{k+1} = ∅: N5 stops, or S4b changes τ, or S4b returns τ and Odd falls back; so k + 1 ends the phase | yes: the same three cases for S4b^τ |
  | P-N5-RL Lemma BL, Steps 0-1 (R37 (b)); P-N5-NEEDB (F-a) (R49) | "S4b computes τ_new as Odd's optimal counterstrategy to σ_k in H′ … V_{σ_k,τ_new}(o) ⊴ V_{σ_k,x}(o) … so τ_new(o) ≠ e*, and k is not an S4c fallback" | yes: the argument shows that τ is NOT value-optimal in H′, so S4b^τ also moves τ |
  No landed per-phase proof was found that uses the identity of S1's output on H′ beyond its value. Because this is a text search, (Στ) is
  stated as a premise and EP-1 as an implication.
- Lemma TIE-W (PROVED, every game; offered, not needed by §1-§3). Let k → k+1 be in-phase and suppose (u, σ̄_k(u)) ∈ Iτ_k for every u ∈ D_k.
  Then W_k = Ξ_k.
  Proof. Every edge of σ̄_k lies in S4b's arena H′_G (off D_k, σ̄_k = τ; on D_k by hypothesis). S4b's output on G is τ (in-phase, as in
  RESTRICT_E (iv)), so V_{σ_k,τ} ⊴ V_{σ_k,σ̄_k} by Lemma S (a) on H′_G, i.e. W_k ⊴ Ξ_k; and Ξ_k ⊴ W_k by Lemma S (a) on G. □
  So with |D_E| = 1, N5 and N5^τ on G′_E can differ inside E only at states with W_k = Ξ_k. At such a state S4b's arena on G′_E is exactly the
  graph on which S1 computes Ξ′ (u keeps both of its edges, every other Odd vertex is forced), so SPEC's S4b output there is S1's own
  counterstrategy σ̄′ on G′_E; N5 would leave the phase iff σ̄′(u) ≠ τ(u). A proof that this never happens would make EP-1 unconditional.

## 5. DATA (not to sign; experiments/new/box45/eprestrict.py, itcheck.py, outputs in experiments/new/box45/out/)
- eprestrict.py checks per epoch: XI_V (RESTRICT_E (i) at every state of E), OPT_V (RESTRICT_E (iv) at every in-phase transition), REP_V (REPRO:
  N5^τ on G′_E reproduces σ and the fallback flags through y′), EP0_V (an epoch with D = ∅ and y − x ≥ n + m transitions inside it). DIV: epochs in
  which SPEC's OWN S4b on G′_E would move τ before y′ (where N5 and N5^τ on G′_E would differ). Mutation control EPR_MUT=1: u ∈ D keeps only
  τ(u).
| sample | runs | phases | epochs | XI_V / OPT_V / REP_V / EP0_V | DIV | epochs (max y − x, the transitions with both ends in E) by \|D\| |
| --- | --- | --- | --- | --- | --- | --- |
| lib41 (n ≤ 64), S3 + 2 random starts, seed 7 | 1,101 | 5,377 | 8,727 | 0 / 0 / 0 / 0 | 0 | 0: 2,083 (56); 1: 5,016 (91); 2: 277 (27); 3: 212 (17); 4: 174 (8); ≥ 5: 965 (≤ 2) |
| 3,000 random 𝒞^kO (k 2-4, n 5-18, games seed 111), S3 + 4 random, seed 8 | 15,000 | 40,203 | 40,582 | 0 / 0 / 0 / 0 | 0 | 0: 18,487 (3); 1: 12,244 (3); 2: 6,940 (2); 3: 2,484 (1); 4: 427 (0) |
| MUTATION, lib41 S3 only | 367 | 1,737 | 3,511 | XI_V 2,788, REP_V 1,615 (the control bites) | 0 | — |
- DIV = 0 in every sample: premise (Στ) is NEVER EXERCISED. On all these runs N5^τ on G′_E coincides with SPEC's N5 on G′_E inside each epoch.
- itcheck.py (in-phase states with D ≠ ∅ at which some (u, σ̄(u)) ∈ Iτ): lib41 × 3 starts, 65 of 8,608 states (none with |D| = 1); 3,000 random
  × 5 starts, 25 of 671 states, 7 of them with |D| = 1, all 7 with W = Ξ (TIE-W), and at none of them does SPEC's S4b on G′_E move τ.
- Reading of the data: 81% of lib41's epochs have |D| ≤ 1 (7,099 of 8,727), and they include the longest epochs (91 transitions with |D| = 1,
  56 with |D| = 0); epochs with |D| ≥ 2 are short (≤ 27). Every EP bound is far above every observed length.
- Reproduce (from experiments/new/box45): `python3 eprestrict.py 2 7 --list ../box41/lib41.txt`; `python3 eprestrict.py 4 8 --rand 3000 5 18 111`;
  `EPR_MUT=1 python3 eprestrict.py 0 7 --list ../box41/lib41.txt`; `python3 itcheck.py 2 7 --list ../box41/lib41.txt`; `python3 itcheck.py 4 8
  --rand 3000 5 18 111`.

## 6. Not to sign: how this combines, and what it does not give (READING)
- With P-N5-FBK's ALT corollary (signed by both referees, conditional on RESULTS R56 and P-N5-2T): N_ep ≤ 1 + Σ_q (ρ_q + tie_q + nc_q + cyc_q). So if
  every epoch of a phase has |D_E| ≤ 1, the phase has at most N_ep·max_E len(E) = O(m·Δ·n¹¹)·(1 + ρ + ties + non-clean + cycle-node changes)
  transitions (under (Στ) for the |D| = 1 epochs).
- No bound on N_ep (CONJECTURE ρ-POLY stays a conjecture, P-N5-FBRED §5). Nothing for epochs with |D_E| ≥ 2: by EP-k they are phases of N5^τ on
  𝒞^kO (k = |D_E| ≥ 2) with binary Odd choices, the open frontier. Nothing on the number of phases beyond RESULTS R54 (Φ-kO, exponential in
  the number of Odd choice vertices).
- The restriction replaces the lemma-by-lemma port of R19-R34 per epoch with o := u (docs/new/N5-DELTA-box44.md §7): the whole landed 𝒞^1O
  per-phase chain applies at once to an epoch with |D| = 1, with no translation of R_D, (h_D) or "unsplit" to G′_E, because the epoch's
  length bounds every count inside it.
