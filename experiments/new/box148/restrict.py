#!/usr/bin/env python3
"""L-NEW box 148 RESTRICT: check of Lemma INTERVAL-RESTRICT and the per-interval unchained counts.
Split a run at the falls of TOP_1 (box 147: TOP_1 falls at t iff RANK_t = 1, i.e. the top unstable mover m moves). On an interval
[a, b) (states s_a .. s_(b-1), steps a+1 .. b-1 inside, TOP_1 constant) every mover with pi >= pi(m) is static. Build the RESTRICTED
genome: each mover with pi >= pi(m) keeps only its current option (deg 1), start = s_a; run it (R178 §1 rule, box139/paths.py) and
check that s_a .. s_(b-1) is a prefix of its run (PREFIXVIOL must be 0). Also count, per interval, the unchained steps of the original
run strictly inside it (UNCH_IN) and the active movers (pi < pi(m)). Prints the list of (active, UNCH_IN, length) per interval.
Usage: restrict.py genome.json ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(HERE, "..", "box147", "stat.py")
ns = {"__file__": os.path.abspath(P)}; exec(open(P).read().split('\nif __name__')[0], ns); analyse, run = ns["analyse"], ns["run"]
def restricted(G, s, keep):
    H = json.loads(json.dumps(G)); st = list(s)
    for x in keep:
        H["opts"][x] = [G["opts"][x][s[x]]]; H["gate"][x] = [G["gate"][x][s[x]]]; st[x] = 0
    H["start"] = st; return H
def intervals(G, R):
    S, FS, pos = R["S"], R["FS"], R["pos"]; n = G["N"]; T = len(S) - 1
    top = lambda s: max((pos[x] for x in range(n) if FS[s]["UNST"][x]), default=-1)
    cuts = [0] + [t for t in range(1, T + 1) if top(t) != top(t - 1)] + [T + 1]
    return [(cuts[i], cuts[i + 1]) for i in range(len(cuts) - 1)], top
if __name__ == "__main__":
    for p in sys.argv[1:]:
        G = json.load(open(p)); R = analyse(G); S, pos, lab = R["S"], R["pos"], R["lab"]; n = G["N"]
        ivs, top = intervals(G, R); viol = 0; rows = []
        for a, b in ivs:
            pm = top(a)
            if pm < 0: rows.append((0, 0, b - a)); continue
            keep = [x for x in range(n) if pos[x] >= pm]; H = restricted(G, S[a], keep)
            S2 = run(H, cap=5000)[0]
            want = [tuple(0 if x in keep else S[t][x] for x in range(n)) for t in range(a, b)]
            viol += [tuple(v) for v in S2[:len(want)]] != want
            rows.append((pm, sum(1 for t in range(a + 1, b) if t in lab and not lab[t]), b - a))
        U = sum(1 for c in lab.values() if not c)
        print(f"RESTRICT {os.path.basename(p)} N {n} STEPS {R['T']} U {U} INTERVALS {len(ivs)} PREFIXVIOL {viol} MAXUNCH_IN {max(r[1] for r in rows)} "
              f"(active, unch_in, len): {rows}", flush=True)
