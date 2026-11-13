"""Causal classification of every switch in a key run (own engine sim70): for a switch of x at step t (state S[t-1] -> S[t]):
 key-ready since tk (earliest step such that the target option is the key-least of x's two options under S[tau] for all tau in [tk, t]);
 value-ready since tv (earliest step such that Xi_{S[tau-1]}(target) > Xi_{S[tau-1]}(current) for all tau in [tv, t]).
 KL (key-last): tk == t; VL (value-last): tv == t (the Xi-order flipped at state t-1, by the switches of step t-1).
 For VL: the movers that switched at step t-1 and lie on the Xi-chain (at S[t-1]) of the target option."""
import sys, sim244 as sim70
G = sim70.load(sys.argv[1]); T, sw, S = sim70.run(G, trace=True); N = G["N"]; lev = G["lev"]; opts = G["opts"]; gate = G["gate"]
topo, om, lord = sim70.prep(G)
def vals(s):
    V = [0] * (N + 1)
    for x in topo: V[x] = om[x][s[x]] + V[opts[x][s[x]][1]]
    return V
def keys(s):
    key = [None] * N
    for x in lord:
        o = opts[x][s[x]]; key[x] = (key[o[0]] if o[0] >= 0 else ()) + (gate[x][s[x]],)
    return key
VS = [vals(s) for s in S]; KS = [keys(s) for s in S]
def kp(x, t):   # key-least option of x under S[t]
    ks = [((KS[t][o[0]] if o[0] >= 0 else ()) + (gate[x][k],)) for k, o in enumerate(opts[x])]
    return min(range(len(ks)), key=lambda k: ks[k])
def xb(x, t, k, c):  # Xi_{S[t]}(x,k) > Xi_{S[t]}(x,c)
    return om[x][k] + VS[t][opts[x][k][1]] > om[x][c] + VS[t][opts[x][c][1]]
def chain(u, t):
    out = []
    while u >= 0: out.append(u); u = opts[u][S[t][u]][1]
    return out
xs = [int(a) for a in sys.argv[2].split(",")]
moved = [set(x for x in range(N) if t > 0 and S[t][x] != S[t - 1][x]) for t in range(T + 1)]
stat = {x: dict(KL=0, VL=0, both=0, lagk=[], lagv=[], cause={}) for x in xs}
for t in range(1, T + 1):
    for x in xs:
        if S[t][x] == S[t - 1][x]: continue
        c, k = S[t - 1][x], S[t][x]
        tk = t
        while tk - 1 >= 1 and S[tk - 2][x] == c and kp(x, tk - 1) == k: tk -= 1
        tv = t
        while tv - 1 >= 1 and S[tv - 2][x] == c and xb(x, tv - 2, k, c): tv -= 1
        st = stat[x]; KL = tk == t; VL = tv == t
        st["KL"] += KL and not VL; st["VL"] += VL and not KL; st["both"] += KL and VL; st["lagk"].append(t - tk); st["lagv"].append(t - tv)
        if VL and t >= 2:
            ch = chain(opts[x][k][1], t - 1); cs = tuple(sorted(z for z in ch if z in moved[t - 1]))
            st["cause"][cs] = st["cause"].get(cs, 0) + 1
for x in xs:
    st = stat[x]
    print(f"x{x} L{lev[x]} sw {sw[x]}: KL-only {st['KL']} VL-only {st['VL']} both {st['both']} | VL causes (movers switching at t-1 on the target chain): " +
          ", ".join(f"{list(c)}x{n}" for c, n in sorted(st["cause"].items(), key=lambda q: -q[1])[:6]))
