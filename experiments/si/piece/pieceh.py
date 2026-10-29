#!/usr/bin/env python3
"""L-SI box 25 (successor 21): DATA for CONJECTURE PIECE (docs/si/N5-PIECE-box25.md). For every sigma-bar-constant piece [a, b] of every
fallback-free in-phase run (same pieces as root/staticdepth.py), classify which of RESULTS R77's hypotheses fail:
  H3W  at some state the W-cycles differ from the honest cycles;   H3C  the cycles (either frame) change inside the piece;
  LW   lambda_W (W cycle node per vertex) changes inside the piece; H4 the end-state graph H_b has a cycle off the cycle vertices.
Per piece also: length, n, the number of Even vertices that switch, and SLACK := (n - 1) - length. Prints one line per failing piece
(VERB=1) and a summary. Usage: pieceh.py --list FILE (env NMAX) | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, phases, load, readstart, Dset, avoid
from staticdepth import walk, depth
C = Counter(); OUT = []

def norm(cs): return frozenset(min(tuple(c[k:] + c[:k]) for k in range(len(c))) for c in cs)
def cyc(nx, n): return norm(frozenset(walk(nx, v)[1] for v in range(n)))

def pieces(R):
    for i, j in phases(R):
        rs, s = [], i
        for k in range(i, j):
            if R[k]["fb"]: rs.append((s, k)); s = k + 1
        rs.append((s, j))
        for s, e in rs:
            a = s
            while a < e:
                b = a
                while b < e and R[b + 1]["sb"] == R[a]["sb"]: b += 1
                if b > a: yield a, b
                a = b + 1 if b > a else a + 1

def run(g, name, start=None):
    E, R = rows(g, start); n = g.n
    for a, b in pieces(R):
        ln = b - a; B = R[b]; D = Dset(g, B)
        cw = [cyc(R[t]["wn"], n) for t in range(a, b + 1)]; ch = [cyc(R[t]["nxt"], n) for t in range(a, b + 1)]
        h3w = any(cw[k] != ch[k] for k in range(len(cw))); h3c = any(x != cw[0] for x in cw) or any(x != ch[0] for x in ch)
        lw = any(tuple(x[0] for x in R[t]["W"]) != tuple(x[0] for x in R[a]["W"]) for t in range(a, b + 1))
        oncyc = {v for c in cw[-1] for v in c}
        try: depth(g, B, D, oncyc); h4 = False
        except (ValueError, RecursionError): h4 = True
        sw = {v for t in range(a, b) for v in range(n) if g.owner[v] == 0 and R[t]["s"][v] != R[t + 1]["s"][v]}
        fail = h3w or h3c or h4
        C["pieces"] += 1; C["fail"] += fail; C["h3w"] += h3w; C["h3c"] += h3c; C["lw"] += lw; C["h4"] += h4
        key = "F" if fail else "OK"
        C[key + "_len_max"] = max(C[key + "_len_max"], ln); C[key + "_slack_min"] = min(C.get(key + "_slack_min", 10 ** 9), n - 1 - ln)
        C[key + "_ratio_max_x1000"] = max(C[key + "_ratio_max_x1000"], (1000 * ln) // max(n - 1, 1))
        if ln > n - 1: C["PIECE_V"] += 1
        if fail: OUT.append((ln, n, name, a, b, h3w, h3c, lw, h4, len(sw), len(D)))

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            f = line.split()[0] if line.strip() and not line.startswith("#") else None
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > int(os.environ.get("NMAX", "10000")): continue
            run(g, f)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    if os.environ.get("VERB"):
        for x in sorted(OUT, key=lambda x: (x[1] - 1 - x[0], -x[0])): print("FAILPIECE len %d n %d %s [%d,%d] H3W %d H3C %d LW %d H4 %d sw %d |D| %d" % x)
    print("PIECE PASS" if "PIECE_V" not in C else "PIECE FAIL")

if __name__ == "__main__":
    main()
