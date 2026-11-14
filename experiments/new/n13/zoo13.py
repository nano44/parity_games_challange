#!/usr/bin/env python3
"""zoo13.py MODE OUT: n13 on every .pg file under experiments/ (all lanes' instances), regions against Oink --tl.
One line per file: path n m d jumps peels work maxbits status verdict; last line SUMMARY."""
import sys, os, subprocess, tempfile, glob
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = subprocess.run(['git', '-C', HERE, 'rev-parse', '--show-toplevel'], capture_output=True, text=True).stdout.strip()
import n13
OINK = ROOT + '/tools/oink/build/oink'
mode = sys.argv[1]

def one(f):
    try:
        n, owner, pr, succ, ids = n13.read_pg(f)
        if n == 0: raise ValueError('empty')
    except Exception as e:
        return '%s PARSEERR' % os.path.relpath(f, ROOT)
    R = n13.solve(n, owner, pr, succ, mode, cap=50000)
    with tempfile.NamedTemporaryFile(suffix='.sol', delete=False) as t: sol = t.name
    v = 'REFERR'
    try:
        subprocess.run([OINK, '--tl', f, sol], capture_output=True, text=True, timeout=300)
        ref = {}
        for line in open(sol):
            q = line.rstrip(';\n').split()
            if q and q[0].isdigit(): ref[int(q[0])] = int(q[1])
        refw = [ref[i] for i in ids]
        v = 'OK' if (R.status == 'done' and R.win == refw) else ('CAP' if R.status != 'done' else 'MISMATCH')
    except Exception:
        pass
    finally:
        if os.path.exists(sol): os.unlink(sol)
    return '%s n %d m %d d %d jumps %d peels %d work %d maxbits %d %s %s' % (os.path.relpath(f, ROOT), n, sum(map(len, succ)), len(set(pr)), R.jumps, R.peels, R.work, R.maxbits, R.status, v)

if __name__ == '__main__':
    files = sorted(f for f in glob.glob(ROOT + '/experiments/**/*.pg', recursive=True) if '/new/n13/' not in f)
    cnt = {}; mj = 0; tot = 0; mx = ''
    with Pool(3) as pool, open(sys.argv[2], 'w') as out:
        for r in pool.imap(one, files, chunksize=8):
            out.write(r + '\n')
            p = r.split(); cnt[p[-1]] = cnt.get(p[-1], 0) + 1
            if p[-1] != 'PARSEERR':
                j = int(p[8]); tot += j
                if j > mj: mj = j; mx = p[0]
        s = 'SUMMARY mode %s files %d %s total jumps %d max jumps %d (%s)' % (mode, len(files), ' '.join('%s %d' % kv for kv in sorted(cnt.items())), tot, mj, mx)
        out.write(s + '\n'); print(s)
