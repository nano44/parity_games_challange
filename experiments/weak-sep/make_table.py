#!/usr/bin/env python3
"""Collect results/automata/*.json into results/table.md (w and s per convention) with the universal-tree cross-check."""
import json, glob, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from wsep.utrees import f_upper, g_lower
from wsep.analyze import analyze

R = {}
partial = []  # '_k<j>' files: searches started at k = k_start, exact only when k_start is covered by a lower bound
for f in sorted(glob.glob(str(pathlib.Path(__file__).parent / 'results/automata/*.json'))):
    r = json.load(open(f))
    if 'eager' in f:
        continue
    if '_k' in f:
        partial.append((f, r)); continue
    R[(r['mode'], r['conv'], r['n'], r['d'])] = r

def mono_lower(mode, conv, n, d):
    """Largest exact value at a cell (n' <= n, d' <= d), same mode and convention: a lower bound, since every
    (n,d)-separator is an (n',d')-separator (fewer vertices, smaller alphabet; S1-statement.md monotonicity)."""
    return max([r['value'] for (m, c, n2, d2), r in R.items() if m == mode and c == conv and n2 <= n and d2 <= d], default=1)

# A partial run refuted k_start .. value-1; it is exact when no value below k_start is possible (k_start <= lower bound).
for f, r in partial:
    key = (r['mode'], r['conv'], r['n'], r['d'])
    if key not in R and r['k_start'] <= mono_lower(*key):
        R[key] = r
        print(f"exact from partial run: {pathlib.Path(f).name} (k_start {r['k_start']} <= monotone lower bound {mono_lower(*key)})")
ns = sorted({k[2] for k in R}); ds = sorted({k[3] for k in R})
out = ["# w(n,d) and s(n,d): exact values (SAT, verified by the independent checker)", "",
       "Cell = w / s. '-' = not computed. '?' = strongness of the witness not analysed (slow family). '*' after w: the minimal weak separator found is not strong (its transition",
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
            slow = (conv == 'S' and d >= 5) or (conv == 'V' and d >= 9) or n >= 5 or (n == 4 and d >= 5)
            ws = '-' if w is None else str(w['value']) + ('*' if w['automaton'] and not slow and not analyze(w)['strong'] else ('?' if w['automaton'] and slow else ''))
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
out.append("## n = 5 bounds from single-k queries (results/n5/; value >= k+1 by S3 Lemma P)"); out.append("")
out.append("| cell | query | answer | bound | certificate |")
out.append("| --- | --- | --- | --- | --- |")
for f in sorted(glob.glob(str(pathlib.Path(__file__).parent / 'results/n5/*.json'))):
    r = json.load(open(f))
    if r['status'] != 'UNSAT':
        continue
    lrat = pathlib.Path(f[:-5] + '.lrat.log')
    cert = ('LRAT VERIFIED (' + lrat.name + ')') if lrat.exists() and 'VERIFIED' in lrat.read_text() else 'SOLVER-ONLY (no proof)'
    sym = 'w' if r['mode'] == 'weak' else 's'
    out.append(f"| {r['conv']} ({r['n']},{r['d']}) | {r['mode']} k = {r['k']} | UNSAT | {sym} >= {r['k'] + 1} | {cert} |")
out.append("")
(pathlib.Path(__file__).parent / 'results/table.md').write_text("\n".join(out) + "\n")
print("\n".join(out))
