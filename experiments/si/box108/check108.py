#!/usr/bin/env python3
"""Box 108 (L-SI 56) checker for docs/si/box108-gk-proof.md: L(G_k) = 2^k - 2 on R104's IDEAL model.
Checks, for k = KLO..KHI (default 3..12), with the own builder gk108 and the own simulator ideal108:
  SHA     the four sha1 of the Lead's rule (k = 3, 4, 8, 10)
  RUN     L(G_k) = 2^k - 2; the stop is "nothing changes" with the held movers v_1..v_{k-1}
  CLOSED  s_t = c_k(t) for every t (the closed form of the proof, §3: nested phases tau_1 = t, tau_{i+1} = tau_i mod H_i)
  LATCH   Lemma L1 (two-input latch form) on every step, from the definition (chains, keys)
  STATIC  Lemmas K0-K6, X0-X7 (signal formulas for pref / kmin / P / K / Q / R) on every run state and on RAND random states
  SIG     P_j = K_j = [u_j != v_j] on every run state (Lemma SIG)
  SW      switches per mover: 1 on levels 0 (v0) and 1, 2^(i-1) on a middle level i, 2^(k-2) on the top; total 11 * 2^(k-2) - 9 (Corollary SW)
  DOC     with --doc FILE: the position row of §3 and the three phase tables of §4 of the proof file, parsed out of the file, equal
          per position the set of observed (state, Q, [R], Xb, [E], Xi) at c_k(t), signals computed from chains and keys
  TABLE   every (level type, phase class) has ONE row (old signals, new signals, per mover cur / pref / kmin / new) over all k, levels, t;
          --table prints the rows (they are the tables of the proof, §5)
Controls (must FIRE = the check must fail): --ctrl NAME with NAME in CTRLS below (genome mutations: each order / start the proof uses;
closed-form and formula mutations).  Exit 0 iff every check passes (without --ctrl) / the control fires (with --ctrl)."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gk108, ideal108

SHA = {3: "cd3cd7e361dfe16482bbe56eb87d3e3decf9e6af", 4: "7a2218bfa94e37f85b3fc60d874030aeba8ca848",
       8: "d3ad8e2e6f202eb17e66d04dad77de1a33e74eb2", 10: "da29d33ecaf20cb777650729e54acb1dad17cfd9"}
CTRLS = ["H-off", "eps-wv", "eps-wu", "eps-uv", "eps-v0", "dl-y", "dl-y2", "dl-yp", "dl-yp2", "dl-uv", "dl-uvtop", "dl-v0", "dl-u0", "dl-w",
         "dep-yb", "start-yb", "start-ypb", "form-kmin-yp", "form-Q"]

# ---------- the closed form c_k(t) (proof §3) ----------
MID = {0: "0001010", 1: "0101010", 2: "0100010", 3: "0110010", 4: "1110000", 5: "1110100", 6: "1110101",
       7: "1010101", 8: "1000101", 9: "1001101", 10: "0001001", 11: "0001011"}          # u v y yb yp ypb e at S0..S11
TOP = {0: "0001", 1: "0101", 2: "0111", 3: "1110", 4: "1010", 5: "1011"}                  # u v y yb at T0..T5
def H(k, i): return 2 ** (k - i + 1) - 1
def midpos(tau, h):
    """position S0..S11 of a level at phase tau in [0, 4h + 2], h = H_{i+1}"""
    if tau in (0, 4 * h + 2): return 0
    if tau == 1: return 1
    if tau <= h - 1: return 2
    if tau == h: return 3
    if tau <= 2 * h - 1: return 4
    if tau == 2 * h: return 5
    if tau == 2 * h + 1: return 6
    if tau == 2 * h + 2: return 7
    if tau <= 3 * h: return 8
    if tau == 3 * h + 1: return 9
    if tau <= 4 * h: return 10
    assert tau == 4 * h + 1; return 11
def phases(k, t, off=0):
    tau = {1: t}
    for i in range(1, k - 1): tau[i + 1] = tau[i] % (H(k, i) + off)
    return tau
def closed(k, t, names, off=0):
    tau = phases(k, t, off); s = {"u0": 0, "v0": int(t >= 1)}
    for n in names:
        if n[0] == "w": s[n] = 0
    p = midpos(tau[1], H(k, 2) + off) if tau[1] <= 2 * H(k, 2) else None; assert p is not None and p <= 5
    for a, c in zip(("u1", "v1", "y1", "yb1"), MID[p][:4]): s[a] = int(c)
    for i in range(2, k - 1):
        p = midpos(tau[i], H(k, i + 1) + off)
        for a, c in zip((f"u{i}", f"v{i}", f"y{i}", f"yb{i}", f"yp{i}", f"ypb{i}", f"e{i}"), MID[p]): s[a] = int(c)
    p = tau[k - 1] % 6
    for a, c in zip((f"u{k-1}", f"v{k-1}", f"y{k-1}", f"yb{k-1}"), TOP[p]): s[a] = int(c)
    return tuple(s[n] for n in names)

# ---------- direct quantities, from the definition ----------
def keyof(I, s, x, o):
    w = I.opts[x][o][0]
    return (keyof(I, s, w, s[w]) if w >= 0 else ()) + (I.gate[x][o],)
def pref(I, s, x):   return 0 if I.better(I.chain(s, x, 0), I.chain(s, x, 1)) else 1
def kmin(I, n, x):   return 0 if keyof(I, n, x, 0) < keyof(I, n, x, 1) else 1
def val(I, s, x):    return I.chain(s, x, s[x])

# ---------- signal formulas (proof §2), as functions of a state given by names ----------
def signals(k, S, mut=None):
    """K, P, Q, R by the recursive formulas of Lemmas K0, K2, X0, X1, X4, X5 (S: name -> option)"""
    fl = {"u": "v", "v": "u"}; K = {0: "u" if S["v0"] == 0 else "v"}; P = {0: K[0]}; Q = {}; R = {}
    for j in range(1, k):
        u, v, y, yb = S[f"u{j}"], S[f"v{j}"], S[f"y{j}"], S[f"yb{j}"]
        K[j] = "u" if u == v else (K[j - 1] if (u, v) == (0, 1) else fl[K[j - 1]])
        if (y, yb) == (0, 1): Q[j] = "yb"
        elif (y, yb) == (1, 0): Q[j] = "y"
        elif (y, yb) == (0, 0): Q[j] = "y" if P[j - 1] == "u" else "yb"
        else: Q[j] = "y" if P[j - 1] == "v" else "yb"
        if mut == "form-Q" and (y, yb) == (0, 0): Q[j] = "yb" if Q[j] == "y" else "y"
        P[j] = "v" if u != v else (("u" if Q[j] == "yb" else "v") if u == 0 else ("u" if Q[j] == "y" else "v"))
        if 2 <= j <= k - 2:
            c, d = S[f"yp{j}"], S[f"ypb{j}"]
            if (c, d) == (0, 1): R[j] = "ypb"
            elif (c, d) == (1, 0): R[j] = "yp"
            elif (c, d) == (0, 0): R[j] = "yp" if Q[j] == "yb" else "ypb"
            else: R[j] = "yp" if Q[j] == "y" else "ypb"
    return K, P, Q, R
def split(n):
    t = n.rstrip("0123456789"); return t, int(n[len(t):])
def pref_formula(k, S, n, sig):
    K, P, Q, R = sig; t, j = split(n)
    if t[0] == "w": return 0
    if j == 0 and t in ("u", "v"): return 0 if t == "u" else 1
    if t == "u": return 0 if Q[j] == "yb" else 1
    if t == "v": return 0 if Q[j] == "y" else 1
    if t == "e": return 0 if R[j] == "ypb" else 1
    if t == "y": return 0 if P[j - 1] == "u" else 1
    if t == "yb": return 0 if P[j - 1] == "v" else 1
    if t == "yp": return 0 if Q[j] == "yb" else 1
    if t == "ypb": return 0 if Q[j] == "y" else 1
def kmin_formula(k, Sn, n, sign, mut=None):
    K = sign[0]; t, j = split(n); E = lambda i: f"e{i}" if i <= k - 2 else f"u{k-1}"
    if t[0] == "w": return 0
    if j == 0 and t in ("u", "v"): return 0 if t == "u" else 1
    if t in ("u", "v", "e"): return 0 if K[j - 1] == "u" else 1
    if t in ("y", "yb"):
        if j == k - 1: return 0 if K[j] == "u" else 1
        return 1 if (Sn[E(j + 1)] == 1 or K[j] == "u") else 0
    if t in ("yp", "ypb"):
        if mut == "form-kmin-yp": return 1 if (Sn[E(j + 1)] == 0 or K[j] == "u") else 0
        return 1 if (Sn[E(j + 1)] == 0 or K[j] == "v") else 0

# ---------- controls: genome mutations ----------
def mutate(G, names, k, ctrl):
    ix = {n: i for i, n in enumerate(names)}
    def swap_gate(a, b):
        for o in (0, 1): G["gate"][ix[a]][o], G["gate"][ix[b]][o] = G["gate"][ix[b]][o], G["gate"][ix[a]][o]
    def swap_rank(a, oa, b, ob):
        ba, bb = 2 * ix[a] + oa, 2 * ix[b] + ob; G["br"][ba], G["br"][bb] = G["br"][bb], G["br"][ba]
    j = k - 2 if k >= 4 else 1
    if ctrl == "eps-wv": swap_gate(f"wv{j}", f"e{j+1}" if j + 1 <= k - 2 else f"u{k-1}")       # eps(E(j+1), .) < eps(wv_j, 0)   (K4)
    elif ctrl == "eps-wu": swap_gate(f"wu{j}", f"e{j+1}" if j + 1 <= k - 2 else f"u{k-1}")     # eps(E(j+1), .) < eps(wu_j, 0)   (K5); needs k >= 4
    elif ctrl == "eps-uv": swap_gate(f"u{k-1}", f"v{k-1}")                                     # eps(u_j, .) < eps(v_j, .)       (K2)
    elif ctrl == "eps-v0": G["gate"][ix["v0"]][1] = 4                                          # eps(v0, 1) < eps(u0, 0)         (K0)
    elif ctrl == "dl-y": swap_rank(f"y{k-1}", 0, f"yb{k-1}", 1)                                # dl(yb_j, 1) > dl(y_j, 0)        (X1)
    elif ctrl == "dl-y2": swap_rank(f"y{k-1}", 1, f"yb{k-1}", 0)                               # dl(y_j, 1) > dl(yb_j, 0)        (X1)
    elif ctrl == "dl-yp2": swap_rank(f"yp{j}", 1, f"ypb{j}", 0)                                # dl(yp_j, 1) > dl(ypb_j, 0)      (X5); needs k >= 4
    elif ctrl == "dl-uvtop": swap_rank(f"u{k-1}", 0, f"v{k-1}", 1)                             # the top pair's dl order: read by no mover
    elif ctrl == "dl-u0": G["br"][2 * ix["u0"] + 1] = 2 * G["N"]                               # dl(u0, 0) > dl(u0, 1)  (X0): beta(u0, 1) to the top rank
    elif ctrl == "dl-w": swap_rank(f"wv{j}", 0, f"wv{j}", 1)                                   # dl(w, 0) > dl(w, 1)             (X7)
    elif ctrl == "dl-yp": swap_rank(f"yp{j}", 0, f"ypb{j}", 1)                                 # dl(ypb_j, 1) > dl(yp_j, 0)      (X5); needs k >= 4
    elif ctrl == "dl-uv": swap_rank(f"u{k-2}", 0, f"v{k-2}", 1)                                # dl(v_j, .) > dl(u_j, .)  (X4), j <= k - 2 (P_{k-1} is read by no mover)
    elif ctrl == "dl-v0": swap_rank("v0", 0, "v0", 1)                                          # dl(v0, 1) > dl(u0, 0) > dl(v0, 0) (X0)
    elif ctrl == "dep-yb": swap_rank(f"y{k-1}", 1, f"v{k-2}", 0)                               # class B_{j-1} above class Y_j   (X1, X2)
    elif ctrl == "start-yb": G["start"][ix[f"yb{k-1}"]] = 0
    elif ctrl == "start-ypb": G["start"][ix[f"ypb{j}"]] = 0                                    # needs k >= 4
    return G

def classes(k, i, t):
    """(level type, phase class) of level i >= 1 for the step t -> t + 1 (t <= 2^k - 2; the last one is the stop step)"""
    tau = phases(k, t); T = 2 ** k - 2
    if i == 1:
        h = H(k, 2); a = min(midpos(t, h), 4); b = min(midpos(min(t + 1, T), h), 4)      # S5 = S4 on (u, v, y, yb)
        if a == b == 4: return "bot", "A4 stay (stop)" if t == T else ("A4 stay (E=1)" if t + 1 <= 2 * h - 1 else "A4 stay (E=0)")
        return "bot", f"A{a}->A{b}" if a != b else f"A{a} stay"
    if i == k - 1:
        a = tau[i] % 6; b = phases(k, t + 1)[i] % 6 if t < T else 0
        return "top", (f"T{a}->T{b}" if a != b else "T0 idle")
    h = H(k, i + 1); a = midpos(tau[i], h); b = midpos(phases(k, t + 1)[i], h) if t < T else 0
    return "mid", (f"S{a}->S{b}" if a != b else (f"S{a} stay" if a else "S0 idle"))

def check(k, ctrl=None, rand=0, rows=None, verbose=True):
    """returns a dict of failure counts (all zero = pass)"""
    G, names = gk108.build(k); fails = {c: 0 for c in ("SHA", "RUN", "CLOSED", "LATCH", "STATIC", "SIG", "SW")}
    if k in SHA and gk108.sha(G) != SHA[k]: fails["SHA"] += 1
    if ctrl and ctrl not in ("H-off", "form-kmin-yp", "form-Q"): G = mutate(G, names, k, ctrl)
    I = ideal108.Ideal(G); N = G["N"]; ix = {n: i for i, n in enumerate(names)}; S = I.run(cap=2 ** k + 8); L = len(S) - 1; T = 2 ** k - 2
    if L != T: fails["RUN"] += 1
    last, A = I.step(S[-1]); held = sorted(names[x] for x in range(N) if len(A[x]) > 1)
    if last is not None or held != sorted(f"v{j}" for j in range(1, k)): fails["RUN"] += 1
    def swf(n):                                                          # Corollary SW: switches per mover
        t, j = split(n)
        if t[0] == "w" or n == "u0": return 0
        if j <= 1: return 1
        return 2 ** (k - 2) if j == k - 1 else 2 ** (j - 1)
    for x in range(N):
        if sum(1 for t in range(L) if S[t][x] != S[t + 1][x]) != swf(names[x]): fails["SW"] += 1
    if sum(swf(n) for n in names) != 11 * 2 ** (k - 2) - 9: fails["SW"] += 1
    off = -1 if ctrl == "H-off" else 0
    for t in range(min(L, T) + 1):
        try: c = closed(k, t, names, off)
        except AssertionError: c = None                                  # an ill-formed closed form (control H-off) counts as a mismatch
        if S[t] != c: fails["CLOSED"] += 1
    fm = ctrl if ctrl in ("form-kmin-yp", "form-Q") else None
    def static(s, n):
        """formula checks at old state s, new state n (any pair of states with wires and u0 at option 0)"""
        bad = 0; Sd = {names[x]: s[x] for x in range(N)}; Nd = {names[x]: n[x] for x in range(N)}
        sig = signals(k, Sd, fm); sign = signals(k, Nd, fm); K, P, Q, R = sig
        for j in range(k):
            u, v = ix[f"u{j}"], ix[f"v{j}"]
            if (P[j] == "u") != I.better(val(I, s, u), val(I, s, v)): bad += 1
            if (K[j] == "u") != (keyof(I, s, u, s[u]) < keyof(I, s, v, s[v])): bad += 1
            if j >= 1 and (Q[j] == "y") != I.better(val(I, s, ix[f"y{j}"]), val(I, s, ix[f"yb{j}"])): bad += 1
            if j in R and (R[j] == "yp") != I.better(val(I, s, ix[f"yp{j}"]), val(I, s, ix[f"ypb{j}"])): bad += 1
        for x in range(N):
            if pref(I, s, x) != pref_formula(k, Sd, names[x], sig): bad += 1
            if kmin(I, n, x) != kmin_formula(k, Nd, names[x], sign, fm): bad += 1
        return bad, sig, sign
    for t in range(L + 1):
        s = S[t]; n = S[t + 1] if t < L else S[t]
        for x in range(N):                                               # LATCH (Lemma L1), from the definition
            want = s[x] if pref(I, s, x) == s[x] else kmin(I, n, x)
            if n[x] != want: fails["LATCH"] += 1
        bad, sig, sign = static(s, n); fails["STATIC"] += bad; K, P, Q, R = sig
        for j in range(1, k):                                            # SIG
            X = "v" if s[ix[f"u{j}"]] != s[ix[f"v{j}"]] else "u"
            if not (P[j] == K[j] == X): fails["SIG"] += 1
        if rows is not None and L == T and not ctrl:
            Kn = sign[0]; b = lambda z: int(z == "v"); tau = phases(k, t)
            for i in range(1, k):                                        # phase-table tuples at c(t) (for --doc)
                typ = "bot" if i == 1 else ("top" if i == k - 1 else "mid")
                pos = f"A{min(midpos(t, H(k, 2)), 4)}" if i == 1 else (f"T{tau[i] % 6}" if i == k - 1 else f"S{midpos(tau[i], H(k, i + 1))}")
                mvs = ["u", "v", "y", "yb"] + (["yp", "ypb", "e"] if typ == "mid" else [])
                tup = ["".join(str(s[ix[f"{m}{i}"]]) for m in mvs), Q[i]] + ([R[i]] if typ == "mid" else []) + [str(b(P[i - 1]))]
                if i <= k - 2: tup.append(str(s[ix[f"e{i+1}" if i + 1 <= k - 2 else f"u{k-1}"]]))
                tup.append(str(int(s[ix[f"u{i}"]] != s[ix[f"v{i}"]])))
                rows.setdefault(("phase", pos), set()).add(tuple(tup))
            for i in range(1, k):
                typ, cl = classes(k, i, t); E = (f"e{i+1}" if i + 1 <= k - 2 else f"u{k-1}") if i <= k - 2 else None
                mv = ["u", "v", "y", "yb"] + (["yp", "ypb", "e"] if typ == "mid" else [])
                old = f"Q={Q[i]} " + (f"R={R[i]} " if typ == "mid" else "") + f"Xb={b(P[i-1])}"
                new = f"Xb={b(Kn[i-1])} " + (f"E={n[ix[E]]} " if E else "") + f"Xi={b(Kn[i])}"
                cells = []
                for m in mv:
                    x = ix[f"{m}{i}"]; p = pref(I, s, x); q = kmin(I, n, x)
                    cells.append(f"{m}:{s[x]} p{p} " + ("-" if p == s[x] else f"k{q} " + (f"->{n[x]}" if n[x] != s[x] else "hold")))
                rows.setdefault((typ, cl), set()).add(f"old {old} | new {new} | " + " | ".join(cells))
    rng = random.Random(108 + k)
    for _ in range(rand):                                                # STATIC on arbitrary states (wires and u0 at option 0)
        s = tuple(0 if (names[x][0] == "w" or names[x] == "u0") else rng.randrange(2) for x in range(N))
        n = tuple(0 if (names[x][0] == "w" or names[x] == "u0") else rng.randrange(2) for x in range(N))
        fails["STATIC"] += static(s, n)[0]
    fails["_L"] = L
    if verbose:
        print(f"G_{k} N {N} L {L} want {T} held_at_stop {','.join(held)} fails " + " ".join(f"{c}={v}" for c, v in fails.items() if c[0] != "_") + (f" ctrl {ctrl}" if ctrl else ""), flush=True)
    return fails

def doc_tables(fn):
    """parse the position row of §3, the top positions of §3 and the three phase tables of §4 out of the proof file"""
    import re
    ph = {}; st = None; tops = {}
    for line in open(fn, encoding="utf-8"):
        if line.startswith("|"):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            if c[0] == "state" and len(c) == 13: st = [x.replace(" ", "") for x in c[1:]]
            elif len(c) in (6, 7, 8) and re.fullmatch(r"[AST]\d+", c[1]):
                clean = [re.sub(r"\(.*?\)", "", x).replace(" ", "") for x in c[2:]]
                ph.setdefault(c[1], set()).add(tuple(clean))
        for m in re.finditer(r"T(\d) = (\d\d \d\d)", line): tops[int(m.group(1))] = m.group(2).replace(" ", "")
    return st, tops, ph

ORDER = {"bot": ["A0->A1", "A1->A2", "A2 stay", "A2->A3", "A3->A4", "A4 stay (E=1)", "A4 stay (E=0)", "A4 stay (stop)"],
         "mid": ["S0->S1", "S1->S2", "S2 stay", "S2->S3", "S3->S4", "S4 stay", "S4->S5", "S5->S6", "S6->S7", "S7->S8", "S8 stay", "S8->S9",
                 "S9->S10", "S10 stay", "S10->S11", "S11->S0", "S0 idle"],
         "top": ["T0->T1", "T1->T2", "T2->T3", "T3->T4", "T4->T5", "T5->T0", "T0 idle"]}

if __name__ == "__main__":
    a = sys.argv[1:]; table = "--table" in a; a = [x for x in a if x != "--table"]; ctrl = None; rand = 200; doc = None
    if "--doc" in a: i = a.index("--doc"); doc = a[i + 1]; del a[i:i + 2]
    if "--ctrl" in a: i = a.index("--ctrl"); ctrl = a[i + 1]; del a[i:i + 2]
    if "--rand" in a: i = a.index("--rand"); rand = int(a[i + 1]); del a[i:i + 2]
    lo, hi = (int(a[0]), int(a[1])) if len(a) >= 2 else (3, 12)
    if ctrl:
        assert ctrl in CTRLS; fired = 0; n = 0; which = set(); Ls = []
        for k in range(max(lo, 4), hi + 1):
            f = check(k, ctrl, rand, verbose=False); Ls.append(f.pop("_L")); n += 1; fired += int(any(f.values())); which |= {c for c, v in f.items() if v}
        print(f"CONTROL {ctrl}: fired on {fired} of {n} k (k {max(lo, 4)}..{hi}); L {Ls} (unmutated {[2 ** k - 2 for k in range(max(lo, 4), hi + 1)]}); counters {' '.join(sorted(which)) or '-'}")
        sys.exit(0 if fired == n else 1)
    rows = {}; tot = 0
    for k in range(lo, hi + 1):
        f = check(k, None, rand, rows); f.pop("_L"); tot += sum(f.values())
    phase = {key[1]: v for key, v in rows.items() if key[0] == "phase"}; rows = {key: v for key, v in rows.items() if key[0] != "phase"}
    if doc:
        st, tops, ph = doc_tables(doc); bad = 0
        bad += int(st != [MID[p] for p in range(12)]) + int(tops != {p: TOP[p] for p in range(6)})
        for pos in sorted(set(phase) | set(ph)):
            if phase.get(pos) != ph.get(pos): bad += 1; print("DOC mismatch at", pos, "observed", sorted(phase.get(pos, [])), "doc", sorted(ph.get(pos, [])))
        print(f"DOC positions {len(phase)} doc-positions {len(ph)} fails DOC={bad}"); tot += bad
    multi = [key for key, v in rows.items() if len(v) != 1]; missing = [(t, c) for t in ORDER for c in ORDER[t] if (t, c) not in rows]
    extra = [key for key in rows if key[1] not in ORDER[key[0]]]
    print(f"TABLE classes {len(rows)} multi-row {len(multi)} missing {len(missing)} unexpected {len(extra)}")
    if table:
        for t in ("bot", "mid", "top"):
            for c in ORDER[t]:
                for r in sorted(rows.get((t, c), ["(not seen)"])): print(f"{t} {c:14s} | {r}")
    ok = tot == 0 and not multi and not missing and not extra
    print("CHECK108", "PASS" if ok else "FAIL", f"k {lo}..{hi} rand {rand}"); sys.exit(0 if ok else 1)
