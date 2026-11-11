#!/usr/bin/env python3
"""L-LOWER 15: DRUP check of one kr.py UNSAT: CNF (kr.py with env CNF), Glucose4 with proof, l8/sat/drup.c; prints CNF sha1 and
drup's verdict, then deletes proof and CNF. Usage: kdrup.py DRUP WORKDIR GENOME TARGET K P CLIENTS"""
import sys, os, subprocess, hashlib
drup, wd = sys.argv[1], sys.argv[2]; a = sys.argv[3:]
here = os.path.dirname(os.path.abspath(__file__))
cnf = os.path.join(wd, 'kd_%s_%s_%s.cnf' % (a[2], a[3], a[4].replace(',', '-')))
subprocess.run([sys.executable, os.path.join(here, 'kr.py')] + a, check=True, stdout=subprocess.DEVNULL, env=dict(os.environ, CNF=cnf))
sha = hashlib.sha1(open(cnf, 'rb').read()).hexdigest()
from pysat.formula import CNF
from pysat.solvers import Glucose4
F = CNF(from_file=cnf); s = Glucose4(bootstrap_with=F.clauses, with_proof=True)
if s.solve(): print('kdrup K', a[2], 'P', a[3], 'clients', a[4], 'SAT (not UNSAT!)'); os.remove(cnf); sys.exit(1)
pf = cnf + '.proof'; Pr = s.get_proof()
with open(pf, 'w') as f: f.writelines(l + '\n' for l in Pr)
out = subprocess.run([drup, cnf, pf], capture_output=True, text=True).stdout.strip().splitlines()
print('kdrup K', a[2], 'P', a[3], 'clients', a[4], '| cnf sha1', sha, 'clauses', len(F.clauses), 'lemmas', len(Pr), '| drup:', out[-1] if out else 'NO OUTPUT')
os.remove(pf); os.remove(cnf)
