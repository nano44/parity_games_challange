#!/usr/bin/env python3
"""REFEREE succ. 17 probe for packet P-N5-SDPRIME (docs/si/P-N5-SDPRIME-box25.md, sha1 54678c38..., freeze l-si edc14c51).
Own engine only (rl_engine; helpers from my predecessor's depth_probe.py: cycles, play, Hb, dstar). No lane code.
Frames: W next = (sigma, tau), honest next = (sigma, sigmabar). Phase = (lambda_Xi, tau) constant. A fallback-free run: a maximal run of
in-phase S4a transitions (lambda_W may change: (H1')). For every end state b of a fallback-free run: a := the least state of the run with
sigmabar constant on [a, b] and (H3') (every W-cycle / honest cycle of b is one at every state of [a, b]). Depths dW, dH, d by the packet's
recursion; (H4') = the recursion is well founded. Checks (when (H4') holds; GEN_W checked in its used form, see GENW):
 SDV   every v: W-play at b at every t in [a + dW(v), b], honest play at b at every t in [a + dH(v), b]
 SD    b - a <= max d <= |Even - T| <= n - 1       SHARP b - a = max d
 SA    step (A): Even v not in T, y = sigma_b v, s = a + max(dW y, dH y): y in {sigma_t v} u I_sigma_t(v) for t in [s, b]
 SB    step (B): W_{t+1}(v) = W_b(v) for t in [s, b - 1]
 GENW  used form: some v, t with W_t(v) = W_b(v), the same cycle, different W-plays (counted; the theorem needs GEN_W)
 REM   Remark: where R77's (H1) (lambda_W constant), (H3) (common cycles constant on [a77, b]), (H4) (H_b acyclic) hold on [a77, b]:
       (H3') and (H4') hold on [a77, b] and d(v) <= d*(v) for every v, and STATIC-DEPTH's a77 >= our a
 COV   pieces (maximal sigmabar-constant stretches of a fallback-free run): whole piece satisfies (H3'), (H4'), GEN_W(used) / R77's hyps
 EPOCH per piece: epochs from the end, CF = cycle-appearance transitions; k - 1 <= CF always; if (H4') and GEN_W(used) at every epoch end:
       every epoch b_i - a_i <= max d_i and b - a <= (CF + 1) n - 1
Mutations: MUT=1 SDV from a + d - 1;  MUT=2 (H3') with the W frame only (honest cycles not required);  MUT=3 d with the W frame only
 (d(v) := 1 + dW(y));  MUT=4 CF counts W-cycle appearances only.
Usage: sdprime_probe.py rand N nmin nmax kmax seed | list FILE BASE | files...  (RANDSTARTS 2, MAXN 60)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, epr_probe as E, core_probe as CP
from depth_probe import cycles, play, Hb, dstar
EX = []
MUT = int(os.environ.get("MUT", "0"))


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def cycverts(cs): return {v for c in cs for v in c}


def depths(g, x, TW, TH):
    """packet recursion; returns (dW, dH) dicts or None if not well founded"""
    n = g.n; memo = {}; onstack = set()
    def rec(v, f):  # f = 'W' or 'H'
        key = (v, f)
        if key in memo: return memo[key]
        if (f == 'W' and v in TW) or (f == 'H' and v in TH): return 0
        if key in onstack: raise ValueError
        onstack.add(key)
        if g.owner[v] == 1:
            val = rec(x["t"][v], 'W') if f == 'W' else rec(x["sb"][v], 'H')
        else:
            y = x["s"][v]
            if v in TH and v not in TW: val = rec(y, 'W') if f == 'W' else 0
            elif v in TW and v not in TH: val = rec(y, 'H') if f == 'H' else 0
            else:  # Even outside T
                val = 1 + (rec(y, 'W') if MUT == 3 else max(rec(y, 'W'), rec(y, 'H')))
        onstack.discard(key); memo[key] = val; return val
    try:
        dW = {v: rec(v, 'W') for v in range(n)}; dH = {v: rec(v, 'H') for v in range(n)}
    except (ValueError, RecursionError): return None
    return dW, dH


def persist(st, a, b, frames=(0, 1)):
    """every cycle of state b (in each frame of frames) is a cycle at every state of [a, b]"""
    return all(st[b]["cyc"][f] <= st[t]["cyc"][f] for t in range(a, b + 1) for f in frames)


def genw_used(g, st, a, b):
    Wb = st[b]["W"]
    for t in range(a, b + 1):
        for v in range(g.n):
            if st[t]["W"][v] == Wb[v]:
                p1, p2 = play(st[t]["nxW"], v), play(st[b]["nxW"], v)
                if p1 != p2 and set(p1[1]) == set(p2[1]): return False
    return True


def analyse(g, start, cnt, name):
    st = RE.run(g, start); n = g.n
    Q = {v for v in range(n) if g.owner[v] == 1}
    nE = sum(1 for v in range(n) if g.owner[v] == 0)
    for x in st:
        x["nxH"] = [x["s"][v] if g.owner[v] == 0 else x["sb"][v] for v in range(n)]
        x["nxW"] = [x["s"][v] if g.owner[v] == 0 else x["t"][v] for v in range(n)]
        x["W"] = E.wval(g, x["s"], x["t"])
        x["D"] = frozenset(u for u in Q if x["sb"][u] != x["t"][u])
        x["cyc"] = (cycles(x["nxW"]), cycles(x["nxH"]))   # index 0 = W, 1 = honest
        x["lamW"] = tuple(w[0] for w in x["W"])
        x["Isv"] = {}
        for (v, w) in x["Is"]: x["Isv"].setdefault(v, set()).add(w)
    K = len(st); k = 0
    while k < K:
        j = k; lam = tuple(v[0] for v in st[k]["Xi"])
        while j + 1 < K and tuple(v[0] for v in st[j + 1]["Xi"]) == lam and st[j + 1]["t"] == st[k]["t"]: j += 1
        r = k
        while r <= j:
            e = r
            while e < j and not st[e]["fb"]: e += 1
            run(g, st, r, e, cnt, name, nE)
            r = e + 1
        k = j + 1


def run(g, st, r, e, cnt, name, nE):
    n = g.n; cnt["FF_runs"] += 1
    frames = (0,) if MUT == 2 else (0, 1)
    for b in range(r, e + 1):
        a = b
        while a > r and st[a - 1]["sb"] == st[b]["sb"] and persist(st, a - 1, b, frames): a -= 1
        if a == b: continue
        x = st[b]; TW = cycverts(x["cyc"][0]); TH = cycverts(x["cyc"][1]); T = TW | TH
        dd = depths(g, x, TW, TH)
        cnt["SD_cand"] += 1
        if x["cyc"][0] != x["cyc"][1]: cnt["SD_cand_TWneTH"] += 1
        if any(st[t]["lamW"] != x["lamW"] for t in range(a, b + 1)): cnt["SD_cand_lamWchg"] += 1
        if dd is None: cnt["H4p_fail"] += 1; continue
        dW, dH = dd
        gen = genw_used(g, st, a, b)
        if not gen: cnt["GENW_used_fail"] += 1
        ev_out = [v for v in range(n) if g.owner[v] == 0 and v not in T]
        md = max((dW[v] for v in ev_out), default=0)
        cnt["SD_chk"] += 1
        if x["cyc"][0] != x["cyc"][1]: cnt["SD_chk_TWneTH"] += 1
        if any(st[t]["lamW"] != x["lamW"] for t in range(a, b + 1)): cnt["SD_chk_lamWchg"] += 1
        if st[b]["D"]: cnt["SD_withgate"] += 1
        if not (md <= len(ev_out) <= n - 1): fail(cnt, "SDcap", name, a, b)
        if b - a > md:
            if gen: fail(cnt, "SD", name, a, b, md)
            else: cnt["SD_over_nonGEN"] += 1
        if b - a == md: cnt["SD_sharp"] += 1
        cnt["MAX_SD_len"] = max(cnt["MAX_SD_len"], b - a)
        sub = 1 if MUT == 1 else 0
        for v in range(n):
            for f, dv, key in ((0, dW[v], "nxW"), (1, dH[v], "nxH")):
                pb = play(x[key], v)
                for t in range(max(a, a + dv - sub), b + 1):
                    cnt["SDV_chk"] += 1
                    if play(st[t][key], v) != pb:
                        if gen: fail(cnt, "SDV", name, a, b, v, f, t, dv)
                        else: cnt["SDV_nonGEN"] += 1
                        break
        for v in ev_out:
            y = x["s"][v]; s = a + max(dW[y], dH[y])
            for t in range(s, b + 1):
                cnt["SA_chk"] += 1
                if not (st[t]["s"][v] == y or y in st[t]["Isv"].get(v, ())): fail(cnt, "SA", name, a, b, v, t)
            for t in range(s, b):
                cnt["SB_chk"] += 1
                if st[t + 1]["W"][v] != x["W"][v]: fail(cnt, "SB", name, a, b, v, t)
        # Remark vs R77
        a77 = b
        while a77 > r and st[a77 - 1]["sb"] == x["sb"] and st[a77 - 1]["cyc"] == x["cyc"] and st[a77 - 1]["lamW"] == x["lamW"]: a77 -= 1
        if x["cyc"][0] == x["cyc"][1] and a77 < b:
            cv, succ = Hb(g, x); ds = dstar(g, cv, succ)
            if ds is not None:
                cnt["REM_chk"] += 1
                if a77 < a: fail(cnt, "REM_H3p", name, a77, a, b)
                if any(max(dW[v], dH[v]) > ds.get(v, 0) for v in range(n)): fail(cnt, "REM_d", name, a, b)
    # pieces
    p0 = r
    for t in range(r, e + 1):
        if t == e or st[t + 1]["sb"] != st[t]["sb"]:
            piece(g, st, p0, t, cnt, name); p0 = t + 1


def piece(g, st, a, b, cnt, name):
    n = g.n; cnt["PIECES"] += 1
    x = st[b]; TW = cycverts(x["cyc"][0]); TH = cycverts(x["cyc"][1])
    ok3 = persist(st, a, b); dd = depths(g, x, TW, TH) if ok3 else None
    L1 = "_L%d" % min(b - a, 2)   # pieces by length: L0 (one state), L1 (one transition), L2 (>= 2 transitions)
    cnt["PIECES" + L1] += 1
    if ok3 and dd is not None and genw_used(g, st, a, b): cnt["COV_SDp"] += 1; cnt["COV_SDp" + L1] += 1
    if not ok3: cnt["COVX_H3p" + L1] += 1
    elif dd is None: cnt["COVX_H4p" + L1] += 1
    if all(st[t]["cyc"] == x["cyc"] and st[t]["lamW"] == x["lamW"] for t in range(a, b + 1)) and x["cyc"][0] == x["cyc"][1]:
        cv, succ = Hb(g, x)
        if dstar(g, cv, succ) is not None and genw_used(g, st, a, b): cnt["COV_R77"] += 1; cnt["COV_R77" + L1] += 1
    # epochs
    eps = []; bi = b
    while bi >= a:
        ai = bi
        while ai > a and persist(st, ai - 1, bi): ai -= 1
        eps.append((ai, bi)); bi = ai - 1
    eps.reverse(); k = len(eps)
    fr = (0,) if MUT == 4 else (0, 1)
    CF = sum(1 for t in range(a, b) if any(not st[t + 1]["cyc"][f] <= st[t]["cyc"][f] for f in fr))
    cnt["EP_chk"] += 1; cnt["MAX_EPOCHS"] = max(cnt["MAX_EPOCHS"], k); cnt["MAX_CF"] = max(cnt["MAX_CF"], CF)
    if CF >= 1: cnt["PIECES_CF1"] += 1
    if b - a != sum(bb - aa for aa, bb in eps) + k - 1: fail(cnt, "EP_sum", name, a, b)
    if k - 1 > CF: fail(cnt, "EP_k" + ("_MUT4" if MUT == 4 else ""), name, a, b, k, CF)
    allok = True; bound_ok = True
    for (aa, bb) in eps:
        y = st[bb]; d2 = depths(g, y, cycverts(y["cyc"][0]), cycverts(y["cyc"][1]))
        if d2 is None or not genw_used(g, st, aa, bb): allok = False; continue
        ev_out = [v for v in range(n) if g.owner[v] == 0 and v not in cycverts(y["cyc"][0]) | cycverts(y["cyc"][1])]
        if bb - aa > max((d2[0][v] for v in ev_out), default=0): bound_ok = False
    if allok:
        cnt["EP_hyp"] += 1
        if not bound_ok: fail(cnt, "EP_epoch", name, a, b)
        if b - a > (CF + 1) * n - 1: fail(cnt, "EPOCH", name, a, b, CF)
    cnt["MAX_PIECE_minus_n1_plus1000"] = max(cnt["MAX_PIECE_minus_n1_plus1000"], b - a - (n - 1) + 1000)


def main(a):
    cnt = Counter(); rng = random.Random(2525); nst = int(os.environ.get("RANDSTARTS", "2"))
    def do(g, name, r, extra=None):
        starts = ([extra] if extra else []) + ([RE.best_reward_start(g)] if (not extra or nst > 0) else []) + \
                 [D.rand_start(g, r) for _ in range(nst)]
        for j, s0 in enumerate(starts):
            cnt["RUNS"] += 1; analyse(g, s0, cnt, "%s/%d" % (name, j))
    if a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            do(D.rand_ck(r2, nn, r2.randint(0, min(km, nn - 1))), "rand%d" % i, rng)
    elif a[0] == "list":
        base = a[2]
        for l in open(a[1]):
            p = l.split()
            if not p: continue
            g = RE.parse(os.path.join(base, p[0]))
            if g.n > int(os.environ.get("MAXN", "60")): cnt["skip_big"] += 1; continue
            ex = CP.parse_start(g, os.path.join(base, p[1])) if len(p) > 1 else None
            cnt["GAMES"] += 1; do(g, p[0], random.Random(p[0]), ex)
    else:
        for path in a:
            if path.endswith(".start"): continue
            g = RE.parse(path)
            if g.n > int(os.environ.get("MAXN", "60")): cnt["skip_big"] += 1; continue
            sp = path[:-3] + ".start"
            ex = CP.parse_start(g, sp) if os.path.exists(sp) else None
            cnt["GAMES"] += 1; do(g, os.path.relpath(path), random.Random(os.path.relpath(path)), ex)
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
