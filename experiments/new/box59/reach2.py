#!/usr/bin/env python3
"""L-NEW box 60: put L-RED's observer o ON a play without letting it matter: append Z (top ODD priority, self-loop; Even loses there)
and Even E0 -> {o, Z}. Even always plays E0 -> o, so o lies on E0's play at every step; nothing points to E0. Usage: reach2.py IN.pg"""
import sys, re
L = [l for l in open(sys.argv[1]) if l.strip() and not l.startswith("parity")]
o = next(int(re.match(r'\s*(\d+)', l).group(1)) for l in L if l.rstrip().endswith('"o";'))
n = len(L); top = 2 * max(int(l.split()[1]) for l in L) + 3
print(f"parity {n + 1};"); sys.stdout.write("".join(L))
print(f'{n} {top} 0 {n} "Z";'); print(f'{n + 1} 0 0 {o},{n} "E0";')
