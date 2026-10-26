#!/usr/bin/env python3
"""Box 46 DATA: the direct D-changes X_dir ({u} -> {u'}, u != u', in-phase) of docs/new/N5-REC1-box46.md §3: per occurrence, the game, start,
state k, u, u', sigma-bar(u) at k and k+1, tau(u), tau(u'), whether k / k+1 are W-honest, the transition type (S4a / fallback), and Xi / W at
u, u'. Usage: xdir.py STARTS SEED (--list FILE | --rand C LO HI GSEED)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import hon
from levels import load, step, start_pair, Engine, dual, rand_ckO
def run(g, start, nm):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= 4000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t); w = hon.wvals(g, s, t)
        rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), sb=sb, xi=vs, w=w, fb=r[4] if r else 0, D=[q for q in Q if sb[q] != t[q]]))
        if r is None: break
        s, t = r[0], r[1]
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        if (a["lam"], a["t"]) != (b["lam"], b["t"]) or len(a["D"]) != 1 or len(b["D"]) != 1 or a["D"] == b["D"]: continue
        u, u2 = a["D"][0], b["D"][0]
        print(f"{nm} n {g.n} start {'S3' if start is None else 'rand'} k {k} u {u}->{u2} sbar(u) {a['sb'][u]}->{b['sb'][u]} tau(u) {a['t'][u]} "
              f"sbar(u') {a['sb'][u2]}->{b['sb'][u2]} tau(u') {a['t'][u2]} fb {a['fb']} Xi(u) {a['xi'][u]}->{b['xi'][u]} W(u) {a['w'][u]}->{b['w'][u]} "
              f"Xi(u') {a['xi'][u2]}->{b['xi'][u2]} W(u') {a['w'][u2]}->{b['w'][u2]}")
if __name__ == "__main__":
    a = sys.argv[1:]; K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [(l.split()[0], load(os.path.join(R0, l.split()[0]))) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    else:
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [(f"rand{i}", g) for i, g in enumerate(rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    for nm, g in gs:
        if g.n > 64: continue
        for st in [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                             {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]:
            try: run(g, st, nm)
            except RecursionError: pass
