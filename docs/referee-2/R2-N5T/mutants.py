"""Mutation tests: each mutant breaks one definition; the checker must then report failures."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vjbf
orig_phi, orig_le = vjbf.phi, vjbf.pv_le
def run(name):
    st = vjbf.new_stats(); vjbf.exhaustive3(st)
    print(name, {k: v for k, v in st.items() if not k.endswith('_ex')})
# M1: phi with the sign of epsilon flipped
vjbf.phi = lambda g, s, Om: -orig_phi(g, s, Om); run('M1 phi sign flipped')
vjbf.phi = orig_phi
# M2: lengths compared the wrong way round (R+ longer better)
def le2(g, x, y):
    (l, B, k), (l2, B2, k2) = x, y
    if l != l2 or B != B2: return orig_le(g, x, y)
    return k <= k2 if g.plus(l) else k2 <= k
vjbf.pv_le = le2; run('M2 length order reversed')
vjbf.pv_le = orig_le
# M3: phi summed over all (+) vertices, not only cycle nodes
vjbf.phi = lambda g, s, Om: sum((1 if not g.plus(v) else -1) * Om[s[v]][2] for v in s); run('M3 phi over all vertices')
