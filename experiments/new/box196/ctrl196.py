#!/usr/bin/env python3
"""COPY with credit (L-NEW successor 64, for packet P-N5-CHAIN): L-RED 58's experiments/red/r224/ctrl224.py at claude/l-red e7937985,
unchanged except that W196 defaults to this repository root (qt3_196.py here is byte-identical to l-new 08801298's). Original doc follows.
L-RED 58 R224 item 7 (4): controls for the five box-196 counters that have none (nonstd, cnlow, k2fail, crossflip, emon), by FAULT
INJECTION into L-NEW 64's own counter code, which is run unchanged: claude/l-new 08801298 experiments/new/box196/qt3_196.py check(),
imported from a worktree (env W196). Injection touches only evaluate() calls made
from check() itself (the counters' view); the algorithm (n5v.step, its arena engines, idealcyc) runs unchanged, except for FAULT=nonstd,
which perturbs the state the run continues from. A control passes when its counter is 0 on the clean run and > 0 on the injected run.
Faults (env FAULT):
  nonstd    after the first n5v.step, one beta with a mover Xi-target is set to its pb pad (a non-standard state);
  cnlow     every Engine.evaluate result: the first pad's bit is added to the Pi-set of vertex 0;
  k2fail    every evaluate: sigma-bar(K2) := K2;
  crossflip every second evaluate: sigma-bar toggled at every gate (pe <-> pbeta);
  emon      evaluate number 2 only: the most relevant e-vertex is removed from the Pi-set of every vertex whose Pi holds an e.
Usage: ctrl224.py G.json ...   (prints, per genome and fault, the clean and the injected counter)"""
import sys, os, json, importlib.util
W196 = os.environ.get("W196") or os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")); os.environ["Q196_ROOT"] = W196
spec = importlib.util.spec_from_file_location("qt3_196", os.path.join(W196, "experiments/new/box196/qt3_196.py"))
qt = importlib.util.module_from_spec(spec); sys.argv_saved = sys.argv; spec.loader.exec_module(qt)
n5v = qt.n5v; orig_eval = n5v.Engine.evaluate; orig_step = n5v.step
def run(G, fault):
    st = {"calls": 0, "steps": 0}
    def ev(self, sigma):
        vs, sb = orig_eval(self, sigma)
        if sys._getframe(1).f_code.co_name != "check": return vs, sb      # inject only into the counter code's own view
        st["calls"] += 1
        if fault in ("cnlow", "k2fail", "crossflip", "emon"):
            vs = list(vs); sb = list(sb); g = self.g if hasattr(self, "g") else None
            V = st["V"]; K2 = V[("K", 2)]
            if fault == "cnlow":
                pad = V["pA"]; lam, P, k = vs[0]; vs[0] = (lam, P | self.bit[pad], k)
            elif fault == "k2fail": sb[K2] = K2
            elif fault == "crossflip" and st["calls"] % 2 == 0:
                for gt, pe, pbt in st["gates"]: sb[gt] = pbt if sb[gt] == pe else pe
            elif fault == "emon" and st["calls"] == 2:
                for v in range(len(vs)):
                    lam, P, k = vs[v]; es = [u for u in st["evs"] if P & self.bit[u]]
                    if es: top = max(es, key=lambda u: self.rank[u]); vs[v] = (lam, P & ~self.bit[top], k)
        return vs, sb
    def stp(g, E, Ed, sigma, tau, mode):
        res = orig_step(g, E, Ed, sigma, tau, mode); st["steps"] += 1
        if fault == "nonstd" and res is not None and st["steps"] == 1:
            ns = list(res[0])
            for (b, xt, pb) in st["betas"]:
                if ns[b] == xt: ns[b] = pb; break
            res = (ns,) + tuple(res[1:])
        return res
    _, _, _, V = qt.gamma3.build(G, qt.eg195.PADS); st["V"] = V
    O = [(x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]
    st["gates"] = [(V[("g", o)], V[("pe", o)], V[("pbeta", o)]) for o in O]; st["evs"] = [V[("e", o)] for o in O]
    st["betas"] = [(V[("b", o)], G["opts"][o[0]][o[1]][1], V[("pb", o)]) for o in O if G["opts"][o[0]][o[1]][1] >= 0]
    n5v.Engine.evaluate = ev; n5v.step = stp
    try: return qt.check(G)
    finally: n5v.Engine.evaluate = orig_eval; n5v.step = orig_step
if __name__ == "__main__":
    for f in sys.argv[1:]:
        G = json.load(open(f)); clean = run(G, "none"); out = []
        for fault in ("nonstd", "cnlow", "k2fail", "crossflip", "emon"):
            r = run(G, fault); out.append(f"{fault} clean {clean.get(fault, 0)} injected {r.get(fault, 0)}")
        print(f"CTRL224 {os.path.basename(f)} T3 {clean['T3']} Q {clean['Q']} W {clean['W']} | " + " | ".join(out), flush=True)
