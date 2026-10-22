#!/usr/bin/env python3
"""Zadeh's rule with PGSolver's lower-bound tie-break on the zadehexp family (L-RED, R7). Faithful to
src/lib/solvers/stratimpralgs/switch_zadeh.ml @ d3cd624: improvement_policy_optimize_fair (least occurrence record among
improving edges, lines 1407-1457), improvement_policy_optimize_fair_sub_exp_tie_break (lines 1462-1591: state bits from
'leads to' tests on the path sets, state', idxmap, the class function mp, ties by list order = vertex then successor
index), initial_strategy_for_exp_game (lines 1612-1650). Records every tie situation (>= 2 candidates with the minimal
record) and checks whether the choices admit a FIXED total order of the edges (acyclic "chosen before competitor" graph).
Usage: zadeh_lb.py game.pg [--tie lb|index|val] [--trace]"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import vj
path = sys.argv[1]; tie = "lb"; trace = "--trace" in sys.argv
if "--tie" in sys.argv: tie = sys.argv[sys.argv.index("--tie") + 1]
lab = {}; prio = []; owner = []; succ = []
for line in open(path):
    m = re.match(r'^(\d+)\s+(\d+)\s+([01])\s+([\d,]+)\s*(?:"([^"]*)")?', line.strip())
    if m:
        v = int(m.group(1)); lab[v] = m.group(5) or str(v)
        while len(prio) <= v: prio.append(0); owner.append(0); succ.append([])
        prio[v] = int(m.group(2)); owner[v] = int(m.group(3)); succ[v] = sorted({int(x) for x in m.group(4).split(",")})
e = vj.VJ(prio, owner, succ); n_v = len(prio)
byname = {lab[v]: v for v in range(n_v)}
find = lambda s: byname.get(s)
def parse(v):
    s = lab[v]; return (s[0], int(s[1:])) if len(s) > 1 and s[1:].isdigit() else (s[0], 0)
n = 0
while find(f"E{n}") is not None: n += 1
# initial strategy of the exp game
sigma = list(e.initial("best"))
for v in range(n_v):
    if owner[v] == 0 and len(succ[v]) >= 2:
        c, j = parse(v)
        t = {"a": f"o{j}", "b": f"p{j}", "v": f"r{j}", "w": f"q{j}", "o": "m1", "p": "m1", "q": "m1", "r": "m1", "d": f"E{j}", "g": f"c{j}",
             "s": "m0", "m": (f"m{j + 1}" if j < n - 1 else "Y")}.get(c)
        if t and find(t) is not None and find(t) in succ[v]: sigma[v] = find(t)
sigma = tuple(sigma)
occ = {}; steps = 0; ties = 0; cons = set(); tielog = []


def bits(sigma, val):
    """(state, state') of the current strategy: state[i] = (X-gate i closed, E-gate i closed); state' = the bit vector
    PGSolver derives from it (sp[i] = sp[i+1]*s + (1-sp[i+1])*f)"""
    leadsto = lambda a, b: a is not None and b is not None and (val[a][1] >> e.rank[b]) & 1
    state = []
    for i in range(n):
        f = 1 if leadsto(find(f"a{i}"), find(f"E{i}")) and leadsto(find(f"b{i}"), find(f"E{i}")) else 0
        s = 1 if i < n - 1 and leadsto(find(f"v{i}"), find(f"X{i}")) and leadsto(find(f"w{i}"), find(f"X{i}")) else 0
        state.append((s, f))
    sp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        s, f = state[i]; sp[i] = sp[i + 1] * s + (1 - sp[i + 1]) * f
    return state, sp


def lb_rank(sigma, val, v, k):
    """mp value of the candidate edge (v -> k) under the current strategy"""
    nn = 2 * n
    leadsto = lambda a, b: a is not None and b is not None and (val[a][1] >> e.rank[b]) & 1
    state = []
    for i in range(n):
        f = 1 if leadsto(find(f"a{i}"), find(f"E{i}")) and leadsto(find(f"b{i}"), find(f"E{i}")) else 0
        s = 1 if i < n - 1 and leadsto(find(f"v{i}"), find(f"X{i}")) and leadsto(find(f"w{i}"), find(f"X{i}")) else 0
        state.append((s, f))
    sp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        s, f = state[i]; sp[i] = sp[i + 1] * s + (1 - sp[i + 1]) * f
    zeros = sum(1 for i in range(n) if sp[i] == 0); idx = [0] * n; zi, oi = 0, zeros
    for i in range(n):
        if sp[i] == 1: idx[i] = oi; oi += 1
        else: idx[i] = zi; zi += 1
    fi = lambda i: 2 * idx[i] + sp[i + 1]; gi = lambda i: 2 * idx[i] + 1 - sp[i + 1]
    h = lambda c, d, i: 1 if find(f"{c}{i}") is not None and lab[sigma[find(f"{c}{i}")]][0] == d else 0
    (sl, si), (tl, ti), (ol, oi_) = parse(v), parse(k), parse(sigma[v])
    if sl == "m": return -2 * nn
    if sl == "d": return (5 + 2 * nn) * nn
    if sl in "awbv" and ol in "EX": return -3 * nn
    if sl == "o": return ((-4 if h("a", "E", si) else 1) * nn + (nn - si))
    if sl == "p": return ((-4 if h("b", "E", si) else 1) * nn + (nn - si))
    if sl == "q": return ((-4 if h("w", "X", si) else 1) * nn + (nn - si))
    if sl == "r": return ((-4 if h("v", "X", si) else 1) * nn + (nn - si))
    if sl == "a" and tl == "E": return (2 + h("b", "E", si) * nn + fi(si)) * nn
    if sl == "w" and tl == "X": return (2 + h("v", "X", si) * nn + gi(si)) * nn
    if sl == "b" and tl == "E": return (2 + h("a", "E", si) * nn + fi(si)) * nn
    if sl == "v" and tl == "X": return (2 + h("w", "X", si) * nn + gi(si)) * nn
    if sl in "awbv" and ol == "Y": return -3 * nn
    if sl in "awbv": return nn
    if sl in "lgs": return (4 + 2 * nn) * nn
    if sl == "f": return (3 + 2 * nn) * nn
    if sl in "cu": return (4 + 2 * nn) * nn
    raise ValueError(lab[v])


while True:
    val, tau = e.evaluate(sigma); imp = e.improving(sigma, val)
    if not imp: break
    m = min(occ.get(x, 0) for x in imp); cands = [x for x in imp if occ.get(x, 0) == m]   # already in (v, w) order
    if tie == "index": ch = cands[0]
    elif tie == "val": ch = max(cands, key=lambda x: (e.key(val[x[1]]), -x[0], -x[1]))
    else:
        ranks = [(lb_rank(sigma, val, v, k), i) for i, (v, k) in enumerate(cands)]
        ch = cands[min(ranks)[1]]
    if len(cands) > 1:
        ties += 1
        for x in cands:
            if x != ch: cons.add((ch, x))
    occ[ch] = m + 1; steps += 1
    if trace:
        st, sp = bits(sigma, val)
        print(steps, f"{lab[ch[0]]}->{lab[ch[1]]}", "rec", m, "sp", "".join(map(str, sp[:n])), "state", "".join(f"{a}{b}" for a, b in st),
              "ties:", [f"{lab[a]}->{lab[b]}" for a, b in cands] if len(cands) > 1 else "")
    tielog.append((steps, ch, tuple(cands), bits(sigma, val)[1][:n]))
    s = list(sigma); s[ch[0]] = ch[1]; sigma = tuple(s)
# fixed-order feasibility: cycle check on the constraint digraph
adj = {}
for a, b in cons: adj.setdefault(a, set()).add(b)
color = {}; cyc = None
def dfs(u, stack):
    global cyc
    color[u] = 1; stack.append(u)
    for w in adj.get(u, ()):
        if color.get(w, 0) == 1 and cyc is None: cyc = stack[stack.index(w):] + [w]
        elif color.get(w, 0) == 0: dfs(w, stack)
    stack.pop(); color[u] = 2
for u in list(adj):
    if color.get(u, 0) == 0: dfs(u, [])
print(f"{os.path.basename(path)} tie={tie}: {steps} switches, {ties} tie steps, {len(cons)} 'chosen before competitor' constraints; "
      f"fixed total order exists: {cyc is None}" + (f"; a cycle: {' < '.join(f'{lab[a]}->{lab[b]}' for a, b in cyc)}" if cyc else ""))

rev = sorted({(a, b) for a, b in cons if (b, a) in cons and a < b})
if trace or "--rev" in sys.argv:
    print(f"direct reversals (both orders chosen at some tie): {len(rev)}")
    for a, b in rev:
        ctx = [(t, lab[c[0]] + "->" + lab[c[1]], "".join(map(str, sp))) for t, c, cs, sp in tielog if a in cs and b in cs and len(cs) > 1 and c in (a, b)]
        print(f"  {lab[a[0]]}->{lab[a[1]]} vs {lab[b[0]]}->{lab[b[1]]}:", " ".join(f"step{t}:{c}@sp={sp}" for t, c, sp in ctx))
