"""L-RED box 16 (produced on Opus 5.5): disjoint union B ⊎ A with a RANDOM interleaving of the two priority orders (each component's
internal order and every vertex's parity kept; priorities reassigned increasing, as xscore.distinct does). Scored by
starclimb.score. Saves NEST* > base. Usage: DTL_ORDER=.. mergesearch.py B.pg A.pg TRIALS SEED OUTDIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "xctx"))
import xscore as X, starclimb as SC


def merge(b, a, rnd):
    n = b.n; ob = sorted(range(b.n), key=lambda v: b.prio[v]); oa = sorted(range(a.n), key=lambda v: a.prio[v])
    par = list(b.prio) + list(a.prio); seq = []; i = j = 0
    while i < len(ob) or j < len(oa):
        if j >= len(oa) or (i < len(ob) and rnd.random() < len(ob) / (len(ob) + len(oa))): seq.append(ob[i]); i += 1
        else: seq.append(n + oa[j]); j += 1
    prio = [0] * (n + a.n); last = -1
    for v in seq:
        p = last + 1
        if p % 2 != par[v] % 2: p += 1
        prio[v] = p; last = p
    succ = [list(s) for s in b.succ] + [[w + n for w in s] for s in a.succ]
    return X.pg.Game(prio, list(b.owner) + list(a.owner), succ)


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    B = X.distinct(X.pg.read(sys.argv[1])); A = X.distinct(X.pg.read(sys.argv[2])); trials, seed, out = int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    C = X.controller(B); rnd = random.Random(seed); os.makedirs(out, exist_ok=True); sb = SC.score(B, order, C); best = sb
    print("base", sb, flush=True)
    for it in range(trials):
        h = merge(B, A, rnd)
        if not X.inclass(h, C): continue
        try:
            sh = SC.score(h, order, C)
        except RecursionError:
            continue
        if sh[0] > sb[0] or sh[:2] > best[:2]:
            print(it, sh, flush=True); X.pg.write(h, os.path.join(out, f"merge_s{seed}_{it}_{sh[0]}_{sh[1]}.pg"))
        if sh[:2] > best[:2]: best = sh
        if it % 100 == 0: print("hb", it, best, flush=True)
    print("final", best)
