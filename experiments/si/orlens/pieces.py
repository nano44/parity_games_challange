#!/usr/bin/env python3
"""Lead 14:23Z checks on one-Odd-choice games (o = the Odd vertex with a choice).
(1) PIECES (P-N5-RE §5): maximal runs of transitions inside one joint lambda-phase with tau, theta = Xi(o), w = W(o) constant,
    (h) at every state, no S4c fallback, and R constant (R = vertices whose (sigma, tau)-play reaches o).
    For each piece: transitions, value-changing transitions, and whether it contains a PHASE-eliminating transition (some sigma-
    or tau-edge abandoned there and absent from every later state of the PHASE) and a PIECE-eliminating one (absent from every
    later state of the PIECE).
(2) CANCELLATIONS (L-LIT T30, ELIM-CANCEL): transition k -> k+1 at which some Even x switches to z', the play from o under
    (sigma_{k+1}, sbar_k) returns to o through the new edge (x, z') (a mixed cycle closed by the Even switch), and sbar(o) changes.
    HIT if the closing edge (x, z') is never re-adopted later in the phase after it is abandoned, or o's old exit sbar_k(o) is
    never used by sbar again in the phase.
(h): o lies on no cycle of the (sigma, sbar)-play or of the (sigma, tau)-play from o, and Xi(o), W(o) have the same cycle node."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT
from stretchret import playval
def play(g, sig, odd, v, cap):
    seen = []; x = v
    while x not in seen and len(seen) <= cap:
        seen.append(x); x = sig[x] if g.owner[x] == 0 else odd[x]
    return seen, x
def run(path, start=None, verbose=False):
    g, st = OT.load(path, start)
    E, Ed, states, fbf, _ = OT.run_states(g, st)
    n = g.n; o = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1][0]
    info = []
    for (sig, tau, vs, sbar, vt, tbar, Is, It) in states:
        wv = playval(E, sig, tau, o)
        p1, r1 = play(g, sig, sbar, o, n); p2, r2 = play(g, sig, tau, o, n)
        oncyc = (r1 == o) or (r2 == o)
        h = (not oncyc) and vs[o][0] == wv[0]
        R = frozenset(v for v in range(n) if o in play(g, sig, tau, v, n)[0])
        info.append(dict(theta=vs[o], w=wv, h=h, R=R))
    out = dict(pieces=0, piece_noPhaseElim=0, piece_noPieceElim=0, maxpiece=0, cancels=0, hits=0, hit_edge=0, hit_exit=0, examples=[])
    for ph in OT.phases(E, Ed, states):
        S = [states[k][0] for k in ph]; T = [states[k][1] for k in ph]; SB = [states[k][3] for k in ph]
        def edges(i): return {(x, S[i][x] if g.owner[x] == 0 else T[i][x]) for x in range(n)}
        def abandoned(i): return {(x, S[i][x] if g.owner[x] == 0 else T[i][x]) for x in range(n)} - edges(i + 1)
        L = len(ph)
        later = [set() for _ in range(L + 1)]
        for i in range(L - 1, -1, -1): later[i] = later[i + 1] | edges(i)
        # pieces
        i = 0
        while i < L - 1:
            def ok(j):
                a, b = info[ph[j]], info[ph[j + 1]]
                return (a["h"] and b["h"] and not fbf[ph[j]] and T[j] == T[j + 1] and a["theta"] == b["theta"] and a["w"] == b["w"]
                        and a["R"] == b["R"])
            if not ok(i): i += 1; continue
            j = i
            while j < L - 1 and ok(j): j += 1
            trans = list(range(i, j))
            vc = sum(1 for t in trans if states[ph[t]][2] != states[ph[t + 1]][2])
            pe = any(abandoned(t) - later[t + 1] for t in trans)
            within = [set() for _ in range(j + 2)]
            for t in range(j, i - 1, -1): within[t] = within[t + 1] | edges(t)
            pce = any(abandoned(t) - within[t + 1] for t in trans)
            out["pieces"] += 1; out["maxpiece"] = max(out["maxpiece"], len(trans))
            if vc and not pe:
                out["piece_noPhaseElim"] += 1
                if len(out["examples"]) < 3: out["examples"].append(("piece", ph[i], ph[j], vc, pce))
            if vc and not pce: out["piece_noPieceElim"] += 1
            i = j
        # cancellations
        for t in range(L - 1):
            if SB[t][o] == SB[t + 1][o]: continue
            for x in range(n):
                if g.owner[x] != 0 or S[t][x] == S[t + 1][x]: continue
                seq, end = play(g, S[t + 1], SB[t], o, n)
                if end != o: continue
                if x not in seq: continue
                out["cancels"] += 1
                e = (x, S[t + 1][x])
                # edge retired: after first abandonment past t+1, never re-adopted
                used = [e in edges(u) for u in range(t + 1, L)]
                first_off = next((u for u, b in enumerate(used) if not b), None)
                edge_ok = first_off is None or not any(used[first_off:])
                exit_ok = all(SB[u][o] != SB[t][o] for u in range(t + 1, L))
                out["hit_edge"] += edge_ok; out["hit_exit"] += exit_ok; out["hits"] += (edge_ok or exit_ok)
                if not (edge_ok or exit_ok) and len(out["examples"]) < 6: out["examples"].append(("cancel-miss", ph[t], x, e, SB[t][o], SB[t + 1][o]))
    return n, o, out
if __name__ == "__main__":
    for spec in sys.argv[1:]:
        p, _, s = spec.partition(":")
        n, o, out = run(p, s or None)
        print(f"{os.path.basename(p):22s} n={n:3d} o={o} {out}", flush=True)
