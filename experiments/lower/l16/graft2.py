#!/usr/bin/env python3
"""L-LOWER 16: graft an ekr2.py design into a genome. Cascade mover i -> genome mover 16+i (levels 8..7+K); client X's two options
-> the design's client options; EXT targets 'eN' -> mover N; option parities -> bp (even = 0). Ranks: the base order of all other
options is kept; the design's free options (cascade + client) are inserted into it so that their order relative to every fixed
option named in the design (and among themselves) is the decoded one; each free option sits just above the highest fixed option the
design places below it (ties kept in decoded order). Gates of levels 8..7+K from the design's gate bits; starts of the cascade.
env LEVEL=L as in ekr2.py.
Usage: graft2.py DESIGN GENOME CLIENT OUT"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
import sim6
des, gen, X, outp = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
D = sim6.rd(gen); xt = {}; ev = {}; order = []; gate = []; start = []
for ln in open(des):
    w = ln.split()
    if w[0] == 'opt': xt[int(w[1])] = w[3]; ev[int(w[1])] = int(w[5])
    elif w[0] == 'rank_order_ascending': order = w[1:]
    elif w[0] == 'gate': gate = list(map(int, w[1:]))
    elif w[0] == 'start': start = [int(c) for c in w[1]]
H = len(start); K = H // 2; NC = 2 * H
LEV = int(os.environ.get('LEVEL', '8'))
def gopt(op): return 4 * LEV + op if op < NC else 2 * X + (op - NC)      # design option -> genome option
def gtar(z):
    if z == 'exit': return -1
    if z.startswith('e'): return int(z[1:])
    return 2 * LEV + int(z)
free = {gopt(op) for op in range(NC + 2)}
for op in range(NC + 2):
    D['xt'][gopt(op)] = gtar(xt[op]); D['bp'][gopt(op)] = 0 if ev[op] else 1
# ranks
base = sorted((m for m in range(len(D['br'])) if m not in free), key=lambda m: D['br'][m])
anchor = {}; last = None
for a in order:
    if a.startswith('f'):
        last = int(a[1:]); assert last not in free, 'a fixed option of the design is a grafted option'
    else: anchor.setdefault(last, []).append(gopt(int(a)))
seq = list(anchor.get(None, []))
for m in base:
    seq.append(m); seq += anchor.get(m, [])
assert sorted(seq) == list(range(len(D['br'])))
for r, m in enumerate(seq): D['br'][m] = r
for i in range(K):
    l = LEV + i
    for a in (0, 1):
        x, y = D['gate'][4 * l + a], D['gate'][4 * l + 2 + a]; hi, lo = max(x, y), min(x, y)
        D['gate'][4 * l + a], D['gate'][4 * l + 2 + a] = (hi, lo) if gate[2 * i + a] else (lo, hi)
for i in range(H): D['start'][2 * LEV + i] = start[i]
assert sim6.topo(D) is not None, 'cyclic after graft'
sim6.wr(D, outp); print('GRAFT2', des, '->', outp)
