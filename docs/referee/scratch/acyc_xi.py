"""REFEREE successor 28: P-ACYC Corollary ACYC-XI replay. N5'-xi itself is L-NEW's box190 n5v (byte copy pinned in L-SI box81/ref,
run unchanged: I have no second N5'-xi); everything else is mine: Gamma3 builder equality (xicyc_replay.build vs ref gamma3.build),
standard states (every non-mover Even vertex and tau equal to state 0), the first fallback k1 (least iteration with S4c's flag), and
the comparison of N5'-xi's mover choices on states 0..k1-1 with my own Howard run on IDEAL-CYC(Gamma3) (acyc_replay.run, own VJ).
Counters (fix round 1 adds taubad = states 0..k1-1 with tau != the standard tau (pe_g at gates, K2 -> K2), and the
histogram of iterations after the first fallback to the S5 stop): s3startdiff (state 0 off the movers != my transported R104 start), nofb (no fallback within 10^4 iterations or run ended), nonstd, notequal (mover sequence != own Howard, or k1 != T + 1),
bigk (k1 - 1 > N), builderdiff. Usage: acyc_xi.py LSI_BOX81 agen COUNT SEED | LSI_BOX81 files F.json ..."""
import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); box = sys.argv[1]; RN = os.path.join(box, "ref/experiments/new")
sys.path[:0] = [box, os.path.join(RN, "box190"), os.path.join(RN, "box21"), os.path.join(RN, "box189"), os.path.join(RN, "box191")]
import n5v, n5x, gamma3
from acyc_replay import run, acyclic
from xicyc_replay import build
PADS = {"K", "pe", "pb", "m"}
def one(G):
    g, sig0, tau0, V = gamma3.build(G, PADS); prio, own, fs, sig, movers, idx, succ = build(G, True)
    same = (list(g.prio) == prio and list(g.owner) == own and all(sorted(g.succ[v]) == sorted(succ[v]) for v in range(g.n))
            and all(sig0[v] == sig[v] for v in sig0 if g.owner[v] == 0))
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sg, ta = n5x.start_pair(g, E, Ed, None); sg, ta = list(sg), list(ta)
    states = [(sg, ta)]; k1 = None; it = 0
    while it < 10 ** 4:
        r = n5v.step(g, E, Ed, sg, ta, "xi")
        if r is None: break
        it += 1; sg, ta, _, _, fb = r; sg, ta = list(sg), list(ta)
        if fb: k1 = it; break
        states.append((sg, ta))
    s0, t0 = states[0]
    K2 = idx[("K", 2)]; stdtau = {K2: K2}
    for x in range(G["N"]):
        for k in range(len(G["opts"][x])): stdtau[idx[("g", (x, k))]] = idx[("pe", (x, k))]
    taubad = sum(1 for s, t in states if any(t[v] != w for v, w in stdtau.items()))   # tau != R118 (k)'s standard tau
    after = None
    if k1 is not None:                       # iterations after the first fallback, to the S5 stop
        after = 0; s2, t2 = list(sg), list(ta)
        while after < 10 ** 4:
            r = n5v.step(g, E, Ed, s2, t2, "xi")
            if r is None: break
            after += 1; s2, t2 = list(r[0]), list(r[1])
    s3start = all(s0[v] == sig[v] for v in range(g.n) if g.owner[v] == 0 and v not in movers)   # S3 = transported R104 start
    nonstd = sum(1 for s, t in states if any(s[v] != s0[v] for v in range(g.n) if g.owner[v] == 0 and v not in movers) or t != t0)
    seq = [tuple(succ[x].index(s[x]) for x in movers) for s, t in states]
    mine = run(G, True)
    # own Howard mover sequence
    import acyc_replay
    return dict(N=G["N"], acyclic=acyclic(G), builder_equal=same, s3start=s3start, taubad=taubad, after=after, k1=k1, nonstd=nonstd, T_own=mine["T"],
                seq_equal=None), seq
def own_seq(G):
    # re-run own Howard on Gamma3 and return the mover option sequence
    import acyc_replay as A
    prio, own, fs, sig, movers, idx, succ = build(G, True); E = A.VJ(prio, own, fs)
    s = [sig.get(v) for v in range(E.n)]; st, val = E.best_reply(s); seq = [tuple(fs[x].index(s[x]) for x in movers)]
    while True:
        ns = list(s)
        for x in movers:
            b = s[x]
            for w in E.succ[x]:
                if E.cmp(val[w], val[b]) > 0: b = w
            tops = [w for w in E.succ[x] if E.cmp(val[w], val[b]) == 0]; ns[x] = s[x] if s[x] in tops else max(tops)
        if ns == s: return seq
        st, val = E.best_reply(ns, st); s = ns; seq.append(tuple(fs[x].index(s[x]) for x in movers))
if __name__ == "__main__":
    mode = sys.argv[2]; args = sys.argv[3:]
    if mode == "agen":
        from lemma81 import agen
        rng = random.Random(int(args[1])); gl = [(f"agen{args[1]}#{i}", agen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))) for i in range(int(args[0]))]
    else: gl = [(os.path.basename(f), json.load(open(f))) for f in args]
    tot = dict(genomes=0, acyclic=0, builderdiff=0, s3startdiff=0, taubad=0, nofb=0, nonstd=0, notequal=0, bigk=0, states=0); ks = []; AFT = {}
    for name, G in gl:
        r, seq = one(G); mine = own_seq(G); eq = (seq == mine) and r["k1"] == len(mine)
        tot["genomes"] += 1; tot["acyclic"] += r["acyclic"]; tot["builderdiff"] += not r["builder_equal"]; tot["s3startdiff"] += not r["s3start"]; tot["taubad"] += r["taubad"]; AFT[r["after"]] = AFT.get(r["after"], 0) + 1; tot["nofb"] += r["k1"] is None
        tot["nonstd"] += r["nonstd"] > 0; tot["notequal"] += not eq; tot["states"] += len(seq)
        tot["bigk"] += r["k1"] is not None and r["k1"] - 1 > r["N"]; ks.append((r["N"], r["k1"]))
        if mode != "agen": print(name, "N", r["N"], "acyclic", r["acyclic"], "builder_equal", r["builder_equal"], "k1", r["k1"],
                                 "T3_own", len(mine) - 1, "nonstd_states", r["nonstd"], "xi_movers==own_howard_and_k1==T3+1", eq)
    print(f"TOTAL {mode} {' '.join(os.path.basename(a) for a in args)}:", " ".join(f"{k} {v}" for k, v in tot.items()),
          "after-first-fallback histogram", AFT, "max (k1-1)/N", max(round((k - 1) / n, 3) for n, k in ks if k))
