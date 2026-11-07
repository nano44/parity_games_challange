#!/usr/bin/env python3
"""Box 192: ACTION-ELIMINATION data (HMZ 1008.0530 style) on IDEAL-CYC: per run, the number of re-adoptions (a mover switches to an
option it held earlier and left), the max over (mover, option) pairs, and the same for Odd's gate faces (sigma-bar returns).
Usage: ret192.py FILES.json"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rpot192, idealcyc

def analyse(G):
    st = idealcyc.run(G); N = G["N"]; held = [{st[0][x]} for x in range(N)]; ret = {}
    for t in range(1, len(st)):
        for x in range(N):
            if st[t][x] != st[t - 1][x]:
                if st[t][x] in held[x]: ret[(x, st[t][x])] = ret.get((x, st[t][x]), 0) + 1
                held[x].add(st[t][x])
    h, E, V, name, movers, ev = rpot192.states(G); gret = {}
    gates = [v for v in range(h.n) if h.owner[v] == 1]; gh = {g: {ev[0][1][g]} for g in gates}
    for t in range(1, len(ev)):
        for g in gates:
            a = ev[t][1][g]
            if a != ev[t - 1][1][g]:
                if a in gh[g]: gret[(g, a)] = gret.get((g, a), 0) + 1
                gh[g].add(a)
    return len(st) - 1, sum(ret.values()), max(ret.values() or [0]), sum(gret.values()), max(gret.values() or [0])

if __name__ == "__main__":
    for f in sys.argv[1:]:
        T, r, rm, g, gm = analyse(json.load(open(f)))
        print(f"{os.path.basename(f)} T {T} mover re-adoptions {r} (max per option {rm}); face returns {g} (max per face {gm})")
