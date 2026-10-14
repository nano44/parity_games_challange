# M1: hard families (in progress)
- `sweep.py`: generate a family over sizes, run solvers with timeouts, check all finishing solvers (plus py-zlk on small
  instances) agree, write `results/<family>.{csv,md,png}`.
- `run_all.sh`: every family, its sizes, target and contrast solvers.
- `pgsolver_port.py`: Python port of PGSolver generators (recursiveladder, switchallexp, switchbestexp), each line cited
  to github.com/tcsprojects/pgsolver @ d3cd624. Awaiting a referee line-by-line check.
- `families.py`: source, claim and paper reference (all papers awaiting source) per family.
Per-family READMEs and results follow when the sweeps finish.
