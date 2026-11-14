#!/usr/bin/env python3
"""L-RED-B B7: the engine's answers against Oink (pinned 8fbf0a7) and the fleet's harness verifier.
For each game and each rule (howard, rf): regions against `oink --zlk` and `oink --tl` (rz, rt: region mismatches), the
engine's solution file (regions + both strategies) through Oink's `verify` tool (ov: runs it rejects) and through
experiments/harness/verify.py (hv).  All four must be 0.  B7_CTRL=2 flips one region bit (all must fire).
Usage: xoink.py lmcs NMAX | rand SEED COUNT NMAX | pg FILE [START]"""
import sys, os, subprocess, random, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "harness"))
import si7, gens7, st7
OINK = os.path.join(ROOT, "tools", "oink", "build")
CTRL = int(os.environ.get("B7_CTRL", "0"))


def oink_regions(pgpath, solver, n):
    out = pgpath + "." + solver + ".sol"
    r = subprocess.run([os.path.join(OINK, "oink"), "--" + solver, pgpath, out], capture_output=True, text=True)
    if r.returncode != 0:
        return None
    reg = [None] * n
    for line in open(out).read().replace("\n", " ").split(";"):
        a = line.split()
        if len(a) >= 2 and a[0] != "paritysol":
            reg[int(a[0])] = int(a[1])
    return reg


def check(g, s0, tmp, tag):
    import pg as hpg, verify as hver
    c = dict(rz=0, rt=0, ov=0, hv=0); its = {}
    pgp = os.path.join(tmp, tag + ".pg"); open(pgp, "w").write(si7.dump_pg(g))
    rz = oink_regions(pgp, "zlk", g.n); rt = oink_regions(pgp, "tl", g.n)
    for name, rule in (("howard", si7.howard()), ("rf", si7.root_first())):
        E = si7.Engine(g); k, sigma, val, tau = E.run(s0, rule); its[name] = k
        reg = E.regions(val)
        if CTRL == 2:
            reg[0] ^= 1
        c["rz"] += int(reg != rz); c["rt"] += int(reg != rt)
        solp = os.path.join(tmp, f"{tag}.{name}.sol")
        with open(solp, "w") as f:
            f.write(f"paritysol {g.n - 1};\n")
            for v in range(g.n):
                s = sigma[v] if g.owner[v] == 0 else tau[v]
                f.write(f"{v} {reg[v]} {s};\n" if g.owner[v] == reg[v] else f"{v} {reg[v]};\n")
        r = subprocess.run([os.path.join(OINK, "verify"), pgp, solp], capture_output=True, text=True)
        c["ov"] += int(r.returncode != 0)
        hg = hpg.Game(g.prio, g.owner, g.succ)
        strat = [(sigma[v] if g.owner[v] == 0 else tau[v]) if g.owner[v] == reg[v] else None for v in range(g.n)]
        c["hv"] += int(bool(hver.check(hg, reg, strat)))
    return c, its


if __name__ == "__main__":
    a = sys.argv[1:]; tot = dict(rz=0, rt=0, ov=0, hv=0); games = 0
    with tempfile.TemporaryDirectory() as tmp:
        if a[0] == "lmcs":
            for ver in ("fig4", "table4"):
                for n in range(1, int(a[1]) + 1):
                    g, s0 = gens7.lmcs(n, ver); c, its = check(g, s0, tmp, f"lmcs_{ver}_{n}"); games += 1
                    for k in tot: tot[k] += c[k]
                    print(f"B7 xoink lmcs {ver} n {n}: howard {its['howard']} rf {its['rf']} | " + " ".join(f"{k} {c[k]}" for k in c), flush=True)
        elif a[0] == "rand":
            rng = random.Random(int(a[1]))
            for i in range(int(a[2])):
                n = rng.randint(2, int(a[3])); g = st7.rand_game(rng, n)
                s0 = [rng.choice(g.succ[v]) if g.owner[v] == 0 else -1 for v in range(n)]
                c, its = check(g, s0, tmp, f"r{i}"); games += 1
                for k in tot: tot[k] += c[k]
        elif a[0] == "pg":
            g = si7.parse_pg(open(a[1]).read()); E = si7.Engine(g)
            s0 = si7.read_start(a[2], g) if len(a) > 2 else E.initial("best")
            c, its = check(g, s0, tmp, "g"); games += 1
            for k in tot: tot[k] += c[k]
            print(f"B7 xoink pg {os.path.basename(a[1])}: howard {its['howard']} rf {its['rf']}")
    print(f"B7 xoink {a[0]} games {games} ctrl {CTRL}: " + " ".join(f"{k} {tot[k]}" for k in tot))
    sys.exit(1 if any(tot.values()) else 0)
