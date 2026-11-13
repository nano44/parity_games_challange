#!/usr/bin/env python3
"""REFEREE successor 36: sums of the counters in docs/referee/scratch/gkx_logs/*.out (every number of R-P-N5-EXP.md's tables is
printed here from a log line; nothing is typed). Usage: gkx_summ.py [LOGDIR]   (default: the gkx_logs directory next to this file)"""
import sys, os, re, collections

D = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "gkx_logs")

def lines(f):
    p = os.path.join(D, f)
    return [l.rstrip("\n") for l in open(p)] if os.path.exists(p) else []

def kv(l):
    """«name value» pairs of a log line; a value a/b is split into (a, b)."""
    t = l.split()
    out = {}
    for i in range(len(t) - 1):
        if re.fullmatch(r"-?\d+(/\d+)?", t[i + 1]) and not re.fullmatch(r"-?\d+(/\d+)?", t[i]):
            out.setdefault(t[i], t[i + 1])
    return out

FACTS = ("K1", "K2", "K3", "V0", "V0shape", "V1", "V2", "V3", "V4", "K4", "M2", "WIRE")

def facts_sum(ls, title):
    if not ls:
        return
    tot = collections.Counter()
    den = collections.Counter()
    states = 0
    ks = []
    for l in ls:
        d = kv(l)
        ks.append(d["k"])
        states += int(d["states"])
        for c in FACTS:
            a, _, b = d[c].partition("/")
            tot[c] += int(a)
            den[c] += int(b) if b else 0
    print(f"{title}: k {','.join(ks)}; states {states:,}; " + " ".join(f"{c} {tot[c]:,}" + (f"/{den[c]:,}" if den[c] else "") for c in FACTS))

def main():
    g = lines("gen.out")
    if g:
        print(g[0])
        d = [kv(l) for l in g[1:]]
        print(f"gen: k {d[0]['k']}..{d[-1]['k']}; gendiff sum {sum(int(x['gendiff']) for x in d)}; wtie per k {' '.join(x['wtie'] for x in d)}; "
              f"revtie_genome_differs sum {sum(int(x['revtie_genome_differs']) for x in d)}; revtie_run_differs sum {sum(int(x['revtie_run_differs']) for x in d)}")
    m = lines("member.out")
    if m:
        z = [kv(l) for l in m if " ctrl 0 " in l]
        print(f"member: k {z[0]['k']}..{z[-1]['k']}; viol sum {sum(int(x['viol']) for x in z)}; Nform {sum(int(x['Nform']) for x in z)} dform {sum(int(x['dform']) for x in z)} "
              f"MXform {sum(int(x['MXform']) for x in z)}; width per k {' '.join(x['width'] for x in z)}")
        for l in m:
            if " ctrl 0 " not in l:
                d = kv(l)
                print(f"member control {d['ctrl']}: viol {d['viol']}; fires " + " ".join(f"c{i} {d['c' + str(i)]}" for i in range(1, 9) if d["c" + str(i)] != "0"))
    r = lines("run.out")
    if r:
        z = [kv(l) for l in r]
        print(f"run: k {z[0]['k']}..{z[-1]['k']}; L {' '.join(x['L'] for x in z)}; Lform {sum(int(x['Lform']) for x in z)} stopform {sum(int(x['stopform']) for x in z)} "
              f"swk {sum(int(x['swk']) for x in z)} maxform {sum(int(x['maxform']) for x in z)} sumform {sum(int(x['sumform']) for x in z)} nochange {sum(int(x['nochange']) for x in z)}")
    facts_sum(lines("facts_run.out"), "facts, every state of the run")
    fa = lines("facts_arb.out")
    for mode in ("w0u0", "u0", "w0", "free"):
        facts_sum([l for l in fa if f" mode {mode} " in l], f"facts, random states, mode {mode}")
    for l in lines("facts_all.out"):
        facts_sum([l], "facts, ALL states, mode " + l.split(" mode ")[1].split()[0])
    for l in lines("facts_ctrl.out"):
        d = kv(l)
        fired = [f"{c} {d[c]}" for c in FACTS if not d[c].startswith("0")]
        print(f"facts control {d['ctrl']}: fires " + ", ".join(fired))
    c = lines("causal.out")
    if c:
        z = [(kv(l), l) for l in c]
        for tag in ("run states", "arb states"):
            zz = [d for d, l in z if tag in l and " ctrl 0 " in l]
            a = sum(int(d["causal"].split("/")[0]) for d in zz)
            b = sum(int(d["causal"].split("/")[1]) for d in zz)
            print(f"causal, {tag}: k {','.join(d['k'] for d in zz)}; causal {a}/{b:,}")
        for d, l in z:
            if " ctrl 0 " not in l:
                print(f"causal control {d['ctrl']}: causal {d['causal']}")
    a = lines("abs.out")
    if a:
        z = [kv(l) for l in a if " ctrl 0 " in l]
        print(f"abs: k {z[0]['k']}..{z[-1]['k']}; full {sum(int(x['full']) for x in z)} stable {sum(int(x['stable']) for x in z)} "
              f"pref {sum(int(x['pref'].split('/')[0]) for x in z)}/{sum(int(x['pref'].split('/')[1]) for x in z):,}")
        for l in a:
            if " ctrl 0 " not in l:
                d = kv(l)
                print(f"abs control {d['ctrl']}: full {d['full']} pref {d['pref']}")
    rs = lines("resp.out")
    if rs:
        z = [kv(l) for l in rs if " ctrl 0 " in l]
        names = ("sched", "tlen", "h1", "h2", "empty", "econ", "restend", "fin", "stuck")
        print(f"resp: k {z[0]['k']}..{z[-1]['k']}; invocations {sum(int(x['calls']) for x in z):,}; steps {sum(int(x['L']) for x in z):,}; "
              + " ".join(f"{n} {sum(int(x[n]) for x in z)}" for n in names)
              + f"; e1inst {sum(int(x['e1inst']) for x in z)}/{len(z)} e5inst {sum(int(x['e5inst']) for x in z)}/{len(z)} (instances: 1 per k expected)")
        for l in rs:
            if " ctrl 0 " not in l:
                d = kv(l)
                print(f"resp control {d['ctrl']}: fires " + ", ".join(f"{n} {d[n]}" for n in names if d[n] != "0"))
    o = lines("orders.out")
    if o:
        z = [kv(l) for l in o]
        print(f"orders: k {z[0]['k']}..{z[-1]['k']}; variants {sum(int(x['reps']) for x in z):,}; rundiff {sum(int(x['rundiff']) for x in z)} "
              f"notmember {sum(int(x['notmember']) for x in z)} equal_to_G_k {sum(int(x['equal_to_G_k']) for x in z)}")
        for l in o:
            print("orders breaks, k " + l.split()[2] + ": " + " ".join(l.split()[11:]))
    for l in lines("sizes.out"):
        if l.startswith("sizes files") or l.startswith("first k"):
            print(l)
    q = lines("quotes.out")
    for l in q:
        if l.startswith("tags ") or l.startswith("UNTAGGED") or l.startswith("NOTFOUND"):
            print(l[:150])
    n5 = lines("n5.out")
    if n5:
        cs = ("S3START", "STD", "FLFB", "FLTAU", "FLSIG", "LASTFB", "WIN", "EXACT", "PG")
        z = [kv(l) for l in n5]
        print("n5: " + " ".join(l.split()[0] for l in n5) + "; iterations " + " ".join(x["iterations"] for x in z) + "; " +
              " ".join(f"{c} {sum(int(x.get(c, 0)) for x in z)}" for c in cs) + f"; PG compared on {sum(1 for x in z if 'PG' in x)} games")
    pgo = lines("n5_pg.out")
    if pgo:
        z = [kv(l) for l in pgo]
        print("n5_pg (game built here against the lane's frozen .pg, no N5 run): " + " ".join(l.split()[0] for l in pgo) + f"; PG {sum(int(x.get('PG', 0)) for x in z)} "
              f"on {sum(1 for x in z if 'PG' in x)} frozen files; GEN35 {sum(int(x['GEN35']) for x in z)}; "
              f"n {' '.join(x['n'] for x in z)}; m {' '.join(x['m'] for x in z)}; maxprio {' '.join(x['maxprio'] for x in z)}")
    for l in lines("unit.out"):
        print(l)
    cl = lines("closed.out")
    if cl:
        z = [kv(l) for l in cl if " ctrl 0 " in l]
        print(f"closed (box 108's c_k(t), own implementation, against my run): k {z[0]['k']}..{z[-1]['k']}; states {sum(int(x['states']) for x in z):,}; "
              f"closed {sum(int(x['closed']) for x in z)} stopset {sum(int(x['stopset']) for x in z)} HvsP {sum(int(x['HvsP']) for x in z)}")
        for l in cl:
            if " ctrl 0 " not in l:
                d = kv(l)
                print(f"closed control {d['ctrl']} (S3 for S2) on k {d['k']}: closed {d['closed']} of {d['states']} states")
    for l in lines("n5_pg12.out"):
        print("pg12: " + l[:200])
    sl = lines("strat.out")
    if sl:
        z = [(kv(l), l) for l in sl if " ctl 0 " in l]
        print("strat: " + " ".join(l.split()[1] for d, l in z) + f"; iterations {' '.join(d['iterations'] for d, l in z)}; evenregion {' '.join(d['evenregion'] for d, l in z)}; "
              f"oddregion {' '.join(d['oddregion'] for d, l in z)} (the vertex K2 on every line: {int(all(' oddvertices K2 STRATE' in l for d, l in z))}); "
              f"STRATE {sum(int(d['STRATE']) for d, l in z)} STRATO {sum(int(d['STRATO']) for d, l in z)} REG {sum(int(d['REG']) for d, l in z)}")
        for l in sl:
            if " ctl 0 " not in l:
                d = kv(l)
                print(f"strat control {l.split()[3]} on {l.split()[1]}: STRATE {d['STRATE']} STRATO {d['STRATO']}")
    for l in lines("n5_ctl.out"):
        d = kv(l)
        cs = ("S3START", "STD", "FLFB", "FLTAU", "FLSIG", "LASTFB", "WIN", "EXACT")
        print(f"n5 control {l.split()[2]} on {l.split()[0]}: fires " + ", ".join(f"{c} {d[c]}" for c in cs if d[c] != "0"))
    for l in lines("lem.out"):
        d = kv(l)
        cs = ("SBAR", "TAU", "ESC0", "ESC", "W", "XI", "AV", "STEP")
        fired = ", ".join(f"{c} {d[c]}" for c in cs if d[c] != "0")
        print(f"lem k {d['k']} control {l.split()[4]} ({d['states']} states): " + (("fires " + fired) if fired else "all 0"))

if __name__ == "__main__":
    main()
