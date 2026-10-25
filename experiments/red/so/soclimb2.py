#!/usr/bin/env python3
"""Box 37 (L-RED): hill-climb on 𝒞^1O against L-NEW's box-33 lemmas, counter = sox2.analyse. Mutations: soclimb.mutate.
  exr : (fails, max over phases of ε-transitions in one fallback-free segment − (d_o − 1), same count, ε in SN)
        (EXIT-R + ORX give <= d_o − 1 per segment; > 0 refutes the pair)
  seg : (failures of the proved lemmas, as exr; EXIT-R / ORX failures only as a last key)
  small: (EXIT-R fails?, max ε, ε in SN) for small n
  jb  : (proved-lemma failures, max J − (d_o − 1)(f + 1), max ε)
  xsnf: (proved-lemma failures, max X_SN over phases with f >= 1, X there)   rel: (.., max REL per phase, max ε)
  jbf : (.., max J − (d_o − 1)(f + 1) over phases with J >= 1 and f >= 1, J there)
  njb : (proved-lemma + NJB failures, max re-absorptions of block-released exits inside a block, releases, block size)
  xsn : (fails, max X_SN per phase, max X)        post: (fails, max crossings after the SN prefix of a run, max X)
Usage: soclimb2.py mode seed secs OUT (seed.pg | --rand n)"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sox, sox2, pg
from soclimb import mutate, dump
NEG = (-10 ** 9,) * 4

def fit(G, mode):
    g = pg.Game(*G)
    if any(not s for s in G[2]) or len(sox.oddchoice(g)) != 1: return NEG, None
    try: r = sox2.analyse(g, cap=3000)
    except AssertionError: raise
    except Exception: return NEG, None
    rs = r["rows"]; fails = sum(r["C"].values())
    mx = lambda f: max((f(x) for x in rs), default=-10 ** 9)
    if mode == "exr": f = (fails, max((x["maxseg"] - (x["d_o"] - 1) for x in rs if x["maxseg"] >= 1), default=-10 ** 9), mx(lambda x: x["maxseg"]), mx(lambda x: x["epsSN"]))
    elif mode == "seg":   # proved-lemma failures first; EXITR / ORX (refuted) not counted
        pf = sum(v for k, v in r["C"].items() if k not in ("EXITR", "ORX"))
        f = (pf, max((x["maxseg"] - (x["d_o"] - 1) for x in rs if x["maxseg"] >= 1), default=-10 ** 9), mx(lambda x: x["maxseg"]), r["C"].get("ORX", 0))
    elif mode == "small": f = (min(1, r["C"].get("EXITR", 0)), mx(lambda x: x["eps"]), mx(lambda x: x["epsSN"]), 0)
    elif mode == "jb":    # J − (d_o − 1)(f + 1) per phase (sox rows), phases with J >= 1; proved-lemma failures first
        pf = sum(v for k, v in r["C"].items() if k not in ("EXITR", "ORX"))
        r1 = sox.analyse(g, cap=3000); fr = {x["a"]: x["f"] for x in rs}
        f = (pf + sum(r1["C"].values()), max((x["J"] - (x["d_o"] - 1) * (fr.get(x["a"], 0) + 1) for x in r1["rows"] if x["J"] >= 1), default=-10 ** 9),
             mx(lambda x: x["eps"]), 0)
    elif mode in ("xsnf", "jbf", "rel"):   # box 38; proved-lemma failures first (EXITR / ORX refuted, not counted)
        pf = sum(v for k, v in r["C"].items() if k not in ("EXITR", "ORX"))
        if mode == "xsnf": f = (pf, max((x["XSN"] for x in rs if x["f"] >= 1), default=-10 ** 9), max((x["X"] for x in rs if x["f"] >= 1), default=-10 ** 9), 0)
        elif mode == "rel": f = (pf, mx(lambda x: x["RELe"]), mx(lambda x: x["eps"]), mx(lambda x: x["REL"]))   # RELe: releases of ε-absorbed exits
        else:
            r1 = sox.analyse(g, cap=3000); fr = {x["a"]: x["f"] for x in rs}
            f = (pf + sum(r1["C"].values()), max((x["J"] - (x["d_o"] - 1) * (fr.get(x["a"], 0) + 1) for x in r1["rows"] if x["J"] >= 1 and fr.get(x["a"], 0) >= 1), default=-10 ** 9),
                 max((x["J"] for x in r1["rows"] if fr.get(x["a"], 0) >= 1), default=-10 ** 9), 0)
    elif mode == "njb":   # box 38: NJB / FLATALL failures first, then re-absorptions of block-released exits, releases, block fallbacks
        pf = sum(v for k, v in r["C"].items() if k not in ("EXITR", "ORX"))
        f = (pf, mx(lambda x: x["reabs"]), mx(lambda x: x["blkrel"]), mx(lambda x: x["blockfb"]))
    elif mode == "xrun":  # crossings inside the c_w = c_θ prefix of one fallback-free run, minus (n − 1)
        f = (fails, mx(lambda x: x["maxpre"]) - (g.n - 1), mx(lambda x: x["XSN"]), 0)
    elif mode == "mn":    # P-N5-NJB MINSET: NJB / proved failures, sole-minimiser absorptions inside a block, −min |Mn|, Mn-member absorptions
        pf = sum(v for k, v in r["C"].items() if k not in ("EXITR", "ORX"))
        f = (pf, mx(lambda x: x["soleabs"]), mx(lambda x: x["mnabs"]), -min((x["minmn"] for x in rs), default=10 ** 9))   # mnabs before min|Mn| (trap 2)
    elif mode == "xsn": f = (fails, mx(lambda x: x["XSN"]), mx(lambda x: x["X"]), 0)
    elif mode == "post": f = (fails, mx(lambda x: x["maxpost"]), mx(lambda x: x["X"]), 0)
    return f, r

if __name__ == "__main__":
    mode, seed, secs, out = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    if sys.argv[5] == "--rand":
        n = int(sys.argv[6])
        while True:
            prio = [rng.randrange(n) for _ in range(n)]; owner = [rng.randrange(2) for _ in range(n)]
            succ = [sorted(set(rng.sample(range(n), 1 if owner[v] else rng.choice((1, 2, 2, 3))))) for v in range(n)]
            o = rng.randrange(n); owner[o] = 1; succ[o] = sorted(set(rng.sample(range(n), max(2, n // 4))))
            G = [prio, owner, succ]; f, r = fit(G, mode)
            if f != NEG: break
    else:
        g = sox.load(sys.argv[5]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f, r = fit(G, mode)
    t0 = time.time(); it = 0; print("start", f, flush=True); dump(G, out + ".pg")
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh, rh = fit(H, mode)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh} it/fb {rh['it']}/{rh['fb']} C {rh['C']} ex {rh['ex']}", flush=True); dump(H, out + ".pg")
            G, f = H, fh
    print("FINAL", f, it, flush=True)
