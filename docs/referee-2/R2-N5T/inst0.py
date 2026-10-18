"""The reading's section 0 instance, evaluated with vjbf.py (VJ00 definitions; plays enumerated)."""
import sys; sys.path.insert(0, __import__('os').path.dirname(__file__))
from vjbf import *
g = Game([2, 6, 0, 1], [0, 1, 0, 0], [[0, 2], [1, 3], [0], [0, 1, 2]])
d = g.dual()   # (+) = Odd of g: owner 0 in d
print('dual prio', d.prio, 'owner', d.owner, 'rank', d.rank)
for s in strategies(d):
    Om = omega(d, s)
    print('tau', s, 'Omega', [(l, sorted(B), k) for l, B, k in Om], 'improvements', improvements(d, s, Om), 'phi', phi(d, s, Om))
