#!/usr/bin/env python3
"""L-RED 63 R229 item 1 (K7, non-PRIV gate) and item 3 (k = 1): falsification climbs on R221 own.py (cap 600 steps in the climb).
Moves: r226 sharp226.mutate and mclimb228's GROW moves (copied). Census: gate229.census (gate classes, C, T).
ORDER=NP (default): score = (mnp, T, C, -size); mnp = max non-PRIV flips at one gate (PER-GATE MAXIMUM), T = run steps, C = per-(v, I, y)
  max c_y. Any genome with gln > 0 or predfail > 0 (Lemma GATE-LOW-NULL fails) or below > 0 is frozen to out/gkill_<SEED>.json.
ORDER=K1 (item 3, L-NEW BOX 202 K1-FLIP(2)): only genomes whose Ξ-graph has min FVS k <= 1 (seg228.fvs) are accepted;
  score = (fx, C, T, -size), fx = max over gates g of flips(g) - 2 (lamch(g) + 1), lamch(g) = #steps at which Λ changes at e_g or b_g (box 202's lamch; own engine, whole run);
  fx > 0 is a K1-FLIP(2) failure -> frozen to out/k1kill_<SEED>.json.
ORDER=K1C: k <= 1 filter, score = (C, T, fx, -size).
ORDER=DP (BOX 93): score = (bad, dbreak, dpass, -size) from e93_229.census (bad = sum of its must-be-0 counters; dbreak = gates with
  unlocks > 1 + ch_D; dpass = gates whose D-play passes e_q); bad or dbreak > 0 -> frozen to out/dkill_<SEED>.json.
Freezes every strict gain on the first two score entries to out/nc<ORDER>_<CAP>_<SEED>.json. Resumable: RESUME=<json>.
Usage: nclimb229.py SEED CAP ITER START.json"""
import sys, os, json, random, copy, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r228"), os.path.join(H, "..", "r226"),
                                                              os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
import own, gate229
from sharp226 import mutate
from compose226 import add_opt, check
ORDER = os.environ.get("ORDER", "NP"); KG = 3 if ORDER == "DP" else 2   # score prefix whose strict gain is frozen / printed
size = lambda G: G["N"] + sum(len(o) for o in G["opts"])
def kfx(G, cap=600):
    """per-gate flips(g) - 2 (lamch(g) + 1), maximum over gates; flips = changes of Odd's choice at g (all steps, ties included); lamch = steps with a Λ-change at e_g or b_g."""
    out, V, O, _ = own.run(G, cap); best = -10 ** 9; arg = None
    for q in O:
        g, pe, pb = V[("g", q)], V[("e", q)], V[("b", q)]; f = sum(out[t][2][g] != out[t - 1][2][g] for t in range(1, len(out)))
        lc = sum(out[t][1][pe][0] != out[t - 1][1][pe][0] or out[t][1][pb][0] != out[t - 1][1][pb][0] for t in range(1, len(out)))
        if f - 2 * (lc + 1) > best: best, arg = f - 2 * (lc + 1), (q, f, lc)
    return best, arg
def score(G, seed):
    if ORDER == "DP":
        import e93_229
        c = e93_229.census(G, 600); c.update(mnp=c["mfl"], np=c["np_rel"] + c["np_unl"], up=0, lam=0, gln=0, C=0, predfail=0, below=0)
        bad = sum(c[k] for k in ("npside", "npsub", "npboth", "npkind", "relfail", "unlfail", "dexact", "kbfail", "relGup"))
        if bad or c["dbreak"]: json.dump(G, open(f"{H}/out/dkill_{seed}.json", "w"))
        return (bad, c["dbreak"], c["dpass"], -size(G)), c
    if ORDER in ("K1", "K1C"):
        import seg228
        k = seg228.fvs(G)
        if not k.isdigit() or int(k) > 1: return None, None
        c = gate229.census(G, 600); fx, arg = kfx(G); c["fx"] = fx; c["arg"] = arg; c["k"] = k
        if fx > 0: json.dump(G, open(f"{H}/out/k1kill_{seed}.json", "w"))
        if ORDER == "K1": return (fx, c["C"], c["T"], -size(G)), c
        return (c["C"], c["T"], fx, -size(G)), c
    c = gate229.census(G, 600)
    if c["gln"] or c["predfail"] or c["below"]: json.dump(G, open(f"{H}/out/gkill_{seed}.json", "w"))
    return (c["mnp"], c["T"], c["C"], -size(G)), c
def grow(G, rng):
    G = copy.deepcopy(G); N = G["N"]; M = len(G["br"])
    if rng.random() < 0.6:
        x = rng.randrange(N); wt = -1 if G["lev"][x] == 0 else rng.choice([y for y in range(N) if G["lev"][y] == G["lev"][x] - 1])
        return add_opt(G, x, wt, rng.choice(list(range(N)) + [-1]), rng.randint(0, M), rng.randint(0, M), rng.randrange(2))
    lv = rng.choice([0, 1]); y = N; G["N"] += 1; G["lev"].append(lv); G["opts"].append([]); G["gate"].append([]); G["start"].append(0)
    wt = -1 if lv == 0 else rng.choice([z for z in range(N) if G["lev"][z] == 0])
    G = add_opt(G, y, wt, rng.choice(list(range(N)) + [-1]), rng.randint(0, M), rng.randint(0, M), rng.randrange(2)); M += 1
    x = rng.randrange(N); wx = -1 if G["lev"][x] == 0 else rng.choice([z for z in range(N) if G["lev"][z] == G["lev"][x] - 1])
    return add_opt(G, x, wx, y, rng.randint(0, M), rng.randint(0, M), rng.randrange(2))
if __name__ == "__main__":
    seed, CAP, IT, SG = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    G = json.load(open(os.environ.get("RESUME", SG))); G = G.get("genome", G); s, c = score(G, seed)
    print("start", s, None if c is None else {k: c[k] for k in ("mnp", "np", "up", "lam", "gln", "T", "C") + (("fx", "k", "arg") if "fx" in c else ())}, "N", G["N"], "M", len(G["br"]), flush=True)
    if s is None: sys.exit("start genome rejected by the k filter")
    for it in range(IT):
        Hh = grow(G, rng) if (rng.random() < 0.3 and size(G) < CAP) else mutate(G, rng)
        if size(Hh) > CAP: continue
        try: check(Hh); s2, c2 = score(Hh, seed)
        except Exception: continue
        if s2 is None: continue
        if s2[:3] >= s[:3]:
            if s2[:KG] > s[:KG]:
                json.dump(Hh, open(f"{H}/out/nc{ORDER}_{CAP}_{seed}.json", "w"))
                print(it, s2, {k: c2[k] for k in ("mnp", "np", "up", "lam", "gln", "predfail", "below", "T", "C") + (("fx", "k", "arg") if "fx" in c2 else ())},
                      "N", Hh["N"], "M", len(Hh["br"]), flush=True)
            G, s = Hh, s2
    print("FINAL cap", CAP, "score", s, "N", G["N"], "M", len(G["br"]), flush=True)
