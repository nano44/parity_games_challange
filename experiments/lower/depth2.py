#!/usr/bin/env python3
"""Minimal modal depth for two-player Büchi on <= 4 vertices: D-step bisimulation types of ALL (game, vertex) pairs of all
two-player Büchi games with <= 4 vertices (vectorized partition refinement, int32), and the smallest D with W constant on D-types.
Also prints the deepest fooling pair (a winning and a losing vertex with equal depth-(D-1) types)."""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vec2


def main(n=4):
    # nodes: for k = 1..n, each game g and vertex v -> node; labels (owner, p2); successors as class slots
    lab, succ_nodes, W, meta = [], [], [], []
    base = 0
    for k in range(1, n + 1):
        S, ve, p2 = vec2.all_games(k); Wk = vec2.ref_W(S, ve, p2, k)
        M = len(S)
        node_id = base + np.arange(M * k, dtype=np.int64).reshape(M, k)
        lab_k = np.zeros((M, k), dtype=np.int32)
        sn = np.full((M, k, n), -1, dtype=np.int64)
        for v in range(k):
            lab_k[:, v] = (((p2 >> v) & 1).astype(np.int32)) | ((((ve >> v) & 1).astype(np.int32)) << 1)
            for w in range(k):
                has = ((S[:, v] >> w) & 1).astype(bool)
                sn[has, v, w] = node_id[has, w]
            W.append(((Wk >> v) & 1).astype(bool))
        lab.append(lab_k.ravel()); succ_nodes.append(sn.reshape(M * k, n)); meta.append((k, base, M)); base += M * k
    lab = np.concatenate(lab); succ = np.concatenate(succ_nodes)
    W = np.concatenate([np.stack([W[i] for i in range(len(W))], 1).ravel()]) if False else None
    # rebuild W in node order (game-major, vertex-minor)
    Ws = []
    for k, b, M in meta:
        S, ve, p2 = vec2.all_games(k); Wk = vec2.ref_W(S, ve, p2, k)
        Ws.append(np.stack([((Wk >> v) & 1).astype(bool) for v in range(k)], 1).ravel())
    W = np.concatenate(Ws)
    N = len(lab); print(f"nodes {N}", flush=True)
    cls = lab.astype(np.int32); D = 0
    while True:
        k_ = int(cls.max()) + 1
        cnt = np.bincount(cls, minlength=k_); wc = np.bincount(cls, weights=W, minlength=k_)
        mixed = np.nonzero((wc > 0) & (wc < cnt))[0]
        print(f"depth {D}: {k_} types, {len(mixed)} mixed", flush=True)
        if len(mixed) == 0:
            print(f"RESULT: minimal depth for two-player Büchi, n <= {n}: {D}")
            return
        if D >= 2 * n:
            print("RESULT: no separation up to depth", D); return
        # fooling pair example for the current depth (first mixed type)
        if D == 2 * n - 3 or True:
            m = mixed[0]; members = np.nonzero(cls == m)[0]
            win = members[W[members]][:1]; lose = members[~W[members]][:1]
            print(f"   mixed type example at depth {D}: win node {int(win[0])}, lose node {int(lose[0])}")
        t0 = time.time()
        slot = np.where(succ >= 0, cls[np.maximum(succ, 0)], -1).astype(np.int32)
        slot.sort(axis=1)
        dup = np.zeros_like(slot, dtype=bool); dup[:, 1:] = slot[:, 1:] == slot[:, :-1]; slot[dup] = -1; slot.sort(axis=1)
        sig = np.concatenate([cls[:, None], slot], axis=1)
        _, new = np.unique(sig, axis=0, return_inverse=True)
        cls = new.ravel().astype(np.int32); D += 1
        print(f"   refined [{time.time()-t0:.0f}s]", flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 4)
