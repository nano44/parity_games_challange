"""Self-check for kl2.py (no Oink): Algorithm 1 invariants + label-setting == naive lifting at every pivot (--check),
regions == py Zielonka, strategies pass verify.py, primal/dual regions agree; R1 and R2 (seeds 1-3), both tau_1 options.
Usage: selfcheck.py [COUNT] [NMAX]. Exit 1 on any failure."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "harness"))
sys.path.insert(0, HERE)
import exhaustive  # noqa: E402
import gen  # noqa: E402
import verify  # noqa: E402
import zielonka  # noqa: E402
import kl2  # noqa: E402


def one(g, tag):
    ref = zielonka.solve(g)
    for rule, seed in (("r1", 1), ("r2", 1), ("r2", 2), ("r2", 3)):
        for tau1 in ("first", "min"):
            win, strat, _, _ = kl2.solve(g, rule, seed, tau1, check=True)
            if win != ref:
                return f"{tag} {rule} s{seed} {tau1}: MISMATCH"
            errs = verify.check(g, win, strat)
            if errs:
                return f"{tag} {rule} s{seed} {tau1}: BADSTRAT {errs[:2]}"
    return None


def main():
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 9
    bad = 0
    k = 0
    for i, g in enumerate(exhaustive.iter_games(2, 2)):        # all 324 games, n = 2, P = 2
        e = one(g, f"exh{i}"); k += 1
        if e:
            print(e); bad += 1
    for s in range(count):
        n = 1 + s % nmax
        d = 1 + (s * 7) % (n + 2)
        g = gen.random_game(n, d, 1, 3, 20261023 + s)
        e = one(g, f"rand{s}(n={n},d={d})"); k += 1
        if e:
            print(e); bad += 1
    print(f"kl2 selfcheck: {k} games x 8 runs, {bad} failures: {'PASS' if bad == 0 else 'FAILED'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
