"""REFEREE successor 26: P-IDEAL-DBL replays with the referee's own IDEAL simulator t3r_sim.py (written from R104's text; no L-SI code).
Per run: F(l) (flips of the pair (2l, 2l+1): change of the order of the keys of their current options between consecutive states,
keys under each state), moves per mover, DBL-EQ (a) both directions at every level >= 1, (b) and (c) at doubling levels, WINDOW-ONCE,
TOWER-NEED (P(x) >= f + 2, both Xi-targets movers with R >= (f-1)/2 for f >= 2), PASS-FREEZE where applicable, ALIGN's c_l.
Usage: dbl_replay.py FILE.json [START_STRING]"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t3r_sim as S

def keyo(G, s, x):
    return S.key(G, s, x, s[x], {})

def analyse(G, start=None):
    N = G["N"]; d = N // 2; st = S.run(G, start); T = len(st) - 1
    order = lambda s, l: keyo(G, s, 2 * l) < keyo(G, s, 2 * l + 1)
    flips = {l: [t for t in range(1, T + 1) if order(st[t - 1], l) != order(st[t], l)] for l in range(d)}
    F = [len(flips[l]) for l in range(d)]
    mv = [[t for t in range(1, T + 1) if st[t][x] != st[t - 1][x]] for x in range(N)]
    c = lambda s, l: 0 if keyo(G, s, 2 * (l - 1)) < keyo(G, s, 2 * (l - 1) + 1) else 1
    gam = lambda l, j: G["gate"][2 * l][j] < G["gate"][2 * l + 1][j]
    out = dict(T=T, F=F, moves=[len(m) for m in mv], viol=[])
    for l in range(1, d):
        p, q = 2 * l, 2 * l + 1; B = set(flips[l - 1]); Phi = lambda t: sum(st[t][x] != c(st[t], l) for x in (p, q))
        conds = (Phi(0) == 2 and Phi(T) == 0 and all(Phi(t - 1) == 0 for t in B)
                 and not any(st[t][p] != st[t - 1][p] and st[t][q] != st[t - 1][q] for t in range(1, T + 1))
                 and set(flips[l]) == {t for t in range(1, T + 1) if st[t][p] != st[t - 1][p] or st[t][q] != st[t - 1][q]})
        dbl = F[l] == 2 * F[l - 1] + 2
        if conds != dbl: out["viol"].append(("DBLa", l))
        starts = [1] + sorted(t for t in B if t > 1); wins = [(a, (starts[i + 1] - 1 if i + 1 < len(starts) else T)) for i, a in enumerate(starts)]
        for (a, e) in wins:
            for x in (p, q):
                k = sum(1 for t in mv[x] if a <= t <= e)
                if k > 1: out["viol"].append(("WO", l, a, x))
                if dbl and k != 1: out["viol"].append(("DBLb", l, a, x))
            if dbl:
                first = min((t, x) for x in (p, q) for t in mv[x] if a <= t <= e)[1]
                if gam(l, 0) != gam(l, 1) or (first == p) != (not gam(l, 0)): out["viol"].append(("DBLc", l, a))
        if dbl:
            f = F[l - 1]
            for x in (p, q):
                if len(mv[x]) != f + 1: out["viol"].append(("TN-moves", l, x))
                if npaths(G, x) < f + 2: out["viol"].append(("TN-P", l, x))
                if f >= 2:
                    for k in (0, 1):
                        y = G["opts"][x][k][1]
                        if y < 0 or rises(G, st, y) < (f - 1) / 2: out["viol"].append(("TN-R", l, x, k))
    out["doubling"] = [l for l in range(1, d) if F[l] == 2 * F[l - 1] + 2]
    return out, st

def npaths(G, x, memo=None):
    memo = {} if memo is None else memo
    if x in memo: return memo[x]
    r = sum(1 if G["opts"][x][k][1] < 0 else npaths(G, G["opts"][x][k][1], memo) for k in range(len(G["opts"][x])))
    memo[x] = r; return r

def rises(G, st, y):
    vals = [S.value(G, s, y, s[y]) for s in st]
    return sum(1 for a, b in zip(vals, vals[1:]) if a != b)

if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); start = [int(ch) for ch in sys.argv[2]] if len(sys.argv) > 2 else None
    o, st = analyse(G, start)
    print(os.path.basename(sys.argv[1]), "in_LR", S.in_LR(G), "start", "".join(map(str, st[0])), "T", o["T"], "F", o["F"], "doubling", o["doubling"],
          "moves", o["moves"], "violations", o["viol"])
