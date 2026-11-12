#!/usr/bin/env python3
"""L-RED 66 R234: Theorem WINDOW (L-SI 51 box 100 §4) + Lemma LAM-GAP (box 101 §2, §3) on Gamma3 runs.
Engine: L-RED 65's own HOW3 (experiments/red/r232/how3_232.py; Gamma3 graph via r230/elev230 -> needs env LNEW). C = largest SCC of D(G);
t0 = max f(C') over SCCs C' != C reachable from C (box 99 §2). Windows after t0 in box 101 §3's sense: maximal runs a..b >= t0 with
sigma-bar constant on C's gates and Lambda_t(v) constant for every vertex v in SCOPE (all = every Gamma3 vertex; reach = the vertices
reachable from C's movers). A window's length = b' - a, b' = its first state at which no mover of C switches (later states of the window
repeat it: the one-player run has stopped); maxraw = max b - a. Counters (unit: window; scope: largest SCC, the one HOW3 run of the engine):
  must-0  lamgapfail (b - a > N_C + 1, box 101), sharpfail (b - a > N_C, L-RED 66 SHARP), replayfail (the one-player Howard run of
          G_C[sbar_a] restricted to reach(C), from sigma_a, with HOW3's tie rule, differs from the two-player states a..b+1 on C's
          movers, or its values differ from Omega_t on reach(C): WINDOW's «window = one-player run»)
  descriptive: #windows, max b - a, N_C; CTRL=1: replay with sbar_a flipped at one gate of C that is flipped somewhere in the run
          (must fire when such a gate exists).
Usage: w234.py G.json ..."""
import sys, os, json, functools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r232"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r221q"))
import how3_232 as H, own
CTRL = os.environ.get("CTRL") == "1"
def reach_vertices(gm, start):
    seen = set(start); st = list(start)
    while st:
        v = st.pop()
        for w in gm.succ[v]:
            if w not in seen: seen.add(w); st.append(w)
    return seen
def main():
    for fn in sys.argv[1:]:
        G = json.load(open(fn)); G = G.get("genome", G); G.pop("_evals", None)
        full = []; seq = H.how3(G, full=full); a_ = H.analyse(G, seq)
        cs, comp, succD = H.sccs(G); ci = max(range(len(cs)), key=lambda c: len(cs[c])); C = set(cs[ci])
        T = len(seq) - 1; f = [0] * len(cs)
        for t in range(1, T + 1):
            for x in range(G["N"]):
                if seq[t][x] != seq[t - 1][x]: f[comp[x]] = t
        rc = set(); st = [ci]
        while st:
            c = st.pop()
            for d in succD[c]:
                if d not in rc: rc.add(d); st.append(d)
        t0 = max((f[d] for d in rc), default=0)
        gm, sig0, tau0, V, O = H.build(G); n = gm.n; ow = list(gm.owner)
        Q = [(x, k) for x in sorted(C) for k in range(len(G["opts"][x]))]; gates = [V[("g", q)] for q in Q]
        R = reach_vertices(gm, [V[("m", (x, k))] for x in C for k in range(len(G["opts"][x]))] + sorted(C))
        flipped = [g for g in gates if len({full[t][1][g] for t in range(len(full))}) > 1]
        out = dict(N_C=len(C), M_C=len(Q), T3=T, t0=t0)
        for scope in ("all", "reach"):
            S = range(n) if scope == "all" else sorted(R)
            key_t = [(tuple(full[t][1][g] for g in gates), tuple(full[t][0][v][0] for v in S)) for t in range(len(full))]
            wins = []; a = t0
            for t in range(t0 + 1, len(full) + 1):
                if t == len(full) or key_t[t] != key_t[t - 1]: wins.append((a, t - 1)); a = t
            def eff(a, b):   # the one-player run stops at its first state without a switch of C (later window states repeat it)
                for t in range(a, b + 1):
                    if t + 1 >= len(seq) or all(seq[t + 1][x] == seq[t][x] for x in C): return t
                return b
            E = [(a, eff(a, b)) for a, b in wins]
            out[scope] = dict(windows=len(wins), maxraw=max(b - a for a, b in wins), maxlen=max(b - a for a, b in E),
                              lamgapfail=sum(1 for a, b in E if b - a > len(C) + 1), sharpfail=sum(1 for a, b in E if b - a > len(C)))
            if scope == "reach": W = wins
        vj = own.VJ(gm.prio); key = functools.cmp_to_key(vj.cmp); rf = 0; ctrl_hits = 0
        for a, b in W:
            succ = [list(s) for s in gm.succ]; tb = full[a][1]
            face = {g: tb[g] for g in gates}
            if CTRL and flipped:
                g = flipped[0]; face[g] = [w for w in gm.succ[g] if w != tb[g]][0]
            for g, w in face.items(): succ[g] = [w]
            sig = [None] * n
            st_sig = {}
            # rebuild sigma_a exactly as how3 does: frozen non-mover Even choices from sig0, movers from seq[a]
            for v in range(n):
                if ow[v] == 0: sig[v] = sig0[v] if v in sig0 else gm.succ[v][0]
            for x in range(G["N"]): sig[x] = V[("m", (x, seq[a][x]))]
            tbo = {v: (succ[v][0] if len(succ[v]) == 1 else tb[v]) for v in range(n) if ow[v] == 1}
            bad = False
            for t in range(a, b + 2):
                if t >= len(seq): break
                if any(sig[x] != V[("m", (x, seq[t][x]))] for x in C): bad = True; break
                vals, tbo = own.evaluate(n, ow, succ, vj, sig, tbo)
                if t <= b and any(vals[v] != full[t][0][v] for v in R): bad = True; break
                ns = list(sig)
                for x in C: ns[x] = max(gm.succ[x], key=lambda w: (key(vals[w]), w == sig[x], w))
                sig = ns
            rf += bad
        out["replayfail" if not CTRL else "ctrl_replay_mismatch"] = rf; out["flipped_gates"] = len(flipped)
        print(os.path.basename(fn), out, flush=True)
main()
