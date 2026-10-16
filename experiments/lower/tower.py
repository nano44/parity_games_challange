#!/usr/bin/env python3
"""Depth-forcing subset for two-player Büchi, n <= 4: depth-j types of ALL (game, vertex) pairs (as depth2.py), the
W-mixed type pairs first separated at depth j (M_j, one representative pair per pair of depth-j types), and the SAT test
of the subset of games realising M_jmin..M_6 at k gates (an UNSAT answer is a lower-bound certificate made of
depth-forcing games only).  Usage: tower.py k jmin [out.json]"""
import sys, os, time, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vec2
from sat2 import encode2
from coremin import struct_only


def build_nodes(n=4):
    lab, succ_nodes, meta, Ws = [], [], [], []
    base = 0
    for k in range(1, n + 1):
        S, ve, p2 = vec2.all_games(k); Wk = vec2.ref_W(S, ve, p2, k); M = len(S)
        node_id = base + np.arange(M * k, dtype=np.int64).reshape(M, k)
        lab_k = np.zeros((M, k), dtype=np.int32)
        sn = np.full((M, k, n), -1, dtype=np.int64)
        for v in range(k):
            lab_k[:, v] = (((p2 >> v) & 1).astype(np.int32)) | ((((ve >> v) & 1).astype(np.int32)) << 1)
            for w in range(k):
                has = ((S[:, v] >> w) & 1).astype(bool); sn[has, v, w] = node_id[has, w]
        lab.append(lab_k.ravel()); succ_nodes.append(sn.reshape(M * k, n)); meta.append((k, base, M)); base += M * k
        Ws.append(np.stack([((Wk >> v) & 1).astype(bool) for v in range(k)], 1).ravel())
    return np.concatenate(lab), np.concatenate(succ_nodes), np.concatenate(Ws), meta


def game_of(node, meta):
    for k, b, M in meta:
        if b <= node < b + M * k:
            gi, v = divmod(node - b, k)
            S, ve, p2 = vec2.all_games(k)   # cheap for k <= 4 (recomputed; fine)
            return vec2.game_at(S, ve, p2, gi, k), v
    raise ValueError(node)


if __name__ == "__main__":
    k = int(sys.argv[1]); jmin = int(sys.argv[2]); fout = sys.argv[3] if len(sys.argv) > 3 else f"tower_k{k}_j{jmin}.json"
    t0 = time.time(); lab, succ, W, meta = build_nodes(4); N = len(lab); print(f"nodes {N} [{time.time()-t0:.0f}s]", flush=True)
    cls = lab.astype(np.int32); levels = [cls]; D = 0
    while True:
        k_ = int(cls.max()) + 1
        cnt = np.bincount(cls, minlength=k_); wc = np.bincount(cls, weights=W, minlength=k_)
        mixed = np.nonzero((wc > 0) & (wc < cnt))[0]
        print(f"depth {D}: {k_} types, {len(mixed)} mixed [{time.time()-t0:.0f}s]", flush=True)
        if len(mixed) == 0: break
        slot = np.where(succ >= 0, cls[np.maximum(succ, 0)], -1).astype(np.int32)
        slot.sort(axis=1)
        dup = np.zeros_like(slot, dtype=bool); dup[:, 1:] = slot[:, 1:] == slot[:, :-1]; slot[dup] = -1; slot.sort(axis=1)
        sig = np.concatenate([cls[:, None], slot], axis=1)
        _, new = np.unique(sig, axis=0, return_inverse=True)
        cls = new.ravel().astype(np.int32); levels.append(cls); D += 1
    del slot, sig, succ
    # M_j: pairs of depth-j types (winning type, losing type) inside one depth-(j-1) type
    games = {}; counts = {}
    for j in range(1, D + 1):
        prev, cur = levels[j - 1], levels[j]
        # for each depth-j type: its depth-(j-1) parent, whether all-winning or all-losing (types are W-pure iff j = D; else may be mixed)
        kj = int(cur.max()) + 1
        parent = np.zeros(kj, dtype=np.int64); parent[cur] = prev
        cnt = np.bincount(cur, minlength=kj); wc = np.bincount(cur, weights=W, minlength=kj)
        pure_win = wc == cnt; pure_lose = wc == 0
        # representatives: first node of each depth-j type
        first = np.full(kj, N, dtype=np.int64); np.minimum.at(first, cur, np.arange(N))
        # group types by parent; pairs (winning-pure type, losing-pure type) with same parent
        order = np.argsort(parent, kind="stable"); par_sorted = parent[order]
        starts = np.nonzero(np.r_[True, par_sorted[1:] != par_sorted[:-1]])[0]; ends = np.r_[starts[1:], len(order)]
        npairs = 0; sel = set()
        for a, b in zip(starts, ends):
            ts = order[a:b]
            wins = [t for t in ts if pure_win[t]]; loses = [t for t in ts if pure_lose[t]]
            if wins and loses:
                npairs += len(wins) * len(loses)
                for t in wins + loses: sel.add(int(first[t]))
        counts[j] = (npairs, len(sel))
        print(f"M_{j}: {npairs} (winning type, losing type) pairs inside one depth-{j-1} type; {len(sel)} representative nodes", flush=True)
        if j >= jmin:
            for node in sel:
                g, v = game_of(node, meta); games[g] = games.get(g, 0) + 1
    games = sorted(games)
    print(f"subset: {len(games)} games realising M_{jmin}..M_{D}", flush=True)
    S, Wc = struct_only(games)
    t1 = time.time(); solver, decode, ncl = encode2(S, Wc, list(range(S.N)), k); ok = solver.solve()
    print(f"SAT at k={k} on this subset ({S.N} nodes, {ncl} clauses): {'SAT' if ok else 'UNSAT'} [{time.time()-t1:.1f}s]", flush=True)
    json.dump({"k": k, "jmin": jmin, "result": "SAT" if ok else "UNSAT", "counts": counts, "games": games}, open(fout, "w"))
