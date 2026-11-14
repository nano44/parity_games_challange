#!/usr/bin/env python3
"""L-RED R177 TBCHECK: the S4a tie-break among W-equal options (Lemma TB, docs/red/R177-tiebreak.md).
At every fallback-free transition j with I_sigma != {} and every Even mover h (o = sigma_(j-1)(h) -> w = sigma_j(h)), with
W_j := valuation of sigma_j in G with Odd fixed to tau_(j-1) (the arena's Odd strategy):
  FLAT  : W_j(w) == W_j(o) (equal (cycle node, path set, length));  CORNER: h on the sigma_j-play from o or from w, or h = cycle node.
Lemma TB predicts, for every FLAT non-corner move:
  ODD regime  (cycle node c of W_j(h) has odd priority; Odd's longest path in the dual): index(w) < index(o);
  EVEN regime (c even; BFS from c in the dual):  kappa_j(w) <lex kappa_j(o), kappa_j(x) = vertex indices of the sigma_j-play from x
               read backwards from c (c excluded), i.e. (x_(d-1), ..., x_1, x_0 = x) for the play x_0 -> ... -> x_d = c.
Prints TBCHECK <game> n K FLAT_ODD FLAT_EVEN VIOL_ODD VIOL_EVEN CORNER_FLAT FLTRANS (FL transitions: sigma changes, W_j = W_(j-1))
MAXFLRUN; and one line per violation.  Usage: tbcheck.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, start_pair, readstart, Engine, dual, step
import pg

def play(succ1, x):
    seq = [x]; seen = {x}; v = x
    while True:
        v = succ1[v]
        if v in seen: return seq, v
        seen.add(v); seq.append(v)

def main():
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
    n, own, pr = g.n, g.owner, g.prio
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st)
    C = dict(flat_odd=0, flat_even=0, viol_odd=0, viol_even=0, corner_flat=0, fltrans=0, maxflrun=0, K=0)
    run_ = 0; prevW = None; viols = []
    while True:
        r = step(g, E, Ed, list(s), list(t))
        if r is None: break
        ns, nt, Is, It, fb, _, _ = r; C["K"] += 1
        if fb or not Is:
            s, t = ns, nt; run_ = 0; prevW = None; continue
        Gt = pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [t[v]] for v in range(n)])
        EW = Engine(Gt)
        Wj = EW.evaluate(tuple(ns[v] if own[v] == 0 else -1 for v in range(n)))[0]
        Wp = EW.evaluate(tuple(s[v] if own[v] == 0 else -1 for v in range(n)))[0]
        succ1 = [ns[v] if own[v] == 0 else t[v] for v in range(n)]
        mv = [h for h in range(n) if own[h] == 0 and ns[h] != s[h]]
        if mv and Wj == Wp:
            C["fltrans"] += 1; run_ += 1; C["maxflrun"] = max(C["maxflrun"], run_)
        else:
            run_ = 0
        for h in mv:
            o, w = s[h], ns[h]
            if EW.key(Wj[o]) != EW.key(Wj[w]) or Wj[o] != Wj[w]: continue
            c = Wj[h][0]
            po, _ = play(succ1, o); pw, _ = play(succ1, w)
            if h in po or h in pw or h == c:
                C["corner_flat"] += 1; continue
            if pr[c] % 2 == 1:
                C["flat_odd"] += 1
                if not w < o: C["viol_odd"] += 1; viols.append(("ODD", C["K"], h, o, w))
            else:
                C["flat_even"] += 1
                def kap(x, p):
                    i = p.index(c); return tuple(reversed(p[:i]))
                ko, kw = kap(o, po), kap(w, pw)
                if not kw < ko: C["viol_even"] += 1; viols.append(("EVEN", C["K"], h, o, w, ko, kw))
        s, t = ns, nt
    nm = os.path.basename(sys.argv[1])
    print(f"TBCHECK {nm} n {n} " + " ".join(f"{k.upper()} {v}" for k, v in C.items()))
    for v in viols[:20]: print("TBVIOL", nm, *v)

if __name__ == "__main__":
    main()
