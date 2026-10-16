#!/usr/bin/env python3
"""Generic gate relabelling (L-RED; docs/red/R1-MSF.md section B): given a sink parity game and a designer LABEL for every
Even edge, route every Even choice through a Friedmann simple cycle (1106.0778 section 6.1) so that, for any single-switch
rule that ranks improving edges by the position of the first valuation difference (MSF: highest first; LSF: lowest first),
the switch of the underlying edge (v, w) gets the level of its gate = its label, while sign and effect stay the underlying
ones.  Vertex v (Even, out-degree >= 2) becomes a relay v -> d_v; d_v (Even, priority 3) -> e_{v,w} for each old successor w;
e_{v,w} (Odd, even priority 2*label+2) -> {d_v, w}.  Underlying priorities are shifted by C = 2*maxlabel + 4 (parities kept).
Requires: the input is a sink game whose Odd vertex 0 is the sink of priority 1 with a self-loop (unique minimum).
Labels: a dict (v, w) -> positive int, distinct.  Even vertices with one successor are left alone.
Demo (python3 gate.py N): DLMM G_N with labels = Bland numbers reversed (highest label = lowest Bland number) reproduces
gens_red.gated_bland N up to vertex numbering and MSF takes 2^N-1 switches; with labels = Bland numbers, LSF takes 2^N-1."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import vj


def gate(prio, owner, succ, labels):
    n = len(prio); L = max(labels.values()); C = 2 * L + 4
    assert prio[0] == 1 and owner[0] == 1 and succ[0] == [0] and all(p > 1 for p in prio[1:]), "not a sink game with sink 0"
    assert len(set(labels.values())) == len(labels), "labels must be distinct"
    P = [p + C if v else 1 for v, p in enumerate(prio)]; O = list(owner); S = [list(s) for s in succ]
    names = [f"v{v}" for v in range(n)]
    for v in range(n):
        if owner[v] == 0 and len(succ[v]) >= 2:
            d = len(P); P.append(3); O.append(0); S.append([]); names.append(f"d{v}")
            for w in succ[v]:
                e = len(P); P.append(2 * labels[(v, w)] + 2); O.append(1); S.append([d, w]); names.append(f"e{v}_{w}")
                S[d].append(e)
            S[v] = [d]
    return P, O, S, names


def dumps(P, O, S, names):
    return f"parity {len(P) - 1};\n" + "".join(f"{v} {P[v]} {O[v]} {','.join(map(str, S[v]))} \"{names[v]}\";\n" for v in range(len(P)))


def dlmm_G(N):
    sink = 0; A = lambda i: sink if i == N + 1 else 2 * i - 1; B = lambda i: 2 * N + 1 if i == N + 1 else 2 * i
    prio = [1]; owner = [1]; succ = [[0]]; bland = {}
    for i in range(1, N + 1):
        prio += [2 * i + 1, 2 * i + 2]; owner += [0, 1]; succ += [[A(i + 1), B(i + 1)], [A(i + 1), B(i + 1)]]
        bland[(A(i), B(i + 1))] = 2 * i; bland[(A(i), A(i + 1))] = 2 * i - 1
    prio.append(2 * N + 4); owner.append(1); succ.append([sink])
    return prio, owner, succ, bland


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    prio, owner, succ, bland = dlmm_G(N)
    for rule, lab in (("msf", {k: 2 * N + 1 - b for k, b in bland.items()}), ("lsf", dict(bland))):
        P, O, S, names = gate(prio, owner, succ, lab)
        e = vj.VJ(P, O, S)
        # start: the gate of sigma_0 (a_i -> a_{i+1}), given explicitly (best-reward would pick the higher label)
        start = list(e.initial("first"))
        for v in range(len(prio)):
            if owner[v] == 0 and len(succ[v]) >= 2:
                d = S[v][0]; start[d] = next(x for x in S[d] if S[x][1] == succ[v][0])
        _, it, st = e.run(rule, tuple(start))
        print(f"{rule} on gate(G_{N}, labels {'reversed Bland' if rule == 'msf' else 'Bland'}): n={len(P)} switches={it} "
              f"(2^N-1 = {2 ** N - 1}), escapes={st['escape']}")
