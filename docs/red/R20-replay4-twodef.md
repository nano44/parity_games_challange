# R20: replay depth 4 at n = 32 on A_DTL; two DEF fall steps at one context (L-RED successor 3, 18:57Z by date -u; produced on Opus 5.5)

## 1. Replay depth 4 at n = 32 (experiments/red/carry/instances/replay4_n32.pg)
Measure: L-ALG's dtl_pieces.replays2 (GAP-A-M §6.3/§20; read-only, l-alg c7fc7cb) run on A_DTL itself through
experiments/red/carry/replay.py (Oink's exact order with DTL_ORDER=oink; stable otherwise; --c6 for L-ALG's C6).
Climb: dtl_search --fitness replay, seed 901, Oink order, from L-ALG's c6_replay3_n32 (depth 3), step 415.
n = 32, sha1 6cc02483. Pinned Oink: 2 dominions, 38 tangles, 13 iterations, solution verified (15 strategies).
| measure | A_DTL Oink order | A_DTL stable order | C6 (stable) |
|---|---|---|---|
| replay depth | 4 | 4 | 4 |
| replays | 4 | 4 | 4 |
| level sequence of the long phase | 1 0 2 3 1 2 4 3 4 0 | same | same |
Previous maximum anywhere: 3 (L-ALG c6_replay3_n32 / n48, 18:24Z). This is depth at FIXED n = 32, not yet growth with n.
Climbs from padded copies (n = 48, 64) continue.

## 2. Two DEF fall steps at one context (experiments/red/carry/instances/f1_twodef_n48.pg)
Climb: --fitness fallsdef, seed 811, Oink order, from f1_twofall_n48 (R19), step 162. n = 48, sha1 532f1978.
Pinned Oink: 1 dominion, 41 tangles, 11 iterations, solution verified (21 strategies). lex.py, both orders identical:
player 1, context R = G (|R| 48), steps (top changed vertex, before -> after; fallers):
- s5 (ideal moved): top 10 3->4, no fall.
- s6 (ideal SAME): top 45 6->8; FALL 6: 5->4, 10: 4->3.
- s7 (SAME): top 45 8->10, no fall.
- s8 (SAME): top 40 3->6; FALL 46: 6->4, 34: 7->5, 33: 7->6.
- s9, s10 (SAME): rises only; s11 (ideal moved) -> stable.
So (F1) restricted to DEF steps is FALSE as well, in both orders. Both falls are below the top changed vertex ((LEX) holds
at these steps) and the fallers of the two steps are in the two different components of the union (ids < 20 and >= 20),
so there is no nesting ((NR) level 0).
