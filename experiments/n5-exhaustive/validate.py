"""Validate exh.analyse's re-entry classifier against L-RED retcheck.py on the longest phase of named instances.
Prints, per instance, retcheck's line and exh's (longest-phase-only) A/B counts plus all-phase counts."""
import os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
import exh
from exh import Engine, dual, wvals, Rset, trace, load, odd_choice
for path in sys.argv[1:]:
    rc = subprocess.run([sys.executable, os.path.join(ROOT, "experiments/red/n5inj/retcheck.py"), path], capture_output=True, text=True).stdout.strip()
    g = load(path); o = odd_choice(g); st, _ = trace(g, None, check=False)
    E, Ed = Engine(g), Engine(dual(g)); lam = []
    for s, t in st:
        lam.append((tuple(x[0] for x in E.evaluate(s)[0]), tuple(y[0] for y in Ed.evaluate(t)[0])))
    runs, a0 = [], 0
    for i in range(1, len(st) + 1):
        if i == len(st) or lam[i] != lam[i - 1]: runs.append((a0, i - 1)); a0 = i
    a, b = max(runs, key=lambda r: r[1] - r[0])
    x = exh.analyse(g, st[a:b + 1], o); rA, rB = x['reA'], x['reB']    # longest phase only (one lambda value -> one run)
    allr = exh.analyse(g, st, o)
    print(rc); print(f"   exh longest phase {a}..{b}: A {rA} B {rB}; all phases: maxph {allr['maxph']} thch {allr['thch']} trust {allr['trust']} A {allr['reA']} B {allr['reB']}")
