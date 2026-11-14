#!/usr/bin/env python3
"""L-NEW box 144 MERGE-CHARGE on 2-wide deg-2 IDEAL-ACYC ladders (R178 §1 rule; box143/cause.py analyse for classes).
For every DELSTEP t (least mover x of step t is delayed, box 143 STEP-DELAY) with new option k:
- plays (mover sequences) of x's faces k and kbar at state t-2; merge vertex m = first mover of play_k also on play_kbar (T if none);
  pre-merge segments P_k, P_kbar; C_k = movers of step t-1 on P_k, C_kbar on P_kbar, C_suf on the common suffix (from m on).
- NOPRE: DELSTEPS with C_k empty (MERGE + C-ELEM predict 0).
- charge c = the first element of C_k (nearest to x on the play). Counts: MAXX (DELSTEPS per least mover x), MAXXK (per (x, k)),
  MAXXC (per (x, c)), MAXC (per cause c), MAXXCK (per (x, k, c, sigma_(t-1)(c))), distinct pairs; cause classes (CAR/DEL/PRE) and
  CLEAST = how often c is the least mover of step t-1 (a chain of DELSTEPS); SEGLEN max |P_k|.
Usage: merge.py genome.json ... [VERB=1]"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "box143", "cause.py")).read().split('if __name__ == "__main__":')[0]
ns = {"__file__": os.path.join(HERE, "..", "box143", "cause.py")}; exec(src, ns); run = ns["run"]
VERB = os.environ.get("VERB")
def analyse(G):
    S, CUR, KEY, why = run(G, cap=5000); N, opts, lev = G["N"], G["opts"], G["lev"]; d = N // 2; T = len(S) - 1
    def L(t, l):
        K = KEY[min(t, len(KEY) - 1)]; return 2 * l if K[2 * l] < K[2 * l + 1] else 2 * l + 1
    carry = {(l, t) for l in range(d) for t in range(1, T + 1) if L(t, l) != L(t - 1, l)}
    mv = lambda t, x: S[t][x] != S[t - 1][x]
    def play(t, x, k):
        out = []; y = opts[x][k][1]
        while y >= 0: out.append(y); y = opts[y][S[t][y]][1]
        return out
    def cls(t, x):
        l = lev[x]
        if l > 0 and (l - 1, t) in carry: return "CAR"
        cs = [s for s in range(1, t + 1) if l > 0 and (l - 1, s) in carry]
        if not cs: return "PRE"
        return "DEL" if all(not mv(u, x) for u in range(cs[-1], t)) else "OTHER"
    least = {}
    for t in range(1, T + 1):
        ms = [x for x in range(N) if mv(t, x)]
        if ms: least[t] = min(ms, key=lambda x: lev[x])
    cnt = {k: {} for k in ("X", "XK", "XC", "C", "XCK")}; nopre = 0; ds = 0; ccls = {}; cleast = 0; seglen = 0; kbar_hit = 0; suf_hit = 0
    for t in range(2, T + 1):
        if t not in least: continue
        x = least[t]
        if cls(t, x) != "DEL": continue
        ds += 1; k = S[t][x]; pk, pb = play(t - 2, x, k), play(t - 2, x, 1 - k)
        m = next((y for y in pk if y in pb), None)
        Pk = pk[:pk.index(m)] if m is not None else pk; Pb = pb[:pb.index(m)] if m is not None else pb
        Ck = [y for y in Pk if mv(t - 1, y)]; Cb = [y for y in Pb if mv(t - 1, y)]
        Cs = [y for y in (pk[pk.index(m):] if m is not None else []) if mv(t - 1, y)]
        kbar_hit += bool(Cb); suf_hit += bool(Cs); seglen = max(seglen, len(Pk))
        if not Ck:
            nopre += 1
            if VERB: print(f"  NOPRE t {t} x {x} (lev {lev[x]}) -> {k}  Pk {Pk} Pkbar {Pb} merge {m}  Ckbar {Cb} Csuf {Cs} movers(t-1) {[y for y in range(N) if mv(t-1, y)]}")
            continue
        c = Ck[0]; cc = cls(t - 1, c); ccls[cc] = ccls.get(cc, 0) + 1; cleast += least.get(t - 1) == c
        for key, v in (("X", x), ("XK", (x, k)), ("XC", (x, c)), ("C", c), ("XCK", (x, k, c, S[t - 1][c]))):
            cnt[key][v] = cnt[key].get(v, 0) + 1
        if VERB: print(f"  DELSTEP t {t} x {x} (lev {lev[x]}) -> {k}  Pk {Pk} Pkbar {Pb} merge {m}  Ck {Ck} Ckbar {Cb} Csuf {Cs}  c {c} lev {lev[c]} {cc}{' LEAST' if least.get(t-1)==c else ''}")
    mx = {k: max(v.values(), default=0) for k, v in cnt.items()}
    return dict(T=T, d=d, ds=ds, nopre=nopre, mx=mx, pairs=len(cnt["XC"]), ccls=ccls, cleast=cleast, seglen=seglen, kbar=kbar_hit, suf=suf_hit)
if __name__ == "__main__":
    for p in sys.argv[1:]:
        r = analyse(json.load(open(p))); m = r["mx"]
        print(f"MERGE {os.path.basename(p)} d {r['d']} STEPS {r['T']} DELSTEPS {r['ds']} NOPRE {r['nopre']} MAXX {m['X']} MAXXK {m['XK']} MAXXC {m['XC']} MAXC {m['C']} "
              f"MAXXCK {m['XCK']} PAIRS {r['pairs']} CAUSECLS {r['ccls']} CLEAST {r['cleast']} SEGLEN {r['seglen']} KBARHIT {r['kbar']} SUFHIT {r['suf']}")
