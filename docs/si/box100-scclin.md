# Box 100: SCC-LIN inside one SCC: gates re-flip only through value changes (TWO-CROSS), Π-changes are counted by depth (DEPTH-COUNT3), and the run splits into fixed-Λ one-player windows (WINDOW); SCC-LIN ⇐ LAM-GAP ∧ DEEP3
L-SI successor 51 (Opus 5.5), D18 / D14 / D1; Lead 08:01Z («BOX 100 (SCC-LIN) … trace the internal gates on MWR16_2's giant SCC (152
movers) before naming a mechanism»). Labels: PROVED (L-SI lane, unrefereed) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD /
READING. Not a TARGET.md claim; not M3 or M4; not a gauntlet step; G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1). Box 99's H(C) is
read with Addendum A (G1 fixed: maximum over all HOW3-legal tie resolutions). Tools: experiments/si/box100/ (trace100.py, iv100.py,
cross100.py, l1probe100.py; run100.sh, run100b.sh, check100.sh); engine L-RED 65's own HOW3 (claude/l-red 59daaef2, how3_232.py, read-only).

## 0. Answer
- SCC-LIN is NOT proved. The trace (§1) shows what is left inside one SCC C once ONE-CROSS3 has made the exit gates one-shot. Three things
  are proved (lane):
  - Lemma TWO-CROSS (§2): every flip of a gate away from a face coincides with a change of that face's value. So a gate flips at most
    ch(pe) + ch(pβ) times, and at most 2·min(ch(pe), ch(pβ)) + 1 times. ONE-CROSS3 (L-RED 65) is the case min = 0.
  - Lemma DEPTH-COUNT3 (§3): L-NEW 70's DEPTH-COUNT (box 206, IDEAL-CYC) transfers to Γ3 / HOW3 and to the full VJ value (Λ, Π, len). For
    every vertex v and every c ≥ 0, Ω(v) changes Λ at most n3 − 1 times, and makes at most n3·(S_c(n3) − 1) changes of depth ≤ c.
  - Theorem WINDOW (§4): after t0(C), the run inside C splits into windows. In each window Odd's choices at C's gates and every Λ at C's
    movers stay constant, and each window is a Howard run of one fixed one-player game. With TWO-CROSS and DEPTH-COUNT3:
    H-run(C) ≤ (1 + E_C + N_C(n3 − 1) + 2·I_C·n3·S_c(n3) + Deep_c(C)) · (Gap(C) + 1) for every c ≥ 0.
- So, for every family, SCC-LIN in its polynomial form (H(C) ≤ poly) follows from two named conjectures:
  - CONJECTURE LAM-GAP: in a one-player game G_C[φ], a Howard window with every Λ constant has at most N_C + 1 iterations.
  - CONJECTURE DEEP3: for some fixed c, the internal-gate flips charged to a change of depth > c are polynomially many.
  Each is DATA-supported (§5) and unproved. The exact form H(C) ≤ M_C does not follow from this route; the bound is polynomial, not linear.
- DEAD (§5.3): FLIP-LOUD («every gate flip is charged to a Λ change»), killed by MWR4_2 (sha1 856d369b): all 9 flips of gate (34, 0) are
  Λ-quiet.
- Mechanism of the giant SCC of MWR (READING, from the trace, §1): a FUSE plus ONE re-arm gate.
  - The fuse: the chain movers each switch once, one per iteration, with no gate flip.
  - The fuse is cut every few steps by the one-shot exit gates (30-33, 0).
  - The hub 44 re-arms through the single internal gate (34, 0). Its two faces keep Λ = K1 throughout, while the top e-vertex of Π
    climbs one rung per round (e(30,0) → e(31,0) → e(32,0) → e(33,0)), at depth ≤ 3.
  - For lead (b): the giant SCC of MWR has a feedback vertex set of size 1 (k = 1) and exactly 2 internal gates.

## 1. Trace (DATA; trace100.py, iv100.py; unit: state / gate / SCC; scope: largest SCC C of D(G), HOW3 run of L-RED's engine)
- MWR4_2 (sha1 856d369b, out/trace_MWR4_2.out): T3 30, C = 44 of 48 movers, M_C 91. 89 of C's 91 gates are ext (a target outside C or
  −1), 2 are internal. Mover 44 (the hub) switches 9 times with degree 5 (0>4, 4>0, 0>4, 4>1, 1>4, 4>2, 2>4, 4>3, 3>4). Mover 43 switches
  4 times. Every other mover switches once: 29, 28, …, 2 in successive iterations (the fuse). States 2-8 have no gate flip at all. Gate
  (34, 0) flips 9 times (e, b alternating), and the ext gates (30..33, 0) flip once each, at t = 9, 15, 21, 27.
- MWR(n), n = 4 / 8 / 16 (iv100.out): T3 30 / 54 / 102 = 6n + 6. Internal-gate flips Φ_int 9 / 17 / 33 = 2n + 1, all at the one gate.
  Ext flips Φ_ext 4 / 8 / 16 = n. Intervals of constant σ̄|C: 14 / 26 / 50 = 3n + 2, max length 8 at every n. Greedy feedback vertex set
  of D(G)[C]: 1.
- Other giant SCCs (C6G8_n54, RWX_n95, DWT20_2803, DHIB18_2805, DHIB26_2804): 50 / 91 / 96 / 117 / 114 internal gates (C98 climbs: 3-37). Greedy fvs ≤ 16 / 20 /
  20 / 30 / 24 (an upper bound on k), so these are not k = 1. Intervals have mean length 1.04-1.08, max 2. Movers switch far more often
  than their degree (DHIB26: mover 17, 21 switches), so a per-mover count cannot bound H(C).
- Gate (34, 0)'s face values in MWR4_2 (§5.3 lists them): both faces have Λ = K1 (priority 5, odd) at every state. Their Π sets share
  the constant core (K3, K0) and differ below it. Each round, the face Odd leaves gains a more relevant e-vertex than before (depth 2 or 3).

## 2. Lemma TWO-CROSS (PROVED, lane; generalizes ONE-CROSS3, L-RED 65 claude/l-red 59daaef2 R232 §0)
Premises (trunk docs/RESULTS.md, R125 line, quoted by grep at trunk 7f7ee70e1):
- (d) «Facts F1, F3, F4′, F5, F6, DOM, STRICT on HOW3(G) (§4 l. 149-) [every genome]: F1 by R15 (a)».
- (f) Lemma LOC-GATE3: «Let t be a state, g a gate, a := σ̄_t(g) ∈ {pe_g, pβ_g}, b the other face, Ω := Ω_t. If Ω(a) ≠ Ω(b), then Ω(a) ◁ Ω(b).»
- (i) Corollary NO-TIE3: «At every state and gate g, Ω_t(pe_g) ≠ Ω_t(pβ_g).»

Statement. On a run of HOW3(G) (any legal tie resolution), let g be a gate with faces pe, pβ, and let ch(f) := #{t : Ω_t(f) ≠ Ω_(t+1)(f)}.
(i) If σ̄_t(g) = a and σ̄_(t+1)(g) = b ≠ a, then Ω_t(a) ◁ Ω_(t+1)(a).
(ii) Hence flips(g) ≤ ch(pe) + ch(pβ), and flips(g) ≤ 2·min(ch(pe), ch(pβ)) + 1.

Proof.
- (i) By NO-TIE3 and LOC-GATE3: Ω_t(a) ◁ Ω_t(b) and Ω_(t+1)(b) ◁ Ω_(t+1)(a). By F1, Ω_t(b) ⊴ Ω_(t+1)(b). So
  Ω_t(a) ◁ Ω_t(b) ⊴ Ω_(t+1)(b) ◁ Ω_(t+1)(a).
- (ii) By (i), each flip away from face f is charged to a change of Ω(f) at the same step. Distinct flips have distinct steps, so the
  charges are injective: flips(g) ≤ ch(pe) + ch(pβ). Flips alternate between «away from pe» and «away from pβ», so with m := min(ch),
  there are at most m flips away from the face with fewer changes, and at most m + 1 away from the other: 2m + 1. ∎
- ONE-CROSS3 is the case ch = 0 for one face. DATA (cross100; must-0: unm = flips not charged, sumf, minf, tie):
  - 0 on the 26 frozen instances (4,706 gates) and on 400 random genomes (rand191.rgen seed 10001, 5,343 gates).
  - Control CTRL=1 (charge to the face Odd moves TO) fires: unm 102 on 3 instances (out/cross100_ctrl.out).
  - Tight cases (flips = 2·min + 1 ≥ 3): the MWR re-arm gate at n = 4, 8, 16.

## 3. Lemma DEPTH-COUNT3 (PROVED, lane; L-NEW 70's DEPTH-COUNT, claude/l-new docs/new/N5-DEPTH-box206.md §1, transferred to Γ3 / HOW3)
Setting. VJ values Ω = (Λ, Π, len) (Λ a vertex, Π the set of vertices more relevant than Λ on the path to Λ, len its length). The order:
- different Λ: by reward of Λ;
- else by Π: the most relevant element z of Π_a Δ Π_b decides, and Ω_a ◁ Ω_b iff (z ∈ Π_b) = (z even);
- else by len.
(VJ00 §4.2; the same order L-RED's own.py implements in VJ.cmp.)

Depth of a change Ω_t(v) ≠ Ω_(t+1)(v):
- −1 if Λ changes;
- else the number of elements of Π_t (equivalently of Π_(t+1)) more relevant than z, the most relevant element of Π_t Δ Π_(t+1);
- |Π_t| if Π_t = Π_(t+1) (a length-only change).
S_c(n) := Σ_(j=0..c+1) C(n, j). n3 := |Γ3(G)| = N + 7M + 10 (R125).

Statement. On any HOW3 run, for every vertex v and c ≥ 0: Λ(v) changes at most n3 − 1 times, and Ω(v) makes at most n3·(S_c(n3) − 1)
changes of depth in [0, c].

Proof.
- By F1, Ω_t(v) is ⊴-non-decreasing. A change of Λ strictly raises the reward of Λ, so Λ never returns to an earlier vertex: at most
  n3 values, at most n3 − 1 changes, and at most n3 maximal Λ-intervals.
- Order finite vertex sets by X ≺ Y iff (z ∈ Y) = (z even) for z the most relevant element of X Δ Y. This is a strict total order (the
  Π-part of the VJ order).
- On a Λ-interval, let P_t := the c + 1 most relevant elements of Π_t. Take consecutive states a, b with a change of depth d.
  - d ≤ c: the d elements above z are common, and z lies in exactly one of Π_a, Π_b, call it Π_s. Then z is among the d + 1 ≤ c + 1 most
    relevant elements of Π_s, so z ∈ P_s. The elements of P_a and of P_b above z are the same d elements, so z is the most relevant
    element of P_a Δ P_b, on the same side as in Π. Hence P_a ≺ P_b, because Π_a ◁ Π_b at fixed Λ.
  - d > c (including length-only changes): the c + 1 most relevant elements of both sets are common, so P_a = P_b.
- So on a Λ-interval P never falls and strictly rises at every change of depth ≤ c. Its values are sets of size ≤ c + 1 of the n3
  vertices, which gives at most S_c(n3) − 1 such changes per Λ-interval. ∎
- Difference from box 206: there E-MON makes the e-set grow; here the VJ order on Π does the same job for any set and either parity.

## 4. Theorem WINDOW (PROVED, lane, given the definitions; the two factors it leaves are §5's conjectures)
Definitions, for an SCC C of D(G) with t0 = t0(C) (box 99 §2):
- E_C: #ext gates of C's movers.
- I_C: #internal gates.
- G_C[φ] for a face map φ on C's gates: the one-player game in which Odd's choice at each gate of C is φ, the movers outside C are fixed
  at their final strategies, and all other Odd vertices are at their (constant after t0) choices.
- A window is a maximal run of states a..b ≥ t0 on which σ̄_t|C is constant and Λ_t(x) is constant for every mover x ∈ C.
- Gap(C): the maximum, over φ, starts and legal tie resolutions, of the number of iterations in a window of a Howard run of G_C[φ] (a
  window of a one-player run: Λ of every mover of C constant).
- Deep_c(C): #flips of internal gates of C after t0 that TWO-CROSS charges to a change of depth > c.

Statement. The number of HOW3 iterations after t0 at which some mover of C switches is at most
(1 + E_C + N_C·(n3 − 1) + 2·I_C·(n3 − 1 + n3·(S_c(n3) − 1)) + Deep_c(C)) · (Gap(C) + 1), for every c ≥ 0.

Proof.
- Window = one-player run. After t0, plays from C's movers see only fixed vertices outside C (box 99 §1), so Odd's optimal choices there
  are constant. On a window σ̄_t = σ̄_a on the gates of C, so Ω_t is the value of σ_t in the one-player game G_C[σ̄_a]. HOW3's step from
  σ_t uses only these values, so σ_a, …, σ_(b+1) is a Howard run of G_C[σ̄_a] whose states a..b have every Λ in C constant: a window of
  that one-player run. Hence b − a + 1 ≤ Gap(C) + 1.
- Counting windows. A new window starts only at a state where σ̄|C changes or some Λ in C changes.
  - Λ changes: at most N_C·(n3 − 1) such states (DEPTH-COUNT3).
  - σ̄|C changes: each such state has a flip at some gate of C. Ext gates flip at most once after t0 (ONE-CROSS3, R232 §0): at most E_C.
  - Internal gates: by TWO-CROSS each flip is charged injectively to a change of one of the two faces at the same step. The charged
    changes are Λ changes (≤ n3 − 1 per face), changes of depth ≤ c (≤ n3·(S_c(n3) − 1) per face, DEPTH-COUNT3), or deep (counted in
    Deep_c).
  - Summing gives the first factor. ∎
- Corollary. If Gap(C) ≤ poly and Deep_c(C) ≤ poly for one fixed c, then H(C) is polynomial in N + M: SCC-LIN in polynomial form. With
  SCC-RED (box 99 §2), T3 is then polynomial (a polynomial, not U-FREE's N + M + 4).
- What is NOT claimed: the exponent. S_c(n3) = O(n3^(c+1)), so the bound is crude; the measured runs are linear (§5).

## 5. The two conjectures and their DATA (run100.sh, run100b.sh; outputs experiments/si/box100/out/)
### 5.1 CONJECTURE LAM-GAP (open)
Statement. Gap(C) ≤ N_C + 1: in every one-player game G_C[φ], Howard spends at most N_C + 1 iterations with all Λ of C's movers constant.
- READING (why it might hold; not a proof). Inside a fixed-Λ window every play from C ends at its fixed Λ-vertex. Values are then path
  values into fixed targets, ordered lexicographically, and a Howard step dominates one Bellman–Ford round over mover hops. That would give
  N_C rounds. The step not proved: optimal substructure of VJ path values (the best simple path to Λ need not extend a best suffix when
  the suffix would pass the start vertex). That is exactly where a switch could close a new cycle with the same top Λ.
- Literature context (opened: arXiv 2506.12254, abstract only, Asadi–Chatterjee–de Raaij 2025, «Lower Bound on Howard Policy Iteration
  for Deterministic Markov Decision Processes»): Howard on deterministic MDPs needs Ω̃(I) iterations in the input size I. That bound is in
  bits of the weights, so it does not contradict a bound linear in the number of edges. Hansen–Zwick 2010 (ISAAC, LNCS 6506, pp. 415-426)
  is cited only as described in a search summary: NOT opened, not a source.
- DATA (l1probe100.py; unit: one-player Howard run; set: every σ̄|C occurring in the HOW3 run plus 3 random face maps, from the run's
  state and 2 random starts, both tie rules (seed 100); scope: largest SCC; out/l1probe100.out). Counter: maxLamGap = the longest run of
  iterations with every Λ of C's movers constant; LAM-GAP requires it to be ≤ N_C + 1. It holds on all 15 one-giant-SCC instances.
  - Highest ratio, C98_2_2_3: N_C 4, gap 4.
  - MWR4 / 8 / 16_2: gap 26 / 50 / 98 against N_C 44 / 80 / 152 (ratio about 0.6-0.65, linear in n).
  - C6G8_n54, RWX_n95, DWT20_2803, DHIB18_2805, DHIB26_2804: gap 9 / 11 / 5 / 6 / 8 against N_C 50-102.
  - C98 climbs: gap ≤ 4.
  - Max one-player run length L1: 102 on MWR16_2 (= its T3; L1 / M_C 0.308); max L1 / M_C 0.6 (C98_2_2_3).
  - Max Λ-change steps per run: 100 (MWR16_2).
  - Random face maps are a sample, not the maximum over φ, so this does not measure Gap(C) itself.

### 5.2 CONJECTURE DEEP3 (open)
Statement. For some fixed c (the data suggest c = 3, which counts the constant core K3, K0 among Π's top elements), Deep_c(C) is
polynomial in N + M on every genome.
- DATA (cross100 with CMAX = 3; unit: gate flip; counter deep = flips charged to a change of depth > 3; dmax = max depth of a charged
  change). The counter covers EVERY gate over the WHOLE run (states 0..T3), so it is an upper bound on Σ_C Deep_3(C), which counts only
  internal gates after t0.
  - 400 random genomes (seed 10001): deep 0, dmax 3.
  - 26 frozen instances: deep 79 in total, dmax 6.
  - MWR4/8/16_2: deep 0, dmax 3 at every n. The re-arm is entirely shallow, so DEPTH-COUNT3 alone counts it.
  - C98 climbs: deep 0, dmax ≤ 2.
  - Non-zero rows: MW8_2 / MW32_2 deep 8 / 32 (= n, at gates that are not internal: qint 0), DHIB26_2804 24 (dmax 6), DWT20_2803 9,
    C6G8_n54 3, DHIB18_2805 2, Kprev_8 1.
  - Quiet flips (Λ unchanged): 833 on the 26 and 211 on the random set (qint = internal 591 / 197).
  Nothing here is asymptotic beyond the MW / MWR families, where deep grows linearly or stays 0.
- READING. DEEP3 is the Γ3 form of L-NEW 70's CONJECTURE DEEP-k1 (Q_(>c) polynomial at k = 1), restricted to the internal gates of one SCC.
  A counter on internal gates would need deep changes: a Π that changes below its top c + 1 elements super-polynomially often, which is
  what an odometer on the e-sets of a hub does.

### 5.3 DEAD: FLIP-LOUD
- Conjecture (set up while tracing, before the data): «every gate flip is charged to a Λ change of the face Odd leaves». It would have
  bounded internal flips by DEPTH-COUNT3's Λ count alone.
- Killed: MWR4_2 (sha1 856d369b), gate (34, 0). All 9 flips are Λ-quiet: both faces have Λ = K1 at states 0..30. Example step 10 → 11:
  - Odd leaves pe;
  - Π(pe) goes from {K3, K0, e(34,0), b(43,0)} to {K3, K0, e(30,0), e(34,0), b(1,0), b(43,1), b(36,0), b(35,0)} (depth 2);
  - len goes from 13 to 33.
- Counters (cross100 qflip / qint): quiet flips on every instance with internal re-flips.
  - MWR4_2 13 (9 internal);
  - C98_4_5_3 33;
  - C6G8_n54 54.

## 6. What this box leaves open (for L-RED and the next box)
- LAM-GAP: a proof of the Bellman–Ford step for VJ path values at fixed Λ, or a one-player Γ3 game with a fixed-Λ window longer than
  N_C + 1. A kill would not kill SCC-LIN; it would only remove this route.
- DEEP3: a family whose internal gates flip on deep changes. Per §5.2 this is the same target as L-NEW's DEEP-k1, seen from inside one
  SCC.
- Exactness: even with both conjectures, this route gives a polynomial, not H(C) ≤ M_C. On the data H(C) ≤ M_C holds (box 99 §4;
  L-RED's climbs: H ≤ M_C − 1).

## 7. Sources opened (this box)
- claude/l-red 59daaef2 docs/red/R232-box99.md (§0-§2) and experiments/red/r232/how3_232.py, oc3_232.py (read; engine used read-only).
- claude/l-red docs/red/R231-onecross.md (§1-§3; ONE-CROSS on IDEAL-CYC).
- claude/l-new docs/new/N5-DEPTH-box206.md (§0-§2: DEPTH-COUNT, LOUD-SPLIT, DEEP-k1).
- trunk 7f7ee70e1 docs/RESULTS.md R125 (l. 15595-15654: (d) F1, (f) LOC-GATE3, (i) NO-TIE3).
- arXiv 2506.12254 (abstract page only).

## Addendum A (L-SI successor 51, 2026-11-12T10:14Z (date -u); append-only, §0-§7 unchanged): L-RED 66's gaps D1 and W1, fixed
Source: L-RED 66, docs/red/R234-lamgap.md (not yet on origin when this was written; relayed by the Lead 10:15Z). Verdicts: TWO-CROSS
SURVIVES; WINDOW SURVIVES with W1; DEPTH-COUNT3 has the missing case D1.
- D1 (DEPTH-COUNT3, §3): a length-only change has depth |Π_t| by definition. If |Π_t| ≤ c it counts as shallow, but §3's proof put it with
  «d > c: P_a = P_b», so the P-count does not cover it. L-RED measured 284 such changes on the 26 instances and 2,590 on 100 random
  genomes.
  Fix (L-RED 66, PROVED lane; checked here). On a Λ-interval Ω(v) is ⊴-non-decreasing (F1), so Π never falls in the VJ set order ≺:
  each Π value occupies one plateau of consecutive states. On a plateau, Λ and Π are fixed, so every change is length-only, and len is
  strictly monotone there (F1; the direction depends on Λ's parity). That gives at most n3 − 1 changes per plateau. Plateaus with
  |Π| ≤ c number at most S′_c(n3) := Σ_(j ≤ c) C(n3, j) per Λ-interval. Corrected statement of DEPTH-COUNT3: per vertex, at most n3 − 1 Λ
  changes and at most n3·(S_c(n3) − 1) + n3(n3 − 1)·S′_c(n3) changes of depth in [0, c]. Polynomial for fixed c, as before.
- W1 (WINDOW, §4, and box 101 §3): G_C[φ] was defined with EVERY mover outside C fixed at its final strategy, including movers upstream of
  C. Those can still switch after t0(C), so «Λ constant at every vertex» on the two-player run is not «Λ constant at every vertex of
  G_C[φ]».
  Fix: take G_C[φ] on Reach(C), the vertices reachable from C's movers in Γ3. Reach(C) is closed under successors, and after t0(C) it
  contains no switching mover outside C (box 99 §1, §2). Read a window as «σ̄|C and Λ constant on Reach(C)»; then each two-player
  window is a window of the one-player run of G_C[σ̄_a] on Reach(C). L-RED 66 replayed every two-player window that way on the 26
  instances: replayfail 0, and its control mismatches 14 of 14. The Λ-change count stays ≤ n3(n3 − 1).
- Corrected bound (with L-RED 66's Lemma SHARP, b − a ≤ |Ch|; box 101 Add. B), for every c ≥ 0:
  H-run(C) after t0 ≤ (1 + E_C + n3(n3 − 1) + 2·I_C·(n3 − 1 + n3(S_c(n3) − 1) + n3(n3 − 1)S′_c(n3)) + Deep_c(C))·(N_C + 1).
  Deep_c is unchanged: L-RED found no charged flip on a length-only change of depth ≤ c («0 so far»), and Deep_c counts depth > c
  anyway.
