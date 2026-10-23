# experiments/new/esc: N10a-N10c (box 19, docs/new/N10-screen.md). Needs scipy, highspy, networkx (pip).
- esc.py: ACYC (level 0) + ESCAPE cuts (ESC1, ESC-tau), exact min-cut separation; esc_feasible(g, taus=()).
- esctest.py: modes oneplayer / random / exh / files; --tau = N10b (tau from peel.py's REGION LP on the dual, levels 0 and 1).
- cond.py, condtest.py: N10c conditioning on the N10b oracle; tests YES-instances G[W_E], dual(G[W_O]) and NO-instances.
- instances/: pinned gap and STUCK games (sha1 in N10-screen.md). results/: outputs quoted there.
