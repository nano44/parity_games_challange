#!/usr/bin/env python3
"""REFEREE successor 22: own control for packet P-N5-S4B (L-SI box 63, l-si 68fa36619, sha1 f1b65da5). Own engine rl_engine
(written from SPEC only); no lane code. At every state k with I_tau_k != {} of an N5 run:
  H'_k := G with Odd v restricted to A(v) = {tau_k(v)} u {w : (v, w) in I_tau_k}, Even v to sigma_k(v)   (SPEC S4b)
  tn   := S1's procedure on H'_k against sigma_k (rl_engine.evaluate on g.restrict, not dual)
  NEXT  tau_(k+1) = tn unless k -> k+1 is an Odd fallback (fb with I_sigma_k = {})          (Lemma S4B-OPT, second half)
  LOC   one-switch deviation: for every Odd v and w in A(v) minus {tn(v)}, tn with v -> w makes no vertex strictly better for Odd
        (a necessary condition of pointwise optimality; every state, no cap). (s22's first LOC compared val(w) with val(tn(v)); that
        is not a valid test when v is the cycle node of both plays: ffin5_n32 state 0, v 28, w 12, the switch changes no value.)
  ENUM  if prod |A(v)| <= CAP: for every positional Odd rho of H'_k and every x, key val(sigma_k, tn)(x) <= key val(sigma_k, rho)(x)
  KEEP  at every tau-stretch transition (tau_(k+1) = tau_k) with I_tau_k != {}: tau_k = tn                 (Corollary S4B-KEEP)
  ODDFB every Odd fallback changes tau (so it is never a tau-stretch transition)
MUT 1: tn replaced by tau_k (must bite: ENUM / LOC violations). Usage: s4b_probe.py FILES.pg (env MAXN, CAP, MUT, STARTF, PARTIAL)"""
import sys, os, itertools
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
MUT = int(os.environ.get("MUT", "0")); CAP = int(os.environ.get("CAP", "4096"))
EX = []


def fail(cnt, tag, *a):
    cnt[tag + "_V"] += 1
    if len(EX) < 20: EX.append((tag,) + a)


def vals(g, s, t):
    nx = [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]
    return [g.key(RE.play_value(g, nx, v)) for v in range(g.n)]


def analyse(cnt, g, start, name):
    st = RE.run(g, start); n = g.n; K = len(st) - 1
    for k in range(K):
        S, It = st[k], st[k]["It"]
        if not It: continue
        s, t = S["s"], S["t"]
        A = {v: {t[v]} for v in range(n) if g.owner[v] == 1}
        for v, w in It: A[v].add(w)
        keep = [sorted(A[v]) if g.owner[v] == 1 else [s[v]] for v in range(n)]
        _, ch = RE.evaluate(g.restrict(keep), s)
        tn = [ch[v] if g.owner[v] == 1 else None for v in range(n)]
        oddfb = S["fb"] and not S["Is"]
        cnt["states"] += 1
        tnext = st[k + 1]["t"]
        if oddfb:
            cnt["oddfb"] += 1
            if tnext == t: fail(cnt, "ODDFB", name, k)
        elif tnext != tn: fail(cnt, "NEXT", name, k)
        if tnext == t:
            cnt["keep_chk"] += 1
            if t != tn: fail(cnt, "KEEP", name, k)
        if MUT == 1: tn = list(t)
        base = vals(g, s, tn)
        for v in A:
            for w in A[v]:
                if w == tn[v]: continue
                cnt["loc_chk"] += 1
                dev = list(tn); dev[v] = w; r = vals(g, s, dev)
                if any(r[x] < base[x] for x in range(n)): fail(cnt, "LOC", name, k, v, w)   # Odd minimises the Even key
        odd = sorted(A); sizes = [len(A[v]) for v in odd]; tot = 1
        for z in sizes: tot *= z
        if tot > CAP: cnt["enum_skip"] += 1; continue
        cnt["enum_states"] += 1
        for combo in itertools.product(*[sorted(A[v]) for v in odd]):
            rho = list(tn)
            for v, w in zip(odd, combo): rho[v] = w
            cnt["rhos"] += 1
            r = vals(g, s, rho)
            if any(base[x] > r[x] for x in range(n)): fail(cnt, "ENUM", name, k)


def partial_start(g, path):
    """PARTIAL=1: the lane's n5x start_pair rule: best-reward start (SPEC S3), overwritten by the file's «v:w» moves; every given move must
    be an edge of a vertex of the right owner (SIGMA0 lines Even, TAU0 lines Odd), else ValueError."""
    s, t = RE.best_reward_start(g); s, t = list(s), list(t)
    for l in open(path):
        a = l.split()
        if not a: continue
        own = 0 if a[0] == "SIGMA0" else 1 if a[0] == "TAU0" else None
        for tok in a[1:]:
            v, w = map(int, tok.split(":"))
            if own is None or g.owner[v] != own or w not in g.succ[v]: raise ValueError((v, w))
            (s if own == 0 else t)[v] = w
    return s, t


def main(a):
    import core_probe as CP
    cnt = Counter()
    for p in a:
        if p.endswith(".start"): continue
        try: g = RE.parse(p)
        except Exception: cnt["parse_err"] += 1; continue
        if g.n > int(os.environ.get("MAXN", "100")): cnt["skip_big"] += 1; continue
        sp = os.environ.get("STARTF") or p[:-3] + ".start"; ex = None
        if os.path.exists(sp):
            try: ex = CP.parse_start(g, sp) if not os.environ.get("PARTIAL") else partial_start(g, sp)
            except Exception: cnt["start_err"] += 1
        cnt["GAMES"] += 1
        try: analyse(cnt, g, ex, os.path.basename(p))
        except RuntimeError: cnt["maxit"] += 1
    for k in sorted(cnt): print(k, cnt[k])
    print("VIOLATIONS", sum(v for k, v in cnt.items() if k.endswith("_V")))
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
