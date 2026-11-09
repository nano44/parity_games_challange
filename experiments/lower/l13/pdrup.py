#!/usr/bin/env python3
"""L-LOWER 13: DRUP check of one pgad.py UNSAT. Builds the CNF (pgad.py with env CNF), solves it with pysat Glucose4 with proof,
runs l8/sat/drup.c, prints CNF sha1, clause count, lemma count and drup's last line, then DELETES proof and CNF (disk trap; the
same command regenerates the CNF). Usage: pdrup.py DRUP WORKDIR BASE TARGET PREFIX XS G [R0]   (env SKIP passed through)"""
import sys, os, subprocess, hashlib
drup, wd = sys.argv[1], sys.argv[2]; args = sys.argv[3:]
here = os.path.dirname(os.path.abspath(__file__))
cnf = os.path.join(wd, 'pd_' + '_'.join(os.path.basename(a).replace('.txt', '') for a in args).replace(',', '-') + '.cnf')
p = args[:5] + ['/dev/null'] + args[5:]
subprocess.run([sys.executable, os.path.join(here, os.environ.get('PGAD', 'pgad.py'))] + p, check=True, stdout=subprocess.DEVNULL, env=dict(os.environ, CNF=cnf))
sha = hashlib.sha1(open(cnf, 'rb').read()).hexdigest()
from pysat.formula import CNF
from pysat.solvers import Glucose4
F = CNF(from_file=cnf); s = Glucose4(bootstrap_with=F.clauses, with_proof=True); r = s.solve()
if r: print('pdrup', ' '.join(args), 'SAT (not UNSAT!)'); os.remove(cnf); sys.exit(1)
pf = cnf + '.proof'; P = s.get_proof()
with open(pf, 'w') as f: f.writelines(l + '\n' for l in P)
out = subprocess.run([drup, cnf, pf], capture_output=True, text=True).stdout.strip().splitlines()
print('pdrup', os.environ.get('PGAD', 'pgad.py'), ' '.join(args), 'SKIP', os.environ.get('SKIP', ''), '| cnf sha1', sha, 'clauses', len(F.clauses), 'lemmas', len(P),
      '| drup:', out[-1] if out else 'NO OUTPUT')
os.remove(pf); os.remove(cnf)
