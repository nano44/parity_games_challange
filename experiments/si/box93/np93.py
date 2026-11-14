#!/usr/bin/env python3
"""L-SI box 93 (K7, the non-PRIV gate): shape of non-PRIV flips and who pays them, on two engines (engines of box91/mult91.py).
Unit: an Odd vertex o with two successors (faces) p_e, p_b, p_e's play starting at o's e-vertex e_o (as box92/gate92.py); D := e_o's
single successor (the e-face continuation, W-target); a time t of the whole run. NP_t := e_o in E_t(p_b) (non-PRIV); LAM_t := Lambda_t(p_e)
== Lambda_t(p_b). A flip at t is an UNLOCK (p_b -> p_e) or a RELOCK (p_e -> p_b). ch_f := #t with the value of f changed (whole run);
lam_f := #t with Lambda(f) changed; ech_f := #t with E(f) changed and Lambda(f) not; gam_f := ch_f - lam_f - ech_f (value only, below e's).
Counters (TOTALS; must be 0):
  npside : NP_t while Odd at o does not play p_e at t                         [Lemma NP-SHAPE (a): a play passing e_o passes o -> p_e]
  npsub  : NP_t and E_t(p_e) not a subset of E_t(p_b)                          [NP-SHAPE (a): p_e's play is a suffix of p_b's]
  npboth : a flip at t with NP_(t-1) and NP_t                                  [NP-SHAPE (b)]
  npkind : a flip at t with NP_(t-1) that is not a RELOCK, or with NP_t that is not an UNLOCK      [NP-SHAPE (b)]
  relfail: #RELOCKs of o > ch_(p_e);  unlfail: #UNLOCKs of o > 1 + ch_(p_e)    [Corollary E-FACE-PAYS (GATE-RACE (a), PRIV-free)]
  dfail  : a step t with the value of p_e changed and the value of D unchanged, D's play not passing e_o at t-1 and t (proxy: e_o in
           neither E_(t-1)(D) nor E_t(D) and Lambda(D) == Lambda(p_e) at t-1, t)                              [Corollary E-FACE-PAYS (c)]
Records: per genome TOTALS np_rel (relocks with NP_(t-1)), np_unl (unlocks with NP_t), flips; at the max-flip gate: flips, ch_pe, ch_pb,
lam_pe, ech_pe, gam_pe, lam_pb, ech_pb, gam_pb, ch_D; k1c2 := #gates with flips > 2(lamch + 1), lamch := #t with Lambda changed at p_e or
p_b (L-NEW box 202's K1-FLIP(2) counter); k1both := #those gates where BOTH faces have a non-Lambda change (ech + gam >= 1 on each face:
must equal k1c2 by E-FACE-PAYS (d)); relpay: relocks by the kind of p_e's change at t: L (Lambda) / E (e-set) / G (below e's).
Controls: CTRL=swap: p_e and p_b exchanged in relfail / unlfail (fires where the e-face is the frequent changer); CTRL=tight: the bound
lowered by 1 (fires where relocks = ch_(p_e), e.g. MW's race gate).
Usage: np93.py own|g3 G.json ...   (OWN_DIR / ROOT as for box91/mult91.py)"""
import sys, os, json, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box91"))
import mult91
CTRL = os.environ.get("CTRL", "")
K = ("gates", "flips", "np_rel", "np_unl", "npside", "npsub", "npboth", "npkind", "relfail", "unlfail", "dfail", "k1c2", "k1both",
     "relL", "relE", "relG", "mx_flips", "mx_ch_pe", "mx_ch_pb", "mx_lam_pe", "mx_ech_pe", "mx_gam_pe", "mx_lam_pb", "mx_ech_pb",
     "mx_gam_pb", "mx_ch_D")
def run(T, n, nx, lam, E, rk, evs, odd2, val):
    c = collections.Counter({k: 0 for k in K}); best = None
    for (o, p, q) in odd2:
        pe = pb = eo = None
        for f, g in ((p, q), (q, p)):
            if f in evs: pe, pb, eo = f, g, f
            elif nx(0, f) in evs and all(nx(t, f) == nx(0, f) for t in range(T + 1)): pe, pb, eo = f, g, nx(0, f)
        if pe is None: continue
        D = nx(0, eo); c["gates"] += 1
        NP = [eo in E(t, pb) for t in range(T + 1)]
        def kinds(f):
            ch = la = ec = 0
            for t in range(1, T + 1):
                if val(t, f) != val(t - 1, f):
                    ch += 1
                    if lam(t, f) != lam(t - 1, f): la += 1
                    elif E(t, f) != E(t - 1, f): ec += 1
            return ch, la, ec, ch - la - ec
        che, lae, ece, gae = kinds(pe); chb, lab, ecb, gab = kinds(pb); chD = kinds(D)[0]
        fl = rel = unl = lamch = 0
        for t in range(T + 1):
            if NP[t] and nx(t, o) != pe: c["npside"] += 1
            if NP[t] and not (E(t, pe) <= E(t, pb)): c["npsub"] += 1
            if t == 0: continue
            if lam(t, pe) != lam(t - 1, pe) or lam(t, pb) != lam(t - 1, pb): lamch += 1
            if val(t, pe) != val(t - 1, pe) and val(t, D) == val(t - 1, D) and lam(t, D) == lam(t, pe) and lam(t - 1, D) == lam(t - 1, pe) \
               and eo not in E(t, D) and eo not in E(t - 1, D): c["dfail"] += 1
            if nx(t, o) == nx(t - 1, o): continue
            fl += 1; isrel = nx(t - 1, o) == pe
            rel += isrel; unl += not isrel
            if NP[t - 1] and NP[t]: c["npboth"] += 1
            if (NP[t - 1] and not isrel) or (NP[t] and isrel): c["npkind"] += 1
            c["np_rel"] += NP[t - 1] and isrel; c["np_unl"] += NP[t] and not isrel
            if isrel:
                if lam(t, pe) != lam(t - 1, pe): c["relL"] += 1
                elif E(t, pe) != E(t - 1, pe): c["relE"] += 1
                else: c["relG"] += 1
        A, B = (chb, che) if CTRL == "swap" else (che, chb)
        if CTRL == "tight": A -= 1
        c["relfail"] += rel > A; c["unlfail"] += unl > 1 + A
        c["flips"] += fl
        if fl > 2 * (lamch + 1):
            c["k1c2"] += 1; c["k1both"] += (ece + gae >= 1) and (ecb + gab >= 1)
        row = (fl, che, chb, lae, ece, gae, lab, ecb, gab, chD)
        if best is None or row[0] > best[0]: best = row
    if best:
        for k, x in zip(K[16:], best): c[k] = x
    return c
if __name__ == "__main__":
    eng = sys.argv[1]; print("engine", eng, "instance N+M", " ".join(K), flush=True)
    for f in sys.argv[2:]:
        G = json.load(open(f)); G = G.get("genome", G)
        c = run(*(mult91.eng_own(G) if eng == "own" else mult91.eng_g3(G)))
        print(eng, os.path.basename(f), G["N"] + sum(len(o) for o in G["opts"]), " ".join(str(c[k]) for k in K), flush=True)
