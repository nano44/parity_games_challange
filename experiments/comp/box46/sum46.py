#!/usr/bin/env python3
"""L-COMP box 46: the record's tables, computed from out/ (no number typed by hand). Usage: sum46.py 1 | 2 | 3"""
import sys, os, re, glob, json, collections, hashlib
H = os.path.dirname(os.path.abspath(__file__)); O = os.path.join(H, "out")
g = lambda l, k: int(re.search(r"(?:^| )%s (-?\d+)" % k, l).group(1))
has = lambda l, k: re.search(r"(?:^| )%s -?\d+" % k, l) is not None
sha = lambda p: hashlib.sha1(open(p, "rb").read()).hexdigest()[:12]


def rows(fn):
    return [l for l in open(fn) if " must0 " in l] if os.path.exists(fn) else []


def t1():
    print("out/cmp46.out (sha1 %s):" % sha(os.path.join(O, "cmp46.out")))
    for l in open(os.path.join(O, "cmp46.out")): print("    " + l.rstrip())


def t2():
    sets = [("tower", "box 212's 5 towers (Ξ-acyclic)", 5), ("lnew81", "L-NEW's 81 frozen (records 25, corpus 53, dead 3)", 81),
            ("xrand", "1,000 random Ξ-cyclic (rand46.py, seeds 4611 / 4612)", 1000), ("arand", "500 random Ξ-acyclic (rand46.py --acyclic, 4621 / 4622)", 500),
            ("xmine", "my box 39-45 sets, Ξ-cyclic members", 76), ("xbest", "box 44 / 45 climb bests, Ξ-cyclic", 64), ("xbig", "large family members, Ξ-cyclic", 11),
            ("xtower", "224 Ξ-cyclic tower variants (mkx46.py)", 224)]
    print("| set | rows (of) | file (sha1) | must0 | offbacyc | Ξ-cyclic | run_used | max W_key (genome, N + M) | max Wused (genome, N + M) | Σ steps in windows / Σ T_key |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for k, what, tot in sets:
        fu, fo = os.path.join(O, "win46u_%s.out" % k), os.path.join(O, "win46_%s.out" % k)
        R = rows(fu); src = fu
        part = "" if len(R) >= tot else " PARTIAL"
        if len(R) < tot and k in ("xbest", "xbig", "xtower", "xmine") and rows(fo):    # fall back to the first pass (no use columns)
            R = rows(fo); src = fo; part = " (first pass, no use columns)" if len(R) >= tot else " PARTIAL"
        if not R: print("| %s | 0 (%d) | not run | | | | | | | |" % (what, tot)); continue
        u = has(R[0], "run_used")
        nm = lambda l: g(l, "N") + g(l, "M")
        mw = max(R, key=lambda l: (g(l, "Wkey"), -nm(l))); mu = max(R, key=lambda l: (g(l, "Wused"), -nm(l))) if u else None
        print("| %s | %d (%d)%s | %s (%s) | %d | %s | %d | %s | %d (%s, %d) | %s | %d / %d |" % (what, len(R), tot, part, os.path.basename(src), sha(src),
              sum(g(l, "must0") for l in R), sum(g(l, "offbacyc") for l in R) if u else "—", sum(g(l, "xcyc") > 0 for l in R),
              sum(g(l, "run_used") for l in R) if u else "—", g(mw, "Wkey"), mw.split()[0], nm(mw),
              "%d (%s, %d)" % (g(mu, "Wused"), mu.split()[0], nm(mu)) if u else "—", sum(g(l, "inwin") for l in R), sum(g(l, "Tkey") for l in R)))
    # tower variants by parity, first pass (complete)
    tw = {"DBL4": 30, "RECF4": 67, "H5": 136, "H6": 209, "HIT7": 299}; C = collections.Counter()
    for l in rows(os.path.join(O, "win46_xtower.out")):
        b = l.split()[0]; p = b.split("_p")[1][0]; same = g(l, "Tkey") == tw[b.split("_")[0]] and g(l, "Wkey") == g(l, "Tkey")
        C[(p, "n")] += 1; C[(p, "same")] += same
    print("\nTower variants (out/win46_xtower.out, sha1 %s): odd β parity: run equal to the tower's (T_key and one window = the run) on %d of %d; even: on %d of %d." % (
        sha(os.path.join(O, "win46_xtower.out")), C[("1", "same")], C[("1", "n")], C[("0", "same")], C[("0", "n")]))
    U = {l.split()[0]: json.loads(l.split(None, 3)[3]) for l in open(os.path.join(O, "use46.out"))}
    used = sum(1 for c in U.values() if c["offbeta"] or c["cycopt"])
    print("use46.py (independent of win46's use columns; out/use46.out, sha1 %s): %d genomes, cycle used (offbeta or cycopt > 0) on %d." % (sha(os.path.join(O, "use46.out")), len(U), used))
    agree = n = 0
    for f in glob.glob(os.path.join(O, "win46u_*.out")):
        for l in rows(f):
            b = l.split()[0]
            if b in U: n += 1; agree += (g(l, "run_used") == int(bool(U[b]["offbeta"] or U[b]["cycopt"])) and g(l, "offbeta") == U[b]["offbeta"] and g(l, "cycopt") == U[b]["cycopt"])
    print("Cross-check use46 vs win46's use columns (offbeta, cycopt, run_used) on the genomes in both: %d of %d equal." % (agree, n))
    print("\nControls of the use columns (out/win46_usectrl.out, sha1 %s; win46e.py):" % sha(os.path.join(O, "win46_usectrl.out")))
    for l in open(os.path.join(O, "win46_usectrl.out")):
        print("    %s %s must0 %d offbacyc %d T_key %d run_used %d Wused %d offbeta %d cycopt %d Wess %d" % (l.split()[0], l.split()[1], g(l, "must0"), g(l, "offbacyc"), g(l, "Tkey"), g(l, "run_used"), g(l, "Wused"), g(l, "offbeta"), g(l, "cycopt"), g(l, "Wess")))


def t3():
    print("| band | log (sha1) | status | seeds (Wused at N + M) | best file | Wused | N + M | ratio | T_key | W_key | must0 | second engines | ALERT lines |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for b in ("B0", "B1", "B2", "B3", "E3"):
        fn = os.path.join(O, ("climb46e_%s.log" if b == "E3" else "climb46_%s.log") % b)
        if not os.path.exists(fn): print("| %s | — | NOT RUN | | | | | | | | | | |" % b); continue
        L = open(fn).read().splitlines(); st = "DONE" if any(l.startswith("DONE") for l in L) else "PARTIAL (resumable: %s.state)" % os.path.basename(fn)
        seeds = sorted({re.search(r"seed (\S+) Wused (\d+) NM (\d+)", l).groups() for l in L if l.startswith("START")})
        B = [l for l in L if l.startswith("BEST") or l.startswith("ALERT")]
        if not B: print("| %s | %s (%s) | %s | %s | — | | | | | | | | |" % (b, os.path.basename(fn), sha(fn), st, "; ".join("%s %s at %s" % s for s in seeds))); continue
        l = B[-1]; m = re.search(r"BEST (\S+) Wused (\d+) NM (\d+) ratio ([\d.]+) Tkey (\d+) Wkey (\d+) run_used (\d+) must0 (\d+)", l)
        agree = all("agree True" in x for x in B)
        print("| %s | %s (%s) | %s | %s | out/%s/%s | %s | %s | %s | %s | %s | %s | %d of %d bests agree | %d |" % (b, os.path.basename(fn), sha(fn), st, "; ".join("%s %s at %s" % s for s in seeds),
              "climb46e" if b == "E3" else "climb46", m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), m.group(6), m.group(8), sum("agree True" in x for x in B), len(B), sum(x.startswith("ALERT") for x in L)))
    print("\n(E3 row: the second B3 climb, objective W_ess; its «Wused» column is W_ess and its «W_key» column is Wused, names kept from climb46.)")
    q = os.path.join(O, "wess46.out")
    if os.path.exists(q):
        print("\nwess of seeds and final bests (out/wess46.out, sha1 %s; win46e.py):" % sha(q))
        for l in rows(q): print("    %s N+M %d T_key %d W_key %d Wused %d offbeta %d cycopt %d wess_max %d wess_wused %d W_ess %d must0 %d" % (l.split()[0], g(l, "N") + g(l, "M"), g(l, "Tkey"), g(l, "Wkey"), g(l, "Wused"), g(l, "offbeta"), g(l, "cycopt"), g(l, "wess_max"), g(l, "wess_wused"), g(l, "Wess"), g(l, "must0")))


if __name__ == "__main__":
    {"1": t1, "2": t2, "3": t3}[sys.argv[1]]()
