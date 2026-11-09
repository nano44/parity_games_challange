#!/usr/bin/env python3
"""L-RED 63 R229 item 5: independent census for L-NEW 68 BOX 203 (claude/l-new 25e040ee: Theorem GATE-CLASS, Corollary GATE-FLIP,
Corollary QUIET-N) and L-RED's sharpening GATE-FLIP-MIN, on R221 own.py (IDEAL-CYC Howard from the genome's start; cap 3000). No L-NEW code.
class_t(v) = (Λ_t(v), E_t(v)), E_t(v) = e-vertices of Π_t(v); cc(v) = #steps at which class(v) changes (= D^tot(v) - 1 if classes never
repeat); rep = #vertices whose class sequence repeats a class (must be 0: R118 (e) + R121 E-MON). Unit: gate g (faces a = e_g, b = β_g).
Must-be-0 counters (TOTALS):
  lfail  : a flip of g at t with neither class(a) nor class(b) changing at t                      [GATE-CLASS]
  gfail  : flips(g) > cc(a) + cc(b)                                                                 [GATE-FLIP]
  rlfail : a RELOCK (a -> b) at t with class(a) unchanged at t;  ulfail : an UNLOCK (b -> a) with class(b) unchanged   [L-RED CLASS-PAYS]
  mfail  : flips(g) > 2·min(cc(a), cc(b)) + 1                                                      [L-RED GATE-FLIP-MIN]
  bonly  : (state, vertex) with Λ an e-vertex (other than e's whose successor is c_W) or c_W at a non-exception   [R123 B-ONLY]
  qflip  : a step with no class change anywhere at which σ̄ changes at some gate;  qfail: a quiet window longer than N   [QUIET-N]
  Tfail  : T > Q + (Q + 1)·N, Q = #loud steps
Records: maxflip (per-gate MAXIMUM) with (cc(a), cc(b)) there; slack_sum / slack_min = min over flipping gates of the bound minus flips for
GATE-FLIP (sum) and GATE-FLIP-MIN (min form); Q, W = longest quiet window, T.
Usage: cls229.py G.json ..."""
import sys, os, json, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r221")]
import own
K = ("lfail", "gfail", "rlfail", "ulfail", "mfail", "rep", "bonly", "qflip", "qfail", "Tfail", "maxflip", "ccA", "ccB", "slack_sum", "slack_min", "Q", "W")
def census(G, cap=3000):
    out, V, O, _ = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); N = G["N"]
    evs = {V[("e", q)] for q in O}; cW = V["cW"]; T = len(out) - 1; c = collections.Counter({k: 0 for k in K}); c["slack_sum"] = c["slack_min"] = 10 ** 9
    cls = lambda t, v: (out[t][1][v][0], frozenset(f for f in out[t][1][v][1] if f in evs))
    exc = {e for e in evs if succ[e][0] == cW} | {cW}
    rk = own.VJ(prio).rk; emin = min(rk[e] for e in evs)
    loud = [False] * (T + 1)
    ch = {}
    for v in range(n):
        seq = [cls(t, v) for t in range(T + 1)]
        ch[v] = [False] + [seq[t] != seq[t - 1] for t in range(1, T + 1)]
        for t in range(1, T + 1): loud[t] |= ch[v][t]
        seen = set(); prev = None
        for s in seq:
            if s != prev:
                if s in seen: c["rep"] += 1; break
                seen.add(s); prev = s
        if v not in exc:
            c["bonly"] += sum(rk[out[t][1][v][0]] >= emin for t in range(T + 1))
    for q in O:
        g, a, b = V[("g", q)], V[("e", q)], V[("b", q)]
        ca, cb = sum(ch[a]), sum(ch[b]); fl = 0
        for t in range(1, T + 1):
            x, y = out[t - 1][2][g], out[t][2][g]
            if x == y: continue
            fl += 1
            if not (ch[a][t] or ch[b][t]): c["lfail"] += 1
            if x == a and not ch[a][t]: c["rlfail"] += 1
            if x == b and not ch[b][t]: c["ulfail"] += 1
            if not loud[t]: c["qflip"] += 1
        c["gfail"] += fl > ca + cb; c["mfail"] += fl > 2 * min(ca, cb) + 1
        if fl:
            c["slack_sum"] = min(c["slack_sum"], ca + cb - fl); c["slack_min"] = min(c["slack_min"], 2 * min(ca, cb) + 1 - fl)
        if fl > c["maxflip"]: c["maxflip"], c["ccA"], c["ccB"] = fl, ca, cb
    Q = sum(loud[1:]); w = W = 0
    for t in range(1, T + 1):
        w = 0 if loud[t] else w + 1; W = max(W, w)
    c["Q"], c["W"] = Q, W; c["qfail"] = int(W > N); c["Tfail"] = int(T > Q + (Q + 1) * N); c["T"] = T
    if c["slack_sum"] == 10 ** 9: c["slack_sum"] = c["slack_min"] = -1
    return c
if __name__ == "__main__":
    print("instance N+M T " + " ".join(K), flush=True)
    for f in sys.argv[1:]:
        G = json.load(open(f)); G = G.get("genome", G); c = census(G)
        print(os.path.basename(f), G["N"] + sum(len(o) for o in G["opts"]), c["T"], " ".join(str(c[k]) for k in K), flush=True)
