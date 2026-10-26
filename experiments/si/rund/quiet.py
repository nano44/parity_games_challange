#!/usr/bin/env python3
"""L-SI box 19 (successor 15): DATA for note §26. Per phase, class c and q in Q_c: split the phase at every transition that is a
FALLBACK or carries a rho event (Xi change) at some OTHER terminal of the class (Q_c minus q). Inside one piece the class's other
terminals are constant (the 𝒞^1O situation: R50 (b) A0). Reports, over all (phase, q):
  rho_q          q's events in the phase (max: max_rho_q);
  quiet_max      the most events of q in one piece; pieces with >= 1 event of q; events_in_pieces_ge2 (events of q in pieces holding >= 2);
  splits_other / splits_fb: the cuts by kind.
UP=1: cut only at events of UPSTREAM terminals of q (the exits, other than q and c, of q's class exit paths at k or k + 1;
  relay.py's exits()), so events at terminals that merely copy q do not cut.
UP=2: cut only at events of par_k(q), the terminal at the end of sigma-bar_k(q)'s class exit path (flipck.py's par). kappa(q) is the min of
  non-decreasing option values (Xi is non-decreasing in the phase, R15), so a relay event at q needs its chosen option to rise.
A CONJECTURE under test (QUIET-n): quiet_max <= n - 1 (QUIET_V counts pieces with more than n - 1 events of q). FALSE on one-terminal
classes (pftheta34_n32: 34 events in one piece; 𝒞^1O, bounded by R51 but not by n - 1); maxima are also reported per |Q_c| = 1 / >= 2.
Usage: quiet.py --one GAME [START] [-v] | --list FILE [KMIN] (env RS, NMAX)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, HERE)
from n5x import step, start_pair, Engine, dual, load, readstart
from relay import exits
from flipck import par
C = Counter(); VIOL = []; VERB = "-v" in sys.argv; TOP = []; UP = os.environ.get("UP", "0")

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        nxt = [s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)]
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), vs=vs, fb=(r[4] if r else 0), nxt=nxt))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["key"] == rows[i]["key"]: j += 1
        if j > i: phase(g, name, rows, i, j, Q, g.succ)
        i = j + 1

def phase(g, name, rows, i, j, Q, succ):
    ev = lambda k, q: tuple(rows[k]["vs"][q]) != tuple(rows[k + 1]["vs"][q])
    for q in Q:
        c = rows[i]["vs"][q][0]
        if c == q: continue
        Qc = [p for p in Q if p != q and p != c and rows[i]["vs"][p][0] == c]
        rq = sum(ev(k, q) for k in range(i, j))
        if not rq: continue
        C["q_phases"] += 1; C["max_rho_q"] = max(C["max_rho_q"], rq); C["rho_q_total"] += rq
        piece, pieces = 0, []; Qs = set(Q)
        for k in range(i, j):
            if UP == "2":   # cut only at events of q's CHOSEN terminal par_k(q) (exit of sigma-bar_k(q)'s class exit path)
                pk = par(rows[k]["nxt"], q, c, Qs)
                cut_o = bool(pk) and ev(k, pk[0])
            elif UP == "1":   # cut only at events of UPSTREAM terminals: exits of q's class exit paths at k or k + 1
                up = {e for (_, _, e) in exits(rows[k]["nxt"], q, c, Qs, succ) + exits(rows[k + 1]["nxt"], q, c, Qs, succ)}
                cut_o = any(ev(k, p) for p in Qc if p in up)
            else:
                cut_o = any(ev(k, p) for p in Qc)
            cut_f = rows[k]["fb"]
            if ev(k, q): piece += 1
            if cut_o or cut_f:
                pieces.append(piece); piece = 0; C["splits_other"] += cut_o; C["splits_fb"] += cut_f and not cut_o
        pieces.append(piece)
        qm = max(pieces); C["quiet_max"] = max(C["quiet_max"], qm); b = "1" if not Qc else "ge2"
        C["quiet_max_Qc" + b] = max(C["quiet_max_Qc" + b], qm); C["max_rho_q_Qc" + b] = max(C["max_rho_q_Qc" + b], rq)
        C["max_quiet_over_n_pct_Qc" + b] = max(C["max_quiet_over_n_pct_Qc" + b], 100 * qm // g.n)
        C["events_in_pieces_ge2"] += sum(p for p in pieces if p >= 2)
        if qm > g.n - 1: C["QUIET_V"] += 1; VIOL.append(("QUIET", name, i, q, qm, g.n))
        TOP.append((qm, rq, j - i, len(Qc) + 1, g.n, name, i, q))
        if VERB and rq >= 5: print(f"  Q {name} phase@{i} len={j - i} q={q} |Q_c|={len(Qc) + 1} rho_q={rq} pieces={pieces}")

def main():
    a = [x for x in sys.argv[1:] if x != "-v"]
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
    for m in sorted(TOP, reverse=True)[:6]: print("TOP quiet_max/rho_q/len/|Q_c|/n", m)
    for m in sorted((x for x in TOP if x[3] >= 2), reverse=True)[:4]: print("TOP(|Q_c|>=2) quiet_max/rho_q/len/|Q_c|/n", m)
    for v in VIOL[:8]: print("VIOLATION", v)
    print("QUIET PASS" if not VIOL else "QUIET FAIL")

if __name__ == "__main__":
    main()
