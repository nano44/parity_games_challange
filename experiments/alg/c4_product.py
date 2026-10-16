#!/usr/bin/env python3
"""C4 experiment: a complete solver S (Oink's tl / dtl / ptl / zlk ...) run on the prefix-maximum product game H_p(G)
(C2.md: states (v, c), c = max priority since the segment start, start included; entries (x, START) for every p-parity
vertex x; Good states = later visits to a p-parity vertex with c of p's parity, made p-winning sinks). p wins G from x iff
p wins H from (x, START) (section 2 of C2.md with a complete inner solver). Question: does the product abstract the
counter structure (tc) for tangle learning the way it does for psolC (NE'(1) solves tc), while tangle learning handles the
sibling traps? Output: per game, the solver's work counter on H_Even and H_Odd and the answer check against Oink on G.
Usage: c4_product.py SOLVER game.pg ...   or   c4_product.py SOLVER --tc N1,N2,..  --strfam S1,S2  --tile R1,R2"""
import sys, os, subprocess, tempfile, re, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, strfam, oink_fit, zielonka
from collections import deque
OINK = oink_fit.OINK
O = os.path.join(HERE, "..", "..", "tools", "oink", "build")


def product(g, p, X, alive):
    """H_p(G, alive, X): returns (prio, owner, succ, entry index of each x in X)."""
    START = -1
    nodes, out, succ = {}, [], []
    q = deque()
    for x in sorted(X):
        nodes[(x, START)] = len(out); out.append((x, START)); q.append((x, START))
    while q:
        v, c = q.popleft(); i = nodes[(v, c)]
        if c != START and v in X and c % 2 == p:
            succ.append([i]); continue                      # Good sink (self-loop, priority p)
        base = g.prio[v] if c == START else c
        s = []
        for w in sorted(set(g.succ[v])):
            if w not in alive:
                continue
            node = (w, max(base, g.prio[w]))
            if node not in nodes:
                nodes[node] = len(out); out.append(node); q.append(node)
            s.append(nodes[node])
        succ.append(sorted(set(s)))
    prio = [(p if (c != START and v in X and c % 2 == p) else g.prio[v]) for (v, c) in out]
    owner = [g.owner[v] for (v, c) in out]
    entries = {x: nodes[(x, START)] for x in X}
    return prio, owner, succ, entries


def run_oink(prio, owner, succ, solver, timeout=120):
    with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f:
        f.write(pg.dumps(pg.Game(prio, owner, succ))); path = f.name
    sp = path + ".sol"
    try:
        t0 = time.time()
        out = subprocess.run([OINK, f"--{solver}", "-v", "--no-single", "--no-wcwc", path, sp], capture_output=True, text=True, timeout=timeout).stdout
        dt = time.time() - t0
        m = oink_fit._pat.search(out); work = int(m.group(1) or m.group(3)) if m else -1
        win = pg.read_sol(open(sp).read(), len(prio))
        return win, work, dt
    except subprocess.TimeoutExpired:
        return None, 10**9, timeout
    finally:
        for f_ in (path, sp):
            if os.path.exists(f_): os.unlink(f_)


def attractor(g, alive, target, p):
    return zielonka.attractor(g, alive, target, p)


def solve(g, solver):
    """NE'-style outer loop with a complete inner solver: for p in (0,1): X := P_p ∩ alive; repeat X := X ∩ W(X) with
    W(X) = {x in X : p wins H_p(G, alive, X) from (x, START)} until stable; if X non-empty decide Attr_p(X), restart.
    Returns (win, total inner work per player, max |H|, inner calls)."""
    win = [None] * g.n; alive = set(range(g.n)); works = [0, 0]; size = 0; calls = 0
    while alive:
        removed = False
        for p in (0, 1):
            X = {v for v in alive if g.prio[v] % 2 == p}
            while X:
                prio, owner, succ, entries = product(g, p, X, alive)
                size = max(size, len(prio)); calls += 1
                hw, work, dt = run_oink(prio, owner, succ, solver)
                if hw is None:
                    return None, works, size, calls
                works[p] += max(work, 0)
                W = {x for x, i in entries.items() if hw[i] == p}
                if X <= W:
                    break
                X = X & W
            if X:
                D = attractor(g, alive, X, p)
                for v in D:
                    win[v] = p
                alive -= D; removed = True
                break
        if not removed:
            break
    if alive:
        return None, works, size, calls      # incomplete (should not happen with a complete inner solver)
    return win, works, size, calls


def ref(g):
    with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f:
        f.write(pg.dumps(g)); path = f.name
    sp = path + ".sol"
    for s in ("tl", "zlk", "psi"):
        try:
            subprocess.run([OINK, f"--{s}", path, sp], capture_output=True, timeout=120, check=True)
            return pg.read_sol(open(sp).read(), g.n)
        except Exception:
            continue
    return None


def main():
    solver = sys.argv[1]
    games = []
    args = sys.argv[2:]
    for a in args:
        if a.endswith(".pg"): games.append((os.path.basename(a), pg.read(a)))
    opt = lambda k: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else ""
    for N in [int(x) for x in opt("--tc").split(",") if x]:
        games.append((f"tc_{N}", pg.parse(subprocess.run([f"{O}/tc", str(N)], capture_output=True, text=True).stdout)))
    for s in [int(x) for x in opt("--strfam").split(",") if x]:
        games.append((f"S_{s}", strfam.S(s)))
    for R in [int(x) for x in opt("--tile").split(",") if x]:
        games.append((f"T_{R}", pg.read(os.path.join(HERE, "instances", f"zp_tile8_R{R}_n{32*R}.pg"))))
    for name, g in games:
        r = ref(g)
        t0 = time.time(); win, works, size, calls = solve(g, solver)
        ok = "TIMEOUT/INCOMPLETE" if win is None else ("OK" if win == r else "WRONG")
        print(f"{name}: n={g.n} d={len(set(g.prio))} |H|<={size} inner calls={calls} {solver} work Even/Odd = {works}  answer {ok}  t={time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
