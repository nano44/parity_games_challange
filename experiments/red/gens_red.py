#!/usr/bin/env python3
"""L-RED adversarial families against L-SI's MSF (docs/red/R1-MSF.md).

gated_bland N   "Gate relabelling" of the Disser-Loho-Maat-Mosis Bland counter G_N (arXiv 2512.16684 v2, Fig. 4.1 / Lemma 4.4;
                L-SI's port experiments/si/gens.py dlmm_bland):
                  sink (Odd, 1, self-loop); a_i (Even, 2i+1), b_i (Odd, 2i+2), i = 1..N; a_i, b_i -> b_{i+1}, a_{i+1};
                  a_{N+1} = sink, b_{N+1} (Odd, 2N+4) -> sink.  Bland numbers: (a_i, b_{i+1}) = 2i, (a_i, a_{i+1}) = 2i - 1.
                Every choice of a_i is routed through a simple cycle in Friedmann's sense (arXiv 1106.0778 section 6.1,
                Lemma 6.1): a_i -> d_i (Even, priority 3) -> e_i^a, e_i^b (Odd, EVEN priorities); e_i^a -> {d_i, a_{i+1}},
                e_i^b -> {d_i, b_{i+1}}.  By Lemma 6.1 the switch d_i -> e is improving iff Odd currently loops e -> d_i,
                i.e. iff the exit of e beats d_i's current route; its MSF level is the priority of e (the only difference
                is {d_i, e}).  After the switch Odd escapes through the exit (even 2-cycle), so d_i's value becomes the
                exit's value: the gate relabels the LEVEL of an underlying switch without changing its EFFECT.
                Gate priorities decrease with the Bland number (e_i^a: 4N+6-4i, e_i^b: 4N+4-4i), so MSF's "highest level
                first" is Bland's "lowest number first".  The underlying priorities are shifted by C = 4N+4 so that every
                underlying comparison is decided above the gate junk.  PGSolver's best-reward start gives sigma_0 of
                Lemma 4.4 (d_i -> e_i^a, the higher even priority).
                Ids: sink 0; a_i = 5i-4, b_i = 5i-3, d_i = 5i-2, e_i^a = 5i-1, e_i^b = 5i (i = 1..N); b_{N+1} = 5N+1.
Usage: gens_red.py FAMILY N"""
import sys


def gated_bland(N):
    C = 4 * N + 4
    sink = 0
    A = lambda i: sink if i == N + 1 else 5 * i - 4
    B = lambda i: 5 * N + 1 if i == N + 1 else 5 * i - 3
    D = lambda i: 5 * i - 2
    EA = lambda i: 5 * i - 1
    EB = lambda i: 5 * i
    rows = [f"{sink} 1 1 {sink} \"sink\";"]
    for i in range(1, N + 1):
        rows.append(f"{A(i)} {2 * i + 1 + C} 0 {D(i)} \"a{i}\";")
        rows.append(f"{B(i)} {2 * i + 2 + C} 1 {A(i + 1)},{B(i + 1)} \"b{i}\";")
        rows.append(f"{D(i)} 3 0 {EA(i)},{EB(i)} \"d{i}\";")
        rows.append(f"{EA(i)} {4 * N + 6 - 4 * i} 1 {D(i)},{A(i + 1)} \"ea{i}\";")
        rows.append(f"{EB(i)} {4 * N + 4 - 4 * i} 1 {D(i)},{B(i + 1)} \"eb{i}\";")
    rows.append(f"{B(N + 1)} {2 * N + 4 + C} 1 {sink} \"b{N + 1}\";")
    return f"parity {5 * N + 1};\n" + "\n".join(rows) + "\n"


FAMILIES = {"gated_bland": gated_bland}
if __name__ == "__main__":
    sys.stdout.write(FAMILIES[sys.argv[1]](int(sys.argv[2])))
