# R51: the per-search piece map of nest6min_n75, the gate / return roles, and a hand-built fourth part (box 19; L-RED successor 11; produced on Fable 5.1)
Status: DATA plus readings, unrefereed. Started 2026-10-22 05:34Z (date -u) on the Lead's GO (box 19, option (a) of notes/L-RED.md NEXT).
Object and tools as in R49 / R50: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, both order data. Chains come from L-ALG's
unmodified b12_pot / b12_core (through ../xctx/xscore.py). New tools (experiments/red/nest16/): piecemap.py (the map), gatescan.py
(hand-built gate / return configurations on BASE ⊎ E). Maps are committed in experiments/red/nest16/maps/.

## 0. A trap in the earlier tools: solver indices
- fixd_stealentry.run renumbers the vertices by priority before solving (stable order: sorted by (priority, v); oink order:
  stdsort.oink_order). Every vertex set the solver reports (depth-0 pieces, tangle vertices, escapes) is in SOLVER indices.
  ../xctx/tlog.py and partmask.py print those indices unmapped, so their vertex ids and their A/B/C part letters are not file ids.
- piecemap.py maps every set back to file ids (idx[i]) before labelling. The D-vs-nest5 statements of R50 are unaffected (D is the
  top priority band, so its solver indices coincide with its file range up to the two D vertices moved into nest5's band, 50 and 73),
  but any R50 reading that rests on partmask's A / B / C letters (§4, §7) should be re-read against the maps here. The P sequences,
  NEST* values and the table rows do not depend on vertex ids and stand.
- distinct() (fixd_ctx1p) only re-spaces priorities; it does not renumber. Part labels here: A = 0-25 (near4), B = 26-45
  (chainfail), C = 46-48 (climb-added), D = 49-74 (the oseg copy; oseg vertex i is D vertex 49 + i).

## 1. The map of nest6min_n75 (sha1 e2c0d57f0b29e379a33dbcd9cc4f30fb28736563; maps/nest6min_map_min_{oink,stable}.txt)
- Both orders give the same P = 0,1,6,9,7,4,9,3,8,16,17,17,16,1,8,7,16,14,1,13,13,7,0,6 (S 25, |P| 24, I 0), NEST* 6, witness
  (witness.py) 0 (0, 22) ⊃ 1 (1, 18) ⊃ 7 (4, 15) ⊃ 8 (8, 14) ⊃ 16 (9, 12) ⊃ 17 (10, 11). The maps differ between the orders only in
  the vertex order inside pieces. (R50 §8b's last P line, "…,15,13,1,12,12,…", differs from the committed file's at indices 16, 17, 19,
  20; the committed sha1 is the reference. NEST* 6 either way.)
- Chain shape per search (position:parts rank; S = stable, a number = the emptying round of a −1 piece; from the maps):
  - s0-s7: 14-20 positions. nest5's pieces (A, B, C, mixed) occupy positions 0-11; D's pieces occupy the tail (s2: 13D2 14D5 15D4 16D3
    17D2 18DS). Transitions #0-#7 are nest5's: 0, 1, 6, 9, 7, 4, 9, 3.
  - #8 (s8 → s9) at position 8, type G: A[12] rank 3 → AB[2,3,9,10,12,13,19,36] rank 3 (search 8 learned at position 9 the tangles
    A[3,10,13,19] and A[2,3,9,10,13,19]). This opens the 8-window. From s8 the chain has 21 positions: nest5's stable piece at 9,
    then a DESCENDING −1 LADDER of A pieces at 10-14 (ranks 8, 7, 6, 5, 4), a mixed piece AD rank 3 at 15 (it holds the gate source
    23 together with D vertices), and D at 16-20: s9 = 15D2 16D5 17D4 18D3 19DS.
  - The block (#9-#12), all inside D: #9 at 16, O: D[49] rank 5 → D[50] rank 6. #10 at 17, G: D[61] rank 5 → D[51,52,58,59,61,68]
    (search 10 learned D[51,52,58,59,68] at position 18). #11 at 17, G: + 49 (search 11 learned D[49] at 18). #12 at 16, O: D[50]
    rank 6 → the stable D piece {49,50,51,52,53,55,56,57,58,59,61,64,65,67,68,69,70,71,72,73} (search 12 learned at 18 the tangles
    D[55,72] and D[55,57,65,67,71,72] with escapes into B: 27, through the return edge 55→27).
  - #13 (s13 → s14) at position 1, O: the mixed piece ABCD[14,37,40,47,60,62] gains D's 63, 65, 67. Search 13 learned at position
    16 the stable D tangle with escapes ABD[15, 27, 54, 60, 62, 63, 66, 74]: 15 and 27 are exactly the two return edges' targets.
  - After #13 the chain is re-indexed: D moves to the HEAD (s14: 4D5 5D5 6D5 7D9 8D8 9D7 10D6, a second descending ladder) and
    nest5's pieces move to the tail (11-18). #14 at 8, O: D[51,58] rank 8 → D[51,58,72]; #15 at 7, O: D[49] rank 9 → rank 10.
    These two transitions are the "levels 8 and 7 rise once more" of R50 §8b: the SAME POSITIONS, held now by D pieces. Then #16 at
    16 (A[12] → ABC), #17 at 14 (D[61] → the stable ABCD piece), #18 at 1, #19/#20 at 13, #21 at 7 (D[49] rank 10 → stable),
    #22 at 0, #23 at 6.
- Where the five named vertices sit (oink; file ids): 23 is in the mixed ABD piece at positions 5-8 (rank 2-3) in s0-s7 together
  with D's 49 and 50, in AD rank 3 at 14/15 in s8-s13, and in A / mixed pieces at 14-17 afterwards. 73 (priority 55) is in D's tail
  pieces (rank 1-3 or stable) up to s13 and at 12-13 (rank 4-5) after. 55 and 64 are in D's stable tail piece in s7-s13. 27 is in
  the mixed AB / ABC piece at 2-5 (rank 4-5) up to s13 and at 10-11 after. 15 is in A's stable piece (position 10-11) in s2-s7 and in
  the ladder piece A rank 6 at 11-12 in s8-s13.

## 2. The roles of the gate and the two return edges (variants of nest6min; maps/nest6min_map_v_*.txt; oink order)
Variants are nest6min with edges removed and 73 restored to priority 97 (= oseg priority 17 + 80, the band's shift). Note: vertex 50
(oseg 1) carries priority 46 in nest6min (inside nest5's band), so the committed seed is not a plain 'above' placement either; the
seed variant below reproduces R50 §8b's seed P exactly, so 50's priority was part of that seed.
| variant | S | P | NEST* | witness |
| --- | --- | --- | --- | --- |
| seed (no edges, 73 at 97) | 20 | 0,1,6,9,7,4,9,3,8,4,6,7,6,1,6,8,4,0,3 | 5 | 0 (0,17) ⊃ 1 (1,13) ⊃ 6 (2,12) ⊃ 7 (4,11) ⊃ {6, 8} |
| gate only (73 → 55, 23→73) | 25 | 0,1,6,9,7,4,9,3,8,16,17,17,16,1,6,9,10,9,1,8,8,7,0,6 | 5 | 0 ⊃ 1 (1,18) ⊃ 6 (2,14) ⊃ 16 (9,12) ⊃ 17 (10,11) |
| gate + 55→27 | 25 | 0,1,6,9,7,4,9,3,8,16,17,17,16,1,7,19,20,19,1,18,18,7,0,6 | 5 | 0 ⊃ 1 ⊃ 7 (4,14) ⊃ 16 ⊃ 17 |
| gate + 64→15 | 25 | 0,1,6,9,7,4,9,3,8,16,17,17,16,1,12,7,18,16,1,15,15,7,0,6 | 5 | 0 ⊃ 1 ⊃ 7 (4,15) ⊃ 16 ⊃ 17 |
| three edges, no move | 23 | 0,1,6,9,14,14,12,3,7,13,14,14,13,1,8,7,16,14,1,12,7,1,6 | 4 | |
| all (= nest6min) | 25 | 0,1,6,9,7,4,9,3,8,16,17,17,16,1,8,7,16,14,1,13,13,7,0,6 | 6 | 0 ⊃ 1 ⊃ 7 (4,15) ⊃ 8 (8,14) ⊃ 16 ⊃ 17 |
- Seed: D sits at the tail (s8: 10D3 11D2 12D5 13D4 14D3 15DS) and makes no first change until it moves to the head after #13 (s14:
  4D6 5D6 6D6 7DS); its transitions then fall at 6 (#14) and 4 (#16), shallower than nest5's innermost 7 / 8. No D block.
- GATE (the edge 23→73 plus 73 into nest5's band): from s8 the chain gains the A rank ladder (positions 10-14, ranks 8..4) and the
  mixed AD piece at 15, which pushes D's pieces to 16-20 and makes D's transitions the first change of searches 9-12: the block
  16,17,17,16 at indices 9-12, deeper than nest5's 8 and inside the 8-window that #8 opened. S grows 20 → 25. (The priority move alone
  changes nothing, R50 §8b; the three edges without it give a block at 13/14 but lose the 7/8 structure, NEST* 4.) But with the gate
  alone the re-indexing after #13 is the seed's: nest5's levels 6, 9, 10, 9 fire at #14-#17 and 8 and 7 close only at #19-#21,
  OUTSIDE 1's window (1, 18). So 8 is lost from the witness and NEST* stays 5.
- RETURN edges (55→27 and 64→15, D's C-vertices escaping into B and A): they shape D's head ladder after #13. With both, s14 =
  4D5 5D5 6D5 7D9 8D8 9D7 10D6 and the pieces at positions 8 and 7 (D[51,58] rank 8, D[49] rank 9) are the first to change at #14 and
  #15, i.e. right after the block and inside 1's window: this closes 8 and 7 around the block. With 55→27 alone the head ladder is
  13 D pieces long (s14: 7D14 … 16D6), 7 recurs at #14 but 8 never does; with 64→15 alone it is 9 long (7D11 … 12D6), #14 falls at 12
  and 7 recurs at #15, 8 never. Each return edge alone therefore gives NEST* 5.
- Reading. The nesting is by POSITION, not by piece: level 8 opens as nest5's A[12] piece and closes as D's [51,58] piece at the
  same position. The gate's job is to put the new part's block deeper than, and during, the old innermost window; the returns' job
  is to re-index the chain after the block so that pieces with rising −1 ranks sit exactly at the old levels' positions. Both are
  statements about the chain's re-indexing, not about named vertices; this is why index mirroring (R50 §5) fails.

## 3. A fourth part by hand: GATE + RETURN on nest6min_n75 ⊎ oseg_n26 (box 19; oink order unless stated; gatescan.py; scans/ files)
Seed k4u_n101 = nest6min_n75 ⊎ oseg_n26 placed above (pairunion 'above'; the copy E is vertices 75-100, oseg vertex i ↦ 75 + i; sha1
37a45ff8a932bcc6e4a79d4848a0a57dbb82367a, n 101, 𝒞^1P with C = 1). The analogs of the k = 3 roles: gate target 73 ↦ 99, 71 ↦ 97,
50 ↦ 76; return sources 55 ↦ 81, 64 ↦ 90.
- 3a. The plain union (both orders identical): S 25, |P| 24, I 0, P = 0,1,6,9,7,4,9,3,8,16,18,18,16,1,9,7,19,17,1,16,16,7,0,6,
  NEST* 6, witness 0 (0,22) ⊃ 1 (1,18) ⊃ 7 (4,15) ⊃ 9 (6,14) ⊃ 16 (9,12) ⊃ 18 (10,11). Map: maps/union_nest6min_oseg_above_oink.txt.
  - The union already does the gate's job by itself: from s8 the chain has the A ladder at 10-14, ADE rank 3 at 14/15, D at 15,
    then E and D INTERLEAVED at 16-23 (s9: 15D2 16E5 17DE5 18DE4 19D3 20DS 21E3 22ES). The block is #9 at 16, O: E[92] rank 5 → 6;
    #10, #11 at 18, G: D[61] absorbs D[51,52,58,59,68] and D[49] (D's old 17-pair, one position deeper); #12 at 16, O: E[92] → D's
    stable piece. So E's −1 piece {92} at 16 holds the window and D's pair sits INSIDE it: a two-part block 16 (E) ⊃ 18 (D).
  - What is lost: nest5's level 8 (A[12] at #8) no longer re-closes; the union's sixth level is 9 (6, 14) instead. After #13 the
    head is 4D5 5D5 6D5 7E9 8E9 9E9 10ES 11D9 12D8 13D7 14D6 (s14): E's three rank-9 pieces at 7-9 and D's ladder at 11-14. #14 at 9
    (E[92] G) and #15 at 7 (E[100] rank 9 → 10) re-close 9 and 7; position 8 (E rank 9) never changes first.
  - NEST* 6 = the k = 3 value: the fourth part adds a level at the bottom (16 ⊃ 18) and removes one in the middle (8).
- 3b. Gate scan (scans/scan1_gate_oink.txt; 84 configurations = source u ∈ {49, 50, 51, 52, 58, 59, 68} (the D C-vertices of the
  pieces holding the innermost window, positions 16-17 in s9-s12) × target g ∈ {99, 97, 76} × g's priority ∈ {81, 97, 113, 57}):
  - The priority slot never matters: all four slots give the same P for every (u, g) (84 configs, 21 distinct P).
  - g = 97 or 76 (the analogs of 71 and 50, both on even self-loops): the phase collapses, S 10 or 7, NEST* 1, in all 56 configs.
  - g = 99 (the analog of 73): u ∈ {50, 52, 59, 68} give S 25, NEST* 5 with P = 0,1,6,9,7,4,9,3,8,17,18,18,17,1,7,10,19,17,1,16,16,
    10,0,9 (u = 59: …,16,16,7,0,9); u = 49: S 23, NEST* 4; u ∈ {51, 58}: S 24, NEST* 4. Map of u = 50: maps/union_gate50to99_oink.txt,
    instance instances/k4g50_n101.pg (sha1 62cbc3e8b5e11c856a37c13e41eb2f78031aa004).
  - Mechanism (u = 50): the gate puts E's pieces in front of D's at the tail (s9: 16E5 17DE5 18DE4 19E3 20ES 21D4 22D3 23DS) and the
    block becomes E's own: #9 at 17 (DE[49,75] → E[76]), #10/#11 at 18 (E[87] absorbs E tangles), #12 at 17 (E → E stable). D's
    pair is gone from P (D[61]'s changes are no longer the first change of their searches). So a gate from the innermost pieces into
    the new part REPLACES the old block by the new part's block; it does not nest the new block inside the old one. NEST* 5 < 6.
- 3c. Returns on top of that gate (scans/scan2_returns_on_gate_oink.txt; 50 configurations: 81→t and 90→t for t ∈ {27, 15, 49, 50, 61,
  73, 12, 23, 34, 39}, the 25 pairs (81→t1, 90→t2) over {27, 15, 49, 50, 73}, gates 23→{99, 97, 76}, and two mixed configs): NEST* 5
  in 17, 4 in 31, 2 in 2; never 6. The return edges only re-index the tail after #13 (e.g. …,1,7,16,25,23,1,22,22,10,0,9 for
  81→27); the block stays 17,18,18,17 and level 8 never recurs. Gate 23→99 alone (the k = 3 gate source into the copy): the union's
  block 16,18,18,16 survives but the tail becomes 1,9,10,19,17,1,16,16,10,0,9: NEST* 5.
- 3d. Return edges on the plain union (scans/scan3_returns_on_union_oink.txt; 126 configurations = 81→t and 90→t for every
  C-vertex t of nest6min_n75, 63 targets): NEST* 6 in 26 (P unchanged), NEST* 5 in 100. ALL 126 keep S = 25 and the IDENTICAL
  prefix P[0..13] = 0,1,6,9,7,4,9,3,8,16,18,18,16,1; every one has #15 at 7; they differ only in #14 (position 9 in the 26
  unchanged cases, else 10, 12-22) and in the three transitions #16, #17, #19/#20 of the tail. So a return edge re-indexes the chain
  after #13 and nothing else; it never adds a search and never touches the block or what precedes it.
- 3e. Pairs and the full mirror (scans/scan4_pairs_oink.txt): (81→27, 90→15), (81→15, 90→15), (81→0, 90→0), (81→49, 90→49) and the
  triple (81→27, 90→15, 81→15): S 25, NEST* 5, same prefix, #14 at 10, 11 or 19. The literal mirror of the k = 3 step onto the union
  (23→99 with 99 at priority 81 or 99, 81→27, 90→15): S 25, NEST* 4 (both slots); into the previous copy (81→53, 90→64): NEST* 4.
  This agrees with R50 §5 on nest6_n75 ⊎ oseg.
- 3f. Oink check of the union (scans/kcheck_k4u_n101.txt; instances/k4u_n101.pg): stable and oink P identical (above), FIT=pool
  score (6, 116, 25, −101); pinned Oink 8fbf0a7 -v: even iterations 25 = S, odd 1, 2 dominions, 71 tangles, solution verified (87
  strategies). k = 4, n 101, S 25, |P| 24, I 0, NEST* 6: not a class-best raise (nest6_n75 has NEST* 6 at n 75); S/n = 0.25.

## 4. The obstruction (reading of §1-§3; DATA, not a proof)
Why the innermost window of the k = 3 structure cannot host a gate for a fourth part, with the instances:
- (i) The gate's effect is to put the new part's block deeper than, and during, the old innermost open window. On nest6min ⊎ oseg
  the plain union does this already: E's −1 piece {92} occupies position 16 in s9-s12 and D's 17-pair moves to 18 inside it
  (k4u_n101, §3a). The union's bottom is therefore a two-part nesting 16 (E) ⊃ 18 (D), one level deeper than nest6min's 16 ⊃ 17 at
  the same depth count, because D's own window (16, formerly) is now E's. The new part takes over the old innermost window instead of
  opening a new one below it. NEST* stays 6.
- (ii) A gate edge from the pieces that hold the innermost window (D's 49, 50, 51, 52, 58, 59, 68) into the new part does not nest
  either: it reorders the tail so that E's pieces precede D's and the block becomes E's alone (k4g50_n101: 17,18,18,17 all E; D's
  pair leaves P because D's changes stop being the first change of their searches, the masking of R50 §3). NEST* 5 (§3b). Gates into
  the copy's vertices with even self-loops (97, 76) collapse the phase to S 7-10 (§3b): a C-vertex given a successor that player 0
  can cycle on forever cannot be attracted until that successor is, which breaks the old part's own order of consumption.
- (iii) The closing side is fixed by the phase's length. After the block, every variant with the union's prefix (126 single returns,
  5 pairs, 3 mirrors) has exactly two transitions before 7 closes: #14 and #15 = 7, and S = 25 throughout. A seventh level needs two
  positions strictly between 9 and 16 that each change first once before the block and once after it; before the block the only
  free indices are 7 and 8, which carry nest5's own 3 and 8 (the transition #8 that builds the ladder), and after the block there is a
  single free index (#14). Return edges move #14's position (9, 10, 12-22 observed) but never add a search (§3d, §3e). So on this
  seed no choice of return edges can produce the extra level; what is missing is a LENGTHENING of the post-block tail, which in the
  k = 3 step came from the gate (S 20 → 25, the A ladder) and not from the returns.
- (iv) What the gate did at k = 3 that it cannot repeat at k = 4: at k = 3 the gate source 23 lay in the OLD structure's innermost
  −1 pieces (the mixed ABD piece at positions 5-8 with D's 49 and 50) and the gate created a new descending ladder (positions 10-14,
  ranks 8..4) in the old part, in front of the new part's block. At k = 4 the analogous sources (the D pieces at 16-17) are already
  at the tail, in front of nothing but E: there is no old material behind them to form a ladder, so the gate can only reorder E and D
  (§3b). Gates from the A ladder's own C-vertices (§3g) are the remaining source class.
- Instance that kills the recipe: k4u_n101 (sha1 37a45ff8…) with the 84 + 50 + 126 + 8 configurations of scans 1-4 (scans/), all
  NEST* ≤ 6, all with the union's prefix or a collapsed phase. It does not refute a gate-recipe in general: a different fourth part,
  or a gate that lengthens the post-block tail, is untested here (see §5).
