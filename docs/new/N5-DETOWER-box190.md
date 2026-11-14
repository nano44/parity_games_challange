# Box 190 DE-TOWER: which N5 rule makes towers possible, and can a one-rule variant N5′ prevent them? (L-NEW successor 58, Opus 5.5)
Written 2026-11-07 from 03:05Z (date -u at commit). Lead brief 03:03Z (BOX 190, D14, 12 h). D1 applies in full: every N5′ below is a
CANDIDATE, wrong until it passes the TARGET.md §5 gauntlet. Labels: PROVED (lane, unrefereed) / CONJECTURE / DEAD / DATA / READING.
Premises: R104's definitions (IDEAL model, Γ(G)); P-N5-REACH (docs/new/P-N5-REACH.md, frozen 73b3d1fd, at both referees, NOT landed:
used only for the DATA realisation on Γ3 and for the REACH3-XI sketch, which inherits its status); RESULTS R105 (ENC) for the integer
form of Ξ-values; RESULTS R15 (d) for termination.

## 0. Answer
- The ingredient that makes towers possible is the ROOT-FIRST KEY tie-break of S4a's arena ties (SPEC S4a + [RULE] = RESULTS R24 (b)
  TB, as realised by R104 Lemma KEY). It makes a mover's choice depend on the CURRENT states of other movers (its W-chain below), so a
  mover can move back and forth as lower keys flip (PAIR-DOUBLE, the metronome). The availability rule (strictly better Ξ) only supplies
  the fuel. Simultaneous moves are not the cause: SEQ (one Even vertex per step) is longer, not shorter (DATA §3).
- Two one-rule variants that replace the key tie-break bound the IDEAL model polynomially (PROVED, lane):
  IDEAL-XI (a mover takes its Ξ-best available option): T ≤ H(G), the Ξ-height (≤ N);
  IDEAL-IDX (a mover takes the available option of largest gate index): T ≤ M − N.
- Their real versions N5′-xi / N5′-idx break S4a's W-ties by Ξσ / by largest index. On Γ3(G) from S3 they realise IDEAL-XI / IDEAL-IDX
  (DATA: iterations = T + 3 on all 14 corpus genomes; proof sketch §2.3). So the R104 / P-N5-REACH lower-bound route gives them at most
  H + O(1), resp. M − N + O(1) iterations: the tower mechanism is DEAD for them.
- Step 4 (positive route): for N5′-xi the IDEAL analogue is polynomial with a three-line proof. FUEL-RECURSION is not needed there.
  READING: this removes the fleet's known lower-bound route for N5′-xi. It does NOT bound N5′-xi on general games (the REALIZE direction
  is one-way: IDEAL lower bounds ⇒ real lower bounds, never the converse). G-N5-TIME and any N5′ time bound stay OPEN.
- CANDIDATE N5′-xi, gauntlet step 2 (partial): 10,000 random games (n ≤ 40): 0 wrong (regions vs harness Zielonka, positional strategies
  by harness verify.check). On every hard family run: correct, and counts equal to N5's on every family except tc (14 of 15 families; on tc they differ by a few iterations either way; §3).

## 1. Step 1: the SPEC rule behind each tower ingredient (READING with the proof pointers)
| ingredient | IDEAL rule (R104) | SPEC rule realising it (P-N5-REALIZE / P-N5-REACH lemma) |
| --- | --- | --- |
| availability / fuel: a mover may move only to a strictly Ξ-better option; fuel targets' Ξ-values rise | A_s(x) = current ∪ strictly Ξ-better | S2 + S4a's arena H keeps {σ(v)} ∪ Iσ(v) (KEY (a): Iσ at movers = Ξ-better options) |
| PAIR-DOUBLE / metronome: a mover follows every key flip below it | s'(x) = least ROOT-FIRST KEY in A_s(x), keys built from the NEW states of lower levels | S4a's pointwise optimum: all mover options tie in H (W (iii)), and [RULE] (R24 (b) TB) breaks the tie by the root-first key κ (KEY (b)) |
| staggering of a pair | all movers move in the same step | S4: «both steps computed from the SAME (σ, τ), applied together»; S4a sets all Even vertices at once |
- The only rule in the table whose output depends on OTHER movers' current states, without being an availability condition, is the
  key. Under any tie rule that depends only on x's own available set (IDX), or only on Ξ-values (XI), a mover's moves are bounded
  (§2). That is the precise sense of «the key makes towers possible» (PROVED for these two rules; not a statement about all rules).

## 2. The variants and what is proved
### 2.1 Definitions (each changes ONE rule of S4a; S1-S3, S4b, S4c, S5 unchanged; experiments/new/box190/n5v.py)
- N5′-xi: after S4a, at every Even v with |A(v)| ≥ 2 that is not its own H-cycle node, σ_new(v) := the Ξσ-best element of TIE(v) :=
  {w ∈ A(v) : W*(v) = v ⊕ W*(w)} (W* = the values of S4a's arena optimum; ties by SPEC's choice, then by the larger index).
- N5′-idx: the same, with the largest vertex index of TIE(v) instead of the Ξσ-best.
- N5′-seq: SPEC's σ_new applied at the least-index Even vertex where it differs from σ, everywhere else σ_new := σ.
- Correctness and termination (PROVED, lane, from SPEC + R15): every variant keeps σ_new(v) ∈ A(v) = {σ(v)} ∪ Iσ(v). So a non-fallback
  iteration applies a set I ⊆ Iσ of improving switches to σ, non-empty unless only τ changes; S4c is unchanged. R15 (d)'s argument («every
  iteration applies Switch_I with ∅ ≠ I ⊆ Iσ … and/or … Iτ») therefore applies verbatim: no state repeats and the run terminates. At the
  stop Iσ = Iτ = ∅, and SPEC S5's output argument (classical SI; RESULTS R57 OUT-G) does not depend on how the run got there. N5′'s
  output is correct whenever N5's is (same stop condition, same S5). (Whether σ_new is still a pointwise optimum of H does not matter
  for correctness.)

### 2.2 IDEAL analogues (PROVED, lane; G ∈ IDEAL-ACYC, any degree and width)
- IDEAL-XI: s'(x) := the Ξ-best option in A_s(x) (= x's Ξ-best option overall, since A_s(x) contains every strictly better one).
  Height h(x) := 1 + max h over the movers among x's Ξ-targets (1 if all are X); H := max h. Claim: T ≤ H. Proof: the Ξ-values of x's
  options depend only on the states of movers of smaller height (the X-chain of (x, k) passes only Ξ-descendants of x). By induction on
  t, after step t every mover of height ≤ t sits at its Ξ-best option (unique by Fact X) and never moves again: at step t the values of a
  height-t mover's options are already fixed, so it takes the best, after which A = {current}. So no mover moves after step H. ∎
- IDEAL-IDX: s'(x) := the option of largest gate index in A_s(x). Claim: T ≤ M − N. Proof: A_s(x) ∋ s(x), so a moving mover's gate index
  strictly increases; x moves at most deg(x) − 1 times; each step moves a mover. ∎ (Degree 2: each mover moves at most once.)
- Contrast (R113 / L-LOWER, landed + candidate): under R104's key rule, a mover can move ~F(l−1) + 1 times per doubling level
  (PAIR-DOUBLE), and REC_d10_tower has T = 35, RECT_d11_T59 has T = 59 (corpus §3).

### 2.3 Realisation on Γ3 (REACH3-XI / REACH3-IDX: PROVED (lane) as a sketch on P-N5-REACH's lemmas, so with that packet's status)
On Γ3(G) from S3, N5′-xi (resp. idx) runs the IDEAL-XI (resp. IDX) trajectory state for state, then a fallback. Proof sketch: REACH3's
induction, with [RULE]'s step at the movers replaced by the variant's tie rule. In the standard state TIE(x) = R(x) (P-N5-REACH W3 (iii))
and R(x) = the pads of A_s(x) (KEY3 (a)). Ξσ on these pads is the IDEAL Ξ order (KEY3 (a)), and the pad indices follow gate indices
(§3 of the packet). Every non-mover Even vertex with two arena options has a unique W*-optimal one (ESC3: β → xt; K3 (d): K0 → pA), so
its TIE is a singleton and the variant agrees with SPEC there. S4b and S4c are unchanged (TAU3; the fallback at the stop).
DATA: N5′ iterations on Γ3 = IDEAL T + 3 for xi and idx on all 14 corpus genomes (§3 table).

## 3. DATA (experiments/new/box190/; engine n5v.py on box21 n5x; IDEAL sims idealv.py)
- Corpus C14 = experiments/new/box189/corpus (P-N5-REACH §10), Γ3 from S3, iterations [IDEAL T]:
| genome | d | Ξ-height H | L (spec) | N5 spec | N5′-xi [T_XI] | N5′-idx [T_IDX] | N5′-seq [IDEAL-SEQ T] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A_d4_W2_k2 | 4 | 6 | 9 | 12 | 8 [5] | 5 [2] | 31 [11] |
| A_d4_W3_k3 | 4 | 9 | 15 | 18 | 8 [5] | 4 [1] | 67 [29] |
| A_d5_W2_k3 | 5 | 6 | 13 | 16 | 6 [3] | 5 [2] | 52 [20] |
| A_d6_W2_k2 | 6 | 8 | 11 | 14 | 6 [3] | 5 [2] | 36 [12] |
| KILL_M2D_d6_mu13 | 6 | 10 | 13 | 16 | 10 [7] | 5 [2] | 34 [5] |
| KILL_M2D_d8_mu21 | 8 | 8 | 24 | 27 | 8 [5] | 4 [1] | 55 [12] |
| RECT_d11_T59 | 11 | 17 | 59 | 62 | 8 [5] | 5 [2] | 13 [7] |
| REC_d10_mu32 | 10 | 12 | 33 | 36 | 10 [7] | 4 [1] | 18 [7] |
| REC_d10_tower_mu30 | 10 | 13 | 35 | 38 | 6 [3] | 5 [2] | 66 [16] |
| REC_d11_mu40 | 11 | 16 | 44 | 47 | 8 [5] | 5 [2] | 77 [19] |
| REC_d12_mu42 | 12 | 14 | 48 | 51 | 7 [4] | 5 [2] | 55 [16] |
| REC_d7_mu17 | 7 | 12 | 17 | 20 | 11 [8] | 4 [1] | 10 [3] |
| REC_d8_mu24 | 8 | 12 | 25 | 28 | 12 [9] | 6 [3] | 9 [2] |
| REC_d9_mu29 | 9 | 11 | 31 | 34 | 9 [6] | 5 [2] | 65 [7] |
  spec = L + 3, xi = T_XI + 3, idx = T_IDX + 3 on 14/14 (unit: genomes). seq ≠ IDEAL-SEQ + 3 on 14/14: N5′-seq does NOT realise the
  IDEAL-SEQ rule (it changes one Even vertex of the whole game per step, and S4c / later arenas differ). T_XI ≤ H on 14/14.
- Climbs (idealv.py climb, 2-wide degree-2 ladders, 4 seeds × 3,000 mutations, d 3-7): max T spec 6, 7, 8, 9, 10; idx 5, 7, 7, 9, 9;
  xi 6, 8, 10, 11, 12 (xi ≤ H ≤ 2d as proved). This climber is WEAK (L-LOWER reaches 17 at d 7 under spec), so these numbers say nothing
  about spec's growth; they are recorded only as a sanity check of the two bounds.
- Gauntlet step 2 (partial; N5′-xi and N5 = spec): gauntlet190.py random 10000 40: «RANDOM games 10000 n 1..40: spec: wrong 0, max
  iterations 13; xi: wrong 0, max iterations 13» (wrong = regions ≠ harness Zielonka or verify.check error; unit = games).
- Families (all four variants correct = regions = Zielonka and strategies verified, every N run):
  - PGSolver port (pgsolver_port.py), N = 1..7: switchbestexp spec = xi = 20, 32, 41, 47, 55, 62, 68; switchallexp 5, 8, 7, 8, 10,
    12, 14 (equal); friedmannsubexp 4, 10, 15, 19, 23, 27, 31 (equal); fearnleysubexp 4, 8, 12, 14, 16, 18, 21 (equal); recursiveladder
    0, 2, 2, 4, 4, 6, 6 (equal).
  - Oink tc, N = 1..12: spec 1 4 7 16 19 18 23 30 32 27 33 37; xi 1 4 7 17 16 20 20 34 24 35 30 34; idx 1 4 7 16 18 22 25 28 27 25 31
    37; seq 1 5 9 25 48 66 92 182 159 331 354 499.
  - Oink tc+, N = 1..9: spec 0 3 7 11 16 26 24 30 33; xi equal to spec; idx 0 3 7 11 17 24 46 49 58; seq 0 3 9 32 65 112 177 267 379.
  - Oink counter_m, counter_symsi, counter_rr, counter_dp, counter_core, counter_qpt, counter_ortl, counter_rob, N = 1..10 (spec, xi,
    idx; out/fam_counter_*.txt): 80/80 runs correct; xi = idx = spec on 80/80 (e.g. counter_symsi N 10: 55; counter_rob N 10, n 383: 28).
- DEAD (as a de-tower fix; DATA, no exponential proof): N5′-seq. It is longer than N5 on 10/14 corpus genomes (shorter on RECT_d11, REC_d10_mu32, REC_d7, REC_d8) and grows fastest on tc
  (499 at N 12 vs 37) and tc+ (379 at N 9 vs 33).

## 4. What this does NOT show, and next steps (READING)
- Neither N5′-xi nor N5′-idx is shown polynomial on any class beyond the IDEAL images Γ3(G). Their real dynamics on other games are N5's
  wherever W-ties do not occur (families: spec = xi on every family run except tc: 5 PGSolver, tc+, 8 counter_*).
- Natural attack on N5′-xi (for L-RED): a gadget where the Ξ-best tie rule is itself steered. Examples: Ξ-cyclic genomes (outside
  REALIZE's scope), or W-faces that are not all tied, so that S4a's arena optimum, not the tie rule, decides.
- Gauntlet status of N5′-xi: step 1 (pseudocode: §2.1 + n5v.py), step 2 partial (random 10,000 done; families above; second independent
  implementation not done); steps 3-5 not started. Not a TARGET.md claim; G-N5-TIME OPEN.
