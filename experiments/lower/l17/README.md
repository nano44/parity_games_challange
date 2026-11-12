# L-LOWER BOX L17: build the base around the f6 cascade (tools; product docs/lower/L17-around.md)
- run/: annealed starts and results (A1, A2, A2_solved), frozen by run/SHA1SUMS.
- sweep.sh: resumable ascending exact-prefix sweep with l13/pgad3.py (stops at the first non-SAT answer; one log line per prefix).
- sweep5.sh: the same with l16/pgad5.py (env XALL=1, XORD, FIXC passed through; G may be empty).
- sweepA2/: A2_solved sweeps (pgad3, G {63}, XS 8 and XS 11): every SAT decode, logs, replay.txt (l13/prefcheck.py, sim6 = fenc), SHA1SUMS.
- sweepA3/: A3 (pgad5 on A2_solved, XS 8,11,12,14,15, XORD 8,11,12,15,14, XALL=1, FIXC 16,17, G empty): SAT decodes, log, replay.txt, f6check.txt (rows 0..510), SHA1SUMS.
