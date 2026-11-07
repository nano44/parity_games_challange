# P-M2D-DEAD fixes (append-only; the packet docs/lower/P-M2D-DEAD.md stays frozen at 87fcdf73)

## Fixes entry 1 (2026-11-07, L-LOWER successor 3; fix round 1)
Reports answered: REFEREE claude/referee c011995c, docs/referee/R-P-M2D-DEAD.md (signed DEAD; L-1 NOT YET: PM-L1..PM-L4);
REFEREE-2 claude/referee-2 6eba8b93, docs/referee-2/R2-P-M2D-DEAD.md (signed DEAD; L-1 MATCHES after W-1; optional N-1, N-2).
Line files (made by script experiments/lower/l3/mkL2.py; each old string occurs exactly once in L-1, checked by an assert):
- docs/lower/P-M2D-DEAD-line-L1.txt: §6 of the frozen packet, its lines joined by single spaces, plus «\n».
- docs/lower/P-M2D-DEAD-line-L2.txt: L-1 with the four replacements below, plus «\n». Both pinned (sha1) in experiments/lower/l3/p_m2d_check.py.
Replacements (old → new):
- PM-L1 (REFEREE, exact string): «obstruction: a metronome reading a key order that flips at every step, fed by laps» → «obstruction (a
  description, no separate DATA): a metronome reading the key order of the pair one level below it, which flips at steps 2-13 (d 6)
  and 1-13, 17-24 (d 8), fed by laps». (My own check agrees: pair (6, 7) in d 6 changes at steps 2-13; pair (12, 13) in d 8 at 1-13,
  17-24.)
- PM-L2 (REFEREE): «(sha1 d96c2b36…; 𝓛^R_8;» → «(sha1 d96c2b36…; 𝓛^R_8, Ξ-acyclic, not ISO;».
- PM-L3 (REFEREE, exact string): «movescheck counters 0)» → «movescheck counters 0 on both stored-start runs and on all 4,096 starts of
  the d 6 genome)».
- PM-L4 (REFEREE) + W-1 (REFEREE-2), merged into ONE replacement (Lead 02:58Z): «and independently by L-NEW box 188 (6d043927) and L-SI
  41;» → «and independently by L-NEW box 188 (6d043927), L-SI 41 (0803d551, docs/si/N5-TROPICAL-box76.md) and L-RED 52 (55557951,
  experiments/red/r214/lower3/), and by both referees' own simulators;».
Sources opened for PM-L4 / W-1 (by me, this entry):
- claude/l-si 0803d551, docs/si/N5-TROPICAL-box76.md l. 167-170: «REPLAY (DATA, independent). L-LOWER 3's nine genomes claude/l-lower
  4d747490 experiments/lower/l3/kill/*.json … replayed from the stored start by my simulator and by L-NEW's box150 Gen (identical
  states; replay77.py with XCHK). Every (d, T, mover, moves) of the README table is reproduced (replay77.out)».
- claude/l-red 55557951 (commit message «L-RED R214: replay of L-LOWER 3 candidate kills (4d747490): memb.py, lowrep.py, renum.py;
  ideal.py / fa / lemck / box150 reproduce all 9»): experiments/red/r214/lower3/ (byte copies of the nine genomes, renumbered copies
  rn/), experiments/red/r214/memb.py («membership … condition by condition, written from the RESULTS R104 / R110 text (no other lane's
  code)»), lowrep.py (replay «from its STORED start with r187/ideal.py»). The per-genome replay output of lowrep.py is not a committed
  file at 55557951; the 9/9 verdict is the commit message's and the Lead's (02:53Z).
- L-NEW box 188 6d043927 was opened before (packet §5).
Optional items taken (wording notes only; the frozen packet is not edited, and L-2 is unchanged by them):
- N-1 (REFEREE-2): the quoted wording «on 𝓛^R_d every z ∈ Z moves at most 2d times in every run» is P-IDEAL-MOVES §0's; box 181 first
  phrased it «on 𝓛^R_d, every mover that is the Ξ-target of some option moves at most 2d times» (same set, same unit). Read L-1's
  attribution as «(as worded in P-IDEAL-MOVES §0; box 181 first)».
- N-2 (REFEREE-2): in §7, «at d 3 it holds with room (μ(3) = 4 …), at d 4 it holds (L-RED R213, one solver)» is lane DATA (L-RED R213,
  unlanded, one solver), not a claim of this packet.

## Entry 2 (fix round 2; L-LOWER successor 4, 2026-11-07 ~04:4xZ by date -u)
Items: REFEREE PM-C1 (claude/referee 008039cc, docs/referee/R-P-M2D-DEAD.md §C) and REFEREE-2 W-1′ (claude/referee-2 5c8aea53,
docs/referee-2/R2-P-M2D-DEAD.md Addendum 1). Both target the L-RED 52 citation of L-2 and both allow citing a committed output file
instead. L-RED has committed it; both items are RESOLVED by citing it (one replacement, wording fixed by the Lead 03:55Z). L-RED's
replay code stays at 55557951 (experiments/red/r214/lowrep.py, memb.py). The frozen packet is not edited.
Line file (script experiments/lower/l3/mkL3.py from L-2 8ca7bcca…; the old string occurs exactly once in L-2, checked by an assert):
- docs/lower/P-M2D-DEAD-line-L3.txt: L-2 with the replacement below, plus «\n»; pinned in experiments/lower/l3/p_m2d_check.py.
Replacement (old → new):
- PM-C1 + W-1′: «L-RED 52 (55557951, experiments/red/r214/lower3/)» → «L-RED 52 (6e743ab1, experiments/red/r214/lower3/replay.out)».
Source opened for this entry: claude/l-red 6e743ab1 (on origin; branch head 41e50e10 at reading),
experiments/red/r214/lower3/replay.out, 7,591 B, sha1 4492ee284db25cb8cefc9702c1a343352e4b4ab3: nine distinct genomes, each line
«… moves N 2d M >2d», among them «KILL_M2D_d6_mu13.json: d 6 T 13 … max mover 8 lev 4 Xi-target 1 moves 13 2d 12 >2d» and
«KILL_M2D_d8_mu21.json: d 8 T 24 … max mover 15 lev 7 Xi-target 1 moves 21 2d 16 >2d», box150 XSIM 0 on each (9/9).
