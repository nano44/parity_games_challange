#!/usr/bin/env python3
"""L-SI box 20 (successor 16): DATA for note §7 (the D-leaves G_c). Per phase, a D-LEAVE at u is an in-phase transition t -> t+1 with
u in D_t, u not in D_t+1 (sigma-bar_t+1(u) = tau(u) != sigma-bar_t(u)); a D-ENTER the reverse. For every D-leave at u (u in Q, class c):
  kind     fb / s4a;
  ev       u's event at t -> t+1 by relay.py's exits() (paths AND exits to Q_c u {c}): ROUTE (some exit path or exit differs) or RELAY;
  y1, y2   sigma-bar_t(u) and tau(u); e1, e2 their exits at t (first vertex of Q_c u {c} on the play); e2 = c means tau(u)'s option is direct;
  root     the Odd choice vertex of the class with the most rho events in the phase; rootrho: Xi(root) changes at t -> t+1;
  e1rho    Xi(e1) changes at t -> t+1 (e1 a terminal != c);
  CAUSE    COPY  (e1 != c and e1 has a rho event at t: the old option's exit rose, CHOSEN's mechanism, the relay copies its exit)
           OWN   (otherwise: a switch on u's own exit paths, ROUTE at u);
  prior    the last earlier event at u in the phase before t: ENTER (u moved off tau(u)) or none.
Cross counts x_<kind>_<cause>_<e1c|e1t> (e1c: the relay was D-direct-like, its chosen option exits at c).
Summary per phase: leaves, enters, leaves by CAUSE and kind, max leaves of one u, and LV_GT_EN_V (leaves at u > enters at u + 1: impossible,
reported as a consistency check). Usage: dleave.py --one GAME [START] [-v] | --list FILE [KMIN] (env RS, NMAX)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import *
sys.path.insert(0, os.path.join(HERE, "..", "rund"))
from relay import exits
C = Counter(); VIOL = []; TOP = []; VERB = "-v" in sys.argv

def exit_of(nxt, y, c, Ts, q):
    x, seen = y, set()
    while x not in seen and x not in Ts and x != c and x != q: seen.add(x); x = nxt[x]
    return x

def run(g, name, start=None):
    E, R = rows(g, start); Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]; Qs = set(Q)
    for i, j in phases(R):
        rho = Counter()
        for k in range(i, j):
            for q in Q:
                if E.key(R[k]["vs"][q]) != E.key(R[k + 1]["vs"][q]): rho[q] += 1
        lv, en = Counter(), Counter()
        for k in range(i, j):
            A, B = R[k], R[k + 1]; D0, D1 = Dset(g, A), Dset(g, B)
            for u in D1 - D0: en[u] += 1; C["enters"] += 1
            for u in sorted(D0 - D1):
                lv[u] += 1; C["leaves"] += 1
                c = A["vs"][u][0]; U = {v for v in range(g.n) if A["vs"][v][0] == c}; Ts = {q for q in Qs if q in U and q != c}
                root = max((q for q in Ts), key=lambda q: rho[q], default=None)
                ev = "CYC" if u == c else ("ROUTE" if exits(A["nxt"], u, c, Ts, g.succ) != exits(B["nxt"], u, c, Ts, g.succ) else "RELAY")
                y1, y2 = A["sb"][u], A["t"][u]
                e1, e2 = exit_of(A["nxt"], y1, c, Ts, u), exit_of(A["nxt"], y2, c, Ts, u)
                e1rho = e1 in Ts and E.key(A["vs"][e1]) != E.key(B["vs"][e1])
                cause = "COPY" if e1rho else "OWN"
                kind = "fb" if A["fb"] else "s4a"
                C[f"x_{kind}_{cause}_{'e1c' if e1 == c else 'e1t'}"] += 1
                C[f"y_{ev}_{cause}"] += 1
                C[f"leave_{kind}"] += 1; C[f"leave_{cause}"] += 1; C[f"leave_ev_{ev}"] += 1
                C["leave_tau_direct" if e2 == c else ("leave_tau_via_self" if e2 == u else "leave_tau_via_term")] += 1
                C["leave_e1_root" if e1 == root else ("leave_e1_c" if e1 == c else "leave_e1_other")] += 1
                rr = root is not None and E.key(A["vs"][root]) != E.key(B["vs"][root])
                C["leave_rootrho" if rr else "leave_noroot"] += 1
                if VERB: print(f"  {name} phase@{i} t={k - i} {kind} LEAVE u={u} ev={ev} y1={y1}(exit {e1}) tau={y2}(exit {e2}) "
                               f"root={root} rootrho={int(rr)} e1rho={int(e1rho)} cause={cause}")
        for u in lv:
            if lv[u] > en[u] + 1: C["LV_GT_EN_V"] += 1; VIOL.append(("LVEN", name, i, u))
        if lv: C["max_leaves_u"] = max(C["max_leaves_u"], max(lv.values())); TOP.append((sum(lv.values()), j - i, name, i))

def main():
    a = [x for x in sys.argv[1:] if x != "-v"]
    if a[0] == "--one":
        g = load(a[1]); run(g, a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        kmin = int(a[2]) if len(a) > 2 else 2
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin:
                continue
            run(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                run(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                   {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in sorted(TOP, reverse=True)[:5]: print("TOP leaves/len", x)
    for v in VIOL[:8]: print("VIOLATION", v)
    print("DLEAVE PASS" if not VIOL else "DLEAVE FAIL")

if __name__ == "__main__":
    main()
