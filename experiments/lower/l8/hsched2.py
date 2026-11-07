#!/usr/bin/env python3
"""L-LOWER 8 (BOX L8 item 1): as hsched.py, but the helper trajectories are chosen INSIDE the wiring search, step by step, with the
joint condition set checked after every step (a helper's condition at step t depends only on its own chain at s_(t-1), which runs
through placed movers). Exact for its scope. Helper levels h..d-1; a helper of level l > h is placed only after both movers of level
l - 1 are placed (its key needs their states) -- this restricts the wiring order: such a helper cannot be read by level l - 1.
Gate patterns of helper levels h..d-2 enumerated (2 bits each). CLI: hsched2.py h d alpha [first]  (alpha e.g. 1,0,0; alpha[0] unused).
Prints the number of (gate pattern) cases and the first realizing genome (checked by sim6), or NONE."""
import sys, os, itertools, time
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..', 'l6')); sys.path.insert(0, os.path.join(H, '..', 'l7'))
from sim6 import okeys, run, Fprof, caps
from ranksolve import solve, constraints
from sched import schedule
from hsched import chainset
def keyseq(gate, d, S, l):
    D = {'d': d, 'gate': gate}; return [okeys(D, [v if v is not None else 0 for v in s])[l - 1] for s in S]
def realize(d, h, gate, LS, stats, tlimit):
    N = 2 * d; T = len(LS) - 1; S = [list(s) + [None] * (N - 2 * h) for s in LS]; bad = set(); t0 = time.time()
    g = gate
    def lower_conds(x, xt):
        out = []; l = x // 2
        for t in range(1, T + 1):
            s, ns = S[t - 1], S[t]
            if l == 0: free = g[2 * x + 1 - s[x]] < g[2 * x + s[x]]
            else: free = s[x] != okeys({'d': d, 'gate': g}, [v if v is not None else 0 for v in ns])[l - 1]
            if free: out.append((t, x, ns[x], set(chainset(xt, s, x, 0)), set(chainset(xt, s, x, 1))))
        return out
    def dfs(placed, xt, cons):
        if time.time() - t0 > tlimit: raise TimeoutError
        key = frozenset((x, placed[x], tuple(S[t][x] for t in range(T + 1)) if x >= 2 * h else None) for x in placed)
        if key in bad: return None
        if len(placed) == N: return list(xt)
        P = sorted(placed)
        for x in range(N):
            if x in placed: continue
            l = x // 2
            if l > h and not (2 * l - 2 in placed and 2 * l - 1 in placed): continue
            for a in [-1] + P:
                for b in [-1] + P:
                    xt[2 * x], xt[2 * x + 1] = a, b
                    if x < 2 * h:
                        c2 = cons + lower_conds(x, xt); stats['solve'] += 1
                        if solve(c2, 2 * N)[0] is None: continue
                        placed[x] = (a, b); r = dfs(placed, xt, c2); del placed[x]
                        if r is not None: return r
                    else:
                        c = keyseq(g, d, S, l)
                        def step(t, cur, cs):   # choose helper x's state at step t
                            if t > T:
                                placed[x] = (a, b); r = dfs(placed, xt, cs); del placed[x]; return r
                            s = S[t - 1]
                            for nx in ((cur, c[t]) if cur != c[t] else (cur,)):
                                S[t][x] = nx
                                if cur != c[t]:
                                    cc = cs + [(t, x, nx, set(chainset(xt, s, x, 0)), set(chainset(xt, s, x, 1)))]
                                    stats['solve'] += 1
                                    if solve(cc, 2 * N)[0] is None: continue
                                else: cc = cs
                                r = step(t + 1, nx, cc)
                                if r is not None: return r
                            S[t][x] = None; return None
                        for s0 in (0, 1):
                            S[0][x] = s0; r = step(1, s0, cons)
                            if r is not None: return r
                        for t in range(T + 1): S[t][x] = None
            xt[2 * x] = xt[2 * x + 1] = -1
        bad.add(key); return None
    r = dfs({}, [-1] * (2 * N), [])
    return (r, [tuple(s) for s in S]) if r is not None else None
def main():
    h, d = int(sys.argv[1]), int(sys.argv[2]); al = list(map(int, sys.argv[3].split(','))) if len(sys.argv) > 3 else [1] * h
    tl = float(sys.argv[4]) if len(sys.argv) > 4 else 3600
    _, LS = schedule(h, alpha=al); LS = [tuple(s[:2 * h]) for s in LS]
    print('h', h, 'd', d, 'alpha', al, 'lower T', len(LS) - 1, flush=True)
    hl = list(range(h, d - 1)); stats = {'solve': 0}; res = None; cases = 0
    for gp in itertools.product(range(4), repeat=len(hl)):
        gate = [0, 2, 1, 3] + [v for l in range(1, d) for v in (4 * l + 1000, 4 * l + 1001, 4 * l + 1002, 4 * l + 1003)]
        for i, l in enumerate(hl):
            b0, b1 = gp[i] & 1, gp[i] >> 1
            gate[4 * l + 0], gate[4 * l + 2] = (5, 3) if b0 else (3, 5)
            gate[4 * l + 1], gate[4 * l + 3] = (5, 3) if b1 else (3, 5)
        cases += 1
        try: r = realize(d, h, gate, LS, stats, tl)
        except TimeoutError: print('gate case', gp, 'TIMEOUT', flush=True); continue
        print('gate case', gp, 'realized' if r else 'none', 'solves so far', stats['solve'], flush=True)
        if r: res = (gate, r); break
    if not res: print('RESULT h', h, 'd', d, 'alpha', al, 'NONE realizable in', cases, 'gate cases (timeouts listed above)'); return
    gate, (xt, S) = res; N = 2 * d
    E = {'d': d, 'xt': xt, 'br': list(range(2 * N)), 'bp': [0] * (2 * N), 'gate': gate, 'start': list(S[0])}
    (br, bp), _ = solve(constraints(E, S), 2 * N); E['br'], E['bp'] = br, bp
    S2, O2 = run(E); F = Fprof(E, O2)
    print('RESULT h', h, 'd', d, 'alpha', al, 'REALIZED; sim6 T', len(S2) - 1, 'F', F, 'caps', caps(F), 'prefix = target', S2[:len(S)] == S)
    for k in ('d', 'xt', 'br', 'bp', 'gate', 'start'):
        print('GENOME', k, E[k] if k == 'd' else ' '.join(map(str, E[k])))
if __name__ == '__main__': main()
