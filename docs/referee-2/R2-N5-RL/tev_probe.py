#!/usr/bin/env python3
"""REFEREE-2 succ. 8: probe TEV-RED (1)-(4) at every state t after an in-scope fallback k0 with L = M_k0 >= 0, up to the next fallback of the
scope run or its end (k need not exist), with r > L on [k0+1, t] and a COARSE_L(theta) rise in (k0, t). Prints, per case: whether the
threat's play meets Ev, e, f, B_t \\ A, and whether (3) holds in the packet's form ("before e") and in the form "up to and including e".
Own N5 (frz_check.run_n5), S3 start + 2 random starts, det and --rand. Usage: tev_probe.py game.pg"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import frz_check as FC, rl_check as RL
RC = FC.RC
g = RC.parse(open(sys.argv[1]).read()); o = FC.odd_vertex(g); rng = random.Random(7); cnt = {}
for r in range(6):
    s, t0 = FC.s3_start(g) if r % 3 == 0 else RC.rand_start(rng, g)
    A, fbs = FC.run_n5(g, o, s, t0, rng, r >= 3); T = len(fbs)
    inph = [A[k].lamX == A[k + 1].lamX and A[k].tu[o] == A[k + 1].tu[o] for k in range(T)]
    insc = [inph[k] and A[k].hh and A[k + 1].H2 and A[k].w == A[k + 1].w for k in range(T)]
    print(f"run {r}: iterations {T}, fallbacks {sum(fbs)}")
    for k0 in range(T):
        if not (insc[k0] and fbs[k0] and A[k0].gates): continue
        L = max(A[k0].gates.values())
        if L < 0: continue
        Ev = A[k0 + 1].F - A[k0].F; c = A[k0].theta[0]
        H = {v for v in range(g.n) if g.rank[v] > max(L, g.rank[c])}
        Aset = A[k0].theta[1] & H
        t = k0 + 1; risen = False
        while t <= T and (t == k0 + 1 or (insc[t - 1] and not fbs[t - 1])):
            if A[t].r <= L: break
            if t > k0 + 1 and FC.coarse(g, A[t - 1].theta, L) != FC.coarse(g, A[t].theta, L): risen = True
            if risen and A[t].hh:
                St = A[t]; xp = RL.path_to(St.fh, St.sbar, c); full = RL.full_play(St.fh, St.sbar)
                meets = bool(set(full) & Ev)
                key = "meets" if meets else "avoids"; cnt[key] = cnt.get(key, 0) + 1
                if meets and xp is not None and set(xp) & Ev:
                    i = max(j for j, v in enumerate(xp) if v in Ev); e = xp[i]
                    Bt = St.theta[1] & H
                    before = set(xp[:i]) & H; upto = set(xp[:i + 1]) & H
                    f3a = Bt == Aset | before; f3b = Bt == Aset | upto
                    cnt[f"(3) before-e {f3a} / up-to-e {f3b}"] = cnt.get(f"(3) before-e {f3a} / up-to-e {f3b}", 0) + 1
                    print(f"  k0={k0} L={L} t={t} e={e} (Even={g.owner[e]==0}) e in H={e in H} B_t\\A={sorted(Bt - Aset)} (3)before={f3a} (3)upto={f3b}")
            t += 1
print(cnt)
