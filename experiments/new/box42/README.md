# experiments/new/box42 (L-NEW successor 21, box 42)
- nhcheck.py: checks every step of Theorem NH in docs/new/P-N5-NH-box42.md (Lemmas SW, ST, CL, STR-COUNT, NR; Theorem NH (a)-(c)) on N5
  runs. Engines: ../box28/fbre.py → ../box25/common.py (N5 step, Engine, wvals). One Odd choice vertex asserted; other files skipped.
- Runs (2026-10-25 ~19:55Z, date -u):
  - `python3 experiments/new/box42/nhcheck.py --list experiments/new/box41/lib41.txt`: 253 runs, 990 phases, violations 0
    (max per phase O 77, X 100, f^O 12, K_W 25, E 15).
  - `python3 experiments/new/box42/nhcheck.py --rand 3000 6 16 4202 --randstart`: 2,633 runs, 7,042 phases, violations 0.
- Item (2), docs/new/N5-KW-box42.md (working doc):
  - wlag.py (Lemma WLAG): `--list experiments/new/box41/lib41.txt`: 4,661 cases, 0 violations; `--rand 3000 6 16 4203 --randstart`: 98, 0.
  - kwprof.py: K_W / E profile in OTHER U2 / U3 / U23 stretches (121 / 121 new gate edges with y, z ∈ R and Ξ(z) rising one step earlier).
  - kwfreeze.py (Lemma CLS-CONST, Theorem KW-FREEZE (a)-(c), Corollary KW-E): lib41 5,532 sub-runs, 0 violations; `--rand 3000 6 16
    4204 --randstart`: 7,514 sub-runs, 0 violations.
