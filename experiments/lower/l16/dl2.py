#!/usr/bin/env python3
"""L-LOWER 16: decision lists of two signals for a client (after celem2.py): value(t) = c if tr1[t] = v1 else tr2[t] (tr2 may be
negated: W sets contain both polarities). tr1 from base + W1, tr2 from base + W1 + W2. Bitmask search on the required rows lo..P.
Usage: dl2.py GENOME TARGET P CLIENTS lo"""
import sys, os, subprocess, ast, runpy
sys.argv = sys.argv[:6]
here = os.path.dirname(os.path.abspath(__file__))
G, tp, P, CL, lo = sys.argv[1], sys.argv[2], int(sys.argv[3]), [int(c) for c in sys.argv[4].split(',')], int(sys.argv[5])
saved = sys.argv[:]; sys.argv = [saved[0], G, tp, str(P), '0', str(lo)]
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    try: g = runpy.run_path(os.path.join(here, 'celem2.py'), run_name='lib')
    except Exception as e: raise
base, W1, W2 = g['base'], g['W1'], g['W2']
def mask(tr, rows): return sum(1 << i for i, t in enumerate(rows) if tr[t])
for x in CL:
    l = subprocess.run([sys.executable, os.path.join(here, '..', 'l13', 'reqpref.py'), G, tp, str(x), str(P)], capture_output=True, text=True).stdout
    req = [(t, r) for t, r in ast.literal_eval(l[l.index('['):l.index('] |') + 1]) if t >= lo]
    rows = [t for t, r in req]; full = (1 << len(rows)) - 1; R = sum(1 << i for i, (t, r) in enumerate(req) if r)
    A1 = {}
    for W in (base, W1):
        for tr, why in W.items(): A1.setdefault(mask(tr, rows), why)
    A2 = {}
    for W in (base, W1, W2):
        for tr, why in W.items(): A2.setdefault(mask(tr, rows), why)
    hits = []
    for a, why1 in A1.items():
        for br in (a, full & ~a):          # rows taking the first branch (tr1 = v1)
            for c in (0, 1):
                if (R & br) != (br if c else 0): continue
                rest = full & ~br
                need = R & rest
                for b, why2 in A2.items():
                    if (b & rest) == need: hits.append((why1, br == a, c, why2)); break
                if len(hits) > 5: break
            if len(hits) > 5: break
        if len(hits) > 5: break
    print('client', x, 'rows', lo, '..', P, 'DL2 hits', len(hits))
    for h in hits[:5]: print('   ', h)
