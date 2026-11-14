#!/usr/bin/env python3
"""REFEREE successor 32: pre-packet read of L-NEW 72's box 208 (claude/l-new 8db300fe, docs/new/N5-LEVEL-box208.md): own replay.
Own code only: Gamma(G) builder and IDEAL-CYC Howard run xicyc_replay.howard (successor 26; tie rule: keep if best, else larger index),
VJ engine xicyc_vj, generator end_replay.gen. No lane code imported; every counter below is written from the document's STATEMENTS.

class_t(v) := (Lambda_t(v), E_t(v)), E_t(v) the e-vertices of Pi_t(v); order: reward(Lambda), then lex by the most relevant differing e.

Must-be-0 counters (unit):
 k1    (step, vertex)        class falls                                                          (K1)
 k2    (pair of values)      Omega <| or = Omega' but class > class', two non-core vertices at one state, or one at t and t+1  (K2)
 k3a   (state, vertex)       Lambda(v) != Lambda(s(v));   k3c  class(v) != class(s(v)), v not an e-vertex
 k3d   (state, e-vertex with mover successor w)  class(e) != (Lambda(w), {e} + E(w)) or e in E(w)   (also gives (b))
 k3e   (state, vertex)       class of K0..K3, cW, cX or an e -> cW differs from its class at state 0
 k4    (state, gate)         class(g) != min(class(e_g), class(beta_g))
 k5    (step, mover, gate)   class_(t+1)(x) < class_t(y)
 LEVEL, reference b (b = T and two random states), for t < b with LAG_t nonempty:
 l1    (step)                LAG grows; Phi falls; Phi equal at a non-stall; Phi or FRONT changes at a stall
 l2    (state, vertex)       FRONT holds a vertex that is not a mover, a gate or a beta with a mover successor
 l3    (state)               neither (alpha) nor (beta);  l3v (state)  (alpha) with m != class_b(sigma_t(z)) for some such z, or
                             (beta) with m != (c, {}) or c not a beta
 l4    (stall, FRONT vertex) the map s leaves FRONT, or a gate's sbar_t is not its beta-face
 l5    (reference)           more than 2M(N + 2M) values of Phi; or m outside {class_b(gate)} + {(c, {})}
 c4    (reference)           after LAG is empty: a class changes, or more than N steps to b (reference T only for the N bound... see code)
 WIN, S a set meeting every Xi-cycle, every maximal interval [a, b] of constant classes on S, reference b:
 w_stall (step) a stall before LAG is empty;  w_beta (state) a (beta)-cycle;  w_len (interval) b' - a > M(N + 2M) or b - b' > N
 w_quiet (interval) a class changes after b'
 rh    (step, k = 1)         a stall (reference T) at which the class of a feedback vertex changes         (R-HEIGHT)
 PLATEAU, reference T (and the two random references), every maximal interval [u, v], u < v, of constant Phi:
 p1    (state, vertex)       {class_s <= m} != Y, or a vertex of Y changes class
 p2    (state, vertex of Y)  its successor on the play is outside Y
 p3    (state, mover of Y, gate)  class_s(gate) > class_s(mover), or the gate is outside Y
 p4    (state, Odd vertex of Y)   sbar_s differs from sbar_u, or leaves Y
 p5v   (state, vertex of Y)  its value in the one-player game H (own VJ engine on H) differs from Omega_s
 p5h   (step, mover of Y)    the step s -> s+1 (u <= s <= v) is not a legal Howard step of H on H's own values
 p6    (step)                a step s -> s+1, u <= s <= v, switches no mover of Y
 p7    (plateau)             v - u > the number of Even vertices of Y (the document's n_E(H));  p7s: > the number of movers of Y
 tb    (genome)              T > P(N + 2M + 6) + N
Controls (must fire): c_k4 (max in place of min), c_k5 (class_t(x) < class_t(y): no shift), ch1..ch5 (FRONT := highest lagging class:
 the l-counters under that control), c_S (WIN with S := {} on a genome whose Xi-graph has a cycle: stalls), c_Y (PLATEAU with Y := FRONT: p2).
usage: box208_replay.py files G.json ... | gen FAMILY SEED COUNT | mut SEED COUNT MAXMUT G.json ..."""
import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_replay import build, howard
from xicyc_vj import VJ
import end_replay

class Ctr(dict):
    def inc(self, k, d=1): self[k] = self.get(k, 0) + d
    def mx(self, k, v): self[k] = max(self.get(k, 0), v)

def xi_graph(G):
    return [sorted({o[1] for o in G["opts"][x] if o[1] >= 0}) for x in range(G["N"])]

def acyclic_without(adj, removed):
    n = len(adj); col = [0] * n
    for r in removed: col[r] = 2
    for root in range(n):
        if col[root]: continue
        stack = [(root, 0)]; col[root] = 1
        while stack:
            v, i = stack[-1]
            if i < len(adj[v]):
                stack[-1] = (v, i + 1); w = adj[v][i]
                if col[w] == 1: return False
                if col[w] == 0: col[w] = 1; stack.append((w, 0))
            else: col[v] = 2; stack.pop()
    return True

def fvs(adj):
    """(k or None, list of feedback sets to use): all single feedback vertices if k = 1; one minimum pair if found (N <= 80); else greedy."""
    n = len(adj)
    if acyclic_without(adj, []): return 0, [[]]
    singles = [[x] for x in range(n) if acyclic_without(adj, [x])]
    if singles: return 1, singles
    if n <= 80:
        for x in range(n):
            for y in range(x + 1, n):
                if acyclic_without(adj, [x, y]): return 2, [[x, y]]
    S = []
    while not acyclic_without(adj, S):
        deg = [0 if x in S else len(adj[x]) + sum(x in adj[y] for y in range(n) if y not in S) for x in range(n)]
        S.append(max(range(n), key=lambda x: deg[x]))
    return None, [S]

def one(name, G, c, rng, verbose=True):
    E, lab, ties, states, movers, idx = howard(G, False, cap=20000); assert len(lab) < 20000
    T = len(states) - 1; n = E.n; N = G["N"]; M = sum(len(o) for o in G["opts"]); inv = {v: k for k, v in idx.items()}
    kind = [None] * n
    for k, v in idx.items(): kind[v] = k[0] if isinstance(k, tuple) else k
    evs = [v for v in range(n) if kind[v] == "e"]; isE = [kind[v] == "e" for v in range(n)]
    gates = [v for v in range(n) if kind[v] == "g"]; mset = set(movers)
    core = {idx[("K", i)] for i in range(4)}; cW, cX = idx["cW"], idx["cX"]
    face = {}  # gate -> (e_g, beta_g)
    for g in gates:
        q = inv[g][1]; face[g] = (idx[("e", q)], idx[("b", q)])
    e_to_cW = [e for e in evs if E.succ[e] == [cW]]
    const = sorted(core) + [cW, cX] + e_to_cW
    def cls(val_v):
        return (E.reward(val_v[0]), tuple(sorted((E.rk[u] for u in val_v[1] if isE[u]), reverse=True)))
    CL = [[cls(val[v]) for v in range(n)] for (_, _, val) in states]   # CL[t][v]
    ST = [st for (_, st, _) in states]; VAL = [val for (_, _, val) in states]
    c.inc("genomes"); c.inc("states", T + 1); c.mx("maxT", T)
    P = 2 * M * (N + 2 * M)
    if T > P * (N + 2 * M + 6) + N: c.inc("tb")
    # ---------------- class facts
    for t in range(T + 1):
        st, val, cl = ST[t], VAL[t], CL[t]
        for v in range(n):
            w = st[v]
            if val[v][0] != val[w][0]: c.inc("k3a")
            if not isE[v] and cl[v] != cl[w]: c.inc("k3c")
        for e in evs:
            w = E.succ[e][0]
            if w in mset:
                want = (cl[w][0], tuple(sorted(cl[w][1] + (E.rk[e],), reverse=True)))
                if cl[e] != want or E.rk[e] in cl[w][1]: c.inc("k3d")
        for v in const:
            if cl[v] != CL[0][v]: c.inc("k3e")
        for g in gates:
            a, b = face[g]
            if cl[g] != min(cl[a], cl[b]): c.inc("k4")
            if cl[g] != max(cl[a], cl[b]): c.inc("c_k4")
        # K2 on pairs of non-core vertices at this state
        nc = [v for v in range(n) if v not in core]
        pairs = [(v, w) for v in nc for w in nc] if len(nc) <= 60 else [(rng.choice(nc), rng.choice(nc)) for _ in range(1500)]
        for (v, w) in pairs:
            if E.cmp(val[v], val[w]) <= 0 and cl[v] > cl[w]: c.inc("k2")
        if t < T:
            nval, ncl = VAL[t + 1], CL[t + 1]
            for v in range(n):
                if ncl[v] < cl[v]: c.inc("k1")
                if v not in core and E.cmp(val[v], nval[v]) <= 0 and cl[v] > ncl[v]: c.inc("k2")
                if E.cmp(val[v], nval[v]) > 0: c.inc("k1")           # F1 itself
            for x in movers:
                for y in E.succ[x]:
                    if ncl[x] < cl[y]: c.inc("k5")
                    if cl[x] < cl[y]: c.inc("c_k5")
    # ---------------- cycles of plays per state
    def cycles(st):
        seen = [0] * n; out = []
        for v0 in range(n):
            if seen[v0]: continue
            path = []; v = v0
            while not seen[v]:
                seen[v] = 1; path.append(v); v = st[v]
            if v in path: out.append(path[path.index(v):])
        return out
    CYC = [cycles(ST[t]) for t in range(T + 1)]
    # ---------------- LEVEL machinery for an interval [a, b] with reference b
    def level(a, b, tag, plateau_checks, ctrl_hi=False):
        """returns (bprime, list of (t, is_stall), plateaus [(u, v, m, J)], nPhi). Counts l1..l5 under prefix tag ('l' or 'w')."""
        clb = CL[b]; gate_cls = {clb[g] for g in gates}; phis = []; stalls = []; info = {}
        tag = "ch" if ctrl_hi else tag                              # control counters go to ch1..ch5, never to l* / w*
        prevLAG = None; prevPhi = None; prevFRONT = None; prevStall = None; bprime = None
        for t in range(a, b + 1):
            cl = CL[t]; LAG = [v for v in range(n) if cl[v] != clb[v]]
            if prevLAG is not None and not set(LAG) <= prevLAG: c.inc(tag + "1")
            if not LAG:
                if prevLAG and prevStall: c.inc(tag + "1")           # a stall keeps LAG nonempty
                bprime = t; break
            m = (max if ctrl_hi else min)(cl[v] for v in LAG); FRONT = [v for v in LAG if cl[v] == m]; Fs = set(FRONT); Ls = set(LAG)
            Phi = (m, -len(FRONT))
            if prevPhi is not None:
                if prevStall and (Phi != prevPhi or Fs != prevFRONT): c.inc(tag + "1")
                if not prevStall and not Phi > prevPhi: c.inc(tag + "1")
            # (L2)
            for v in FRONT:
                if not (kind[v] in ("x", "g") or (kind[v] == "b" and E.succ[v][0] in mset)): c.inc(tag + "2")
            # (L3)
            st = ST[t]; alpha = [z for z in FRONT if kind[z] == "x" and st[z] not in Ls]
            beta = [cy for cy in CYC[t] if all(kind[v] in ("x", "g", "b") for v in cy) and all(v in Fs for v in cy)]
            if not alpha and not beta: c.inc(tag + "3")
            if tag == "l":                                            # records: how often each case of (L3) occurs
                if alpha: c.inc("n_alpha")
                if beta: c.inc("n_beta")
                if beta and not alpha: c.inc("n_beta_only")
            bad = any(m != clb[st[z]] for z in alpha)
            for cy in beta:
                cnode = VAL[t][cy[0]][0]
                if m != (E.reward(cnode), ()) or kind[cnode] != "b": bad = True
            if bad: c.inc(tag + "3v")
            if m not in gate_cls and not (m[1] == () and beta): c.inc(tag + "5")
            if tag == "w" and beta: c.inc("w_beta")
            phis.append(Phi)
            # stall?
            stall = None
            if t < b:
                ncl = CL[t + 1]; stall = all(ncl[v] == cl[v] for v in FRONT)
                if stall:
                    stb = ST[b]
                    for v in FRONT:                                    # (L4): the map s
                        if kind[v] == "x": w = stb[v]; ok = w in Fs
                        elif kind[v] == "g": w = st[v]; ok = w in Fs and w == face[v][1]
                        elif kind[v] == "b": w = E.succ[v][0]; ok = w in Fs
                        else: ok = False
                        if not ok: c.inc(tag + "4")
                    if any(ncl[v] != cl[v] for v in range(n)): info["stallloud"] = info.get("stallloud", 0) + 1
                stalls.append((t, stall, m, Fs))
            prevLAG, prevPhi, prevFRONT, prevStall = Ls, Phi, Fs, stall
        if bprime is None: bprime = b + 1   # cannot happen: LAG_b is empty
        if len(set(phis)) > 2 * M * (N + 2 * M): c.inc(tag + "5")
        # plateaus: maximal runs of stall steps
        plats = []; i = 0
        while i < len(stalls):
            if stalls[i][1]:
                j = i
                while j + 1 < len(stalls) and stalls[j + 1][1]: j += 1
                plats.append((stalls[i][0], stalls[j][0] + 1, stalls[i][2], stalls[i][3])); i = j + 1
            else: i += 1
        return bprime, stalls, plats, len(set(phis)), info
    def after(bprime, b, tag):
        ok = all(CL[t] == CL[b] for t in range(bprime, b + 1))
        return ok
    # ---------------- PLATEAU checks
    def plateau(u, v, m, J, ctrl=False):
        Y = [x for x in range(n) if CL[u][x] <= m] if not ctrl else sorted(J)
        Ys = set(Y)
        for s in range(u, v + 1):
            cl = CL[s]; st = ST[s]
            if not ctrl:
                for x in range(n):
                    if (cl[x] <= m) != (x in Ys) or (x in Ys and cl[x] != CL[u][x]): c.inc("p1")
            for x in Y:
                if st[x] not in Ys: c.inc("p2" if not ctrl else "c_Y")
            if ctrl: continue
            for x in Y:
                if kind[x] == "x":
                    for y in E.succ[x]:
                        if cl[y] > cl[x] or y not in Ys: c.inc("p3")
                if E.owner[x] == 1 and (st[x] != ST[u][x] or st[x] not in Ys): c.inc("p4")
        if ctrl: return
        # (P5): the one-player game H on Y
        loc = {x: i for i, x in enumerate(Y)}
        try:
            hsucc = [[loc[y] for y in E.succ[x]] if kind[x] == "x" else [loc[ST[u][x]]] for x in Y]
        except KeyError:
            c.inc("p5v"); return
        H = VJ([E.prio[x] for x in Y], [0 if kind[x] == "x" else E.owner[x] for x in Y], hsucc)
        hv = []
        for s in range(u, min(v + 1, T) + 1):
            hst = [loc.get(ST[s][x], None) if kind[x] == "x" else hsucc[i][0] for i, x in enumerate(Y)]
            if any(w is None for w in hst): c.inc("p5v"); return
            val = H.values(hst); hv.append((hst, val))
            if s <= v:
                for i, x in enumerate(Y):
                    g = VAL[s][x]
                    if g[0] not in loc or any(w not in loc for w in g[1]) or val[i] != (loc[g[0]], frozenset(loc[w] for w in g[1]), g[2]): c.inc("p5v")
        for j in range(len(hv) - 1):                                 # steps u+j -> u+j+1, u+j <= v
            (stA, vA), (stB, vB) = hv[j], hv[j + 1]; moved = False
            for i, x in enumerate(Y):
                if kind[x] != "x": continue
                cur, new = stA[i], stB[i]; best = cur
                for w in hsucc[i]:
                    if H.cmp(vA[w], vA[best]) > 0: best = w
                B = [w for w in hsucc[i] if H.cmp(vA[w], vA[best]) == 0]
                if not ((new == cur) if cur in B else (new in B)): c.inc("p5h")
                moved |= new != cur
            if not moved: c.inc("p6")
        nm = sum(1 for x in Y if kind[x] == "x"); ne = sum(1 for x in Y if E.owner[x] == 0)
        if v - u > ne: c.inc("p7")                                    # the document's bound n_E(H)
        if v - u > nm: c.inc("p7s")                                   # REFEREE's sharper form: the movers of Y
        c.inc("plateaus"); c.mx("maxplat", v - u); c.mx("maxplat_pct_movers", (100 * (v - u)) // max(nm, 1))
    # ---------------- reference T and two random references
    refs = [T] + ([rng.randint(1, T), rng.randint(1, T)] if T >= 2 else [])
    for ri, b in enumerate(refs):
        bp, stalls, plats, nphi, info = level(0, b, "l", True)
        if not after(bp, b, "l"): c.inc("c4")
        if b - bp > N: c.inc("c4")
        if ri == 0:
            c.mx("maxPhi", nphi); c.inc("stalls", sum(1 for s in stalls if s[1])); c.inc("stallloud", info.get("stallloud", 0))
            nonstall = sum(1 for s in stalls if s[0] < bp and not s[1])
            if nonstall != nphi: c.inc("l1")                        # (C2): exactly q non-stall steps before b'
        for (u, v, m, J) in plats:
            plateau(u, v, m, J)
            if ri == 0: plateau(u, v, m, J, ctrl=True)
        if ri == 0 and T >= 1: level(0, b, "l", False, ctrl_hi=True)
    # ---------------- WIN and R-HEIGHT
    adj = xi_graph(G); k, sets = fvs(adj)
    c.inc("k=%s" % ("0" if k == 0 else "1" if k == 1 else "2" if k == 2 else ">2"))
    def win(S, tagstall="w_stall"):
        Sv = [movers[x] for x in S]; a = 0
        while a <= T:
            b = a
            while b < T and all(CL[b + 1][x] == CL[a][x] for x in Sv): b += 1
            if tagstall == "w_stall":
                bp, stalls, plats, nphi, info = level(a, b, "w", False); c.inc("intervals")
                if any(s[1] for s in stalls if s[0] < bp): c.inc("w_stall", sum(1 for s in stalls if s[1] and s[0] < bp))
                if bp - a > M * (N + 2 * M) or b - bp > N: c.inc("w_len")
                if not after(bp, b, "w"): c.inc("w_quiet")
                c.mx("maxwinlen", b - a)
            else:                                                     # control: count stalls only, no other counter
                clb = CL[b]
                for t in range(a, b):
                    cl = CL[t]; LAG = [v for v in range(n) if cl[v] != clb[v]]
                    if not LAG: break
                    m = min(cl[v] for v in LAG)
                    if all(CL[t + 1][v] == cl[v] for v in LAG if cl[v] == m): c.inc(tagstall)
            a = b + 1
    for S in sets[:6] if k == 1 else sets: win(S)
    if k != 0: win([], tagstall="c_S")
    if k == 1:
        bp, stalls, plats, nphi, info = level(0, T, "l", False)
        for (t, stall, m, Fs) in stalls:
            if stall:
                for S in sets:
                    R = movers[S[0]]
                    if CL[t + 1][R] != CL[t][R]: c.inc("rh")
    if verbose:
        print("%-22s N %3d M %3d n %4d T %3d k %s ties %d" % (name, N, M, n, T, k if k is not None else ">2", ties))

MUST0 = ["k1", "k2", "k3a", "k3c", "k3d", "k3e", "k4", "k5", "l1", "l2", "l3", "l3v", "l4", "l5", "c4", "w1", "w2", "w3", "w3v", "w4", "w5",
         "w_stall", "w_beta", "w_len", "w_quiet", "rh", "p1", "p2", "p3", "p4", "p5v", "p5h", "p6", "p7", "p7s", "tb"]
REC = ["genomes", "states", "maxT", "k=0", "k=1", "k=2", "k=>2", "maxPhi", "stalls", "stallloud", "plateaus", "maxplat", "maxplat_pct_movers",
       "intervals", "maxwinlen", "n_alpha", "n_beta", "n_beta_only", "c_k4", "c_k5", "ch1", "ch2", "ch3", "ch3v", "ch4", "ch5", "c_S", "c_Y"]

def mutate(G, rng, nm):
    G = json.loads(json.dumps(G)); N = G["N"]
    O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]; M = len(O)
    for _ in range(nm):
        r = rng.randrange(5); x, k = rng.choice(O)
        if r == 0: G["opts"][x][k][1] = rng.choice(list(range(N)) + [-1])                       # retarget Xi
        elif r == 1:
            i, j = rng.randrange(M), rng.randrange(M); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
        elif r == 2: i = rng.randrange(M); G["bp"][i] ^= 1
        elif r == 3: G["start"][x] = rng.randrange(len(G["opts"][x]))
        elif G["lev"][x] > 0:
            G["opts"][x][k][0] = rng.choice([y for y in range(N) if G["lev"][y] == G["lev"][x] - 1])   # retarget W one level down
    return G

def own_gen(rng, fam):
    """tiny: 1-2 levels, 1-2 movers per level, 1-3 options; noX: every Xi-target a mover (no escape to u: every play cycles through
    beta-vertices); big: 4-10 levels, 2-4 movers per level, 2-3 options, Xi-targets mostly upward or level (many Xi-cycles)."""
    if fam == "tiny": d, w, omax = rng.randint(1, 2), rng.randint(1, 2), 3
    elif fam == "big": d, w, omax = rng.randint(4, 10), rng.randint(2, 4), 3
    else: d, w, omax = rng.randint(1, 5), rng.randint(1, 3), 3
    lev = []
    for l in range(d): lev += [l] * rng.randint(1, w)
    N = len(lev); opts = []; b = 0
    for x in range(N):
        oo = []
        for _ in range(rng.randint(2 if fam == "big" else 1, omax)):
            wt = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1
            if fam == "noX": xt = rng.randrange(N)
            elif fam == "big":
                up = [y for y in range(N) if lev[y] >= lev[x]]
                xt = rng.choice(up) if rng.random() < 0.7 else rng.choice(list(range(N)) + [-1])
            else: xt = rng.choice(list(range(N)) + [-1])
            oo.append([wt, xt, b]); b += 1
        opts.append(oo)
    M = b; perm = list(range(M)); rng.shuffle(perm); gate = []; i = 0
    for x in range(N):
        gate.append([perm[i + k] for k in range(len(opts[x]))]); i += len(opts[x])
    br = list(range(M)); rng.shuffle(br)
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [rng.randrange(2) for _ in range(M)],
            "start": [rng.randrange(len(o)) for o in opts]}

def main():
    mode = sys.argv[1]; c = Ctr(); rng = random.Random(3208)
    if mode == "files":
        for fn in sys.argv[2:]: one(os.path.basename(fn)[:-5], json.load(open(fn)), c, rng)
    elif mode == "gen":
        fam, seed, count = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]); g = random.Random(seed)
        for i in range(count): one("%s_%d" % (fam, i), (own_gen(g, fam) if fam in ("tiny", "noX", "big") else end_replay.gen(g, fam)), c, rng, verbose=False)
        print("family %s seed %d count %d" % (fam, seed, count))
    else:
        seed, count, maxmut = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); g = random.Random(seed)
        for fn in sys.argv[5:]:
            G0 = json.load(open(fn))
            for i in range(count): one("mut", mutate(G0, g, g.randint(1, maxmut)), c, rng, verbose=False)
        print("mutants: seed %d, %d per base, 1..%d mutations, bases %s" % (seed, count, maxmut, " ".join(os.path.basename(f)[:-5] for f in sys.argv[5:])))
    print("MUST-0:  " + "  ".join("%s %d" % (k, c.get(k, 0)) for k in MUST0))
    print("RECORDS: " + "  ".join("%s %d" % (k, c.get(k, 0)) for k in REC))

if __name__ == "__main__":
    main()
