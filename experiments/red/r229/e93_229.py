#!/usr/bin/env python3
"""L-RED 63 R229 item 4: independent census for L-SI 49 BOX 93 (claude/l-si f723957b: Lemma NP-SHAPE, Corollary E-FACE-PAYS, Lemma
WAIT-QUIET, the per-gate bound) on R221 own.py (IDEAL-CYC Howard from the genome's start, pad-free Γ; cap 3000). No L-SI code.
Unit: gate g = (x, k): Odd vertex g_q, faces p_e = e_q, p_b = b_q; D = e_q's successor (W-target mover, or cW); step t of the run.
  NP_t := e_q ∈ E_t(p_b); UP_t := e_q ∈ E_t(p_e) (e_q above Λ(p_e)); play(t, v) = the vertex sequence of v's play (simple path + cycle).
  Flip at t = change of Odd's choice at g (ties included; NP states never tie). RELOCK = p_e -> p_b, UNLOCK = p_b -> p_e.
  ch_f = #t with Ω_t(f) != Ω_(t-1)(f); lam_f = #t with Λ_t(f) != Λ_(t-1)(f); nl_f = ch_f - lam_f.
Counters (TOTALS; must be 0 if box 93 is right):
  npside : NP_t and Odd not on p_e;  npsub : NP_t and E_t(p_e) ⊄ E_t(p_b);  npboth : flip with NP_(t-1) and NP_t;
  npkind : flip with NP_(t-1) not a relock, or with NP_t not an unlock                                       [NP-SHAPE]
  relfail: relocks(g) > ch_(p_e);  unlfail: unlocks(g) > 1 + ch_(p_e)  (unit gate)                            [E-FACE-PAYS (a)]
  dexact : steps t where D's play avoids e_q at t-1 AND t (exact, vertex by vertex) and [Ω(p_e) changed] != [Ω(D) changed]  [(b)]
  kbfail : flips(g) > 2·lamch(g) + 2·min(nl_pe, nl_pb) + 1, lamch = #t with Λ changed at p_e or p_b  (unit gate)     [(d)]
  relGup : relocks at t with Λ(p_e), E(p_e) unchanged at t (a «γ-only» payment) and UP_(t-1)   [L-RED R229 Lemma REL-G (this box)]
Records (TOTALS): flips, relocks, unlocks, np_rel (relocks with NP_(t-1)), np_unl (unlocks with NP_t);
  relL / relE / relG = relocks paid by a Λ / e-set / γ-only change of p_e; relGnp = γ-only relocks with NP_(t-1);
  dpass = #gates whose D's play passes e_q at some t (E-FACE-PAYS (b)'s proviso FAILS somewhere);
  dbreak = #gates with unlocks > 1 + ch_D (whole-run ch_D; WAIT-QUIET's bound read WITHOUT the proviso); dbreakp = those among dpass;
  k1c2 = #gates with flips > 2(lamch + 1) (BOX 202's K1-FLIP(2)); mfl = max flips at one gate (per-gate MAXIMUM).
Usage: e93_229.py G.json ..."""
import sys, os, json, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r221")]
import own
K = ("gates", "flips", "relocks", "unlocks", "np_rel", "np_unl", "npside", "npsub", "npboth", "npkind", "relfail", "unlfail", "dexact",
     "kbfail", "relGup", "relL", "relE", "relG", "relGnp", "dpass", "dbreak", "dbreakp", "k1c2", "mfl")
def census(G, cap=3000):
    out, V, O, _ = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); N = G["N"]
    evs = {V[("e", q)] for q in O}; T = len(out) - 1; c = collections.Counter({k: 0 for k in K})
    nxt = [[s[u] if u < N else (tau[u] if o_[u] == 1 else succ[u][0]) for u in range(n)] for (s, vals, tau) in out]
    val = lambda t, v: out[t][1][v]; lam = lambda t, v: out[t][1][v][0]
    E = lambda t, v: frozenset(f for f in out[t][1][v][1] if f in evs)
    pc = {}
    def play(t, v):
        if (t, v) not in pc:
            seen = set(); u = v
            while u not in seen: seen.add(u); u = nxt[t][u]
            pc[(t, v)] = seen
        return pc[(t, v)]
    for q in O:
        g, pe, pb = V[("g", q)], V[("e", q)], V[("b", q)]; D = succ[pe][0]; c["gates"] += 1
        NP = [pe in E(t, pb) for t in range(T + 1)]; UP = [pe in E(t, pe) for t in range(T + 1)]
        ch = {f: sum(val(t, f) != val(t - 1, f) for t in range(1, T + 1)) for f in (pe, pb, D)}
        la = {f: sum(lam(t, f) != lam(t - 1, f) for t in range(1, T + 1)) for f in (pe, pb)}
        lamch = sum(lam(t, pe) != lam(t - 1, pe) or lam(t, pb) != lam(t - 1, pb) for t in range(1, T + 1))
        av = [pe not in play(t, D) for t in range(T + 1)]
        if not all(av): c["dpass"] += 1
        rel = unl = fl = 0
        for t in range(T + 1):
            if NP[t]:
                c["npside"] += nxt[t][g] != pe; c["npsub"] += not (E(t, pe) <= E(t, pb))
            if t == 0: continue
            if av[t - 1] and av[t]: c["dexact"] += (val(t, pe) != val(t - 1, pe)) != (val(t, D) != val(t - 1, D))
            a, b = nxt[t - 1][g], nxt[t][g]
            if a == b: continue
            fl += 1; isrel = a == pe
            if NP[t - 1] and NP[t]: c["npboth"] += 1
            if (NP[t - 1] and not isrel) or (NP[t] and isrel): c["npkind"] += 1
            if isrel:
                rel += 1; c["np_rel"] += NP[t - 1]
                if lam(t, pe) != lam(t - 1, pe): c["relL"] += 1
                elif E(t, pe) != E(t - 1, pe): c["relE"] += 1
                else:
                    c["relG"] += 1; c["relGnp"] += NP[t - 1]; c["relGup"] += UP[t - 1]
            else: unl += 1; c["np_unl"] += NP[t]
        c["flips"] += fl; c["relocks"] += rel; c["unlocks"] += unl; c["mfl"] = max(c["mfl"], fl)
        c["relfail"] += rel > ch[pe]; c["unlfail"] += unl > 1 + ch[pe]
        c["kbfail"] += fl > 2 * lamch + 2 * min(ch[pe] - la[pe], ch[pb] - la[pb]) + 1
        c["k1c2"] += fl > 2 * (lamch + 1)
        if unl > 1 + ch[D]: c["dbreak"] += 1; c["dbreakp"] += not all(av)
    c["T"] = T
    return c
if __name__ == "__main__":
    print("instance N+M T " + " ".join(K), flush=True)
    for f in sys.argv[1:]:
        G = json.load(open(f)); G = G.get("genome", G); c = census(G)
        print(os.path.basename(f), G["N"] + sum(len(o) for o in G["opts"]), c["T"], " ".join(str(c[k]) for k in K), flush=True)
