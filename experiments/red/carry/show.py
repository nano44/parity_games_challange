#!/usr/bin/env python3
"""Debug view (L-RED CARRY box): run the instrumented tracer and print every piece and pruning round with vertex NAMES
(the .pg labels), regions per top, candidates, forgiven, distractions, and new tangles. show.py GAME.pg [--search K] [--rounds]"""
import sys, os, re, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ff", os.path.join(HERE, "..", "dtl", "dtl_flipflop.py"))
ff = importlib.util.module_from_spec(spec); spec.loader.exec_module(ff)
path = sys.argv[1]
names = {}
for line in open(path):
    m = re.match(r'\s*(\d+)\s+\d+\s+\d+\s+[\d,]+\s*"([^"]*)"', line)
    if m: names[int(m.group(1))] = m.group(2)
d = ff.load(path, "oink")
N = lambda v: names.get(d.idx[v], str(d.idx[v]))
S = lambda s: "{" + ",".join(sorted(N(v) for v in s)) + "}"
only = int(sys.argv[sys.argv.index("--search") + 1]) if "--search" in sys.argv else None
rounds = "--rounds" in sys.argv
print(f"n={d.n} tangles={d.tangles} dominions={d.dominions} iterations={d.iterations}")
for s in d.searches:
    if only is not None and s["index"] != only: continue
    print(f"== search {s['index']} player {s['player']} new tangles {len(s['tangles'])} dominions {s['dominions']}")
    bvs = iter(s["bv"])
    for i, pc in enumerate(s["pieces"]):
        kind = pc["kind"]
        extra = {k: v for k, v in pc.items() if k not in ("kind", "depth", "rounds", "tangles", "bv")}
        ex = " ".join(f"{k}={S(v) if isinstance(v, (set, frozenset, list)) else v}" for k, v in extra.items())
        print(f"  piece {i} d{pc['depth']} {kind} {ex}")
        if rounds:
            for r, rd in enumerate(pc.get("rounds", [])):
                regs = " ".join(f"{N(t)}:{S(z)}" for t, z in sorted(rd["regions"].items(), reverse=True))
                print(f"     r{r} V={S(rd['V'])} cands={S(rd['cands'])} forg={ {N(k): v for k, v in rd['forgiven'].items()} } dist={S(rd['distractions'])}")
                print(f"        regions {regs}")
        for top, vs, _ in pc["tangles"]:
            print(f"    NEW TANGLE top {N(top)} {S(vs)}")
