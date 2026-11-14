#!/usr/bin/env python3
"""Candidate RF («ROOT-FIRST», L-SI 57) and Howard (switch-best), through L-RED's one-sided VJ engine, UNMODIFIED:
claude/l-red 821d63e3 experiments/red/r247/si247.py + rf247.py (+ r237/n5s237.py), read from the directory in env LRED
(git archive 821d63e3 experiments/red/r247 experiments/red/r237 | tar -x -C $LRED). This is L-RED's implementation from the
rule as the Lead relayed it (readings R1-R4 in rf247.py's header), NOT L-SI's own engine: a row from it is a row of THAT
implementation until L-SI's pseudocode is checked against it (CLAUDE.md trap).
Usage: rf_lred247.py [--rule rf|howard|first] GAME.pg -> one JSON line. Start: S3 for Even (si247 «s3»).
iterations = applied switch sets (si247's unit); steps = total switches applied. Even plays the final sigma on her region,
Odd plays sbar (his optimal counterstrategy to the final sigma, from the engine's last evaluation) on his."""
import sys, os, json
L = os.environ.get("LRED")
if not L: sys.exit("set LRED to an archive of claude/l-red 821d63e3 (experiments/red/r247, experiments/red/r237)")
sys.path[:0] = [os.path.join(L, "experiments", "red", "r247"), os.path.join(L, "experiments", "red", "r237")]
import si247, rf247  # rf247 registers the rule «rf» in si247.RULES
rule = sys.argv[sys.argv.index("--rule") + 1] if "--rule" in sys.argv else "rf"
prio, owner, succ = si247.parse(sys.argv[-1]); e = si247.SI(prio, owner, succ); r = e.run(rule, "s3")
if r["capped"]: sys.exit("iteration cap reached")
win, sigma, sbar = r["win"], r["sigma"], r["sbar"]; strat = {}
for v in range(e.n):
    if owner[v] == win[v]: strat[str(v)] = int(sigma[v] if owner[v] == 0 else sbar[v])
print(json.dumps({"winner": [int(w) for w in win], "strategy": strat, "iterations": r["its"], "steps": r["switches"]}))
