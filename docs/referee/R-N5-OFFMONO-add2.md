# R-N5-OFFMONO-add2: REFEREE report on addendum 2 P-N5-OFFMONO-add2 (L-NEW box 49: Fact (A-F), Lemma FT-COUNT, Remark FT-CONST, Corollary CHAIN-COUNT″; code-level Lemma PF-CHOICE, Corollary TIE-CHARGE; every game)
Referee: REFEREE (successor 16), Opus 5.5 (owner ruling D15). FIRST referee (Lead queue of 18:43Z / 18:52Z by date -u, item 1).
- Object and pin: docs/new/P-N5-OFFMONO-add2-box49.md, sha1 f2d123ef6ebbb71408dc25b503b78edc085cbf9a, 157 lines, author L-NEW successor 29:
  the same sha1 on my tree, at the l-new freeze 6ef3dd25 and at the trunk pin d5ad0929 (an ancestor of HEAD). Quote base 278616c6.
- Written 2026-10-26T19:05Z-19:13Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ file on add2 on my tree, on trunk or on origin/claude/referee-2 (re-listed in the same turn;
  0 / 0 / 0 at 19:09Z). No lane code run as a checker (experiments/new/box48/ft.py, tie.py, tieclimb.py, quotecheck2.py neither executed
  nor imported). experiments/si/si.py IS executed, as the OBJECT of the code-level §4 (its Engine.evaluate is what PF-CHOICE is about),
  never as a checker. D1.
- Premises read against their text: RESULTS R38 (a) KEY (l. 1825), R56 setting and (a) (l. 2840, 2851), (SW) (l. 3768-3769);
  P-N5-FBPOLY-box41 §0.3 (M2κ), (INJ) (l. 97-98); P-N5-OFFMONO-box49 §0-§2 (κ, par, off, κ-Y-FORM_D, OFFSET-MONO, CHAIN-SUM, EXIT_x, CYC_c);
  P-N5-OFFMONO-add-box49 §0-§3 (Z_t(c), ZCH_c, ZC_c, (CYC-ID), (CYC-SHAPE), Z-CONST, CHAIN-COUNT′ with Step A, ZCH-COUNT's kinds); SPEC
  docs/new/N5-ssi-global.md S1 (l. 33-44); experiments/si/si.py l. 78-205, read line by line.
- Quotes and pins: all 23 curly-quoted passages of §8 verbatim at 278616c6, each ending at its cited line (scratch/fbc_quotes.py). Pins
  N5-ssi-global.md 66fde9ef, si.py e688b963, P-N5-OFFMONO-box49.md d9705ac6, P-N5-OFFMONO-add-box49.md 5911aba8, P-N5-FBPOLY-box41.md
  de244dcd: at 278616c6 and on my tree, match.
- Tool: scratch/add2_probe.py (own engine rl_engine; offmono_probe's κ and par; zch_probe's Z_t(c); checks in §5). Logs scratch/add2_logs/.

## Verdicts (sign-off line per item)
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §0 | Fact (A-F) | SIGNED |
| §1 | Lemma FT-COUNT | SIGNED (note ADD2-N1: the per-vertex count is ≤ n, sharper than 2(n − 1)) |
| §2 | Remark FT-CONST | SIGNED |
| §3 | Corollary CHAIN-COUNT″ (Step A″, sum form, D form, the |ZC″_c| bound, the closing line) | SIGNED (a REDUCTION: EXIT_x and D are not bounded here, as the packet says) |
| §4 | Lemma PF-CHOICE (code-level, against si.py e688b963) | SIGNED (code read line by line; executed on 75,525 states, §5) |
| §4 | Corollary TIE-CHARGE | SIGNED (note ADD2-N2: the Even step needs x′ ∈ U_c from (Aκ), not from add1's "on Z_{t+1}(c)") |
| §4 | ODDC remark; §5 READING; §6 data; §7 open | not signed (as briefed); the READING's "ZC″_c ⊆ ZC_c" is true by definition |
No gap. Notes ADD2-N1..N4. Nothing here bounds EXIT_x, D, ODDC_c or N5's running time; not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. (A-F), FT-COUNT, FT-CONST, re-derived (parentheticals checked one by one)
- (A-F) ✓. κ_t(z) = (signed weight of P(Ξ_t z), s_c·ℓ); by (INJ) the weight is 0 iff the set is empty ✓; ℓ ≥ 1 (z ≠ c) ✓; "ℓ ≤ n − 1 since the
  play to c is simple" ✓. Both directions ✓.
- FT-COUNT ✓. Charging each FT_c transition to one z with an F-touching change ✓; κ(z) non-decreasing over the states of P by (M2κ) ✓; "(after
  it leaves v, κ(z) ≻ v forever)" ✓ and "(after it reaches v from below, it is never below v again)" ✓: so each v ∈ F is the source of ≤ 1
  and the target of ≤ 1 change of κ(z) ✓; 2|F| = 2(n − 1) per z ✓; |U_c| − 1 vertices ✓. ADD2-N1: F is exactly the set of κ-values with first
  component 0 (for z ≠ c), a contiguous block of the lexicographic order, so a monotone κ(z) enters F at most once, moves inside it at most
  |F| − 1 times and leaves it at most once: ≤ n F-touching changes per z. Data: at most 7 per vertex per phase (§5).
- FT-CONST ✓. A_t = A_{t+1} both ways via (A-F) ✓; κ(c) = (0, 0) (A0κ) ✓; x ∈ Z_t(c) ∖ {c} is path-free by (CYC-SHAPE) ✓; p = par_{t+1}(x) lies
  on x's honest play at t + 1 before c, or p = c ✓; "(P of a vertex on the play is the part of P(Ξ_{t+1} x) after it, which is empty)" ✓,
  and those vertices lie in U_c (λ constant on the phase), so p ∈ A_{t+1} ∪ {c} = A_t ∪ {c} ✓; κ(x), κ(p) unchanged, so off(x; p) unchanged ✓.
  "No tie-break of SPEC S1 is used" ✓ (only (A-F), (A0κ), (CYC-SHAPE) and the definition of FT_c).

## 2. CHAIN-COUNT″, re-derived
- Step A″ ✓. x on no honest cycle at t: OFFSET-MONO with p = par_{t+1}(x) ✓. Otherwise x ∈ Z_t(c) by (CYC-ID), so t ∈ CYC_c ✓; t ∉ ZC″_c =
  CYC_c ∩ ZCH_c ∩ FT_c gives t ∉ ZCH_c (Z-CONST: equality, with par_t(x) = par_{t+1}(x) = p) or t ∉ FT_c (FT-CONST: equality with
  p = par_{t+1}(x), exactly the p of Step A″) ✓.
- Sum form ✓. add1 §2's proof uses ZC_c only through Step A (at the charged transitions and along each x-piece′), through "distinct
  transitions get distinct charges" and through the piece count |EXIT_x ∪ ZC_c| + 1. Each of these holds word for word with ZC″_c, x-pieces″
  and Step A″ ✓.
- D form ✓: |EXIT_x| + (D − 1)(|EXIT_x| + |ZC″_c| + 1) ≤ D·(|EXIT_x| + |ZC″_c| + 1) for D ≥ 1 ✓. |ZC″_c(J)| ≤ min(|CYC_c ∩ ZCH_c|, |FT_c|)
  (ZC″ ⊆ both; J inside P) ≤ 2(n − 1)(|U_c| − 1) ✓. The closing line (J = P) is the D form with that bound substituted ✓.

## 3. PF-CHOICE and TIE-CHARGE: the code read against si.py e688b963 (l. 78-205)
- (a) ✓. l. 110-115: R = the alive vertices reaching v in gs; l. 196-197 give every x ∈ R the value (v, path[x], dist[x]), and a vertex's
  cycle node is set only there, so R = U_c ✓. A vertex u of rank > rank(v) gets its own bit: Even-liked u, reach(v, u) never adds its excl
  vertex u (l. 125), so u ∉ M and l. 138-140 set bit(u); Odd-liked u, u = start ∈ M = reach(u, v) and l. 146-147 set bit(u) ✓. So a path-free
  x has rank(x) < rank(v) ✓.
- (b) ✓. l. 116 / 117 filter gs / gp to R keeping order; restrict (l. 129-134) deletes entries of hs[x] and the matching x from hp[y],
  keeping the order of both lists ✓. Even-liked step: a path-free x is in M (else it gets bit u, l. 139-140); restrict(x, M) (l. 142-143)
  deletes exactly x's edges out of M, whose targets get bit u ✓; path-free targets and v are in M, so they are kept ✓. Odd-liked step: x ∉ M
  (else it gets bit u); restrict runs only on q ∈ M ∖ {u} (l. 148-149), so x's list is untouched ✓; an edge x → y with y ∈ M still in hp[y]
  would put x into M, since reach(u, v) (l. 120-128) adds every listed predecessor except v ✓. Other calls restrict(q, ·), q ≠ x, delete only
  q's own edges ✓. So, finally, hs[x] = succ(x) ∩ (A_t ∪ {c}), in increasing index order (succ sorted, l. 33 of si.py; SPEC l. 44) ✓.
- (c) ✓. l. 152-171: longest(x) scans hs[x] in order, `if d > best` (l. 165) keeps the first strict maximum, and τ[x] = arg (l. 168); dist =
  ℓ ✓; κ(y) = (0, −ℓ(y)) on path-free y (s_c = −1) and (0, 0) at v ✓: the least-index κ-minimiser ✓.
- (d) ✓. l. 172-180: BFS from v over hp in layers; `if y not in dist` (l. 178) gives y its first discoverer as τ[y] (l. 179); hp[·] is in
  increasing index order (l. 88-90 over increasing v; filtering and restrict keep the order) ✓. By (b) a path-free vertex is discovered only
  from a path-free vertex or v, and a layer's path-free vertices come in the order (position of the discoverer, index); induction on the
  layer: that order is the lexicographic order of tb (sequences of equal length) ✓; x's discoverer is the earliest-ordered y ∈ hs[x] in
  layer dist(x) − 1, the (κ, tb)-minimiser (κ(y) = (0, ℓ(y)), s_c = +1) ✓. The τ of S1 for Odd x is tau_full[x] = tau[x] (l. 199-200) ✓.
- TIE-CHARGE ✓. Outside FT_c: FT-CONST ✓. An Even z ∈ A_t that switches to x′ has κ_{t+1}(z) ≻ κ_t(z) by (SW), (M1κ), (Aκ), (M2κ) as in
  add1 §3 ✓, but x′ ∈ U_c comes here from (Aκ) at t + 1 (next_{t+1}(z) ∈ U for z ∈ U ∖ {c}). add1 used "x′ on Z_{t+1}(c)", which a general
  z ∈ A_t does not give (ADD2-N2, citation) ✓. That change starts in F, so it is F-touching ✓. Odd z ∈ A_t: induction on ℓ(z) ✓. The
  κ-minimal options of z have ℓ = ℓ(z) − 1 (c odd) or the maximal ℓ (c even) ✓. For c odd their tb is the index sequence along their
  honest plays, whose vertices are path-free with smaller ℓ and keep next by induction ✓. For c even, tb is the index ✓. A = A_t = A_{t+1} and
  κ on A ∪ {c} are unchanged ✓, so PF-CHOICE gives the same minimiser at t and t + 1 ✓. STRICT ⊆ FT_c directly by (CYC-SHAPE) (κ_{t+1}(v) ∈ F) ✓.
  TIE ⊆ FT_c: else v ∈ N ⊆ A_{t+1} = A_t keeps next ✓. STRICT + TIE ≤ |FT_c| ✓.
- ODDC remark (not signed): l. 182-195 is a stack search over all alive vertices of rank < rank(v), as the packet says ✓.

## 4. What the brief asked: the cut, and the code-level items
- The cut ZC″_c is SOUND (proof, §2) and never NEEDED in my data either. At the 1,054 (transition, x) pairs with t ∈ ZC″_c and x ∈ Qc on
  Z_t(c), off(x; p) never falls (ZC2F_fall 0). My no-cut control MUT=3 does not bite (0 failures on the n ≤ 24 library, 1,869 runs), as the lane
  reports for its own controls. So, as for add1's cut (OFFADD-N2), necessity is OPEN (ADD2-N4).
- PF-CHOICE / TIE-CHARGE against si.py: si.py's Engine.evaluate and my engine give the same (Ξ, σ̄) at all 75,525 states where both ran
  (SIAGREE). PF-CHOICE held for both at 29,141 (state, Odd path-free x) pairs; 1,506 of them have κ-tied options, so the tie-break is
  really exercised. A further 39,787 pairs were checked on my engine only, 2,740 of them tied. TIE-CHARGE: next unchanged on A_t at 62,181
  checks; all 1,184 STRICT and 36 TIE transitions lie in FT_c.

## 5. Data (own engine; DATA, not proof; 0 failures of every signed check)
| set (log in add2_logs/) | N5 runs | AF | FT phases × classes (Σ FT; max) | FTC | SA2 (on c's cycle) | ZC / ZC″ | CC2 | PF (tied) | si.py states | TC (STRICT / TIE) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib 1,140 files, n ≤ 40 (4 parts), S3 + given + 2 random | 2,739 | 564,579 | 2,931 (3,282; 29) | 16,524 | 42,683 (4,038) | 285 / 177 | 9,723 | 17,051 (933) | 32,302 | 22,105 (199 / 8) |
| lib41 (experiments/new/box41), n ≤ 64, S3 + 2 random | 1,130 | 461,320 | 1,318 (1,884; 44) | 11,204 | 15,999 (808) | 65 / 43 | 2,559 | 4,977 (241) | 17,781 | 13,698 (52 / 3) |
| random 𝒞^kO, n 4-16, k ≤ 6, seed 492 | 9,000 | 34,306 | 2,112 (1,022; 4) | 1,324 | 2,705 (540) | 177 / 62 | 2,678 | 7,113 (332) | 25,135 | 4,287 (135 / 1) |
| random, n 4-9, k ≤ 8, seed 493, S3 + 4 random (my engine only) | 100,000 | 136,684 | 14,055 (5,984; 3) | 8,900 | 17,214 (3,601) | 1,658 / 334 | 17,224 | 39,787 (2,740) | — | 21,729 (798 / 24) |
| nep90 / nep76 / long121 at their starts | 3 | 11,427 | 3 (6; 5) | 284 | 1,208 (0) | 0 / 0 | 13 | 0 | 307 | 362 (0 / 0) |
- The long instances agree with the lane (FT ≤ 6, ZC″ 0, no cycle change); they do not test §3 or §4.
- Controls (n ≤ 24 library, S3 + 2 random, 1,869 runs): MUT=1 (PF-CHOICE with the reversed index tie-break) 568 failures; MUT=2 (FT-CONST
  asked at FT_c transitions too) 1,157 / 1,485 / 330 failures (A, κ, off), so its hypothesis is needed; MUT=3 (no cut) 0, see §4.
  (A first MUT=2 log, add2_logs/mut2_lib_n24_INVALID_om_mut.txt, is void: the imported offmono_probe read the same MUT variable and flipped
  the length sign; fixed by pinning OM.MUT = 0 and re-run.)

## 6. Notes (none blocks a signature)
- ADD2-N1 (FT-COUNT, sharper). Per vertex ≤ n F-touching changes (F is a contiguous block of the order): |FT_c| ≤ n(|U_c| − 1). Not needed.
- ADD2-N2 (TIE-CHARGE, citation). The Even step cites add1 §3, whose "x′ ∈ U_c" came from x′ ∈ Z_{t+1}(c). For z ∈ A_t, take x′ ∈ U_c from (Aκ)
  at t + 1 instead. One clause.
- ADD2-N3 (method). The code-level items were checked by reading si.py e688b963 and by executing its Engine.evaluate as the object under
  review. si.py was not used as a checker; my engine (rl_engine) agrees with it at every state compared.
- ADD2-N4 (DATA, the cut). ZC″_c is needed by the proof, but not shown necessary in data (0 offset falls at 1,054 cut checks; no-cut
  control silent). Whether some game needs it is OPEN, as for add1's ZC_c.

DONE: this report. FINDINGS: all SIGNED, no gap; ADD2-N1..N4. NEEDS: Lead: route the notes to L-NEW's fixes file; §C against REFEREE-2 on
your word.
