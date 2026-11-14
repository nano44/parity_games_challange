#!/usr/bin/env python3
"""g10k.py DIR OUT [mode]: gauntlet step 2 on a corpus: for every .pg in DIR run n13 (regions + strategies), compare regions with
Oink (unoptimised Zielonka, --uzlk, -w 0 single thread default) and verify both strategies with harness/verify.py.
OUT gets one line per game; the last line is the summary."""
import sys, os, glob, subprocess, tempfile
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = subprocess.run(['git', '-C', HERE, 'rev-parse', '--show-toplevel'], capture_output=True, text=True).stdout.strip()
sys.path.insert(0, ROOT + '/experiments/harness')
import pg, verify
import n13
OINK = ROOT + '/tools/oink/build/oink'
mode = sys.argv[3] if len(sys.argv) > 3 else 'alt+'

def one(f):
    g = pg.read(f)
    succ = [sorted(set(s)) for s in g.succ]
    R = n13.solve(g.n, g.owner, g.prio, succ, mode, cap=100000)
    with tempfile.NamedTemporaryFile(suffix='.sol', delete=False) as t: sol = t.name
    subprocess.run([OINK, '--uzlk', f, sol], capture_output=True, text=True, timeout=300)
    ref = [None] * g.n
    for line in open(sol):
        q = line.rstrip(';\n').split()
        if q and q[0].isdigit(): ref[int(q[0])] = int(q[1])
    os.unlink(sol)
    if R.status != 'done': st = 'CAP'
    elif R.win != ref: st = 'MISMATCH'
    elif verify.check(g, R.win, R.strat): st = 'BADSTRAT'
    else: st = 'OK'
    return '%s n %d m %d d %d jumps %d peels %d work %d maxbits %d wbits %d %s' % (os.path.basename(f), g.n, g.m, len(set(g.prio)), R.jumps, R.peels, R.work, R.maxbits, R.wbits, st)

if __name__ == '__main__':
    files = sorted(glob.glob(os.path.join(sys.argv[1], '*.pg')))
    cnt = {}; mj = 0; tot = 0; mx = None
    with Pool(3) as pool, open(sys.argv[2], 'w') as out:
        for r in pool.imap(one, files, chunksize=8):
            out.write(r + '\n')
            p = r.split(); cnt[p[-1]] = cnt.get(p[-1], 0) + 1; j = int(p[8]); tot += j
            if j > mj: mj = j; mx = r
        s = 'SUMMARY games %d %s total jumps %d max jumps %d (%s)' % (len(files), ' '.join('%s %d' % kv for kv in sorted(cnt.items())), tot, mj, mx)
        out.write(s + '\n'); print(s)
