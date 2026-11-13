#!/usr/bin/env python3
"""L-COMP box 47: the port check (Lead 09:08Z): one47 (C, bin/one47) against L-NEW's one217.py (claude/l-new a32a588d, imported unchanged
from env LNEW217 = an archive root) for the rules key / howard / seq, and against n5v mode spec on Γ3 (replay47.run, env LNEW) for the key
rule, STATE BY STATE (the whole list of mover states, so lengths count).
Must-0 counter mism (unit (genome, comparison)): mism_k1 (C key vs one217 key), mism_h1 (C howard vs one217 howard), mism_s1 (C seq vs one217
seq), mism_kn (C key vs n5v spec, states up to the first fallback).
Numbering: a genome may carry "eperm" (replay47's convention: the e-vertex of the i-th option in gate order goes to the eperm[i]-th e-slot);
one217 then gets eidx = the e-index of each option after that renumbering (its eps), the C port gets er (gen47.py); n5v runs the renumbered game.
Control (env ONE47_CTRL=1 passed to the C port only): the C key uses a fixed permutation of the e-ranks; mism_k1 / mism_kn must fire.
Sets: towers (inst/towers), rand (one217's own generator eg195.gen(rng, "acyc"), half of them with a random eperm), mut (gen47 mutants of the
towers with random eperm, from bin/mut47). Usage: chk47.py towers | rand SEED COUNT | mut SEED PER | files F.json ...   (one line per genome, then a TOTAL line)"""
import sys, os, json, random, subprocess, tempfile
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
L217 = os.environ["LNEW217"]; NEW = os.path.join(L217, "experiments", "new")
sys.path[:0] = [os.path.join(NEW, "box217"), os.path.join(NEW, "box195")]; os.environ.setdefault("EG195_ROOT", L217)
import one217, replay47, gen47
CTRL = os.environ.get("ONE47_CTRL", "0")
def cstates(G):
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f: f.write(gen47.j2t(G)); p = f.name
    o = subprocess.run([os.path.join(H, "bin", "one47"), p, "--states"], capture_output=True, text=True, env=dict(os.environ, ONE47_CTRL=CTRL)).stdout; os.unlink(p)
    S = {"key": [], "howard": [], "seq": []}
    for l in o.splitlines():
        if l.startswith("S "): w = l.split(); S[w[1]].append(tuple(map(int, w[3:])))
    return S
def eidx(G):
    if "eperm" not in G: return None
    O = [(x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]; go = sorted(O, key=lambda q: G["gate"][q[0]][q[1]])
    return {q: G["eperm"][i] for i, q in enumerate(go)}
def one(name, G, tot):
    C = cstates(G); P = one217.OneP(G, eidx(G)); r = dict(key=P.run("key"), howard=P.run("howard"), seq=P.run("seq"))
    N5 = replay47.run(G, "spec")["seq"]
    m = dict(mism_k1=int(C["key"] != [tuple(s) for s in r["key"]]), mism_h1=int(C["howard"] != [tuple(s) for s in r["howard"]]),
             mism_s1=int(C["seq"] != [tuple(s) for s in r["seq"]]), mism_kn=int(C["key"] != [tuple(s) for s in N5]))
    for k, v in m.items(): tot[k] = tot.get(k, 0) + v
    tot["genomes"] = tot.get("genomes", 0) + 1; tot["maxT"] = max(tot.get("maxT", 0), len(C["key"]) - 1)
    print("%s N %d M %d eperm %d T_key %d (one217 %d, n5v %d) T_howard %d T_seq %d | %s | ctrl %s" % (name, G["N"], sum(len(o) for o in G["opts"]), int("eperm" in G),
          len(C["key"]) - 1, len(r["key"]) - 1, len(N5) - 1, len(C["howard"]) - 1, len(C["seq"]) - 1, " ".join("%s %d" % kv for kv in m.items()), CTRL), flush=True)
if __name__ == "__main__":
    a = sys.argv[1:]; tot = {}
    if a[0] == "towers": fs = sorted(os.path.join(H, "inst", "towers", f) for f in os.listdir(os.path.join(H, "inst", "towers")) if f.endswith(".json")); a = ["files"] + fs
    if a[0] == "files":
        for f in a[1:]:
            G = json.load(open(f)); G = G if "N" in G else G["genome"]; one(os.path.basename(f), G, tot)
    elif a[0] == "mut":                                          # mut SEED PER: PER mutants of each tower, 1 + (i mod 40) mutations each (PER <= 40)
        seed, per = int(a[1]), int(a[2]); td = os.path.join(H, "inst", "towers"); od = os.path.join(H, "inst", "mut"); os.makedirs(od, exist_ok=True)
        for t in sorted(f for f in os.listdir(td) if f.endswith(".json")):
            G0 = json.load(open(os.path.join(td, t))); G0 = G0 if "N" in G0 else G0["genome"]
            with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f: f.write(gen47.j2t(G0)); p = f.name
            for i in range(per):
                nm = "mut%d_%s_%d" % (seed, t[:-5], i); q = os.path.join(od, nm + ".txt")
                subprocess.run([os.path.join(H, "bin", "mut47"), p, str(seed * 1000 + i), str(1 + i % 40), q], check=True)
                G = gen47.t2j(open(q).read()); json.dump(G, open(os.path.join(od, nm + ".json"), "w"), sort_keys=True); os.unlink(q)
                one(nm, G, tot)
            os.unlink(p)
    elif a[0] == "rand":
        import eg195
        seed, cnt = int(a[1]), int(a[2]); rng = random.Random(seed); k = 0
        while k < cnt:
            G = eg195.gen(rng, "acyc")
            if G is None or G["N"] < 2: continue
            if k % 2: M = sum(len(o) for o in G["opts"]); p = list(range(M)); rng.shuffle(p); G["eperm"] = p
            one("rand%d_%d" % (seed, k), G, tot); k += 1
    print("TOTAL " + " ".join("%s %d" % kv for kv in sorted(tot.items())) + " ctrl %s" % CTRL, flush=True)
