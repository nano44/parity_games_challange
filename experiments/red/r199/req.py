#!/usr/bin/env python3
"""L-RED R199 REQ: the C-ELEMENT form of a degree-2 IDEAL step on a ladder, and Xi-synthesis for a PRESCRIBED state sequence.
C-ELEMENT (PROVED below, lane): at degree 2, let KP_t(x) be the key-preferred option of x under the keys of s_t and C_s(x) the
strictly Xi-better option of x at s (faces of distinct beta-sets never tie). Then s_t(x) = KP_t(x) if KP_t(x) = C_(t-1)(x), else
s_(t-1)(x). (Proof: A_(t-1)(x) = {s_(t-1)(x)} or both options; x takes the key-least available; it changes iff both are available
(C_(t-1)(x) != s_(t-1)(x)) and KP_t(x) != s_(t-1)(x); in both remaining cases s_t(x) = s_(t-1)(x).)
So a prescribed run s_0..s_L is an IDEAL run iff (i) every move goes to KP_t (W side: gates), (ii) C_(t-1)(x) = s_t(x) at every
move, (iii) C_(t-1)(x) = s_(t-1)(x) at every non-move with KP_t(x) != s_(t-1)(x) (Xi side). This file: derive (i)-(iii) from a
target (genome or schedule spec + gates), and solve the Xi side with z3 (states fixed; free Xi-targets (acyclic), REL weights or
exact +-2^rank). Usage: req.py target.json out.json   (target: {"movers": [[lev, [W0, W1]], ...], "states": [[...], ...],
"gate": [[g0, g1], ...]} or a genome; env REL=1, FIXXT=1 (keep the target's Xi-targets), TMO=seconds)"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
def keys(lev, WT, gate, s):
    N = len(lev); key = [None] * N
    for v in sorted(range(N), key=lambda v: lev[v]):
        w = WT[v][s[v]]; key[v] = (gate[v][s[v]],) if w < 0 else key[w] + (gate[v][s[v]],)
    return key
def kp(lev, WT, gate, key, v):
    a, b = WT[v]
    ka = (gate[v][0],) if a < 0 else key[a] + (gate[v][0],); kb = (gate[v][1],) if b < 0 else key[b] + (gate[v][1],)
    return 0 if ka < kb else 1
def requirements(lev, WT, gate, S):
    """returns (W-side violations, Xi requirements {(s, x): bit})"""
    N = len(lev); bad = []; req = {}
    for t in range(1, len(S)):
        key = keys(lev, WT, gate, S[t])
        for x in range(N):
            k = kp(lev, WT, gate, key, x); old, new = S[t - 1][x], S[t][x]
            if new != old:
                if k != new: bad.append((t, x))
                req[(t - 1, x)] = new
            elif k != old: req[(t - 1, x)] = old
    return bad, req
def solve(lev, WT, S, req, xtfix=None, rel=True, tmo=None):
    import z3
    N = len(lev); faces = [(v, k) for v in range(N) for k in (0, 1)]; M = len(faces); Z = z3.Solver()
    if tmo: Z.set("timeout", tmo * 1000)
    xt = {f: z3.Int(f"x{f}") for f in faces}; pos = [z3.Int(f"p{v}") for v in range(N)]
    for f in faces:
        Z.add(xt[f] >= -1, xt[f] < N, xt[f] != f[0])
        for u in range(N): Z.add(z3.Implies(xt[f] == u, pos[u] > pos[f[0]]))
        if xtfix is not None: Z.add(xt[f] == xtfix[f])
    if rel:
        Wt = {f: z3.Int(f"w{f}") for f in faces}; Z.add(z3.Distinct(*Wt.values()), *[Wt[f] != 0 for f in faces])
    else:
        rank = {f: z3.Int(f"r{f}") for f in faces}; par = {f: z3.Bool(f"q{f}") for f in faces}
        Z.add(z3.Distinct(*rank.values()), *[z3.And(rank[f] >= 0, rank[f] < M) for f in faces])
        Wt = {f: z3.If(par[f], -1, 1) * z3.Sum([z3.If(rank[f] == r, 2 ** r, 0) for r in range(M)]) for f in faces}
    need = sorted({s for (s, x) in req})
    for s in need:
        X = [z3.Int(f"X{s}_{u}") for u in range(N)]
        def Fv(v, k): return Wt[(v, k)] + z3.Sum([z3.If(xt[(v, k)] == u, X[u], 0) for u in range(N)])
        for u in range(N): Z.add(X[u] == Fv(u, S[s][u]))
        for x in range(N):
            if (s, x) in req: Z.add((Fv(x, 1) > Fv(x, 0)) == (req[(s, x)] == 1))
    r = Z.check()
    if r != z3.sat: return str(r), None
    m = Z.model(); ev = lambda e: m.eval(e, model_completion=True).as_long() if not z3.is_bool(e) else z3.is_true(m.eval(e, model_completion=True))
    out = dict(xt={f: ev(xt[f]) for f in faces}, pos=[ev(p) for p in pos])
    if not rel: out.update(rank={f: ev(rank[f]) for f in faces}, par={f: ev(par[f]) for f in faces})
    else: out.update(w={f: ev(Wt[f]) for f in faces})
    return "sat", out
def genome(lev, WT, gate, start, sol):
    N = len(lev); faces = [(v, k) for v in range(N) for k in (0, 1)]
    order = sorted(range(N), key=lambda v: sol["pos"][v])
    return dict(N=N, lev=lev, deg=2, opts=[[[WT[v][k], sol["xt"][(v, k)], 2 * v + k] for k in (0, 1)] for v in range(N)],
                gate=[list(g) for g in gate], br=[sol["rank"][f] for f in faces], bp=[1 if sol["par"][f] else 0 for f in faces],
                start=list(start), xorder=order)
if __name__ == "__main__":
    import ideal, time
    T = json.load(open(sys.argv[1])); out = sys.argv[2]
    if "opts" in T:   # a genome: its own run is the target
        lev = T["lev"]; WT = [[o[0] for o in T["opts"][v]] for v in range(T["N"])]; gate = T["gate"]; S, why = ideal.traj(T)
        xtf = {(v, k): T["opts"][v][k][1] for v in range(T["N"]) for k in (0, 1)}
    else:
        lev = [m[0] for m in T["movers"]]; WT = [m[1] for m in T["movers"]]; gate = T["gate"]; S = [tuple(s) for s in T["states"]]; xtf = None
    bad, req = requirements(lev, WT, gate, S)
    print("REQ L", len(S) - 1, "W-side violations", bad, "Xi requirements", len(req), flush=True)
    if bad: sys.exit(1)
    t0 = time.time(); r, sol = solve(lev, WT, S, req, xtfix=xtf if os.environ.get("FIXXT") == "1" else None, rel=os.environ.get("REL") == "1",
                                     tmo=int(os.environ["TMO"]) if os.environ.get("TMO") else None)
    print("XI-SOLVE", r, f"{time.time() - t0:.1f} s", flush=True)
    if r == "sat" and "rank" in sol:
        G = genome(lev, WT, gate, S[0], sol); json.dump(G, open(out, "w")); S2, why = ideal.traj(G)
        print("replay L", len(S2) - 1, why, "prefix matches target:", list(S2[:len(S)]) == list(S), out)
    elif r == "sat": json.dump({f"{v},{k}": sol["xt"][(v, k)] for (v, k) in sol["xt"]}, open(out, "w")); print("REL xt written", out)
