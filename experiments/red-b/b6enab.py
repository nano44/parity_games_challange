#!/usr/bin/env python3
"""L-RED-B B6 attempt 2 (for the referees): the ENABLING predicates of P-N5-EXP §5 (V4, K4) against the model itself, on the real
run of G_k, state by state and mover by mover.

For every state s_t of the key run of G_k and every mover x, the packet's predicates are computed from the rule's table (the
quantities C, E, EY, EY′, D, Z of K1-K3 / V1-V3) and compared with what the simulator computes from R104's definition:
  venab  (unit (state, mover)): «x is value-enabled under s_t» (V4) differs from |A_(s_t)(x)| = 2 (the definition's availability)
  kenab  (unit (step, mover)):  «x is key-enabled in the step s_t -> s_(t+1)» (K4) differs from «the key of x's OTHER option is
                                smaller than the key of its current one, both with s_(t+1) on the lower levels» (MOVE-2 (b))
  movd   (unit (step, mover)):  (value-enabled under s_t and key-enabled in the step) differs from «x moves at that step»
Must be 0 everywhere. Controls: B6E_CTRL=1 swaps V2's two cases (EY_j; venab must fire); B6E_CTRL=2 swaps D_j's two disjuncts
in K4 (kenab must fire). (A control that drops V1's «aligned» case is INERT on this family: along the run the aligned case also
evaluates to 0, which is why the controls below are the ones used.)
Usage: b6enab.py k ..."""
import sys, os
import onep, gk
CTRL = os.environ.get("B6E_CTRL", "0")


def test(k):
    G, names = gk.build(k)
    ix = {n: i for i, n in enumerate(names)}
    P = onep.OneP(G)
    S = P.run("key")
    T = len(S) - 1
    E = lambda j: f"e{j}" if j <= k - 2 else f"u{j}"
    c = {"venab": 0, "kenab": 0, "movd": 0}

    def quantities(s):
        o = lambda n: s[ix[n]]
        C = {0: o("v0")}
        Ev = {0: o("v0")}
        EY = {}
        EYp = {}
        for j in range(1, k):
            C[j] = int(o(f"v{j}") == C[j - 1]) if o(f"u{j}") != o(f"v{j}") else 0
            y, yb = o(f"y{j}"), o(f"yb{j}")
            EY[j] = (int(y != Ev[j - 1]) if y != yb else yb) if CTRL == "1" else (yb if y != yb else int(y != Ev[j - 1]))
            Ev[j] = 1 if o(f"u{j}") != o(f"v{j}") else int(EY[j] == o(f"v{j}"))
            if 2 <= j <= k - 2:
                yp, ypb = o(f"yp{j}"), o(f"ypb{j}")
                EYp[j] = ypb if yp != ypb else int((1 - yp) != EY[j])
        D = {}
        Z = {}
        for j in range(1, k - 1):
            D[j] = int(o(E(j + 1)) == 1 or C[j] == 0)
            if CTRL == "2":
                D[j] = int(o(E(j + 1)) == 0 or C[j] == 1)
        for j in range(2, k - 1):
            Z[j] = int(o(E(j + 1)) == 0 or C[j] == 1)
        return o, C, Ev, EY, EYp, D, Z

    def venab(n, s):
        o, C, Ev, EY, EYp, D, Z = quantities(s)
        if n == "u0":
            return False
        if n == "v0":
            return o("v0") == 0
        if n.startswith("w"):
            return False
        kind = n.rstrip("0123456789")
        j = int(n[len(kind):])
        if kind == "v":
            return EY[j] == 1 - o(n)
        if kind == "u":
            return EY[j] == o(n)
        if kind == "e":
            return EYp[j] == o(n)
        if kind == "y":
            return Ev[j - 1] == (1 if o(n) == 0 else 0)
        if kind == "yb":
            return Ev[j - 1] == (0 if o(n) == 0 else 1)
        if kind == "yp":
            return EY[j] == (0 if o(n) == 0 else 1)
        if kind == "ypb":
            return EY[j] == (1 if o(n) == 0 else 0)
        raise AssertionError(n)

    def kenab(n, s, sn):
        """K4 for x at its CURRENT option under s, with the quantities of the new state sn (which the step has fixed below x)"""
        _, C, Ev, EY, EYp, D, Z = quantities(sn)
        o = lambda m: s[ix[m]]
        if n.startswith("w") or n in ("u0", "v0"):
            return (n == "v0" and o("v0") == 0)
        kind = n.rstrip("0123456789")
        j = int(n[len(kind):])
        if kind in ("u", "v", "e"):
            return o(n) != C[j - 1]
        top = j == k - 1
        if kind in ("y", "yb"):
            d = C[k - 1] if top else D[j]
            return (d == 1) if o(n) == 0 else (d == 0)
        if kind in ("yp", "ypb"):
            return (Z[j] == 1) if o(n) == 0 else (Z[j] == 0)
        raise AssertionError(n)

    for t in range(T + 1):
        s = S[t]
        A, _ = P.improving(s)
        for n in names:
            c["venab"] += int(venab(n, s) != (len(A[ix[n]]) == 2))
        if t < T:
            sn = S[t + 1]
            key = {}
            kk = {}
            for x in P.bylev:                 # keys of both options with s_(t+1) below
                for o2 in range(2):
                    wt = G["opts"][x][o2][0]
                    kk[(x, o2)] = (key[wt] if G["lev"][x] > 0 else ()) + (G["gate"][x][o2],)
                key[x] = kk[(x, sn[x])]
            for n in names:
                x = ix[n]
                cur = s[x]
                ke = kk[(x, 1 - cur)] < kk[(x, cur)]
                c["kenab"] += int(kenab(n, s, sn) != ke)
                c["movd"] += int((venab(n, s) and ke) != (sn[x] != cur))
    print(f"G_{k} ctrl {CTRL} states {T + 1} venab {c['venab']} kenab {c['kenab']} movd {c['movd']} T {T}", flush=True)


if __name__ == "__main__":
    for a in sys.argv[1:]:
        test(int(a))
