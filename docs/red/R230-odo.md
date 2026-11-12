# R230 item 6: a hand-built ODOMETER against L-SI 50 BOX 98 CONJECTURE U-FREE (designed attack)
L-RED successor 64, D1 / D18 / D14. Lead routing 2026-11-12 02:24Z. Written 2026-11-12T02:35Z (date -u).
Object: claude/l-si dc20e816 docs/si/box98-udep.md (`git show dc20e816:docs/si/box98-udep.md | sha1sum` = 95c992a9, 74 lines).
- §4, CONJECTURE U-FREE: «for every genome G, N5′-xi from S3 on Γ3(G) has T3 ≤ N + M + 4 …, independent of U(G)».
- §3, the blueprint: «a hub's e-set could behave like an ODOMETER … a reset must route through a DIFFERENT item … Howard's greed blocks
  it … unless genomes can host delays».
Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA / DEAD / READING.

## 0. Verdict
- ODOMETER NOT BUILT. U-FREE survives this attack.
  - Best designed instance: ODO(16, 16), T3 41 at N 36, M 82, U 2, [E-LEV] violated.
  - Its run has TWO rounds: a partial domino, a reset of all 16 chain movers in one iteration, then a full 16-step domino.
  - T3 stays additive in k and m (T3 ≈ m + k + O(1)), far below N + M + 4. DATA in §3.
- Under [E-LEV] the same design does nothing: T3 = 1 (§3). Every working variant needs the chain's e-items LESS relevant than the
  sources' items, which [E-LEV] forbids, because the chain lies above the sources.
- The exact blocking steps (§4) are three lemma candidates for L-SI: CAP, SELF-SIGHT and RACE-BUDGET. Together they say that a domino
  between two rival sources is paid for one rival option per iteration, so rounds × domino length ≤ M.
- PROVED (lane): Lemma SCC-CHAIN (§2). If the mover graph D(G) has no strongly connected component with 2 or more movers, then
  T3 ≤ Hc ≤ M. So any run longer than M needs a non-trivial SCC, and every long run in the fleet's corpora has one (DATA).

## 1. Returns (DATA; experiments/red/r230/ret230.py)
- PROVED (lane, pigeonhole): T3 ≤ (M − N) + R.
  - R is the number of returns: (iteration, mover) switches to an option the mover held earlier and abandoned.
  - Proof: each iteration before the first fallback switches at least one mover (REACH3-ALL: a HOW3 run, which stops when no mover
    switches). A mover x makes at most deg(x) − 1 switches to options it has never held.
- So super-linear T3 needs super-linear R. But R is common and does not make runs long:

| set | T3 | R | max returns of one mover |
| --- | --- | --- | --- |
| item-5 bests c12 / c24 / c48 | 23 / 31 / 39 | 48 / 97 / 39 | 8 / 11 / 3 |
| [STD3] climb bests A / B / C ([E-LEV] order) | 12 / 34 / 21 | 20 / 55 / 57 | 5 / 4 / 9 |

  Counters: unit (iteration, mover) switches; scope states 0 … first fallback; engine L-NEW gamma3 / n5v at l-new fcba92fc.
- R is not the binding axis. Returns happen in parallel, so they add switches without adding iterations.

## 2. Lemma SCC-CHAIN (PROVED, lane, unrefereed; experiments/red/r230/scc230.py)
- D(G): one node per mover, with edges x → wt and x → xt for every option (wt, xt ≥ 0), Ξ self-loops included.
- Let h(C) = 1 for a single mover without a self-loop, and h(C) = deg(x) for a single mover x with a Ξ self-loop.
- Hc := the maximum of Σ h(C) over chains of SCCs (source to sink).
- Statement: if every SCC of D is a single mover, then T3 ≤ Hc ≤ M.
- Proof, on HOW3(G), which N5′-xi's run is until its first fallback by REACH3-ALL (RESULTS R125):
  - Non-mover Even vertices are frozen.
  - From a mover x, a play visits only movers reachable from x in D, plus their gates, pads and β's, the core and c_W.
  - So the four values of x's options, and Odd's optimal choice at x's gates, depend only on the strategy at D-successors of x.
  - Let t0 be a state from which every D-successor of x is final.
    - If x has no self-loop, its option values are fixed from t0, so the Howard step at t0 moves x to a best option. Ties keep the
      current option. x never switches again, so x is final from t0 + 1.
    - If x has a self-loop, its option values depend only on its own choice. Each switch strictly increases V(x) (RESULTS R15 (a),
      F1). There are deg(x) choices, so after at most deg(x) − 1 switches x is final.
  - Induction from the sinks gives that every mover is final by Hc, and T3 is the first state with no switch.
- DATA:
  - 400 random genomes forced acyclic (seed 2316, xt only to strictly lower levels): violations 0 (unit: genomes with T3 > Hc).
    Max T3 5. Max T3 / Hc = 1.0, so the bound is attained.
  - All 11 long-run instances (item-5 bests, seeds, [STD3] bests) have a non-trivial SCC: largest 12 / 23 / 39 (c12 / c24 / c48),
    60 (MWR8_2), 59 (best_B). The U upward Ξ-edges join the W-levels into one big SCC.
- READING: the U-FREE question is about Howard inside a non-trivial SCC. Under U = 0 every SCC lies inside one level, so its exits
  (e-faces) are fixed once the lower levels are final.

## 3. The design ODO(k, m) and what it does (experiments/red/r230/odo230.py)
### Blueprint
- Two sources at level 1:
  - hub h, with options X_1 … X_k;
  - rival S, with options Y_1 … Y_k.
- A chain z_1 … z_m at levels 2 … m + 1. Each z_i has two options:
  - P_i, toward the hub: wt z_(i−1), and for z_1 wt h;
  - Q_i, toward the rival: through relays ρ to S.
- Every z / ρ option has an even Ξ self-loop. Odd then takes its e-face, and among its improving options Howard picks by β rank.
- The sources observe the top of the chain through u → z_m and u2 → z_m. These are the only upward edges: U = 2.
- e-items are permuted with chain items < X_1 < Y_1 < X_2 < … < Y_k < e_u. [E-LEV] is violated (inv > 0).
- Intended run: k rounds. In each, a domino of m switches runs toward the leading source, then the other source overtakes and resets
  the chain. Target T3 ≈ k·m at N + M = O(k + m).

### Runs
Counters per genome: one run of N5′-xi from S3 on Γ3(G), states 0 … first fallback.

| variant | k | m | N | M | U | T3 | total | fb | nstd | R | what happens |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| base | 3 | 8 | 20 | 32 | 2 | 2 | 5 | 1 | 0 | 0 | both sources jump at once; the chain never moves (all z stay on Q) |
| base, [E-LEV] order (EORD=lev, DOM, YLOW) | 3 | 8 | 20 | 32 | 2 | 1 | 4 | 1 | 0 | 0 | nothing moves |
| DOM (X_1 un-gated; e_Q > e_P) | 3 | 8 | 20 | 32 | 2 | 2 | 5 | 1 | 0 | 0 | the rival climbs to its top first; no domino |
| DOM + YLOW (rival items below the hub's) | 1 / 3 / 8 / 16 | 8 | 20 | 28 / 32 / 42 / 58 | 2 | 8 / 10 / 15 / 23 | T3 + 3 | 1 | 0 | 0 | ONE domino of m steps, then the hub climbs its options one per iteration |
| DOM + YLOW | 8 | 16 | 36 | 66 | 2 | 23 | 26 | 1 | 0 | 0 | as above |
| DOM + YLOW | 16 | 16 | 36 | 82 | 2 | 41 | 44 | 1 | 0 | 20 | TWO rounds (below) |

Trace of ODO(16, 16), DOM + YLOW (the rival's items interleave with the hub's from Y_12 on):
- Iterations 1-10: a domino P… runs while the rival climbs Y_1 → Y_11, one option per iteration.
- Iteration 11: the rival passes the hub's X_1. All 16 z's reset to Q in one iteration (12 switches).
- Iterations 12-16: hub and rival climb to X_7 / Y_16.
- Iterations 17-32: a full 16-step domino.
- Iterations 33-41: the hub climbs to X_16.
- Total: rounds 2, T3 41, N + M 118.

## 4. Where it is blocked (lemma candidates for L-SI; READING, checked on the traces above, not proved)
- CAP. Howard ranks option (x, k) at its value min⊴(A_k, B_k), where A_k is the e-face play and B_k = β_k then xt's play.
  - So an option that observes upward through its β-face can lift x at most to what it observes, plus β_k (less relevant than every
    e).
  - x collects its own item e_k only if the observed play is ALREADY worth more than the e-face.
  - Seen in base and DOM: a gated source that is behind can never gain an item above the leader's top item.
- SELF-SIGHT. If the observed play passes through x itself, it contains x's current play, so B_k ⊋ V(x) (lex-greater: the extra part
  holds an even e).
  - Then the gate is open for every option with A_k ⊳ V(x), and x climbs those options one per iteration, in β order.
  - Seen: once the domino completes, the hub climbs all its remaining options without pause; the rival climbs whenever the chain
    passes through it.
  - A source therefore cannot pause between rounds. Its gate is open exactly while the chain points at it.
- RACE-BUDGET. A reset needs the rival to overtake the leader. By CAP the rival cannot do that while its observer passes through the
  leader, so it must overtake DURING a domino, while the chain still passes through the rival.
  - During that window the rival, by SELF-SIGHT, either switches every iteration, consuming one of its options, or has no improving
    option. In the second case it cannot overtake at the end, by CAP.
  - So every iteration of a domino that is followed by a reset costs the rival one option: Σ over rounds of domino lengths ≤ #rival
    options ≤ M. Seen in ODO(16, 16): the first, aborted domino ran 10 iterations while the rival used Y_1 … Y_11.
  - To beat it, the rival would need a STALL gadget: an option that becomes improving only after a delay. That delay is itself a
    domino, so the construction recurses, and each level of the recursion pays its own options.
  - That is L-SI's «delay gadget» question one level down. I did not find a stall that is not paid for in options.
- [E-LEV]. Under [E-LEV] the chain's own e-items are the most relevant on its plays (W-edges go down, the chain sits above the
  sources). So z_i's choice between P_i and Q_i is fixed by e_(P_i) against e_(Q_i), and no domino starts: EORD=lev gives T3 = 1.
  - A domino under [E-LEV] would need each z_i's e-face play to pick up a more relevant item through an upward Ξ-edge.
  - With U ≤ 2, all chain movers share those two edges.

## 5. DEAD (this attempt)
DEAD ODO-2SRC: the two-source odometer, at U = 2, [E-LEV] violated.
- Obstruction: RACE-BUDGET, with CAP and SELF-SIGHT as above. Rounds × domino length ≤ #rival options.
- Instance that killed it: experiments/red/r230/inst/odo_dom_ylow_k16_m16.json. T3 41, 2 rounds, N + M 118.
- Frozen controls: odo_base_k3_m8.json (T3 2), odo_dom_k3_m8.json (T3 2), odo_dom_ylow_k{1,8,16}_m8.json and
  odo_dom_ylow_k8_m16.json.
- sha1 from `git show <SHA>:path | sha1sum` in the commit / notebook.

## 6. Not done / limits
- Only one design family. No stall gadget built. U = 2 only. One engine: L-NEW gamma3 / n5v, via elev230.build.
- RACE-BUDGET is argued on this family only. A general form would need the notion of «leader» and «observer» defined for every
  non-trivial SCC.
- The ODO genomes violate [E-LEV]. U-FREE's own scope is gamma3's [E-LEV] order, where the design gives T3 = 1.

## 7. Sources opened
- claude/l-si dc20e816 docs/si/box98-udep.md (§0-§4).
- Trunk docs/RESULTS.md R125 (REACH3-ALL, HOW3) and R15 (a) (F1), at 4c2f407d2.
- L-NEW gamma3.py (box189) and n5v.py (box190) at l-new fcba92fc (code, as engine).
