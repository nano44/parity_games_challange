#!/usr/bin/env python3
"""L-RED 69 R241: instances for «box 215's gate-key form DEPENDS ON NUMBERING» (R240's pattern). For eg195.gen genomes (box 195, object)
the Γ3 game is renumbered (kt241.renumber: e = the e-vertices permuted among themselves; all = every vertex), N5 (n5s237 spec) is run
from S3 on the renumbered game, and kt241's counters are read. A genome is SAVED when a gate-key counter fires (kflip, kflipm, kpg)
while every KEY-TAU counter and every e-key counter is 0 on the SAME run, and every counter is 0 on the original numbering.
Saved per instance: inst/NUMB_<how><pseed>_<mode><seed>_<i>.json ({"genome", "perm", "pseed"}) and the renumbered game as .pg
(Oink / pgsolver format), both with sha1 in inst/SHA1SUMS; n5v (box 190 mode spec) is re-run on every saved instance (xdiff).
Usage: numb241.py MODE SEED COUNT HOW PSEED MAXSAVE | numb241.py files HOW PSEED MAXSAVE F.json ...   (env LNEW; LRED unset)"""
import sys, os, json, random, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import kt241 as K
import gamma3, eg195
TAU = ("std", "tau3", "w3", "lenvar", "kp", "kpf", "kpa", "unreach", "mukappa", "muinc", "muflat", "mulen", "kviol", "nomove")
EK = tuple(k for k in K.KEYS if k.endswith("_e"))
GK = ("kflip", "kflipm", "kpg")
REQ = os.environ.get("REQ")   # save only instances where this gate-key counter fires (e.g. kflipm: moves(x) > 1 + KF_x in gate keys)

def pgtext(g):
    return f"parity {g.n - 1};\n" + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n))

def main():
    if sys.argv[1] == "files":                                   # numb241.py files HOW PSEED MAXSAVE F.json ...
        how, pseed, maxsave = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]); fs = sys.argv[5:]; mode, seed, cnt = "files", "", len(fs)
        src = lambda i: (os.path.basename(fs[i]).rsplit(".", 1)[0], K.load(fs[i]))
    else:
        mode, seed, cnt, how, pseed, maxsave = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], int(sys.argv[5]), int(sys.argv[6])
        rng = random.Random(seed); src = lambda i: (f"{mode}{seed}_{i}", eg195.gen(rng, mode))
    out = os.path.join(HERE, "inst"); os.makedirs(out, exist_ok=True); saved = 0; tally = dict(gen=0, fire=0)
    for i in range(cnt):
        nm, G = src(i); tally["gen"] += 1
        K.PERM = "none"; c0, _, _ = K.analyse(G)
        K.PERM, K.PSEED = how, pseed; c, d, info = K.analyse(G)
        if not any(c[k] for k in GK): continue
        tally["fire"] += 1
        if sum(c0.values()) or any(c[k] for k in TAU + EK) or saved >= maxsave: continue
        if REQ and not c[REQ]: continue
        c2, _, info2 = K.analyse(G, second=True)
        name = f"NUMB_{how}{pseed}_{nm}"
        g, _, _, V = gamma3.build(G, K.PADS); g, V = K.renumber(g, V, how, pseed)
        js = json.dumps(dict(genome=G, perm=how, pseed=pseed), sort_keys=True); pg = pgtext(g)
        open(os.path.join(out, name + ".json"), "w").write(js); open(os.path.join(out, name + ".pg"), "w").write(pg)
        h1, h2 = hashlib.sha1(js.encode()).hexdigest(), hashlib.sha1(pg.encode()).hexdigest()
        with open(os.path.join(out, "SHA1SUMS"), "a") as f: f.write(f"{h1}  {name}.json\n{h2}  {name}.pg\n")
        saved += 1
        print(f"NUMB241 SAVED {name} json {h1[:12]} pg {h2[:12]} | original numbering: all counters 0 | renumbered: "
              + " ".join(f"{k} {c2[k]}" for k in GK) + f" | KEY-TAU and e-key counters 0 | T {d['T']} n {info2['n']} | n5v xdiff {info2['xd']}", flush=True)
    print(f"NUMB241 {mode} {seed} {cnt} {how} {pseed}: genomes {tally['gen']} with a gate-key counter > 0: {tally['fire']} saved {saved}", flush=True)

if __name__ == "__main__": main()
