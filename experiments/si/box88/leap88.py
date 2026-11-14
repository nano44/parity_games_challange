#!/usr/bin/env python3
"""L-SI box 88: leap87's census (docs/si/box87-leapfrog.md §4) as a module, with the nesting counters of box 88.
Unit = (mover x, SET option S, maximal interval I with every cycle node constant and Lambda(x) in {K1, K2}); events = steps t -> t+1
inside I where [sigma(x) = S] changes (leap87's convention, byte-identical counts on the real bits). Per unit:
  ev, EU = #e-vertices at least as relevant as e_S, k = #type-II events,
  depth = #distinct heads min(H) over the type-II events (L-RED R225-leap §2 «maxdepth», claude/l-red 029e5d8b), H = {v in a_t & b_t
          more relevant than z_t},
  excess = ev - EU (L-RED's maxexcess), ascfail (Claim C), boundfail (ev > EU + 2k + 1, as leap87).
Options: real bits (names file, B<digit>, option SET) by default; ALL=1 in the environment: every option whose Xi-target is its own mover.
Usage: leap88.py BOX81DIR GENOME.json ...  (VERB=1 prints every unit)"""
import sys, os, json
def setup(B81):
    sys.path[:0] = [B81, os.path.join(B81, "ref", "experiments", "new", "box191"), os.path.join(B81, "ref", "experiments", "new", "box189")]
def face(G, h, V, ev, rank, r0, eS, x, S, lam, cur, sb, lm, K):
    """(a, b) of box 87 §1 at one state, as descending rank lists (lex order = Python list order)."""
    nxt = lambda v: cur[v] if h.owner[v] == 0 else sb[v]
    def eset(v):
        seen = set(); out = set()
        while v not in seen:
            seen.add(v)
            if v in ev and rank(v) >= r0: out.add(v)
            v = nxt(v)
        return out
    a = K({eS} | eset(h.succ[eS][0]), rank); b = None
    for k2 in range(len(G["opts"][x])):
        if k2 == S: continue
        g = V[("g", (x, k2))]
        if lm[g] != lam: continue
        c = K(eset(g), rank)
        if b is None or c > b: b = c
    return a, b
def census(G, nm=None, allset=False, cap=3000):
    import idealcyc, gamma3
    K = lambda X, rank: sorted((rank(v) for v in X), reverse=True)
    N = G["N"]; h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G, cap=cap); _, _, _, V = gamma3.build(G, set())
    ev = {V[("e", (x, k))] for x in range(N) for k in range(len(G["opts"][x]))}; rank = lambda v: (h.prio[v], v)
    K12 = {V[("K", 1)], V[("K", 2)]}
    if allset or nm is None:
        bits = [(x, k) for x in range(N) for k in range(len(G["opts"][x])) if G["opts"][x][k][1] == x]
    else:
        bits = [(x, nm["opts"][x].index("SET")) for _, x in sorted((int(n[1:]), j) for j, n in enumerate(nm["movers"]) if n[0] == "B" and n[1:].isdigit())]
    rows = []
    for s in st:
        cur = list(s0)
        for x in range(N): cur[movers[x]] = V[("g", (x, s[x]))]
        vs, sb = E.evaluate(tuple(cur)); rows.append((s, cur, sb, tuple(vs[v][0] for v in range(h.n))))
    units = []; t0 = 0
    for t in range(1, len(rows) + 1):
        if t < len(rows) and rows[t][3] == rows[t - 1][3]: continue
        seg = range(t0, t); t0s = t0; t0 = t
        for x, S in bits:
            lam = rows[t0s][3][movers[x]]
            if lam not in K12: continue
            eS = V[("e", (x, S))]; r0 = rank(eS); EU = sum(1 for v in ev if rank(v) >= r0)
            nev = k = af = f2 = 0; heads = set(); evs = []; ab = []
            for u in seg:
                if u + 1 >= t: break
                s, cur, sb, lm = rows[u]
                ab.append(face(G, h, V, ev, rank, r0, eS, x, S, lam, cur, sb, lm, K))
                if (s[x] == S) == (rows[u + 1][0][x] == S): continue
                nxt = lambda v: cur[v] if h.owner[v] == 0 else sb[v]
                def seq(v):
                    seen = set(); out = []
                    while v not in seen: seen.add(v); out += [v] if v in ev else []; v = nxt(v)
                    return out
                sw = [eS] + seq(h.succ[eS][0]); A = {v for v in sw if rank(v) >= r0}
                best = None
                for k2 in range(len(G["opts"][x])):
                    if k2 == S: continue
                    g = V[("g", (x, k2))]
                    if lm[g] != lam: continue
                    sg = seq(g); Bs = {v for v in sg if rank(v) >= r0}
                    if best is None or K(Bs, rank) > K(best[1], rank): best = (sg, Bs)
                if best is None: continue
                sg, Bs = best; d = A ^ Bs
                if not d: f2 += 1; continue      # a_t = b_t at an event: F2 fails (PRIV / NODE not met); not counted as an event
                nev += 1; z = max(d, key=rank); Hd = [v for v in A & Bs if rank(v) > rank(z)]
                on = rows[u + 1][0][x] == S
                if Hd:
                    k += 1; heads.add(min(Hd, key=rank)); pl = sw if z in A else sg; i = pl.index(z)
                    af += not any(rank(v) > rank(z) for v in pl[i + 1:])
                evs.append((u, "ON" if on else "OFF", "II" if Hd else "I", rank(z), len(Hd)))
            da = sum(ab[i][0] != ab[i - 1][0] for i in range(1, len(ab))); db = sum(ab[i][1] != ab[i - 1][1] for i in range(1, len(ab)))
            mono = sum(ab[i][0] < ab[i - 1][0] or (ab[i][1] is not None and ab[i - 1][1] is not None and ab[i][1] < ab[i - 1][1]) for i in range(1, len(ab)))
            if nev:
                units.append({"f2fail": f2, "da": da, "db": db, "chargefail": int(nev > 1 + da + db), "monofail": mono, "x": x, "S": S, "I": (t0s, t), "ev": nev, "EU": EU, "k": k, "depth": len(heads), "excess": nev - EU,
                              "ascfail": af, "boundfail": int(nev > EU + 2 * k + 1), "events": evs})
    return units, len(st) - 1
def summary(units):
    return {"units": len(units), "typeI": sum(u["ev"] - u["k"] for u in units), "typeII": sum(u["k"] for u in units),
            "maxk": max([u["k"] for u in units], default=0), "maxdepth": max([u["depth"] for u in units], default=0),
            "maxexcess": max([u["excess"] for u in units], default=None), "maxev": max([u["ev"] for u in units], default=0),
            "ascfail": sum(u["ascfail"] for u in units), "boundfail": sum(u["boundfail"] for u in units),
            "chargefail": sum(u["chargefail"] for u in units), "monofail": sum(u["monofail"] for u in units),
            "maxratio": max([round(u["ev"] / (1 + u["da"] + u["db"]), 3) for u in units], default=0)}
if __name__ == "__main__":
    setup(sys.argv[1]); allset = os.environ.get("ALL") == "1"
    for f in sys.argv[2:]:
        G = json.load(open(f)); nf = f[:-5] + ".names.json"; nm = json.load(open(nf)) if os.path.exists(nf) else None
        U, T = census(G, nm, allset); s = summary(U)
        f2 = sum(u["f2fail"] for u in U)        # events with a_t = b_t (F2's hypotheses not met); printed only when nonzero
        print(os.path.basename(f), "T", T, " ".join(f"{a} {b}" for a, b in s.items()) + (f" f2fail {f2}" if f2 else ""))
        if os.environ.get("VERB") == "1":
            for u in U: print("  ", {a: b for a, b in u.items() if a != "events"}, u["events"])
