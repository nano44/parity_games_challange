"""L-RED box 26 (produced on Opus 5.5): along an N5 run (n5tr.trace replica of experiments/new/n5.py, counts asserted equal to
n5.run), for each player: the number of moves made at each size |I| of the mover's improving set, the number of improving edges
the move takes (switched vertices), how often a player WAITS (I nonempty, no move), and the largest number of visited strategies
sharing one improving set (R58 Lemma 1: at most 2n(n-1)+1). Usage: movehist.py G.pg [STARTFILE]"""
import io, os, sys
from collections import Counter, defaultdict
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, os.path.join(R, "experiments", "red", "n5"))
import n5tr  # noqa: E402
import n5  # noqa: E402
import pg  # noqa: E402
from si import Engine  # noqa: E402


def run(g, st=None):
    buf = io.StringIO(); it, fb, _ = n5tr.trace(g, st, None, 10 ** 9, buf)
    lines = [l for l in buf.getvalue().splitlines() if "| O:" in l]
    res = {}
    for side, tag in (("Even", "E:"), ("Odd", "O:")):
        mv, wait, take = Counter(), Counter(), Counter()
        for l in lines:
            k = int(l.split("|Is| ")[1].split()[0]) if side == "Even" else int(l.split("|It| ")[1].split()[0])
            part = l.split("| E:")[1].split("| O:")[0] if side == "Even" else l.split("| O:")[1]
            sw = [t for t in part.split() if t != "-"]
            if sw:
                mv[k] += 1; take[len(sw)] += 1
            elif k:
                wait[k] += 1
        res[side] = (mv, wait, take)
    return it, fb, res


def replay_share(g, st=None):
    """Replays n5.run's loop (same Engine calls as n5.py, mode n5) and returns, per player, max #visited strategies per I."""
    n = g.n
    E, Ed = Engine(g), Engine(n5.dual(g))
    sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    if st:
        for v, w in st[0].items(): sigma[v] = w
        for v, w in st[1].items(): tau[v] = w
    sh = (defaultdict(set), defaultdict(set))
    while True:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        sh[0][frozenset(Is)].add(tuple(sigma)); sh[1][frozenset(It)].add(tuple(tau))
        if not Is and not It: break
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
            if Is:
                for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
            else:
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        sigma, tau = ns, nt
    return tuple(max((len(s) for s in d.values()), default=0) for d in sh)


if __name__ == "__main__":
    path = sys.argv[1]
    g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
    st = n5tr.read_start(sys.argv[2]) if len(sys.argv) > 2 else None
    it, fb, res = run(g, st)
    se, so = replay_share(g, st)
    print(f"{os.path.basename(path)} n {g.n} iterations {it} fallback {fb}; max visited strategies per improving set: Even {se}, Odd {so}")
    for side in ("Even", "Odd"):
        mv, wait, take = res[side]
        print(f"  {side}: moves by |I|: " + " ".join(f"{k}:{mv[k]}" for k in sorted(mv)) + f" | waits by |I|: " +
              " ".join(f"{k}:{wait[k]}" for k in sorted(wait)) + " | switches per move: " + " ".join(f"{k}:{take[k]}" for k in sorted(take)))
