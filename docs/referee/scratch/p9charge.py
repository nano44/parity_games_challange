"""REFEREE packet 9 (Opus 5.5, D12): independent check of Lemma CHARGE (GAP-A-M §23g) on my own p8probe logs.
Per (phase, context R), consecutive visits; EVENTS = relevant steals (pair m, step (r, tau), tangle t) from p8probe.newsteals.
For each re-steal of q = (r, tau, t) at pair i with previous event at pair j, lists the events at pairs j < m < i at steps
strictly earlier (round smaller, or same round and higher top) = causes; also the vertices w of t that left P(tau+).
Usage: p9charge.py [oink|stable] G.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import p8probe as Q, pg, dtl_pyref as P

def main(order, path):
    g = pg.read(path); old = P.DTL; P.DTL = Q.Probe
    try: _, _, d = P.solve_game(g, order=order)
    finally: P.DTL = old
    ss = d.searches; i = 0; nre = nocause = 0
    while i < len(ss):
        j = i
        while j + 1 < len(ss) and ss[j + 1]["p"] == ss[i]["p"] and ss[j + 1]["G"] == ss[i]["G"]: j += 1
        byR = {}
        for si in range(i, j + 1):
            for vis in ss[si]["visits"]: byR.setdefault(vis["R"], []).append(vis)
        for R, vs in byR.items():
            ev = []   # (pair m, (r, tau), t)
            for m in range(len(vs) - 1):
                for (r, tau, ts, rts) in Q.newsteals(d, vs[m], vs[m + 1]):
                    for t in rts: ev.append((m, (r, tau), t))
            last = {}
            for (m, st, t) in sorted(ev):
                q = (st, t)
                if q in last:
                    jj = last[q]; nre += 1
                    causes = [(m2, st2, t2) for (m2, st2, t2) in ev if jj < m2 < m and (st2[0] < st[0] or (st2[0] == st[0] and st2[1] > st[1]))]
                    print(f"RE-STEAL |R|={len(R)} pair {m} step {st} t {t}; previous pair {jj}; causes {causes}")
                    if not causes: nocause += 1
                last[q] = m
        i = j + 1
    print(order, "re-steals", nre, "no cause", nocause)

if __name__ == "__main__": main(sys.argv[1], sys.argv[2])
