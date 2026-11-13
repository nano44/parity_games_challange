#!/usr/bin/env python3
"""L-LOWER 19: DRUP check of one enc19 UNSAT (l13/pdrup.py's procedure): builds the CNF (enc19 with env CNF, same env VAL / SB),
solves it with pysat Glucose4 with proof, runs l8/sat/drup.c, prints CNF sha1, clauses, lemmas, solve time and drup's last line,
then deletes proof and CNF (the same command regenerates them). Usage: drup19.py DRUP WORKDIR enc19-args...  (e.g. 2,2 5 len)"""
import sys, os, subprocess, hashlib, time
drup, wd = sys.argv[1], sys.argv[2]; args = sys.argv[3:]
here = os.path.dirname(os.path.abspath(__file__))
cnf = os.path.join(wd, 'd19_' + '_'.join(args).replace(',', '-') + '.cnf')
subprocess.run([sys.executable, os.path.join(here, 'enc19.py')] + args, check=True, stdout=subprocess.DEVNULL, env=dict(os.environ, CNF=cnf))
sha = hashlib.sha1(open(cnf, 'rb').read()).hexdigest()
from pysat.formula import CNF
from pysat.solvers import Glucose4
F = CNF(from_file=cnf); s = Glucose4(bootstrap_with=F.clauses, with_proof=True); t0 = time.time(); r = s.solve(); ts = time.time() - t0
if r: print('drup19', ' '.join(args), 'SAT (not UNSAT!)'); os.remove(cnf); sys.exit(1)
pf = cnf + '.proof'; P = s.get_proof()
with open(pf, 'w') as f: f.writelines(l + '\n' for l in P)
out = subprocess.run([drup, cnf, pf], capture_output=True, text=True).stdout.strip().splitlines()
print('drup19 enc19', ' '.join(args), 'VAL', os.environ.get('VAL', 'ro'), 'SB', os.environ.get('SB', '1'), '| cnf sha1', sha, 'clauses', len(F.clauses),
      'lemmas', len(P), f'glucose {ts:.1f}s', '| drup:', out[-1] if out else 'NO OUTPUT')
os.remove(pf); os.remove(cnf)
