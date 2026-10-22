#!/usr/bin/env python3
"""L-RED box 10 (produced on Opus 5.5): climb the CONTROL wiring of the relay + region-clock skeleton (lag3.build plus NH
free helper vertices) toward the R39 relay schema. Observed per root-context visit x and level j: F if t_j (the tangle with
vertex set {tau_j, w_j, y_j, v_j}) fired at step (1, T_j), X if excluded there. Target = relaymodel's F/X table. Score =
(dtl_stealdepth max depth, 3 (10 #matching F cells + #matching X cells) + 3 #levels learned + 2 min(phase length, D+OFF+3), then the parts) by the UNMODIFIED L-ALG model (run_game,
analyze). Free: out-edges/owner of T_j and of the helpers; helper priorities. Usage: schemaclimb.py SEED D STEPS OUT.pg [NH]"""
import sys, os, random
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
for k_, v_ in (("RM_DV", "0"), ("RM_LIGHT", "1"), ("RM_EXCL", "1"), ("RM_PREF", "1")): os.environ[k_] = v_
import pg, dtl_stealdepth as SD, lag3, lag4
sys.setrecursionlimit(100000)
OFF = 3
def target(D, NV):
    L = list(range(-1, D + 1)); F = {}
    for j in L:
        F[j] = [x >= 1 and not ((j > -1 and F[j - 1][x]) or x >= j + OFF) for x in range(NV)]
    return F
def score(g, names, D):
    try: d = SD.run_game(g, os.environ.get("DTL_ORDER", "stable"))
    except RecursionError: return (-9,)
    if not all(w is not None for w in d.win): return (-1,)
    tot = {}; mk, md, _ = SD.analyze(d, "", tot, [])
    inv = {v: i for i, v in enumerate(d.idx)}; L = list(range(-1, D + 1))
    tid = {}
    for j in L:
        want = {inv[names[f"{c}{j}"]] for c in ("tau", "w", "y", "v")}
        for t in range(len(d.tv)):
            if {v for v, _ in d.tv[t]} == want: tid[j] = t
    ph = SD.FD.phase_rows(d)[0]; rcs = [rc for r in ph for rc in r["recs"] if rc["key"][0] == 0 and len(rc["key"][1]) == len(ph[0]["G"])]
    F = target(D, len(rcs)); match = 0
    for j in L:
        if j not in tid: continue
        k = (1, inv[names[f"T{j}"]])
        for x, rc in enumerate(rcs):
            if x == 0: continue
            o = "F" if tid[j] in rc.get("fired", {}).get(k, ()) else ("X" if tid[j] in rc.get("excl", {}).get(k, ()) else "-")
            match += (10 if F[j][x] else 1) * (o == ("F" if F[j][x] else "X"))      # an F cell weighs 10, an X cell 1
    return (md, 3 * match + 3 * len(tid) + 2 * min(len(ph), D + OFF + 3), match, len(tid), len(ph))
if __name__ == "__main__":
    seed, D, steps, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; NH = int(sys.argv[5]) if len(sys.argv) > 5 else 3
    rng = random.Random(seed); gb = (lag4 if os.environ.get("SKEL") == "4" else lag3).build(D)
    for h in range(NH): gb.v(f"h{h}", rng.randrange(2, 40), rng.randrange(2)); gb.e(f"h{h}", "W")
    names = dict(gb.ids); n = len(gb.pr)
    ctrl = [gb.ids[nm] for nm in gb.ids if nm[0] in "Th" and nm != "tau"] ; ctrl = [c for c in ctrl if not [k for k, v in gb.ids.items() if v == c][0].startswith("tau")]
    hs = [gb.ids[f"h{h}"] for h in range(NH)]
    g = pg.Game(gb.pr, gb.ow, [sorted(s) for s in gb.out]); f = score(g, names, D); print("start", f, flush=True)
    for it in range(steps):
        pr, ow, sc = list(g.prio), list(g.owner), [list(s) for s in g.succ]
        for _ in range(rng.randint(1, 2)):
            v = rng.choice(ctrl); r = rng.random()
            if r < 0.55: sc[v] = sorted(set(rng.sample(range(n), rng.randint(1, 2))))
            elif r < 0.7 and v in hs: u = rng.choice(ctrl); sc[u] = sorted(set(sc[u]) | {v})      # an edge INTO a helper (from a control vertex)
            elif r < 0.85: ow[v] ^= 1
            elif v in hs: pr[v] = rng.randrange(2, 2 * n)
        h = pg.Game(pr, ow, sc); fh = score(h, names, D)
        if fh >= f:
            if fh > f: print(it, fh, flush=True); pg.write(h, out)
            g, f = h, fh
    print("final", f)
