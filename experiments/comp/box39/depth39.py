#!/usr/bin/env python3
"""L-COMP box 39 item 1: loud-depth counter Q, Q_(>c), maxdepth and the loud-depth histogram on MY IDEAL-CYC engine (box37/ideal37.py:
build + Howard switch-best run, my tie rule), written from L-NEW box 206's TEXT (claude/l-new 134adb53, docs/new/N5-DEPTH-box206.md),
not from L-NEW's code. Definitions quoted (line numbers of that file):
  l. 7   «class_t(v) = (Λ_t(v), E_t(v)), E_t(v) the e-vertices of Π_t(v), sets of e-vertices compared lexicographically by their most
          relevant differing element»
  l. 12-14 «CHANGE DEPTH. At a step t with Λ_(t−1)(v) = Λ_t(v) and E_(t−1)(v) ≠ E_t(v), let z be the most relevant element of
          E_(t−1)(v) Δ E_t(v); depth := the number of elements of E_(t−1)(v) ∪ E_t(v) more relevant than z»
  l. 15-16 «LOUD DEPTH of a loud step t (some vertex changes class): −1 if some vertex changes Λ at t, else the least change depth over
          the vertices whose E changes at t.»
  l. 20  «Q the number of loud steps and Q_(>c) those of loud depth > c»
  l. 74  «Scope «all» = every vertex of Γ(G) (LOUD-SPLIT's quantity); «movers» = the movers only.»
Relevance of e-vertices = priority (all e-priorities are distinct and even; higher = more relevant).
ekey: if G has "ekey" (L-RED R230-elev §1: the same SET of e-priorities re-assigned in order of the per-option key ekey[x][k], ties by
(x, k)), it is applied; otherwise [E-LEV] order (lev, gate) as ideal37.build.
Must-0 counters (unit in brackets): elfall [(vertex, step)]: E falls (lex) at fixed Λ (R121 E-MON); ufail[c0] [(change, c0), c0 = 0,1,2]:
P^(c0) (the c0 + 1 most relevant elements of E) does not strictly rise at a change of depth <= c0, or changes at a change of depth > c0
(DEPTH-COUNT, box 206 §1). DEP_CTRL=1: relevance reversed in the depth bookkeeping (control: elfall/ufail must fire).
Output per genome (one IDEAL-CYC run from the start, scope all unless --movers): T, Q, Q>0, Q>1, Q>2, maxdepth, maxloud, hist.
Usage: depth39.py [--movers] G.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, "..", "box37"))
import ideal37
from n5b import SpecSI

CTRL = os.environ.get("DEP_CTRL") == "1"

def build(G):
    g, V, st = ideal37.build(G)
    if "ekey" in G:
        O = [k[1] for k in V if isinstance(k, tuple) and k[0] == "e"]
        ps = sorted(g.prio[V[("e", q)]] for q in O)
        for p, q in zip(ps, sorted(O, key=lambda q: (G["ekey"][q[0]][q[1]], q))): g.prio[V[("e", q)]] = p
    return g, V, st

def run(G, cap=20000):
    """= ideal37.run with the ekey-aware build (same Howard loop and tie rule)."""
    g, V, st = build(G); si = SpecSI(g); mv = [V[("x", x)] for x in range(G["N"])]; Hs = []
    while True:
        val, ch = si.evaluate_choice(list(st)); Hs.append((val, ch, list(st)))
        new = list(st); changed = False
        for x in mv:
            cur = st[x]; best = cur
            for y in g.succ[x]:
                c = si.nvo(val[y], val[best])
                if c > 0 or (c == 0 and best != cur and y > best): best = y
            if si.nvo(val[best], val[cur]) > 0: new[x] = best; changed = True
        if not changed or len(Hs) > cap: break
        st = new
    return g, V, Hs

def measure(G, movers=False, cap=20000):
    g, V, Hs = run(G, cap); T = len(Hs) - 1
    ev = [V[k] for k in V if isinstance(k, tuple) and k[0] == "e"]
    rel = {e: (-g.prio[e] if CTRL else g.prio[e]) for e in ev}; evs = set(ev)
    verts = [V[("x", x)] for x in range(G["N"])] if movers else range(len(g.prio))
    def E(t, v): return sorted(Hs[t][0][v][1] & evs, key=lambda e: -rel[e])        # most relevant first
    hist = {}; maxdepth = -1; elfall = 0; ufail = [0, 0, 0]
    for t in range(1, T + 1):
        lamch = False; dmin = None
        for v in verts:
            l0, l1 = Hs[t - 1][0][v][0], Hs[t][0][v][0]
            if l0 != l1: lamch = True; continue
            a, b = E(t - 1, v), E(t, v)
            if a == b: continue
            sa, sb = set(a), set(b); sym = sa ^ sb; z = max(sym, key=lambda e: rel[e])
            d = sum(1 for e in sa | sb if rel[e] > rel[z])
            if z not in sb: elfall += 1
            for c0 in range(3):
                pa, pb = a[:c0 + 1], b[:c0 + 1]
                if d <= c0:
                    s = set(pa) ^ set(pb)
                    if not s or max(s, key=lambda e: rel[e]) not in pb: ufail[c0] += 1
                elif pa != pb: ufail[c0] += 1
            maxdepth = max(maxdepth, d); dmin = d if dmin is None else min(dmin, d)
        if lamch: ld = -1
        elif dmin is not None: ld = dmin
        else: continue
        hist[ld] = hist.get(ld, 0) + 1
    Q = sum(hist.values()); qg = lambda c: sum(n for k, n in hist.items() if k > c)
    return dict(T=T, Q=Q, Q0=qg(0), Q1=qg(1), Q2=qg(2), maxdepth=maxdepth, maxloud=max(hist) if hist else None,
                hist={k: hist[k] for k in sorted(hist)}, elfall=elfall, ufail=ufail)

if __name__ == "__main__":
    a = sys.argv[1:]; mov = "--movers" in a; a = [f for f in a if f != "--movers"]
    for f in a:
        G = json.load(open(f)); r = measure(G, mov)
        print(os.path.basename(f), "N+M", G["N"] + sum(map(len, G["opts"])), "scope", "movers" if mov else "all",
              json.dumps(r), flush=True)
