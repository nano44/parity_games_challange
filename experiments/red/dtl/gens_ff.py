#!/usr/bin/env python3
"""L-RED R9 (2026-10-16): generators for the hand-built DTL gadgets of R9 section 4b. Even is the counted player.
hdelay m K: the one-search-delay ladder (H-level). Vertices: sink s (Odd, pr 1, self-loop); timer chain c_0..c_K (Even tops,
pr 2k+2, c_k -> y_k -> {c_k, c_{k-1}}, c_0 -> s) whose top c_K is the unique argmax of piece 0 (P1 = Dom(c_K), fixed);
z_0 (Even pr 1) -> c_K (always in P1); h_0 (Even pr 2K+6) -> q_0 (Even pr 1) -> r_0 (Odd pr 1) -> {e_0, z_0}, e_0 (Even pr 1)
-> h_0: a permanently stable top at piece 1 (its cycle's only escape z_0 is forgiven at piece 1). For j = 1..m the ladder
step h_j (Even pr 2K+6+2j) -> q_j -> r_j -> {e_j, x_j, g_{j-1}}, e_j -> {h_j, h_0}, x_j (Even pr 2) -> r_j (the deadlock:
plain attraction never gets r_j because x_j is reachable only through r_j), g_{j-1} (Even pr 1) -> h_{j-1} (the witness:
covered iff h_{j-1} is alive or removed). Prediction (R9 4b): h_j becomes stable at piece 1 exactly one search after
h_{j-1} did, because the tangle K_j = {x_j, r_j} (escapes e_j, g_{j-1}) is learned at a later piece only when g_{j-1} is
forgiven, and it rescues h_j at piece 1 only from the next search on. Expected: m+2 Even searches.
Usage: gens_ff.py hdelay m K > game.pg"""
import sys


class G:
    def __init__(self): self.v = []          # (name, pr, owner, succ names)
    def add(self, name, pr, ow, succ): self.v.append((name, pr, ow, list(succ))); return name
    def dump(self):
        idx = {name: i for i, (name, _, _, _) in enumerate(self.v)}
        out = [f"parity {len(self.v) - 1};"]
        for name, pr, ow, succ in self.v:
            out.append(f"{idx[name]} {pr} {ow} {','.join(str(idx[t]) for t in succ)} \"{name}\";")
        return "\n".join(out) + "\n"


def hdelay(m, K):
    g = G()
    g.add("s", 1, 1, ["s"])
    g.add("c0", 2, 0, ["s"])
    for k in range(1, K + 1):
        g.add(f"y{k}", 1, 1, [f"c{k}", f"c{k-1}"]); g.add(f"c{k}", 2 * k + 2, 0, [f"y{k}"])
    g.add("z0", 1, 0, [f"c{K}"])
    base = 2 * K + 6
    g.add("e0", 1, 0, ["h0"]); g.add("r0", 1, 1, ["e0", "z0"]); g.add("q0", 1, 0, ["r0"]); g.add("h0", base, 0, ["q0"])
    for j in range(1, m + 1):
        g.add(f"g{j-1}", 1, 0, [f"h{j-1}"])
        g.add(f"e{j}", 1, 0, [f"h{j}", "h0"]); g.add(f"x{j}", 2, 0, [f"r{j}"])
        g.add(f"r{j}", 1, 1, [f"e{j}", f"x{j}", f"g{j-1}"]); g.add(f"q{j}", 1, 0, [f"r{j}"]); g.add(f"h{j}", base + 2 * j, 0, [f"q{j}"])
    return g


if __name__ == "__main__":
    kind = sys.argv[1]
    if kind == "hdelay":
        sys.stdout.write(hdelay(int(sys.argv[2]), int(sys.argv[3])).dump())
