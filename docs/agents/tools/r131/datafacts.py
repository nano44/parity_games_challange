#!/usr/bin/env python3
"""DATA facts of R131, read from the lane's PINNED outputs at the l-red-b commit cfg.json names (git show), with
the arithmetic of the entry recomputed in exact integers. Used by fill131.py (numbers printed in the draft) and by
tools/data.py (the same facts as a list of checks, with a negative control).

Every check is (name, ok, detail). Nothing of the lane is executed here: the outputs are read, not regenerated.
"""
import json

from lib131 import sha1, show


def kv(line):
    """'G_3 mode spec ctrl 0 N 11 ...' -> ('G_3', {'mode': 'spec', 'ctrl': '0', 'N': '11', ...}) (pairs after the name)."""
    t = line.split()
    d, i = {}, 1
    while i + 1 < len(t):
        d.setdefault(t[i], t[i + 1])
        i += 2
    return t[0], d


def rows(commit, path):
    return [kv(l) for l in show(commit, path).decode("utf-8").split("\n") if l.strip()]


def gk(name):
    return int(name.split("_")[1].split(".")[0])


def first_beyond(c, with_m):
    k = 3
    while True:
        n = 135 * k - 230
        m = 176 * k - 300
        size = n + m if with_m else n
        if 2 ** k - 1 > size ** c:
            return k, size, 2 ** k - 1, size ** c
        k += 1


def facts(cfg):
    H = cfg["heads"]["l-red-b"]
    FZ = cfg["packet"]["freeze_commit"]
    D = "experiments/red-b/data/b6b/"
    O = D + "out/"
    C = []                                 # checks
    F = {}                                 # facts for the draft

    def chk(name, ok, detail):
        C.append((name, bool(ok), detail))

    def z(d, keys):
        return all(d.get(x) == "0" for x in keys)

    # D1 membership
    r = rows(H, O + "member.out")
    ks = [gk(n) for n, _ in r]
    ok = ks == list(range(3, 15)) and all(
        d["member"] == "1" and z(d, ["viol", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"])
        and int(d["N"]) == 9 * k - 16 and int(d["M"]) == 18 * k - 32 and int(d["d"]) == k + 1
        for k, (_, d) in zip(ks, r))
    chk("member.out", ok, "G_3..G_14: member 1, viol and c1..c8 0, N = 9k - 16, M = 18k - 32, d = k + 1 on %d lines" % len(r))
    r = rows(H, O + "member_ctrl.out")
    chk("member_ctrl.out", len(r) == 8 and all(d["member"] == "0" and int(d["viol"]) >= 1 for _, d in r),
        "%d damaged copies of G_5, each member 0 and viol >= 1" % len(r))
    # D3 the run on three simulators
    r = rows(H, O + "sim.out")
    ks = [gk(n) for n, _ in r]
    ok = ks == list(range(3, 15)) and all(
        int(d["T"]) == int(d["TB"]) == int(d["TC"]) == 2 ** k - 2 and d["ideq"] == "0" and d["stop"] == "stuck"
        and int(d["maxsw"]) == 2 ** (k - 2) and int(d["sumsw"]) == 11 * 2 ** (k - 2) - 9 for k, (_, d) in zip(ks, r))
    chk("sim.out", ok, "k = 3..14: T = TB = TC = 2^k - 2, ideq 0, stop stuck, maxsw 2^(k-2), sumsw 11*2^(k-2) - 9")
    F["howard_max"] = max(int(d["howard"]) for _, d in r)
    chk("sim.out howard", F["howard_max"] == 4, "Howard's rule on the model: at most %d steps" % F["howard_max"])
    # D4 the proof's facts on the run
    r = rows(H, O + "lemma.out")
    ks = [gk(n) for n, _ in r]
    ok = ks == list(range(3, 15)) and all(
        z(d, ["kfact", "vfact", "sched", "tlen", "rest", "swk"]) and int(d["T"]) == 2 ** k - 2
        and int(d["moves"]) == 11 * 2 ** (k - 2) - 9 and int(d["states"]) == 2 ** k - 1 for k, (_, d) in zip(ks, r))
    chk("lemma.out", ok, "k = 3..14: kfact, vfact, sched, tlen, rest, swk 0; T = 2^k - 2; moves 11*2^(k-2) - 9")
    r = rows(H, O + "lemma_ctrl.out")
    chk("lemma_ctrl.out", len(r) == 2 and r[0][1]["sched"] == "19" and r[1][1]["kfact"] == "25",
        "control 1 sched %s, control 2 kfact %s (both fire)" % (r[0][1]["sched"], r[1][1]["kfact"]))
    # D6 N5 itself, k = 3..11 (two engines), k = 12 (two engines), k = 13 (engine 1)
    r = rows(H, O + "n5.out")
    ks = [gk(n) for n, _ in r]

    def n5ok(k, d, two):
        base = (int(d["n"]) == 135 * k - 230 and int(d["T1p"]) == int(d["F"]) == 2 ** k - 2 and int(d["its"]) == 2 ** k + 1
                and d["fb"] == "1" and z(d, ["mism", "wrong", "nonmover", "gdiff"])
                and d["pg_sha1"] == sha1(show(H, D + "pg/G_%d_g3.pg" % k)))
        if two:
            base = base and int(d["its2"]) == 2 ** k + 1 and d["fb2"] == "1" and z(d, ["wrong2", "engdiff"])
        return base

    chk("n5.out", ks == list(range(3, 12)) and all(n5ok(k, d, True) for k, (_, d) in zip(ks, r)),
        "k = 3..11: n = 135k - 230, T1p = F = 2^k - 2, its = its2 = 2^k + 1, fb = fb2 = 1, mism, wrong, nonmover, wrong2, "
        "engdiff, gdiff 0, pg_sha1 = sha1 of the pinned game file")
    F["n5_its"] = {k: int(d["its"]) for k, (_, d) in zip(ks, r)}
    r12 = rows(H, O + "n5_k12.out")
    chk("n5_k12.out", len(r12) == 1 and gk(r12[0][0]) == 12 and n5ok(12, r12[0][1], True),
        "k = 12: its = its2 = %s on n = %s, one fallback, the six counters 0" % (r12[0][1]["its"], r12[0][1]["n"]))
    F["n5_its"][12] = int(r12[0][1]["its"])
    r13 = rows(H, O + "n5_k13.out")
    d13 = r13[0][1]
    chk("n5_k13.out", len(r13) == 1 and gk(r13[0][0]) == 13 and n5ok(13, d13, False) and "its2" not in d13,
        "k = 13, engine 1 only: its %s on n = %s, fb %s, F %s, mism, wrong, nonmover, gdiff 0" % (d13["its"], d13["n"], d13["fb"], d13["F"]))
    F["n5_its"][13] = int(d13["its"])
    r = rows(H, O + "n5ck_check.out")
    chk("n5ck_check.out", len(r) == 6 and all(int(d["its"]) == 2 ** gk(n) + 1 and z(d, ["mism", "wrong", "nonmover", "gdiff"]) for n, d in r),
        "the checkpointed driver on k = 3..8: the frozen values")
    # D9 sizes and explicit bounds
    txt = show(H, O + "size.out").decode("utf-8").split("\n")
    sz = [kv(l) for l in txt if l.startswith("G_")]
    ok = len(sz) == 9 and all(int(d["n"]) == 135 * int(d["k"]) - 230 and int(d["m"]) == 176 * int(d["k"]) - 300 and d["sizediff"] == "0" for _, d in sz)
    chk("size.out sizes", ok, "nine .pg files: n = 135k - 230, m = 176k - 300, sizediff 0")
    F["smallest"] = (int(sz[0][1]["n"]), int(sz[0][1]["m"]))
    fl = [l for l in txt if l.startswith("first k with")]
    exp = []
    F["beyond"] = {}
    for c in (2, 3, 4):
        for wm in (False, True):
            k, size, lhs, rhs = first_beyond(c, wm)
            F["beyond"]["%s^%d" % ("n+m" if wm else "n", c)] = (k, size, lhs, rhs)
            exp.append("first k with 2^k - 1 > (%s)^%d: k %d size %d iterations_bound %d poly %d" % ("n+m" if wm else "n", c, k, size, lhs, rhs))
    chk("size.out bounds", fl == exp, "the six 'first k' lines equal exact-integer recomputation: k = " + ", ".join(
        "%d" % F["beyond"][x][0] for x in ("n^2", "n^3", "n^4", "n+m^2", "n+m^3", "n+m^4")))
    r = rows(H, O + "size_k13.out")
    chk("size_k13.out", r[0][1]["n"] == "1525" and r[0][1]["m"] == "1988" and r[0][1]["sizediff"] == "0" and r[1][1]["sizediff"] == "1",
        "k = 13: n 1525, m 1988, sizediff 0; control fires")
    # D11 LEMMA', CAUSAL, STABLE direct tests
    r = rows(H, O + "prefix_run.out")
    r0 = [(n, d) for n, d in r if d["ctrl"] == "0"]
    ks = [gk(n) for n, _ in r0]
    w, p = sum(int(d["windows"]) for _, d in r0), sum(int(d["pairs"]) for _, d in r0)
    ok = ks == list(range(3, 15)) and all(z(d, ["h1", "h2", "h2last", "psched", "empty"]) and int(d["windows"]) == 2 ** (k - 1) - 1 for k, (_, d) in zip(ks, r0))
    chk("prefix_run.out", ok and w == 16368 and p == 376836, "k = 3..14: h1, h2, h2last, psched, empty 0 at %s windows, %s (window, step) pairs" % (w, p))
    F["windows"], F["pairs"] = w, p
    r = rows(H, O + "prefix_all.out")
    r0 = [(n, d) for n, d in r if d["ctrl"] == "0"]
    ks = [gk(n) for n, _ in r0]
    tr = sum(int(d["triples"]) for _, d in r0)
    ok = ks == list(range(3, 13)) and all(d["aviol"] == "0" and int(d["windows"]) == int(d["expected"]) == 2 ** (k - 1) - 1 for k, (_, d) in zip(ks, r0))
    chk("prefix_all.out", ok and tr == 163970, "k = 3..12: aviol 0, windows = expected = 2^(k-1) - 1, %s triples" % tr)
    F["triples"] = tr
    lines = [l for l in show(H, O + "prefix_ctrl.out").decode("utf-8").split("\n") if " ctrl 5 " in l]
    fr = [(gk(l.split()[0]), int(kv(l)[1]["frozen_conclusion_fails"])) for l in lines]
    chk("prefix_ctrl.out", [k for k, _ in fr] == list(range(3, 9)) and all(f == k - 1 for k, f in fr),
        "control 5 (the lemma as frozen), k = 3..8: fails at exactly k - 1 triples per k: " + " ".join("%d" % f for _, f in fr))
    r = [(n, d) for n, d in rows(H, O + "prefix_off.out") if d["ctrl"] == "0"]
    a = (sum(int(d["windows"]) for _, d in r), sum(int(d["proper"]) for _, d in r), sum(int(d["steps"]) for _, d in r))
    chk("prefix_off.out", all(d["pviol"] == "0" for _, d in r) and a == (42902, 1089, 346644), "pviol 0 on %d windows (%d proper), %d steps" % a)
    F["off"] = a
    r = [(n, d) for n, d in rows(H, O + "prefix_drive.out") if d["ctrl"] == "0"]
    a = (sum(int(d["windows"]) for _, d in r), sum(int(d["proper"]) for _, d in r), sum(int(d["steps"]) for _, d in r))
    chk("prefix_drive.out", all(d["dviol"] == "0" for _, d in r) and a == (28000, 16423, 190500), "dviol 0 on %d driven windows (%d proper), %d steps" % a)
    F["drive"] = a
    r = [(n, d) for n, d in rows(H, O + "prefix_loc.out") if d["ctrl"] == "0"]
    a = (sum(int(d["states"]) for _, d in r), sum(int(d["hits"]) for _, d in r))
    chk("prefix_loc.out", all(d["loc"] == "0" for _, d in r) and a == (81000, 78534), "loc 0 on %d states (%d repeated triples)" % a)
    F["loc"] = a
    r = [(n, d) for n, d in rows(H, O + "prefix_stable.out") if d["ctrl"] == "0"]
    a = sum(int(d["cases"]) for _, d in r)
    chk("prefix_stable.out", all(d["stviol"] == "0" for _, d in r) and a == 14698, "stviol 0 on %d cases" % a)
    F["stcases"] = a
    r = [(n, d) for n, d in rows(H, O + "prefix_u0.out") if d["ctrl"] == "0"]
    chk("prefix_u0.out", len(r) == 4 and all(d["c0e0"] == "0" and int(d["c0e0_u0free"]) > 0 for _, d in r), "c0e0 0 on 8,000 states per k, k = 3..6; with u_0 free the count is positive")
    r = [(n, d) for n, d in rows(H, O + "prefix_exh.out") if d["ctrl"] == "0"]
    chk("prefix_exh.out", [d["states"] for _, d in r] == ["512", "65536"] and all(z(d, ["c0e0", "loc", "stviol", "pviol"]) for _, d in r),
        "every state of G_3 (512) and G_4 (65,536) with the wires and u_0 at 0: c0e0, loc, stviol, pviol 0")
    # D20 strategies, enabling predicates, renumberings, R117's side conditions
    r = rows(H, O + "strat.out")
    r2 = rows(H, O + "n5_clean.out")
    chk("strat.out, n5_clean.out", [gk(n) for n, _ in r] == list(range(3, 9)) and [gk(n) for n, _ in r2] == list(range(3, 11))
        and all(d["badstrat"] == "0" for _, d in r + r2), "badstrat 0 for k = 3..8 (strat.out) and k = 3..10 (n5_clean.out)")
    r = rows(H, O + "enab.out")
    chk("enab.out", [gk(n) for n, _ in r] == list(range(3, 13)) and all(z(d, ["venab", "kenab", "movd"]) for _, d in r), "k = 3..12: venab, kenab, movd 0")
    r = rows(H, O + "perm.out")
    a = sum(int(d["perms"]) for _, d in r)
    chk("perm.out", all(d["keep"] == "0" for _, d in r) and a == 7050, "keep 0 on %d relabelings" % a)
    r = rows(H, O + "reach.out")
    chk("reach.out", [gk(n) for n, _ in r] == list(range(3, 9)) and all(z(d, ["startdiff", "padcyc", "padp", "fbpos"]) for _, d in r), "k = 3..8: startdiff, padcyc, padp, fbpos 0")
    # D21 pins: every SHA1SUMS_b6b* file of the lane at the head
    from lib131 import git
    pinfiles = sorted(x.split("/")[-1] for x in git("ls-tree", "-r", "--name-only", H, "--", D).decode().split("\n")
                      if x.split("/")[-1].startswith("SHA1SUMS_b6b"))
    tot, bad = 0, 0
    for f in pinfiles:
        for l in show(H, D + f).decode("utf-8").split("\n"):
            if l.strip():
                h, p = l.split()
                tot += 1
                bad += sha1(show(H, D + p)) != h
    chk("pins", bad == 0 and tot >= 81 and len(pinfiles) >= 4, "%d pinned files of %d pin files (%s): %d mismatches" % (tot, len(pinfiles), ", ".join(pinfiles), bad))
    F["pins"], F["pinfiles"] = tot, pinfiles
    # entry 7's direct test of clause (R3) as read (present from fixes entry 7 on)
    from lib131 import exists
    if exists(H, O + "e7_r3.out"):
        r = [(n, d) for n, d in rows(H, O + "e7_r3.out") if d["ctrl"] == "0"]
        a = (sum(int(d["windows"]) for _, d in r), sum(int(d["windows2"]) for _, d in r))
        chk("e7_r3.out", [gk(n) for n, _ in r] == list(range(3, 15)) and all(z(d, ["r3in", "r3move", "r3rest", "litdiff"]) for _, d in r) and a == (16368, 16356),
            "k = 3..14: r3in, r3move, r3rest, litdiff 0 at %d windows (%d with j >= 2)" % a)
        F["r3"] = a
    # fixes entry 10: the rank gloss (rule R against the old wording of the lines)
    if exists(H, O + "gloss.out"):
        r = rows(H, O + "gloss.out")
        chk("gloss.out", [gk(n) for n, _ in r] == list(range(3, 13)) and all(
            z(d, ["rulediff", "Ldiff", "wire0diff"]) and int(d["Lrule"]) == 2 ** gk(n) - 2 and d["Loldinc"] == "3" and d["Lolddec"] == "1"
            and d["oldfires"] == "2" and d["member"] == "1" for n, d in r),
            "k = 3..12: rulediff, Ldiff, wire0diff 0 (rule R: L = 2^k - 2); the old gloss of the lines gives L = 3 and L = 1 on every k (control fires)")
        F["gloss"] = True
    # the chain of lines L-1 -> ... -> the line of cfg.json, by the lane's own build records
    import re as _re
    last = int(cfg["line"]["name"].split("-")[1])
    P = "docs/red-b/P-N5-EXP-line-L%d.txt"
    prev = show(H, P % 1).decode("utf-8")
    names, okc, det = {}, True, []
    F["lines"] = {1: (sha1(show(H, P % 1)), len(show(H, P % 1)))}
    for i in range(2, last + 1):
        rec = show(H, O + "line_L%d_build.out" % i).decode("utf-8").split("\n")
        items = []
        for j, l in enumerate(rec):
            m = _re.match(r"--- (.+): at character (\d+) of L-%d, " % (i - 1), l)
            if m:
                items.append((int(m.group(2)), m.group(1), rec[j + 1][2:], rec[j + 2][2:]))
        cur = prev[:-1]
        for pos, name, old, new in sorted(items, reverse=True):
            okc = okc and cur[pos:pos + len(old)] == old and cur.count(old) >= 1
            cur = cur[:pos] + new + cur[pos + len(old):]
        nxt = show(H, P % i).decode("utf-8")
        okc = okc and cur + "\n" == nxt and len(items) >= 1
        names[i] = [n for _, n, _, _ in sorted(items)]
        det.append("L-%d -> L-%d: %d (%s)" % (i - 1, i, len(items), ", ".join(names[i])))
        F["lines"][i] = (sha1(nxt.encode("utf-8")), len(nxt.encode("utf-8")))
        prev = nxt
    chk("line chain", okc and F["lines"][last][0] == cfg["line"]["expect_sha1"],
        "each line is the one before it with the named replacements of the lane's build record applied at their recorded characters, byte for byte: " + "; ".join(det))
    F["line_names"] = names
    chk("frozen pins", show(H, D + "SHA1SUMS_b6b") == show(FZ, D + "SHA1SUMS_b6b"), "SHA1SUMS_b6b byte-equal at the freeze commit and at the head")
    # D23 arithmetic: every measured run is below n^2
    below = all(F["n5_its"][k] < (135 * k - 230) ** 2 for k in F["n5_its"])
    k23 = F["beyond"]["n^2"]
    chk("below n^2", below and sorted(F["n5_its"]) == list(range(3, 14)) and k23[0] == 23 and k23[1] == 2875
        and 2 ** 22 - 1 < (135 * 22 - 230) ** 2 and 2 ** 20 - 2 < (135 * 20 - 230) ** 2,
        "N5 itself, k = 3..13: 2^k + 1 < n^2 at every k (k = 13: %d < %d); the model's k = 20: %d < %d; 2^k - 1 > n^2 first at k = %d (n = %d: %d > %d)"
        % (F["n5_its"][13], 1525 ** 2, 2 ** 20 - 2, (135 * 20 - 230) ** 2, k23[0], k23[1], k23[2], k23[3]))
    F["above_n_from"] = min(k for k in F["n5_its"] if F["n5_its"][k] > 135 * k - 230)
    F["above_nm_from"] = min(k for k in F["n5_its"] if F["n5_its"][k] > 311 * k - 530)
    chk("above n, n + m", F["above_n_from"] == 11 and F["above_nm_from"] == 12, "2^k + 1 > n from k = %d and > n + m from k = %d" % (F["above_n_from"], F["above_nm_from"]))
    # D24 the genomes of record
    ok = True
    for k in range(3, 15):
        g = json.loads(show(H, D + "G/G_%d.json" % k).decode("utf-8"))
        ok = ok and g["N"] == 9 * k - 16 and g["deg"] == 2 and len(g["lev"]) == g["N"] and max(g["lev"]) == k and all(x == 0 for x in g["bp"])
    chk("genomes", ok, "G_3..G_14 (JSON): N = 9k - 16, deg 2, levels 0..k, all parities 0")
    return F, C
