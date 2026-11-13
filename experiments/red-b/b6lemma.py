#!/usr/bin/env python3
"""L-RED-B B6 attempt 2: DIRECT TEST of the proof of L(G_k) = 2^k - 2 (docs/red-b/B6b-construction.md par. 4-6) on the actual key run.

For G_k = gk.build(k) (names kept) and its key run s_0, ..., s_T (onep.py), must-0 counters:
  kfact  (unit (state, comparison)): a key order differs from the static key facts
           K1  C_j = [v_j key-ahead of u_j] = [s(v_j) = c_j] if the pair is split, 0 if aligned     (c_j := C_(j-1); c_1 := s(v0))
           K2  D_j = [E(j+1) key-ahead of wv_j] = [s(E(j+1)) = 1] or [C_j = 0]                       (1 <= j <= k-2)
           K3  Z_j = [E(j+1) key-ahead of wu_j] = [s(E(j+1)) = 0] or [C_j = 1]                       (2 <= j <= k-2)
  vfact  (unit (state, comparison)): a value order differs from the static value facts
           V1  E_j = [v_j value-ahead of u_j] = 1 if split, [EY_j = s(v_j)] if aligned               (E_0 := s(v0))
           V2  EY_j = [yb_j value-ahead of y_j] = s(yb_j) if s(y_j) != s(yb_j), else [s(y_j) != E_(j-1)]
           V3  EYp_j = [ypb_j value-ahead of yp_j] = s(ypb_j) if s(yp_j) != s(ypb_j), else [1 - s(yp_j) != EY_j]
  sched  (unit steps): the set of (mover, new option) of step t differs from the RESPONSE LEMMA's schedule (generated recursively:
           unit j at rest a, input flips to c = 1 - a at step t: v_j at t; the forward observer goes back at t + 1; the upper unit
           responds from t; the other observer goes forward in the step t1 the upper end-follower arrives; u_j (and the forward
           member of Y'_j goes back) at t1 + 1; the upper unit responds from t1 + 1; the other member of Y'_j goes forward in the
           step t2 the upper end-follower returns; e_j at t2 + 1; top unit: v at t, the back observer forward at t + 1, u and the
           other observer back at t + 2)
  tlen   1 if T != 2^k - 2 or the schedule's last step != T;  rest  1 if the final state is not the predicted rest state
  swk    (unit movers): the number of switches of a mover differs from Theorem EXP-IDEAL (c): u_j, v_j, e_j and every observer of
         level j (y_j, yb_j, yp_j, ypb_j) 2^(j-1); v0 1; u0 and the wires 0
Descriptive: T, moves (total), maxsw.
Control B6L_CTRL=1: the schedule is generated with the two observers of every pair exchanged (sched must fire);
        B6L_CTRL=2: fact K2 is tested with «and» in place of «or» (kfact must fire).
Usage: b6lemma.py k ..."""
import sys, os
import onep, gk
CTRL = os.environ.get("B6L_CTRL", "0")


def test(k):
    G, names = gk.build(k)
    ix = {n: i for i, n in enumerate(names)}
    P = onep.OneP(G)
    S = P.run("key")
    T = len(S) - 1
    E = lambda j: f"e{j}" if j <= k - 2 else f"u{j}"
    c = {"kfact": 0, "vfact": 0, "sched": 0, "tlen": 0, "rest": 0}
    # static facts at every state
    for s in S:
        key = P.keys(s)
        mv, _ = P.values(s)
        o = lambda n: s[ix[n]]
        ka = lambda p, q: int(key[ix[p]] < key[ix[q]])        # p key-ahead of q
        va = lambda p, q: int(mv[ix[p]] > mv[ix[q]])          # p value-ahead of q
        C = {0: o("v0")}
        Ev = {0: o("v0")}
        EY = {}
        for j in range(1, k):
            Cj = int(o(f"v{j}") == C[j - 1]) if o(f"u{j}") != o(f"v{j}") else 0
            c["kfact"] += int(ka(f"v{j}", f"u{j}") != Cj)
            C[j] = Cj
            y, yb = o(f"y{j}"), o(f"yb{j}")
            EY[j] = yb if y != yb else int(y != Ev[j - 1])
            c["vfact"] += int(va(f"yb{j}", f"y{j}") != EY[j])
            Ev[j] = 1 if o(f"u{j}") != o(f"v{j}") else int(EY[j] == o(f"v{j}"))
            c["vfact"] += int(va(f"v{j}", f"u{j}") != Ev[j])
        c["kfact"] += int(ka("v0", "u0") != C[0]) + 0
        c["vfact"] += int(va("v0", "u0") != Ev[0])
        for j in range(1, k - 1):
            e1 = o(E(j + 1))
            D = int(e1 == 1 and C[j] == 0) if CTRL == "2" else int(e1 == 1 or C[j] == 0)
            c["kfact"] += int(ka(E(j + 1), f"wv{j}") != D)
        for j in range(2, k - 1):
            Z = int(o(E(j + 1)) == 0 or C[j] == 1)
            c["kfact"] += int(ka(E(j + 1), f"wu{j}") != Z)
            yp, ypb = o(f"yp{j}"), o(f"ypb{j}")
            EYp = ypb if yp != ypb else int((1 - yp) != EY[j])
            c["vfact"] += int(va(f"ypb{j}", f"yp{j}") != EYp)
    # the schedule
    sched = {}

    def add(t, n, opt):
        sched.setdefault(t, set()).add((n, opt))

    def resp(j, t, a):
        cc = 1 - a
        add(t, f"v{j}", cc)
        f, g = (f"yb{j}", f"y{j}") if a == 0 else (f"y{j}", f"yb{j}")
        if CTRL == "1":
            f, g = g, f
        if j == k - 1:
            add(t + 1, g, 1)
            add(t + 2, f"u{j}", cc)
            add(t + 2, f, 0)
            return t + 2
        add(t + 1, f, 0)
        t1 = resp(j + 1, t, 0)
        add(t1, g, 1)
        add(t1 + 1, f"u{j}", cc)
        hasp = 2 <= j <= k - 2
        if hasp:
            fp, gp = (f"ypb{j}", f"yp{j}") if a == 0 else (f"yp{j}", f"ypb{j}")
            add(t1 + 1, fp, 0)
        t2 = resp(j + 1, t1 + 1, 1)
        if hasp:
            add(t2, gp, 1)
            add(t2 + 1, f"e{j}", cc)
            return t2 + 1
        return t2

    add(1, "v0", 1)
    last = resp(1, 1, 0)
    for t in range(1, max(T, last) + 1):
        act = {(names[x], S[t][x]) for x in range(G["N"]) if S[t][x] != S[t - 1][x]} if t <= T else set()
        c["sched"] += int(act != sched.get(t, set()))
    c["tlen"] = int(T != 2 ** k - 2 or last != T)
    fin = S[-1]
    exp = {n: 0 for n in names}
    exp["v0"] = 1
    exp["u1"] = exp["v1"] = 1
    exp["y1"] = 1
    for j in range(2, k):
        exp[f"yb{j}"] = 1
        if j <= k - 2:
            exp[f"ypb{j}"] = 1
    c["rest"] = int(any(fin[ix[n]] != exp[n] for n in names))
    st = onep.stats(G, S)
    import re
    swk = 0
    for n in names:
        m = re.fullmatch(r"(u|v|e|y|yb|yp|ypb)(\d+)", n)
        want = 0 if n == "u0" or n.startswith("w") else (1 if n == "v0" else 2 ** (int(m.group(2)) - 1))
        swk += int(st["sw"][ix[n]] != want)
    print(f"G_{k} ctrl {CTRL} states {T + 1} kfact {c['kfact']} vfact {c['vfact']} sched {c['sched']} tlen {c['tlen']} rest {c['rest']} swk {swk} T {T} moves {sum(st['sw'])} maxsw {max(st['sw'])}", flush=True)


if __name__ == "__main__":
    for a in sys.argv[1:]:
        test(int(a))
