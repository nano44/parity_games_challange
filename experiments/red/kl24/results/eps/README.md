# ε(L) evidence for R56 §3 (L-RED box 24; produced on Opus 5.5)
Games: HL_k = experiments/red/kl24/hlgen.sh k L L (regenerable).
- eps_HL1_L.txt, eps_HL2_L.txt (L = 5..7; HL_2 at L = 6, 7): r2mean.py full runs, seeds 1..20 or 1..10. Early stop = a run below 99%
  of the full count.
- ex_steady_L.txt: exactlap.py, ONE-lap exact chain on HL_2 (L7 = L8 = L), base seed 3, W 300, J 1, with failure-mass tables.
- multilap*.txt: exactlap.py with LAPS = m (P(fail within m laps)); same snapshot.
- ex_laps.txt: one-lap exact ε along base seed 3 from the start (W 0), J = 1..100. Some lines of an earlier run were overwritten by
  a script edit; only lines that contain "exact P" are valid.
- ex_fail8.txt: exact one-lap ε at the laps 35,723-35,725 of HL88_2 seed 3, the run that stopped early at pivot 1,230,538.
- lt2_4.txt: laptrial2.py Monte Carlo average at L = 4 (cross-check).
