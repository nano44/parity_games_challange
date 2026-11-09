#!/usr/bin/env python3
"""L-LOWER 13: EXACT PREFIX GADGET (BOX L13). Generalizes L-COMP box 32 gadget.py (read-only; this file is own code on top of
L-COMP's enc32, read-only copy ../l12/enc32_lcomp.py, sha1 a8c4f5e3).
Question: on a BASE genome (wiring and ranks fixed), with FREE wiring on the options of the movers XS (core culprits, rewired into
the gadget) and of a helper set G, insertion ranks (free positions in the fixed order) for those options, and free signs / helper
gate bits / helper starts / helper states everywhere, does the run realize the core TARGET on rows 0..PREFIX (all core movers'
constraints; no fixed point)?
Candidates (acyclic for every choice): options of x in XS: -1, G, and x's own base targets when they do not reach a free mover or a
NOREACH mover via fixed edges; options of G[i]: -1, G[j] (j > i), and the movers in R0 that do not reach a free / NOREACH mover.
A mover in XS never points to another mover of XS (acyclic).
Usage: pgad.py BASE TARGET PREFIX XS G OUTPREFIX [R0]   (lists like 13 / 11,13 / 56-58; R0 default 0-63; env NOREACH default 14,15;
       env SKIP=list drops these core movers' constraints (culprit diagnosis); env CNF=path writes DIMACS instead of solving)
Prints RESULT SAT (decoded genome written to OUTPREFIX_dec.txt + sha1) or RESULT UNSAT."""
import sys, os, time, hashlib
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '..', 'l12'))
import enc32_lcomp as enc32
def rng(sp):
    out = []
    for part in sp.split(','):
        if '-' in part: a, b = map(int, part.split('-')); out += list(range(a, b + 1))
        elif part: out.append(int(part))
    return out
base, tp, PREFIX, XS, G, outp = sys.argv[1], sys.argv[2], int(sys.argv[3]), rng(sys.argv[4]), rng(sys.argv[5]), sys.argv[6]
R0 = rng(sys.argv[7]) if len(sys.argv) > 7 else list(range(64))
D = enc32.rdgen(base); S, nc = enc32.rdtarget(tp); H = nc // 2; xt = D['xt']; N = 2 * D['d']
S = S[:PREFIX + 1]
F = XS + G; Fset = set(F)
NOREACH = set(rng(os.environ.get('NOREACH', '14,15')))
reach = set(Fset) | NOREACH; ch = True
while ch:
    ch = False
    for m in range(2 * N):
        if m // 2 in Fset: continue
        if xt[m] in reach and m // 2 not in reach: reach.add(m // 2); ch = True
ok = lambda z: z not in reach
cand = {}
for x in XS:
    own = [z for z in (xt[2 * x], xt[2 * x + 1]) if z >= 0 and ok(z)]
    for k in (0, 1): cand[2 * x + k] = sorted(set([-1] + G + own))
for i, g in enumerate(G):   # v2: a helper also keeps its own base target when acyclic (so the k+1 question contains the k one)
    for k in (0, 1):
        own = [xt[2 * g + k]] if xt[2 * g + k] >= 0 and (ok(xt[2 * g + k]) or xt[2 * g + k] in G[i + 1:]) else []
        cand[2 * g + k] = sorted(set([-1] + G[i + 1:] + [z for z in R0 if ok(z)] + own))
freerank = sorted(cand)
enc32.SKIPCORE.clear(); enc32.SKIPCORE.update(rng(os.environ.get('SKIP', '')))
print('PGAD base', os.path.basename(base), hashlib.sha1(open(base, 'rb').read()).hexdigest()[:8], 'target', os.path.basename(tp),
      'prefix', PREFIX, 'XS', XS, 'G', G, 'NOREACH', sorted(NOREACH), 'R0 ok', [z for z in R0 if ok(z)],
      'cand sizes', {m: len(v) for m, v in cand.items()}, 'SKIP', sorted(enc32.SKIPCORE), flush=True)
cnfp = os.environ.get('CNF'); cl = []
if cnfp: sink = cl.append
else:
    from pysat.solvers import Solver
    sv = Solver(name='cadical195'); sink = sv.add_clause
t0 = time.time()
try:
    E, info, ctx = enc32.build(D, S, H, {'ranks'}, sink=sink, freerank=freerank, cand_in=cand, fixpoint=False)
except SystemExit as e:
    print('RESULT UNSAT (blocked at build:', e, ')'); sys.exit()
# FIX (L-LOWER 13): enc32's --freerank leaves the order among free options in the SAME insertion slot unconstrained (no
# transitivity), so a model may use a cyclic order that decode() cannot realize (found on C4 k 1 prefix 10: SAT, decoded genome
# rejected by enc32 --fix all at prefix 3). Ban both 3-cycles of every triple of free options. A sound strengthening: UNSAT
# verdicts without it remain valid (the unfixed encoding is a relaxation); SAT models with it decode to a strict total order.
fl = sorted(freerank); ordl = ctx['ordl']; ntr = 0
for i in range(len(fl)):
    for j in range(i + 1, len(fl)):
        for k in range(j + 1, len(fl)):
            a, b, c = fl[i], fl[j], fl[k]
            sink([-ordl(a, b), -ordl(b, c), -ordl(c, a)]); sink([-ordl(a, c), -ordl(c, b), -ordl(b, a)]); ntr += 2
info['transitivity_clauses'] = ntr
info['build_s'] = round(time.time() - t0, 1); print('INFO', info, flush=True)
if cnfp:
    with open(cnfp, 'w') as f:
        f.write(f'p cnf {E.nv} {len(cl) + (1 if E.empty else 0)}\n')
        if E.empty: f.write('0\n')
        for c in cl: f.write(' '.join(map(str, c)) + ' 0\n')
    print('CNF ->', cnfp, hashlib.sha1(open(cnfp, 'rb').read()).hexdigest()); sys.exit()
if E.empty: print('RESULT UNSAT (empty clause at build)'); sys.exit()
t1 = time.time(); r = sv.solve(); print(f'SOLVE -> {"SAT" if r else "UNSAT"} {time.time() - t1:.1f}s', flush=True)
if not r: print('RESULT UNSAT'); sys.exit()
M = set(l for l in sv.get_model() if l > 0)
Gn = enc32.decode(D, M, ctx, H); enc32.wrgen(Gn, outp + '_dec.txt')
print('RESULT SAT decoded ->', outp + '_dec.txt', hashlib.sha1(open(outp + '_dec.txt', 'rb').read()).hexdigest())
# self-check: the decoded genome, everything fixed (enc32 checker mode), must realize the same prefix
from pysat.solvers import Solver as _S
cv = _S(name='cadical195')
try:
    E2, _, _ = enc32.build(Gn, S, H, {'ranks', 'signs', 'gates', 'starts'}, sink=cv.add_clause, fixpoint=False)
    ok2 = (not E2.empty) and cv.solve()
except SystemExit as e:
    ok2 = False
print('CHECK decoded genome, all fixed, prefix', PREFIX, '->', 'SAT (consistent)' if ok2 else 'UNSAT (DECODE MISMATCH)')
