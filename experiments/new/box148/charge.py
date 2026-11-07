#!/usr/bin/env python3
"""L-NEW box 148 CHARGE: the briefed charge «each unchained step with RANK > k consumes a key change of a mover strictly above y_t».
Definitions (box 147 stat.py features, deg 2): y_t = max-pi mover of step t; RANK_t = 1 + #(unstable at s_(t-1), pi > pi(y_t));
FROZ_t = the unstable movers above y_t (they do not move at t: box 147 DECREMENT); KP(m) at s = key-preferred option under the keys of s;
a KEY FLIP of m at step t' means KP(m) at s_(t'-1) != KP(m) at s_(t'). For each k, the high steps H_k = {unchained t : RANK_t > k}, in
order; window(t) = (previous step of H_k, t] (from step 1 for the first).
  NOFLIP_ABOVE: t in H_k with no key flip of ANY mover above y_t in window(t)  (briefed charge fails at t);
  NOFLIP_FROZ : t in H_k with no key flip of any m in FROZ_t in window(t)    (charge to a frozen mover fails at t).
The windows are disjoint, so where both counts are 0 the charge is injective: |H_k| <= number of key flips of movers above.
Also: SAMETOP = max number of H_k steps inside one interval on which TOP_k (box 147) is constant; CARRIES = number of (level, step)
with L_l flipped (2-wide ladder: L_l = key-smaller of u_l, v_l); KFLIPS = total key flips. Usage: charge.py genome.json ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(HERE, "..", "box147", "stat.py")
ns = {"__file__": os.path.abspath(P)}; exec(open(P).read().split('\nif __name__')[0], ns); analyse = ns["analyse"]
def info(G, R):
    S, FS, pos, lab = R["S"], R["FS"], R["pos"], R["lab"]; n = G["N"]; T = len(S) - 1; d = n // 2
    y = {}; rank = {}; froz = {}
    for t in range(1, T + 1):
        y[t] = max((x for x in range(n) if S[t][x] != S[t - 1][x]), key=lambda x: pos[x])
        froz[t] = [x for x in range(n) if FS[t - 1]["UNST"][x] and pos[x] > pos[y[t]]]; rank[t] = 1 + len(froz[t])
    flip = {t: {m for m in range(n) if FS[t - 1]["KP"][m] != FS[t]["KP"][m]} for t in range(1, T + 1)}
    K = lambda s: FS[s]["key"]
    Lw = lambda s, l: 2 * l if K(s)[2 * l] < K(s)[2 * l + 1] else 2 * l + 1
    carries = sum(1 for t in range(1, T + 1) for l in range(d) if Lw(t, l) != Lw(t - 1, l))
    return y, rank, froz, flip, carries
def topk(FS, pos, s, k, n): return tuple(sorted((pos[x] for x in range(n) if FS[s]["UNST"][x]), reverse=True)[:k])
def analyse_k(G, R, k, y, rank, froz, flip):
    lab, pos, FS = R["lab"], R["pos"], R["FS"]; n = G["N"]
    H = [t for t in sorted(lab) if not lab[t] and rank[t] > k]; na = nf = 0; prev = 0; ex = None
    for t in H:
        win = range(prev + 1, t + 1)
        above = any(pos[m] > pos[y[t]] for u in win for m in flip[u]); fz = any(m in froz[t] for u in win for m in flip[u])
        na += not above; nf += not fz
        if not fz and ex is None: ex = t
        prev = t
    same = {}; 
    for t in H: same[topk(FS, pos, t - 1, k, n)] = same.get(topk(FS, pos, t - 1, k, n), 0) + 1  # TOP_k is constant between its falls; key by value
    return len(H), na, nf, max(same.values(), default=0), ex
if __name__ == "__main__":
    tot = {}
    for p in sys.argv[1:]:
        G = json.load(open(p)); R = analyse(G); y, rank, froz, flip, car = info(G, R)
        kf = sum(len(v) for v in flip.values()); U = sum(1 for c in R["lab"].values() if not c); out = []
        for k in (0, 1, 2, 3):
            h, na, nf, same, ex = analyse_k(G, R, k, y, rank, froz, flip); out.append(f"k{k}: H {h} NOFLIP_ABOVE {na} NOFLIP_FROZ {nf} SAMETOP {same} FIRSTFAIL {ex}")
            a = tot.setdefault(k, [0, 0, 0]); a[0] += h; a[1] += na; a[2] += nf
        print(f"CHARGE {os.path.basename(p)} N {G['N']} STEPS {R['T']} U {U} CARRIES {car} KFLIPS {kf} | " + " | ".join(out), flush=True)
    print("TOTAL " + " | ".join(f"k{k}: H {v[0]} NOFLIP_ABOVE {v[1]} NOFLIP_FROZ {v[2]}" for k, v in tot.items()))
