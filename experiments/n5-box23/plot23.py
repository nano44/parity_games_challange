#!/usr/bin/env python3
"""Box 23 (c): plot of the climb maxima against n, from results/climbs_end.txt (no plotting library needed: writes SVG by hand).
Series (best over every climb that measures it, at each n): R*_F with a free start pair (families fresh, chain), R*_F from the S3 start
(s3fresh, s3chain), and the longest W-run |F| found by any climb (all families). Dashed line: y = n. Light and dark via CSS.
Usage: plot23.py results/climbs_end.txt results/rstar_vs_n.svg"""
import re
import sys

E = {"free": {}, "s3": {}, "F": {}}
for line in open(sys.argv[1]):
    m = re.search(r"rs_(\w+?)_n(\d+)_r\d+\.log END steps \d+ best \((\d+), (\d+), (\d+)\) n", line)
    if not m:
        continue
    fam, n, a, b, c = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))
    if fam in ("fresh", "chain"):
        E["free"][n] = max(E["free"].get(n, 0), a)
    if fam in ("s3fresh", "s3chain"):
        E["s3"][n] = max(E["s3"].get(n, 0), a)
    F = a if fam.startswith("F") else (b if fam.startswith("fl") else c)
    E["F"][n] = max(E["F"].get(n, 0), F)
W, H, L, R, T, B = 640, 400, 56, 150, 48, 48
xmax, ymax = 64, 64
X = lambda n: L + (W - L - R) * n / xmax
Y = lambda v: H - B - (H - T - B) * v / ymax
S = [("F", "longest W-run |F|", "s3", "circle"), ("free", "R*_F, free start pair", "s1", "square"), ("s3", "R*_F, S3 start", "s2", "diamond")]
o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="system-ui, sans-serif" font-size="12">',
     "<style>.bg{fill:#fcfcfb}.t1{fill:#1d1d1b}.t2{fill:#5f5e58}.g{stroke:#e4e3de}.ax{stroke:#a8a7a0}.ref{stroke:#a8a7a0}"
     ".s1{stroke:#2a78d6;fill:#2a78d6}.s2{stroke:#eb6834;fill:#eb6834}.s3{stroke:#1baf7a;fill:#1baf7a}"
     "@media (prefers-color-scheme: dark){.bg{fill:#1a1a19}.t1{fill:#f0efec}.t2{fill:#c3c2b7}.g{stroke:#2e2e2b}.ax{stroke:#6b6a63}"
     ".ref{stroke:#6b6a63}.s1{stroke:#3987e5;fill:#3987e5}.s2{stroke:#d95926;fill:#d95926}.s3{stroke:#199e70;fill:#199e70}}</style>",
     f'<rect class="bg" width="{W}" height="{H}"/>',
     f'<text class="t1" x="{L}" y="22" font-size="14" font-weight="600">Box 23: climb maxima per W-run of N5 against n (lower bounds, budget-limited)</text>']
for v in range(0, ymax + 1, 16):
    o.append(f'<line class="g" x1="{L}" x2="{W - R}" y1="{Y(v)}" y2="{Y(v)}"/><text class="t2" x="{L - 8}" y="{Y(v) + 4}" text-anchor="end">{v}</text>')
for n in (0, 10, 20, 30, 40, 50, 60):
    o.append(f'<text class="t2" x="{X(n)}" y="{H - B + 18}" text-anchor="middle">{n}</text>')
o.append(f'<line class="ax" x1="{L}" x2="{W - R}" y1="{Y(0)}" y2="{Y(0)}"/>')
o.append(f'<text class="t2" x="{(L + W - R) / 2}" y="{H - 10}" text-anchor="middle">n (vertices)</text>')
o.append(f'<line class="ref" stroke-dasharray="4 4" stroke-width="1.5" x1="{X(0)}" y1="{Y(0)}" x2="{X(60)}" y2="{Y(60)}"/>'
         f'<text class="t2" x="{X(60) + 6}" y="{Y(60) + 4}">y = n</text>')
for key, name, cls, mk in S:
    pts = sorted(E[key].items())
    if not pts:
        continue
    o.append(f'<polyline class="{cls}" style="fill:none" stroke-width="2" points="' + " ".join(f"{X(n)},{Y(v)}" for n, v in pts) + '"/>')
    for n, v in pts:
        x, y = X(n), Y(v)
        if mk == "circle":
            o.append(f'<circle class="{cls}" cx="{x}" cy="{y}" r="4.5" stroke="#fcfcfb" stroke-width="1.5"><title>{name}: n {n}, {v}</title></circle>')
        elif mk == "square":
            o.append(f'<rect class="{cls}" x="{x - 4}" y="{y - 4}" width="8" height="8" rx="1"><title>{name}: n {n}, {v}</title></rect>')
        else:
            o.append(f'<path class="{cls}" d="M{x} {y - 5.5}L{x + 5.5} {y}L{x} {y + 5.5}L{x - 5.5} {y}Z"><title>{name}: n {n}, {v}</title></path>')
    n, v = pts[-1]
    o.append(f'<text class="t1" x="{X(n) + 10}" y="{Y(v) + 4 + (12 if key == "s3" else 0) - (6 if key == "F" else 0)}">{name.split(",")[0] if key == "F" else name} ({v})</text>')
o.append("</svg>")
open(sys.argv[2], "w").write("\n".join(o))
print({k: dict(sorted(v.items())) for k, v in E.items()})
