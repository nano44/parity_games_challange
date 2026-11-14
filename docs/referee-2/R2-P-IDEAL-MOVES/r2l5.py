# REFEREE-2 successor 30: C129 E-1/E-2 measurements with my own r2moves.py simulator (no lane code).
import sys, os, glob, json, itertools, hashlib
import r2moves as M
root = sys.argv[1]
files = sorted(f for f in glob.glob(os.path.join(root, 'box1[5-8][0-9]/**/*.json'), recursive=True)
               if 150 <= int(os.path.relpath(f, root)[3:6]) <= 187)
runs = eqZ = eqS = 0
for f in files:
    try: raw = json.load(open(f))
    except Exception: continue
    if not isinstance(raw, dict) or 'opts' not in raw: continue
    try: g = M.G(raw)
    except Exception: continue
    if not g.ok_lr(): continue
    starts = list(itertools.product((0, 1), repeat=g.N)) if g.N <= 10 else [tuple(g.start)]
    for st in starts:
        S = g.run(list(st)); T = len(S) - 1; runs += 1
        Z = {o[1] for ox in g.O for o in ox if o[1] != M.X}
        Mv = [None] + [{x for x in range(g.N) if S[t][x] != S[t - 1][x]} for t in range(1, T + 1)]
        zst = sum(1 for t in range(1, T) if Mv[t] & Z)
        smv = sum(sum(1 for t in range(1, T + 1) if z in Mv[t]) for z in Z)
        eqZ += T == 1 + zst; eqS += T == 1 + smv
print('E-1 runs %d  T=1+#{t<=T-1: Mv_t cap Z nonempty} on %d  T=1+sum_z moves(z) on %d' % (runs, eqZ, eqS))
for f, st in [('box186/out/pass_d3_D3.json', '110100'), ('box186/out/pass_d4_D4.json', '01010111')]:
    raw = open(os.path.join(root, f), 'rb').read(); g = M.G(json.loads(raw))
    for s0 in ([int(c) for c in st], list(g.start)):
        S = g.run(s0); print('E-2 %s sha1 %s start %s T %d' % (f, hashlib.sha1(raw).hexdigest()[:8], ''.join(map(str, s0)), len(S) - 1))
