#!/usr/bin/env python3
"""L-NEW box 59: make an observer REACHABLE without letting it matter: append Even T (top even priority, self-loop) and Even E0 -> {o, T},
where o is the vertex labelled "o" (L-RED's observer, sbev.py --drop fc,obs). Even always prefers T. Usage: reach.py IN.pg > OUT.pg"""
import sys, re
L = [l for l in open(sys.argv[1]) if l.strip() and not l.startswith("parity")]
o = next(int(re.match(r'\s*(\d+)', l).group(1)) for l in L if l.rstrip().endswith('"o";'))
n = len(L); top = 2 * max(int(l.split()[1]) for l in L) + 2
print(f"parity {n + 1};"); sys.stdout.write("".join(L))
print(f'{n} {top} 0 {n} "T";'); print(f'{n + 1} 0 0 {o},{n} "E0";')
