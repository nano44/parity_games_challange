#!/usr/bin/env python3
"""Step (c) of C1.md: random games n = NMIN..NMAX, K per n, varied priorities/degrees/owner mix (harness gen.py, seeded).
For each game: smallest k <= KMAX with NE(k) complete; soundness against Zielonka at every k; on every game NE(k)
solves, oracle-extracted positional strategies are verified with harness verify.py when --strat is given (slower).
Games needing k >= 2 (or unsolved at KMAX) are written to out/random_hard_<tag>.jsonl.
Usage: random_test.py NMIN NMAX K SEED [--kmax 3] [--strat] [--tag T]"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import alglib, zielonka


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    nmin, nmax, K, seed = map(int, args[:4])
    opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    kmax = int(opt("--kmax", 3)); tag = opt("--tag", f"n{nmin}-{nmax}_K{K}_s{seed}"); ws = "--strat" in sys.argv
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    rnd = alglib.gen.Rng(f"alg-random|{seed}")
    hist, unsound, hard = {}, 0, []
    t0 = time.time()
    with open(os.path.join(HERE, "out", f"random_hard_{tag}.jsonl"), "w") as ff:
        for n in range(nmin, nmax + 1):
            for i in range(K):
                d = rnd.choice([2, 3, 4, max(2, n // 2), n, n + 1])
                dmin = rnd.choice([1, 1, 2]); dmax = dmin + rnd.choice([0, 1, 2, n])
                peven = rnd.choice([0.0, 0.3, 0.5, 0.7, 1.0]); sl = rnd.random() < 0.7
                g = alglib.random_game(n, d, dmin, dmax, rnd.randrange(2**31), peven, sl)
                ref = zielonka.solve(g)
                k, undec, verd = alglib.k_needed(g, ref, kmax, with_strat=ws)
                key = (n, k)
                hist[key] = hist.get(key, 0) + 1
                if k == "UNSOUND":
                    unsound += 1
                if ws and verd and (verd["verify"] or verd["strat_fail"]):
                    hist[(n, "STRAT")] = hist.get((n, "STRAT"), 0) + 1
                    ff.write(json.dumps(alglib.game_record(g, ref, k=k, undec=undec, verd=str(verd))) + "\n")
                if k == "UNSOUND" or k is None or k >= 2:
                    rec = alglib.game_record(g, ref, k=k, undec=undec, verd=str(verd))
                    ff.write(json.dumps(rec) + "\n"); hard.append(rec)
            print(f"n={n}: " + ", ".join(f"k={k}:{c}" for (nn, k), c in sorted(hist.items(), key=str) if nn == n)
                  + f"  ({time.time()-t0:.0f}s)", flush=True)
    print(f"total games {K*(nmax-nmin+1)}, unsound {unsound}, needing k>=2 or unsolved: {len(hard)}; "
          f"by k: " + ", ".join(f"{k}:{sum(c for (nn, kk), c in hist.items() if kk == k)}" for k in list(range(kmax+1)) + [None, 'UNSOUND']))


if __name__ == "__main__":
    main()
