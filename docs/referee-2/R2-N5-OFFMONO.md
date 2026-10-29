# R2-N5-OFFMONO: REFEREE-2 report on the P-N5-OFFMONO unit (box 49): OFFMONO + add + add2 + add3, reviewed as ONE unit
Referee: REFEREE-2 successor 18 (session_01WT4cukhJyjxHKaBJWikCkK), Opus 5.5 (D15, L37). Written 2026-10-26 from 19:20Z (date -u).
Objects (all frozen, all on trunk 77f2664e; each pin measured with `git show origin/claude/vibrant-johnson-nxvvxo:<path> | sha1sum`):
| file | sha1 | lines | author |
| --- | --- | --- | --- |
| docs/new/P-N5-OFFMONO-box49.md | d9705ac6cede9849d68bf9b8d0fc5c54ab6fc3c4 | 160 | L-NEW successor 28 |
| docs/new/P-N5-OFFMONO-add-box49.md ("add1") | 5911aba8fc4e968187523c27b4f48cdc55433b3f | 165 | L-NEW successor 29 |
| docs/new/P-N5-OFFMONO-add2-box49.md | f2d123ef6ebbb71408dc25b503b78edc085cbf9a | 157 | L-NEW successor 29 |
| docs/new/P-N5-OFFMONO-add3-box49.md (l-new 8b7e2e6e) | b7cd0ff103ead10054c8f42f787369710f7feb40 | 92 | L-NEW successor 29 |
Independence: written before opening any REFEREE file on OFFMONO or its addenda. In the push turn, after `git fetch origin claude/referee`,
`git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic offmono` gave 10 at 19:31:22Z (19:04:54Z: 8). I saw file NAMES only and opened
nothing under docs/referee/. Exposure I could not avoid: add3 itself quotes two lines of REFEREE 15's R-N5-OFFMONO-add.md (its OFFADD-N2
conjecture and "0 failures in 4,006 + 1,371 checks"). I read those two quotes as packet text. I did NOT check them against the REFEREE file
(that would open it); they are checked only in my §C, after this report is pushed.
Lane tools (experiments/new/box48/offmono2.py, offmono3.py, zch.py, ft.py, tie.py, tieclimb.py, quotecheck2.py) NOT run or imported.
Checker: docs/referee-2/R2-N5-OFFMONO/offmono_check.py (own). State loop = my lane's SPEC loop (R2-N5-DUAL/dual_check.Runner on si.py, which is
SPEC S1's own implementation). Ξ = my own play values of (σ, σ̄) (R2-N5-RUND/rund_check.state_info, ENGXI cross-check against the engine).
κ, par, Z_t(c), A_t, F, EXIT, CYC, ZCH, FT and every piece are computed in the checker from the packets' definitions. Quote check: own
R2-N5-OFFMONO/quotes2.py (per-file commit pins).
Scope (D1): the unit reduces the per-phase, per-class count of κ-changes to EXIT_x (exit changes) and D (offset values on a piece). Both are
OPEN. Nothing here bounds N5's running time. Not a TARGET.md claim (TARGET.md §2/§5 untouched: no iteration bound, no algorithm claim).
G-N5-TIME stays OPEN.

## 0. Verdicts (all "(Opus 5.5, D15)")
| file § | item | verdict | premises (checked) |
| --- | --- | --- | --- |
| OFFMONO §1 | Lemma OFFSET-MONO | SIGN | (Aκ), (A0κ), (M1κ) (R56 (a)); κ-Y-FORM_D (R56 (d)); Lemma S (a) (R18 (d), every game by R57 (a), standing premise 1E-N3); (SW) (R72 premises); SPEC S1's order |
| OFFMONO §2 | Corollary CHAIN-SUM | SIGN | OFFSET-MONO; (A0κ) |
| OFFMONO §2 | Corollary CHAIN-COUNT | SIGN | CHAIN-SUM, OFFSET-MONO |
| add1 §0 | Facts (CYC-ID), (CYC-SHAPE) (used, labelled PROVED, not in the to-sign table) | CORRECT | next_t a function; cycle node = top of its cycle (FBPOLY §0.3 (A0κ)); (Aκ) |
| add1 §1 | Remark Z-CONST | SIGN | CYC-SHAPE; (A0κ) |
| add1 §2 | Corollary CHAIN-COUNT′ (Step A, sum form, stated form, Remarks (i)-(iii)) | SIGN | OFFSET-MONO, CYC-ID, Z-CONST, CHAIN-SUM |
| add1 §3 | Lemma ZCH-COUNT (and its Corollary) | SIGN | (M1κ), (M2κ), (Aκ), (A0κ), (SW), CYC-SHAPE; "c is Even / Odd" read as OWNER (N-OFF-5) |
| add2 §0 | Fact (A-F) (used, labelled PROVED) | CORRECT | (INJ); play to c simple |
| add2 §1 | Lemma FT-COUNT | SIGN | (M2κ) |
| add2 §2 | Remark FT-CONST | SIGN | (A-F), CYC-SHAPE, (A0κ); the offset clause read for x ∈ Q (N-OFF-3) |
| add2 §3 | Corollary CHAIN-COUNT″ (Step A″, sum form, D form, the |ZC″| bound) | SIGN | OFFSET-MONO, CYC-ID, Z-CONST, FT-CONST, FT-COUNT |
| add2 §4 | Lemma PF-CHOICE, Corollary TIE-CHARGE (CODE-LEVEL) | SIGN against si.py e688b963 l. 78-205 (= SPEC S1, l. 33) | si.py read line by line (§1.4); FT-CONST; add1 §3's Even-switch step |
| add3 §1 | Lemma OFFSET-MONO⁺ | SIGN | OFFSET-MONO's Step 1 and Case L; CYC-ID, CYC-SHAPE; Lemma S (a); (M1κ); (Aκ) |
| add3 §2 | Corollary CHAIN-COUNT‴ (sum form and D form) | SIGN | CHAIN-SUM, OFFSET-MONO⁺ |
| all | quotes | 53 of 55 VERBATIM at their pinned commits (line numbers match); the 2 add3 quotes from REFEREE's report not checked before my §C | own quotes2.py |
No gap. Notes N-OFF-1..9 (§3). Not reviewed, as the packets ask: OFFMONO §3-§5, add1 §4-§7, add2 §5-§7, add3 §3-§4 (READING/DATA/OPEN). I
comment on two READINGs where my data say something (N-OFF-2, N-OFF-7).

## 1. Proof check
Notation as in the packets: phase P = maximal run with (λ_Ξ, τ) constant; c a cycle node; U = U_c; Q = Odd vertices of out-degree ≥ 2;
κ_t(z) = (signed weight of P(Ξ_t z), s_c·ℓ); next_t = σ_t / σ̄_t; par_t(q) = the first vertex of Q ∖ {q} on q's honest play before c, else c.

### 1.1 OFFMONO §1 Lemma OFFSET-MONO
- Setup. p = par_{t+1}(q) lies on q's (t+1)-play, so λ_{t+1}(p) = c and p ∈ U (U is the same set at t and t+1, the phase fixes λ_Ξ), so κ_t(p) is
  defined. The vertices x_1..x_r of π lie strictly before p on that play, hence strictly before c, hence in U ∖ {c}. None is in Q (p is the
  first one). None is q: the play from q is a lasso whose cycle contains c, so it is simple up to its first visit of c. CORRECT.
- Step 1 (backwards along π). (Aκ) at t+1 for x ∈ U ∖ {c}: off_{t+1}(x; p) = κwt(x) + off_{t+1}(x′; p). The three cases:
  - x Odd ∉ Q has one successor, so next_t(x) = x′.
  - x Even with σ unchanged: next_t(x) = x′.
  - x Even switched: (SW) gives σ_{t+1}(x) ∈ Iσ_t(x), i.e. Ξ_t(x′) ▷ Ξ_t(σ_t x) (S2's strictness). x′ ∈ U (on q's (t+1)-play) and σ_t(x) ∈ U
    ((Aκ) at t), so both valuations have cycle node c and (M1κ) turns ▷ into κ_t(x′) ≻ κ_t(σ_t x).
  In each case κwt(x) + κ_t(x′) ⪰ κ_t(x). The induction never uses x's t-play. CORRECT. (SW) holds for S4a (arena A(v) = {σ(v)} ∪ Iσ(v)) and
  for S4c alike, so in-phase fallbacks are covered.
- Step 2. Case N: y2 ∈ succ(q) ∩ U and its t-play avoids q, so y2 ∈ Y^q_t. R56 (d) (q on no honest cycle at t) and (Aκ) at q give κ_t(y1) =
  min_Y κ_t ⪯ κ_t(y2). Case L: q is on no honest cycle at t, so it is not on Z_t(c), and y2's t-play meets q on its tail, before its first
  c. Then κ_t(y2) = κwt(ζ) + κ_t(q) = κwt(Z) + κ_t(y1), with the cycle Z = q → ζ → q.
  - Under (σ_t, τ″) the play from q is exactly Z: every vertex of ζ except its last keeps its honest choice, and the last returns to q.
  - Lemma S (a) (L_σ = pointwise minimum over Odd's τ′; Ξ_t = L_{σ_t} by 1E-N3) gives Ξ_t(q) ⊴ V″(q). The cycle nodes differ (c ∉ Z) and
    rewards are injective (p′ injective), so reward(u*) > reward(c).
  - Some vertex of Z above c: u* has the top rank on Z and dominates wt_c(Z) (distinct powers of 2). An odd u* would have reward −p′(u*) <
    −p′(c) ≤ p′(c), which is false. So u* is even and wt_c(Z) > 0.
  - No vertex above c: wt_c(Z) = 0. If c had even Ω, then reward(c) = p′(c) ≥ every reward of lower rank, which is false. So s_c = +1 and
    κwt_c(Z) = (0, |Z|) ≻ (0, 0).
  CORRECT. Remark (iii) is right: Step 2 uses (Aκ) at t+1 only for q ∈ U ∖ {c}, whatever q's cycle status at t+1.

### 1.2 OFFMONO §2 CHAIN-SUM, CHAIN-COUNT
- CHAIN-SUM. The chain is the list of Q-vertices on q's (t+1)-play before c, in order. Each x_i's play is the suffix of q's play, and q does
  not reappear before c. The sum telescopes and κ(c) = (0, 0). Each level on no honest cycle at t is OFFSET-MONO with p = x_{i+1}. CORRECT.
- CHAIN-COUNT. Off CYC_c every level is on no honest cycle at t. The terms of an ordered group sum are all ⪰ 0 and their sum is ≠ 0, so some
  term is ≻ 0. The transition is charged once, to that level. On an x-piece, par(x) is fixed, so OFFSET-MONO applies at every transition
  and off(x; p) is non-decreasing: ≤ D − 1 strict rises. There are ≤ |EXIT_x| + |CYC_c| + 1 pieces. The final inequality needs only
  |EXIT_x| ≤ D·|EXIT_x| (D ≥ 1). CORRECT.

### 1.3 add1: CYC-ID, CYC-SHAPE, Z-CONST, CHAIN-COUNT′, ZCH-COUNT
- CYC-ID, CYC-SHAPE: correct as written. ℓ ≤ |Z| − 1 ≤ n − 1, and every vertex of Z_t(c) other than c has rank < rank(c), so wt_c = 0.
- Z-CONST. Equal sequences fix next on every cycle vertex, including the last vertex's return to c. κ on the cycle is (0, s_c·ℓ) with the
  same ℓ at both states. par(x) is read off the same walk, and p is on the cycle or is c. CORRECT.
- CHAIN-COUNT′ Step A. An on-cycle level puts the transition in CYC_c (CYC-ID). Off ZC_c it is then off ZCH_c, and Z-CONST gives equality
  with par_t(x) = par_{t+1}(x) = p. The charging is the CHAIN-COUNT argument with every level signed. CORRECT.
  - Remark (iii): a cycle change with no Q-vertex on Z_t(c) is outside CYC_c, so OFFSET-MONO covers every level. Correct.
- ZCH-COUNT.
  - N = ∅ ⇒ next(c) changed: otherwise tracing next_t from c reproduces Z_{t+1}(c). Correct.
  - STRICT: the target value of a strict rise of κ(v) lies in F (CYC-SHAPE at t+1). By (M2κ) each value is the target of at most one rise, so
    each v takes ≤ n − 1 charges.
  - Even v ∈ N rises strictly: the S2-strict (SW) step and (M1κ), then (M2κ) at x′, and x′ = c is allowed (κ(c) = (0, 0)). So a TIE has
    only Odd N-vertices, each with κ equal: ⪯ from "not STRICT" in a total order, ⪰ from (M2κ).
  - CEVEN: ψ_s = κ_s(next_s c) takes values (0, s_c·ℓ), 0 ≤ ℓ ≤ n − 1, and is non-decreasing on P (unchanged next by (M2κ); a switch of the
    Even c by (SW) + (M1κ) + (M2κ)). It rises strictly at every CEVEN transition, so CEVEN ≤ n − 1.
  - ODDC: c is Odd, next(c) changed, so out-degree ≥ 2 and c ∈ Q.
  - The four kinds partition ZCH_c. Sum (n − 1)(|U_c| − 1) + (n − 1) + TIE + ODDC. CORRECT.

### 1.4 add2: (A-F), FT-COUNT, FT-CONST, CHAIN-COUNT″, PF-CHOICE, TIE-CHARGE
- (A-F): (INJ) gives M = 0 ⇔ P = ∅; then 1 ≤ ℓ ≤ n − 1. Correct.
- FT-COUNT: κ(z) is non-decreasing. Each value of F is the source of at most one change and the target of at most one. So ≤ 2(n − 1) charges
  per z, over |U_c| − 1 vertices z. CORRECT.
- FT-CONST: A_t = A_{t+1} and κ is fixed on A_t ∪ {c}. An on-cycle x is path-free. Every vertex before c on x's (t+1)-play has P ⊆ P(Ξ_{t+1} x)
  = ∅, so p ∈ A_{t+1} ∪ {c}. CORRECT.
- CHAIN-COUNT″: Step A″ splits "not in ZC″ ∩ CYC" into "not in ZCH" (Z-CONST) or "not in FT" (FT-CONST). The rest is add1 §2 verbatim, and
  |ZC″| ≤ |FT_c|. CORRECT.
- PF-CHOICE, read against si.py at e688b963 (= the working-tree file; SPEC S1 l. 33 names l. 78-205):
  - (a) Every u ∈ R of rank > rank(c) gets its own bit:
    - Even-liked u: M = reach(v, u) excludes u (l. 137, 139-140).
    - Odd-liked u: u ∈ reach(u, v) (l. 145-147).
    So a path-free x has rank < rank(c). R = U_c (l. 196-199).
  - (b) Initially hs[x] = succ(x) ∩ R in increasing index order (l. 86, 116; succ sorted at l. 33). restrict deletes entries and keeps the
    order (l. 129-134). Every vertex that gets a bit has its in-edges from path-free x removed:
    - Even-liked step: x ∈ M is restricted to M, and exactly R ∖ M gets bit u.
    - Odd-liked step: an edge x → y with y ∈ M would put x into reach(u, v), because hp is kept consistent by restrict (l. 132-133) and
      x ≠ v. So that edge is already gone.
    No edge from x to a path-free vertex or to c is ever removed (both lie in every Even-liked M; x ∉ the restricted set at Odd-liked
    steps). CORRECT.
  - (c) Ω(c) even: l. 152-171 (longest, l. 154-169), the first strict maximum in hs order (l. 165), i.e. min (κ, index) with κ = (0, −ℓ). CORRECT.
  - (d) Ω(c) odd: BFS l. 172-181. tau[y] is set by the first vertex of the current layer, in layer order, whose hp list holds y (l. 177-179).
    hp lists are in increasing index order (built at l. 88-90 over increasing v, filtered and restricted keeping order). Path-free vertices
    are discovered only from path-free vertices or c, since hs[y] ⊆ A ∪ {c} by (b). Induction on the layer: among path-free vertices of a
    layer, the order is (position of the discoverer, own index) = lexicographic tb. The discoverer of x is the first y ∈ hs[x] in layer
    dist(x) − 1, i.e. min (ℓ, tb). CORRECT.
- TIE-CHARGE: off FT_c, an Even z ∈ A_t that switched would rise strictly (the add1 step; next_{t+1}(z) ∈ U_c by (Aκ)), which is F-touching.
  So Even z keep next. Odd z by induction on ℓ: for c odd, tb of the κ-minimal options is fixed by next on vertices of smaller ℓ; for c even,
  tb is the index. STRICT and TIE need some v ∈ N ⊆ Z_{t+1}(c) ∖ {c} ⊆ A_{t+1} = A_t (off FT) with next changed, which is impossible off FT.
  So STRICT_c + TIE_c ≤ |FT_c|. CORRECT. The ODDC remark (stack search over all alive vertices, l. 182-195) is right: PF-CHOICE says nothing
  about c's own choice.

### 1.5 add3: OFFSET-MONO⁺, CHAIN-COUNT‴
- On-cycle q: Step 1 is independent of q's t-position. It remains to show κ_t(y2) ⪰ κ_t(y1). y2's t-play ends in Z_t(c) ∋ q, so it meets q.
- Case L1 (meets q before c): OFFSET-MONO's Case L word for word. Z avoids c, and nothing there uses q's position.
- Case L2 (meets c first). I checked that the τ″-play from q is a simple cycle. y2's play enters Z_t(c) at some w and runs w → … → c
  without meeting q, so q lies on the arc from c to w. The arcs c → q and w → c are then disjoint, and the cycle is q, y2's path to c, and
  the arc c → q.
  - P(Ξ_t y2) ≠ ∅: its top u* has the top rank on the τ″-cycle (other vertices are below c, or lower vertices of P). As in Case L, u* is
    even, so M_t(y2) > 0 = M_t(y1) (y1 = next_t(q) is on Z_t(c) or is c).
  - P(Ξ_t y2) = ∅: the cycle's top is c and V″(q) = q ⊕ Ξ_t(y2). (M1κ) applies to any two valuations with cycle node c, not only honest
    ones (it is S1's order with equal rewards). With (Aκ) at q, κ_t(y1) ⪯ κ_t(y2).
  CORRECT.
- CHAIN-COUNT‴: every chain term ⪰ 0 by OFFSET-MONO⁺, pieces are cut at EXIT_x only, ≤ |EXIT_x| + 1 pieces, and |EXIT_x| + (D − 1)(|EXIT_x| + 1)
  ≤ D(|EXIT_x| + 1). CORRECT.

## 2. DATA (my checker; each violation count must be 0; every count below is from docs/referee-2/R2-N5-OFFMONO/logs/)
Corpus (logs/total.txt sums the main runs):
- named.txt, 18 instances from their .start files:
  - nep90_n40, nep76_n40, long121_n40, frz40;
  - the 7 qpcclimb games incl. snap_n80_s62;
  - the 4 tieclimb games;
  - du/nep90x2-x4.
- lib41_x3.txt: the 410-game lib41 list, 3 starts each (S3 + 2 random).
- lib2o_x5.txt: 41 games × 5 starts.
- c1o_503_x2.txt: 503 𝒞^1O games × 2 starts.
- rand_*.txt, random games:
  - k = 2, n 6-14 (3000 × 3);
  - k = 4, n 8-18 (2000 × 3);
  - kO, n 8-20 (1500 × 3);
  - k = 3, n 20-30 (400 × 2);
  - k = 5, n 20-40 (600 × 2).
Totals: 23,959 runs, 100,122 states, 68,116 phases, 142,287 (phase, class) pairs, 32,006 in-phase transitions. 26 RESULT lines, all OK,
violations 0. ENGXI 100,122 checks, 0 differences.
| check | checks | violations | case counts |
| --- | --- | --- | --- |
| (Aκ)/(A0κ), CYC-ID, CYC-SHAPE, (A-F) | 2,552,208 vertex-states | 0 | — |
| OFFSET-MONO (q off-cycle at t), incl. Step 1 at every π-vertex and κ_t(y2) ⪰ κ_t(y1) | 69,881 | 0 | Case N 69,743, Case L 138; strict rises 13,723; parent changed 3,470 |
| OFFSET-MONO⁺ (q on Z_t(c)), same sub-checks | 4,049 | 0 | L1 1, L2 4,048 (all with P(Ξ_t y2) = ∅); strict 147; parent changed 30 |
| CHAIN-SUM (identity, and chain = Q-vertices of the (t+1)-play) | 73,930 | 0 | — |
| Z-CONST (transitions with unchanged Z_t(c)) | 38,639 | 0 | — |
| ZCH-COUNT (kinds, STRICT ≤ n − 1 per v, CEVEN ≤ n − 1, ψ, TIE vertices, ODDC, total bound) | 1,562 ZCH transitions | 0 | STRICT 459, TIE 14, CEVEN 1,060, ODDC 29; max per phase and class: ZCH 6, TIE 1, ODDC 1 |
| FT-COUNT (per phase, class) / FT-CONST (off FT) | 142,287 / 34,281 | 0 / 0 | FT 5,920 transitions in all; max per phase and class 44 (x32_rand48, class 36), within its bound |
| PF-CHOICE (every Odd x ∈ A_t, every state) | 315,088 (128,674 with ≥ 2 options) | 0 | — |
| TIE-CHARGE (next unchanged on A_t off FT; STRICT and TIE ⊆ FT) | in the FT-CONST checks and the 1,562 ZCH transitions | 0 | — |
| CHAIN-COUNT / ′ / ″ / ‴: offset non-decreasing on every piece, sum form, D form, for every q, on J = the phase and one random sub-run per (phase, class) | 27,395 (q, J) per form | 0 | cut sizes: CYC 3,181, ZC 729, ZC″ 331 |
Controls (counted; they must and do bite):
- OFFSET-MONO with the opposite length sign (CTL_sign): 2,756.
- p := par_t(q) instead of par_{t+1}(q) (CTL_part): 1,358.
- Pieces not cut at EXIT, p := the current parent (CTL_noexit): 904 (q, J) with a fall.
- PF-CHOICE with the index tie-break for both parities (CTL_tbidx): 2,585.
- PF-CHOICE with the reversed index (CTL_tbrev): 13,369.
- PF-CHOICE with the path-sequence tie-break at even c (CTL_tbseq_ceven): 645.
Two controls do not bite:
- FT-COUNT with (n − 1)(|U| − 1) instead of 2(n − 1)(|U| − 1) (CTL_ft1): 0. The factor 2 is never needed on this corpus.
- CHAIN-COUNT‴'s sum form is tight: count = bound in 2,857 (q, J) cases. The largest is 51 κ-changes of one q against a sum form of 51 and a D form
  of 52 (lev_l_x, lib41).
Thin-spot search (logs/thin_*.txt; random games, n 4-14, k ∈ {2, 3, 4, kO}, 63,000 games × 4 starts; all OK):
- 13,890 more OFFSET-MONO⁺ checks: L2 with P(Ξ_t y2) ≠ ∅ occurs 2 times (it holds), L1 0 times.
- 44,966 more OFFSET-MONO checks.
Quotes (logs/quotes.txt), 53 of 55 found verbatim:
- OFFMONO 12/12 at 58061d91;
- add1 12/12 at 366fd235 / 331f0337;
- add2 22/22 at 278616c6, incl. 7 si.py lines;
- add3 7/9 at 3e03271f: the 2 MISSING are the REFEREE quotes, deliberately not checked (§ header).
Pins: N5-ssi-global.md 66fde9ef, si.py e688b963 (= working tree), FBPOLY de244dcd, FBRED 11b15455, OFFMONO d9705ac6, add 5911aba8 all match.

## 3. Notes (none changes a verdict)
- N-OFF-1 (premise wording; all four files). "RESULTS R38 (a) KEY (λ is constant on a phase)" cites KEY for the constancy of λ_Ξ. KEY's quoted
  sentence is about λ_U (Odd's valuation map): "λ_U is a function of τ alone". λ_Ξ is constant on a phase by the definition of a (λ_Ξ, τ)-phase;
  KEY's second clause is what makes these the joint phases. No effect on any proof. My checker cuts phases at (λ_Ξ, τ), as all landed
  results do. On τ-constant runs alone λ_Ξ does change: my first draft cut at τ only and crashed on that.
- N-OFF-2 (add3 §3 READING, not signed). "all follow from CHAIN-COUNT‴ (their cut sets only add pieces and a non-negative term)" is true of the
  ROUTE (‴ needs only EXIT_x and D), not of the NUMBERS.
  - A cut transition at which several levels rise is charged once (|X|) by the cut versions, but once per level by ‴'s sum form.
  - ‴'s D is a maximum over longer pieces.
  Data: a cut version's sum bound is below ‴'s in 15 (CC0), 10 (CC1), 12 (CC2) of 27,395 (q, J) pairs, e.g. tcS8_N9 J = 19..21: 39 against
  55. Its D bound is below in 2 pairs per form. The cut versions stay true on their own proofs (signed above). Suggested wording: "are no
  longer needed", not "follow from".
- N-OFF-3 (add2 §2). FT-CONST's offset clause says "for every x ∈ Z_t(c), x ≠ c, and p := par_{t+1}(x)", but par is defined only for q ∈ Q ∩ U.
  Read "x ∈ Z_t(c) ∩ Q". It is used only so (Step A″).
- N-OFF-4 (OFFMONO §0). "the minimum is attained at σ̄_t(q)" follows from R56 (d) together with (Aκ) at q. R56 (d) alone states the equality
  of values only; the packet says "with (Aκ)", so this is fine. Recorded because Case N uses exactly this.
- N-OFF-5 (add1 §3). "CEVEN if N = ∅ and c is Even; ODDC if … c is Odd" means the OWNER of c: ODDC needs c ∈ Q, and CEVEN's ψ argument needs c
  to switch by (SW). Ω(c)'s parity plays no role there. My checker uses the owner.
- N-OFF-6 (CHAIN-COUNT family). The D form also needs D ≥ 1, which every non-empty piece gives. All four sum forms are the sharper
  statements: the D forms add nothing on data (§2: the sum form is tight).
- N-OFF-7 (OFFMONO §4 / add3 §4 DATA, not signed). The lane's on-cycle case split agrees with mine: Case L1 is (almost) absent (1 in 4,049; 0 in
  13,890 more). L2 with P(Ξ_t y2) ≠ ∅, the one L2 branch that uses Lemma S (a), is exercised only 2 times in all my data. It rests on the
  proof.
- N-OFF-8 (thin spots). TIE 14 and ODDC 29 transitions in all. FT-COUNT's factor 2 is never needed (CTL_ft1 = 0). Max EXIT per level 6.
- N-OFF-9 (independence). add3 quotes REFEREE 15's OFFADD-N2 and its counts. I could not avoid reading those two quotes; my OFFSET-MONO⁺ check
  was written from add3 §1's proof, with my own Case L1/L2 split.

## 4. What the unit gives (my reading, for the Lead; not a signature)
- Per phase and class, every q: κ(q)-changes ≤ Σ_x (|EXIT_x| + Σ_π (v_x(π) − 1)), pieces cut at EXIT_x only (CHAIN-COUNT‴). This is PROVED,
  every game.
- A polynomial bound on this route still needs EXIT_x per phase and the offset value counts v_x(π) (or D). Both are OPEN, and neither is
  addressed by the unit.
- add1's ZCH-COUNT and add2's FT-COUNT / TIE-CHARGE are true and signed, but they are no longer on the route.
- ODDC_c stays unbounded (add2 §4's own remark).

## §C. Comparison with REFEREE (successors 15 and 16), written 2026-10-28 21:09Z (date -u), after my report was pushed (4e9a6372)
REFEREE files, as on trunk bb399acd (file sha1 by `sha1sum`):
- R-N5-OFFMONO.md, commit 04a563d3, sha1 f06a1c68, successor 15;
- R-N5-OFFMONO-add.md, commit c2a97189, sha1 b23b9035, successor 15;
- R-N5-OFFMONO-add2.md, commit d6e07396 + stamp fix ff99f1f5, sha1 fee77023, successor 16;
- R-N5-OFFMONO-add3.md, commit 907e21b9 + stamp fix d1a22e18, sha1 10a0beca, successor 16.
These were opened for the first time in this §C.
### C1. Verdicts
Identical on every to-sign item: SIGN, no gap, in all four files. Both of us also check (CYC-ID), (CYC-SHAPE) and (A-F) as correct.
JOINT GAP MAP: EMPTY.
### C2. Notes, item by item
| REFEREE note | my reading | status |
| --- | --- | --- |
| OFFMONO-N1 (lane's "parent changed" column: 53 / 60 / 48 vs the packet's 28 / 42 / 26) | CONFIRMED independently. My logs/named.txt gives exactly 455 / 390 / 363 checks, 53 / 60 / 48 parent changes and Case L 2 on long121, with par as in §0 | agree (DATA; lane to state its definition) |
| OFFMONO-N2 (D large on the lane instances) | same direction as my N-OFF-6: the sum form is tight in 2,857 (q, J) cases | agree |
| OFFMONO-N3 (name P1 / 1E-N3 in the premise list) | I used 1E-N3 the same way (§1.1); wording | agree |
| OFFMONO-N4, OFFADD-N2 (conjecture: OFFSET-MONO without the cycle hypothesis) | PROVED by add3's OFFSET-MONO⁺, which both of us sign (= ADD3-N3) | closed |
| OFFADD-N1 (CHAIN-COUNT′ ⇒ CHAIN-COUNT through the SUM form, not the stated form) | CORRECT; I re-derived it, details below. It also corrects my N-OFF-2 | agree; N-OFF-2 refined below |
| ADD2-N1 (FT-COUNT: ≤ n per vertex, since F is a contiguous block of the order for z ≠ c) | CORRECT. F = the κ-values with first component 0 (z ≠ c), so a monotone κ(z) enters F once, moves inside it ≤ n − 2 times and leaves once. My CTL_ft1 = 0 (even (n − 1)(\|U\| − 1) is never exceeded) agrees | agree (missed by me) |
| ADD2-N2 (TIE-CHARGE's Even step: x′ ∈ U_c from (Aκ), not from "x′ on Z_{t+1}(c)") | I used (Aκ) there in §1.4 but did not make it a note | agree |
| ADD2-N3 (si.py executed as the object, not as a checker) | same method on my side (si.py is SPEC S1's own implementation in my state loop) | agree |
| ADD2-N4 (the ZC″ cut not shown necessary; OPEN) | the necessity question is CLOSED by OFFSET-MONO⁺: no level's offset ever falls, so no game needs any cycle cut | superseded by add3 |
| ADD3-N1 (say y2 ≠ q) | correct: a self-loop at q would make q its own cycle node at t + 1. REFEREE 15 had it in OFFMONO §1; I checked it but did not write it | agree |
| ADD3-N2 (L2a, P(Ξ_t y2) ≠ ∅, never occurs; "rests on proof alone") | NEW DATA (below): L2a occurs, and holds strictly, in 2 random games I saved. It is very thin (2 in about 17,900 on-cycle checks), not vacuous | refined |
| ADD3-N3 (mark OFFADD-N2 / OFFMONO-N4 PROVED by add3) | agree | agree |
REFEREE has no counterpart for my notes N-OFF-1 (R38 (a) KEY is about λ_U; λ_Ξ is constant on a phase by definition), N-OFF-3 (FT-CONST's
offset clause: x ∈ Q), N-OFF-5 (CEVEN / ODDC = owner of c), N-OFF-9 (independence exposure). They are wording notes and stand as mine.
### C3. N-OFF-2 refined by OFFADD-N1 (the one point where we read differently)
- REFEREE (add3 §2) reads add3 §3 as "the earlier cut forms follow from CHAIN-COUNT‴". My N-OFF-2 said they do not, as numbers. Both are right,
  for different forms.
  - The stated / D forms of CHAIN-COUNT, CHAIN-COUNT′ and CHAIN-COUNT″ DO follow from CHAIN-COUNT‴'s SUM form. Fix a cut set X and assume
    ≤ D values on every cut piece. An x-piece‴ is a union of cut pieces glued at X-transitions, and each glue transition adds at most one
    strict rise. So Σ_{π‴}(v − 1) ≤ (D − 1)(|EXIT_x| + |X| + 1) + |X|, and the ‴ sum bound is ≤ Σ_x (|EXIT_x| + (D − 1)(|EXIT_x| + |X| + 1) + |X|).
    That is at most the cut D form |X| + Σ_x D(|EXIT_x| + |X| + 1); the difference is |X| + Σ_x 1 ≥ 0. This is OFFADD-N1's argument.
  - The cut SUM forms (CHAIN-COUNT′ and CHAIN-COUNT″ state one) do NOT follow. Their bound can be strictly smaller than ‴'s sum bound: my
    CMP data have 10 (CC1) and 12 (CC2) such (q, J) pairs (CC0, which has no sum form, 15), e.g. tcS8_N9, J = 19..21: 39 against 55. These
    statements stand on their own proofs, which both of us signed.
- Joint reading: add3 §3's "follow from" is right for the stated / D forms, through ‴'s sum form, and not for the cut sum forms. The route
  (count reduced to EXIT_x and D) is unaffected.
### C4. Data
Both see the long instances agree with the lane, every signed check at 0, and the controls biting (opposite sign, p := par_t, tie-break
mutations). Where we differ:
- Case L1: REFEREE found it once (harm_n12_seed412, not in my lib41 list). I found it once in my lib41 runs. Both exercise L1's c-odd branch
  or its strict branch, at least once each.
- Case L2a, my two instances, saved in docs/referee-2/R2-N5-OFFMONO/l2a/ (dump_random.py replays the generator; WHERE=1 prints the event):
  - r1814_6302_0.pg (sha1 9c575fc9), t = 1, c = 0, q = 4, y1 = 8, y2 = p = 3: κ_t(y1) = (0, −1), κ_t(y2) = (2048, −3); off rises (−2048, 1) → (0, −1).
  - r1813_619_1.pg (sha1 fd6d95a4), t = 0, c = 7, q = 3, y1 = 5, y2 = p = 1: κ_t(y1) = (0, 2), κ_t(y2) = (64, 1); off rises (−64, 2) → (0, 1).
  In both, M_t(y2) > 0 = M_t(y1), exactly the strict sub-case of the proof (an even top of P(Ξ_t y2)).
- Quotes: the 2 add3 quotes from REFEREE's file, unchecked in my report, are VERBATIM at c2a97189 (l. 43-44, l. 58; logs/quotes_add3_full.txt).
  add3 §5 is now 9/9, and the unit 55/55.
### C5. Result
No disagreement on any verdict. Joint gap map EMPTY. Notes to the lane, as the union:
- REFEREE's: OFFMONO-N1..N3, OFFADD-N1, ADD2-N1..N3, ADD3-N1..N3.
- Mine: N-OFF-1, -3, -5, -9, and N-OFF-2 in the refined form of C3.
- Data for ADD3-N2: L2a is thin, not vacuous.
OFFMONO-N4, OFFADD-N2 and ADD2-N4 are closed by OFFSET-MONO⁺. My verdicts are unchanged. REFEREE-2 successor 18 (Opus 5.5, D15).
