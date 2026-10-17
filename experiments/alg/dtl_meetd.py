"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 7), GAP-C §18r: which statement survives kin_viol_n29 (L-RED R29,
RESULTS DE13)? For every search(p) with D := W_p(G') ≠ ∅ (Zielonka on G'), classify:
  (K)        the search learns some new tangle or finds a dominion (plain Lemma K);
  (MEET)     the search learns a new tangle MEETING D, or finds a dominion;
  (IN)       the search learns a new tangle INSIDE D, or finds a dominion (= (K-in) plus dominions);
  (PHASE-IN) the search, or a later search of the same player before the next dominion (same G', same D), learns a new
             tangle inside D or finds a dominion;
  (PHASE-IN-MEET) MEET at this search and PHASE-IN.
Games and env as dtl_step5stats.games (UNIONS, UM_CROSS, SEED, NMAX, RANDOM); MIXED=1 keeps only mixed searches
(|W_{1-p}| >= 3). DTL_ORDER = oink | stable. Usage: dtl_meetd.py G.pg ...   (prints the first failures of each)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_step5 as S5, dtl_step5stats as ST
tab = {}; shown = {}


def bump(k, ok, f, extra=""):
    key = f"{k} {'holds' if ok else 'FAILS'}"; tab[key] = tab.get(key, 0) + 1
    if not ok and shown.get(k, 0) < 3:
        shown[k] = shown.get(k, 0) + 1; print(f"{k} FAILS {f if f.startswith('union') else os.path.relpath(f)} {extra}", flush=True)


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    mixed = os.environ.get("MIXED") == "1"
    for f, g in ST.games(sys.argv[1:]):
        d = S5.build(g); d.run()
        if not all(w is not None for w in d.win): print("INCOMPLETE RUN", f, flush=True)
        tr = d.trace
        for i, t in enumerate(tr):
            D = t["Wp"]
            if not D or (mixed and len(t["G"]) - len(D) < 3): continue
            new = t["newt"]; dom = t["dom"]
            K = dom or bool(new); MEET = dom or any(C & D for C in new); IN = dom or any(C <= D for C in new)
            ph = False
            for u in tr[i:]:
                if u["p"] != t["p"] or u["G"] != t["G"]: 
                    if u["p"] == t["p"]: break
                    continue
                if u["dom"] or any(C <= D for C in u["newt"]): ph = True; break
                if u["dom"]: break
            ex = f"search {i} p={t['p']} |G'|={len(t['G'])} |D|={len(D)} new={[sorted(d.idx[v] for v in C) for C in new]}"
            bump("(K)", K, f, ex); bump("(MEET)", MEET, f, ex); bump("(IN)", IN, f, ex); bump("(PHASE-IN)", ph, f, ex)
            bump("(PHASE-IN-MEET)", ph and MEET, f, ex)
    print({k: tab[k] for k in sorted(tab)})
