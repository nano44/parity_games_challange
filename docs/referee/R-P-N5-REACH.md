# R-P-N5-REACH: REFEREE report on P-N5-REACH (L-NEW successor 58, box 189)
REFEREE successor 25 (Opus 5.5, D15); header time: see the commit (date -u at writing: 2026-11-07T03:04Z). Packet frozen at
claude/l-new 73b3d1fd. I did not read docs/referee-2/ for this report.

## 0. Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §1 | premises | all LANDED; quotes byte-checked (§1 below) |
| §2 | Theorem NO-REACH (a)-(d) | SIGN |
| §3 | Γ3(G) and its size n3 = N + 7M + 10 | SIGN |
| §4 | Lemma S3-START | SIGN |
| §5 | Lemma PAD (a)-(c) | SIGN |
| §6 | K3, PLAY3, SBAR3, TAU3, ESC3, W3, KEY3 | SIGN (every LENGTH and INDEX spot re-derived, §2 below) |
| §7 | Theorem REACH3 | SIGN; replayed on two corpus games with L-COMP's n5b against my own simulator (§3) |
| §8 | Corollary REAL-IDEAL-S3 (a), (b) | SIGN as a reduction / necessity statement |
| §9 | DEAD SUBDIV (A, B) | SIGN; replayed with my own G^pad builder and n5b (§3) |
| L-1 | the line | NOT YET: RE-L1 (DATA coverage), exact text in §4 |

## 1. Objects and premises
- sha1 of the bytes at 73b3d1fd; every one is EQUAL to the Lead's relay:
  - P-N5-REACH.md b7bd6937…;
  - L-1 b12ec57a…;
  - reachcheck.py c368b363…, reachcheck.out af50ee34…;
  - gamma3.py 8758456f…, subdiv.py 63c7ae38…;
  - reach.pins f0fc1ba6…;
  - inst RECT_d11_T59_g3.pg 0825f9d1…, REC_d10_tower_mu30_g3.pg c6058ce5….
- Premises:
  - 38 «…» quotes of §1 checked against trunk 6ca995ed docs/RESULTS.md and docs/new/N5-ssi-global.md (sha1 66fde9ef…, as cited),
    whitespace-normalised.
  - 34 occur verbatim. The other 4 contain «…» elisions, and each of their pieces occurs verbatim («## SPEC (EXACT», «N5 (SPEC S1-S5»,
    «maximising (Ξσ(w), w)» + «otherwise do the same for Odd on Iτ», «changes at least one of them»).
  - All cited results are landed: R104, R57 (b), R24, R103, R36 (c), R15 (d). No theorem of R104 is used: I checked every proof step
    against [DEF] only.

## 2. Proofs re-derived (every step; LENGTH and INDEX spots in full)
- §0 Fact DUAL, Fact X: correct. Fact X needs acyclicity: the chain of (x, k′) never returns to x.
- §2 NO-REACH:
  - j = 0 by FIX 1: K0 {K1 Ω 5, K3 Ω top + 3}, both odd, the lowest is K1. K1 {K0 even, K1 odd}: K0.
  - Step: K1's loop: (K0, ∅, 1) vs (K0, ∅, 0), c even, the shorter is better: not improving.
  - K0 → K3 with σ(K3) = K1: (K0, {K3}, 2) vs (K0, ∅, 1), difference {K3} odd: not improving.
  - K0 → K3 with σ(K3) = K2: Odd's pointwise optimum is ⊴ the K2-loop value, reward < 0 < p′(K0): not improving.
  - S4a keeps σ off Iσ; S4c touches only improving vertices.
  - (d): the only entry into K is β → K0, the cycle {K0, K1} is fixed, and every cycle outside K has an e-vertex or c_W node
    (acyclicity). All correct.
- §3 count: core 4 + gate faces 2M + escapes M + mover edges M = 4M + 4 pads; n3 = N + 3M + 6 + 4M + 4. Correct. Pads Ω ≤ 2 leave top
  unchanged (the unused loop already has Ω 2).
- §4 S3-START, from S3's formula (max r(w), r = Ω if even else −Ω; Odd on Ω + 1). Every case correct:
  - mover: the unique Ω-2 pad;
  - β: xt (r 0) over pb (r −1);
  - K0: pA (0 > −5); K1: s (0 > −1); K3: K2 (−3 > −5);
  - gate on Ω + 1: pe (2) over pβ (−1); K2: loop (4) over r (−1).
- §5 PAD:
  - every cycle meets K0, K1, K3 (Ω ≥ 5), K2's loop (3), a gate face (e or β, Ω ≥ 6) or c_W; a pad's successor is in Γ.
  - c_X's loop has no pad.
  - (c) follows. Correct.
- §6.1 K3, recomputed:
  - (a) values: K1 (K1, ∅, 0), s 1, r 1, K2 2, K3 (K1, {K3}, 3), pA 4, K0 (K1, {K0, K3}, 5), q 6. MATCH.
  - (b): K0: {K3} odd, K1 better: improving. K1: q's P has K3 at the top, odd: not improving. K3: LENGTH, 0 vs 2 with node K1 odd, the
    longer K2 is better for Even: not improving (in Γ 0 vs 1, same direction). MATCH.
  - (c) Even's escape r → K1 → q → K0 → K1 reaches node K0 > 0: correct.
  - (d) H-plays: K1-node vs K2-node, −p′(K2) > −p′(K1): pA kept. Correct.
- §6.2 PLAY3: plays read off the edges. Node K1; P = B(g) ∪ {K0, K3} (β Ω ≥ 6 > 5; K2, pads, movers, gates below). lev 0: (c_W, ∅, 1)
  and (c_W, ∅, 2). lev ≥ 1: e_g in P. Correct.
- §6.3 SBAR3:
  - (i) lev ≥ 1: e_g outranks every β and is even, so pe is better for Even. lev 0: node c_W vs K1.
  - K2: LENGTH, φ(K2) = (K1, ∅, 2) vs φ(r) = (K1, ∅, 1), longer better for Even, so the loop is not Odd-improving. Re-derived; MATCH.
  - (ii) R36 (c) on G^d gives ρ pointwise optimal; P1 then makes the values equal.
  - (iii) uniqueness: a cycle through e has an even e-node ≠ K1; otherwise the value differs by node (lev 0) or by e_g ∈ P. Correct.
- §6.4 TAU3: under τ every gate takes e, so plays from pe end at c_W. From pβ, Even reaches node K0 > c_W. Correct.
- §6.5 ESC3: xt(g) leads to node c_W (even), pb to an odd node (K3 (d)). β is on no H-cycle. Correct.
- §6.6 W3, LENGTH re-counted:
  - The play from a level-ℓ mover passes 5 vertices per level (x, m, g, pe, e) for levels ℓ..0, then c_W: 5ℓ + 5. Then m 5ℓ + 4, g
    5ℓ + 3, pe 5ℓ + 2, e 5ℓ + 1. β with mover xt: 1 + 5·lev(xt) + 5 = 5·lev(xt) + 6.
  - P = ∅ (all below c_W), so W does not depend on s. MATCH.
  - (ii)-(iii): every H-option of x is a pad with W* 5ℓ + 4 = W*(x) − 1, so TIE = R. Correct.
- §6.7 KEY3:
  - (a): node K1 on both sides, K0 and K3 cancel, the β of largest rank decides; Ω(β) = 6 + 2·rank + parity carries rank order and
    parity. Correct.
  - (b) INDEX, re-derived: the root-first sequence e_0, pe_0, g_0, m_0, x_0, …, e_ℓ, pe_ℓ, g_ℓ, m_ℓ has length 5ℓ + 4 for every option.
    Block i is a function of g_i, so the first difference is e_(g_i) vs e_(g′_i). e-indices follow gate indices, which is [DEF]'s
    lexicographic gate-index key. Equal lengths: no prefix case. MATCH.
- §7 REACH3:
  - The induction uses TAU3, ESC3, [1E-N3] P2, W3 (iii), [RULE], KEY3 (a)/(b) level by level, with σ_new below level ℓ = the standard
    σ for s_(j+1).
  - Step L: σ_new = σ, τ_new = τ, Iσ ∋ (K0, K1), so the transition is a fallback.
  - Correct. Maximality and finiteness are argued without assuming L finite.
- §8: (a) is REACH3 with n3; (b) is the contrapositive with ≥ L + 1 iterations. A reduction only; the not-claimed list is right.
- §9: the killed statement is quoted. Instances: §3.
- §13 TARGET: priorities ≤ top + 3 < n3 (R104 count, not re-derived by me); reduction only, G-N5-TIME OPEN. Agreed.

## 3. Independent replays (review items «engine not L-NEW's» and DEAD)
- REACH3 with L-COMP's n5b.py (spec mode, default start = S3), and L(G) and the IDEAL states from my own t3r_sim.py. Driver
  scratch/reach_replay.py. It checks:
  - n = N + 7M + 10 and that every mover edge goes through a pad to one of x's gates;
  - the maximal FL run from state 0, recomputing each play valuation myself;
  - the mover choices at states 0..L against the IDEAL states.

  | game | n | L(G) own sim | n5b iterations / fallbacks | FL run from state 0 | transition L + 1 fallback | movers = IDEAL states 0..L |
  | --- | --- | --- | --- | --- | --- | --- |
  | RECT_d11_T59_g3 | 340 | 59 | 62 / 1 | 59 | yes | yes |
  | REC_d10_tower_mu30_g3 | 310 | 35 | 38 / 1 | 35 | yes | yes |
- DEAD SUBDIV. Driver scratch/subdiv_replay.py: G^pad built from §9's text by my own code, run on n5b (spec).
  - A: G from (σ0, τ0): 1 iteration, flags [1]. G^pad (n 8) from S3: 1 iteration, flags [0].
  - B: G 2 iterations; G^pad (n 17) 3 iterations.
  - In both, S3's start on G^pad is the transported (σ0, τ0). DEAD SIGN.
- Lane check block: `reachcheck.py --approx` at 73b3d1fd is byte-equal to reachcheck.out (11.5 s).
- Oink: NOT RUN by me (Oink not built in this container). The lane's xcheck.out is lane DATA.

## 4. DATA rule (§10 and L-1)
- Counter code read (reachcheck.py l. 67-125, 143-180):
  - NO-REACH counts per state and per (state, vertex ∉ {K2, K3, c_X}).
  - S3-START counts per genome.
  - PAD counts per (state of the S3 run on Γ3, vertex ≠ c_X, world), both worlds.
  - REACH3 per genome, with states 0..L standard, transitions 1..L FL (fallback flag, τ kept, σ changed, play value kept), L + 1
    fallback.
  - W3 counts per (state ≤ L, mover).
  - §10's unit / set / scope statements MATCH the code.
- L-1:
  - Shape: one line, 52 «(» / 52 «)», depth never negative, 0 «|».
  - The statement clauses match §2-§9 (NO-REACH, Γ3 with 4M + 4 pads and n = N + 7M + 10, S3-START, PAD, REACH3, the Corollary,
    DEAD SUBDIV). The DATA figures it gives match reachcheck.out. «L(G) 9 to 59» is the C14 range (A_d4_W2_k2 9, RECT_d11_T59 59).
  - Not-claims present.
- RE-L1 (required, DATA coverage; the C127 E-1 / C128 E-5 class). L-1's DATA parenthesis covers NO-REACH (a)-(b), the iteration
  histogram, REACH3 and the cross-checks. It has neither a count nor a «no separate DATA» entry for these signed clauses:
  - NO-REACH's «no β-vertex … in the P-set» (counted: 42,880 pairs);
  - S3-START (454 genomes);
  - PAD (693,030 triples);
  - DEAD SUBDIV (instances re-run);
  - the Corollary (no data).

  Replace (the old string occurs exactly once in L-1):
  «0 failures of REACH3 in 454 genomes,» → «0 failures of REACH3 in 454 genomes, the β-free P-sets of NO-REACH 0 on 42,880 (state, vertex)
  pairs, S3-START 0 on 454 genomes, PAD 0 on 693,030 (state, vertex, world) triples of the S3 runs on Γ3, both DEAD SUBDIV instances
  re-run, Corollary REAL-IDEAL-S3 no separate DATA,»
- Verdict L-1: NOT YET (RE-L1). With it, it MATCHES.

## DONE / FINDINGS / NEEDS
- DONE:
  - premises byte-checked;
  - every proof re-derived, LENGTH and INDEX spots in full;
  - REACH3 replayed on 2 corpus games with n5b against my own simulator;
  - DEAD SUBDIV replayed with my own builder;
  - check block re-run;
  - DATA rule clause by clause.
- FINDINGS: §2-§9 all SIGN; L-1 NOT YET (RE-L1, DATA coverage only).
- NEEDS: L-NEW: fixes entry 1 + L-2 with RE-L1; I will byte-test it.

## §C. Fixes entry 1 and line L-2 (REFEREE successor 25; date -u at writing 2026-11-07T03:58Z)
- Objects at claude/l-new 571c75c5:
  - L-2 sha1 4de27b32d5ed11accb092cf44cb27e14be6b9609 (3,628 B);
  - fixes file 307651b2… (5,344 B);
  - L-1 b12ec57a and the packet b7bd6937 unchanged.
  - REFEREE-2's report read for its W-1, W-2 texts: claude/referee-2 b0860fcd, R2-P-N5-REACH.md l. 101-108.
- Byte test (own script):
  - the three replacements of entry 1 (RE-L1, W-1, W-2), as written there, each occur exactly once in L-1 (and once in order);
  - L-1 + the three is byte-equal to L-2;
  - shape: one line, 57 «(» / 57 «)», depth never negative, 0 «|», no «c_X»;
  - RE-L1 is my text verbatim; W-1's and W-2's new texts are REFEREE-2's verbatim.
- W-1's old span (the Lead's question): REFEREE-2 gave only the new text, ending «is DEAD». The shortest L-1 span it replaces is «the
  statement «S3 can be simulated on every game by subdividing every edge» is DEAD». L-2 then reads «… to the run of the game from that
  start pair is DEAD as stated (DEAD SUBDIV: …». The reading is CONFIRMED.
- Meaning:
  - W-2 MATCHES: «the unused even self-loop of priority 2» is R104's own wording for c_X.
  - RE-L1, DATA rule against reachcheck.py, re-checked:
    - NO-REACH (d): the counter's set (state, v ∉ {K2, K3, c_X}) is exactly the scope of the clause it is attached to («at a vertex
      outside K2, K3 and the unused even self-loop»). «(state, vertex) pairs» therefore names the statement's own pairs. MATCH.
    - S3-START 454 genomes: MATCH.
    - Both SUBDIV instances: MATCH. Corollary no-DATA: MATCH.
    - PAD: NOT a match (my own miss in RE-L1). L-2's clause is «no pad is ever a cycle node or in a P-set», at every vertex. The
      counter (l. 106-109) skips v = c_X; it tests «cycle node Ω < 3 or a pad in P», which is stronger. So 693,030 counts (state,
      vertex ≠ c_X, world), and «(state, vertex, world) triples» states a wider set than was counted. This is the C124 E-1 pattern;
      the DATA rule's set clause applies to my own text too.
  - W-1, new finding. The killed statement's game is not determined without §9's pad index order («indices n, n + 1, … in (a, b)
    order», packet l. 272). N5's run depends on vertex indices, and §9's obstruction is index-driven (FIX 2's DFS order). A DEAD
    record must name the exact statement that is killed.
- Required, two replacements on L-2 (each old string occurs exactly once):
  - RC-1 (DATA set): «PAD 0 on 693,030 (state, vertex, world) triples of the S3 runs on Γ3» → «PAD 0 on 693,030 (state, vertex other
    than the unused loop, world) triples of the S3 runs on Γ3»
  - RC-2 (DEAD statement exact): «1 (Odd, start edge) or 0 has an N5 run» → «1 (Odd, start edge) or 0, the pads indexed after the
    game's vertices in edge order, has an N5 run»
  - Result (my script, with «\n»): 3,714 B, 57 «(» / 57 «)», depth never negative, sha1 13d0ce803260aa5e3a704c311b83766e8be50d8e.
  - My own G^pad builder (scratch/subdiv_replay.py, §3) used exactly this order, so the replay stands for the corrected statement.
- Verdict:
  - Fixes entry 1 is CORRECT as an application of RE-L1, W-1 and W-2.
  - L-2 MATCHES the byte test.
  - In meaning, L-2 is NOT YET: RC-1 (my own RE-L1 wording) and RC-2. With both, the line MATCHES.
  - All statements stay SIGNED.
