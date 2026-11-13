#!/usr/bin/env python3
"""L-RED 68 R239: hill-climb against box 212 RF-D's hypothesis [IMP3] (imp239.one: N5 = n5s237 spec from S3 on Γ3(G) up to its first
fallback). Random genomes give short runs (F1 <= 5 on 2,000), so the climb lengthens N5's run (score = (counter sum, F1)) while every
transition before the first fallback is checked. Mutations: experiments/red/r230/mut230 (env NMAX, DMAX). Every XEVERY-th evaluation
and every candidate also runs the second engine (box 190 n5v spec, state by state). Checkpoint OUT/ick_TAG.json (RESUME=1); TLIMIT.
Env: LNEW (LRED unset), as imp239.py. Usage: impclimb239.py TAG SEED EVALS START(rand|FILE.json)"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r230")]
import imp239, rf239, mut230
OUT = os.environ.get("OUT", os.path.join(HERE, "out")); TLIMIT = float(os.environ.get("TLIMIT", "1e18")); XE = int(os.environ.get("XEVERY", "25"))
if __name__ == "__main__":
    tag, seed, evals, start = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    os.makedirs(OUT, exist_ok=True); ck = os.path.join(OUT, f"ick_{tag}.json"); rng = random.Random(seed); mut230.set_rng(rng); t0 = time.time()
    if os.environ.get("RESUME") == "1" and os.path.exists(ck):
        S = json.load(open(ck)); st = S["rng"]; rng.setstate((st[0], tuple(st[1]), st[2]))
    else:
        G = rf239.rand_genome(rng, int(os.environ.get("NMAX", "16")), 3, 2) if start == "rand" else json.load(open(start))
        G = G.get("genome", G); G.pop("_evals", None); G = mut230.renum(G); c, F1, its, fbs, steps, n, _ = imp239.one(G)
        S = dict(tag=tag, seed=seed, evals=1, cur=G, cur_score=[sum(c.values()), F1], best=G, best_score=[sum(c.values()), F1], tot=dict(c),
                 steps=steps, maxF1=F1, maxn=n, x=0, xdiff=0, cands=0)
    def save():
        st = rng.getstate(); S["rng"] = [st[0], list(st[1]), st[2]]; tmp = ck + ".tmp"; json.dump(S, open(tmp, "w")); os.replace(tmp, ck)
    def line(w):
        print(f"IMPCLIMB239 {tag} {w}: evals {S['evals']} cur {S['cur_score']} best {S['best_score']} N_best {S['best']['N']} | " + " ".join(f"{k} {S['tot'][k]}" for k in imp239.KEYS)
              + f" | transitions checked {S['steps']} max F1 {S['maxF1']} max |V| {S['maxn']} | second engine sampled {S['x']} xdiff {S['xdiff']} | cands {S['cands']} | {time.time() - t0:.0f} s", flush=True)
    while S["evals"] < evals and time.time() - t0 < TLIMIT:
        G = mut230.mutate(S["cur"]); sec = S["evals"] % XE == 0
        try: c, F1, its, fbs, steps, n, xd = imp239.one(G, sec)
        except (AssertionError, IndexError, KeyError, ValueError): continue
        S["evals"] += 1; kill = sum(c.values())
        for k in imp239.KEYS: S["tot"][k] += c[k]
        S["steps"] += steps; S["maxF1"] = max(S["maxF1"], F1); S["maxn"] = max(S["maxn"], n)
        if xd is not None: S["x"] += 1; S["xdiff"] += xd
        if kill:
            S["cands"] += 1
            if S["cands"] <= 20:
                c2 = imp239.one(G, True); json.dump(dict(genome=G, counters=c, second_xdiff=c2[6]), open(os.path.join(OUT, f"icand_{tag}_{S['evals']}.json"), "w"))
                print(f"IMPCLIMB239 CANDIDATE {tag} eval {S['evals']}: {c} F1 {F1} | second engine xdiff {c2[6]}", flush=True)
        sc = [kill, F1]
        if sc >= S["cur_score"]: S["cur"] = G; S["cur_score"] = sc
        if sc > S["best_score"]: S["best"] = G; S["best_score"] = sc; json.dump(G, open(os.path.join(OUT, f"ibest_{tag}.json"), "w"))
        if S["evals"] % 100 == 0: save(); line("at")
    save(); line("END" if S["evals"] >= evals else "PAUSED (TLIMIT)")
