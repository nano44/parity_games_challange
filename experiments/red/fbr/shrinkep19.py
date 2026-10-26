#!/usr/bin/env python3
"""Box 45b: greedy vertex deletion to drive an epoch to n − 1 fallbacks (EPOCH (a)/(b) non-vacuous). Objective: ep_fb − (n − 1)
(fbr19). Delete v: drop it and every edge into it (refused if a successor set becomes empty); start entries pointing to v are
reset to the first remaining successor. Accept if the objective does not decrease. Usage: shrinkep19.py in.pg in.start.json OUT [passes]"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import fbr19, pg
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); st = json.load(open(sys.argv[2]))["start"]
out = sys.argv[3]; passes = int(sys.argv[4]) if len(sys.argv) > 4 else 3
cur = (list(g.prio), list(g.owner), [list(s) for s in g.succ], list(st))
def score(c):
    prio, owner, succ, s = c
    try: gg = pg.Game(prio, owner, succ)
    except Exception: return None, None
    r = fbr19.analyse(gg, s, cap=5000); return r["ep_fb_gap"], r
def delete(c, v):
    prio, owner, succ, s = c; n = len(prio); m = [i for i in range(n) if i != v]; idx = {x: i for i, x in enumerate(m)}
    ns = []
    for x in m:
        t = sorted({idx[y] for y in succ[x] if y != v})
        if not t: return None
        ns.append(t)
    nst = [idx[s[x]] if s[x] != v else ns[idx[x]][0] for x in m]
    return ([prio[x] for x in m], [owner[x] for x in m], ns, nst)
cs, cr = score(cur); print("START n", len(cur[0]), "gap", cs, "ep_fb", cr["ep_fb"], flush=True)
for p in range(passes):
    changed = False; v = len(cur[0]) - 1
    while v >= 0:
        c = delete(cur, v)
        if c is not None:
            s, r = score(c)
            if s is not None and s >= cs and not r["fails"]:
                cur, cs, cr = c, s, r; changed = True
                print("del", v, "n", len(cur[0]), "gap", cs, "ep_fb", r["ep_fb"], "fmax", r["fmax"], flush=True)
                json.dump(dict(prio=cur[0], owner=cur[1], succ=cur[2], start=cur[3], r=r), open(out + "_best.json", "w"))
            elif r is not None and r["fails"]: print("FAIL", r["fails"], flush=True); json.dump(dict(prio=c[0], owner=c[1], succ=c[2], start=c[3], r=r), open(out + "_FAIL.json", "w"))
        v -= 1
    if not changed: break
print("END n", len(cur[0]), "gap", cs, cr["ep_fb"], cr["fmax"], cr["epoch_n1"], cr["fails"])
