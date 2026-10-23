"""L-RED box 25 (produced on Opus 5.5): per-vertex switch counts of N5 (via n5tr.trace, counts asserted = n5.run): for each player, the
number of vertices that ever switch, the maximum number of switches at one vertex, and how many vertices switch back to a successor
they used before (a "return"). Usage: perswitch.py G.pg [STARTFILE]"""
import io, os, re, sys
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import n5tr  # noqa: E402
import pg  # noqa: E402
path = sys.argv[1]; g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
st = n5tr.read_start(sys.argv[2]) if len(sys.argv) > 2 else None
buf = io.StringIO(); it, fb, _ = n5tr.trace(g, st, None, 10 ** 9, buf)
for side, tag in (("Even", "E:"), ("Odd", "O:")):
    cnt = defaultdict(int); seq = defaultdict(list); ret = set()
    for l in buf.getvalue().splitlines():
        if "| O:" not in l: continue
        part = l.split("| E:")[1].split("| O:")[0] if tag == "E:" else l.split("| O:")[1]
        for t in part.split():
            if t == "-": continue
            v, w = t.rstrip("*").split(">"); v, w = int(v), int(w)
            cnt[v] += 1
            if w in seq[v]: ret.add(v)
            seq[v].append(w)
    mx = max(cnt.values(), default=0)
    print(f"{os.path.basename(path)} n {g.n} it {it}: {side}: vertices switching {len(cnt)}, max switches at one vertex {mx}, vertices with a return {len(ret)}")
