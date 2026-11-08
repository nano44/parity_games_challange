# R2-P-N5-ASC: second-referee report on packet P-N5-ASC (L-NEW successor 61, box 193)
REFEREE-2 successor 31 (Opus 5.5, D1), 2026-11-07 from 22:1xZ (date -u). Independent: docs/referee/ not read on this item.

## Object (claude/l-new 95dc76d7b71fd6832794eed94a3f76c1258cddf5, FROZEN)
- docs/new/P-N5-ASC.md 9c9cb50d89e8bba3232ca2790ddbf95f85580af6 (19,345 B) = the Lead's relay.
- experiments/new/box193/asc.pins: 27 files, all 27 sha1 match at 95dc76d7 (my loop).
- experiments/new/box193/check193.sh re-run on `git archive 95dc76d7` (8 s): exit 0, output byte-equal to the committed check193.out
  (lane_check193_95dc76d7.out). Lane code was run only, never read for my checks or imported.
- No line file exists for this packet yet; the DATA rule is applied to §7 (below) for the line to come.

## Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §2 | definitions (e-sets, lex order, ascents, CS(M), runs, hubs) | consistent; used as written |
| §3 | Lemma E-MON (with its E-DOM step) | **SIGN** (Opus 5.5, D1) |
| §3 | Lemma CHAIN-DECOMP | **SIGN** (Opus 5.5, D1) |
| §4 | Lemma SKELETON (a)-(c) | **SIGN** (Opus 5.5, D1) |
| §4 | Theorem HUB-ASC(B), with B = 0 = DESC-POLY, and the degree 5·2^B − 3 | **SIGN** (Opus 5.5, D1) |
| §5 | Corollary HUB-ASC-G and the whole-run corollary | **SIGN** (Opus 5.5, D1) |
| §6 | Lemma UP-JUMP, Corollary UP-B, Corollary NOUP (each under [E-LEV]) | **SIGN** (Opus 5.5, D1) |
| §1/§0/title | the [E-LEV] scope statements | **W-1 required**: NOUP needs [E-LEV] and is FALSE without it (control below); §1, the table and the title omit it |
| §8 | pins | **W-2 required**: 5 cited instances are not in asc.pins |
| §7 | DATA | reproduced by my own code; D-1..D-3 for the line |
| §9 | TARGET.md diff and scope sentence | ✓ |
Nothing is REFUSED. Nothing here bounds R or a running time; G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE.

## Premises (script R2-P-N5-ASC/r2q.py, out r2q.out; trunk docs/RESULTS.md at 5470cc0c, the packet's trunk)
- Every «…» of §1 (and the [DEF] quote in CHAIN-DECOMP) is verbatim at the line the packet names:
  - R104 (l. 9864), its seven definition quotes, and l. 10085 «the exact e-priorities to packet §3.1»;
  - R118 (a) l. 13677, (b) l. 13682, (e) l. 13691 (both quotes).
  - F1, F2, F3 are verbatim in the frozen docs/new/P-N5-XICYC.md (sha1 149e2414, the object of landed R118) l. 69-73.
  - R118 (b) replaces only F4 (by F4′); F1-F3 stand as landed ✓.
- Both entries carry «[refereed-only]» ✓.
- Not used, as stated: [LOC], OVT-DV, IN-BOUND (none of these appears in RESULTS: 0 hits), F4/F4′, F5, F6 ✓.
- **E-DOM from R104's priorities ✓.** The only vertices of priority above an e-vertex are other e's, c_W, K0 and K3. «e of even
  priority above every β» puts every β (≥ 6), K1 (5), K2 (3), the unused loop (2), gates (1) and movers (0) below every e, and c_W, K0
  (top + 2) and K3 (top + 3) above. The order among e's is not needed. Checked on all 13 instances and 300 random genomes (EDOM 0).
- **[E-LEV]** is not landed; it is a hypothesis.
  - box189/gamma3.py l. 43 sorts the e-priorities by (level, gate index), as the packet says ✓; so does my builder.
  - It is used in UP-JUMP only («By [E-LEV], b more relevant than a gives lev(x′) ≥ ℓ»), so UP-B and NOUP inherit it. §3-§5 do not use
    it ✓: with the e-order reversed, all §3-§5 counters stay 0 (control below).

## Proofs (own re-derivation)
- **E-MON.**
  - With Λ equal, VJ's order decides by the most relevant z of Π_t Δ Π_(t+1), and F1 puts z in Π_(t+1) when z is even.
  - c_W is the cycle node of any play through it, so it is not in Π.
  - K0 → K3 → K2 are frozen; K3 is entered only from K0, and K1, K2 only from the core. So K0, K3 ∈ Π iff Λ ∈ {K1, K2}; both plays have
    the same Λ, so both or neither contain them.
  - Hence if Δ meets an e-vertex, z is an e-vertex (E-DOM), even, and E_t < E_(t+1); otherwise the E-sets are equal ✓.
- **CHAIN-DECOMP.**
  - f ∈ Π is more relevant than w, so f is on the prefix.
  - f has one successor; F3 applies since Λ_t(f) = w ≠ f.
  - y_f = c_W would make w = c_W, which is more relevant than f; so y_f is the W-target mover.
  - The play from y_f is the suffix of v's play, so it has the same Λ and the same Π restricted to the suffix ✓.
  - The Reading (next_t defines one forest on the e-vertices with cycle node w, and the chain of an active item x is seq_t(x)) holds,
    since x ∈ Π_t(x) when Λ_t(x) = w ✓.
- **SKELETON.**
  - (a): τ(x) ∈ chain(x) ∖ {x}, and chain(τ(x)) is a suffix ✓.
  - (b): everything after τ^i(x) is ≤ τ^(i+1)(x). So the segment elements are below it, τ^(i+2) < τ^(i+1), and τ(z) = τ^(i+1)(x),
    because chain(z) is a suffix that contains it and has nothing larger ✓.
  - (c) follows from (b) ✓.
- **HUB-ASC(B).**
  - Lex order on subsets is the integer order of Σ 2^x, so a monotone value strictly increases at each change ✓.
  - **τ monotone ✓.** Removing a common element keeps the lex order, and a lex-larger set has an at-least-as-large top.
  - **Levels ✓.** τ(x) changes ≤ M − 1 times and the hub top ≤ M times, so there are at most M² + 1 levels. The packet's M² + M + 1 is
    a valid looser count (N-1).
  - **B = 0 ✓.**
    - The first element is the top, which changes ≤ M times.
    - At a change with the same first element, the last common element x has next_s(x) ≠ next_t(x), and next(x) = τ(x) on a descending
      value.
    - τ(x) is non-decreasing over all times, and both values lie in {0, …, x − 1}, so there are ≤ x − 1 such changes per x.
    - Total ≤ M + Σ(x − 1) = M(M + 1)/2.
  - **B ≥ 1, the three shapes.** (N) is fixed in the level. In (a) τ(s) = T since T is the top of chain(s), s ≠ T. In (c) z = next(y_i)
    has τ(z) = y_(i+1). Both decompositions follow from SKELETON (b) ✓.
  - **Ascents.** The prefix y_0 > … > y_i and the step y_i → z (z < y_(i+1) < y_i) are descents. So ascents(R(z)) + 1 +
    ascents(chain(y)) ≤ B, and each part has ≤ B − 1 ✓.
  - **The entry node fixes the shape:** y = T exactly in (a) ✓.
  - **(i) ✓.** On the level's times with entry node y, the constant hub y has a lex-nondecreasing value with ≤ B − 1 ascents in the
    restricted run (a run, since the conditions are pairwise).
  - **(ii), the Fix(y) ⊔ R(z) split ✓.**
    - Z_y is constant in the level.
    - For w ∈ Z_y, chain(w) = R(w) ⊔ chain(y) with R(w) ⊆ Z_y (SKELETON (b) at x = w, i = 0).
    - R(w) and chain(y) are disjoint: a w ∈ chain(y) with y ∈ chain(w) ∖ {w} would close a cycle.
    - At equal chain(y) = C, removing C keeps each R(w) lex-nondecreasing.
    - w ↦ (next(w) if ≠ y, else ⊥) is a forest on Z_y with chains R(w), so these times carry a run of CS(|Z_y|).
    - z_t ∈ Z_y in both shapes, and the hub value is (skeleton nodes above y) ∪ C ∪ R(z_t), constant apart from R(z_t). So z_t is a hub
      with ≤ B − 1 ascents, and F_(B−1) is monotone in M.
  - **Per-level and total counts ✓.** Per level: 1 + Σ_y F_(B−1)² ≤ 1 + M·F_(B−1)², with at most M entry nodes on P(T). Values never
    repeat across levels, which gives F_B ✓.
  - **Degree ✓:** d_B + 3 = 2(d_(B−1) + 3), d_0 = 2.
- **HUB-ASC-G.**
  - Active intervals: by F1 + F2 the reward of Λ_t(x) strictly increases at each change, so Λ = w on a contiguous set ✓.
  - The forest is CHAIN-DECOMP, monotonicity is E-MON with transitivity inside an interval, and the hub is f_t(v), an active item or ⊥ ✓.
  - With the active set constant, the refined levels number ≤ M² + 2M + 1 ≤ M² + 3M + 1 ✓.
  - Inside a refined level the active items form a genuine run of CS(|active|). The §4 recursion then gives the abstract F_(B−1), so
    using F′_(B−1) ≥ F_(B−1) is valid but loose (N-2).
  - **Whole run ✓:** Λ_t(v) takes ≤ 2M + 3 values (R118 (e)), each on one interval, and M_w ≤ M.
- **UP-JUMP.**
  - ℓ ≥ 1, else the play goes to c_W.
  - b's mover x′ has lev(x′) ≥ ℓ by [E-LEV].
  - Between a and b, levels change only at e-steps (−1) and Ξ-steps; β → u never returns.
  - So the first step reaching a level ≥ ℓ is a Ξ-step from a β of an option (x″, k″) with lev(xt) > lev(x″) and lev(xt) ≥ ℓ ✓.
- **UP-B ✓.** The segments are disjoint parts of the prefix, and each β belongs to one option, so distinct ascents use distinct upward
  options.
- **NOUP ✓** is UP-B with U = 0 and F′_0 = F_0.
- **Scope sentence ✓.** «It bounds the e-set height D_E,I(v) … and NOT R and NOT any running time» is accurate: every statement bounds
  D_E (or the abstract hub count), and OVT-DV and IN-BOUND are not in RESULTS. I found no over-claim beyond W-1's title phrase.

## Machine checks (own code; docs/referee-2/R2-P-N5-ASC/)
- **r2hub.py, the exhaustive counter-search from §2/§4's definitions** (r2hub.out, 48 s).
  - Method: the exact maximum of distinct hub values over ALL runs of CS(M) and all hubs with ≤ B ascents, as a longest path over
    (forest, hub) states; lex order = integer order.
  - Range: M = 1..6 (up to 16,807 forests), B = 0..3. **0 violations of F_B.**
  - Exact maxima:
    - B 0: 2, 4, 7, 11, 16, 22, which is F_0, attained;
    - B 1: 2, 4, 8, 16, 29, 50;
    - B 2 and B 3: 2, 4, 8, 16, 32, 64 (= 2^M, the unconstrained maximum).
  - These equal the packet's B 0 (11 at M 4), B 1 (16 at M 4, 29 at M 5) and tightness rows (M 1-6) ✓.
  - SKELETON (a)-(c): 0 violations on every (forest, item) of CS(1..6) (100,842 units at M 6).
- **r2asc.py, the game replay.**
  - Setup: IDEAL-CYC Howard on Γ(G) from my lane's builder (R2-N5-REALIZE, from R104 §3.1) with the fleet si.py Engine as in
    R2-P-N5-XICYC/r2howcyc.py. Plays, Λ, Π, seq and ascents are computed by me, and my Λ equals the Engine's on all units.
  - **13 instances** (the packet's set; r2asc_inst.out), all 0 violations:
    - EDOM on 13 genomes; EMON on 46,830 (step, vertex) pairs with equal Λ, at EVERY vertex (the lane tests W-targets only);
    - CDEC on 24,818 (state, vertex) with nonempty seq; UPJ on 10,751 ascents; UPB on 50,881 (state, vertex);
    - HUBG (D_E,I ≤ F′_B(M_w)) on 4,051 (vertex, Λ-interval).
    - Max ascents per instance equal check193.out's maxasc on all 13, and each is ≤ U(G). The packet's four UP-B rows are reproduced
      (RSG_K4 1 ≤ 1, RS3 2 ≤ 6, rd2_d9 3 ≤ 20, cR_d2_w8_R22 3 ≤ 9). Max D_E per Λ-interval is 18.
  - **NOUP** (r2asc_noup.out; my own generator, 300 genomes with no strictly upward Ξ-edge, 142 Ξ-cyclic, seed 31): max ascents 0 on
    21,135 plays; max D_E per Λ-interval 3 (= the packet's 3); all counters 0.
  - **Control CTRL=elevrev** (e-priorities in decreasing level order, so [E-LEV] is false; r2asc_*_elevrev.out):
    - EDOM, EMON, CDEC and HUBG all stay 0, on the instances and on the 300 genomes;
    - UPJ fails on 1,583 of 10,289 instance ascents and on all 222 ascents of the U = 0 genomes;
    - **UPB/NOUP fail on 209 of 21,116 plays of U = 0 genomes (up to 2 ascents).**
    - So [E-LEV] is necessary for UP-JUMP, UP-B and NOUP alike, and §3-§5 do not depend on it.

## DATA rule on §7 (clause by clause, for the line to come)
- E-MON / CHAIN-DECOMP / E-DOM: unit, set, scope and tool are named.
  - **D-1:** no clause gives the NUMBER of units. check193.out prints tmonfail / decfail / edomfail 0 but no unit counts.
  - The E-MON unit «consecutive state pairs at W-targets» is narrower than the statement («every vertex»). It is stated, so it is OK
    for a lane counter; my 46,830 every-vertex units can be cited.
- UP-JUMP: unit «ascents in movers' plays with Λ below every e» is narrower than the lemma. It is stated; the count is check193.out's
  «asc» column (sum 1,956). D-1 applies.
- **D-2:** UP-B's «12 instances were run once» has no output on record, so it is not DATA; drop it or commit the output. My
  r2asc_inst.out has all 13 against U(G).
- NOUP ✓ (units, set, seed, counts given).
- HUB-ASC(B) ✓ and SKELETON ✓ (units, sets, tools; reproduced exactly).
- Tightness B = 0: M ≤ 5 in check193.sh ✓; M 6, 7 from dp193.c's data/cs_dp.txt, «not re-run here». My r2hub.py reproduces M 6 = 22;
  **D-3:** M 7 = 29 is not re-run by any check.
- «No separate DATA» items listed ✓. The «Context, not a clause» B-1 every-chain row is not a clause ✓.

## Required changes (packet frozen: fixes entry; each old string occurs once in the packet, checked)
- **W-1 ([E-LEV] scope; NOUP is false without it, CTRL=elevrev).**
  - §1: «(only for §6 UP-JUMP and UP-B)» → «(only for §6 UP-JUMP, UP-B and NOUP)»;
  - «To sign» table: «UP-JUMP and UP-B under HYPOTHESIS [E-LEV]» → «UP-JUMP, UP-B and NOUP under HYPOTHESIS [E-LEV]»;
  - title: «in particular on genomes with boundedly many upward Ξ-edges (UP-B)» → «in particular, under the e-priority hypothesis [E-LEV],
    on genomes with boundedly many upward Ξ-edges (UP-B)».
  - §6's NOUP heading and §9 already say «under [E-LEV]».
- **W-2 (pins).**
  - The five cited instances ../box192/inst/cR_d2_w8_R22, rd2_d9, rd2_d10, rd3_d7, rf_d5.json are not in asc.pins. Their sha1s match
    box192/inst/SHA1SUMS (my `sha1sum -c`), but no check.sh block verifies that file.
  - So §8's «sha1 of this packet and of every tool and instance it cites» is not true at 95dc76d7.
  - Fix: add the five to asc.pins (fixes entry; check block unchanged), or state the pin source.
- **For the line (DATA):** D-1 (unit counts per clause), D-2 (drop «12 instances were run once» or commit its output), D-3 (M 7 tightness
  marked as not re-run).

## Notes (no verdict change)
- N-1: the level count can be M² + 1 (τ(x) has ≤ M − 1 changes, the hub top ≤ M); M² + M + 1 is valid.
- N-2: in §5 the recursion inside a refined level uses the abstract F_(B−1), so (M² + 3M + 1)(1 + M·F_(B−1)²) already bounds D_E,I;
  F′ is valid and looser.
- N-3: §9's «far from tight» is confirmed: at M ≤ 6, B = 2 already reaches the unconstrained 2^M while F_2 is ≥ 678.

## TARGET.md diff
- No statement names an algorithm's running time, a winning region or a complexity class.
- D_E,I(v) is a count of distinct e-sets in IDEAL-CYC runs of R104 / R118 genomes, not a running time (TARGET.md §2-§4); not M3/M4,
  not a gauntlet step ✓.
- The 2^rank-style integers are not used here; lex orders are compared as sets ✓.

## Findings
- F-1: every statement SIGN; HUB-ASC(B)'s induction (the three shapes, the Fix(y) ⊔ R(z) split, and the restriction to equal chain(y))
  is correct.
- F-2: no counterexample in an exhaustive search of all runs of CS(M), M ≤ 6, B ≤ 3; F_0 is attained at M 1-6.
- F-3 (W-1): NOUP is false without [E-LEV] (209 plays with ascents at U(G) = 0 under reversed e-order); §1, the table and the title
  must name it.
- F-4 (W-2): five cited instances are not pinned by the packet's pin block.
- F-5: own replay reproduces every §7 number on all 13 instances and 300 genomes; §3-§5 hold on every vertex.

## Tools and outputs
r2q.py / r2q.out; r2hub.py / r2hub.out (`python3 r2hub.py 6 3`); r2asc.py / r2asc_inst.out, r2asc_noup.out,
r2asc_inst_elevrev.out, r2asc_noup_elevrev.out (`r2asc.py FILES…`, `r2asc.py noup 300 31`, `CTRL=elevrev`); lane_check193_95dc76d7.out.

## Addendum 1: comparison with REFEREE 27 (claude/referee 26b2b516, docs/referee/R-P-N5-ASC.md; REFEREE-2 successor 31, 2026-11-07 22:5xZ by date -u)
- **Order.** Read only now: my report (533744a5) was on origin before I opened it (Lead 22:48Z). REFEREE did not read mine.
- **Verdicts: identical.** Every statement is SIGN in both reports, and nothing is REFUSED. The premise checks (all quotes verbatim,
  F1-F3 from the frozen P-N5-XICYC l. 69-73, E-DOM from R104's priorities), the scope sentence (OVT-DV and IN-BOUND 0 times in RESULTS)
  and the TARGET diff (CLEAN) agree.
- **Required items, one to one:**
  - REFEREE AS-2 = the first two strings of my W-1, byte-identical old/new strings («UP-JUMP, UP-B and NOUP under HYPOTHESIS [E-LEV]»,
    «(only for §6 UP-JUMP, UP-B and NOUP)»).
  - REFEREE AS-3 = my W-1 title string. REFEREE makes it a condition on the line; I asked for a packet fix. Either closes it, as long as
    the line carries «under [E-LEV]» on every UP-B / NOUP clause.
  - My W-1 adds measured evidence: NOUP is false without [E-LEV] (CTRL=elevrev: 209 plays with ascents at U(G) = 0). REFEREE's argument
    is textual (NOUP is proved from UP-B). Both are right.
  - REFEREE AS-D2 = my W-2 (the five box192 instances not in asc.pins; SHA1SUMS matches but is not run).
  - REFEREE AS-D1 = my D-1 (no unit counts for tmonfail / decfail / edomfail / upfail). Both of us note that «asc» is probably
    UP-JUMP's count (my sum: 1,956).
- **Mine only:**
  - D-2 («12 instances were run once» has no output on record);
  - D-3 (the M = 7 tightness value is not re-run; REFEREE also notes M 6, 7 «not replayed»; my r2hub.py replays M = 6 = 22);
  - N-2 / N-3.
- **REFEREE only:**
  - AS-1 (optional). F′_0 in §5 is DESC-POLY on the whole interval I, not «word for word» per level. I agree. I checked it now: the top
    of seq_t(v) is monotone on I (≤ M changes), and an item x blamed for a change lies on the hub's value at both times, so it is active
    at both. τ(x) is monotone on x's active interval, which contains both times. So ≤ x − 1 changes per x, and F′_0 = F_0 holds. My report
    did not make this explicit, and my N-2 spoke only of B ≥ 1. A good clarification; it changes no verdict.
  - AS-4 (optional): define the whole-run D_E(v) in §2. I agree; I read it the same way.
  - The RMON-2 witness: a box-doc item, not a packet clause.
- **Numbers.**
  - REFEREE's CS(M) maxima (B 0: 2, 4, 7, 11, 16; B 1: 2, 4, 8, 16, 29) equal my r2hub.out for M ≤ 5. Mine extends to M = 6 and B ≤ 3.
  - REFEREE's game rows on RSG_K4 (T 7, 623 E-MON / 450 CHAIN-DECOMP / 164 UP-JUMP units) equal my per-instance counts for RSG_K4: my
    single-instance run printed 623 / 450 / 164 (the 712 (state, vertex) units of 8 states × 89 vertices).
  - The other three rows' U(G) and max ascents equal mine.
  - Both level counts are M² + 1 (REFEREE «M(M − 1) + M + 1»; my N-1).
- **Verdict.** The two reports agree. The combined required set for fixes entry 1 / L-1 is:
  - AS-2 = W-1 (§1 and table) and AS-3 = W-1 (title / line);
  - AS-D1 = D-1;
  - AS-D2 = W-2;
  - my D-2 and D-3;
  - optional AS-1 and AS-4.
  - I will byte-test L-1 when it arrives.

## Addendum 2: fix round 1 / L-1 (claude/l-new 19cc23e3; REFEREE-2 successor 31, 2026-11-08 00:0xZ by date -u)
- **Object** (sha1 at 19cc23e3, equal to the Lead's relay 23:52Z):
  - docs/new/P-N5-ASC-fixes.md 68139c3e… (5,973 B, entry 1);
  - L-1 docs/new/P-N5-ASC-line-L1.txt 08cced78… (4,896 B, 1 line, 116 «(» = 116 «)», depth never negative, 0 «|»);
  - packet 9c9cb50d… unchanged;
  - asc.pins: 34 rows, all match (`sha1sum -c` on `git archive 19cc23e3`).
- **Re-run:** check193.sh on `git archive 19cc23e3` (40 s): exit 0, output byte-equal to the committed check193.out
  (lane_check193_19cc23e3.out). Sums over the 13 instance lines (bt_l1.py / bt_l1.out): edomfail 0 in edomunits 1,892; decfail 0 in
  decunits 24,818; tmonfail 0 in tmonunits 2,552; upfail 0 in asc 1,956 ✓.
  - «CS(M 7, A 0): max distinct hub chains 29» ✓; 13 ug193 lines, each ≤ U(G), equal to my r2asc_inst.out on all 13 ✓.
  - CHAIN-DECOMP's 24,818 equals my own independent count exactly (r2asc_inst.out «CDEC_units 24818») ✓.
- **Required strings:** W-1's three new strings (§1, table, title) each occur once in L-1, and the old strings 0 times ✓. The fixes
  entry gives the packet replacements with the same old/new strings ✓.
  - Every UP-B / NOUP clause carries «under [E-LEV]» ✓, and the scope sentence is kept ✓.
  - My control is cited correctly («209 of 21,116 plays», 533744a5) ✓.
  - L-RED R220's NOUPC witnesses are cited as another lane's DATA, «one route only»; I did not replay them, and no verdict here rests on
    them.
- **Items met:**
  - W-2: the five box192 instances are now in asc.pins, with sha1s equal to box192 SHA1SUMS ✓.
  - D-1: unit counts printed and stated ✓, except the two mismatches below.
  - D-2: ug193 runs on all 13, output committed ✓.
  - D-3: M 6, 7 re-run by check193.sh ✓.
  - AS-1 «F′_0 = F_0 (DESC-POLY on the whole interval)» ✓. AS-4 defines D_E(v) as distinct (Λ_t(v), E_t(v)) pairs; the whole-run bound
    (2M + 3)·F′_B holds for that count exactly ✓.
- **DATA rule on L-1, clause by clause.** Premises, definitions, statements and scope tail all agree with the packet + entry 1 ✓; NOUP,
  HUB-ASC(B), SKELETON, tightness and the no-DATA list ✓. Two clauses do not match their counters (asc193.py l. 50-80 read):
  - **W-3 (E-MON unit).** tmonunits counts every successor y of an e-vertex with Λ(y) fixed («v in W.values()»). That includes c_W
    (level-0 e's go to c_W), which adds one unit per step: Σ T = 229 of the 2,552. So the unit is «W-target or c_W», as fixes entry 1
    itself says («W-target or c_W-successor y»), not «W-target».
    - Old (once in L-1): «(consecutive state pair, W-target with Λ fixed) pairs»
    - New: «(consecutive state pair, W-target or c_W with Λ fixed) pairs»
  - **W-4 (UP-JUMP tested form).**
    - upfail tests only «some β on the segment whose Ξ-target is a mover of level ≥ lev(a's mover)» («lev(nxt[z]) >= la»). The lemma
      also asserts that this Ξ-step goes strictly up, to a level > that of the mover the β was entered from. A Ξ-step between equal
      levels ≥ ℓ would pass the counter.
    - So «UP-JUMP: violations 0 in 1,956 ascents» cites a weaker test than the clause. **My miss in round 1:** I had not read the counter
      and called this clause OK. My own r2asc.py tests the full form: UPJ 0 in 10,751 ascents of all vertices' plays.
    - Fix, either (a) or (b):
      - (a) add the strict condition to upfail in asc193.py (lev(nxt[z]) > lev of z's own mover) and re-run; the count stays 1,956 if
        0 again; L-1 unchanged;
      - (b) Old (once in L-1): «UP-JUMP: violations 0 in 1,956 ascents of movers' plays with Λ below every e» → New: «UP-JUMP, tested
        as «a β on the segment whose Ξ-target mover has level ≥ that of a's mover»: violations 0 in 1,956 ascents of movers' plays with
        Λ below every e; with the strict «above the β's own mover» condition added, 0 in 10,751 ascents of all vertices' plays
        (REFEREE-2 r2asc.py, docs/referee-2/R2-P-N5-ASC/r2asc_inst.out at claude/referee-2 533744a5)»
  - Both old strings occur exactly once in L-1 (bt_l1.out).
- **Verdict:**
  - fixes entry 1 **CORRECT**;
  - W-1, W-2, D-1 (counts), D-2 and D-3 **met**; AS-1 and AS-4 taken correctly;
  - **L-1 NOT YET: W-3 and W-4** (DATA rule, wording or counter only; no statement changes) (Opus 5.5, D1).
  - Statement verdicts are unchanged: all SIGN.

## Addendum 3: fix round 2 / L-2 (claude/l-new a5dcf9c6; REFEREE-2 successor 32, 2026-11-08 01:08Z by date -u)
- **Object** (sha1 at a5dcf9c642d191aa95b0bbab08a97b180ce88925, equal to the Lead's relay 01:08Z):
  - L-2 docs/new/P-N5-ASC-line-L2.txt f109cb69… (4,907 B, 1 line, 116 «(» = 116 «)», depth never negative, 0 «|»);
  - packet 9c9cb50d… unchanged; L-1 08cced78… unchanged; fixes docs/new/P-N5-ASC-fixes.md 28cf8f9f… (entry 2 appended);
  - asc.pins: 35 rows (asc193.py and the fixes file re-pinned; L-2 added), all 35 OK by `sha1sum -c --strict` on `git archive a5dcf9c6`
    (DOCS/ → docs/new/, as check193.sh l. 998 does).
- **Byte test** (own script R2-P-N5-ASC/bt_l2.py, out bt_l2.out):
  - W-3: the new string «(consecutive state pair, W-target or c_W with Λ fixed) pairs» occurs once in L-2; the old string «(consecutive
    state pair, W-target with Λ fixed) pairs» occurs 0 times in L-2 (once in L-1) ✓.
  - Word diff L-1 → L-2: exactly «or c_W» inserted, and «entry 1,» → «entries 1-2,» (the source tail); nothing else ✓ (= the Lead's
    word diff and fixes entry 2's own account).
- **W-4, option (a)**, read against the lemma (asc193.py l. 79-80 at a5dcf9c6, git diff 19cc23e3..a5dcf9c6: one line changed):
  - upfail now needs, for some β z on the segment between a and b, that its Ξ-target nxt[z] is a mover with «lev(nxt[z]) >= la and
    lev(nxt[z]) > lev(V[("x", name[z][1][0])])».
  - name[z][1][0] is the mover x of the option (x, k) of z = β_(x,k). The only edge into β_(x,k) is from its gate, whose mover is x, so x
    is «the mover it was entered from». la is lev of a's mover = ℓ.
  - This is UP-JUMP's statement verbatim: «a β-vertex whose Ξ-target is a mover of level > the level of the mover it was entered from,
    and ≥ ℓ» ✓. The unit (ascents in movers' plays with Λ below every e) is unchanged, stated, and already accepted (Add. 2).
  - Re-run: check193.sh on `git archive a5dcf9c6` (43 s), exit 0, output BYTE-EQUAL to the committed check193.out
    (lane_check193_a5dcf9c6.out). Sums over the 13 instance lines: upfail 0 in asc 1,956; tmonfail 0 in tmonunits 2,552; decfail 0 in
    decunits 24,818; edomfail 0 in edomunits 1,892 (all as in Add. 2) ✓.
  - So L-1's UP-JUMP clause «violations 0 in 1,956 ascents …», unchanged in L-2, now cites a counter that tests the clause ✓. The second
    route (my predecessor's r2asc.py, 0 in 10,751) is cited as REFEREE-2's and «not re-run here» ✓.
- **DATA rule on L-2, clause by clause.** L-2 = L-1 + the two strings above.
  - Add. 2 found every other clause of L-1 matching its counter. Unchanged clauses keep that verdict.
  - E-MON: unit «W-target or c_W with Λ fixed» = tmonunits' loop set («v in W.values()», W = each e's only successor, W-target mover or
    c_W) ✓.
  - UP-JUMP: counter = clause (above) ✓.
  - Source tail «with fixes entries 1-2» ✓.
- **Verdict:**
  - fixes entry 2 **CORRECT**;
  - W-3 and W-4 **met** (W-4 by option (a));
  - **L-2 MATCHES** (byte test, the counter read against the lemma, the re-run, and the DATA rule clause by clause) (Opus 5.5, D1).
  - Statement verdicts unchanged: all SIGN.

## Addendum 4: L-3 for CHECKER C135 (claude/l-new a2512364; REFEREE-2 successor 32, 2026-11-08 04:09Z by date -u)
- **Object:** L-3 docs/new/P-N5-ASC-line-L3.txt 0012d671… (5,154 B, 1 line, 122 «(» = 122 «)», depth never negative, 0 «|», one « — »)
  = CHECKER C135 §5's target (claude/checker 0942e8be); packet 9c9cb50d… unchanged; L-2 f109cb69… unchanged.
- **Byte test** (own R2-P-N5-ASC/bt_l3.py, out bt_l3.out; the R1-R4 strings typed from C135 §5, wrapped lines joined by one space as
  C135 says):
  - each of R1-R4: old string once in L-2, 0 times in L-3, new string once in L-3;
  - the rebuild L-2 + R1, R2, R3, R4 (in that order) = L-3 byte for byte (0012d671…), so nothing else changed.
- **My strings still hold:**
  - W-1's «under [E-LEV]»: 4 occurrences in L-2 and in L-3.
  - W-3: new string once, old string 0 times.
  - W-4's UP-JUMP clause: once (its counter is the strict one, Add. 3).
- **R2-R4 read in meaning:**
  - R1: the source note «L-NEW successors 61-62»: successor 62 wrote fixes entry 2 and L-2 ✓.
  - R2: «the proof of record of HUB-ASC-G's B = 0 case (F′_0 = F_0, DESC-POLY on the whole interval) is referee-originated (REFEREE
    R-P-N5-ASC §3 AS-1, restated in P-N5-ASC's fixes entry 1 AS-1), signed by both referees».
    - True. My predecessor checked AS-1 independently in Add. 1 (l. 212: «F′_0 in §5 is DESC-POLY on the whole interval I … I agree.
      I checked it now») and accepted its restatement in entry 1 in Add. 2 (l. 254) ✓.
  - R3: «hence seq_t(v) = (f, seq_t(y_f))» is the packet's signed sentence (l. 81) verbatim.
    - It follows from E_t(v) = {f} ∪ E_t(y_f) together with play order: f is the first e-vertex of v's play, and the rest of v's
      play is y_f's play with the same cycle node.
    - The forest «Reading» it replaces was not part of the signed lemma, so removing it from the signed clause is right ✓.
  - R4: «seq_t(v) the e-vertices in Π_t(v) in play order, E_t(v) their set, an ascent of seq_t(v) a step to a more relevant element» =
    packet §2 l. 52-55 (seq_t(v) «the e-vertices that lie in Π_t(v), in the order of» the play; an ascent «an index i with c_(i+1)
    more relevant than c_i») ✓. With R4, UP-JUMP's and the DATA clauses' «ascent» are now defined in the line ✓.
- **DATA rule on L-3:** R1-R4 add no DATA and change no count; every DATA clause is byte-equal to L-2's (Add. 3) ✓.
- **Verdict: L-3 MATCHES** (Opus 5.5, D1). Statement verdicts unchanged: all SIGN.

## Addendum 5: L-4 = L-3 + REFEREE 28's R5 (claude/l-new a744677e; REFEREE-2 successor 33, 2026-11-08 05:25Z by date -u)
- **Object:** L-4 docs/new/P-N5-ASC-line-L4.txt at a744677e: sha1 4017305a34eac21615ba8f172a9b899544d25659, 5,198 B, 1 line,
  125 «(» = 125 «)», depth never negative, 0 «|», one « — », «under [E-LEV]» 4 times. a2512364 is an ancestor of a744677e.
  - Packet docs/new/P-N5-ASC.md unchanged: 9c9cb50d…, 19,345 B.
  - The only box193 changes are in asc.pins: the fixes file is re-pinned, and L-4 and mkl4_193.py are added.
- **Byte test** (own R2-P-N5-ASC/bt_l4.py, out bt_l4.out; strings typed from REFEREE 28 §E, claude/referee 013f821b, l. 303-304):
  - R5's old string occurs once in L-3 and 0 times in L-4.
  - R5's new string occurs 0 times in L-3 and once in L-4.
  - Rebuilding L-3 + R5 gives 4017305a…, 5,198 B, which is L-4 byte for byte («L-4 == L-3 + R5: True»). Nothing else changed.
- **R5 read in meaning against packet l. 80** («**Lemma CHAIN-DECOMP.** If seq_t(v) = (f, …), then …»):
  - R5's finding is right: the old wording is false.
    - The old line hypothesis, «the first e-vertex on v's play is f», does not give f ∈ Π_t(v).
    - Example: v's play reaches an e-vertex f whose successor is c_W. Then Λ_t(v) = c_W, which is more relevant than f, so f ∉ Π_t(v).
      Also y_f = c_W is not a mover, so the old conclusion fails.
    - Measured with own counters, added to a copy of my predecessor's replay. The copy is R2-P-N5-ASC/r2cd5.py; only the counters are
      new. Outputs: r2cd5_inst.out (13 pinned instances, from a git archive of a744677e) and r2cd5_noup.out (300 own random genomes, seed 33).
    - On the pinned instances: of 33,102 (state, vertex) plays with some e-vertex, 8,284 have their first e-vertex ∉ Π_t(v), and the
      old conclusion fails on all 8,284 (OLDHYP_notinPi = OLDHYP_concl_fails = 8,284).
    - On the random genomes: 1,819 of 5,409, with the same equality.
    - This confirms REFEREE 28's R5 witness independently. CDEC 0 of 24,818 reproduces the lane's CHAIN-DECOMP count exactly.
  - The new hypothesis's conjunction («first e-vertex on v's play is f and f ∈ Π_t(v)») implies the packet's «seq_t(v) = (f, …)» on
    every game. f lies in Π_t(v) and no e-vertex comes before it, so f is the first element of seq_t(v). So L-4's lemma, read with
    the conjunction, is the packet's lemma or a special case of it, and it is true.
  - **N-1 (note, no change required):** the «i.e.» also asserts the converse. The converse can fail only when the cycle node is an
    e-vertex. The argument:
    - Suppose seq_t(v) = (f, …) and an e-vertex g ∉ Π_t(v) comes before f. Then g lies on the prefix and is less relevant than
      w := Λ_t(v), while f is more relevant than w.
    - By [DEF] (E-MON's proof, packet l. 70-71), w is then an e-vertex, c_W, K0 or K3.
    - w ≠ c_W, because c_W tops every other priority and f is more relevant than w.
    - K0 and K3 are never cycle nodes (packet l. 74-76).
    - So w is an e-vertex.
    - Measured: 0 plays with an e-vertex as cycle node among the 50,881 plays of the pinned instances and the 20,549 plays of the random
      genomes. The direct counter GLOSS («first e-vertex on the play ≠ first element of seq_t(v)») is 0 in 24,818 and 0 in 3,590.
    - So on all data the «i.e.» is an exact restatement. It does not weaken the signed clause, which carries the packet's
      «seq_t(v) = (f, …)» first.
    - My predecessor's Add. 4, reading R3, used the same gloss («f is the first e-vertex of v's play»). It is true under the
      same proviso.
- **Correction to Add. 4:** «L-3 MATCHES» in Add. 4 was a miss. Add. 4 checked R1-R4 and the W strings. It did not compare the
  CHAIN-DECOMP hypothesis of L-1 to L-3 against packet l. 80. REFEREE 28 found the gap. I agree with R5 and with its verdict that L-3
  did not yet match.
- **DATA rule on L-4:** R5 is a statement wording. It adds no DATA and changes no count. Every DATA clause is byte-equal to L-3's
  (bt_l4.py: the rebuild equals L-4) ✓. Its witness is REFEREE 28's asc_cd_l0.py, and my r2cd5_*.out counts are a second witness.
- **Verdict: L-4 MATCHES** (Opus 5.5, D1). All statement verdicts are unchanged: SIGN.

## Addendum 6: L-5 = L-4 + REFEREE 29's R-A and R-I (claude/l-new e28e962d; REFEREE-2 successor 33, 2026-11-08 07:47Z by date -u)
- **Object:** L-5 docs/new/P-N5-ASC-line-L5.txt at e28e962d214971b8ef8739967185117a3e5f221c: sha1 fe4d3f90…, 5,192 B, 1 line, 124 «(» =
  124 «)», depth never negative, 0 «|», «under [E-LEV]» 4 times. a744677e is an ancestor, and the packet is unchanged (9c9cb50d).
- **Byte test** (own R2-P-N5-ASC/bt_l5.py, out bt_l5.out; strings typed from the Lead's 07:48Z message):
  - R-A and R-I: each old string occurs once in L-4 and 0 times in L-5; each new string 0 times in L-4 and once in L-5.
  - The rebuild L-4 + R-A + R-I is fe4d3f90…, 5,192 B, which is L-5 byte for byte, so nothing else changed.
- **Meaning:**
  - R-A («items 1..M compared by number, …, an ascent a step to a larger item») is packet §2 l. 58 («items 1..M, compared by number
    («rank»)») with l. 55's ascent («c_(i+1) more relevant than c_i») read in CS(M), where «more relevant» is «larger number» ✓. It
    defines the abstract system's terms in the line, and HUB-ASC(B) is unchanged.
  - R-I removes the «i.e.» gloss. The clause now reads «(Lemma CHAIN-DECOMP) if seq_t(v) = (f, …), then …», which is packet l. 80's
    hypothesis exactly, with seq_t(v) defined in the line (R4).
    - My Add. 5 N-1 (the converse of the gloss needs a non-e cycle node; true on all data) lapses with the gloss. R-I leaves no
      equivalence claim, which is the cleaner form ✓.
- **DATA rule on L-5:** wording only; no DATA added and no count changed ✓.
- **Verdict: L-5 MATCHES** (Opus 5.5, D1). Statement verdicts unchanged: all SIGN.
