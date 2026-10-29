#!/usr/bin/env python3
"""L-NEW box 49 (successor 30), DATA for docs/new/N5-READER-box49.md. PASSIVE DRESSINGS of a game: append new vertices H (indices n0, n0+1, ...)
with edges only out of H into the old game or inside H, so no old vertex has an edge into H. Runs N5 on the base and on the dressed game and
checks that the run on the old vertices is the same (sigma, tau, sigma-bar, fallback flags, every old Xi as (cycle node, path-set as a vertex
set, length), and the phases), as L-SI's experiments/si/root/orcheck.py does for one reader (written fresh here, not imported). Then prints,
per phase of length >= n, the Xi-changes (XR) and Even / Odd strategy changes of every new vertex, the largest XR of an old vertex, and 2n.
An argument EDGE:P:hK adds the edge P -> hK at an old vertex P (then H has an old predecessor; the gadget is no longer passive and the
comparison is the test). Gadget spec: one argument per new vertex, OWNER:PRIO:SUCC1,SUCC2,...:START (owner 0 = Even, 1 = Odd; START = its sigma0 / tau0 successor);
a successor written hK means the K-th new vertex (h0 = index n0).
Usage: dress.py BASE.pg BASE.start OUT_PREFIX SPEC [SPEC ...]   (writes OUT_PREFIX.pg / .start, then runs the comparison)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, phases, load, readstart
from collections import Counter

def build(base, start, out, specs):
    L = [l.rstrip("\n") for l in open(base) if l.strip() and not l.lstrip().startswith("%")]
    n0 = len(L) - 1; assert L[0].startswith("parity")
    res = lambda x: n0 + int(x[1:]) if x.startswith("h") else int(x)
    ls = [l.rstrip("\n") for l in open(start) if l.strip()]
    edges = [sp for sp in specs if sp.startswith("EDGE:")]; specs = [sp for sp in specs if not sp.startswith("EDGE:")]
    for sp in edges:                               # EDGE:p:hK adds the edge p -> hK at an OLD vertex p (H is then not passive)
        _, p, y = sp.split(":"); p = int(p)
        f = L[p + 1].rstrip(";").split(); assert int(f[0]) == p
        L[p + 1] = " ".join(f[:3] + [f[3] + "," + str(res(y))] + f[4:]) + ";"
    for k, sp in enumerate(specs):
        ow, pr, su, st = sp.split(":"); su = [res(x) for x in su.split(",")]; st = res(st); assert st in su
        L.append(f"{n0 + k} {int(pr)} {int(ow)} {','.join(map(str, sorted(su)))};")
        ls[0 if ow == "0" else 1] += f" {n0 + k}:{st}"
    L[0] = f"parity {n0 + len(specs) - 1};"
    open(out + ".pg", "w").write("\n".join(L) + "\n"); open(out + ".start", "w").write("\n".join(ls) + "\n")
    return n0

def compare(base, bstart, dpg, dstart, quiet=False):
    g0, g1 = load(base), load(dpg); n0, n = g0.n, g1.n
    E0, R0 = rows(g0, readstart(bstart)); E1, R1 = rows(g1, readstart(dstart))
    vset = lambda E, m: frozenset(v for v in range(len(E.rank)) if m >> E.rank[v] & 1)
    old = range(n0); first = None
    for k in range(min(len(R0), len(R1))):
        a, b = R0[k], R1[k]
        ok = (a["s"][:n0] == b["s"][:n0] and a["t"][:n0] == b["t"][:n0] and a["sb"][:n0] == b["sb"][:n0] and a["fb"] == b["fb"]
              and all((a["vs"][v][0], vset(E0, a["vs"][v][1]), a["vs"][v][2]) == (b["vs"][v][0], vset(E1, b["vs"][v][1]), b["vs"][v][2]) for v in old))
        if not ok: first = k; break
    same = first is None and len(R0) == len(R1)
    P0 = list(phases(R0)); P1 = list(phases(R1))
    out = dict(same=same, first_diff=first, states=(len(R0), len(R1)), phases_equal=P0 == P1, n=n, rows=[])
    for i, j in P1:
        if j - i < n0: continue
        xr, sw = Counter(), Counter()
        for k in range(i, j):
            for z in range(n):
                if R1[k]["vs"][z] != R1[k + 1]["vs"][z]: xr[z] += 1
                own = g1.owner[z]
                if (R1[k]["s"][z] if own == 0 else R1[k]["sb"][z]) != (R1[k + 1]["s"][z] if own == 0 else R1[k + 1]["sb"][z]): sw[z] += 1
        oldmax = max((xr[z] for z in old), default=0)
        out["rows"].append(dict(phase=(i, j), length=j - i, fb=sum(R1[k]["fb"] for k in range(i, j)), oldmax=oldmax,
                                new=[(z, g1.owner[z], xr[z], sw[z]) for z in range(n0, n)], twon=2 * n))
    if not quiet:
        print("SAME" if same else f"DIFFERENT (first differing state {first})", "states", out["states"], "phases_equal", out["phases_equal"], "n", n)
        for r in out["rows"]:
            print(f"phase {r['phase']} len {r['length']} fallbacks {r['fb']} XR_max(old) {r['oldmax']} 2n {r['twon']} new (vertex, owner, XR, "
                  f"strategy changes): {r['new']}")
    return out

if __name__ == "__main__":
    base, bstart, outp, specs = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
    build(base, bstart, outp, specs)
    print("dressed:", outp + ".pg", " ".join(specs))
    compare(base, bstart, outp + ".pg", outp + ".start")
