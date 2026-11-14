#!/usr/bin/env python3
"""Per-step trace on an L^R_d genome: state, c_l (KP of level l), pair-order bit o_l (0 iff mover 2l has the smaller key),
pi(x) (Xi-preferred option), values. Usage: trace.py genome.json [start]"""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sim import load, val, run, moves

def keys(G, s):
    N = G["N"]; key = [None] * N
    for x in sorted(range(N), key=lambda v: G["lev"][v]):
        wt = G["opts"][x][s[x]][0]; key[x] = (key[wt] if wt >= 0 else ()) + (G["gate"][x][s[x]],)
    return key

def info(G, s):
    N = G["N"]; d = N // 2; key = keys(G, s)
    o = [0 if key[2 * l] < key[2 * l + 1] else 1 for l in range(d)]   # o_l: index (0/1 within pair) of key-smaller mover
    c = [None] + o[:-1]                                                 # c_l = o_(l-1)
    pi = [max(range(2), key=lambda k: val(G, s, x, k)) for x in range(N)]
    return o, c, pi

if __name__ == "__main__":
    G = load(sys.argv[1]); N = G["N"]; d = N // 2
    s0 = [int(ch) for ch in sys.argv[2]] if len(sys.argv) > 2 else G["start"]
    S = run(G, s0)
    print("lev pairs: " + " ".join(f"[{2*l}{2*l+1}]" for l in range(d)))
    for t, s in enumerate(S):
        o, c, pi = info(G, s)
        mv = "".join("*" if t and S[t][x] != S[t-1][x] else "." for x in range(N))
        print(f"{t:3d} s={' '.join(f'{s[2*l]}{s[2*l+1]}' for l in range(d))}  mv={' '.join(mv[2*l:2*l+2] for l in range(d))}"
              f"  o={''.join(map(str,o))}  pi={' '.join(f'{pi[2*l]}{pi[2*l+1]}' for l in range(d))}")
    print("moves", moves(S, N))
