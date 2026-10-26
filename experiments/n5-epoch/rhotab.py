#!/usr/bin/env python3
"""Box 13 (2): rho_q per q per phase, with the class columns, ALT classes and the RELAY-GRAPH-CYCLE column (Lead 10:11Z, 10:23Z, 10:42Z).
Own code on census.py (n5b SPEC engine). The ROUTE / RELAY classification is a reimplementation of the LOGIC of L-SI's
experiments/si/rund/relay.py (l-si 24a70938; docs/si/N5-RUND-box17.md §22), read, not imported:
  per phase ((lambda_Xi, tau) constant, >= 1 transition), q in Q, t -> t+1 with Xi_t(q) != Xi_{t+1}(q)  (a rho_q event):
    c := lambda(q) (constant on the phase); CYC if c == q or q lies on its honest cycle at t or at t+1;
    else EXITS(q, t) := for y in succ(q) (sorted): y's honest play up to its first vertex in Q u {c, q} (path, exit vertex);
    ROUTE if EXITS(q, t) != EXITS(q, t+1); else RELAY with SOURCES := exits e not in {c, q} with Xi_t(e) != Xi_{t+1}(e).
  RELAY GRAPH of the phase: edge q -> e for every source e of a relay event at q;  CYCG = it has a directed cycle; CYC2 = a 2-cycle.
  Checks (L-SI lemmas, lane-PROVED, unrefereed): R_EMPTY (a relay event without a source), ONE_RELAY (a relay event on a class with one Odd
  choice vertex), ROOT (a transition with a rho event at which every Q-exit path is unchanged).
Class columns: |Q| (Odd vertices of out-degree >= 2), |QE| (Even vertices of out-degree >= 2), CLASS = 1O if |Q| = 1, 1E if |QE| = 1 (both
labels may apply), kq per honest class := #{q in Q : lambda(q) = c, q != c} for each cycle node c with kq >= 1 (as relay.py's kq).
Usage: rhotab.py STARTS SEED (--list FILE | FILE.pg[:START] ...) [--rows MIN_NEP] [--lsi-starts RS] [--nmax N] [--kmin K]
  --rows M: print one ROW per phase with N_ep >= M (default: only phases with a rho event on a q with kq >= 2, or N_ep >= 10)
  --lsi-starts RS: L-SI's start pairs (S3 + RS starts from random.Random(path): Even dict first, then Odd), for the cross-check."""
import os
import random
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import census as C  # noqa: E402
from census import SpecSI, EVEN, ODD, pg  # noqa: E402

T = Counter(); VIOL = []


def oncyc(H, q):
    return q in C.lasso(H, q)[1]


def exits(H, q, c, Qs, succ):
    out = []
    for y in sorted(set(succ[q])):
        path, x, seen = [], y, set()
        while x not in seen and x not in Qs and x != c and x != q:
            seen.add(x); path.append(x); x = H[x]
        out.append((y, tuple(path), x if (x in Qs or x == c or x == q) else None))
    return tuple(out)


def qexits(H, Qs, succ):
    out = []
    for q in sorted(Qs):
        for y in sorted(set(succ[q])):
            path, x, seen = [], y, set()
            while x not in seen and x not in Qs:
                seen.add(x); path.append(x); x = H[x]
            out.append((q, y, tuple(path), x))
    return tuple(out)


def has_cycle(edges):
    color = {}

    def dfs(u):
        color[u] = 1
        for w in edges.get(u, ()):
            if color.get(w) == 1 or (color.get(w) is None and dfs(w)):
                return True
        color[u] = 2
        return False
    return any(color.get(u) is None and dfs(u) for u in list(edges))


def run(g, name, states, fbs, rows_min, out):
    n = g.n; SG = SpecSI(g)
    A = [C.state_info(g, SG, s, t) for s, t in states]
    Q = [v for v in range(n) if g.owner[v] == ODD and len(set(g.succ[v])) >= 2]; Qs = set(Q)
    QE = [v for v in range(n) if g.owner[v] == EVEN and len(set(g.succ[v])) >= 2]
    cls = ("1O" if len(Q) == 1 else "") + ("1E" if len(QE) == 1 else "") or f"{len(Q)}O"
    key = [(A[k]["lam"], states[k][1]) for k in range(len(A))]
    T["runs"] += 1
    i = 0
    while i < len(A):
        j = i
        while j + 1 < len(A) and key[j + 1] == key[i]:
            j += 1
        if j > i:
            phase(g, name, A, fbs, i, j, Q, Qs, QE, cls, rows_min, out)
        i = j + 1


def phase(g, name, A, fbs, i, j, Q, Qs, QE, cls, rows_min, out):
    T["phases"] += 1
    lam = A[i]["lam"]
    kq = Counter(lam[q] for q in Q if lam[q] != q)
    # epochs
    conf = [tuple(A[k]["sbar"][q] for q in Q) for k in range(i, j + 1)]
    nep = 1 + sum(1 for a, b in zip(conf, conf[1:]) if a != b)
    rho = Counter(); route = Counter(); relay = Counter(); cyc = Counter(); edges = defaultdict(set); tk = defaultdict(set)
    for k in range(i, j):
        X0, X1 = A[k]["Xi"], A[k + 1]["Xi"]
        if any(X0[q] != X1[q] for q in Q):
            T["rho_transitions"] += 1
            if qexits(A[k]["H"], Qs, g.succ) == qexits(A[k + 1]["H"], Qs, g.succ):
                T["ROOT_V"] += 1; VIOL.append(f"ROOT {name} t={k}")
        for q in Q:
            if X0[q] == X1[q]:
                continue
            rho[q] += 1; c = lam[q]
            if c == q or oncyc(A[k]["H"], q) or oncyc(A[k + 1]["H"], q):
                cyc[q] += 1; T["CYC_OR_ONCYCLE"] += 1; tk[(c, k)].add("R"); continue
            tag = "multi" if kq[c] >= 2 else "one"
            ea, eb = exits(A[k]["H"], q, c, Qs, g.succ), exits(A[k + 1]["H"], q, c, Qs, g.succ)
            if ea != eb:
                route[q] += 1; T["ROUTE_" + tag] += 1; tk[(c, k)].add("R"); continue
            relay[q] += 1; T["RELAY_" + tag] += 1; tk[(c, k)].add("L")
            src = {e for (_, _, e) in ea if e is not None and e != c and e != q and X0[e] != X1[e]}
            if not src:
                T["R_EMPTY_V"] += 1; VIOL.append(f"R_EMPTY {name} t={k} q={q}")
            if kq[c] < 2:
                T["ONE_RELAY_V"] += 1; VIOL.append(f"ONE_RELAY {name} t={k} q={q}")
            for e in src:
                edges[q].add(e)
    for kinds in tk.values():
        if kinds == {"L"}:
            T["ALLRELAY_T"] += 1
    cycg = has_cycle(edges); cyc2 = any(b in edges and a in edges[b] for a in edges for b in edges[a])
    T["CYCG_phases"] += cycg; T["CYC2_phases"] += cyc2; T["phases_with_relay"] += bool(edges)
    R = sum(rho.values())
    multi = any(kq[lam[q]] >= 2 for q in rho)
    lab = cls if cls in ("1O", "1E", "1O1E") else "kO"
    T[f"phases_{lab}"] += 1; T[f"rho_{lab}"] += R
    for q, v in rho.items():
        T[f"max_rho_q_{lab}"] = max(T[f"max_rho_q_{lab}"], v)
        if kq[lam[q]] >= 2:
            T["max_rho_q_on_multi_class"] = max(T["max_rho_q_on_multi_class"], v)
    T["max_N_ep"] = max(T["max_N_ep"], nep)
    if (rows_min is not None and nep >= rows_min) or (rows_min is None and (multi or nep >= 10)):
        kqs = ",".join(f"{c}:{v}" for c, v in sorted(kq.items()))
        rq = " ".join(f"{q}:{rho[q]}(R{route[q]}/L{relay[q]}/C{cyc[q]})" for q in sorted(rho))
        out.append(f"ROW class={cls} |Q|={len(Q)} |QE|={len(QE)} kq/class=[{kqs}] | {name} phase[{i},{j}] n={g.n} N_ep={nep} len={j - i} "
                   f"rho={R} | rho_q {rq} | relaygraph={{{', '.join(f'{a}->{sorted(b)}' for a, b in sorted(edges.items()))}}} CYCG={int(cycg)} CYC2={int(cyc2)}")


def main():
    argv = sys.argv[1:]; rows_min = None; lsi = None; nmax = 10 ** 9; kmin = 0
    for opt in ("--rows", "--lsi-starts", "--nmax", "--kmin"):
        if opt in argv:
            i = argv.index(opt); v = int(argv[i + 1]); del argv[i:i + 2]
            if opt == "--rows": rows_min = v
            elif opt == "--lsi-starts": lsi = v
            elif opt == "--nmax": nmax = v
            else: kmin = v
    starts, seed = int(argv[0]), int(argv[1]); rng = random.Random(seed); out = []
    for name, g, st in C.games_from_args(argv[2:]):
        if g.n > nmax or sum(1 for v in range(g.n) if g.owner[v] == ODD and len(set(g.succ[v])) >= 2) < kmin:
            continue
        pairs = [("S3", None, None)]
        if st:
            s, t = C.full_start(g, *C.read_start(st, g)); pairs = [("start", s, t)]
        if lsi is not None:
            r2 = random.Random(name)
            for x in range(lsi):
                se = {v: r2.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == EVEN}
                so = {v: r2.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == ODD}
                pairs.append((f"L{x}", [se.get(v, -1) for v in range(g.n)], [so.get(v, -1) for v in range(g.n)]))
        for r in range(starts):
            s, t = C.rand_start(g, rng); pairs.append((f"R{r}", s, t))
        for tag, s, t in pairs:
            try:
                states, fbs = C.run_states(g, s, t, cap=3000)
            except Exception as e:   # noqa: BLE001
                T["runs_failed"] += 1; print("RUNFAIL", name, tag, repr(e)[:150]); continue
            run(g, f"{name}[{tag}]", states, fbs, rows_min, out)
    for r in out:
        print(r)
    print(" ".join(f"{k}={v}" for k, v in sorted(T.items())))
    for v in VIOL[:10]:
        print("VIOLATION", v)
    print("RESULT", "FAIL" if VIOL else "OK", f"violations={len(VIOL)}")


if __name__ == "__main__":
    main()
