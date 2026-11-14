#!/usr/bin/env python3
"""L-RED 71 R247: EXHAUSTIVE search for the longest run of a one-sided rule (default RF) on small parity games.
Instances: n vertices with priorities prio[v] = v (every game with distinct priorities is isomorphic to one of these), every owner
assignment (MODE two) or every vertex Even (MODE one), every choice of nonempty successor sets of size <= D, every start (one successor
per Even vertex). Prints the maximum number of iterations, the number of instances attaining it, the histogram of maxima per game, and one
witness (PGSolver text + start line); with Howard's maximum over the same instances for comparison.
Usage: exh247.py N D MODE [RULE=rf] [PART=i/k]   (PART splits the enumeration of successor-set tuples by index mod k)"""
import sys, os, itertools, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r237")]
import si247, rf247

if __name__ == "__main__":
    n, D, mode = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; rule = sys.argv[4] if len(sys.argv) > 4 else "rf"
    pi, pk = (int(x) for x in sys.argv[5].split("/")) if len(sys.argv) > 5 else (0, 1)
    sets = [list(c) for d in range(1, D + 1) for c in itertools.combinations(range(n), d)]
    owners = [tuple([0] * n)] if mode == "one" else list(itertools.product((0, 1), repeat=n))
    best = (-1, None); cnt = 0; games = runs = 0; hbest = -1; t0 = time.time(); hist = {}
    for idx, succ in enumerate(itertools.product(sets, repeat=n)):
        if idx % pk != pi: continue
        for own in owners:
            ev = [v for v in range(n) if own[v] == 0]
            if not ev: continue
            e = si247.SI(list(range(n)), list(own), [list(s) for s in succ]); games += 1; gmax = 0
            for ch in itertools.product(*[succ[v] for v in ev]):
                st = dict(zip(ev, ch)); r = e.run(rule, dict(st), cap=10000); runs += 1
                assert not r["capped"]
                if r["its"] > gmax: gmax = r["its"]
                if r["its"] > best[0]: best = (r["its"], (own, succ, st)); cnt = 1
                elif r["its"] == best[0]: cnt += 1
            hist[gmax] = hist.get(gmax, 0) + 1
    own, succ, st = best[1]
    e = si247.SI(list(range(n)), list(own), [list(s) for s in succ]); h = e.run("howard", dict(st))["its"]
    print("EXH247 n", n, "D", D, "mode", mode, "rule", rule, "part", f"{pi}/{pk}", "games", games, "runs", runs, "max_its", best[0], "attained_by", cnt,
          "howard_its_on_witness", h, "secs", f"{time.time() - t0:.0f}", flush=True)
    print("EXH247 histogram of per-game maxima:", " ".join(f"{k}:{hist[k]}" for k in sorted(hist)), flush=True)
    print("EXH247 witness:", f"parity {n - 1}; " + " ".join(f"{v} {v} {own[v]} {','.join(map(str, succ[v]))};" for v in range(n)) + " % start " + " ".join(f"{v}:{w}" for v, w in sorted(st.items())), flush=True)
