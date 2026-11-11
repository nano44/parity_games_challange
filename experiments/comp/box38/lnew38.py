#!/usr/bin/env python3
"""L-COMP box 38: SECOND engine for N5'-xi run to the end = L-NEW's code, imported read-only from a checkout (env LNEW):
gamma3.build(G, eg195.PADS) (box 189) -> eg195.topg -> n5v.step mode "xi" (box 190, S4a [N5XI] + S4b + fallback) from
n5x.start_pair (S3), as asc197.run builds it. --noelev: gamma3's e-priority key (lev, gate) replaced by (gate) (the box 33 enum33.py
patch, asserted to hit exactly once). Counters as full38.py: T3 = passes before the first fallback, Ttot = total passes
(len(states) - 1), F = fallback passes.  Usage: LNEW=<dir> lnew38.py G.json [...] [--noelev]"""
import sys, os, types, json
LNEW = os.environ["LNEW"]
sys.path[:0] = [os.path.join(LNEW, p) for p in ("experiments/new/box197", "experiments/new/box196", "experiments/new/box195", "experiments/new/box191",
                "experiments/new/box189", "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
for k in ("ROOT", "Q196_ROOT", "EG195_ROOT"): os.environ.setdefault(k, LNEW)
NOELEV = "--noelev" in sys.argv
if NOELEV:
    src = open(os.path.join(LNEW, "experiments/new/box189/gamma3.py")).read()
    old = 'sorted(O, key=lambda q: (lev[q[0]], gate[q[0]][q[1]]))): prio[V[("e", q)]]'
    assert src.count(old) == 1, "gamma3 e-priority line not found"
    src = src.replace(old, 'sorted(O, key=lambda q: gate[q[0]][q[1]])): prio[V[("e", q)]]')
    mod = types.ModuleType("gamma3"); mod.__file__ = os.path.join(LNEW, "experiments/new/box189/gamma3.py")
    exec(compile(src, mod.__file__, "exec"), mod.__dict__); sys.modules["gamma3"] = mod
import gamma3, eg195, n5v, n5x


def full(G, cap=100000):
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0)
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    passes = F = 0; first = None
    while passes < cap:
        r = n5v.step(g, E, Ed, sigma, tau, "xi")
        if r is None: break
        sigma, tau, _, _, fb = r; passes += 1
        if fb:
            F += 1
            if first is None: first = passes
    else:
        raise RuntimeError("cap")
    return dict(T3=(first - 1) if first is not None else passes, Ttot=passes, F=F, first=first, n=g.n)


if __name__ == "__main__":
    for f in [a for a in sys.argv[1:] if not a.startswith("--")]:
        print(os.path.basename(f), json.dumps(full(json.load(open(f)))))
