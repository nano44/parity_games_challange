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

## 8. CYC_c refined to cycle changes, and the cycle changes counted (PROVED, every game; DATA; Lead's routing of 16:56Z; written 17:01Z by date -u)
Setting as P-N5-OFFMONO-box49 §0 (frozen, sha1 d9705ac6…; not edited). Z_t(c) := c's honest cycle at t as a sequence from c (the honest play from c
up to its return). ZCH_c := the in-phase transitions of a run J with Z_t(c) ≠ Z_{t+1}(c).
- Remark Z-CONST (PROVED, elementary). If Z_t(c) = Z_{t+1}(c), then for every x on it, κ_t(x) = κ_{t+1}(x) (a valuation is a function of the play),
  and for x ∈ Q on it, par_t(x) = par_{t+1}(x) and off(x; par(x)) is unchanged. So in OFFSET-MONO's corollaries the CYC transitions at which c's
  cycle does not change contribute nothing.
- Corollary CHAIN-COUNT′ (PROVED). P-N5-OFFMONO's CHAIN-COUNT holds with CYC_c replaced by ZCH_c (x-pieces cut at EXIT_x ∪ ZCH_c): on a piece,
  either x is on no honest cycle at the source (OFFSET-MONO) or x lies on c's unchanged cycle (Z-CONST, offset constant). The proof is otherwise
  CHAIN-COUNT's, with CHAIN-SUM's terms at unchanged-cycle levels equal to (0, 0).
- Lemma ZCH-COUNT (PROVED, every game). In a phase P and class c: ZCH_c ≤ (n − 1)·(|U_c| − 1) + n + TIE_c + ODDC_c, where TIE_c := the cycle
  changes at which every vertex v ≠ c of Z_{t+1}(c) with next_{t+1}(v) ≠ next_t(v) is Odd with κ_{t+1}(v) = κ_t(v), and ODDC_c := the cycle changes
  at which c ∈ Q and σ̄(c) changes and no other vertex qualifies.
  Proof. Let t → t + 1 change c's cycle and let N := {v ∈ Z_{t+1}(c), v ≠ c : next_{t+1}(v) ≠ next_t(v)}.
  - Every vertex of Z_{t+1}(c) other than c has κ_{t+1} = (0, s_c·ℓ) with 1 ≤ ℓ ≤ n − 1 (its play to c runs along the cycle, all below c in rank,
    so the path set is empty).
  - If some v ∈ N has κ_{t+1}(v) ≻ κ_t(v) (STRICT): charge the transition to v. κ(v) is non-decreasing on P ((M2κ)), so the transitions at which
    κ(v) rises strictly TO a value (0, s_c·ℓ), ℓ ∈ [1, n − 1], are at most n − 1. Over v ∈ U_c ∖ {c}: ≤ (n − 1)(|U_c| − 1).
  - Every Even v ∈ N is STRICT: by (SW), (v, x′) ∈ Iσ_t with x′ := next_{t+1}(v), so κ_t(x′) ≻ κ_t(next_t v) ((M1κ); both in U_c), and κ_{t+1}(v) =
    κwt_c(v) + κ_{t+1}(x′) ⪰ κwt_c(v) + κ_t(x′) ≻ κ_t(v) ((Aκ), (M2κ)). So a non-STRICT change has N consisting of Odd vertices with unchanged κ
    (TIE_c) or N = ∅, i.e. only c's own successor changed.
  - N = ∅ and c Even: let ψ_t := κ_t(next_t c). next_t(c) lies on c's cycle, so ψ_t = (0, s_c·ℓ) with 0 ≤ ℓ ≤ n − 1. ψ is non-decreasing on P: where
    next(c) is unchanged by (M2κ); where c switches, by (SW) and (M1κ) as for v above, strictly. So such transitions number ≤ n − 1 ≤ n.
  - N = ∅ and c Odd (c ∈ Q, σ̄(c) changes): ODDC_c. □
- So the CYC part of the remaining count is polynomial except for TIE_c and ODDC_c (Odd vertices re-routing on c's cycle with unchanged κ, and the
  cycle node's own Odd choice; these are R61 (f)'s tie_q and cyc_q kinds). OPEN: TIE_c, ODDC_c per phase.
- DATA (experiments/new/box48/cyc.py; out/cyc_lib41_n34_k2.txt, out/cyc_long7.txt, out/cyc_long2.txt): lib41 n ≤ 34, S3 + 2, 746 phases, 6,752
  transitions: CYC (old sense, any q on c's cycle) sums to 457 and reaches 25 = a whole phase (kw25_n32: the Odd choice vertex sits on an unchanged
  cycle all phase, Z-CONST's case); cycle changes: STRICT 50, TIE 3, c-only 80 (c Even 85 / c Odd 1 moves of c in all, some together with STRICT),
  ZCH_OTHER_V 0; max ZCH per phase 6. nep90, nep76, long121 and the four climbed games: c's cycle never changes (ZCH 0); old-sense CYC 0 except 2 on
  the n-48 nep90 descendant.

## 9. Note: the term-by-term matches the Lead asked for (READING; elementary facts marked; not a packet)
(a) R61 (b) SAT-k against CHAIN-COUNT's "≤ D values on every x-piece". NOT an exact match. SAT-k (RESULTS l. 3119-3121) gives κ_t(x) ∈ S_{x,p} + κ_t(p),
|S_{x,p}| ≤ d_x, only at states t later than the w_c-th fallback of the p-run Θ_p containing t (and t > g_{w_c}, which FBK-N1 says is unused). A
p-run ends whenever κ(p) changes, so inside one x-piece (p fixed) the states are partitioned by p's runs, and at the EARLY states of each p-run
(before its w_c-th fallback) SAT-k says nothing. OFFSET-MONO still makes off(x; p) non-decreasing across the whole piece, so the LATE states of
the piece carry at most d_x distinct offsets in total (PROVED, elementary: a monotone sequence whose late terms lie in a d_x-set), but the early
states can carry other values in between. So CHAIN-COUNT applies with D = d_x to the late states only, and its count of κ(q)-changes then needs,
in addition, the transitions at early states of some level's p-run: one early segment per p-run, i.e. per change of κ(p). That re-introduces
a dependence on the PARENT's change count (a recursion, not yet a product, since each early segment is charged once to a change of κ(p), not to
each value). Whether that recursion closes linearly (each κ(p)-change is itself a counted event of the same class) is the next step; I have
not done it. R61's own V_q counts values at late FALLBACKS only, which avoids early segments by construction.
(b) RESULTS R72's ROUTE / RELAY against EXIT ∪ same-exit offset rises. NOT the same partition. R72: a ρ event at q (q on no honest cycle at t,
t + 1) is ROUTE if SOME successor y ∈ succ(q) ∩ U_c changes its class exit path or exit, RELAY otherwise (P-N5-CHOSEN l. 25-27). Mine look at
q's CHOSEN option only (par(q) = the exit of σ̄(q), which is CHOSEN's chosen exit). Two elementary facts:
- (b1) (PROVED, elementary, up to ties) a same-exit offset rise at q (par fixed, off(q; p) strictly up) is a ROUTE event: if no successor's class
  exit path or exit changed, both chosen options y1, y2 exit at p with fixed paths, their offsets to p are fixed, κ-Y-FORM_D at t picked the
  smaller (y1), so at t + 1 Odd's minimum is again y1 unless the two offsets tie; so off(q; p) cannot rise. Ties excepted.
- (b2) an EXIT change at q can be a RELAY event: q switches between two options with unchanged paths and different exits because the exits'
  values moved (the ping-pong of N5-NCONF §8 / P-N5-ROOT). So EXIT ⊄ ROUTE; R72 charges those to the chosen exit's own ρ event (CHOSEN), mine
  counts them as EXIT_q. The two decompositions are complementary, not nested; neither yields a new statement here.

## 10. Pointer (successor 29): §8 is frozen as docs/new/P-N5-OFFMONO-add-box49.md
Remark Z-CONST, Corollary CHAIN-COUNT′ and Lemma ZCH-COUNT are restated with full proofs there; that addendum governs. Differences (its §5):
the cut set is ZC_c = ZCH_c ∩ CYC_c (KPOLY's ZCH_c form follows); TIE requires N ≠ ∅; the bound is (n − 1)|U_c| + TIE_c + ODDC_c. DATA zch.py: 0
violations on lib41 n ≤ 34 (746 phases, 133 cycle changes: STRICT 50, TIE 3, CEVEN 79, ODDC 1) and seven long instances; sign and exit controls bite.

## 11. The cycle part of the count is polynomial without TIE_c / ODDC_c (PROVED, every game; DATA; queue item 3 (a); written 17:48Z by date -u)
Setting as P-N5-OFFMONO-box49 §0 and P-N5-OFFMONO-add-box49 §0 (both frozen; not edited). F := {(0, s_c·ℓ) : 1 ≤ ℓ ≤ n − 1}; A_t := {z ∈ U_c ∖ {c} :
P(Ξ_t z) = ∅} (the path-free vertices of the class). By (INJ) (R56 (a)), for z ∈ U_c ∖ {c}: z ∈ A_t ⇔ κ_t(z) ∈ F (M = 0 ⇔ P = ∅; ℓ ≥ 1 as z ≠ c).
FT_c := the in-phase transitions of P at which some z ∈ U_c ∖ {c} has κ_t(z) ≠ κ_{t+1}(z) with κ_t(z) ∈ F or κ_{t+1}(z) ∈ F (an F-touching change).
- Lemma FT-COUNT (PROVED, elementary). |FT_c| ≤ 2(n − 1)(|U_c| − 1). Proof: charge each FT transition to one z with an F-touching change. κ(z) is
  non-decreasing on P ((M2κ)), so each value of F is left at most once and entered at most once: z takes at most 2|F| = 2(n − 1) charges. □
- Remark FT-CONST (PROVED, elementary). At a transition not in FT_c: A_t = A_{t+1}, κ_t = κ_{t+1} on A_t ∪ {c}, and for x ∈ Z_t(c), x ≠ c, and
  p := par_{t+1}(x): off_{t+1}(x; p) = off_t(x; p). Proof: z ∈ A_t has κ_t(z) ∈ F, so (no F-touching change) κ_{t+1}(z) = κ_t(z) ∈ F, z ∈ A_{t+1};
  symmetrically; κ(c) = (0, 0) (A0κ). x ∈ A_t by (CYC-SHAPE), so x ∈ A_{t+1}; p lies on x's honest play at t + 1 (a suffix of a path-free play) or
  p = c, so p ∈ A_{t+1} ∪ {c} = A_t ∪ {c}; both κ-values are unchanged. □ No tie-break of SPEC S1 is used.
- Corollary CHAIN-COUNT″ (PROVED). P-N5-OFFMONO-add-box49 §2 (CHAIN-COUNT′, both forms) holds with ZC_c replaced by ZC″_c := CYC_c ∩ ZCH_c ∩ FT_c,
  and |ZC″_c| ≤ min(|ZC_c|, 2(n − 1)(|U_c| − 1)). Proof: only Step A changes. At a transition not in ZC″_c and a level x on an honest cycle at t
  (x ∈ Z_t(c) by (CYC-ID), so the transition is in CYC_c): it is not in ZCH_c (Remark Z-CONST: equality) or not in FT_c (Remark FT-CONST: equality).
  Off-cycle levels: Lemma OFFSET-MONO. The rest of the proof is CHAIN-COUNT′'s word for word. □
  So per phase and class, for every q ∈ Q ∩ U_c ∖ {c}: (κ(q)-changes) ≤ 2(n − 1)(|U_c| − 1) + Σ_x D·(|EXIT_x| + 2(n − 1)(|U_c| − 1) + 1). The cycle
  part is polynomial UNCONDITIONALLY; TIE_c and ODDC_c are no longer needed on this route. What remains: EXIT_x per phase (L-SI 18) and D.
- Lemma PF-CHOICE (PROVED from SPEC S1's procedure, as implemented in si.py Engine.evaluate l. 78-205; a reading of exact tie-breaks, so
  referees should check it against the code). For an Odd x ∈ A_t: σ̄_t(x) is the argmin over y ∈ succ(x) ∩ (A_t ∪ {c}) of (κ_t(y), tb_t(y)), where
  tb(y) := y's index if c is even, and the index sequence of y's honest path read from c (empty for c) if c is odd. Proof sketch: (i) path-free
  ⇒ rank(x) < rank(c) (a vertex of rank > rank(c) carries its own bit). (ii) In S1 (iii)'s restricted graph, x keeps exactly its edges to
  path-free successors in R = U_c (and to c): at an Even-liked u, x ∈ M (else x would get bit u), so restrict(x, M) cuts exactly the edges to
  vertices outside M, which get bit u; a path-free y is in M and kept; at an Odd-liked u, x ∉ M, and any edge x → y with y ∈ M still present
  would put x into M (reach(u, c) runs over predecessors), so such edges are already cut; x's edges are never touched there. (iii) c even:
  longest path, first strict maximum in increasing index order: the least-index y maximising ℓ(y), i.e. minimising κ(y) = (0, −ℓ(y)). (iv) c
  odd: BFS over predecessors in increasing index order; path-free vertices are discovered only from path-free vertices, so within a layer they
  are ordered by (position of their BFS parent, index), i.e. by the lexicographic order of tb; the BFS parent is the earliest-ordered
  successor at distance ℓ − 1, i.e. the argmin of (κ, tb). □
- Corollary TIE-CHARGE (PROVED from PF-CHOICE). At a transition not in FT_c, next_{t+1} = next_t on A_t. Proof: A and κ on A ∪ {c} are unchanged
  (FT-CONST); an Even z ∈ A switching would raise κ(z) strictly (addendum §3, (SW) + (M1κ) + (M2κ)), an F-touching change; for Odd z, induction
  on ℓ: the κ-minimal options of z have ℓ = ℓ(z) − 1, their tb is fixed by next on smaller ℓ (induction), so the argmin of PF-CHOICE is the same. □
  So every STRICT and every TIE transition is in FT_c: STRICT_c + TIE_c ≤ 2(n − 1)(|U_c| − 1). ODDC_c (c's own stack-DFS choice, S1 (v)) is NOT
  bounded by this: c's DFS runs over all alive vertices of rank < rank(c), including non-path-free vertices of U_c whose Even switches are not
  F-touching. ODDC_c stays OPEN, and by CHAIN-COUNT″ it is not needed.
- DATA (experiments/new/box48/ft.py, tie.py, tieclimb.py; out/ft_*.txt, out/tie2_*.txt, out/tieclimb/):
  - ft.py (FT-COUNT: FTB_V; FT-CONST: OC_V; CHAIN-COUNT″: PM_V, CC_V, CCD_V): lib41 n ≤ 34, S3 + 2, seed 7: FT 1,102, max per phase and class 29;
    CYC 432; cut CYC ∩ FT (MUT=0) 270 transitions, cut CYC ∩ ZCH ∩ FT (MUT=5, the stated ZC″) 42 (against ZC = CYC ∩ ZCH 59 in the addendum);
    every check 0 in both. Seven long instances (MUT=0 and MUT=5): FT ≤ 6, ZC″ 0, all checks 0. Controls
    MUT=1 (no cut) and MUT=4 (one cut transition dropped) do not bite here, as in the addendum's MUT=1: the cut is needed by the proof, not shown
    necessary by data.
  - tie.py (PF-CHOICE: CHAR_V; TIE-CHARGE: FT_V; FT-COUNT: FTB_V): lib41: 2,523 characterisation checks, CHAR_V 0, FT_V 0 (1,102 transitions with
    an A or next change on A, all F-touching), FTB_V 0. Controls bite: MUT=1 (index tie-break for both parities) CHAR_V 1, MUT=2 (path-sequence
    tie-break for both) 55, MUT=3 (reversed index) 182. Events: the 3 TIEs (klcount_n16 / n18) all have c odd, v on Z_t(c), the old option's κ
    strictly up, the new option tied at t; the ODDC (u3ev_n16) has the old option's M rising to 8192.
  - tieclimb.py (4 climbs × 3,000 steps from u3ev_n16 / klcount_n16, n ≤ 24, objectives ODDC / TIE): best ODDC_c 1, best TIE_c 1 per phase and class;
    292,764 characterisation checks on climbed games, CHAR_V / FT_V / FTB_V 0.

## 12. Queue item 3 (b): §9 (a)'s recursion, measured; where the count really sits (READING; DATA; one DEAD guess; written 18:09Z by date -u)
- (i) PROVED (elementary, a re-reading of P-N5-OFFMONO-add §2's sum form): the κ(q)-count needs NO recursion over the chain. By CHAIN-COUNT″'s
  sum form, κ(q)-changes ≤ |ZC″_c| + Σ_{x ∈ Q_c} OR(x), OR(x) := the transitions at which off(x; par_{t+1}(x)) rises strictly (each κ(q)-change
  is charged to one level x of its chain and one transition, injectively in the transition). The sum is ADDITIVE over levels and the same
  for every q. §9 (a)'s recursion appears only if OR(x) is bounded THROUGH R61 (b) SAT-k, whose window is per p-run (one early segment per
  κ(p)-change); that recursion, OR(x) ≤ A_x + E·(κ(p)-changes + 1) with κ(p)-changes ≤ |ZC″| + Σ_{x′ above x} OR(x′), is exponential in the
  depth for every E ≥ 1 (OR(x_h) ~ (1 + E)^h). So it does NOT close linearly by itself; the way out is to bound OR(x) directly. ANSWER to (b): no.
- (ii) DATA (experiments/new/box48/orun.py; out/orun_lib41_n34_k2.txt, out/orun_long7.txt): per x-piece (cut EXIT_x ∪ ZC″) and p-run inside it.
  - R61 (b)'s late window is NEVER entered: LR = 0 (no strict offset rise after the w_c-th fallback of its p-run) in all 1,466 p-runs of lib41
    n ≤ 34 (S3 + 2, seed 7) and all p-runs of the seven long instances (nep90, nep76, long121, three climbed n-40 games, the n-80 snap). Every
    rise is EARLY. SAT-k's |S| ≤ d_x therefore bounds nothing that happens in these runs.
  - The rises sit at DIRECT levels (p = c, off(x; c) = κ(x)): lib41 2,282 of 2,300 rises (relayed levels: 18, at most 2 per p-run); nep90 95 / 99;
    long121 35 / 40; the n-80 snap 186 / 191; exception nep76 36 / 76 (relayed max 15 in one p-run). One p-run of a direct level carries up to
    51 rises (lev_l_x n 32, d_x 14, no fallback AT a rising transition), so "≤ d_x values per p-run" (HA) fails 102 times on lib41.
  - So the open quantity behind D is the number of κ-changes of DIRECT terminals inside a phase, mostly inside fallback-free runs (RESULTS R58
    (d) DIR bounds a direct terminal's κ only after the phase's w_c-th fallback, a window these phases also rarely reach).
- (iii) DEAD (successor 29's guess FRZ_c, a general-game form of RESULTS R50 (c) FRZ-U): "in a fallback-free run of a phase, M(κ(z)) is
  constant for every z ∈ U_c ∖ {c} from the run's (|U_c| − 1)-th transition on". Killed by experiments/red/so/instances/so_th_n32.pg (L-RED; sha1
  ae9126ad1bf963114bdd56b6e50c8c1cc571779e) from the S3 start: 31 late M-changes (out/frz_so_th_n32_S3.txt), one at a direct Odd choice vertex
  (z = 3, c = 5 even, w = 31, at position 31 of a 33-transition run, M −50331648 → 16777216). Same on pftheta_cex_n32 (53) and
  thclimb_n16_s12 (12). All violations on lib41 (frz.py: 128, 5 at direct terminals) are in classes with ONE Odd choice vertex, at positions w to
  w + 2. Obstruction: R50 (c) freezes the route ABOVE m* (the more relevant of c_θ and the W-frame's c_w), not above c; between c and c_w the
  path set may still move. The seven long instances have 0 late M-changes. OPEN: the right general-game frame (an m*_c per class).
- (iv) So the route to G-N5-TIME through OFFMONO + CHAIN-COUNT″ now needs, per phase: EXIT_x (L-SI 18), OR(x) at relayed levels (small in
  data) and the κ-changes of direct terminals (the bulk). The last is the multi-class analogue of what R50 / R51 settle on 𝒞^1O.
- (Successor 29) §11 is frozen, with full proofs and the code-level part separated, as docs/new/P-N5-OFFMONO-add2-box49.md; that addendum governs.

## 13. Record: QP_c on long phases (§0 and N5-NCONF §12 OPEN (1)) is answered by L-RED's R92 (DATA, not mine; written 18:24Z by date -u)
docs/red/R92-qpc-ladder.md (l-red 1e851da4, L-RED successor 22; opened, §1-§2): the LADDER family (experiments/red/ul/mkladder.py k [ent]), n = 3k + 12,
one phase with no fallback. D0 form: QP_c = k + 2 = D0, phase length k + 1; ENT form: QP_c = k, ENT = k − 1, N_ep = NCONF = k. One class (one
Bellman-Ford clock read by every gate), so not disjoint copies. Counted with this lane's qp.py unmodified; phrestrict.py (RESTRICT_H) holds,
its MUT=1 bites. So QP_c grows LINEARLY in n within one class, on phases of length ≈ n/3: not a long-phase growth law, and RESTRICT_H is a
reduction, not a size bound (Lead's reading of 18:03Z). §0's DATA (QP_c 36 at n 80) is consistent with it.

## 14. REFEREE's OFFADD-N2 closes: OFFSET-MONO needs no honest-cycle hypothesis, so CHAIN-COUNT needs no cut but EXIT (PROVED, every game; DATA; Lead's note of 18:25Z; written 18:34Z by date -u)
Setting and notation as P-N5-OFFMONO-box49 §0-§1 (frozen; not edited). REFEREE 15's addendum report (docs/referee/R-N5-OFFMONO-add.md, c2a97189;
relayed by the Lead, not yet opened by me: opened before any packet cites it) conjectures this as OFFADD-N2; its OFFMONO-N4 found that
dropping the hypothesis never bites at 4,006 cycle levels.
- Lemma OFFSET-MONO⁺ (PROVED). OFFSET-MONO holds for every q ∈ Q ∩ U_c, q ≠ c, at every in-phase transition, with no hypothesis on honest
  cycles: off_{t+1}(q; p) ⪰ off_t(q; p) for p := par_{t+1}(q).
  Proof. If q is on no honest cycle at t: OFFSET-MONO. Let q ∈ Z_t(c) (add1 (CYC-ID)). Step 1 of OFFMONO's proof (the path π from y2 := σ̄_{t+1}(q)
  to p, backwards induction with (Aκ) at t + 1, (SW), (M1κ)) never uses q's position at t, so off_{t+1}(q; p) ⪰ κwt_c(q) + κ_t(y2) − κ_t(p).
  By (Aκ) at t (q ≠ c), off_t(q; p) = κwt_c(q) + κ_t(y1) − κ_t(p), y1 := σ̄_t(q). It remains to show κ_t(y2) ⪰ κ_t(y1). y2 ∈ U_c (on q's t+1 play,
  λ constant), so y2's honest play at t reaches c's cycle Z_t(c), which contains q; so it meets q, either before c or not.
  - Case L1 (y2's t-play meets q before c). Exactly OFFMONO's Case L: ζ := that play up to q, Z := q → ζ → q avoids c, κ_t(y2) = κwt_c(Z) +
    κ_t(y1), and κwt_c(Z) ⪰ (0, 0) by Lemma S (a) and S1's reward order; that argument does not use q's position.
  - Case L2 (y2's t-play meets c before q). Let τ″ := σ̄_t with q's choice replaced by y2, and V″ := V_{σ_t,τ″}. Under (σ_t, τ″) the play from q
    is q → y2 → (y2's t-play up to c) → (Z_t(c) from c up to q) → q: y2's t-play up to c avoids q (Case L2) and Z_t(c) from c to q uses only
    vertices whose choice is unchanged. Its cycle consists of q, y2's t-path to c, and the arc of Z_t(c) from c to q; the latter has ranks
    ≤ rank(c) (c is the top of Z_t(c)). Lemma S (a) (RESULTS R18 (d), every game by R57 (a), Ξ_t optimal under 1E-N3): Ξ_t(q) ⊴ V″(q).
    - If P(Ξ_t y2) ≠ ∅: the top u* of the new cycle is the top of P(Ξ_t y2), rank(u*) > rank(c). S1's order compares rewards first and
      rewards are injective, so reward(u*) > reward(c); an odd u* of rank > rank(c) has reward −p′(u*) < min(p′(c), −p′(c)) ≤ reward(c), so u* is
      even, and M_t(y2) = wt_c(P(Ξ_t y2)) > 0 (the top power dominates). κ_t(y1) has M = 0 (y1 lies on Z_t(c) or is c; add1 (CYC-SHAPE)), so
      κ_t(y2) ≻ κ_t(y1).
    - If P(Ξ_t y2) = ∅: the new cycle's top is c, and V″(q) = (c, ∅, 1 + ℓ_t(y2)) = q ⊕ Ξ_t(y2) (rank(q) < rank(c), q path-free). Ξ_t(q) ⊴ V″(q)
      with equal cycle nodes is κ_t(q) ⪯ κwt_c(q) + κ_t(y2) by (M1κ), i.e. κ_t(y1) ⪯ κ_t(y2) with (Aκ). □
- Corollary CHAIN-COUNT‴ (PROVED). For a run J of in-phase transitions and the class c, with x-pieces cut at EXIT_x ONLY: for every
  q ∈ Q ∩ U_c ∖ {c}, κ(q)-changes in J ≤ Σ_{x ∈ Q ∩ U_c ∖ {c}} (|EXIT_x| + Σ_π (v_x(π) − 1)) ≤ Σ_x D·(|EXIT_x| + 1). Proof: CHAIN-SUM with every
  term ⪰ (0, 0) by OFFSET-MONO⁺; add1 §2's charging with an empty cut set. □ So the CYC / ZCH / FT machinery of add1 and add2 is not needed
  for the count; their lemmas stay true (and FT-COUNT, PF-CHOICE stand on their own).
- DATA (experiments/new/box48/offmono3.py = offmono2.py with the hypothesis dropped; out/offmono3_lib41_n34_k2.txt, _MUT.txt, out/offmono3_long7.txt):
  lib41 n ≤ 34, S3 + 2, seed 7: 7,689 checks, 471 with q on an honest cycle at t (all Case L2; L1 never occurs), V_Kc 0, V_M 0. Controls bite
  at on-cycle checks too: opposite length sign V_Kx_ONCYC 25; MUT=1 (p off q's play) V_Kc_ONCYC 51. Seven long instances: 0 violations (2
  on-cycle checks). This also explains why the no-cut controls of add1 (MUT=1) and add2 (MUT=1, MUT=4) never bit.
