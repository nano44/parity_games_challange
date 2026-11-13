# B6 attempt 2 (D1 / D22 / D25): KILL attempt on QUIET-KEY-1P by construction: lane report (verdict, record of the session, how the rule was found, dead ends). The statement, the rule, every proof and the DATA are in docs/red-b/P-N5-EXP.md and nowhere else
L-RED-B successor 5 (session_01V5yGRXFf3kFNfkycCHTnLT; Fable 5.2, xhigh), 2026-11-13. Second independent adversary (D22): L-RED's
R243 was not read before the verdict below was written. Labels: READING / record, except where a line says DATA or points to the packet.

## 0. Verdict (kill candidate; lane DATA and a lane proof until two referees sign; D1)
- Object: [Q claude/l-new a143d406 docs/new/N5-QUIETKEY-box217.md §2] «**QUIET-KEY-1P (OPEN).** There is a polynomial p with
  T_key(1P(G)) ≤ p(N + M) for every Ξ-acyclic genome G.», with its kill criterion «A family G_n of Ξ-acyclic genomes with
  T_key(1P(G_n)) super-polynomial in N + M (a fit with residuals on a constructed or climbed sequence, then the simulator's numbers
  re-checked by N5 itself on Γ3 at the sizes where that is feasible) kills QUIET-KEY-1P, hence O1 and O1′».
- Outcome: a RULE G_k (not a climb) with T_key = L(G_k) = 2^k − 2 at N = 9k − 16, M = 2N, k + 1 levels, every degree 2 (packet
  P-N5-EXP: Theorem EXP-IDEAL, PROVED lane, unrefereed), and by landed R117 at least 2^k − 1 iterations of N5 from S3 on Γ3(G_k)
  (135k − 230 vertices; Corollary EXP-N5). DATA (packet §9): three simulators state by state to k = 14; the proof's schedule equal
  to the real run step by step to k = 14; N5 itself on two engines with two Γ3 builders to k = 11 (2^k + 1 iterations, every winner
  equal to Zielonka's); every control fires. The brief's alternative («the exact step at which every such rule fails») did not
  occur: the rule delivers the signal with O(1) movers per level.
- The enumeration depth k(G_k) of box 217 is 1: ENUM-LOG (a necessary condition only) is not the obstacle; SW-POLY fails.

## 1. Record of the session (times by date -u)
- 11:29Z trap check (branch, ff to 18dd585f, skew 0 s); EARLY START wait for 1fbd6d0d (on origin 12:11Z); reading: box 217 (all),
  one217.py (all), R113 / R120 title lines, the five tower genomes of claude/l-comp experiments/comp/box29.
- 11:35Z onep.py (own simulator) equal to one217.py on the five towers (30, 136, 209, 67, 299).
- ~11:40-12:10Z paper work (§2 below). 12:13Z handover check committed (4cbabe14), push started.
- 12:14Z gk.py written; first run: T_key = 6, 14, 30, 62 for k = 3..6; 12:16Z to the Lead; 12:18Z N5 itself (n5v spec) on Γ3(G_3..G_8):
  9, 17, 33, 65, 129, 257 iterations; 12:19Z to the Lead; 12:17Z «go»; 12:21Z generator text and G_3, G_4 to the Lead.
- 12:23-12:41Z membership script, three simulators, own Γ3 builder cross-check, second engine n5b, k = 9, 10, 11; b6lemma.py (the
  proof's direct test). 12:38Z the Lead relays independent rebuilds (L-COMP 22, L-RED 70, the Lead). 12:41Z statement of P-N5-EXP
  to the Lead; 12:43Z accepted with changes C1-C7 (applied in the packet).

## 2. How the rule was found (first principles, the Lead's (a)-(c); READING)
- (a) What a doubling level forces. On a 2-per-level ladder a pair that flips its key order at each of its moves has a LEADER that
  moves at once when the pair below flips and a FOLLOWER that must wait until every level above has finished (landed form: RESULTS
  R120, PULSE-NEST; I re-derived it as a counter: the levels above a pending follower form a binary counter that must reach 0).
- (b) What the Ξ side must deliver. The follower's Ξ-order must flip exactly when the levels above are finished, and the leader's
  once per window. Read by value from the ladder above this is impossible: at every quiescent moment all pairs above are aligned on
  the same options, while the mover's own option alternates from window to window (a parity obstruction; any Ξ-closed set whose
  state recurs cannot make a mover alternate, because values rise strictly at every switch). This is why 2-wide ladders need fuel
  levels, and it is the exact step where «Ξ-targets one level up» fails (§3, dead end 1).
- (c) The delivery with O(1) movers per level. Every mover with two options is a two-input latch (packet Lemma MOVE-2): it moves iff
  the key order of its two W-targets (new state) and the value order of its two Ξ-targets (old state) both point to the other
  option. With ranks ordered by Ξ-depth and all parities even, a value is compared «root-first» exactly as a key is, so the model
  is a boolean asynchronous network and one can design in it: (1) «finished above» goes UP BY KEY: an end-follower e_(j+1) of the
  level above reaches the leader's new key only when its own window is over, and an observer two levels up compares it with a wire
  to v_j (first half) or to u_j (second half); (2) it comes BACK BY VALUE: the observers form a pair whose value order flips once
  per window, and the block pair (resp. the end-follower) is Ξ-above that pair; (3) the window parity the observers need comes by
  value from the pair BELOW (its value order is «split / aligned»). All Ξ-edges go down the levels: acyclic. Cost 9 movers per level.
- The duality that suggested it: W-chains with keys (smaller is better, compared from level 0) and Ξ-chains with values (larger is
  better, compared from the exit) are the same kind of object once ranks are depth-major.

## 3. Dead ends (each with its obstruction and instance)
1. «Anti-aligned» 2-wide ladders: W as in 𝓛^R_d, Ξ-target one level UP, depth-major ranks (experiments/red-b/bilad.py). DATA:
   20,000 random ones of depth 6 (seed 1) have T ≤ 6 (data/b6b/bilad_d6.out; the last record line is an instance with T = 6).
   Obstruction: (b) above; the pair above returns to the same state between two decisions of a lower pair.
2. A block pair reading the value order of the block pair above (both doubling, leader parallel and follower crossed, or the
   reverse): the pair above is value-led by its follower at every aligned moment, whatever the window (paper computation; it is
   the special case of (b)). No instance beyond dead end 1's.
3. Reading «finished above» by value along the followers of the upper levels (u_j Ξ-above u_(j+1), …): forces the leader v_j to be
   Ξ-above u_j or u_(j−1) for its own alternation, and then u_j cannot learn the window parity without a Ξ-cycle (u_j ≻ u_(j−1) ≻
   u_j). Paper obstruction; it is why the observers take the parity from the pair below and the completion signal by key.
4. Ablations of the rule itself (DATA, packet §9.6, gkvar.py): without the wires wu_j T = 6; without end-followers T = 2k + 2;
   follower parallel T = 2; ȳ, ȳ′ started on back T = 3; ranks depth-major the other way T = 1. Without the wires wv_j (observers
   reading v_(j+1)) T is still 2^k − 2 at N = 8k − 14: not a dead end, a leaner variant outside the proof.

## 4. What I did not do
- R243 (L-RED) not read. The other lanes' rebuilds are cited in the packet as relayed by the Lead, not opened.
- No N5 run beyond k = 11 (k = 12 would take about 25 + 40 minutes on the two Python engines). No Oink run on Γ3(G_k) (Zielonka of
  experiments/harness is the reference). No statement for N5′-xi, Howard, or any start pair other than S3.
- No attempt at the least number of movers per level, and no proof for the «nowv» variant.
