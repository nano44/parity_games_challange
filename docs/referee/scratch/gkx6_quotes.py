#!/usr/bin/env python3
"""REFEREE successor 37, stage 5b: byte tests on P-N5-EXP-fixes.md entries 7 and later (claude/l-red-b 10dfedb6 by default) and
on the RESULTS line. Own script (helpers of gkx5_quotes.py); the lane's b6fixquote.py, b6line.py, b6guard.py are not imported
and were not opened. Sources are read from git objects; run from inside the repository.
Usage: python3 -I gkx6_quotes.py [--commit C] [--from N] MODE
  entries  the objects (append-only chain, packet, frozen paths), then every Q-tagged quote of the entries that begin at line
           >= N (default 882) in the cited lines of its source; REF2 / REF2B quotes BY SCRIPT ONLY (docs/referee-2/ is not read)
  spoil    control: the first letter of every quote replaced
  pins     the pin files added since entry 6, the sha1 values written in those entries, the pasted DATA blocks
  facts    single sentences of those entries against the files they speak of; the lane's e7_*.out against this lane's logs
  linedata the DATA clauses of the line against the pinned output files they name
  line L   byte tests of the line file docs/red-b/P-N5-EXP-line-L.txt at the commit (L = L3, L4, ...), its difference from the
           previous lines, its quotations at the commits the line names, the commit ids it names"""
import sys, os, re, subprocess, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gkx5_quotes as q5

show, norm, sha1, git = q5.show, q5.norm, q5.sha1, q5.git
D = q5.D
FIXP, PKT = q5.FIXP, q5.PKT
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gkx_logs")
SRC = dict(q5.SRC)
SRC.update({
    "REF2B": ("f17a2708de653b306eaedf878f6120d2d0b31e06", "docs/referee-2/R2-P-N5-EXP.md"),
    "REF1D": ("78515253a74a353a829b435d53f4987a8552989a", "docs/referee/R-P-N5-EXP.md"),
    "FIX5": ("24f4d436a0fea1f62ae736f20f78ff9e84333a90", FIXP),
})
SCRIPT_ONLY = ("REF2", "REF2B")
CHAIN = [("06d399c2", 125), ("24f4d436", 829), ("0c8fdf9ea", 881), ("b1a937004", 1147), ("10dfedb65", 1180)]


def opt(args, flag, default):
    if flag in args:
        i = args.index(flag)
        v = args[i + 1]
        del args[i:i + 2]
        return v
    return default


def entries_mode(C, start, spoil):
    fix = show(C, FIXP)
    lines = fix.split("\n")
    ent = [e for e in q5.entries(fix) if e[1] >= start]
    if not spoil:
        print(f"fixes file at {C}: lines {fix.count(chr(10))} sha1 {sha1(fix)}; packet there sha1 {sha1(show(C, PKT))} "
              f"(frozen c0449b17193f19619f33b366096762dfde27d542: {int(sha1(show(C, PKT)) == 'c0449b17193f19619f33b366096762dfde27d542')})")
        prev, chain = None, []
        for c, n in CHAIN:
            t = show(c, FIXP)
            ok = int(fix.startswith(t))
            chain.append(f"{c[:8]} {t.count(chr(10))} lines (stated {n}: {int(t.count(chr(10)) == n)}) sha1 {sha1(t)[:8]}… a byte prefix of the file at {C}: {ok}")
        for l in chain:
            print("append-only: " + l)
        paths = [PKT, "experiments/red-b/gk.py", D + "G", D + "raw", D + "pg", D + "SHA1SUMS_b6b", D + "SHA1SUMS_b6b_fixes1", D + "SHA1SUMS_b6b_fixes2",
                 D + "SHA1SUMS_b6b_fixes3"]
        fz = [l for l in git("diff", "--name-status", "0c8fdf9ea", C, "--", *paths).split("\n") if l.strip()]
        ns = [l for l in git("diff", "--name-status", "0c8fdf9ea", C, "--", "docs/red-b", "experiments/red-b").split("\n") if l.strip()]
        old_out = [l.split()[1] for l in ns if l.split()[0] != "A" and "/data/" in l]
        print(f"0c8fdf9e -> {C}: the packet, gk.py, data/b6b/G, raw, pg and the pin files of the frozen packet and of entries 1-6: changed {len(fz)}; "
              f"under docs/red-b, experiments/red-b: added {sum(1 for l in ns if l.split()[0] == 'A')}, modified "
              f"{' '.join(sorted(l.split()[1].split('/')[-1] for l in ns if l.split()[0] == 'M'))}, deleted {sum(1 for l in ns if l.split()[0] == 'D')}; "
              f"data files of entries 1-6 modified {len(old_out)}")
        print("entries by their headings: " + "; ".join(f"{n} l. {a}-{b}" for n, a, b in ent))
    pos = [0]
    for l in lines:
        pos.append(pos[-1] + len(l) + 1)
    def entry_at(p):
        for n, a, b in ent:
            if pos[a - 1] <= p < pos[b]:
                return n
        return None
    srcs, stat, bad = {}, {}, []
    for m in re.finditer(r"\[Q ([A-Za-z0-9]+)((?: [^\]]*)?)\]", fix):
        e = entry_at(m.start())
        if e is None:
            continue
        label, loc = m.group(1), m.group(2)
        qs = q5.quotes_after(fix, m.end())
        st = stat.setdefault(e, {})
        if label not in srcs:
            srcs[label] = show(*SRC[label]).split("\n")
        sl = srcs[label]
        rg = q5.ranges(loc)
        assert rg, f"tag without line numbers: {m.group(0)}"
        rtxt = [norm("\n".join(sl[a - 1:b])) for (a, b) in rg]
        for qq in qs:
            nq = norm(qq)
            if spoil:
                nq = ("#" if nq[0] != "#" else "%") + nq[1:]
            ok = any(nq in t for t in rtxt) or nq in " ".join(rtxt)
            s = st.setdefault(label, [0, 0])
            s[0] += 1
            s[1] += int(ok)
            if not ok and not spoil:
                where = "elsewhere in the source" if nq in norm("\n".join(sl)) else "NOT in the source"
                bad.append(f"NOT in the cited lines ({where}): {e} {m.group(0)} «{qq[:40]}…»" if label not in SCRIPT_ONLY else
                           f"NOT in the cited lines ({where}; by script): {e} {m.group(0)}")
    for b in bad:
        print(b)
    tag = "quotes control (first letter spoiled)" if spoil else "quotes"
    tq = tf = 0
    for n, a, b in ent:
        st = stat.get(n, {})
        tq += sum(v[0] for v in st.values())
        tf += sum(v[1] for v in st.values())
        print(f"{tag}, {n} (l. {a}-{b}): " + ("; ".join(f"{l}{' (by script only)' if l in SCRIPT_ONLY else ''} {v[1]} of {v[0]} in the cited lines" for l, v in sorted(st.items())) or "no tagged quote"))
    print(f"{tag}, together: quotes {tq} in the cited lines {tf}")
    if not spoil:
        for l in ("REF2B", "REF1D", "FIX5"):
            if l in srcs:
                t = "\n".join(srcs[l])
                print(f"source {l} = {SRC[l][0][:8]}:{SRC[l][1]}: lines {t.count(chr(10))} sha1 {sha1(t)}")


def pins_mode(C, start):
    fix = show(C, FIXP)
    outs = {}
    for pf in ("SHA1SUMS_b6b_fixes4", "SHA1SUMS_b6b_fixes5"):
        rows = [l.split() for l in show(C, D + pf).split("\n") if l.strip()]
        mism = 0
        for want, rel in rows:
            outs[rel] = show(C, D + rel)
            mism += int(sha1(outs[rel]) != want)
        print(f"pins: {pf} at {C}: files {len(rows)}; sha1 mismatches {mism}")
    pool = set()
    for txt in outs.values():
        pool.update(l.rstrip() for l in txt.split("\n"))
    ent = [e for e in q5.entries(fix) if e[1] >= start]
    inblock, per = False, {}
    for i, l in enumerate(fix.split("\n"), 1):
        if i < start:
            continue
        if l.strip() == "```":
            inblock = not inblock
            continue
        if inblock:
            e = [n for n, a, b in ent if a <= i <= b][0]
            p = per.setdefault(e, [0, 0, []])
            p[0] += 1
            if l.rstrip() not in pool:
                p[1] += 1
                p[2].append(i)
    print("pins: fenced DATA lines / of them not a line of a pinned output file: " +
          "; ".join(f"{e} {p[0]} / {p[1]}" + (f" (fixes l. {' '.join(map(str, p[2][:8]))})" if p[2] else "") for e, p in per.items()))
    # the sha1 values written in the entries against the git objects
    want = [("f17a2708de653b306eaedf878f6120d2d0b31e06:docs/referee-2/R2-P-N5-EXP.md", "7128d83e76c675609af3f74c73cb0015c9de2ef3", 549),
            ("78515253a74a353a829b435d53f4987a8552989a:docs/referee/R-P-N5-EXP.md", "0ec7d605ffd23b31114cdc328d792261a108ced9", 542),
            ("24f4d436a0fea1f62ae736f20f78ff9e84333a90:" + FIXP, "9dc9179fb08063cd59de25c5d3e16b0f8c693fbd", 829),
            ("350d84eb:" + PKT, "c0449b17193f19619f33b366096762dfde27d542", None),
            (f"{C}:docs/red-b/P-N5-EXP-line-L2.txt", "6e047c676e582484fe8eb87891764e8c1a7d9a18", 1),
            (f"{C}:docs/red-b/P-N5-EXP-line-L3.txt", "fd9074a3b9961f59a1b64d5acdaa28529306ede9", 1)]
    bad = absent = nl = 0
    for obj, w, n in want:
        c, path = obj.split(":")
        t = show(c, path)
        bad += int(sha1(t) != w)
        absent += int(w not in fix)
        nl += int(n is not None and t.count("\n") != n)
    print(f"pins: sha1 values written in the entries (REF2B's file by script, REF1D, FIX5, the packet, L-2, L-3): {len(want)}; not in the fixes file {absent}; "
          f"different from the git object {bad}; stated line counts wrong {nl}")
    r496 = "\n".join(show("78515253a74a353a829b435d53f4987a8552989a", "docs/referee/R-P-N5-EXP.md").split("\n")[:496]) + "\n"
    print(f"pins: REF1D's first 496 lines equal the report at 7ca9c2b4 byte for byte: {int(r496 == show('7ca9c2b4', 'docs/referee/R-P-N5-EXP.md'))}; "
          f"Addendum 2 «is its l. 321-549» (by script: the first line with «Addendum 2» in a heading of REF2B): "
          f"{[i + 1 for i, l in enumerate(show(*SRC['REF2B']).split(chr(10))) if l.startswith('#') and 'Addendum 2' in l][:1]}")
    # 7.4: the E lines of runfix.out carry the sha1s of SHA1SUMS_b6b_fixes2; those pinned files are untouched since 24f4d436
    f2 = {l.split()[1].split("/")[-1]: l.split()[0] for l in show(C, D + "SHA1SUMS_b6b_fixes2").split("\n") if l.strip()}
    E = [l.split() for l in show(C, D + "out/runfix.out").split("\n") if l.startswith("E ") and " sha1 " in l]
    eb = sum(int(f2.get(w[1]) != w[3] or w[5] != "0" or w[7] != "1") for w in E)
    ch = [l for l in git("diff", "--name-status", "24f4d436", C, "--", D + "SHA1SUMS_b6b_fixes2", *[D + "out/" + w[1] for w in E]).split("\n") if l.strip()]
    print(f"pins: runfix.out E lines {len(E)}: sha1 = the pin of SHA1SUMS_b6b_fixes2, cmp-with-data 0, sha1-equals-pin 1: lines failing {eb}; "
          f"those {len(E)} pinned files and the pin file changed since 24f4d436: {len(ch)}; last line «{show(C, D + 'out/runfix.out').strip().split(chr(10))[-1]}»")


def facts_mode(C):
    def kvl(l, start=1):
        w = l.split()
        return {w[i]: w[i + 1] for i in range(start, len(w) - 1, 2)}
    # 7.1 / 7.3: the lane's e7_r3.out, e7_xt.out, e7_ctrl.out against this lane's s37_r3.out, s37_xt.out (own model)
    mine_r3 = {r["k"]: r for r in (kvl(l) for l in open(os.path.join(HERE, "s37_r3.out"), encoding="utf-8") if l.startswith("r3 k"))  if r["ctrl"] == "0"}
    mine_c1 = {r["k"]: r for r in (kvl(l) for l in open(os.path.join(HERE, "s37_r3.out"), encoding="utf-8") if l.startswith("r3 k")) if r["ctrl"] == "1"}
    n = bad = 0
    ks = []
    for l in show(C, D + "out/e7_r3.out").split("\n"):
        if not l.startswith("G_"):
            continue
        k, r = l.split()[0][2:], kvl(l)
        ks.append(k)
        for col in ("windows", "windows2", "r3in", "r3move", "r3rest", "literal", "expected", "litdiff"):
            n += 1
            bad += int(r[col] != mine_r3[k][col])
    c1 = 0
    for l in show(C, D + "out/e7_ctrl.out").split("\n"):
        if l.startswith("G_") and " mode r3 ctrl 1 " in l:
            k, r = l.split()[0][2:], kvl(l)
            n += 1
            c1 += 1
            bad += int(r["r3in"] != mine_c1[k]["r3in"])
    print(f"facts 7.1: e7_r3.out k {ks[0]}..{ks[-1]} (8 columns) and the {c1} r3 control lines of e7_ctrl.out (r3in) against this lane's own r3 counters: "
          f"compared {n} different {bad}; windows2 total {sum(int(mine_r3[k]['windows2']) for k in ks):,}, literal total {sum(int(mine_r3[k]['literal']) for k in ks):,}")
    mine_xt = {}
    for l in open(os.path.join(HERE, "s37_xt.out"), encoding="utf-8"):
        if l.startswith("xt k"):
            w = l.split()
            mine_xt[w[2]] = {"kinds": " ".join(w[w.index("kinds") + 1:w.index("wiretgt")]), **{c: w[w.index(c) + 1] for c in ("N", "wiretgt", "etgt", "yptgt", "expected", "ypdiff")},
                             "outside": w[-1]}
    n = bad = 0
    ks = []
    for src, isctl in ((show(C, D + "out/e7_xt.out"), False), (show(C, D + "out/e7_ctrl.out"), True)):
        for l in src.split("\n"):
            if not l.startswith("G_") or " mode xt " not in l:
                continue
            w = l.split()
            k = w[0][2:]
            if not isctl:
                ks.append(k)
            for c in ("N", "wiretgt", "etgt", "yptgt", "expected", "ypdiff"):
                n += 1
                bad += int(w[w.index(c) + 1] != mine_xt[k][c])
            n += 1
            bad += int(" ".join(w[w.index("kinds") + 1:w.index("wiretgt")]) != mine_xt[k]["kinds"])
            if isctl:
                n += 1
                bad += int(w[w.index("outside") + 1] != mine_xt[k]["outside"])
    print(f"facts 7.3: e7_xt.out k {ks[0]}..{ks[-1]} and the xt control lines of e7_ctrl.out (kinds, N, wiretgt, etgt, yptgt, expected, ypdiff, outside) "
          f"against this lane's own Ξ-target counters: compared {n} different {bad}")
    # 7.2: the table's frozen lines; the untagged guillemet phrases of 7.2 in the packet
    pk = show("350d84eb", PKT).split("\n")
    chk = [("191", "P_(k−1) := 3 and P_j := 2·P_(j+1) + 1" in pk[190]), ("192", pk[191].startswith("**RESPONSE LEMMA.** Let 1 ≤ j ≤ k − 1, a ∈ {0, 1}, c := 1 − a, t ≥ 1")),
           ("193", pk[192].lstrip().startswith("(H1)")), ("194", pk[193].lstrip().startswith("(H2)")),
           ("195a", pk[194].startswith("Let F be the observer of Y_j that is on forward under s_(t−1) and B the other one; F′, B′ the same for Y′_j.")),
           ("195b", pk[194].rstrip().endswith("Then the run reaches")), ("197", pk[196].lstrip().startswith("(i) j = k − 1")),
           ("198", pk[197].lstrip().startswith("(ii) j ≤ k − 2")), ("202", "No mover of unit j moves at any other step" in pk[201]),
           ("203", pk[202].startswith("In both cases:")), ("204", pk[203].rstrip().endswith("hold.")),
           ("198p", "(from REST_(j+1)(0), to the input (1, 1))" in pk[197]), ("200p", "(from REST_(j+1)(1), to the input (0, 0))" in norm(pk[198] + " " + pk[199])),
           ("258", pk[257].startswith("**STABLE.**"))]
    print(f"facts 7.2: the packet's l. 191-204 and l. 258 begin / end as the table's rows say: checks {len(chk)} failed {sum(1 for _, ok in chk if not ok)}"
          + ("" if all(ok for _, ok in chk) else " (" + " ".join(nm for nm, ok in chk if not ok) + ")"))
    # 7.6 / entry 8: the lane's records of the lines against this lane's measurements
    l1, l2, l3 = (show(C, f"docs/red-b/P-N5-EXP-line-L{i}.txt") for i in (1, 2, 3))
    rec = show(C, D + "out/line_L2_build.out").split("\n")
    pairs = []
    for i, l in enumerate(rec):
        if l.startswith("--- "):
            pairs.append((l[4:].split(":")[0], int(re.search(r"at character (\d+)", l).group(1)), rec[i + 1][2:], rec[i + 2][2:]))
    at = sum(int(l1[pos:pos + len(old)] == old) for _, pos, old, _ in pairs)
    built = l1
    for _, pos, old, new in sorted(pairs, key=lambda x: -x[1]):
        built = built[:pos] + new + built[pos + len(old):]
    # conventions of entry 7, 7.5, and the line's «Addendum 2 §A2.3» (the second referee's file: by script only, headings and counts)
    qf, qc = show(C, D + "out/quote_fixes7.out").strip().split("\n")[-1], show(C, D + "out/quote_fixes7_ctrl.out").strip().split("\n")[-1]
    r2 = show(*SRC["REF2B"]).split("\n")
    heads = [(i + 1, l) for i, l in enumerate(r2) if l.startswith("#")]
    above = [h for h in heads if h[0] <= 464][-1]
    names = ("QUIET-KEY-1P", "SW-POLY", "P-N5-KEY1P")
    print(f"facts conventions: quote_fixes7.out ends «{qf}», its control «{qc}»; REF1D's §12 heading at l. "
          f"{[i + 1 for i, l in enumerate(show(*SRC['REF1D']).split(chr(10))) if l.startswith('## 12.')]} of 542; commits 577e8df9, 4cf6e1ff ancestors of 78515253: "
          f"{int(all(subprocess.run(['git', 'merge-base', '--is-ancestor', c, '78515253'], cwd=q5.TOP).returncode == 0 for c in ('577e8df9', '4cf6e1ff')))}")
    print(f"facts 7.5 and the tail: L-1, L-2, L-3 name QUIET-KEY-1P, SW-POLY or P-N5-KEY1P: {sum(int(n in x) for n in names for x in (l1, l2, l3))} times; "
          f"in REF2B the last heading at or above l. 464 is at l. {above[0]} and names A2.3: {int('A2.3' in above[1])}; a heading with «Addendum 2» at l. "
          f"{[h[0] for h in heads if 'Addendum 2' in h[1]][:1]}")
    d23 = [i for i in range(min(len(l2), len(l3))) if l2[i] != l3[i]]
    print(f"facts 7.6: line_L2_build.out records {len(pairs)} replacements ({', '.join(n for n, _, _, _ in pairs)}); L-1 has the recorded old text at the "
          f"stated character for {at} of {len(pairs)}; L-1 with them applied at those characters is L-2 byte for byte: {int(built == l2)}; "
          f"L-1 characters outside the recorded old texts {len(l1) - sum(len(o) for _, _, o, _ in pairs)} (the record: 5144 of 5463)")
    print(f"facts entry 8: L-2 -> L-3: same length {int(len(l2) == len(l3))}; characters that differ {len(d23)} at {d23}: "
          f"{' '.join(repr(l2[i]) + '->' + repr(l3[i]) for i in d23)}; «with fixes entries 1-5» once in L-2 {int(l2.count('with fixes entries 1-5') == 1)}, "
          f"«L-RED-B successors 5-6» once in L-2 {int(l2.count('L-RED-B successors 5-6') == 1)}; L-3 = L-2 with the two replacements "
          f"{int(l2.replace('with fixes entries 1-5', 'with fixes entries 1-7').replace('L-RED-B successors 5-6', 'L-RED-B successors 5-7') == l3)}")


def linedata_mode(C):
    """The DATA clauses of the line against the pinned files they name (ctrl-0 lines only)."""
    def rows(commit, name):
        out = []
        for l in show(commit, D + "out/" + name).split("\n"):
            w = l.split()
            if not w or not w[0].startswith("G_"):
                continue
            k = int(re.match(r"G_(\d+)", w[0]).group(1))
            d = {"_": l}
            for i in range(1, len(w) - 1):
                d[w[i]] = w[i + 1]                       # the last occurrence of a name wins («mode loc … loc 0»)
            d["K"] = k
            out.append(d)
        return out
    def z(rs, cols):
        return sum(int(r[c]) for r in rs for c in cols)
    def ks(rs):
        s = sorted(set(r["K"] for r in rs))
        return f"{s[0]}..{s[-1]}" if s == list(range(s[0], s[-1] + 1)) else str(s)
    m = [r for r in rows("350d84eb", "member.out") if r["ctrl"] == "0"]
    print(f"linedata member.out: k {ks(m)} ({len(m)} lines) viol sum {z(m, ['viol'])}; clauses c1..c8 present {int(all(all(f'c{i}' in r for i in range(1, 9)) for r in m))}; member 1 on {sum(int(r['member']) for r in m)}")
    s = [r for r in rows("350d84eb", "sim.out") if r["ctrl"] == "0"]
    print(f"linedata sim.out: k {ks(s)} ideq sum {z(s, ['ideq'])}; T = TB = TC = 2^k − 2 fails on {sum(int(not (int(r['T']) == int(r['TB']) == int(r['TC']) == 2 ** r['K'] - 2)) for r in s)}; "
          f"stop stuck on {sum(int(r['stop'] == 'stuck') for r in s)} of {len(s)}; howard max {max(int(r['howard']) for r in s)}")
    le = [r for r in rows("350d84eb", "lemma.out") if r["ctrl"] == "0"]
    print(f"linedata lemma.out: k {ks(le)} kfact, vfact, sched, tlen, rest, swk sum {z(le, ['kfact', 'vfact', 'sched', 'tlen', 'rest', 'swk'])}")
    pr = [r for r in rows(C, "prefix_run.out") if r["ctrl"] == "0"]
    pa = [r for r in rows(C, "prefix_all.out") if r["ctrl"] == "0"]
    po = [r for r in rows(C, "prefix_off.out") if r["ctrl"] == "0"]
    pd = [r for r in rows(C, "prefix_drive.out") if r["ctrl"] == "0"]
    pl = [r for r in rows(C, "prefix_loc.out") if r["ctrl"] == "0"]
    ps = [r for r in rows(C, "prefix_stable.out") if r["ctrl"] == "0"]
    pe = [r for r in rows(C, "prefix_exh.out") if r["ctrl"] == "0"]
    pu = [r for r in rows(C, "prefix_u0.out") if r["ctrl"] == "0"]
    pc = [r for r in rows(C, "prefix_ctrl.out") if r.get("mode") == "all" and r["ctrl"] == "5"]
    print(f"linedata prefix_*.out: run k {ks(pr)} windows {sum(int(r['windows']) for r in pr):,} h1 {z(pr, ['h1'])} h2 {z(pr, ['h2'])} psched {z(pr, ['psched'])}; "
          f"all k {ks(pa)} aviol {z(pa, ['aviol'])}; exh k {ks(pe)} pviol {z(pe, ['pviol'])} loc {z(pe, ['loc'])} stviol {z(pe, ['stviol'])} c0e0 {z(pe, ['c0e0'])}; "
          f"off pviol {z(po, ['pviol'])}; drive dviol {z(pd, ['dviol'])}; loc {z(pl, ['loc'])}; stable stviol {z(ps, ['stviol'])}; u0 c0e0 {z(pu, ['c0e0'])}; "
          f"the frozen wording (control 5) k {ks(pc)}: fails = k − 1 on {sum(int(int(r['frozen_conclusion_fails']) == r['K'] - 1) for r in pc)} of {len(pc)} lines")
    n5 = [r for r in rows("350d84eb", "n5.out") + rows(C, "n5_k12.out") if r["ctrl"] == "0"]
    print(f"linedata n5.out + n5_k12.out: k {ks(n5)}; its = its2 = 2^k + 1, fb = fb2 = 1, F = 2^k − 2 fails on "
          f"{sum(int(not (int(r['its']) == int(r['its2']) == 2 ** r['K'] + 1 and r['fb'] == r['fb2'] == '1' and int(r['F']) == 2 ** r['K'] - 2)) for r in n5)}; "
          f"mism, wrong, wrong2, nonmover, engdiff, gdiff sum {z(n5, ['mism', 'wrong', 'wrong2', 'nonmover', 'engdiff', 'gdiff'])}; "
          f"n {n5[0]['n']} … {[r for r in n5 if r['K'] == 11][0]['n']} for k 3 … 11, iterations {n5[0]['its']} … {[r for r in n5 if r['K'] == 11][0]['its']}")
    k13 = rows(C, "n5_k13.out")[0]
    print(f"linedata n5_k13.out: its {k13['its']} n {k13['n']} F {k13['F']} (fallback at iteration {int(k13['F']) + 1}) fb {k13['fb']}; mism, wrong, nonmover, gdiff sum "
          f"{z([k13], ['mism', 'wrong', 'nonmover', 'gdiff'])}; has a second engine's columns {int('its2' in k13)}")
    tree = git("ls-tree", "-r", "--name-only", "350d84eb", "--", D + "pg", D + "G").split()
    pgk = sorted(int(re.search(r"G_(\d+)_g3", x).group(1)) for x in tree if x.endswith("_g3.pg"))
    gk = sorted(int(re.search(r"G_(\d+)\.json", x).group(1)) for x in tree if "/G/" in x and x.endswith(".json"))
    print(f"linedata at 350d84eb: pg/G_k_g3.pg for k {pgk[0]}..{pgk[-1]} ({len(pgk)} files); G/G_k.json for k {gk[0]}..{gk[-1]} ({len(gk)} files); "
          f"G_13_g3.pg at {C}: {int(bool(show(C, D + 'pg/G_13_g3.pg')))}")
    sz = [l for l in open(os.path.join(HERE, "sizes.out"), encoding="utf-8") if "first" in l and "(n)^" in l]
    print("linedata this lane's sizes.out (stage 1): " + "; ".join(norm(l)[:70] for l in sz))


def balanced(t):
    pairs = {")": "(", "]": "[", "»": "«", "}": "{"}
    st = []
    for i, ch in enumerate(t):
        if ch in "([«{":
            st.append(ch)
        elif ch in pairs:
            if not st or st[-1] != pairs[ch]:
                return False
            st.pop()
    return not st


def top_quotes(t):
    out, depth, start = [], 0, None
    for i, ch in enumerate(t):
        if ch == "«":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "»":
            depth -= 1
            if depth == 0:
                out.append(t[start + 1:i])
    return out


def line_mode(C, L):
    path = f"docs/red-b/P-N5-EXP-line-{L}.txt"
    t = show(C, path)
    print(f"line {L} at {C} {path}: bytes {len(t.encode('utf-8'))} chars {len(t)} sha1 {sha1(t)}")
    print(f"line {L} byte tests: newlines {t.count(chr(10))} (must 1), ends with a newline {int(t.endswith(chr(10)))}, pipes {t.count('|')} (must 0), tabs "
          f"{t.count(chr(9))}, carriage returns {t.count(chr(13))}, double spaces {t.count('  ')} (must 0 each), brackets balanced and properly nested "
          f"{int(balanced(t))}: ( {t.count('(')} ) {t.count(')')} [ {t.count('[')} ] {t.count(']')} {{ {t.count('{')} }} {t.count('}')} « {t.count('«')} » {t.count('»')}; "
          f"begins with a heading marker {int(t.lstrip().startswith('#'))} (L41: must 0)")
    # the quotations at the commits the line names (trunk for RESULTS; R104's packet for the definition)
    trunk = "origin/claude/vibrant-johnson-nxvvxo"
    places = [("RESULTS at trunk", trunk, "docs/RESULTS.md"), ("R104's packet docs/red/P-N5-REALIZE.md at trunk", trunk, "docs/red/P-N5-REALIZE.md"),
              ("claude/referee c881709b docs/referee/R-P-N5-EXP.md", "c881709b", "docs/referee/R-P-N5-EXP.md"),
              ("claude/referee 78515253 docs/referee/R-P-N5-EXP.md", "78515253", "docs/referee/R-P-N5-EXP.md"),
              ("claude/referee-2 f17a2708 docs/referee-2/R2-P-N5-EXP.md (by script only)", "f17a2708", "docs/referee-2/R2-P-N5-EXP.md"),
              ("the frozen packet", "350d84eb", PKT)]
    texts = [(nm, show(c, p).split("\n")) for nm, c, p in places]
    for qq in top_quotes(t):
        nq = norm(qq)
        hits = []
        for nm, ls in texts:
            if nq in norm("\n".join(ls)):
                where = "?"
                for w in range(1, 8):
                    cand = [i + 1 for i in range(len(ls)) if nq in norm(" ".join(ls[i:i + w]))]
                    if cand:
                        where = (f"{cand[0]}" if w == 1 else f"{cand[0]}-{cand[0] + w - 1}") + (f" (and {len(cand) - 1} more places)" if len(cand) > 1 else "")
                        break
                hits.append(f"{nm} l. {where}")
        print(f"line {L} quote «{qq[:64]}{'…' if len(qq) > 64 else ''}» ({len(qq)} chars): " + ("; ".join(hits) if hits else "NOT FOUND"))
    for m in sorted(set(re.findall(r"\b[0-9a-f]{8}\b", t))):
        rc = subprocess.run(["git", "cat-file", "-e", m + "^{commit}"], cwd=q5.TOP, capture_output=True).returncode
        print(f"line {L} id {m}: " + ("a commit in the object store" if rc == 0 else "not a commit (a sha1 prefix of a file: " +
              str([p for p, s in (("the fixes file at 24f4d436", sha1(show('24f4d436', FIXP))),) if s.startswith(m)]) + ")"))
    # difference from the earlier lines of the same commit
    prev = {"L3": "L2", "L4": "L3", "L5": "L4"}.get(L)
    if prev:
        try:
            p = show(C, f"docs/red-b/P-N5-EXP-line-{prev}.txt")
        except SystemExit:
            p = None
        except subprocess.CalledProcessError:
            p = None
        if p is not None:
            sm = difflib.SequenceMatcher(None, p.split(), t.split(), autojunk=False)
            n = 0
            for tag, i1, i2, j1, j2 in sm.get_opcodes():
                if tag != "equal":
                    n += 1
                    print(f"line {L} against {prev}, change {n}: «{' '.join(p.split()[i1:i2])}» -> «{' '.join(t.split()[j1:j2])}»")
            print(f"line {L} against {prev}: word-level changes {n}; {prev} sha1 {sha1(p)}")


if __name__ == "__main__":
    args = sys.argv[1:]
    C = opt(args, "--commit", "10dfedb65")
    start = int(opt(args, "--from", "882"))
    mode = args[0]
    if mode == "entries":
        entries_mode(C, start, False)
    elif mode == "spoil":
        entries_mode(C, start, True)
    elif mode == "pins":
        pins_mode(C, start)
    elif mode == "facts":
        facts_mode(C)
    elif mode == "linedata":
        linedata_mode(C)
    elif mode == "line":
        line_mode(C, args[1])
