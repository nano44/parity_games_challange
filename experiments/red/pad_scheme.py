#!/usr/bin/env python3
"""Structured pads (g > 0: geometric g^(n-i); g <= 0: polynomial (n+1-i)^|g|) on the parity encoding of FHZ's G_{n,1,1,1}: pads(x_i) = round(W[x] * g^(n - i)) for x in {u, w, a, b} at
level i; S7 (vjfast most-improved) iterations for n in a range; prints growth.  Usage: pad_scheme.py VJFAST g Wu Ww Wa Wb nmin nmax"""
import sys, os, subprocess, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import fhz
vjf, g, Wu, Ww, Wa, Wb, nmin, nmax = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]), int(sys.argv[7]), int(sys.argv[8])
W = {"u": Wu, "w": Ww, "a": Wa, "b": Wb}
row = []
for n in range(nmin, nmax + 1):
    G, P, B0, B0P, names, ename, pid = fhz.build(n, 1, 1, 1)
    with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f: start = fhz.export_pg(P, B0P, names, f.name); base = open(f.name).read().splitlines(); os.unlink(f.name)
    lines = list(base[1:]); nx = P.N; total = 0
    for x in range(G.N - 1):
        lab = names[x + 1]; typ = lab[0]; lvl = int(lab[1:].split(",")[0])
        k = int(round(W[typ] * (g ** (n - lvl) if g > 0 else (n + 1 - lvl) ** (-g)))); total += k   # g <= 0: polynomial (n+1-i)^|g|
        for _ in range(k): lines.append(f"{nx} 0 0 {pid[('v', x)]};"); nx += 1
    with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f: f.write(f"parity {nx - 1};\n" + "\n".join(lines) + "\n"); p = f.name
    r = subprocess.run([vjf, "most-improved", p, "--start", start], capture_output=True, text=True, timeout=3000); os.unlink(p)
    it = int([l for l in r.stderr.splitlines() if l.startswith("solved with")][0].split()[2]); row.append((n, it, total))
    print(f"g={g} W=({Wu},{Ww},{Wa},{Wb}) n={n}: {it} iterations (pads {total}, |V|={nx})", flush=True)
