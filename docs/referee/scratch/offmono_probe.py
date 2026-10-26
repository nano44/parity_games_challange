#!/usr/bin/env python3
"""REFEREE succ. 15 probe for packet P-N5-OFFMONO (docs/new/P-N5-OFFMONO-box49.md, l-new 1f816370, sha1 d9705ac6). Own engine only (rl_engine,
flip_probe helpers). No lane code. Per phase ((lambda, tau) const), per class U = U_c, Q := Odd vertices of out-degree >= 2:
 OM     Lemma OFFSET-MONO: every in-phase t -> t+1, q in Q n U, q != c, q on no honest cycle at t, p := par_{t+1}(q):
        off_{t+1}(q; p) >= off_t(q; p) in Z^2 (kappa = (signed weight, s_c * length)); counts Case L (y2's play at t passes q), parent changes
 STEP1  its Step 1 at every vertex x of q's (t+1)-path from y2 to p
 CS     Corollary CHAIN-SUM: the telescoping identity, and every term with x_i on no honest cycle at t is >= 0
 CC     Corollary CHAIN-COUNT on J := each maximal run of in-phase transitions (the whole phase), with D := the actual max number of values of
        off(x; p) over the x-pieces: #(transitions changing kappa(q)) <= |CYC_c| + sum_x D (|EXIT_x| + |CYC_c| + 1)
Mutations: MUT=1 p := par_t(q) (the old routing vertex) when it differs;  MUT=2 the opposite length sign;  MUT=3 drop "q on no honest cycle
 at t" (include q on an honest cycle at t).
Usage: offmono_probe.py rand N nmin nmax kmax seed | files[:start]...  (env RANDSTARTS 2, MAXN 64, NOS3)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, hon_probe as HP
from flip_probe import nxt, on_cycle
EX = []
MUT = int(os.environ.get("MUT", "0"))


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def kap(g, c, val):
    s = 1 if g.prio[c] % 2 else -1
    if MUT == 2: s = -s
    return (g.weight(val[1]), s * val[2])


def kwt(g, c, v):
    s = 1 if g.prio[c] % 2 else -1
    if MUT == 2: s = -s
    return ((g.weight(1 << g.rank[v]) if g.rank[v] > g.rank[c] else 0), s)


def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def add(a, b): return (a[0] + b[0], a[1] + b[1])


def par(nx, Q, q, c):
    x = nx[q]; seen = {q}
    while x != c and x not in seen:
        if x in Q: return x
        seen.add(x); x = nx[x]
    return c


def analyse(g, start, cnt, name):
    st = RE.run(g, start); n = g.n
    Q = {v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1}
    for x in st: x["nx"] = nxt(g, x["s"], x["sb"])
    K = len(st); k = 0
    while k < K:
        j = k; lam = tuple(v[0] for v in st[k]["Xi"])
        while j + 1 < K and tuple(v[0] for v in st[j + 1]["Xi"]) == lam and st[j + 1]["t"] == st[k]["t"]: j += 1
        if j > k: phase(g, st, k, j, lam, Q, cnt, name)
        k = j + 1


def phase(g, st, a, b, lam, Q, cnt, name):
    n = g.n; cnt["PHASES"] += 1
    for c in sorted(set(lam)):
        U = {v for v in range(n) if lam[v] == c}
        Qc = sorted((Q & U) - {c})
        if not Qc: continue
        K = lambda t, z: kap(g, c, st[t]["Xi"][z])
        cyc_t = {t: [x for x in Qc if on_cycle(st[t]["nx"], x)] for t in range(a, b + 1)}
        for t in range(a, b):
            nx0, nx1 = st[t]["nx"], st[t + 1]["nx"]
            for q in Qc:
                if cyc_t[t] and q in cyc_t[t] and MUT != 3: continue
                if MUT == 3 and q not in cyc_t[t]: continue
                p = par(nx1, Q, q, c)
                if MUT == 1:
                    p0 = par(nx0, Q, q, c)
                    if p0 == p: continue
                    p = p0
                o0, o1 = sub(K(t, q), K(t, p)), sub(K(t + 1, q), K(t + 1, p))
                cnt["OM_chk"] += 1
                if par(nx0, Q, q, c) != p: cnt["OM_parent_changed"] += 1
                y2 = st[t + 1]["sb"][q]; pre, cy = RE.lasso(nx0, y2)
                if q in pre or q in cy: cnt["OM_caseL"] += 1
                if o1 < o0: fail(cnt, "OM", name, t, c, q, p, o0, o1)
                # Step 1 along q's (t+1)-path from y2 to p
                if MUT == 0:
                    x = y2; guard = 0
                    while x != p and guard <= n:
                        guard += 1; cnt["STEP1_chk"] += 1
                        if sub(K(t + 1, x), K(t + 1, p)) < sub(K(t, x), K(t, p)): fail(cnt, "STEP1", name, t, c, q, x)
                        x = nx1[x]
            if MUT: continue
            # CHAIN-SUM
            for q in Qc:
                ch = [q]
                while ch[-1] != c and len(ch) <= n: ch.append(par(nx1, Q, ch[-1], c))
                tot = (0, 0); okterms = True
                for i in range(len(ch) - 1):
                    term = sub(sub(K(t + 1, ch[i]), K(t + 1, ch[i + 1])), sub(K(t, ch[i]), K(t, ch[i + 1])))
                    tot = add(tot, term)
                    if ch[i] not in cyc_t[t] and term < (0, 0): okterms = False
                cnt["CS_chk"] += 1
                if tot != sub(K(t + 1, q), K(t, q)) or not okterms: fail(cnt, "CS", name, t, c, q)
        if MUT: continue
        # CHAIN-COUNT on J = the whole phase
        CYC = {t for t in range(a, b) if cyc_t[t]}
        EXIT = {x: {t for t in range(a, b) if par(st[t]["nx"], Q, x, c) != par(st[t + 1]["nx"], Q, x, c)} for x in Qc}
        Dmax = 1
        for x in Qc:
            t = a
            while t < b:
                if t in EXIT[x] or t in CYC: t += 1; continue
                s = t
                while t < b and t not in EXIT[x] and t not in CYC: t += 1
                p = par(st[s]["nx"], Q, x, c)
                vals = {sub(K(k, x), K(k, p)) for k in range(s, t + 1)}
                Dmax = max(Dmax, len(vals))
        cnt["MAX_D"] = max(cnt["MAX_D"], Dmax)
        for q in Qc:
            chg = sum(1 for t in range(a, b) if K(t, q) != K(t + 1, q))
            bound = len(CYC) + sum(Dmax * (len(EXIT[x]) + len(CYC) + 1) for x in Qc)
            cnt["CC_chk"] += 1; cnt["MAX_KCHG"] = max(cnt["MAX_KCHG"], chg)
            if chg > bound: fail(cnt, "CC", name, a, c, q, chg, bound)


def main(a):
    cnt = Counter(); rng = random.Random(1587); nst = int(os.environ.get("RANDSTARTS", "2"))
    def do(g, name, r, extra=None):
        starts = ([extra] if extra else []) + ([] if (extra and os.environ.get("NOS3")) else [RE.best_reward_start(g)]) + \
                 [D.rand_start(g, r) for _ in range(nst)]
        for j, s0 in enumerate(starts):
            cnt["RUNS"] += 1; analyse(g, s0, cnt, "%s/%d" % (name, j))
    if a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            do(D.rand_ck(r2, nn, r2.randint(0, min(km, nn - 1))), "rand%d" % i, rng)
    else:
        for f in a:
            path, _, sp = f.partition(":")
            try: g = RE.parse(path)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "64")): cnt["skip_big"] += 1; continue
            do(g, os.path.relpath(path), random.Random(os.path.relpath(path)), HP.parse_start(g, sp) if sp else None)
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
