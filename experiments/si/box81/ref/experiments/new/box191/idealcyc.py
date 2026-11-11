#!/usr/bin/env python3
"""Box 191 XI-CYCLIC (L-NEW successor 59): the model IDEAL-CYC(G) for ANY genome G (Xi-cycles allowed).
Game = R104's Gamma(G) (box189 gamma3.build(G, {})), every Even vertex that is not a mover FROZEN at R104's stated start
(beta -> its Xi-target or u, core K0 -> K3, K1 -> K1, K3 -> K2), Odd free everywhere (best response = VJ optimal counterstrategy).
A step = HOWARD (switch-best) at the movers: every mover goes to its successor of largest VJ value (ties: keep the current one, then
larger index); stop when no mover has a strictly better successor. Valuation engine = experiments/si/si.py Engine (VJ / Friedmann).
run(G) -> list of mover states (genome option indices), one per state.  Also: cycle-step / path-step decomposition (kinds)."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, "experiments/new/box189"), os.path.join(ROOT, "experiments/si"), os.path.join(ROOT, "experiments/harness")]
import gamma3, pg
from si import Engine

ONEP = os.environ.get("ONEP") == "1"     # ONE-PLAYER variant: every gate forced to its beta-face (Odd has no choice at gates)

def build(G):
    g, sig, tau, V = gamma3.build(G, set()); N = G["N"]; movers = [V[("x", x)] for x in range(N)]
    succ = [list(s) if (g.owner[v] == 1 or v in movers) else [sig[v]] for v, s in enumerate(g.succ)]
    if ONEP:
        for x in range(N):
            for k in range(len(G["opts"][x])): succ[V[("g", (x, k))]] = [V[("b", (x, k))]]
    h = pg.Game(list(g.prio), list(g.owner), succ)
    inv = {V[("g", (x, k))]: k for x in range(N) for k in range(len(G["opts"][x]))}
    s0 = tuple(sig[v] if h.owner[v] == 0 else -1 for v in range(h.n))
    return h, s0, movers, inv

def run(G, cap=10 ** 5, want_kinds=False):
    h, s, movers, inv = build(G); E = Engine(h); out = [tuple(inv[s[x]] for x in movers)]; kinds = []
    vs, _ = E.evaluate(s)
    while len(out) - 1 < cap:
        ns = list(s)
        for x in movers:
            ns[x] = max(h.succ[x], key=lambda w: (E.key(vs[w]), w == s[x], w))
        ns = tuple(ns)
        if ns == s: break
        nvs, _ = E.evaluate(ns)
        if want_kinds: kinds.append("C" if any(nvs[v][0] != vs[v][0] for v in range(h.n)) else "p")
        s, vs = ns, nvs; out.append(tuple(inv[s[x]] for x in movers))
    return (out, "".join(kinds)) if want_kinds else out

if __name__ == "__main__":
    for f in sys.argv[1:]:
        st, k = run(json.load(open(f)), want_kinds=True); print(f"{os.path.basename(f)} T {len(st) - 1} kinds {k}")
