#!/usr/bin/env python3
"""L-RED 56 R221 (Lead 00:36Z, POST-FALLBACK): run N5'-xi (box 190 n5v.step, mode xi) on Gamma3(G) (box 189 gamma3.build, all pads) and log
every iteration: mover option tuple change (M), other sigma change (S), tau change (t), fallback flag (F), and whether the fallback
switched sigma or tau. Summary: iterations, #fallbacks, phases (maximal runs between fallbacks) with their lengths, mover changes before
/ after the first fallback, own.py IDEAL-CYC T. Needs env WT, WT3 (r218/env.sh). Usage: post221.py [-v] G.json ..."""
import sys, os, json
WT, WT3 = os.environ["WT"], os.environ["WT3"]
sys.path[:0] = [os.path.join(WT3, "experiments/new/box191"), os.path.join(WT, "experiments/new/box190"), os.path.join(WT, "experiments/harness"), os.path.join(WT3, "experiments/new/box189")]
import gamma3, n5v, n5x, pg
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import own
def topg(g): return f"parity {g.n - 1};\n" + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n))
def post(G, cap=20000, verbose=False):
    T = len(own.run(G)[0]) - 1
    pads = {"K", "pe", "pb", "m"}; g, _, _, VV = gamma3.build(G, pads); gp = pg.parse(topg(g))
    E, Ed = n5v.Engine(gp), n5v.Engine(n5v.dual(gp)); sigma, tau = n5x.start_pair(gp, E, Ed, None)
    log = []; ms = gamma3.mover_state(G, VV, sigma, pads)
    while len(log) < cap:
        r = n5v.step(gp, E, Ed, sigma, tau, "xi")
        if r is None: break
        ns, nt, Is, It, fb = r; ms2 = gamma3.mover_state(G, VV, ns, pads)
        ent = dict(M=ms2 != ms, S=any(ns[v] != sigma[v] for v in range(gp.n)) and ms2 == ms, t=nt != list(tau), F=fb, Fs=fb and bool(Is))
        log.append(ent); sigma, tau, ms = ns, nt, ms2
        if verbose: print(len(log), ms2, "".join(k for k in "MStF" if ent[k]), "(fb sigma)" if ent["Fs"] else ("(fb tau)" if fb else ""))
    fbi = [i for i, e in enumerate(log) if e["F"]]; first = fbi[0] if fbi else len(log)
    cuts = [-1] + fbi + [len(log)]; phases = [cuts[i + 1] - cuts[i] - 1 for i in range(len(cuts) - 1)]
    return dict(N=G["N"], n=gp.n, T=T, xi=len(log), fb=len(fbi), fb_sigma=sum(e["Fs"] for e in log), phases=phases,
                Mpre=sum(e["M"] for e in log[:first]), Mpost=sum(e["M"] for e in log[first:]), tpost=sum(e["t"] for e in log[first:]))
if __name__ == "__main__":
    v = "-v" in sys.argv
    for f in [a for a in sys.argv[1:] if a != "-v"]:
        try: G = json.load(open(f))
        except Exception: continue
        if not (isinstance(G, dict) and "opts" in G): continue
        print(f.split("/")[-1], post(G, verbose=v), flush=True)
