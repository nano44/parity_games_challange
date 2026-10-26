#!/usr/bin/env python3
"""L-SI box 19 (successor 15): DATA for note §26.2 (Lemma CHOSEN, Corollary RELAY-CHAIN). Per phase, class c, transition k -> k+1 and
q in Q_c with a rho event (Xi_k(q) != Xi_k+1(q)):
  CYC    q = c or q on its honest cycle at k or k + 1 (relay.py's CYC_OR_ONCYCLE);
  ROUTE  some class exit path of q (relay.py exits()) differs between k and k + 1;
  RELAY  otherwise. Lemma CHOSEN says: e := par-exit of sigma-bar_k(q) (the first vertex of Q_c u {c} on sigma-bar_k(q)'s play at k, the
         exit of the chosen option) is a terminal != c and (e has a rho event at k) or (e's play at k + 1 passes q: TOG).
CHOSEN_V counts relay events violating it; TOG counts the toggle alternative (event-free chosen exit whose play at k + 1 passes q).
Corollary RELAY-CHAIN: following e from a relay event (repeatedly, while the event at e is a RELAY) ends at a ROUTE / CYC event or a TOG
step within |Q_c| steps; CHAIN_V counts failures (a repeat or a chosen exit without an event and without TOG); max_chain the longest chain.
MUT=1 control: use sigma-bar_k+1(q)'s exit in place of sigma-bar_k(q)'s (must bite on a run with relay events where the choice moves).
Usage: chosen.py --one GAME [START] | --list FILE [KMIN] (env RS, NMAX)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, HERE)
from n5x import step, start_pair, Engine, dual, load, readstart
from relay import exits
from pot import oncycle
C = Counter(); VIOL = []; MUT = os.environ.get("MUT") == "1"

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        nxt = [s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)]
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), vs=vs, nxt=nxt))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["key"] == rows[i]["key"]: j += 1
        if j > i: phase(g, name, rows, i, j, Q)
        i = j + 1

def exit_of(nxt, y, c, Qs, q):
    x, seen = y, set()
    while x not in seen and x not in Qs and x != c: seen.add(x); x = nxt[x]
    return x if (x in Qs or x == c) else None

def passes(nxt, e, q, c):
    x, seen = e, set()
    while x not in seen and x != c:
        if x == q: return True
        seen.add(x); x = nxt[x]
    return False

def phase(g, name, rows, i, j, Q):
    Qs = set(Q)
    for k in range(i, j):
        A, B = rows[k], rows[k + 1]
        ev = {q for q in Q if tuple(A["vs"][q]) != tuple(B["vs"][q])}
        kind = {}
        for q in ev:
            c = rows[i]["vs"][q][0]
            if c == q or oncycle(A["nxt"], q) or oncycle(B["nxt"], q): kind[q] = "CYC"
            elif exits(A["nxt"], q, c, Qs, g.succ) != exits(B["nxt"], q, c, Qs, g.succ): kind[q] = "ROUTE"
            else: kind[q] = "RELAY"
            C[kind[q]] += 1
        for q in ev:
            if kind[q] != "RELAY": continue
            c = rows[i]["vs"][q][0]; chain = [q]; x = q
            while True:
                nx = B["nxt"] if MUT else A["nxt"]
                e = exit_of(A["nxt"], nx[x], c, Qs, x)
                if e is None or e == c or e == x:
                    C["CHOSEN_V"] += (x == q); C["CHAIN_V"] += 1; VIOL.append(("CHOSEN", name, k, q, x, e)); break
                if e not in ev:
                    if passes(B["nxt"], e, x, c): C["TOG"] += (x == q); break
                    C["CHOSEN_V"] += (x == q); C["CHAIN_V"] += 1; VIOL.append(("CHOSEN", name, k, q, x, e)); break
                if e in chain: C["CHAIN_V"] += 1; VIOL.append(("REPEAT", name, k, q, chain)); break
                chain.append(e); x = e
                if kind[e] != "RELAY": break
            C["max_chain"] = max(C["max_chain"], len(chain) - 1)

def main():
    a = sys.argv[1:]
    if a[0] == "--one":
        g = load(a[1]); check(g, a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        kmin = int(a[2]) if len(a) > 2 else 2
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin:
                continue
            check(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                check(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for v in VIOL[:8]: print("VIOLATION", v)
    print("CHOSEN PASS" if not VIOL else "CHOSEN FAIL")

if __name__ == "__main__":
    main()
