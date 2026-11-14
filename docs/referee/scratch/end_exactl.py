"""REFEREE successor 29: P-N5-END EXACT-L / ENDGAME-3-N5 replay under SPEC's exact tie-breaks.
Game Gamma3(G) from MY builder (xicyc_replay.build, pad=True). N5 = L-COMP's n5b.py in --mode spec (SPEC S1 choices; not L-NEW's code),
run from its S3 start (initial_strategy_by_best_reward), compared with my FIX-1 start (end_replay.s3_start). L(G) from t3r_sim.run
(successor 24's own IDEAL simulator). IDEAL-ACYC by my own test (self-loops count). Checks on n5b's trace (my code):
  K-config sequence: k0 on states 0..F-1, k1 at F, k2 at F+1, k3 at F+2 = final; tau constant; exactly one fallback, at F; total F + 2;
  final beta's with a mover Xi-target on pb.  EXACT-L: F = L + 1 and total = L + 3 on IDEAL-ACYC genomes.
Usage: end_exactl.py N5SECOND_DIR gen FAMILY SEED COUNT | N5SECOND_DIR files G.json ..."""
import sys, os, json, random, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
D = sys.argv[1]; sys.path[:0] = [D, os.path.join(D, "..", "hard-families"), os.path.join(D, "..", "harness")]
import n5b, pg
from xicyc_replay import build
import t3r_sim
from end_replay import acyclic, s3_start, gen
n5b.MODE = "spec"

def one(G):
    prio, own, fs, sig0, movers, idx, succ = build(G, True); n = len(prio)
    g = pg.parse(f"parity {n - 1};\n" + "".join(f"{v} {prio[v]} {own[v]} {','.join(map(str, succ[v]))};\n" for v in range(n)))
    K0, K1, K2, K3 = (idx[("K", i)] for i in range(4)); pA, s_, q = idx["pA"], idx["s"], idx["q"]
    k0, k1, k2, k3 = (pA, s_, K2), (K1, s_, K2), (K1, q, K2), (K1, q, K1)
    N = G["N"]; O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]
    s = n5b.N5(g); tr = []; fbt = []; win, strat, it, fb = s.run(trace=tr, fbtrace=fbt)
    st3, _ = s3_start(prio, own, succ)
    startok = all(tr[0][0][v] == st3[v] for v in range(n) if own[v] == 0) and all(tr[0][1][v] == st3[v] for v in range(n) if own[v] == 1)
    Ks = [(S[K0], S[K1], S[K3]) for S, T in tr]; taus = set(T for S, T in tr)
    F = fbt.index(1) + 1 if 1 in fbt else None
    bad = collections.Counter()
    bad["tau"] += len(taus) != 1; bad["nfb"] += fb != 1
    if F is None: bad["nofb"] += 1
    else:
        bad["k0"] += any(k != k0 for k in Ks[:F]); bad["k1"] += len(Ks) <= F or Ks[F] != k1
        bad["k2"] += len(Ks) <= F + 1 or Ks[F + 1] != k2; bad["k3"] += len(Ks) != F + 3 or Ks[-1] != k3
        bad["total"] += it != F + 2
        fin = tr[-1][0]; bad["pb"] += any(G["opts"][x][k][1] >= 0 and fin[idx[("b", (x, k))]] != idx[("pb", (x, k))] for x, k in O)
    return bad, it, F, startok

def main():
    if sys.argv[2] == "gen":
        fam, seed, cnt = sys.argv[3], int(sys.argv[4]), int(sys.argv[5]); rng = random.Random(seed)
        gl = [(f"{fam}{seed}#{i}", gen(rng, fam)) for i in range(cnt)]
    else: gl = [(os.path.basename(f), json.load(open(f))) for f in sys.argv[3:]]
    tot = collections.Counter(); acyc = lfail = 0; Lmax = 0; startbad = 0; Fmax = 0
    for name, G in gl:
        bad, it, F, startok = one(G); tot.update(bad); startbad += not startok; Fmax = max(Fmax, F or 0)
        ac = acyclic(G); L = len(t3r_sim.run(G)) - 1 if ac else None
        if ac:
            acyc += 1; Lmax = max(Lmax, L); lf = F != L + 1 or it != L + 3; lfail += lf
        if sys.argv[2] == "files" or any(bad.values()) or (ac and lf):
            print(" ", name, "IDEAL-ACYC" if ac else "not-acyclic", "L", L, "F", F, "iters", it, dict(+bad), "EXACT-L FAIL" if ac and lf else "")
    keys = ["tau", "nfb", "nofb", "k0", "k1", "k2", "k3", "total", "pb"]
    print(f"n5b-spec {' '.join(sys.argv[2:6]) if sys.argv[2] == 'gen' else 'files ' + str(len(gl))}: runs {len(gl)} |",
          " ".join(f"{k} {tot[k]}" for k in keys), f"| start != my S3 {startbad} | maxF {Fmax} | IDEAL-ACYC {acyc} lfail {lfail} maxL {Lmax}")

if __name__ == "__main__":
    main()
