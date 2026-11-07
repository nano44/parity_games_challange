"""REFEREE successor 26: P-N5-XICYC replays with own code (xicyc_vj.py); Gamma(G) / Gamma3(G) built from R104's text as quoted in
P-N5-REACH §1/§3 (own builder, no lane code). Genome JSON: N, lev, opts[x][k] = [W-target, Xi-target (-1 = X), option id], gate[x][k],
br[id], bp[id], start[x].
Usage: xicyc_replay.py run FILE.json [pad]      IDEAL-CYC Howard run on Gamma (or Gamma3 with 'pad'): labels C/R/p, ties, checks
       xicyc_replay.py brute FILE.json          cross-check best_reply against brute force on every state of the run"""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_vj import VJ, opt_choices

def build(G, pad=False):
    N, lev, opts, gate, br, bp = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"]
    O = [(x, k) for x in range(N) for k in range(len(opts[x]))]; M = len(O); gord = sorted(O, key=lambda q: gate[q[0]][q[1]])
    idx = {}; n = 0
    def new(key):
        nonlocal n; idx[key] = n; n += 1
    for x in range(N): new(("x", x))
    for q in gord: new(("g", q))
    for q in O: new(("b", q))               # beta-vertices in option order (packet §3.1 detail quoted in P-N5-REACH §1)
    for q in gord: new(("e", q))
    new("cX"); new("cW")
    for i in range(4): new(("K", i))
    if pad:
        for nm in ("pA", "s", "q", "r"): new(nm)
        for q in gord: new(("pe", q))
        for q in gord: new(("pbeta", q))
        for q in O: new(("pb", q))
        for q in gord: new(("m", q))
    prio = [0] * n; own = [0] * n; succ = [None] * n; sig = {}
    K0, K1, K2, K3 = (idx[("K", i)] for i in range(4))
    for q in O:
        x, k = q; wt, xt, b = opts[x][k]; g, bv, e = idx[("g", q)], idx[("b", q)], idx[("e", q)]
        prio[g] = 1; own[g] = 1
        prio[bv] = 6 + 2 * br[b] + bp[b]
        P = lambda nm, tgt: idx[(nm, q)] if pad else tgt
        succ[g] = [P("pe", e), P("pbeta", bv)]
        esc = idx[("pb", q)] if pad else K0
        succ[bv] = [xt, esc] if xt >= 0 else [esc]; sig[bv] = xt if xt >= 0 else esc
        succ[e] = [idx["cW"] if wt < 0 else wt]
        if pad:
            prio[idx[("pe", q)]] = 1; succ[idx[("pe", q)]] = [e]
            prio[idx[("pbeta", q)]] = 0; succ[idx[("pbeta", q)]] = [bv]
            prio[idx[("pb", q)]] = 1; succ[idx[("pb", q)]] = [K0]
            prio[idx[("m", q)]] = 2 if G["start"][x] == k else 0; succ[idx[("m", q)]] = [g]
    bmax = max(prio[idx[("b", q)]] for q in O); eb = bmax + 1 + (bmax + 1) % 2   # least even above every beta
    for i, q in enumerate(sorted(O, key=lambda q: (lev[q[0]], gate[q[0]][q[1]]))): prio[idx[("e", q)]] = eb + 2 * i
    for x in range(N):
        succ[x] = [idx[("m", (x, k))] if pad else idx[("g", (x, k))] for k in range(len(opts[x]))]
    prio[idx["cX"]] = 2; succ[idx["cX"]] = [idx["cX"]]
    top = max(prio) + 2; top += top % 2   # least even number at least 2 above every other priority
    cW = idx["cW"]; prio[cW] = top; succ[cW] = [cW]
    prio[K0], prio[K1], prio[K2], prio[K3] = top + 2, 5, 3, top + 3; own[K2] = 1
    if pad:
        succ[K0] = [K1, idx["pA"]]; succ[K1] = [idx["q"], idx["s"]]; succ[K2] = [idx["r"], K2]
        prio[idx["pA"]] = 0; succ[idx["pA"]] = [K3]; prio[idx["s"]] = 0; succ[idx["s"]] = [K1]
        prio[idx["q"]] = 1; succ[idx["q"]] = [K0]; prio[idx["r"]] = 0; succ[idx["r"]] = [K1]
        sig[K0] = idx["pA"]; sig[K1] = idx["s"]
    else:
        succ[K0] = [K1, K3]; succ[K1] = [K0, K1]; succ[K2] = [K1, K2]; sig[K0] = K3; sig[K1] = K1
    succ[K3] = [K1, K2]; sig[K3] = K2
    for v in range(n):
        if own[v] == 0 and v not in sig: sig[v] = succ[v][0]
    movers = [idx[("x", x)] for x in range(N)]
    for x in range(N): sig[movers[x]] = succ[movers[x]][G["start"][x]]
    # IDEAL-CYC: every non-mover Even vertex frozen at its start successor
    fsucc = [list(succ[v]) if (own[v] == 1 or v in movers) else [sig[v]] for v in range(n)]
    return prio, own, fsucc, sig, movers, idx, succ

def howard(G, pad=False, cap=100000, brute=False):
    prio, own, succ, sig, movers, idx, _ = build(G, pad); E = VJ(prio, own, succ)
    s = [sig.get(v) for v in range(E.n)]; st, val = E.best_reply(s); lab = []; ties = 0; states = [(tuple(s), st, val)]
    if brute: assert all(E.cmp(a, b) == 0 for a, b in zip(E.brute(s), val))
    while len(lab) < cap:
        ns = list(s)
        for x in movers:
            cand = list(E.succ[x]); b = s[x]
            for w in cand:
                if E.cmp(val[w], val[b]) > 0: b = w
            tops = [w for w in cand if E.cmp(val[w], val[b]) == 0]
            if s[x] in tops: ns[x] = s[x]
            else:
                ties += len(tops) > 1; ns[x] = max(tops)   # tie rule (only if ties occur): larger index
        if ns == s: break
        nst, nval = E.best_reply(ns, st)
        if brute: assert all(E.cmp(a, b) == 0 for a, b in zip(E.brute(ns), nval))
        C = any(nval[v][0] != val[v][0] for v in range(E.n)); R = any(nst[v] != st[v] for v in range(E.n) if own[v] == 1)
        lab.append("C" if C else ("R" if R else "p")); s, st, val = ns, nst, nval; states.append((tuple(s), st, val))
    return E, "".join(lab), ties, states, movers, idx

def lam_keep_max(E, states):
    """longest run of consecutive steps keeping every Lambda (rule-independent: Lambda is part of the unique value)."""
    best = cur = 0
    for (a, b) in zip(states, states[1:]):
        if all(a[2][v][0] == b[2][v][0] for v in range(E.n)): cur += 1; best = max(best, cur)
        else: cur = 0
    return best

if __name__ == "__main__":
    mode, f = sys.argv[1], sys.argv[2]; G = json.load(open(f)); pad = len(sys.argv) > 3 and sys.argv[3] == "pad"
    E, lab, ties, states, movers, idx = howard(G, pad, brute=(mode == "brute"))
    pm = max((len(r) for r in lab.replace("R", "C").split("C")), default=0)
    print(os.path.basename(f), "pad" if pad else "gamma", "n", E.n, "N", G["N"], "T", len(lab), "C", lab.count("C"), "R", lab.count("R"),
          "p", lab.count("p"), "max p-run", pm, "max Lambda-keeping run", lam_keep_max(E, states), "Howard ties", ties, lab,
          "brute-checked" if mode == "brute" else "")
