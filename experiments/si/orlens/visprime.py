#!/usr/bin/env python3
"""Check Lemma VIS' (docs/si/N5-OR-lens-box2.md §2): after exit e = sbar_k(o) enters R with loop L (top new vertex t), any later
state j of the same joint lambda-phase (tau fixed, (h) at k, k+1, j) with sbar_j(o) = e has top(P(theta_k) xor P(theta_j)) at
least as relevant as t.  Counts checks and violations."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT
from thclass import hstate
def run(path, start=None):
    g, st = OT.load(path, start)
    E, Ed, states, fbf, _ = OT.run_states(g, st)
    n = g.n; o = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1][0]
    def path_to_o(sig, tau, v):
        seen = []; x = v
        while x not in seen:
            if x == o: return seen
            seen.append(x); x = sig[x] if g.owner[x] == 0 else tau[x]
        return None
    chk = viol = 0
    for ph in OT.phases(E, Ed, states):
        H = [hstate(g, E, states[k], o) for k in ph]
        for i in range(len(ph) - 1):
            s0, s1 = states[ph[i]], states[ph[i + 1]]
            if not (H[i] and H[i + 1]): continue
            e = s0[3][o]
            if path_to_o(s0[0], s0[1], e) is not None: continue
            p = path_to_o(s1[0], s1[1], e)
            if p is None: continue
            c = s0[2][o][0]; Pa = s0[2][e][1]
            new = [E.rank[x] for x in p + [o] if E.rank[x] > E.rank[c] and not (Pa >> E.rank[x]) & 1]
            t = max(new) if new else None
            for j in range(i + 2, len(ph)):
                sj = states[ph[j]]
                if not H[j] or sj[3][o] != e or sj[1] != s0[1]: continue
                chk += 1
                dd = s0[2][o][1] ^ sj[2][o][1]
                v = dd.bit_length() - 1 if dd else None
                if t is not None and (v is None or v < t): viol += 1
    return chk, viol
if __name__ == "__main__":
    for spec in sys.argv[1:]:
        p, _, s = spec.partition(":")
        print(os.path.basename(p), run(p, s or None), flush=True)
