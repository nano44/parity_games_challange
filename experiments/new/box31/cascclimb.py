#!/usr/bin/env python3
"""Box 31 (a) climbs on o-cyclic C^1O (SPEC tie-breaks, best-reward start). Fitness by mode:
  thw : route-form pieces with c_θ more relevant than c_w (P3′'s case): (Ξ-changes on R in the piece, piece length)  [Lead request]
  flat: W-flat runs in route-form pieces: (max switches of one R-vertex in one run, R-switches in the run, run length)
Any CASC violation is printed at once and saved as <out>_viol.pg. Usage: cascclimb.py mode seed secs out seed.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from casccheck import *
from climb_fix import mutate

def fit_g(g, mode):
    rows, o = rows_of(g, None, cap=400); best = (0, 0, 0); k = 0; viol = 0
    while k < len(rows):
        if not rows[k]["rf"]: k += 1; continue
        j = k
        while j + 1 < len(rows) and rows[j + 1]["rf"] and all(rows[j + 1][f] == rows[k][f] for f in ("ph", "R", "th", "w")): j += 1
        Rs = [v for v in rows[k]["R"] if v != o]; E = Engine(g)
        if mode == "thw":
            if j > k and E.rank[rows[k]["cth"]] > E.rank[rows[k]["cw"]]:
                xc = sum(1 for i in range(k, j) if any(rows[i]["Wk"][v] != rows[i + 1]["Wk"][v] or rows[i]["s"][v] != rows[i + 1]["s"][v] for v in Rs))
                best = max(best, (xc, j - k, 0))
        else:
            i = k
            while i < j:
                if rows[i]["fb"] or any(rows[i]["Wk"][v] != rows[i + 1]["Wk"][v] for v in Rs): i += 1; continue
                a = i; per = {}; tot = 0
                while i < j and not rows[i]["fb"] and all(rows[i]["Wk"][v] == rows[i + 1]["Wk"][v] for v in Rs):
                    for v in Rs:
                        if g.owner[v] == 0 and rows[i]["s"][v] != rows[i + 1]["s"][v]:
                            per[v] = per.get(v, 0) + 1; tot += 1
                            if i - a > rows[i]["Wl"][v] - rows[i]["Wl"][o] - 2: viol += 1
                    i += 1
                best = max(best, (max(per.values()) if per else 0, tot, i - a))
        k = j + 1
    return best, viol

def fit(G, mode):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, -1, -1), 0
    o = odd[0]; g = pg.Game(*G); Y = split(g, o)
    if not any(w in Y for w in G[2][o]): return (-1, -1, -1), 0
    try: return fit_g(g, mode)
    except Exception: return (-1, -1, -1), 0

def save(path, G):
    n = len(G[0]); open(path, "w").write(f"parity {n-1};\n" + "".join(f"{v} {G[0][v]} {G[1][v]} {','.join(map(str, G[2][v]))};\n" for v in range(n)))

if __name__ == "__main__":
    mode, seed, secs, out = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    g = load(sys.argv[5]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f, _ = fit(G, mode)
    t0 = time.time(); it = 0; print("start", f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh, vi = fit(H, mode)
        if vi: print(f"CASC VIOLATION it {it} fit {fh}", flush=True); save(out + "_viol.pg", H)
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); save(out + ".pg", H)
            G, f = H, fh
    print("FINAL", f, it, flush=True)
