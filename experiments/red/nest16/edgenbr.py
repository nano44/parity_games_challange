"""L-RED box 16 (produced on Opus 5.5): the full single-edge neighbourhood of a class game (add one edge from a C-vertex, or remove one
edge from a C-vertex with >= 2 successors), scored by starclimb.score. Prints the best few and saves NEST* >= base+1.
Usage: DTL_ORDER=.. edgenbr.py G.pg OUTDIR"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "xctx"))
import xscore as X, starclimb as SC
sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
g = X.distinct(X.pg.read(sys.argv[1])); C = X.controller(g); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
sb = SC.score(g, order, C); print("base", sb, flush=True); res = []
for v in range(g.n):
    if g.owner[v] != C: continue
    for w in range(g.n):
        succ = [list(s) for s in g.succ]
        if w in succ[v]:
            if len(succ[v]) < 2: continue
            succ[v].remove(w); mv = f"-{v}>{w}"
        else:
            succ[v] = sorted(succ[v] + [w]); mv = f"+{v}>{w}"
        h = X.pg.Game(list(g.prio), list(g.owner), succ)
        if not X.inclass(h, C): continue
        try:
            sh = SC.score(h, order, C)
        except RecursionError:
            continue
        res.append((sh, mv))
        if sh[0] > sb[0]: print("HIT", mv, sh, flush=True); X.pg.write(h, os.path.join(out, f"nbr_{mv.replace('>', '_')}_{sh[0]}.pg"))
res.sort(reverse=True)
for r in res[:8]: print(r)
