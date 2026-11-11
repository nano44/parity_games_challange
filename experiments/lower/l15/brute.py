#!/usr/bin/env python3
"""L-LOWER 15: brute-force check of kr.py's relaxed model K for small k: enumerate every total order of the 2k helpers, every better
function (a truth table over the states of the movers before it), every gate-bit vector and every start; simulate (M3)/(M4) with
o(7) = t mod 2; report whether some system separates the client lists on rows 0..P. Independent of kr.py's CNF.
Usage: brute.py GENOME TARGET K P CLIENTS"""
import sys, os, subprocess, ast, itertools
here = os.path.dirname(os.path.abspath(__file__))
gen, tp, K, P, CL = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), [int(c) for c in sys.argv[5].split(',')]
lists = []
for x in CL:
    l = subprocess.run([sys.executable, os.path.join(here, '..', 'l13', 'reqpref.py'), gen, tp, str(x), str(P)], capture_output=True, text=True).stdout
    L = ast.literal_eval(l[l.index('['):l.index('] |') + 1]); lists.append([(t, r) for t, r in L])
H = 2 * K
def run(order, funcs, gates, start):
    pos = {y: i for i, y in enumerate(order)}
    s = list(start); S = [tuple(s)]
    for t in range(P):
        bet = []
        for y in range(H):
            pre = [z for z in order[:pos[y]]]; idx = 0
            for z in pre: idx = 2 * idx + s[z]
            bet.append((funcs[y] >> idx) & 1)
        ns = list(s); op = (t + 1) % 2
        for i in range(K):
            for y in (2 * i, 2 * i + 1):
                if bet[y] != s[y] and s[y] != op: ns[y] = op
            a, b = ns[2 * i], ns[2 * i + 1]
            op = (a ^ op) if a != b else gates[2 * i + a]
        s = ns; S.append(tuple(s))
    return S
def ok(S):
    for L in lists:
        seen = {}
        for t, r in L:
            if seen.setdefault(S[t], r) != r: return False
    return True
found = None; n = 0
for order in itertools.permutations(range(H)):
    sizes = [2 ** (2 ** i) for i in range(H)]
    for fs in itertools.product(*[range(sz) for sz in sizes]):
        funcs = [0] * H
        for i, y in enumerate(order): funcs[y] = fs[i]
        for gates in itertools.product((0, 1), repeat=2 * K):
            for start in itertools.product((0, 1), repeat=H):
                n += 1
                if ok(run(order, funcs, gates, start)): found = (order, funcs, gates, start); break
            if found: break
        if found: break
    if found: break
print('BRUTE K', K, 'P', P, 'clients', CL, 'systems tried', n, 'RESULT', 'SAT' if found else 'UNSAT', found or '')
