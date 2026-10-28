# XR-LIN kill: independent reproduction (L-COMP successor 6; Lead 2026-10-28 21:27Z). DATA.
- **Subject.** L-SI's counterexample to CONJECTURE XR-LIN: l121reader_n41, which is long121_n40 plus a passive Odd reader o = 40.
  - Source: origin/claude/l-si 2e94557d, experiments/si/root/instances/.
  - instances/l121reader_n41.pg sha1 084da8cd47707b8937ebe30fdfae88d3d988bdaf; .start sha1 7ca283c43b7092acc454c5ffc6b1995e3a29bf68.
  - instances/long121_n40.pg sha1 c667c085 and .start sha1 d750664a, copied from experiments/new/box48/instances (identical to
    experiments/red/n3/instances).
- **Engine.** Only L-COMP's n5b.py SPEC (experiments/n5-second). No experiments/si/ code is imported (repro.py). Regions: Oink zlk @ 8fbf0a7.
  Strategies: harness/verify.py.
- **Command.** `python3 repro.py > repro.out` (about 1 s).

## Results (repro.out)
- **Same run on 0..39.** The game restricted to 0..39 is identical to long121_n40. Over all 123 states, σ, τ and σ̄ restricted to 0..39
  are equal to long121_n40's run. Both runs have 122 iterations and 8 fallbacks, with equal fallback flags.
  - The phases are equal: [0, 0] and [1, 122], both in long121_n40 and in the reader run, on all 41 vertices and keyed on 0..39 only.
  - τ(o) never changes; o has priority 0, out-degree 14 and in-degree 0.
- **Ξ(o) changes in the phase [1, 122]: 86.** This equals L-SI's 86 and is above 2n = 82 (n = 41). XR of that phase = 86, attained at
  o. For comparison, the same phase of long121_n40 has XR = 44, at v 6.
- **Checks.** Regions = Oink zlk on both games; verify OK on both.
- **No disagreement with L-SI.**
