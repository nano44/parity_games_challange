#!/usr/bin/env python3
"""tools/landtest.py <draft>: tests of land131.py, all as DRYRUN into docs/agents/tools/r131/tmp/ (the repository's
RESULTS / GAPS / NOW are read, never written).
 T1 the draft as it is: land131.py must REFUSE while open slots remain (or, when none remain, must run).
 T2 a COPY of the draft in which every open-slot word but the title's checker token is replaced by a marker, with
    hashes recomputed for the copy: the DRYRUN must succeed; its results are then examined line by line.
 T3 that copy with one letter of the block changed and T2's hashes: land131.py must REFUSE.
 T4 that copy with a second copy of the open-slot word in its header: land131.py must REFUSE.
The stamp and checker are the fixed values of cfg.json "dryrun". Exit 1 on any failure."""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
from lib131 import OPEN_WORD, ROOT, block_sha1, line_sha1, load_cfg, sha1, split_draft

TMP = os.path.join(HERE, "tmp")


def run(draft, hashes, outdir, cfg):
    env = dict(os.environ, R131_DRAFT=draft, R131_HASHES=hashes, R131_NOW="%s %s" % (cfg["dryrun"]["date"], cfg["dryrun"]["time"]))
    p = subprocess.run([sys.executable, "-B", os.path.join(HERE, "land131.py"), cfg["dryrun"]["checker"], "DRYRUN", outdir], capture_output=True, env=env)
    return p.returncode, p.stdout.decode("utf-8", "replace") + p.stderr.decode("utf-8", "replace")


def rd(p):
    return open(p, encoding="utf-8").read()


def main(path):
    cfg = load_cfg()
    os.makedirs(TMP, exist_ok=True)
    E, PREV, CN = cfg["entry"], cfg["prev_entry"], cfg["checker_number"]
    fails = 0
    text = rd(path)
    nopen = text.count(OPEN_WORD) - 1
    hashes = os.path.join(HERE, "out", "hashes.json")
    stand_in = json.load(open(hashes))["line_stand_in"]
    # T1
    rc, out = run(path, hashes, os.path.join(TMP, "dry1"), cfg)
    want_refuse = nopen > 0 or stand_in
    ok = (rc == 2 and "REFUSED" in out) if want_refuse else rc == 0
    print("T1 the draft as it is (%d open-slot tokens besides the checker token; stand-in line %s): rc %d, %s: %s" % (
        nopen, stand_in, rc, "refused" if "REFUSED" in out else "ran", "as expected" if ok else "UNEXPECTED"))
    for l in out.strip().split("\n")[:3]:
        print("   T1 " + l[:230].replace(OPEN_WORD, "<open-slot word>"))
    fails += not ok
    # T2
    d = split_draft(text, cfg)
    L = list(d["lines"])
    token = "checker %s)" % OPEN_WORD
    assert L[d["b0"]].endswith(token)
    for i in range(len(L)):
        if i == d["b0"]:
            continue
        L[i] = L[i].replace(OPEN_WORD, "closed-for-the-dry-run")
    sat = "\n".join(L)
    ds = split_draft(sat, cfg)
    satp, hp = os.path.join(TMP, "draft.sat.md"), os.path.join(TMP, "hashes.sat.json")
    open(satp, "w", encoding="utf-8").write(sat)
    json.dump({"block_sha1": block_sha1(ds["block"]), "block_lines": len(ds["block"]), "update_sha1": line_sha1(ds["update"]),
               "line_stand_in": False, "line_name": cfg["line"]["name"]}, open(hp, "w"))
    dry = os.path.join(TMP, "dry2")
    rc, out = run(satp, hp, dry, cfg)
    print("T2 satisfied copy (%d tokens replaced; hashes recomputed for the copy): rc %d" % (nopen, rc))
    for l in out.strip().split("\n"):
        print("   T2 " + l[:330])
    ok = rc == 0
    if ok:
        chk = cfg["dryrun"]["checker"]
        R0, R1 = rd(os.path.join(ROOT, "docs/RESULTS.md")).split("\n"), rd(os.path.join(dry, "docs/RESULTS.md")).split("\n")
        G0, G1 = rd(os.path.join(ROOT, "docs/GAPS.md")).split("\n"), rd(os.path.join(dry, "docs/GAPS.md")).split("\n")
        N0, N1 = rd(os.path.join(ROOT, "docs/NOW.md")), rd(os.path.join(dry, "docs/NOW.md"))
        D1 = rd(os.path.join(dry, "docs/agents/R131-draft.md")).split("\n")
        a = [i for i, l in enumerate(R1) if l.startswith("### %s [refereed-only] " % E)]
        er = [i for i, l in enumerate(R1) if l.startswith(cfg["results"]["insert_before_prefix"])]
        nb = len(ds["block"])
        c = []
        c.append(("RESULTS: one %s heading at l. %d, block l. %d-%d, empty l. %d, Erratum line l. %d" % (E, a[0] + 1, a[0] + 1, a[0] + nb, a[0] + nb + 1, er[0] + 1),
                  len(a) == 1 and len(er) == 1 and er[0] == a[0] + nb + 1 and R1[a[0] + nb] == "" and R1[a[0] - 1] == ""))
        c.append(("RESULTS: pure insertion (the %d lines before and the %d lines after are unchanged), %d -> %d lines" % (a[0], len(R0) - a[0], len(R0) - 1, len(R1) - 1),
                  R1[:a[0]] == R0[:a[0]] and R1[a[0] + nb + 1:] == R0[a[0]:] and len(R1) == len(R0) + nb + 1))
        c.append(("RESULTS: the inserted block is the copy's block with the checker token filled (%s once, no open-slot word, no fill token)" % ("checker %s)" % chk),
                  R1[a[0] + 1:a[0] + nb] == ds["block"][1:] and R1[a[0]] == ds["block"][0][:-len(token)] + "checker %s)" % chk
                  and OPEN_WORD not in "\n".join(R1[a[0]:a[0] + nb])))
        hd = [m.group(1) for l in R1 for m in [re.match(r"### (R\d+) \[", l)] if m]
        c.append(("RESULTS: headings %d, the last two %s %s; pipes %d -> %d" % (len(hd), hd[-2], hd[-1], "\n".join(R0).count("|"), "\n".join(R1).count("|")),
                  hd[-2:] == [PREV, E] and "\n".join(R0).count("|") == "\n".join(R1).count("|")))
        gid = cfg["gaps"]["row_id"]
        g0 = [i for i, l in enumerate(G0) if l.startswith("| %s | " % gid)][0]
        g1 = [i for i, l in enumerate(G1) if l.startswith("| %s | " % gid)]
        row0, row1 = G0[g0], G1[g1[0]]
        ci = G1.index(cfg["gaps"]["closed_heading"])
        m = re.match(r"(\| %s \| [^|]+ \| [^|]+ \| )open( \| )" % re.escape(gid), row0)
        upd_f = ds["update"].replace("<DATE>", cfg["dryrun"]["date"]).replace("<HH:MM>", cfg["dryrun"]["time"]).replace("<checker>", chk)
        exp = m.group(1) + "closed" + m.group(2) + row0[m.end():-1] + upd_f + " |"
        c.append(("GAPS: the row is the old row with status closed and ' ' + UPDATE + ' ¦' appended, nothing else (%d -> %d characters)" % (len(row0), len(row1)),
                  len(g1) == 1 and row1 == exp))
        c.append(("GAPS: row l. %d -> l. %d, below the closed heading (l. %d), the last table row of the file; every other line unchanged; %d -> %d lines" % (
            g0 + 1, g1[0] + 1, ci + 1, len(G0) - 1, len(G1) - 1),
            g1[0] > ci and G1[g1[0] + 1:] == [""] and [l for l in G1 if l != row1] == [l for l in G0 if l != row0] and len(G0) == len(G1)))
        cells = [x.strip() for x in row1.strip().strip("|").split("|")]
        c.append(("GAPS: check_docs cells of the row: id %s, severity %s, owner present %s, status %s; row pipes %d -> %d" % (
            cells[0], cells[1], bool(cells[2]), cells[3], row0.count("|"), row1.count("|")), cells[3] == "closed" and row0.count("|") == row1.count("|")))
        ups = re.findall(r"UPDATE \d{4}-\d\d-\d\d \d\d:\d\dZ: RESULTS (R\d+) ", row1)
        c.append(("GAPS: RESULTS UPDATEs on the row %d -> %d, the last three %s" % (len(ups) - 1, len(ups), " ".join(ups[-3:])), ups[-2:] == [PREV, E]))
        diff = [(x, y) for x, y in zip(N0.split("\n"), N1.split("\n")) if x != y]
        c.append(("NOW: %d line(s) differ, %d -> %d lines; only the cfg replacements" % (len(diff), N0.count("\n"), N1.count("\n")),
                  N1 == _rep(N0, cfg) and len(diff) == len(cfg["now"]["replacements"])))
        c.append(("draft copy: first line ends with the landing note, the rest unchanged",
                  D1[0] == L[0] + " — LANDED in RESULTS %s %sZ (CHECKER %s %s PASS), after %s, before Erratum E-1" % (
                      cfg["dryrun"]["date"], cfg["dryrun"]["time"], CN, chk, PREV) and D1[1:] == L[1:]))
        p = subprocess.run([sys.executable, "-B", os.path.join(dry, "scripts", "check_docs.py")], capture_output=True)
        c.append(("scripts/check_docs.py on the copies: rc %d" % p.returncode, p.returncode == 0))
        bad = os.path.join(dry, "docs", "RESULTS.md")
        t = rd(bad)
        open(bad, "w", encoding="utf-8").write(t.replace("### %s [refereed-only] " % E, "### %s " % E))
        p = subprocess.run([sys.executable, "-B", os.path.join(dry, "scripts", "check_docs.py")], capture_output=True)
        c.append(("negative control (the landed title without its label): check_docs rc %d, message names the entry %s" % (
            p.returncode, ("### %s " % E) in p.stdout.decode("utf-8", "replace")), p.returncode == 1))
        open(bad, "w", encoding="utf-8").write(t)
        print("   T2 sha1 of the results: RESULTS %s GAPS %s NOW %s" % (sha1(t.encode()), sha1("\n".join(G1).encode()), sha1(N1.encode())))
        for name, good in c:
            print("   T2 %s %s" % ("OK  " if good else "FAIL", name))
            ok = ok and good
    fails += not ok
    # T3
    i = d["b0"] + 3
    L3 = list(L)
    j = len(L3[i]) // 2
    L3[i] = L3[i][:j] + ("x" if L3[i][j] != "x" else "y") + L3[i][j + 1:]
    p3 = os.path.join(TMP, "draft.t3.md")
    open(p3, "w", encoding="utf-8").write("\n".join(L3))
    rc, out = run(p3, hp, os.path.join(TMP, "dry3"), cfg)
    ok = rc == 2 and "REFUSED" in out and "block" in out
    print("T3 the copy with one letter of the block changed, T2's hashes: rc %d: %s" % (rc, out.strip().split("\n")[0][:200]))
    fails += not ok
    # T4
    L4 = list(L)
    L4[1] = L4[1] + " " + OPEN_WORD
    p4 = os.path.join(TMP, "draft.t4.md")
    open(p4, "w", encoding="utf-8").write("\n".join(L4))
    rc, out = run(p4, hp, os.path.join(TMP, "dry4"), cfg)
    ok = rc == 2 and "REFUSED" in out
    print("T4 the copy with one more open-slot word in its header: rc %d: %s" % (rc, out.strip().split("\n")[0][:200].replace(OPEN_WORD, "<open-slot word>")))
    fails += not ok
    print("landtest: %s" % ("PASS" if fails == 0 else "FAILED"))
    return 1 if fails else 0


def _rep(n, cfg):
    for old, new, _ in cfg["now"]["replacements"]:
        n = n.replace(old, new)
    return n


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
