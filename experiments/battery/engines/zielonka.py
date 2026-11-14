#!/usr/bin/env python3
"""Second engine and worked example: the recursive algorithm (McNaughton / Zielonka), self-contained, with strategies.
Usage: zielonka.py GAME.pg -> one JSON line. iterations = recursive calls on a non-empty subgame; steps = edges scanned by attractors."""
import sys, json, threading
sys.setrecursionlimit(10 ** 6); threading.stack_size(512 * 1024 * 1024)
pr, ow, succ = {}, {}, {}
for line in open(sys.argv[-1]):
    p = line.strip().rstrip(";").split()
    if len(p) >= 4 and p[0].isdigit(): v = int(p[0]); pr[v], ow[v], succ[v] = int(p[1]), int(p[2]), [int(x) for x in p[3].split(",")]
pred = {v: [] for v in pr}
for v in succ:
    for w in set(succ[v]): pred[w].append(v)
calls = steps = 0

def attr(V, U, i, S):
    """Attractor of U for player i inside V; S gets i's attracting moves."""
    global steps
    A = set(U); todo = list(U); out = {}
    while todo:
        w = todo.pop()
        for v in pred[w]:
            steps += 1
            if v not in V or v in A: continue
            if ow[v] == i: S[v] = w
            else:
                out[v] = out.get(v, sum(1 for x in set(succ[v]) if x in V)) - 1
                if out[v] > 0: continue
            A.add(v); todo.append(v)
    return A

def solve(V):
    """(W0, W1, S): the regions of the subgame V and a winning positional strategy S for each winner on its region."""
    global calls
    if not V: return set(), set(), {}
    calls += 1
    p = max(pr[v] for v in V); i = p % 2; U = {v for v in V if pr[v] == p}; S = {}
    A = attr(V, U, i, S); W = solve(V - A)
    if not W[1 - i]:
        S.update(W[2])
        for v in U:
            if ow[v] == i: S[v] = next(w for w in succ[v] if w in V)
        return (V, set(), S) if i == 0 else (set(), V, S)
    S = {v: w for v, w in W[2].items() if v in W[1 - i]}
    B = attr(V, W[1 - i], 1 - i, S); X = solve(V - B)
    S.update(X[2]); R = [X[0], X[1]]; R[1 - i] = R[1 - i] | B
    return R[0], R[1], S

def main():
    W0, W1, S = solve(set(pr))
    print(json.dumps({"winner": [0 if v in W0 else 1 for v in range(len(pr))], "strategy": {str(v): w for v, w in S.items()}, "iterations": calls, "steps": steps}))

t = threading.Thread(target=main); t.start(); t.join()
