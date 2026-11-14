"""REFEREE successor 26: DEAD ODD-FIXED rule-independence. For every R-step t -> t+1 of the IDEAL-CYC Howard run (own engine, no
Howard ties): necessary candidate sets of optimal Odd choices, C_t(v) := {u : ext(v, Om_t(u)) = Om_t(v)} if Lambda_t(v) != v, else
{u : Lambda_t(u) = v}. If C_t(v) and C_(t+1)(v) are disjoint at some Odd v, then NO Odd strategy is optimal in both states: the
sigma-bar change is forced for every deterministic rule. Usage: xicyc_oddfixed.py FILE.json..."""
import sys, os, json; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_replay import howard, lam_keep_max
def cand(E, val, v):
    if val[v][0] != v: return {u for u in E.succ[v] if E.cmp(E.ext(v, val[u]), val[v]) == 0}
    return {u for u in E.succ[v] if val[u][0] == v}
for f in sys.argv[1:]:
    G = json.load(open(f)); E, lab, ties, states, movers, idx = howard(G)
    out = []
    for t, c in enumerate(lab):
        if c != "R": continue
        a, b = states[t][2], states[t + 1][2]
        forced = [v for v in range(E.n) if E.owner[v] == 1 and not (cand(E, a, v) & cand(E, b, v))]
        lamkeep = all(a[v][0] == b[v][0] for v in range(E.n))
        out.append(f"step {t}->{t+1} Lambda-kept {lamkeep} forced-at {len(forced)} Odd vertices")
    print(os.path.basename(f), "N", G["N"], "Howard ties", ties, "labels", lab, "max Lambda-keeping run", lam_keep_max(E, states)); print("  " + "\n  ".join(out))
