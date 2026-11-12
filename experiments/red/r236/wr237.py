#!/usr/bin/env python3
"""L-RED 66 R237 (Lead 17:08Z item 1): Lemma WRAP's six must-0 counters (L-SI 52 box 104, claude/l-si 26704e01 wrap104.py header) on
L-RED's OWN engine n5x236 (N5'-xi from SPEC S3; independent «up to SPEC's cycle-node and S4b tie rules»). The wrapper W(H, s0), the
frozen random list, switchallexp_n and W(G_n, iota) are taken from box 104's wrap104.py (the OBJECTS only; env LNEW, LRED, LLIT as
there). The run, the H-valuation (n5x236.Val + one-player optimum for Odd on H) and the counters are L-RED's:
  s3fail (the S3 start is not the standard state of s0), nonstd (states before the first fallback that are not standard), nohoward
  ((step, Even vertex of H) before the first fallback: the new successor is not a best successor of v by H's own valuation, or a best
  current successor was left), fbwrong (first fallback != T + 1), endwrong (fallbacks != 1 or iterations != T + 3), wrong (regions of W
  against harness Zielonka). T = first state at which no Even vertex of H has a strictly better successor in H.
CTRL=1: «best» := worst (nohoward must fire).
Usage: wr237.py json FILE.json | fried n... | lmcs VER n..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.environ["BOX104"])
import n5x236 as X
import wrap104 as WR
import pg, zielonka
CTRL = int(os.environ.get("CTRL", "0"))
def hval(H, sH):
    V = X.Val(list(H.prio)); vals, _ = X.optimum(V, list(H.owner), [list(s) for s in H.succ], [sH[v] if H.owner[v] == 0 else None for v in range(H.n)], 1,
                                                {v: H.succ[v][0] for v in range(H.n) if H.owner[v] == 1}, False)
    return V, vals
def check(H, s0):
    g, std_s, std_t, mp, inv = WR.wrap(H, s0); n = H.n; ev = [v for v in range(n) if H.owner[v] == 0]
    tr = []; fbt = []
    its, fbs, win, sig, sb = X.run(list(g.prio), list(g.owner), [list(s) for s in g.succ], "xi", trace=tr, fbtrace=fbt)
    c = dict(s3fail=0, nonstd=0, nohoward=0, fbwrong=0, endwrong=0, wrong=0)
    s0s, t0s = tr[0]
    c["s3fail"] = int(any(s0s[v] != mp[(v, s0[v])] for v in ev) or any(s0s[v] != w for v, w in std_s.items()) or any(t0s[v] != w for v, w in std_t.items()))
    F1 = fbt[0] if fbt else None; T = None
    upto = F1 if F1 is not None else its
    for t in range(0, min(upto, len(tr))):
        sig_t, tau_t = tr[t]
        c["nonstd"] += int(any(sig_t[v] != w for v, w in std_s.items()) or any(tau_t[v] != w for v, w in std_t.items()))
        sH = [inv[sig_t[v]] if H.owner[v] == 0 else None for v in range(n)]; V, vals = hval(H, sH)
        def best(v):
            b = H.succ[v][0]
            for w in H.succ[v][1:]:
                if (V.better(vals[b], vals[w]) if CTRL == 1 else V.better(vals[w], vals[b])): b = w
            return vals[b]
        if T is None and not any(V.better(vals[w], vals[sH[v]]) for v in ev for w in H.succ[v]): T = t
        if t + 1 < len(tr) and t + 1 < upto:
            nxt = tr[t + 1][0]
            for v in ev:
                ref = best(v); nw = inv[nxt[v]]
                c["nohoward"] += int(vals[nw] != ref or (vals[sH[v]] == ref and nw != sH[v]))
    if T is None: T = -1
    c["fbwrong"] = int(F1 != T + 1); c["endwrong"] = int(fbs != 1 or its != T + 3)
    z = zielonka.solve(g); c["wrong"] = int(any((0 if win[v] else 1) != z[v] for v in range(g.n)))
    return c, T, its, g.n
def report(tag, c, T, its, wn, ref=None):
    print(f"WR237 {tag}: |W| {wn} T {T} iterations {its}" + (f" (box 104: {ref})" if ref is not None else "") + " | " + " ".join(f"{k} {v}" for k, v in c.items()), flush=True)
if __name__ == "__main__":
    m = sys.argv[1]
    if m == "json":
        D = json.load(open(sys.argv[2])); tot = {}; diff = []
        for i, d in enumerate(D["games"]):
            H = pg.Game(d["prio"], d["owner"], d["succ"]); c, T, its, wn = check(H, d["s0"])
            for k, v in c.items(): tot[k] = tot.get(k, 0) + v
            if (T, its, wn) != (d["T"], d["iterations"], d["W"]): diff.append((i, (T, its, wn), (d["T"], d["iterations"], d["W"])))
        print("WR237 json games", len(D["games"]), tot, "rows differing from box 104's (T, iterations, |W|):", len(diff), diff, flush=True)
    elif m == "fried":
        for n in map(int, sys.argv[2:]):
            H, s0, Tf = WR.fried_game(n); c, T, its, wn = check(H, s0); report(f"W(switchallexp_{n})", c, T, its, wn, f"Howard T {Tf}, T + 3 = {Tf + 3}")
    elif m == "lmcs":
        ver = sys.argv[2]
        for n in map(int, sys.argv[3:]):
            H, s0 = WR.lmcs_game(n, ver); c, T, its, wn = check(H, s0); report(f"W(G_{n}, iota) {ver}", c, T, its, wn)
