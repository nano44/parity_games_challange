# Box 131 N5-CANON: which W-optimal strategy S4a's procedure returns, and FL runs under that rule
L-NEW successor 45, 2026-11-01 10:38-10:5xZ (date -u). Lead GO 10:41Z. Code: experiments/new/box131/ (canon.py, runcorp.sh, c_corpus.txt).
check.sh block «box 131 CANON». Pin: u2flat73_n32 (box 130 pincheck.txt: Oink --zlk / --tl verified, n5b identical). Labels: PROVED
(lane), DATA, READING. «Corner» = an option's play runs through the mover (box 128 W2).

## 0a. Attribution (added 11:1xZ after the Lead's 11:08Z relay of L-RED 42's R177 interim)
- The rule of §0 and the per-vertex potential of FL-CANON are ALREADY SIGNED: RESULTS R24 (b) Lemma TB, with R24 (a) Lemma R (S1's
  restriction keeps every fully optimal successor), both on 𝒞^1O. R24 (c) Lemma CASC bounds W-flat runs there.
  - FL-CANON (a)/(b) below is my re-derivation. What is new here: the every-game DATA (813 pairs) and Lemma KEY=VJ.
  - §1's «not proved line by line» identification is R24 (a) Lemma R on 𝒞^1O.
  - On every game, TB / R are lane readings until both referees lift them (Lead reading L44). Nothing here cites them on every game.
- L-RED 42 (interim, relayed): the CASC digraph D (Even v → u if u lies on v's W-play prefix or on the Ξ-play of a W-tight option of v).
  If D is acyclic, FL ≤ height(D) + 1. The lex-min rule alone allows 2(2^(d+1) − d − 2) transitions on a 2-wide W-ladder under adversarial
  availability. So only Ξ-availability can bound FL, which agrees with §3 (ii).
- DATA on D (experiments/new/box131/dcyc.py, rundcyc.sh, d_corpus.txt; my reading of D at the FL run's first state; 813 distinct pairs):
  - 20 maximal FL runs (τ-stretch level), the longest 8 transitions (u23sw64_n32).
  - D acyclic in 4 runs (max height 14, u1t_cex_n32), with CASC's bound holding: 0 violations.
  - D cyclic in 16 runs. In 7 of them every nontrivial SCC contains a Ξ-edge whose Ξ-play passes an ODIFF vertex; in 9 some SCC has
    none (e.g. u23sw64_n32, cw11_n24).
  - So «charge each D-cycle to an ODIFF vertex on a Ξ-play» fails as stated in 9 runs. Not tested: L-RED's other source of upward edges,
    the W-cycle. My D may differ from L-RED's unpushed definition, so this is DATA only, not a DEAD.

## 0. Answer
- The canonical optimum (SPEC S1 (iv) on S4a's dual arena; Even = the dual's Odd), for Even x whose W-cycle node is c:
  - c odd (Even prefers LONGER paths): among the W-tied arena options, the SMALLEST INDEX («first strict maximum in list order»);
  - c even (Even prefers SHORTER paths): among the W-tied arena options, the one with the lexicographically smallest BFS KEY, where
    key(y) := the play path from c to y, written from c's side with c excluded. BFS from c over predecessors in list order discovers
    vertices in exactly this order.
  - DATA, 813 distinct pairs, every non-fallback transition with τ fixed, every real tie: c even 666 / 666, c odd 8 / 8 (non-corner);
    corner 42 / 45 and 0 / 1. Smallest index FAILS as a description at c even: 483 / 666.
- FL iteration under that rule:
  - c odd: polynomial. The index of σ(x) strictly decreases at every FL move (Theorem FL-CANON (a)), so x makes ≤ deg(x) − 1 such
    moves per FL run.
  - c even: the BFS key of every vertex is non-increasing over an FL run, strictly at every move (Theorem FL-CANON (b)). DATA: 168 /
    168 non-corner FL moves; the other 9 are the cycle node itself, key (). Its range is the number of W-tight shortest paths from c,
    exponential in general. So (b) is a potential specific to the rule, NOT a polynomial bound.
- Exactly how the rule can follow gen(n) (§3): on equal-length paths the BFS-key order IS an all-even CDAG order (VJ order with
  relevance = index), so there is no order mismatch to block it. Two things are needed for an embedding, both for L-RED R177:
  - (i) a G_τ in which all CDAG paths used are W-tied, which includes equal length;
  - (ii) Ξ-gating that releases one switch at a time. The procedure itself is switch-BEST in key order among the released options,
    not single-switch.
- Input from L-RED 41 R176 (claude/l-red 76601782, docs/red/R176-depth.md), recorded as asked:
  - Box 129's «ODIFF ≥ 1: D ≤ 4» is a START effect. topfix_n10 from its own start file (new/box52/out/topfix_n10.start) has long
    ODIFF-1 windows with charge depth 59. On topfix_nk (n = 21k), D = 6k − 1 from k = 6, fan-in ≤ 10, on linear runs (K ≈ 2.3n).
  - So GATE-REC's bound roots·(F + … + F^D) is exponential on a provably polynomial family. A useful chain bound needs additivity
    along chains, or a different charge.
  - My corpus uses topfix_n10 WITHOUT its start file (si/anc58/corpus_fixed.lst l. 508, as in sbcg.lst), and my box 128-129 pins say
    «default start written out». Both are consistent, but they do not show the start-file behaviour.
- Correction to box 130 §0 («most flat moves ride along with W-strict moves (u2flat73_n32: 73 flat moves, 7 FL transitions)»):
  WRONG for that instance. All 73 flat moves of u2flat73_n32 lie INSIDE its 7 FL transitions (many movers per transition; FLMOVES 73).
  - Over τ-stretches: 181 moves in FL transitions against box 130's 247 flat moves, so most flat moves are in FL transitions.
  - The correct reading: FL TRANSITIONS remain the unit for TF-RED, and they are few (box 130 §3).

## 1. Derivation of the rule from SPEC S1 (READING; DATA above)
- S4a computes σ_new as Odd's counterstrategy in the DUAL of the arena H to τ. In G^d the priorities are Ω + 1, so a cycle node v with
  Ω^d(v) even has Ω(v) odd.
- S1 (iv): «if Ω(v) even, Odd takes the LONGEST path … first strict maximum wins; if Ω(v) odd, the SHORTEST (BFS from v over
  predecessors in list order; first discovery sets Odd's choice)».
- Read in G: c odd ⇒ longest, ties to the smallest index; c even ⇒ BFS.
- Ties: two arena options of x with equal W-values have equal path sets above c. So step (iii)'s deletions treat them alike: for each
  u, both lie in M or neither does. Both survive whenever x's chosen edge survives, and they have equal lengths. So the longest case
  picks the smallest index among them.
- In the BFS case, x is discovered from its first-dequeued surviving successor in layer d − 1. Layer d is ordered by
  (order of parent, own index), so the discovery order is the lex order of the c-side path.
- That the surviving successors in layer d − 1 are exactly the W-tied options is supported by DATA (KEYMIN 666 / 666); it is not
  proved line by line.

## 2. PROVED (lane)
- Setting: a maximal run of consecutive FL transitions (W_j = W_{j−1}) inside a fallback-free τ-stretch, standing premise 1E-N3 =
  RESULTS R102 (S4B-OPT). The rule of §0 holds (READING §1 + DATA).
- Theorem FL-CANON.
  - (a) If x's W-cycle node c is odd, every FL move of x strictly lowers the index of σ(x). Hence ≤ deg(x) − 1 such moves per FL run.
    - Proof: by FL-OPT (box 130), σ_{j−1}(x) is W-optimal in the arena, so it lies in TIE_j(x). The rule picks min TIE_j(x) ≤
      σ_{j−1}(x), with equality only if x does not move. ∎
  - (b) If c is even, K_j(x) ≤ K_{j−1}(x) lexicographically for every x of c's class (non-corner), with strict inequality when x moves.
    - Proof: by induction on the layer d = ℓ (constant over the run, since W is). Layer 1: K = (x) is fixed. Layer d:
      K_j(x) = (min_{y ∈ TIE_j(x)} K_j(y), x). σ_{j−1}(x) ∈ TIE_j(x) (FL-OPT), so K_j(x) ≤ (K_j(σ_{j−1}(x)), x) ≤ (K_{j−1}(σ_{j−1}(x)),
      x) = K_{j−1}(x), using induction on layer d − 1.
    - Distinct vertices have distinct keys (last coordinate), so the argmin is unique and strictly smaller when x moves. ∎
  - (c) Count. FL run length ≤ Σ_{x : c odd} (deg(x) − 1) + Σ_{x : c even} D(x), where D(x) := the number of distinct keys x takes.
    D(x) ≤ Σ_{y ∈ T_x} D(y): exponential in the layer depth in the worst case. No polynomial bound on D is claimed.
- Lemma KEY=VJ. Let P, Q be c-side paths of equal length; their keys are the paths' vertex sequences. If every key coordinate
  sequence is increasing, as in CDAG_n (paths descend towards c = 0), then key(Q) < key(P) iff min(P Δ Q) ∈ Q. That is CDAG_n's
  (all-even) VJ order with relevance = index.
  - Proof: for two increasing sequences of equal length, the first differing position holds the smaller of the two elements there.
    That element is min(P Δ Q). ∎ (In general keys are not increasing, and the key order is by INDEX, unrelated to priority.)

## 3. What R177 has to realise (READING)
- (i) W-ties: TIE(x) needs equal W-values, including length. CDAG_n's 2^n − n − 1 chain uses paths of every length. A fixed-length
  slice has at most C(n − 1, k − 1) paths (still exponential at k ≈ n/2). Whether a chain inside one slice is long is not checked.
- (ii) Gating: in an FL step every Even x jumps to its key-best RELEASED option (switch-best in key order). A long climb therefore needs
  Ξ (on G_σ̄) to release options one at a time in key order. This is the TWO-FIX pattern one level down: an «arena optimum of one
  order, gated by another game's improvements». Box 121's TWO-FIX had (W, Ξ); here it is (key, Ξ).
- So the exact way the rule can follow gen(n) is through Ξ-gating. The rule alone is switch-best in key order and cannot be
  single-switch.

## 4. DATA table (813 distinct pairs, c_corpus.txt; every non-fallback transition with τ fixed and Iσ ≠ ∅)
| quantity | c even | c odd |
| --- | --- | --- |
| real ties (non-corner / corner) | 666 / 45 | 8 / 1 |
| rule holds (BFS-key min / smallest index) | 666 / 42 | 8 / 0 |
| smallest index holds | 483 / 26 | (same) |
| moves in FL transitions | 177 | 4 |
| FL moves lowering the mover's key / equal (all 9: cycle node) | 168 / 9 | — |
| FL moves lowering the index | 113 / 177 | 0 / 4 |
| most FL moves of one vertex in one FL run | 6 (u23sw64_n32) | 1 |
- Odd case: the 4 FL moves with c odd (FLDEC_ODD 0 / 4) are one move counted 4 times. nep22f_n64 appears twice in the corpus (with
  and without its start), and has 2 such moves per run (j = 15 and j = 24): vertex 48 is its own W-cycle node and moves 19 → 28. It is
  a corner move, and its old option is not in TIE. Checked by hand (box 131 session). So FL-CANON (a)'s premise holds for none of them.
  Outside FL, the rule-kind move-ties at c odd all lower the index (DEC_ODD 3 / 3).

## 5. Next (Lead decides)
- R177 (L-RED 42): realise (i) and (ii).
- L-NEW: bound D(x) using the gating. Ξ is monotone on G_σ̄ (one-player), and the released set at x is the set of Ξ-improving options.
  This is a two-order problem, the same shape as TWO-FIX-NL.
