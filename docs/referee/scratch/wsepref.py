r"""REFEREE throwaway, independent of L-STRUCT's wsep/: brute-force checks for deterministic weak/strong (n,d)-separators
(CDFJLP 1807.10546 S3.3; S1-statement.md D1-D5). Max-parity on labels 1..d. Conventions: E = edge-labelled multigraph
(any set of labels per ordered pair), S = at most one label per ordered pair, V = vertex-labelled (edge (u,v) labelled pr(u)).
Automaton: delta[q][p-1] in {state, None}; state 0 initial; None = rejecting sink (not counted).
Graphs are enumerated exhaustively (all of them, not maximal ones); vertices without an infinite continuation are pruned.
Usage: python3 -I wsepref.py <command> ...   (see main)"""
import sys, itertools, json

# ---------- graphs ----------
def prune(n, edges):
    alive = set(range(n)); ch = True
    while ch:
        ch = False
        for v in list(alive):
            if not any(u == v and w in alive for (u, p, w) in edges):
                alive.discard(v); ch = True
    return alive

def cycle_class(n, edges):
    """'even' if every cycle has even max, 'odd' if every cycle has odd max, 'mixed', or 'none' (no cycle)."""
    alive = prune(n, edges)
    E = [(u, p, w) for (u, p, w) in edges if u in alive and w in alive]
    maxes = set()
    for (u, p, w) in E:
        if p in maxes: continue
        seen = {w}; st = [w]
        while st:
            x = st.pop()
            for (a, q, b) in E:
                if a == x and q <= p and b not in seen:
                    seen.add(b); st.append(b)
        if u in seen: maxes.add(p)
    if not maxes: return 'none'
    par = {p % 2 for p in maxes}
    return 'mixed' if len(par) == 2 else ('even' if 0 in par else 'odd')

def graphs_V(n, d):
    succsets = [s for r in range(1, n + 1) for s in itertools.combinations(range(n), r)]
    for labels in itertools.product(range(1, d + 1), repeat=n):
        for succ in itertools.product(succsets, repeat=n):
            yield [(u, labels[u], w) for u in range(n) for w in succ[u]]

def graphs_S(n, d):
    pairs = [(u, w) for u in range(n) for w in range(n)]
    for lab in itertools.product(range(0, d + 1), repeat=len(pairs)):   # 0 = no edge
        yield [(u, p, w) for (u, w), p in zip(pairs, lab) if p]

def graphs_E2(d):
    """All edge-labelled multigraphs on 2 vertices: every ordered pair gets any subset of labels. 64^4 for d=6."""
    subsets = [[p for p in range(1, d + 1) if m >> (p - 1) & 1] for m in range(1 << d)]
    pairs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for ms in itertools.product(range(1 << d), repeat=4):
        yield [(u, p, w) for (u, w), m in zip(pairs, ms) for p in subsets[m]]

# ---------- automata ----------
def accepts_all(delta, n, edges):
    alive = prune(n, edges)
    E = [(u, p, w) for (u, p, w) in edges if u in alive and w in alive]
    seen = {(v, 0) for v in alive}; st = list(seen)
    while st:
        v, q = st.pop()
        for (a, p, b) in E:
            if a != v: continue
            q2 = delta[q][p - 1]
            if q2 is None: return False
            if (b, q2) not in seen: seen.add((b, q2)); st.append((b, q2))
    return True

def rejects_all(delta, n, edges):
    alive = prune(n, edges)
    E = [(u, p, w) for (u, p, w) in edges if u in alive and w in alive]
    seen = {(v, 0) for v in alive}; st = list(seen); adj = {}
    while st:
        v, q = st.pop(); adj.setdefault((v, q), [])
        for (a, p, b) in E:
            if a != v: continue
            q2 = delta[q][p - 1]
            if q2 is None: continue
            adj[(v, q)].append((b, q2))
            if (b, q2) not in seen: seen.add((b, q2)); st.append((b, q2))
    col = {x: 0 for x in adj}
    for s in adj:
        if col[s]: continue
        stack = [(s, iter(adj[s]))]; col[s] = 1
        while stack:
            x, it = stack[-1]
            for y in it:
                if col[y] == 1: return False
                if col[y] == 0: col[y] = 1; stack.append((y, iter(adj[y]))); break
            else:
                col[x] = 2; stack.pop()
    return True

def strong_S2(delta, d):
    """(S2): every cycle of the reachable transition graph has even maximum."""
    k = len(delta); seen = {0}; st = [0]
    while st:
        q = st.pop()
        for q2 in delta[q]:
            if q2 is not None and q2 not in seen: seen.add(q2); st.append(q2)
    edges = [(q, p, delta[q][p - 1]) for q in seen for p in range(1, d + 1) if delta[q][p - 1] is not None]
    return cycle_class(k, edges) in ('even', 'none')

def check(delta, n, d, conv, strong=False, want_witness=True):
    """Returns dict with counts and the first violating graph of each kind."""
    gen = {'V': lambda: graphs_V(n, d), 'S': lambda: graphs_S(n, d), 'E': lambda: graphs_E2(d)}[conv]
    assert conv != 'E' or n == 2
    cnt = {'even': 0, 'odd': 0, 'other': 0}; bad = {}
    for edges in gen():
        c = cycle_class(n, edges)
        if c == 'even':
            cnt['even'] += 1
            if 'W1' not in bad and not accepts_all(delta, n, edges): bad['W1'] = edges
        elif c == 'odd':
            cnt['odd'] += 1
            if not strong and 'W2' not in bad and not rejects_all(delta, n, edges): bad['W2'] = edges
        else:
            cnt['other'] += 1
    if strong and not strong_S2(delta, d): bad['S2'] = None
    return cnt, bad

def sub_n(n, d, conv, strong, delta):
    """Check for all sizes 1..n (a graph with fewer vertices is one with at most n; checked separately for clarity)."""
    out = {}
    for m in range(1, n + 1):
        out[m] = check(delta, m, d, conv, strong)
    return out

# ---------- universal trees (CFGO Props 6.10, 6.11) ----------
def f_upper(n, h):
    if n <= 0: return 0
    if h == 1: return n
    if n == 1: return 1
    return f_upper(n, h - 1) + f_upper(n // 2, h) + f_upper(n - 1 - n // 2, h)
def g_lower(n, h):
    if n <= 0: return 0
    if h == 1: return n
    if n == 1: return 1
    return sum(g_lower(n // dl, h - 1) for dl in range(1, n + 1))

WITNESS = [[1, 0, 1, 0, 2, 0], [2, 1, None, 0, None, 0], [None, 1, None, 1, None, 0]]

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "witness":   # witness n conv [strong]
        n, conv = int(sys.argv[2]), sys.argv[3]; strong = len(sys.argv) > 4
        delta = WITNESS if len(sys.argv) <= 5 else json.load(open(sys.argv[5]))['automaton']['delta']
        for m, (cnt, bad) in sub_n(n, 6, conv, strong, delta).items():
            print(f"conv {conv} n={m} d=6 {'strong' if strong else 'weak'} k={len(delta)}: graphs even={cnt['even']} odd={cnt['odd']} other={cnt['other']}; violations: " + (str({k: v for k, v in bad.items()}) if bad else "none"))
    elif cmd == "json":   # json path n conv
        r = json.load(open(sys.argv[2])); n, conv = int(sys.argv[3]), sys.argv[4]
        delta = r['automaton']['delta']; strong = r['mode'] == 'strong'
        for m, (cnt, bad) in sub_n(n, r['d'], conv, strong, delta).items():
            print(f"{sys.argv[2].split('/')[-1]} checked in conv {conv} n={m}: k={len(delta)} even={cnt['even']} odd={cnt['odd']}; violations: " + (str(bad) if bad else "none"))
    elif cmd == "utrees":
        for (n, h) in [(2, 2), (2, 3), (3, 2), (3, 3), (4, 2), (4, 3)]:
            print(f"universal tree ({n},{h}): g={g_lower(n, h)} f={f_upper(n, h)}")
    elif cmd == "k2":   # exhaustive 2-state automata, weak, conv V, n=2
        d = 6; evens, odds = [], []
        for m in (1, 2):
            for e in graphs_V(m, d):
                c = cycle_class(m, e)
                if c == 'even': evens.append((m, e))
                elif c == 'odd': odds.append((m, e))
        found = 0; tested = 0
        for flat in itertools.product([0, 1, None], repeat=2 * d):
            delta = [list(flat[:d]), list(flat[d:])]; tested += 1
            if all(accepts_all(delta, m, e) for m, e in evens) and all(rejects_all(delta, m, e) for m, e in odds):
                found += 1; print("2-state weak separator found:", delta); break
        print(f"k2 exhaustive conv V n<=2 d=6: {tested} automata tested, weak separators found: {found}")
