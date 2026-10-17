"""REFEREE packet 7 probe (Opus 5.5, D12), independent of dtl_rootmono.py. Subclasses experiments/alg/dtl_pyref.DTL.
best_vertices is re-implemented from dtl.cpp 644-776 (same as dtl_pyref) with recording:
 - per round r: V_r, and for every top tau in V_r (decreasing index): the prefix P(tau+) (processed or not), region Z_tau;
 - the alive tangle set T at the call.
Checks:
 (A) EXACT: for every processed tau, P(tau+) | Z_tau == Cl_{pr tau}(P(tau+) | {tau}; T \\ E_tau) (my own closure below);
     also counts steps where the plain closure over all of T differs (step deficits).
 (B) consecutive visits of each context R (same player, same G): RV per vertex; Pi-non-rise detection is via RV fall
     (pointwise) only; new steal at aligned round r and tau processed in the earlier run: E'_tau & T  not subset of E_tau.
     Reports (fall, new steal) incidence, and per falling vertex the round/tau of new steals.
Usage: p7probe.py [oink|stable] G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "..", "..")
for d_ in ("experiments/alg", "experiments/harness", "experiments/dtl-bench"): sys.path.insert(0, os.path.join(ROOT, d_))
import pg, dtl_pyref as P
INF = 10 ** 9

def cl(d, p, base, R, q, tl):
    S = set(base); ch = True
    while ch:
        ch = False
        for u in R:
            if u in S or d.pr[u] > q: continue
            sc = d.outs[u]
            if d.ow[u] == p: ok = any(w in S for w in sc)
            else: ok = any(w in S for w in sc) and all(w in S for w in sc if w in R)
            if ok: S.add(u); ch = True
        for t in tl:
            vs = [v for v, _ in d.tv[t]]
            if any(v not in S and v not in R for v in vs): continue
            new = [v for v in vs if v not in S]
            if not new or any(d.pr[v] > q for v in new): continue
            esc = d.tout[t]
            if any(w not in S and w in R for w in esc) or not any(w in S for w in esc): continue
            S.update(new); ch = True
    return S

def alive(d, t, p):
    return d.tpr[t] != -1 and d.tpr[t] % 2 == p and all(w in d.G for w, _ in d.tv[t])

class Probe(P.DTL):
    def __init__(s, *a, **k):
        super().__init__(*a, **k); s.searches = []; s.cur = None; s.stats = dict(s.stats, exact_fail=0, steps=0, deficit_steps=0)
    def search(s, p):
        s.cur = dict(p=p, G=frozenset(s.G), visits=[]); s.searches.append(s.cur)
        return super().search(p)
    def best_vertices(s, V, R, p):
        tl = [t for t in range(len(s.tv)) if alive(s, t, p)]
        rec = dict(R=frozenset(R), T=frozenset(tl), rounds=[], rv={}); s.cur["visits"].append(rec)
        V.clear(); V.update(v for v in R if s.pr[v] % 2 == p)
        allV = set(V)
        def fin(res):
            for v in allV: rec["rv"].setdefault(v, INF)
            return res
        if not V: return fin(0)
        rnd = 0
        while True:
            rnd += 1; prevV = set(V); Z = set(); CurR = set(R); pre = {}; reg = {}
            for top in range(s.n - 1, -1, -1):
                if top not in V: continue
                pre[top] = frozenset(Z)
                if top in Z: continue
                CurZ = {top}; s.Q = [top]
                s.tattr(p, CurZ, CurR, CurR, s.pr[top], CurR)
                reg[top] = frozenset(CurZ)
                # (A) EXACT
                E = {t for t in tl if any(v in Z for v, _ in s.tv[t]) and not all(v in Z for v, _ in s.tv[t])}
                c = cl(s, p, Z | {top}, R, s.pr[top], [t for t in tl if t not in E])
                s.stats["steps"] += 1
                if c != Z | CurZ: s.stats["exact_fail"] += 1; print("EXACT FAIL", rnd, top)
                if cl(s, p, Z | {top}, R, s.pr[top], tl) != Z | CurZ: s.stats["deficit_steps"] += 1
                Z |= CurZ
            rec["rounds"].append(dict(V=frozenset(V), pre=pre, reg=reg))
            cand = [v for v in sorted(V, reverse=True) if not s.attracts(p, v, Z, R)]
            if not cand: return fin(1)
            for t in [0] + [q for q in s.prios if q > 0 and q <= s.maxpr]:
                s.Q = sorted(Z); s.tattr(p, Z, R, R, t, None)
                keep = []
                for i, u in enumerate(cand):
                    if s.pr[u] <= t: keep += cand[i:]; break
                    if not s.attracts(p, u, Z, R): keep.append(u)
                cand = keep
            for u in cand: rec["rv"][u] = rnd
            V -= set(cand)
            if not cand: return fin(1)
            if not V:
                V.clear(); V.update(prevV); return fin(-1)

def E(d, T, prefix):
    return {t for t in T if any(v in prefix for v, _ in d.tv[t]) and not all(v in prefix for v, _ in d.tv[t])}

def newsteals(d, a, b):
    out = []
    for r in range(min(len(a["rounds"]), len(b["rounds"]))):
        ra, rb = a["rounds"][r], b["rounds"][r]
        for tau in ra["reg"]:
            pa = ra["pre"][tau]
            pb = rb["pre"].get(tau)
            if pb is None:   # tau not in V'_r: prefix of run 2 before tau = union of regions of tops > tau
                pb = frozenset().union(*[z for t2, z in rb["reg"].items() if t2 > tau])
            ns = (E(d, a["T"], pb) & a["T"]) - E(d, a["T"], pa)
            if ns: out.append((r + 1, tau, sorted(ns)))
    return out

def check(path, order, tot, watch=None):
    g = pg.read(path)
    old = P.DTL; P.DTL = Probe
    try: _, _, d = P.solve_game(g, order=order)
    finally: P.DTL = old
    for k in ("exact_fail", "steps", "deficit_steps"): tot[k] += d.stats[k]
    i, ss = 0, d.searches
    while i < len(ss):
        j = i
        while j + 1 < len(ss) and ss[j + 1]["p"] == ss[i]["p"] and ss[j + 1]["G"] == ss[i]["G"]: j += 1
        last = {}
        for si in range(i, j + 1):
            for vis in ss[si]["visits"]:
                key = vis["R"]
                if key in last:
                    a = last[key]
                    falls = sorted(v for v in vis["rv"] if vis["rv"][v] < a["rv"].get(v, INF))
                    ns = newsteals(d, a, vis)
                    tot["pairs"] += 1; tot[("fall" if falls else "nofall") + "_" + ("ns" if ns else "nons")] += 1
                    if watch and falls and len(key) == len(ss[si]["G"]):
                        print(f"  root fall s{a['s']}->s{si}: falls {[(v, d.pr[v], a['rv'][v], vis['rv'][v]) for v in falls]}; new steals (round, tau, tangles) {ns}")
                vis["s"] = si; last[key] = vis
        i = j + 1

if __name__ == "__main__":
    from collections import Counter
    order = sys.argv[1]; tot = Counter(); watch = os.environ.get("P7_WATCH")
    for f in sys.argv[2:]:
        try: check(f, order, tot, watch)
        except Exception as ex: print("ERR", f, repr(ex)); tot["err"] += 1
    print(order, dict(tot))
