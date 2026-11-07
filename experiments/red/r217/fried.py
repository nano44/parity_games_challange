#!/usr/bin/env python3
"""L-RED 54 R217: Friedmann's switchallexp (0901.2731 G_n; trunk experiments/hard-families/pgsolver_port.py, env WTT, read-only) and
Howard = switch-all VJ (si.Engine, env WT3 tree) on the ORIGINAL game from the best-reward start (reward(w) = p if even else -p).
Usage: fried.py n  -> prints Howard iterations on G_n."""
import sys, os, subprocess
WTT, WT3 = os.environ["WTT"], os.environ["WT3"]
sys.path[:0] = [os.path.join(WT3, "experiments/si"), os.path.join(WT3, "experiments/harness")]
from si import Engine
def game(n):
    txt = subprocess.run([sys.executable, os.path.join(WTT, "experiments/hard-families/pgsolver_port.py"), "switchallexp", str(n)],
                         capture_output=True, text=True, check=True).stdout
    V = []
    for line in txt.splitlines()[1:]:
        line = line.strip().rstrip(";")
        if not line: continue
        a, nm = line.split('"')[0].split(), line.split('"')[1]
        V.append((int(a[0]), int(a[1]), int(a[2]), [int(x) for x in a[3].split(",")], nm))
    V.sort(); return V
def rew(p): return p if p % 2 == 0 else -p
def howard(V, cap=100000):
    import pg
    g = pg.Game([v[1] for v in V], [v[2] for v in V], [v[3] for v in V]); E = Engine(g)
    s = tuple(max(v[3], key=lambda w: (rew(V[w][1]), w)) if v[2] == 0 else -1 for v in V)
    vs, _ = E.evaluate(s); T = 0; traj = [s]
    while T < cap:
        ns = tuple(max(g.succ[v], key=lambda w: (E.key(vs[w]), w == s[v], w)) if g.owner[v] == 0 else -1 for v in range(g.n))
        if ns == s: break
        s = ns; vs, _ = E.evaluate(s); T += 1; traj.append(s)
    return T, traj
if __name__ == "__main__":
    for n in map(int, sys.argv[1:]):
        V = game(n); T, _ = howard(V); print(f"switchallexp n {n} |V| {len(V)} Howard(VJ switch-all, best-reward start) T {T}", flush=True)
