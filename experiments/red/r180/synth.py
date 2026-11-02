#!/usr/bin/env python3
"""L-RED R180 SYNTH: z3 search for an IDEAL-model Xi-structure (fastabs semantics: acyclic G_X, one beta per option with free rank
and parity, free Xi-targets, AUX extra Xi-only Even vertices with 2 static options) that makes N5's S4a dynamics follow a given
LADDERBF chain exactly. Unknowns: xt per face, beta rank/parity, xorder positions. Data: gates and the chain (ladderchain.py).
Constraint per step t and vertex v: the chain's sigma_(t+1)(v) is the key-least option of A_t(v) = {sigma_t(v)} + Xi-better faces.
If SAT, writes a fastabs genome and replays it with fastabs.simulate. Usage: synth.py chain.json out_genome.json [prefix_len]"""
import sys, os, json
import z3
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r177"))
import fastabs as F
C = json.load(open(sys.argv[1])); d, gate, chain = C["d"], C["gate"], C["chain"]
if len(sys.argv) > 3: chain = chain[:int(sys.argv[3]) + 1]
N = 2 * d; lev = [v // 2 for v in range(N)]; L = len(chain) - 1
def keys(s):
    key = [None] * N; ok = {}
    for v in range(N):
        for k in (0, 1): ok[(v, k)] = ((gate[v][k],) if lev[v] == 0 else key[2 * (lev[v] - 1) + k] + (gate[v][k],))
        key[v] = ok[(v, s[v])]
    return ok
faces = [(v, k) for v in range(N) for k in (0, 1)]; M = len(faces)
sol = z3.Solver()
rank = {f: z3.Int(f"r_{f[0]}_{f[1]}") for f in faces}; par = {f: z3.Bool(f"p_{f[0]}_{f[1]}") for f in faces}
xt = {f: z3.Int(f"x_{f[0]}_{f[1]}") for f in faces}; pos = [z3.Int(f"pos_{v}") for v in range(N)]
sol.add(z3.Distinct(*rank.values()))
for f in faces:
    sol.add(rank[f] >= 0, rank[f] < M, xt[f] >= -1, xt[f] < N, xt[f] != f[0])
    for u in range(N): sol.add(z3.Implies(xt[f] == u, pos[u] > pos[f[0]]))
def wt(f):
    mag = z3.Sum([z3.If(rank[f] == r, 2 ** r, 0) for r in range(M)])
    return z3.If(par[f], -mag, mag)
W = {f: wt(f) for f in faces}
for t in range(L + 1):
    s = chain[t]; X = [z3.Int(f"X_{t}_{u}") for u in range(N)]
    def Fv(v, k): return W[(v, k)] + z3.Sum([z3.If(xt[(v, k)] == u, X[u], 0) for u in range(N)])
    for u in range(N): sol.add(X[u] == Fv(u, s[u]))
    if t == L: break
    nx = chain[t + 1]; key = keys(nx)
    for v in range(N):
        cur, nxt = s[v], nx[v]; o = 1 - cur
        avail_o = Fv(v, o) > Fv(v, cur)
        if nxt != cur: sol.add(avail_o)
        elif key[(v, o)] < key[(v, cur)]: sol.add(z3.Not(avail_o))
r = sol.check(); print("SYNTH d", d, "steps", L, "->", r, flush=True)
if r == z3.sat:
    m = sol.model(); ev = lambda e: m.eval(e, model_completion=True)
    order = sorted(range(N), key=lambda v: ev(pos[v]).as_long())
    G = dict(N=N, lev=lev, deg=2, opts=[[[-1 if lev[v] == 0 else 2 * (lev[v] - 1) + k, ev(xt[(v, k)]).as_long(), 2 * v + k] for k in (0, 1)] for v in range(N)],
             gate=[list(gate[v]) for v in range(N)], br=[ev(rank[f]).as_long() for f in faces], bp=[1 if z3.is_true(ev(par[f])) else 0 for f in faces],
             start=list(chain[0]), xorder=order)
    json.dump(G, open(sys.argv[2], "w")); print("replay", F.simulate(G))
