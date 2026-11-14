# N13 SEESAW: alternating exact first-exit jumps of a potential, with reduced-trap peeling (proposal; LIVE candidate, unattacked)
L-NEW successor 78, 2026-11-14 (design day; D14, D18, D1). Written 19:09Z by date -u, after the fleet's pause (15:55Z-18:30Z).
One implementation: experiments/new/n13/n13.py, sha1 35d77db8f03abf0b331e0f5cbe4fc8d30266df99 (Python, exact integers), mode alt+.
Nothing here is a result (CLAUDE.md hard rule 1). Labels: PROVED (lane, unrefereed, argument given), SOURCE (in the opened paper, not
refereed by the fleet), DATA (a committed run), CONJECTURE, READING, NOT KNOWN. **No polynomial bound is claimed: termination itself
is not proved.** By D1 the candidate is to be treated as wrong until the gauntlet says otherwise.

## 0. In five lines
- Same frame as N12 (parity game as a mean-payoff game, potentials), but no recursion and no per-node choice: one potential is moved by
  alternating jumps of the two sign zones; each jump is the exact first-exit value of every vertex of the zone (one game-Dijkstra).
- DATA: regions and both strategies correct on 10,000 random games (≤ 10 jumps) and on every .pg file of the repo (2,843 files of all
  lanes, ≤ 15 jumps); tc_N: N + 1 jumps; tc+_N: 137 at N = 24; counter_symsi_N: 8 for every N, also with all pads that killed N12.
- Plain GKK (the constant shift this replaces) is exponential on the same games: 3^N on tc and tc+, 2^N on counter_symsi (DATA).
- NOT KNOWN: whether the alternation always terminates; any bound on the number of jumps. My own climbs reach more jumps than vertices
  (15 at n = 12, 20 at n = 18).
- It is probably close to «AESL» of Ohlmann's thesis (described in trunk docs/lit/T27-untested.md §3; thesis NOT opened by me).

## 1. Sources (opened this session)
- P. Ohlmann, «The GKK algorithm is the fastest over simple mean-payoff games», arXiv 2110.04533v1 (9 Oct 2021), PDF sha256
  3f9c9def67dc3db45e05e4b3eb4171fc47db991af116fcd30a49e861d3f84062. Used: §2 (potential reductions; Theorem 3, item 1 «For any potential
  φ we have MP_0 = MP_φ»; positively / negatively safe potentials; simple and reduced games, Lemma 6), §3 (the partition N*, P*, the
  constants δ−, δ+, the GKK potential; Lemma 7), Lemma 9, Theorem 11 (≤ N + E+ + E− + 1 iterations), Theorem 12 (O(2^(n/2))).
- P. Ohlmann, arXiv 2603.07555v1 (N12's source; sha256 292bde19…): only its §2 vocabulary.
- NOT opened: Ohlmann's thesis (Ch. 10 §6: ESL, AESL). T27 reports its sentence «we are not able to establish its termination … (even
  over parity games)». Whether N13's step equals AESL's update, and whether AESL peels, is an open question to L-LIT (asked 15:37Z).

## 2. The algorithm, exactly as implemented (n13.py, mode alt+)
```
INPUT a parity game.  Compress priorities (order and parity preserved) to p(v); B := n + 1; Even = Max, Odd = Min.
w(v) := +B^p(v) if p(v) is even, −B^p(v) if odd; every edge leaving v has weight w(v).  φ := 0; X := V; turn := +1.
while X ≠ ∅:
  a. c(v, u) := w(v) + φ(u) − φ(v) for the edges inside X.
  b. N* := the least S ⊆ X containing: Min vertices with an edge of c < 0; Max vertices all of whose edges have c < 0; Min vertices
     with no edge of c < 0 and some edge of c = 0 into S; Max vertices with no edge of c > 0 all of whose c = 0 edges lead into S.
     P* := X \ N*.                                    (SOURCE §3: Min forces the first non-zero weight to be negative from N*.)
  c. g+ := FIRSTEXIT(P*, Max, e := c);  g− := FIRSTEXIT(N*, Min, e := −c), where FIRSTEXIT(Z, M, e) is the least fixed point of
       v ∈ Z, owner M:      g(v) = max({e(v,u) + g(u) : u ∈ Z, e(v,u) ≥ 0} ∪ {e(v,u) : u ∉ Z, e(v,u) ≥ 0} ∪ {0 : v has an edge of e < 0})
       v ∈ Z, owner not M:  g(v) = min({e(v,u) + g(u) : u ∈ Z} ∪ {e(v,u) : u ∉ Z})                    (all these e are ≥ 0)
     with value ∞ unless forced finite; computed by one Dijkstra (an M-vertex is ready when all its targets in Z over edges of e ≥ 0
     are final; pop the least ready / tentative value; vertices never made final have g = ∞).
  d. T+ := {g+ = ∞}, T− := {g− = ∞}.  If T+ ∪ T− ≠ ∅:  Even's vertices of T+ take their least successor in T+ with c ≥ 0;
     A := Even-attractor of T+ in X with the attractor strategy; W_E ∪= A; X := X \ A; then the same for Odd, T−, c ≤ 0 in the new X;
     continue (no jump, turn unchanged).
  e. JUMP: if turn = +1: φ += g+ on P*, else φ −= g− on N*.  turn := −turn.
OUTPUT W_E, W_O and the strategies recorded in d.   Measure: jumps = executions of e.
```
Controls in the engine: alt- (N* jumps first), plus / minus (always the same zone), both (both zones from the same c).

## 3. What is proved, and what is not
- PROVED (lane) partial correctness: a potential changes no cycle weight, so no winner (also SOURCE Theorem 3, item 1). In T+ Even
  keeps edges of c ≥ 0 inside T+, Odd's vertices of T+ have all their edges inside T+ with c ≥ 0 (a vertex never made final has no
  exit and only non-final targets), so every play stays in T+ and every cycle has weight ≥ 0, hence > 0 (no zero cycle: |cycle
  weight| ≥ B^p − (n − 1)B^(p−1) > 0): T+ is an Even dominion of G[X] with that strategy; dually T−. Removing the Even-attractor of an
  Even dominion, then the Odd-attractor of an Odd dominion of the rest, preserves the winners of the remaining subgame (the usual
  Zielonka argument: Odd vertices left have no edge into the removed Odd part, Even vertices left none into the removed Even part).
  So if the loop ends, regions and strategies are correct.
- PROVED (lane): g+ > 0 on P* and g− > 0 on N* (induction along the zero-edge attractor that defines the zone; no zero cycle), so
  every jump changes φ on a non-empty zone. PROVED: a P*-jump alone is positively safe in SOURCE's sense (0 ≤ g+ ≤ En+ of the
  current game: Max realises the sum), an N*-jump negatively safe. The sum over both kinds is NOT known to be safe.
- Cost of one jump: O(m) arithmetic operations plus O(m log n) heap steps. Bits (PROVED, coarse): each jump multiplies the largest
  |c| by at most 2n + 1, so potentials have at most wbits + jumps·⌈log2(2n + 1)⌉ bits; DATA: maxbits ≤ wbits on the 634 family runs and
  ≤ wbits + 4 on the 10,000 random games (columns maxbits, wbits).
- NOT KNOWN: termination of alt+ / alt−; any bound on jumps. DATA against a naive hope: mode «both» oscillates (cap of 20,000 jumps
  hit on 100 of 200 random games in check_n13.out; 730 of 1,500 in a scratch run), so the alternation is what makes the runs end. CONJECTURE (weak, data only): the alternation
  always terminates, with polynomially many jumps. The one-sided modes are sums of positively safe potentials (SOURCE Lemma 4), which
  bounds them pseudo-polynomially on Odd's region; they are slower (below).

## 4. Measurements (DATA; experiments/new/n13/out, pinned by out/SHA1SUMS)
- Gauntlet step 2, random part (out/g10k_altp.txt): harness corpus `gen.py corpus DIR 10000 20261114 --nmax 200` (sha1 of the
  concatenated sorted files d0b2ec69aea0a09ddd09127ac478ff86bc7f7f09): 10,000 of 10,000 OK (regions = Oink --uzlk, both strategies
  pass harness verify.py), 5,434 jumps in total, at most 10 (n = 187).
- Zoo (out/zoo_*.txt): every .pg under experiments/ at b4a9ae47 (2,844 files, one unparsable: experiments/red/r182/out/d5.pg):
  regions = Oink --tl on 2,843 of 2,843 in all four modes; alt+ 3,876 jumps in total, at most 15 (red/tcpert/instances/tcR4_N8.pg);
  alt− at most 18; plus at most 83 (new/box52/out/topfix_n12.pg; alt+ needs 4 there); minus at most 59.
- Families (out/tables13.txt, out/summary13.txt; 634 runs, all ended, maxbits ≤ wbits), jumps in mode alt+:
  tc_N: N + 1 (N = 1..12, 16, …, 32); tc+_N (n = Θ(N³)): 1, 3, 4, 8, 9, 14, 19, 21, 27, 33, 36, 43, 54, 70, 84, 99, 137 for N = 1..12,
  14, 16, 18, 20, 24; counter_symsi_N: 4, then 8 for N = 2..32; counter_rob, counter_core: 2; counter_dp, counter_rr: ≤ 3;
  counter_qpt, recursiveladder: 1; counter_m, counter_ortl, switchallexp, switchbestexp: 0 (peeling alone); Γ3(G_k) k = 3..13,
  W_2..8, F_2..8, WL_1..4: 2; N12's killers symsi_u50T0, symsi_T0, symsi_D, symsi_u50, symsi_Y1: 8 each.
  alt−: the same on tc, tc+; 7 on counter_symsi. plus / minus: tc 2N + 1, tc+ 2N, counter_symsi about 1.8N (58 at N = 32).
- Plain GKK on the same weights (gkk_plain.py): tc 4, 19, 52, 139, 388, 1123, 3316, 9883, 29572; tc+ 2, 15, 44, 121, 342, 995, 2944,
  8781, 26282 (N = 1..9); counter_symsi 11, 28, 52, 94, 172, 322, 616, 1198, 2356, 4666, 9280, 18502 (N = 1..12). Dead, as L1 predicts.
- Exhaustive (scratch, not pinned): n = 2 priorities 0..3 (576 games), n = 3 priorities 0..2 (74,088 games): 0 wrong, all end, ≤ 2
  jumps. Random with Zielonka + verify.py: 1,500 games, 0 failures in alt+, alt−, plus, minus (rtest13.py).
- My own climbs for jumps (climb13.py, 150,000-200,000 evaluations; instances in inst/): 6, 9, 13, 15, 20 jumps at n = 6, 8, 10, 12,
  18. So jumps > n is reachable; the growth seen is about linear.

## 5. Barrier notes (first statement; READING)
- Friedmann-type counters: no strategy is improved; switchallexp / switchbestexp are solved by peeling at φ = 0 (they have an
  even-only dominion). That says nothing about padded versions without such a dominion: UNTESTED.
- van Dijk's two counters: tc N + 1, tc+ about N²/4.4 jumps. Universal trees / universal graphs: no fixed value domain is walked
  step by step (each jump goes to the next exit event); the bound on the size of a value domain does not bound jumps. To be checked
  by L-LIT, as is the relation to ESL / AESL and to Schewe's improvement step (T27 says ESL is that step; then Friedmann's bound for
  it concerns the one-sided mode, not the alternation).
- Lane lesson L1 (a single trajectory of potentials is lapped by a counter) applies in principle: N13 is one trajectory. The delay-lane
  counters built against N8 (in the zoo) need ≤ 15 jumps.

## 6. My own kill guesses (ranked)
1. NON-TERMINATION: a cycle of the alternation. «both» cycles; alt may cycle on a game where the two zones undo each other with a
   period > 2. Tests not yet run: exhaustive n = 4; arbitrary small integer weights (the step is a mean-payoff algorithm; if it
   cycles there, find what parity weights prevent); potentials compared modulo constants for repetition.
2. LONG RUNS: a tower of zones in which each jump releases one layer and the next jump of the other zone re-closes it; the climbs'
   traces show many jumps of a zone of one vertex. Pseudo-polynomial creeping looks unlikely (a pump is a positive cycle and is
   peeled), but that is a READING, not a proof.
3. Who starts: alt+ and alt− differ (15 against 18 on tcR4_N8); an adversary may use the asymmetry.

## 7. Not done (stopped by the usage limit; for successor 79)
The non-termination hunt of §6.1; L-COMP's battery (claude/l-comp 1eddbb56) on the engine; a second implementation; larger tc+.
