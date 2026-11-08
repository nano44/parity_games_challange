#!/usr/bin/env python3
"""L-RED 61 R227 item 1d: INDEPENDENT census for L-NEW 66 BOX 199 (claude/l-new cde01dcb) on R221 own.py (IDEAL-CYC Howard, my own Gamma:
gate g = (x, k) is an Odd vertex with faces e(g), b(g); no pads). No L-NEW code.
For (v, maximal Lambda-interval I) and each change t-1 -> t of E(v) (e-vertices of Pi(v)): split u := first vertex of the play at t whose
successor differs from the play at t-1; old / new successors. Checks (must be 0): kind (u not a mover / gate), trA (Lambda(u) != w at t-1 or t),
trD (E(v) delta != E(u) delta), hw (mover: not val_(t-1)(new) > val_(t-1)(old)), gt (gate: Odd's face at t not the smaller, or a tie).
For consecutive y-tops t1 < t2 of (v, I): re-win iff the split pair (u, new) is equal at t1 and t2 (b := new, a := u's successor at t2 - 1).
  dn (REWIN (a)): not val_(t2-1)(a) > val_t1(b);  rh (REWIN-HI): not E_t2(b) ∩ U_y >lex E_t1(b) ∩ U_y;
  rw (CONJECTURE RW-WT): E(wt(y)) ∩ U_y takes < 2 values on [t1, t2]  (wt(y) = the successor of the e-vertex y);
  wc (RW-WT asked for every re-entry, not only re-wins): same test on non-re-win re-entries;
  nobelow (BOX 199 §3 DEAD downward charge): re-wins where no vertex q of b's play at t2 has Lambda_t1(q) != Lambda_(t2-1)(q) or a change of
      its e-letters less relevant than y on [t1, t2-1];  wb (BOX 199 wbfail): (v, I, y) with c_y > #values of E(wt(y)) ∩ U_y on the y-tops' span;
  maxW = max over (v, I, y) of W_y(v, I) (non-re-win re-entries: BOX 199 REWIN-COUNT's W); maxc = max c_y;
  zb: a re-win whose most relevant changed letter above y (between E_t1(b) and E_t2(b)) is on b's play BEFORE y at t2.
Usage: rwwt227.py G.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r226"), os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
import own
def census(G, cap=3000):
    out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); vj = own.VJ(prio); rk = vj.rk; N = G["N"]
    evs = {V[("e", q)] for q in O}; gates = {V[("g", q)] for q in O}; T = len(out) - 1
    nx = []
    for (s, vals, tau) in out:
        nx.append([s[u] if u < N else (tau[u] if o_[u] == 1 else succ[u][0]) for u in range(n)])
    def play(t, v):
        p = []; seen = set(); u = v
        while u not in seen: seen.add(u); p.append(u); u = nx[t][u]
        return p
    E = lambda t, v: frozenset(e for e in out[t][1][v][1] if e in evs)
    def lexgt(A, B):            # A >lex B (e-vertices are even: more relevant top in A wins)
        d = A ^ B
        return bool(d) and max(d, key=lambda e: rk[e]) in A
    c = dict(maxW=0, maxc=0, nobelow=0, wb=0, changes=0, kind=0, trA=0, trD=0, hw=0, gt=0, reent=0, rewin=0, dn=0, rh=0, rw=0, wc=0, zb=0, T=T)
    for v in range(n):
        t = 0
        while t <= T:
            u_ = t
            while u_ + 1 <= T and out[u_ + 1][1][v][0] == out[t][1][v][0]: u_ += 1
            w = out[t][1][v][0]; split = {}; tops = []
            for i in range(t + 1, u_ + 1):
                A, B = E(i - 1, v), E(i, v)
                if A == B: continue
                c["changes"] += 1; z = max(A ^ B, key=lambda e: rk[e]); tops.append((i, z))
                p1, p0 = play(i, v), play(i - 1, v)
                uu = next(x for x in p1 if nx[i][x] != nx[i - 1][x])
                old, new = nx[i - 1][uu], nx[i][uu]; split[i] = (uu, new)
                if not (uu < N or uu in gates): c["kind"] += 1
                if out[i - 1][1][uu][0] != w or out[i][1][uu][0] != w: c["trA"] += 1
                if (A ^ B) != (E(i - 1, uu) ^ E(i, uu)): c["trD"] += 1
                va = out[i - 1][1]
                if uu < N:
                    if not vj.cmp(va[new], va[old]) > 0: c["hw"] += 1
                elif uu in gates:
                    vb = out[i][1]
                    if not vj.cmp(vb[new], vb[old]) < 0: c["gt"] += 1
            letters = {z for _, z in tops}
            for y in letters:
                ts = [i for i, z in tops if z == y]; wty = nx[0][y]
                Uy = lambda S: frozenset(e for e in S if rk[e] > rk[y])
                Ly = lambda S: frozenset(e for e in S if rk[e] < rk[y])
                if len(ts) > len({Uy(E(s, wty)) for s in range(ts[0], ts[-1] + 1)}): c["wb"] += 1
                Wy = sum(1 for t1, t2 in zip(ts, ts[1:]) if split[t1] != split[t2])
                c["maxW"] = max(c["maxW"], Wy); c["maxc"] = max(c["maxc"], len(ts))
                for t1, t2 in zip(ts, ts[1:]):
                    c["reent"] += 1
                    vals_wt = {Uy(E(s, wty)) for s in range(t1, t2 + 1)}
                    if split[t1] == split[t2]:
                        c["rewin"] += 1; uu, b = split[t1]; a = nx[t2 - 1][uu]
                        if not vj.cmp(out[t2 - 1][1][a], out[t1][1][b]) > 0: c["dn"] += 1
                        if not any(out[t1][1][q][0] != out[t2 - 1][1][q][0] or any(Ly(E(s, q)) != Ly(E(s + 1, q)) for s in range(t1, t2 - 1))
                                   for q in play(t2, b)): c["nobelow"] += 1
                        if not lexgt(Uy(E(t2, b)), Uy(E(t1, b))): c["rh"] += 1
                        if len(vals_wt) < 2: c["rw"] += 1
                        d = Uy(E(t2, b)) ^ Uy(E(t1, b))
                        if d:
                            zz = max(d, key=lambda e: rk[e]); pb = play(t2, b)
                            if zz in pb and y in pb and pb.index(zz) < pb.index(y): c["zb"] += 1
                    elif len(vals_wt) < 2: c["wc"] += 1
            t = u_ + 1
    return c
if __name__ == "__main__":
    K = ("T", "maxc", "maxW", "nobelow", "wb", "changes", "kind", "trA", "trD", "hw", "gt", "reent", "rewin", "dn", "rh", "rw", "wc", "zb")
    print("instance", " ".join(K))
    for f in sys.argv[1:]:
        c = census(json.load(open(f))); print(os.path.basename(f), " ".join(str(c[k]) for k in K), flush=True)
