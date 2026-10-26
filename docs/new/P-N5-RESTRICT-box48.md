# Packet P-N5-RESTRICT (box 48): N5 on any in-phase run is N5^τ on every Odd cut of the game that keeps τ and the run's best replies (Lemma RESTRICT_H, Corollary REPRO_H); instances: the epoch game G′_E (R64), G^u (R68 (f)), the frozen-side game G^{u|J}, and the used-edge game G^P of a whole phase — every game
L-NEW successor 28 (Opus 5.5), D14 / D18, Lead reading L40; Lead's GO of 15:38Z (Lead's stamp): "Yes, freeze RESTRICT_H as a packet now. Do not
wait for a QP count." Written 2026-10-26 15:39Z onward (date -u). FROZEN at push: later text goes into a fixes file.
Source: docs/new/N5-NCONF-box48.md §10 (l-new 7b5876d8; this packet governs) and §9 (L-NEW successor 27, the conjecture RESTRICT_{u|J}).
Tool: experiments/new/box48/phrestrict.py (sha1 b4624a454e7cee776cbd4aa3bc70aa9d75cb19e8); for §9's data fsrestrict.py (sha1
2f09852d030481e5e13542fb49f4e2cae4e7bb1a).
Labels: PROVED (L-NEW 28, unrefereed) / OPEN / DATA / READING. Not a TARGET.md claim; no running-time bound; G-N5-TIME stays open.
What this is and is not, plainly:
- It is a GENERALISATION of the signed proof of RESULTS R64 (a), (b): the same proof, item by item, with the restricted game G′_E replaced by any
  game H that keeps G's Even edges and a subset of each Odd vertex's edges, as long as H contains τ and every Odd best reply σ̄_k of the run.
- It bounds nothing. It says that a run of N5 inside one phase depends only on the Odd edges the run uses. The number of Odd vertices that use
  two or more edges in one phase (QP below) is OPEN.

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Lemma RESTRICT_H: RESULTS R64 (a) (i)-(iv) on every H-admissible run | PROVED (to sign) |
| §1 | Corollary REPRO_H: R64 (b) (with EPR-1) on every H-admissible run | PROVED (to sign) |
| §2 | Instances: G′_E (= R64), G^u (= R68 (f)), G^{u|J} (frozen-side u-stretch), G^P (whole phase) | PROVED (to sign; each is admissibility by definition) |
| §3 | data | DATA (not to sign) |
| §4 | what it gives; QP | READING / OPEN (not to sign) |
- Premises (LANDED):
  - SPEC S1-S5 of docs/new/N5-ssi-global.md (FIX 1-4, Q1-Q4), as in RESULTS R64. Standing premise 1E-N3 (RESULTS R57), as R64 (a)'s item (i)
    rests on it (N-EPR-1).
  - RESULTS R18 (d) Lemma S (a) (= (VJ), RESULTS R57 (a), on every game), on G, on H and on S4b's arenas.
  - RESULTS R38 (a) (phases: (λ_Ξ, τ) constant).
  - RESULTS R64 (a), (b) (docs/RESULTS.md l. 3221-3229 at trunk 9bbd86e4; R68 (f) at l. 3546-3548) and their proof, packet docs/new/P-N5-EPR-box45.md §1-§2 (sha1 8fecca797478d1a77564ac1c5b82d11e952559e0, pinned in R64),
    read with the repair EPR-1 (R64 (b)).
  - For the instance G^u: RESULTS R68 (f). No other result is used.

## 0. Setting (every game)
As RESULTS R64's setting line: N5 = SPEC S1-S5; state k = (σ_k, τ_k); σ̄_k := S1's Odd counterstrategy to σ_k; Ξ_k := V_{σ_k,σ̄_k}; W_k :=
V_{σ_k,τ_k}; λ := Ξ's cycle-node map; phases as in RESULTS R38 (a); Q := the Odd vertices of out-degree ≥ 2; N5^τ := SPEC N5 with S4b replaced by
S4b^τ (keep τ when Iτ ≠ ∅ and τ is value-optimal against σ in S4b's arena). Inside a phase P, τ_k = τ is constant.
- An ODD CUT of G is a game H with G's vertices, priorities, owners and Even successor lists, in which every Odd v has a non-empty successor list
  succ_H(v) ⊆ succ_G(v). Objects computed by SPEC on H carry a prime (Ξ′, W′, Iσ′, Iτ′).
- Let J = (x, …, y) be a run of consecutive states of one phase P of N5 on G. J is H-ADMISSIBLE if for every Odd v: τ(v) ∈ succ_H(v), and
  σ̄_k(v) ∈ succ_H(v) for every k ∈ J. len(J) := (y − x) + [1 if y → y + 1 is an in-phase transition, else 0].
- So, at every k ∈ J: (P1) every Odd strategy of H is an Odd strategy of G; (P2) σ̄_k is an Odd strategy of H; (P3) τ is an Odd strategy of H,
  and Even has the same successor lists in H as in G.

## 1. Lemma RESTRICT_H and Corollary REPRO_H (PROVED, every game)
Lemma RESTRICT_H. Let J be an H-admissible run of a phase of N5 on G, and k ∈ J. Then, at the pair (σ_k, τ):
- (i) Ξ′_k = Ξ_k and W′_k = W_k.
- (ii) Iσ′_k = Iσ_k; SPEC S4a's output on H equals its output on G; S4c's Even switch-all on Iσ is the same on H as on G.
- (iii) Odd's dual valuation of τ is the same on H as on G; hence Iτ′_k = Iτ_k ∩ E(H).
- (iv) if k → k+1 is an in-phase transition of N5 on G and Iτ′_k ≠ ∅, then τ is value-optimal against σ_k in S4b's arena of H.
Proof. P-N5-EPR §1's proof of RESTRICT_E (l. 55-70) with H in place of G′_E. That proof uses G′_E only through (P1)-(P3) at the one state k;
each use, by line:
- (i), l. 56: “Every Odd strategy of G′_E is one of G (G′_E's edges are G's).” This is (P1). With Lemma S (a) on G against S1's
  counterstrategy σ̄′_k on H: Ξ_k ⊴ Ξ′_k. l. 57-58: “Lemma S (a) on G′_E: Ξ′_k ⊴ V_{σ_k,σ̄_E} = Ξ_k, since σ̄_E is an Odd strategy of G′_E and σ̄_k
  = σ̄_E.” Here this is (P2) directly: σ̄_k is an Odd strategy of H, so Lemma S (a) on H gives Ξ′_k ⊴ V_{σ_k,σ̄_k} = Ξ_k. RESTRICT_E needs σ̄_k = σ̄_E
  to get (P2); RESTRICT_H assumes (P2) at each k, so σ̄ may change along J. Antisymmetry (l. 58-59) is a property of the order, not of the game:
  Ξ′_k = Ξ_k. l. 59-60: “W: G_τ and (G′_E)_τ are the same one-player game (every Odd v keeps τ(v), which is an edge of G′_E), so W′_k = W_k.” This
  is (P3).
- (ii), l. 61: “Iσ (S2) is read from Ξ and Even's successor lists, both unchanged by (i).” Ξ by (i), Even's lists by (P3). l. 61-62: S4a's arena
  (Even v restricted to {σ_k(v)} ∪ Iσ_k(v), every Odd v to τ(v)) “is the same game for G and G′_E”: by (P3) (Even lists, and τ(v) ∈ succ_H(v)).
  S1 on its dual is deterministic, and S4c “reads Iσ, Ξ and vertex indices only” (l. 62-63).
- (iii), l. 64: “S1 on G^d for τ runs on the graph in which τ's owner (Odd) keeps only τ and Even keeps all its edges: the same graph for G and
  G′_E.” This is (P3). S2 on G^d then reads Odd's successor lists, which in H are subsets of G's (P1), so Iτ′_k = Iτ_k ∩ E(H) (l. 65).
- (iv), l. 66-70: Iτ′_k ≠ ∅ gives Iτ_k ≠ ∅ by (iii); the transition is in-phase, so S4b's output on G is τ (S4c, S4d; a statement about G
  only); Lemma S (a) on S4b's arena H′_G of G; S4b's arena on H restricts Odd v to {τ(v)} ∪ Iτ′_k(v) ⊆ {τ(v)} ∪ Iτ_k(v), so “every Odd strategy of it
  is one of H′_G, and τ is one of them” (l. 69-70): (iii) and (P3). Lemma S (a) on that arena closes the step.
Nothing else about G′_E is used: not that Odd vertices outside D_E have out-degree 1, not that D_E-vertices have out-degree 2, and not that σ̄ is
constant on the run, because each item is a statement at ONE state k. □
Corollary REPRO_H (with R64 (b)'s repair EPR-1). Let J = (x, …, y) be H-admissible and y′ := x + len(J). Then N5^τ on H from (σ_x, τ) passes
through (σ_x, τ), …, (σ_{y′}, τ) with the same fallback / non-fallback type at each of its len(J) transitions as N5 on G; the states x, …, y lie
in one phase of that N5^τ run; the last transition y → y′ has its source there and may leave it (EPR-1), unless σ̄_{y′} is also an Odd strategy
of H (then J ∪ {y′} is H-admissible and y′ is in that phase too).
Proof. P-N5-EPR §2's induction (l. 76-82) on k ∈ [x, y′ − 1] ⊆ J verbatim, with RESTRICT_H (ii) for S4a's output, Iσ′_k = Iσ_k ≠ ∅ and S4c, and
RESTRICT_H (iv) with the definition of S4b^τ for τ_new = τ; and RESTRICT_H (i) at the states of J for λ′ = λ (one N5^τ phase). R64 (b)'s
repair applies unchanged: (i) at y′ needs (P2) at y′. □

## 2. Instances (PROVED; in each, J is H-admissible by the definitions)
| H | Odd cut | J | admissibility | status |
| --- | --- | --- | --- | --- |
| G′_E | v ∉ D_E cut to τ(v); u ∈ D_E to {τ(u), σ̄_E(u)} | an epoch E | σ̄_k = σ̄_E on E | RESULTS R64 (a), (b) |
| G^u | v ∈ Q ∖ {u} cut to τ(v); u keeps all edges | a u-run (D_k ⊆ {u}) | σ̄_k(v) = τ(v) for v ≠ u | RESULTS R68 (f) |
| G^{u|J} | v ∈ D⁻ cut to {τ(v), σ̄_J(v)}; other v ≠ u to τ(v); u keeps all edges | a frozen-side u-stretch | σ̄_k = σ̄_J on Q ∖ {u} | NEW (N5-NCONF §9's CONJECTURE RESTRICT_{u|J}) |
| G^P | v cut to {τ(v)} ∪ {σ̄_k(v) : k ∈ P} | the whole phase P | by construction | NEW |
- Frozen-side u-stretch (N5-NCONF §9): a maximal run J of a phase on which σ̄ is constant on Q ∖ {u}; D⁻ := {v ∈ Q ∖ {u} : σ̄_J(v) ≠ τ(v)}. For Odd v ∉
  Q, σ̄_k(v) = τ(v) is v's only successor. So J is G^{u|J}-admissible.
- The used-edge game G^P of a phase P = (x, …, y): every Odd v keeps τ(v) and each best reply it takes in P. P is G^P-admissible, and len(P) =
  y − x (y → y + 1 leaves P by maximality), so REPRO_H reproduces every in-phase transition of P with no EPR-1 exit: EVERY PHASE OF N5 ON G IS
  ONE N5^τ PHASE ON G^P, from (σ_x, τ), state by state, with the same fallback types. QP(P) := #{Odd v : |succ_{G^P}(v)| ≥ 2} and XDEG(P) :=
  Σ_v (|succ_{G^P}(v)| − 1); G^P ∈ 𝒞^{QP}O.

## 3. DATA (not to sign; experiments/new/box48/phrestrict.py; outputs in experiments/new/box48/out/)
XI_V = Ξ on G^P differs from Ξ on G at a state of P; REP_V = N5^τ on G^P fails to reproduce σ, τ and the fallback type at an in-phase transition
of P. MUT=1 drops the edge (v, σ̄_x(v)) from G^P for one v with σ̄_x(v) ≠ τ(v) (P2 fails at x; must bite).
| sample | phases (≥ 2 states) | in-phase transitions | phases with QP ≥ 2 | max QP | max XDEG | XI_V | REP_V | MUT=1: XI_V / REP_V (mutated) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| liball n ≤ 34 (experiments/new/box47/out/liball.txt), S3 + 2 random, seed 7 | 1,031 | 8,458 | 147 | 11 | 20 | 0 | 0 | 514 / 292 (561) |
| nep90_n40 (experiments/red/rec0/instances, start experiments/si/rund/instances/nep90_n40.start) | 1 | 91 | 1 | 5 | 22 | 0 | 0 | 1 / 0 (1) |
| nep76_n40 (experiments/n5-epoch/instances, with its .start) | 1 | 78 | 1 | 5 | 24 | 0 | 0 | 1 / 1 (1) |
| long121_n40 (experiments/new/box48/instances, with its .start) | 1 | 121 | 1 | 3 | 8 | 0 | 0 | 1 / 1 (1) |
- Files: out/phrestrict_liball_n34_k2.txt, out/phrestrict_liball_n34_MUT.txt, out/phrestrict_long3.txt.
- §9's G^{u|J} data (fsrestrict.py, successor 27; out/fsrestrict_*.txt): 75 frozen-side stretches on liball n ≤ 34 and 25 / 21 / 12 on nep90 /
  nep76 / long121, XI_V 0, REP_V 0; its MUT=1 (v ∈ D⁻ cut to τ(v) only) bites. Blind spot named there: pft34's D⁻ = {32}.
- Engine: the lane's experiments/new/box43/multi.py (N5 on G) and experiments/new/box45/eprestrict.py step_tau (N5^τ), as imported by fsrestrict.py.

## 4. READING and OPEN (not to sign)
- READING. A phase of N5 depends only on the Odd edges it uses. So every per-phase count may be taken on G^P ∈ 𝒞^{QP}O, a game with QP Odd choice
  vertices, each of out-degree ≤ 1 + (the distinct non-τ replies it takes in P). nep90, nep76 and long121, the fleet's longest phases (91, 78
  and 121 transitions at n = 40), are N5^τ phases of games with 5, 5 and 3 Odd choice vertices.
- READING. With RESULTS R61 (𝒞^kO counts, conditional on R56 and R58: f = O(n^{k+1}) on 𝒞^kO, Corollary FB-kO) and R51 (𝒞^1O, per-phase bound T* under (Στ)): if a count
  proved on 𝒞^kO transfers to N5^τ (as R64 (e) EP-1 transfers R51 under (Στ)), then it bounds every phase of every game with k := QP(P). Whether
  R61's chain holds for N5^τ is not checked here.
- OPEN. QP(P) and XDEG(P) on general games; whether QP is bounded by a quantity already counted (ρ, NCONF, epochs).

## 5. Quotes and pins (checked by script)
Every quote above, set in curly double quotes, is verbatim from docs/new/P-N5-EPR-box45.md at l-new 08abd9cb (sha1 8fecca79…, unchanged on trunk
9bbd86e4), at the line named. Pins: P-N5-EPR-box45.md 8fecca797478d1a77564ac1c5b82d11e952559e0; N5-NCONF-box48.md at 7b5876d8 (§9, §10);
phrestrict.py b4624a45…, fsrestrict.py 2f09852d….
Script: `python3 experiments/new/box48/quotecheck2.py docs/new/P-N5-RESTRICT-box48.md 08abd9cb:docs/new/P-N5-EPR-box45.md` (output
experiments/new/box48/out/quotecheck_restrict.txt).
