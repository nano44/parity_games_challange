#!/usr/bin/env python3
"""L-RED 57 R222: independent check of L-SI box 83 Lemma LOCK-UP / Corollary LADDER-2 on own.py (L-RED's own IDEAL-CYC Howard run;
no L-SI code). Input: genome .json + .names.json (ladder83 naming: bits B1..Bh, top T, SET option named "SET").
Counters per bit B_l and per Lambda-interval (maximal run of states with every cycle node constant):
  adopt = #t with sigma_t(B_l) = SET and sigma_(t-1)(B_l) != SET; reset = #t with the reverse.
LOCK-UP check (own reading of the hypotheses): HYP(t) = sigma_t(B_l) = SET, Odd takes e at SET's gate, w (SET's W-target) reaches
X = B_(l+1) before any e-vertex, and top(E_t(X)) more relevant than e_SET. CLAIM: HYP(t) => for every later s of the same interval
sigma_s(B_l) = SET and w reaches X e-free.
Usage: lock222.py G.json [names.json]  (env START=rand:<seed> randomises the start strategy)"""
import sys, json, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import own
def analyse(G, nm):
    out, V, O, ow = own.run(G)
    N = G["N"]; idx = {s: i for i, s in enumerate(nm["movers"])}
    bits = sorted(int(s[1:]) for s in nm["movers"] if s[0] == "B" and s[1:].isdigit())
    h = max(bits); X = {l: idx[f"B{l + 1}"] if l < h else idx["T"] for l in bits}
    SET = {l: nm["opts"][idx[f"B{l}"]].index("SET") for l in bits}
    evs = {V[("e", q)] for q in O}; mv = {V[("x", x)]: x for x in range(N)}
    res = {"moves": {l: [0] for l in bits}, "T": len(out) - 1, "C": 0, "adopt": {l: [] for l in bits}, "reset": {l: [] for l in bits}, "hyp": 0, "viol": []}
    # rebuild full successor function per state
    n, prio, own_, succ, V2, O2 = own.build(G)
    def step_fn(sig, tau):
        f = [None] * n
        for v in range(n):
            if own_[v] == 1: f[v] = tau[v]
            elif len(succ[v]) == 1: f[v] = succ[v][0]
        for x in range(N): f[V[("x", x)]] = sig[x]
        return f
    def reaches_e_free(f, v, target):
        seen = set()
        while v not in seen:
            seen.add(v)
            if v == target: return True
            if v in evs: return False
            v = f[v]
        return False
    def eset(vals, v): return {u for u in vals[v][1] if u in evs}
    interval = 0; hyp_open = []   # list of (l, t, interval)
    for l in bits: res["adopt"][l].append(0); res["reset"][l].append(0)
    for t in range(len(out)):
        sigx, vals, tau = out[t]
        if t > 0 and any(out[t - 1][1][v][0] != vals[v][0] for v in range(n)):
            res["C"] += 1; interval += 1; hyp_open = []
            for l in bits: res["adopt"][l].append(0); res["reset"][l].append(0); res["moves"][l].append(0)
        f = step_fn(sigx, tau)
        for l in bits:
            B = idx[f"B{l}"]; g = V[("g", (B, SET[l]))]; e = V[("e", (B, SET[l]))]; on = sigx[B] == g
            if t > 0:
                was = out[t - 1][0][B] == g
                if out[t - 1][0][B] != sigx[B] and not (t > 0 and res["C"] and False): res["moves"][l][-1] += 1
                if on and not was: res["adopt"][l][-1] += 1
                if was and not on: res["reset"][l][-1] += 1
            w = f[e]; xv = V[("x", X[l])]
            wA = reaches_e_free(f, w, xv)
            for (l2, t0) in hyp_open:
                if l2 == l and not (on and wA): res["viol"].append((l, t0, t))
            hyp_open = [(l2, t0) for (l2, t0) in hyp_open if not (l2 == l and not (on and wA))]
            EX = eset(vals, xv)
            top_ok = bool(EX) and max(prio[u] for u in EX) > prio[e]
            if on and tau[g] == e and wA and top_ok:
                res["hyp"] += 1
                if not any(l2 == l for (l2, _) in hyp_open): hyp_open.append((l, t))
    res["maxadopt"] = max(max(a) for a in res["adopt"].values()); res["maxreset"] = max(max(a) for a in res["reset"].values())
    res["maxmoves"] = max(max(a) for a in res["moves"].values())
    return res
if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); nmf = sys.argv[2] if len(sys.argv) > 2 else sys.argv[1].replace(".json", ".names.json")
    nm = json.load(open(nmf)); st = os.environ.get("START", "")
    if st.startswith("rand:"):
        rnd = random.Random(int(st[5:])); G["start"] = [rnd.randrange(len(o)) for o in G["opts"]]
    r = analyse(G, nm)
    print(f"LOCK222 {os.path.basename(sys.argv[1])} START={st or 'stored'} T {r['T']} C {r['C']} hyp {r['hyp']} viol {len(r['viol'])} "
          f"maxmoves {r['maxmoves']} maxadopt {r['maxadopt']} maxreset {r['maxreset']} adopt {dict((l, a) for l, a in r['adopt'].items())} "
          f"reset {dict((l, a) for l, a in r['reset'].items())}" + (f" VIOL {r['viol'][:5]}" if r['viol'] else ""))
