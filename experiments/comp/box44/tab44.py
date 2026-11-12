#!/usr/bin/env python3
"""L-COMP box 44: the README's tables, generated from out/ (no number is typed by hand).
Usage: tab44.py fam | free | lev SET ... | big"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); O = os.path.join(HERE, "out")


def f(l, pat, d=None):
    m = re.search(pat, l); return m.group(1) if m else d


def use(l):
    m = re.search(r"tie rules before the first fallback \(all passes\): (.*?)(?: \||$)", l); kv = m.group(1).split()
    return {kv[i]: (int(kv[i + 1]), int(kv[i + 2].strip("()"))) for i in range(0, len(kv), 3)}


def rows(fn):
    p = os.path.join(O, fn); return [l.rstrip("\n") for l in open(p)] if os.path.exists(p) else []


def must(l, drop=("tdiff",)):
    part = next(p for p in l.split(" | ") if p.startswith("s3fail "))
    kv = part.split(); return sum(int(kv[i + 1]) for i in range(0, len(kv), 2) if kv[i] not in drop)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "fam":
        spec = {(f(l, r"fam (\w+) n"), f(l, r" n (\d+) ")): l for l in rows("wrap44_fam_spec.out")}
        specl = {(f(l, r"fam (\w+) n"), f(l, r" n (\d+) ")): l for l in rows("wrap44_fam_spec_lsi.out")}
        lsi = {(f(l, r"fam (\w+) n"), f(l, r" n (\d+) ")): l for l in rows("wrap44_famlsi.out")}
        print("| H | n | \\|H\\|, edges | T: my Howard on H (tie events) | \\|W\\| | N5′-xi on my build: iterations, fallbacks | iterations − T | sum of the nine must-0 counters | S4b passes / own-cycle-node vertices / Ξσ-ties before the first fallback | frozen file vs my build (my order): isomorphic, H's indices fixed | frozen file vs my build in the frozen order: bytes equal; run on it: iterations | N5 (spec): my order / frozen order |")
        print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
        for l in rows("wrap44_fam.out"):
            k = (f(l, r"fam (\w+) n"), f(l, r" n (\d+) ")); u = use(l); z = lsi.get(k)
            name = {"switchall": "switchallexp_n", "lmcs": "G_n, ι (Figure 4 priorities)", "lmcst4": "G_n, ι (Table 4 priorities)"}[k[0]]
            fz = f(l, r"isomorphic with H's indices fixed (\w+)", "no frozen file")
            zb = "no frozen file" if z is None else "%s; %s" % (f(z, r"bytes equal (\w+)"), "not run" if "NOT RUN" in z else "%s (must-0 sum %d)" % (f(z, r"iterations (\d+) "), must(z)))
            sp = "%s / %s" % (f(spec[k], r"iterations (\d+) ") if k in spec else "not run", f(specl[k], r"iterations (\d+) ") if k in specl else "not run")
            print("| %s | %s | %s, %s | %s (%s) | %s | %s, %s | %s | %d | %d / %d / %d | %s | %s | %s |" % (
                name, k[1], f(l, r"\|H\| (\d+)"), f(l, r" m (\d+) "), f(l, r"myHoward T (\d+)"), f(l, r"ties (\d+) \|"), f(l, r"\|W\| (\d+)"), f(l, r"iterations (\d+) "),
                f(l, r"fallbacks (\d+)"), f(l, r"it-T (-?\d+)"), must(l), u["s4b"][0], u["owncyc"][0], u["xities"][0], fz, zb, sp))
    elif a[0] == "free":
        spec = {f(l, r"^FREE44 (F_\d+)"): l for l in rows("free44_spec.out")}
        print("| F_n | N, M | \\|V\\|, edges | T(G_n): my Howard on switchallexp_n (tie events) | N5′-xi on F_n: T3*, iterations, fallbacks | iterations − T | sum of the eleven counters | S4b passes / own-cycle-node vertices / Ξσ-ties before the first fallback | rebuilt from its decoded free genome by my builder: bytes equal | e-vertices below some β; odd β above some e; carriers; c_W | N5 (spec): iterations |")
        print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
        for l in rows("free44.out"):
            k = f(l, r"^FREE44 (F_\d+)"); u = use(l); part = next(p for p in l.split(" | ") if p.startswith("s3fail ")); kv = part.split()
            print("| %s | %s, %s | %s, %s | %s (%s) | %s, %s, %s | %s | %d | %d / %d / %d | %s | %s of %s; %s; %s..%s; %s | %s |" % (
                k, f(l, r" N (\d+) M"), f(l, r" M (\d+) \|V"), f(l, r"\|V\| (\d+)"), f(l, r" m (\d+) maxprio"), f(l, r": T (\d+) ties"), f(l, r"ties (\d+) \|"),
                f(l, r"T3\* (\d+)"), f(l, r"iterations (\d+) "), f(l, r"fallbacks (\d+)"), f(l, r"it-T (-?\d+)"), sum(int(kv[i + 1]) for i in range(0, len(kv), 2)),
                u["s4b"][0], u["owncyc"][0], u["xities"][0], f(l, r"bytes equal (\w+)"), f(l, r"e below some β (\d+)"), f(l, r"of (\d+); odd e"), f(l, r"odd β above some e (\d+)"),
                f(l, r"carriers (\d+)"), f(l, r"carriers \d+\.\.(\d+)"), f(l, r"c_W (\d+)"), f(spec[k], r"iterations (\d+) ") if k in spec else "not run"))
    elif a[0] == "lev":
        print("| set (file in out/) | genomes | sum of my 47 must-0 counters | max T3 | max T3 / bound | sum of T3 | stalls | plateaus (longest) | longest tail | reference states per genome | S4b passes / own-cycle-node vertices / Ξσ-ties before the first fallback (sums) |")
        print("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
        for s in a[1:]:
            R = [l for l in rows("lev44_%s.out" % s) if " | sum " in l]
            if not R: continue
            g = lambda k: [int(f(l, r" %s (\d+)" % k)) for l in R]
            us = [use(l) for l in R]; refs = g("refs")
            print("| lev44_%s.out | %d | %d | %d | %.2e | %d | %d | %d (%d) | %d | %s | %d / %d / %d |" % (
                s, len(R), sum(int(f(l, r"\| sum (\d+)")) for l in R), max(g("T3")), max(float(f(l, r"T3/bound ([0-9.e+-]+)")) for l in R), sum(g("T3")), sum(g("stalls")),
                sum(g("plateaus")), max(g("platmax")), max(g("tail_len")), "1 (b = T3)" if max(refs) == 1 else "every b" if all(r >= t or t == 0 for r, t in zip(refs, g("T3"))) else "%d-%d" % (min(refs), max(refs)),
                sum(u["s4b"][0] for u in us), sum(u["owncyc"][0] for u in us), sum(u["xities"][0] for u in us)))
    elif a[0] == "big":
        print("| genome | N + M | n | T3 | iterations | bound P3·(n_E3 + 1) + n_E3 | T3 / bound | sum of my 47 | stalls, plateaus (longest), tail |")
        print("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
        for l in rows("lev44_%s.out" % (a[1] if len(a) > 1 else "big")):
            if " | sum " not in l: continue
            N, M = int(f(l, r" N (\d+) M")), int(f(l, r" M (\d+) n"))
            print("| %s | %d | %s | %s | %s | %s | %s | %s | %s, %s (%s), %s |" % (l.split()[0].replace(".json", ""), N + M, f(l, r" n (\d+) \|"), f(l, r" T3 (\d+) Ttot"), f(l, r"Ttot (\d+)"), f(l, r"bound (\d+) "),
                  f(l, r"T3/bound ([0-9.e+-]+)"), f(l, r"\| sum (\d+)"), f(l, r"stalls (\d+)"), f(l, r" plateaus (\d+)"), f(l, r"platmax (\d+)"), f(l, r"tail_len (\d+)")))
