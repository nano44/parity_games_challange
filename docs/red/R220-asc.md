# R220 Adversary vs packet P-N5-ASC (L-RED successor 55; Lead GO 22:17Z 2026-11-07)
Target: claude/l-new 95dc76d7, docs/new/P-N5-ASC.md, sha1 9c9cb50d89e8bba3232ca2790ddbf95f85580af6 (checked: 19,345 B). Referee files not read.
Labels: SURVIVES / BROKEN (frozen instance) / GAP / DATA (unit, set, scope, counter). Nothing here is a TARGET.md claim.
Tools: experiments/red/r220/ (own.py = R217's independent IDEAL-CYC implementation + env EORD; cs220.py, asc220.py, hubg220.py,
export220.py). No L-NEW code is used.

## 0. Verdicts
| packet statement | verdict | evidence |
| --- | --- | --- |
| §3 Lemma E-MON | SURVIVES | proof re-read: uses only [DEF] (e above every β; c_W, K0, K3 placement), F1, [VJ]; no e-order among e's |
| §3 Lemma CHAIN-DECOMP | SURVIVES | proof re-read: [DEF] (one W-edge or c_W), F3; no e-order |
| §4 Lemma SKELETON | SURVIVES | proof re-read; the B ≥ 1 counts below never exceed what it allows |
| §4 Theorem HUB-ASC(B) | SURVIVES | exhaustive CS(M), M ≤ 5, B 0-3 (§1); proof re-read (shapes N / a / c, Z_y sub-run) |
| §5 Corollary HUB-ASC-G | SURVIVES | 58 runs × 2 e-orders, 0 violations (§2) |
| §6 Lemma UP-JUMP, Corollaries UP-B, NOUP | SURVIVE under [E-LEV]; [E-LEV] is NEEDED | 58 runs under [E-LEV]: 0 violations; with level-reversed e-order: U(G) = 0 and 2-4 ascents (§3) |
| «§3-§5 do not use [E-LEV]» (§9) | SURVIVES | text scan (§4); HUB-ASC-G holds with the reversed order too (§2) |
No BROKEN, no GAP.

## 1. HUB-ASC(B), exhaustive (cs220.py; DATA)
- Method: all forests on M items × hub choices. Runs = monotone paths in the product order of (chain(1), …, chain(M), hub value), with
  lex order = integer order of bitmasks. Longest path counting strict hub increases. Only the HUB value is restricted to ≤ B ascents,
  as in the theorem.
- Unit: distinct hub values. Set: all runs of CS(M). Scope: abstract. Counter: max over runs.

| M | B 0 (F_0) | B 1 (F_1) | B 2 (F_2) | B 3 |
| --- | --- | --- | --- | --- |
| 1 | 2 (2) | 2 (15) | 2 (678) | 2 |
| 2 | 4 (4) | 4 (231) | 4 (747,061) | 4 |
| 3 | 7 (7) | 8 (1,924) | 8 (1.4·10⁸) | 8 |
| 4 | 11 (11) | 16 (10,185) | 16 (8.7·10⁹) | 16 |
| 5 | 16 (16) | 29 (39,711) | 32 (2.4·10¹¹) | 32 |

- F_0 is tight for M ≤ 5. F_1, F_2 hold with a large margin. The maxima equal L-NEW's per-chain-restricted CS(M, A) maxima (box 193 §3),
  although here only the hub is restricted. M = 6 not run (117k states, quadratic DP; not feasible here).

## 2. HUB-ASC-G on game runs (hubg220.py; DATA)
- For every vertex v of IDEAL-CYC and every maximal interval with Λ(v) fixed: D_E ≤ F′_B(M_w)? Here B is the max ascents of seq(v) on the
  interval and M_w is the number of e's above w.
- Unit: (vertex, Λ-interval) pairs. Set: 58 runs (L-NEW's 17 box 192 R-bests, R217's 19, R218's 17, R219's 5 incl. NOUPC_1-3, rd3_d4).
  Scope: own.py IDEAL-CYC, e-order EORD = lev and EORD = rev.
- Counter: violations 0 / 58 (lev), 0 / 58 (rev). Files hubg220_lev.txt, hubg220_rev.txt.

## 3. UP-B and the premise [E-LEV] (asc220.py, export220.py; DATA + scope finding)
- Under the builder's order ([E-LEV], EORD = lev): max ascents ≤ U(G) at every (state, vertex). Unit: (t, v) pairs. Set: the same 58 runs.
  Counter: violations 0. E.g. LEAP_k64: U 129, max 2; NOUPC_1-3: U 0, max 0 (asc220_lev.txt).
- With [E-LEV] violated (EORD = rev: e-priorities ordered by (−level, gate)): the game is still R104's Γ(G) shape (every e above every β,
  even, distinct). Per the Lead, R104 leaves the order among e's open. Counter: NOUPC_1 / 2 / 3 have U(G) = 0 and max ascents 2 / 3 / 4,
  in 120 / 450 / 280 (t, v) pairs (asc220_rev.txt). Total over 58 runs: 3 runs violate.
  - Witness (export220.py): NOUPC_1, t 0, v 10: seq = e of option (10, 2) at level 3, priority 72, then e of (5, 1) at level 1,
    priority 100. An ascent with no upward Ξ-edge: the play goes down one level and meets a lower-level e of higher priority.
  - Frozen: inst/NOUPC_{1,2,3}.json (genomes, = r219/inst) with inst/NOUPC_{1,2,3}_rev_idealcyc.pg (own.py's IDEAL-CYC arena with
    EORD = rev; sha1 82e41194…, 7ea66452…, 94db68d5…; inst/SHA1SUMS). Oink 8fbf0a7 --zlk parses and solves the .pg (shape check only).
    The run itself is checked by one route only (own.py; box191 idealcyc hard-codes the (level, gate) order).
- Finding (scope, not a kill): [E-LEV] is necessary for UP-JUMP, UP-B and NOUP. The packet already states it as a hypothesis (§1, §6,
  §9). For a landing, the scope line should say the bound holds for Γ(G) as BUILT by gamma3.py (or under [E-LEV]), not for every
  e-order R104 allows.

## 4. Does anything outside §6 use [E-LEV]? (text check)
- grep of «level / lev(» in the packet: outside §6 only the quoted [DEF] line (W-targets one level lower) and «LEVEL» in §4/§5, which
  means the τ-constant stretches, not genome levels.
- §3 E-MON: «every vertex more relevant than some e-vertex is an e-vertex, c_W, K0 or K3». This needs e above β / mover / gate / K1 / K2,
  not an order among e's.
- §5: the item order is «relevance order» of U_w, whatever the e-order is. [XICYC] (e) (2M + 3 cycle nodes per vertex) has no e-order.
- So no silent use. Consistent with §2: HUB-ASC-G holds with the reversed order.

## 5. Not done
- M = 6 exhaustive (needs a faster DP than mine).
- A second implementation for the EORD = rev runs (idealcyc / gamma3 cannot take another e-order).
- An attack on the proof of HUB-ASC(B) for B ≥ 2 beyond M = 5: exhaustive data cannot reach where F_2 would bind.
