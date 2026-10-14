# Owner rulings (append only; quote verbatim; a reading is labelled "Lead reading")

## D1 (2026-10-14): launch brief
Full text, verbatim: docs/decisions/D001-launch-brief.md. Key lines:
> Spawn no attack lane before I approve it.
> Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
> A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
> Never downgrade the referee to save money.
> At most 5 working sessions at once unless you justify more to me.
> On "stop", follow the playbook's stop procedure; restart only on my word. On paid overage, stop the fleet and tell me.

Lead reading L1 (superseded by the amended L1 under D2): M2 clock start was held while arxiv.org was blocked.
Lead reading L2: the playbook's `main` branch is replaced, until the owner says otherwise, by the Lead branch
claude/vibrant-johnson-nxvvxo as trunk; lanes merge into it only through the pipeline.

## D2 (2026-10-14 ~18:15Z): TARGET.md v0.1 approved with changes; network opened
Verbatim:
> I have provided you with full internet access,
>
> TARGET.md v0.1: approved with these changes. Record this ruling verbatim, bump to v1.0, and date it.
> 1. Section 1: priorities range over {0, ..., n} (d ≤ n + 1); the compression step stays charged to the algorithm.
> 2. Section 6: add a check that the Lean `solve` implements exactly the pseudocode whose running time is analysed.
>    The referee signs this, and the CHECKER diffs it.
> 3. 7a approved with change 1. 7c, 7d, 7e approved as written.
> 4. 7b changed: a randomized (Las Vegas, expected polynomial) algorithm is labelled M4-R, not M3, and reported to me
>    at once like an M4 claim.
> 5. Gauntlet addition: every implementation also outputs positional strategies, and L-COMP verifies them on every
>    test game.
> Attack lanes may start once v1.0 is pushed.

Lead reading L3: change 5 applies to every implementation that enters the gauntlet (fleet claims and audited external
claims such as 2511.03752); the target statement itself still requires only the regions (7d as written).
Lead reading L4: "Attack lanes may start" lifts D1's hold; lanes are still added one at a time in L-LIT's ranked order (D1).
Lead reading L1 (amended): the M2 clock starts 2026-10-14 18:30Z (paper hosts reachable, REFEREE spawned); deadline 2026-10-16 18:30Z.
Lead reading L5 (M1 wording, D1 "confirms their blow-up in Oink"): Oink has no implementation of the switch-all/switch-best rules that
Friedmann's SI games target, so those two families are confirmed with REFEREE-checked Python ports of PGSolver's SI loop, quoted as
"the strategy-improvement loop (= PGSolver with -dgo -dsd -dlo -dsg)"; the other families are confirmed in Oink itself.
