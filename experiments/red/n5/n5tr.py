"""L-RED box 25 (produced on Opus 5.5): per-iteration trace of N5 (experiments/new/n5.py, read-only), with each switch classified
against SSI (2309.02223 Algorithm 2): an Even switch v -> w is SSI-type iff w == tau_bar(v) (Even's best reply to tau, on the dual),
an Odd switch iff w == sigma_bar(v) (Odd's best reply to sigma). The loop is n5.run's loop line for line (same Engine calls); the
script asserts at the end that its iteration and fallback counts equal n5.run's.
Usage: n5tr.py G.pg [--start SIGFILE] [--names] [--max K]  (start file: two lines 'SIGMA0 v:w ...' / 'TAU0 v:w ...')"""
import os
import re
import sys

R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
for d in ("new", "si", "harness"):
    sys.path.insert(0, os.path.join(R, "experiments", d))
import n5  # noqa: E402
import pg  # noqa: E402
from si import Engine  # noqa: E402


def names_of(path):
    out = {}
    for line in open(path):
        m = re.match(r'^\s*(\d+)\s.*"([^"]*)"', line)
        if m:
            out[int(m.group(1))] = m.group(2)
    return out


def read_start(fn):
    sig, tau = {}, {}
    for line in open(fn):
        t = line.split()
        if not t:
            continue
        d = sig if t[0] == "SIGMA0" else tau
        for x in t[1:]:
            v, w = map(int, x.split(":"))
            d[v] = w
    return sig, tau


def trace(g, start=None, nm=None, mx=10 ** 9, out=sys.stdout):
    nm = nm or {}
    N = lambda v: nm.get(v, str(v))  # noqa: E731
    n = g.n
    E, Ed = Engine(g), Engine(n5.dual(g))
    sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    if start:
        for v, w in start[0].items():
            sigma[v] = w
        for v, w in start[1].items():
            tau[v] = w
    it = fb = 0
    stats = {"even_ssi": 0, "even_non": 0, "odd_ssi": 0, "odd_non": 0, "even_moves": 0, "odd_moves": 0}
    while True:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        if not Is and not It:
            break
        it += 1
        ns, nt = list(sigma), list(tau)
        if Is:
            opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
            for v, w in Is:
                opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
            Er = Engine(n5.dual(pg.Game(list(g.prio), list(g.owner), succ)))
            _, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 0:
                    ns[v] = best[v]
        if It:
            opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
            for v, w in It:
                opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
            Er = Engine(pg.Game(list(g.prio), list(g.owner), succ))
            _, best = Er.evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 1:
                    nt[v] = best[v]
        fbk = False
        if ns == sigma and nt == tau:
            fb += 1; fbk = True
            if Is:
                for v in {v for v, _ in Is}:
                    ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
            else:
                for v in {v for v, _ in It}:
                    nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        ev = []
        for v in range(n):
            if g.owner[v] == 0 and ns[v] != sigma[v]:
                ssi = ns[v] == tbar[v]
                stats["even_ssi" if ssi else "even_non"] += 1
                ev.append(f"{N(v)}>{N(ns[v])}{'' if ssi else '*'}")
        od = []
        for v in range(n):
            if g.owner[v] == 1 and nt[v] != tau[v]:
                ssi = nt[v] == sbar[v]
                stats["odd_ssi" if ssi else "odd_non"] += 1
                od.append(f"{N(v)}>{N(nt[v])}{'' if ssi else '*'}")
        stats["even_moves"] += bool(ev); stats["odd_moves"] += bool(od)
        if it <= mx:
            print(f"{it}{' FB' if fbk else ''}: |Is| {len(Is)} |It| {len(It)} | E: {' '.join(ev) or '-'} | O: {' '.join(od) or '-'}", file=out)
        sigma, tau = ns, nt
    ref = n5.run(g, "n5", start)
    assert (it, fb) == (ref[0], ref[1]), f"trace {it},{fb} != n5.run {ref[0]},{ref[1]}"
    print(f"iterations {it} fallback {fb} (= n5.run); {stats}  (* = not the SSI switch)", file=out)
    return it, fb, stats


if __name__ == "__main__":
    path = sys.argv[1]
    g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
    st = read_start(sys.argv[sys.argv.index("--start") + 1]) if "--start" in sys.argv else None
    mx = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 10 ** 9
    trace(g, st, names_of(path) if "--names" in sys.argv else None, mx)
