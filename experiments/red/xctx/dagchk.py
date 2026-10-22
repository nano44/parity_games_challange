"""L-RED successor 9 (box 14, produced on Opus 5.5): mechanical check of (DAG-1P) on L-ALG's class set. Claim (reading, R42 §2):
in a q-phase search of a 𝒞^1P game, at every search_rec call of depth >= 1 with subgame R, every nontrivial SCC of the fixed
graph on R (q-vertices: their unique edge; C-vertices: all edges into R) lies inside the vertex set of one known tangle
(a self-loop counts as nontrivial). Wraps b12_pot.CH (unmodified) by subclassing. Also counts depth >= 1 calls and their sizes.
Usage: DTL_ORDER=.. [TRIALS=3 SEED=2 NMAX=200] dagchk.py FILES..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xscore as X
B = X.B
from b12_topchain import classgames
STAT = {"calls": 0, "sccs": 0, "bad": 0, "maxR": 0, "ex": None}


def sccs(R, succ):
    idx, low, on, st, out, c = {}, {}, set(), [], [], [0]
    def visit(v):
        idx[v] = low[v] = c[0]; c[0] += 1; st.append(v); on.add(v)
        for w in succ(v):
            if w not in idx: visit(w); low[v] = min(low[v], low[w])
            elif w in on: low[v] = min(low[v], idx[w])
        if low[v] == idx[v]:
            C = []
            while True:
                w = st.pop(); on.discard(w); C.append(w)
                if w == v: break
            out.append(C)
    for v in sorted(R):
        if v not in idx: visit(v)
    return out


class DG(B.CH):
    def search_rec(self, R, p, depth):
        if depth >= 1 and getattr(self, "Cq", None) == p:
            Rs = set(R); STAT["calls"] += 1; STAT["maxR"] = max(STAT["maxR"], len(Rs))
            succ = lambda v: [w for w in self.outs[v] if w in Rs]
            T = [set(w for w, _ in tv) for tv in self.tv]
            for C in sccs(Rs, succ):
                if len(C) == 1 and C[0] not in self.outs[C[0]]: continue
                STAT["sccs"] += 1
                if not any(set(C) <= t for t in T):
                    STAT["bad"] += 1; STAT["ex"] = STAT["ex"] or (getattr(self, "_name", ""), depth, sorted(C))
        return super().search_rec(R, p, depth)


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable"); os.environ["DIST"] = "1"; games = 0
    for name, g in classgames(sys.argv[1:], int(os.environ.get("TRIALS", "3")), int(os.environ.get("SEED", "2")), int(os.environ.get("NMAX", "200"))):
        C = X.controller(g)
        if C is None: continue
        saved = B.SE.SE; DG.Cq = 1 - C; DG._name = name; B.SE.SE = DG
        try:
            B.SE.run(g, order); games += 1
        except RecursionError:
            pass
        finally:
            B.SE.SE = saved
    print("order", order, "class games", games, "q-phase depth>=1 search_rec calls", STAT["calls"], "max |R|", STAT["maxR"],
          "nontrivial SCCs", STAT["sccs"], "outside every tangle", STAT["bad"], "first", STAT["ex"])
