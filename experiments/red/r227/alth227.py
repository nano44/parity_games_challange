#!/usr/bin/env python3
"""L-RED 61 R227: check Lemma ALT-H on own.py runs. Per (v, maximal Lambda-interval I), tops = most relevant e of each E-change.
ALT-H(i): every top ENTERS (top in the new set)   [all e-vertices have even priority, so an improving change's top is new].
ALT-H(ii): for every symbol y: #(tops == y) <= 1 + #(tops strictly more relevant than y, strictly between the first and last y-top).
ALT-H(iii): alt(x, y) <= 2 * (1 + H) + 1, H = #(tops strictly more relevant than max(x, y)) in I.
Prints per file: intervals, maxalt, violations of (i)-(iii), and the max over intervals of (alt, H_pair) at the max-alt pair.
Usage: alth227.py G.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r226"), os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
import own
def altpair(tops, x, y):
    L = 0; want = x
    for z in tops:
        if z == want: L += 1; want = y if want == x else x
    return L
def check(G, cap=3000):
    out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); rk = own.VJ(prio).rk; evs = {V[("e", q)] for q in O}
    T = len(out) - 1; viol = [0, 0, 0]; nI = 0; best = (0, 0)
    for v in range(n):
        t = 0
        while t <= T:
            u = t
            while u + 1 <= T and out[u + 1][1][v][0] == out[t][1][v][0]: u += 1
            prev = None; tops = []
            for i in range(t, u + 1):
                E = frozenset(e for e in out[i][1][v][1] if e in evs)
                if prev is not None and E != prev:
                    z = max(E ^ prev, key=lambda e: rk[e]); tops.append(z)
                    if z not in E: viol[0] += 1
                prev = E
            if tops:
                nI += 1; S = set(tops)
                for y in S:
                    idx = [i for i, z in enumerate(tops) if z == y]
                    above = sum(1 for z in tops[idx[0] + 1:idx[-1]] if rk[z] > rk[y])
                    if len(idx) > 1 + above: viol[1] += 1
                for x in S:
                    for y in S:
                        if x == y: continue
                        a = altpair(tops, x, y); top = x if rk[x] > rk[y] else y; Hc = sum(1 for z in tops if rk[z] > rk[top])
                        if a > 2 * (1 + Hc) + 1: viol[2] += 1
                        best = max(best, (a, -Hc))
            t = u + 1
    return nI, viol, best[0], -best[1], T
if __name__ == "__main__":
    tot = [0, 0, 0]
    for f in sys.argv[1:]:
        nI, viol, a, Hc, T = check(json.load(open(f)))
        tot = [p + q for p, q in zip(tot, viol)]
        print(os.path.basename(f), "T", T, "intervals", nI, "viol(i,ii,iii)", viol, "maxalt", a, "H at a max-alt pair (min)", Hc, flush=True)
    print("TOTAL viol", tot)
