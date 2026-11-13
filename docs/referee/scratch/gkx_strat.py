#!/usr/bin/env python3
"""REFEREE successor 36: own verification of N5's positional strategies at its stop on Gamma3(G_k) (TARGET.md section 5, D2
change 5: «every implementation also outputs positional strategies»), for the dead-end record of P-N5-EXP (fixes entry 1, 9.9).

Engine: this lane's rl_engine.py; game: gk_gamma3.build3 of gkx.rule(k). N5's output (SPEC S5): W := {v : the cycle node of
Xi_sigma(v) has even priority}; Even's strategy = sigma on W; Odd's strategy = sigma-bar (S1's counterstrategy) on V - W.
The verifier below is self-contained (no Zielonka, no lane code): a positional strategy rho of player P wins from every vertex
of a region R iff (closure) rho(v) is in R for P's vertices of R and every successor of the opponent's vertices of R is in R, and
(cycles) every cycle of the graph on R in which P's vertices keep only rho has a largest priority of P's parity. The cycle test:
for every priority p of the WRONG parity, no vertex of priority p lies on a cycle of the subgraph on {v in R : prio(v) <= p}.
Counters (must be 0): STRATE (violations for Even on W), STRATO (violations for Odd on V - W), REG (W differs from Zielonka's).
Controls (--ctl): allE = Even's test on the region V (must fire STRATE when Odd wins somewhere); allO = Odd's test on V (STRATO).
Usage: gkx_strat.py kmin kmax [--ctl NAME]"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gkx, gkx_n5
import rl_engine as eng
import gk_gamma3 as g3
import gk_reach as R


def on_cycle(nodes, out):
    """the set of vertices of `nodes` that lie on a cycle of the graph (out restricted to nodes); iterative Tarjan."""
    index, low, st, onst, res = {}, {}, [], set(), set()
    cnt = [0]
    for r in nodes:
        if r in index:
            continue
        stack = [(r, iter([w for w in out[r] if w in nodes]))]
        index[r] = low[r] = cnt[0]
        cnt[0] += 1
        st.append(r)
        onst.add(r)
        while stack:
            v, it = stack[-1]
            adv = False
            for w in it:
                if w not in index:
                    index[w] = low[w] = cnt[0]
                    cnt[0] += 1
                    st.append(w)
                    onst.add(w)
                    stack.append((w, iter([y for y in out[w] if y in nodes])))
                    adv = True
                    break
                elif w in onst:
                    low[v] = min(low[v], index[w])
            if adv:
                continue
            stack.pop()
            if stack:
                low[stack[-1][0]] = min(low[stack[-1][0]], low[v])
            if low[v] == index[v]:
                comp = []
                while True:
                    w = st.pop()
                    onst.discard(w)
                    comp.append(w)
                    if w == v:
                        break
                if len(comp) > 1 or v in out[v]:
                    res.update(comp)
    return res


def verify(prio, owner, succ, region, rho, player):
    """number of violations of «rho (player's positional strategy) wins from every vertex of region»."""
    bad = 0
    out = {}
    for v in region:
        if owner[v] == player:
            if rho[v] not in succ[v] or rho[v] not in region:
                bad += 1
                out[v] = []
            else:
                out[v] = [rho[v]]
        else:
            if any(w not in region for w in succ[v]):
                bad += 1
            out[v] = [w for w in succ[v] if w in region]
    for p in sorted(set(prio[v] for v in region)):
        if p % 2 == player:           # player 0 = Even wins on even priorities; a priority of the player's parity is harmless
            continue
        nodes = {v for v in region if prio[v] <= p}
        cyc = on_cycle(nodes, out)
        bad += sum(1 for v in cyc if prio[v] == p)
    return bad


def main():
    a = sys.argv[1:]
    ctl = ""
    if "--ctl" in a:
        i = a.index("--ctl")
        ctl = a[i + 1]
        del a[i:i + 2]
    for k in range(int(a[0]), int(a[1]) + 1):
        J, _ = gkx.rule(k)
        G = gkx_n5.to_dict(J)
        prio, owner, succ, names, idx = g3.build3(G)
        n = len(prio)
        g = eng.Game(prio, owner, succ)
        out = eng.run(g, maxit=10 ** 7)
        fin = out[-1]
        Xi = fin["Xi"]
        W = {v for v in range(n) if prio[Xi[v][0]] % 2 == 0}
        sig = fin["s"]
        sb = fin["sb"]
        RE = set(range(n)) if ctl == "allE" else W
        RO = set(range(n)) if ctl == "allO" else set(range(n)) - W
        se = verify(prio, owner, succ, RE, sig, 0)
        so = verify(prio, owner, succ, RO, sb, 1)
        WE = R.zielonka(prio, owner, succ)
        print(f"strat G_{k} ctl {ctl or 0} n {n} iterations {len(out) - 1} evenregion {len(W)} oddregion {n - len(W)} "
              f"oddvertices {' '.join(names[v] for v in sorted(set(range(n)) - W)[:4])} STRATE {se} STRATO {so} REG {len(W ^ WE)}", flush=True)


if __name__ == "__main__":
    main()
