"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4), GAP-A-M §18j: does the FULL actual state (the round sequence, i.e. every
death) at one context revisit an earlier value within one phase, with T only growing in between? Reports, per context
with >= 3 calls in one phase, revisits of the full round sequence and of the return set alone, and whether the ideal (C6)
result stayed the same over the revisit. Usage: DTL_ORDER=oink dtl_revisit.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_regvec as RV, pg

def retset(r): return r[-2] if len(r) > 1 and not r[-1] else r[-1]

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = {}
    def inc(k): tot[k] = tot.get(k, 0) + 1
    for f in sys.argv[1:]:
        g = pg.read(f); d = RV.build(g); d.run(); name = os.path.basename(f)
        phase = {i + 1: (t["p"], t["dom"]) for i, t in enumerate(d.trace)}
        for key, occ in d.calls.items():
            runs, cur = [], []
            for o in occ:      # split into maximal runs of consecutive searches of one phase with T growing
                if cur and not (phase[o[0]] == phase[cur[-1][0]] and o[0] == cur[-1][0] + 1 and set(cur[-1][4]) <= set(o[4])):
                    runs.append(cur); cur = []
                cur.append(o)
            runs.append(cur)
            for run in runs:
                if len(run) < 3: continue
                inc("ctx_runs_3plus")
                for j in range(len(run)):
                    for i in range(j - 1):
                        if any(run[k][1] != run[i][1] for k in range(i + 1, j)):
                            same_ideal = all(run[k][3] == run[i][3] for k in range(i, j + 1))
                            if run[j][1] == run[i][1]:
                                inc("FULL_STATE_REVISIT" + ("_ideal_same" if same_ideal else "_ideal_moved"))
                                print(f"{name} |R|={len(key[1])} full state revisit s{run[i][0]} = s{run[j][0]} ideal same={same_ideal}")
                            elif retset(run[j][1]) == retset(run[i][1]) and any(retset(run[k][1]) != retset(run[i][1]) for k in range(i + 1, j)):
                                inc("returnset_revisit_only" + ("_ideal_same" if same_ideal else "_ideal_moved"))
    print(os.environ.get("DTL_ORDER", "stable"), tot)
