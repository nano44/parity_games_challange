#!/usr/bin/env python3
"""L-LOWER 11: write (1) the ann core file (header «rows K», then one bit string per step) and (2) an empty start genome at depth d
(all options to the exit, ranks = option ids, signs 0, core gates from the tight target, helper gates 4l+1000.., start = core row 0
then zeros) for annk. Usage: mkstart.py TARGET d CORE_OUT GENOME_OUT"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tsat import rdtarget
LS, cg = rdtarget(sys.argv[1]); d = int(sys.argv[2]); h = len(cg) // 4; N = 2 * d; M = 2 * N
with open(sys.argv[3], 'w') as f:
    f.write(f'{len(LS)} {2 * h}\n'); f.writelines(''.join(map(str, s)) + '\n' for s in LS)
gate = list(cg) + [v for l in range(h, d) for v in (4 * l + 1000, 4 * l + 1001, 4 * l + 1002, 4 * l + 1003)]
with open(sys.argv[4], 'w') as f:
    f.write(f'd {d}\nxt ' + ' '.join(['-1'] * M) + '\nbr ' + ' '.join(map(str, range(M))) + '\nbp ' + ' '.join(['0'] * M) +
            '\ngate ' + ' '.join(map(str, gate)) + '\nstart ' + ' '.join(map(str, list(LS[0]) + [0] * (N - 2 * h))) + '\n')
