# Box 153 N5-CUBE: an IDEAL-ACYC run (degree 2) is a W-gated multi-switch policy iteration on a DECOMPOSABLE acyclic USO (Lemma DECOMP, PROVED lane, Step 1 gate PASSED); multi-switch steps unfold into single improving switches (MULTI→SINGLE); W-free improving paths are already exponential-looking (2-wide Ξ-ladders 8/22/52/114 for n = 4..10), so no Ξ-side-only argument can give IDEAL-ACYC-POLY; no imported theorem fits the W-key rule
L-NEW successor 50, 2026-11-04 (date -u: see the commit). Lead GO 00:47Z (box 153, «IDEAL-ACYC as policy iteration on a decomposable
cube»; Step 1 is the gate; every imported theorem with an opened source; long-path families via my simulator and to the Lead).
Labels: PROVED (lane), DATA, DEAD, CONJECTURE, READING. Model: P-IDEAL-RED §0 (RESULTS R104's definition), degree ≤ 2.
Not a TARGET.md claim; no polynomial bound; IDEAL-ACYC-POLY and G-N5-TIME stay OPEN.

## 0. Answer
- Step 1 (gate) PASSED.
  - Lemma DECOMP (PROVED, lane, §1): the improvement orientation of every degree-2 IDEAL-ACYC genome is a unique sink orientation
    [WW22 Def. 4]. It is acyclic, and decomposable in the sense of [WW22 §2.2] («each face is combed»). In every face the free
    mover of largest π is a combed dimension.
  - Machine check (box153/decomp.py, brute force): 119 genomes (corpus, the R198 / R199 d 5 pins, and random ones with ≤ 10 degree-2
    movers), 603,741 faces. USO 0, COMB 0, ORDER 0, ACYC 0, JUMP 0 violations.
- The cast:
  - An IDEAL step switches the set S_t = {x improving at s_(t−1) whose key-preferred option under the new keys is the better one}
    (C-ELEMENT).
  - So IDEAL = policy iteration with a W-GATED multi-switch rule on a decomposable AUSO.
  - Lemma MULTI→SINGLE (PROVED, §1): S_t unfolds into |S_t| single improving switches, in increasing π. So T ≤ LP(start), the
    longest improving path from the start.
- Known rules on this class (Step 2):
  - Switch-all (JumpAntipodal) reaches the sink in ≤ n jumps on every decomposable USO [WW22 Thm 18 and the remark after it].
  - On acyclic graphs the downstream-first (topological) rule makes at most linearly many switches [MC94 §2]. Both are the same
    fact as DECREMENT here.
  - [MC94]'s exponential examples (Thm 2.8, Cor. 2.9, 2.10) are for STOCHASTIC graphs (average vertices, ½-½ transitions) and a
    one-at-a-time largest-index / topological / difference rule. Their hypotheses do not match the IDEAL model (deterministic
    chains, W-gated multi-switch). Nothing is imported from them.
- Step 3 (DATA, exact per instance: the longest path is a DP over the acyclic cube):
  - Without W gating, improving paths are long.
    - 2-wide Ξ-ladders with K pairs (n = 2K), ranks / parities / starts climbed (box153/ladlp.py): LP = 8, 22, 52, 114 for
      K = 2, 3, 4, 5.
    - These fit f(K) = 2 f(K − 1) + 2K + 2, i.e. about 2^(n/2).
    - Free climbs (longpath.py CLIMB): 10, 16, 23, 38 at n = 4-7.
  - Real IDEAL runs on the same genomes are much shorter (x3_L8: LP 16 vs T 8; dc_d8: 64 vs 23; dd_d5_F14: 35 vs 14).
- DEAD (route): «IDEAL-ACYC-POLY from the Ξ side alone» (any argument that bounds improving paths of the decomposable AUSO without
  the W gate). Instance: the K = 5 Ξ-ladder champion box153/ladlp_5.json, LP 114 > n² = 100 at n = 10; the trend is
  exponential (DATA, not proved).
- CONJECTURE LP-EXP (DATA K ≤ 5): 2-wide Ξ-ladders have improving paths of length 2^(Θ(n)) (recurrence above).
- READING:
  - Every bound must come from the W gate.
  - The gate lets x switch only when its key-preferred option is the better one, and KEYFLIP charges each re-switch to a W-key
    flip. That is the known circularity (KCH-GCH / KEYFLIP), now located precisely: polynomial ⇔ the W-gated rule cannot follow
    exponential improving paths that the Ξ side offers.
  - In USO language the question is whether a «gated» pivot rule, whose gate is itself a lower IDEAL process, can be forced along a
    Klee-Minty-type path. No known theorem covers that rule.
  - Step 3's Klee-Minty-gating encoding is a counter construction again, i.e. L-RED's line. I did not build one in this box.
- Recommendation (Lead decides): close box 153 as a reformulation (DECOMP, MULTI→SINGLE) plus a DEAD route. The open question is the
  W-gated rule.

## 1. Proofs (PROVED, lane)
- Setting. Degree ≤ 2. D2 := the degree-2 movers; degree-1 movers never move and are fixed. The cube is {0, 1}^D2. C_s(x) := the
  strictly better option of x at s (no ties: P-IDEAL-RED ENC).
  - By LOCAL (b), C_s(x) depends only on s at the strict Ξ-descendants of x, so not on s(x).
  - Orient the edge {s, s ⊕ e_x} toward the endpoint whose x-coordinate is C_s(x). This is well defined: both endpoints have the same
    C(x).
  - The improving switches at s are the x with s(x) ≠ C_s(x).
- Lemma DECOMP. This orientation is (a) a USO, (b) acyclic, (c) decomposable: in every face, the free mover of largest π is combed.
  - (c) In a face F, let y be the free mover of largest π. Its strict Ξ-descendants have larger π, so they are fixed on F, and
    C(y) is constant on F. All y-edges of F point to the same side.
  - (a) By induction on the face dimension. A sink of F lies in the facet of F on y's side C(y) (the y-edge at a sink points into
    it). That facet has a unique sink v by induction, and v's y-edge points into the facet. So v is the unique sink of F.
  - (b) E(s) := Σ_x [s(x) ≠ C_s(x)] 2^π(x) falls strictly along every edge. A switch of x to C_s(x) makes x stable and leaves every C
    of a mover with larger π unchanged (those depend only on their descendants, which do not include x). This is DECREMENT for a
    single switch. ∎
- Lemma MULTI→SINGLE. Let an IDEAL step switch the set S at s (every x ∈ S improving at s). Switch the members of S one at a time,
  in increasing π. Each is improving when switched.
  - Proof: when x is switched, only movers with smaller π have changed. They are not strict Ξ-descendants of x, so C(x) is still
    C_s(x) ≠ s(x).
  - So the step is a directed path of length |S| in the orientation, and T ≤ Σ_t |S_t| ≤ LP(s_0). ∎
- Switch-all bound (= [WW22] Thm 18 remark, re-proved here). If every improving mover switches at every step, the largest-π
  improving mover becomes stable and stays stable (its C is fixed, by (c) applied to the whole cube restricted above it). So ≤ |D2|
  steps. This is DECREMENT again.

## 2. Sources opened (also in notes/L-NEW.md)
- [WW22] S. Weber, J. Widmer, «Realizability Makes a Difference: A Complexity Gap for Sink-Finding in USOs», arXiv:2207.05985
  (ar5iv HTML opened 2026-11-04):
  - Def. 4: USO = every non-empty face has a unique sink.
  - §2.2: «each face is combed … decomposable» (after Observation 7).
  - Thm 18 and its remark: JumpAntipodal needs only n vertex evaluations on all decomposable USOs.
  - The same remark, citing Schurr's thesis: exponentially many on some acyclic USOs.
- [MC94] M. Melekopoglou, A. Condon, «On the Complexity of the Policy Improvement Algorithm for Markov Decision Processes», ORSA J.
  Computing 6(2) 188-192 (1994), DOI 10.1287/ijoc.6.2.188 (author PDF, cs.ubc.ca/~condon, opened and text-extracted 2026-11-04):
  - §2: the simple / topological / difference / best-decrease select rules; «if the graph is acyclic the [topological] algorithm
    makes at most linear number of switches».
  - Thm 2.8, Cor. 2.9, 2.10: exponential for difference / topological / simple, on graphs with average (½-½) vertices.
- Klee-Minty 1972 (Inequalities III, Academic Press) and Schurr's thesis: NOT opened; not used.

## 3. Status
- PROVED (lane): DECOMP, MULTI→SINGLE, switch-all bound.
- DATA: decomp.py 0 violations; LP vs T table; Ξ-ladder LP 8 / 22 / 52 / 114.
- DEAD: Ξ-side-only route to IDEAL-ACYC-POLY.
- CONJECTURE: LP-EXP.
- OPEN: whether the W-gated rule can follow exponential improving paths (= IDEAL-ACYC-POLY), G-N5-TIME.
