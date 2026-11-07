#!/usr/bin/env python3
"""REFEREE-2 succ. 30: my own replay (r2moves.py class G, R104 text; no lane code) of the 9 genomes in L-RED's
experiments/red/r214/lower3/ (claude/l-red 6e743ab1), from the stored start, compared row by row with that commit's replay.out
(section 3: d, T, max mover, its level, Xi-target, moves, 2d, >2d, moves per mover, F per level = moves of the level's two
movers, as lowrep.py l. 11 defines it).
Usage: r2m2d9.py LOWER3_DIR REPLAY_OUT"""
import sys, os, json, hashlib, re
H = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(H, '..', 'R2-P-IDEAL-MOVES', 'r2moves.py')).read().split("\nif __name__")[0]
ns = {'__name__': 'lib'}; a = sys.argv; sys.argv = ['x']; exec(src, ns); sys.argv = a
G, X = ns['G'], ns['X']
rows = {}
for line in open(sys.argv[2], encoding='utf-8'):
    if line.startswith('# 4.'): break
    m = re.match(r'(\S+\.json): d (\d+) T (\d+) end \S+ \| max mover (\d+) lev (\d+) Xi-target (\d) moves (\d+) 2d (\d+) (\S+) \| moves (\[[^\]]*\]) \| F (\[[^\]]*\])', line)
    if m: rows[m.group(1)] = m.groups()[1:]
ok = 0
for f in sorted(os.listdir(sys.argv[1])):
    if not f.endswith('.json'): continue
    raw = open(os.path.join(sys.argv[1], f), 'rb').read(); g = G(json.loads(raw)); N = g.N; d = N // 2
    S = g.run(g.start); T = len(S) - 1
    Z = {o[1] for ox in g.O for o in ox if o[1] != X}
    mv = [sum(S[t][x] != S[t - 1][x] for t in range(1, T + 1)) for x in range(N)]
    best = max(range(N), key=lambda x: (mv[x], -x))
    F = [mv[2 * l] + mv[2 * l + 1] for l in range(d)]   # lowrep.py l. 11: F per level = moves of its two movers
    mine = (str(d), str(T), str(best), str(g.lev[best]), str(int(best in Z)), str(mv[best]), str(2 * d),
            '>2d' if mv[best] > 2 * d else '<=2d', str(mv), str(F))
    theirs = rows.get(f)
    eq = theirs == mine; ok += eq
    print('%s sha1 %s lr %s acyclic %s | mine d %s T %s max mover %s lev %s Xi-target %s moves %s 2d %s %s | moves %s | F %s | EQUAL %s'
          % ((f, hashlib.sha1(raw).hexdigest()[:8], g.ok_lr(), g.acyclic()) + mine + (eq,)))
    if not eq: print('   theirs', theirs)
print('ROWS EQUAL %d / %d' % (ok, len(rows)))
