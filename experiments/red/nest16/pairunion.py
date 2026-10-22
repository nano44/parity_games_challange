"""L-RED box 16 (produced on Opus 5.5): disjoint unions B ⊎ A of two class games with the same controller C, for A over a file list,
priorities placed 3 ways (parity kept): 'above' (A shifted above B), 'below' (B shifted above A), 'inter' (f(p) = 2p - p%2 for B,
f(p) + 2 for A). Scored by starclimb.score. Usage: DTL_ORDER=.. pairunion.py B.pg OUTDIR A.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "xctx"))
import xscore as X, starclimb as SC
sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")


def un(b, a, mode):
    mb, ma = max(b.prio), max(a.prio); sh = lambda m: m + 2 + (m % 2)
    if mode == "above": pb, pa = list(b.prio), [p + sh(mb) for p in a.prio]
    elif mode == "below": pb, pa = [p + sh(ma) for p in b.prio], list(a.prio)
    else: f = lambda p: 2 * p - p % 2; pb, pa = [f(p) for p in b.prio], [f(p) + 2 for p in a.prio]
    n = b.n; succ = [list(s) for s in b.succ] + [[w + n for w in s] for s in a.succ]
    return X.pg.Game(pb + pa, list(b.owner) + list(a.owner), succ)


B = X.distinct(X.pg.read(sys.argv[1])); C = X.controller(B); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
sb = SC.score(B, order, C); print("base", sb, flush=True)
for f in sys.argv[3:]:
    A = X.distinct(X.pg.read(f))
    if X.controller(A) != C: continue
    for mode in ("above", "below", "inter"):
        h = un(B, A, mode)
        if not X.inclass(h, C): continue
        h = X.distinct(h)
        try:
            sh = SC.score(h, order, C)
        except RecursionError:
            continue
        print(os.path.basename(f), mode, h.n, sh, flush=True)
        if sh[0] > sb[0]: print("HIT", f, mode, flush=True); X.pg.write(h, os.path.join(out, f"pu_{os.path.basename(f)[:-3]}_{mode}_{sh[0]}.pg"))
