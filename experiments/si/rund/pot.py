#!/usr/bin/env python3
"""L-SI box 17 (successor 13): DATA for the potential question (note §20). Per PHASE ((lambda_Xi, tau) constant; fallbacks included), per Odd
choice vertex q (|succ| >= 2), the sequence of changes of Xi(q) (rho_q events, RESULTS R61 (f)), each with:
  lev   top rank of P(Xi_t q) delta P(Xi_t+1 q) (-1: length only)
  cls   ALT class of the transition at q: SB (sigma-bar(q) unchanged; the change comes through b = sigma-bar(q)), CLEAN (strict), TIE,
        NONCLEAN, CYC (R61 (e) definitions, as experiments/new/box44/altcheck.py)
  ing   q in D (a gate) at t and t+1
Reports per phase and q: rho_q, distinct levels, max reuse of one level (REUSE), and whether levels between two uses of one level include a
higher one (RULER, R-RULER_V counts failures: Lemma RULER says 0). Also per phase: the four candidate potentials' strict moves at each
XI boundary (sum of gate Xi, sigma-bar kappa vector, Odd value multiset, W coarse vector) -- all monotone, so we report their moves only.
Usage: pot.py --one GAME [START] [-v] | --list FILE [KMIN] (env RS)"""
import sys, os, random
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import step, start_pair, Engine, dual, load, readstart
C = Counter(); VIOL = []; VERB = "-v" in sys.argv

def top(m): return m.bit_length() - 1 if m else -1

def oncycle(nxt, q):
    x, seen = nxt[q], set()
    while x not in seen and x != q: seen.add(x); x = nxt[x]
    return x == q

def avoids(nxt, y, q):
    x, seen = y, set()
    while x not in seen:
        if x == q: return False
        seen.add(x); x = nxt[x]
    return True

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        nxt = [s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)]
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), vs=vs, sb=list(sb), nxt=nxt, D={u for u in Q if sb[u] != t[u]}))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["key"] == rows[i]["key"]: j += 1
        if j > i: phase(g, E, name, rows, i, j, Q)
        i = j + 1

def phase(g, E, name, rows, i, j, Q):
    C["phases"] += 1; C["trans"] += j - i; C["max_phase"] = max(C["max_phase"], j - i)
    for q in Q:
        ev = []
        for k in range(i, j):
            A, B = rows[k], rows[k + 1]
            if tuple(A["vs"][q]) == tuple(B["vs"][q]):
                if A["sb"][q] != B["sb"][q]: C["sbar_change_no_xi_change"] += 1
                continue
            lev = top(A["vs"][q][1] ^ B["vs"][q][1])
            y1, y2 = A["sb"][q], B["sb"][q]
            if y1 == y2: cls = "SB"
            elif A["vs"][q][0] == q: cls = "CYC"
            elif oncycle(A["nxt"], q) or oncycle(B["nxt"], q) or not avoids(A["nxt"], y2, q): cls = "NONCLEAN"
            else: cls = "CLEAN" if E.key(B["vs"][q]) > E.key(A["vs"][q]) else "TIE"
            ing = q in A["D"] and q in B["D"]
            ev.append((k - i, lev, cls, ing)); C["rho"] += 1; C["rho_" + cls] += 1; C["rho_gate"] += ing
            if not E.key(B["vs"][q]) > E.key(A["vs"][q]): C["XI_DROP_V"] += 1; VIOL.append(("XI_DROP", name, k, q))
        if not ev: continue
        levs = [e[1] for e in ev if e[1] >= 0]; cnt = Counter(levs)
        kq = sum(1 for p in Q if rows[i]["vs"][p][0] == rows[i]["vs"][q][0])
        if kq >= 2:
            C["q_phase_multi"] += 1; C["max_rho_q_multi"] = max(C["max_rho_q_multi"], len(ev))
            C["q_reuse_multi"] += any(c > 1 for c in cnt.values())
            if any(c > 1 for c in cnt.values()) or len(ev) > g.n:
                print(f"  MULTI {name} phase@{i} q={q} class_odd_choices={kq} rho={len(ev)} n={g.n} levels={levs}")
            if len(ev) > g.n and any(c > 1 for c in cnt.values()): C["RULER_RHO_GT_N_MULTI"] += 1
        if os.environ.get("TRACE") == "1" and len(ev) >= 10:
            for (kk, lev, cls, ing) in ev:
                if lev < 0: continue
                A, B = rows[i + kk], rows[i + kk + 1]; y = B["sb"][q]; path, x, seen = [], y, set()
                while x not in seen: seen.add(x); path.append(x); x = B["nxt"][x]
                sw = [v for v in path if g.owner[v] == 0 and A["nxt"][v] != B["nxt"][v]]
                print(f"  TRACE q={q} t={kk} lev={lev} sbar {A['sb'][q]}->{y} new honest play {path[:12]}{'...' if len(path) > 12 else ''} Even switched on it: {sw}")
        C["max_rho_q"] = max(C["max_rho_q"], len(ev)); C["max_reuse"] = max(C["max_reuse"], max(cnt.values()) if cnt else 0)
        C["q_with_reuse"] += any(c > 1 for c in cnt.values()); C["q_phase"] += 1
        if len(ev) > g.n: C["RHO_GT_N"] += 1; print("RHO_GT_N", name, i, q, len(ev), g.n)
        for a in range(len(levs)):
            for b in range(a + 1, len(levs)):
                if levs[b] == levs[a]:
                    if not any(levs[c] > levs[a] for c in range(a + 1, b)): C["R_RULER_V"] += 1; VIOL.append(("RULER", name, i, q, levs))
                    break
        if VERB and len(ev) >= 3: print(f"  Q {name} phase@{i} len={j - i} q={q} rho={len(ev)} n={g.n} events={ev}")

def main():
    a = [x for x in sys.argv[1:] if x != "-v"]
    if a[0] == "--one":
        g = load(a[1]); check(g, a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        kmin = int(a[2]) if len(a) > 2 else 2
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin:
                continue
            check(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                check(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for v in VIOL[:8]: print("VIOLATION", v)
    print("POT PASS" if not VIOL else "POT FAIL")

if __name__ == "__main__":
    main()
