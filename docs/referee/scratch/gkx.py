#!/usr/bin/env python3
"""REFEREE successor 36: own tools for the first review of P-N5-EXP (l-red-b 350d84eb, sha1 c0449b17...).

Everything here is written from two texts only:
  (T1) the packet's section 3 TABLE (rule R), transcribed row by row in rule(); the lane's gk.py is NOT imported;
  (T2) P-N5-REALIZE.md section 2 (R104's definitions: genome, X-chain, B_s, the order, the IDEAL step), in step().
Subcommands (each prints one line per k with named must-0 counters; `ctrl N` rows are firing controls):
  gen   DIR k..      own rule output against the frozen files DIR/G_k.json (gendiff), wire-rank ties in the TABLE's rank key (wtie)
  member k..         R104's clauses c1..c8 on the own rule output; controls damage one clause each
  run   k..          the IDEAL run by step(): L, stop word, per-mover switch counts against Theorem EXP-IDEAL (c)
  facts k.. [--arb n seed] [--ctrl c]   K1-K3, V0-V4, K4, MOVE-2, WIRE on every run state, and on n random states
  resp  k.. [--ctrl c]  the RESPONSE LEMMA: schedule generated recursively from the lemma's text, compared step by step;
                     (H1) and (H2) tested at EVERY invocation; the «E(j) stays at a, moves at the last step» clause; REST at the end
  abs   k.. [--ctrl c]  abstract unit machine (bits + the formulas of section 5 only) driven by a FREE input stream: both a,
                     the PREFIX form (H2 only up to T), and the stop
  causal k.. [--arb n seed] [--ctrl c]   the abstract machine against the definition's step, inputs taken from the definitions
  orders k.. [--reps n] [--seed s]       section 8: random gates / ranks inside the listed constraints give the same run
  sizes DIR k..      n, m, largest priority of the frozen DIR/G_k_g3.pg; the explicit instances of the dead-end paragraph
  unit [wmax] [--ctrl c]   ONE generic unit against an abstract unit above with arbitrary delays (the induction step of LEMMA')
  closed k.. [--ctrl c]    L-SI box 108's closed form c_k(t) (own implementation from its section 3) against my run
No absolute paths. Run with python3 -I.
"""
import sys, json, random, itertools

# ---------------------------------------------------------------- (T1) the rule, from the packet's TABLE
def rule(k, wire_tie="bid"):
    assert k >= 3
    rows = []          # (name, level, (W0, W1), (X0, X1), start, (eps0, eps1), depth or None for a wire, (delta0, delta1))
    def E(j):          # END-FOLLOWER of level j: e_j for 2 <= j <= k-2, u_(k-1) for j = k-1
        return f"e{j}" if 2 <= j <= k - 2 else (f"u{j}" if j == k - 1 else None)
    rows.append(("u0", 0, (None, None), (None, None), 0, (2, 5), 0, (2, 0)))
    rows.append(("v0", 0, (None, None), (None, None), 0, (3, 1), 0, (1, 3)))
    for j in range(1, k):                                   # the pairs
        rows.append((f"u{j}", j, (f"u{j-1}", f"v{j-1}"), (f"yb{j}", f"y{j}"), 0, (2, 3), 2 * j, (1, 0)))
        rows.append((f"v{j}", j, (f"u{j-1}", f"v{j-1}"), (f"y{j}", f"yb{j}"), 0, (4, 5), 2 * j, (3, 2)))
    for j in range(2, k - 1):                               # the e's, 2 <= j <= k-2
        rows.append((f"e{j}", j, (f"u{j-1}", f"v{j-1}"), (f"ypb{j}", f"yp{j}"), 0, (0, 1), 2 * j + 1, (4, 5)))
    for j in range(1, k - 1):                               # wv_j, 1 <= j <= k-2
        rows.append((f"wv{j}", j + 1, (f"v{j}", f"v{j}"), (None, None), 0, (6, 7), None, (1, 0)))
    for j in range(2, k - 1):                               # wu_j, 2 <= j <= k-2
        rows.append((f"wu{j}", j + 1, (f"u{j}", f"u{j}"), (None, None), 0, (8, 9), None, (3, 2)))
    for j in range(1, k):                                   # the pairs Y
        if j <= k - 2:
            rows.append((f"y{j}", j + 2, (f"wv{j}", E(j + 1)), (f"u{j-1}", f"v{j-1}"), 0, (10, 11), 2 * j - 1, (1, 3)))
            rows.append((f"yb{j}", j + 2, (f"wv{j}", E(j + 1)), (f"v{j-1}", f"u{j-1}"), 1, (12, 13), 2 * j - 1, (0, 2)))
        else:
            rows.append((f"y{j}", k, (f"u{j}", f"v{j}"), (f"u{j-1}", f"v{j-1}"), 0, (20, 21), 2 * k - 3, (1, 3)))
            rows.append((f"yb{j}", k, (f"u{j}", f"v{j}"), (f"v{j-1}", f"u{j-1}"), 1, (22, 23), 2 * k - 3, (0, 2)))
    for j in range(2, k - 1):                               # the pairs Y'
        rows.append((f"yp{j}", j + 2, (f"wu{j}", E(j + 1)), (f"yb{j}", f"y{j}"), 0, (14, 15), 2 * j, (5, 7)))
        rows.append((f"ypb{j}", j + 2, (f"wu{j}", E(j + 1)), (f"y{j}", f"yb{j}"), 1, (16, 17), 2 * j, (4, 6)))
    names = [r[0] for r in rows]
    idx = {n: i for i, n in enumerate(names)}
    N = len(rows)
    opts, gnum, rkey = [], [], {}
    wtie = 0
    seen = {}
    for i, (n, lev, W, X, st, eps, dep, dl) in enumerate(rows):
        row, g = [], []
        for o in range(2):
            b = 2 * i + o
            row.append([idx[W[o]] if W[o] is not None else -1, idx[X[o]] if X[o] is not None else -1, b])
            g.append(100 * lev + eps[o])
            d = dep if dep is not None else 2 * k + 5
            key = (-d, dl[o])                               # the TABLE's rank key: (-depth, local delta)
            if key in seen:
                wtie += 1
            seen[key] = b
            rkey[b] = key
        opts.append(row)
        gnum.append(g)
    allg = sorted(x for g in gnum for x in g)
    assert len(set(allg)) == len(allg), "gate numbers not distinct"
    grk = {x: r for r, x in enumerate(allg)}
    gate = [[grk[x] for x in g] for g in gnum]
    if wire_tie == "bid":
        order = sorted(rkey, key=lambda b: (rkey[b], b))
    elif wire_tie == "rev":
        order = sorted(rkey, key=lambda b: (rkey[b], -b))
    else:
        rnd = random.Random(int(wire_tie))
        t = {b: rnd.random() for b in rkey}
        order = sorted(rkey, key=lambda b: (rkey[b], t[b]))
    br = [0] * (2 * N)
    for r, b in enumerate(order):
        br[b] = r
    G = {"N": N, "lev": [r[1] for r in rows], "deg": 2, "opts": opts, "gate": gate, "br": br, "bp": [0] * (2 * N),
         "start": [r[4] for r in rows]}
    meta = {"names": names, "idx": idx, "depth": {r[0]: r[6] for r in rows}, "wtie": wtie, "E": E, "rows": rows}
    return G, meta


# ---------------------------------------------------------------- (T2) R104's definitions
def degs(G):
    return [len(o) for o in G["opts"]]

def chain(G, s, x, k):
    """X-chain of the face (x, k): list of (mover, option); ends at the first option whose Xi-target is X."""
    out = []
    seen = set()
    while True:
        assert x not in seen, "Xi-cycle"
        seen.add(x)
        out.append((x, k))
        xt = G["opts"][x][k][1]
        if xt < 0:
            return out
        x, k = xt, s[xt]

def Bset(G, s, x, k):
    return frozenset(G["opts"][y][o][2] for (y, o) in chain(G, s, x, k))

def ahead_sets(G, A, B):
    """A is better than B: the beta of LARGEST rank in A delta B has parity 0 and lies in A, or parity 1 and lies in B."""
    D = A ^ B
    if not D:
        return False
    b = max(D, key=lambda b: G["br"][b])
    return (G["bp"][b] == 0 and b in A) or (G["bp"][b] == 1 and b in B)

def keys_of_state(G, s):
    """key_s(x) for every mover: key of x's current option, s on the lower levels."""
    key = {}
    for x in sorted(range(G["N"]), key=lambda x: G["lev"][x]):
        wt = G["opts"][x][s[x]][0]
        key[x] = (key[wt] if wt >= 0 else ()) + (G["gate"][x][s[x]],)
    return key

def step(G, s):
    """One IDEAL step. Returns (s', word): word in {"step", "opt", "stuck"}; s' is None unless word == "step"."""
    N = G["N"]
    A = []
    for x in range(N):
        cur = Bset(G, s, x, s[x])
        A.append([k for k in range(len(G["opts"][x])) if k == s[x] or ahead_sets(G, Bset(G, s, x, k), cur)])
    if all(len(a) == 1 for a in A):
        return None, "opt", A
    s2 = list(s)
    key = {}
    for x in sorted(range(N), key=lambda x: G["lev"][x]):
        def okey(k):
            wt = G["opts"][x][k][0]
            return (key[wt] if wt >= 0 else ()) + (G["gate"][x][k],)
        kk = min(A[x], key=okey)
        s2[x] = kk
        key[x] = okey(kk)
    if s2 == list(s):
        return None, "stuck", A
    return s2, "step", A

def run(G, s0=None, cap=10 ** 7):
    s = list(G["start"] if s0 is None else s0)
    S = [s]
    while True:
        s2, word, _ = step(G, s)
        if s2 is None:
            return S, word
        S.append(s2)
        s = s2
        assert len(S) <= cap


# ---------------------------------------------------------------- membership (R104 section 2 clauses)
def member(G):
    c = [0] * 9
    N = G["N"]
    lev = G["lev"]
    d = max(lev) + 1
    M = sum(len(o) for o in G["opts"])
    if set(lev) != set(range(d)) or any(len(o) < 1 for o in G["opts"]) or len(lev) != N or len(G["opts"]) != N:
        c[1] += 1
    for x in range(N):
        for (wt, xt, b) in G["opts"][x]:
            if lev[x] == 0:
                if wt != -1:
                    c[2] += 1
            elif not (0 <= wt < N and lev[wt] == lev[x] - 1):
                c[2] += 1
            if not (xt == -1 or 0 <= xt < N):
                c[3] += 1
    bids = [b for o in G["opts"] for (_, _, b) in o]
    if sorted(bids) != list(range(M)):
        c[4] += 1
    gs = [g for row in G["gate"] for g in row]
    if sorted(gs) != list(range(M)) or [len(r) for r in G["gate"]] != [len(o) for o in G["opts"]]:
        c[5] += 1
    if sorted(G["br"]) != list(range(M)) or any(p not in (0, 1) for p in G["bp"]) or len(G["bp"]) != M:
        c[6] += 1
    if len(G["start"]) != N or any(not (0 <= G["start"][x] < len(G["opts"][x])) for x in range(N)):
        c[7] += 1
    # acyclic Xi-graph, self-loops count
    adj = {x: set(xt for (_, xt, _) in G["opts"][x] if 0 <= xt < N) for x in range(N)}
    col = {}
    cyc = 0
    for r in range(N):
        if r in col:
            continue
        st = [(r, iter(adj[r]))]
        col[r] = 1
        while st:
            v, it = st[-1]
            for w in it:
                if col.get(w) == 1:
                    cyc = 1
                elif w not in col:
                    col[w] = 1
                    st.append((w, iter(adj[w])))
                    break
            else:
                col[v] = 2
                st.pop()
    c[8] = cyc
    return c[1:]


# ---------------------------------------------------------------- the packet's formulas (section 5), bits only
class Bits:
    """The orders C, D, Z, E, EY, EY' as the packet's K1-K3 / V1-V3 state them, computed from the option bits alone."""
    def __init__(self, k, meta, s, ctrl=0):
        self.k = k
        ix = meta["idx"]
        g = lambda n: s[ix[n]]
        self.s = s
        self.g = g
        Efn = meta["E"]
        C = {0: g("v0")}                       # K1 at level 0 (needs s(u0) = 0)
        E = {0: g("v0")}                       # V1 at level 0 (needs s(u0) = 0)
        EY, EYp, D, Z = {}, {}, {}, {}
        for j in range(1, k):
            u, v = g(f"u{j}"), g(f"v{j}")
            y, yb = g(f"y{j}"), g(f"yb{j}")
            # V2
            if y != yb:
                EY[j] = yb
            else:
                EY[j] = int(y != E[j - 1])
            if ctrl == 3:                      # control: V2's aligned case read the other way
                if y == yb:
                    EY[j] = int(y == E[j - 1])
            # V1
            if u != v:
                E[j] = 1
            else:
                E[j] = int(EY[j] == v)
            if ctrl == 4 and u != v:           # control: V1 split case 0
                E[j] = 0
            # K1
            if u != v:
                C[j] = int(v == C[j - 1])
            else:
                C[j] = 0
            if ctrl == 1 and u == v:           # control: K1 aligned case 1
                C[j] = 1
            # V3
            if 2 <= j <= k - 2:
                yp, ypb = g(f"yp{j}"), g(f"ypb{j}")
                if yp != ypb:
                    EYp[j] = ypb
                else:
                    EYp[j] = int((1 - yp) != EY[j])
                if ctrl == 5 and yp == ypb:    # control: V3 aligned case read the other way
                    EYp[j] = int((1 - yp) == EY[j])
        for j in range(1, k - 1):              # K2, 1 <= j <= k-2
            e = g(Efn(j + 1))
            D[j] = int(e == 1 or C[j] == 0)
            if ctrl == 2:                      # control (the packet's): «and» for «or»
                D[j] = int(e == 1 and C[j] == 0)
        for j in range(2, k - 1):              # K3, 2 <= j <= k-2
            e = g(Efn(j + 1))
            Z[j] = int(e == 0 or C[j] == 1)
            if ctrl == 6:
                Z[j] = int(e == 0 and C[j] == 1)
        self.C, self.E, self.EY, self.EYp, self.D, self.Z = C, E, EY, EYp, D, Z

def value_enabled_formula(k, meta, B, ctrl=0):
    """V4, per mover name -> bool, from the bits B (computed under s)."""
    g = B.g
    out = {}
    out["u0"] = False if g("u0") == 0 else None       # None: the packet states nothing (u0 at 1 is outside its standing assumption)
    out["v0"] = (g("v0") == 0)
    for j in range(1, k):
        out[f"v{j}"] = (B.EY[j] == 1 - g(f"v{j}"))
        out[f"u{j}"] = (B.EY[j] == g(f"u{j}"))
        if ctrl == 7:                                   # control: u's rule read as v's
            out[f"u{j}"] = (B.EY[j] == 1 - g(f"u{j}"))
        y, yb = g(f"y{j}"), g(f"yb{j}")
        out[f"y{j}"] = (B.E[j - 1] == 1) if y == 0 else (B.E[j - 1] == 0)
        out[f"yb{j}"] = (B.E[j - 1] == 0) if yb == 0 else (B.E[j - 1] == 1)
        if 2 <= j <= k - 2:
            out[f"e{j}"] = (B.EYp[j] == g(f"e{j}"))
            yp, ypb = g(f"yp{j}"), g(f"ypb{j}")
            out[f"yp{j}"] = (B.EY[j] == 0) if yp == 0 else (B.EY[j] == 1)
            out[f"ypb{j}"] = (B.EY[j] == 1) if ypb == 0 else (B.EY[j] == 0)
    return out

def key_enabled_formula(k, meta, s, B2, ctrl=0):
    """K4, per mover name -> bool: option of x under s, the orders C, D, Z under s' (B2)."""
    ix = meta["idx"]
    g = lambda n: s[ix[n]]
    out = {}
    for j in range(1, k):
        for n in (f"u{j}", f"v{j}") + ((f"e{j}",) if 2 <= j <= k - 2 else ()):
            out[n] = (g(n) != B2.C[j - 1])
        if j <= k - 2:
            for n in (f"y{j}", f"yb{j}"):
                out[n] = (B2.D[j] == 1) if g(n) == 0 else (B2.D[j] == 0)
        else:
            for n in (f"y{j}", f"yb{j}"):
                out[n] = (B2.C[j] == 1) if g(n) == 0 else (B2.C[j] == 0)
        if 2 <= j <= k - 2:
            for n in (f"yp{j}", f"ypb{j}"):
                out[n] = (B2.Z[j] == 1) if g(n) == 0 else (B2.Z[j] == 0)
                if ctrl == 8:
                    out[n] = (B2.Z[j] == 0) if g(n) == 0 else (B2.Z[j] == 1)
    return out


# ---------------------------------------------------------------- facts: definitions against formulas on one state
def facts_on_state(k, G, meta, s, cnt, ctrl=0, do_step=True):
    ix = meta["idx"]
    names = meta["names"]
    dep = meta["depth"]
    N = G["N"]
    keyS = keys_of_state(G, s)
    kahead = lambda p, q: keyS[ix[p]] < keyS[ix[q]]
    Bs = {x: Bset(G, s, x, s[x]) for x in range(N)}
    vahead = lambda p, q: ahead_sets(G, Bs[ix[p]], Bs[ix[q]])
    B = Bits(k, meta, s, ctrl)
    Efn = meta["E"]
    # K1 (C_j), incl. level 0
    cnt["K1n"] += k
    cnt["K1"] += int(kahead("v0", "u0") != bool(B.C[0]))
    for j in range(1, k):
        cnt["K1"] += int(kahead(f"v{j}", f"u{j}") != bool(B.C[j]))
    # K2, K3
    for j in range(1, k - 1):
        cnt["K2n"] += 1
        cnt["K2"] += int(kahead(Efn(j + 1), f"wv{j}") != bool(B.D[j]))
    for j in range(2, k - 1):
        cnt["K3n"] += 1
        cnt["K3"] += int(kahead(Efn(j + 1), f"wu{j}") != bool(B.Z[j]))
    # V1 (E_j incl. level 0), V2, V3
    cnt["V1n"] += k
    cnt["V1"] += int(vahead("v0", "u0") != bool(B.E[0]))
    for j in range(1, k):
        cnt["V1"] += int(vahead(f"v{j}", f"u{j}") != bool(B.E[j]))
        cnt["V2n"] += 1
        cnt["V2"] += int(vahead(f"yb{j}", f"y{j}") != bool(B.EY[j]))
        if 2 <= j <= k - 2:
            cnt["V3n"] += 1
            cnt["V3"] += int(vahead(f"ypb{j}", f"yp{j}") != bool(B.EYp[j]))
    # V0: every pair of faces of non-wire movers of ONE depth with different chains
    bydep = {}
    for n in names:
        if dep[n] is not None:
            bydep.setdefault(dep[n], []).append(n)
    brk = G["br"]
    for D_, ms in bydep.items():
        faces = [(n, o) for n in ms for o in (0, 1)]
        chs = {f: chain(G, s, ix[f[0]], f[1]) for f in faces}
        for f in faces:
            ch = chs[f]
            # exactly one option at each depth D, D-1, .., 0
            cnt["V0shape"] += int([dep[names[x]] for (x, _) in ch] != list(range(D_, -1, -1)))
        for f1, f2 in itertools.combinations(faces, 2):
            c1, c2 = chs[f1], chs[f2]
            if c1 == c2:
                continue
            cnt["V0n"] += 1
            # least depth with different options (chains are listed from depth D down to 0: position i has depth D - i)
            dstar = None
            scan = range(0, D_ + 1) if ctrl != 9 else range(D_, -1, -1)      # control 9: the LARGEST differing depth
            for depth in scan:
                pos = D_ - depth
                if c1[pos] != c2[pos]:
                    dstar = depth
                    break
            pos = D_ - dstar
            (x1, o1), (x2, o2) = c1[pos], c2[pos]
            pred = brk[G["opts"][x1][o1][2]] > brk[G["opts"][x2][o2][2]]
            real = ahead_sets(G, frozenset(G["opts"][x][o][2] for (x, o) in c1), frozenset(G["opts"][x][o][2] for (x, o) in c2))
            cnt["V0"] += int(pred != real)
            # below d* the chains coincide; and coincidence at one mover propagates down
            if ctrl != 9:
                cnt["V0"] += int(c1[pos + 1:] != c2[pos + 1:])
            # «iff the local delta of (x, i) is the larger»
            d1 = [r for r in meta["rows"] if r[0] == names[x1]][0][7][o1]
            d2 = [r for r in meta["rows"] if r[0] == names[x2]][0][7][o2]
            cnt["V0"] += int((d1 > d2) != pred)
    # V4: value-enabled by the definition against the formula
    vf = value_enabled_formula(k, meta, B, ctrl)
    ven = {}
    for n in names:
        x = ix[n]
        o = s[x]
        ven[n] = ahead_sets(G, Bset(G, s, x, 1 - o), Bs[x])
        if n in vf and vf[n] is not None:
            cnt["V4n"] += 1
            cnt["V4"] += int(vf[n] != ven[n])
    if not do_step:
        return
    # the step: K4, MOVE-2, WIRE's static part
    s2, word, A = step(G, s)
    if word == "opt":
        cnt["optstates"] += 1
        return
    if s2 is None:
        s2 = list(s)            # «stuck»: s' = s (the definition computes s' and finds it equal)
    # keys of the two options of x with s' on the lower levels (the definition)
    key2 = keys_of_state(G, s2)
    B2 = Bits(k, meta, s2, ctrl)
    kf = key_enabled_formula(k, meta, s, B2, ctrl)
    for n in names:
        x = ix[n]
        o = s[x]
        def okey(kk):
            wt = G["opts"][x][kk][0]
            return (key2[wt] if wt >= 0 else ()) + (G["gate"][x][kk],)
        ken = okey(1 - o) < okey(o)
        # MOVE-2: s'(x) = o' iff (a) and (b)
        cnt["M2n"] += 1
        if ctrl == 10:                        # control 10: MOVE-2 without clause (b)
            cnt["M2"] += int((s2[x] != o) != ven[n])
        else:
            cnt["M2"] += int((s2[x] != o) != (ven[n] and ken))
        # MOVE-2's second sentence: W-targets differ -> wt(x, o') key-ahead of wt(x, o) under s'; equal -> gates
        w0, w1 = G["opts"][x][o][0], G["opts"][x][1 - o][0]
        if w0 >= 0:
            if w0 != w1:
                cnt["M2"] += int(ken != (key2[w1] < key2[w0]))
            else:
                cnt["M2"] += int(ken != (G["gate"][x][1 - o] < G["gate"][x][o]))
        if n in kf:
            cnt["K4n"] += 1
            cnt["K4"] += int(kf[n] != ken)
        if n.startswith("w") or n == "u0":
            # WIRE (static part): at option 0 never key-enabled; (the packet's reason: gate order)
            if o == 0 or ctrl == 11:           # control 11: the same claimed at option 1 (false: it returns to 0)
                cnt["WIREn"] += 1
                cnt["WIRE"] += int(ken) + int(s2[x] != o)


def new_counters():
    return {c: 0 for c in ("K1", "K1n", "K2", "K2n", "K3", "K3n", "V0", "V0n", "V0shape", "V1", "V1n", "V2", "V2n", "V3", "V3n",
                           "V4", "V4n", "K4", "K4n", "M2", "M2n", "WIRE", "WIREn", "optstates")}

def fmt(cnt):
    order = ("K1", "K2", "K3", "V0", "V0shape", "V1", "V2", "V3", "V4", "K4", "M2", "WIRE")
    tot = {"K1": "K1n", "K2": "K2n", "K3": "K3n", "V0": "V0n", "V1": "V1n", "V2": "V2n", "V3": "V3n", "V4": "V4n", "K4": "K4n",
           "M2": "M2n", "WIRE": "WIREn"}
    return " ".join(f"{c} {cnt[c]}" + (f"/{cnt[tot[c]]}" if c in tot else "") for c in order) + f" optstates {cnt['optstates']}"


# ---------------------------------------------------------------- the RESPONSE LEMMA's schedule, from its text
def P(k, j):
    return 3 if j == k - 1 else 2 * P(k, j + 1) + 1

def response(k, meta, j, a, t, sched, calls, swapFB=False):
    """Append to sched[step] the moves (name, new option) of the response of unit j from REST_j(a), first step t.
    Returns the last step. calls collects (j, a, t, last) for the hypothesis tests."""
    c = 1 - a
    # F: the observer of Y_j on forward under REST_j(a): (y, yb) = (a, 1-a); forward = option 1
    F, Bk = (f"yb{j}", f"y{j}") if a == 0 else (f"y{j}", f"yb{j}")
    Fp, Bp = (f"ypb{j}", f"yp{j}") if a == 0 else (f"yp{j}", f"ypb{j}")
    if swapFB:
        F, Bk = Bk, F
        Fp, Bp = Bp, Fp
    add = lambda st, n, o: sched.setdefault(st, []).append((n, o))
    if j == k - 1:
        add(t, f"v{j}", c)
        add(t + 1, Bk, 1)
        add(t + 2, f"u{j}", c)
        add(t + 2, F, 0)
        last = t + 2
    else:
        add(t, f"v{j}", c)
        l1 = response(k, meta, j + 1, 0, t, sched, calls, swapFB)
        add(t + 1, F, 0)
        t1 = t + P(k, j + 1) - 1
        assert l1 == t1
        add(t1, Bk, 1)
        add(t1 + 1, f"u{j}", c)
        if j >= 2:
            add(t1 + 1, Fp, 0)
        l2 = response(k, meta, j + 1, 1, t1 + 1, sched, calls, swapFB)
        t2 = t1 + P(k, j + 1)
        assert l2 == t2
        if j >= 2:
            add(t2, Bp, 1)
            add(t2 + 1, f"e{j}", c)
            last = t2 + 1
            assert last == t + P(k, j) - 1
        else:
            last = t2
            assert last == t + P(k, j) - 2
    calls.append((j, a, t, last))
    return last

def rest(k, meta, s, j, a):
    ix = meta["idx"]
    g = lambda n: s[ix[n]]
    ok = g(f"u{j}") == a and g(f"v{j}") == a and (g(f"y{j}"), g(f"yb{j}")) == (a, 1 - a)
    if 2 <= j <= k - 2:
        ok = ok and g(f"e{j}") == a and (g(f"yp{j}"), g(f"ypb{j}")) == (a, 1 - a)
    return ok


def cmd_gen(args):
    d = args[0]
    for k in map(int, args[1:]):
        G, meta = rule(k)
        F = json.load(open(f"{d}/G_{k}.json"))
        gendiff = int(G != F)
        # the same with the other tie orders of the wire ranks: is the genome different, is the run different?
        G2, _ = rule(k, "rev")
        S1, w1 = run(G)
        S2, w2 = run(G2)
        print(f"gen k {k} N {G['N']} M {2 * G['N']} gendiff {gendiff} wtie {meta['wtie']} revtie_genome_differs {int(G2 != G)} "
              f"revtie_run_differs {int(S1 != S2 or w1 != w2)}", flush=True)

def cmd_member(args):
    for k in map(int, args):
        G, meta = rule(k)
        c = member(G)
        N = G["N"]
        lev = G["lev"]
        width = max(lev.count(l) for l in set(lev))
        MX = sum(1 for o in G["opts"] for (_, xt, _) in o if xt >= 0)
        print(f"member k {k} ctrl 0 viol {sum(c)} " + " ".join(f"c{i + 1} {v}" for i, v in enumerate(c)) +
              f" N {N} Nform {int(N != 9 * k - 16)} M {2 * N} d {max(lev) + 1} dform {int(max(lev) + 1 != k + 1)} width {width} "
              f"MX {MX} MXform {int(MX != 14 * k - 26)} alldeg2 {int(all(len(o) == 2 for o in G['opts']))}", flush=True)
    # controls on G_5: one clause damaged each
    k = 5
    def dmg(i):
        G, meta = rule(k)
        ix = meta["idx"]
        if i == 1:
            G["lev"] = [l + 1 if l >= 3 else l for l in G["lev"]]          # a skipped level
        if i == 2:
            G["opts"][ix["u2"]][0][0] = ix["v2"]                           # W-target of the same level
        if i == 3:
            G["opts"][ix["u2"]][0][1] = G["N"] + 3                         # Xi-target no mover
        if i == 4:
            G["opts"][ix["u2"]][0][2] = G["opts"][ix["u2"]][1][2]          # repeated beta-id
        if i == 5:
            G["gate"][ix["u2"]][0] = G["gate"][ix["u2"]][1]                # repeated gate
        if i == 6:
            G["bp"][3] = 2                                                 # parity 2
        if i == 7:
            G["start"][ix["u2"]] = 2                                       # start no option
        if i == 8:
            G["opts"][ix["u2"]][0][1] = ix["u2"]                           # Xi self-loop
        if i == 9:
            G["opts"][ix["y1"]][0][1] = ix["u2"]                           # a Xi-cycle of length > 1 (u2 -> yb2/y2 ... ; y1 -> u2 -> y2? )
            G["opts"][ix["u1"]][0][1] = ix["y2"]                           # u1 -> y2 -> u1: a 2-cycle
            G["opts"][ix["y2"]][0][1] = ix["u1"]
        return G
    for i in range(1, 10):
        c = member(dmg(i))
        print(f"member k {k} ctrl {i} viol {sum(c)} " + " ".join(f"c{j + 1} {v}" for j, v in enumerate(c)), flush=True)

def cmd_run(args):
    for k in map(int, args):
        G, meta = rule(k)
        S, word = run(G)
        L = len(S) - 1
        sw = [sum(1 for a, b in zip(S, S[1:]) if a[x] != b[x]) for x in range(G["N"])]
        bad = 0
        for n, x in meta["idx"].items():
            if n == "v0":
                want = 1
            elif n == "u0" or n.startswith("w"):
                want = 0
            else:
                j = int("".join(ch for ch in n if ch.isdigit()))
                want = 2 ** (j - 1)
            bad += int(sw[x] != want)
        tot = sum(sw)
        nochange = sum(1 for a, b in zip(S, S[1:]) if a == b)
        print(f"run k {k} L {L} Lform {int(L != 2 ** k - 2)} stop {word} stopform {int(word != 'stuck')} swk {bad} maxsw {max(sw)} "
              f"maxform {int(max(sw) != 2 ** (k - 2))} sumsw {tot} sumform {int(tot != 11 * 2 ** (k - 2) - 9)} nochange {nochange}", flush=True)

def take(args, flag, n=1, default=None):
    if flag in args:
        i = args.index(flag)
        v = args[i + 1:i + 1 + n]
        del args[i:i + 1 + n]
        return v if n > 1 else v[0]
    return default

def cmd_facts(args):
    arb = take(args, "--arb", 2)
    ctrl = int(take(args, "--ctrl", 1, 0))
    mode = take(args, "--mode", 1, "w0u0")     # w0u0: wires and u0 at 0; w0: wires at 0, u0 free; u0: u0 at 0, wires free; free: all free
    allm = take(args, "--all", 1)              # EVERY state with the wires and u0 at 0 (w0u0), or with u0 at 0 only (u0)
    for k in map(int, args):
        G, meta = rule(k)
        ix = meta["idx"]
        cnt = new_counters()
        if allm is not None:
            fixed = [x for nm, x in ix.items() if nm == "u0" or (nm.startswith("w") and allm == "w0u0")]
            free = [x for x in range(G["N"]) if x not in fixed]
            n = 0
            for bits in itertools.product((0, 1), repeat=len(free)):
                s = [0] * G["N"]
                for x, b in zip(free, bits):
                    s[x] = b
                facts_on_state(k, G, meta, s, cnt, ctrl)
                n += 1
            print(f"facts k {k} ctrl {ctrl} set ALL states mode {allm} states {n} " + fmt(cnt), flush=True)
            continue
        if arb is None:
            S, word = run(G)
            for s in S:
                facts_on_state(k, G, meta, s, cnt, ctrl)
            print(f"facts k {k} ctrl {ctrl} set run states {len(S)} " + fmt(cnt), flush=True)
        else:
            n, seed = int(arb[0]), int(arb[1])
            rnd = random.Random(seed * 1000 + k)
            for _ in range(n):
                s = [rnd.randrange(2) for _ in range(G["N"])]
                for nm, x in ix.items():
                    if nm.startswith("w") and mode in ("w0u0", "w0"):
                        s[x] = 0
                    if nm == "u0" and mode in ("w0u0", "u0"):
                        s[x] = 0
                facts_on_state(k, G, meta, s, cnt, ctrl)
            print(f"facts k {k} ctrl {ctrl} set arb mode {mode} states {n} seed {seed} " + fmt(cnt), flush=True)

def cmd_resp(args):
    ctrl = int(take(args, "--ctrl", 1, 0))
    for k in map(int, args):
        G, meta = rule(k)
        ix = meta["idx"]
        names = meta["names"]
        S, word = run(G)
        L = len(S) - 1
        sched, calls = {}, []
        last = response(k, meta, 1, 0, 1, sched, calls, swapFB=(ctrl == 1))
        sched.setdefault(1, []).append(("v0", 1))            # WIRE: v0 moves at step 1
        schedbad = 0
        for t in range(1, L + 1):
            real = sorted((names[x], S[t][x]) for x in range(G["N"]) if S[t][x] != S[t - 1][x])
            schedbad += int(real != sorted(sched.get(t, [])))
        schedbad += sum(1 for t in sched if t > L or t < 1)
        tlen = int(L != 2 ** k - 2 or last != L)
        # hypotheses and conclusions at every invocation
        h1 = h2 = econ = restend = empty = 0
        for (j, a, t, lst) in calls:
            c = 1 - a
            B0 = Bits(k, meta, S[t - 1])
            if ctrl == 2:
                h1 += int(not rest(k, meta, S[t - 1], j, c))                           # control: wrong rest value
            else:
                h1 += int(not rest(k, meta, S[t - 1], j, a))
            h1 += sum(int(not rest(k, meta, S[t - 1], i, 0)) for i in range(j + 1, k))
            h1 += int((B0.C[j - 1], B0.E[j - 1]) != (a, a))
            hi = t + P(k, j) - 1
            for tau in range(t, min(hi, L) + 1):
                Bt = Bits(k, meta, S[tau])
                want = (c, c) if ctrl != 3 else (a, a)                                 # control: the input read as unchanged
                h2 += int((Bt.C[j - 1], Bt.E[j - 1]) != want)
            # every step from t to the last changes some mover
            for tau in range(t, lst + 1):
                empty += int(S[tau] == S[tau - 1])
            # for j >= 2: s_tau(E(j)) = a for tau < t + P_j - 1 and E(j) moves to c at step t + P_j - 1
            if j >= 2:
                e = ix[meta["E"](j)]
                for tau in range(t - 1, t + P(k, j) - 1):
                    econ += int(S[tau][e] != a)
                econ += int(S[t + P(k, j) - 1][e] != c)
            # under the last state REST_j(c) and REST_i(0) above
            restend += int(not rest(k, meta, S[lst], j, c)) + sum(int(not rest(k, meta, S[lst], i, 0)) for i in range(j + 1, k))
        # the final state and the stop
        fin = int(not rest(k, meta, S[L], 1, 1)) + sum(int(not rest(k, meta, S[L], i, 0)) for i in range(2, k))
        _, w, A = step(G, S[L])
        stuck = int(w != "stuck" or len(A[ix["v1"]]) != 2)
        # E-1's instance: (H1) for (j, a) = (1, 1) holds under the FINAL state (t - 1 = L), where (H2) is vacuous
        BL = Bits(k, meta, S[L])
        e1inst = int(rest(k, meta, S[L], 1, 1) and all(rest(k, meta, S[L], i, 0) for i in range(2, k))
                     and (BL.C[0], BL.E[0]) == (1, 1) and w == "stuck")
        # E-5's instance: under s_0 unit 1 is at rest 0 with input (0, 0) under s_0, and v_1 moves in step 1
        B0 = Bits(k, meta, S[0])
        e5inst = int(rest(k, meta, S[0], 1, 0) and (B0.C[0], B0.E[0]) == (0, 0) and S[1][ix["v1"]] != S[0][ix["v1"]])
        print(f"resp k {k} ctrl {ctrl} L {L} calls {len(calls)} sched {schedbad} tlen {tlen} h1 {h1} h2 {h2} empty {empty} econ {econ} "
              f"restend {restend} fin {fin} stuck {stuck} e1inst {e1inst} e5inst {e5inst}", flush=True)


# ---------------------------------------------------------------- abstract unit machine with a free input stream
def abs_names(k, j0):
    ns = []
    for j in range(j0, k):
        ns += [f"u{j}", f"v{j}", f"y{j}", f"yb{j}"]
        if 2 <= j <= k - 2:
            ns += [f"e{j}", f"yp{j}", f"ypb{j}"]
    return ns

def abs_step(k, j0, st, cin_new, ein_old, ein_new_unused=None):
    """One step of the units j0..k-1 as bits, by the packet's K1-K4 / V1-V4 only.
    st: dict name -> option (old state). cin_new: C_(j0-1) under the NEW state (key input); ein_old: E_(j0-1) under the OLD
    state (value input). Returns the new dict. Level by level: unit j's pair/e (level j), then observers (level j+2) read
    D_j, Z_j under the new state, i.e. need the new E(j+1) (level j+1): so process levels in increasing order."""
    Efn = lambda j: f"e{j}" if 2 <= j <= k - 2 else f"u{j}"
    # old value orders
    E = {j0 - 1: ein_old}
    EY, EYp = {}, {}
    for j in range(j0, k):
        y, yb = st[f"y{j}"], st[f"yb{j}"]
        EY[j] = yb if y != yb else int(y != E[j - 1])
        u, v = st[f"u{j}"], st[f"v{j}"]
        E[j] = 1 if u != v else int(EY[j] == v)
        if 2 <= j <= k - 2:
            yp, ypb = st[f"yp{j}"], st[f"ypb{j}"]
            EYp[j] = ypb if yp != ypb else int((1 - yp) != EY[j])
    new = dict(st)
    C = {j0 - 1: cin_new}
    # levels: pair/e of unit j at level j; observers of Y_j, Y'_j at level j+2 (top Y_(k-1) at level k)
    for lev in range(j0, k + 1):
        j = lev
        if j <= k - 1:
            for n in (f"u{j}", f"v{j}") + ((f"e{j}",) if 2 <= j <= k - 2 else ()):
                o = st[n]
                if n[0] == "v":
                    ven = EY[j] == 1 - o
                elif n[0] == "u":
                    ven = EY[j] == o
                else:
                    ven = EYp[j] == o
                ken = o != C[j - 1]
                if ven and ken:
                    new[n] = 1 - o
            u, v = new[f"u{j}"], new[f"v{j}"]
            C[j] = int(v == C[j - 1]) if u != v else 0
        # observers at this level: Y_i with i + 2 == lev (i <= k-2), or i = k-1 if lev == k
        obs = []
        i = lev - 2
        if j0 <= i <= k - 2:
            obs.append(i)
        if lev == k:
            obs.append(k - 1)
        for i in obs:
            if i <= k - 2:
                e = new[Efn(i + 1)]
                Dk = int(e == 1 or C[i] == 0)
                Zk = int(e == 0 or C[i] == 1)
            else:
                Dk = C[i]
                Zk = None
            for n in (f"y{i}", f"yb{i}"):
                o = st[n]
                if n.startswith("yb"):
                    ven = (E[i - 1] == 0) if o == 0 else (E[i - 1] == 1)
                else:
                    ven = (E[i - 1] == 1) if o == 0 else (E[i - 1] == 0)
                ken = (Dk == 1) if o == 0 else (Dk == 0)
                if ven and ken:
                    new[n] = 1 - o
            if 2 <= i <= k - 2:
                for n in (f"yp{i}", f"ypb{i}"):
                    o = st[n]
                    if n.startswith("ypb"):
                        ven = (EY[i] == 1) if o == 0 else (EY[i] == 0)
                    else:
                        ven = (EY[i] == 0) if o == 0 else (EY[i] == 1)
                    ken = (Zk == 1) if o == 0 else (Zk == 0)
                    if ven and ken:
                        new[n] = 1 - o
    return new

def abs_rest(k, j0, a):
    st = {}
    for j in range(j0, k):
        b = a if j == j0 else 0
        st[f"u{j}"] = st[f"v{j}"] = b
        st[f"y{j}"], st[f"yb{j}"] = b, 1 - b
        if 2 <= j <= k - 2:
            st[f"e{j}"] = b
            st[f"yp{j}"], st[f"ypb{j}"] = b, 1 - b
    return st

def cmd_abs(args):
    """For every bottom unit j0 and both a: (1) the response with the input held at (c, c): moves equal the schedule, last
    state REST_j0(c), REST_i(0); then STABLE: no move while the input stays (c, c).
    (2) PREFIX: the input is (c, c) only for t <= tau <= T (key input C at tau <= T, value input E at tau <= T - 1), then
    arbitrary bits: the moves of the steps t..T equal the schedule's, for every T and many random tails."""
    ctrl = int(take(args, "--ctrl", 1, 0))
    for k in map(int, args):
        full = pref = stable = prefn = 0
        rnd = random.Random(77 + k)
        for j0 in range(1, k):
            for a in (0, 1):
                c = 1 - a
                sched, calls = {}, []
                last = response(k, None, j0, a, 1, sched, calls, swapFB=(ctrl == 1))
                st = abs_rest(k, j0, a)
                # (1) full response; old value input at step 1 is a (H1), then c
                states = [st]
                for t in range(1, last + 1):
                    ein_old = a if t == 1 else c
                    nw = abs_step(k, j0, states[-1], c, ein_old)
                    real = sorted((n, nw[n]) for n in nw if nw[n] != states[-1][n])
                    full += int(real != sorted(sched.get(t, [])))
                    states.append(nw)
                want = abs_rest(k, j0, c)
                full += int(states[-1] != want)
                for _ in range(5):                      # STABLE under the unchanged input
                    nw = abs_step(k, j0, states[-1], c, c)
                    stable += int(nw != states[-1])
                # (2) PREFIX: the input is held only up to T; the steps 1..T are compared (the machine is causal, so this is
                # the full run cut at T; the control breaks the key input AT step T and must change step T somewhere)
                Ts = range(1, last + 1) if last <= 40 else sorted(set(rnd.randrange(1, last + 1) for _ in range(40)))
                for T in Ts:
                    s = abs_rest(k, j0, a)
                    for t in range(1, T + 1):
                        ein_old = a if t == 1 else c
                        cin = a if (ctrl == 2 and t == T) else c
                        nw = abs_step(k, j0, s, cin, ein_old)
                        real = sorted((n, nw[n]) for n in nw if nw[n] != s[n])
                        prefn += 1
                        pref += int(real != sorted(sched.get(t, [])))
                        s = nw
        print(f"abs k {k} ctrl {ctrl} full {full} stable {stable} pref {pref}/{prefn}", flush=True)


# ---------------------------------------------------------------- ONE unit against an abstract environment (all delays)
def unit_step(kind, st, cin_new, ein_old, eup_new):
    """One step of ONE unit j by the formulas of section 5 (K1-K4, V1-V4). kind: "mid" (u, v, e, y, yb, yp, ypb) or "bot" (unit 1:
    u, v, y, yb). Inputs: cin_new = C_(j-1) under the new state, ein_old = E_(j-1) under the old state, eup_new = the option of
    E(j + 1) under the new state. Returns (new state, C_j under the new state)."""
    u, v, y, yb = st["u"], st["v"], st["y"], st["yb"]
    EY = yb if y != yb else int(y != ein_old)
    new = dict(st)
    if EY == 1 - v and v != cin_new:
        new["v"] = 1 - v
    if EY == u and u != cin_new:
        new["u"] = 1 - u
    if kind == "mid":
        yp, ypb, e = st["yp"], st["ypb"], st["e"]
        EYp = ypb if yp != ypb else int((1 - yp) != EY)
        if EYp == e and e != cin_new:
            new["e"] = 1 - e
    C = int(new["v"] == cin_new) if new["u"] != new["v"] else 0
    D = int(eup_new == 1 or C == 0)
    Z = int(eup_new == 0 or C == 1)
    if ((ein_old == 1) if y == 0 else (ein_old == 0)) and ((D == 1) if y == 0 else (D == 0)):
        new["y"] = 1 - y
    if ((ein_old == 0) if yb == 0 else (ein_old == 1)) and ((D == 1) if yb == 0 else (D == 0)):
        new["yb"] = 1 - yb
    if kind == "mid":
        if ((EY == 0) if yp == 0 else (EY == 1)) and ((Z == 1) if yp == 0 else (Z == 0)):
            new["yp"] = 1 - yp
        if ((EY == 1) if ypb == 0 else (EY == 0)) and ((Z == 1) if ypb == 0 else (Z == 0)):
            new["ypb"] = 1 - ypb
    return new, C

def unit_E(st, ein):
    """E_j under a state of the unit, with the value input E_(j-1) of the same state."""
    EY = st["yb"] if st["y"] != st["yb"] else int(st["y"] != ein)
    return 1 if st["u"] != st["v"] else int(EY == st["v"])

def cmd_unit(args):
    """The induction step of LEMMA' for a GENERIC unit and ARBITRARY delays of the unit above (assume-guarantee form).
    Assumed of the unit above (LEMMA' for j + 1, as a contract): E(j + 1) is at 0; when the key input C_j becomes 1 at a step t0
    it moves to 1 at step t0 + W (W = P_(j+1) - 1 >= 2) if its input stays (1, 1) for t0..t0 + W; when C_j becomes 0 at a step t1
    it moves to 0 at step t1 + W2 if its input stays (0, 0). Checked of the unit (both kinds, both a, every pair W, W2 in the range):
      list   a step whose moves differ from the lemma's list (t_1 = t + W, t_2 = t_1 + 1 + W2)
      up     the unit's outputs (C_j under s_tau, E_j under s_tau) break the contract's premise: (1, 1) on [t, t_1], (0, 0) on [t_1 + 1, last]
      down   (mid) e_j is not at a before the last step or not at c after it
      rest   the last state is not REST_j(c)
      fix    a waiting step (no listed move) at which the unit is NOT a fixed point of its own step: must be 0, so that the result
             for every pair of delays >= 2 follows from the pairs tested
      after  the unit moves again under the unchanged input after its last step (STABLE)
    Control (--ctrl 1): the list with F and B exchanged."""
    ctrl = int(take(args, "--ctrl", 1, 0))
    wmax = int(args[0]) if args else 7
    tot = dict(list=0, up=0, down=0, rest=0, fix=0, after=0)
    runs = 0
    for kind in ("mid", "bot"):
        for a in (0, 1):
            c = 1 - a
            F, B = ("yb", "y") if a == 0 else ("y", "yb")
            Fp, Bp = ("ypb", "yp") if a == 0 else ("yp", "ypb")
            if ctrl == 1:
                F, B = B, F
            for W in range(2, wmax + 1):
                for W2 in range(2, wmax + 1):
                    runs += 1
                    t = 1
                    t1 = t + W
                    t2 = t1 + 1 + W2
                    last = t2 + 1 if kind == "mid" else t2
                    sched = {t: [("v", c)], t + 1: [(F, 0)], t1: [(B, 1)], t1 + 1: [("u", c)]}
                    if kind == "mid":
                        sched[t1 + 1].append((Fp, 0))
                        sched[t2] = [(Bp, 1)]
                        sched[t2 + 1] = [("e", c)]
                    st = {"u": a, "v": a, "y": a, "yb": 1 - a}
                    if kind == "mid":
                        st.update({"e": a, "yp": a, "ypb": 1 - a})
                    eup = 0
                    for tau in range(1, last + 4):
                        ein_old = a if tau == 1 else c
                        # the unit above, by its contract: E(j + 1) to 1 at t1, to 0 at t2
                        eup_new = 1 if t1 <= tau < t2 else 0
                        new, C = unit_step(kind, st, c, ein_old, eup_new)
                        moves = sorted((n, new[n]) for n in new if new[n] != st[n])
                        if tau <= last:
                            tot["list"] += int(moves != sorted(sched.get(tau, [])))
                            if not sched.get(tau):
                                tot["fix"] += int(new != st)
                            Eout = unit_E(new, c)
                            want = (1, 1) if tau <= t1 else (0, 0)
                            tot["up"] += int((C, Eout) != want)
                            if kind == "mid":
                                tot["down"] += int(new["e"] != (c if tau == last else a))
                        else:
                            tot["after"] += int(new != st)
                        st = new
                        if tau == last:
                            want = {"u": c, "v": c, "y": c, "yb": 1 - c}
                            if kind == "mid":
                                want.update({"e": c, "yp": c, "ypb": 1 - c})
                            tot["rest"] += int(st != want)
    # cross-check of unit_step against the abstract machine abs_step (itself tied to the definition by `causal`): on random
    # states of a whole tower and random inputs, each unit j <= k - 2 of abs_step's result equals unit_step with the inputs taken
    # from abs_step's own old / new states
    rnd = random.Random(99)
    cross = ncross = 0
    for k in (4, 5, 6, 7):
        Efn = lambda j: f"e{j}" if 2 <= j <= k - 2 else f"u{j}"
        for _ in range(1500):
            st = {n: rnd.randrange(2) for n in abs_names(k, 1)}
            cin, ein = rnd.randrange(2), rnd.randrange(2)
            new = abs_step(k, 1, st, cin, ein)
            # C_j under the new state and E_j under the old state, bottom-up
            C = {0: cin}
            E = {0: ein}
            for j in range(1, k):
                u, v = new[f"u{j}"], new[f"v{j}"]
                C[j] = int(v == C[j - 1]) if u != v else 0
                y, yb = st[f"y{j}"], st[f"yb{j}"]
                EYo = yb if y != yb else int(y != E[j - 1])
                E[j] = 1 if st[f"u{j}"] != st[f"v{j}"] else int(EYo == st[f"v{j}"])
            for j in range(1, k - 1):
                kind = "bot" if j == 1 else "mid"
                loc = {"u": st[f"u{j}"], "v": st[f"v{j}"], "y": st[f"y{j}"], "yb": st[f"yb{j}"]}
                if kind == "mid":
                    loc.update({"e": st[f"e{j}"], "yp": st[f"yp{j}"], "ypb": st[f"ypb{j}"]})
                got, Cj = unit_step(kind, loc, C[j - 1], E[j - 1], new[Efn(j + 1)])
                ref = {"u": new[f"u{j}"], "v": new[f"v{j}"], "y": new[f"y{j}"], "yb": new[f"yb{j}"]}
                if kind == "mid":
                    ref.update({"e": new[f"e{j}"], "yp": new[f"yp{j}"], "ypb": new[f"ypb{j}"]})
                ncross += 1
                cross += int(got != ref or Cj != C[j])
    print(f"unit ctrl {ctrl} kinds mid,bot a 0,1 delays 2..{wmax} runs {runs} " + " ".join(f"{k} {v}" for k, v in tot.items())
          + f" cross {cross}/{ncross}", flush=True)


# ---------------------------------------------------------------- L-SI box 108's closed form (docs/si/box108-gk-proof.md section 3)
SPOS = {"S0": "0001010", "S1": "0101010", "S2": "0100010", "S3": "0110010", "S4": "1110000", "S5": "1110100", "S6": "1110101",
        "S7": "1010101", "S8": "1000101", "S9": "1001101", "S10": "0001001", "S11": "0001011"}      # u v y yb yp ypb e
TPOS = ["0001", "0101", "0111", "1110", "1010", "1011", "0001"]                                    # u v y yb; T6 = T0

def pos108(tau, h, ctrl=0):
    if tau in (0, 4 * h + 2): return "S0"
    if tau == 1: return "S1"
    if 2 <= tau <= h - 1: return "S2" if ctrl != 1 else "S3"
    if tau == h: return "S3"
    if h + 1 <= tau <= 2 * h - 1: return "S4"
    if tau == 2 * h: return "S5"
    if tau == 2 * h + 1: return "S6"
    if tau == 2 * h + 2: return "S7"
    if 2 * h + 3 <= tau <= 3 * h: return "S8"
    if tau == 3 * h + 1: return "S9"
    if 3 * h + 2 <= tau <= 4 * h: return "S10"
    if tau == 4 * h + 1: return "S11"
    raise ValueError((tau, h))

def closed108(k, meta, t, ctrl=0):
    """the state c_k(t) of box 108 section 3, as a list in gkx's mover order."""
    ix = meta["idx"]
    s = [0] * len(ix)
    H = {i: 2 ** (k - i + 1) - 1 for i in range(1, k)}
    tau = {1: t}
    for i in range(1, k - 1):
        tau[i + 1] = tau[i] % H[i]
    s[ix["v0"]] = int(t >= 1)
    p = SPOS[pos108(t, H[2], ctrl)]
    for n, b in zip(("u1", "v1", "y1", "yb1"), p[:4]):
        s[ix[n]] = int(b)
    for i in range(2, k - 1):
        p = SPOS[pos108(tau[i], H[i + 1], ctrl)]
        for n, b in zip((f"u{i}", f"v{i}", f"y{i}", f"yb{i}", f"yp{i}", f"ypb{i}", f"e{i}"), p):
            s[ix[n]] = int(b)
    p = TPOS[tau[k - 1]]
    for n, b in zip((f"u{k-1}", f"v{k-1}", f"y{k-1}", f"yb{k-1}"), p):
        s[ix[n]] = int(b)
    return s

def cmd_closed(args):
    """L-SI box 108: its closed form c_k(t) against my run, state by state; its claim on the stop (exactly v_1..v_(k-1) have a
    second available option at the final state); its periods H_i against the packet's P_i. Control 1: S3 for S2 in pos()."""
    ctrl = int(take(args, "--ctrl", 1, 0))
    for k in map(int, args):
        G, meta = rule(k)
        S, word = run(G)
        L = len(S) - 1
        bad = sum(1 for t in range(L + 1) if closed108(k, meta, t, ctrl) != S[t])
        _, w, A = step(G, S[L])
        held = sorted(meta["names"][x] for x in range(G["N"]) if len(A[x]) == 2)
        stop = int(held != sorted(f"v{j}" for j in range(1, k)) or w != "stuck")
        hp = sum(1 for j in range(1, k) if 2 ** (k - j + 1) - 1 != P(k, j))
        print(f"closed k {k} ctrl {ctrl} states {L + 1} closed {bad} stopset {stop} HvsP {hp}", flush=True)


def cmd_causal(args):
    """CAUSAL (referee): for every j0, the restriction of s+ (the definition's s') to the units j0..k-1 equals the abstract
    machine's step from (s on those units, E_(j0-1)(s), C_(j0-1)(s+)), the two input bits taken from the DEFINITION
    (value-ahead under s, key-ahead under s+). Random states with u0 at 0 (wires free or at 0), and all run states."""
    arb = take(args, "--arb", 2)
    ctrl = int(take(args, "--ctrl", 1, 0))
    for k in map(int, args):
        G, meta = rule(k)
        ix = meta["idx"]
        names = meta["names"]
        if arb is None:
            S, _ = run(G)
            states = S
            tag = f"run states {len(S)}"
        else:
            n, seed = int(arb[0]), int(arb[1])
            rnd = random.Random(seed * 1000 + k)
            states = []
            for _ in range(n):
                s = [rnd.randrange(2) for _ in range(G["N"])]
                s[ix["u0"]] = 0
                for nm, x in ix.items():
                    if nm.startswith("w"):
                        s[x] = 0
                states.append(s)
            tag = f"arb states {n} seed {seed}"
        bad = tot = opt = 0
        for s in states:
            s2, word, _ = step(G, s)
            if word == "opt":
                opt += 1
                continue
            if s2 is None:
                s2 = list(s)
            key2 = keys_of_state(G, s2)
            key1 = keys_of_state(G, s)
            Bs = {x: Bset(G, s, x, s[x]) for x in range(G["N"])}
            Bs2 = {x: Bset(G, s2, x, s2[x]) for x in range(G["N"])}
            for j0 in range(1, k):
                u, v = ix[f"u{j0-1}"], ix[f"v{j0-1}"]
                cin = int(key2[v] < key2[u])
                ein = int(ahead_sets(G, Bs[v], Bs[u]))
                if ctrl == 1:
                    cin = int(key1[v] < key1[u])                 # control: the key bit read under s
                if ctrl == 2:
                    ein = int(ahead_sets(G, Bs2[v], Bs2[u]))     # control: the value bit read under s+
                st = {n: s[ix[n]] for n in abs_names(k, j0)}
                nw = abs_step(k, j0, st, cin, ein)
                tot += 1
                bad += int(any(nw[n] != s2[ix[n]] for n in nw))
        print(f"causal k {k} ctrl {ctrl} set {tag} causal {bad}/{tot} optstates {opt}", flush=True)


# ---------------------------------------------------------------- section 8: which orders are used
def random_linext(items, less, rnd):
    """A random linear extension of the partial order given by pairs (a, b) in less (a before b)."""
    items = list(items)
    pred = {x: set() for x in items}
    for a, b in less:
        if a in pred and b in pred:
            pred[b].add(a)
    out = []
    done = set()
    while len(out) < len(items):
        av = [x for x in items if x not in done and pred[x] <= done]
        x = rnd.choice(av)
        out.append(x)
        done.add(x)
    return out

def variant(k, rnd, breakc=0):
    """A genome with the SAME movers, targets, start and beta-ids as G_k, and with gates and ranks drawn at random among all
    orders that satisfy the constraints section 8 lists (and nothing else). breakc > 0 violates one listed constraint."""
    G, meta = rule(k)
    ix = meta["idx"]
    names = meta["names"]
    Efn = meta["E"]
    lev = G["lev"]
    # ---- gates: inside each level a random linear extension of section 8's epsilon constraints; levels interleaved at random
    less = []
    less += [(("v0", 1), ("u0", 0)), (("u0", 0), ("v0", 0)), (("u0", 0), ("u0", 1))]
    for j in range(1, k):
        less += [((f"u{j}", 0), (f"v{j}", 0)), ((f"u{j}", 1), (f"v{j}", 1))]
    for j in range(1, k - 1):
        less += [((Efn(j + 1), 1), (f"wv{j}", 0)), ((f"wv{j}", 0), (f"wv{j}", 1))]
    for j in range(2, k - 1):
        less += [((Efn(j + 1), 0), (f"wu{j}", 0)), ((f"wu{j}", 0), (f"wu{j}", 1))]
    if breakc == 1:      # K1 aligned: v before u at one level
        less.remove((("u2", 0), ("v2", 0)))
        less.append((("v2", 0), ("u2", 0)))
    if breakc == 2:      # K2: the wire before E's option 1
        less.remove(((Efn(2), 1), ("wv1", 0)))
        less.append((("wv1", 0), (Efn(2), 1)))
    if breakc == 3:      # level 0: u0 before v0's option 1
        less.remove((("v0", 1), ("u0", 0)))
        less.append((("u0", 0), ("v0", 1)))
    if breakc == 6:      # K3: the wire wu_2 before E(3)'s option 0 (needs k >= 4)
        less.remove(((Efn(3), 0), ("wu2", 0)))
        less.append((("wu2", 0), (Efn(3), 0)))
    seqs = []
    for L in range(max(lev) + 1):
        its = [(n, o) for n in names if lev[ix[n]] == L for o in (0, 1)]
        seqs.append(random_linext(its, less, rnd))
    # random interleaving of the per-level sequences (keys compare gates of ONE level only)
    order = []
    ptr = [0] * len(seqs)
    while any(ptr[i] < len(seqs[i]) for i in range(len(seqs))):
        i = rnd.choice([i for i in range(len(seqs)) if ptr[i] < len(seqs[i])])
        order.append(seqs[i][ptr[i]])
        ptr[i] += 1
    for r, (n, o) in enumerate(order):
        G["gate"][ix[n]][o] = r
    # ---- ranks: depth-major on the non-free betas, section 8's constraints inside a depth; wires and (u0, 1) anywhere
    dep = meta["depth"]
    more = []            # (a, b): a ranks ABOVE b
    more += [(("v0", 1), ("u0", 0)), (("u0", 0), ("v0", 0))]
    for j in range(1, k):
        more += [((f"v{j}", 0), (f"u{j}", 1)), ((f"v{j}", 1), (f"u{j}", 0))]          # the split case reads these two only
        more += [((f"y{j}", 1), (f"yb{j}", 0)), ((f"yb{j}", 1), (f"y{j}", 0))]
        if 2 <= j <= k - 2:
            more += [((f"yp{j}", 1), (f"ypb{j}", 0)), ((f"ypb{j}", 1), (f"yp{j}", 0))]
    if breakc == 4:      # V2: back above forward in Y_1
        more.remove((("y1", 1), ("yb1", 0)))
        more.append((("yb1", 0), ("y1", 1)))
    if breakc == 7:      # V1 split: u above v at level 2
        more.remove((("v2", 0), ("u2", 1)))
        more.append((("u2", 1), ("v2", 0)))
    free = [(n, o) for n in names for o in (0, 1) if dep[n] is None] + [("u0", 1)]
    seq = []             # from the LOWEST rank up: largest depth first
    depths = sorted(set(d for d in dep.values() if d is not None), reverse=True)
    if breakc == 5:      # not depth-major: depth order reversed
        depths = depths[::-1]
    for d in depths:
        its = [(n, o) for n in names if dep[n] == d for o in (0, 1) if (n, o) != ("u0", 1)]
        seq += random_linext(its, [(b, a) for (a, b) in more], rnd)
    for f in free:
        seq.insert(rnd.randrange(len(seq) + 1), f)
    for r, (n, o) in enumerate(seq):
        G["br"][G["opts"][ix[n]][o][2]] = r
    return G, meta

def cmd_orders(args):
    """Section 8: «Nothing else»: every genome whose gates and ranks satisfy the listed constraints has the SAME run."""
    reps = int(take(args, "--reps", 1, 200))
    seed = int(take(args, "--seed", 1, 1))
    for k in map(int, args):
        G0, meta = rule(k)
        S0, w0 = run(G0)
        rnd = random.Random(seed * 100 + k)
        diff = notmember = same_genome = 0
        for _ in range(reps):
            G, _ = variant(k, rnd)
            notmember += int(sum(member(G)) != 0)
            same_genome += int(G == G0)
            S, w = run(G, cap=4 * len(S0) + 50)
            diff += int(S != S0 or w != w0)
        line = f"orders k {k} reps {reps} seed {seed} rundiff {diff} notmember {notmember} equal_to_G_k {same_genome}"
        # controls: one listed constraint violated; the count of variants whose run differs
        for bc in (1, 2, 3, 4, 5, 6, 7):
            if bc == 6 and k < 4:
                line += " break6 n/a"
                continue
            d = 0
            n = max(20, reps // 10)
            for _ in range(n):
                G, _ = variant(k, rnd, bc)
                try:
                    S, w = run(G, cap=4 * len(S0) + 50)
                except AssertionError:
                    S, w = None, "cap"
                d += int(S != S0 or w != w0)
            line += f" break{bc} {d}/{n}"
        print(line, flush=True)


def cmd_sizes(args):
    """The Corollary's sizes on the frozen .pg files DIR/G_k_g3.pg (n, m, largest priority) and the explicit instances."""
    d = args[0]
    bad = 0
    for k in map(int, args[1:]):
        L = open(f"{d}/G_{k}_g3.pg").read().strip().split("\n")
        rows = [l.rstrip(";").split() for l in L[1:]]
        n = len(rows)
        m = sum(len(r[3].split(",")) for r in rows)
        mx = max(int(r[1]) for r in rows)
        M = 18 * k - 32
        b = int(n != 135 * k - 230) + int(m != 176 * k - 300) + int(mx != 4 * M + 9) + int(mx > n) + int(n != 9 * k - 16 + 7 * M + 10)
        bad += b
        print(f"sizes k {k} n {n} m {m} maxprio {mx} sizebad {b}")
    print(f"sizes files {len(args) - 1} sizebad_sum {bad}")
    n = lambda k: 135 * k - 230
    m = lambda k: 176 * k - 300
    for c in (2, 3, 4):
        for nm, f in (("n", n), ("n+m", lambda k: n(k) + m(k))):
            k = 3
            while not (2 ** k - 1 > f(k) ** c):
                k += 1
            later = all(2 ** j - 1 > f(j) ** c for j in range(k, k + 400))
            print(f"first k with 2^k-1 > ({nm})^{c}: k {k} size {f(k)} lhs {2 ** k - 1} rhs {f(k) ** c} holds_for_next_400 {int(later)}")


if __name__ == "__main__":
    cmd = sys.argv[1]
    {"gen": cmd_gen, "member": cmd_member, "run": cmd_run, "facts": cmd_facts, "resp": cmd_resp, "abs": cmd_abs,
     "orders": cmd_orders, "causal": cmd_causal, "sizes": cmd_sizes, "unit": cmd_unit, "closed": cmd_closed}[cmd](sys.argv[2:])
