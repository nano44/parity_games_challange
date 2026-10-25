#!/usr/bin/env python3
"""Box 42 (L-RED successor 18): exact checker of the frozen packets
  P-N5-FBPOLY (docs/new/P-N5-FBPOLY-box41.md, sha1 de244dcd) §0.3, §1-§6 and
  P-N5-FX     (docs/si/P-N5-FX-box14.md, sha1 aa227b0b) §1 (a) with its inputs R-STICK and the in-phase transition kinds,
written from the packet texts (not from fbpoly.py / fbpoly17.py / pfz17.py). 𝒞^1O asserted (exactly one Odd vertex o of out-degree > 1).
Trace: sox.trace (= n5.run, SPEC S3) or ex16.trace from a start pair (own copies of n5.py's loop; engine si.py read-only).
κ_t(z) = (M_t(z), s_θ·ℓ(Ξ_t z)), κwt(v) = (wt(v), s_θ); lexicographic. Simple-path optima by reverse DFS from the sink (budget; a
phase over budget skips only the path-based checks, counted as SKIP_paths).
Checks (FAIL_<name> printed with the state):
  TKIND  in-phase transition: σ changes only (τ constant); fallback ⇒ switched set = gate sources and x*_v = argmax (Ξ_k(w), w).
  AK     (Aκ) z ∈ U∖{c_θ}: next_t z ∈ U and κ_t z = κwt z + κ_t(next_t z).   A0K  κ_t(c_θ) = (0,0), M_t(next_t c_θ) = 0.
  M2K    κ_t(z) ≤ κ_{t+1}(z), z ∈ U, in-phase.   HP  honest play = (σ,τ)-play up to the first o; (i)/(ii).   YB  ¬H1: P(θ)=∅, 1≤ℓ≤|U|−1.
  FBR    κ-FB-ROUND.   KHa/KHb/KHc  κ-HAT-FREEZE (a)/(b)/(c).   KPFZ  κ-PFZ (o≠c_θ; and the G_U form used in FB-POLY (c) if o=c_θ).
  KYF    κ-Y-FORM.   EXSW EXIT-SWITCH (existence + p_u simple, in G_Û / G_U^o, κ identity for every such u).
  FEX    FREEZE-EXIT.  CNO CN-ONLY.  THA THETA-AFTER.  FBP FB-POLY (a)-(d).  RST R-STICK.  FX Corollary FX (a).
Usage: fbx18.py [--start file.json] game.pg ...  (prints FAIL lines and a final dict of counters / regime counts / slacks)"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import sox, ex16
from sox import lev

BUDGET = 400000

def opt_paths(nodes, adj, sink, kw, maxe):
    """best[z][e] = max κwt(p ∖ {sink}) over simple paths z → sink with exactly e edges (reverse DFS). None if over budget."""
    radj = {v: [] for v in nodes}
    for v in nodes:
        for w in adj.get(v, ()):
            if w in radj: radj[w].append(v)
    best = {v: {} for v in nodes}; best[sink][0] = (0, 0); steps = [0]
    def dfs(z, e, val, on):
        for y in radj[z]:
            if y in on: continue
            steps[0] += 1
            if steps[0] > BUDGET: raise OverflowError
            nv = (val[0] + kw[y][0], val[1] + kw[y][1]); ne = e + 1
            if ne not in best[y] or nv > best[y][ne]: best[y][ne] = nv
            if ne < maxe:
                on.add(y); dfs(y, ne, nv, on); on.discard(y)
    try: dfs(sink, 0, (0, 0), {sink})
    except OverflowError: return None
    def upto(z, j):
        c = [v for e, v in best[z].items() if e <= j]
        return max(c) if c else None
    return upto

def analyse(g, acc, name, st=None, cap=500):
    oc = sox.oddchoice(g); assert len(oc) == 1, "not C^1O"; o = oc[0]; n = g.n
    S, FB, E = (ex16.trace(g, st, cap=cap) if st is not None else sox.trace(g, cap=cap))
    N = len(S); ev = [E.evaluate(tuple(s)) for s, _ in S]
    Xi = [e[0] for e in ev]; SB = [e[1] for e in ev]; lam = [tuple(x[0] for x in X) for X in Xi]
    rank = E.rank
    def bump(k, v=1): acc[k] = acc.get(k, 0) + v
    def mx(k, v): acc[k] = max(acc.get(k, -10 ** 9), v)
    def fail(k, *a):
        bump("FAIL_" + k)
        if acc.get("FAIL_" + k) <= 5: print("FAIL_" + k, name, st is not None, *a, flush=True)
    def nxt(t, v): return S[t][0][v] if g.owner[v] == 0 else SB[t][v]
    def stp(t, v): return S[t][0][v] if g.owner[v] == 0 else S[t][1][v]
    def walk(f, v):
        seen, out, x = set(), [], v
        while x not in seen: seen.add(x); out.append(x); x = f(x)
        return out, x                       # lasso vertices in order, first repeated vertex
    Rs = []
    for t in range(N):
        r = set()
        for v in range(n):
            if v != o and o in walk(lambda x: stp(t, x), v)[0]: r.add(v)
        Rs.append(frozenset(r))
    def H1(t):
        p, x = walk(lambda y: nxt(t, y), o); return o not in p[p.index(x):]
    bump("runs")
    a = 0
    while a < N:
        b = a
        while b + 1 < N and lam[b + 1] == lam[a] and S[b + 1][1] == S[a][1]: b += 1
        bump("phases")
        ct = lam[a][o]; U = frozenset(z for z in range(n) if lam[a][z] == ct); u = len(U); T = {o, ct}; Uh = U - {o}
        sth = 1 if E.par[ct] == 1 else -1
        def wt(v): return E.weight(E.bit[v]) if rank[v] > rank[ct] else 0
        kw = {v: (wt(v), sth) for v in range(n)}
        def kap(t, z): return (E.weight(Xi[t][z][1]), sth * Xi[t][z][2])
        def F(t): return set(range(n)) - Rs[t] - {o}
        degU = len(set(g.succ[o]) & U)
        efb = [k for k in range(a, b) if FB[k]]          # in-phase fallbacks (transition k -> k+1, both ends in the phase)
        f = len(efb)
        # ---- transition kinds (P-N5-FX §0, P-N5-FBPOLY §0.1)
        for k in range(a, b):
            if S[k][1] != S[k + 1][1]: fail("TKIND_tau", k)
            if FB[k]:
                gates = E.improving(S[k][0], Xi[k]); src = {y for y, _ in gates}
                sw = {v for v in range(n) if g.owner[v] == 0 and S[k][0][v] != S[k + 1][0][v]}
                if sw != src: fail("TKIND_switch", k, sorted(sw), sorted(src))
                for v in src:
                    xs = max((w for y, w in gates if y == v), key=lambda w: (E.key(Xi[k][w]), w))
                    if S[k + 1][0][v] != xs: fail("TKIND_xstar", k, v)
        # ---- facts at every state / transition
        for t in range(a, b + 1):
            if Xi[t][o][0] != ct: fail("PHASE_ct", t)
            for z in U - {ct}:
                y = nxt(t, z); bump("AK_checks")
                if y not in U or kap(t, z) != (kw[z][0] + kap(t, y)[0], kw[z][1] + kap(t, y)[1]): fail("AK", t, z)
            if kap(t, ct) != (0, 0) or E.weight(Xi[t][nxt(t, ct)][1]) != 0: fail("A0K", t)
            for v in range(n):
                hp, hx = walk(lambda x: nxt(t, x), v); sp, sx = walk(lambda x: stp(t, x), v)
                hpre = hp[:hp.index(o) + 1] if o in hp else hp; spre = sp[:sp.index(o) + 1] if o in sp else sp
                if (o in hp) != (o in sp) or hpre != spre: fail("HP_agree", t, v)
                if o not in hp and v != o and v not in F(t): fail("HP_i", t, v)
                if o in hp and lam[t][v] != ct: fail("HP_ii", t, v)
            if not H1(t):
                bump("YB_checks")
                if E.weight(Xi[t][o][1]) != 0 or Xi[t][o][1] != 0: fail("YB_P", t)
                if o != ct and not (1 <= Xi[t][o][2] <= u - 1): fail("YB_len", t, Xi[t][o][2], u)
            else:
                Y = [y for y in set(g.succ[o]) if y in U and y in F(t)]; bump("KYF_checks")
                if SB[t][o] not in Y: fail("KYF_mem", t)
                elif kap(t, o) != (kw[o][0] + min(kap(t, y) for y in Y)[0], kw[o][1] + min(kap(t, y) for y in Y)[1]): fail("KYF_val", t)
        for t in range(a, b):
            for z in U:
                if kap(t, z) > kap(t + 1, z): fail("M2K", t, z)
        # ---- κ-FB-ROUND
        for k in efb:
            for v in U - {ct}:
                if g.owner[v] != 0: continue
                for x in set(g.succ[v]) & U:
                    bump("FBR_checks")
                    if kap(k + 1, v) < (kw[v][0] + kap(k, x)[0], kw[v][1] + kap(k, x)[1]): fail("FBR", k, v, x)
        # ---- path optima
        adjh = {}
        for v in Uh - {ct}:
            adjh[v] = [w for w in set(g.succ[v]) if w in Uh] if g.owner[v] == 0 else [w for w in g.succ[v] if w in Uh]
        upc = opt_paths(set(Uh), adjh, ct, kw, max(u - 2, 0)) if ct in Uh else None
        Uo = U - {ct} if o != ct else U
        adjo = {}
        for v in Uo - {o}:
            adjo[v] = [w for w in set(g.succ[v]) if w in Uo] if g.owner[v] == 0 else [w for w in g.succ[v] if w in Uo]
        upo = opt_paths(set(Uo), adjo, o, kw, len(Uo) - 1)
        if (ct in Uh and upc is None) or upo is None: bump("SKIP_paths")
        # θ-runs
        runid = {}; rs = a; rid = 0
        for t in range(a, b + 1):
            if t > a and Xi[t][o] != Xi[t - 1][o]: rid += 1
            runid[t] = rid
        # ---- κ-HAT-FREEZE
        if upc is not None:
            for t in range(a, b + 1):
                jt = sum(1 for k in efb if k < t)
                for z in Uh:
                    for j in range(0, min(jt, u - 2) + 1):
                        bv = upc(z, j)
                        if bv is not None:
                            bump("KHa_checks")
                            if kap(t, z) < bv: fail("KHa", t, z, j); break
                for z in F(t) & U:
                    bv = upc(z, u - 2); bump("KHb_checks")
                    if bv is None: fail("KHb_undef", t, z)
                    elif kap(t, z) > bv: fail("KHb", t, z)
                    elif u >= 2 and jt >= u - 2:
                        bump("KHc_checks")
                        if kap(t, z) != bv: fail("KHc", t, z)
        # ---- κ-PFZ (θ-run fallbacks) ; o = c_θ: the G_U form (FB-POLY (c))
        if upo is not None:
            for t in range(a, b + 1):
                jt = sum(1 for k in efb if k < t and runid[k] == runid[t])
                for z in Uo - {o}:
                    for j in range(0, min(jt, len(Uo) - 1) + 1):
                        bv = upo(z, j)
                        if bv is not None:
                            bump("KPFZ_checks" if o != ct else "KPFZc_checks")
                            ko = kap(t, o)
                            if kap(t, z) < (bv[0] + ko[0], bv[1] + ko[1]): fail("KPFZ" if o != ct else "KPFZc", t, z, j); break
        # ---- fallbacks: EXIT-SWITCH, FREEZE-EXIT, CN-ONLY
        cn = 0
        for j, k in enumerate(efb, 1):
            i = sum(1 for kk in efb if kk <= k and runid[kk] == runid[k])
            sw = [v for v in range(n) if g.owner[v] == 0 and S[k][0][v] != S[k + 1][0][v]]; SU = [v for v in sw if v in U - T]
            if not SU:
                cn += 1; bump("CNO_fallbacks")
                for y, z in E.improving(S[k][0], Xi[k]):
                    if lam[k][y] != y or lev(Xi[k][S[k][0][y]], Xi[k][z]) != -1: fail("CNO_gate", k, y, z); break
                if k + 1 != b: fail("CNO_last", k, b)
                continue
            good = []
            for v in SU:
                x = S[k + 1][0][v]; p = [v]; kind = None; seen = set()
                while True:
                    if x in T: kind = "ct" if (x == ct and o != ct) else "o"; p.append(x); break
                    if x == v: kind = "loop"; break
                    if x in seen: kind = "nocycle"; break
                    seen.add(x); p.append(x); x = nxt(k, x)
                bump("EXSW_kind_" + kind)
                if kind in ("ct", "o"):
                    good.append(v); e = p[-1]
                    if len(set(p)) != len(p): fail("EXSW_simple", k, v)
                    adj = adjo if e == o else adjh
                    for q, r in zip(p, p[1:]):
                        if r not in adj.get(q, ()): fail("EXSW_graph", k, v, q, r); break
                    s0 = (sum(kw[w][0] for w in p[1:-1]), sum(kw[w][1] for w in p[1:-1]))
                    ke = kap(k, e); xs = S[k + 1][0][v]
                    if kap(k, xs) != (s0[0] + ke[0], s0[1] + ke[1]): fail("EXSW_kappa", k, v)
                    if e == ct and j >= u - 1: fail("FEX_half_ct", k, v, j, u)
                    if e == o and o != ct and i >= u - 1: fail("FEX_half_o", k, v, i, u)
                    if o == ct and i >= u: fail("FEXc", k, v, i, u)      # FB-POLY (c) proof: i-th fallback, i >= |U|
            if not good: fail("EXSW", k, SU)
            if o != ct and j >= u - 1 and i >= u - 1:
                bump("FEX_hyp"); fail("FEX", k, j, i, u, SU)
            if j >= u - 1: bump("REG_j_ge_U-1_U%d" % min(u, 9))
        if cn > 1: fail("CNO_count", a, cn)
        # ---- THETA-AFTER
        if o != ct and u >= 2 and f >= u - 2:
            st0 = a if u == 2 else efb[u - 3] + 1
            ch = sum(1 for t in range(st0, b) if Xi[t][o] != Xi[t + 1][o]); bump("THA_phases")
            if u >= 3: bump("THA_phases_U3+")
            mx("THA_slack", ch - (degU + u - 2))
            if ch > degU + u - 2: fail("THA", a, ch, degU, u)
        # ---- FB-POLY
        if o != ct:
            bd = 1 if u == 2 else 1 + (u - 2) * (degU + u)
        else: bd = u
        mx("FBP_slack", f - bd); mx("FBCAP_slack", f - max(1, u - 2))
        if f > bd: fail("FBP", a, f, u, degU)
        # ---- P-N5-FX: R-STICK, X ≤ n(f + X_SN) + n − 1
        X = XSN = 0
        for k in range(a, b):
            cross = Rs[k] != Rs[k + 1]; X += cross
            pw, x = walk(lambda y: stp(k, y), o); cyc = pw[pw.index(x):]; cw = max(cyc, key=lambda v: rank[v])
            if not FB[k]:
                if cw != ct:
                    bump("RST_checks")
                    if not Rs[k] <= Rs[k + 1]: fail("RST", k)
                elif cross: XSN += 1
        mx("FX_slack", X - (n * (f + XSN) + n - 1)); mx("X_max", X)
        if X > n * (f + XSN) + n - 1: fail("FX", a, X, f, XSN)
        a = b + 1
    return acc

if __name__ == "__main__":
    args = sys.argv[1:]; st = None
    if args and args[0] == "--start": st = json.load(open(args[1])); args = args[2:]
    acc = {}
    for f in args:
        try: g = sox.load(f)
        except Exception: continue
        if len(sox.oddchoice(g)) != 1: continue
        if st is not None and isinstance(st, dict): st = st.get("start", st)
        analyse(g, acc, os.path.basename(f), st)
    print(json.dumps(acc, sort_keys=True))
