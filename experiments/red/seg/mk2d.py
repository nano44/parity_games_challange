#!/usr/bin/env python3
"""L-RED successor 25: hand-designed two-deadlock gadget for CONJECTURE SEG-COUNT (docs/red/R105). Named vertices, PGSolver output.
Roles: h (H-sink), w1, w2 (W-sinks), A1/A2/A3 Odd self-loop W-cycles (tau = self, odd priorities 7 > 5 > 3), z the honest sink
(Even self-loop, priority 41). Markers > 41 order the honest values. Pads = Odd single-successor chains (length only).
Usage: mk2d.py OUT.pg OUT.start [key=value ...]"""
import sys
P = dict(lq=1, lo2=2, Bq=43, G3=44, M0=46, B1=47, MP=48, M2=50, h=38, loopA1=7, loopA2=5, loopA3=3, z=41)
for kv in sys.argv[3:]:
    k, v = kv.split("="); P[k] = int(v)
V, E, pr, own, sig, tau = [], {}, {}, {}, {}, {}
low = iter(x for x in range(8, 40) if x != 38)
def add(name, owner, prio=None, succ=()):
    V.append(name); own[name] = owner; pr[name] = prio if prio is not None else next(low); E[name] = list(succ)
def chain(prefix, k, target):
    """k Odd pads ending at target; returns the head."""
    nxt = target
    for i in range(k):
        add(f"{prefix}{i}", 1, succ=[nxt]); nxt = f"{prefix}{i}"
    return nxt
add("z", 0, P["z"], ["z"])
add("M2", 1, P["M2"], ["z"]); add("M0", 1, P["M0"], ["z"])
co = chain("po", P["lo2"], "M2"); ce = chain("pe", P["lq"], "M2")
add("h", 0, P["h"], ["z", "A1", "C2", "YH"]); sig["h"] = "z"
add("w1", 0, succ=["M0", "A2"]); sig["w1"] = "M0"
add("w2", 0, succ=["o2", "A3"]); sig["w2"] = "o2"
add("o2", 0, succ=[co, "h"]); sig["o2"] = co
add("EQ", 0, succ=[ce, "h"]); sig["EQ"] = ce
add("A1", 1, P["loopA1"], ["A1", "B1"]); tau["A1"] = "A1"
add("B1", 1, P["B1"], ["w2"])
add("A2", 1, P["loopA2"], ["A2", "h"]); tau["A2"] = "A2"
add("A3", 1, P["loopA3"], ["A3", "G3"]); tau["A3"] = "A3"
add("G3", 1, P["G3"], ["h"])
add("MP", 1, P["MP"], ["w1"])
add("Bq", 1, P["Bq"], ["EQ"])
add("C2", 1, succ=["MP", "Bq"]); tau["C2"] = "MP"
add("YH", 1, succ=["w2", "o2"]); tau["YH"] = "w2"
ix = {v: i for i, v in enumerate(V)}
with open(sys.argv[1], "w") as f:
    f.write(f"parity {len(V) - 1};\n")
    for v in V:
        f.write(f"{ix[v]} {pr[v]} {own[v]} {','.join(str(ix[w]) for w in E[v])} \"{v}\";\n")
with open(sys.argv[2], "w") as f:
    f.write("SIGMA0 " + " ".join(f"{ix[v]}:{ix[sig.get(v, E[v][0])]}" for v in V if own[v] == 0) + "\n")
    f.write("TAU0 " + " ".join(f"{ix[v]}:{ix[tau.get(v, E[v][0])]}" for v in V if own[v] == 1) + "\n")
print(" ".join(f"{v}={ix[v]}" for v in V))
