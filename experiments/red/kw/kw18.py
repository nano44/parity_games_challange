#!/usr/bin/env python3
"""Box 43 (L-RED successor 18): independent checker of
  L-NEW 21 docs/new/N5-KW-box42.md (sha1 349d553c): WLAG, ABOVE-h, CSTRICT, KW-FREEZE (a)-(c), PAR, H-PATH, DIR, CW;
  L-SI 10  docs/si/N5-KW-box15.md  (sha1 5ebbb3b6): W-ONCE, Fact A (as ABOVE-h), FRZ-U, LEN counts, KIND-MONO, CW-INT;
written from the note texts. Engine: Ξ from si.py Engine.evaluate (read-only); W (the (σ, τ)-play valuation) computed HERE from the play;
trace = sox.trace (= n5.run, SPEC S3) or ex16.trace from a start pair. 𝒞^1O asserted.
Objects: phase = λ_Ξ and τ constant; STRETCH = maximal run of states of a phase with R, θ = Ξ(o), w = W(o) constant (o ∈ R);
RUN = maximal run of consecutive non-fallback transitions inside a stretch; h = m* = the more relevant (higher rank) of c_θ, c_w;
π_v = v's (σ, τ)-path before its first visit of o (π_o = ∅); KIND(v) = A iff c_w ∈ π_v (v ∈ R ∖ {o}).
Prints FAIL_<check> lines (first 5 per check) and a final JSON of counters, regimes and maxima. Usage: kw18.py [--start f.json] g.pg ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import sox, ex16

def wval(g, E, s, t):
    """W: valuation of the (σ, τ)-play from every vertex, (cycle node, path bitmask, length), as Engine's format."""
    n = g.n; nx = [s[v] if g.owner[v] == 0 else t[v] for v in range(n)]; out = [None] * n
    for v in range(n):
        seen, p, x = {}, [], v
        while x not in seen: seen[x] = len(p); p.append(x); x = nx[x]
        cyc = p[seen[x]:]; c = max(cyc, key=lambda u: E.rank[u])
        # path from v to its first visit of c
        q, x = [], v
        while x != c: q.append(x); x = nx[x]
        mask = 0
        for u in q:
            if E.rank[u] > E.rank[c]: mask |= E.bit[u]
        out[v] = (c, mask, len(q))
    return out

def analyse(g, acc, name, st=None, cap=600):
    oc = sox.oddchoice(g); assert len(oc) == 1, "not C^1O"; o = oc[0]; n = g.n; rank = E_rank = None
    S, FB, E = (ex16.trace(g, st, cap=cap) if st is not None else sox.trace(g, cap=cap))
    N = len(S); ev = [E.evaluate(tuple(s)) for s, _ in S]; Xi = [e[0] for e in ev]
    W = [wval(g, E, s, t) for s, t in S]; lam = [tuple(x[0] for x in X) for X in Xi]; rank = E.rank
    def bump(k, v=1): acc[k] = acc.get(k, 0) + v
    def mx(k, v): acc[k] = max(acc.get(k, -10 ** 9), v)
    def fail(k, *a):
        bump("FAIL_" + k)
        if acc["FAIL_" + k] <= 5: print("FAIL_" + k, name, st is not None, *a, flush=True)
    key = E.key
    def nx(t, v): return S[t][0][v] if g.owner[v] == 0 else S[t][1][v]
    def pi(t, v):
        p, x, seen = [], v, set()
        while x != o and x not in seen: seen.add(x); p.append(x); x = nx(t, x)
        return p if x == o else None
    PI = []; Rs = []
    for t in range(N):
        d = {o: []}
        for v in range(n):
            if v != o:
                p = pi(t, v)
                if p is not None: d[v] = p
        PI.append(d); Rs.append(frozenset(d))
    bump("runs_traced")
    # Lemma G (a) sanity of the W engine: off R, Ξ = W
    for t in range(N):
        for v in range(n):
            if v not in Rs[t] and Xi[t][v] != W[t][v]: fail("ENG_G", t, v)
    def oncyc(t, nxt):
        seen, x = [], o
        while x not in seen: seen.append(x); x = nxt(x)
        return o in seen[seen.index(x):]
    H1 = [not oncyc(t, lambda v, t=t: S[t][0][v] if g.owner[v] == 0 else ev[t][1][v]) for t in range(N)]
    H2 = [not oncyc(t, lambda v, t=t: nx(t, v)) for t in range(N)]
    # PAR at every state
    for t in range(N):
        cth, cw = Xi[t][o][0], W[t][o][0]
        if rank[cw] > rank[cth]:
            bump("PAR_states")
            if E.par[cw] == 1: fail("PAR", t)
    # W-ONCE and WLAG inside phases
    inph = [k + 1 < N and lam[k] == lam[k + 1] and S[k][1] == S[k + 1][1] for k in range(N - 1)]
    for k in range(N - 2):
        if inph[k] and inph[k + 1] and not FB[k] and not FB[k + 1]:
            if Xi[k + 1] == Xi[k]:
                bump("WONCE_checks")
                if W[k + 2] != W[k + 1]: fail("WONCE", k)
            if W[k + 2] != W[k + 1]:
                bump("WLAG_checks")
                ok = False
                for y in range(n):
                    if g.owner[y] != 0: continue
                    z = S[k + 2][0][y]
                    if z == S[k][0][y] or key(Xi[k][z]) > key(Xi[k][S[k][0][y]]): continue   # z ∈ H_{k-1}(y)  (states k, k+1, k+2 here)
                    if key(Xi[k + 1][z]) > key(Xi[k][z]): ok = True; break
                if not ok: fail("WLAG", k)
    # stretches
    a = 0
    while a < N:
        b = a
        while b + 1 < N and lam[b + 1] == lam[a] and S[b + 1][1] == S[a][1] and Rs[b + 1] == Rs[a] and Xi[b + 1][o] == Xi[a][o] and W[b + 1][o] == W[a][o]: b += 1
        bump("stretches"); R = Rs[a]; r = len(R); th, w = Xi[a][o], W[a][o]; cth, cw = th[0], w[0]
        h = cth if rank[cth] >= rank[cw] else cw; hmask = sum(E.bit[u] for u in range(n) if rank[u] > rank[h])
        def coarse(x): return (x[0], x[1] & hmask)
        def ck(x): return (E.rew[x[0]], E.weight(x[1] & hmask))
        typ = ("U1" if H1[a] and H2[a] else "U2" if H2[a] else "U3" if H1[a] else "U23")
        U3x = (not H2[a]) and cw != o and rank[cw] > rank[cth]
        if U3x: bump("STR_U3x_" + typ)
        KW = (w[1] & hmask) if H2[a] else 0; KX = (th[1] & hmask) if H1[a] else 0
        # per state: ABOVE-h, CSTRICT, H-PATH
        for t in range(a, b + 1):
            for v in R:
                pm = sum(E.bit[u] for u in PI[t][v] if rank[u] > rank[h])
                if v != o or True:
                    if (W[t][v][1] & hmask) != (pm | KW) or (pm & KW): fail("ABOVEH_W", t, v)
                    if (Xi[t][v][1] & hmask) != (pm | KX) or (pm & KX): fail("ABOVEH_X", t, v)
                if W[t][v][0] != cw: fail("CW_NODE", t, v)
                if Xi[t][v][0] != cth: fail("CTH_NODE", t, v)
                if U3x:
                    kA = v != o and cw in PI[t][v]
                    if kA != bool(Xi[t][v][1] & E.bit[cw]): fail("HPATH", t, v)
            for x in R:
                if x == o or g.owner[x] != 0: continue
                aa = S[t][0][x]
                for z in set(g.succ[x]):
                    if z == aa or z not in R: continue
                    if ck(W[t][z]) > ck(W[t][aa]):
                        bump("CSTRICT_cases")
                        if not key(Xi[t][z]) > key(Xi[t][aa]): fail("CSTRICT", t, x, z)
        # runs
        k = a
        while k < b:
            if FB[k]: k += 1; continue
            k0 = k
            while k + 1 < b and not FB[k + 1]: k += 1
            k1 = k + 1; k = k1          # run states k0..k1
            L = k1 - k0; bump("RUN_runs"); mx("RUN_len", L)
            lastW = lastX = lastK = -1
            for t in range(k0 + 1, k1 + 1):
                if any(coarse(W[t][v]) != coarse(W[t - 1][v]) for v in R): lastW = t - k0
                if any(coarse(Xi[t][v]) != coarse(Xi[t - 1][v]) for v in R): lastX = t - k0
                if any({u for u in PI[t][v] if rank[u] > rank[h]} != {u for u in PI[t - 1][v] if rank[u] > rank[h]} for v in R): lastK = t - k0
            # a change at transition into state index i means coarse value at i differs from i-1; freeze from index n-1 means no change at i ≥ n
            mx("KWF_lastchange_minus_n", max(lastW, lastX) - (n - 1)); mx("FRZU_lastchange_minus_r", lastK - (r - 1))
            mx("FRZU_lastchange", lastK)
            if max(lastW, lastX) > n - 1: fail("KWFREEZE_a", k0, lastW, lastX, n)
            if lastK > r - 1: fail("FRZU", k0, lastK, r)
            if lastK >= 1: bump("FRZU_runs_with_change"); mx("FRZU_margin_changed", lastK - (r - 1))
            if max(lastW, lastX) >= 1: bump("KWF_runs_with_change"); mx("KWF_margin_changed", max(lastW, lastX) - (n - 1)); mx("KWF_margin_r_changed", max(lastW, lastX) - (r - 1))
            wch = sum(1 for t in range(k0, k1) if any(W[t + 1][v] != W[t][v] for v in R))
            xch = sum(1 for t in range(k0, k1) if any(Xi[t + 1][v] != Xi[t][v] for v in R))
            fch = sum(1 for t in range(k0, k1) if any(Xi[t + 1][v] != Xi[t][v] for v in range(n) if v not in R))
            mx("RUN_Wchanges", wch); mx("RUN_Xchanges", xch)
            if rank[cw] >= rank[cth]:
                if wch > (n - 1) + 2 * n * r: fail("KWF_b1", k0, wch)
            elif wch > n + 2 * n * r + fch: fail("KWF_b2", k0, wch)
            if rank[cth] >= rank[cw] and xch > (n - 1) + 2 * n * r: fail("KWF_c", k0, xch)
            # L-SI LEN counts (post-freeze, states ≥ k0 + r − 1)
            f0 = k0 + r - 1
            if rank[cth] >= rank[cw]:
                if xch > (r - 1) ** 2: fail("LEN_X", k0, xch, r)
            elif wch > (r - 1) ** 2: fail("LEN_W", k0, wch, r)
            # KIND-MONO (post-freeze part of the run) and CW-INT, U3/U23 with c_w ≻ c_θ
            if U3x:
                bump("U3x_runs"); mx("U3x_run_len", L)
                kinds = {}
                for t in range(max(k0, f0), k1 + 1):
                    for v in R:
                        if v == o: continue
                        kinds.setdefault(v, []).append(cw in PI[t][v])
                for v, ks in kinds.items():
                    ch = sum(1 for i in range(1, len(ks)) if ks[i] != ks[i - 1]); bump("KM_postfreeze_kindchanges", ch)
                    if ch > 1: fail("KINDMONO_count", k0, v, ch)
                    for i in range(1, len(ks)):
                        if ks[i] != ks[i - 1] and ks[i] != (E.par[cw] == 0): fail("KINDMONO_dir", k0, v)
                # CW-INT: maximal sub-intervals with no kind change and no kind-B switch
                seg = 0
                for t in range(k0, k1):
                    kc = any((cw in PI[t][v]) != (cw in PI[t + 1][v]) for v in R if v != o)
                    bsw = any(g.owner[v] == 0 and S[t][0][v] != S[t + 1][0][v] and cw not in PI[t][v] for v in R if v != o)
                    if kc or bsw: seg = 0; continue
                    if S[t][0][cw] != S[t + 1][0][cw]:
                        seg += 1; bump("CWINT_cwswitches"); mx("CWINT_max", seg - (len(set(g.succ[cw])) - 1))
                        if seg > len(set(g.succ[cw])) - 1: fail("CWINT", t, seg)
        # DIR / CW over the whole stretch (U3x)
        if U3x:
            P_A = E.par[cw] == 0; kap = 0; Bs = 0; fs = 0; cwsw = 0
            for t in range(a, b):
                if FB[t]: fs += 1
                kc = [v for v in R if v != o and (cw in PI[t][v]) != (cw in PI[t + 1][v])]
                if kc: kap += 1
                if any(g.owner[v] == 0 and S[t][0][v] != S[t + 1][0][v] and cw not in PI[t][v] for v in R if v != o): Bs += 1
                if g.owner[cw] == 0 and S[t][0][cw] != S[t + 1][0][cw]: cwsw += 1
                wflat = not FB[t] and all(W[t + 1][v] == W[t][v] for v in R)
                if wflat:
                    bump("DIR_wflat")
                    for v in kc:
                        bump("DIR_kindchanges_at_wflat")
                        if (cw in PI[t + 1][v]) != P_A: fail("DIR", t, v)
            # CASC-B (L-NEW §5 / L-SI §5): in a maximal run Γ of consecutive W-flat transitions with no kind change, a kind-B vertex v
            # switches only at steps ≤ |π_v| − 2 (step = index of the transition inside Γ)
            i = -1
            for t in range(a, b):
                kc = any((cw in PI[t][v]) != (cw in PI[t + 1][v]) for v in R if v != o)
                wflat = not FB[t] and all(W[t + 1][v] == W[t][v] for v in R)
                if not wflat or kc: i = -1; continue
                i += 1
                for v in R:
                    if v == o or g.owner[v] != 0 or cw in PI[t][v] or S[t][0][v] == S[t + 1][0][v]: continue
                    bump("CASCB_switches"); mx("CASCB_slack", i - (len(PI[t][v]) - 2))
                    if i > len(PI[t][v]) - 2: fail("CASCB", t, v, i, len(PI[t][v]))
            bump("CW_stretches"); bump("CW_switches", cwsw); bump("U3x_kindchange_transitions", kap)
            bound = len(set(g.succ[cw])) * (1 + Bs + kap + fs); mx("CW_slack", cwsw - bound)
            if cwsw > bound: fail("CW", a, cwsw, bound)
        a = b + 1
    return acc

if __name__ == "__main__":
    args = sys.argv[1:]; st = None
    if args and args[0] == "--start": st = json.load(open(args[1])); st = st.get("start", st); args = args[2:]
    acc = {}
    for f in args:
        try: g = sox.load(f)
        except Exception: continue
        if len(sox.oddchoice(g)) != 1: continue
        analyse(g, acc, os.path.basename(f), st)
    print(json.dumps(acc, sort_keys=True))
