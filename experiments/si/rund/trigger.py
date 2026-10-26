#!/usr/bin/env python3
"""L-SI box 19 (successor 15): DATA for note §28. For one phase and one Odd choice vertex q (default: the q with the most rho events),
every transition k -> k+1 at which an Even vertex x on q's CHOSEN class exit path at k (sigma-bar_k(q)'s path up to its exit) switches
to z := sigma_k+1(x) is traced back to the moment (x, z) became improving: k0 := the last state <= k with (x, z) NOT improving
(Xi_k0(z) not > Xi_k0(sigma_k0 x)); the TRIGGER is what changed at k0 -> k0 + 1:
  SELF     sigma(x) changed at k0 (x moved; z is improving against its new edge)
  TERM     z's exit e (first vertex of Q_c u {c} on z's play) is a terminal != c whose kappa changed at k0 (re-thaw by a terminal)
  PATH     z's class exit path or exit changed at k0 (an Even switch downstream of z)
  OTHER    none of these (kappa(z) changed for another reason, e.g. a Q vertex on z's play outside the class)
  START    (x, z) was improving at every state since the phase start (k0 undefined).
Also: fallback or S4a at k; z's exit at k (c or a terminal). Usage: trigger.py GAME START [Q]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, HERE)
from n5x import step, start_pair, Engine, dual, load, readstart
from chosen import exit_of

def path_to(nxt, y, c, Qs):
    p, x, seen = [], y, set()
    while x not in seen and x not in Qs and x != c: seen.add(x); p.append(x); x = nxt[x]
    return tuple(p), x

def main():
    g = load(sys.argv[1]); st = readstart(sys.argv[2]); E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]; Qs = set(Q)
    while len(rows) < 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        nxt = [s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)]
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), vs=vs, sb=list(sb), nxt=nxt, s=list(s), fb=(r[4] if r else 0)))
        if r is None: break
        s, t = r[0], r[1]
    best = None; i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["key"] == rows[i]["key"]: j += 1
        if j > i:
            for q in Q:
                rq = sum(tuple(rows[k]["vs"][q]) != tuple(rows[k + 1]["vs"][q]) for k in range(i, j))
                if best is None or rq > best[0]: best = (rq, i, j, q)
        i = j + 1
    rq, i, j, q = best
    if len(sys.argv) > 3: q = int(sys.argv[3])
    c = rows[i]["vs"][q][0]; key = lambda k, v: E.key(rows[k]["vs"][v]); Cn = Counter()
    print(f"phase@{i} len={j - i} q={q} rho_q={rq} c={c}")
    for k in range(i, j):
        A, B = rows[k], rows[k + 1]
        p, e = path_to(A["nxt"], A["sb"][q], c, Qs)
        for x in p:
            if g.owner[x] != 0 or A["s"][x] == B["s"][x]: continue
            z = B["s"][x]; k0 = None
            for kk in range(k, i - 1, -1):
                if not key(kk, z) > key(kk, rows[kk]["s"][x]): k0 = kk; break
            if k0 is None: trig = "START"
            else:
                X, Y = rows[k0], rows[k0 + 1]
                pa, ea = path_to(X["nxt"], z, c, Qs); pb, eb = path_to(Y["nxt"], z, c, Qs)
                if X["s"][x] != Y["s"][x]: trig = "SELF"
                elif (pa, ea) != (pb, eb): trig = "PATH"
                elif ea != c and ea in Qs and key(k0, ea) != key(k0 + 1, ea): trig = "TERM"
                else: trig = "OTHER"
            _, ez = path_to(A["nxt"], z, c, Qs)
            Cn[trig] += 1; Cn["fb" if A["fb"] else "s4a"] += 1; Cn["zexit_c" if ez == c else "zexit_term"] += 1
            print(f"  t={k - i} {'fb ' if A['fb'] else 's4a'} x={x} {A['s'][x]}->{z} z_exit={ez} trigger={trig} k0={None if k0 is None else k0 - i}")
    print(" ".join(f"{a}={b}" for a, b in sorted(Cn.items())))

if __name__ == "__main__":
    main()
