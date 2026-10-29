#!/usr/bin/env python3
"""L-SI box 25 (successor 21): DATA check of Theorem STATIC-DEPTH' (docs/si/N5-PIECE-box25.md §2), the two-frame form of RESULTS R77 (c).
Piece [a, b] (sigma-bar constant, fallback-free, in-phase; piece/pieceh.py). T_W / T_H := vertices on W-cycles / honest cycles at b.
(H3') every W-cycle at b is a W-cycle at every state of [a, b], every honest cycle at b an honest cycle at every state (vertex sequences,
rotation-normalised). Depths: dW(v) = 0 on T_W, dH(v) = 0 on T_H; Odd v: dW = dW(tau v), dH = dH(sigma-bar v); Even v in T_H \\ T_W:
dW = dW(sigma_b v); Even v in T_W \\ T_H: dH = dH(sigma_b v); Even v outside T_W u T_H: dW = dH = 1 + max(dW(y), dH(y)), y = sigma_b(v).
(H4') this recursion is well founded (the graph J_b acyclic). Claims checked when (H3') and (H4') hold:
  SET_V  some v whose W-play at a state of [a + dW(v), b] or honest play at a state of [a + dH(v), b] differs from that at b;
  LEN_V  b - a > max dW (the theorem's length bound);  N1_V b - a > n - 1.
GEN_W failures are counted (not excluded). MUT=1 uses d - 1 in place of d (must bite). Usage: sdprime.py --list FILE | --one GAME [START] | --rand COUNT NLO NHI SEED"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart
from staticdepth import walk
from pieceh import pieces, cyc
C = Counter(); EX = []; MUT = os.environ.get("MUT") == "1"

def depths(g, B, TW, TH):
    n = g.n; memo = {}; st = {}
    def d(v, fr):                                     # fr: "W" or "H"
        T = TW if fr == "W" else TH
        if v in T: return 0
        k = (v, fr)
        if k in memo: return memo[k]
        if st.get(k) == 1: raise ValueError("cycle")
        st[k] = 1
        if g.owner[v] == 1: r = d(B["t"][v] if fr == "W" else B["sb"][v], fr)
        elif v in TW or v in TH: r = d(B["s"][v], fr)          # v in the other frame's terminals: sigma constant, no step
        else: y = B["s"][v]; r = 1 + max(d(y, "W"), d(y, "H"))
        st[k] = 2; memo[k] = r; return r
    return {v: d(v, "W") for v in range(n)}, {v: d(v, "H") for v in range(n)}

def run(g, name, start=None):
    E, R = rows(g, start); n = g.n
    for a, b in pieces(R):
        ln = b - a; B = R[b]; C["pieces"] += 1
        cwb, chb = cyc(B["wn"], n), cyc(B["nxt"], n)
        h3p = all(cwb <= cyc(R[t]["wn"], n) and chb <= cyc(R[t]["nxt"], n) for t in range(a, b + 1))
        if not h3p: C["h3p_fail"] += 1; EX.append(("H3P", name, a, b, ln, n)); continue
        TW = {v for c in cwb for v in c}; TH = {v for c in chb for v in c}
        try: dW, dH = depths(g, B, TW, TH)
        except (ValueError, RecursionError): C["h4p_fail"] += 1; EX.append(("H4P", name, a, b, ln, n)); continue
        C["checked"] += 1; dm = max(list(dW.values()) + list(dH.values()))
        if cyc(B["wn"], n) != cyc(B["nxt"], n) or any(cyc(R[t]["wn"], n) != cwb or cyc(R[t]["nxt"], n) != chb for t in range(a, b + 1)):
            C["checked_beyond_H3"] += 1; C["beyond_len_max"] = max(C["beyond_len_max"], ln)
        if ln > dm: C["LEN_V"] += 1; EX.append(("LEN", name, a, b, ln, dm))
        if ln > n - 1: C["N1_V"] += 1
        if ln == dm: C["tight"] += 1
        seen = {}; gf = 0
        for t in range(a, b + 1):
            for v in range(n):
                if seen.setdefault((v, R[t]["W"][v]), walk(R[t]["wn"], v)[0]) != walk(R[t]["wn"], v)[0]: gf += 1
        C["genw_fail"] += gf; C["genw_fail_pieces"] += gf > 0
        for v in range(n):
            fw, fh = walk(B["wn"], v), walk(B["nxt"], v)
            for t in range(a + max(dW[v] - MUT, 0), b + 1):
                if walk(R[t]["wn"], v) != fw: C["SET_V"] += 1; EX.append(("SETW", name, a, b, v, t, dW[v])); break
            for t in range(a + max(dH[v] - MUT, 0), b + 1):
                if walk(R[t]["nxt"], v) != fh: C["SET_V"] += 1; EX.append(("SETH", name, a, b, v, t, dH[v])); break

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    elif a[0] == "--rand":                            # random C^kO games as root/staticdepth.py --rand (box43 multi.rand_ckO)
        import random
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box43")); from multi import rand_ckO
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); q = 0
        while q < cnt:
            g = rand_ckO(rng, lo, hi, rng.choice((2, 2, 3, 4)))
            if g is None: continue
            q += 1
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})
            run(g, f"rand seed {seed} #{q}", None if q % 2 else st)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            f = line.split()[0] if line.strip() and not line.startswith("#") else None
            if f: run(load(os.path.join(ROOT, f)), f)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in EX[:12]: print("EXAMPLE", x)
    print("SDPRIME PASS" if not any(k in C for k in ("SET_V", "LEN_V", "N1_V")) else "SDPRIME FAIL")

if __name__ == "__main__":
    main()
