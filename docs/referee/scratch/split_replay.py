"""REFEREE successor 30: P-N5-SPLIT replay on HOW3(G) (own engine: xicyc_replay.howard on own Γ3 builder, as chain_replay.py; own generator
end_replay.gen). Counters (must be 0): emon (a change whose top leaves), playfail (E changes but plays equal), kindfail (SPLIT (i)),
hwfail (SPLIT (ii)), gtfail (SPLIT (iii)), trfail (TRANSFER (iv)), a2fail (PAIR-SPLIT (a′)/(b′)), rh2fail (PAIR-SPLIT (c′), all same-pair
y-top couples t < t′), jbfail (y-tops of one pair not in one Λ-interval of b), spfail (SPLIT-COUNT, Dhi over b's whole Λ-interval J_b),
splfail (|SPL| > 3M), phafail (PAIR-HIGH (a)), phcfail (PAIR-HIGH (c)). Controls: ctrlU (rh2 with U_y := ∅), ctrlG (gate test negated).
Usage: split_replay.py FAM SEED COUNT | split_replay.py --files F.json ..."""
import sys, os, json, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_replay import howard
from end_replay import gen

def one(G, C):
    E, lab, ties, states, movers, idx = howard(G, True)
    n = E.n; N = G["N"]; O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]; M = len(O)
    evs = {idx[("e", q)] for q in O}; gates = {idx[("g", q)] for q in O}; mv = set(movers); rk = E.rk
    T = len(states) - 1; C["runs"] += 1; C["T"] = max(C["T"], T)
    Es = [[frozenset(val[v][1] & evs) for v in range(n)] for (_, _, val) in states]
    Ls = [[val[v][0] for v in range(n)] for (_, _, val) in states]
    def lexgt(A, B):            # A >lex B
        d = A ^ B
        return bool(d) and max(d, key=lambda z: rk[z]) in A
    def ivl(v, t):              # Λ-interval of v containing t
        a = t
        while a > 0 and Ls[a - 1][v] == Ls[t][v]: a -= 1
        b = t
        while b < T and Ls[b + 1][v] == Ls[t][v]: b += 1
        return a, b
    tops = collections.defaultdict(list)    # (v, I-start, y) -> [(t, u, b)]
    for t in range(1, T + 1):
        st0, st1 = states[t - 1][1], states[t][1]; v0, v1 = states[t - 1][2], states[t][2]
        for v in range(n):
            if Ls[t - 1][v] != Ls[t][v] or Es[t - 1][v] == Es[t][v]: continue
            d = Es[t - 1][v] ^ Es[t][v]; y = max(d, key=lambda z: rk[z])
            if y not in Es[t][v]: C["emon"] += 1
            x = v; seen = set()
            while st0[x] == st1[x] and x not in seen: seen.add(x); x = st0[x]
            if x in seen: C["playfail"] += 1; continue
            u = x; old, new = st0[u], st1[u]
            if u in mv: C["hwfail"] += not (E.cmp(v0[new], v0[old]) > 0)
            elif u in gates:
                ok = E.cmp(v0[old], v0[new]) < 0 and E.cmp(v1[new], v1[old]) < 0
                C["gtfail"] += not ok; C["ctrlG"] += ok
            else: C["kindfail"] += 1
            C["trfail"] += Ls[t - 1][u] != Ls[t][u] or (Es[t - 1][u] ^ Es[t][u]) != d
            tops[(v, ivl(v, t)[0], y)].append((t, u, new))
    M3 = 3 * M
    for (v, a, y), L in tops.items():
        Uy = {z for z in evs if rk[z] > rk[y]}; byp = collections.defaultdict(list)
        for (t, u, b) in L: byp[(u, b)].append(t)
        C["splfail"] += len(byp) > M3; C["maxspl"] = max(C["maxspl"], len(byp)); C["maxc"] = max(C["maxc"], len(L))
        tot = 0
        for (u, b), ts in byp.items():
            J = {ivl(b, t) for t in ts}; C["jbfail"] += len(J) > 1
            ja, jb = min(J); tot += len({Es[s][b] & Uy for s in range(ja, jb + 1)})
            for i in range(len(ts)):
                for j in range(i + 1, len(ts)):
                    t, t2 = ts[i], ts[j]; aa = states[t2 - 1][1][u]; V1 = states[t2 - 1][2]
                    C["couples"] += 1
                    C["a2fail"] += not (E.cmp(V1[aa], states[t][2][b]) > 0 and E.cmp(V1[b], states[t][2][b]) > 0)
                    C["rh2fail"] += not lexgt(Es[t2][b] & Uy, Es[t][b] & Uy); C["ctrlU"] += not lexgt(frozenset(), frozenset())
        C["spfail"] += len(L) > tot
        ia, ib = ivl(v, L[0][0])
        dhi = len({Es[s][v] & Uy for s in range(ia, ib + 1)}); C["phafail"] += len(L) > dhi
        cz = sum(1 for t in range(ia + 1, ib + 1) if Es[t - 1][v] != Es[t][v] and max(Es[t - 1][v] ^ Es[t][v], key=lambda z: rk[z]) in Uy)
        C["phcfail"] += dhi != 1 + cz

KEYS = ("emon", "playfail", "kindfail", "hwfail", "gtfail", "trfail", "a2fail", "rh2fail", "jbfail", "spfail", "splfail", "phafail",
        "phcfail", "ctrlU", "ctrlG", "couples", "runs", "T", "maxc", "maxspl")
def show(tag, C): print(tag, " ".join(f"{k} {C[k]}" for k in KEYS), flush=True)
if __name__ == "__main__":
    if sys.argv[1] == "--files":
        for f in sys.argv[2:]:
            C = collections.Counter(); one(json.load(open(f)), C); show(os.path.basename(f), C)
    else:
        fam, seed, cnt = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); C = collections.Counter()
        for _ in range(cnt): one(gen(rng, fam), C)
        show(f"{fam} seed {seed} x{cnt}", C)
