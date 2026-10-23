# T25: gauntlet step 3 for N8a, Koh-Loho tree SI with the "global" and switch-all rules (L-LIT, 2026-10-23)

Asked by the Lead at 02:10Z (Lead clock). The object is L-NEW's N8a, read on claude/l-new at 4fd179c8:
- spec, fidelity table and bench: docs/new/N8a-kohloho.md (§2 pivot rules, frozen);
- code: experiments/new/kl/kl.py.

Every source below was opened by L-LIT in this session (2026-10-23). sha256 values are in notes/L-LIT.md "Sources opened". "p." is the
printed page (Ohlmann thesis: printed = PDF − 2) unless marked "PDF p.". "L-LIT reading" marks interpretation, not a stated theorem.

**Verdict (step 3): SIGN WITH CAVEATS (§5).**
- No published lower bound covers Koh-Loho SI under ANY pivot rule. The paper itself leaves pivot rules open, and its two citers
  do not study the method.
- N8a lies outside B1-B21 by model. The nearest rows, B8 (Friedmann) and Ohlmann's non-positionality obstruction, are about
  different valuations.
- Neither rule appears in the literature as applied to tree-SI.
- Caveat C1 (§4) matters most for the Lead: the hard bench contains no family built against tree-SI. On every bench family, plain
  SI is already polynomial, so the bench data are weak evidence.

## 0. What is being checked
- **Method.** Koh-Loho Algorithm 1 over the perfect (n, d/2)-universal tree. Odd is the improver. After every pivot µ ← the least
  fixed point of G_τ↑ that is ≥ the current µ (forced increase). The fixed point is computed by Algorithm 3 (Dijkstra on trees).
- **Rule "all"** (switch-all). Every Odd node with an admissible arc switches to the arc with the largest Tighten(µ, vw).
- **Rule "global".**
  - Even's counter-strategy σ is read off µ.
  - Odd's one-player game is then solved exactly in the arena where Odd may use τ(v) or any admissible arc, and Even is fixed to σ.
  - Odd's winning set gets the cycle/attractor strategy. All other Odd nodes with an admissible arc use the switch-all choice.
- **Bench.** Pivots stay small on all 13 hard families, both rules, all outputs verified. Random games (step 2) are still pending.

## 1. Known lower bounds for the method and its relatives
| source (opened) | statement | covers N8a? |
| --- | --- | --- |
| Koh-Loho arXiv 2108.13338 v5 = LMCS 21(2:24) 2025, sha256 21ee0e43… (= L-NEW's copy) | p.24:3: "The total number of strategy iterations is trivially bounded by n\|L(T)\|, the same bound for the progress measure algorithm"; "Identifying a pivot rule that may provide strictly improved (and possibly even polynomial) running time is left for future research." Alg. 1 and Thm 3.1 p.24:9: correctness only. No lower bound and no experiments (grep: no "experiment", "empiric" or "conclusion" section) | **no lower bound exists**. Only upper bound: n·n^(d/2) iterations for the perfect tree |
| MFCS 2022 version, LIPIcs.MFCS.2022.63, sha256 553cf18c… | same "left for future research" sentence (p.63:3) | same |
| Semantic Scholar citers of 2108.13338 (2 records): Majumdar-Saglam-Thejaswini arXiv 2401.07548 (sha256 33b041fc…), Loho-Maat-Skomra arXiv 2503.17294 v1 (sha256 32460e2c…) | 2401.07548 PDF p.3: cites KL only in "Universal trees are found underlying all the quasi-polynomial algorithms". 2503.17294 PDF p.3: "Strategy improvement has been considered more generally on lattices [7, 34]" | **no**; neither studies KL's iterations |
| Loho's publication list (lohomath.github.io, fetched 2026-10-23) | only KL, van Dijk-Loho-Maat 2309.02223 (B11) and Disser-Loho-Maat-Mosis 2512.16684 (B9) on this topic | no follow-up by the authors |
| Ohlmann PhD thesis, Université Paris Cité 2021, "Monotonic graphs for parity and mean-payoff games" (pageperso.lis-lab.fr/pierre.ohlmann/contents/these.pdf, sha256 a5c909cb…) | Thm 9.1 p.167: a fixpoint valuation "uniformly positionally determined for Adam over finite arenas has improving switches". Ch. 9 §2.3 p.170: the Jurdziński/Walukiewicz valuation over [0, n−1]^(d/2) "is not positional for Adam" (Fig. 9.2). The same holds for the quasi-polynomial trees: "We believe that this fact underlies the non-availability, as of today, of quasipolynomial strategy improvements." On KL, p.171: "seemingly contradicting our discussion"; there "the progress measure ... is forced to increase; it does not necessarily correspond to the least fixpoint of G_τ ... each strategy may arise multiple times" | **an obstruction to classical SI over tree labels, not a lower bound.** KL (and N8a) avoids it by forcing increase. No iteration bound for KL |
| Ohlmann thesis, p.17 (intro, "Strategy improvements") | "To date, no quasipolynomial strategy improvement algorithm is known" | context only |
| Friedmann arXiv 0901.2731 v1 (sha256 6c56adb2…) | Thm 8: 13·2^n − 9 iterations on G_n, locally optimizing policy (VJ valuations). §6: the same family with "simple transformations" covers "both variants ([12] and [10]) of Schewe's globally optimizing technique". A random initial strategy also gives super-polynomial expected time, stated "without proof" | **no, by model**: VJ valuations, and the start strategy is part of the construction |
| Friedmann arXiv 1106.0778 v2 (sha256 46c96f44…) | Thm 6.14 (I^loc, switch-all) and Thm 8.4 (I^glo, "computes a globally optimal successor strategy", §4) | **no, by model**: same reason (B8) |
| van Dijk, Two Counters, EPTCS 305.8 (tvandijk.nl/pdf/2019tc.pdf, sha256 9d2da849…) | §9.4 p.14: SPM and the quasi-polynomial progress-measure algorithms "are certainly slow ... but this is not due to the design of the Two Counters games. Rather, these algorithms tend to be extremely slow even for trivial games"; "strategy iteration [15] ... is the only algorithm that can quickly and in polynomial time solve the Two Counters games" | tc is **not** a lower bound for any SI. See C1, C2 |

Searched with no further hits:
- web search for KL with "lower bound", "pivot" and "exponential";
- web search for "strategy improvement" with "progress measures" and "hybrid lifting".

Hybrids were looked for (tree SI, progress-measure SI, lifting/attractor SI):
- found only those above, plus the non-oblivious snare SI. Snare SI has Friedmann's super-polynomial bound (cited in Ohlmann's intro as [Fri13]), but it uses VJ valuations and memorized snares, so it is not N8a.
- **No exponential or quasi-polynomial family exists for any pivot rule of tree-SI.**

## 2. Have the two rules been studied?
- **Switch-all on KL.** Not studied. KL fixes no rule, and Fig. 4 (p.24:10) is a 2-iteration example.
  - The classical analogue is Friedmann's I^loc (B8, exponential).
  - KL's switch-all is a different rule: it acts on tree labels, picks the largest Tighten, and the labels are history-dependent
    through the forced increase. Friedmann's bound does not transfer (§3).
- **"Global" on KL.** Not found anywhere.
  - Nearest relative 1, Schewe's globally optimizing policy (switch-best: the best valuation over all combinations of improving
    switches, with the opponent best-responding). Exponential for VJ (0901.2731 §6; 1106.0778 Thm 8.4).
    - N8a differs. It optimizes a QUALITATIVE target (Odd wins a one-player game against a FIXED σ) inside the admissible arena,
      not a valuation against a best-responding Even.
    - Odd nodes outside that win fall back to switch-all.
  - Nearest relative 2: N5 (T20), the same "best response against the opponent's current strategy in the improvement arena" idea.
    - N5 uses VJ valuations and moves both players.
    - N8a moves only Odd; σ is derived from µ, not maintained.
- **L-LIT reading.** "Global" is the N5 idea transplanted, one-sided, onto KL tree labels.

## 3. Barrier fit, B1-B21 (BARRIERS.md)
| row | N8a | why |
| --- | --- | --- |
| B1, B2 universal-tree / separator size | **outside, by model** | The size bounds lower-bound algorithms that traverse the value domain (value iteration; CFGO Cor. 6.13 is "informal"). KL uses a universal tree only as a value domain. Each iteration jumps to a least fixed point in O(d(m + n log n)) (Thm 4.5) without walking L(T). No theorem bounds KL iterations by any function of \|T\|. N8a uses the perfect tree (size n^(d/2)), so quasi-polynomial tree size is irrelevant. The only proven iteration bound is n^(d/2+1) (p.24:3). Polynomiality must come from the rule, not the tree |
| B3 ANP nested fixpoints | **outside** | KL reads the explicit graph (SCCs, base nodes, Dijkstra, strategies), not a black-box f |
| B4-B7 attractor/dominion families | **outside the class; families are data** | N8a is SI. "Global" uses exact one-player attractors only as a subroutine. Completeness holds by Thm 3.1, so B7 (incompleteness) does not apply. B5/B6 families are in the bench |
| B8 Friedmann switch-all / switch-best / Zadeh / Cunningham | **outside, by model** | Every construction is for VJ valuations (or MDP/LP analogues) from a fixed start. KL labels are least-fixed-point tree labels with forced increase; strategies can repeat (p.24:9). Ohlmann p.170 shows these labels are not even an SI valuation in the classical sense. **Open:** a Friedmann-style counter built against KL labels. Nobody has tried one (§1) |
| B9 index-based single-switch | **outside** | multi-switch, label-based |
| B10 randomized | **outside** | deterministic |
| B11 symmetric SI | **outside** | only Odd's strategy is maintained; σ is a function of µ |
| B12 PSPACE path prediction | **outside** | proved for VJ all-switches; no analogue for KL |
| B13-B15, B18, B21 LCP / USO / IPM / discounted | **outside** | no LCP, cube, LP path or discount |
| B16 time-bounded weak separators | **outside** | no automaton |
| B17 complexity | consistent | - |
| B19 LDT representability | **outside** | weight-compression statement for mean payoff, not a running-time bound. KL labels are O(d log n) bits (L-NEW §0) |
| B20 deep-trap switchallexp (DATA) | **outside** | against Howard on discounted rewards |

**Summary.** No row applies. The method sits exactly where Ohlmann (p.170-171) and KL (p.24:3) say the question is open:
"possibly even polynomial ... left for future research".

## 4. Caveats (the "with caveats")
- **C1. The bench is not adversarial for tree-SI.** Each bench family is easy for classical SI with some rule or start. N8a's small
  counts are expected of an SI method and do not separate it from classical SI.
  - The Friedmann families are exponential only for the targeted PGSolver rule and its start strategy. Oink psi is linear on both
    (experiments/hard-families/switchallexp/README.md: 132 major iterations at N = 64; switchbestexp: 390).
  - tc is polynomial for strategy iteration (van Dijk §9.4 p.14).
  - In the repo data, psi is 7..93 major iterations on tc for N = 2..32 (experiments/hard-families/results/tc.md).
  - **Needed before step 4: a family built against KL labels** (an L-RED box). Also needed: the random-game half of step 2.
- **C2. Mis-citation in N8a-kohloho.md §3 "Reading".** It says tc is "exponential for the progress-measure algorithms on the SAME
  perfect tree, BARRIERS B6".
  - B6 lists zlk, pp, dp, rr, rrdp, tl, atl, not SPM.
  - van Dijk §9.4 says SPM slowness "is not due to the design of the Two Counters games".
  - The repo does measure tspm super-polynomial on tc: 221 lifts at N = 2, 25,938,757 at N = 12, timeout at 14 (results/tc.md).
    That is an Oink measurement, not B6.
  - The Lead should have the line corrected.
- **C3. Dual runs carry the B8 test.** Friedmann's families make Even (player 0) the improver, so for N8a the relevant counts are
  the DUAL ones.
  - switchbestexp dual is non-monotone: global 13, 34, 27, 33; switch-all 20, 21, 54, 60, for N = 1..4 only.
  - Four points cannot show polynomial growth. Larger N is needed.
- **C4. Start strategy.** Friedmann's bounds fix the start. kl_init.py's random starts cover only tc and counter_qpt, not the
  switch* families.
- **C5. No upper bound.** The only proven bound is n·n^(d/2) iterations, worse than quasi-polynomial. A step-4 proof must bound
  iterations for the specific rule. No lemma in KL helps beyond monotonicity (Thm 3.1's proof).

## 5. Novelty
- **Not found anywhere:** "KL SI with this rule (or switch-all) is polynomial on these families". This covers KL (no experiments),
  its 2 citers, Ohlmann's thesis, Loho's list and web search.
- The observation is new as DATA. It is not a claim (D1).
- Given C1, its novelty is low except on families built against KL, and none exist yet.

## Sign-off
L-LIT signs step 3 for N8a WITH CAVEATS C1-C5:
- outside every known framework, by model;
- no lower bound for KL under any rule;
- the decisive missing evidence is an adversarial family against KL labels (C1, C3).
