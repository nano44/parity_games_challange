#!/usr/bin/env python3
"""L-RED 65 R231 (b2): counter for Lemma ONE-CROSS (lane) on IDEAL-CYC(G), own engine (r221q/own.py). For every gate g whose face a in
{e_g, beta_g} has a CONSTANT value Omega_t(a) over the whole run: count changes of sigma-bar_t(g).
Must-0: xfail (gate with a constant face and >= 2 changes), dfail (a change away from the constant face, i.e. a -> b), tie (Omega(e) = Omega(beta)).
Descriptive: gates with a constant face, of them with exactly 1 change; gates with no constant face and >= 2 changes (control: shows the
counter can see repeated flips). Usage: onecross231.py G.json ... | onecross231.py rand SEED COUNT [k1]"""
import sys, os, json, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r221q"))
import own
from dep231 import rgen
from blk231 import xi_k
CTRL = os.environ.get("OC_CTRL") == "1"
def measure(G):
    out, V, O, ow = own.run(G, 20000); c = dict(gates=len(O), const=0, one=0, xfail=0, dfail=0, tie=0, multi_nonconst=0)
    for q in O:
        g, e, b = V[("g", q)], V[("e", q)], V[("b", q)]
        ve = [v[e] for _, v, _ in out]; vb = [v[b] for _, v, _ in out]; ch = [t[g] for _, _, t in out]
        c["tie"] += sum(1 for x, y in zip(ve, vb) if x == y)
        flips = [(ch[i], ch[i + 1]) for i in range(len(ch) - 1) if ch[i] != ch[i + 1]]
        if CTRL: const = [a for a, vs in ((e, ve), (b, vb)) if vs[:2] == [vs[0]] * min(2, len(vs))]   # control: «constant» = equal on the first two states only (first = last cannot fire: F1)
        else: const = [a for a, vs in ((e, ve), (b, vb)) if all(v == vs[0] for v in vs)]
        if const:
            c["const"] += 1; c["one"] += len(flips) == 1
            if len(flips) >= 2: c["xfail"] += 1
            if len(const) == 1 and any(f[0] == const[0] for f in flips): c["dfail"] += 1
        elif len(flips) >= 2: c["multi_nonconst"] += 1
    return c
if __name__ == "__main__":
    tot = {}
    if sys.argv[1] == "rand":
        rng = random.Random(int(sys.argv[2])); k1 = len(sys.argv) > 4; Gs = []
        while len(Gs) < int(sys.argv[3]):
            G = rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.choice([2, 3]))
            if not k1 or xi_k(G) == 1: Gs.append((f"r{len(Gs)}", G))
    else: Gs = [(os.path.basename(f), json.load(open(f))) for f in sys.argv[1:]]
    for tag, G in Gs:
        c = measure(G)
        for k, v in c.items(): tot[k] = tot.get(k, 0) + v
        if sys.argv[1] != "rand" or c["xfail"] or c["dfail"] or c["tie"]: print(tag, c, flush=True)
    print("TOTAL", tot, flush=True)
