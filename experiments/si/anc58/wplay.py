"""L-SI box 58 §8: the W-REOPEN failures in detail (W-plays, Xi-plays, switches of x)."""
import sys, io, contextlib, os
ANC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "anc.py")
argv = sys.argv[1:]; sys.argv = [ANC] + argv
g = {'__file__': ANC, '__name__': 'x'}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(open(ANC).read(), ANC, 'exec'), g)
ROOT, runs, B, S, TAU, Wv, E, n, own, runof = g['ROOT'], g['runs'], g['B'], g['S'], g['TAU'], g['Wv'], g['E'], g['n'], g['own'], g['runof']
K = E.key
def wplay(k, tau, x):
    out, seen = [], set()
    while x not in seen: seen.add(x); out.append(x); x = S[k][x] if own[x] == 0 else tau[x]
    return out
esc = {}
for (u, z), r in ROOT.items():
    if r[0] == 'O' and r[2] is not None and u in runof: esc[(r[1], u)] = (r[2], r[3])
seqs = {}
for (s, u), og in sorted(esc.items(), key=lambda t: t[0][1]): seqs.setdefault((runof[u], s, B[u][s]), []).append((u, og))
for (ri, s, x), L in seqs.items():
    tau = TAU[runs[ri][0]]
    for (u1, (o1, c1)), (u2, (o2, c2)) in zip(L, L[1:]):
        x2s = {B[t + 1][s] for t in range(u1, u2)} - {x}
        if K(Wv(u2, tau)[x]) > K(Wv(u1, tau)[x]) or any(K(Wv(u2, tau)[y]) > K(Wv(u1, tau)[y]) for y in x2s): continue
        P = set(wplay(u1, tau, x)) | set(wplay(u2, tau, x)) | {q for y in x2s for q in wplay(u1, tau, y) + wplay(u2, tau, y)}
        rp = [q for q in P if K(Wv(u2, tau)[q]) > K(Wv(u1, tau)[q])]
        anyrise = [q for q in range(n) if K(Wv(u2, tau)[q]) > K(Wv(u1, tau)[q])]
        print("CASE s", s, "x", x, "x2s", sorted(x2s), "u", u1, u2, "og", o1, o2, "tau(s)", tau[s], "Wrise on plays", sorted(rp)[:8], "Wrise anywhere", len(anyrise),
              "sigma changed", sum(S[u1][v] != S[u2][v] for v in range(n) if own[v] == 0), "Zcl", c1, c2)
def xplay(k, x):
    out, seen = [], set()
    while x not in seen: seen.add(x); out.append(x); x = S[k][x] if own[x] == 0 else B[k][x]
    return out
print("XIPLAY-TEST")
for (ri, s, x), L in seqs.items():
    tau = TAU[runs[ri][0]]
    for (u1, (o1, c1)), (u2, (o2, c2)) in zip(L, L[1:]):
        x2s = {B[t + 1][s] for t in range(u1, u2)} - {x}
        if K(Wv(u2, tau)[x]) > K(Wv(u1, tau)[x]) or any(K(Wv(u2, tau)[y]) > K(Wv(u1, tau)[y]) for y in x2s): continue
        P = {q for t in range(u1, u2 + 1) for y in {x} | x2s for q in xplay(t, y)}
        rp = sorted(q for q in P if K(Wv(u2, tau)[q]) > K(Wv(u1, tau)[q]))
        print("  s", s, "x", x, "Xi-play vertices", len(P), "W-rise among them", rp[:10], "sigma(x) at u1..u2", [S[t][x] if own[x] == 0 else B[t][x] for t in range(u1, u2 + 1)])
print("TIE-TEST")
for (ri, s, x), L in seqs.items():
    tau = TAU[runs[ri][0]]
    for (u1, (o1, c1)), (u2, (o2, c2)) in zip(L, L[1:]):
        x2s = {B[t + 1][s] for t in range(u1, u2)} - {x}
        if K(Wv(u2, tau)[x]) > K(Wv(u1, tau)[x]) or any(K(Wv(u2, tau)[y]) > K(Wv(u1, tau)[y]) for y in x2s): continue
        for t in range(u1 - 1, u2 + 1):
            if own[x] == 0 and S[t][x] != S[t + 1][x]:
                a, b = S[t][x], S[t + 1][x]; W = Wv(t, tau)
                print("  x", x, "switch at", t, a, "->", b, "W(old) == W(new) at t:", W[a] == W[b], "W(x) changes at t:", Wv(t, tau)[x] != Wv(t + 1, tau)[x])
