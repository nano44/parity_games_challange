#!/usr/bin/env python3
"""L-RED 63 R229 item 1: independent census for L-SI 48 BOX 92 (claude/l-si d962efdb) Lemma GATE-LOW-NULL and the WAIT-CLOSED rows,
on R221 own.py (IDEAL-CYC Howard from the genome's start, pad-free Γ; cap 3000). No L-SI code.
Unit: gate g = (x, k) (Odd, faces p_e = e_q, p_b = b_q), step t of the run. Λ, P = the VJ value (Λ, P-set, len); E_t(v) = e-vertices of P.
  LAM_t: Λ_t(e_q) = Λ_t(b_q);  PRIV_t: e_q ∉ E_t(b_q);  UP_t: e_q ∈ E_t(e_q) (e_q above Λ: the lemma's (b) hypothesis).
  π(X) = {f ∈ X : rk f >= rk e_q}.  Flip of g at t: Odd's choice differs at t-1, t (only where the two face values differ at both; a tie
  step is counted in 'tie').  Each flip goes to the FIRST class that applies:
  lam  : Λ differs at t-1 or t;  np : non-PRIV at t-1 or t;  below : LAM ∧ PRIV both, but not UP at t-1 or t (outside (b)'s proof);
  up   : LAM ∧ PRIV ∧ UP both, π changed (the lemma's case);  gln : the same with π unchanged (Lemma (b) FAILS; must be 0).
  predfail (unit (g, t), TOTAL): at LAM ∧ PRIV ∧ UP, Odd's choice is not the face predicted by (a) (Odd takes the face whose π is <lex).
  belowfl: 'below' flips with π unchanged (box 92's tool counts them as glnfail; DATA claim 0).
Per gate MAXIMA: mfl (all flips), mnp (np flips), mbelow; K1 (unit vertex v, whole run): lamch = max #Λ-changes of one vertex; lamret =
  #vertices whose Λ returns to an earlier value after leaving it (box 91 TRIGGER (α): «never undone»; TOTAL).
Output line: instance N+M T C flips lam np below up gln tie predfail belowfl mfl mnp mbelow lamch lamret gates
Usage: gate229.py G.json ..."""
import sys, os, json, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r221")]
import own
K = ("flips", "lam", "np", "below", "up", "gln", "tie", "predfail", "belowfl", "mfl", "mnp", "mbelow", "lamch", "lamret", "gates")
def census(G, cap=3000):
    out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); vj = own.VJ(prio); rk = vj.rk
    evs = {V[("e", q)] for q in O}; T = len(out) - 1; c = collections.Counter({k: 0 for k in K}); c["T"] = T
    lam = lambda t, v: out[t][1][v][0]
    E = lambda t, v: frozenset(f for f in out[t][1][v][1] if f in evs)
    for q in O:
        g, pe, pb = V[("g", q)], V[("e", q)], V[("b", q)]; r0 = rk[pe]; c["gates"] += 1
        pi = lambda X: frozenset(f for f in X if rk[f] >= r0)
        def ch(t):
            a, b = out[t][1][pe], out[t][1][pb]
            return None if a == b else out[t][2][g]
        L = lambda t: lam(t, pe) == lam(t, pb); P = lambda t: pe not in E(t, pb); U = lambda t: pe in E(t, pe)
        fl = collections.Counter()
        for t in range(T + 1):
            if L(t) and P(t) and U(t) and ch(t) is not None:
                A, B = pi(E(t, pe)), pi(E(t, pb)); z = max(A ^ B, key=lambda f: rk[f])
                pred = pb if z in A else pe          # Odd avoids the face holding the top (even) e-letter
                c["predfail"] += out[t][2][g] != pred
            if t == 0: continue
            a, b = ch(t - 1), ch(t)
            if a is None or b is None:
                c["tie"] += (a != b); continue
            if a == b: continue
            c["flips"] += 1; fl["all"] += 1
            if not (L(t) and L(t - 1)): c["lam"] += 1; continue
            if not (P(t) and P(t - 1)): c["np"] += 1; fl["np"] += 1; continue
            same = pi(E(t, pe)) == pi(E(t - 1, pe)) and pi(E(t, pb)) == pi(E(t - 1, pb))
            if not (U(t) and U(t - 1)): c["below"] += 1; fl["below"] += 1; c["belowfl"] += same; continue
            if same: c["gln"] += 1
            else: c["up"] += 1
        c["mfl"] = max(c["mfl"], fl["all"]); c["mnp"] = max(c["mnp"], fl["np"]); c["mbelow"] = max(c["mbelow"], fl["below"])
    for v in range(n):
        seen = [lam(0, v)]; nch = 0; ret = False
        for t in range(1, T + 1):
            if lam(t, v) != lam(t - 1, v):
                nch += 1
                if lam(t, v) in seen: ret = True
                seen.append(lam(t, v))
        c["lamch"] = max(c["lamch"], nch); c["lamret"] += ret
    Cc = 0                                    # C = per-(v, I, y) max #y-tops (own census, as mclimb228)
    for v in range(n):
        t = 0
        while t <= T:
            u = t
            while u + 1 <= T and lam(u + 1, v) == lam(t, v): u += 1
            Es = [E(i, v) for i in range(t, u + 1)]; t = u + 1
            tops = collections.Counter(max(a ^ b, key=lambda e: rk[e]) for a, b in zip(Es, Es[1:]) if a != b)
            Cc = max(Cc, max(tops.values(), default=0))
    c["C"] = Cc
    return c
if __name__ == "__main__":
    print("instance N+M T C " + " ".join(K), flush=True)
    for f in sys.argv[1:]:
        G = json.load(open(f)); G = G.get("genome", G); c = census(G)
        print(os.path.basename(f), G["N"] + sum(len(o) for o in G["opts"]), c["T"], c["C"], " ".join(str(c[k]) for k in K), flush=True)
