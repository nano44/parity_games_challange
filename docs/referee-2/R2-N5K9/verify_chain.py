"""Extract a longest single-switch chain of a game and re-verify every step with vjbf (plays enumerated): each step switches
one improvement (vjbf.improvements) and the pair (Omega, phi) strictly rises (R15 potential)."""
import sys, os, ast, functools; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from onep import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'R2-N5T'))
from vjbf import improvements, phi
gm = ast.literal_eval(sys.argv[1]); g = Game(*gm); P = OneP(g)
@functools.lru_cache(maxsize=None)
def L(t):
    im = P.imps(t); best = (0, None)
    for i in range(len(t)):
        for w in im[i]:
            u = t[:i] + (w,) + t[i + 1:]; c = 1 + L(u)[0]
            if c > best[0]: best = (c, u)
    return best
t = max(P.starts(), key=lambda s: L(s)[0]); chain = [t]
while L(chain[-1])[1] is not None: chain.append(L(chain[-1])[1])
ok = True; flat = 0
for a, b in zip(chain, chain[1:]):
    ra, rb = P.rho(a), P.rho(b); sa = {v: ra[v] for v in range(g.n) if g.owner[v] == 0}; sb = {v: rb[v] for v in range(g.n) if g.owner[v] == 0}
    Oa, Ob = omega(g, sa), omega(g, sb); diff = [(v, sb[v]) for v in sa if sa[v] != sb[v]]
    if len(diff) != 1 or diff[0] not in improvements(g, sa, Oa): ok = False
    if Oa == Ob:
        flat += 1
        if not phi(g, sb, Ob) > phi(g, sa, Oa): ok = False
    elif not all(pv_le(g, Oa[u], Ob[u]) for u in range(g.n)): ok = False
print('chain length', len(chain) - 1, 'flat steps', flat, 'all steps verified' if ok else 'VERIFICATION FAILED')
print('start', dict(zip(P.ev, chain[0])))
