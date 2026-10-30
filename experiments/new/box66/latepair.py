#!/usr/bin/env python3
"""L-NEW box 66: per-edge late adoptions of plain N5 (box21/n5x.step; SPEC S3 start, --start: GAME.start).
A PIECE: maximal run of states joined by non-fallback transitions with tau constant (W-frame tau fixed). In a piece, (v, c) is BLOCKED at
state t if W_t(c) > W_t(sigma_t v) and (v, c) not in I_sigma_t (R88), W = val(sigma, tau) on G_tau. A LATE adoption of (v, c) at
transition j -> j+1 of a piece: sigma_{j+1}(v) = c != sigma_j(v) and (v, c) was blocked at some state of the piece before j+1.
Reports max over (lambda_Xi-run, edge), (piece, edge), (W-run, edge) of the late adoptions, and checks Lemma LATE-W (box 66 §2): in a
W-run, between a leave of c by v (v off its own W-cycle after the leave) and the next late adoption of (v, c), W(c) strictly rises.
Usage: latepair.py GAME.pg [--start]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
from collections import Counter
p = sys.argv[1]; g = load(p); n = g.n
start = readstart(p[:-3] + ".start") if "--start" in sys.argv and os.path.exists(p[:-3] + ".start") else None
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); s, t = tuple(s), tuple(t)
Wc = {}
def W(s, t):
    if t not in Wc: Wc[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[t].evaluate(s)[0], Wc[t]
def info(s, t):
    vx, _ = E.evaluate(s); Is = set(E.improving(s, vx)); w, Ew = W(s, t)
    bl = {(v, x) for v in range(n) if g.owner[v] == 0 for x in g.succ[v] if x != s[v] and Ew.key(w[x]) > Ew.key(w[s[v]]) and (v, x) not in Is}
    return dict(lx=tuple(vx[x][0] for x in range(n)), w=w, Ew=Ew, bl=bl)
cur = info(s, t)
lam_c, piece_c, wrun_c = Counter(), Counter(), Counter()
blocked_piece = set(cur["bl"]); lastleave = {}      # (v, c) -> W(c) value right after v left c, inside the current W-run
lw_viol = lw_checked = 0; late_total = 0; lamid = pid = wid = 0
while True:
    r = step(g, E, Ed, list(s), list(t))
    if r is None: break
    ns, nt, _, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt)
    nxt = info(ns, nt)
    if nxt["lx"] != cur["lx"]: lamid += 1
    if fb or nt != t:                        # piece boundary (and W-run boundary)
        pid += 1; wid += 1; blocked_piece = set(nxt["bl"]); lastleave = {}
        s, t, cur = ns, nt, nxt; continue
    lwchange = any(nxt["w"][x][0] != cur["w"][x][0] for x in range(n))
    Ew = cur["Ew"]
    for v in range(n):
        if g.owner[v] != 0 or ns[v] == s[v]: continue
        c = ns[v]
        if (v, c) in blocked_piece:
            late_total += 1; lam_c[(lamid, v, c)] += 1; piece_c[(pid, v, c)] += 1; wrun_c[(wid, v, c)] += 1
            if (v, c) in lastleave:
                lw_checked += 1
                if not Ew.key(cur["w"][c]) > Ew.key(lastleave[(v, c)]): lw_viol += 1
        old = s[v]
        if nxt["w"][v][0] != v:              # v off its own W-cycle after the leave
            lastleave[(v, old)] = nxt["w"][old]
        else:
            lastleave.pop((v, old), None)
    if lwchange: wid += 1; lastleave = {}
    blocked_piece |= nxt["bl"]
    s, t, cur = ns, nt, nxt
mx = lambda C: max(C.values()) if C else 0
print(f"LATEPAIR {os.path.basename(p)} n {n} late {late_total} max-per-lambda-run-edge {mx(lam_c)} max-per-piece-edge {mx(piece_c)} "
      f"max-per-Wrun-edge {mx(wrun_c)} LATE-W checked {lw_checked} viol {lw_viol}")
