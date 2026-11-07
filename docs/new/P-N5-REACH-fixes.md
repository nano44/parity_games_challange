# P-N5-REACH fixes (append-only; the frozen packet b7bd6937 and line L-1 b12ec57a are never edited)
L-NEW. Each entry quotes the referee item, gives the reply and says where the change lands (packet reading here; line text in a revision
file P-N5-REACH-line-L<k>.txt). Where an entry and the frozen packet differ, the entry governs.

## Entry 1 (2026-11-07 from 03:4xZ by date -u; L-NEW successor 58; Lead relay 03:29Z of fix round 1)
- Sources: REFEREE docs/referee/R-P-N5-REACH.md at claude/referee f66942c1; REFEREE-2 docs/referee-2/R2-P-N5-REACH.md at
  claude/referee-2 b0860fcd. Verdicts: both SIGN every statement (§2-§9), no gap; the line needs RE-L1 (REFEREE) and W-1, W-2
  (REFEREE-2). No statement, proof, tool, output or instance of the packet changes. This entry carries no proof.
- RE-L1 (REFEREE, required, DATA coverage; ACCEPTED). Each count was checked against reachcheck.py's counter code (unit, set, scope)
  before applying:
  - «the β-free P-sets of NO-REACH 0 on 42,880 (state, vertex) pairs»: counter NR-BETA over NR-PAIRS (gamma_counts), unit = (state,
    vertex) with v ∉ {K2, K3, c_X}, set = every state of the N5 runs from S3 on Γ(G) for C14 + R440; NR-BETA also counts a cycle node
    ranked at or below a β, i.e. it checks all of §2 (d). reachcheck.out: «(state, vertex) pairs 42880: beta-in-P-or-low-cycle-node 0». MATCH.
  - «S3-START 0 on 454 genomes»: counter S3-START over S3-GENOMES, unit = genomes, set = C14 + R440. «S3-START genomes 454: S3 !=
    stated start 0». MATCH.
  - «PAD 0 on 693,030 (state, vertex, world) triples of the S3 runs on Γ3»: counter PAD over PAD-PAIRS, unit = (state of the Γ3 S3 run,
    vertex ≠ c_X, world ∈ {Ξσ, Ξτ}), set = C14 + R440. «PAD (state, vertex, world) triples 693030: pad-in-P-or-cycle-node-Om<3 0». MATCH.
  - «both DEAD SUBDIV instances re-run»: the two «SUBDIV-DEAD instance A / B» lines. MATCH.
  - «Corollary REAL-IDEAL-S3 no separate DATA»: packet §10 no-DATA list («§8 (a), (b) (reduction, no data)»). MATCH.
- W-1 (REFEREE-2, required; ACCEPTED). The quoted words «S3 can be simulated on every game by subdividing every edge» are not in the
  packet; §9 kills a specific statement. The replacement text is REFEREE-2's verbatim. REFEREE-2 gives the new text ending «is DEAD» but
  not the exact old span; the old span used is the shortest one that the new text replaces, «the statement «S3 can be simulated on every
  game by subdividing every edge» is DEAD» (occurs once in L-1). The words after it («as stated (DEAD SUBDIV: …») are unchanged.
- W-2 (REFEREE-2, required; ACCEPTED). «c_X» is not defined in R104's line; REFEREE-2's replacement is applied verbatim.
- Notes (no line change, no packet edit):
  - REFEREE-2 N-1 (K3 labelled «every genome» while (b) cites SBAR3, which is IDEAL-ACYC): ACCEPTED as REFEREE-2 states it. For every
    genome K3 holds anyway: K is closed, so K's values depend only on the strategies on K, and Odd's unique best at K2 is r. REACH3 uses K3
    only under IDEAL-ACYC.
  - REFEREE-2 N-2 (c_X undefined): ACCEPTED; c_X is R104 packet §3.1's name for «an unused even self-loop of priority 2» (the line now
    says so, W-2). In the packet, read c_X with that meaning.
  - REFEREE-2 N-3 (§13's bound top + 3 ≤ 4M + 9 assumes β-ranks 0..M − 1): ACCEPTED. R104's genomes have «a distinct β-rank», and
    box189/norm.py relabels the L-LOWER genomes order-preservingly to 0..M − 1; the IDEAL run depends only on the rank order. Not signed.
  - REFEREE-2 N-4 ([RULE] at transition L + 1, σ_new before S4c): ACCEPTED; used as R104 used it (P-N5-REALIZE fixes entry 1, G-REAL-1).
  - REFEREE-2 D-1 (NR-LAM checks only the cycle node of Ξσ(K0), not the full value (K0, ∅, 0)): ACCEPTED as wording. The packet §10
    clause names the counter «cycle-node(K0)!=K0», which is what it checks; the full value is proved in §2, not counted.
- Line L-2 (docs/new/P-N5-REACH-line-L2.txt, sha1 4de27b32d5ed11accb092cf44cb27e14be6b9609, 1 line with its newline, 3,628 bytes,
  57 «(» = 57 «)», depth never negative, 0 «|»): L-2 = L-1 (b12ec57aa18893701bd88bfdab75e3f7e9cf80e0) with exactly these three replacements, applied by script; each old
  string occurs exactly once in L-1; no other byte changes; L-2 contains no «c_X»:
  - RE-L1: «0 failures of REACH3 in 454 genomes,» → «0 failures of REACH3 in 454 genomes, the β-free P-sets of NO-REACH 0 on 42,880
    (state, vertex) pairs, S3-START 0 on 454 genomes, PAD 0 on 693,030 (state, vertex, world) triples of the S3 runs on Γ3, both DEAD
    SUBDIV instances re-run, Corollary REAL-IDEAL-S3 no separate DATA,»
  - W-1: «the statement «S3 can be simulated on every game by subdividing every edge» is DEAD» → «the statement that, for every game and
    start pair, the game with every priority + 4 and every edge subdivided by an Even pad of priority 2 (Even, start edge), 1 (Odd, start
    edge) or 0 has an N5 run from S3 equal state for state and transition for transition (fallbacks included) to the run of the game from
    that start pair is DEAD»
  - W-2: «outside {K2, K3, c_X}» → «outside K2, K3 and the unused even self-loop of priority 2»
- Pins: experiments/new/box189/reach.pins gains this file and L-2; check.sh block «P-N5-REACH» pins reach.pins' new sha1.
