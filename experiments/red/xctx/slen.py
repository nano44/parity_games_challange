"""L-RED successor 9 (box 14, produced on Opus 5.5): class climb maximising the longest q-phase S (then NEST, then -n) with
vertex insertions, to read S against n on 𝒞^1P. Logs every improvement as "it (S, NEST, -n)"; NEUTRAL=1 makes the last component +n (size-neutral ties accept growth). Usage: [GROW=p NMAX=m]
DTL_ORDER=.. slen.py climb C START.pg STEPS SEED OUTDIR"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xscore as X, nestclass as NC


def score(g, order, C):
    P, d = NC.positions(g, order, C)
    if not P: return (0, 0, 0)
    return (max(len(p) + 1 for p in P.values()), max(NC.nest(p) for p in P.values()), g.n if os.environ.get("NEUTRAL") == "1" else -g.n)


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    NC.score = score
    NC.climb(int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), sys.argv[6], order)
