#!/usr/bin/env python3
"""L-COMP box 44 item 1, F_n: L-SI 52's FREE genomes (claude/l-si 26704e01 docs/si/box104-map.md §4) on MY builder and MY engine.
Quoted definition (box 104 §4): «G* = (G, π): G has the data of an R104 genome without its β-ranks and parities (N movers with levels; M
options q = (x, k), each with a W-target of level lev(x) − 1 (none at level 0), a Ξ-target (a mover or X), a distinct gate index; a
start), and π is an injective map from the 2M CARRIERS β_q, e_q into the integers ≥ 6, of either parity. Γ3*(G*) is R117's Γ3 (same
vertices, indices, owners, edges and pads) with Ω(β_q) := π(β_q), Ω(e_q) := π(e_q), top := the least even number ≥ max π + 2, Ω(c_W) :=
top, Ω(K0) := top + 2, Ω(K3) := top + 3; movers 0, gates 1, c_X 2, K2 3, K1 5 and the pad priorities are R117's.»
  g3free(G, piB, piE): MY builder = box34/own34.build's vertices, indices, owners, edges and pads (my text builder of R117's Γ3), with
    the priorities of the definition above. free104.py was NOT opened.
  decode(g): reads a free genome G* back from a game by its SHAPE alone (gates = the Odd vertices of priority 1; m-pads = the vertices
    whose one successor is a gate; movers = the Even vertices all of whose successors are m-pads; faces by the pads' priorities; option
    order = β-vertex order, gate order = gate-vertex order), checking every level condition; the game is then rebuilt by g3free and
    compared with the file (bytes, then isomorphism).
  check: Lemma FREE-REACH's counters (box 104 §4, quoted): s3fail «unit genomes: S3's pair is not the standard state», nonstd «unit
    states before the first fallback», nohoward «unit (step, mover) pairs: the mover's new choice is not a ⊴-best successor, or it left
    a best current one», fbwrong «unit genomes: the first fallback is not at T3* + 1», endwrong «unit genomes: fallbacks ≠ 1 or
    iterations ≠ T3* + 3», wrong «unit genomes: regions ≠ harness Zielonka». T3* := the first state at which no mover has a strictly
    better successor. Values for the Howard test: the engine's Ξσ (n5b SpecSI), compared by MY comparator val44.cmpval; VALB=k also
    recomputes Ξσ by val44.evaluate at every k-th state (valdiff, unit (state, vertex)).
    Mine: stratbad (verify.check on the output strategies); outsideA (unit (step, mover): a mover moved to an option that is not
    strictly Ξσ-better; FREE-REACH (e)'s «A(x) = {current} ∪ {strictly Ξσ-better}», the test that replaces nohoward in MODE=spec); tdiff (unit genomes: T3* ≠ T(G_n) = MY Howard run of PGSolver's
    switchallexp_n from its best-reward start); profdiff (unit steps t < T3*: the number of movers that switch at step t ≠ the number
    of Even vertices of G_n that switch at step t of my Howard run: a mapping-free trajectory check).
  prio: the E-DOM census of box 104 §5.1 («odd β-vertices above some e-vertex», e-vertices below some β).
Controls: CTRL=1 (best := worst: nohoward), CTRL=2 (T3* shifted: fbwrong, endwrong), CTRL=3 (standard state with σ(K0) = K1: s3fail,
nonstd), CTRL=4 (Zielonka on the game with c_W odd: wrong).
Usage: free44.py F.pg n OUT   (env MODE=xi|spec, CTRL, VALB; resumable: OUT rows are skipped, the run checkpoints)"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE, os.path.join(R, "experiments", "n5-second"), os.path.join(R, "experiments", "hard-families"), os.path.join(R, "experiments", "harness")]
import pg, zielonka, verify
import wrap44, n5xi44, val44
EVEN, ODD = 0, 1
MODE = os.environ.get("MODE", "xi"); CTRL = os.environ.get("CTRL", "0"); VALB = int(os.environ.get("VALB", "0"))
KEYS = ("s3fail", "nonstd", "nohoward", "fbwrong", "endwrong", "wrong", "stratbad", "outsideA", "valdiff", "tdiff", "profdiff")


def g3free(G, piB, piE):
    """G: dict N, opts[x] = [[wt, xt], ...] (wt = -1: c_W; xt = -1: X), gate[x][k] (distinct gate indices), start[x]; piB / piE: dicts
    (x, k) -> priority. Vertex order (R117's, as box34/own34.build): movers, gates (gate order), β (option order), e (gate order), c_X,
    c_W, K0..K3, pA, s, q, r, pe (gate order), pβ (gate order), pb (option order), m (gate order)."""
    N, opts, gate = G["N"], G["opts"], G["gate"]
    O = [(x, k) for x in range(N) for k in range(len(opts[x]))]; byg = sorted(O, key=lambda q: gate[q[0]][q[1]])
    V = {}
    def add(key): V[key] = len(V)
    for x in range(N): add(("x", x))
    for q in byg: add(("g", q))
    for q in O: add(("b", q))
    for q in byg: add(("e", q))
    add("cX"); add("cW")
    for j in range(4): add(("K", j))
    for p in ("pA", "s", "q", "r"): add(p)
    for q in byg: add(("pe", q))
    for q in byg: add(("pB", q))
    for q in O: add(("pb", q))
    for q in byg: add(("m", q))
    n = len(V); prio = [0] * n; own = [EVEN] * n; succ = [None] * n
    pis = [piB[q] for q in O] + [piE[q] for q in O]
    assert len(set(pis)) == len(pis) and min(pis) >= 6, "π is not injective into the integers >= 6"
    top = max(pis) + 2; top += top % 2
    K = [V[("K", j)] for j in range(4)]
    prio[V["cX"]] = 2; prio[V["cW"]] = top; prio[K[0]] = top + 2; prio[K[1]] = 5; prio[K[2]] = 3; prio[K[3]] = top + 3; own[K[2]] = ODD
    for x in range(N): succ[V[("x", x)]] = [V[("m", (x, k))] for k in range(len(opts[x]))]
    for q in O:
        x, k = q; wt, xt = opts[x][k][0], opts[x][k][1]
        g = V[("g", q)]; own[g] = ODD; prio[g] = 1; succ[g] = [V[("pe", q)], V[("pB", q)]]
        succ[V[("pe", q)]] = [V[("e", q)]]; prio[V[("pe", q)]] = 1
        succ[V[("pB", q)]] = [V[("b", q)]]; prio[V[("pB", q)]] = 0
        prio[V[("b", q)]] = piB[q]; prio[V[("e", q)]] = piE[q]
        succ[V[("b", q)]] = ([V[("x", xt)]] if xt >= 0 else []) + [V[("pb", q)]]
        succ[V[("pb", q)]] = [K[0]]; prio[V[("pb", q)]] = 1
        succ[V[("e", q)]] = [V[("x", wt)] if wt >= 0 else V["cW"]]
        m = V[("m", q)]; succ[m] = [g]; prio[m] = 2 if G["start"][x] == k else 0
    succ[V["cX"]] = [V["cX"]]; succ[V["cW"]] = [V["cW"]]
    succ[K[0]] = [K[1], V["pA"]]; succ[V["pA"]] = [K[3]]
    succ[K[1]] = [V["q"], V["s"]]; succ[V["q"]] = [K[0]]; prio[V["q"]] = 1; succ[V["s"]] = [K[1]]
    succ[K[2]] = [V["r"], K[2]]; succ[V["r"]] = [K[1]]
    succ[K[3]] = [K[1], K[2]]
    return pg.Game(prio, own, [sorted(s) for s in succ]), V


def decode(g):
    """Free genome (G, piB, piE) of a Γ3*-shaped game, read from the shape; raises AssertionError with the clause that fails."""
    n = g.n
    gates = [v for v in range(n) if g.owner[v] == ODD and g.prio[v] == 1 and len(set(g.succ[v])) == 2]; gs = set(gates)
    rest = [v for v in range(n) if g.owner[v] == ODD and v not in gs]; assert len(rest) == 1, "Odd vertices other than gates: %s" % rest
    mp = {v: g.succ[v][0] for v in range(n) if g.owner[v] == EVEN and len(g.succ[v]) == 1 and g.succ[v][0] in gs}
    assert len(set(mp.values())) == len(mp) == len(gates), "m-pads and gates are not in bijection"
    movers = [v for v in range(n) if g.owner[v] == EVEN and v not in mp and all(w in mp for w in g.succ[v])]
    mi = {v: i for i, v in enumerate(movers)}; N = len(movers)
    face = {}
    for gt in gates:
        a, b = sorted(set(g.succ[gt]), key=lambda u: g.prio[u]); assert (g.prio[a], g.prio[b]) == (0, 1), "gate faces are not pads of priority 0 / 1"
        beta = g.succ[a][0]; e = g.succ[b][0]; assert len(g.succ[a]) == 1 and len(g.succ[b]) == 1 and len(g.succ[e]) == 1
        face[gt] = (beta, e)
    opt = []                                    # (mover index, β vertex, gate vertex, m-pad)
    for x in movers:
        for m in g.succ[x]: opt.append((mi[x], face[mp[m]][0], mp[m], m))
    opt.sort(key=lambda o: (o[0], o[1])); M = len(opt); assert M == len(gates)
    assert n == N + 7 * M + 10, "vertex count %d is not N + 7M + 10 (N %d, M %d)" % (n, N, M)
    grank = {gt: i for i, gt in enumerate(sorted(gates))}
    G = dict(N=N, opts=[[] for _ in range(N)], gate=[[] for _ in range(N)], start=[None] * N); piB = {}; piE = {}; cW = None
    for x, beta, gt, m in opt:
        k = len(G["opts"][x]); e = face[gt][1]
        w = g.succ[e][0]
        if w in mi: wt = mi[w]
        else:
            assert g.succ[w] == [w], "an e-vertex leads to neither a mover nor a self-loop"; assert cW in (None, w); cW = w; wt = -1
        bs = [u for u in g.succ[beta] if u in mi]; pbs = [u for u in g.succ[beta] if u not in mi]
        assert len(pbs) == 1 and len(bs) <= 1 and g.prio[pbs[0]] == 1, "β-vertex %d: successors are not (Ξ-target,) pb" % beta
        G["opts"][x].append([wt, mi[bs[0]] if bs else -1]); G["gate"][x].append(grank[gt])
        piB[(x, k)] = g.prio[beta]; piE[(x, k)] = g.prio[e]
        if g.prio[m] == 2:
            assert G["start"][x] is None, "two start pads at mover %d" % x; G["start"][x] = k
        else: assert g.prio[m] == 0
    assert None not in G["start"], "a mover without a start pad"
    lev = [None] * N                            # levels: 0 iff the W-target is c_W, else lev(W-target) + 1; all options of a mover agree
    def L(x, seen=()):
        if lev[x] is None:
            assert x not in seen, "W-targets form a cycle"
            ls = {(0 if o[0] < 0 else L(o[0], seen + (x,)) + 1) for o in G["opts"][x]}
            assert len(ls) == 1, "mover %d: its options have W-targets of different levels" % x; lev[x] = ls.pop()
        return lev[x]
    for x in range(N): L(x)
    G["lev"] = lev
    return G, piB, piE


def standard(G, g, V):
    s = [-1] * g.n; t = [-1] * g.n
    for v in range(g.n):
        if len(g.succ[v]) == 1: (s if g.owner[v] == EVEN else t)[v] = g.succ[v][0]
    for x in range(G["N"]):
        s[V[("x", x)]] = V[("m", (x, G["start"][x]))]
        for k, o in enumerate(G["opts"][x]):
            s[V[("b", (x, k))]] = V[("x", o[1])] if o[1] >= 0 else V[("pb", (x, k))]; t[V[("g", (x, k))]] = V[("pe", (x, k))]
    s[V[("K", 0)]] = V["pA"]; s[V[("K", 1)]] = V["s"]; s[V[("K", 3)]] = V[("K", 2)]; t[V[("K", 2)]] = V[("K", 2)]
    return s, t


class Checker:
    def __init__(self, G, g, V):
        self.G, self.g, self.V = G, g, V; self.mv = [V[("x", x)] for x in range(G["N"])]
        self.st = dict(c=dict.fromkeys(KEYS, 0), prev=None, prevval=None, Tstar=None, prof=[], first_info={})
    def get(self): return self.st
    def set(self, st):
        if st is not None: self.st = st
    def fail(self, k, t, info, cnt=1):
        self.st["c"][k] += cnt; self.st["first_info"].setdefault(k, (t, info))
    def best(self, val, v, ctrl):
        ws = sorted(set(self.g.succ[v])); top = ws[0]
        for w in ws[1:]:
            c = val44.cmpval(self.g, val[w], val[top])
            if (c < 0) if ctrl else (c > 0): top = w
        return [w for w in ws if val44.cmpval(self.g, val[w], val[top]) == 0]
    def hook(self, t, sigma, tau, vs, Is, It, F):
        if F > 0: return
        G, g, V, st = self.G, self.g, self.V, self.st
        cur = dict(G); cur["start"] = [None] * G["N"]; okm = True
        for x in range(G["N"]):
            ks = [k for k in range(len(G["opts"][x])) if V[("m", (x, k))] == sigma[V[("x", x)]]]
            if ks: cur["start"][x] = ks[0]
            else: okm = False
        ok = False
        if okm:
            sg, tu = standard(cur, g, V)
            if CTRL == "3": sg[V[("K", 0)]] = V[("K", 1)]
            ok = sg == sigma and tu == tau
        if t == 0 and not (ok and cur["start"] == G["start"]): self.fail("s3fail", 0, "S3 is not the standard state of the genome start")
        if not ok: self.fail("nonstd", t, "state %d is not standard" % t)
        if VALB and t % VALB == 0:
            vb, _ = val44.evaluate(g, sigma)
            d = sum(1 for v in range(g.n) if tuple(vs[v]) != tuple(vb[v]))
            if d: self.fail("valdiff", t, "%d vertices" % d, d)
        if st["prev"] is not None:
            pv, pval = st["prev"], st["prevval"]; sw = 0
            for x in self.mv:
                B = self.best(pval, x, CTRL == "1")
                if MODE == "xi" and (sigma[x] not in B or (pv[x] in B and sigma[x] != pv[x])): self.fail("nohoward", t - 1, "step %d, mover %d: %d -> %d, best %s" % (t - 1, x, pv[x], sigma[x], B))
                if sigma[x] != pv[x] and not val44.cmpval(self.g, pval[sigma[x]], pval[pv[x]]) > 0: self.fail("outsideA", t - 1, "step %d, mover %d: not strictly better" % (t - 1, x))
                sw += sigma[x] != pv[x]
            st["prof"].append(sw)
        if st["Tstar"] is None and all(sigma[x] in self.best(vs, x, False) for x in self.mv): st["Tstar"] = t
        st["prev"] = [sigma[v] for v in range(g.n)]; st["prevval"] = {w: vs[w] for x in self.mv for w in g.succ[x]}
    def finish(self, r, n):
        st, g = self.st, self.g; T = st["Tstar"]; Tc = (T + 1) if (CTRL == "2" and T is not None) else T
        if MODE == "xi":
            if Tc is None or r["first"] != Tc + 1: self.fail("fbwrong", -1, "first fallback at %s, T3* %s" % (r["first"], Tc))
            if r["F"] != 1 or Tc is None or r["Ttot"] != Tc + 3: self.fail("endwrong", -1, "fallbacks %d iterations %d T3* %s" % (r["F"], r["Ttot"], Tc))
        elif r["F"] != 1 or r["first"] is None or r["Ttot"] != r["first"] + 2: self.fail("endwrong", -1, "fallbacks %d iterations %d first %s" % (r["F"], r["Ttot"], r["first"]))
        gz = g
        if CTRL == "4":
            p = list(g.prio); p[self.V["cW"]] += 1; gz = pg.Game(p, g.owner, g.succ)
        if r["win"] != zielonka.solve(gz): self.fail("wrong", -1, "regions differ from Zielonka")
        if verify.check(g, r["win"], r["strat"]): self.fail("stratbad", -1, "verify.check rejects")
        d = dict(T=T, Ttot=r["Ttot"], F=r["F"], first=r["first"], n=g.n, evenwins=r["win"].count(0), Tn=None, ties=None, use=n5xi44.usestr(r))
        if n and MODE == "xi":
            import pgsolver_port
            from n5b import SpecSI
            h = pg.parse(pgsolver_port.switchallexp(n)); s0 = SpecSI(h).initial_strategy_by_best_reward()
            states, Tn, ties, sw = val44.howard(h, s0); d["Tn"] = Tn; d["ties"] = ties
            if T != Tn: self.fail("tdiff", -1, "T3* %s, Howard on switchallexp_%d %d" % (T, n, Tn))
            prof = [sum(1 for v in range(h.n) if a[v] != b[v]) for a, b in zip(states, states[1:])]
            mine = st["prof"][:T] if T is not None else st["prof"]
            dd = sum(1 for a, b in zip(prof, mine) if a != b) + abs(len(prof) - len(mine))
            if dd: self.fail("profdiff", -1, "%d steps" % dd, dd)
        return d


def census(g, G, V):
    O = [(x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]
    pb = [g.prio[V[("b", q)]] for q in O]; pe = [g.prio[V[("e", q)]] for q in O]
    return dict(ebelow=sum(1 for e in pe if any(b > e for b in pb)), odde=sum(1 for e in pe if e % 2), oddbabove=sum(1 for b in pb if b % 2 and any(e < b for e in pe)),
                lo=min(pb + pe), hi=max(pb + pe), cW=g.prio[V["cW"]])


if __name__ == "__main__":
    a = sys.argv[1:]; fn, n, out = a[0], int(a[1]), a[2]
    tag = "FREE44 %s n %d" % (os.path.basename(fn), n)
    if os.path.exists(out) and any(l.startswith(tag + " alg %s ctrl %s " % (MODE, CTRL)) for l in open(out)): sys.exit(0)
    fg = pg.read(fn); G, piB, piE = decode(fg); g, V = g3free(G, piB, piE)
    raw = pg.dumps(g) == open(fn).read(); isoq = raw or wrap44.iso(g, fg, 0) is not None
    assert isoq, "the file is not Γ3*(decode(file))"
    cz = census(g, G, V); M = sum(len(o) for o in G["opts"]); t0 = time.time()
    C = Checker(G, g, V)
    r = n5xi44.run(g, MODE, hook=C.hook, ck=out + ".%s_%s_%s.ck" % (os.path.basename(fn), MODE, CTRL), ckget=C.get, ckset=C.set)
    d = C.finish(r, n); c = C.st["c"]
    line = "%s alg %s ctrl %s | %s | T3* %s iterations %d fallbacks %d first %s it-T %s | N %d M %d |V| %d m %d maxprio %d levels %d Even wins %d | Howard on switchallexp_%d: T %s ties %s | rebuilt by g3free: bytes equal %s isomorphic %s | e below some β %d of %d; odd e %d; odd β above some e %d; carriers %d..%d; c_W %d | %s" % (
        tag, MODE, CTRL, " ".join("%s %d" % (k, c[k]) for k in KEYS), d["T"], d["Ttot"], d["F"], d["first"], (d["Ttot"] - d["T"]) if d["T"] is not None else None,
        G["N"], M, g.n, g.m, max(g.prio), max(G["lev"]) + 1, d["evenwins"], n, d["Tn"], d["ties"], raw, isoq, cz["ebelow"], M, cz["odde"], cz["oddbabove"], cz["lo"], cz["hi"], cz["cW"], d["use"])
    with open(out, "a") as f: f.write(line + "".join(" | FIRST %s %s" % (k, v) for k, v in C.st["first_info"].items()) + "\n")
    print("%s: %.0f s" % (tag, time.time() - t0), file=sys.stderr)
