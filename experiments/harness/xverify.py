#!/usr/bin/env python3
"""Cross-check verify.py against Oink's `verify` tool on correct and mutated solutions.
Usage: xverify.py COUNT [SEED]. Mutants: strategy of one winner-owned vertex redirected to another successor,
or the winner of one vertex flipped (its strategy entry adjusted to stay well-formed). Exit 1 on any verdict difference."""
import sys, os, subprocess, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pg, gen, zielonka, verify, solvers

VERIFY = os.path.join(os.path.dirname(solvers.OINK), "verify")


def oink_ok(gpath, win, strat, td):
    sp = os.path.join(td, "s.sol"); pg.write_sol(win, sp, strat)
    p = subprocess.run([VERIFY, gpath, sp], capture_output=True, text=True, timeout=60)
    return p.returncode == 0


def main(count, seed=0):
    diff = stats = 0
    kinds = {"ok": [0, 0], "fail": [0, 0]}
    with tempfile.TemporaryDirectory() as td:
        for i in range(count):
            r = gen.Rng(f"xv|{seed}|{i}")
            n = r.randint(2, 30)
            g = gen.random_game(n, r.randint(1, n + 1), 1, r.randint(1, 4), r.randrange(10**9), r.choice([0.3, 0.5, 0.7]), r.random() < 0.6)
            gp = os.path.join(td, "g.pg"); pg.write(g, gp)
            win, strat = zielonka.solve_with_strategy(g)
            win, strat = list(win), list(strat)
            m = r.randrange(3)
            if m == 1:  # redirect a strategy
                cand = [v for v in range(n) if strat[v] is not None and len(set(g.succ[v])) > 1]
                if cand:
                    v = r.choice(cand); strat[v] = r.choice([w for w in set(g.succ[v]) if w != strat[v]])
            elif m == 2:  # flip one winner
                v = r.randrange(n); win[v] ^= 1
                strat[v] = r.choice(g.succ[v]) if g.owner[v] == win[v] else None
            mine = not verify.check(g, win, strat)
            theirs = oink_ok(gp, win, strat, td)
            kinds["ok" if theirs else "fail"][0 if mine == theirs else 1] += 1
            if mine != theirs:
                diff += 1
                print(f"DIFF game {i}: mine={mine} oink={theirs}\n{pg.dumps(g)}{win}\n{strat}")
                break
    print(f"xverify: {count} solutions (Oink verdict accepted {sum(kinds['ok'])}, rejected {sum(kinds['fail'])}); "
          f"{'all verdicts agree' if not diff else 'VERDICTS DIFFER'}")
    return 1 if diff else 0


if __name__ == "__main__":
    sys.exit(main(int(sys.argv[1]), int(sys.argv[2]) if len(sys.argv) > 2 else 0))
