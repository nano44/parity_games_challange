"""REFEREE packet 6 probe (Opus 5.5, D12), independent of dtl_rootmono.py. Subclasses experiments/alg/dtl_pyref.DTL.
Logs every tattr call (caller, Z_in, R, Gx, maxpr, seeds) -> set output; for Dom steps also the (R, X) of the dom() call.
Per phase (same player, same G), consecutive searches s, s+1, sptl entries dropped (e* not in sptl, R-P4):
 (1) per-input monotonicity: for each input I, outputs along the phase are non-decreasing (1.2b, incl. the Dom variant
     where only the top is pushed);
 (2) first difference e*: equal input, strictly larger output; caller counted; per-input e* chain length <= n;
 (3) Dom inputs per (R, X) and -1 attractor inputs per (R, X) over the phase (is the input fixed by (R, X)?).
Usage: p6probe.py [oink|stable] G.pg ..."""
import sys, os, inspect
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "..", "..")
sys.path.insert(0, os.path.join(ROOT, "experiments", "alg")); sys.path.insert(0, os.path.join(ROOT, "experiments", "harness")); sys.path.insert(0, os.path.join(ROOT, "experiments", "dtl-bench"))
import pg, dtl_pyref as P

class Probe(P.DTL):
    def __init__(s, *a, **k):
        super().__init__(*a, **k); s.searches = []; s.cur = None; s.domctx = None
    def search(s, p):
        s.cur = dict(p=p, G=frozenset(s.G), log=[]); s.searches.append(s.cur)
        return super().search(p)
    def dom(s, V, R, X, p):
        s.domctx = (frozenset(R), frozenset(X)); super().dom(V, R, X, p); s.domctx = None
    def tattr(s, p, Z, R, Gx, maxpr, consume):
        caller = inspect.stack()[1].function
        if caller == "search_rec" and s.domctx is None: caller = "m1"
        key = (caller, frozenset(Z), frozenset(R), frozenset(Gx), maxpr, frozenset(s.Q))
        ctx = s.domctx if caller == "dom" else ((frozenset(R),) if caller == "m1" else None)
        super().tattr(p, Z, R, Gx, maxpr, consume)
        if s.cur is not None and caller != "sptl":
            s.cur["log"].append((key, frozenset(Z), ctx))

def check(path, order, tot):
    g = pg.read(path) if hasattr(pg, "read") else pg.parse(open(path).read())
    P_DTL = P.DTL; P.DTL = Probe
    try: _, _, d = P.solve_game(g, order=order)
    finally: P.DTL = P_DTL
    ss = d.searches; n = d.n
    i = 0
    while i < len(ss):
        j = i
        while j + 1 < len(ss) and ss[j + 1]["p"] == ss[i]["p"] and ss[j + 1]["G"] == ss[i]["G"]: j += 1
        ph = ss[i:j + 1]; i = j + 1
        last = {}; chain = {}; dom_in = {}; m1_in = {}
        for k, s in enumerate(ph):
            for key, out, ctx in s["log"]:
                if key in last and not last[key] <= out: tot["mono_fail"] += 1; print("MONO FAIL", path, order, key[0])
                last[key] = out
                if key[0] == "dom": dom_in.setdefault(ctx, set()).add(key)
            if k + 1 < len(ph):
                a, b = s["log"], ph[k + 1]["log"]; tot["trans"] += 1
                e = next((x for x in range(min(len(a), len(b))) if a[x][:2] != b[x][:2]), None)
                if e is None: tot["no_diff"] += 1; continue
                if a[e][0] != b[e][0]: tot["input_differs"] += 1; print("INPUT DIFFERS at e*", path, order); continue
                if not a[e][1] < b[e][1]: tot["not_strict"] += 1; print("NOT STRICT", path, order); continue
                tot["e_" + a[e][0][0]] += 1
                chain.setdefault(a[e][0], []).append(b[e][1])
        for I, outs in chain.items():
            if len(outs) > n or any(not outs[x] < outs[x + 1] for x in range(len(outs) - 1)): tot["chain_fail"] += 1; print("CHAIN FAIL", path)
            tot["max_chain"] = max(tot["max_chain"], len(outs))
        for c, ks in dom_in.items():
            tot["dom_RX"] += 1
            byseed = {}
            for k in ks: byseed.setdefault(k[5], set()).add(k)
            if any(len(v) > 1 for v in byseed.values()): tot["dom_RX_step_input_varies"] += 1
            tot["max_dom_inputs_per_RX_top"] = max([tot["max_dom_inputs_per_RX_top"]] + [len(v) for v in byseed.values()])

if __name__ == "__main__":
    from collections import Counter
    order = sys.argv[1]; tot = Counter(max_chain=0, max_dom_inputs_per_RX_top=0)
    for f in sys.argv[2:]:
        try: check(f, order, tot)
        except Exception as ex: print("ERR", f, ex); tot["err"] += 1
    print(order, dict(tot))
