"""REFEREE probe (R-PROVED2, First-Difference Lemma (ii)): run L-ALG's own checker logic (experiments/alg/dtl_fdlcheck.py,
positional alignment of the tattr logs of consecutive searches of a phase) on random games, and report the first transition
where the first differing tattr has a different caller or input. Usage: DTL_ORDER=oink|stable fdl_random.py N0 N1 SEEDS"""
import sys, os
A = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "experiments", "alg")
sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
import pg, gen, dtl_fdlcheck as CKM
FD = CKM.FD
sys.setrecursionlimit(100000)
n0, n1, seeds = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
tr = bad = 0
for n in range(n0, n1 + 1):
    for seed in range(seeds):
        g = gen.random_game(n, max(2, n // 2 + 1), 1, 3, seed)
        d0 = FD.P.X.build(g); d = CKM.CK(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx
        try: d.run()
        except Exception as e: continue
        for ph in FD.phase_rows(d):
            for a, b in zip(ph, ph[1:]):
                la = [e for e in a["log"] if e[0] != "extract"]; lb = [e for e in b["log"] if e[0] != "extract"]
                k = 0
                while k < min(len(la), len(lb)) and la[k][:4] == lb[k][:4]: k += 1
                if k == min(len(la), len(lb)): continue
                tr += 1; x, y = la[k], lb[k]
                if not (x[0] == y[0] and x[1] == y[1] and x[2] == y[2] and x[4] == y[4] and y[3] > x[3]):
                    bad += 1
                    if bad <= 3:
                        print("VIOLATION n=%d seed=%d p=%s s:%s s+1:%s" % (n, seed, a["p"], x[:3], y[:3]), flush=True)
                        pg.write(g, f"/tmp/claude-0/-home-user-parity-games-challange/dd5ebe7b-7043-55cd-9853-fe494d411400/scratchpad/fdl_v_{os.environ.get('DTL_ORDER','stable')}_n{n}_s{seed}.pg")
print(os.environ.get("DTL_ORDER", "stable"), "transitions", tr, "violations", bad)
