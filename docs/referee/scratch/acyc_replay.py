"""REFEREE successor 28: P-ACYC (L-SI 43) DATA replay with the referee's own engine (xicyc_vj.py) and own Gamma / Gamma3 builder
(xicyc_replay.build, successor 26; no lane code in the counters). Per genome, on Gamma (IDEAL-CYC) and on Gamma3 (IDEAL-CYC(Gamma3),
pads K/pe/pb/m): the Howard run from the stored start; on every state: notbeta = (state, gate) pairs with sigma-bar off the beta-face
(pbeta_g on Gamma3); nonstrict = pairs where the beta-face value is not strictly better for Odd than the e-face value; lamfail = states
where some vertex's cycle node differs from LAMBDA-CONST's prediction (cW for cW and for e / pe of level-0 options, cX for cX, K1 for
every other vertex); C, R labels; T, T > N. Own Xi-acyclicity test. Optional brute-force cross-check of sigma-bar values (small games).
The genome SET A is lemma81.agen's (imported only to reproduce the set; it is the set's definition).
Brute force (--brute) on games with M <= 12 options only. eplay = (state, vertex) pairs, vertex not an e or pe, whose (sigma, sigma-bar)-play meets an e-vertex.
Usage: acyc_replay.py LSI_BOX81 agen COUNT SEED | LSI_BOX81 starts COUNT SEED R | LSI_BOX81 files F.json ... [--brute]"""
import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_vj import VJ
from xicyc_replay import build

def acyclic(G):
    N = G["N"]; adj = [set(o[1] for o in G["opts"][x] if o[1] >= 0) for x in range(N)]; col = [0] * N
    def dfs(u):
        col[u] = 1
        for w in adj[u]:
            if col[w] == 1 or (col[w] == 0 and not dfs(w)): return False
        col[u] = 2; return True
    return all(col[u] or dfs(u) for u in range(N))

def run(G, pad, brute=False):
    prio, own, fs, sig, movers, idx, succ = build(G, pad); E = VJ(prio, own, fs); N = G["N"]
    O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]
    bface = {idx[("g", q)]: (idx[("pbeta", q)] if pad else idx[("b", q)]) for q in O}
    eface = {idx[("g", q)]: (idx[("pe", q)] if pad else idx[("e", q)]) for q in O}
    K1, cW, cX = idx[("K", 1)], idx["cW"], idx["cX"]
    pred = [K1] * E.n; pred[cW] = cW; pred[cX] = cX
    evs = {idx[("e", q)] for q in O} | ({idx[("pe", q)] for q in O} if pad else set())
    for q in O:
        if G["opts"][q[0]][q[1]][0] < 0:
            pred[idx[("e", q)]] = cW
            if pad: pred[idx[("pe", q)]] = cW
    s = [sig.get(v) for v in range(E.n)]; st, val = E.best_reply(s)
    out = dict(T=0, notbeta=0, nonstrict=0, lamfail=0, C=0, R=0, states=0, eplay=0, brutechecked=0, brutefail=0, howard=[])
    def visit(s, st, val):
        out["states"] += 1
        for g in bface:
            out["notbeta"] += st[g] != bface[g]; out["nonstrict"] += not (E.cmp(val[bface[g]], val[eface[g]]) < 0)
        out["lamfail"] += any(val[v][0] != pred[v] for v in range(E.n))
        for v in range(E.n):            # BETA-ACYC second clause: no (sigma, sigma-bar)-play from a non-e, non-pe vertex meets an e
            if v in evs: continue
            seen = set(); w = v
            while w not in seen:
                if w in evs: out["eplay"] += 1; break
                seen.add(w); w = st[w]
        if brute and len(O) <= 12: out["brutechecked"] += 1; out["brutefail"] += not all(E.cmp(a, b) == 0 for a, b in zip(E.brute(s), val))
        out["howard"].append(tuple(fs[x].index(s[x]) for x in movers))
    visit(s, st, val)
    while out["T"] < 10 ** 5:
        ns = list(s)
        for x in movers:
            b = s[x]
            for w in E.succ[x]:
                if E.cmp(val[w], val[b]) > 0: b = w
            tops = [w for w in E.succ[x] if E.cmp(val[w], val[b]) == 0]
            ns[x] = s[x] if s[x] in tops else max(tops)
        if ns == s: break
        nst, nval = E.best_reply(ns, st)
        if any(nval[v][0] != val[v][0] for v in range(E.n)): out["C"] += 1
        elif any(nst[v] != st[v] for v in range(E.n) if own[v] == 1): out["R"] += 1
        out["T"] += 1; s, st, val = ns, nst, nval; visit(s, st, val)
    return out

if __name__ == "__main__":
    box = sys.argv[1]; mode = sys.argv[2]; brute = "--brute" in sys.argv; args = [a for a in sys.argv[3:] if a != "--brute"]
    if mode == "agen":
        sys.path[:0] = [box, os.path.join(box, "ref/experiments/new/box191"), os.path.join(box, "ref/experiments/new/box189")]
        from lemma81 import agen
        cnt, seed = int(args[0]), int(args[1]); rng = random.Random(seed)
        gl = [(f"agen{seed}#{i}", agen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))) for i in range(cnt)]
    elif mode == "starts":   # set A with every genome's start replaced by R random mover states (genome G' = G with that start)
        sys.path[:0] = [box, os.path.join(box, "ref/experiments/new/box191"), os.path.join(box, "ref/experiments/new/box189")]
        from lemma81 import agen
        cnt, seed, Rn = int(args[0]), int(args[1]), int(args[2]); rng = random.Random(seed); rs = random.Random(1000 + seed); gl = []
        for i in range(cnt):
            G = agen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))
            for j in range(Rn):
                H = dict(G); H["start"] = [rs.randrange(len(o)) for o in G["opts"]]; gl.append((f"agen{seed}#{i}/start{j}", H))
    else:
        gl = [(os.path.basename(f), json.load(open(f))) for f in args]
    tot = {}; Ndist = {}
    for name, G in gl:
        ac = acyclic(G); line = [name, "N", G["N"], "acyclic", ac]
        for pad in (False, True):
            r = run(G, pad, brute); h = r.pop("howard")
            if pad: line += ["gamma3-howard==gamma-howard", h == hg]; tot[("G3", "howard_equal")] = tot.get(("G3", "howard_equal"), 0) + (h == hg)
            else: hg = h
            r["T_gt_N"] = int(r["T"] > G["N"]); r["T_eq_N"] = int(r["T"] == G["N"])
            tag = "G3" if pad else "G"
            for k, v in r.items():
                tot[(tag, k)] = tot.get((tag, k), 0) + v
            tot[(tag, "maxT/N")] = max(tot.get((tag, "maxT/N"), 0), round(r["T"] / G["N"], 3))
            if r["T"] == G["N"]: Ndist.setdefault(tag, []).append(G["N"])
            line += [tag] + [f"{k} {v}" for k, v in r.items()]
        tot[("acyclic",)] = tot.get(("acyclic",), 0) + ac
        if mode == "files": print(*line)
    print(f"TOTAL {mode} {' '.join(args)} genomes {len(gl)} acyclic {tot[('acyclic',)]}")
    for tag in ("G", "G3"):
        print(tag, " ".join(f"{k[1]} {v}" for k, v in tot.items() if k[0] == tag), "N of runs with T = N:", sorted(Ndist.get(tag, [])))
