#!/usr/bin/env python3
"""L-NEW box 155: which W-side lets the REAL IDEAL run of the Xi-ladder L_K (P-IDEAL-CUBE §4) follow the first m switches of the
LADDER-LP path, exactly (state t of the run = state t of the path, one switch per step)?
The Xi side of L_K is fixed (targets, ranks, parities, start). The W side is searched EXACTLY:
- every level assignment lev: movers -> {0, 1, ...} with contiguous levels (an ordered set partition);
- per option of a level-l mover (l >= 1), a W-target among the level-(l-1) movers (z3 choice);
- distinct gate indices (z3 integers).
Requirements (R104 step rule, P-IDEAL-RED §0): for t = 1..m and every mover x, with A := A_(s_(t-1))(x) (fixed by the Xi side):
if |A| = 2, the prescribed s_t(x) is the key-least option of x under the keys of s_t (keys root-first: key(x, k) = key(wt(x, k),
s_t(wt)) followed by g(x, k)); if |A| = 1 the prescribed state must not change (checked; never violated, since path switches are
improving). The run must not stop before m: guaranteed, since step t changes the state. UNSAT for a level assignment = no W-targets
and gates work for it. Output per (K, m): number of level assignments tried, SAT, and the first SAT witness (levels, W-targets,
gates), re-simulated with box150's simulator (XSIM: the real run's first m states equal the path's).
SEG=1: the run may take a consecutive SEGMENT of path switches per step (distinct movers; the run's states = the path's
states at the segment ends); all compositions of the first m switches are tried.
Usage: gate.py K m [TMO]"""
import sys, os, json, itertools, time
import z3
H = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(H, "..", "box154")]
ns = {"__file__": os.path.join(H, "..", "box154", "ladder.py")}; exec(open(ns["__file__"]).read().split("\nif __name__")[0], ns)
genome, Gen = ns["genome"], ns["Gen"]
K, m = int(sys.argv[1]), int(sys.argv[2]); TMO = int(sys.argv[3]) if len(sys.argv) > 3 else 120
G0 = genome(K); g = Gen(G0); N = G0["N"]
# the LADDER-LP path (same DFS as ladder.py), as a list of states
def path():
    s = list(G0["start"]); out = [tuple(s)]
    C = lambda s, x: 1 if g.face(s, x, 1) > g.face(s, x, 0) else 0
    B = lambda s, i: 0 if g.face(s, 2 * i, s[2 * i]) > g.face(s, 2 * i + 1, s[2 * i + 1]) else 1
    def sw(x):
        i = x // 2; b0 = B(s, i); s[x] = C(s, x); out.append(tuple(s))
        if B(s, i) != b0 and i + 1 < K: sw(2 * (i + 1)); sw(2 * (i + 1) + 1)
    sw(0); sw(1); return out
PATH = path()[: m + 1]
SEG = os.environ.get("SEG") == "1"
def comps(m):
    """compositions of the m path switches into consecutive segments (cut points), each segment with distinct movers"""
    sw = [next(x for x in range(N) if PATH[t][x] != PATH[t - 1][x]) for t in range(1, m + 1)]
    for mask in range(2 ** (m - 1)):
        cuts = [0] + [i + 1 for i in range(m - 1) if mask >> i & 1] + [m]
        if all(len(set(sw[a:b])) == b - a for a, b in zip(cuts, cuts[1:])): yield cuts
COMPS = list(comps(m)) if SEG else [list(range(m + 1))]
def partitions(n):
    """ordered set partitions of range(n) into contiguous levels 0..L-1 (as level lists)"""
    for L in range(1, n + 1):
        for lev in itertools.product(range(L), repeat=n):
            if set(lev) == set(range(L)): yield list(lev)
def solve(lev):
    Z = z3.Solver(); Z.set("timeout", TMO * 1000)
    gate = {(x, k): z3.Int(f"g{x}_{k}") for x in range(N) for k in (0, 1)}; Z.add(z3.Distinct(*gate.values()))
    wt = {}
    for x in range(N):
        cands = [y for y in range(N) if lev[y] == lev[x] - 1]
        for k in (0, 1):
            if lev[x] > 0:
                wt[(x, k)] = z3.Int(f"w{x}_{k}"); Z.add(z3.Or([wt[(x, k)] == y for y in cands]))
    order = sorted(range(N), key=lambda v: lev[v])
    def lt(a, b):
        e = z3.BoolVal(False)
        for j in reversed(range(len(a))): e = z3.Or(a[j] < b[j], z3.And(a[j] == b[j], e))
        return e
    for t in range(1, m + 1):
        s = S[t]; key = {}
        def okey(x, k):
            if lev[x] == 0: return [gate[(x, k)]]
            cands = [y for y in range(N) if lev[y] == lev[x] - 1]
            sub = [key[y] for y in cands]; L = lev[x]
            pref = [z3.Sum([z3.If(wt[(x, k)] == y, sub[i][j], 0) for i, y in enumerate(cands)]) for j in range(L)]
            return pref + [gate[(x, k)]]
        for x in order: key[x] = okey(x, s[x])
        for x in range(N):
            if len(A[t - 1][x]) == 2:
                Z.add(lt(okey(x, s[x]), okey(x, 1 - s[x])))
    r = Z.check()
    if r != z3.sat: return str(r), None
    M = Z.model(); ev = lambda e: M.eval(e, model_completion=True).as_long()
    return "sat", {"lev": lev, "gate": [[ev(gate[(x, 0)]), ev(gate[(x, 1)])] for x in range(N)],
                   "wt": [[ev(wt[(x, k)]) if (x, k) in wt else -1 for k in (0, 1)] for x in range(N)]}
t0 = time.time(); tried = sat = unk = 0; first = None; firstcut = None; satcuts = set()
for cuts in COMPS:
    S = [PATH[c] for c in cuts]; mm = len(S) - 1
    A = [[g.avail(list(S[t]), x) for x in range(N)] for t in range(mm)]
    if not all(S[t][x] in A[t - 1][x] for t in range(1, mm + 1) for x in range(N)): continue
    m_save = m; m = mm
    for lev in partitions(N):
        tried += 1; r, w = solve(lev)
        if r == "sat":
            sat += 1; satcuts.add(tuple(cuts))
            if first is None: first = w; firstcut = cuts; S_first = S
        elif r != "unsat": unk += 1
    m = m_save
if first: S = S_first; m = len(S) - 1
xsim = None
if first:
    G = json.loads(json.dumps(G0)); G["lev"] = first["lev"]; G["gate"] = first["gate"]
    for x in range(N):
        for k in (0, 1): G["opts"][x][k][0] = first["wt"][x][k]
    R = Gen(G).run(G["start"])[0]; xsim = [tuple(r) for r in R[: m + 1]] == S
    json.dump(G, open(os.path.join(H, f"gate_K{K}_m{m}.json"), "w"))
print(f"GATE{'-SEG' if SEG else ''} K {K} m {len(PATH) - 1} path {[next(x for x in range(N) if PATH[t][x] != PATH[t-1][x]) for t in range(1, len(PATH))]} tried {tried} cuts_sat {sorted(satcuts)} "
      f"SAT {sat} UNKNOWN {unk} first {first and first['lev']} XSIM {xsim} ({time.time() - t0:.0f} s)", flush=True)
