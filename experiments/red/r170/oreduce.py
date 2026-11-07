#!/usr/bin/env python3
"""L-RED R170: greedy ODIFF reduction. Start from a game G with start pair; repeatedly pick an Odd choice vertex v and cut it to one edge
(MODE tau: keep tau_0(v) as given in the start; MODE sbar: keep sbar(v) at the start state of the run; MODE both: try tau, then sbar), and
keep the cut if the longest TWO-FIX window of the new game (same start pair restricted) is at least KEEP (env, default 0.9) times the
current one. Prints the kept cuts and the final (L, ODIFF, number of Odd choice vertices); writes OUT.pg / OUT.start.
Usage: oreduce.py G.pg START OUT_PREFIX [MODE]"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freeze import run, windows, load, readstart, start_pair, Engine, dual
import pg

def longest(g, s, t):
    S, T, F, E = run(g, s, t, cap=20000); W, SB = windows(g, S, T, E)
    if not W: return 0, 0, None
    a, b = max(W, key=lambda w: w[1] - w[0])
    od = sum(1 for v in range(g.n) if g.owner[v] == 1 and SB[a][v] != T[a][v])
    return b - a, od, (a, b, sum(F[a + 1:b + 1]))

def main():
    g = load(sys.argv[1]); st = readstart(sys.argv[2]); out = sys.argv[3]; mode = sys.argv[4] if len(sys.argv) > 4 else "both"
    keep = float(os.environ.get("KEEP", "0.9"))
    names = {}
    for l in open(sys.argv[1]):
        m = re.match(r'\s*(\d+) .*"(\S+)"', l)
        if m: names[int(m.group(1))] = m.group(2)
    s, t = start_pair(g, Engine(g), Engine(dual(g)), st)
    sb0 = Engine(g).evaluate(tuple(s))[1]
    L, od, w = longest(g, s, t); print(f"START L {L} ODIFF {od} window {w}")
    succ = [list(x) for x in g.succ]; changed = True
    while changed:
        changed = False
        for v in range(g.n):
            if g.owner[v] != 1 or len(succ[v]) < 2: continue
            for keepw in ([t[v]] if mode == "tau" else [sb0[v]] if mode == "sbar" else [t[v], sb0[v]]):
                trial = [list(x) for x in succ]; trial[v] = [keepw]
                h = pg.Game(list(g.prio), list(g.owner), trial); t2 = list(t); t2[v] = keepw
                L2, od2, w2 = longest(h, s, t2)
                if L2 >= keep * L:
                    print(f"cut {names.get(v, v)} -> {names.get(keepw, keepw)}: L {L2} ODIFF {od2} window {w2}", flush=True)
                    succ, t, L, od, changed = trial, t2, L2, od2, True; break
    h = pg.Game(list(g.prio), list(g.owner), succ)
    och = sum(1 for v in range(h.n) if h.owner[v] == 1 and len(h.succ[v]) > 1)
    print(f"FINAL L {L} ODIFF {od} oddchoice {och} n {h.n}")
    with open(out + ".pg", "w") as f:
        f.write(f"parity {h.n - 1};\n")
        for v in range(h.n): f.write(f"{v} {h.prio[v]} {h.owner[v]} {','.join(map(str, h.succ[v]))} \"{names.get(v, v)}\";\n")
    with open(out + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in range(h.n) if h.owner[v] == 0) + "\n")
        f.write("TAU0 " + " ".join(f"{v}:{t[v]}" for v in range(h.n) if h.owner[v] == 1) + "\n")

if __name__ == "__main__":
    main()
