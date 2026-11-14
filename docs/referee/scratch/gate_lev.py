"""REFEREE successor 31: P-N5-GATE SAME-SUFFIX copy rows and DEAD numbers with own code (xicyc_replay.howard; no lane code).
Per nested instance (lane's NAMES.json maps v, Q, R and l<j>_v, l<j>_Q, l<j>_R to mover indices): for each level j, the SETS S(v_j),
S(g_Qj), S(R_j) (steps with a value change), flips(g_Qj); prints seteq_j := [S(R_j) == S(R_(j-1))] (as sets, not sizes) for j >= 2.
Per any instance: T, C (max c_y(v, I)), max gate flips, and for MWR-type rows the max-flip gate's lamch and ch_D.
Usage: gate_lev.py ENGINE CAP F.json [F.names.json] ...   (pairs: a .json followed by its .names.json when it has one)"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_replay import howard

def stats(G, eng, cap, names=None):
    E, lab, ties, states, movers, idx = howard(G, eng == "g3", cap)
    T = len(states) - 1; V = [s[2] for s in states]; ST = [s[1] for s in states]; n = E.n; rk = E.rk
    O = [(x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]; evs = frozenset(idx[("e", q)] for q in O)
    S = lambda v: {t for t in range(1, T + 1) if E.cmp(V[t][v], V[t - 1][v]) != 0}
    out = [f"T {T}"]
    # C
    C = 0
    for v in range(n):
        a = 0
        while a <= T:
            b = a
            while b < T and V[b + 1][v][0] == V[a][v][0]: b += 1
            cnt = {}
            for t in range(a + 1, b + 1):
                A0, A1 = frozenset(V[t - 1][v][1]) & evs, frozenset(V[t][v][1]) & evs
                if A0 != A1:
                    y = max(A0 ^ A1, key=lambda z: rk[z]); cnt[y] = cnt.get(y, 0) + 1
            C = max([C] + list(cnt.values())); a = b + 1
    best = (0, 0, 0)
    for q in O:
        g = idx[("g", q)]; fl = sum(ST[t][g] != ST[t - 1][g] for t in range(1, T + 1))
        e = idx[("e", q)]; D = E.succ[e][0]
        pe, pb = (idx[("pe", q)], idx[("pbeta", q)]) if eng == "g3" else (e, idx[("b", q)])
        lamch = sum(V[t][pe][0] != V[t - 1][pe][0] or V[t][pb][0] != V[t - 1][pb][0] for t in range(1, T + 1))
        best = max(best, (fl, -lamch, len(S(D))))
    out.append(f"C {C} maxflips {best[0]} lamch@max {-best[1]} chD@max {best[2]}")
    if names:
        prevR = None; j = 1
        while True:
            p = "" if j == 1 else f"l{j}_"
            if p + "Q" not in names: break
            sv, sr = S(idx[("x", names[p + "v"])]), S(idx[("x", names[p + "R"])])
            gq = idx[("g", (names[p + "Q"], 0))]; fq = sum(ST[t][gq] != ST[t - 1][gq] for t in range(1, T + 1))
            s = f"L{j} |v| {len(sv)} |R| {len(sr)} flQ {fq}"
            if prevR is not None: s += f" seteq {int(sr == prevR)}"
            out.append(s); prevR = sr; j += 1
    return " | ".join(out)

if __name__ == "__main__":
    eng, cap = sys.argv[1], int(sys.argv[2]); a = sys.argv[3:]; i = 0
    while i < len(a):
        f = a[i]; nm = None
        if i + 1 < len(a) and a[i + 1].endswith(".names.json"): nm = json.load(open(a[i + 1])); i += 1
        G = json.load(open(f)); G = G.get("genome", G)
        print(eng, os.path.basename(f), stats(G, eng, cap, nm), flush=True); i += 1
