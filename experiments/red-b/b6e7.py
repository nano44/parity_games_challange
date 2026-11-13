#!/usr/bin/env python3
"""L-RED-B packet P-N5-EXP, fixes entry 7: DIRECT TESTS for REFEREE-2 42's items F-1 and F-3 (two modes, one line per k).
No other lane's file is needed (gk.py, onep.py and b6prefix.py's class Fam only).

Mode r3 (F-1): clause (R3) of LEMMA' WITH ITS RANGE.
  (R3), as restated in entry 7: for T = last and j >= 2, s_tau(E(j)) = a for every tau with t - 1 <= tau < last, and E(j)
  moves to c at step last; and under s_last: REST_j(c) and REST_i(0) for every i > j (the rest clause for every j >= 1).
  E(j) = e_j for 2 <= j <= k - 2 and u_(k-1) for j = k - 1 (the end-follower of level j; the packet's par. 3).
  The wording «for tau < last» of fixes entry 4.4 (inherited from the frozen l. 203) has no lower end; read literally (every
  tau with 0 <= tau < last) it is false at every window of a unit j >= 2 but the first, because E(j) stood at c until the
  previous response of unit j ended. That literal reading is the firing control here.
  UNIT: a response window (j, t, a) of the proof's recursion on the run of G_k (the windows of b6prefix.py mode run), resp. a
  (window, tau) pair. All states are read off the simulator.
    windows2          the windows with j >= 2 (2^(k-1) - 2 of the 2^(k-1) - 1 windows)
    r3in     (must 0) (window with j >= 2, tau) with t - 1 <= tau < last and s_tau(E(j)) != a
    r3move   (must 0) windows with j >= 2 where E(j) does not move from a to c exactly at step last
    r3rest   (must 0) windows (every j >= 1) where REST_j(c) or some REST_i(0), i > j, fails under s_last
    literal           windows with j >= 2 where s_tau(E(j)) != a for some tau < t - 1 (the literal reading «tau < last» fails);
                      expected 2^(k-1) - k (every window of a unit j >= 2 but its first): a firing control for every k >= 3
    litdiff  (must 0) [literal != 2^(k-1) - k]
  Control B6E7_CTRL=1: the range one step too long (t - 1 <= tau <= last): r3in must fire, once per window with j >= 2.

Mode xt (F-3): which movers are Xi-targets in G_k (fixes entry 5.1's parenthesis).
  UNIT: an option of G_k. kinds = the kinds of movers that are the Xi-target of some option (u, v, y, yb, yp, ypb = the
  packet's u, v, y, y-bar, y', y'-bar); wiretgt (must 0) = options whose Xi-target is a wire; etgt (must 0) = options whose
  Xi-target is an end-follower e_j; yptgt = options whose Xi-target is a y'_j or y'-bar_j (expected 2(k - 3): the two options
  of each e_j), ypdiff (must 0) = [yptgt != 2(k - 3)].
  Control B6E7_CTRL=2: the list of 5.1's parenthesis as written (u, v, y, y-bar only): outside = options whose Xi-target is a
  mover of another kind; it must fire for k >= 4 (it equals yptgt).

Usage: b6e7.py r3 k [k ...]   |   b6e7.py xt k [k ...]"""
import sys, os, re
import b6prefix, gk

CTRL = os.environ.get("B6E7_CTRL", "0")


def mode_r3(k):
    F = b6prefix.Fam(k)
    S = F.P.run("key")
    T = len(S) - 1
    wins = []
    F.resp(1, 1, 0, {}, wins)
    c = dict(r3in=0, r3move=0, r3rest=0, literal=0)
    w2 = 0
    for (j, t, a, last) in wins:
        cc = 1 - a
        assert last == F.end(j, t) and last <= T
        if not (F.rest(S[last], j, cc) and all(F.rest(S[last], i, 0) for i in range(j + 1, k))):
            c["r3rest"] += 1
        if j < 2:
            continue
        w2 += 1
        e = F.ix[f"e{j}"] if j <= k - 2 else F.ix[f"u{j}"]
        hi = last + 1 if CTRL == "1" else last
        c["r3in"] += sum(1 for tau in range(t - 1, hi) if S[tau][e] != a)
        c["r3move"] += int(not (S[last - 1][e] == a and S[last][e] == cc))
        c["literal"] += int(any(S[tau][e] != a for tau in range(0, t - 1)))
    exp = 2 ** (k - 1) - k
    print(f"G_{k} mode r3 ctrl {CTRL} T {T} windows {len(wins)} windows2 {w2} r3in {c['r3in']} r3move {c['r3move']} "
          f"r3rest {c['r3rest']} literal {c['literal']} expected {exp} litdiff {int(c['literal'] != exp)}", flush=True)


def mode_xt(k):
    G, names = gk.build(k)
    kind = lambda x: re.sub(r"\d+", "", names[x])
    kinds = set()
    wiretgt = etgt = yptgt = outside = 0
    for x in range(G["N"]):
        for (wt, xt, b) in G["opts"][x]:
            if xt < 0:
                continue
            kd = kind(xt)
            kinds.add(kd)
            wiretgt += int(kd in ("wv", "wu"))
            etgt += int(kd == "e")
            yptgt += int(kd in ("yp", "ypb"))
            outside += int(kd not in ("u", "v", "y", "yb"))
    exp = 2 * (k - 3)
    line = (f"G_{k} mode xt ctrl {CTRL} N {G['N']} kinds {' '.join(sorted(kinds))} wiretgt {wiretgt} etgt {etgt} yptgt {yptgt} "
            f"expected {exp} ypdiff {int(yptgt != exp)}")
    if CTRL == "2":
        line += f" outside {outside}"
    print(line, flush=True)


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in ("r3", "xt"):
        print(__doc__)
        sys.exit(2)
    for a in sys.argv[2:]:
        (mode_r3 if sys.argv[1] == "r3" else mode_xt)(int(a))
