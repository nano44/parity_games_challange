#!/usr/bin/env python3
"""L-RED: named trace of N5-SF (sf2.py engine): per iteration, Even vertices that switch (label:old->new), Odd vertices whose
sigma-bar changes, tau changes. Labels from the .pg description strings. Usage: sftrace.py GAME.pg [--mode spec|orig] [--start F]"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sf2, pg, n5b

def labels(path):
    lab = {}
    for line in open(path):
        m = re.match(r'\s*(\d+)\s+\d+\s+\d+\s+[\d,]+\s*"([^"]*)"', line)
        if m: lab[int(m.group(1))] = m.group(2)
    return lab

def main():
    a = sys.argv[1:]; mode = a[a.index("--mode") + 1] if "--mode" in a else "spec"
    start = a[a.index("--start") + 1] if "--start" in a else None
    g = pg.read(a[0]); lab = labels(a[0]); L = lambda v: lab.get(v, str(v))
    s = sf2.SF(g, mode=mode); rec = []
    sig, tau = n5b.read_start(start, g) if start else (None, None)
    s.run_sf(sig, tau, rec=rec)
    for i, (x, y) in enumerate(zip(rec, rec[1:])):
        ds = [f"{L(v)}:{L(x['s'][v])}>{L(y['s'][v])}" for v in range(g.n) if x["s"][v] != y["s"][v]]
        db = [f"{L(v)}:{L(x['sb'][v])}>{L(y['sb'][v])}" for v in range(g.n) if x["sb"][v] != y["sb"][v]]
        dt = [f"{L(v)}:{L(x['t'][v])}>{L(y['t'][v])}" for v in range(g.n) if x["t"][v] != y["t"][v]]
        print(f"{i+1:4d} |Is|={x['nIs']:3d} S[{' '.join(ds)}]" + (f"  SBAR[{' '.join(db)}]" if db else "") + (f"  T[{' '.join(dt)}]" if dt else ""))

if __name__ == "__main__":
    main()
