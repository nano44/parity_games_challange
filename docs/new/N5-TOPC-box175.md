# Box 175 N5-TOPC: the C = 1 proof attempt of L-RED's CONJECTURE TOP-C breaks at once — with the definition as relayed, TOP-C is DEAD at C = 1 on 2-wide genomes: gain′ = gain″ = 4 at d 2 (L-RED's fa_d2_k2_W2, N 4), gain′ 8 / gain″ 7 on R110's landed instance iso_d4_st9 (𝓛^R_4); the coupled mover is re-armed once per top move
L-NEW successor 55, 2026-11-06 (from 01:28Z, date -u: see the commit). Lead brief BOX 175 (01:27Z): lane proof attempt of L-RED's
CONJECTURE TOP-C at C = 1 (claude/l-red 16ae702d, docs/red/R208-topcouple.md); if the proof breaks, the failing configuration goes to
L-RED as a seed. Labels: PROVED (lane, unrefereed) / DATA / CONJECTURE / DEAD (instance) / READING. Model: RESULTS R104's definition
(P-IDEAL-KEYS §0 notation). Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Answer
- SOURCE CAVEAT. claude/l-red 16ae702d is not on origin at 01:2xZ (git fetch: «Not a valid object name»; origin/claude/l-red =
  39b1f852, no docs/red/R208-*). I used the definitions in the Lead's relay, quoted here verbatim: «a coupling is a lower option whose
  Ξ-target is a top mover, and C is their number. gain′(G) := T(G) − max over all acyclic re-routings of the couplings (to X or to a
  lower mover) of T(G minus top).» «Conjecture: gain′ ≤ 2 + C. TOP-ADD is C = 0.» «G minus top» is read as in L-RED's Lemma TOP-ADD
  (R207 §1, claude/l-red 39b1f852 docs/red/R207-tstar.md, opened): «Let G − U be the genome on the other movers, with the same start»,
  and as in L-RED's r207/topadd_ck.py (the same construction). If R208 defines gain′ differently, this kill must be re-checked against it.
- Two readings, both computed:
  - gain′ (same start, as TOP-ADD): T(G) − max over re-routings of T(G − top) from G's start restricted to the lower movers;
  - gain″ (start-free, weaker as a conjecture, so a kill of it kills both): T(G) − max over re-routings AND over all starts of the
    lower genome of T(G − top).
- DEAD (DATA instances, two simulators): CONJECTURE TOP-C at C = 1 («gain′ ≤ 2 + C»), on 2-wide degree-2 genomes:
  | instance | class | N | C (coupling) | T(G) | max T(G − top), same start / all starts | gain′ / gain″ |
  | --- | --- | --- | --- | --- | --- | --- |
  | fa_d2_k2_W2 (claude/l-red r177/out; copy box175/out/fa_d2_k2_W2.json, sha1 6451b7c7…) | 𝓛_2 (free W) | 4 | 1: (0, 1) → 3 | 4 | 0 / 0 | 4 / 4 |
  | iso_d4_st9 (R110's landed DEAD instance; box160/out/iso_d4_st9.json, sha1 7ca1e68c…) | 𝓛^R_4 | 8 | 1: (3, 0) → 6 | 11 | 3 / 4 | 8 / 7 |
  | g4_L12 (claude/l-red r188/instances; copy box175/out/g4_L12.json, sha1 7d9c1025…) | 𝓛_4 (free W) | 8 | 1: (4, 1) → 6 | 12 | 5 / 6 | 7 / 6 |
  | tri_d5_L12 (claude/l-red r197/lag; copy box175/out/tri_d5_L12.json, sha1 9d419424…) | 𝓛^R_5 | 10 | 1: (2, 1) → 8 | 12 | 8 / 8 | 4 / 4 |
  - Checks: box175/gain.py and gain2.py (box 150 simulator) and box175/xgain.py (L-RED's r187/ideal.py, an independent simulator) give
    the same T(G), the same re-routing values and the same gains; box150/check.py on each file: XSIM 0 and every R105 check 0.
  - Corpus DATA (box175/log/corpus_gain*.txt; in-tree boxes 150-174 and claude/l-red 39b1f852 experiments/red, degree ≤ 2, C ≤ 2, stored
    starts): gain′ histogram at C = 1: −3:1, 0:27, 1:10, 2:6, 3:3, 4:5, 8:1 (53 files); at C = 0: 0:74, 1:15, 2:5, 3:1 (the 3 is
    gate_K3_m2 with 6 two-option top movers, allowed by TOP-ADD). C = 0 never exceeds TOP-ADD's bound.
- Hand proof of the d 2 instance (§1): the lower genome runs 0 steps from every start under the only acyclic re-routing, while G runs 4.
- Where the C = 1 proof attempt breaks (the Lead's question «can the proxy re-arm L_q only O(1) times?»): NO. On iso_d4_st9 (DATA,
  box 150 simulator, values by ENC) the coupled mover 3 (option 0 Ξ-targets top mover 6) moves at steps 4, 7 and 11:
  - step 4, to option 0: top mover 6 moved at step 3 and cv(6) rose from −16382 to −8180, so v(3, 0) = ε(3, 0) + cv(6) rose from −16414
    to −8212 > v(3, 1) = −12288 (a re-arm by the coupling); KP(3) = 0 throughout;
  - step 7, back to option 1: v(3, 1) rose to 5248 at step 5 (lower rise, RETURN), and 3 waited until KP(3) flipped to 1 at step 7
    (pair (0, 1) flips when mover 1 moves, PAIR-KF);
  - step 11, to option 0 again: 6 moved at step 10 and v(3, 0) rose to 9324 > 5248 (a second re-arm by the coupling).
  So the single coupling re-arms the lower part after two different top moves, and the lower part in between makes 3 return. READING:
  nothing in the model limits these rounds by C; they are limited by the coupled top mover's moves (≤ 1 + F(d − 2), PAIR-MOVES), the
  SLOT-TRADE quantity again.
- Seeds for L-RED (R209): the four files above; the smallest is the d 2 one (N 4), whose 4 steps alternate top / lower / lower / top.
- READING (value): TOP-C's route «T*(d) ≤ T*(d − 1) + 2 + C» is closed as stated. What survives is the data observation that on
  2-wide genomes gain′ stays small (≤ 8) in everything we have; a bound must allow a gain per top move, i.e. gain′ ≤ c·(moves of the
  coupled top movers), which is no better than PAIR-MOVES.

## 1. The d 2 instance by hand (R104 definition, R105 ENC)
- fa_d2_k2_W2: movers 0, 1 (level 0), 2, 3 (level 1), all of degree 2. Option fields (W-target, Ξ-target, gate, β rank, parity):
  0: (−, X, 7, 3, odd), (−, 3, 5, 5, odd); 1: (−, 0, 2, 6, odd), (−, X, 3, 0, odd); 2: (1, 1, 4, 4, odd), (0, X, 1, 1, odd);
  3: (1, X, 6, 7, even), (0, X, 0, 2, even). Start 0111. The only coupling is (0, 1) → 3 (C = 1). Ξ-edges 0 → 3, 1 → 0, 2 → 1:
  acyclic.
- G's run (box 150 simulator and L-RED's ideal.py): 0111, 0110, 1110, 1010, 1000; movers per step [3], [0], [1], [2]: T(G) = 4.
- G − top (movers 0, 1). Re-routings of (0, 1): to X, or to mover 1 (cycle 0 → 1 → 0, excluded), or to 0 (self-loop, excluded): only X.
  - Mover 0: v(0, 0) = −2^3 = −8 > v(0, 1) = −2^5 = −32 at every state. At option 0 its A-set is {0}; at option 1 it is {1, 0} and its
    keys are the gates (5) for option 1 < (7) for option 0, so it stays. Mover 0 never moves.
  - Mover 1: v(1, 0) = −2^6 + cv(0) ≤ −64 − 8 < −1 = v(1, 1). At option 1, A = {1}; at option 0, A = {0, 1} with gates 2 < 3, so it
    stays. Mover 1 never moves.
  - So T(G − top) = 0 from every start: gain′ = gain″ = 4 > 2 + C = 3. ∎ (PROVED (lane), for this instance.)

## 2. Files (experiments/new/box175/)
- gain.py (gain′, same start), gain2.py (gain″, all starts), xgain.py (gain′ with L-RED's simulator; usage xgain.py <l-red experiments/red> files);
  out/fa_d2_k2_W2.json, out/g4_L12.json, out/tri_d5_L12.json (byte copies of L-RED's files); log/corpus_gain.txt, log/corpus_gain2.txt.

## 3. Next (Lead decides)
- Check R208's exact definition of gain′ (16ae702d was not on origin). If it matches, TOP-C (C = 1) is DEAD as stated; L-RED's «DATA: 3
  at C = 1» must come from a narrower class (helpers?) or a different «minus top».
- A surviving form would need a per-top-move term: gain′ ≤ 2 + Σ over coupled top movers of their moves — true by TOP-SPLIT-type
  accounting? Not attempted here; it is not polynomial by itself.
