"""REFEREE packet 10 (Opus 5.5, D12): check Lemma ENTRY-CHARGE (GAP-A-M §23q) on my own p8probe logs.
Per (phase, context R), consecutive visit pairs, rounds aligned where both visits have round r (events and entries/exits
counted on the same aligned rounds). Prefix P_i(r, tau+) = union of the regions of tops > tau in round r of visit i.
Reports: sum_q k_q, N_ent, X_R, max events per entry (fan-out), max |F_sigma(i)| vs |R|, and checks
sum_q k_q <= |R| * N_ent and, per (step, vertex), entries <= exits + 1.
Usage: p10entry.py [oink|stable] G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import p8probe as Q, pg, dtl_pyref as P

def pref(rd, tau):
    return frozenset().union(*[z for t2, z in rd["reg"].items() if t2 > tau])

def run(order, path, tot):
    g = pg.read(path); old = P.DTL; P.DTL = Q.Probe
    try: _, _, d = P.solve_game(g, order=order)
    finally: P.DTL = old
    ss = d.searches; i = 0
    while i < len(ss):
        j = i
        while j + 1 < len(ss) and ss[j + 1]["p"] == ss[i]["p"] and ss[j + 1]["G"] == ss[i]["G"]: j += 1
        byR = {}
        for si in range(i, j + 1):
            for vis in ss[si]["visits"]: byR.setdefault(vis["R"], []).append(vis)
        for R, vs in byR.items():
            if len(vs) < 2: continue
            nR = len(R); events = []; ent = {}; ex = {}
            for m in range(len(vs) - 1):
                a, b = vs[m], vs[m + 1]
                for (r, tau, ts, rts) in Q.newsteals(d, a, b):
                    for t in rts: events.append((m, (r, tau), t))
                for r in range(min(len(a["rounds"]), len(b["rounds"]))):
                    ra, rb = a["rounds"][r], b["rounds"][r]
                    for tau in set(ra["V"]) | set(rb["V"]):
                        pa, pb = pref(ra, tau), pref(rb, tau)
                        for w in pb - pa: ent[((r + 1, tau), w)] = ent.get(((r + 1, tau), w), 0) + 1
                        for w in pa - pb: ex[((r + 1, tau), w)] = ex.get(((r + 1, tau), w), 0) + 1
                for rd in a["rounds"]:
                    for fs in rd["fired"].values():
                        tot["max_F_over_R_x100"] = max(tot["max_F_over_R_x100"], 100 * len(fs) // nR)
                        if len(fs) >= nR: tot["F_ge_R"] += 1
            # map each event to an entry (sigma, w, m) with w in t entering
            fan = {}
            for (m, st, t) in events:
                a, b = vs[m], vs[m + 1]; r, tau = st
                pa, pb = pref(a["rounds"][r - 1], tau), pref(b["rounds"][r - 1], tau)
                tv = {v for v, _ in d.tv[t]}
                ws = sorted((tv & pb) - pa)
                if not ws: tot["event_without_entry"] += 1; continue
                fan[(st, ws[0], m)] = fan.get((st, ws[0], m), 0) + 1
            N_ent = sum(ent.values()); X = sum(ex.values()); sk = len(events)
            tot["contexts"] += 1; tot["events"] += sk
            if sk > nR * N_ent: tot["ENTRYCHARGE_FAIL"] += 1
            for k_ in ent:
                if ent[k_] > ex.get(k_, 0) + 1: tot["alternation_fail"] += 1
            tot["max_fanout"] = max([tot["max_fanout"]] + list(fan.values()))
            tot["max_exits_per_step_vertex"] = max([tot["max_exits_per_step_vertex"]] + list(ex.values()))
            if sk: tot["max_events_over_Nent_x100"] = max(tot["max_events_over_Nent_x100"], 100 * sk // max(1, N_ent))
        i = j + 1

if __name__ == "__main__":
    from collections import Counter
    order = sys.argv[1]; tot = Counter(max_fanout=0, max_exits_per_step_vertex=0, max_F_over_R_x100=0, max_events_over_Nent_x100=0)
    for f in sys.argv[2:]:
        try: run(order, f, tot)
        except Exception as e: print("ERR", f, repr(e)); tot["err"] += 1
    print(order, dict(tot))
