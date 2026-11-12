#!/usr/bin/env python3
"""L-COMP box 44 item 1: Lemma WRAP (L-SI 52, claude/l-si 26704e01 docs/si/box104-map.md §3) on a THIRD engine.
Game: MY builder wrap44.wrap (from the text). Run: MY N5'-xi engine n5xi44.run from SPEC's S3. H's own valuation: n5b's SpecSI on H
(val A) and my independent evaluator val44.evaluate (val B). No code of wrap104.py / n5v.py / si.py / n5x236.py.
Counters, as box 104 §3 defines them (quoted), scope: the run from S3 on W(H, s0):
  s3fail   «unit games: S3's pair is not the standard state of s0»
  nonstd   «unit states before the first fallback» (the state is not the standard state of its H-part)
  nohoward «unit (step, Even vertex of H) pairs before the first fallback: the new successor is not a ⊴-best successor BY H'S OWN
           VALUATION ..., or a best current successor was left»
  fbwrong  «unit games: the first fallback is not at T + 1»; T := the first state whose H-part has no Even vertex with a strictly
           better successor by H's own valuation (the end of the Howard run that the H-parts form)
  endwrong «unit games: fallbacks ≠ 1 or iterations ≠ T + 3» (mode spec: iterations ≠ F1 + 2, F1 the first fallback)
  wrong    «unit games: regions of W ≠ harness Zielonka on W»
Mine in addition: stratbad (unit games: harness verify.check rejects the strategies N5'-xi outputs; TARGET.md §5, D2 change 5);
  outsideA (unit (step, Even vertex of H) pairs before the first fallback: the vertex moved to a successor that is not strictly ⊴-better
  by H's own valuation; WRAP (v)'s «inside A(v)», the test that replaces nohoward in MODE=spec, where nohoward and fbwrong are not tested);
  valdiff (unit (state before the first fallback, vertex of H): val A ≠ val B; only when VALB=1); tdiff (unit games: T ≠ the length of
  MY Howard run of H from s0 under the rule «keep a best current successor, else the largest index»; a difference needs a tie event);
  ties (descriptive: tie events of my Howard run, as box 104 §5.2 counts them).
Controls: CTRL=1 («best» := worst in the Howard test; nohoward must fire), CTRL=2 (T shifted by one; fbwrong, endwrong must fire),
  CTRL=3 (the standard state is taken with σ(K0) = K1; s3fail, nonstd must fire), CTRL=4 (Zielonka is run on W with c_W's priority
  made odd; wrong must fire), CTRL=5 (every strategy entry at a vertex with two or more successors is replaced by another edge; stratbad must fire
  where a winner has a choice).
Usage: wchk44.py json RAND300.json OUT [first last] | wchk44.py fam switchall|lmcs|lmcst4 N OUT [FROZEN.pg]
  (fam: H = PGSolver's switchallexp_N with its best-reward start, or Friedmann's G_N with ι (lmcs: Figure 4's priorities; lmcst4: Table
  4's); FROZEN.pg = L-SI's frozen W to compare my build with: bytes, isomorphism with H's indices fixed, isomorphism)
  (env MODE=xi|spec, CTRL, VALB=1, ORDER as wrap44, NORUN=1: only the comparison of the build with FROZEN.pg; OUT is appended to and
  resumable: finished rows are skipped)"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE, os.path.join(R, "experiments", "n5-second"), os.path.join(R, "experiments", "hard-families"), os.path.join(R, "experiments", "harness")]
import pg, zielonka, verify
import wrap44, n5xi44, val44
from n5b import SpecSI
EVEN, ODD = 0, 1
MODE = os.environ.get("MODE", "xi"); CTRL = os.environ.get("CTRL", "0"); VALB = os.environ.get("VALB") == "1"
KEYS = ("s3fail", "nonstd", "nohoward", "fbwrong", "endwrong", "wrong", "stratbad", "outsideA", "valdiff", "tdiff")


class Checker:
    def __init__(self, h, s0, g, V):
        self.h, self.s0, self.g, self.V = h, s0, g, V
        self.siH = SpecSI(h)
        self.st = dict(c=dict.fromkeys(KEYS, 0), prev=None, prevval=None, Tstar=None, pre=0, first_info={})
    def get(self): return self.st
    def set(self, st):
        if st is not None: self.st = st
    def fail(self, k, t, info, cnt=1):
        self.st["c"][k] += cnt; self.st["first_info"].setdefault(k, (t, info))
    def std(self, s, sigma, tau):
        if None in s: return False
        sg, tu = wrap44.standard(self.h, s, self.g, self.V)
        if CTRL == "3": sg[self.V["K0"]] = self.V["K1"]
        return sg == sigma and tu == tau
    def best(self, val, v):
        ws = sorted(set(self.h.succ[v])); top = ws[0]
        for w in ws[1:]:
            c = val44.cmpval(self.h, val[w], val[top])
            if (c < 0) if CTRL == "1" else (c > 0): top = w
        return [w for w in ws if val44.cmpval(self.h, val[w], val[top]) == 0]
    def hook(self, t, sigma, tau, vs, Is, It, F):
        if F > 0: return
        h, st = self.h, self.st; st["pre"] = t
        s = wrap44.hpart(h, sigma, self.V)
        ok = self.std(s, sigma, tau)
        if t == 0 and not (ok and all(s[v] == self.s0[v] for v in range(h.n) if h.owner[v] == EVEN)): self.fail("s3fail", 0, "S3 is not the standard state of s0")
        if not ok: self.fail("nonstd", t, "state %d is not standard" % t)
        if None in s: return
        val = self.siH.evaluate(list(s))
        if VALB:
            vb, _ = val44.evaluate(h, s)
            d = sum(1 for v in range(h.n) if tuple(val[v]) != tuple(vb[v]))
            if d: self.fail("valdiff", t, "%d vertices of H" % d, d)
        if st["prev"] is not None:
            pv, pval = st["prev"], st["prevval"]
            for v in range(h.n):
                if h.owner[v] != EVEN: continue
                B = self.best(pval, v)
                if MODE == "xi" and (s[v] not in B or (pv[v] in B and s[v] != pv[v])): self.fail("nohoward", t - 1, "step %d, vertex %d: %d -> %d, best %s" % (t - 1, v, pv[v], s[v], B))
                if s[v] != pv[v] and not val44.cmpval(h, pval[s[v]], pval[pv[v]]) > 0: self.fail("outsideA", t - 1, "step %d, vertex %d: %d -> %d is not strictly better" % (t - 1, v, pv[v], s[v]))
        if st["Tstar"] is None and all(s[v] in val44.bestset(h, val, v) for v in range(h.n) if h.owner[v] == EVEN): st["Tstar"] = t
        st["prev"], st["prevval"] = s, val
    def finish(self, r):
        st, c, g = self.st, self.st["c"], self.g
        T = st["Tstar"]; Tc = (T + 1) if (CTRL == "2" and T is not None) else T
        if MODE == "xi":
            if Tc is None or r["first"] != Tc + 1: self.fail("fbwrong", -1, "first fallback at %s, T %s" % (r["first"], Tc))
            if r["F"] != 1 or Tc is None or r["Ttot"] != Tc + 3: self.fail("endwrong", -1, "fallbacks %d iterations %d T %s" % (r["F"], r["Ttot"], Tc))
        else:
            if r["F"] != 1 or r["first"] is None or r["Ttot"] != r["first"] + 2 + (1 if CTRL == "2" else 0): self.fail("endwrong", -1, "fallbacks %d iterations %d first %s" % (r["F"], r["Ttot"], r["first"]))
        gz = g
        if CTRL == "4":
            p = list(g.prio); p[self.V["cW"]] += 1; gz = pg.Game(p, g.owner, g.succ)
        if r["win"] != zielonka.solve(gz): self.fail("wrong", -1, "regions differ from Zielonka")
        strat = list(r["strat"])
        if CTRL == "5":
            for v in range(g.n):
                if strat[v] is not None and len(g.succ[v]) > 1: strat[v] = next(w for w in g.succ[v] if w != strat[v])
        if verify.check(g, r["win"], strat): self.fail("stratbad", -1, "verify.check rejects")
        states, To, ties, sw = val44.howard(self.h, self.s0)
        if MODE == "xi" and T != To: self.fail("tdiff", -1, "T %s, my Howard %d (tie events %d)" % (T, To, ties))
        return dict(T=T, Town=To, ties=ties, switches=sw, Ttot=r["Ttot"], F=r["F"], first=r["first"], W=g.n, evenwins=r["win"].count(0), use=n5xi44.usestr(r))


def check(h, s0, g, V, ck=None):
    C = Checker(h, s0, g, V)
    r = n5xi44.run(g, MODE, hook=C.hook, ck=ck, ckget=C.get, ckset=C.set)
    d = C.finish(r)
    return C.st["c"], d, C.st["first_info"]


def fmt(tag, c, d, extra=""):
    return "%s alg %s ctrl %s | %s | T %s iterations %d fallbacks %d first %s it-T %s | |W| %d Even wins %d | myHoward T %d ties %d | %s%s" % (
        tag, MODE, CTRL, " ".join("%s %d" % (k, c[k]) for k in KEYS), d["T"], d["Ttot"], d["F"], d["first"],
        (d["Ttot"] - d["T"]) if d["T"] is not None else None, d["W"], d["evenwins"], d["Town"], d["ties"], d["use"], extra)


def done(out):
    return {l.split(" alg ")[0] for l in open(out)} if os.path.exists(out) else set()


def lmcs(n, ver="fig4"):
    """Friedmann arXiv 1106.0778v2 §6.2 Table 4 with the start ι; MY transcription (as box43/lev43.lmcs, whose docstring quotes the table
    from claude/l-lit docs/lit/T66; vertices indexed by sorted name, as L-LIT's function lmcs does). ver table4: Table 4's priorities as
    printed. ver fig4 (box 104 §5.1, quoted): «the INJECTIVE priorities of the paper's Figure 4, d_i = 4i − 1, e_i = 4i, g_i = 4i + 2,
    k_i = 8n + 4i + 5, f_i = 8n + 4i + 7, h_i = 8n + 4i + 8, the others as in Table 4» (the six formulas are Table 4's minus 2).
    Returns (game, ι, names, tab): tab[v] = v's successors in the TABLE's order (used only for the vertex order ORDER=lsi)."""
    V = []; o = 0 if ver == "table4" else 2
    def add(nm, pl, pr, su): V.append((nm, pl, pr, su))
    add("t1", 0, 4 * n + 3, ["s", "r", "c"])
    for i in range(2, 2 * n + 1): add("t%d" % i, 0, 4 * n + 2 * i + 1, ["s", "r", "t%d" % (i - 1)])
    for i in range(1, 2 * n + 1): add("a%d" % i, 1, 4 * n + 2 * i + 2, ["t%d" % i])
    add("c", 0, 8 * n + 4, ["s", "r"])
    for i in range(1, n + 1):
        add("d%d" % i, 0, 4 * i + 1 - o, ["s", "e%d" % i, "r"] + ["a%d" % j for j in range(1, 2 * i + 1)])
        add("e%d" % i, 1, 4 * i + 2 - o, ["d%d" % i, "h%d" % i])
        add("g%d" % i, 0, 4 * i + 4 - o, ["f%d" % i, "k%d" % i])
        add("k%d" % i, 0, 8 * n + 4 * i + 7 - o, ["x"] + ["g%d" % j for j in range(i + 1, n + 1)])
        add("f%d" % i, 1, 8 * n + 4 * i + 9 - o, ["e%d" % i])
        add("h%d" % i, 1, 8 * n + 4 * i + 10 - o, ["k%d" % i])
    add("s", 0, 8 * n + 6, ["f%d" % j for j in range(1, n + 1)] + ["x"])
    add("r", 0, 8 * n + 8, ["g%d" % j for j in range(1, n + 1)] + ["x"])
    add("x", 1, 1, ["x"])
    V.sort(); names = [v[0] for v in V]; idx = {nm: i for i, nm in enumerate(names)}
    assert len(V) == 10 * n + 4, "Fact 6.1: 10n + 4 nodes"
    tab = [[idx[w] for w in v[3]] for v in V]
    g = pg.Game([v[2] for v in V], [v[1] for v in V], [sorted(t) for t in tab], names)
    assert g.m == (3 * n * n + 41 * n + 10) // 2, "Fact 6.1: 1.5 n^2 + 20.5 n + 5 edges"
    if ver == "fig4": assert len(set(g.prio)) == g.n and max(g.prio) == 12 * n + 8, "fig4: priorities not injective or top != 12n + 8"
    iota = {"t1": "c", "c": "r", "s": "x", "r": "x"}
    for i in range(2, 2 * n + 1): iota["t%d" % i] = "r"
    for i in range(1, n + 1): iota["g%d" % i] = "k%d" % i; iota["d%d" % i] = "r"; iota["k%d" % i] = "x"
    return g, [-1 if g.owner[v] == 1 else idx[iota[names[v]]] for v in range(g.n)], names, tab


def switchall(n):
    import pgsolver_port
    h = pg.parse(pgsolver_port.switchallexp(n)); s0 = SpecSI(h).initial_strategy_by_best_reward()
    return h, s0


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "json":
        D = json.load(open(a[1])); out = a[2]; lo = int(a[3]) if len(a) > 3 else 0; hi = int(a[4]) if len(a) > 4 else len(D["games"])
        fin = done(out)
        for i in range(lo, hi):
            tag = "WCHK44 json %s game %d" % (os.path.basename(a[1]), i)
            if tag in fin: continue
            G = D["games"][i]; h = pg.Game(G["prio"], G["owner"], G["succ"]); g, V = wrap44.wrap(h, G["s0"])
            c, d, fi = check(h, G["s0"], g, V)
            fz = "" if MODE != "xi" else " | frozen (T, iterations, |W|) %s mine %s frozendiff %d" % ((G["T"], G["iterations"], G["W"]), (d["T"], d["Ttot"], d["W"]), int((G["T"], G["iterations"], G["W"]) != (d["T"], d["Ttot"], d["W"])))
            with open(out, "a") as f: f.write(fmt(tag, c, d, " | |H| %d%s" % (h.n, fz)) + ("".join(" | FIRST %s %s" % (k, v) for k, v in fi.items())) + "\n")
    elif a[0] == "fam":
        fam, n, out = a[1], int(a[2]), a[3]; frozen = a[4] if len(a) > 4 else None
        tag = "WCHK44 fam %s n %d order %s" % (fam, n, wrap44.ORDER)
        if tag in done(out): sys.exit(0)
        tab = None
        if fam == "switchall": h, s0 = switchall(n)
        else: h, s0, _, tab = lmcs(n, "table4" if fam == "lmcst4" else "fig4")
        g, V = wrap44.wrap(h, s0, tab if wrap44.ORDER == "lsi" else None); extra = " | |H| %d m %d maxprio %d distinct priorities %d" % (h.n, h.m, max(h.prio), len(set(h.prio)))
        if frozen:
            fg = pg.read(frozen); raw = open(frozen).read() == pg.dumps(g)
            phi = wrap44.iso(g, fg, h.n); phi0 = phi if phi is not None else wrap44.iso(g, fg, 0)
            extra += " | frozen %s: bytes equal %s, isomorphic with H's indices fixed %s, isomorphic %s" % (os.path.basename(frozen), raw, phi is not None, phi0 is not None)
        if os.environ.get("NORUN") == "1":       # build comparison only
            with open(out, "a") as f: f.write("%s alg %s ctrl %s | NOT RUN (build comparison only) | |W| %d%s\n" % (tag, MODE, CTRL, g.n, extra))
            sys.exit(0)
        t0 = time.time()
        c, d, fi = check(h, s0, g, V, ck=out + ".%s_%d_%s_%s_%s.ck" % (fam, n, wrap44.ORDER.replace(":", ""), MODE, CTRL))
        with open(out, "a") as f: f.write(fmt(tag, c, d, extra) + ("".join(" | FIRST %s %s" % (k, v) for k, v in fi.items())) + "\n")
        print("%s: %.0f s" % (tag, time.time() - t0), file=sys.stderr)
