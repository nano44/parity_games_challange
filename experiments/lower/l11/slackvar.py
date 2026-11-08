#!/usr/bin/env python3
"""L-LOWER 11: one-slack variants of a tight target: row k duplicated (the core holds one step after step k; T + 1).
Usage: slackvar.py TARGET k OUT"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tsat import rdtarget
from ttarget import F
LS, g = rdtarget(sys.argv[1]); k = int(sys.argv[2]); L2 = LS[:k + 1] + LS[k:]
with open(sys.argv[3], 'w') as f:
    f.write(f'# {sys.argv[1]} with row {k} duplicated\ngate ' + ' '.join(map(str, g)) + '\n'); f.writelines(' '.join(map(str, s)) + '\n' for s in L2)
print(sys.argv[3], 'T', len(L2) - 1, 'F', F(L2, g, len(g) // 4))
