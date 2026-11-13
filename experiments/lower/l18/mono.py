#!/usr/bin/env python3
"""L-LOWER 18 (successor 16): horizon monotonicity check for pgad6 / n.sh questions (Lead ruling 02:22Z, condition 1).
Builds the DIMACS of one n.sh question (XALL, XORD, FIXC 16,17) at two horizons Ra < Rb (env CNF) with enc32c.Enc.new instrumented:
every variable gets a structural name (source line of the allocation, the row index t of the enclosing frame if any, running count
within that (line, t)). Variable numbers differ between horizons (state variables of all rows are allocated before the transitions),
so the check maps each Ra variable (except the unused row-(Ra+1) gates, see below) to the Rb variable with the same name and tests that every Ra clause, renamed, is an Rb clause.
INCLUDED => the Rb formula contains the Ra formula (up to renaming) => UNSAT at Ra implies UNSAT at Rb for the same clients.
Usage: mono.py BASE P XS XORD Ra Rb WORKDIR      (internal: mono.py --wrap OUTKEYS pgad6-args...)"""
import sys, os, subprocess, pickle, runpy
here = os.path.dirname(os.path.abspath(__file__))
if sys.argv[1] == '--wrap':
    keys_out = sys.argv[2]; sys.argv = [os.path.join(here, 'pgad6.py')] + sys.argv[3:]
    sys.path.insert(0, here); sys.path.insert(0, os.path.join(here, '..', 'l13'))
    import enc32c
    names = [None]; cnt = {}
    def new(s):
        f = sys._getframe(1); line = f.f_lineno; t = None; g = f
        for _ in range(12):
            if g is None: break
            if 't' in g.f_locals and isinstance(g.f_locals['t'], int): t = g.f_locals['t']; break
            g = g.f_back
        k = (line, t); cnt[k] = cnt.get(k, 0) + 1
        s.nv += 1; names.append((line, t, cnt[k])); return s.nv
    enc32c.Enc.new = new
    try: runpy.run_path(sys.argv[0], run_name='__main__')
    except SystemExit: pass
    pickle.dump(names, open(keys_out, 'wb')); sys.exit()
B, P, XS, XO, Ra, Rb, wd = sys.argv[1:8]
def build(R):
    p = os.path.join(wd, f'mono_R{R}.cnf'); kp = p + '.keys'
    env = dict(os.environ, F6R=R, XALL='1', XORD=XO, FIXC='16,17', CNF=p)
    subprocess.run(['python3', os.path.abspath(__file__), '--wrap', kp, B, os.path.join(here, '..', 'l10/out/core8_HIT7.txt'), P, XS, '',
                    os.path.join(wd, 'mono_dummy')], env=env, check=True, capture_output=True)
    names = pickle.load(open(kp, 'rb'))
    with open(p) as f:
        nv = int(f.readline().split()[2]); cl = [list(map(int, l.split()[:-1])) for l in f]
    os.remove(p); os.remove(kp); assert len(names) == nv + 1, (len(names), nv)
    return names, cl
na, A = build(Ra); nb, Bc = build(Rb)
idx = {n: v for v, n in enumerate(nb) if v}
assert len(idx) == len(nb) - 1, 'names not unique at Rb'
unmapped = sum(1 for v in range(1, len(na)) if na[v] not in idx)
ren = lambda l: (1 if l > 0 else -1) * idx[na[abs(l)]]
SB = set(tuple(sorted(c)) for c in Bc)
# X = Ra variables named with row t = Ra + 1 (enc32c builds O[t] for t in range(T + 2); O[T + 1] is read only with fixpoint, which
# pgad6 does not use). Core = Ra clauses without an X variable: each must occur in Rb after renaming. X clauses: each must have its
# largest variable in X, and for every X variable v (increasing order) the clauses whose largest variable is v must be satisfiable by
# some value of v under EVERY assignment of their other variables (checked by enumeration). Then any Rb model, renamed back, satisfies
# the core and extends over X in increasing order: Rb SAT => Ra SAT, i.e. UNSAT at Ra => UNSAT at Rb.
X = {v for v in range(1, len(na)) if na[v][1] == int(Ra) + 1}
miss = 0; xcl = {}; bad = 0
for c in A:
    if any(abs(l) in X for l in c):
        m = max(abs(l) for l in c)
        if m not in X: bad += 1
        else: xcl.setdefault(m, []).append(c)
        continue
    try:
        if tuple(sorted(ren(l) for l in c)) not in SB:
            miss += 1
            if miss <= int(os.environ.get('SHOWMISS', '0')): print('MISS', [(l, na[abs(l)]) for l in c])
    except KeyError: miss += 1
from itertools import product
noext = 0
for v, cs in xcl.items():
    oth = sorted({abs(l) for c in cs for l in c} - {v}); assert len(oth) <= 16, (v, len(oth))
    for bits in product((False, True), repeat=len(oth)):
        a = dict(zip(oth, bits))
        if not any(all(any((a[abs(l)] if l > 0 else not a[abs(l)]) if abs(l) != v else (val if l > 0 else not val) for l in c) for c in cs)
                   for val in (False, True)): noext += 1; break
ok = miss == 0 and bad == 0 and noext == 0
print(f'MONO base {os.path.basename(B)} P {P} XS {XS} XORD {XO} | R {Ra}: vars {len(na)-1} clauses {len(A)} | R {Rb}: vars {len(nb)-1}'
      f' clauses {len(Bc)} | Ra vars without an Rb name {unmapped} | row-{int(Ra)+1} vars {len(X)}, their clauses {sum(map(len, xcl.values()))},'
      f' not max-var {bad}, not extendable {noext} | core clauses missing from Rb after renaming {miss} | {"INCLUDED" if ok else "NOT INCLUDED"}')
