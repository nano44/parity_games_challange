#!/usr/bin/env python3
"""L-RED successor 22: the READER construction against CONJECTURE UL_C (docs/si/N5-GCX-box21.md §4). A class S of constant size 8 (cycle node
c_s) whose three Odd gates u1, u2, u3 have tau into a second class B (cycle node b, better for Even than c_s; Odd's best reply sigma-bar
closes the cycle c_s <-> u1 instead). tau is Odd-OPTIMAL (Even's best reply to tau runs c_s -> q -> v_0 -> ... -> G), so I_tau is empty
and tau never moves. B holds a Bellman-Ford chain v_0 .. v_L (wave from G back to v_0, one switch per step). In S:
- z's Xi-better edge to r2 (-> u3, tau(u3) = v_1) is W-trapped while W(p2) > W(v_1); the wave reaches v_1 at state L, z switches at L -> L+1;
- (y, z) is FORBIDDEN while W(z) (via p2) > W(a) (via c_s, u1, p1) and Xi(z) <= Xi(a); z's switch raises Xi(z) above Xi(a) and y takes the
  edge at L+1 -> L+2: a U event at index L+1 of S's C-interval [0, ...] (A_S empty, D cap S = {u1, u2, u3} constant), |S| = 8.
- c_s's Xi-improving edge to q (class b) is W-trapped by W(p1) > W(q) until q joins the wave (q -> v_0 at L+1 -> L+2); c_s leaves S at
  L+2 -> L+3, ending the phase after the U event.
Usage: mkreader.py L OUT.pg   (writes OUT.pg and OUT.start; ranks are set by distinct priorities)"""
import sys

def build(L):
    V = {}; order = []
    def add(name, owner): V[name] = [len(V), owner, []]; order.append(name)
    low = []                                              # weight-0 vertices (ranks below c_s): chain, gates, z, y
    for i in range(L + 1): add("v%d" % i, 0); low.append("v%d" % i)
    for nm, ow in (("u1", 1), ("u2", 1), ("u3", 1), ("z", 0), ("y", 0)): add(nm, ow); low.append(nm)
    mid = ["c_s", "a", "r2", "b"]                          # even, increasing rank: c_s < a < r2 < b
    for nm in mid: add(nm, 0)
    high = ["o%d" % i for i in range(L, -1, -1)] + ["ql", "q", "p1", "p2", "G"]   # even, increasing rank above b
    for nm in high: add(nm, 0)
    E = {}
    for i in range(L): E["v%d" % i] = ["o%d" % i, "v%d" % (i + 1)]
    E["v%d" % L] = ["o%d" % L, "G"]
    for i in range(L + 1): E["o%d" % i] = ["b"]
    E.update({"ql": ["b"], "q": ["ql", "v0"], "p1": ["b"], "p2": ["b"], "G": ["b"], "b": ["b"],
              "c_s": ["u1", "q"], "u1": ["c_s", "p1"], "a": ["c_s"], "y": ["a", "z"], "z": ["u2", "r2"], "u2": ["c_s", "p2"],
              "r2": ["u3"], "u3": ["c_s", "v1"]})
    prio = {}; p = 0
    for nm in low: prio[nm] = p; p += 1                    # low priorities: any parity (weight 0 relative to c_s and b)
    p += p % 2
    for nm in mid + high: prio[nm] = p; p += 2             # even, strictly increasing
    sigma = {"v%d" % i: "o%d" % i for i in range(L + 1)}
    sigma.update({"q": "ql", "c_s": "u1", "y": "a", "z": "u2"})
    tau = {"u1": "p1", "u2": "p2", "u3": "v1"}
    return V, order, E, prio, sigma, tau

def main():
    L = int(sys.argv[1]); out = sys.argv[2]
    V, order, E, prio, sigma, tau = build(L)
    idx = {nm: V[nm][0] for nm in order}
    with open(out, "w") as f:
        f.write("parity %d;\n" % (len(order) - 1))
        for nm in order:
            f.write("%d %d %d %s \"%s\";\n" % (idx[nm], prio[nm], V[nm][1], ",".join(str(idx[x]) for x in E[nm]), nm))
    st = out[:-3] + ".start"
    full_s = {nm: E[nm][0] for nm in order if V[nm][1] == 0}; full_s.update(sigma)
    full_t = {nm: E[nm][0] for nm in order if V[nm][1] == 1}; full_t.update(tau)
    with open(st, "w") as f:
        f.write("SIGMA0 " + " ".join("%d:%d" % (idx[a], idx[b]) for a, b in sorted(full_s.items(), key=lambda x: idx[x[0]])) + "\n")
        f.write("TAU0 " + " ".join("%d:%d" % (idx[a], idx[b]) for a, b in sorted(full_t.items(), key=lambda x: idx[x[0]])) + "\n")
    print(out, "n", len(order), {nm: idx[nm] for nm in ("c_s", "u1", "u2", "u3", "a", "y", "z", "r2", "b", "q", "v0", "v1", "G")})

if __name__ == "__main__":
    main()
