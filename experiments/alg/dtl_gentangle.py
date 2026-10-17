"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4): random GENUINE p-tangle on a given vertex set (strongly connected under a\np-strategy inside C plus all opponent edges inside C, every cycle won by p), DTL storage format (tv, escapes)."""
import random
def genuine(d, p, C, pr):
    """Random genuine p-tangle on vertex set C (internal ids) or None: p-strategy inside C, opponent edges inside C,
    strongly connected, every cycle won by p (max priority on it has parity p)."""
    C = set(C); st = {}
    for v in C:
        if d.ow[v] == p:
            ins = [w for w in d.outs[v] if w in C]
            if not ins: return None
            st[v] = pr.choice(ins)
    E = {v: ([st[v]] if d.ow[v] == p else [w for w in d.outs[v] if w in C]) for v in C}
    if any(not E[v] for v in C): return None
    def reach(s, allowed):
        seen = {s}; st_ = [s]
        while st_:
            x = st_.pop()
            for y in E[x]:
                if y in allowed and y not in seen: seen.add(y); st_.append(y)
        return seen
    v0 = next(iter(C))
    if reach(v0, C) != C: return None
    Erev = {v: [u for u in C if v in E[u]] for v in C}
    seen = {v0}; s_ = [v0]
    while s_:
        x = s_.pop()
        for y in Erev[x]:
            if y not in seen: seen.add(y); s_.append(y)
    if seen != C: return None
    for w in C:                       # no cycle through w within priorities <= pr(w) when pr(w) has opponent parity
        if d.pr[w] % 2 != p:
            allowed = {u for u in C if d.pr[u] <= d.pr[w]}
            if any(w in E[x] for x in reach(w, allowed) if x in allowed): return None
    esc = sorted({w for v in C if d.ow[v] != p for w in d.outs[v] if w not in C})
    return [(v, st.get(v, -1)) for v in sorted(C)], esc
