#!/usr/bin/env python3
"""Box 10: structured exploit variants on the gadgeted Odd-CDAG; prints tail length, whether sigma is optimal, and the CDAG switch trace."""
import sys
from tailsim import build, tail, tau_all_sink, cdag_target
n = int(sys.argv[1]); variant = sys.argv[2]
ex = {}
for x in range(1, n + 1):
    for u in range(x):
        if variant == "up1" and x < n: ex[(x, u)] = [x + 1]                      # e[y,w] -> y+1
        if variant == "up1top" : ex[(x, u)] = [x + 1] if x < n else [n - 1]       # top gadgets -> n-1
        if variant == "upall" and x < n: ex[(x, u)] = list(range(x + 1, n + 1))  # e[y,w] -> every higher vertex
        if variant == "upg" and x < n: ex[(x, u)] = [(x + 1, u)]                  # e[y,w] -> e[y+1,w]
        if variant == "upg_up1" and x < n: ex[(x, u)] = [(x + 1, u), x + 1]
g, sigma, gid = build(n, ex)
r = tail(g, sigma, tau_all_sink(g, gid, n))
print(f"n={n} variant={variant} |V|={g.n} tail steps={r['steps']} sigma optimal={r['optimal_sigma']} even_moves={r['even_moves']} fallbacks={r['fallbacks']}")
for k, (sw, f, a, b) in enumerate(r["hist"]):
    print(" ", k, [(x, cdag_target(g, gid, o), cdag_target(g, gid, t)) for x, o, t in sw], "fb" if f else "", "|Iτ|", b)
