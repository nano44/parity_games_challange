# R224 item 7: adversary on L-NEW 64's box 196 «CLOSE THE Γ3 CHAIN» (L-RED successor 58, Opus 5.5, D1 / D18 / D14; 2026-11-08, date -u)
Target: claude/l-new f725af5a + Addendum 1 08801298, docs/new/N5-CHAIN-box196.md (read at 08801298), experiments/new/box196/.
Lead (07:49Z) priorities, in order:
- (1) the hand-read Ξ-token steps of ESC3 / W3;
- (2) QUIET3's window bound and the n3 substitution on Γ3 (my item-7 pre-check, with L3 as stated);
- (3) whether CHAIN3's formula follows exactly (+3);
- (4) build controls for the five counters that have none (nonstd, cnlow, k2fail, crossflip, emon).
Labels: SURVIVES / BROKEN; DATA with counters (unit, set, scope).

## 0. Verdict
| statement | verdict | basis |
| --- | --- | --- |
| ESC3-ALL, W3-ALL, Theorem REACH3-ALL (§2) | SURVIVE | proofs re-derived (§1); R223-reach.md DATA: 50,816 Ξ-cyclic genomes, all counters 0, control fires |
| CN2-3, LOC-GATE3, LOC-K2-3, B-ONLY3, NO-TIE3, QUIET3, T-QUIET3 (§3) | SURVIVE | proofs read (§2); window and T3 bounds measured directly on Γ3 runs by my own code and by box 196's (§3) |
| E-MON3, CHAIN-DECOMP3, HUB-ASC-G3, UP-JUMP3, UP-B3 (§4) | SURVIVE (read, not re-derived line by line) | §2 |
| Theorem CHAIN3 (§5): ≤ (1 + n3((2M + 3)F′_U(G)(M) − 1))(L3 + 1) + 3 | SURVIVES: follows exactly from §2-§4 + ENDGAME-3 | §4 |
| DEAD RUN-TRANSFER (§6) | AGREE (my R221 §7 found the same divergence, 11 of 2,150) | — |
| the five uncontrolled counters | controls BUILT; all five fire (§5) | — |
No break. Premise status as box 196 states it: P-N5-END, P-N5-ASC (R121) and P-N5-QUIET are not landed, and [E-LEV] (C10) is a
hypothesis. CHAIN3 is a lane result on those premises.

## 1. Priority (1): the Ξ-token steps of ESC3 / W3, by hand
- ESC3.3 «β_g with xt(g) a mover: its options in H are within {xt(g), pb_g}». This names β_g's two successors ([DEF] edges). No
  property of the Ξ-graph is used. OK.
- ESC3.4: an H-play from xt(g) is mover → m → gate → pe (τ in H) → e → W-target (one level lower) → …; it never leaves a gate by pβ, so it
  never meets a β-vertex. Its length is bounded by the level and it ends at c_W. «β_g on no H-cycle» uses only in-edges (pβ_g → β_g,
  gate → pβ_g, and the gate plays pe in H). An H-play from pb_g enters K0 and stays in the core (K3 (d), every genome). OK.
- W3.5 «W(β_g) = (c_W, ∅, 5·lev(xt(g)) + 6)»: one β → xt step, then the (σ, τ)-play of a mover, which takes pe at every gate. Only the
  level of xt(g) matters, and no cycle can form, because levels then strictly decrease. OK.
- ESC3.2, W3.2: scope labels only. OK.
- REACH3-ALL's induction: at a mover with |A(x)| = 1, σ_new(x) = σ(x) is forced; at |A(x)| ≥ 2, TIE(x) = A(x) (W3-ALL (iii)), so
  N5′-xi's Ξσ-best element of A(x) is a best successor overall. A strictly better successor lies in Iσ(x) ⊆ A(x), so it is a Howard
  step, and S4c cannot fire while some mover improves. At T3, ESC3-ALL keeps the non-movers, TAU3 keeps τ, and (K0, K1) ∈ Iσ, so S4c
  fires. OK.
- DATA: docs/red/R223-reach.md (l-red 71133de5). Own Γ3 builder, n5v mode xi, checks by own.py. Counters nstd / esc / w3 / how / fbx
  are 0 on 43,816 exhaustive N ≤ 2 Ξ-cyclic genomes and 7,000 random cyclic ones (N 3-6). The control MODE=spec fires (how 143, fbx 296
  of 500), the same phenomenon as box 196's «nohoward» in spec mode.

## 2. §3-§4 read
- CN2-3 follows from PAD (a): every cycle except c_X's loop has a vertex of Ω ≥ 3, and c_X has no in-edge but its loop.
- LOC-K2-3 is re-derived: the frozen K1 → s → K1, and r gives node K1 against the loop's K2, so σ̄(K2) = r with Ω(K2) = (K1, ∅, 2).
- B-ONLY3: τ_β avoids every pe, so it meets no e-vertex except at its start and never meets c_W. The exclusion of pe_g for level-0 e's is
  needed and present.
- NO-TIE3: equality would need pβ_g's play to pass g, pe_g and e_g, which makes its length larger. OK.
- QUIET3 (Q1)-(Q6): the substitutions are the ones my R223-q2.md §4 (2) list predicted (pads never cycle nodes or in Π; one pad per
  face; n → n3 in (Q3) and (Q6)). L3 = (M + 1)(2M + 1)(N + 1) + N(n3 − 1) is consistent with (Q6) for n3 = N + 7M + 10.
- Code check: qt3_196.py computes L3 with n = g.n, the vertex count of the padded game, which is n3.
- HUB-ASC-G3's «2M + 3 possible cycle nodes» (M e's, M β's, c_W, K1, K2): c_X is a cycle node only for c_X itself (D = 1), and pads,
  movers, gates, K0, K3 never are. OK.

## 3. Priority (2): QUIET3 / T-QUIET3 measured directly on Γ3 (my code: experiments/red/r223/quiet3.py)
Unit: genome = an N5′-xi run (n5v mode xi @ l-new 131b4c1c on own3's Γ3, from S3, up to the first fallback). Values by own.py.
class_t(v) = (Λ, E) over ALL n3 vertices. Counters:
- wov: some quiet window > L3;
- tq: T3 > Q3 + (Q3 + 1)·L3.
| set | genomes | wov | tq | max quiet window | max T3 | max Q3 | max U(G) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [E-LEV] (own3 orders e's by (level, gate)), U(G) ≤ 2, cyclic, N 4-8, seed 2250 | 2,000 | 0 | 0 | 3 | 6 | 6 | 2 |
| random cyclic N 3-4, seed 2251 | 3,000 | 0 | 0 | 3 | 5 | 5 | 5 |
| random cyclic N 5-6, seed 2252 | 1,000 | 0 | 0 | 2 | 8 | 7 | 7 |
(out/quiet3.txt. The exhaustive N ≤ 2 set and the ladders were not run with my own-code valuation: own.py is too slow on the 800-vertex
ladders. Their Γ3 numbers below come from box 196's engine.)
- On L-SI's long box-85 ladders (Ξ-cyclic: SET self-loops), box 196's own engine gives the clean-run T3, Q and W as by-products of the
  control runs (§5, out/ctrl224.txt). For example TC4m: T3 37, Q 18, longest quiet window 5; CL2_21: T3 23, Q 10, W 8. L3 is in the
  hundreds of thousands there. So no window comes near L3.
- Weakness, stated: every measured run is short (T3 ≤ 43). L3 is a loose bound, and these data cannot test its tightness, only that
  nothing exceeds it.

## 4. Priority (3): does CHAIN3's formula follow exactly?
- REACH3-ALL: the run up to its first fallback is a HOW3 run of length T3, and the first fallback is iteration T3 + 1.
- ENDGAME-3: total = F + 2 = T3 + 3.
- T-QUIET3: T3 ≤ (1 + Σ_v (D^tot_E(v) − 1))(L3 + 1), the sum over the n3 vertices.
- HUB-ASC-G3 with UP-B3: D^tot_E(v) ≤ (2M + 3)F′_(U(G))(M) for every v. So 1 + Σ_v (D^tot_E(v) − 1) ≤ 1 + n3((2M + 3)F′_(U(G))(M) − 1).
- Exactly CHAIN3's formula, with +3 = (T3 + 1) + 2 − T3. OK.
- Two remarks:
  - The bound uses UP-B3 for EVERY vertex of Γ3, pads and K-vertices included. For those, seq_t(v) is the e-sequence of v's play, which
    UP-JUMP3 covers (it is a statement about plays, not about movers).
  - The degree claim «O(5·2^B) in M» rests on P-N5-ASC's F′. I did not re-check that.

## 5. Priority (4): controls for nonstd, cnlow, k2fail, crossflip, emon (experiments/red/r224/ctrl224.py)
Method: FAULT INJECTION into box 196's own counter code, run unchanged.
- qt3_196.py's check() is imported from a worktree of 08801298.
- Injection touches only the evaluate() calls made from check() itself, i.e. the counters' view. The algorithm (n5v.step, its arena
  engines, idealcyc) is unchanged. The exception is FAULT=nonstd, which perturbs the state the run continues from.
- Faults:
  - nonstd: after step 1, one β with a mover Ξ-target is set to its pb pad;
  - cnlow: pad pA is added to vertex 0's Π;
  - k2fail: σ̄(K2) := K2;
  - crossflip: σ̄ is toggled at every gate on every second evaluation;
  - emon: at the 2nd evaluation, the most relevant e is removed from every Π that holds an e.
- A control passes when the counter is 0 on the clean run and > 0 on the injected run.
- Set: L-SI's 11 frozen box-85 genomes (inst_si85/, sha1 = L-SI pins) + 4 corpus genomes (A_d4_W2_k2, REC_d7_mu17_norm,
  KILL_M2D_d6_mu13_norm, A_d5_W2_k3). Output: out/ctrl224.txt.
| genome | T3 | Q | longest quiet window | nonstd | cnlow | k2fail | crossflip | emon (clean → injected) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CL2_21 | 23 | 10 | 8 | 0 → 1 | 0 → 24 | 0 → 24 | 0 → 2645 | 0 → 131 |
| CL2_22 | 28 | 9 | 8 | 0 → 1 | 0 → 29 | 0 → 29 | 0 → 5716 | 0 → 181 |
| CL3_31 | 15 | 10 | 2 | 0 → 1 | 0 → 16 | 0 → 16 | 0 → 941 | 0 → 148 |
| CL3_32 | 24 | 11 | 7 | 0 → 1 | 0 → 25 | 0 → 25 | 0 → 4092 | 0 → 214 |
| TC2 | 12 | 8 | 1 | 0 → 1 | 0 → 13 | 0 → 13 | 0 → 434 | 0 → 81 |
| TC2d | 10 | 6 | 1 | 0 → 1 | 0 → 11 | 0 → 11 | 0 → 440 | 0 → 83 |
| TC3 | 18 | 13 | 2 | 0 → 1 | 0 → 19 | 0 → 19 | 0 → 1062 | 0 → 154 |
| TC3d | 14 | 9 | 2 | 0 → 1 | 0 → 15 | 0 → 15 | 0 → 1079 | 0 → 158 |
| TC3m | 17 | 12 | 2 | 0 → 1 | 0 → 18 | 0 → 18 | 0 → 1060 | 0 → 154 |
| TC4m | 37 | 18 | 5 | 0 → 1 | 0 → 38 | 0 → 38 | 0 → 9135 | 0 → 311 |
| TC5m | 43 | 21 | 9 | 0 → 1 | 0 → 44 | 0 → 44 | 0 → 17333 | 0 → 486 |
| A_d4_W2_k2 | 5 | 0 | 5 | 0 → 1 | 0 → 6 | 0 → 6 | 0 → 80 | 0 → 24 |
| REC_d7_mu17_norm | 8 | 0 | 8 | 0 → 8 | 0 → 9 | 0 → 9 | 0 → 224 | 0 → 48 |
| KILL_M2D_d6_mu13_norm | 7 | 0 | 7 | 0 → 1 | 0 → 8 | 0 → 8 | 0 → 168 | 0 → 40 |
| A_d5_W2_k3 | 3 | 0 | 3 | 0 → 2 | 0 → 4 | 0 → 4 | 0 → 90 | 0 → 48 |
- All 75 (genome, counter) controls pass: clean 0, injected > 0.
- Reading: each counter detects its condition. The controls are artificial, since they edit values rather than build a genome that
  breaks the lemma: no such genome exists if the lemmas hold. That is the most a control for a PROVED invariant can show.

## 6. Tools and sources
- experiments/red/r224/ctrl224.py (env W196 = worktree of l-new 08801298); experiments/red/r223/quiet3.py, reach223.py, own3.py (env WT =
  WT3 = worktree of l-new 131b4c1c); outputs experiments/red/r224/out/ctrl224.txt, experiments/red/r223/out/quiet3.txt.
- Sources opened: claude/l-new 08801298 docs/new/N5-CHAIN-box196.md §0-§6 (l. 1-205), experiments/new/box196/qt3_196.py (counters, l.
  1-115); P-N5-QUIET §4; P-N5-REACH §3, §6; my R221-quiet.md §7, R223-q2.md §4, R223-reach.md.
Not a TARGET.md claim; not M3 or M4; G-N5-TIME stays OPEN.
