#!/usr/bin/env python3
"""L-SI box 18 (successor 14): DATA for note §22 (the CAUSE of each rho_q event; not a rho_q census, which is L-COMP 5's box 13).
Per PHASE ((lambda_Xi, tau) constant), per Odd choice vertex q and transition t -> t+1 with Xi_t(q) != Xi_t+1(q), q on no honest cycle at t
and t+1 (the others are counted as CYC_OR_ONCYCLE and skipped):
  EXIT PATHS of q at t: for y in succ(q), y's honest play (sigma_t for Even, sigma-bar_t for Odd) up to its first vertex in
  T_t := Q u {c} (c = lambda(q), the cycle node; q itself included); the tuple of these paths and the exit vertices.
  ROUTE  some exit path of q differs between t and t+1 (an Even switch on it, or a change of where it exits);
  RELAY  every exit path is the same at t and t+1; the event's SOURCES are the exits e != c, e != q whose Xi changed (Lemma ROUTE-RELAY,
         note §22, says the source set is non-empty: R_EMPTY_V counts failures).
ROOT_V: a transition with a rho event and all Q-exit paths unchanged (Lemma ROOT, PROVED, says none; MUT=1 inverts the test).
ALLRELAY_T: a (class, transition) whose rho events are ALL relays (CONJECTURE ROOT-C, note §22, says none).
Per phase: the RELAY GRAPH (edge q -> e for each source e of a relay event at q); CYC2 = a pair q1 -> q2, q2 -> q1 in one phase; CYCG = any
directed cycle. On a class with one Odd choice vertex every event must be ROUTE (ONE_RELAY_V counts failures).
Usage: relay.py --one GAME [START] [-v] | --list FILE [KMIN] (env RS, NMAX)"""
import sys, os, random
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, HERE)
from n5x import step, start_pair, Engine, dual, load, readstart
from pot import oncycle
C = Counter(); VIOL = []; VERB = "-v" in sys.argv; SHOW = []

def exits(nxt, q, c, Qs, succ):
    out = []
    for y in sorted(set(succ[q])):
        path, x, seen = [], y, set()
        while x not in seen and x not in Qs and x != c and x != q:
            seen.add(x); path.append(x); x = nxt[x]
        out.append((y, tuple(path), x if (x in Qs or x == c or x == q) else None))
    return tuple(out)

def qexits(nxt, Qs, succ):
    """Lemma ROOT's Q-exit paths: for q in Q, y in succ(q): y's play up to the first vertex of Q or the first repeat (that vertex included)."""
    out = []
    for q in sorted(Qs):
        for y in sorted(set(succ[q])):
            path, x, seen = [], y, set()
            while x not in seen and x not in Qs: seen.add(x); path.append(x); x = nxt[x]
            out.append((q, y, tuple(path), x))
    return tuple(out)

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        nxt = [s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)]
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), vs=vs, sb=list(sb), nxt=nxt))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["key"] == rows[i]["key"]: j += 1
        if j > i: phase(g, E, name, rows, i, j, Q)
        i = j + 1

def phase(g, E, name, rows, i, j, Q):
    C["phases"] += 1; Qs = set(Q); edges = defaultdict(set); per = Counter(); tk = defaultdict(set)
    for k in range(i, j):
        A, B = rows[k], rows[k + 1]
        if any(tuple(A["vs"][q]) != tuple(B["vs"][q]) for q in Q):
            C["rho_transitions"] += 1
            same = qexits(A["nxt"], Qs, g.succ) == qexits(B["nxt"], Qs, g.succ)
            if os.environ.get("MUT") == "1": same = not same   # control: must bite on any run with a rho event
            if same: C["ROOT_V"] += 1; VIOL.append(("ROOT", name, k))
    for q in Q:
        c = rows[i]["vs"][q][0]
        kq = sum(1 for p in Q if rows[i]["vs"][p][0] == c and p != c)
        for k in range(i, j):
            A, B = rows[k], rows[k + 1]
            if tuple(A["vs"][q]) == tuple(B["vs"][q]): continue
            if c == q or oncycle(A["nxt"], q) or oncycle(B["nxt"], q): C["CYC_OR_ONCYCLE"] += 1; tk[(c, k)].add("R"); continue
            ea, eb = exits(A["nxt"], q, c, Qs, g.succ), exits(B["nxt"], q, c, Qs, g.succ)
            tag = "multi" if kq >= 2 else "one"
            if ea != eb:
                C["ROUTE_" + tag] += 1; per[(q, "R")] += 1; tk[(c, k)].add("R")
                if os.environ.get("TRACE") == "1": print(f"    EV {name} phase@{i} t={k - i} q={q} ROUTE sbar {A['sb'][q]}->{B['sb'][q]}")
                continue
            C["RELAY_" + tag] += 1; per[(q, "L")] += 1; tk[(c, k)].add("L")
            src = {e for (_, _, e) in ea if e is not None and e != c and e != q and tuple(A["vs"][e]) != tuple(B["vs"][e])}
            if not src: C["R_EMPTY_V"] += 1; VIOL.append(("R_EMPTY", name, k, q))
            if kq < 2: C["ONE_RELAY_V"] += 1; VIOL.append(("ONE_RELAY", name, k, q))
            for e in src: edges[q].add(e)
            if os.environ.get("TRACE") == "1": print(f"    EV {name} phase@{i} t={k - i} q={q} RELAY src={sorted(src)} sbar {A['sb'][q]}->{B['sb'][q]}")
    for key, kinds in tk.items():
        C["class_event_transitions"] += 1
        if kinds == {"L"}: C["ALLRELAY_T"] += 1; VIOL.append(("ALLRELAY_T", name, key))
    for (q, kind), v in per.items():
        if kind == "L": C["max_relay_q_phase"] = max(C["max_relay_q_phase"], v)
    qs = {q for (q, _) in per}
    for q in qs:
        rq, lq = per[(q, "R")], per[(q, "L")]
        C["max_rho_q"] = max(C["max_rho_q"], rq + lq)
        if lq > rq: C["q_phase_relay_majority"] += 1
    if any(b in edges and a in edges[b] for a in edges for b in edges[a]):
        C["CYC2_phases"] += 1; SHOW.append((name, i, {a: sorted(b) for a, b in edges.items()}))
    color = {}
    def dfs(u):
        color[u] = 1
        for w in edges.get(u, ()):
            if color.get(w) == 1 or (color.get(w) is None and dfs(w)): return True
        color[u] = 2; return False
    if any(color.get(u) is None and dfs(u) for u in list(edges)): C["CYCG_phases"] += 1
    if edges: C["phases_with_relay"] += 1
    if VERB and edges: print(f"  RELAYGRAPH {name} phase@{i} len={j - i} {dict((a, sorted(b)) for a, b in edges.items())} per={dict(per)}")

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
    for s in SHOW[:6]: print("CYC2", s)
    for v in VIOL[:8]: print("VIOLATION", v)
    print("RELAY PASS" if not VIOL else "RELAY FAIL")

if __name__ == "__main__":
    main()
