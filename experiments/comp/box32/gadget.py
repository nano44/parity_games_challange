#!/usr/bin/env python3
"""L-COMP box 32 (c): exact test of a FRESH helper gadget for f6 (mover 13) on a base genome (target core8, d 32).
Free movers F = [13] + G (G = movers of levels 28-31 by default: 56..63), in this order. Candidate targets:
  13's options: G, -1, and the extra list X13 (default: 13's own base targets and 18, 60 when they do not reach any free mover);
  options of G[i]: -1, G[j] for j > i, and the fixed movers in R0 (default: pairs 0-5 = movers 0..11) that do not reach any free mover.
Acyclic for every choice: free -> free edges go forward in F, and free -> fixed edges end at movers that never reach a free mover.
Ranks: the base genome's ranks fixed, except the options of F, whose positions are inserted freely (unary insertion encoding).
Signs, helper gate bits, helper starts and helper trajectories free. Constraints: only mover 13's (--only 13) unless ALL=1.
Usage: gadget.py BASE TARGET OUTPREFIX [R0 list e.g. 0-11] [G list e.g. 56-63]"""
import sys, os, time, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import enc32
from pysat.solvers import Solver
def rng(sp): 
    out = []
    for part in sp.split(','):
        if '-' in part: a, b = map(int, part.split('-')); out += list(range(a, b + 1))
        elif part: out.append(int(part))
    return out
base, tp, outp = sys.argv[1], sys.argv[2], sys.argv[3]
R0 = rng(sys.argv[4]) if len(sys.argv) > 4 else list(range(12))
G = rng(sys.argv[5]) if len(sys.argv) > 5 else list(range(56, 64))
D = enc32.rdgen(base); S, nc = enc32.rdtarget(tp); H = nc // 2; xt = D['xt']; N = 2 * D['d']
F = [13] + G; Fset = set(F)
# movers reaching a free mover (or a NOREACH mover, default 14, 15 = pair 7: Lead 10:41Z, the carrier must not take its timing
# from pair 7) via fixed edges; gadget movers may point only to movers outside this set
NOREACH = set(rng(os.environ.get('NOREACH', '14,15')))
reach = set(Fset) | NOREACH; ch = True
while ch:
    ch = False
    for m in range(2 * N):
        if m // 2 in Fset: continue
        if xt[m] in reach and m // 2 not in reach: reach.add(m // 2); ch = True
ok = lambda z: z not in reach
X13 = [z for z in (xt[26], xt[27], 18, 60) if z >= 0 and ok(z)]
cand = {}
for k in (0, 1): cand[26 + k] = sorted(set([-1] + G + X13))
for i, g in enumerate(G):
    for k in (0, 1): cand[2 * g + k] = sorted(set([-1] + G[i + 1:] + [z for z in R0 if ok(z)]))
freerank = sorted(cand)
only = set(range(2 * H)) - ({13} if not os.environ.get('ALL') else set(range(2 * H)))
enc32.SKIPCORE.clear(); enc32.SKIPCORE.update(only)
info_c = {m: len(v) for m, v in cand.items()}
print('GADGET NOREACH', sorted(NOREACH), 'base', os.path.basename(base), hashlib.sha1(open(base, 'rb').read()).hexdigest()[:8], 'F', F, 'R0 ok', [z for z in R0 if ok(z)],
      'X13', X13, 'cand sizes', info_c, flush=True)
sv = Solver(name='cadical195')
t0 = time.time()
E, info, ctx = enc32.build(D, S, H, {'ranks'}, sink=sv.add_clause, freerank=freerank, cand_in=cand)
info['build_s'] = round(time.time() - t0, 1); print('INFO', info, flush=True)
if E.empty: print('RESULT UNSAT (empty clause at build)'); sys.exit()
t1 = time.time(); r = sv.solve(); print(f'SOLVE -> {"SAT" if r else "UNSAT"} {time.time() - t1:.1f}s', flush=True)
if not r: print('RESULT UNSAT'); sys.exit()
M = set(l for l in sv.get_model() if l > 0)
Gn = enc32.decode(D, M, ctx, H); enc32.wrgen(Gn, outp + '_dec.txt')
print('RESULT SAT decoded ->', outp + '_dec.txt', hashlib.sha1(open(outp + '_dec.txt', 'rb').read()).hexdigest())
