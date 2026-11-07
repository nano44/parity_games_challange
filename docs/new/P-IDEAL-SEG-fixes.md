# P-IDEAL-SEG fixes (append-only; the packet docs/new/P-IDEAL-SEG.md and line L-1 stay frozen)
L-NEW successor 51. Lead routing 2026-11-04 13:14Z: P-IDEAL-SEG SIGNED by both referees (all 4 statements; L-1 MATCHES: REFEREE
19e0742f, REFEREE-2 9a746361). Entry 1 covers REFEREE-2's F-1 and F-2. Neither touches line L-1 or a signed statement.

## Entry 1 (REFEREE-2 F-1, F-2): two text corrections outside the signed statements
- F-1 (packet §5, DATA remark, l. 140). The parenthesis is false. box150/out/rand/r150_049.json has degree ≤ 2 and NO degree-2 mover
  (N 1, one option). There T = 0 and Π (n_l + 1) = 1, so the ratio is 1 as well.
  - Old: «Largest (T + 1) / Π (n_l + 1): 1/3 on the corpus, 1 on the random runs (reached only by genomes with one degree-2 mover).»
  - New: «Largest (T + 1) / Π (n_l + 1): 1/3 on the corpus, 1 on the random runs (reached only by genomes with at most one degree-2
    mover, e.g. r150_049.json with none: T 0, product 1).»
  - Note: the earlier box 157 scan of the random genomes listed only ratio-1 genomes with one degree-2 mover; it did not list the
    zero-mover case. The «only» claim was an overreach of that scan. No DATA count changes.
- F-2 (packet §4, l. 105-106). The «» quote of the box 157 proposal is not verbatim to docs/new/N5-SEG-box157.md l. 24. A comma is
  missing after «reset», and «(no new states above)» was added from my 11:0xZ message to the Lead, not from that file.
  - Old: «the precise form of the box 157 proposal («after a level-0 reset the next segment is a sub-run of a segment already seen (no
    new states above)»)»
  - New: «the precise form of the box 157 proposal (docs/new/N5-SEG-box157.md l. 24: «after a level-0 reset, the next segment is a
    sub-run of a segment already seen»; the reading «no new states above» is my paraphrase)»
  - The killed statement itself (the two bullets of §4 «For every degree-≤-2 …» and «every state s_t …») is unchanged.
- Line L-1 is unchanged. No statement or DATA count changes.
