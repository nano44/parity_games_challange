"""L-RED box 26 (produced on Opus 5.5): fate of the improving edges N5 DECLINES (R58 §3). Replays n5.py's loop (mode n5; same Engine
calls; counts asserted equal to n5.run). At each iteration t the mover (Even: I = Is; Odd: I = It) declines D_t = I_t minus the
switches it takes (all of I_t if it waits). For every declined edge e = (v, w) we record what happens next at v:
  TAKEN-LATER  v later switches to w while (v, w) is improving (the switch was deferred),
  DROPPED      (v, w) stops being improving before v switches to w (or v switches elsewhere first),
  END          still declined when the run stops (cannot happen: the run stops with I empty).
Usage: declines.py G.pg [STARTFILE]"""
import os, sys
from collections import Counter
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, os.path.join(R, "experiments", "red", "n5"))
import n5tr  # noqa: E402
import n5  # noqa: E402
import pg  # noqa: E402
from si import Engine  # noqa: E402


def states(g, st=None):
    n = g.n
    E, Ed = Engine(g), Engine(n5.dual(g))
    sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    if st:
        for v, w in st[0].items(): sigma[v] = w
        for v, w in st[1].items(): tau[v] = w
    out = []; it = fb = 0
    while True:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        out.append((tuple(sigma), tuple(tau), frozenset(Is), frozenset(It)))
        if not Is and not It: break
        it += 1
        ns, nt = list(sigma), list(tau)
        if Is:
            opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
            for v, w in Is: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
            _, best = Engine(n5.dual(pg.Game(list(g.prio), list(g.owner), succ))).evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 0: ns[v] = best[v]
        if It:
            opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
            for v, w in It: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
            _, best = Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 1: nt[v] = best[v]
        if ns == sigma and nt == tau:
            fb += 1
            if Is:
                for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
            else:
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        sigma, tau = ns, nt
    ref = n5.run(g, "n5", st); assert (it, fb) == ref[:2], (it, fb, ref[:2])
    return out


def fates(seq, side):
    k = 0 if side == "Even" else 1; I = 2 if side == "Even" else 3
    c = Counter(); lag = []
    for t in range(len(seq) - 1):
        s, s2 = seq[t][k], seq[t + 1][k]
        for (v, w) in seq[t][I]:
            if s2[v] == w: continue          # taken now
            # declined at t: follow v
            u = t + 1; fate = "END"
            while u < len(seq):
                if (v, w) not in seq[u][I]: fate = "DROPPED"; break
                if u + 1 < len(seq) and seq[u + 1][k][v] != seq[u][k][v]:
                    fate = "TAKEN-LATER" if seq[u + 1][k][v] == w else "DROPPED"; break
                u += 1
            c[fate] += 1
            if fate == "TAKEN-LATER": lag.append(u - t)
    return c, lag


if __name__ == "__main__":
    path = sys.argv[1]
    g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
    st = n5tr.read_start(sys.argv[2]) if len(sys.argv) > 2 else None
    seq = states(g, st)
    for side in ("Even", "Odd"):
        c, lag = fates(seq, side)
        print(f"{os.path.basename(path)} {side}: declined edge-events {sum(c.values())}: {dict(c)}; deferral lag max {max(lag, default=0)}")
