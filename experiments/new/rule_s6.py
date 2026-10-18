#!/usr/bin/env python3
"""Box 2 (1): S6 (Cunningham, index order) on switchbestexp under numberings given by an explicit RULE, i.e. a numbering defined
for every N from the vertex labels alone (no per-N search). A rule: an order of the label classes (label without its trailing
bit index; e, e', f, ... are different classes), a direction per class (bit index ascending or descending), and a mode:
'class' (class-major: all of class 1 by bit, then class 2, ...) or 'bit' (bit-major: unindexed classes first, then for each bit
the classes in rule order). The climb runs over rules (not numberings) with fitness = Cunningham iterations at N = --fitN;
the best rule is then applied unchanged to N = 2..--maxN and every count is the vjfast count (verbatim copy of L-SI's engine).
Usage: rule_s6.py climb --steps S --seed X [--fitN 4] [--rule-out r.json]
       rule_s6.py apply r.json --maxN 8 [--write DIR]   (prints N, n, iterations, sha1 of the renumbered game)"""
import sys, os, re, json, random, subprocess, hashlib, argparse
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "harness")); import pg
GEN = os.path.join(HERE, "..", "hard-families", "pgsolver_port.py"); TMP = os.path.join(HERE, "out", "s6rule"); os.makedirs(TMP, exist_ok=True)
_cache = {}
def game(N):
    if N not in _cache:
        t = subprocess.run(["python3", GEN, "switchbestexp", str(N)], capture_output=True, text=True, check=True).stdout
        _cache[N] = pg.parse("".join(l for l in t.splitlines(True) if not l.lstrip().startswith("%")))
    return _cache[N]
def split(lab):
    m = re.match(r"^(.*?)(\d+)$", lab); return (m.group(1), int(m.group(2))) if m else (lab, -1)
def classes(N): return sorted({split(l)[0] for l in game(N).labels})
def order(rule, N):
    g = game(N); rank = {c: i for i, c in enumerate(rule["order"])}
    def key(v):
        c, i = split(g.labels[v]); r = rank.get(c, len(rank)); d = i if rule["dir"].get(c, 1) > 0 else -i
        if rule["mode"] == "class": return (r, d)
        return (0, r, 0) if i < 0 else (1, i if rule.get("bitdir", 1) > 0 else -i, r)
    return sorted(range(g.n), key=key)
def text(rule, N):
    g = game(N); od = order(rule, N); new = {v: k for k, v in enumerate(od)}
    out = [f"parity {g.n - 1};"]
    for v in od: out.append(f"{new[v]} {g.prio[v]} {g.owner[v]} {','.join(str(new[w]) for w in g.succ[v])} \"{g.labels[v]}\";")
    return "\n".join(out) + "\n"
def count(rule, N, path=None):
    t = text(rule, N); p = path or os.path.join(TMP, f"cur_{os.getpid()}.pg"); open(p, "w").write(t)
    r = subprocess.run([os.path.join(HERE, "vjfast"), "cunningham", p, "/dev/null"], capture_output=True, text=True, timeout=600)
    m = re.search(r"with (\d+) iterations", r.stdout + r.stderr); return (int(m.group(1)) if m else -1), hashlib.sha1(t.encode()).hexdigest()
def mutate(rule, rng):
    r = json.loads(json.dumps(rule)); k = rng.random(); o = r["order"]
    if k < 0.5: i, j = rng.randrange(len(o)), rng.randrange(len(o)); o[i], o[j] = o[j], o[i]
    elif k < 0.7: i = rng.randrange(len(o)); c = o.pop(i); o.insert(rng.randrange(len(o) + 1), c)
    elif k < 0.9: c = rng.choice(o); r["dir"][c] = -r["dir"].get(c, 1)
    elif k < 0.95: r["mode"] = "bit" if r["mode"] == "class" else "class"
    else: r["bitdir"] = -r.get("bitdir", 1)
    return r
if __name__ == "__main__":
    a = argparse.ArgumentParser(); a.add_argument("cmd"); a.add_argument("rule", nargs="?"); a.add_argument("--steps", type=int, default=300)
    a.add_argument("--seed", type=int, default=1); a.add_argument("--fitN", type=int, default=4); a.add_argument("--maxN", type=int, default=8)
    a.add_argument("--rule-out"); a.add_argument("--write"); a.add_argument("--init"); x = a.parse_args(); rng = random.Random(x.seed)
    if x.cmd == "climb":
        cs = classes(x.fitN)
        cur = json.load(open(x.init)) if x.init else {"order": rng.sample(cs, len(cs)), "dir": {c: rng.choice([1, -1]) for c in cs}, "mode": rng.choice(["class", "bit"]), "bitdir": 1}
        best = count(cur, x.fitN)[0]; print("start", best, flush=True)
        for s in range(x.steps):
            cand = mutate(cur, rng); f = count(cand, x.fitN)[0]
            if f >= best:
                if f > best: print(f"step {s} fitness {f}", flush=True)
                cur, best = cand, f
        print("best", best); json.dump(cur, open(x.rule_out or os.path.join(TMP, f"rule_seed{x.seed}.json"), "w"), indent=0)
    else:
        rule = json.load(open(x.rule))
        for N in range(2, x.maxN + 1):
            p = os.path.join(x.write, f"sbe_rule_N{N}.pg") if x.write else None
            c, h = count(rule, N, p); print(N, game(N).n, c, h, flush=True)
