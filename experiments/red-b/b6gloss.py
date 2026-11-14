#!/usr/bin/env python3
"""L-RED-B packet P-N5-EXP, fixes entry 10 (REFEREE 37's F-L3-1, relayed by the Lead): the RANK CLAUSE of rule R against the
gloss that the lines L-1 to L-4 gave of it. One line per k; no other lane's file is needed (gk.py, onep.py).

Rule R (packet l. 98-99, read as fixes entry 5.1): br := the rank of the TRIPLE (-depth, local delta, beta-id), a wire counting as
depth 2k + 5: a smaller Xi-depth outranks a larger one, inside a depth the larger local delta outranks, and the beta-id breaks
the remaining ties (wire options only; the smaller beta-id gets the smaller rank).
The gloss of L-1 .. L-4 was «beta-ranks by Xi-depth with ties broken by beta-id»: it drops the local delta.

The depths and local deltas are transcribed here from the packet's table (par. 3), independently of gk.py's own dictionaries.
For each variant the genome is gk.build(k) with br replaced, and L is the length of its IDEAL run (onep, rule key).
  rule     the triple (-depth, delta, beta-id) from this file's transcription; rulediff (must 0) = [its br != gk.py's br]
  Lrule    its run length; Ldiff (must 0) = [Lrule != 2^k - 2]
  wire0    rule R with the wires counted at Xi-depth 0 (their Xi-target is X, like u_0, v_0) instead of 2k + 5:
           Lwire0; wire0diff (must 0) = [Lwire0 != 2^k - 2]  (the run does not depend on where the wire ranks stand)
  oldinc   THE OLD GLOSS: rank by (-depth, beta-id), ties by increasing beta-id: Loldinc (the control: it must differ from
           2^k - 2; REFEREE 37 reports 3 for k = 3..10); member = [its br is a bijection onto 0..M-1]
  olddec   the old gloss with ties by decreasing beta-id: Lolddec (REFEREE 37 reports 1)
  oldfires = [Loldinc != 2^k - 2] + [Lolddec != 2^k - 2]  (must be 2: the old wording describes another genome)
Usage: b6gloss.py k [k ...]"""
import sys, re
import gk, onep


def table(name, k):
    """(Xi-depth, (local delta of option 0, of option 1)) of a mover, from the packet's table"""
    m = re.match(r"([a-z]+)(\d+)$", name)
    kind, j = m.group(1), int(m.group(2))
    if kind == "u":
        return (0, (2, 0)) if j == 0 else (2 * j, (1, 0))
    if kind == "v":
        return (0, (1, 3)) if j == 0 else (2 * j, (3, 2))
    if kind == "e":
        return 2 * j + 1, (4, 5)
    if kind == "wv":
        return 2 * k + 5, (1, 0)
    if kind == "wu":
        return 2 * k + 5, (3, 2)
    if kind == "y":
        return 2 * j - 1, (1, 3)
    if kind == "yb":
        return 2 * j - 1, (0, 2)
    if kind == "yp":
        return 2 * j, (5, 7)
    if kind == "ypb":
        return 2 * j, (4, 6)
    raise SystemExit("b6gloss: unknown mover " + name)


def ranks(G, names, k, variant):
    key = {}
    for x, n in enumerate(names):
        dep, dl = table(n, k)
        if variant == "wire0" and n.startswith("w"):
            dep = 0
        for o in range(2):
            b = G["opts"][x][o][2]
            if variant in ("rule", "wire0"):
                key[b] = (-dep, dl[o], b)
            elif variant == "oldinc":
                key[b] = (-dep, b)
            else:
                key[b] = (-dep, -b)
    order = sorted(key, key=lambda b: key[b])
    br = [0] * len(order)
    for r, b in enumerate(order):
        br[b] = r
    return br


def one(k):
    G, names = gk.build(k)
    exp = 2 ** k - 2
    out = {}
    for v in ("rule", "wire0", "oldinc", "olddec"):
        H = dict(G)
        H["br"] = ranks(G, names, k, v)
        out[v] = (len(onep.OneP(H).run("key")) - 1, H["br"])
    rulediff = int(out["rule"][1] != G["br"])
    member = int(sorted(out["oldinc"][1]) == list(range(2 * G["N"])))
    fires = int(out["oldinc"][0] != exp) + int(out["olddec"][0] != exp)
    print(f"G_{k} mode gloss N {G['N']} expected {exp} rulediff {rulediff} Lrule {out['rule'][0]} Ldiff {int(out['rule'][0] != exp)} "
          f"Lwire0 {out['wire0'][0]} wire0diff {int(out['wire0'][0] != exp)} Loldinc {out['oldinc'][0]} Lolddec {out['olddec'][0]} "
          f"member {member} oldfires {fires}", flush=True)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    for a in sys.argv[1:]:
        one(int(a))
