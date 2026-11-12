#!/usr/bin/env python3
"""REFEREE successor 32: pre-packet read of L-SI 51's Lemma RESTRICT-C (claude/l-si d8945c4a, docs/si/box101-lamgap.md Addendum D.2).
Own code only: Gamma3 builder and Howard run xicyc_replay (successor 26), VJ engine xicyc_vj, generator end_replay.gen (successor 29).
No lane code imported.

For a genome G: HOW3 run on Gamma3(G) (my tie rule: keep if best, else larger index). D(G): x -> W-target, x -> Xi-target (movers).
For an SCC C of D(G), R := Reach(C); f(C') := the first state from which no mover of C' switches again; t0(C) := max f(C') over the
SCCs C' != C reachable from C (0 if none) -- the SAFE reading of box 99's t0.  For a state a: G' := G restricted to R, renumbered in
increasing order, same (lev, gate, br, bp), targets renamed, start := sigma_a.  phi: Gamma3(G') -> Gamma3(G) by vertex keys.

Must-be-0 counters (unit in brackets):
 (i)   i_img   [pair (C,a)]  phi's image != V_R + {cX}, V_R := vertices reachable from R's movers in the full edge relation
       i_own   [vertex]      owner differs;      i_edge [vertex]  successor LIST differs under phi
       i_start [vertex]      G' start (standard state of G') != sigma_a transported (every Even vertex)
       i_rel   [pair (C,a)]  relevance order (prio, index) on the non-m-pad vertices not preserved by phi
       i_par   [vertex]      parity of the priority differs (all vertices)
 (ii)  ii_val  [(state, vertex)]  value of the transported positional pair (sigma_t, sbar_t) in G' != phi^-1 of the value in G
       ii_br   [(state, vertex)]  Odd's best-reply value computed in G' on its own != transported value
       ii_sbar [(state, Odd vertex)] G' best reply's choice != transported sbar_t (computed from a cold start AND from sbar's image)
       ii_rand [(random pair, vertex)] same as ii_val on random positional pairs of the FULL edge relation (every Even and Odd vertex random)
       cn_pad  [(random pair or state, vertex)] a pad, mover or gate is a cycle node or in a set Pi (CN2-3), in G or in G'
 (iii) iii_step [(step, mover of G')] the transported step t -> t+1 (t >= a) is not a legal Howard step of G' on G''s own values
       iii_stut [pair (C,a)] a step that changes nothing on R is followed by a later change on R, or G' is not terminal there
 (iv)  iv_brseg [pair (C,a)] BR-SEG form: more than N' consecutive steps (t >= a), each changing sigma on R, with Lambda and sbar
                constant on V_R over their states
Records (not must-0):
       lit     [pair (C,a), a = t0] LITERAL (iv): a maximal run of states >= a with sbar and Lambda constant on V_R has more than N' steps
       gtNC    [pair (C,a), a >= t0] a BR-SEG-form window longer than |C|
       tdiff   [pair (C,a)] G''s own run (my tie rule) differs from the transported run (states list)
       mpadchg [pair (C,a)] some m-pad priority differs between Gamma3(G') and Gamma3(G)|V_R
       maxwin, maxwin/N'
Controls (must fire): c_mpad [pair] relevance order INCLUDING m-pads broken;  c_open [pair] C not successor-closed: restricting to C
       alone with outside targets cut to -1 changes some value (ii_val-type);  c_iv [pair] BR-SEG form with bound N'//4 violated.
env COMPRESS=1: G' with br and gate compressed order-preservingly onto 0..M'-1 (a genome in P-N5-REALIZE's strict sense).
usage: restrictc_replay.py files MAXSCC G.json ... | gen FAMILY SEED COUNT MAXSCC"""
import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_replay import build, howard
from xicyc_vj import VJ
import end_replay

PADTAGS = ("pe", "pbeta", "pb", "m")
def is_low(key):  # pads, movers, gates: never a cycle node or in Pi (CN2-3)
    return key in ("pA", "s", "q", "r") or (isinstance(key, tuple) and key[0] in PADTAGS + ("x", "g"))

def dgraph(G):
    return [sorted({o[0] for o in G["opts"][x] if o[0] >= 0} | {o[1] for o in G["opts"][x] if o[1] >= 0}) for x in range(G["N"])]

def sccs(adj):
    n = len(adj); index = [None] * n; low = [0] * n; on = [False] * n; st = []; out = []; cnt = [0]
    sys.setrecursionlimit(100000)
    def dfs(v):
        index[v] = low[v] = cnt[0]; cnt[0] += 1; st.append(v); on[v] = True
        for w in adj[v]:
            if index[w] is None: dfs(w); low[v] = min(low[v], low[w])
            elif on[w]: low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            c = []
            while True:
                w = st.pop(); on[w] = False; c.append(w)
                if w == v: break
            out.append(sorted(c))
    for v in range(n):
        if index[v] is None: dfs(v)
    return out

def reach(adj, C):
    seen = set(C); todo = list(C)
    while todo:
        v = todo.pop()
        for w in adj[v]:
            if w not in seen: seen.add(w); todo.append(w)
    return sorted(seen)

def restrict(G, R, start, cut=False):
    """genome on the movers R (sorted), renumbered; cut=True: targets outside R become -1 (control only)."""
    ren = {x: i for i, x in enumerate(R)}; opts = []; br = []; bp = []
    for x in R:
        oo = []
        for (wt, xt, b) in G["opts"][x]:
            if cut:
                wt2 = ren.get(wt, -1) if wt >= 0 else -1; xt2 = ren.get(xt, -1) if xt >= 0 else -1
            else:
                wt2 = ren[wt] if wt >= 0 else -1; xt2 = ren[xt] if xt >= 0 else -1
            oo.append([wt2, xt2, len(br)]); br.append(G["br"][b]); bp.append(G["bp"][b])
        opts.append(oo)
    gate = [list(G["gate"][x]) for x in R]
    if os.environ.get("COMPRESS") == "1":   # W-2: P-N5-REALIZE's genome has br and gate as bijections onto 0..M-1
        rk = {v: i for i, v in enumerate(sorted(br))}; br = [rk[v] for v in br]
        gk = {v: i for i, v in enumerate(sorted(g for row in gate for g in row))}; gate = [[gk[g] for g in row] for row in gate]
        assert sorted(br) == list(range(len(br))) and sorted(g for row in gate for g in row) == list(range(len(br)))
    return {"N": len(R), "lev": [G["lev"][x] for x in R], "opts": opts, "gate": gate, "br": br, "bp": bp,
            "start": [start[x] for x in R]}

def keymap(R):
    def f(key):
        if isinstance(key, tuple) and key[0] == "x": return ("x", R[key[1]])
        if isinstance(key, tuple) and key[0] != "K": return (key[0], (R[key[1][0]], key[1][1]))
        return key
    return f

class Ctr(dict):
    def inc(self, k, d=1): self[k] = self.get(k, 0) + d

def one(name, G, maxscc, rng, c, verbose=True):
    E, lab, ties, states, movers, idx, fullsucc = howard3(G)
    T = len(states) - 1; N = G["N"]; n = E.n; inv = {v: k for k, v in idx.items()}
    adj = dgraph(G); comps = sccs(adj); compof = {}
    for i, C in enumerate(comps):
        for x in C: compof[x] = i
    # f(C'): first state from which no mover of C' switches again
    lastsw = [0] * N
    for t in range(T):
        for x in range(N):
            if states[t + 1][0][movers[x]] != states[t][0][movers[x]]: lastsw[x] = t + 1
    f = [max(lastsw[x] for x in C) for C in comps]
    def choice(t, x): return fullsucc[movers[x]].index(states[t][0][movers[x]])
    order = sorted(range(len(comps)), key=lambda i: -len(comps[i]))
    pick = order[:maxscc] if len(order) <= 2 * maxscc else order[:maxscc] + rng.sample(order[maxscc:], maxscc)
    best = (0, 0, 0)
    for ci in pick:
        C = comps[ci]; R = reach(adj, C); Cset = set(C)
        t0 = max([f[compof[y]] for y in R if y not in Cset] + [0])
        cand = sorted({0, t0, rng.randint(t0, T), rng.randint(0, T)})
        for a in cand:
            c.inc("pairs"); start = [choice(a, x) for x in range(N)]
            G2 = restrict(G, R, start); p2, o2, fs2, sig2, mov2, idx2, full2 = build(G2, True); E2 = VJ(p2, o2, fs2); n2 = E2.n
            km = keymap(R); phi = [idx[km(inv2k)] for inv2k in sorted(idx2, key=lambda k: idx2[k])]; back = {w: v for v, w in enumerate(phi)}
            key2 = sorted(idx2, key=lambda k: idx2[k])
            # (i)
            VR = set(movers[x] for x in R); todo = list(VR)
            while todo:
                v = todo.pop()
                for w in fullsucc[v]:
                    if w not in VR: VR.add(w); todo.append(w)
            if set(phi) != VR | {idx["cX"]} or len(set(phi)) != n2: c.inc("i_img")
            sa = states[a][0]
            for v in range(n2):
                if o2[v] != E.owner[phi[v]]: c.inc("i_own")
                if [phi[w] for w in full2[v]] != list(fullsucc[phi[v]]): c.inc("i_edge")
                if o2[v] == 0 and phi[sig2[v]] != sa[phi[v]]: c.inc("i_start")
                if p2[v] % 2 != E.prio[phi[v]] % 2: c.inc("i_par")
            nonm = [v for v in range(n2) if not (isinstance(key2[v], tuple) and key2[v][0] == "m")]
            seq = sorted(nonm, key=lambda v: E2.rk[v])
            if any(E.rk[phi[u]] >= E.rk[phi[v]] for u, v in zip(seq, seq[1:])): c.inc("i_rel")
            seqall = sorted(range(n2), key=lambda v: E2.rk[v])
            if any(E.rk[phi[u]] >= E.rk[phi[v]] for u, v in zip(seqall, seqall[1:])): c.inc("c_mpad")
            if any(p2[v] != E.prio[phi[v]] for v in range(n2) if isinstance(key2[v], tuple) and key2[v][0] == "m"): c.inc("mpadchg")
            def tr(valG):  # value in G of phi(v) -> value in G' terms
                return (back[valG[0]], frozenset(back[u] for u in valG[1]), valG[2])
            # (ii) on the run's states t >= a, (iii) steps
            prev2 = None; stut = None; stutbad = False; runlen = 0; maxwin = 0; maxwin4 = 0; myrun = None
            trans = []
            for t in range(a, T + 1):
                s, st, val = states[t]
                st2 = [back[st[phi[v]]] for v in range(n2)]
                v2 = E2.values(st2)
                for v in range(n2):
                    if v2[v] != tr(val[phi[v]]): c.inc("ii_val")
                    if is_low(key2[v]) and (v2[v][0] == v or any(is_low(key2[u]) for u in v2[v][1])): c.inc("cn_pad")
                sg2 = [st2[v] if o2[v] == 0 else None for v in range(n2)]
                b1, bv1 = E2.best_reply(sg2); b2, bv2 = E2.best_reply(sg2, st2)
                for v in range(n2):
                    if E2.cmp(bv1[v], v2[v]) != 0 or E2.cmp(bv2[v], v2[v]) != 0 or bv1[v] != v2[v]: c.inc("ii_br")
                    if o2[v] == 1 and (b1[v] != st2[v] or b2[v] != st2[v]): c.inc("ii_sbar")
                trans.append((st2, v2))
            for j in range(len(trans) - 1):
                (stA, vA), (stB, vB) = trans[j], trans[j + 1]; changed = False
                for x in mov2:
                    cur, new = stA[x], stB[x]; cand2 = fs2[x]
                    bestv = cur
                    for w in cand2:
                        if E2.cmp(vA[w], vA[bestv]) > 0: bestv = w
                    B = [w for w in cand2 if E2.cmp(vA[w], vA[bestv]) == 0]
                    ok = (new == cur) if cur in B else (new in B)
                    if not ok: c.inc("iii_step")
                    changed |= new != cur
                if not changed:
                    if stut is None:
                        stut = j
                        # terminal in G': no mover has a strictly better successor
                        if any(E2.cmp(vA[w], vA[stA[x]]) > 0 for x in mov2 for w in fs2[x]): stutbad = True
                elif stut is not None: stutbad = True
                # (iv) BR-SEG form: consecutive sigma-changing steps with Lambda, sbar constant on all of G' over their states
                same = all(vA[v][0] == vB[v][0] for v in range(n2)) and all(stA[v] == stB[v] for v in range(n2) if o2[v] == 1)
                if changed and same: runlen += 1
                else: runlen = 0
                maxwin = max(maxwin, runlen)
            if stutbad: c.inc("iii_stut")
            N2 = len(R)
            if maxwin > N2: c.inc("iv_brseg")
            if maxwin > N2 // 4: c.inc("c_iv")
            if a >= t0 and maxwin > len(C): c.inc("gtNC")
            if best[1] == 0 or maxwin * best[1] > best[0] * N2: best = (maxwin, N2, len(C))
            c["maxwin"] = max(c.get("maxwin", 0), maxwin)
            # literal (iv) at a = t0: maximal runs of states with sbar and Lambda constant on V_R
            if a == t0:
                cur = 0; lit = 0
                for j in range(len(trans) - 1):
                    (stA, vA), (stB, vB) = trans[j], trans[j + 1]
                    same = all(vA[v][0] == vB[v][0] for v in range(n2)) and all(stA[v] == stB[v] for v in range(n2) if o2[v] == 1)
                    cur = cur + 1 if same else 0; lit = max(lit, cur)
                if lit > N2:
                    c.inc("lit")
                    if "lit_ex" not in c: c["lit_ex"] = "%s C=%s |R|=%d a=t0=%d T3=%d window %d steps" % (name, C[:6], N2, a, T, lit)
            # G''s own run with my tie rule vs the transported run
            E3, lab3, ties3, states3, mov3, idx3, _ = howard3(G2)
            mine = [tuple(s3[0][x] for x in mov3) for s3 in states3]
            theirs = [tuple(stA[x] for x in mov2) for (stA, _) in trans]
            k = stut if stut is not None else len(theirs) - 1
            if mine != theirs[:k + 1]: c.inc("tdiff")
            # random positional pairs of the full edge relation
            for _ in range(3):
                c.inc("randpairs"); stR = [rng.choice(fullsucc[v]) for v in range(n)]
                valR = E.values(stR); st2 = [back[stR[phi[v]]] for v in range(n2)]; v2 = E2.values(st2)
                for v in range(n2):
                    if v2[v] != tr(valR[phi[v]]): c.inc("ii_rand")
                    if is_low(key2[v]) and (v2[v][0] == v or any(is_low(key2[u]) for u in v2[v][1])): c.inc("cn_pad")
                for v in range(n):
                    if is_low(inv[v]) and (valR[v][0] == v or any(is_low(inv[u]) for u in valR[v][1])): c.inc("cn_pad")
            # control: C alone, cut (only meaningful when C is not successor-closed)
            if len(R) > len(C):
                c.inc("openpairs"); G4 = restrict(G, C, start, cut=True); p4, o4, fs4, sig4, mov4, idx4, full4 = build(G4, True); E4 = VJ(p4, o4, fs4)
                km4 = keymap(C); key4 = sorted(idx4, key=lambda k: idx4[k]); phi4 = [idx[km4(k)] for k in key4]; back4 = {w: v for v, w in enumerate(phi4)}
                bad = False
                for t in range(a, T + 1):
                    s, st, val = states[t]
                    sg4 = [None] * E4.n
                    for v in range(E4.n):
                        if o4[v] == 0:
                            w = st[phi4[v]]; sg4[v] = back4[w] if w in back4 else fs4[v][0]
                    b4, bv4 = E4.best_reply(sg4)
                    for x in mov4:
                        vg = val[phi4[x]]
                        if vg[0] not in back4 or any(u not in back4 for u in vg[1]) or bv4[x] != (back4[vg[0]], frozenset(back4[u] for u in vg[1]), vg[2]): bad = True
                    if bad: break
                if bad: c.inc("c_open")
    if verbose:
        print("%-16s N %3d M %3d n3 %4d T3 %3d SCCs %3d ties %d  best window %d / N' %d (|C| %d)" % (name, N, sum(len(o) for o in G["opts"]), n, T, len(comps), ties, best[0], best[1], best[2]))

def howard3(G):
    E, lab, ties, states, movers, idx = howard(G, True, cap=20000)
    assert len(lab) < 20000
    fullsucc = build(G, True)[6]
    return E, lab, ties, states, movers, idx, fullsucc

MUST0 = ["i_img", "i_own", "i_edge", "i_start", "i_rel", "i_par", "ii_val", "ii_br", "ii_sbar", "ii_rand", "cn_pad", "iii_step", "iii_stut", "iv_brseg"]
REC = ["pairs", "randpairs", "openpairs", "lit", "gtNC", "tdiff", "mpadchg", "maxwin", "c_mpad", "c_open", "c_iv"]

def main():
    mode = sys.argv[1]; c = Ctr(); rng = random.Random(3201)
    if mode == "files":
        maxscc = int(sys.argv[2])
        for fn in sys.argv[3:]:
            one(os.path.basename(fn)[:-5], json.load(open(fn)), maxscc, rng, c)
    else:
        fam, seed, count, maxscc = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]); g = random.Random(seed)
        for i in range(count):
            one("%s_%d_%d" % (fam, seed, i), end_replay.gen(g, fam), maxscc, rng, c, verbose=False)
        print("family %s seed %d count %d" % (fam, seed, count))
    print("MUST-0:  " + "  ".join("%s %d" % (k, c.get(k, 0)) for k in MUST0))
    print("RECORDS: " + "  ".join("%s %d" % (k, c.get(k, 0)) for k in REC))
    if "lit_ex" in c: print("LITERAL (iv) example: " + c["lit_ex"])

if __name__ == "__main__":
    main()
