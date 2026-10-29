#!/usr/bin/env python3
"""L-NEW box 64: cut each tau-stretch of plain N5 (box21/n5x.step, SPEC S3 start, --start for GAME.start) into RESULTS
R88's frozen W-phases (no S4c fallback; tau, sbar(sigma), lambda_Xi, lambda_W constant; W = val(sigma, tau) on G_tau) and
count, per tau-stretch: frozen phases, and the boundary causes (fb, sbar, lx, lw); per frozen phase: W-changing
transitions, W-flat transitions, R*_T (adoptions of an edge blocked at an earlier state of the phase: W-better than sigma's
choice but not in I_sigma). Checks R88 FW-R* (W-changing <= (n-1)(R*+1)) as a control.
With --wrun the cuts are only fallbacks and lambda_W-changes (W-runs; box 64 §1.8 Lemma GP*-RUN), sbar / lambda_Xi
changes are not cuts. Usage: frozen.py GAME.pg [--start] [--wrun]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg

def main():
    p = sys.argv[1]; g = load(p); n = g.n
    global WRUN; WRUN = "--wrun" in sys.argv
    start = readstart(p[:-3] + ".start") if "--start" in sys.argv and os.path.exists(p[:-3] + ".start") else None
    E, Ed = Engine(g), Engine(dual(g))
    s, t = start_pair(g, E, Ed, start); s, t = tuple(s), tuple(t)
    Wc = {}
    def W(s, t):
        if t not in Wc:
            Wc[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
        return Wc[t].evaluate(s)[0], Wc[t]
    def info(s, t):
        vx, sb = E.evaluate(s); Is = set(E.improving(s, vx)); w, Ew = W(s, t)
        blocked = {(v, x) for v in range(n) if g.owner[v] == 0 for x in g.succ[v]
                   if x != s[v] and Ew.key(w[x]) > Ew.key(w[s[v]]) and (v, x) not in Is}
        return dict(lx=tuple(vx[x][0] for x in range(n)), sb=tuple(sb), lw=tuple(w[x][0] for x in range(n)), w=w, bl=blocked)
    cur = info(s, t); T = 0
    stretches = []; st_ = dict(ph=1, sig=0, cause=dict(fb=0, sbar=0, lx=0, lw=0)); ph = dict(len=0, wch=0, flat=0, R=0, bl=set(cur["bl"]))
    worst_ph = dict(len=0, wch=0, flat=0, R=0); viol = 0; maxph_per_stretch = 0
    def close_ph():
        nonlocal viol
        if ph["wch"] > (n - 1) * (ph["R"] + 1): viol += 1
        for k in ("len", "wch", "flat", "R"): worst_ph[k] = max(worst_ph[k], ph[k])
    while True:
        r = step(g, E, Ed, list(s), list(t))
        if r is None: break
        ns, nt, Is, It, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt); T += 1
        if nt != t:
            close_ph(); stretches.append(st_)
            st_ = dict(ph=1, sig=0, cause=dict(fb=0, sbar=0, lx=0, lw=0))
            s, t = ns, nt; cur = info(s, t); ph = dict(len=0, wch=0, flat=0, R=0, bl=set(cur["bl"])); continue
        if ns == s: continue
        st_["sig"] += 1
        nxt = info(ns, t)
        causes = [c for c, ok in (("fb", fb), ("sbar", nxt["sb"] != cur["sb"]), ("lx", nxt["lx"] != cur["lx"]),
                                  ("lw", nxt["lw"] != cur["lw"])) if ok and (c in ("fb", "lw") or not WRUN)]
        if causes:
            close_ph(); st_["ph"] += 1
            for c in causes: st_["cause"][c] += 1
            ph = dict(len=0, wch=0, flat=0, R=0, bl=set(nxt["bl"]))
        else:
            ph["len"] += 1
            if nxt["w"] == cur["w"]: ph["flat"] += 1
            else: ph["wch"] += 1
            if any((v, ns[v]) in ph["bl"] for v in range(n) if g.owner[v] == 0 and ns[v] != s[v]): ph["R"] += 1
            ph["bl"] |= nxt["bl"]
        s, cur = ns, nxt
    close_ph(); stretches.append(st_)
    big = max(stretches, key=lambda x: x["sig"])
    print(f"{'WRUN' if WRUN else 'FROZEN'} {os.path.basename(p)} n {n} m {g.m} iters {T} tau-stretches {len(stretches)} max-stretch-sig {big['sig']} "
          f"its-phases {big['ph']} its-causes {big['cause']} max-phases-per-stretch {max(x['ph'] for x in stretches)} "
          f"worst-frozen-phase {worst_ph} FWR-viol {viol}")

main()
