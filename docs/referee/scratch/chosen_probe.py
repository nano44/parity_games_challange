#!/usr/bin/env python3
"""REFEREE succ. 15 probe for packet P-N5-CHOSEN (docs/si/P-N5-CHOSEN-box19.md, pin 9196c318, sha1 764cfbb3...). Own engine only (rl_engine;
helpers of my lane's flip_probe). No lane code. Per phase ((lambda_Xi, tau) constant), per class U_c, Q_c := Q n U_c - {c}, T := Q u {c}:
 CLS     every rho event at q in Q_c is exactly one of CYC (q on an honest cycle at t or t+1), ROUTE, RELAY (P-N5-FLIP §3 / packet §1)
 CHO     Lemma CHOSEN at a RELAY event: y* = sigmabar_t(q) in U_c, y*'s play at t avoids q; its exit e != c; and (kappa_t(e) != kappa_t+1(e)
         or e's play at t+1 passes q (TOG));  CHOX  e in Q_c - {q}
 CHAIN   RELAY-CHAIN: e_0 = q, e_i+1 = chosen exit of e_i while RELAY: distinct, <= |Q_c| - 1 steps, ends at ROUTE / CYC event or TOG
 CNTB    consequence (b): per phase and class, sum_q rho_q <= |Q_c| (ROUTE_c + CYC_c + TOG_c)
 TVE     Lemma TV-END at EVERY state where (H) holds (not only after R56 (g)'s trigger): kappa_t = TV_Theta on U_c - T => no Even vertex of
         U_c - T switches, Xi|Q_c unchanged, (H) at t + 1   (TV_Theta from exact kappa_opt by simple-path enumeration in G_c, G_c^q)
 TVG     sanity: landed R56 (g) (trigger: |U_c| - 1 fallbacks of the phase and of the Q-run before t) => (H)
 CTRL    count of switches in U_c - T at non-(H) states (detection works);  MUT=1 CHOSEN with sigmabar_t+1(q) (lane's control);
         MUT=2 (H) read with TV' := kappa_opt_c only (the q-terms dropped): TVE must fail somewhere
Usage: chosen_probe.py rand N nmin nmax kmax seed | files[:start]...  (env RANDSTARTS 2, MAXN 64, BUDGET 2e6 path extensions per class)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, hon_probe as HP
from flip_probe import nxt, kap, kwt, add, on_cycle, class_exit
EX = []
MUT = int(os.environ.get("MUT", "0"))
BUDGET = float(os.environ.get("BUDGET", "2e6"))


class Over(Exception): pass


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def on_play(nx, z, v):
    """does z's honest play (lasso) pass v?"""
    pre, cyc = RE.lasso(nx, z)
    return v in pre or v in cyc


def kopt(g, c, U, allowed, sink, s0):
    """best kappa-weight (sum of kwt over p minus the end) of a simple path from each z in allowed to sink, inside allowed u {sink};
    Even vertices keep their edges inside, Odd vertices are forced (their only edge, if inside)."""
    inside = set(allowed) | {sink}; best = {}; used = 0
    for z in allowed:
        b = None; stack = [(z, (z,), (0, 0))]
        while stack:
            v, p, w = stack.pop(); used += 1
            if used > BUDGET: raise Over()
            if v == sink:
                if b is None or w > b: b = w
                continue
            w2 = add(w, kwt(g, c, v))
            for y in g.succ[v]:
                if y in inside and y not in p: stack.append((y, p + (y,), w2))
        best[z] = b
    return best


def analyse(g, start, cnt, name):
    st = RE.run(g, start); n = g.n
    Q = {v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1}
    for x in st: x["nx"] = nxt(g, x["s"], x["sb"])
    K = len(st); k = 0
    while k < K:
        j = k; lam = tuple(v[0] for v in st[k]["Xi"])
        while j + 1 < K and tuple(v[0] for v in st[j + 1]["Xi"]) == lam and st[j + 1]["t"] == st[k]["t"]: j += 1
        phase(g, st, k, j, lam, Q, cnt, name)
        k = j + 1


def phase(g, st, a, b, lam, Q, cnt, name):
    n = g.n; cnt["PHASES"] += 1
    C = sorted({lam[v] for v in range(n)})
    U = {c: {v for v in range(n) if lam[v] == c} for c in C}
    for c in C:
        Qc = sorted((Q & U[c]) - {c}); stop = set(Qc) | {c}; T = Q | {c}
        rho = Counter(); route = cyc = tog = 0
        for t in range(a, b):
            s0, s1 = st[t], st[t + 1]; nx0, nx1 = s0["nx"], s1["nx"]
            ev = [q for q in Qc if s0["Xi"][q] != s1["Xi"][q]]
            kind = {}
            for q in ev:
                rho[q] += 1
                if on_cycle(nx0, q) or on_cycle(nx1, q): kind[q] = "CYC"; cyc += 1; continue
                ch = any(class_exit(nx0, y, stop) != class_exit(nx1, y, stop) for y in g.succ[q] if y in U[c])
                kind[q] = "ROUTE" if ch else "RELAY"
                if ch: route += 1
            cnt["EV_ROUTE"] += sum(1 for q in kind if kind[q] == "ROUTE"); cnt["EV_CYC"] += sum(1 for q in kind if kind[q] == "CYC")
            cnt["EV_RELAY"] += sum(1 for q in kind if kind[q] == "RELAY")

            def chosen(q):
                ys = (s1 if MUT == 1 else s0)["sb"][q]
                if ys not in U[c] or on_play(nx0, ys, q): fail(cnt, "CHO", name, t, c, q, "y*")
                p, e = class_exit(nx0, ys, stop)
                return e
            for q in [q for q in kind if kind[q] == "RELAY"]:
                cnt["CHO_chk"] += 1
                e = chosen(q)
                if e is None or e == c: fail(cnt, "CHO", name, t, c, q, "e=c"); continue
                if e not in Qc or e == q: fail(cnt, "CHOX", name, t, q, e)
                isrho = kap(g, s0["Xi"][e]) != kap(g, s1["Xi"][e]); istog = on_play(nx1, e, q)
                if istog:
                    cnt["TOG_seen"] += 1; cnt["TOG_with_rho_at_e"] += isrho
                    if cnt["TOG_ex"] < 3: cnt["TOG_ex"] += 1; EX.append(("TOG", name, t, c, q, e, isrho))
                if not (isrho or istog): fail(cnt, "CHO", name, t, c, q, e)
                # chain
                seq = [q]; end = None
                while True:
                    cur = seq[-1]
                    if kind.get(cur) != "RELAY":
                        end = kind.get(cur, "NONE"); break
                    nxt_e = chosen(cur)
                    if nxt_e is None or nxt_e == c: end = "BAD"; break
                    if nxt_e not in kind:
                        end = "TOG" if on_play(nx1, nxt_e, cur) else "NOTOG"; break
                    if nxt_e in seq: end = "REPEAT"; break
                    seq.append(nxt_e)
                cnt["CHAIN_chk"] += 1; cnt["CHAIN_MAXLEN"] = max(cnt["CHAIN_MAXLEN"], len(seq) - 1)
                cnt["CHAIN_END_" + end] += 1
                if end not in ("ROUTE", "CYC", "TOG") or len(seq) - 1 > len(Qc) - 1: fail(cnt, "CHAIN", name, t, c, q, end, len(seq))
                if end == "TOG": tog += 1
        if sum(rho.values()):
            cnt["CNTB_chk"] += 1
            if sum(rho.values()) > len(Qc) * (route + cyc + tog): fail(cnt, "CNTB", name, a, c)
        tv_end(g, st, a, b, c, U[c], Qc, T, cnt, name)


def tv_end(g, st, a, b, c, Uc, Qc, T, cnt, name):
    inner = sorted(Uc - T)
    if not inner: return
    try:
        oc = kopt(g, c, Uc, [z for z in Uc if z not in (T - {c}) and z != c], c, None)
        oq = {q: kopt(g, c, Uc, [z for z in Uc if z not in T], q, None) for q in Qc}
    except Over: cnt["TV_UNK"] += 1; return
    runs = []; k = a                                    # Q_c-runs
    while k <= b:
        j = k
        while j + 1 <= b and all(st[j + 1]["Xi"][q] == st[k]["Xi"][q] for q in Qc): j += 1
        runs.append((k, j)); k = j + 1
    Qall = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
    fb = [t for t in range(a, b) if st[t]["fb"]]
    def TV(z, k):
        cand = [oc[z]] if oc.get(z) is not None else []
        if MUT != 2 or not cand:
            cand += [add(oq[q][z], kap(g, st[k]["Xi"][q])) for q in Qc if oq[q].get(z) is not None]
        return max(cand) if cand else None
    def H(k): return all(kap(g, st[k]["Xi"][z]) == TV(z, k) for z in inner)
    for (r0, r1) in runs:
        for t in range(r0, r1 + 1):
            h = H(t)
            # R56 (g) sanity: Q-run containing t (all of Q constant) and fallbacks before t
            q0 = t
            while q0 > a and all(st[q0 - 1]["Xi"][q] == st[t]["Xi"][q] for q in Qall): q0 -= 1
            if sum(1 for f in fb if f < t) >= len(Uc) - 1 and sum(1 for f in fb if q0 <= f < t) >= len(Uc) - 1:
                cnt["TVG_chk"] += 1
                if not h and MUT != 2: fail(cnt, "TVG", name, t, c)
            if not h:
                if t < b and any(st[t]["s"][x] != st[t + 1]["s"][x] for x in inner if g.owner[x] == 0): cnt["CTRL_switch_nonH"] += 1
                continue
            cnt["H_states"] += 1
            if len(Qc) >= 2: cnt["H_states_Qc2"] += 1
            if t == b: continue
            cnt["TVE_chk"] += 1; cnt["TVE_Qc%d" % min(len(Qc), 3)] += 1
            sw = [x for x in inner if g.owner[x] == 0 and st[t]["s"][x] != st[t + 1]["s"][x]]
            same = all(st[t + 1]["Xi"][q] == st[t]["Xi"][q] for q in Qc)
            if sw or not same or not H(t + 1): fail(cnt, "TVE", name, t, c, sw, same)


def main(a):
    cnt = Counter(); rng = random.Random(1557); nst = int(os.environ.get("RANDSTARTS", "2"))
    def do(g, name, r, extra=None):
        starts = ([extra] if extra else []) + ([] if (extra and os.environ.get("NOS3")) else [RE.best_reward_start(g)]) + [D.rand_start(g, r) for _ in range(nst)]
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
