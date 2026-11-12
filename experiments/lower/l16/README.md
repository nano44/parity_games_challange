# L-LOWER BOX L16: hand-built shared cascade on C12 (tools; product docs/lower/L16-cascade.md)
- graft.py / cmpgraft.py: graft an l15 ekr.py cascade at levels 8..7+k; compare its run inside the genome (core clamped) with the stand-alone run.
- pgad4.py: l13/pgad3.py + XC (extra candidates for XS) + FIXC (signs / gates / starts of listed movers fixed by unit clauses).
- pgad5.py: pgad4 + XALL / XORD: the options of XS may point to any mover compatible with a client order (acyclic by construction).
- diag.py: first row where a free sim6 run leaves the core target, and why (key / better / closure).
- celem.py, celem2.py, dl2.py, rw.py: C-element / decision-list designers on fixed (clamped) trajectories (heuristic search aids only).
- kr2.py: l15/kr.py (relaxed) + EXT inputs (core movers whose states the cascade and client may read).
- ekr2.py: EXACT cascade + client design with EXT inputs whose chains are the base genome's fixed chains (clamped run); env LEVEL (slot level),
  KEEPO (top key unchanged), KEEPR / KEEPRSKIP / KEEPRONLY (movers whose chains enter the client or the slots keep their base better),
  FORCEBASE (debug: client exactly as in the base), DEBUGCORE (UNSAT core over kept (reader, row) constraints).
- sim2.py: independent replay of an ekr2 design (integer ENC values, own chain walk). graft2.py: graft an ekr2 design into a genome.
- run/: designs and genomes (sha1 in the doc). Builds: none (Python + pysat).
