#!/usr/bin/env python3
"""L-RED 57 R222: sweep of the ladder83 class (L-SI's builder, imported read-only from $WTSI83 = a worktree of claude/l-si 2a44b7d6)
with L-RED's own run (own.py) and counters (lock222.py). Modes per genome:
  stored : ladder83's start (UP / EXIT);           rstart : uniformly random start strategy (LOCK-UP's proof does not use the start);
  rbeta  : random beta ranks, parities kept (bp), plus random start (the proof uses only beta parities via dead gates / even beta_S);
  rev    : EORD=rev, level-reversed e-order (violates [E-LEV]; boundary probe, NOT in LOCK-UP's scope).
Usage: sweep222.py SEED COUNT OUT.txt   (one line per run; resumable: skips run ids already in OUT.txt)"""
import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.environ["WTSI83"], "experiments/si/box83"))
import ladder83, lock222, own
seed, cnt, outf = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
done = set()
if os.path.exists(outf):
    for ln in open(outf):
        if ln.startswith("RUN "): done.add(ln.split()[1])
fo = open(outf, "a"); rnd = random.Random(seed)
for i in range(cnt):
    h = rnd.randint(2, 5); Ls = [rnd.randint(1, 6) for _ in range(h)]; upe = rnd.randint(0, 1)
    fl = rnd.choice(["none", "exitup", "chainup"]); Ms = [rnd.randint(1, 4) for _ in range(h)]
    mode = rnd.choice(["stored", "rstart", "rstart", "rbeta", "rbeta", "rev"]); s2 = rnd.randrange(10 ** 9)
    rid = f"{seed}_{i}"
    if rid in done: continue
    G, nm = ladder83.build(h, Ls, upe, fl, Ms)
    G = json.loads(json.dumps(G)); nm = json.loads(json.dumps(nm)); r2 = random.Random(s2)
    if mode in ("rstart", "rbeta"): G["start"] = [r2.randrange(len(o)) for o in G["opts"]]
    if mode == "rbeta":
        perm = list(range(len(G["br"]))); r2.shuffle(perm); G["br"] = perm
    os.environ["EORD"] = "rev" if mode == "rev" else "lev"
    try:
        r = lock222.analyse(G, nm)
        fo.write(f"RUN {rid} h {h} L {','.join(map(str, Ls))} upe {upe} fl {fl} M {','.join(map(str, Ms))} mode {mode} s2 {s2} "
                 f"N {G['N']} T {r['T']} C {r['C']} hyp {r['hyp']} viol {len(r['viol'])} maxmoves {r['maxmoves']} maxadopt {r['maxadopt']} maxreset {r['maxreset']}"
                 + (f" VIOL {r['viol'][:3]}" if r['viol'] else "") + "\n")
    except Exception as ex:
        fo.write(f"RUN {rid} ERROR {type(ex).__name__} {ex}\n")
    fo.flush()
