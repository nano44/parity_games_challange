#!/usr/bin/env python3
"""L-LOWER 16: C-element designer. In the R104 model a mover w of level L >= 1 moves at step u iff better_w(S_(u-1)) = c_L(u) !=
s_(u-1)(w), with c_L(u) = o(L-1)(S_u): w is a Muller C-element of (better_w delayed one row, key). If better_w = b or 1-b for a
single mover b (copy wiring; R105 ENC with b's options top-ranked in w's chains), w's trajectory is determined by b, the key row
pattern and w's start. This script takes the CLAMPED run of GENOME (core forced to TARGET, l7/clamp) on rows 0..P, and for each
client x and each (level L, source b, negation, start) lists the C-element trajectories that match x's required list on rows
lo..P (up to the client sign). It ignores the feedback of w's own pair on o(L) and above (checked later by simulation).
Usage: celem.py GENOME TARGET P CLIENTS [lo]"""
import sys, os, subprocess, ast
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '..', 'l6')); sys.path.insert(0, os.path.join(here, '..', 'l7'))
import sim6, clamp
G, tp, P, CL = sys.argv[1], sys.argv[2], int(sys.argv[3]), [int(c) for c in sys.argv[4].split(',')]
lo = int(sys.argv[5]) if len(sys.argv) > 5 else 0
D = sim6.rd(G); T = open(tp).read().split(); tg = [[int(c) for c in T[2 + i]] for i in range(P + 1)]
tgt = [r + (D['start'][16:] if t == 0 else [0] * 48) for t, r in enumerate(tg)]
S = clamp.runclamp(D, tgt, set(range(16))); K = [sim6.okeys(D, list(s)) for s in S]
for x in CL:
    l = subprocess.run([sys.executable, os.path.join(here, '..', 'l13', 'reqpref.py'), G, tp, str(x), str(P)], capture_output=True, text=True).stdout
    req = [(t, r) for t, r in ast.literal_eval(l[l.index('['):l.index('] |') + 1]) if t >= lo]
    hits = []
    for L in range(8, 32):
        for b in range(64):
            for nb in (0, 1):
                for w0 in (0, 1):
                    w = [w0]
                    for u in range(1, P + 1):
                        bb = S[u - 1][b] ^ nb; c = K[u][L - 1]
                        w.append(c if (bb == c and w[-1] != c) else w[-1])
                    for nx in (0, 1):
                        if all((w[t] ^ nx) == r for t, r in req): hits.append((L, b, nb, w0, nx, ''.join(map(str, w))))
    print('client', x, 'rows', lo, '..', P, 'hits', len(hits))
    for h in hits[:12]: print('  L %d src %d neg %d start %d clientneg %d traj %s' % h)
