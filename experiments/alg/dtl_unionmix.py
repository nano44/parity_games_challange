"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5): MIXED test games for GAP-C from disjoint unions of two corpus
games (priorities kept, ids shifted). For every search of p with W_p(G') != {}, |W_{1-p}(G')| >= 3 and no dominion, checks
(K4-B) (first stable piece's regions inside W_p) and (K-in); with UM_KFIRST=1 it checks (K-first) and (K-in) instead. UM_CROSS=k adds k random cross edges between the two
components (interacting mixed games). DTL_ORDER = oink | stable. Usage: dtl_unionmix.py nmax seed pairs G.pg ..."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_k4b as KB, dtl_whichpiece as WPm
if __name__ == "__main__":
    sys.setrecursionlimit(100000); nmax, seed, pairs = map(int, sys.argv[1:4]); games = [pg.read(f) for f in sys.argv[4:]]
    games = [g for g in games if g.n <= nmax]; rnd = random.Random(seed); tab = {}; tested = 0
    for k in range(pairs):
        a, b = rnd.sample(games, 2); off = a.n
        succ = [list(s) for s in a.succ] + [[w + off for w in s] for s in b.succ]
        for _ in range(int(os.environ.get("UM_CROSS", "0"))):          # random cross edges between the two components
            u = rnd.randrange(a.n + b.n); w = rnd.randrange(off, a.n + b.n) if u < off else rnd.randrange(0, off)
            succ[u] = sorted(set(succ[u]) | {w})
        g = pg.Game(list(a.prio) + list(b.prio), list(a.owner) + list(b.owner), succ)
        if os.environ.get("UM_KFIRST") == "1":
            d0 = KB.K.P.build(g); d = WPm.WP(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.run()
            for tr in d.trace:
                W = tr["Wp"]; G = set(tr["G"])
                if not W or len(G - W) < 3 or tr["d1"] > tr["dom"] or not tr["pieces"]: continue
                tested += 1; pcs = tr["pieces"]; passes = tr["passes"]; hi = pcs[1]["passes_from"] if len(pcs) > 1 else len(passes)
                ok = any(tops and tops[-1] in W and any(t == tops[-1] and C <= W for t, C in ev) for tops, ev in passes[pcs[0]["passes_from"]:hi])
                fw = next((i for i, pc in enumerate(pcs) if pc["V"] & W), None)
                okw = fw is not None and any(t and t[-1] in W and any(x == t[-1] and C <= W for x, C in ev) for t, ev in passes[pcs[fw]["passes_from"]:(pcs[fw + 1]["passes_from"] if fw + 1 < len(pcs) else len(passes))])
                okl = any(t and t[-1] in W and any(x == t[-1] and C <= W for x, C in ev) for t, ev in passes)
                key = ("K-first holds" if ok else "K-first VIOLATION", "FIRST-W holds" if okw else "FIRST-W VIOLATION", "K-low holds" if okl else "K-low VIOLATION", "K-in holds" if any(C <= W for C in tr["newt"]) else "K-in VIOLATION")
                if not (okw and okl): pg.write(g, f"/tmp/claude-0/-home-user-parity-games-challange/0dd58dc3-4d81-5440-a264-2427cc618519/scratchpad/cross_viol_{seed}_{k}.pg"); print("VIOLATION", key, "pair", k, flush=True)
                tab[key] = tab.get(key, 0) + 1
                if not ok and not os.environ.get("UM_CROSS"): pg.write(g, f"/tmp/claude-0/-home-user-parity-games-challange/0dd58dc3-4d81-5440-a264-2427cc618519/scratchpad/union_kfirst_viol_{seed}_{k}.pg")
            continue
        d0 = KB.K.P.build(g); d = KB.K4B(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.run()
        for tr in d.trace:
            W = tr["Wp"]; G = set(tr["G"])
            if not W or len(G - W) < 3 or tr["d1"] > tr["dom"] or "first" not in tr: continue
            tested += 1; V, Z, R = tr["first"]
            key = ("regions inside W_p" if Z <= W else "K4-B VIOLATION", "learned inside W_p" if any(C <= W for C in tr["newt"]) else "K-in VIOLATION")
            tab[key] = tab.get(key, 0) + 1
            if key != ("regions inside W_p", "learned inside W_p"): print("VIOLATION", key, "pair", k, flush=True); pg.write(g, f"/tmp/claude-0/-home-user-parity-games-challange/0dd58dc3-4d81-5440-a264-2427cc618519/scratchpad/union_viol_{seed}_{k}.pg")
    print(f"pairs {pairs}: mixed searches tested {tested};", tab)
