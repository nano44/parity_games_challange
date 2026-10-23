"""L-RED box 25 (produced on Opus 5.5): VJ delay lanes on chosen edges of a game (for N5 tests). For each edge (v, w) listed (by node
name), with v of owner o and exit x (a named successor of v): L lane nodes l_1..l_L of owner o are added; l_1 -> {x, w}, l_j -> {x, l_{j-1}};
v's edge to w is replaced by v -> l_L. Lane priority: P (default 1 for an Even lane, 0 for an Odd lane: a low priority of the owner's
losing parity, so a longer path through the lane is a small cost to the owner when it matters). Start pair: lane nodes start on the
exit x; a start entry v:w for a laned edge is rewritten to v:l_L.
Usage: vjlane.py G.pg START L 'v>w>x' ... > OUT.pg   (writes OUT start to stderr)"""
import re, sys
path, startf, L = sys.argv[1], sys.argv[2], int(sys.argv[3])
specs = [s.split(">") for s in sys.argv[4:]]
lines = [l for l in open(path).read().splitlines() if l.strip() and not l.startswith("parity")]
nodes = {}
for l in lines:
    m = re.match(r'^\s*(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*(?:"([^"]*)")?\s*;?\s*$', l)
    v = int(m.group(1)); nodes[v] = [int(m.group(2)), int(m.group(3)), [int(x) for x in m.group(4).split(",")], m.group(5) or str(v)]
idx = {nodes[v][3]: v for v in nodes}
start = [l.split() for l in open(startf).read().splitlines() if l.strip()]
st = {t[0]: dict(tuple(map(int, x.split(":"))) for x in t[1:]) for t in start}
nxt = max(nodes) + 1
for vn, wn, xn in specs:
    v, w, x = idx[vn], idx[wn], idx[xn]
    o = nodes[v][1]; P = 1 if o == 0 else 0
    prev = w
    for j in range(1, L + 1):
        nodes[nxt] = [P, o, [x, prev], f"L{vn}{wn}_{j}"]
        st["SIGMA0" if o == 0 else "TAU0"][nxt] = x
        prev = nxt; nxt += 1
    nodes[v][2] = [prev if y == w else y for y in nodes[v][2]]
    key = "SIGMA0" if o == 0 else "TAU0"
    if st[key].get(v) == w:
        st[key][v] = prev
print(f"parity {max(nodes)};")
for v in sorted(nodes):
    p, o, s, nm = nodes[v]
    print(f'{v} {p} {o} {",".join(map(str, s))} "{nm}";')
for k in ("SIGMA0", "TAU0"):
    sys.stderr.write(k + " " + " ".join(f"{v}:{w}" for v, w in sorted(st[k].items())) + "\n")
