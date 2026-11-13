#!/usr/bin/env python3
"""REFEREE successor 36: N5 (SPEC, from S3) on Gamma3(G), run level, for the first reviews of P-N5-EXP and P-N5-KEY1P.

Genome and IDEAL run: gkx.py (own rule transcription / own definition-based step). Game: this lane's builder gk_gamma3.py
(successor 35, from P-N5-REALIZE section 3.1 and P-N5-REACH section 3). Engine: this lane's rl_engine.py (REFEREE 8, from SPEC).
Winners: the lane's own Zielonka (gk_reach.zielonka). No file of another lane is imported.
One line per genome with named must-0 counters:
  S3START  state 0 is not the standard state for s_0
  STD      a state j <= L is not the standard state for s_j (unit: states), or the run is shorter than L + 1 transitions
  FLFB     a transition 1..L is a fallback            FLTAU   tau changes at a transition 1..L
  FLSIG    sigma is unchanged at a transition 1..L    LASTFB  transition L + 1 is not a fallback
  WIN      vertices where N5's winner differs from Zielonka's
  EXACT    [iterations != L + 3] + [number of fallbacks != 1]      (R124 ENDGAME-3-N5 / EXACT-L, landed)
  PG       (with --pg DIR, G_k only) the built game differs from the lane's frozen DIR/G_k_g3.pg (priority, owner, successors)
  GEN35    (with --pgonly, G_k only) number of genome fields in which gkx.rule(k) differs from successor 35's gk_build.genome(k)
Usage: gkx_n5.py gk kmin kmax [--pg DIR] [--pgonly] [--ctl NAME]   |   gkx_n5.py file G.json ... [--ctl NAME]
       | gkx_n5.py lift D G.json ... [--ctl NAME]
Controls (--ctl; each names the counter that must fire):
  start    the game is built with ONE mover's start option flipped (its Omega-2 pad), the model keeps the genome start: S3START
  win      Zielonka is given the game with c_W's priority made odd (top + 1): WIN
  lastfb   LASTFB read at transition L instead of L + 1: LASTFB
  nonmover FLSIG evaluated on sigma restricted to the non-movers (which FL transitions never change): FLSIG
  noesc    the game without the escape edges beta_g -> pb_g -> K0 at the options whose Xi-target is a mover: FLTAU or STD
  rank     the game is built with the beta-ranks reversed (M - 1 - br), the model keeps br: STD
  revE     the e-vertices' indices in reversed gate order (successor 35's control): STD, FLFB
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gkx
import rl_engine as eng
import gk_gamma3 as g3
import gk_reach as R


def to_dict(J):
    """lanes' JSON genome -> the dict form gk_gamma3 reads."""
    N = J["N"]
    return {"N": N, "lev": list(J["lev"]), "deg": [len(o) for o in J["opts"]],
            "wt": [[(o[0] if o[0] >= 0 else None) for o in J["opts"][x]] for x in range(N)],
            "xt": [[(o[1] if o[1] >= 0 else "X") for o in J["opts"][x]] for x in range(N)],
            "bid": [[o[2] for o in J["opts"][x]] for x in range(N)],
            "gate": [list(r) for r in J["gate"]], "br": list(J["br"]), "bp": list(J["bp"]), "start": list(J["start"])}


def read_pg(path):
    L = open(path).read().strip().split("\n")
    rows = [l.rstrip(";").split() for l in L[1:]]
    n = len(rows)
    prio = [None] * n
    owner = [None] * n
    succ = [None] * n
    for r in rows:
        v = int(r[0])
        prio[v] = int(r[1])
        owner[v] = int(r[2])
        succ[v] = [int(w) for w in r[3].split(",")]
    return prio, owner, succ


def replay(J, name, ctl="", pgdir=None, k=None):
    S, word = gkx.run(J)
    L = len(S) - 1
    G = to_dict(J)
    Gb = G
    if ctl == "start":
        Gb = json.loads(json.dumps(G))
        x = max(range(G["N"]), key=lambda x: (G["deg"][x] >= 2, -x))          # the first mover of degree >= 2
        Gb["start"][x] = (G["start"][x] + 1) % G["deg"][x]
    if ctl == "rank":
        Gb = json.loads(json.dumps(G))
        M = sum(G["deg"])
        Gb["br"] = [M - 1 - r for r in G["br"]]
    prio, owner, succ, names, idx = g3.build3_revE(Gb) if ctl == "revE" else g3.build3(Gb)
    n3 = len(prio)
    if ctl == "noesc":
        for x in range(G["N"]):
            for kk in range(G["deg"][x]):
                if G["xt"][x][kk] != "X":
                    b = idx[("b", (x, kk))]
                    succ[b] = [w for w in succ[b] if w != idx[("pb", (x, kk))]]
                    assert len(succ[b]) == 1
    c = dict(S3START=0, STD=0, FLFB=0, FLTAU=0, FLSIG=0, LASTFB=0, WIN=0, EXACT=0)
    pg = ""
    if pgdir is not None and k is not None and os.path.exists(f"{pgdir}/G_{k}_g3.pg"):
        p2, o2, s2 = read_pg(f"{pgdir}/G_{k}_g3.pg")
        pg = f" PG {int((p2, o2, [sorted(a) for a in s2]) != (prio, owner, [sorted(a) for a in succ]))}"
    if PGONLY:
        gen35 = ""
        if k is not None:                    # my genome against successor 35's rebuild gk_build.genome(k), field by field
            import gk_build
            b = gk_build.genome(k)
            gen35 = f" GEN35 {sum(1 for key in G if G[key] != b.get(key))}"
        return f"{name} pgonly N {G['N']} M {sum(G['deg'])} n {n3} m {sum(len(a) for a in succ)} maxprio {max(prio)} L {L}" + pg + gen35
    g = eng.Game(prio, owner, succ)
    t0 = time.time()
    out = eng.run(g, maxit=10 ** 7)
    dt = time.time() - t0
    iters = len(out) - 1
    fbs = [j + 1 for j in range(iters) if out[j]["fb"]]

    def std(s):
        sig, tau = g3.standard(G, idx, s, n3)          # the standard state of the UNPERTURBED genome
        for v in range(n3):
            if owner[v] == 0 and sig[v] is None:
                sig[v] = succ[v][0]
        return sig, tau

    def is_std(st, s):
        sig, tau = std(s)
        return all(st["s"][v] == sig[v] for v in range(n3) if owner[v] == 0) and \
            all(st["t"][v] == tau[v] for v in range(n3) if owner[v] == 1)
    if not is_std(out[0], S[0]):
        c["S3START"] += 1
    for j in range(0, min(L, iters) + 1):
        if not is_std(out[j], S[j]):
            c["STD"] += 1
    if iters < L + 1:
        c["STD"] += 1
    N = G["N"]
    for j in range(1, min(L, iters) + 1):
        if out[j - 1]["fb"]:
            c["FLFB"] += 1
        if out[j]["t"] != out[j - 1]["t"]:
            c["FLTAU"] += 1
        if ctl == "nonmover":
            if out[j]["s"][N:] == out[j - 1]["s"][N:]:
                c["FLSIG"] += 1
        elif out[j]["s"] == out[j - 1]["s"]:
            c["FLSIG"] += 1
    jl = L - 1 if ctl == "lastfb" else L
    if iters >= L + 1 and jl >= 0 and not out[jl]["fb"]:
        c["LASTFB"] += 1
    c["EXACT"] = int(iters != L + 3) + int(len(fbs) != 1)
    pz = list(prio)
    if ctl == "win":
        pz[idx["cW"]] += 1
    WE = R.zielonka(pz, owner, succ)
    Xi = out[-1]["Xi"]
    for v in range(n3):
        if (prio[Xi[v][0]] % 2 == 0) != (v in WE):
            c["WIN"] += 1
    return (f"{name} ctl {ctl or 0} N {N} M {sum(G['deg'])} n {n3} m {sum(len(a) for a in succ)} maxprio {max(prio)} L {L} stop {word} "
            f"iterations {iters} fallbacks {fbs} " + " ".join(f"{a} {b}" for a, b in c.items()) + pg + f" evenwins {len(WE)} secs {dt:.1f}")


PGONLY = False

if __name__ == "__main__":
    a = sys.argv[1:]
    ctl = ""
    if "--pgonly" in a:                      # build the game and compare it with the frozen .pg file; do not run N5
        PGONLY = True
        a.remove("--pgonly")
    pgdir = None
    if "--ctl" in a:
        i = a.index("--ctl")
        ctl = a[i + 1]
        del a[i:i + 2]
    if "--pg" in a:
        i = a.index("--pg")
        pgdir = a[i + 1]
        del a[i:i + 2]
    if a[0] == "gk":
        for k in range(int(a[1]), int(a[2]) + 1):
            J, _ = gkx.rule(k)
            print(replay(J, f"G_{k}", ctl, pgdir, k), flush=True)
    elif a[0] == "lift":                       # LIFT(G, D) of P-N5-KEY1P section 11 (k1p.lift)
        import k1p
        for f in a[2:]:
            J = k1p.lift(json.load(open(f)), int(a[1]))
            print(replay(J, f"LIFT({f.split('/')[-1]},{a[1]})", ctl), flush=True)
    else:
        for f in a[1:]:
            J = json.load(open(f))
            if "genome" in J:
                J = J["genome"]
            print(replay(J, f.split("/")[-1], ctl), flush=True)
