#!/usr/bin/env python3
"""Collect results/automata/*.json into results/table.md (w and s per convention) with the universal-tree cross-check."""
import json, glob, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from wsep.utrees import f_upper, g_lower
from wsep.analyze import analyze

R = {}
for f in sorted(glob.glob('results/automata/*.json')):
    r = json.load(open(f))
    if '_k' in f or 'eager' in f:
        continue
    R[(r['mode'], r['conv'], r['n'], r['d'])] = r
ns = sorted({k[2] for k in R}); ds = sorted({k[3] for k in R})
out = ["# w(n,d) and s(n,d): exact values (SAT, verified by the independent checker)", "",
       "Cell = w / s. '-' = not computed. '*' after w: the minimal weak separator found is not strong (its transition",
       "graph has a reachable odd cycle). Universal-tree row: least leaves of an (n, d/2)-universal tree for even d",
       "(CFGO Prop. 6.10/6.11 recursions f = g where they agree; brute force in wsep/utrees.py where run); equals s^E by",
       "CFGO Thm 4.1 + Lemma 6.8. Conventions: E = edge-labelled multigraphs (CDFJLP/CFGO), S = at most one label per",
       "ordered pair, V = vertex-labelled (TARGET.md). Columns: d = largest letter of the alphabet {1..d}.", ""]
for conv in ['E', 'S', 'V']:
    out.append(f"## Convention {conv}"); out.append("")
    out.append("| n \\ d | " + " | ".join(str(d) for d in ds) + " |")
    out.append("| --- | " + " | ".join("---" for _ in ds) + " |")
    for n in ns:
        row = []
        for d in ds:
            w = R.get(('weak', conv, n, d)); s = R.get(('strong', conv, n, d))
            ws = '-' if w is None else str(w['value']) + ('*' if w['automaton'] and not analyze(w)['strong'] else '')
            ss = '-' if s is None else str(s['value'])
            row.append(f"{ws} / {ss}")
        out.append(f"| {n} | " + " | ".join(row) + " |")
    out.append("")
out.append("## Universal trees (n, h = d/2), least leaves: g(n,h) <= value <= f(n,h) (CFGO Props 6.11 / 6.10)"); out.append("")
out.append("| n \\ d | " + " | ".join(str(d) for d in ds if d % 2 == 0) + " |")
out.append("| --- | " + " | ".join("---" for d in ds if d % 2 == 0) + " |")
for n in ns:
    cells = []
    for d in ds:
        if d % 2: continue
        h = d // 2; g, f = g_lower(n, h), f_upper(n, h)
        cells.append(str(g) if g == f else f"[{g},{f}]")
    out.append(f"| {n} | " + " | ".join(cells) + " |")
out.append("")
pathlib.Path('results/table.md').write_text("\n".join(out) + "\n")
print("\n".join(out))
