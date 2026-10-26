# Epochs with |D| ≤ 1 are runs of N5 on a one-Odd-choice game (box 45): restriction to the epoch's Odd choices (RESTRICT_E, REPRO, EP-0, EP-1, EP-k)
L-NEW successor 24 (Opus 5.5), D14 / D18, Lead reading L40; Lead's GO 05:39Z (Lead's stamp), step 2 (b): "X_SN^pre for epochs with
|D| = 1. Port R19-R34 per epoch with o := u." Written 2026-10-26 05:54Z (date -u). Working doc, not a packet, unrefereed.
Labels: PROVED (L-NEW 24, unrefereed) / CONDITIONAL / READING / OPEN / DATA. Not a TARGET.md claim; nothing here bounds N5's running time
on any class beyond 𝒞^1O ∪ 𝒞^1E. G-N5-TIME stays open.

## Summary
- Instead of porting R19-R34 lemma by lemma, the epoch's run is shown to BE a run of a (tie-break variant of) N5 on a smaller game
  G′_E ∈ 𝒞^{|D|}O: every Odd vertex outside D is cut down to its τ-edge, every u ∈ D to its two edges {τ(u), σ̄_E(u)}. N5's Even side
  (Ξ, Iσ, S4a, S4c) is literally the same on G and G′_E at every state of the epoch (Lemma RESTRICT_E), so the landed one-player and
  one-Odd-choice per-phase bounds apply to the epoch as a whole.
- D = ∅: an epoch has at most n + m transitions (Corollary EP-0; PROVED from R17 alone).
- |D| = 1: an epoch has at most T*(n, m, Δ, d_o = 2) + 1 = O(m·Δ·n¹¹) transitions (Corollary EP-1), CONDITIONAL on premise (Στ): the
  per-phase chain behind RESULTS R51 (a) (R48 (i), R50 (h)) holds for N5^τ, the variant of N5 whose S4b keeps τ when τ is already
  value-optimal in its arena. The audit of the landed texts for S4b uses is in §4 (READING). In data, SPEC's own S4b never leaves τ
  inside an epoch on G′_E (DIV = 0), so the variant is never exercised.
- So X_SN^pre(E) ≤ (transitions of E) is polynomial for |D_E| ≤ 1, and so are E's fallbacks, crossings and S4a runs. Per phase, on every
  game (Corollary EP-k): transitions = Σ_E len(E), and len(E) is a per-phase transition count of N5^τ on 𝒞^{|D_E|}O with
  binary Odd choices. The open core shrinks to (1) N_ep (charged to ρ by ALT, P-N5-FBK, in review) and (2) epochs with |D| ≥ 2.

## 0. Setting (every game)
- N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md (with FIX 1-4, Q1-Q4). State k = (σ_k, τ_k); σ̄_k = S1's Odd counterstrategy to σ_k;
  Ξ_k = S1's valuation of σ_k = the play valuation under (σ_k, σ̄_k); W_k := the valuation of σ_k in G_τ (Odd fixed to τ_k); λ := Ξ's
  cycle-node map. PHASE: maximal run with (λ, τ) constant (a joint λ-phase, R38 (a) KEY). Q := Odd vertices of out-degree ≥ 2.
- EPOCH: a maximal run E of consecutive states of a phase with σ̄|Q constant (P-N5-ACCEL §0); σ̄_E := σ̄ on E (constant on E: Odd
  vertices outside Q have one successor). D_E := {u ∈ Q : σ̄_E(u) ≠ τ(u)} (D-EPOCH, P-N5-XEP §3). len(E) := the number of transitions
  with both ends in E, plus 1 if the transition leaving E stays in the phase.
- G′_E: the game with G's vertices, priorities, owners and Even successor lists; every Odd v ∉ D_E has the single successor τ(v), and
  every u ∈ D_E has the successors {τ(u), σ̄_E(u)} (two, since u ∈ D_E). So G′_E ∈ 𝒞^{|D_E|}O, every Odd choice vertex has out-degree 2,
  n′ = n, m′ ≤ m, Δ′ ≤ Δ. σ̄_E and τ are positional Odd strategies of G′_E.
- N5^τ: N5 with S4b replaced by S4b^τ: if Iτ ≠ ∅ and τ is VALUE-OPTIMAL against σ in S4b's arena H′ (V_{σ,τ} = the valuation S1
  computes on H′ against σ, pointwise), then τ_new := τ; otherwise τ_new := SPEC's S4b output. Everything else (S1, S2, S3, S4a, S4c, S5)
  is SPEC's. N5 and N5^τ differ only where SPEC's S4b would replace τ by a value-equal τ_new (a tie in S1's procedure on H′).

## 1. Lemma RESTRICT_E (PROVED, every game)
Let E be an epoch of a phase of N5 on G, with τ, σ̄_E, D := D_E, and let k ∈ E. Write Ξ′, W′, Iσ′, Iτ′, … for the SPEC objects computed
on G′_E at the same pair (σ_k, τ).
- (i) Ξ′_k = Ξ_k and W′_k = W_k.
- (ii) Iσ′_k = Iσ_k; SPEC S4a's output at (σ_k, τ) on G′_E equals its output on G; the Even part of S4c (the switch-all on Iσ) is the same.
- (iii) Odd's dual valuation of τ is the same on G′_E as on G, so Iτ′_k = Iτ_k ∩ E(G′_E).
- (iv) If k → k+1 is an in-phase transition of N5 on G (τ_{k+1} = τ) and Iτ′_k ≠ ∅, then τ is value-optimal against σ_k in S4b's arena
  H′ of G′_E.
Proof.
- (i) By RESULTS R18 (d) Lemma S (a) (S1's valuation is the pointwise minimum of V_{σ,τ′} over Odd's strategies τ′; game-general, both
  referees, R56 landing note N-FBRED-3): on G, Ξ_k ⊴ V_{σ_k,τ′} for every Odd strategy τ′ of G, in particular for S1's counterstrategy σ̄′
  on G′_E (G′_E's Odd edges are G's), so Ξ_k ⊴ V_{σ_k,σ̄′} = Ξ′_k. On G′_E, Ξ′_k ⊴ V_{σ_k,σ̄_E} = Ξ_k (σ̄_E is a strategy of G′_E, and σ̄_k =
  σ̄_E on E). The order on valuations is total and antisymmetric on triples (injective rewards fix c, distinct sets have distinct signed
  weights, then ℓ), so Ξ′_k = Ξ_k. W: G_τ and (G′_E)_τ are the same one-player game (each Odd v keeps τ(v) ∈ E(G′_E)).
- (ii) Iσ (S2) is read from Ξ and Even's successor lists, both unchanged ((i)). S4a's arena H has Even v restricted to A(v) = {σ(v)} ∪ Iσ(v)
  and every Odd v restricted to τ(v): the same game on G and on G′_E, and S1 on its dual is deterministic, so the outputs are equal. S4c's
  Even switch-all reads Iσ, Ξ and indices only.
- (iii) S1 on G^d for τ works on the graph in which τ's owner (Odd) keeps only τ and Even keeps all its edges: the same graph for G and G′_E.
  S2 on G^d then gives Iτ′ = the τ-improving Odd edges of G′_E = Iτ ∩ E(G′_E).
- (iv) Iτ′_k ≠ ∅ gives Iτ_k ≠ ∅ ((iii)), so S4b runs on G at k. In-phase, τ_{k+1} = τ; an Odd fallback changes τ (S4c), so S4b's output on G
  at k is τ_new = τ (S4d). S4b's output is S1's
  counterstrategy to σ_k on H′_G, so by Lemma S (a) on the game H′_G: V_{σ_k,τ} ⊴ V_{σ_k,τ″} for every Odd strategy τ″ of H′_G. By (iii),
  H′ of G′_E (Odd v restricted to {τ(v)} ∪ Iτ′_k(v), Even fixed to σ_k) is a sub-arena of H′_G containing τ; every Odd strategy of it is one of
  H′_G, so τ attains the pointwise minimum there too, which is S1's valuation on it (Lemma S (a) on H′ of G′_E). □

## 2. Corollary REPRO (PROVED, every game)
Let E = (x, …, y) be an epoch of a phase P of N5 on G, and y′ := y + 1 if y → y + 1 stays in P, else y′ := y. Then N5^τ on G′_E from the
start pair (σ_x, τ) visits σ_x, σ_{x+1}, …, σ_{y′} with τ constant, with the same fallback flags; all these states lie in one phase of
that N5^τ run (λ′ = λ by RESTRICT_E (i)).
Proof. Induction on k ∈ [x, y′ − 1]. At k the run on G′_E is at (σ_k, τ). In-phase transitions of N5 on G have Iσ_k ≠ ∅ (if Iσ_k = ∅,
σ_new = σ_k, and N5 stops or τ changes), so N5^τ does not stop. S4a's output is G's (RESTRICT_E (ii)). S4b^τ returns τ: if Iτ′_k = ∅ by
SPEC, else by RESTRICT_E (iv) and the definition of S4b^τ. The fallback fires on G′_E iff S4a's output is σ_k (τ_new = τ), which is G's
condition at an in-phase transition (G's S4b returned τ), and its Even switch-all is G's (RESTRICT_E (ii)); an Odd fallback needs
Iσ = ∅. So the next state is (σ_{k+1}, τ). □
- Start-freeness: the landed per-phase results are start-free (RESULTS R51 (b); docs/referee/R-N5-START.md), so the arbitrary start pair
  (σ_x, τ) on G′_E is allowed.

## 3. Corollaries EP-0, EP-1, EP-k
- **EP-0 (PROVED, every game).** If D_E = ∅, then len(E) ≤ n + m.
  Proof. G′_E is a one-player game (every Odd vertex has out-degree 1), so Iτ′ = ∅ at every state and N5^τ = N5 on it. (RESTRICT_E (i)
  needs no Lemma S here: σ̄_E = τ, so Ξ_k = V_{σ_k,τ} = S1's valuation on G′_E.) By REPRO, E's transitions are consecutive N5 iterations on
  G′_E inside one λ-phase. RESULTS R17 (c), (e): on a one-player game a λ-phase has fewer than n + m′ switch-best steps, and N5's fallback
  fires only in the value-flat situation and leaves no improving edge (N5 stops next). So len(E) ≤ (n + m′ − 1) + 1 ≤ n + m. □
- **EP-1 (PROVED, CONDITIONAL on (Στ); every game).** If D_E = {u}, then len(E) ≤ T*(n, m, Δ, 2), where T* is RESULTS R51 (a)'s per-phase
  bound for 𝒞^1O (R50 (h) with f := 2n², R48 (i)) evaluated at d_o = 2; so len(E) = O(m·Δ·n¹¹).
  Premise (Στ): RESULTS R48 (i) and R50 (h) (with everything they cite) hold for the phases of N5^τ, not only of N5.
  Proof. G′_E ∈ 𝒞^1O with o := u, d_o = 2, n′ = n, m′ ≤ m, Δ′ ≤ Δ. By REPRO, E's len(E) transitions are transitions of one phase of an
  N5^τ run on G′_E from the start pair (σ_x, τ). Under (Στ), that phase has f ≤ 2n² fallbacks (R48 (i)) and at most T* transitions
  (R50 (h)). □
- **EP-k (PROVED, every game; a REDUCTION).** For every phase P of N5 on any game: transitions of P = Σ_E len(E) (each in-phase transition is counted once, by the epoch of its
  source), and for
  each epoch, len(E) ≤ the length of one phase of N5^τ on G′_E ∈ 𝒞^{|D_E|}O (all Odd choice vertices of out-degree 2), from the start pair
  (σ_x, τ). With EP-0, EP-1 and ALT (P-N5-FBK §4, in review; N_ep ≤ 1 + Σ_q (ρ_q + tie_q + nc_q + cyc_q)): if every epoch of P has |D_E| ≤ 1,
  then P has O(m·Δ·n¹¹)·(1 + ρ + ties + non-clean + cycle-node changes) transitions (under (Στ) for the |D| = 1 epochs).
- **Consequence for X_SN^pre (the Lead's item).** X_SN^pre(E) ≤ len(E). So for |D_E| = 0 it is ≤ n + m (PROVED), and for |D_E| = 1 it is
  O(m·Δ·n¹¹) (CONDITIONAL on (Στ)); sharper (also under (Στ)), via RESULTS R52 (a), (b) on G′_E: crossings ≤ n·(f + X_SN) + n − 1 = O(n⁶) per phase, read on G′_E,
  where R_D on G′_E is the set whose (σ, τ)-play meets u (D′ = {u} on E). The full epoch length is the stronger statement and needs no
  crossing-by-crossing translation.

## 4. Premise (Στ): what it needs, and the audit (READING, for the referees)
- What differs. A phase of N5^τ is a run with (λ, τ) constant whose transitions are SPEC's S4a / Even S4c outputs, at states where τ is
  value-optimal in S4b's arena (or Iτ = ∅). A phase of N5 is the same with "S1's procedure on H′ returns τ itself". The per-phase
  statements of R19-R50 are statewise facts, per-transition facts and inductions over windows (R51 (b); R-N5-START + Addendum 1; REFEREE-2
  R2-N5-1O §3 for R34 (b)-(f)). A per-transition fact transfers to N5^τ unless its proof uses S4b's procedure-level tie-break.
- Audit by text search (2026-10-26 05:5xZ; `grep -n "S4b\|Iτ\|τ_new\|τ-improving\|Odd's step\|S4b returns\|S4b leaves"` over the landed
  packets docs/new/P-N5-*.md and docs/si/P-N5-*.md, fixes files excluded; P-N5-DUAL (R54, mirror, not in the per-phase chain) excluded):
  | packet (RESULTS) | use of S4b / Iτ | transfers to N5^τ? |
  | --- | --- | --- |
  | P-N5-RE, XA, X, U1, U23, OUT, NEB, SCOPE §0, FBPOLY §0, RHO §0, Z, FB, FBW, KW (R19-R26, R29, R31, R38, R39, R42, R45, R48, R50) | definitions: "inside a phase S4b returns τ", "the fallback fires iff S4a returns σ_k and S4b returns τ_k", "the fallback is Even's" | yes: read with S4b^τ, each holds verbatim in an N5^τ phase |
  | P-N5-LP §0 (R27) | "every N5 iteration changes σ or τ (if S4a and S4b change nothing, the S4c fallback switches)" | yes (same in N5^τ) |
  | P-N5-SCOPE §6 CN-LAST (iii) (R38 (f)) | at Iσ_{k+1} = ∅: N5 stops, or S4b changes τ, or S4b returns τ and Odd falls back; so k + 1 ends the phase | yes: the same three cases for S4b^τ |
  | P-N5-RL Lemma BL Step 0-1 (R37 (b)); P-N5-NEEDB (F-a) (R49) | "S4b computes τ_new as Odd's optimal counterstrategy to σ_k in H′ … V_{σ_k,τ_new}(o) ⊴ V_{σ_k,x}(o) … so τ_new(o) ≠ e*, and k is not an S4c fallback" | yes: the argument shows τ is NOT value-optimal in H′, so S4b^τ also moves τ |
  No landed per-phase proof found that uses which optimal counterstrategy S1's procedure returns on H′. The audit is a text search, not
  a line-by-line read of every proof; (Στ) is therefore stated as a premise, not as PROVED.
- DATA: (Στ) is never exercised: in every epoch of every sample, SPEC's own S4b on G′_E returns τ (DIV = 0, §5), so on these runs N5^τ on
  G′_E is SPEC's N5 on G′_E. A proof that DIV = 0 always would remove (Στ); I do not have one (a tie at u between τ(u) and σ̄_E(u) in S1's
  procedure on H′ is not excluded; it forces W_k = Ξ_k at that state, since then σ̄_E is a strategy of H′_G, which is all I can derive).
- Lemma TIE-W (PROVED, every game; added 06:10Z by date -u). Let k → k+1 be in-phase, and suppose (u, σ̄_k(u)) ∈ Iτ_k for every u ∈ D_k
  (for |D_k| = 1: Iτ′_k ≠ ∅ on G′_E). Then W_k = Ξ_k.
  Proof. Every edge of σ̄_k lies in S4b's arena H′_G (off D_k, σ̄_k = τ; on D_k, by hypothesis). S4b's output on G is τ (in-phase, as in
  RESTRICT_E (iv)), an optimal counterstrategy on H′_G (Lemma S (a)), so W_k = V_{σ_k,τ} ⊴ V_{σ_k,σ̄_k} = Ξ_k; and Ξ_k ⊴ W_k (Lemma S (a) on G). □
  So on G′_E with |D_E| = 1, SPEC's S4b can differ from S4b^τ only at states with W_k = Ξ_k. On G′_E, S4b's arena at such a state is
  exactly the graph on which S1 computes Ξ′ (u keeps both edges, every other Odd vertex is forced), so SPEC's S4b output is S1's own
  counterstrategy σ̄′ on G′_E; DIV means σ̄′(u) = σ̄_E(u) there. Not excluded by anything I can prove.
- DATA (experiments/new/box45/itcheck.py; out/itcheck_*.txt): in-phase states with D ≠ ∅ and some (u, σ̄(u)) ∈ Iτ: lib41 × 3 starts 65 of
  8,608 (none with |D| = 1); 3,000 random × 5 starts 25 of 671, 7 with |D| = 1, all 7 with W = Ξ (TIE-W), and at none of them does SPEC's
  S4b on G′_E move τ (DIV = 0).

## 5. DATA (experiments/new/box45/eprestrict.py; DATA, not proof)
Checks per epoch: XI_V (RESTRICT_E (i) at every state), OPT_V (RESTRICT_E (iv) at every in-phase transition), REP_V (REPRO: N5^τ on G′_E
reproduces σ and the fallback flags, through y′), EP0_V (an epoch with D = ∅ and len ≥ n + m: stricter than EP-0). Context: DIV (epochs
where SPEC's own S4b on G′_E would move τ), epochs and max len by |D|, G1PH (length of the whole N5^τ phase on G′_E for |D| = 1).
Mutation control EPR_MUT=1: u ∈ D keeps only τ(u) (σ̄_E(u) dropped).
| sample | runs | phases | epochs | XI_V / OPT_V / REP_V / EP0_V | DIV | epochs (max len) by |D| | G1PH (n) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lib41 (n ≤ 64), S3 + 2 random starts, seed 7 | 1,101 | 5,377 | 8,727 | 0 / 0 / 0 / 0 | 0 | 0: 2,083 (56); 1: 5,016 (91); 2: 277 (27); 3: 212 (17); 4: 174 (8); ≥ 5: 965 (≤ 2) | 103 (64) |
| 3,000 random 𝒞^kO (k 2-4, n 5-18, games seed 111), S3 + 4 random, seed 8 | 15,000 | 40,203 | 40,582 | 0 / 0 / 0 / 0 | 0 | 0: 18,487 (3); 1: 12,244 (3); 2: 6,940 (2); 3: 2,484 (1); 4: 427 (0) | 3 (18) |
| MUTATION, lib41 S3 only | 367 | 1,737 | 3,511 | XI_V 2,788, REP_V 1,615 (bite) | 0 | — | — |
Reading (DATA): 81% of lib41's epochs have |D| ≤ 1 (7,099 of 8,727), and they hold the longest epochs (91 and 56 transitions); epochs with
|D| ≥ 2 are short (≤ 27). The restriction reproduces every epoch exactly; the mutation shows the check discriminates.

## 6. What this does not give
- No bound on N_ep (the number of epochs in a phase). ALT (P-N5-FBK §4, in review) charges it to ρ, ties, non-clean alternations and
  cycle-node changes; ρ-POLY is a CONJECTURE (P-N5-FBRED §5).
- Nothing for epochs with |D| ≥ 2: they are phases of N5^τ on 𝒞^kO (k = |D| ≥ 2, binary Odd choices), the open frontier.
- EP-1 is CONDITIONAL on (Στ). EP-0 and RESTRICT_E, REPRO, EP-k are not.
- Phases: Φ-kO (R54) gives ≤ n(n − 1) + ∏ deg(o_i) phases, exponential in the number of Odd choice vertices; not addressed here.

## 7. DIV occurs: premise (Στ) is exercised on some epochs (DATA; added 06:37Z by date -u, after packet P-N5-EPR froze at 08abd9cb)
- experiments/new/box45/divsearch.py searches random 𝒞^kO games (k 2-3, n 4-16) from random start pairs for in-phase tie states (D = {u},
  (u, σ̄(u)) ∈ Iτ, so W = Ξ by TIE-W) and for DIV (SPEC's own S4b on G′_E moves τ there). Distinct game seeds 1-4, 11-15 (154,000 games,
  5 random start pairs each; outputs out/divsearch_*.txt, out/divsearch2_*.txt, the latter re-running seeds 11, 13, 14 with the cycle-node
  counter and adding seed 15): 190 tie states, DIV 2 (seed 13: k 2, n 6-14; seed 15: k 2, n 8-16).
- Instance experiments/new/box45/instances/div_n8.pg (n 8, Q = {3, 7}; sha1 4ed57ef2c1c92ee526ccd2683ae7c28b1caf5bfa) with the start pair
  instances/div_n8.start (sha1 604a98e0…; the tie state itself, allowed since everything is start-free). N5 on G: the first transition is in-phase
  (S4a, σ(6): 7 → 0), D = {3}, Ξ(3) = (3, ∅, 0) (u is its own cycle node), W = Ξ; Iτ = {(3, 0), (3, 7)}; on G, S4b keeps τ(3) = 5. On G′_E
  (3 keeps {5, 7}), Ξ′ = Ξ and S1's counterstrategy picks 7 at 3, so SPEC's S4b moves τ(3): 5 → 7 and SPEC N5 on G′_E LEAVES the phase, while
  N5^τ keeps τ (divshow.py, out/divshow_n8.txt). Engine: experiments/new/box21/n5x.py (SPEC step); Oink not built, nothing here needs a
  solver (one transition is compared).
- So the variant N5^τ in REPRO is NEEDED (SPEC N5 on G′_E does not reproduce every epoch), and EP-1 genuinely rests on (Στ) for such epochs.
  The packet's statements are unaffected (EP-1 is an implication; §5's "DIV = 0" is about its listed samples, which is still true), but
  its sentence "premise (Στ) is NEVER EXERCISED" holds only for those samples. For the fixes file.
- Observation (CONJECTURE TIE-CYC, DATA only): at every tie state where it was recorded (148 of 148, seeds 11, 13, 14, 15; both DIV
  states included), u is its own honest cycle node (λ(u) = u, Ξ(u) =
  (u, ∅, 0)). Not proved; I see no reason in the definitions (Ξ(x) = Ξ(τ u) with U(x) ◁ U(τ u) is not contradictory when u is off its cycle).

## 8. N5^τ on 𝒞^1O: the R48 (i) bound in data (DATA for (Στ); experiments/new/box45/n5tau.py; added 06:44Z by date -u)
- n5tau.py runs N5^τ itself (not N5) on 𝒞^1O games and checks R48 (i) (f ≤ 1 + (n − 2)(2n − 1)) on every N5^τ phase; TIEKEEP counts the
  iterations where N5^τ keeps τ although SPEC's S4b would move it (so the N5^τ run differs from the N5 run from there on).
| sample | runs | phases | TIEKEEP (phases with one) | R48 (i) violations | max f per phase | max phase length (n) |
| --- | --- | --- | --- | --- | --- | --- |
| REFEREE-2's 503 𝒞^1O files (R2-N5-KW/files.lst), S3 + 2 random, seed 7 | 1,509 | 6,256 | 88 (46) | 0 | 37 | 112 (48) |
| lib41's 𝒞^1O games (253), S3 + 2 random, seed 7 | 759 | 3,164 | 29 (16) | 0 | 33 | 112 (48) |
| 5,000 random 𝒞^1O, n 5-20, games seed 22, S3 + 4 random, seed 9 | 25,000 | 61,452 | 613 (560) | 0 | 1 | 5 (15) |
- Reading (DATA): N5^τ and N5 do differ on 𝒞^1O runs (the variant is exercised), and the N5^τ phases stay within R48 (i), with the same
  maxima as N5 in R51's data (f 37, phase length 112). Data for (Στ), not a proof of it.

## 9. (Στ), line by line: every use of S4b / Iτ / τ_new / "τ unchanged" in the R48 (i) and R50 (h) chains (Lead 06:48Z; written 06:56Z by date -u)
### 9.1 Lemma Στ-STEP (PROVED, every game): what N5 and N5^τ share
For every game and every state (σ, τ):
- (a) N5 and N5^τ compute the same Ξ, W, Iσ, Iτ, the same S4a output σ_a, and the same Even and Odd S4c switch-alls (S4b^τ only changes S4b).
- (b) If N5's transition from (σ, τ) keeps τ, N5^τ's transition from (σ, τ) is identical. (N5 keeps τ ⇒ Iτ = ∅, or S4b's output is τ, which is
  then value-optimal in H′ (Lemma S (a)), so S4b^τ returns τ too; the fallback condition "σ_a = σ and τ_new = τ" is then the same.)
- (c) If N5^τ's transition from (σ, τ) keeps τ, then Iσ ≠ ∅ and σ_new = Σ(σ, τ) := σ_a if σ_a ≠ σ, else Even's S4c switch-all on Iσ. (If
  Iσ = ∅, then σ_a = σ, and N5^τ either stops (Iτ = ∅), or S4b^τ moves τ, or S4b^τ keeps τ and the fallback is Odd's, which moves τ.)
  The same holds for N5 (with "S4b's output is τ").
- (d) Every N5^τ iteration applies a non-empty switch of improving edges to σ or to τ (S4a's output differs from σ only on Iσ edges; S4b^τ moves
  τ only to SPEC's S4b output; if neither moves, the fallback switches Iσ ∪ Iτ ≠ ∅). This is the hypothesis of R15 (c), (d)'s proofs
  (docs/new/G-N5-TERM-reading.md: "every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even or to Odd"; Iσ, Ξσ are functions of σ alone and
  Iτ, Ξτ of τ alone), so R15 (c), (d) hold for N5^τ runs.
So the in-phase transitions of both algorithms are Σ-transitions (σ, τ) → (Σ(σ, τ), τ) at states with Iσ ≠ ∅ where τ is value-optimal in
S4b's arena (or Iτ = ∅): a τ-STABLE state. N5's in-phase states are τ-stable with one more property: S1's procedure on H′ returns τ itself.
A per-phase proof transfers to N5^τ unless it uses that extra property.
### 9.2 The chain and the files read
- Citation closure of R48 and R50 in docs/RESULTS.md (entries R15-R50 cited by them, transitively): R15, R17, R18, R19-R34, R38, R39, R42,
  R44, R45, R47 (cited only in R50's not-signed reading), R48, R50.
- Files (the "Object" / packet / fixes / proof-doc files named in those entries): G-N5-TERM-reading; N5-phase-bound-box10; N5-time-box21,
  N5-1Oacyc-box24; P-N5-RE-box26, N5-xing-box27; P-N5-XA-box27 + fixes-box28; P-N5-X-box28 + fixes-box29, docs/agents/R19-note-X1; P-N5-NH-box30
  + fixes; docs/si/P-N5-Z-box5 + fixes; P-N5-U1-box31 + fixes; docs/si/P-N5-FB-box7 + fixes, fixes2; P-N5-U23-box31 + fixes; P-N5-LP-box32 +
  fixes, P-N5-SO-box32 + fixes, N5-L-box32, docs/si/N5-C-box8; P-N5-OE-box32 + fixes; docs/si/P-N5-CLS-box8 + fixes, fixes2; P-N5-SN-box33 +
  fixes; docs/si/P-N5-FBW-box9 + fixes; P-N5-FRZ-box34 + fixes, fixes2; P-N5-L2-box34 + fixes, fixes2; P-N5-TOG-box35 + fixes, fixes2;
  P-N5-SCOPE-box36 + fixes; P-N5-OUT-box37 + fixes; P-N5-NEB-box38 + fixes; N5-RW-box39, P-N5-PFZ-box39, P-N5-PFZ-ext-box39, P-N5-PFZ-fixes-box39;
  P-N5-RHO-box40 + fixes; P-N5-FBPOLY-box41 + fixes, docs/red/R72-fx-fbpoly-k; docs/si/P-N5-KW-box15 + addendum + fixes, N5-KW-box42,
  docs/si/N5-KW-box15 (all under docs/new/ unless named). 66 files.
- Search: `grep -n` for S4b, Iτ, I_τ, τ_new, Odd's step, Odd step, Odd fall, Odd's fallback, "optimal counterstrategy to σ", "τ unchanged",
  "fallback fires", "fallback happens", "S4c fires", "τ is unchanged", "τ changes", "Odd moves", τ_{k+1} (108 hits), and a second pass for
  Odd's move, τ moves, Odd's arena, H′, τ-step, τ′, Odd switches, Odd improves, τ-optimal (no further use of S4b's output: H′ in P-N5-FB is a
  functional graph, τ′ elsewhere is a quantifier in Lemma S (a)). Every hit was read in context.
### 9.3 Every use, classified
Kinds: DEF = a restatement of SPEC (true for N5^τ with S4b^τ, by 9.1); FIX = "in a phase τ_{k+1} = τ_k, so the transition is S4a or an Even
fallback" (9.1 (c)); END = "Iσ = ∅ ⇒ τ changes or N5 stops" (9.1 (c)); VAL = a value statement about S4b's output (holds for N5^τ: τ is moved
by S4b^τ whenever it is not value-optimal); R15 = a use of R15 (c), (d) (9.1 (d)); HYP = "τ_{k+1} = τ_k" as a hypothesis.
| RESULTS | file: line(s) | the use | kind | holds for N5^τ? |
| --- | --- | --- | --- | --- |
| R15 | G-N5-TERM-reading: 83, 85, 91 | Iσ / Iτ are functions of σ / τ alone; flat iterations ≤ 4n(n − 1) | DEF, R15 | yes (9.1 (a), (d)) |
| R17 | N5-phase-bound-box10: 86 | "N5's fallback fires only when the arena optimum returns σ unchanged although Iσ ≠ ∅" (one-player games) | DEF | yes (one-player: Iτ = ∅, N5^τ = N5) |
| R18 | N5-time-box21: 77, 99-103, 107, 119 | Odd's step minimises V_{σ_k,·} over its arena; Theorem B (a) "τ_{k+1} = τ_k ⇒ σ_{k+1} = F_{τ_k}(σ_k)"; Iσ = ∅ ⇒ τ changes; Iτ_0 = ∅ ⇒ τ never changes; fallback fires only when the arena optimum is σ_k | DEF, FIX, END | yes |
| R18 | N5-1Oacyc-box24: 99-103 | "(o, a) ∈ Iτ … S4b runs … value at o under τ′ ⊴ o ⊕ Ξ(a) ◁ o ⊕ Ξ(b). Hence τ′(o) ≠ b, and S4b changes τ" | VAL (τ strictly not optimal) | yes: S4b^τ = SPEC there |
| R18 | N5-1Oacyc-box24: 119-122 | at a pure transition S4b returned τ; S4c fires iff S4a returns σ_k; Iσ_k ≠ ∅ | FIX | yes (9.1 (b), (c)) |
| R19 | P-N5-RE-box26: 12-13, 51, 58; N5-xing-box27: 60 | SPEC restated; hypotheses τ_{k+1} = τ_k; fallback only when S4a's optimum is σ | DEF, HYP | yes |
| R20 | P-N5-XA-box27: 13-14; XA-fixes-box28: 49, 140-143 | SPEC restated; l. 49 describes an OPEN configuration (no proof step); R15 (d) for value-preserving transitions | DEF, R15 | yes |
| R21 | P-N5-X-box28: 13-14, 21, 64, 76, 170 | SPEC; R15 (d); "S4c step: Even's, since τ is fixed (S4c switches Odd only if Iσ_k = ∅, and then τ changes)"; hypothesis | DEF, R15, FIX, HYP | yes |
| R22 | P-N5-NH-box30: 25 | R15 (a), (d) | R15 | yes |
| R23 | si/P-N5-Z-box5: 25, 38, 48, 57, 171 | "S4c happens iff S4a returns σ_k and S4b returns τ_k"; (F0) with τ_{k+1} = τ_k; FBL-N (i); WM: "τ_{k+1} = τ_k, σ_{k+1} is S4a's choice" | DEF, HYP, FIX | yes (in an N5^τ phase both conditions of the fallback hold) |
| R24 | P-N5-U1-box31: 13, 16; U1-fixes: 171 | "inside a phase S4b returns τ"; the fallback is Even's (FIX 3) | DEF, FIX | yes |
| R25 | si/P-N5-FB-box7: 20-21, 45, 149; FB-fixes2: 25, 27, 32 | SPEC; Odd's fallback changes τ; FIX 3; WM | DEF, FIX, END | yes |
| R26 | P-N5-U23-box31: 22 | "every non-fallback transition is an S4a step: S4b returns τ" | FIX | yes |
| R27 | P-N5-LP-box32: 14, 33-34 | "every N5 iteration changes σ or τ" | DEF | yes (9.1 (d)) |
| R28 | P-N5-OE-box32 (+ fixes) | no hit | — | yes (no use) |
| R29 | si/P-N5-CLS-box8: 17; CLS-fixes: 10-11; fixes2: 10 | "no gate ⇒ σ unchanged ⇒ τ changes ⇒ the phase is left" | END | yes |
| R30 | P-N5-SN-box33: 35; SN-fixes: 12, 19 | WM uses only τ_{k+1} = τ_k and the S4a optimum | HYP | yes |
| R31 | si/P-N5-FBW-box9: 17-18 | "an S4c fallback fires exactly when S4a returns σ_k and S4b returns τ_k" | DEF | yes |
| R32 | P-N5-FRZ-box34: 48 | "an in-phase S4c fallback happens only when S4a returned σ_k" | FIX | yes |
| R33 | P-N5-L2-box34 (+ fixes, fixes2) | no hit | — | yes (no use) |
| R34 | P-N5-TOG-box35: 18, 104 | at an Odd fallback σ is unchanged; "τ is constant in a phase, so it is not an Odd fallback" | DEF, FIX | yes |
| R38 | P-N5-SCOPE-box36: 25-28, 91, 204-207 | SPEC; CN-LAST (iii): at Iσ_{k+1} = ∅ N5 stops, or S4b moves τ, or S4b returns τ and Odd falls back | DEF, END | yes (the same three cases for S4b^τ) |
| R39 | P-N5-OUT-box37: 43-46, 82, 84, 110; OUT-fixes: 24 | SPEC; FBL-N, ACT premise rows ("τ unchanged"); the fallback is Even's | DEF, FIX | yes |
| R42 | P-N5-NEB-box38: 34-36, 89, 91; NEB-fixes: 32 | as R39 | DEF, FIX | yes |
| R44 | P-N5-PFZ-box39: 33, 67-68 (ext, fixes: no hit) | SPEC; premise rows | DEF | yes |
| R45 | P-N5-RHO-box40: 40-41 | "every transition has τ unchanged, so it is an S4a step … or an Even S4c fallback" | FIX | yes |
| R48 | P-N5-FBPOLY-box41: 34-35, 46, 68, 248 | SPEC; in-phase ⇒ S4a or Even fallback; an Odd fallback ends the phase | DEF, FIX | yes |
| R50 | si/P-N5-KW-box15: 48 | "if S4a leaves σ unchanged and S4b leaves τ unchanged, the S4c fallback is Even's" | FIX | yes |
| R47 | not needed: cited only in R50's not-signed reading (phase count across phases) | — | — | — |
### 9.4 Conclusion (lane READING, for the referees)
- No step in the R48 (i) / R50 (h) chain uses which optimal counterstrategy S1's procedure returns on S4b's arena. Every use of S4b is of kind
  DEF, FIX, END, HYP, R15 or VAL, and each holds for N5^τ by Στ-STEP (9.1). The other per-phase steps use N5 only through the state
  (Ξ, W, Iσ, σ̄, …, all functions of (σ, τ)) and through Σ-transitions with τ fixed, which N5^τ shares (9.1 (a), (c)).
- So (Στ) holds, as far as this enumeration reaches: EP-1 becomes a lane result (PROVED by the lane, unrefereed), with the audit as its
  premise check. What a referee should verify: (1) the file list (9.2) is the whole chain (proofs may sit in a doc a packet cites but RESULTS
  does not name); (2) no proof uses S4b's output implicitly (for instance "the phase ended, so S1's procedure returned some τ′ ≠ τ").
- Data for (Στ): §8 (N5^τ on 𝒞^1O: R48 (i) holds per N5^τ phase; the variant is exercised, TIEKEEP 88 / 29 / 613). L-COMP is building N5^τ
  as an engine variant to re-check R48 (i) and R50 (h) (Lead 06:48Z).
- TIE-CYC stays a CONJECTURE (DATA: 148 of 148 recorded tie states have λ(u) = u); §7.
