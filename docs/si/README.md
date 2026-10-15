# L-SI: strategy-improvement design loop toward M4 / M4-R (owner: L-SI; Lead brief 2026-10-15 10:10Z)

Method (Lead brief): per candidate S<k>, docs/si/candidates/S<k>.md states the exact rule, its bit cost per iteration, which of
B8-B14 it lies outside and why (before testing), and every unproven assumption; experiments/si/ implements it on top of an own
VJ-valuation engine cross-checked against the REFEREE-checked PGSolver port; falsification runs cheapest first (M1 families
incl. switchallexp/switchbestexp, adversarial search on n ≤ 10, random games). Dead candidates: docs/si/DEAD.md with the killing
family or instance and the growth. A survivor is reported to the Lead at once (gauntlet steps 2-5 are not run by L-SI).

| file | what |
| --- | --- |
| candidates/S1.md | Random-Action-Removal = original Random-Facet (Zwick 2607.06334 Fig. 1), M4-R candidate |
| candidates/S2.md | significance-ranked single switch (MSF / LSF) |
| candidates/S3.md | steepest single switch (re-evaluated), most-vertices-improved |
| candidates/S4.md | subgame-optimal start (constructive reading of Friedmann Lemma 4.3) |
| DEAD.md | dead candidates with killers |
| RESULTS.md | iteration tables and growth fits per family and rule; plots in plots/ |

Engine: experiments/si/si.py (rules, CLI solver), xcheck.py (cross-check), families.py (family sweeps), adversarial.py
(hill-climb), check.sh (fast self-test run by scripts/verify.sh). Sources opened: notes/L-SI.md.
