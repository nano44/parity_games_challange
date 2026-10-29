#!/usr/bin/env python3
r"""REFEREE-2 successor 20 (Opus 5.5, D15): own control for P-N5-MPGS Part (B), Lemma GATE-SHUT (docs/lit/P-N5-MPGS.md, sha1 24913a7f
@ l-lit a23179b0). State loop = R2-N5-DUAL/dual_check.Runner (my lane's SPEC loop on si.py = SPEC S1's own implementation, read-only).
The lane's T34-gateshut-check.py, L-COMP's n5b / hn are NOT imported. Everything below is written from the packet's B0 definitions.
At every state t = (sigma, tau) of a run, on G^d (owners swapped, Omega + 1): (Xi_tau, taubar) = S1 on G^d, I_tau = SPEC S2 on G^d.
For every Odd e, h := tau(e), every successor d != h of e that is Even, every simple path pi = (d = pi_1, ..., pi_m) of distinct Even
vertices with pi_k -> pi_{k+1} and pi_m -> e (at most PCAP paths per (t, e, d), DFS in index order), Q := pi + {e}:
  (H1) rank(u) > rank(c_h) for all u in Q, c_h the cycle node of Xi_tau(h); (H2) the (taubar, tau)-play rho from h (prefix and cycle)
  avoids Q; (H3) the top-rank vertex of Q has even Omega in G.
Checks (each must be 0):
  GS     (H1)-(H3) => (e, d) not in I_tau.
  GS2    proof step 2: with sigma' := taubar except along pi (pi_k -> pi_{k+1}, pi_m -> e), the play from h is rho, vertex by vertex.
  GS3    step 3: the play value of d under (sigma', tau) on G^d = (c_h, P(rho) + Q, len(rho) + |Q|).
  GS4    step 4: V strictly worse in G^d's order than Xi_tau(h) (and strictly better in G's order: Fact B1 instance).
  GS5    step 5 (B2 = (VJ) on G^d): Xi_tau(d) <=_d V.
  GSC    Corollary: tau_t(e) = h and some pi with (H1)-(H3) for (e, d) at t => tau_{t+1}(e) != d.
  B1     Fact B1 on random pairs (same cycle node, P != P'): X <_d X' iff X' < X (FB1 pairs per game).
  ENGXI  premise data: engine Xi_tau(v) = play value of (taubar, tau) from v on G^d, every v (SPEC S1-val; standing premise of R57).
Controls (counted per (t, e, d); expected to bite: each hypothesis is needed):
  X1 (H2),(H3) hold for some pi, (H1) fails for it, no pi satisfies all three, and (e, d) in I_tau;  X2 the same with (H2) failing;
  X3 the same with (H3) failing; FLIP all h -> d moves of tau; FLIPH those at a state with an (H1)-(H3) path (must equal GSC = 0).
Mode tau: the Lemma (not GSC) at NT arbitrary (sigma, tau) per random game, Even share pe (no N5 run).
Mode alltau: the Lemma at every tau of random games (Odd strategy count <= 256).
Usage: gs_check.py random N nmin nmax seed [starts] | files list.txt [runs] | tau N nmin nmax seed NT [pe] | alltau N nmin nmax seed [pe]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL"))
import dual_check as DC
pg, Engine = DC.pg, DC.Engine
PCAP = int(os.environ.get("PCAP", "64"))
FB1 = int(os.environ.get("FB1", "200"))


class St:
    def __init__(s): s.c = {}
    def inc(s, k, d=1): s.c[k] = s.c.get(k, 0) + d
    def bad(s, k, msg):
        s.inc(k)
        if s.c[k] <= 5: print("VIOLATION", k, msg, flush=True)


def play(nx, v):
    seen, path, x = {}, [], v
    while x not in seen:
        seen[x] = len(path); path.append(x); x = nx[x]
    return path, seen[x]


def value(Ed, nx, v):
    path, j = play(nx, v)
    c = max(path[j:], key=lambda y: Ed.pp[y]); i = path.index(c); m = 0
    for y in path[:i]:
        if Ed.rank[y] > Ed.rank[c]: m |= Ed.bit[y]
    return (c, m, i)


def even_paths(g, d, e):
    """simple paths of Even vertices from d whose last vertex has an edge to e (DFS, index order, at most PCAP)."""
    out = []
    def dfs(x, path, vis):
        if len(out) >= PCAP: return
        if e in g.succ[x]: out.append(list(path))
        for y in sorted(set(g.succ[x])):
            if y not in vis and g.owner[y] == 0:
                vis.add(y); path.append(y); dfs(y, path, vis); path.pop(); vis.discard(y)
    if g.owner[d] == 0: dfs(d, [d], {d})
    return out


def check_fb1(g, E, Ed, rng, st):
    n = g.n
    for _ in range(FB1):
        c = rng.randrange(n); hi = [u for u in range(n) if E.rank[u] > E.rank[c]]
        m1 = sum(E.bit[u] for u in hi if rng.random() < 0.5); m2 = sum(E.bit[u] for u in hi if rng.random() < 0.5)
        if m1 == m2: continue
        X, Y = (c, m1, rng.randrange(n)), (c, m2, rng.randrange(n))
        st.inc("B1_pairs")
        if (Ed.key(X) < Ed.key(Y)) != (E.key(Y) < E.key(X)): st.bad("B1", f"c={c} {m1} {m2}")


def run_game(g, s, t, st, name, rng):
    E, Ed = Engine(g), Engine(DC.dual(g)); n = g.n
    check_fb1(g, E, Ed, rng, st)
    states = [(s, t)] if os.environ.get("NORUN") else DC.Runner(g).run(s, t)[0]
    paths = {}
    for k, (sg, tu) in enumerate(states):
        st.inc("states")
        vt, tb = Ed.evaluate(tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n)))
        It = set(Ed.improving(tuple(tu), vt))
        nx = [tb[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
        for v in range(n):
            st.inc("ENGXI_checks")
            if value(Ed, nx, v) != tuple(vt[v]): st.bad("ENGXI", f"{name} k={k} v={v}")
        nxt = states[k + 1][1] if k + 1 < len(states) else None
        for e in range(n):
            if g.owner[e] != 1: continue
            h = tu[e]; rho, _ = play(nx, h); rset = set(rho); ch = vt[h][0]
            for d in sorted(set(g.succ[e])):
                if d == h: continue
                moved = nxt is not None and nxt[e] == d
                if moved: st.inc("FLIP")
                if g.owner[d] != 0: continue
                key = (e, d)
                if key not in paths: paths[key] = even_paths(g, d, e)
                allok, fl = False, set()
                for pi in paths[key]:
                    Q = pi + [e]
                    h1 = all(E.rank[u] > E.rank[ch] for u in Q)
                    h2 = not (rset & set(Q))
                    top = max(Q, key=lambda u: E.rank[u]); h3 = g.prio[top] % 2 == 0
                    if h1 and h2 and h3:
                        allok = True; st.inc("GS_paths")
                        check_steps(g, E, Ed, nx, vt, tu, e, h, d, pi, rho, st, name, k)
                    elif (h2, h3) == (True, True): fl.add(1)
                    elif (h1, h3) == (True, True): fl.add(2)
                    elif (h1, h2) == (True, True): fl.add(3)
                if allok:
                    st.inc("GS_triples")
                    if key in It: st.bad("GS", f"{name} k={k} e={e} h={h} d={d}")
                    if moved: st.bad("GSC", f"{name} k={k} e={e} h={h} d={d}"); st.inc("FLIPH")
                else:
                    for f in fl:
                        st.inc(f"H{f}fail_triples")
                        if key in It: st.inc(f"X{f}")


def check_steps(g, E, Ed, nx, vt, tu, e, h, d, pi, rho, st, name, k):
    n = g.n; nx2 = list(nx)
    for a, b in zip(pi, pi[1:] + [e]): nx2[a] = b
    rho2, _ = play(nx2, h)
    if rho2 != rho: st.bad("GS2", f"{name} k={k} e={e} d={d}")
    V = value(Ed, nx2, d); Xh = tuple(vt[h])
    Qm = sum(Ed.bit[u] for u in pi + [e])
    if V != (Xh[0], Xh[1] | Qm, Xh[2] + len(pi) + 1) or (Xh[1] & Qm): st.bad("GS3", f"{name} k={k} e={e} d={d} V={V} Xh={Xh}")
    if not (Ed.key(V) < Ed.key(Xh) and E.key(Xh) < E.key(V)): st.bad("GS4", f"{name} k={k} e={e} d={d}")
    if not (Ed.key(tuple(vt[d])) <= Ed.key(V)): st.bad("GS5", f"{name} k={k} e={e} d={d}")


def main():
    st = St(); a = sys.argv[1:]; rng = random.Random(2020)
    if a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); ns = int(a[5]) if len(a) > 5 else 2; rng = random.Random(seed)
        for i in range(N):
            g = DC.rand_game(rng, rng.randint(nmin, nmax), "kO")
            for r in range(ns + 1):
                if r == 0: s, t = Engine(g).initial("best"), Engine(DC.dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, list(s), list(t), st, f"rand{seed}:{i}#{r}", rng)
    elif a[0] == "tau":   # the Lemma at arbitrary states: random games, NT random (sigma, tau) each, no run (NORUN)
        os.environ["NORUN"] = "1"
        N, nmin, nmax, seed, NT = map(int, a[1:6]); rng = random.Random(seed); pe = float(a[6]) if len(a) > 6 else 0.5
        for i in range(N):
            nn = rng.randint(nmin, nmax)
            g = DC.rand_game(rng, nn, "kO")
            g = pg.Game(list(g.prio), [0 if rng.random() < pe else 1 for _ in range(nn)], [list(x) for x in g.succ])
            for r in range(NT):
                s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, s, t, st, f"tau{seed}:{i}#{r}", rng)
    elif a[0] == "alltau":   # the Lemma at EVERY tau (product of Odd out-degrees <= 256) of random games; sigma irrelevant to I_tau
        os.environ["NORUN"] = "1"; import itertools
        N, nmin, nmax, seed = map(int, a[1:5]); rng = random.Random(seed); pe = float(a[5]) if len(a) > 5 else 0.6
        for i in range(N):
            nn = rng.randint(nmin, nmax)
            g = DC.rand_game(rng, nn, "kO")
            g = pg.Game(list(g.prio), [0 if rng.random() < pe else 1 for _ in range(nn)], [list(x) for x in g.succ])
            odd = [v for v in range(nn) if g.owner[v] == 1]; tot = 1
            for v in odd: tot *= len(set(g.succ[v]))
            if tot > 256: continue
            s = [rng.choice(g.succ[v]) for v in range(nn)]
            for ch in itertools.product(*[sorted(set(g.succ[v])) for v in odd]):
                t = list(s)
                for v, w in zip(odd, ch): t[v] = w
                run_game(g, s, t, st, f"alltau{seed}:{i}", rng)
    elif a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 2
        for path in [l.split()[0] for l in open(a[1]) if l.strip()]:
            g = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                if r == 0: s, t = Engine(g).initial("best"), Engine(DC.dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, list(s), list(t), st, f"{path}#{r}", rng)
    print("MODE", " ".join(a), "PCAP", PCAP, "FB1", FB1)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    bad = sum(st.c.get(k, 0) for k in ("GS", "GS2", "GS3", "GS4", "GS5", "GSC", "B1", "ENGXI"))
    print("RESULT", "PASS" if bad == 0 else "FAIL", "violations", bad)


if __name__ == "__main__":
    main()
