# experiments/new/sa: N9a / N9b kill tests (box 18, docs/new/N9-screen.md)
Needs scipy >= 1.18 with HiGHS (`pip install scipy highspy`); not part of scripts/verify.sh (scipy is not in the gate's environment).
- sa.py: ACYC program and its SA+_k lift; sa_feasible(g, k). sanity.py: program = Zielonka, full level exact, monotone in k.
- gaps.py (random games, four queries per game), exh.py (exhaustive tiny games), kstar.py (k* of listed gaps).
- ring.py / ringtest.py (R_L), kfam.py (K_n), twoout.py (circ(n,a,b), random 2-out one-player all-odd games).
- peel.py (N9b certified peeling), peeltest.py. pin.py writes instances/ (sha1 in N9-screen.md).
- results/: the outputs quoted in N9-screen.md §1(f), §2(f).
Reproduce the main rows: `python3 -I twoout.py circ 3 7 3 1 2` (k* = 1 2 2 2 3), `python3 -I peel.py instances/peel_r1147.pg` (STUCK),
`python3 -I peeltest.py random 0 300 3 12` (294 solved, 6 stuck), `python3 -I gaps.py random 1000 3000 3 14 1` (44 gaps).
