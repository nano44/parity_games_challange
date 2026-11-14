#!/usr/bin/env python3
"""L-RED 71 R247: variants of Friedmann's G_n (gens_red.friedmann_Gn, with its start iota) for the RF experiments.
fvar247.py n OUT.pg [opts]   opts: buf=K (K Even buffer vertices of priority 0 between g_j and f_j, each with the second option k_j),
noCS (c loses its edge to s), decoy=all|1 (k_i -> z_i -> d_i, z_i Even, priority 0, one successor; for every i or for i = 1 only)"""
import sys, re, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r237"), os.path.join(HERE, "..")]
import gens_red
def build(n, opts):
    txt = gens_red.friedmann_Gn(n); rows = {}; start = {}
    for line in txt.splitlines():
        m = re.match(r'(\d+) (\d+) (\d+) ([\d,]+) "([^"]+)";', line)
        if m: rows[int(m.group(1))] = [int(m.group(2)), int(m.group(3)), [int(x) for x in m.group(4).split(",")], m.group(5)]
        if line.startswith("% start"): start = {int(a): int(b) for a, b in (x.split(":") for x in line.split()[2:])}
    byl = {r[3]: v for v, r in rows.items()}; nxt = len(rows)
    def new(prio, owner, succ, lab, st=None):
        nonlocal nxt
        rows[nxt] = [prio, owner, succ, lab]
        if st is not None: start[nxt] = st
        nxt += 1; return nxt - 1
    if opts.get("noCS"):
        c = byl["c"]; rows[c][2] = [w for w in rows[c][2] if w != byl["s"]]; start[c] = byl["r"]
    if opts.get("decoy"):
        for i in range(1, n + 1):
            if opts["decoy"] == "1" and i > 1: continue
            z = new(0, 0, [byl[f"d{i}"]], f"z{i}"); rows[byl[f"k{i}"]][2].append(z)
    K = int(opts.get("buf", 0))
    if K:
        for j in range(1, n + 1):
            g, f, k = byl[f"g{j}"], byl[f"f{j}"], byl[f"k{j}"]
            prev = f
            for b in range(K):
                # buffer: Even, low even priority 0, options {prev, k_j}; starts at k_j (as g_j does)
                prev = new(0, 0, [prev, k], f"b{j}_{b}", k)
            rows[g][2] = [prev if w == f else w for w in rows[g][2]]
    return rows, start
def dumps(rows, start):
    n = len(rows)
    return f"parity {n - 1};\n" + "".join(f'{v} {rows[v][0]} {rows[v][1]} {",".join(map(str, rows[v][2]))} "{rows[v][3]}";\n' for v in range(n)) + "% start " + " ".join(f"{v}:{w}" for v, w in sorted(start.items())) + "\n"
if __name__ == "__main__":
    n = int(sys.argv[1]); opts = dict((a.split("=") + ["1"])[:2] for a in sys.argv[3:])
    rows, start = build(n, opts); open(sys.argv[2], "w").write(dumps(rows, start))
