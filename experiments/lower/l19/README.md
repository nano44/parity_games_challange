# L-LOWER BOX L19: exact questions on box 217's one-player model 1P(G) by SAT (product docs/lower/L19-onep.md)
Model: claude/l-new a32a588d docs/new/N5-QUIETKEY-box217.md §1, experiments/new/box217/one217.py (read-only; a worktree of that commit is used
for replays: ONE217_DIR = <worktree>/experiments/new/box217).
- enc19.py: symbolic degree-2 genome on a fixed level-width profile W, the key step (one217.OneP.step, rule key) as a circuit, L steps
  unrolled. Modes: enum K (first level-(K-1) mover makes >= 2^K - 1 switches in steps 0..L-1), len (s_L != s_(L-1)), free; env FIXG
  (checker mode: genome fixed), CNF (DIMACS out), SB (symmetry breaks, default on: s_0 = option 0 everywhere; Xi-acyclicity by the
  exact longest-path depth instead of a free order).
- val19.py: checker-mode validation against one217 (random genomes: SAT with the simulator's states; a wrong state bit UNSAT).
- rep19.py: replay of a decode with one217 (T_key, switches per mover, |K| by box 217's DP, enumeration depth k(G)) and, with --n5, N5
  itself on Gamma3 (one217.report --check: n5 steps, mism).
