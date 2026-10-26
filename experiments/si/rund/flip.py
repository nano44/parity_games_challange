#!/usr/bin/env python3
"""L-SI box 18 (successor 14): trace of one phase for note §24 (relay flips). Per transition t of the phase starting at state P: Even switches
(v: old -> new, with v's position: on a class exit path of which terminal), and per q in QS: kappa change, sigma-bar, the exits of
succ(q) (class form, relay.exits), and whether the event is ROUTE / RELAY. Usage: flip.py GAME [START] P q1,q2,..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, HERE)
from n5x import step, start_pair, Engine, dual, load, readstart
from relay import exits

def main():
    a = sys.argv[1:]; g = load(a[0]); start = readstart(a[1]) if len(a) == 4 else None; P = int(a[-2]); QS = [int(x) for x in a[-1].split(",")]
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]; Qs = set(Q)
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        nxt = [s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)]
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), vs=vs, sb=list(sb), nxt=nxt, s=list(s), t=tuple(t), fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    j = P
    while j + 1 < len(rows) and rows[j + 1]["key"] == rows[P]["key"]: j += 1
    c0 = {q: rows[P]["vs"][q][0] for q in QS}
    print(f"phase states {P}..{j}; classes {c0}; D at start {[u for u in Q if rows[P]['sb'][u] != rows[P]['t'][u]]}")
    for k in range(P, j):
        A, B = rows[k], rows[k + 1]
        sw = [(v, A["s"][v], B["s"][v]) for v in range(g.n) if g.owner[v] == 0 and A["s"][v] != B["s"][v]]
        ex = {q: exits(A["nxt"], q, c0[q], Qs, g.succ) for q in QS}
        where = {}
        for (v, o, nw) in sw:
            where[v] = sorted({(q, e) for q in QS for (y, p, e) in ex[q] if v in p or v == y})
        line = [f"t={k - P}{' FB' if A['fb'] else ''} sw={[(v, o, nw, where[v]) for (v, o, nw) in sw]}"]
        for q in QS:
            ch = tuple(A["vs"][q]) != tuple(B["vs"][q])
            eb = exits(B["nxt"], q, c0[q], Qs, g.succ)
            kind = "" if not ch else ("ROUTE" if ex[q] != eb else "RELAY")
            exa = [(y, e) for (y, p, e) in ex[q]]; exb = [(y, e) for (y, p, e) in eb]
            line.append(f"   q={q} {kind} sb {A['sb'][q]}->{B['sb'][q]} D={'Y' if A['sb'][q] != A['t'][q] else 'n'} exits {exa}{' -> ' + str(exb) if exb != exa else ''}"
                        f" lev={(A['vs'][q][1] ^ B['vs'][q][1]).bit_length() - 1 if ch else ''}")
        print("\n".join(line))

if __name__ == "__main__":
    main()
