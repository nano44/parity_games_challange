# Toward an N5^τ count on 𝒞^kO polynomial in n AND k (box 49): where R61's exponent comes from, Lemma OFFSET-MONO, and what the exit changes leave open
L-NEW successor 28 (Opus 5.5), D14 / D18, Lead reading L40; Lead's routing of 16:24Z (Lead's stamp): "put your main effort into (2): an N5^τ count
on 𝒞^kO polynomial in n AND k". Written 2026-10-26 16:3xZ onward (date -u). Working doc, unrefereed. Not a TARGET.md claim; G-N5-TIME stays open.
Labels: PROVED (L-NEW 28, unrefereed) / CONJECTURE / OPEN / DATA / READING / DEAD.
Why it matters: by P-N5-RESTRICT-box48 (frozen, sha1 48c63a8e…) every phase of N5 on any game is one N5^τ phase on its used-edge game G^P ∈
𝒞^{QP}O. N5-NCONF §11-§12 show QP and QP_c are NOT small on long phases (§0 below: QP_c ≈ 0.45n at n = 80). So a count that is polynomial in n
but exponential in k = QP bounds nothing; one polynomial in n and k would bound every phase.

## Summary
| § | item | label |
| --- | --- | --- |
| §0 | QP_c on long phases grows with n: 13-14 at n 48, 24 at n 64, 36 at n 80 (climbs) | DATA |
| §1 | R61's exponent is SAT-k's set form iterated along a routing chain (an odometer); landed R56 (f) with the signed CHOSEN / RELAY-CHAIN (b) already gives a count linear in k, in terms of ROUTE events | READING (an assembly of signed items) |
| §2 | Lemma OFFSET-MONO: with its exit fixed and no entry into the exit's region, an Odd choice vertex's offset to its exit never falls | PROVED (every game) |
| §2 | 0 resets and 0 entries on lib41 and six long instances; every M(q) change sits on an event of q's chain; controls bite | DATA |
| §3 | ROUTE events split into exit changes and same-exit rises; the same-exit part is monotone (§2) and rare in data; the exit changes carry the count | READING + DATA |
| §4 | Lower-envelope (Davenport-Schinzel) view of σ̄(q): needs a bound on pairwise option swaps; swaps reach 15-22 in a phase | READING + DATA (the route is not closed) |
| §5 | Other fields: what transfers and what does not | READING |
| §6 | Open items | OPEN |

## 0. DATA: QP_c on long phases scales with n (N5-NCONF §12 continued; experiments/new/box48/qpcclimb.py, out/qpcclimb/scale/)
One climb per seed (Lead 16:24Z), genome = game + start, O-moves allowed, objective (QP_c · len, len); each best re-checked by qp.py and
phrestrict.py (out/qpcclimb/scale/verify.txt; RESTRICT_H XI_V 0, REP_V 0 on all).
| seed | n ≤ | best: n, |Q|, QP_c (classes), D0, ENT, N_ep, NCONF, len | game / start sha1 |
| --- | --- | --- | --- |
| nep90_n40 (its start), seed 51 (§12) | 48 | 48, 13, 13 (1), 7, 6, 84, 82, 99 | 180e8af5 / ac16f911 |
| nep76_n40, seed 52 (§12) | 48 | 48, 14, 14 (1), 10, 4, 46, 41, 81 | ae540870 / 6b153deb |
| nep90_n40, seed 61 (stopped at step ≥ 2,052 for one climb per seed) | 64 | 64, 25, 24 (1), 15, 9, 76, 76, 97 | 5cde286d / e50f6e42 |
| nep76_n40, seed 63 | 64 | 64, 25, 24 (1), 9, 15, 76, 76, 86 | e6b7123e / b1092e27 |
| nep90_n40, seed 62 (snapshot at step ≥ 2,246; snap_n80_s62.pg) | 80 | 80, 36, 36 (1), 13, 23, 83, 83, 100 | 06dd25e2 / e11e3a0d |
- READING. On these long phases every Odd choice vertex of the game disagrees with τ somewhere in the phase, in ONE class, and QP_c ≈ 0.27n-0.45n.
  A count exponential in k = QP_c is exponential in n here.

## 1. Where RESULTS R61's exponent comes from, and the linear-in-k assembly that already exists (READING)
- R61 (c) Theorem FB-kT (docs/RESULTS.md l. 3122-3123): N_late ≤ 1 + Σ_c Σ_q (V_q − 1), V_q := the distinct values of κ(q) at late fallbacks, and
  "V_q ≤ Σ_{h=0}^{m_c−1} D_c·((m_c − 1)·D_c)^h". The product comes from R61 (b) SAT-k, κ_t(q) ∈ S_{q,p} + κ_t(p) with |S_{q,p}| ≤ d_q, iterated
  along a routing chain q → par(q) → … of depth ≤ m_c − 1 (R61 (a) ROUTE-k): κ(q) is a sum of one offset per level, and the proof counts the
  possible SUMS. R61's not-signed §5 (l. 3134) names the obstruction: the lemmas used admit abstract tuple sequences with D^{depth} values per
  terminal. In words: a lower level's offset may fall while a higher level rises (an odometer), so the values of κ(q) are bounded only by the
  product.
- What avoids the product. Count CHANGE EVENTS instead of values. The signed (both referees, R72 draft, landing pending) P-N5-CHOSEN-box19
  Corollary RELAY-CHAIN (b) (docs/si/P-N5-CHOSEN-box19.md l. 81, sha1 764cfbb3…): "Σ_{q ∈ Q_c} ρ_q ≤ |Q_c| · (ROUTE_c + CYC_c + TOG_c)". With landed RESULTS R56
  (f) (f ≤ 1 + (n − 1)(2 + ρ)), summing over classes gives f ≤ 1 + (n − 1)(2 + Σ_c |Q_c|(ROUTE_c + CYC_c + TOG_c)) + (the ρ events at cycle nodes
  that are Odd choice vertices). READING, not a new statement: it is linear in k = |Q_c| GIVEN the class's ROUTE / CYC / TOG events, and it is
  what replaces R61's product. Whether CHOSEN's ρ_q and R56's ρ count the same transitions term by term I have not checked line by line; this
  is an assembly for orientation, not a claim to sign.
- So the k-dependence is not in the chain structure; it is in the number of ROUTE events (a terminal's class exit path changes). §2-§4 look
  inside ROUTE.

## 2. Lemma OFFSET-MONO (PROVED, every game)
Setting. A phase P of N5 (τ, λ constant), a cycle node c, U := U_c, Q := the Odd vertices of out-degree ≥ 2. M_t(z) := the path weight of Ξ_t(z)
in class c (RESULTS R56's κ first component; wt(v) = sgn(v)·2^rank(v) above rank(c), else 0). Facts used, all in RESULTS R56 (a), (d) (docs/RESULTS.md
l. 2851, 2858), on every game, in the form of docs/si/N5-ROOT-box20.md §0: (Aκ) for z ∈ U ∖ {c}, next_t(z) ∈ U and M_t(z) = wt(z) + M_t(next_t z),
where next_t is the honest successor (σ_t at Even, σ̄_t at Odd vertices); (M1κ) for valuations with cycle node c, x ⊴ x′ implies Mx ≤ Mx′;
κ-Y-FORM_D (R56 (d)): for q ∈ Q ∩ U, q ≠ c, on no honest cycle at t, κ_t(q) = κwt(q) + min over Y^q_t := {y ∈ succ(q) ∩ U : y's honest play at t
avoids q} of κ_t(y), the minimum attained at σ̄_t(q), with κ comparing M first. SPEC: at an in-phase transition σ_{t+1}(x) ∈ {σ_t(x)} ∪ Iσ_t(x)
for every Even x (S4a's arena restricts Even x to these edges; S4c switches only along Iσ_t), and τ is constant.
For q ∈ Q ∩ U ∖ {c}: par_t(q) := the first vertex of Q ∖ {q} on q's honest play at t strictly before c (none: q is DIRECT). For z whose honest play
at t meets p before c: seg_t(z, p) := M_t(z) − M_t(p) (by (Aκ) iterated, the sum of wt over the vertices of z's play before p).
Statement. Let t → t + 1 be an in-phase transition, q ∈ Q ∩ U ∖ {c} on no honest cycle at t, and p := par_t(q) = par_{t+1}(q) ≠ none. Assume NO
ENTRY: (E1) y2 := σ̄_{t+1}(q) is p, or y2's honest play at t meets p before c and avoids q; (E2) every vertex strictly between y2 and p on q's
honest play at t + 1 has an honest play at t that meets p before c. Then seg_{t+1}(q, p) ≥ seg_t(q, p).
Proof.
- Step 1 (the segment). For every vertex x of q's (t + 1)-play from y2 up to p: seg_{t+1}(x, p) ≥ seg_t(x, p). Induction backwards from p
  (seg = 0 at both times). Let x ≠ p, x′ := next_{t+1}(x), the next vertex of the segment; by induction seg_{t+1}(x′, p) ≥ seg_t(x′, p) (x′ = p, or
  x′ satisfies (E2)). By (Aκ) at t + 1, seg_{t+1}(x, p) = wt(x) + seg_{t+1}(x′, p) ≥ wt(x) + seg_t(x′, p).
  - x Odd: x ≠ q (the play is simple before c) and x ∉ Q (p is the first vertex of Q ∖ {q}), so x has one successor and next_t(x) = x′; (Aκ) at t:
    seg_t(x, p) = wt(x) + seg_t(x′, p).
  - x Even, σ_{t+1}(x) = σ_t(x): the same.
  - x Even, switched: (x, x′) ∈ Iσ_t, i.e. Ξ_t(x′) ▷ Ξ_t(σ_t x). x's t-play meets p before c ((E2), or x = y2 by (E1)), so σ_t(x)'s does (or σ_t x
    = p); x′'s does too ((E2), or x′ = p). Both values have cycle node c, so (M1κ) gives M_t(x′) ≥ M_t(σ_t x), i.e. seg_t(x′, p) ≥ seg_t(σ_t x, p), and
    seg_t(x, p) = wt(x) + seg_t(σ_t x, p) ≤ wt(x) + seg_t(x′, p).
  In all cases seg_{t+1}(x, p) ≥ seg_t(x, p).
- Step 2 (q's choice). By (Aκ) at t + 1 and Step 1 at y2: seg_{t+1}(q, p) = wt(q) + seg_{t+1}(y2, p) ≥ wt(q) + seg_t(y2, p). At t, q is on no
  honest cycle, so by κ-Y-FORM_D the minimum of κ_t over Y^q_t is attained at y1 := σ̄_t(q), and κ compares M first: M_t(y1) ≤ M_t(y) for every
  y ∈ Y^q_t. By (E1), y2 ∈ Y^q_t (or y2 = p, whose play avoids q at t since p's play at t is a suffix of q's simple play). q's t-play is q, then
  y1's play, which meets p; so seg_t(y1, p) ≤ seg_t(y2, p), and seg_t(q, p) = wt(q) + seg_t(y1, p) ≤ wt(q) + seg_t(y2, p) ≤ seg_{t+1}(q, p). □
- Remarks. (i) The proof is the Bellman-Ford monotonicity of BF-F_D (docs/si/N5-ROOT-box20.md §2) restricted to a region with a fixed sink p
  instead of c: Even vertices only take Ξ-improving edges, and inside one region Ξ-improving means "larger offset to the sink". It does not need
  FREEZE-A's "A does not grow" over a run, only (E1)-(E2) at the one transition. (ii) A RESET (the offset falls with p fixed) therefore needs an
  ENTRY (a vertex of the new segment, or q's new option, joined p's region at that transition) or q on an honest cycle at t. That is exactly
  where R61's odometer would have to act.
- DATA (experiments/new/box48/reset.py; RESET = offset falls with p fixed; ENTRY = (E1) or (E2) fails; RESET_NOT_ENTRY_V must be 0; CHAIN_V =
  an M(q) change at a transition with NO event on q's chain (no parent change, no offset change, no entry at any vertex of the chain q, par(q), …,
  and no M change at its direct end), must be 0 since M(q) = Σ offsets + M(direct end) by (Aκ)):
  | sample | phases | checks (p fixed) | RESET | ENTRY | RISE | PARCHG | M(q) changes | CHAIN_V |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | lib41 (experiments/new/box41/lib41.txt), n ≤ 34, S3 + 2 random, seed 7 (out/reset_lib41_n34_k2.txt) | 746 | 853 | 0 | 0 | 17 | 106 | 1,847 | 0 |
  | nep90 / nep76 / long121 from their starts (out/reset_long6.txt) | 1 / 1 / 1 | 170 / 171 / 106 | 0 | 0 | 4 / 32 / 6 | 53 / 60 / 48 | 268 / 155 / 116 | 0 |
  | §12's climbed n = 48 games (same file) | 2 / 1 / 1 | 494 / 455 / 507 | 0 | 0 | 2 / 9 / 6 | 167 / 88 / 103 | 520 / 303 / 285 | 0 |
  Controls: MUT=1 (the chain check ignores parent changes) CHAIN_V 55 on nep90, 54 on long121; MUT=2 (ENTRY tested against another Odd choice
  vertex of the class instead of p) ENTRY 161 on nep90. ENTRY never occurred unmutated, so the lemma's hypothesis held at every check; the
  lemma's content (RESET only at an ENTRY) is untested by a real ENTRY (thin spot).

## 3. Exit changes carry the count (READING + DATA)
- A ROUTE event at q (CHOSEN's terminology: q's class exit path changes) is either an EXIT CHANGE (par(q) changes, my PARCHG), or a same-exit
  change. By OFFSET-MONO a same-exit change without entry never lowers the offset; it raises it (RISE) or keeps it (a length-only change).
- DATA (§2's table): same-exit offset rises are rare (17 on lib41; 2-32 on the long instances) against exit changes (106 on lib41; 48-167 on the
  long instances). On nep90's root-and-relay structure (N5-NCONF §8, P-N5-ROOT) almost all route activity is exit changes.
- READING. So the k-dependence that R61's product expresses is, in data, the number of EXIT CHANGES per phase: how often an Odd choice vertex
  switches between options that leave its region through different Odd choice vertices (relays) or through c. That is the relays' ping-pong of
  L-SI's P-N5-ROOT and L-RED R88, and it is L-SI 17's current work (G_c, X_u per fallback-free run). I do not duplicate that count here.

## 4. A lower-envelope view of σ̄(q) (READING + DATA; the route is not closed)
- σ̄_t(q) is the κ-argmin over q's options (R56 (d)). Over a phase this is the lower envelope of d_q functions of time. If any two options of q
  change their relative order at most s times in the phase, the sequence of argmins has no alternation a … b … a … of length s + 2, a
  Davenport-Schinzel sequence of order s on d_q symbols; for s = 1 every symbol occupies one block, so σ̄(q) changes at most d_q − 1 times
  (elementary). For general s the DS bound λ_s(d_q) (near-linear in d_q for fixed s) would apply; that is a cited result I have NOT opened, so
  it is not used here (L-LIT would open a source before any use).
- DATA (experiments/new/box48/swaps.py, out/swaps_long4.txt): pairwise order swaps between two options of one q inside one phase reach 15
  (nep90, root 0, d = 18, 66 changes of σ̄(0)), 15 (nep76), 11 (long121), 22 (§12's climbed nep90 descendant). So the order parameter s is not
  small on long phases, and the envelope view needs a bound on pairwise swaps, which is the same difficulty (two options swap when their exits'
  values rise at different times). READING: the route is not closed; it reformulates exit changes as order swaps of option pairs.

## 5. Other fields: what transfers and what does not (READING; no cited result is used)
- Policy iteration as LP simplex and shadow-vertex counts: a shadow-vertex bound counts the vertices of a 2-dimensional projection of a
  polytope. A phase of N5 is a one-parameter family only if the option values move along a common parameter; here each exit's value moves on
  its own schedule (§4: up to 22 swaps per pair), so there is no single parameter to project onto. Does not transfer as such; it would need a
  potential that orders all option values at once. Sources not opened; not used.
- Tropical geometry (regions of an arrangement): N5's values are tuples compared lexicographically with 2^rank weights, i.e. a max-plus
  structure; counting regions of an arrangement of k tropical hyperplanes is polynomial for fixed k and exponential in the dimension. That is
  the same exponent in k as R61. Does not remove the k-dependence by itself.
- Discrete convex analysis (L♮ / M♮-convex functions, steepest descent bounded by an L∞-diameter): would give a count additive over the k Odd
  choice vertices if Odd's best-response problem over configurations were L♮-convex in some ordering of each q's options. OFFSET-MONO is the kind
  of monotonicity such a structure would need (offsets to a fixed exit only rise), but the exit changes (§3) break any fixed ordering of q's
  options (nep90: 15 swaps of one pair). CONJECTURE-level at best; nothing stated.
- The common thread (READING): every route that removes the product needs either a fixed order on each q's options over a phase (swaps bounded)
  or a charge of exit changes to a quantity counted once per vertex. The data say exit changes are many (66 for nep90's root) but each is
  preceded by a value rise at a relay (CHOSEN): the open question is whether those rises can be charged without multiplying along chains.

## 6. OPEN
- (1) Exit changes per phase (PARCHG), the count left by §1-§3; L-SI 17's G_c / X_u work is the bound side of the same quantity.
- (2) A real ENTRY instance, to test OFFSET-MONO's content (no ENTRY occurred in data).
- (3) Pairwise option swaps per phase (§4).
- (4) The n-scaling of QP_c on long phases beyond n = 80 (§0, DATA only).

## 7. (a) closes: OFFSET-MONO without the ENTRY hypotheses; packet P-N5-OFFMONO-box49 (PROVED; DATA; Lead's routing of 16:41Z; written 16:5xZ by date -u)
- The lemma of §2 holds with NO region hypothesis: at every in-phase transition, for q ∈ Q, q ≠ c, on no honest cycle at t, with p := q's routing
  vertex at t + 1 (par_{t+1}(q), or c), κ_{t+1}(q) − κ_{t+1}(p) ⪰ κ_t(q) − κ_t(p) in κ = (M, s_c·ℓ). Step 1 never needed (E2) (λ is constant on the
  phase, so every vertex of q's new path is in U_c and its t-offset to p is defined whether or not its t-play met p); Step 2's remaining case
  (y2's t-play passes q, "Case L") closes by Odd's optimality (Lemma S (a)) on the cycle Z = q → … → q: κwt_c(Z) ⪰ 0. So ENTRY is irrelevant and R61's
  odometer reset is impossible at every level on no honest cycle. §2's (E1)-(E2) form is superseded.
- Corollaries CHAIN-SUM (a κ change of q is a sum of non-negative level rises along its (t+1)-chain) and CHAIN-COUNT (per vertex, κ changes ≤
  |CYC_c| + Σ_x D·(|EXIT_x| + |CYC_c| + 1) when offsets take ≤ D values on fixed-exit pieces). Answer to the Lead's question: the product over chain
  levels is gone; the exit changes EXIT_x (and CYC) take its place, so polynomial in n and k follows exactly when exits per phase are polynomial.
- Full statements, proofs, premises, quotes and data: docs/new/P-N5-OFFMONO-box49.md (frozen at this push). DATA (offmono2.py): 0 violations in
  15,741 checks (lib41 n ≤ 34 and seven long instances incl. the n = 80 climb), 25 Case L checks, 590 parent-changed checks; controls bite.
