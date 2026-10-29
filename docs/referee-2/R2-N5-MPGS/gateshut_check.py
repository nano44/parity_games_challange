#!/usr/bin/env python3
r"""REFEREE-2 successor 19 (Opus 5.5, D15): independent check of P-N5-MPGS Part (B), Lemma GATE-SHUT and added statement (B)
(docs/lit/P-N5-MPGS.md, sha1 24913a7f @ l-lit a23179b0). Own code on my lane's SPEC loop (dual_check.Runner on si.py = SPEC S1, read-only);
G^d = dual_check.dual(g) (owner swapped, Omega + 1); Xi_tau, taubar, I_tau from S1's procedure on G^d (Engine(dual).evaluate / improving), Xi_tau
also recomputed as the play value of (tau, taubar) on G^d (DENG). The lane's T34 script / L-COMP's n5b, hn.py are NOT imported.
Gates enumerated on EVERY game (not only Friedmann's): at every state t, every Odd e with h := tau(e), every Even successor d != h of e, every
sequence pi of distinct Even vertices from d with pi_m -> e (m <= PCAP_LEN, at most PCAP paths per (e, d)); Q := pi + {e}; rho := the
(taubar, tau)-play from h; c_h := cycle node of Xi_tau(h).
Checks where (H1) rank(u) > rank(c_h) on Q, (H2) rho avoids Q, (H3) the top-rank vertex of Q has even Omega:
  GS      (e, d) not in I_tau_t
  S3      V := play value on G^d of the (sigma', tau)-play from d (sigma' = taubar rerouted along pi) has cycle node c_h and set P(rho) + Q
  S4      V <_d Xi_tau(h) (strictly worse for Odd);  S5  Xi_tau(d) <=_d V
  B1      Fact B1 on every pair of G^d valuations at the state with equal cycle node and different P: X <_d X' iff X' < X (G order)
  CORB    at a transition t -> t+1 from such a state: tau_{t+1}(e) != d
Controls (counted CTL_*, expected nonzero; NOT violations): CTL_noH3 ((H1), (H2) hold, top of Q odd: (e, d) in I_tau), CTL_noH2 ((H1), (H3)
hold, rho meets Q: (e, d) in I_tau), CTL_noH1 ((H2), (H3) hold, some u in Q below c_h: (e, d) in I_tau); CTL_flip_nohyp (h -> d moves of tau
at gates where some hypothesis fails).
Usage: gateshut_check.py files list [runs] | pairs list prefix | start game.pg [game.start] | random N nmin nmax seed k [starts]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND"))
import rund_check as R
DC, pg, Stats = R.DC, R.pg, R.Stats
PCAP_LEN = int(os.environ.get("PCAP_LEN", "6"))
PCAP = int(os.environ.get("PCAP", "40"))
B1CAP = int(os.environ.get("B1CAP", "200"))


def run_game(gp, s, t, st, name, rng):
    g, n = gp, gp.n
    states, fbs = DC.Runner(gp).run(s, t)
    gd = DC.dual(gp); Ed = DC.Engine(gd); E = DC.Engine(gp)
    st.inc("runs"); st.inc("states", len(states))
    # Even-vertex paths are a function of the game only: precompute per (e, d)
    paths = {}
    for e in range(n):
        if g.owner[e] != 1: continue
        for d in set(g.succ[e]):
            if g.owner[d] != 0: continue
            out = []
            def dfs(x, path, seen):
                if len(out) >= PCAP: return
                if e in g.succ[x]: out.append(list(path))
                if len(path) >= PCAP_LEN: return
                for y in sorted(set(g.succ[x])):
                    if g.owner[y] == 0 and y not in seen:
                        seen.add(y); path.append(y); dfs(y, path, seen); path.pop(); seen.discard(y)
            dfs(d, [d], {d})
            paths[(e, d)] = out
    for k, (sg, tu) in enumerate(states):
        vt, tb = Ed.evaluate(tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n)))
        It = set(Ed.improving(tuple(tu), vt))
        nx = [tu[v] if g.owner[v] == 1 else tb[v] for v in range(n)]
        st.inc("DENG_checks")
        if any(R.play_value(Ed, nx, v) != tuple(vt[v]) for v in range(n)): st.bad("DENG", f"{name}@{k}")
        # Fact B1 on sampled pairs of valuations with the same cycle node
        byc = {}
        for v in range(n): byc.setdefault(vt[v][0], []).append(tuple(vt[v]))
        cnt = 0
        for c, vals in byc.items():
            for i in range(len(vals)):
                for j in range(len(vals)):
                    if cnt >= B1CAP: break
                    X, Y = vals[i], vals[j]
                    if X[1] == Y[1]: continue
                    cnt += 1; st.inc("B1_checks")
                    if (Ed.key(X) < Ed.key(Y)) != (E.key(Y) < E.key(X)): st.bad("B1", f"{name}@{k} c={c}")
        nxt = states[k + 1][1] if k + 1 < len(states) else None
        for e in range(n):
            if g.owner[e] != 1: continue
            h = tu[e]
            rho, _ = R.lasso(nx, h); rhos = set(rho)
            ch = vt[h][0]
            for d in set(g.succ[e]):
                if d == h or g.owner[d] != 0: continue
                ps = paths.get((e, d), [])
                anyhyp = False
                for pi in ps:
                    Q = pi + [e]
                    h1 = all(E.rank[u] > E.rank[ch] for u in Q)
                    h2 = not (rhos & set(Q))
                    top = max(Q, key=lambda u: E.rank[u])
                    h3 = g.prio[top] % 2 == 0
                    inI = (e, d) in It
                    if h1 and h2 and h3:
                        anyhyp = True
                        st.inc("GS_checks")
                        if inI: st.bad("GS", f"{name}@{k} e={e} d={d} pi={pi}")
                        nx2 = list(nx)
                        for j in range(len(pi) - 1): nx2[pi[j]] = pi[j + 1]
                        nx2[pi[-1]] = e
                        V = R.play_value(Ed, nx2, d)
                        Prho = R.play_value(Ed, nx, h)[1]
                        Qm = 0
                        for u in Q: Qm |= Ed.bit[u]
                        if V[0] != ch or V[1] != (Prho | Qm): st.bad("S3", f"{name}@{k} e={e} d={d}")
                        if not Ed.key(V) < Ed.key(vt[h]): st.bad("S4", f"{name}@{k} e={e} d={d}")
                        if not Ed.key(vt[d]) <= Ed.key(V): st.bad("S5", f"{name}@{k} e={e} d={d}")
                    elif h1 and h2 and not h3:
                        st.inc("CTL_noH3_checks")
                        if inI: st.inc("CTL_noH3")
                    elif h1 and h3 and not h2:
                        st.inc("CTL_noH2_checks")
                        if inI: st.inc("CTL_noH2")
                    elif h2 and h3 and not h1:
                        st.inc("CTL_noH1_checks")
                        if inI: st.inc("CTL_noH1")
                if nxt is not None and ps:
                    if anyhyp:
                        st.inc("CORB_checks")
                        if nxt[e] == d: st.bad("CORB", f"{name}@{k} e={e} d={d}")
                    elif nxt[e] == d: st.inc("CTL_flip_nohyp")


def main():
    st = Stats(); a = sys.argv[1:]; rng = random.Random(3434)
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                s, t = R.starts(gp, r, rng); run_game(gp, s, t, st, f"{path}#{r}", rng)
    elif a[0] == "pairs":
        for line in [l.split() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(a[2], line[0]))
            if len(line) > 1:
                s, t = R.read_start(gp, os.path.join(a[2], line[1]))
                for v in range(gp.n):
                    x = s if gp.owner[v] == 0 else t
                    if x[v] not in gp.succ[v]: st.inc("INVALID_START_ENTRIES"); x[v] = gp.succ[v][0]
            else: s, t = R.starts(gp, 0, None)
            run_game(gp, s, t, st, line[0] + ("#" + os.path.basename(line[1]) if len(line) > 1 else "#S3"), rng)
    elif a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); k = int(a[5]) if len(a) > 5 else 2; ns = int(a[6]) if len(a) > 6 else 2
        rng = random.Random(seed)
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H
        for i in range(N):
            nn = rng.randint(nmin, nmax)
            gp = DC.rand_game(rng, nn, "kO") if k == 0 else H.rand_kO(rng, nn, k)
            for r in range(ns):
                s, t = R.starts(gp, r, rng); run_game(gp, s, t, st, f"random{seed}:{i}#{r}", rng)
    elif a[0] == "start":
        gp = pg.read(a[1])
        if len(a) > 2: s, t = R.read_start(gp, a[2]); nm = os.path.basename(a[1]) + "#start"
        else: s, t = R.starts(gp, 0, None); nm = os.path.basename(a[1]) + "#S3"
        run_game(gp, s, t, st, nm, rng)
    print("MODE", " ".join(a), "PCAP_LEN", PCAP_LEN, "PCAP", PCAP)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for v in st.viol[:40]: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
