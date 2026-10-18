# L-NEW notebook ((c) design lane under D14; Lead reading L35)
Overwrite the top sections; append to "Sources opened" and "Dead ends". Box 1 started 2026-10-18 09:10Z (date -u).

## Resume point
- 2026-10-18 09:10Z: lane created on branch claude/l-new from trunk ff4e60c. Read: CLAUDE.md, TARGET.md, DECISIONS D1/D13/D14/L35,
  lit/RANKING.md, lit/BARRIERS.md, RESULTS DE1-DE8 (DE9-DE21 are DTL proof routes), si/README.md, S5.md, S6.md, si.py, vjfast.cpp.
- Next: Box 1 (i) S5/S6 fast kill under adversarial renumbering (experiments/new/renum.cpp), then (ii) own approaches.

## Queue
1. (i) S5 (zadeh, index tie-break) and S6 (cunningham, index order): hard bench, gated_*, fhz_padded, randomfacetsubexp, M_L,
   zadehexp, cunninghamexp; renumbering hill climb on the iteration count.
2. (ii) up to three own approaches in docs/new/<name>.md (pseudocode, novelty, barrier draft, cheapest killer) before code.
3. Implement the most promising; Zielonka agreement and strategy check first; then hard bench and its killer.

## Sources opened
(none yet; docs/lit is a map, not a source)

## Dead ends
(none yet)

## Things only I know
- Index dependence in L-SI's engine: the vertex numbering enters (a) the injective priority rank (ties of equal priority by
  index), (b) the best-reward start (ties), (c) the zadeh tie-break / the cunningham cyclic order. A renumbering changes all three.
