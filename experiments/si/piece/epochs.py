#!/usr/bin/env python3
"""L-SI box 25 (successor 21): DATA for Corollary EPOCH (docs/si/N5-PIECE-box25.md §3). Each piece [a, b] (piece/pieceh.py) is cut from
the end into EPOCHS: [a_k, b_k] with b_k = b, a_k the least state from which every cycle (W and honest) of state b_k is a cycle of its frame
at every state of [a_k, b_k]; then b_(k-1) = a_k - 1, and so on. Prints per game: pieces, epochs, the largest epoch count of a piece, CF
(transitions of a piece at which a W- or honest cycle appears that is not a cycle at the state before), epochs with (H4') failing, the
longest epoch and max (epoch length - its max d), which Theorem STATIC-DEPTH' says is <= 0 when (H4') holds and GEN_W holds.
Usage: epochs.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart
from pieceh import pieces, cyc
from sdprime import depths
C = Counter(); EX = []

def run(g, name, start=None):
    E, R = rows(g, start); n = g.n
    CW = [cyc(r["wn"], n) for r in R]; CH = [cyc(r["nxt"], n) for r in R]
    for a, b in pieces(R):
        C["pieces"] += 1; k = 0; e = b
        cf = sum(1 for t in range(a, b) if not CW[t + 1] <= CW[t] or not CH[t + 1] <= CH[t])
        C["cf_max"] = max(C["cf_max"], cf)
        while e >= a:
            s = e
            while s > a and CW[e] <= CW[s - 1] and CH[e] <= CH[s - 1]: s -= 1
            k += 1; C["epochs"] += 1; C["epoch_len_max"] = max(C["epoch_len_max"], e - s)
            B = R[e]
            try:
                dW, dH = depths(g, B, {v for c in CW[e] for v in c}, {v for c in CH[e] for v in c})
                dm = max(list(dW.values()) + list(dH.values()))
                C["slack_min_plus1000"] = min(C.get("slack_min_plus1000", 10 ** 6), 1000 + dm - (e - s))
                if e - s > dm: C["EPOCH_V"] += 1; EX.append((name, s, e, dm))
            except (ValueError, RecursionError): C["epoch_h4p_fail"] += 1
            e = s - 1
        C["k_max"] = max(C["k_max"], k)
        if k > 1: C["pieces_multi_epoch"] += 1; C["multi_len_max"] = max(C["multi_len_max"], b - a)
        if k - 1 > cf: C["K_GT_CF_V"] += 1

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            f = line.split()[0] if line.strip() and not line.startswith("#") else None
            if f: run(load(os.path.join(ROOT, f)), f)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in EX[:6]: print("EXAMPLE", x)
    print("EPOCHS PASS" if not any(k in C for k in ("EPOCH_V", "K_GT_CF_V")) else "EPOCHS FAIL")

if __name__ == "__main__":
    main()
