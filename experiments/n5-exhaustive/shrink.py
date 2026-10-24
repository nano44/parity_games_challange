#!/usr/bin/env python3
"""Greedy shrink of a C^1O game + start pair while a property holds (default: some theta-driven (A) re-entry in a joint
lambda-phase). Moves, repeated to a fixpoint: delete a vertex (redirecting nothing: edges into it are dropped; a vertex left
without successors makes the move invalid), delete an edge, drop a vertex's start choice to another successor, lower a priority
(compress). The start pair is restricted accordingly. Usage: shrink.py IN.pg IN.start|- OUT_PREFIX [--prop A|canonA]  (canonA: from the canonical start; pass - as start)"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import exh  # noqa: E402
from exh import pg, trace  # noqa: E402


def prop(g, start, mode):
    try:
        if sum(1 for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1) != 1:
            return False
        o = exh.odd_choice(g)
        st, _ = trace(g, None if mode == "canonA" else start, check=False)
        return len(st) > 2 and exh.analyse(g, st, o)["reA"] > 0
    except Exception:
        return False


def delete_vertex(g, start, x):
    keep = [v for v in range(g.n) if v != x]; idx = {v: i for i, v in enumerate(keep)}
    succ = []
    for v in keep:
        s = [idx[w] for w in g.succ[v] if w != x]
        if not s:
            return None
        succ.append(s)
    h = pg.Game([g.prio[v] for v in keep], [g.owner[v] for v in keep], succ)
    st = None
    if start:
        st = []
        for side in start:
            d = {}
            for v, w in side.items():
                if v == x:
                    continue
                d[idx[v]] = idx[w] if w != x else succ[idx[v]][0]
            st.append(d)
        st = tuple(st)
    return h, st


def main():
    g = pg.read(sys.argv[1]); start = exh.readstart(sys.argv[2]) if sys.argv[2] != "-" else None; outp = sys.argv[3]
    mode = sys.argv[sys.argv.index("--prop") + 1] if "--prop" in sys.argv else "A"
    assert prop(g, start, mode), "property does not hold on the input"
    changed = True
    while changed:
        changed = False
        for x in range(g.n - 1, -1, -1):
            r = delete_vertex(g, start, x)
            if r and prop(r[0], r[1], mode):
                g, start = r; changed = True; break
        if changed:
            continue
        for v in range(g.n):
            for w in list(g.succ[v]):
                if len(g.succ[v]) < 2:
                    continue
                succ = [list(s) for s in g.succ]; succ[v].remove(w)
                st = tuple({a: (b if not (a == v and b == w) else succ[v][0]) for a, b in side.items()} for side in start) \
                    if start else None
                h = pg.Game(g.prio, g.owner, succ)
                if prop(h, st, mode):
                    g, start = h, st; changed = True; break
            if changed:
                break
        if changed:
            continue
        for v in range(g.n):                                     # lower priorities (keep parity)
            if g.prio[v] >= 2:
                pr = list(g.prio); pr[v] -= 2; h = pg.Game(pr, g.owner, g.succ)
                if prop(h, start, mode):
                    g = h; changed = True; break
    pg.write(g, outp + ".pg")
    if start:
      with open(outp + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(start[0].items())) + "\n")
        f.write("TAU0 " + " ".join(f"{v}:{w}" for v, w in sorted(start[1].items())) + "\n")
    st, _ = trace(g, start if mode != "canonA" else None, check=False)
    print(f"shrunk to n {g.n}, m {sum(len(s) for s in g.succ)}: {exh.analyse(g, st, exh.odd_choice(g))}")


if __name__ == "__main__":
    main()
