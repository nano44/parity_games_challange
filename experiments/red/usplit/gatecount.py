#!/usr/bin/env python3
"""Box 51: per run (o1_19.trace), per phase: D-membership toggles of every Odd vertex (enter / leave D); per Even edge (x, z): forbidden
EPISODES (maximal runs of states where (x, z) is forbidden, §16 definition with L = −1) and switches into it; Ξ changes of Odd vertices
(ρ_q); stretch_D boundaries (D, R_D, gate values). Usage: gatecount.py game.pg start.json [--oink]"""
import sys, os, json, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "o1")); sys.path.insert(0, os.path.join(HERE, "..", "rec0"))
import o1_19 as O, pg, verify, rec0_20 as R0
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); st = json.load(open(sys.argv[2]))["start"]
n = g.n; S, FB, E = O.trace(g, st)
ev = [E.evaluate(s) for s, _ in S]; Xi = [X for X, _ in ev]; SB = [B for _, B in ev]
W = [[R0.playval(g, E, s, t, x) for x in range(n)] for s, t in S]
lam = [tuple(x[0] for x in X) for X in Xi]; K = E.key; co = lambda v: (E.rew[v[0]], E.weight(v[1]))
D = [frozenset(u for u in range(n) if g.owner[u] == 1 and SB[k][u] != S[k][1][u]) for k in range(len(S))]
ph = 1 + sum(1 for k in range(len(S) - 1) if lam[k] != lam[k + 1] or S[k][1] != S[k + 1][1])
tog = {u: sum(1 for k in range(len(S) - 1) if (u in D[k]) != (u in D[k + 1])) for u in range(n) if g.owner[u] == 1}
rho = {u: sum(1 for k in range(len(S) - 1) if K(Xi[k][u]) != K(Xi[k + 1][u])) for u in range(n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1}
ep = {}; sw = {}
for x in range(n):
    if g.owner[x] != 0: continue
    for z in set(g.succ[x]):
        f = [z != S[k][0][x] and co(W[k][z]) > co(W[k][S[k][0][x]]) and not K(Xi[k][z]) > K(Xi[k][S[k][0][x]]) for k in range(len(S))]
        e = sum(1 for k in range(len(S)) if f[k] and (k == 0 or not f[k - 1]))
        if e: ep[(x, z)] = e; sw[(x, z)] = sum(1 for k in range(len(S) - 1) if S[k][0][x] != z and S[k + 1][0][x] == z)
r = dict(n=n, ITER=len(FB), FB=sum(1 for f in FB if f), phases=ph, D_changes=sum(1 for k in range(len(S) - 1) if D[k] != D[k + 1]),
         max_toggles=max(tog.values()), toggles={u: t for u, t in tog.items() if t}, max_rho=max(rho.values()),
         max_forb_episodes=max(ep.values(), default=0), edges_multi_episode={f"{a}->{b}": e for (a, b), e in ep.items() if e > 1},
         switch_into={f"{a}->{b}": sw[(a, b)] for (a, b), e in ep.items() if e > 1},
         max_switches_vertex=max(sum(1 for k in range(len(S) - 1) if S[k][0][x] != S[k + 1][0][x]) for x in range(n) if g.owner[x] == 0))
r["switches_top"] = sorted(((sum(1 for k in range(len(S) - 1) if S[k][0][x] != S[k + 1][0][x]), x) for x in range(n) if g.owner[x] == 0), reverse=True)[:3]
win, ws = E.regions(S[-1][0]); e = verify.check(g, win, ws); r["out"] = "OK" if not e else e[0]
if "--oink" in sys.argv: r["oink"] = O.oink_check(g, win, ws, tempfile.mkdtemp())
print(json.dumps(r))
