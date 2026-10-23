"""L-RED box 23 (produced on Opus 5.5): Friedmann's Random-Edge lower-bound PARITY game G_zeta, transcribed from O. Friedmann, PhD thesis,
LMU Munich 2011 (edoc.ub.uni-muenchen.de/13294, PDF sha256 68748f53...), §4.7.2, node sets p.185 (printed) and Table 4.19 "Edges and
Priorities of G_zeta" (printed p.185; L-LIT T26 cites p.184), Figure 4.24; parameters h = 8n, g = 22n, l_k = 25 k^2 n (T26 C6).
Player 0 (Even) = Friedmann's improver; player 1 = A_i, B_i. Max-parity priorities as in the table.
Every player-0 node of out-degree 2 lists its "0" edge FIRST (thesis §4.7.2 p.?: sigma(u) = 1 iff u moves into its level, i.e. not to
r, s, u_{i+1}, w_{i+1}, x_i), so a first-successor tau_1 is the all-0 start, which we read as Lemma 4.74's "sigma(w*) = sigma(s*) = 0"
(reading: the thesis does not spell out the other nodes). --order table lists successors in the table's printed order instead.
Usage: gzeta.py n [--order zero|table] > G.pg   (comments '%' carry node names)"""
import sys
n = int(sys.argv[1]); order = sys.argv[sys.argv.index("--order") + 1] if "--order" in sys.argv else "zero"
h, g = 8 * n, 22 * n; ell = {k: 25 * k * k * n for k in range(1, n + 1)}
ids, names = {}, []
def node(nm):
    if nm not in ids: ids[nm] = len(names); names.append(nm)
    return ids[nm]
E, P, O = {}, {}, {}
def add(nm, owner, prio, succ_zero_first, succ_table):
    v = node(nm); O[v] = owner; P[v] = prio; E[v] = succ_zero_first if order == "zero" else succ_table
add("t", 0, 1, ["t"], ["t"]); add(f"w{n+1}", 0, 2, ["t"], ["t"]); add(f"u{n+1}", 0, 2, ["t"], ["t"])
add("r", 0, 6, ["w1"], ["w1"]); add("s", 0, 2, ["u1"], ["u1"])
for i in range(1, n + 1):
    add(f"w{i}", 0, 2, [f"w{i+1}", f"A{i}"], [f"w{i+1}", f"A{i}"])
    add(f"u{i}", 0, 2, [f"u{i+1}", f"d{i}"], [f"u{i+1}", f"d{i}"])
    add(f"A{i}", 1, 4, [f"d{i}", f"a{i},{h}"], [f"d{i}", f"a{i},{h}"])
    add(f"a{i},1", 0, 3, [f"x{i}", f"A{i}"], [f"A{i}", f"x{i}"])
    for j in range(1, h): add(f"a{i},{j+1}", 0, 3, [f"x{i}", f"a{i},{j}"], [f"a{i},{j}", f"x{i}"])
    add(f"x{i}", 0, 4 * i + 3, ["s"], ["s"])
    add(f"d{i}", 0, 4 * i + 5, [f"B{i}"], [f"B{i}"])
    add(f"y{i}", 0, 4 * i + 6, [f"w{i+1}"], [f"w{i+1}"])
    add(f"B{i}", 1, 4, [f"y{i}", f"b{i},{ell[i]}", f"c{i},{g}"], [f"y{i}", f"b{i},{ell[i]}", f"c{i},{g}"])
    add(f"b{i},1", 0, 3, ["s", f"B{i}"], [f"B{i}", "s"])
    for j in range(1, ell[i]): add(f"b{i},{j+1}", 0, 3, ["s", f"b{i},{j}"], [f"b{i},{j}", "s"])
    add(f"c{i},1", 0, 3, ["r", f"B{i}"], [f"B{i}", "r"])
    for j in range(1, g): add(f"c{i},{j+1}", 0, 3, ["r", f"c{i},{j}"], [f"c{i},{j}", "r"])
N = len(names); assert all(nm in ids for v in E for nm in E[v])
out = [f"parity {N - 1};"] + [f"{v} {P[v]} {O[v]} {','.join(str(ids[x]) for x in E[v])} \"{names[v]}\";" for v in range(N)]
print("\n".join(out))
