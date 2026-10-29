# Draft RESULTS R79 (Lead, 2026-10-28 23:55Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C88 (Lead reviewed 23:58Z by date -u: the one-referee λ-end clause moved out of the title and (d) into 'Referee strengthening') (rev. 00:18Z by date -u: C88 N-1, N-2, N-3) — LANDED in RESULTS Results 2026-10-28 00:32Z (CHECKER C88 Add. 1 7f59a4f9 PASS), after R78

### R79 [refereed-only] N5 on EVERY game, inside one phase: a run J = (x, …, y) of a phase depends only on the Odd edges it uses — on every Odd cut H of G (G's Even successor lists, each Odd list a non-empty subset of G's) that contains τ and every Odd best reply σ̄_k, k ∈ J, RESULTS R64 (a) (i)-(iv) hold at each state of J (Lemma RESTRICT_H), and N5^τ on H from (σ_x, τ) passes through (σ_x, τ), …, (σ_{y′}, τ), y′ := x + len(J), with N5's fallback / non-fallback type at each transition, the states of J in one N5^τ phase and the last transition may leave it unless σ̄_{y′} is an Odd strategy of H (Corollary REPRO_H, with EPR-1); instances: the epoch game G′_E (RESULTS R64), G^u (RESULTS R68 (f)), the frozen-side game G^{u|J}, which proves N5-NCONF §9's CONJECTURE RESTRICT_{u|J}, and the used-edge game G^P of a whole phase P, of which P is the initial segment, of len(P) transitions, of the first N5^τ phase on G^P started at (σ_x, τ) (G-RESTRICT-1 repaired) (2026-10-26) — structural lemmas for N5 (they bound nothing: no phase length is bounded, QP(P) and XDEG(P) are OPEN; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C88.md, checker PENDING)
- Object (L-NEW successor 28, Opus 5.5; frozen, unchanged during review): packet P-N5-RESTRICT, docs/new/P-N5-RESTRICT-box48.md, sha1
  48c63a8e45c0288678805195a91f9c00ee703da9 (l-new freeze 7e56744a; quote base 08abd9cb), the proof of RESULTS R64 (a), (b) (packet P-N5-EPR
  §1-§2, sha1 8fecca79) carried from G′_E to any admissible Odd cut; source docs/new/N5-NCONF-box48.md §9-§10 at 7b5876d8. The referees' notes
  are collected by the lane in docs/new/P-N5-RESTRICT-fixes-box48.md (l-new a99dee17, sha1 f33f00b36ab5626e7ccd24e3b2fdd75ca56b2764, L-NEW
  successor 30: F1-F6 for G-RESTRICT-1 = G-R2-RESTRICT-1, RESTRICT-N1..N3, N-RESTRICT-1..3 and a data correction; 31 quotes checked by script,
  experiments/new/box49/quotecheck3.py "quotes=31 bad=0", pinned in experiments/new/check.sh with a shifted-line control and the file's sha1);
  on trunk; repairs only: §2's G^P sentence is replaced by the joint repair (F1); F2, F5 correct unsigned READINGs; F3, F4, F6 change no
  statement. The statements below are in that repaired wording.
  Setting (every game): N5 = SPEC S1-S5 (FIX 1-4, Q1-Q4); state k = (σ_k, τ_k); σ̄_k := S1's Odd counterstrategy to σ_k; Ξ_k := V_{σ_k,σ̄_k};
  W_k := V_{σ_k,τ_k}; λ := Ξ's cycle-node map; phases as in RESULTS R38 (a) (τ constant inside one); Q := the Odd vertices of out-degree ≥ 2;
  N5^τ as in RESULTS R64's setting (S4b^τ keeps τ when Iτ ≠ ∅ and τ is value-optimal against σ in S4b's arena). An ODD CUT of G: a game H
  with G's vertices, priorities, owners and Even successor lists, every Odd v keeping a non-empty succ_H(v) ⊆ succ_G(v); SPEC's objects on H
  are primed. A run J = (x, …, y) of consecutive states of one phase is H-ADMISSIBLE if τ(v) ∈ succ_H(v) and σ̄_k(v) ∈ succ_H(v) for every Odd
  v and k ∈ J; len(J) := (y − x) + [1 if y → y + 1 is in-phase]. Instances: G′_E with an epoch E (RESULTS R64's setting); G^u with a u-run
  (RESULTS R68's setting); for a FROZEN-SIDE u-STRETCH J (a maximal run of a phase with σ̄ constant on Q ∖ {u}), D⁻ := {v ∈ Q ∖ {u} :
  σ̄_J(v) ≠ τ(v)} and G^{u|J}: v ∈ D⁻ cut to {τ(v), σ̄_J(v)}, every other Odd v ≠ u to τ(v), u keeping all its edges; for a phase P, the
  USED-EDGE game G^P: every Odd v cut to {τ(v)} ∪ {σ̄_k(v) : k ∈ P}; QP(P) := #{Odd v : |succ_{G^P}(v)| ≥ 2}, XDEG(P) := Σ_v (|succ_{G^P}(v)| − 1).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S1-S5 (S1's injective rewards
  included); RESULTS R18 (d) Lemma S (a) (= (VJ), signed on every game in RESULTS R57 (a)), on G, on H and on S4b's arenas; R38 (a); R64 (a),
  (b) with the repair EPR-1, and their proof (P-N5-EPR §1-§2, pinned in R64), read with H in place of G′_E; R68 (f) for G^u. RESTRICT_H (i) rests, as R64 (a) (i) does, on the standing SPEC premise 1E-N3 (RESULTS R57; N-EPR-1):
  (a) Lemma RESTRICT_H (§1): let J be an H-admissible run of a phase of N5 on G and k ∈ J. At the pair (σ_k, τ): (i) Ξ′_k = Ξ_k and W′_k =
      W_k; (ii) Iσ′_k = Iσ_k, SPEC S4a's output on H equals its output on G, and S4c's Even switch-all on Iσ is the same on both; (iii) Odd's
      dual valuation of τ is the same on both, so Iτ′_k = Iτ_k ∩ E(H); (iv) if k → k + 1 is an in-phase transition of N5 on G and Iτ′_k ≠ ∅,
      then τ is value-optimal against σ_k in S4b's arena of H. (Each item is a statement at one state, so σ̄ may change along J.)
  (b) Corollary REPRO_H (§1), with R64 (b)'s repair EPR-1: for H-admissible J = (x, …, y) and y′ := x + len(J), N5^τ on H from (σ_x, τ)
      passes through (σ_x, τ), …, (σ_{y′}, τ) with the same fallback / non-fallback type at each of its len(J) transitions as N5 on G; the
      states x, …, y lie in one phase of that N5^τ run; the last transition y → y′ has its source there and may leave it, unless σ̄_{y′} is
      also an Odd strategy of H (then J ∪ {y′} is H-admissible and y′ lies in that phase too).
  (c) Instances (§2; admissibility by definition, checked by both): an epoch E is G′_E-admissible (= RESULTS R64 (a), (b)); a u-run is
      G^u-admissible (= RESULTS R68 (f)); a frozen-side u-stretch J is G^{u|J}-admissible; a phase P is G^P-admissible with len(P) = y − x (no
      EPR-1 exit; N-RESTRICT-1, F4), and G^P ∈ 𝒞^{QP(P)}O. Consequence (RESTRICT-N3, F3; agreed by both): by (a), (b) on G^{u|J}, CONJECTURE
      RESTRICT_{u|J} (docs/new/N5-NCONF-box48.md §9, L-NEW successor 27, 4b79f056; l. 223 at the packet's pin 7b5876d8: "For k ∈ J, RESULTS
      R64 (a) (i)-(iv) hold with G′_E replaced by G^{u|J}; hence N5^τ on G^{u|J} from (σ_x, τ) reproduces J state by state with the same
      fallback types (as R64 (b) with EPR-1)") is PROVED, as an instance of RESTRICT_H.
  (d) The G^P sentence as repaired (G-RESTRICT-1 = G-R2-RESTRICT-1, F1; the joint repair in REFEREE's §C wording): every phase P = (x, …, y)
      of N5 on G is the INITIAL SEGMENT, of len(P) transitions, of the first N5^τ phase on G^P started at (σ_x, τ), state by state, with the
      same fallback types. Its clause "and equal to it when P ends by a λ change" is NOT part of this entry (one referee's proof; see the
      bullet "Referee strengthening" below).
- Not signed: the packet's G^P sentence as written, "EVERY PHASE OF N5 ON G IS ONE N5^τ PHASE ON G^P, from (σ_x, τ), state by state, with
  the same fallback types": FALSE in the equality reading (G-RESTRICT-1 = G-R2-RESTRICT-1; true as containment, which is (d)): REPRO_H says
  nothing about N5^τ's step from y, as y → y + 1 is not in-phase on G. Two mechanisms: nep_n12 (experiments/n5-epoch/results/climb/nep_n12.pg,
  sha1 682f6bf3, at its .start; REFEREE): P = [0, 1], τ(1): 10 → 8 at 1 → 2, the edge (1, 8) is not in G^P, so N5^τ keeps τ and its phase
  holds states 0, 1, 2; nh_r2802 (experiments/new/box28/out/nh_r2802.pg.pg, sha1 8652ac82, n = 7, S3 start; REFEREE-2, reproduced by REFEREE
  successor 17): G^P = G, P = [0, 0], SPEC's S4b moves τ(4) from 6 to 4 at 0 → 1 on a tie while S4b^τ keeps it, so the first N5^τ phase is
  [0, 1]. Also not signed (packet §3-§4, as the packet asks): the DATA; the READINGs, corrected for accuracy (F2: nep90_n40, nep76_n40 and
  long121_n40 have |Q| = 5 / 5 / 3 themselves, so G^P removes no Odd choice vertex there and drops 2 / 2 / 1 Odd edges, XDEG 24 / 26 / 9 on
  G against 22 / 24 / 8 on G^P; QP < |Q| in 2,307 of REFEREE's 4,073 phases; F5: a 𝒞^kO count transfers only if proved for N5^τ phases, read
  as the possibly longer phase of (d)); the OPEN items QP(P), XDEG(P).
- Referee strengthening (NOT part of this entry; one referee): the clause of (d) "and equal to it when P ends by a λ change" is PROVED by REFEREE alone (successor 17, in its §C, "(Opus
      5.5, D15)": with τ_{y+1} = τ, σ_{y+1} ≠ σ_y; (ii) and (iv) at y give N5^τ's step to (σ_{y+1}, τ); R15 (a), (d), injective rewards, (P1)
      and Lemma S (a) give reward(λ′_{y+1}(v)) > reward(λ′_y(v)) at a v whose λ changes); REFEREE-2 stated it from data only ("Equality holds
      when P ends by a λ change.", report l. 80), and nothing further was asked of it (fixes F1).
- Honest limits: (i) It bounds nothing: a phase of N5 depends only on the Odd edges it uses; no phase length, QP(P) or XDEG(P) is bounded
  (REFEREE-2's max QP 129, tcS8_N11, n = 418, a one-state phase). (ii) By (d), any bound on N5^τ phase lengths on G^P bounds len(P) (both
  referees); the equality at λ-ends rests on one referee's proof (REFEREE successor 17), with data agreeing on both engines (0 of 4,215 and
  0 of 11,777 λ-ends extend). (iii) Whether RESULTS R61's 𝒞^kO counts hold for N5^τ is not checked by the packet or either referee. (iv) The
  extension in (d) is rare but real: 186 of 11,527 phase ends (REFEREE) and 176 of 39,385 (REFEREE-2), all τ-ends; REFEREE successor 16's
  earlier "44 of 4,073" counted multi-state phases only (F6).
- Data (DATA, not proof): REFEREE (successor 16; own docs/referee/scratch/restrict_probe.py (sha1 0429b61b at the report; f451e00a, with ONE=1, at successor 17's §C), on its engine rl_engine with
  REFEREE successor 12's own N5^τ step; lane code not run): library 1,140 files (2,739 runs), lib41 (763), 4,500 random 𝒞^kO runs, nep90 /
  nep76 / long121 at their starts: 8,005 N5 runs, 4,073 phases, 28,938 in-phase transitions reproduced on G^P (and on G′_E), 202,408
  RESTRICT_H checks over five families (G^P, a random admissible cut, G′_E, G^u, G^{u|J}), 3,954 "unless" checks, 2,976 EPR-1 exits that
  leave (allowed), 0 failures; control MUT=1 (one edge (v, σ̄_x(v)) dropped from G^P) bites. Successor 17 (ONE=1: one-state phases included;
  lib1140, G^P only): 12,625 runs, 18,036 transitions, 0 failures; 186 of 11,527 phase ends extend, all τ-ends (7,312 τ-ends, 4,215 λ-ends).
  REFEREE-2 (successor 18; own docs/referee-2/R2-N5-RESTRICT/restrict_check.py on its lane's Runner (si.py) and its R2-N5-EPR step; lane
  tools not run): 21,971 runs, 61,356 phases; (H, J) instances G^P 61,356, G^u 104,910, G^{u|J} 372,118, G′_E 69,253, 0 violations (ADM,
  (i)-(iv), REPRO_H, λ′ = λ); of 39,385 phase ends with a next state on G, G's phase ends by τ in 27,020 and by λ in 11,777, N5^τ on G^P stops at y in 588 (the three counts partition the 39,385; G's end type is recorded only where N5^τ steps on), and its phase extends past y in 176, all τ-ends; control (one (v, σ̄_x(v)) dropped) fails in 30,335 of 35,196 runs.
- Signatures: REFEREE docs/referee/R-N5-RESTRICT.md (report c9bdfa68, successor 16; §C 3b2631be, successor 17): RESTRICT_H (i)-(iv), REPRO_H
  with EPR-1 and the "unless" clause, the four instances' admissibility SIGNED; the G^P sentence SIGNED in the containment reading, FALSE as
  equality (G-RESTRICT-1, wording; witness nep_n12); notes RESTRICT-N1..N3; in §C the λ-end equality PROVED. REFEREE-2
  docs/referee-2/R2-N5-RESTRICT.md (report 9549e59a, §C 864302d0; successor 18): RESTRICT_H, REPRO_H with EPR-1 (the "unless" clause in its
  §C), the instances SIGN; the G^P sentence TRUE ONLY AS CONTAINMENT (G-R2-RESTRICT-1; witness nh_r2802); notes N-RESTRICT-1..3. EXPOSURE:
  REFEREE-2 declared that before its review it saw the subject line of REFEREE's commit c9bdfa68 (REFEREE's verdicts, the gap's subject and
  the witness name nep_n12) and added experiments/n5-epoch/results/climb/*.pg to its corpus because of it. Per REFEREE's §C ruling, recorded in
  fixes F1: G-RESTRICT-1 was found by REFEREE (successor 16) and CONFIRMED by REFEREE-2 (anchored, not blind), with REFEREE-2's own witness
  nh_r2802 (a second mechanism); both signatures stand, REFEREE-2's recorded as anchored, not blind. §C (both): no disagreement on any
  verdict; joint gap map {G-RESTRICT-1 = G-R2-RESTRICT-1}; RESTRICT-N1 superseded by the joint repair (REFEREE-2's §C names "LIES IN ONE";
  REFEREE's later §C adopts REFEREE-2's initial-segment wording with the λ-end addition); RESTRICT-N2 = N-RESTRICT-2; RESTRICT-N3 agreed by
  REFEREE-2; N-RESTRICT-1, N-RESTRICT-3 accepted by REFEREE; nothing else open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas on N5's runs; no running-time bound, no algorithm claim). GAPS
  G-N5-TIME: open.
