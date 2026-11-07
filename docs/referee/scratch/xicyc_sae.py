"""REFEREE successor 26: BR-SEG-G replay on .pg files with own engine (xicyc_vj.py). Start: SPEC S3 / FIX 1 best-reward rule from its
text (Even v: highest even priority successor, else lowest odd; equal priorities: largest index if even, smallest if odd). Howard at
every Even vertex (keep current on ties, else larger index). Labels C / R / p; H0 per step; longest p-run vs n_E.
Usage: xicyc_sae.py FILE.pg..."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_vj import VJ
def read(path):
    pr = {}; ow = {}; su = {}
    for line in open(path):
        line = line.strip().rstrip(";")
        if not line or line.startswith("parity") or line.startswith("start"): continue
        t = line.split(); v = int(t[0]); pr[v] = int(t[1]); ow[v] = int(t[2]); su[v] = [int(a) for a in t[3].split(",")]
    n = max(pr) + 1; return [pr[v] for v in range(n)], [ow[v] for v in range(n)], [su[v] for v in range(n)]
def best_reward(pr, su, v):
    ev = [w for w in su[v] if pr[w] % 2 == 0]
    if ev: return max(ev, key=lambda w: (pr[w], w))
    return min(su[v], key=lambda w: (pr[w], w))
for f in sys.argv[1:]:
    pr, ow, su = read(f); n = len(pr); E = VJ(pr, ow, su); nE = sum(1 for v in range(n) if ow[v] == 0)
    s = [best_reward(pr, su, v) if ow[v] == 0 else None for v in range(n)]; st, val = E.best_reply(s); lab = []; h0fail = 0
    while True:
        ns = list(s)
        for v in range(n):
            if ow[v]: continue
            b = s[v]
            for u in su[v]:
                c = E.cmp(val[u], val[b])
                if c > 0 or (c == 0 and b != s[v] and u > b): b = u
            ns[v] = b
        if ns == s: break
        nst, nval = E.best_reply(ns, st)
        h0fail += not any(ns[v] != s[v] and val[v][0] != v and nval[v][0] != v for v in range(n))
        C = any(nval[v][0] != val[v][0] for v in range(n)); R = any(nst[v] != st[v] for v in range(n) if ow[v] == 1)
        lab.append("C" if C else ("R" if R else "p")); s, st, val = ns, nst, nval
    lab = "".join(lab); mp = max((len(r) for r in lab.replace("R", "C").split("C")), default=0)
    print(os.path.basename(f), "n", n, "nE", nE, "T", len(lab), "C", lab.count("C"), "R", lab.count("R"), "p", lab.count("p"), "longest p-run", mp,
          "H0-failing steps", h0fail, flush=True)
