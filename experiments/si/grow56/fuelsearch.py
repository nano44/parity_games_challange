#!/usr/bin/env python3
"""L-SI box 56: random search against CONJECTURE FUEL-DESC (srcfuel.py, run in-process on random games written to a scratch dir).
Random games: n vertices, random owners / priorities, out-degree 1..DMAX, random start pair (as si/sb53/rsearch.py). Saves any game with
DESCV > 0 or OTHER > 0 to OUT/. Prints the summed SRCFUEL fields. Usage: fuelsearch.py SEED COUNT N DMAX OUT"""
import sys, os, random, io, contextlib, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
seed, cnt, N, DMAX, OUT = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
code = compile(open(os.path.join(HERE, "srcfuel.py")).read(), "srcfuel.py", "exec")
rng = random.Random(seed); os.makedirs(OUT, exist_ok=True); tmp = os.path.join(OUT, f"tmp_{seed}")
tot = {}; bad = 0
for i in range(cnt):
    n = N; own = [rng.randint(0, 1) for _ in range(n)]; pr = [rng.randint(0, n) for _ in range(n)]
    succ = [rng.sample(range(n), rng.randint(1, DMAX)) for _ in range(n)]
    st = ({v: rng.choice(succ[v]) for v in range(n) if own[v] == 0}, {v: rng.choice(succ[v]) for v in range(n) if own[v] == 1})
    with open(tmp + ".pg", "w") as h:
        h.write(f"parity {n - 1};\n" + "".join(f"{v} {pr[v]} {own[v]} {','.join(map(str, succ[v]))};\n" for v in range(n)))
    with open(tmp + ".start", "w") as h:
        h.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in st[0].items()) + "\nTAU0 " + " ".join(f"{v}:{w}" for v, w in st[1].items()) + "\n")
    buf = io.StringIO(); sys.argv = ["srcfuel.py", tmp + ".pg", tmp + ".start"]
    with contextlib.redirect_stdout(buf): exec(code, {"__file__": os.path.join(HERE, "srcfuel.py"), "__name__": "__main__"})
    w = buf.getvalue().strip().splitlines()[-1].split()
    d = dict(zip(w[2::2], w[3::2]))
    for k, v in d.items():
        if k == "n": continue
        tot[k] = max(tot.get(k, 0), int(v)) if k.startswith("MAX") else tot.get(k, 0) + int(v)
    if int(d.get("DESCV", 0)) or int(d.get("OTHER", 0)):
        bad += 1; shutil.copy(tmp + ".pg", os.path.join(OUT, f"fd_{seed}_{i}.pg")); shutil.copy(tmp + ".start", os.path.join(OUT, f"fd_{seed}_{i}.start"))
        print("BAD", os.path.join(OUT, f"fd_{seed}_{i}"), d.get("DESCV"), d.get("OTHER"), flush=True)
print(f"FUELSEARCH seed {seed} n {N} dmax {DMAX} games {cnt} bad {bad} " + " ".join(f"{a} {b}" for a, b in tot.items()))
