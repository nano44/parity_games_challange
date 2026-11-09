#!/usr/bin/env python3
"""L-COMP box 36: Python glue for the C engine fast36.c (bin/fast36_w1 for n <= 64, bin/fast36_w8 for n <= 512)."""
import os, subprocess, json
H = os.path.dirname(os.path.abspath(__file__))


def gtext(G):
    N = G["N"]; L = [f"{N} {sum(len(o) for o in G['opts'])}", " ".join(map(str, G["lev"]))]; br = []; bp = []
    for x in range(N):
        for k, (wt, xt, b) in enumerate(G["opts"][x]):
            L.append(f"{x} {wt} {xt} {b} {G['gate'][x][k]}")
    L.append(" ".join(map(str, G["br"]))); L.append(" ".join(map(str, G["bp"]))); L.append(" ".join(map(str, G["start"])))
    return "\n".join(L) + "\n"


def one(G, noelev=False):
    n = G["N"] + 8 * sum(len(o) for o in G["opts"]) + 10
    w = next(w for w in (1, 8, 16, 48) if n <= 64 * w)
    exe = os.path.join(H, "bin", f"fast36_w{w}")
    env = dict(os.environ); env.pop("FAST36_NOELEV", None)
    if noelev: env["FAST36_NOELEV"] = "1"
    out = subprocess.run([exe, "one"], input=gtext(G), capture_output=True, text=True, env=env, check=True).stdout.split("\n")
    h = out[0].split(); T3, fb = int(h[1]), int(h[3]); rows = []
    for line in out[1:]:
        if line.startswith("gate"):
            _, x, k, f, l = line.split(); rows.append(((int(x), int(k)), int(f), int(l)))
    return T3, fb, sorted(rows)


def run_block(N, lev, D, xts, M):
    exe = os.path.join(H, "bin", "fast36_w1")
    args = [exe, "block", str(N), str(M)] + [str(a) for a in lev] + [str(a) for a in D] + [str(a) for a in xts]
    d = json.loads(subprocess.run(args, capture_output=True, text=True, check=True).stdout)
    assert d.pop("capped") == 0, "capped run in block"
    for key in ("ratio_arg", "kfx_arg"):
        d[key].update(lev=list(lev), D=list(D), xts=list(xts))
    return d
