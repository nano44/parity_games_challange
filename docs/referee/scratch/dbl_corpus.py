"""REFEREE successor 26: own-simulator cross-check of P-IDEAL-DBL §2-§4 on corpus genomes (t3r_sim.py + dbl_replay.analyse; the corpus
genomes are read from git at l-new 9995f5a2 by path, list taken from L-SI's corpus_lr.json.gz paths only).
Adds HIT ((mover, step): value of the current option changes iff the old chain meets Mv_t; MONO: no fall) and ALT-MIN (a)-(d) per mover.
Usage: dbl_corpus.py CORPUS_GZ MAXN"""
import sys, os, json, gzip, subprocess, itertools, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t3r_sim as S, dbl_replay as D
gz, maxn = sys.argv[1], int(sys.argv[2]); C = collections.Counter()
def score(G, P):   # ENC integer of a beta set
    return sum((1 if G["bp"][b] == 0 else -1) * 2 ** G["br"][b] for b in P)
for blob, path, _ in json.loads(gzip.open(gz).read()):
    G = json.loads(subprocess.run(["git", "show", "9995f5a2:" + path], capture_output=True, text=True, check=True).stdout)
    if G["N"] > maxn or not S.in_LR(G): continue
    C["genomes"] += 1
    for s0 in itertools.product((0, 1), repeat=G["N"]):
        o, st = D.analyse(G, list(s0)); C["runs"] += 1; C["steps"] += o["T"]
        for v in o["viol"]: C["viol " + v[0]] += 1
        C["doubling (run, level)"] += len(o["doubling"]); N = G["N"]; T = o["T"]
        val = [[score(G, S.value(G, s, x, k)) for x in range(N) for k in range(2)] for s in st]
        V = lambda t, x, k: val[t][2 * x + k]
        for x in range(N):
            rise = 0
            for t in range(1, T + 1):
                cur0, cur1 = V(t - 1, x, st[t - 1][x]), V(t, x, st[t][x])
                if cur1 < cur0: C["viol MONO"] += 1
                chain = [x]; z = G["opts"][x][st[t - 1][x]][1]
                while z >= 0: chain.append(z); z = G["opts"][z][st[t - 1][z]][1]
                hit = any(st[t][z] != st[t - 1][z] for z in chain); C["HIT units"] += 1
                if (cur1 > cur0) != hit: C["viol HIT"] += 1
            pi = [0 if V(t, x, 0) > V(t, x, 1) else 1 for t in range(T + 1)]
            Rk = [sum(1 for t in range(1, T + 1) if V(t, x, k) > V(t - 1, x, k)) for k in range(2)]
            ch = [sum(1 for t in range(1, T + 1) if pi[t] != pi[t - 1] and pi[t] == k) for k in range(2)]
            mv = o["moves"][x]; m = min(Rk); C["ALT units"] += 1
            for k in range(2):
                if ch[k] > Rk[k]: C["viol ALTa"] += 1
                y = G["opts"][x][k][1]
                Ry = 0 if y < 0 else sum(1 for t in range(1, T + 1) if V(t, y, st[t][y]) > V(t - 1, y, st[t - 1][y]))
                if Rk[k] != Ry: C["viol ALTd"] += 1
            if sum(ch) > 2 * m + 1: C["viol ALTb"] += 1
            if mv > 2 + 2 * m: C["viol ALTc"] += 1
print(f"own cross-check, corpus genomes with N <= {maxn}, every start:", dict(sorted(C.items())))
