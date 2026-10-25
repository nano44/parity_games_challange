#!/usr/bin/env python3
"""Box 42 (2): profile of events (switches across c_w, c_w's own switches) in U3/U23 stretches (¬H2, c_w ≠ o), by c_w parity and
c_w vs c_θ, fallback or S4a, W unchanged at the switcher or not; per fallback-free run: events and run length.
Usage: evprof.py --list FILE | --rand N lo hi seed [--randstart]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from kwfreeze import *

def go3(g, acc, tag, start=None):
    if sum(1 for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1) != 1: return
    rows, o, E = rows_raw(g, start); n = g.n; rk = E.rank
    a = 0
    for i in range(1, len(rows) + 1):
        if not (i == len(rows) or rows[i]["ph"] != rows[i - 1]["ph"]): continue
        x, y_ = a, i - 1; a = i; k = x
        while k <= y_:
            j = k
            while j + 1 <= y_ and all(rows[j + 1][f] == rows[k][f] for f in ("R", "th", "w")): j += 1
            r0 = rows[k]; R = r0["R"]; ct, cw = r0["ct"], r0["cw"]
            if not r0["h2"] and cw != o:
                band = ("cw>ct" if rk[cw] > rk[ct] else "ct>cw") + ("_odd" if E.par[cw] else "_even")
                runev = 0
                for q in range(k, j):
                    sw = [v for v in R if v != o and g.owner[v] == 0 and rows[q]["s"][v] != rows[q + 1]["s"][v]]
                    for v in sw:
                        A0 = cw in route(rows[q]["nxt"], v, o); A1 = cw in route(rows[q + 1]["nxt"], v, o)
                        kind = "cwsw" if v == cw else ("A->B" if A0 and not A1 else ("B->A" if A1 and not A0 else None))
                        if kind is None: continue
                        flat = rows[q]["W"][v] == rows[q + 1]["W"][v]
                        key = (band, kind, "fb" if rows[q]["fb"] else "s4a", "Wflat" if flat else "Wchg")
                        acc[key] = acc.get(key, 0) + 1
                        if not rows[q]["fb"]: runev += 1
                    if rows[q]["fb"]: runev = 0
                    acc["max_ev_run_" + band] = max(acc.get("max_ev_run_" + band, 0), runev)
                if j > k: acc.setdefault("where", {}); acc["where"][tag] = acc["where"].get(tag, 0) + 1
            k = j + 1

if __name__ == "__main__":
    args = sys.argv[1:]; acc = {}; root = os.path.join(HERE, "..", "..", "..")
    if args[0] == "--rand":
        RS = "--randstart" in args; N, lo, hi, seed = map(int, args[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            go3(g, acc, ("rand", seed, i), st)
    else:
        for f in [l.strip() for l in open(args[1])]:
            p = f if os.path.exists(f) else os.path.join(root, f)
            try: g = load(p)
            except Exception: continue
            go3(g, acc, f)
    w = acc.pop("where", {})
    for k_, v in sorted(acc.items(), key=lambda kv: str(kv[0])): print(k_, v)
    print("files with U3/U23 stretches:", len(w))
