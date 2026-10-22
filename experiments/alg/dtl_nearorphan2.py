"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5): HOW a near-orphan (dtl_nearorphan.py) goes when its last escape is
removed. Logs every successful attractTangle inside search_rec's removals (Dom = dtl_pyref.dom, the -1 attractor) with:
the caller, the threshold, whether t's top-priority vertex m was already in the target, and pr(m). For each near-orphan whose
escape and vertices all leave in the next removal, reports whether t was taken AS A TANGLE in that removal and, if so, which
of (threshold >= pr(m)) / (m already in the target) let it pass. DTL_ORDER = oink | stable. Usage: dtl_nearorphan2.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_nearorphan as NOm
D = NOm.D

class NO2(NOm.NO):
    def tattr(s, p, Z, R, Gx, maxpr, consume):
        who = sys._getframe(1).f_code.co_name; s.cur_who = who; s.cur_th = maxpr; s.cur_Z = Z
        return D.DTL.tattr(s, p, Z, R, Gx, maxpr, consume)
    def attractTangle(s, t, p, R, Z, Gx, maxpr):
        C = [v for v, _ in s.tv[t]] if t < len(s.tv) else []
        m = max(C, key=lambda v: (s.pr[v], v)) if C else None; m_in = m in Z if C else None
        r = D.DTL.attractTangle(s, t, p, R, Z, Gx, maxpr)
        if r and getattr(s, "cur_who", "") in ("dom", "search_rec"):
            s.tev.setdefault(frozenset(C), []).append((len(s.calls), s.cur_who, maxpr, m_in, s.pr[m]))
        return r

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tab = {}
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = NOm.SL.P.X.build(g); d = NO2(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.near_at = {}
        orig = d.search
        def search(p, d=d, orig=orig):
            d.near_at = {}; d.tev = {}; r = orig(p); d.trace[-1]["near"] = d.near_at; d.trace[-1]["tev"] = d.tev; return r
        d.search = search; d.run()
        for tr in d.trace:
            calls = tr["calls"]; near = tr.get("near", {}); tev = tr.get("tev", {})
            for k, lst in near.items():
                pos = calls[k][0]
                j = next((i for i in range(k + 1, len(calls)) if calls[i][0] == pos[:-1] + (pos[-1] + 1,)), None)
                if j is None: continue
                R2 = calls[j][1]
                for C, e, m in lst:
                    if e in R2 or (C & R2): continue
                    ev = [x for x in tev.get(C, []) if k + 1 <= x[0] <= j]      # attractions between call k and call j
                    if not ev: key = ("taken vertex-wise (no tangle attraction)",)
                    else:
                        _, who, th, m_in, prm = ev[0]
                        key = ("taken as a tangle", who, "threshold >= pr(m)" if th < 0 or th >= prm else "threshold < pr(m)", "m already in target" if m_in else "m not in target")
                    tab[key] = tab.get(key, 0) + 1
    for k, v in sorted(tab.items(), key=lambda kv: -kv[1]): print(v, k)
