#!/usr/bin/env python3
"""L-COMP box 47 (successor 22; Lead 09:08Z 2026-11-13): replay of a genome on L-NEW's box 190 n5v (run UNCHANGED from an archive of claude/l-new,
env LNEW = its root), from S3 on Γ3(G) = box 189 gamma3.build(G, {"K", "pe", "pb", "m"}) (the pads L-RED R241 uses), with the e-vertices
optionally renumbered among themselves:
  genome json may carry "eperm" (a permutation of 0..M-1): the e-vertex of the i-th option in GATE order (box 189's own e-order) is moved to
  the eperm[i]-th e-slot (the e-slots are box 189's e-indices, ascending). Priorities and edges move with the vertex (an isomorphic copy).
Modes (n5v): spec (N5), xi (N5′-xi, Howard's tie rule), seq, idx. Per mode: T = steps before the first fallback, Ttot, F (fallbacks), and
sig = the movers' option sequence s_0..s_T (option index k per mover per state; mover state read through the m-pads), sha1 of it.
Usage: replay47.py G.json [MODE ...] [--cap C] [--dump OUT.json]   -> one line per mode"""
import sys, os, json, hashlib
L = os.environ["LNEW"]; NEW = os.path.join(L, "experiments", "new")
sys.path[:0] = [os.path.join(NEW, "box190"), os.path.join(NEW, "box189"), os.path.join(NEW, "box21"), NEW, os.path.join(L, "experiments", "si"), os.path.join(L, "experiments", "harness")]
import gamma3, n5v, n5x, n5, pg
from si import Engine
PADS = {"K", "pe", "pb", "m"}


def build(G):
    g, sig, tau, V = gamma3.build(G, PADS); ep = G.get("eperm")
    if ep is None: return g, V
    O = [(x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]
    go = sorted(O, key=lambda q: G["gate"][q[0]][q[1]]); slots = sorted(V[("e", q)] for q in go)
    assert sorted(ep) == list(range(len(go))), "eperm is not a permutation of 0..M-1"
    pi = list(range(g.n))
    for i, q in enumerate(go): pi[V[("e", q)]] = slots[ep[i]]
    n = g.n; prio = [0] * n; own = [0] * n; succ = [None] * n
    for v in range(n): prio[pi[v]] = g.prio[v]; own[pi[v]] = g.owner[v]; succ[pi[v]] = sorted(pi[w] for w in g.succ[v])
    return pg.Game(prio, own, succ), {k: pi[v] for k, v in V.items()}


def mstate(G, V, sigma):
    inv = {V[("m", (x, k))]: k for x in range(G["N"]) for k in range(len(G["opts"][x]))}
    return tuple(inv[sigma[V[("x", x)]]] for x in range(G["N"]))


def run(G, mode, cap=10 ** 6):
    g, V = build(G); E, Ed = Engine(g), Engine(n5.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    seq = [mstate(G, V, sigma)]; T = None; F = 0; t = 0
    while t < cap:
        r = n5v.step(g, E, Ed, sigma, tau, mode)
        if r is None: break
        sigma, tau, fb = r[0], r[1], r[4]; t += 1
        if fb and T is None: T = t - 1
        F += fb
        if T is None: seq.append(mstate(G, V, sigma))
    if T is None: T = t
    return dict(T=T, Ttot=t, F=F, seq=seq, n=g.n)


if __name__ == "__main__":
    a = sys.argv[1:]; cap = 10 ** 6; dump = None
    if "--cap" in a: i = a.index("--cap"); cap = int(a[i + 1]); del a[i:i + 2]
    if "--dump" in a: i = a.index("--dump"); dump = a[i + 1]; del a[i:i + 2]
    fn, modes = a[0], (a[1:] or ["spec"])
    G = json.load(open(fn)); G = G.get("genome", G) if "N" not in G else G
    if "N" not in G: G = json.load(open(fn))["genome"]
    M = sum(len(o) for o in G["opts"]); out = {}
    for m in modes:
        r = run(G, m, cap); h = hashlib.sha1(json.dumps(r["seq"]).encode()).hexdigest()[:12]; out[m] = r
        print("%s N %d M %d N+M %d n %d eperm %d mode %s T %d Ttot %d F %d sig %s" % (os.path.basename(fn), G["N"], M, G["N"] + M, r["n"], int("eperm" in G), m, r["T"], r["Ttot"], r["F"], h), flush=True)
    if dump: json.dump({m: r["seq"] for m, r in out.items()}, open(dump, "w"))
