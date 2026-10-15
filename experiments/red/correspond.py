#!/usr/bin/env python3
"""Switch-for-switch correspondence: MSF on gated_bland N (gens_red.py) versus Bland's rule on the plain DLMM counter G_N
(lowest Bland number first: (a_i, b_{i+1}) = 2i, (a_i, a_{i+1}) = 2i-1; DLMM 2512.16684 Fig. 4.1, Lemma 4.4).
Prints the two sequences as (level i, target 'a'|'b') and whether they are equal.  Usage: correspond.py N [N ...]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import vj, gens_red


def plain_bland(N):
    """G_N as in Fig. 4.1 (ids: sink 0, a_i = 2i-1, b_i = 2i, b_{N+1} = 2N+1), run with Bland's rule from sigma_0."""
    sink = 0; A = lambda i: sink if i == N + 1 else 2 * i - 1; B = lambda i: 2 * N + 1 if i == N + 1 else 2 * i
    prio = [1]; owner = [1]; succ = [[0]]
    for i in range(1, N + 1):
        prio += [2 * i + 1, 2 * i + 2]; owner += [0, 1]; succ += [[A(i + 1), B(i + 1)], [A(i + 1), B(i + 1)]]
    prio.append(2 * N + 4); owner.append(1); succ.append([sink])
    e = vj.VJ(prio, owner, succ)
    bland = {}
    for i in range(1, N + 1):
        bland[(A(i), B(i + 1))] = 2 * i; bland[(A(i), A(i + 1))] = 2 * i - 1
    sigma = tuple(-1 if owner[v] == 1 else A(i + 1) for v, i in [(v, (v + 1) // 2) for v in range(len(prio))])
    seq = []
    while True:
        val, tau = e.evaluate(sigma); imp = e.improving(sigma, val)
        if not imp:
            return seq
        v, w = min(imp, key=lambda vw: bland[vw])
        seq.append(((v + 1) // 2, "b" if w == B((v + 1) // 2 + 1) else "a"))
        s = list(sigma); s[v] = w; sigma = tuple(s)


def gated_msf(N):
    txt = gens_red.gated_bland(N); p = os.path.join(os.environ.get("TMPDIR", "/tmp"), f"gb_corr_{N}.pg")
    open(p, "w").write(txt); e = vj.VJ(*vj.read_pg(p)); os.unlink(p)
    seq = []
    e.run("msf", e.initial("best"), hook=lambda it, sg, val, tau, v, w, lv, c, ch: seq.append(((v + 2) // 5, "a" if w == v + 1 else "b")))
    return seq


ok = True
for N in map(int, sys.argv[1:] or ["2", "3", "4", "5", "6", "7", "8"]):
    a, b = plain_bland(N), gated_msf(N)
    print(f"N={N}: Bland on G_N {len(a)} switches, MSF on gated G'_N {len(b)} switches, sequences equal: {a == b}")
    if N <= 3:
        print("   ", a); print("   ", b)
    ok &= (a == b)
sys.exit(0 if ok else 1)
