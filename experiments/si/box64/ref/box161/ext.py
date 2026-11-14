#!/usr/bin/env python3
"""L-NEW box 161: the external-flip model E_m (box 160 §1, Lemma W-ONLY). A genome G with levels 0..m (R197 2-wide ladder, ISO: no
option has a level-0 mover as Xi-target); level 0 = the external agent: its two movers' states are set by a schedule, every other mover
follows the IDEAL step rule (keys under the NEW state). Helpers: random ISO ladders, simulation under a schedule, frozen remainders
R_q(s) (run of the genome with level 0 frozen at q), all with the box 150 simulator."""
import os, json, random, itertools
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box150", "check.py")
ns = {"__file__": P}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]; restrict = ns["restrict"]

def rand_iso(d, rng):
    N = 2 * d; lev = [v // 2 for v in range(N)]
    order = list(range(N)); rng.shuffle(order); pos = {v: i for i, v in enumerate(order)}
    opts, M = [], 0
    for x in range(N):
        o = []
        for k in range(2):
            wt = 2 * (lev[x] - 1) + k if lev[x] > 0 else -1
            later = [v for v in range(N) if pos[v] > pos[x] and lev[v] > 0]
            xt = rng.choice(later) if later and rng.random() < 0.8 else -1
            o.append([wt, xt, M]); M += 1
        opts.append(o)
    g = list(range(M)); rng.shuffle(g); it = iter(g); gate = [[next(it), next(it)] for _ in range(N)]
    br = list(range(M)); rng.shuffle(br); bp = [rng.randint(0, 1) for _ in range(M)]
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": [rng.randint(0, 1) for _ in range(N)],
            "xorder": order}

def step_forced(g, cur, q):
    """one IDEAL step with the level-0 movers forced to q; returns the new state (tuple)"""
    N = g.N; A = [g.avail(cur, v) for v in range(N)]; key = [None] * N; nw = list(cur)
    for v in g.byl:
        k = q[v] if g.lev[v] == 0 else min(A[v], key=lambda k: g.optkey(key, v, k))
        nw[v] = k; key[v] = g.optkey(key, v, k)
    return tuple(nw)

def frozen_R(G, g, s, q, cap=10000):
    """number of steps (moving a mover of level >= 1) of the run from s with level 0 held at q"""
    cur = tuple(q[v] if g.lev[v] == 0 else s[v] for v in range(g.N)); n = 0
    while n < cap:
        nw = step_forced(g, cur, q)
        if nw == cur: return n
        cur = nw; n += 1
    raise RuntimeError("cap")

def b0(g, s):
    k = g.keys(s); return int(k[0] < k[1])
