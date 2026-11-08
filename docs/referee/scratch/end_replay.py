"""REFEREE successor 29: P-N5-END (L-NEW 63) DATA replay with the referee's own code only.
- Game: Gamma3(G) from my own builder (xicyc_replay.build(G, pad=True), successor 26; checked equal to the lane's gamma3 then).
- Engine: my own SPEC S1-S5 (N5) and N5'-xi on top of xicyc_vj.VJ (own VJ valuation + Odd local improvement = pointwise optimum).
  S1: Xi_sigma = values under sigma and Odd's optimal counterstrategy; tau side on G^d (owner swapped, prio + 1).
  S2: I_sigma / I_tau strict improvements. S3 (FIX 1) start computed from the priorities here, and compared with the builder's start.
  S4a: arena H (Even keeps A(v), Odd keeps tau(v)); its pointwise optimum = Odd's best reply on H^d (warm start sigma).
       N5'-xi: at every Even v with |A(v)| >= 2 not its own H-cycle node: sigma_new(v) = Xi_sigma-best of TIE(v) =
       {w in A(v): W*(v) = v (+) W*(w)}, ties: the H-optimum's own choice if among them, else the larger index.
  S4b: symmetric on G^d (never needed if E0 holds; implemented).
  S4c: fallback, FIX 3.  S5: stop when I_sigma = I_tau = empty.
- Counters per run (my own, from the packet's statements):
  e0fail  states with tau != tau0 or I_tau != empty
  e1fail  states before the first fallback with K-config != k0 or I_sigma on {K0,K1,K3} != {(K0,K1)}; S4a results there with K != k0
  e2fail  first fallback: input K != k0, not an Even fallback (I_sigma empty or tau changed), result K != k1
  e3fail  iteration F+1: input K != k1, is a fallback, or result K != k2
  e4fail  iteration F+2: input K != k2, is a fallback, result K != k3, or some beta with a mover Xi-target not on pb
  stopfail  state after F+2 not final (I_sigma or I_tau nonempty), or the run goes on
  finsbar   final state: sigma-bar not pe at a gate, or sigma-bar(K2) != K2;  fintie final: a mover with two option values
  nfb       number of fallbacks != 1;  total != F + 2
  EXACT-L (IDEAL-ACYC genomes, own acyclicity test with self-loops as cycles): lfail = F != L + 1 or total != L + 3,
          L from t3r_sim.run (successor 24's own IDEAL simulator).
Controls: env CTRL=1 (k1, k2 expectations swapped), CTRL=2 (start tau(K2) = r, sigma(K1) = q; not S3).
MODE n5w = N5 with S4a = MY pointwise optimum of H (warm start sigma: ties keep sigma(v)); this is NOT SPEC's S1 tie-break
(FIX 2 / FIX 4), so it tests every statement that uses only (H) / pointwise optimality, not EXACT-L. MODE xi = N5'-xi (ties of
the Xi-best element of TIE: my H choice if among them, else larger index).
Usage: end_replay.py MODE(n5w|xi) gen FAMILY SEED COUNT | MODE files G.json ...
Families (own generator): rand, acyc (Xi-targets of smaller index or X), selfl (at least one Xi self-loop), deep, wide."""
import sys, os, json, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_vj import VJ
from xicyc_replay import build
import t3r_sim

def acyclic(G):
    N = G["N"]; adj = [[o[1] for o in G["opts"][x] if o[1] >= 0] for x in range(N)]; col = [0] * N
    def dfs(u):
        col[u] = 1
        for w in adj[u]:
            if col[w] == 1 or (col[w] == 0 and not dfs(w)): return False
        col[u] = 2; return True
    return all(col[u] or dfs(u) for u in range(N))

def s3_start(prio, own, succ):
    st = []
    for v in range(len(prio)):
        S = succ[v]
        if own[v] == 0:
            ev = [w for w in S if prio[w] % 2 == 0]
            pick = max(ev, key=lambda w: (prio[w], w)) if ev else min(S, key=lambda w: (prio[w], -w))
            amb = len([w for w in (ev or S) if prio[w] == prio[pick]]) > 1
        else:
            od = [w for w in S if prio[w] % 2 == 1]
            pick = max(od, key=lambda w: (prio[w], w)) if od else min(S, key=lambda w: (prio[w], -w))
            amb = len([w for w in (od or S) if prio[w] == prio[pick]]) > 1
        st.append((pick, amb))
    return [p for p, _ in st], sum(a for _, a in st)

class Game:
    def __init__(self, prio, own, succ):
        self.prio, self.own, self.succ, self.n = prio, own, succ, len(prio)
        self.E = VJ(prio, own, succ)
        self.Ed = VJ([p + 1 for p in prio], [1 - o for o in own], succ)
    def xi_sigma(self, sig, warm=None):            # sig: full list (Even entries used)
        st, val = self.E.best_reply(sig, warm); return st, val
    def xi_tau(self, tau, warm=None):              # tau: full list (Odd entries used) = Even strategy of G^d
        st, val = self.Ed.best_reply(tau, warm); return st, val
    def improv(self, E, strat, val, owner):
        I = {}
        for v in range(self.n):
            if self.own[v] != owner: continue
            b = [w for w in self.succ[v] if w != strat[v] and E.cmp(val[w], val[strat[v]]) > 0]
            if b: I[v] = b
        return I

def h_opt(prio, own, succ_H, keep, warm):
    """pointwise optimum for the player 'own == keep' ... implemented as Odd best reply on the dual (keep = 0: Even maximises)."""
    if keep == 0: Hd = VJ([p + 1 for p in prio], [1 - o for o in own], succ_H)
    else: Hd = VJ(prio, own, succ_H)
    fixed = [succ_H[v][0] if len(succ_H[v]) == 1 else None for v in range(len(prio))]
    st, val = Hd.best_reply(fixed, warm)
    return st, val, Hd

def run(G, mode, cap=20000):
    prio, own, fs, sig0, movers, idx, succ = build(G, True); n = len(prio); g = Game(prio, own, succ)
    start, amb = s3_start(prio, own, succ)
    sbuild = [sig0.get(v) for v in range(n)]
    s3eq = all(start[v] == sbuild[v] for v in range(n) if own[v] == 0)
    K0, K1, K2, K3 = (idx[("K", i)] for i in range(4)); pA, s_, q, r = idx["pA"], idx["s"], idx["q"], idx["r"]
    k0, k1, k2, k3 = (pA, s_, K2), (K1, s_, K2), (K1, q, K2), (K1, q, K1)
    if os.environ.get("CTRL") == "1": k1, k2 = k2, k1          # negative control: swapped expectations must fire e2/e3/e4
    N = G["N"]; O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]
    gates = [(idx[("g", o)], idx[("pe", o)]) for o in O]
    betas = [(idx[("b", o)], G["opts"][o[0]][o[1]][1], idx[("pb", o)]) for o in O]
    sig = list(start); tau = list(start); tau0 = list(start)
    if os.environ.get("CTRL") == "2": tau[K2] = r; sig[K1] = q; tau0 = list(tau)   # negative control: not S3 (must fire e0/e1)
    K = lambda s: (s[K0], s[K1], s[K3])
    c = collections.Counter(); states = 0; it = 0; fbs = []; Kin = []; Kout = []; isk = []
    wst = None; wtd = None
    while it < cap:
        states += 1
        st, val = g.xi_sigma(sig, wst); wst = st
        td, vald = g.xi_tau(tau, wtd); wtd = td
        Is = g.improv(g.E, sig, val, 0); It = g.improv(g.Ed, tau, vald, 1)
        c["e0fail"] += (any(tau[v] != tau0[v] for v in range(n) if own[v] == 1) or bool(It))
        if not Is and not It:
            final = (sig, st, val); break
        isk.append(sorted((v, w) for v in (K0, K1, K3) for w in Is.get(v, [])))
        Kin.append(K(sig))
        # S4a
        sn = list(sig)
        if Is:
            A = {v: [sig[v]] + Is.get(v, []) for v in range(n) if own[v] == 0}
            sH = [A[v] if own[v] == 0 else [tau[v]] for v in range(n)]
            hst, hval, Hd = h_opt(prio, own, sH, 0, sig)
            for v in range(n):
                if own[v] != 0: continue
                sn[v] = hst[v]
                if mode == "xi" and len(A[v]) >= 2 and hval[v][0] != v:
                    tie = [w for w in A[v] if hval[v] == Hd.ext(v, hval[w])]
                    assert tie, "empty TIE"
                    best = [tie[0]]
                    for w in tie[1:]:
                        cc = g.E.cmp(val[w], val[best[0]])
                        if cc > 0: best = [w]
                        elif cc == 0: best.append(w)
                    sn[v] = hst[v] if hst[v] in best else max(best)
        tn = list(tau)
        if It:
            A = {v: [tau[v]] + It.get(v, []) for v in range(n) if own[v] == 1}
            sH = [A[v] if own[v] == 1 else [sig[v]] for v in range(n)]
            hst, hval, Hd = h_opt(prio, own, sH, 1, tau)
            for v in range(n):
                if own[v] == 1: tn[v] = hst[v]
        fb = False
        if sn == sig and tn == tau:
            fb = True
            if Is:
                for v, ws in Is.items():
                    b = ws[0]
                    for w in ws[1:]:
                        cc = g.E.cmp(val[w], val[b])
                        if cc > 0 or (cc == 0 and w > b): b = w
                    sn[v] = b
            else:
                for v, ws in It.items():
                    b = ws[0]
                    for w in ws[1:]:
                        cc = g.Ed.cmp(vald[w], vald[b])
                        if cc > 0 or (cc == 0 and w > b): b = w
                    tn[v] = b
            c["evenfb"] += bool(Is)
        fbs.append(fb); Kout.append(K(sn)); it += 1
        sig, tau = sn, tn
    else:
        c["capped"] += 1; return c, dict(it=it, F=None, s3eq=s3eq, amb=amb)
    F = fbs.index(True) + 1 if True in fbs else None
    c["nfb"] += fbs.count(True) != 1
    if F is None: c["nofb"] += 1; return c, dict(it=it, F=F, s3eq=s3eq, amb=amb)
    for t in range(F - 1):     # iterations 1..F-1 (index t = iteration t+1)
        c["e1fail"] += Kin[t] != k0 or isk[t] != [(K0, K1)] or Kout[t] != k0
    t = F - 1
    c["e1fail"] += isk[t] != [(K0, K1)]
    c["e2fail"] += Kin[t] != k0 or Kout[t] != k1
    if it >= F + 1: c["e3fail"] += Kin[F] != k1 or fbs[F] or Kout[F] != k2
    else: c["e3fail"] += 1
    if it >= F + 2: c["e4fail"] += Kin[F + 1] != k2 or fbs[F + 1] or Kout[F + 1] != k3
    else: c["e4fail"] += 1
    c["stopfail"] += it != F + 2
    sig, st, val = final
    c["e4fail"] += any(xt >= 0 and sig[b] != pb for b, xt, pb in betas)
    c["finsbar"] += any(st[gv] != pe for gv, pe in gates) or st[K2] != K2
    c["fintie"] += any(len(set(val[w] for w in succ[x])) > 1 for x in movers)
    return c, dict(it=it, F=F, s3eq=s3eq, amb=amb)

def gen(rng, fam):
    if fam == "deep": d = rng.randint(5, 8); w = rng.randint(1, 2)
    elif fam == "wide": d = rng.randint(1, 3); w = rng.randint(3, 5)
    else: d = rng.randint(1, 5); w = rng.randint(1, 3)
    lev = []
    for l in range(d): lev += [l] * rng.randint(1, w)
    N = len(lev); opts = []; b = 0
    for x in range(N):
        oo = []
        for _ in range(rng.randint(1, 3)):
            wt = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1
            if fam == "acyc": xt = rng.choice(list(range(x)) + [-1])
            else: xt = rng.choice(list(range(N)) + [-1])
            oo.append([wt, xt, b]); b += 1
        opts.append(oo)
    if fam == "selfl":
        x = rng.randrange(N); k = rng.randrange(len(opts[x])); opts[x][k][1] = x
    M = b; perm = list(range(M)); rng.shuffle(perm); gate = []; i = 0
    for x in range(N):
        gate.append([perm[i + k] for k in range(len(opts[x]))]); i += len(opts[x])
    br = list(range(M)); rng.shuffle(br)
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [rng.randrange(2) for _ in range(M)],
            "start": [rng.randrange(len(o)) for o in opts]}

def main():
    mode = sys.argv[1]
    if sys.argv[2] == "gen":
        fam, seed, cnt = sys.argv[3], int(sys.argv[4]), int(sys.argv[5]); rng = random.Random(seed)
        gl = [(f"{fam}{seed}#{i}", gen(rng, fam)) for i in range(cnt)]
    else:
        gl = [(os.path.basename(f), json.load(open(f))) for f in sys.argv[3:]]; gl = [(a, b) for a, b in gl if isinstance(b, dict) and "N" in b]
    tot = collections.Counter(); tally = collections.Counter(); acyc = 0; lfail = 0; Lmax = 0; s3bad = 0; amb = 0; Fs = []
    for name, G in gl:
        c, info = run(G, mode); tot.update(c); s3bad += not info["s3eq"]; amb += info["amb"]
        if info["F"] is not None: tally[(c["nfb"] == 0, info["it"] - info["F"] + 1)] += 1; Fs.append(info["F"])
        if False:   # EXACT-L is tested under SPEC tie-breaks by end_exactl.py, not here
            acyc += 1; L = len(t3r_sim.run(G)) - 1; Lmax = max(Lmax, L)
            bad = info["F"] != L + 1 or info["it"] != L + 3; lfail += bad
            if bad or sys.argv[2] == "files": print("  EXACT-L", name, "L", L, "F", info["F"], "iters", info["it"], "FAIL" if bad else "ok")
        elif sys.argv[2] == "files": print("  ", name, "not IDEAL-ACYC; F", info["F"], "iters", info["it"])
    keys = ["e0fail", "e1fail", "e2fail", "e3fail", "e4fail", "stopfail", "finsbar", "fintie", "nfb", "nofb", "capped"]
    print(f"{mode} {sys.argv[2]} {' '.join(sys.argv[3:6]) if sys.argv[2] == 'gen' else len(gl)}: runs {len(gl)} |",
          " ".join(f"{k} {tot[k]}" for k in keys), f"| evenfb {tot['evenfb']} | tally(one fb, iters from F) {dict(tally)}",
          f"| S3 != builder start {s3bad} | S3 priority ties {amb} | maxF {max(Fs) if Fs else None}",
          f"| IDEAL-ACYC {acyc} lfail {lfail} maxL {Lmax}")

if __name__ == "__main__":
    main()
