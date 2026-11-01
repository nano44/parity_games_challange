# N5-BRTREE (box 121): Odd's best-response forest inside a τ-stretch; the forest potential is DEAD, and the τ-stretch core on the builds is a two-fixed-strategy climb (TWO-FIX)
- L-NEW successor 44 (Opus 5.5), D14 / D18. Lead GO 2026-11-01 01:56Z: «Measure first: does each fresh Ξ-change feeding an inconsistent step
  lie in the subtree below Even's switch at k − 1, in G_σ's Odd best-response forest? How often does the tree's shape change per step (link /
  cut counts)? Only if the data say «yes» on the corpus AND on L-RED's builds, try the potential … Say early if the data kill the idea.»
- Tools: experiments/new/box121/brtree.py, twofix.py; runs box121/runred.sh (→ red.txt), box121/runcorp.sh (→ b_sbcg.txt, b_alt.txt), box121/pincheck.sh (→ pincheck.txt).
  Engine as box 118 (n5x / si.Engine); valid or repaired starts (box 113 / 116b / 117).
- Status words: PROVED (lane) = proved here, not refereed; DATA = measured; DEAD = killed at a named instance; READING = interpretation.

## 0. Answer
- The containment question is a theorem, not DATA (Lemma PLAY-CONTAIN, §1). Every Ξ-change at a transition k → k + 1 lies on a play
  that passes through a σ-switch of k. The play has to include its cycle: in the tree path alone the containment fails once
  (lend107_n32: 277 of 278 Ξ-changes).
  - So the «yes» is automatic and carries no counting power by itself.
- The forest potentials are DEAD as potentials (§2).
  - PHL := Σ_v log2(subtree size) and PDEP := Σ_v depth, on F_k, rise and FALL inside τ-stretches on every build. cp_K4: PHL rises at 39
    and falls at 5 of 44 transitions. This is the trap the Lead named: a quantity of polynomial range that is not monotone gives no bound.
  - I did not try a heavy-light amortization. A heavy-light argument bounds the cost of the link / cut operations, not how many of them
    there are. The count of operations is what is open here.
- What the data DO show (§3, DATA) is that Odd's part of the forest is almost frozen in the long stretches. σ̄ is the optimal Odd
  counterstrategy to σ, so this gives a cleaner core (Lemma TWO-FIX, §4).
  - On cp_K4, suf_K8 and s3quad_K8_m30 the whole run, apart from its first transition, is ONE window where τ and σ̄ are both fixed.
  - In that window N5 is an improvement run in the ONE-PLAYER game G_σ̄ whose steps are selected by G_τ.
  - Switch-best on G_σ̄ finishes from the window start in 2 steps; N5 takes 43 / 151 / 263.

## 1. Lemma PLAY-CONTAIN (PROVED, lane)
- Setting: an N5 run (SPEC S1-S5). σ̄_k := any optimal Odd counterstrategy to σ_k, so Ξ_k(v) = V_(σ_k, σ̄_k)(v) for every v (VJ00 (11);
  RESULTS R18 (d) Lemma S (a), whose proof uses no 𝒞^1O hypothesis). Write π_k(x) for the (σ_k, σ̄_k)-play from x: its path to the cycle
  node, plus the cycle.
- Statement: if Ξ_(k+1)(x) ≠ Ξ_k(x), then π_k(x) visits an Even vertex y with σ_(k+1)(y) ≠ σ_k(y).
- Proof.
  - Suppose not. Every Even vertex on π_k(x) keeps its choice. Then (σ_(k+1), σ̄_k) produces the same play from x, because a positional
    play is fixed by the choices at the vertices it visits. The VJ00 valuation depends only on the play.
  - So Ξ_(k+1)(x) ⊴ V_(σ_(k+1), σ̄_k)(x) = V_(σ_k, σ̄_k)(x) = Ξ_k(x), where the ⊴ is the minimum over Odd's strategies (Lemma S (a)).
  - Lemma S (b) (Ξ non-decreasing along the run) gives Ξ_k(x) ⊴ Ξ_(k+1)(x). Hence they are equal, which contradicts the hypothesis. ∎
- DATA: 100% on L-RED's builds and on the corpus (box121/brtree.py, field XIN_OLD; §5).
  - The fresh-fed form (box 119: the target z of a switch (y, z) ∉ Is_(k−1)) is the case x = z at k − 1 (field IN_OLD, 100%).
  - The «path only» variant, without the cycle, fails at one Ξ-change of lend107_n32 (277 / 278). That is why the play must include its
    cycle.

## 2. DEAD: the forest potentials
- F_k := the in-forest f_k(v) = σ_k(v) (Even v) or σ̄_k(v) (Odd v), with each cycle node's out-edge cut. ROOTOK := every root is
  Ξ_k(v)'s cycle node; it held on every run.
- Statement killed: «inside every τ-stretch, PHL (or PDEP) is monotone».
  - cp_K4 (box113/inst/cp_K4.pg with cp_K4.start, n = 192): PHL rises at 39 and falls at 5 of the 44 stretch transitions; PDEP 36 / 4.
  - Every L-RED build shows both directions (red.txt: fbg_K12_m6_m24 PHL 378 / 25, PDEP 355 / 48; s3quad_K8_m30 PHL 255 / 9).
- Without a monotone direction the range bound (n log2 n, resp. n²) bounds nothing. The idea dies in the form the Lead allowed.

## 3. DATA: link / cut counts, and the frozen Odd forest (box121/red.txt)
| build | n | K | Even links (LINKE) | Odd links (LINKO) | stretch transitions with an Odd link | longest Odd-fixed run |
| --- | --- | --- | --- | --- | --- | --- |
| cp_K4 | 192 | 44 | 3,282 | 16 | 1 | 43 |
| suf_K8 | 199 | 152 | 1,497 | 32 | 1 | 151 |
| s3quad_K8_m30 | 479 | 264 | 513 | 32 | 1 | 263 |
| topfix_n10 | 210 | 64 | 826 | 28 | 3 | 58 |
| fbg_K12_m6_m24 | 290 | 404 | 823 | 168 | 72 | 24 |
| fbA_K8_m8_m8 | 192 | 88 | 225 | 144 | 65 | 2 |
| lend107_n32 | 32 | 112 | 152 | 3 | 2 | 107 |
| switchbestexp_6 | 160 | 62 | 402 | 16 | 4 | 32 |
- So there are two regimes. On cp / suf / s3quad / topfix / lend107 Odd's response is frozen and Even's own switches drive everything. On
  fbA / fbg, σ̄ changes at most transitions (65 of 88 on fbA_K8).

## 4. Lemma TWO-FIX (PROVED, lane) and its DATA
- Definition: a TWO-FIX window is a maximal run of transitions j → j + 1, a ≤ j < b, with τ_j = τ and σ̄_j = σ̄ for a ≤ j ≤ b.
  - σ̄_j is si.Engine's optimal counterstrategy. The lemma holds for any fixed choice of optimal counterstrategies.
  - G_σ̄ := G with Odd fixed to σ̄, a one-player game.
- Statement: in a TWO-FIX window, for a ≤ j < b:
  - (i) Ξ_j is the valuation of σ_j in G_σ̄, and Is_j is G_σ̄'s improving set of σ_j.
  - (ii) σ_(j+1) ≠ σ_j, and σ_(j+1) switches only edges of Is_j.
  - (iii) hence the window is a strategy-improvement run in the one-player game G_σ̄: its G_σ̄-values rise strictly at every step, and at
    each step the choice is S4a's optimum, in G_τ, of the arena {σ_j} ∪ Is_j.
  - (iv) if moreover σ̄ = τ on every Odd vertex, every transition of the window that is not a fallback is consistent (P-N5-GATE), so
    CONSISTENT-RED's Corollary bounds the window by (FB + 1)(B − 1) + FB, with FB := its fallbacks and B := (n² − n + 1)(n + m)
    (R17 (d)). Without fallbacks, b − a < B.
- Proof.
  - (i): Ξ_j = V_(σ_j, σ̄) = the G_σ̄-valuation of σ_j, by the definition of σ̄_j (Lemma S (a)). SPEC S2's improving set is defined from Ξ_j
    edge by edge, so it equals G_σ̄'s.
  - (ii): if S4a and S4b changed nothing, then τ_(j+1) = τ_j forces an S4c fallback. With σ̄ fixed the fallback is Even's branch (Is ≠ ∅),
    which switches inside Is_j. Otherwise S4a's arena only offers {σ_j(y)} ∪ Is_j(y). This is the argument of CONSISTENT-RED (i) in
    P-N5-GATE.
  - (iii): switching a non-empty set of improving edges strictly improves the values (RESULTS R15 (a), here on the one-player game G_σ̄).
  - (iv): with σ̄ = τ, Ξ_j = V_(σ_j, τ) = W_j, so Is_j = IW_j and every non-fallback transition is consistent. CONSISTENT-RED and its
    Corollary apply, with INC = FB. ∎
- DATA (box121/twofix.py: the longest window; ODIFF := Odd vertices with σ̄ ≠ τ; SB := the length of switch-best on G_σ̄ from the window
  start; SBSTEP := N5 steps equal to G_σ̄'s switch-best step):

| build | windows | in windows / K | longest L | ODIFF | SB | SBSTEP |
| --- | --- | --- | --- | --- | --- | --- |
| cp_K4 | 1 | 43 / 44 | 43 | 16 | 2 | 1 |
| suf_K8 | 1 | 151 / 152 | 151 | 32 | 2 | 1 |
| s3quad_K8_m30 | 1 | 263 / 264 | 263 | 32 | 2 | 1 |
| topfix_n10 | 3 | 61 / 64 | 58 | 0 | 58 | 58 |
| switchbestexp_6 | 6 | 52 / 62 | 32 | 0 | 32 | 32 |
| lend107_n32 | 1 | 107 / 112 | 107 | 3 | 26 | 25 |
| fbg_K12_m6_m24 | 37 | 331 / 404 | 24 | 49 | 6 | 0 |
| fbA_K8_m8_m8 | 16 | 23 / 88 | 2 | 32 | 2 | 0 |

- With ODIFF = 0 (topfix_n10, switchbestexp_6), N5 IS switch-best on G_τ, as (iv) says. On the corpus (§5), 38 such windows end with one
  step that is not switch-best. There G_τ's switch-best stalls (the arena optimum is σ itself; twofix.py prints SB < 0), and N5 takes an
  S4c fallback.
- On cp / suf / s3quad, N5 walks 43 / 151 / 263 strict G_σ̄-improvements from a start where G_σ̄'s switch-best needs 2. The slowness is
  entirely the selection rule «improve in G_σ̄, choose by G_τ» with σ̄ ≠ τ on 16-32 Odd vertices.

## 5. Corpus (box121/runcorp.sh; L-SI box 53's 1,132 runs)
- Every run: ROOTOK; PLAY-CONTAIN 172,104 / 172,104 Ξ-changes at stretch transitions (path only 167,514); the 15,665 fresh-fed
  transitions (inconsistent or not) all contained.
- PHL falls inside a stretch in 660 runs (12,920 rises, 4,730 falls in total). The §2 DEAD holds broadly, not only on cp_K4.
- Stretch transitions: 17,841 (= box 118's climb steps). 5,663 have an Odd link. 12,275 lie in TWO-FIX windows.
- Longest TWO-FIX window per run (722 runs with one):
  - ODIFF = 0 in 354 runs. 316 equal G_τ's switch-best run step for step; 38 differ at one final fallback step (SB < 0, see §4).
  - ODIFF > 0 in 368 runs. The largest L / n is 3.34 (lend107_n32: L 107, ODIFF 3). Longest: s3quad_K8_m30 263 (ODIFF 32), lend107_n32
    107, returns_ph64 93 (ODIFF 1, SB 37), lend82_n32 81, b5_os_n40 77 (ODIFF 1, SB 7).
  - Even ODIFF = 1 gives windows far longer than switch-best (b5_os_n40: 77 against 7). Caveat: that run has 9 S4c fallbacks, so part of
    its window may be fallback steps. cp / suf / s3quad have 0 fallbacks.

## 5b. Pins (box121/pincheck.sh → pincheck.txt)
- cp_K4 (box113/inst/cp_K4.pg sha1 db621f0ab3a8…, start cp_K4.start 4c8694a84f79…).
- n5-exhaustive/instances/b5_os_n40.pg (00fc4562fea7…). It has no start file in the corpus, so box121/inst/b5_os_n40_default.start
  (3301f31e2e0a…) writes out n5x's default start.
- red/seg/instances/s3quad_K8_m30.pg (9576333116f7…, start box116/inst/s3quad_K8_m30_default.start 3a0f39323865…).
- On all three: Oink 8fbf0a7 --zlk and --tl «solution verified»; N5's regions = Oink's (box107/pinwin.py AGREE True); L-COMP's n5b and n5x
  give identical state sequences (44 / 81 / 264 iterations). brtree.py and twofix.py lines as in §2-§5.
- lend107_n32 and fbg_K12_m6_m24 are pinned in box120/pincheck.txt.

## 6. READING (not to sign)
- PLAY-CONTAIN shows that the best-response-tree view adds no counting power by itself. A Ξ-change is always «below» a σ-switch, and a
  switch can move a subtree of any size.
- Inside a τ-stretch, a step is of one of two kinds:
  - (a) a σ̄-change step: Odd's response to σ moves; this is the fbA / fbg regime;
  - (b) a TWO-FIX step, which is an improving switch in a fixed one-player game G_σ̄ chosen by a second fixed one-player game G_τ.
- The trivial bound is stretch ≤ #(σ̄-change transitions) + Σ window lengths.
- TWO-FIX is a pivot rule for strategy improvement on one-player games: the improving set comes from G_σ̄ and the choice from G_τ.
  - Pointers I have NOT opened, so they are not sources here: L-LIT's docs/lit/T12-MSF-barriers.md records Post-Ye 1208.5083 (Dantzig's
    rule strongly polynomial on deterministic one-player discounted MDPs) and an Ω(2^L) bound for a least-significant-switch rule on
    one-player sink games.
  - So one-player SI is polynomial for some rules and exponential for others. Whether TWO-FIX's rule is of the first kind is the
    question. This links the τ-stretch core to the pivot-rule / simplex literature, not to games.
- Candidate next box (untested): TWO-FIX-POLY, i.e. bound a TWO-FIX window by a polynomial in n and ODIFF; or build a TWO-FIX family
  where L grows exponentially in ODIFF, which would be an L-RED-type adversary, not mine to run.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box121/{brtree.py, twofix.py, runred.sh, red.txt, runcorp.sh, b_sbcg.txt, b_alt.txt, pincheck.sh,
  pincheck.txt, inst/b5_os_n40_default.start}; check.sh block
  «box 121».
- FINDINGS:
  - PLAY-CONTAIN PROVED (lane): the containment the Lead asked about is automatic, including the cycle.
  - The forest potentials PHL / PDEP are DEAD as monotone potentials (cp_K4: PHL falls 5 times).
  - TWO-FIX PROVED (lane): a window with τ and σ̄ fixed is SI on the one-player G_σ̄ selected by G_τ.
  - DATA: cp / suf / s3quad are one TWO-FIX window each (43 / 151 / 263 steps against switch-best 2). Corpus: 12,275 of 17,841 stretch
    transitions lie in TWO-FIX windows, and ODIFF = 1 already gives 77 against 7 (b5_os_n40).
- NEEDS: Lead: GO or redirect on TWO-FIX-POLY (bound via ODIFF), or route the TWO-FIX selection rule to L-RED as an adversary target.
