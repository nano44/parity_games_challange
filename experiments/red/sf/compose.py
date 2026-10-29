#!/usr/bin/env python3
"""L-RED: compose two fcN blocks (sbev.py N --drop fc). Block B keeps its priorities; block A's priorities are shifted above B's
(by an even offset, parity kept). Wiring MODE (comma list): 'sink' = B's FinalSink p_B -> A's StartEven s_A instead of B's q;
'root' = B's DecLaneOddRoot d gets an extra edge to s_A; 'sinkE' = p_B becomes Even with edges [q_B, s_A].
Usage: compose.py NA NB MODE > game.pg"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sbev import sbev


def parse(txt):
    V = []
    for line in txt.splitlines()[1:]:
        m = re.match(r'(\d+) (\d+) (\d+) ([\d,]+) "([^"]*)";', line)
        V.append([int(m.group(2)), int(m.group(3)), [int(x) for x in m.group(4).split(",")], m.group(5)])
    return V


def compose(NA, NB, mode):
    B = parse(sbev(NB, drop=("fc",))); A = parse(sbev(NA, drop=("fc",)))
    nb = len(B); off = max(v[0] for v in B) + 2; off += off % 2
    lab = lambda V, s: [i for i, v in enumerate(V) if v[3] == s][0]
    G = [[p, o, list(s), "B" + d] for p, o, s, d in B] + [[p + off, o, [x + nb for x in s], "A" + d] for p, o, s, d in A]
    sA = nb + lab(A, "s"); pB = lab(B, "p"); dB = lab(B, "d"); qB = lab(B, "q")
    if "sink" in mode: G[pB][2] = [sA]
    if "sinkE" in mode: G[pB][1] = 0; G[pB][2] = [qB, sA]
    if "root" in mode: G[dB][2] = sorted(set(G[dB][2] + [sA]))
    out = [f"parity {len(G) - 1};"] + [f'{i} {p} {o} {",".join(map(str, sorted(set(s))))} "{d}";' for i, (p, o, s, d) in enumerate(G)]
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    sys.stdout.write(compose(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3].split(",")))
