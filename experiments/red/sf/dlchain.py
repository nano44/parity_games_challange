#!/usr/bin/env python3
"""L-RED successor 29 (R116): dwN = fcN (sbev.py N --drop fc) + DELAY CHAINS ("repeaters") on the escape-chain edges v_i -> r_(i+1).
Each such edge becomes v_i -> u_i0 -> ... -> u_i(L-1) -> r_(i+1). u_ih is Even with edges {u_i(h+1) (r_(i+1) for the last), v_(i+1)};
for i = N-2 (no v_(N-1)) and with env FB=p the fallback is the sink p instead. u's priorities are low ODD and distinct (3, 5, ...),
ABOVE q's 1 (below q the valuation ignores them). Every other priority >= 2 is shifted up by 2M + 2 (M = number of u's), parity kept.
Idea (L-NEW box59 §1.3 LATENCY): the lane hears a set of bit j in 2 F-steps, the lower escape chain one step later, so EVERY set
cascades (not only records); the fallback v_(i+1) re-arms the repeater whenever bit i+1 resets. dwN := dlchain.py N 1, n = 26N + 9.
Usage: dlchain.py N L [EDGES] > game.pg   EDGES = 'all' (default) or a comma list of i."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from sbev import sbev
from compose import parse
FB = os.environ.get("FB", "v")


def dl(N, L, which="all"):
    G = [[p, o, list(s), d] for p, o, s, d in parse(sbev(N, drop=("fc",)))]
    lab = lambda s: [i for i, v in enumerate(G) if v[3] == s][0]
    P = lab("p"); idx = list(range(N - 1)) if which == "all" else [int(x) for x in which.split(",")]
    M = L * len(idx)
    for v in G:
        if v[0] >= 2: v[0] += 2 * M + 2           # q (priority 1) stays below the chains
    k = 0
    for i in idx:
        vi, ri = lab(f"v{i}"), lab(f"r{i + 1}")
        assert ri in G[vi][2], (i, G[vi])
        us = list(range(len(G), len(G) + L))
        for h, u in enumerate(us):
            nxt = us[h + 1] if h + 1 < L else ri
            alt = P if (FB == "p" or i + 1 >= N - 1) else lab(f"v{i + 1}")
            G.append([2 * k + 3, 0, [nxt, alt], f"u{i}_{h}"]); k += 1
        if us: G[vi][2] = [us[0] if s == ri else s for s in G[vi][2]]
    out = [f"parity {len(G) - 1};"] + [f'{i} {p} {o} {",".join(map(str, sorted(set(s))))} "{d}";' for i, (p, o, s, d) in enumerate(G)]
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    a = sys.argv[1:]
    sys.stdout.write(dl(int(a[0]), int(a[1]), a[2] if len(a) > 2 else "all"))
