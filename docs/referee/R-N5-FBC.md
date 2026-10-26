# R-N5-FBC: REFEREE report on packet P-N5-FBC (L-NEW box 47: Lemma FB-RISE_C, Lemma SAT_C, Theorem FB-C (in-phase fallbacks per phase ≤ |𝒞_f(P)|·(4n² − 3n)), Corollaries (a)-(d); every game)
Referee: REFEREE (successor 15), Opus 5.5 (owner ruling D15). FIRST referee (Lead brief; GO 13:44Z Lead stamp). REFEREE-2 successor 17 reviews in parallel.
- Object: docs/new/P-N5-FBC-box47.md, sha1 32d3776cf4090fb15c1d0cb4c8b4f59276f64e21 (on the tree, at the l-new freeze 1f8d6d7d and at the pin
  trunk de02d37e, an ancestor of HEAD), 138 lines. Author: L-NEW successor 26.
- Written 2026-10-26T13:56Z-14:04Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ file on FBC or CHOSEN on my tree, on trunk or on origin/claude/referee-2 at any of my fetches
  (re-listed in the same turns; 0 / 0 / 0 at 14:03Z). No lane code run (experiments/new/box47/fbconf.py, fbcount.py, fbpot.py, quotecheck.py neither executed nor
  imported). D1.
- Premises read against their text: SPEC S1, S2, S4c, FIX 3 (docs/new/N5-ssi-global.md); RESULTS R15 (a), (b), (d); R17 (a) (V1)/(V2) and
  box 10 §2 Case A (A1, A2) (docs/new/N5-phase-bound-box10.md l. 19-38); R38 (a), (f) CN-LAST; R56 (f); R57 (a) (VJ) and premise 1E-N3;
  R60 (c) EPOCH (setting line: EPOCH = maximal run with σ̄|Q constant, N_ep their number); R61 (d), (f); P-N5-HONFF §1 (items 2-3 and Q-A,
  my lane's R-N5-HONFF: Q-A YES, §C joint map empty); P-N5-HON §0 (D_k) and step 2.
- Quotes and pins: all 14 curly-quoted passages of §6 found verbatim (whitespace normalised) in the named files at l-new 80509398, each
  ending at the cited line (own script scratch/fbc_quotes.py; 80509398 is an ancestor of the freeze 1f8d6d7d). Pins re-measured on the tree,
  at 80509398 and at 1f8d6d7d: P-N5-HONFF 98101d1f, N5-FB-box47.md 9ad340b2, fbconf.py a5932c09, N5-ssi-global.md 66fde9ef,
  N5-phase-bound-box10.md e1a27529: all match.
- Tool: scratch/fbc_probe.py (own engine rl_engine; exact LEV_C by simple-path enumeration in H_C for every configuration C visited in the
  phase, with a path budget per configuration; checks listed in §4). Logs scratch/fbc_logs/.

## Verdicts
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | Lemma FB-RISE_C | SIGNED |
| §1 | Lemma SAT_C (both parts) | SIGNED (note FBC-N2: R15 (d) reaches Ξ through R57 (a) (VJ)) |
| §1 | Theorem FB-C: f ≤ \|𝒞_f(P)\|·(4n² − 3n) | SIGNED (note FBC-N3: the saturated term is at most 1 per configuration, so f ≤ n·\|𝒞_f(P)\|; referee's proof, §2) |
| §2 | Corollary (a) | SIGNED |
| §2 | Corollary (b) | SIGNED |
| §2 | Corollary (c) | SIGNED (note FBC-N1: D_k is defined in P-N5-HON §0, not in P-N5-HONFF §0) |
| §2 | Corollary (d) | SIGNED (the inequality; the comparison sentences after it are READINGS, note FBC-N4) |
| header | "(a)'s N_ep form and (d) are WEAKER than R60 (c) EPOCH" | CONFIRMED for n ≥ 2 (both are implied by EPOCH, with R61 (f) for (d)); at n = 1 f = 0 (§3) |
| §3-§5 | context, data, OPEN | not signed (as briefed) |
No gap. Notes FBC-N1..N4. Theorem FB-C bounds f per phase by the number of distinct configurations at fallback sources, which is not
bounded here on general games; it bounds no running time; not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. The three lemmas, re-derived
Parentheticals and "by (x)" inside the signed statements and proofs are listed and checked one by one (my predecessor's G-FLIP-3 lesson).
- §0 setting ✓. A C-state's honest play follows σ_k at Even vertices (edges of G, all kept in H_C) and σ̄_k = C on Q, the forced edge elsewhere,
  so it is a play of H_C, and Ξ_k (the (σ_k, σ̄_k)-play value, P-N5-HONFF §0) is σ_k's valuation in the one-player game H_C (Odd has one
  choice there) ✓. H_{τ|Q} = G_τ ✓. LEV_C(k) ≥ 0 at every state (j = 0: x = u a cycle node of λ, Ξ_k(u) = (u, ∅, 0)) ✓; non-decreasing along
  P because H_C and λ are fixed on P and Ξ is pointwise non-decreasing ((MON) = R15 (a), (d), via R57 (a)) ✓.
- FB-RISE_C ✓.
  - In-phase ⇒ τ kept ⇒ the fallback is Even's (S4c with FIX 3: an Odd fallback changes τ); λ_{t+1} = λ_t ✓. |r| = 0 trivial ✓; for
    1 ≤ |r| ≤ min(LEV_C(t) + 1, n − 1), r = x → z → r′ with r′ ⊆ H_C avoiding x, |r′| ≤ LEV_C(t), so Ξ_t(z) ⪰ value(r′) ✓ (r′ is an H_C-path,
    which is what LEV_C(t) speaks about).
  - Odd x: z is x's only H_C-edge, z = σ̄_C(x) = σ̄_t(x) "(t is a C-state; outside Q, x has one successor)" ✓. λ(x) ≠ x: (V1) for the honest
    play at t (a functional graph; Ξ_t(x) = x ⊕ Ξ_t(z), z's path to λ(x) avoiding x) and (V2) ("r′ avoids x": both paths avoid x) ✓.
    λ(x) = x: z lies on x's honest cycle, so λ(z) = x; value(r′) has cycle node u ≠ x (r simple, |r| ≥ 1); Ξ_t(z) ⪰ value(r′) with
    distinct cycle nodes forces reward(x) > reward(u) (injective p′, cycle node compared first), so (x, ∅, 0) ≻ value(r) ✓. Then (MON) ✓.
    The Odd case does not use the fallback at all: it holds at EVERY C-state (my check ODDC tests it there).
  - Even x: P-N5-HONFF items 2-3 verbatim ✓. They use the edge (x, z) of G (kept in H_C: "Even vertices keep all their edges in H_C as in
    G_τ" ✓), Ξ_t(z) ⪰ value(r′), S4c's (Ξ_t(w), w)-maximum (item 3: Ξ_t(z*) ⪰ Ξ_t(z)), Case A with Ω := Ξ_t (Q-A, YES by both referees on
    P-N5-HONFF; Case A uses only non-improvement, the bound on Ω(z), (V1) for a single play and (V2), none of which sees the frame of r′),
    (MON), (V1)/(V2) at t + 1 and λ_{t+1} = λ ✓. "None of them uses the frame of r′" ✓: the frame enters only through Ξ_t(z) ⪰ value(r′).
- SAT_C ✓.
  - (1): at a C-state the honest play from x is a lasso of H_C; its prefix up to the first visit of λ(x) is a simple H_C-path r_x to a cycle
    node of λ and Ξ_t(x) = value(r_x) (S1: cycle node, the more relevant vertices before it, the steps to it) ⪯ B_C(x) "(as HON step 2)" ✓
    (P-N5-HON l. 70, the same argument in G_τ). LEV_C(t) = n − 1 covers every simple path (≤ n − 1 edges), so Ξ_t ⪰ B_C ✓.
  - (2): Ξ_t = B_C ⪰ Ξ_{t′} "(t′ a C-state)" ⪰ Ξ_t (MON) ✓, so Ξ is constant on t, …, t′ ✓. τ constant on P ⇒ Ωτ constant ✓. R15 (d)'s window
    ("at most 4n(n−1) consecutive N5 iterations leave both Ωσ and Ωτ unchanged") gives t′ − t ≤ 4n(n − 1) ✓, once Ωσ is Ξ: that is R57 (a)
    (VJ) under the standing premise 1E-N3, as R60's premise list records it (ACCEL-N2). The packet cites 1E-N3 but writes "Ωσ read as S1's
    Ξ, as every per-phase packet does" without naming R57 (a) (FBC-N2, a citation note).
- Theorem FB-C ✓. Per C: unsaturated sources t_i (LEV_C ≤ n − 2) rise strictly from one to the next (FB-RISE_C at t_i, then LEV_C
  non-decreasing from t_i + 1 to t_{i+1}), values in {0, …, n − 2}: ≤ n − 1 ✓. Saturated ones lie between the first and the last saturated
  C-state source, a window of ≤ 4n(n − 1) transitions by SAT_C (2): ≤ 4n(n − 1) + 1 ✓. Sum over 𝒞_f(P) ✓. The remark "For C = τ|Q … the Odd
  term automatically ≥ LEV + 1 at D = ∅ sources" ✓ with the cap: LEV_odd(t) ≥ min(LEV(t) + 1, n − 1) (my Odd-case reading above).

## 2. Note FBC-N3: the saturated term is at most one fallback per configuration (referee's proof; strengthens Theorem FB-C to f ≤ n·|𝒞_f(P)|)
The packet's §5 lists "a better saturated term" as OPEN (data: at most 1 saturated fallback per configuration and phase) and says the HON-FB
route is not proved in H_C. It follows from SAT_C (2) and two landed lemmas, without that route:
- Claim. Per phase P and configuration C, at most one in-phase fallback has a saturated C-state source. Hence f ≤ |𝒞_f(P)|·((n − 1) + 1) =
  n·|𝒞_f(P)|.
- Proof. Let t < t′ be two such sources. SAT_C (2): Ξ is constant on t, …, t′, so the fallback t → t + 1 has Ξ_{t+1} = Ξ_t. It applies
  Switch_I with I := {(v, z*(v)) : Iσ_t(v) ≠ ∅}, a non-empty unambiguous set of improvements (S4c). Through R57 (a) (Ξ = VJ00's Ω), RESULTS
  R15 (b) gives: every (v, z*(v)) ∈ I is a length-only switch at a cycle node, λ_t(v) = v, Λ(z*(v)) = Λ(σ_t v) = v and both path sets above v
  are empty. Every Even v with Iσ_t(v) ≠ ∅ is switched (S4c), so every gate (y, w) ∈ Iσ_t has λ_t(y) = y; and Ξ_t(σ_t y) ◁ Ξ_t(w) ⊴ Ξ_t(z*(y))
  with equal cycle node y at both ends and empty path sets at both ends forces cycle node y and signed weight 0, i.e. an empty path set, at w
  (a non-empty set has non-zero weight): lev(Ξ_t(σ_t y), Ξ_t(w)) = −1 ("length" level, docs/si/N5-C-box5.md l. 36). So RESULTS R38 (f)
  CN-LAST applies: t + 1 is the last state of P. Then t′ ≥ t + 1 cannot be the source of an in-phase transition: contradiction. □
- Data (own engine, §4): every Ξ-flat in-phase fallback ends its phase (check FLATLAST: 231 of 630 fallbacks at n ≤ 20 and 720 of 727 in
  the second random 𝒞^kO batch are Ξ-flat; 0 failures); at most 1 saturated fallback per configuration and phase in every sample. The check bites: under MUT=3 (S4c takes the minimum of
  Iσ(x)) FLATLAST fails 8 times and MAX_SAT_C reaches 3.
- Consequence for the header's comparison: with FBC-N3, (a)'s N_ep form becomes f ≤ n·N_ep, which is EPOCH's 1 + n·N_ep less one; the
  per-configuration form f ≤ n·|𝒞_f(P)| is new against EPOCH exactly where configurations recur. This is a note for the lane, not a signed
  statement of the packet (REFEREE-2 has not reviewed it).

## 3. Corollaries and the header claim
- (a) ✓. An epoch (R60 / R61 / R63 setting lines: a maximal run of the phase with σ̄|Q constant) has one configuration, so the configurations
  visited number ≤ N_ep; a configuration is a successor choice at each q ∈ Q, so ≤ Π_q deg(q); 𝒞_f(P) ⊆ the visited ones ✓.
- (b) ✓. Π_q deg(q) ≤ Δ^k on 𝒞^kO. The parenthetical comparison with R61 (d) (f = O(n^{k+1}), constant O(k^{k+1}·2^k)) is accurate as a
  comparison of forms ("a different trade"; R61 (d) is better for unbounded degree, (b) for bounded Δ) ✓.
- (c) ✓. D_k := {q ∈ Q : σ̄_k(q) ≠ τ(q)} (P-N5-HON §0 l. 44; the packet's §0 points to P-N5-HONFF §0, which does not define D: FBC-N1).
  |D_k| ≤ 1 ⇒ σ̄_k|Q is τ|Q or τ|Q with one u moved to y ≠ τ(u): ≤ 1 + Σ_q (deg q − 1) ≤ 1 + m ✓. The general count Σ_{j ≤ d} C(|Q|, j)(Δ − 1)^j ✓.
- (d) ✓ as an inequality: (a) with R61 (f)'s bound on N_ep. The two sentences after it compare bound forms (READING; FBC-N4): R56's bound is
  smaller than FB-C's in every phase of the two batches that ran this check (the n ≤ 20 library and the second random batch: 0 phases where 1 + (n − 1)(2 + ρ) exceeds |𝒞_f|(4n² − 3n); max ρ 20 in a phase with a
  fallback at n ≤ 20). "Incomparable in general" is witnessed in one direction only; the other direction needs ρ ≳ 4n·|𝒞_f(P)|, which no
  known phase has (RESULTS R56 limits: max ρ 218 at n 350). As a reading it is harmless; it is not a signed statement.
- Header claim "(a)'s N_ep form and (d) are WEAKER than R60 (c)" CONFIRMED. R60 (c) is on every game, per phase, with the same f and the same
  N_ep. For n ≥ 2 and N_ep ≥ 1: 1 + n·N_ep ≤ (4n² − 3n)·N_ep ⇔ 1 ≤ 4n(n − 1)·N_ep ✓, so EPOCH implies (a)'s N_ep form; with R61 (f),
  1 + n(1 + Σ) ≤ (4n² − 3n)(1 + Σ), so EPOCH + R61 (f) implies (d) ✓. At n = 1 the only vertex has a self-loop only, Iσ = ∅, f = 0, and both
  forms are trivial. The packet's CORRECTION paragraph states this accurately; its "(b) and (c) … not implied by EPOCH" is a reading
  (EPOCH bounds by epochs, and epochs repeat configurations: RESULTS R60 limit (i); my samples: 455 configurations against 497 epochs in the
  365 phases with a fallback at n ≤ 20).

## 4. Data (own engine; DATA, not proof; 0 failures of every signed check)
Checks: REAL (Ξ_k = the honest play's value, every state), MONO (LEV_C non-decreasing along P for every visited C, at every state), FBC
(FB-RISE_C), ODDC (FB-RISE_C's Odd case at every C-state), SATB (SAT_C (1)), SATW (SAT_C (2)), THM (per C: unsaturated ≤ n − 1, saturated
≤ 4n(n − 1) + 1; f ≤ |𝒞_f|(4n² − 3n)), CORA, CORC, and FLATLAST (FBC-N3). Starts: S3 and random start pairs.
| sample | runs | phases | in-phase fallbacks (FB-RISE_C checked) | Ξ-flat fallbacks (FLATLAST) | ODDC C-states | SATB / SATW | max unsaturated / saturated per C in a phase | Σ \|𝒞_f\| / Σ configurations / Σ epochs (phases with a fallback) | UNK phases |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scratch/fbc_lib.txt (1,140 .pg files of experiments/ and docs/referee/, none of docs/referee-2/), n ≤ 20 (471 files), S3 + 6 random starts | 3,297 | 12,172 | 630 (630) | 231, all end their phase | 2,077 | 635 / 396 | 12 / 1 | 374 / 455 / 497 | 0 |
| the same list, n ≤ 34 (807 files), S3 + 2 random, budget 3·10⁶ per configuration (run before FLATLAST was added) | 2,421 | 11,911 | 1,391 (801) | — | 3,341 | 620 / 448 | 25 / 1 | 512 / 1,275 / 1,930 | 115 |
| random 3,000 𝒞^kO (n 5-18, k ≤ 4, seed 151), S3 + 4 random | 15,000 | 40,132 | 597 (597) | — | 1,346 | 1,191 / 595 | 1 / 1 | 597 / 606 / 606 | 0 |
| random 3,000 𝒞^kO (n 6-22, k ≤ 8, seed 152), S3 + 4 random | 15,000 | 45,301 | 727 (727) | 720, all end their phase | 1,661 | 1,449 / 723 | 1 / 1 | 727 / 737 / 737 | 0 |
| experiments/red/fbr/instances/fr39_q4_n48.pg, L-RED's start and S3, budget 5·10⁷ | 2 | 7 | 39 (39) | — | 49 | — | 24 / 0 | 7 / 8 / 11 | 0 |
REAL held at every state (17,786 + 24,747 + 44,493 + 49,518 + 87 states); MONO, CORA, CORC, THM 0 failures in every row. The n ≤ 34 maximum
of 25 unsaturated fallbacks in one configuration is the packet's farrise25_n32 figure.
- Mutations (each bites): MUT=1 (every fallback read in G_τ, i.e. C := τ|Q): FBC fails 79 times (n ≤ 20, 1,413 runs), as the packet's τ-frame
  control does; MUT=2 (FB-RISE_C with + 2): 144 failures; MUT=3 (S4c takes the (Ξ, w)-minimum of Iσ(x)): FBC fails 15 times and FLATLAST 8
  times (item 3 needs the maximum).
- Reproductions: fr39_q4_n48 at L-RED's start (experiments/new/box47/instances/fr39_q4_n48.start, read as data): 39 in-phase fallbacks in one
  phase, 7 configurations at fallback sources, max 24 unsaturated per configuration, 0 saturated: the packet's row exactly.
  experiments/red/so/instances/s4c8_n13.pg (S3 + 2 random): 8 in-phase fallbacks in one phase, all in one configuration and all
  unsaturated (8 ≤ n − 1 = 12), 0 failures (packet §3's instance).

## 5. Notes (none blocks a signature)
- FBC-N1 (definitions). §0 says "As P-N5-HONFF §0", but D_k (used in (c), §3) and EPOCH / N_ep (used in (a), (d)) are defined in P-N5-HON
  §0 (l. 44, landed R68) and RESULTS R60 / R61 / R63, not in P-N5-HONFF §0. Name them.
- FBC-N2 (citation). SAT_C (2) applies R15 (d) to Ξ; the bridge is R57 (a) (VJ) under 1E-N3 (as in R60's premises, ACCEL-N2). Cite it
  instead of "read as … as every per-phase packet does".
- FBC-N3 (strengthening, §2). At most one saturated fallback per configuration and phase (SAT_C (2) + R15 (b) + R38 (f) CN-LAST), so
  f ≤ n·|𝒞_f(P)|, which answers the packet's §5 second item. For the lane to take up; REFEREE-2 has not reviewed it.
- FBC-N4 (reading). (d)'s "incomparable in general" with R56 is witnessed in one direction only (§3); the header's "INCOMPARABLE" likewise.

## §C. Comparison with REFEREE-2 (written 2026-10-26T15:01Z-15:05Z by date -u, after the Lead's word of 14:58Z; REFEREE-2's report
docs/referee-2/R2-N5-FBC.md at origin/claude/referee-2 64ee8e9c, read only after my report was pushed at 0addfc5f)
### Verdicts
| item | REFEREE (0addfc5f) | REFEREE-2 (64ee8e9c) | joint |
| --- | --- | --- | --- |
| FB-RISE_C | SIGNED | SIGN | SIGNED |
| SAT_C | SIGNED | SIGN | SIGNED |
| Theorem FB-C | SIGNED | SIGN | SIGNED |
| Corollaries (a), (b), (c), (d) | SIGNED ((d): the inequality; its comparison sentences a READING) | SIGN | SIGNED |
| header: (a)'s N_ep form and (d) weaker than R60 (c) EPOCH | CONFIRMED for n ≥ 2; n = 1: f = 0 | CONFIRMED for n ≥ 2; n = 1 vacuous exception (N-FBC-4) | CONFIRMED for n ≥ 2 |
| quotes (14) | verbatim at 80509398 | verbatim at 80509398 and de02d37e | verbatim |
Verdicts identical. Joint gap map: EMPTY (neither referee found a gap).
### Notes, matched
| REFEREE | REFEREE-2 | joint |
| --- | --- | --- |
| FBC-N1 (D_k, EPOCH / N_ep imported from P-N5-HON §0 and R60/R61, not HONFF §0) | N-FBC-3 (D_k from P-N5-HON §0 l. 44) | same note; FBC-N1 also names EPOCH / N_ep |
| FBC-N2 (cite R57 (a) (VJ) for R15 (d) on Ξ) | — (REFEREE-2 uses the same bridge in its premise column: "(MON) = R15 (a), (d) via (VJ) under P1") | REFEREE's citation note; nothing at issue |
| FBC-N3 (PROOF: ≤ 1 saturated fallback per configuration and phase, so f ≤ n·\|𝒞_f(P)\|) | N-FBC-6 (SAT_C's 4n(n − 1) + 1 term untested: max 1 saturated per C everywhere, longest window 2; its control "≤ 1 saturated per C" does not bite) | they fit: FBC-N3 proves that the "≤ 1 saturated per C" control cannot bite on any game, and that SAT_C's window term is never used by FB-C. FBC-N3 is REFEREE's alone and unreviewed by REFEREE-2; I ask the Lead to route it to L-NEW as a note and to REFEREE-2 if a check is wanted |
| FBC-N4 ("incomparable with R56": witnessed in one direction only; R56's number smaller in every phase I checked) | N-FBC-5 (FB-C's number never beat EPOCH's or R56's; max N_ep/\|𝒞_f\| = 45 at n = 32 against 4n − 3 = 125); "incomparable as FORMULAS" | same observation; both read "incomparable" as a statement about forms only |
| header n = 1 remark (§3: one vertex, self-loop only, Iσ = ∅, f = 0) | N-FBC-4 ("f ≤ 1 either way") | same; at n = 1 f = 0 exactly, so both forms hold trivially |
| — (checked in my §1: "LEV_C(k) ≥ 0 at every state", not raised as a note) | N-FBC-1 (FB-C's count needs LEV_C ≥ 0; the packet does not say it) | ACCEPTED (I checked the fact but did not flag that the packet omits it) |
| — (my §1: the Odd case needs no fallback and holds at every C-state) | N-FBC-2 (the Even case holds at any source state; the C-state hypothesis is needed only for the Odd case) | ACCEPTED; the two remarks are complementary (Odd case: any C-state, no fallback; Even case: any state, the fallback) |
### Data
Both own engines, 0 failures of every signed check (mine: 36,720 runs, 3,394 FB-RISE_C checks; REFEREE-2: 2,294 exact checks, 32·10⁶ Case A
checks); both reproduce the packet's figures (fr39_q4_n48: 39 / 7 / 24; farrise25_n32: 25 unsaturated); both τ-frame controls bite (mine 79,
REFEREE-2 14,399). Nothing open between the referees on FBC.
