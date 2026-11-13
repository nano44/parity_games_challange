#!/usr/bin/env python3
"""REFEREE successor 35: an ABSTRACT bit model of the IDEAL run on G_k, derived by hand from the rule (my own derivation of the
static comparison facts; R-GK-precheck / the review of P-N5-EXP), and its test against the genome simulator gk_ideal.py.
State: dict name -> bit, names u_j, v_j (0 <= j <= k-1), e_j (2 <= j <= k-2), y_j, yb_j (1 <= j <= k-1), yp_j, ypb_j (2 <= j <= k-2).
Wires are constant (option 0: its beta outranks option 1's, start 0).

Xi side (old state s; all parities even, so the chain whose beta-set holds the top-ranked beta of the symmetric difference wins;
ranks fall with dep, so two chains are compared from the exit end backwards):
  Wn(0)  = 'v' if beta(v0, s) outranks beta(u0, s)   [ranks u0.1 < v0.0 < u0.0 < v0.1]
  z(j)   = which of y_j, yb_j has the better chain: targets t(y_j) = u/v for 0/1, t(yb_j) = v/u for 0/1 (in B_(j-1));
           different targets: the one aiming at Wn(j-1); both at u: yb; both at v: y
  Wn(j)  = which of u_j, v_j has the better chain: t(u_j) = yb/y for 0/1, t(v_j) = y/yb for 0/1; different: the one aiming at z(j);
           equal: v
  z'(j)  = which of yp_j, ypb_j has the better chain: t(yp_j) = yb/y for 0/1, t(ypb_j) = y/yb for 0/1; different: the one aiming at
           z(j); both at yb: ypb; both at y: yp
  preferred options: u0: 0; v0: 1; y_j: 1 iff Wn(j-1) = v; yb_j: 0 iff Wn(j-1) = v; u_j: 1 iff z(j) = y; v_j: 0 iff z(j) = y;
           yp_j: 1 iff z(j) = y; ypb_j: 0 iff z(j) = y; e_j: 1 iff z'(j) = yp
W side (NEW state s', level by level): kap(j) = which of u_j, v_j has the smaller key:
  kap(0) = 'v' iff gate(v0, s') < gate(u0, s')   [eps u0: 2, 5; v0: 3, 1]
  kap(j) = (same W-target: 'u'; else the one whose W-target is kap(j-1)), W-target of option o = u_(j-1) / v_(j-1) for o = 0 / 1
  key-least options: u_j, v_j, e_j: 0 iff kap(j-1) = u;
    y_j, yb_j (j <= k-2): fwd (1) iff E' = 1 or (E' = 0 and kap(j) = u), with E' := e'_(j+1) (j <= k-3), u'_(k-1) (j = k-2);
    y_(k-1), yb_(k-1): 1 iff kap(k-1) = v;
    yp_j, ypb_j: fwd (1) iff E' = 0 or (E' = 1 and kap(j) = v)
A mover switches iff its other option is preferred (strictly Xi-better) and key-least."""
import sys


def start(k):
    s = {}
    for j in range(k): s['u%d' % j] = 0; s['v%d' % j] = 0
    for j in range(2, k - 1): s['e%d' % j] = 0
    for j in range(1, k): s['y%d' % j] = 0; s['yb%d' % j] = 1
    for j in range(2, k - 1): s['yp%d' % j] = 0; s['ypb%d' % j] = 1
    return s


def xi_side(k, s):
    """returns (Wn, z, zp) dicts for the old state s"""
    Wn, z, zp = {}, {}, {}
    rank0 = {('u', 1): 0, ('v', 0): 1, ('u', 0): 2, ('v', 1): 3}
    Wn[0] = 'v' if rank0[('v', s['v0'])] > rank0[('u', s['u0'])] else 'u'
    for j in range(1, k):
        ty = 'u' if s['y%d' % j] == 0 else 'v'
        tyb = 'v' if s['yb%d' % j] == 0 else 'u'
        if ty != tyb: z[j] = 'y' if ty == Wn[j - 1] else 'yb'
        else: z[j] = 'yb' if ty == 'u' else 'y'
        tu = 'yb' if s['u%d' % j] == 0 else 'y'
        tv = 'y' if s['v%d' % j] == 0 else 'yb'
        if tu != tv: Wn[j] = 'u' if tu == z[j] else 'v'
        else: Wn[j] = 'v'
        if 2 <= j <= k - 2:
            tp = 'yb' if s['yp%d' % j] == 0 else 'y'
            tpb = 'y' if s['ypb%d' % j] == 0 else 'yb'
            if tp != tpb: zp[j] = 'yp' if tp == z[j] else 'ypb'
            else: zp[j] = 'ypb' if tp == 'yb' else 'yp'
    return Wn, z, zp


def preferred(k, s):
    Wn, z, zp = xi_side(k, s)
    p = {'u0': 0, 'v0': 1}
    for j in range(1, k):
        p['y%d' % j] = 1 if Wn[j - 1] == 'v' else 0
        p['yb%d' % j] = 0 if Wn[j - 1] == 'v' else 1
        p['u%d' % j] = 1 if z[j] == 'y' else 0
        p['v%d' % j] = 0 if z[j] == 'y' else 1
        if 2 <= j <= k - 2:
            p['yp%d' % j] = 1 if z[j] == 'y' else 0
            p['ypb%d' % j] = 0 if z[j] == 'y' else 1
            p['e%d' % j] = 1 if zp[j] == 'yp' else 0
    return p


def step(k, s):
    p = preferred(k, s)
    n = {}
    kap = {}
    eps0 = {('u', 0): 2, ('u', 1): 5, ('v', 0): 3, ('v', 1): 1}

    def move(name, least):
        n[name] = p[name] if (p[name] != s[name] and p[name] == least) else s[name]
    # level 0: key = (gate); least option of u0 is 0 (eps 2 < 5), of v0 is 1 (eps 1 < 3)
    move('u0', 0); move('v0', 1)
    kap[0] = 'v' if eps0[('v', n['v0'])] < eps0[('u', n['u0'])] else 'u'
    for lev in range(1, k + 1):
        j = lev
        if j <= k - 1:
            least = 0 if kap[j - 1] == 'u' else 1
            move('u%d' % j, least); move('v%d' % j, least)
            if 2 <= j <= k - 2: move('e%d' % j, least)
            tu = 'u' if n['u%d' % j] == 0 else 'v'
            tv = 'u' if n['v%d' % j] == 0 else 'v'
            kap[j] = 'u' if tu == tv else ('u' if tu == kap[j - 1] else 'v')
        i = lev - 2                                   # y_i, yb_i, yp_i, ypb_i live at level i + 2 for i <= k - 2
        if 1 <= i <= k - 2:
            Ep = n['e%d' % (i + 1)] if i <= k - 3 else n['u%d' % (k - 1)]
            least_y = 1 if (Ep == 1 or kap[i] == 'u') else 0
            move('y%d' % i, least_y); move('yb%d' % i, least_y)
            if i >= 2:
                least_p = 1 if (Ep == 0 or kap[i] == 'v') else 0
                move('yp%d' % i, least_p); move('ypb%d' % i, least_p)
        if lev == k:
            least_t = 1 if kap[k - 1] == 'v' else 0
            move('y%d' % (k - 1), least_t); move('yb%d' % (k - 1), least_t)
    return n, p, kap


def run(k, keep=False, maxsteps=10 ** 8):
    s = start(k); L = 0; S = [dict(s)] if keep else None
    while True:
        n, p, kap = step(k, s)
        if n == s: return L, S
        s = n; L += 1
        if keep: S.append(dict(s))
        if L > maxsteps: raise RuntimeError('maxsteps')


if __name__ == '__main__':
    import gk_build as B
    import gk_ideal as I
    for k in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
        G = B.genome(k); nm = G['names']
        L, why, S = I.run(G, keep=True)
        La, Sa = run(k, keep=True)
        bad = 0
        for t in range(min(L, La) + 1):
            for x in range(G['N']):
                want = S[t][x]
                got = Sa[t].get(nm[x], 0)             # wires: constant 0
                if want != got: bad += 1
        # the preferred option of the abstract model against the genome's availability, at every state of the run
        badp = 0
        for t in range(min(L, La) + 1):
            p = preferred(k, Sa[t])
            for x in range(G['N']):
                if nm[x].startswith('w'): continue
                av = I.avail(G, S[t], x)
                other_better = (len(av) == 2)
                if other_better != (p[nm[x]] != S[t][x]): badp += 1
        print('G_%d: L genome %d, L abstract %d; ABS (state bits that differ, all steps) %d; PREF (mover-states where «the other option is Xi-better» differs) %d' % (k, L, La, bad, badp))
        sys.stdout.flush()
