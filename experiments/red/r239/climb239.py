#!/usr/bin/env python3
"""L-RED 68 R239: adversarial hill-climb against box 212 RF-A / RF-B / RF-C (rf239.analyse: own IDEAL-CYC engine, any improving rule).
The rule is fixed per climb (TAG's RULE); its random choices use random.Random(RSEED * 1000003 + eval), so every candidate is
reproducible from (genome, RULE, rule seed). Genome mutations: experiments/red/r230/mut230 (wiring, Xi-targets, gates, beta ranks and
parities, start, options, movers; env NMAX, DMAX).
Score (env SCORE): plat = (must-0 sum, longest plateau, stalls, T); ns = (must-0 sum, max non-stall steps / P, T); T = (must-0 sum, T,
longest plateau). Any must-0 counter > 0 writes OUT/cand_TAG_EVAL.json (genome + rule + rule seed) and prints CANDIDATE.
Checkpoint OUT/ck_TAG.json (current genome, best, counters, rng state); RESUME=1; TLIMIT seconds.
Env: as rf239.py (CTRL: the climb then counts control firings). Usage: climb239.py TAG RULE SEED EVALS START(rand|FILE.json)"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r230")]
import rf239, mut230
OUT = os.environ.get("OUT", os.path.join(HERE, "out")); TLIMIT = float(os.environ.get("TLIMIT", "1e18")); SC = os.environ.get("SCORE", "plat")

def score(G, rule, rs):
    c, d = rf239.analyse(G, rule, random.Random(rs)); m = sum(c[k] for k in rf239.MUST0)
    s = {"plat": [m, d["maxplat"], d["stalls"], d["T"]], "ns": [m, round(d["maxns"] / max(1, d["P"]), 4), d["T"]], "T": [m, d["T"], d["maxplat"]]}[SC]
    return s, c, d

if __name__ == "__main__":
    tag, rule, seed, evals, start = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    os.makedirs(OUT, exist_ok=True); ck = os.path.join(OUT, f"ck_{tag}.json"); rng = random.Random(seed); mut230.set_rng(rng); t0 = time.time()
    if os.environ.get("RESUME") == "1" and os.path.exists(ck):
        S = json.load(open(ck)); st = S["rng"]; rng.setstate((st[0], tuple(st[1]), st[2]))
    else:
        G = rf239.rand_genome(rng, int(os.environ.get("NMAX", "16")), 3, 2) if start == "rand" else json.load(open(start))
        G = G.get("genome", G); G.pop("_evals", None); G = mut230.renum(G); s, c, d = score(G, rule, seed * 1000003)
        S = dict(tag=tag, rule=rule, seed=seed, score=SC, evals=1, cur=G, cur_score=s, best=G, best_score=s, tot={k: c[k] for k in rf239.MUST0 + rf239.DESC},
                 maxT=d["T"], maxplat=d["maxplat"], maxns=d["maxns"], maxn=d["n"], sumT=d["T"], cands=0, ctrl=rf239.CTRL)
    def save():
        st = rng.getstate(); S["rng"] = [st[0], list(st[1]), st[2]]; tmp = ck + ".tmp"; json.dump(S, open(tmp, "w")); os.replace(tmp, ck)
    def line(w):
        print(f"CLIMB239 {tag} rule {rule} score {SC} {w}: evals {S['evals']} cur {S['cur_score']} best {S['best_score']} N_best {S['best']['N']} | must0 "
              + " ".join(f"{k} {S['tot'][k]}" for k in rf239.MUST0) + " | desc " + " ".join(f"{k} {S['tot'][k]}" for k in rf239.DESC)
              + f" | max T {S['maxT']} max plateau {S['maxplat']} max nonstall {S['maxns']} max |V| {S['maxn']} sum T {S['sumT']} | cands {S['cands']} ctrl {S['ctrl']} | {time.time() - t0:.0f} s", flush=True)
    while S["evals"] < evals and time.time() - t0 < TLIMIT:
        G = mut230.mutate(S["cur"]); rs = seed * 1000003 + S["evals"]
        try: s, c, d = score(G, rule, rs)
        except (AssertionError, IndexError, KeyError, ValueError): continue
        S["evals"] += 1
        for k in S["tot"]: S["tot"][k] += c[k]
        S["maxT"] = max(S["maxT"], d["T"]); S["maxplat"] = max(S["maxplat"], d["maxplat"]); S["maxns"] = max(S["maxns"], d["maxns"]); S["maxn"] = max(S["maxn"], d["n"]); S["sumT"] += d["T"]
        if s[0] > 0:
            S["cands"] += 1
            if S["cands"] <= 20:
                json.dump(dict(genome=G, rule=rule, rule_seed=rs, counters=c), open(os.path.join(OUT, f"cand_{tag}_{S['evals']}.json"), "w"))
                if not rf239.CTRL: print(f"CLIMB239 CANDIDATE {tag} eval {S['evals']} rule {rule} rule_seed {rs}: " + str({k: v for k, v in c.items() if v and k in rf239.MUST0}), flush=True)
        if s >= S["cur_score"]: S["cur"] = G; S["cur_score"] = s
        if s > S["best_score"]: S["best"] = G; S["best_score"] = s; json.dump(dict(genome=G, rule=rule, rule_seed=rs, score=s), open(os.path.join(OUT, f"best_{tag}.json"), "w"))
        if S["evals"] % 200 == 0: save(); line("at")
    save(); line("END" if S["evals"] >= evals else "PAUSED (TLIMIT)")
