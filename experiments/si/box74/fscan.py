# L-SI box 74: F (top-pair key-order flips, flip-free runs, max over starts and bits) and T_0 for real genome JSONs. Usage: fscan.py files...
import sys, os, json, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box64")); from flipdp import Ext
for p in sys.argv[1:]:
    try: G = json.load(open(p)); E = Ext(G)
    except Exception: continue
    m = max(G["lev"]); bestF = (-1,); T0 = 0
    def keys(st):
        key = [None] * E.N
        for v in E.byl:
            wt = E.opts[v][st[v]][0]; key[v] = (E.gate[v][st[v]],) if wt < 0 else key[wt] + (E.gate[v][st[v]],)
        return key
    for u in itertools.product((0, 1), repeat=len(E.UP)):
        for b in (0, 1):
            seq = [u]
            while len(seq) < 200:
                n = E.step(seq[-1], b)
                if n == seq[-1]: break
                seq.append(n)
            o = [(lambda k: k[2 * m] < k[2 * m + 1])(keys(E.full(x, b))) for x in seq]
            F = sum(1 for i in range(len(o) - 1) if o[i] != o[i + 1]); T0 = max(T0, len(seq) - 1)
            if (F, len(seq) - 1) > bestF[:2]: bestF = (F, len(seq) - 1, list(u), b)
    print("%s m %d T0 %d maxF %d (run T %d, start %s, b %d)" % ((os.path.relpath(p), m, T0) + bestF))
