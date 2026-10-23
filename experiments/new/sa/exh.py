#!/usr/bin/env python3
"""Exhaustive SA_k gap search over every game of experiments/harness/exhaustive.py (n vertices, priorities 0..P)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
import exhaustive
from gaps import run
n, P, k = map(int, sys.argv[1:4])
run([(f"x{n}_{P}_{i}", g) for i, g in enumerate(exhaustive.iter_games(n, P))], k, f"exhaustive n={n} P={P}")
