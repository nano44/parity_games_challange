# Box 151 N5-NEST: R199's nested-doubling refutations are WAKE-ORDER obstructions (r199/xwake.py lacks antisymmetry); Lemma NEST-BARE (PROVED, lane): no k ≥ 2 nested schedule runs on the bare ladder; wake-order lower bound «k nested doublings need ≥ ⌈k/2⌉ levels above» (EXACT z3 relaxation, k ≤ 5, any gates); the brief's candidate bound needs value semantics and an exponential cost, so it stays OPEN
L-NEW successor 50, 2026-11-03 (date -u: see the commit). Lead brief BOX 151 (proof side): turn L-RED 48's R199 (k = 2 nesting SAT at d 5,
k = 3 UNSAT at d 5, «empty core over main Ξ-requirements, pure wake-order relaxation SAT, so the obstruction lives in the value semantics»)
into a lemma. Labels: PROVED (lane), EXACT (z3 on a sound relaxation; machine-checked, not Lean), CONJECTURE, DATA, DEAD, READING.
Model: IDEAL-ACYC (RESULTS R104 definition, restated in docs/new/P-IDEAL-RED.md §0), degree 2, 2-wide W-ladder (R198 §1 notation).
Not a TARGET.md claim; no polynomial bound; G-N5-TIME and IDEAL-ACYC-POLY stay OPEN.

## 0. Answer
- FINDING (tool defect, for L-RED; l-red 2f60fa74, experiments/red/r199/xwake.py): the «x reaches y» relation is not acyclic.
  - DEG=1 (default): re(x, y) := e(x, y) ∨ ∃w (e(x, w) ∧ re(w, y)) for x ≠ y, and re(x, x) := false separately. A 2-cycle of edges
    x → y → x satisfies every clause.
  - DEG=0: transitivity is imposed only for three distinct movers, so re(x, y) ∧ re(y, x) is allowed again.
  - The SAT model of xwake.py on the bare k = 3 target (d 4, E = 0) has re(0, 1) and re(1, 0).
  - Fix: one clause ¬(re(x, y) ∧ re(y, x)) for x < y. It holds on every acyclic Ξ-graph. It removes every cycle, since on a real cycle
    the recursion relates every pair both ways.
- With the fix, the wake-order relaxation (xwake.py's clauses K, RR, LAG, CBIT, unchanged) reproduces every exact R197 / R199 result on
  the genk nested targets, in seconds (§2 table). So the d 5 refutation of k = 3 does NOT need the value semantics of the aux movers.
  - R199's «xwake.py … is SAT: the d 5 refutation needs the priority-value semantics» (l-red notes/L-RED.md l. 88-90) rests on the
    missing clause.
  - READING: up to d 5 the nested obstruction is order-theoretic (who can wake whom in an acyclic order), so hand proofs as in R199 §2
    are possible. §1 gives one for every k.
- PROVED (lane), §1, Lemma NEST-BARE: for every k ≥ 2, no 2-wide degree-2 IDEAL-ACYC ladder runs NEST(k)'s mover sets at steps 2-5
  unless some mover outside the k + 1 stack levels moves at one of the steps 2-5. In particular the bare ladder (d = k + 1) never runs
  NEST(k). Gates are not fixed. This generalises R199 §2 (k = 3 there).
- EXACT (z3, sound relaxation), §2: the least number E_min(k) of ladder levels above the stack for which the wake-order relaxation is
  satisfiable:
  - with the main gates of build.py: E_min = 2, 2, 3, ≥ 3 for k = 2, 3, 4, 5;
  - gate-free (main key orders free, changing only at steps where a mover at or below their level moves): E_min = 1, 2, 2, 3 for
    k = 2, 3, 4, 5 (k = 5: E = 2 UNSAT 205 s, E = 3 SAT 229 s). k = 6 at E = 2, 3: running at the push (§2).
  - Every UNSAT row is an exact lower bound for real runs: every clause is a consequence of the IDEAL rule. So «NEST(k) needs
    ≥ ⌈k/2⌉ levels above the stack, for any gates and any Ξ-graph» holds for k ≤ 5. Every SAT row is only a relaxation witness.
- READING on the brief's candidates (why this is NOT yet a bound):
  - «nesting depth ≤ c · (levels above)» is consistent with the data (c = 2 fits E_min ≥ ⌈k/2⌉ for k ≤ 5). But it does NOT imply a
    polynomial bound. A ladder of d levels could then stack k = 2d/3 doublings under d/3 levels, with F_top ≈ 2^(2d/3) and run length
    ≥ F_top.
  - «DBL_l − ZERO_l ≤ f(levels above l)» with f polynomial WOULD imply Σ_l F_l = poly (F_l ≤ F_(l−1) + 1 + f(d − 1 − l)). Applied to
    NEST(k) with E levels above (top doubled level: DBL − ZERO = F_k − F_(k−1) − 1 = 3 · 2^(k−1) − 1), it forces E_min(k) ≥ f^(−1)(3 · 2^(k−1) − 1),
    i.e. the stack must need EXPONENTIALLY many (in k) levels above it. The wake order gives only ⌈k/2⌉.
  - So any proof of the candidate must use the value semantics (P-IDEAL-RED MONO: current Ξ-values never fall; face values are monotone).
    The wake order alone cannot do it, unless E_min grows much faster beyond k = 5.
  - Conversely, if the wake-order witnesses (k = 3 at E = 2, d 6; k = 4 at E = 2 gate-free, d 7) are realisable in the exact model,
    a family k ↦ (k nested, ≈ k/2 levels above) would be a super-polynomial IDEAL-ACYC family, which kills FL-POLY by R104.
  - Those witnesses are in experiments/new/box151/hints/ (aux schedules, reach order, main key orders) as L-RED targets.
- DEAD: the per-level form with f independent of F_(l−1) as a route to a CONSTANT bound. dd_d5_F14 level 3 has DBL − ZERO = 7 = F_2 + 1
  with one level above: a single level can double fully at one level of height, so the danger is compounding, not one large jump.
  (Not DEAD: «DBL_l − ZERO_l ≤ f(a)» for some f; no exact datum refutes it. It is OPEN and needs f exponential, per the reading above.)
- CONJECTURE NEST-DEPTH (open, DATA k ≤ 5, wake-order only): E_min(k) = ⌈k/2⌉ in the gate-free wake-order relaxation.
  - If the exact model has the same E_min, IDEAL-ACYC-POLY is FALSE on 2-wide ladders, assuming NEST(k) with ⌈k/2⌉ levels above is
    realisable for every k.
  - If the exact E_min is exponential in k, the brief's candidate holds for these schedules.
  - Either way, the next decisive datum is an EXACT run of k = 3 at E = 2 (d 6) or k = 4 at E = 2 (d 7, gate-free).

## 1. Lemma NEST-BARE (PROVED, lane)
- Schedule NEST(k) (r199/genk.py, NPER 3).
  - P = 2^k, L = 3P.
  - For 1 ≤ j ≤ k, level j has a prompt mover p_j moving exactly at the steps τ ∈ [1, L] with τ ≡ 1 (mod 2^(k−j+1)), and a late mover
    q_j moving exactly at τ ≡ 1 + 2^(k−j) (mod 2^(k−j+1)).
  - The two level-0 movers move once each, at P + 1 and 2P + 1.
  - Hence, for k ≥ 2:
    - at an even step, the only stack mover is q_k (all others need τ odd);
    - at a step τ ≡ 3 (mod 4) the stack movers are exactly p_k and q_(k−1). For j ≤ k − 2, p_j needs τ ≡ 1 (mod 2^(k−j+1)) with
      k − j + 1 ≥ 3, and q_j needs τ ≡ 1 + 2^(k−j) with 2^(k−j) ≥ 4, so both are ≡ 1 (mod 4). Level 0 moves at P + 1 ≡ 1 (mod 4).
- Three facts (degree 2, any IDEAL-ACYC genome, any gates).
  - (F1) LOCAL (P-IDEAL-RED Lemma LOCAL (c)): if no mover of level < lev(x) moves at step t, then KP_t(x) = KP_(t−1)(x). Here KP_s is
    the key-preferred option under the keys of s.
  - (F2) LAG: if x moves at t ≥ 2, did not move at t − 1, and KP_t(x) = KP_(t−1)(x), then a strict Ξ-descendant of x moved at t − 1.
    - Proof. Put o := s_(t−1)(x) = s_(t−2)(x) and w := s_t(x).
    - At step t, x takes the key-least option of A_(t−1)(x) ∋ o under the keys of s_t, and leaves o. So w = KP_t(x) = KP_(t−1)(x).
    - Suppose w ∈ A_(t−2)(x). Then step t − 1 takes the key-least element of A_(t−2)(x) = {o, w} under the keys of s_(t−1), which is w,
      and x moves at t − 1. Contradiction.
    - So w ∉ A_(t−2)(x) and w ∈ A_(t−1)(x). The comparison of x's two faces changed between s_(t−2) and s_(t−1), and by P-IDEAL-RED
      LOCAL (b) some strict Ξ-descendant of x is in Mv_(t−1). ∎
  - (F3) RE-REVERSAL: if x moves at a and next at c > a, a strict Ξ-descendant of x moves at some step in [a, c − 1].
    - Proof. Let C_s(x) be the strictly better of x's two options at s. Two faces never tie (P-IDEAL-RED ENC: distinct β-sets).
    - A mover moves only to a strictly better option (P-IDEAL-RED §0). So the move at a to o needs C_(s_(a−1))(x) = o, and the move at
      c from o to w ≠ o needs C_(s_(c−1))(x) = w.
    - So C(x) changes at some step in [a, c − 1], and LOCAL (b) gives the descendant. ∎
- Lemma NEST-BARE. Let k ≥ 2. Take any degree-2 IDEAL-ACYC genome containing a 2-wide ladder stack, levels 0..k, whose run moves
  exactly the NEST(k) stack movers at steps 2, 3, 4, 5. Assume also that no mover outside the stack moves at steps 2-5. Then the genome
  is not Ξ-acyclic, a contradiction. So such a run does not exist; in particular the bare ladder never runs NEST(k).
- Proof. Mv_2 = Mv_4 = {q_k}, Mv_3 = {p_k, q_(k−1)}, and p_k ∈ Mv_5, by the schedule.
  - (a) q_k moves at 4 and not at 3, and no mover of level < k moves at 4. By F1 and F2, q_k reaches (Ξ) a mover of Mv_3 = {p_k, q_(k−1)}.
  - (b) q_(k−1) moves at 3 and not at 2, and no mover of level < k − 1 moves at 3. By F1 and F2, q_(k−1) reaches a mover of
    Mv_2 = {q_k}.
    - So q_(k−1) reaches q_k. Acyclicity excludes q_k → q_(k−1), so by (a) q_k reaches p_k.
  - (c) p_k moves at 3 and next at 5 (not at 4). By F3, a strict Ξ-descendant of p_k lies in Mv_3 ∪ Mv_4 = {p_k, q_(k−1), q_k}.
    - It is not p_k itself, and not q_k (q_k reaches p_k, acyclicity). So p_k reaches q_(k−1).
  - (d) p_k → q_(k−1) → q_k → p_k is a cycle of the Ξ-reachability order. Contradiction. ∎
- Does NOT claim:
  - anything when movers above the stack move at steps 2-5 (they can be wakers; that is how k = 2 succeeds with E = 2);
  - any bound on F_l, DBL_l or run length;
  - anything beyond the NEST(k) schedule family.
- Relation to R199 §2: the same cycle (u3 → v2 → x_3 → u3 there), now for every k ≥ 2, any gates, and with F1-F3 proved from the model.
  R199 cites R189 LAG / RE-REVERSAL from lane files.

## 2. EXACT runs of the wake-order relaxation (experiments/new/box151/; z3-solver 4.x from pip)
- Tools.
  - box151/xwake.py, req.py, build.py, genk.py: copies of l-red 2f60fa74 experiments/red/r199/ (read-only sources, unchanged).
  - box151/xwake_anti.py: xwake.py plus two env switches. ANTI=1 adds the antisymmetry clause. FREEKP=1 makes the key orders R_l of
    the main levels free Booleans, constrained only by F1 (R_l constant at a step where no main mover of level ≤ l moves), and
    requires every main move to go to KP (R198 K1); the main level-0 KP is a free constant. Both switches only drop or add valid
    consequences of the IDEAL rule.
  - run.sh regenerates the table into stdout; runs.txt holds the run of this commit.
- Clause soundness (each holds on every degree-2 IDEAL-ACYC ladder run):
  - K: moves go to KP (R198 K1; P-IDEAL-RED §0).
  - RR: F3.
  - LAG: F2.
  - CBIT: the C-ELEMENT rule s_t = KP_t if KP_t = C_(t−1) else s_(t−1) (R199 §1, re-proved there from the R104 rule). C changes only
    when a reached mover moves (P-IDEAL-RED LOCAL (b)).
  - degree: each mover has ≤ 2 Ξ-out-edges (DEG=1), or reach is any strict partial order (DEG=0, weaker).
  - antisymmetry and F1 (FREEKP): P-IDEAL-RED.
- Table (genk swapmask 0; E = ladder levels above the stack; d = k + 1 + E). Exact R197 / R199 results are quoted from l-red R199 §3.
  | k | E | d | exact (R197 / R199) | xwake.py as committed | + ANTI, build.py gates | + ANTI, gate-free |
  | --- | --- | --- | --- | --- | --- | --- |
  | 2 | 0 | 3 | (UNSAT, ⊂ d 4) | | UNSAT | UNSAT |
  | 2 | 1 | 4 | UNSAT | | UNSAT | SAT |
  | 2 | 2 | 5 | SAT (nd2_d5_F12) | | SAT | SAT |
  | 3 | 0 | 4 | UNSAT | SAT | UNSAT | UNSAT |
  | 3 | 1 | 5 | UNSAT | SAT | UNSAT | UNSAT |
  | 3 | 2 | 6 | UNKNOWN | | SAT | SAT |
  | 4 | 0 | 5 | | | UNSAT | UNSAT |
  | 4 | 1 | 6 | | | UNSAT | UNSAT |
  | 4 | 2 | 7 | | | UNSAT | SAT |
  | 4 | 3 | 8 | | | SAT | |
  | 5 | 0 | 6 | | | UNSAT | UNSAT |
  | 5 | 1 | 7 | | | UNSAT | UNSAT |
  | 5 | 2 | 8 | | | UNSAT | UNSAT (205 s) |
  | 5 | 3 | 9 | | | running at the push | SAT (229 s) |
  | 6 | 2, 3 | 9, 10 | | | | running at the push |
- A further relaxation check (not in the table): without CBIT, ANTI at k 3, E 1 is SAT, so the C-ELEMENT clause is needed.
- Exact value-level increment propagation (cv(y) rises at t iff y moves or its current Ξ-target's cv rises; a C-flip toward b needs
  face b to rise) added to the gate-fixed relaxation at k 3, E 2: still SAT (141 s, scratch run). So the k = 3, E = 2 question is not
  settled by monotonicity bookkeeping either.
- Windows (gate-fixed, DEG=0, k 3, E 1): the shortest UNSAT windows are the 8 steps 2-9 and 10-17. Each starts right after a level-1
  prompt step (τ ≡ 1 mod 8), so the E = 1 obstruction involves levels 1-3, not only the top two.

## 3. Status
- PROVED (lane): NEST-BARE (every k ≥ 2, any gates), F2 LAG, F3 RE-REVERSAL (re-proved from the model).
- EXACT (z3, sound relaxation): NEST(k) needs ≥ ⌈k/2⌉ levels above, for any gates, k ≤ 5 (≥ 2, 2, 3, ≥ 3 with build.py's gates).
- FINDING: r199/xwake.py lacks antisymmetry. With it, R199's d ≤ 5 nested refutations are wake-order obstructions, and R199's
  «value semantics» reading is withdrawn as far as it rests on that tool (L-RED to confirm).
- OPEN: NEST-DEPTH, the Lead's DBL − ZERO candidate (needs f exponential and the value semantics), IDEAL-ACYC-POLY, G-N5-TIME.
- L-RED target (Lead decides): realise exactly k = 3 at E = 2 (d 6) or k = 4 at E = 2 (d 7, gate-free), starting from
  box151/hints/wo_free_k3_E2.json, wo_gates_k3_E2.json, wo_free_k4_E2.json (aux schedules, reach order, main key orders).
