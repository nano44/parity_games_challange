#!/usr/bin/env python3
"""Box 217 (L-NEW successor 76): the one-player model 1P(G) of a Xi-acyclic genome G (docs/new/N5-QUIETKEY-box217.md §1) and three rules.
Xi_s(x, k): follow x -k-> beta(x, k) -> xt(x, k) -s-> ... to the exit; value = (signed rank-weight of the beta set, 5 * hops), larger
better (weight: +2^rank for an even priority, -2^rank for an odd one, rank = order of the beta priorities 6 + 2 br + bp; hops longer =
better, the common cycle node K1 being odd). A_s(x) = {s(x)} + strictly better options.
  key  : s' level by level from level 0; s'(x) = argmin over A_s(x) of key(x, k) = key(wt, s'(wt)) + (eps(x, k),)   (KEY-TAU (i))
         eps(x, k) = the vertex index of e_(x,k) in the game N5 runs on (R241: numbering-free form; box 189's Gamma3 numbers the
         e-vertices in gate order, so eps orders options as G["gate"] does; a renumbering is given by --numb)
  howard: s'(x) = the Xi_s-best option
  seq  : the key rule's s' applied at the least-index mover where it differs
Run stops at s' = s or when no option is strictly better anywhere. Returns the list of states.
Faithfulness check (mism): compare the key run with N5 itself on Gamma3 (box 215 keyside215.states, n5v spec) state by state.
Control ONE217_CTRL=1: the key uses a fixed random permutation of the gate numbers (seed 5): mism must fire.
Numbered instances: --numb NUMB.json (L-RED R241 format {"genome", "perm", "pseed"}): eps from L-RED kt241.renumber's permutation
  (re-implemented here, same algorithm and seed; checked by comparing the rebuilt game's text with the instance's .pg), N5 run on that game.
Usage: one217.py G.json ...        (prints T for key / howard / seq and, with --check, mism)
       one217.py --numb [--check] NUMB.json ...
       one217.py --check G.json ... | one217.py --rand SEED COUNT [--check]"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CTRL = os.environ.get("ONE217_CTRL", "0")

def acyclic(G):
    N = G["N"]; col = [0] * N
    def dfs(x):
        col[x] = 1
        for (_, y, _) in G["opts"][x]:
            if y >= 0 and (col[y] == 1 or (col[y] == 0 and not dfs(y))): return False
        col[x] = 2; return True
    return all(col[x] or dfs(x) for x in range(N))

class OneP:
    def __init__(self, G, eidx=None):
        assert acyclic(G), "Xi-graph not acyclic"
        self.G = G; N = self.N = G["N"]; self.lev = G["lev"]; self.opts = G["opts"]
        M = sum(len(o) for o in self.opts)
        pr = {b: 6 + 2 * G["br"][b] + G["bp"][b] for x in range(N) for (_, _, b) in self.opts[x]}
        order = sorted(pr, key=lambda b: (pr[b], b)); rank = {b: r for r, b in enumerate(order)}
        self.bw = {b: (1 << rank[b]) if pr[b] % 2 == 0 else -(1 << rank[b]) for b in pr}
        gate = [[eidx[(x, k)] for k in range(len(self.opts[x]))] for x in range(N)] if eidx else G["gate"]
        if CTRL == "1":
            vals = sorted(v for row in gate for v in row); perm = vals[:]; random.Random(5).shuffle(perm); mp = dict(zip(vals, perm)); gate = [[mp[gk] for gk in row] for row in gate]
        self.gate = gate
        # topological order of the Xi-DAG (targets first)
        seen = set(); self.topo = []
        def visit(x):
            if x in seen: return
            seen.add(x)
            for (_, y, _) in self.opts[x]:
                if y >= 0: visit(y)
            self.topo.append(x)
        for x in range(N): visit(x)
        self.bylev = sorted(range(N), key=lambda x: self.lev[x])

    def values(self, s):
        """Xi value of every mover (its chosen option) and of every option, as (weight, hops)"""
        mv = [None] * self.N; ov = {}
        for x in self.topo:
            for k, (_, y, b) in enumerate(self.opts[x]):
                w, h = (0, 0) if y < 0 else mv[y]
                ov[(x, k)] = (w + self.bw[b], h + 1)
            mv[x] = ov[(x, s[x])]
        return mv, ov

    def step(self, s, rule):
        _, ov = self.values(s)
        A = [[k for k in range(len(self.opts[x])) if k == s[x] or ov[(x, k)] > ov[(x, s[x])]] for x in range(self.N)]
        if all(len(a) == 1 for a in A): return None
        if rule == "howard":
            return tuple(max(A[x], key=lambda k: ov[(x, k)]) for x in range(self.N))
        new = list(s); key = {}
        for x in self.bylev:
            def kk(k):
                wt = self.opts[x][k][0]
                return (key[wt] if wt >= 0 and self.lev[x] > 0 else ()) + (self.gate[x][k],)
            new[x] = min(A[x], key=kk); key[x] = kk(new[x])
        new = tuple(new)
        if rule == "seq":
            d = [x for x in range(self.N) if new[x] != s[x]]
            if not d: return tuple(s)
            t = list(s); t[d[0]] = new[d[0]]; return tuple(t)
        return new

    def run(self, rule="key", cap=10 ** 6):
        s = tuple(self.G["start"]); S = [s]
        while len(S) <= cap:
            t = self.step(s, rule)
            if t is None or t == s: break
            s = t; S.append(s)
        return S

def n5states(G):
    sys.path.insert(0, os.path.join(ROOT, "experiments/new/box215"))
    os.environ.setdefault("KM_MODE", "spec")
    import keyside215
    return [tuple(x) for x in keyside215.states(G)]

def renumbered(G, how, seed):
    """L-RED R241 kt241.renumber, re-implemented: Gamma3(G) (box 189, all pads) with vertex indices permuted (how = e: the e-vertices
    among themselves; all: every vertex), random.Random(seed); returns (pg text, V renumbered)"""
    sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box195", "experiments/new/box189", "experiments/new/box190",
                    "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
    os.environ.setdefault("EG195_ROOT", ROOT)
    import gamma3, eg195
    g, _, _, V = gamma3.build(G, eg195.PADS); n = g.n; rr = random.Random(seed); pi = list(range(n))
    if how == "e":
        es = sorted(v for k, v in V.items() if isinstance(k, tuple) and k[0] == "e"); sh = es[:]; rr.shuffle(sh)
        for a, b in zip(es, sh): pi[a] = b
    elif how == "all": rr.shuffle(pi)
    prio = [0] * n; owner = [0] * n; succ = [None] * n
    for v in range(n): prio[pi[v]] = g.prio[v]; owner[pi[v]] = g.owner[v]; succ[pi[v]] = sorted(pi[w] for w in g.succ[v])
    txt = f"parity {n - 1};\n" + "".join(f"{v} {prio[v]} {owner[v]} {','.join(map(str, succ[v]))};\n" for v in range(n))
    return txt, {k: pi[v] for k, v in V.items()}

def n5states_pg(txt, G, V):
    """N5 (n5v spec) from S3 on the given game text; mover option per state through V (renumbered), until the first fallback"""
    import pg, n5v, n5x
    g = pg.parse(txt); E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    inv = {V[("m", (x, k))]: k for x in range(G["N"]) for k in range(len(G["opts"][x]))}
    rd = lambda s: tuple(inv.get(s[V[("x", x)]], -1) for x in range(G["N"])); S = [rd(sigma)]
    while len(S) <= 20000:
        res = n5v.step(g, E, Ed, sigma, tau, "spec")
        if res is None or res[4]: break
        sigma, tau = list(res[0]), list(res[1]); S.append(rd(sigma))
    return S

def numb(fn, check):
    import hashlib
    D = json.load(open(fn)) if isinstance(fn, str) else fn; fn = fn if isinstance(fn, str) else D["name"]; G = D["genome"]
    if not acyclic(G): return f"{os.path.basename(fn)} perm {D['perm']} {D['pseed']} SKIPPED Xi-cyclic (1P(G) is defined for Xi-acyclic G)"
    txt, V = renumbered(G, D["perm"], int(D["pseed"]))
    pgf = fn[:-5] + ".pg"; same = int(os.path.exists(pgf) and open(pgf).read() == txt)
    eidx = {(x, k): V[("e", (x, k))] for x in range(G["N"]) for k in range(len(G["opts"][x]))}
    P = OneP(G, eidx); S = P.run("key"); P0 = OneP(G)
    out = (f"{os.path.basename(fn)} perm {D['perm']} {D['pseed']} pgsame {same} N {G['N']} key {len(S) - 1} howard {len(P.run('howard')) - 1} "
           f"seq {len(P.run('seq')) - 1} key_box189 {len(P0.run('key')) - 1}")
    if check:
        R = n5states_pg(txt, G, V); out += f" n5 {len(R) - 1} mism {int(R != S)}"
    return out

def report(name, G, check):
    P = OneP(G); S = P.run("key"); out = f"{name} N {G['N']} M {sum(len(o) for o in G['opts'])} key {len(S) - 1} howard {len(P.run('howard')) - 1} seq {len(P.run('seq')) - 1}"
    if check:
        R = n5states(G); out += f" n5 {len(R) - 1} mism {int(R != S)}"
    return out

if __name__ == "__main__":
    a = sys.argv[1:]; check = "--check" in a; a = [x for x in a if x != "--check"]
    if a and a[0] == "--renum":                                  # --renum HOW SEED G.json ...: own renumberings, same check
        how, sd = a[1], int(a[2])
        for f in a[3:]:
            G = json.load(open(f)); G = G.get("genome", G)
            print(numb({"genome": G, "perm": how, "pseed": sd, "name": os.path.basename(f)}, check) + f" ctrl {CTRL}", flush=True)
    elif a and a[0] == "--numb":
        for fn in a[1:]: print(numb(fn, check) + f" ctrl {CTRL}", flush=True)
    elif a and a[0] == "--rand":
        sys.path.insert(0, os.path.join(ROOT, "experiments/new/box195")); os.environ.setdefault("EG195_ROOT", ROOT)
        import eg195
        seed, cnt = int(a[1]), int(a[2]); rng = random.Random(seed); k = 0; mism = 0; mx = [0, 0, 0]
        while k < cnt:
            G = eg195.gen(rng, "acyc")
            if G is None or G["N"] < 2: continue
            k += 1; P = OneP(G); S = P.run("key"); mx = [max(mx[0], len(S) - 1), max(mx[1], len(P.run("howard")) - 1), max(mx[2], len(P.run("seq")) - 1)]
            if check and n5states(G) != S: mism += 1
        print(f"rand acyc seed {seed} genomes {k} ctrl {CTRL} maxkey {mx[0]} maxhoward {mx[1]} maxseq {mx[2]}" + (f" mism {mism}" if check else ""), flush=True)
    else:
        for fn in a:
            G = json.load(open(fn)); G = G.get("genome", G)
            print(report(os.path.basename(fn), G, check) + f" ctrl {CTRL}", flush=True)
