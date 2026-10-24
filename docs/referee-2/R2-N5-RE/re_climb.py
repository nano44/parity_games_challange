#!/usr/bin/env python3
"""REFEREE-2 hill climb for P-N5-RE: find C^1O games whose N5 runs have re-entries with theta UNCHANGED (the case Lemma RE is
about), leaves where (NC) fails, and long PIECE stretches. Fitness = 50*RE_theta_equal + 5*RE_reentries + 3*NC_FAILS + leaves_checked + PIECE_max_vc.
Each candidate is scored on 4 own-mode runs (random tie-breaks, random starts) + 1 spec run from the first start; every scored
run is fully checked by re_check.check_run (a violation stops the climb and is printed).
Usage: re_climb.py n steps seed outprefix [initial.pg]"""
import sys, random, copy
import re_check as rc

def mutate(rng, g, o):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    n = g.n; r = rng.random()
    if r < 0.5:
        v = rng.randrange(n)
        if owner[v] == 1 and v != o: succ[v] = [rng.randrange(n)]
        else:
            k = len(succ[v])
            if rng.random() < 0.5 and k > (2 if v == o else 1): succ[v].pop(rng.randrange(k))
            elif k < 3: succ[v].append(rng.randrange(n))
            else: succ[v][rng.randrange(k)] = rng.randrange(n)
    elif r < 0.8:
        prio[rng.randrange(n)] = rng.randrange(0, n + 1)
    else:
        v = rng.randrange(n)
        if v != o:
            owner[v] = 1 - owner[v]
            if owner[v] == 1: succ[v] = [succ[v][0]]
    h = rc.Game(prio, owner, succ)
    if len(h.succ[o]) < 2: return None
    return h

def score(g, o, seed, st):
    rng = random.Random(seed)
    tot = rc.Stats()
    for r in range(5):
        s, t = rc.rand_start(rng, g)
        if r == 4:
            s, t = rc.rand_start(random.Random(seed), g)
            states, fbs = rc.n5_spec(g, o, s, t)
        else:
            states, fbs = rc.n5_own(g, o, s, t, rng)
        rc.check_run(g, o, states, fbs, tot, f"climb", spec=(r == 4))
    for k, v in tot.c.items(): st.c[k] += v
    st.viol += tot.viol
    c = tot.c
    return 50 * c["RE_theta_equal"] + 5 * c["RE_reentries"] + 3 * c["NC_FAILS(honest)"] + c["leaves_checked"] + tot.mx["PIECE_max_vc"], tot

def main():
    n, steps, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rng = random.Random(seed); st = rc.Stats()
    if len(sys.argv) > 5:   # optional initial game
        g = rc.parse(open(sys.argv[5]).read()); oc = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]; assert len(oc) == 1, f'not C^1O: Odd choice vertices {oc}'; o = oc[0]
    else:
        g, o = rc.rand_game(rng, n)
    best, bt = score(g, o, seed, st)
    for i in range(steps):
        h = mutate(rng, g, o)
        if h is None: continue
        f, t = score(h, o, seed, st)
        if st.viol:
            print("VIOLATION", st.viol[:5]); break
        if f >= best:
            if f > best:
                print(f"step {i}: fitness {f} RE_theta_equal={t.c['RE_theta_equal']} NC={t.c['NC_FAILS(honest)']} "
                      f"leaves={t.c['leaves_checked']} piece={t.mx['PIECE_max_vc']}", flush=True)
            g, best, bt = h, f, t
    with open(out + ".pg", "w") as fh:
        fh.write(f"parity {g.n - 1};\n")
        for v in range(g.n): fh.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
    print("FINAL", best, dict((k, bt.c[k]) for k in ("RE_reentries", "RE_theta_equal", "RE_theta_changed", "NC_FAILS(honest)",
          "leaves_checked", "PIECE_stretches")), "PIECE_max_vc", bt.mx["PIECE_max_vc"])
    print("checked over the whole climb:", sum(st.c[k] for k in ("runs",)), "runs,", st.c["transitions"], "transitions,",
          st.c["RE_theta_equal"], "theta-equal re-entries,", st.c["NC_FAILS(honest)"], "NC-failing leaves")
    print("RESULT", "FAIL" if st.viol else "OK", f"violations={len(st.viol)}")

if __name__ == "__main__":
    main()
