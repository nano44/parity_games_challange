#!/usr/bin/env python3
"""L-RED successor 38 (Lead 13:32Z, D-ODD-1 / F-1): validate START files. Every SIGMA0 / TAU0 entry v:w must have v owned by the right
player (SIGMA0: Even = 0, TAU0: Odd = 1) and (v, w) in E. Usage: startck.py G.pg START [G2.pg START2 ...]; prints OK or each bad entry,
exit 1 if any is bad. Also importable: check(pgpath, startpath) -> list of problems."""
import sys, re
def load(p):
    own, succ = {}, {}
    for line in open(p):
        m = re.match(r'\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)', line)
        if m: v = int(m.group(1)); own[v] = int(m.group(3)); succ[v] = {int(a) for a in m.group(4).split(",")}
    return own, succ
def check(gp, sp):
    own, succ = load(gp); bad = []
    for line in open(sp):
        t = line.split()
        if not t or t[0] not in ("SIGMA0", "TAU0"): continue
        pl = 0 if t[0] == "SIGMA0" else 1
        for e in t[1:]:
            v, w = map(int, e.split(":"))
            if v not in own: bad.append(f"{t[0]} {v}:{w} unknown vertex")
            elif own[v] != pl: bad.append(f"{t[0]} {v}:{w} owner {own[v]}")
            elif w not in succ[v]: bad.append(f"{t[0]} {v}:{w} NON-EDGE (succ {sorted(succ[v])[:6]}...)")
    return bad
def repair(gp, sp, op):
    own, succ = load(gp); out = []
    for line in open(sp):
        t = line.split()
        if not t or t[0] not in ("SIGMA0", "TAU0"): out.append(line.rstrip("\n")); continue
        pl = 0 if t[0] == "SIGMA0" else 1; keep = [t[0]]
        for e in t[1:]:
            v, w = map(int, e.split(":"))
            if v not in own or own[v] != pl: continue
            keep.append(f"{v}:{w if w in succ[v] else min(succ[v])}")
        out.append(" ".join(keep))
    open(op, "w").write("\n".join(out) + "\n")
if __name__ == "__main__" and sys.argv[1] == "--repair": repair(*sys.argv[2:5]); sys.exit(0)
if __name__ == "__main__":
    rc = 0
    for gp, sp in zip(sys.argv[1::2], sys.argv[2::2]):
        b = check(gp, sp); rc |= bool(b)
        print(f"{sp}: " + ("OK" if not b else f"BAD {len(b)}: " + "; ".join(b[:5])))
    sys.exit(rc)
# repair mode (appended): python3 startck.py --repair G.pg START OUT.start  -> each bad entry v:w becomes v:min(succ(v)); owner-mismatch
# entries are dropped.
