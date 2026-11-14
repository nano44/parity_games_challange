#!/usr/bin/env python3
"""L-SI box 106, layer 1 (exact, no valuation): the KEY rule on the depth-2 ladder (box 105 ladder105.py / RESULTS R110 shape: movers 0, 1
on level 0, movers 2, 3 on level 1, degree 2, option k of a level-1 mover W-points to mover k) with ADVERSARIAL availability: at a state
s every mover x has A(x) = {s(x)} or {0, 1}, chosen freely (the values decide this in KEY(G*); here nothing does). Keys (box 105 §1):
key(x, k) = gate(x, k) on level 0; key(x, k) = (gate(k, s'(k)), gate(x, k)) on level 1, s' the NEW level-0 choices. The two first
entries of a level-1 mover's options are gates of different level-0 movers, so they always differ: only the order of the four level-0
gates matters (24 orders), and movers 2 and 3 rank their options the same way. A step moves x to the key-least element of A(x),
level 0 first. No state repeats (KEY-MONO*), so runs are paths in a DAG on the 16 states.
For every gate order (24) and start (16) the tool enumerates EVERY path of non-trivial steps from the start, and records, per step and
mover, the availability the step needs: «A» (the mover moves: its other option must be available), «N» (it stays although its other
option is key-less under s': the other option must NOT be available), «-» (it stays and its other option is key-larger: free).
Output: the maximum length over all (order, start) and the number of paths of each length >= MINLEN, with each path of length >= MINLEN
written as one line «SKEL106 order O start S states ... need ...» (O = the level-0 gates' ranks in the order (0,0) (0,1) (1,0) (1,1)).
Usage: skel106.py MINLEN [OUT.txt]"""
import sys, itertools
MOV = range(4)

def step(s, a, g):
    """s: state (4 options), a: availability bits, g: gate rank of (x, k) for x in {0, 1}. Returns s'."""
    t = list(s)
    for x in (0, 1):
        o = 1 - s[x]
        if a[x] and g[(x, o)] < g[(x, s[x])]: t[x] = o
    pref = 0 if g[(0, t[0])] < g[(1, t[1])] else 1          # the key-least option of a level-1 mover under s'
    for x in (2, 3):
        if a[x] and s[x] != pref: t[x] = pref
    return tuple(t)

def need(s, t, g):
    r = []
    for x in (0, 1):
        o = 1 - s[x]
        r.append("A" if t[x] != s[x] else ("N" if g[(x, o)] < g[(x, s[x])] else "-"))
    pref = 0 if g[(0, t[0])] < g[(1, t[1])] else 1
    for x in (2, 3):
        r.append("A" if t[x] != s[x] else ("N" if s[x] != pref else "-"))
    return "".join(r)

def main():
    minlen = int(sys.argv[1]); out = open(sys.argv[2], "w") if len(sys.argv) > 2 else None
    hist = {}; best = 0; nlines = 0
    for perm in itertools.permutations(range(4)):
        g = {(0, 0): perm[0], (0, 1): perm[1], (1, 0): perm[2], (1, 1): perm[3]}
        succ = {}
        for s in itertools.product((0, 1), repeat=4):
            succ[s] = sorted({step(s, a, g) for a in itertools.product((0, 1), repeat=4)} - {s})
        for s0 in itertools.product((0, 1), repeat=4):
            stack = [[s0]]
            while stack:
                p = stack.pop(); L = len(p) - 1
                hist[L] = hist.get(L, 0) + 1; best = max(best, L)
                if L >= minlen and out:
                    out.write("SKEL106 order %s start %s states %s need %s\n" % ("".join(map(str, perm)), "".join(map(str, s0)),
                              " ".join("".join(map(str, q)) for q in p), " ".join(need(p[i], p[i + 1], g) for i in range(L))))
                    nlines += 1
                for t in succ[p[-1]]:
                    assert t not in p, "state repeated: KEY-MONO* violated"
                    stack.append(p + [t])
    print("SKEL106 max length over 24 gate orders x 16 starts: %d | paths by length %s | lines written (length >= %d) %d"
          % (best, " ".join("%d:%d" % (k, hist[k]) for k in sorted(hist)), minlen, nlines))

if __name__ == "__main__":
    main()
