"""L-RED box 26 (produced on Opus 5.5): edge classes of N5's jump-ahead switches (R58 §1). A jump-ahead switch = an N5 switch that
SSI would not make at the same state (n5tr's '*': Even v -> w with w != tau_bar(v), Odd v -> w with w != sigma_bar(v); R57 §6 C2).
Edge classes from SSI's own run from the same start (2309.02223 Alg. 2 SWITCH-ALL, n5.run mode 'ssi', loop replicated, count asserted):
  COUNTER = a choice edge some SSI strategy uses, THREAT = a choice edge no SSI strategy uses.
Also: the edge is RE-USED if N5's own run switches to it more than once. Usage: jumpclass.py G.pg [STARTFILE]"""
import io, os, sys
from collections import Counter
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, os.path.join(R, "experiments", "red", "n5"))
import n5tr  # noqa: E402
import n5  # noqa: E402
import pg  # noqa: E402
from si import Engine  # noqa: E402
path = sys.argv[1]; g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
st = n5tr.read_start(sys.argv[2]) if len(sys.argv) > 2 else None
E, Ed = Engine(g), Engine(n5.dual(g))
sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
if st:
    for v, w in st[0].items(): sigma[v] = w
    for v, w in st[1].items(): tau[v] = w
used = {(v, sigma[v] if g.owner[v] == 0 else tau[v]) for v in range(g.n)}; it = 0
while True:
    vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
    vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
    if not Is and not It: break
    it += 1
    ns, nt = list(sigma), list(tau)
    for v, w in Is:
        if tbar[v] == w: ns[v] = w
    for v, w in It:
        if sbar[v] == w: nt[v] = w
    sigma, tau = ns, nt
    used |= {(v, sigma[v] if g.owner[v] == 0 else tau[v]) for v in range(g.n)}
assert it == n5.run(g, "ssi", st)[0]
buf = io.StringIO(); n5it, _, _ = n5tr.trace(g, st, None, 10 ** 9, buf)
sw = []
for l in buf.getvalue().splitlines():
    if "| O:" not in l: continue
    t = int(l.split(":")[0].split()[0])
    for side, part in (("E", l.split("| E:")[1].split("| O:")[0]), ("O", l.split("| O:")[1])):
        for x in part.split():
            if x == "-": continue
            v, w = x.rstrip("*").split(">"); sw.append((t, side, int(v), int(w), x.endswith("*")))
times = Counter((v, w) for _, _, v, w, _ in sw)
cls = Counter()
for t, side, v, w, star in sw:
    c = ("COUNTER" if (v, w) in used else "THREAT") + ("/re-used" if times[(v, w)] > 1 else "")
    cls[("jump" if star else "ssi-type", side, c)] += 1
print(f"{os.path.basename(path)} n {g.n}: SSI {it} iterations, N5 {n5it}; switch classes (kind, player, edge class): count")
for k in sorted(cls): print("  ", k, cls[k])
print("  jump-ahead switches:", " ".join(f"{t}{s}:{v}>{w}" for t, s, v, w, star in sw if star))
