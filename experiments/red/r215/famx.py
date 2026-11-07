#!/usr/bin/env python3
"""L-RED 53, R215 (a): tie-forcing transforms of classical SI lower-bound families, scored by N5'-xi (n5v xi @ acdbd28b) and SPEC.
Transforms of a game G (Even = 0, Odd = 1; harness pg.Game):
  none     : G itself
  padback  : every edge v->w of an Even v with >= 2 successors goes through a fresh Odd pad p (priority 0 slot below all, see LOW)
             with edges p->w and p->v (the back edge lets Odd refuse the switch; Xi_sigma vs the tau-arena can then differ)
  padsink  : as padback but p->w and p->z, z one global Odd vertex with a self-loop of the largest odd priority (Odd-won sink)
  padpair  : p->w and p->w' where w' = the next successor of v (cyclically): tau pins p to one of two of v's own targets
Pads get priority 0..; all original priorities are shifted up by 2 so pads are lowest. Every result is checked (zielonka + verify).
Usage: famx.py FAMILY TRANSFORM NMAX     FAMILY: pgs:<gen> or an Oink generator (counter_symsi, ...)"""
import sys, os, subprocess
WT = os.environ["WT"]
sys.path[:0] = [os.path.join(WT, "experiments/new/box190"), os.path.join(WT, "experiments/new/box189"), os.path.join(WT, "experiments/harness")]
import n5v, pg, zielonka, verify
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../.."))
def fam(f, N):
    cmd = (["python3", os.path.join(WT, "experiments/hard-families/pgsolver_port.py"), f[4:], str(N)] if f.startswith("pgs:")
           else [os.path.join(ROOT, "tools/oink/build", f), str(N)])
    txt = subprocess.run(cmd, capture_output=True, text=True).stdout
    return pg.parse("".join(l for l in txt.splitlines(True) if not l.lstrip().startswith("%")))
def transform(g, t):
    if t == "none": return g
    n = g.n; prio = [p + 2 for p in g.prio]; own = list(g.owner); succ = [list(s) for s in g.succ]
    z = None
    if t == "padsink":
        z = len(prio); top = max(prio) + 1; top += (top % 2 == 0); prio.append(top); own.append(1); succ.append([z])
    for v in range(n):
        if own[v] != 0 or len(g.succ[v]) < 2: continue
        new = []
        S = list(g.succ[v])
        for i, w in enumerate(S):
            p = len(prio); prio.append(1); own.append(1)   # priority 1 (odd, lowest after shift); 0 unused
            other = v if t == "padback" else (z if t == "padsink" else S[(i + 1) % len(S)])
            succ.append(sorted({w, other})); new.append(p)
        succ[v] = new
    return pg.Game(prio, own, succ)
f, t, nmax = sys.argv[1], sys.argv[2], int(sys.argv[3])
for N in range(1, nmax + 1):
    g = transform(fam(f, N), t)
    st, fb, E = n5v.run(g, "xi", cap=100000); sp, fb2, _ = n5v.run(g, "spec", cap=100000)
    win, strat = n5v.solution(g, st, E); ok = win == zielonka.solve(g) and not verify.check(g, win, [strat[v] if win[v] == g.owner[v] else None for v in range(g.n)])
    print(f"{f} {t} N {N} n {g.n} xi {len(st)-1} spec {len(sp)-1} {'OK' if ok else 'WRONG'}", flush=True)
    if not ok: pg.write(g, f"fam/WRONG_{f.replace(':','_')}_{t}_{N}.pg")
