#!/usr/bin/env python3
"""Heuristic upper bounds: from a k-state separator (JSON automaton), try every merge of two states j -> i (all
transitions into j redirected to i; at letters where i and j disagree, each choice is tried, capped at 2^10), and
report every (k-1)-state result that the independent checker (check.py) accepts as a weak (n,d)-separator.
Usage: merge.py n d automaton.json [--depth 2]   (depth 2: also merge pairs in the merged automata)"""
import sys, os, json, itertools, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import graphs, check


def merges(delta):
    k = len(delta)
    for i in range(k):
        for j in range(i + 1, k):
            opts = []
            for a in range(len(delta[0])):
                xs = {delta[i][a], delta[j][a]}
                opts.append(sorted(xs, key=lambda x: (x is None, x)))
            combos = itertools.product(*opts)
            for cnt, row in enumerate(combos):
                if cnt >= 1024:
                    break
                ren = lambda x: None if x is None else (i if x == j else (x - 1 if x > j else x))
                nd = []
                for q in range(k):
                    if q == j:
                        continue
                    src = list(row) if q == i else delta[q]
                    nd.append([ren(x) for x in src])
                yield (i, j), nd


def reachable_part(delta):
    seen, st = {0}, [0]
    while st:
        q = st.pop()
        for x in delta[q]:
            if x is not None and x not in seen:
                seen.add(x); st.append(x)
    order = sorted(seen)
    idx = {q: n for n, q in enumerate(order)}
    return [[None if x is None else idx[x] for x in delta[q]] for q in order]


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int); ap.add_argument("d", type=int); ap.add_argument("aut")
    ap.add_argument("--depth", type=int, default=1)
    a = ap.parse_args()
    evens, odds = graphs.family(a.n, a.d, 0), graphs.family(a.n, a.d, 1)
    obj = json.load(open(a.aut))
    delta = obj["automaton"]["delta"] if "automaton" in obj else obj["delta"]
    level = [delta]
    for depth in range(1, a.depth + 1):
        found, seen = [], set()
        for dl in level:
            for pair, nd in merges(dl):
                nd = reachable_part(nd)
                key = json.dumps(nd)
                if key in seen:
                    continue
                seen.add(key)
                aut = {"k": len(nd), "d": a.d, "delta": nd}
                if not check.violations(aut, evens, odds, first=True):
                    found.append(nd)
        print(f"depth {depth}: {len(seen)} distinct merged automata tested, {len(found)} weak separators; "
              f"sizes {sorted({len(x) for x in found})}", flush=True)
        for x in found[:3]:
            print("  ", json.dumps(x))
        if not found:
            break
        level = found
