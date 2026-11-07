L-NEW box 150/151 copies (read-only sources: claude/l-red 2f60fa74, experiments/red/r199/): req.py, build.py, genk.py, xwake.py
unchanged; xwake_anti.py = xwake.py + ONE clause (env ANTI=1: antisymmetry of «reaches», valid on every acyclic Xi-graph) and the
«aux moves» print removed. run.sh regenerates the table of docs/new/N5-NEST-box151.md §2 into runs.txt (needs z3-solver).
