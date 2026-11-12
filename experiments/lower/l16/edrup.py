#!/usr/bin/env python3
"""L-LOWER 16: DRUP check of one ekr2.py UNSAT (env passed through: LEVEL, KEEPO, KEEPR, ...): CNF (ekr2.py with env CNF), Glucose4 with
proof, l8/sat/drup.c; prints CNF sha1, clauses, lemmas and drup's verdict, then deletes proof and CNF.
Usage: edrup.py DRUP WORKDIR GENOME TARGET K P CLIENT EXT"""
import sys, os, subprocess, hashlib
drup, wd = sys.argv[1], sys.argv[2]; a = sys.argv[3:]
here = os.path.dirname(os.path.abspath(__file__))
cnf = os.path.join(wd, 'ed_%s_%s_%s_%d.cnf' % (a[2], a[3], a[4], os.getpid()))
subprocess.run([sys.executable, os.path.join(here, 'ekr2.py')] + a + ['/dev/null'], check=True, stdout=subprocess.DEVNULL, env=dict(os.environ, CNF=cnf))
sha = hashlib.sha1(open(cnf, 'rb').read()).hexdigest()
from pysat.formula import CNF
from pysat.solvers import Glucose4
F = CNF(from_file=cnf); s = Glucose4(bootstrap_with=F.clauses, with_proof=True)
tag = 'edrup %s K %s P %s client %s EXT %s env LEVEL=%s KEEPO=%s KEEPR=%s' % (os.path.basename(a[0]), a[2], a[3], a[4], a[5],
      os.environ.get('LEVEL', '8'), os.environ.get('KEEPO', '0'), os.environ.get('KEEPR', '0'))
if s.solve(): print(tag, 'SAT (not UNSAT!)'); os.remove(cnf); sys.exit(1)
pf = cnf + '.proof'; Pr = s.get_proof()
with open(pf, 'w') as f: f.writelines(l + '\n' for l in Pr)
out = subprocess.run([drup, cnf, pf], capture_output=True, text=True).stdout.strip().splitlines()
print(tag, '| cnf sha1', sha, 'clauses', len(F.clauses), 'lemmas', len(Pr), '| drup:', out[-1] if out else 'NO OUTPUT')
os.remove(pf); os.remove(cnf)
