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
