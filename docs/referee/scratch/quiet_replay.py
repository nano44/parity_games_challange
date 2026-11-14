"""REFEREE successor 28: P-N5-QUIET DATA replay with the referee's own engine (xicyc_vj.py VJ values, local-improvement optimal
counterstrategy; xicyc_replay.build Γ builder from R104's text, e-priorities by (level, gate)). No lane code in the counters; the random set
is rand191.rgen (imported only as the set's definition). Howard run of IDEAL-CYC(G) from the stored start, my tie rule (largest index;
ties counted). Counters (per run, summed):
  cnlow    (state, vertex) pairs whose cycle node has priority < 2                    [CN2]
  k2fail   states with sigma-bar(K2) != K1 or not Omega(K1) < Omega(K2)               [LOC-K2]
  gst/ties (state, gate) pairs / pairs with Omega(e_g) == Omega(beta_g)               [NO-TIE]
  locfail  no-tie (state, gate) pairs where sigma-bar(g) is not the strictly smaller face [LOC-GATE]
  bpairs/bfail (state, v) pairs, v not cW and not an e with successor cW / Lambda an e or at least as relevant as the least e [B-ONLY]
  Q, W     loud steps (some vertex changes class (Lambda, E)), longest quiet window (steps); wfail W > L; Tfail T > Q + (Q+1)L
  crossflip sigma-bar changes on quiet steps at gates whose two faces are in different classes
  DEtot    max over v of the number of distinct classes; sumDE = sum over v
Usage: quiet_replay.py LNEW_ROOT files F.json ... | LNEW_ROOT rand COUNT SEED"""
import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_vj import VJ
from xicyc_replay import build

def run(G):
    prio, own, fs, sig, movers, idx, succ = build(G, False); E = VJ(prio, own, fs); n = E.n; N = G["N"]
    O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]; M = len(O)
    gates = [(idx[("g", q)], idx[("e", q)], idx[("b", q)]) for q in O]
    evs = {idx[("e", q)] for q in O}; cW = idx["cW"]; K1, K2 = idx[("K", 1)], idx[("K", 2)]
    excl = {cW} | {idx[("e", q)] for q in O if G["opts"][q[0]][q[1]][0] < 0}
    leaste = min(E.rk[e] for e in evs)
    L = (M + 1) * (2 * M + 1) * (N + 1) + N * (n - 1)
    r = dict(T=0, states=0, cnlow=0, k2fail=0, gst=0, ties=0, locfail=0, bpairs=0, bfail=0, Q=0, W=0, crossflip=0, howardties=0)
    s = [sig.get(v) for v in range(n)]; st, val = E.best_reply(s); hist = []
    def cls(val):
        return [(val[v][0], frozenset(u for u in val[v][1] if u in evs)) for v in range(n)]
    def visit(st, val):
        r["states"] += 1
        r["cnlow"] += sum(1 for v in range(n) if prio[val[v][0]] < 2)
        r["k2fail"] += not (st[K2] == K1 and E.cmp(val[K1], val[K2]) < 0)
        for g, e, b in gates:
            r["gst"] += 1; c = E.cmp(val[e], val[b])
            if c == 0: r["ties"] += 1
            elif st[g] != (e if c < 0 else b): r["locfail"] += 1
        for v in range(n):
            if v in excl: continue
            r["bpairs"] += 1; r["bfail"] += E.rk[val[v][0]] >= leaste
        hist.append((cls(val), [st[g] for g, e, b in gates]))
    visit(st, val)
    while r["T"] < 10 ** 5:
        ns = list(s)
        for x in movers:
            b = s[x]
            for w in E.succ[x]:
                if E.cmp(val[w], val[b]) > 0: b = w
            tops = [w for w in E.succ[x] if E.cmp(val[w], val[b]) == 0]
            if s[x] in tops: ns[x] = s[x]
            else: r["howardties"] += len(tops) > 1; ns[x] = max(tops)
        if ns == s: break
        st, val = E.best_reply(ns, st); s = ns; r["T"] += 1; visit(st, val)
    cur = 0
    for t in range(1, len(hist)):
        (c0, g0), (c1, g1) = hist[t - 1], hist[t]
        if c0 != c1: r["Q"] += 1; cur = 0
        else:
            cur += 1; r["W"] = max(r["W"], cur)
            for i, (g, e, b) in enumerate(gates):
                if g0[i] != g1[i] and c1[e] != c1[b]: r["crossflip"] += 1
    r["L"] = L; r["wfail"] = int(r["W"] > L); r["Tfail"] = int(r["T"] > r["Q"] + (r["Q"] + 1) * L)
    per = [len(set(h[0][v] for h in hist)) for v in range(n)]; r["DEtot"] = max(per); r["sumDE"] = sum(per); r["N"] = N
    return r

if __name__ == "__main__":
    root = sys.argv[1]; mode = sys.argv[2]
    if mode == "rand":
        sys.path.insert(0, os.path.join(root, "experiments/new/box191")); import rand191
        cnt, seed = int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed)
        gl = [(f"rand{seed}#{i}", rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))) for i in range(cnt)]
    else: gl = [(os.path.basename(f), json.load(open(f))) for f in sys.argv[3:]]
    tot = {}; mx = dict(T=0, W=0, WoverN=0.0)
    for name, G in gl:
        r = run(G)
        if mode != "rand": print(name, " ".join(f"{k} {v}" for k, v in r.items()))
        for k in ("states", "cnlow", "k2fail", "gst", "ties", "locfail", "bpairs", "bfail", "crossflip", "wfail", "Tfail", "howardties", "T"):
            tot[k] = tot.get(k, 0) + r[k]
        mx["T"] = max(mx["T"], r["T"]); mx["W"] = max(mx["W"], r["W"]); mx["WoverN"] = max(mx["WoverN"], round(r["W"] / r["N"], 3))
    print(f"TOTAL {mode} {len(gl)} genomes:", " ".join(f"{k} {v}" for k, v in tot.items()), "| max", mx)
