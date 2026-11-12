#!/usr/bin/env python3
"""Markdown tables for docs/red-b/B1-box208.md from the files in data/ (L-RED-B). Usage: summ_b1.py exh | climbs"""
import sys, re, glob, os

def sweepline(f):
    l = open(f).read().strip().splitlines()[-1]
    runs = int(re.search(r"runs (\d+)", l).group(1)); viol = int(re.search(r"viol (\d+)", l).group(1))
    p = l.split("|"); cnt = sum(int(x) for x in p[1].split()[1::2])
    cov = {k: int(v) for k, v in zip(p[2].split()[0::2], p[2].split()[1::2])}
    mx = {k: float(v) for k, v in zip(p[3].split()[0::2], p[3].split()[1::2])}
    return runs, viol, cnt, cov, mx

def exh():
    tiers = {}
    for f in sorted(glob.glob("data/exh_N*_M*.out")):
        m = re.match(r"exh_N(\d+)_M(\d+)(?:_p(\d+)of(\d+))?\.out", os.path.basename(f))
        key = (int(m.group(2)), int(m.group(1)))
        t = tiers.setdefault(key, {"runs": 0, "cnt": 0, "viol": 0, "cov": {}, "T": 0, "chunks": 0, "of": int(m.group(4)) if m.group(4) else 1})
        runs, viol, cnt, cov, mx = sweepline(f)
        t["runs"] += runs; t["cnt"] += cnt; t["viol"] += viol; t["chunks"] += 1; t["T"] = max(t["T"], int(mx.get("max_T", 0)))
        for k, v in cov.items(): t["cov"][k] = t["cov"].get(k, 0) + v
    print("| (N, M) | genomes (all, each once) | chunks done | sum of the 27 must-0 counters (all refs) | descriptive |")
    print("| --- | --- | --- | --- | --- |")
    tot = 0
    for (M, N) in sorted(tiers):
        t = tiers[(M, N)]; c = t["cov"]; tot += t["runs"]
        print("| (%d, %d) | %s | %d of %d | %d | max T %d; stalls %s (loud %s), plateaus %s, beta %s, cov_tie %s |" % (
            N, M, format(t["runs"], ","), t["chunks"], t["of"], t["cnt"], t["T"], format(c["stalls"], ","), c["stallloud"],
            format(c["plateaus"], ","), format(c["beta"], ","), format(c["cov_tie"], ",")))
    print("Total %s genomes." % format(tot, ","))

def climbs():
    print("| objective | seed | caps (N, M) | start | iterations | best run found (the climb's last «best» line) | candidates with a non-zero counter |")
    print("| --- | --- | --- | --- | --- | --- | --- |")
    for f in sorted(glob.glob("data/climb2_*.out")):
        m = re.match(r"climb2_([A-Za-z0-9]+)_s(\d+)_N(\d+)_M(\d+)(?:_(.*))?\.out", os.path.basename(f))
        ls = open(f).read().splitlines()
        done = [l for l in ls if l.startswith("CLIMB2")]
        best = [l for l in ls if l.startswith("it ")]
        b = best[-1] if best else ""
        b = re.sub(r"\s+\d+s$", "", b); b = re.sub(r"^it \d+ best \d+ ", "", b)
        if done:
            it = re.search(r"done it (\d+)", done[-1]).group(1); viol = re.search(r"viol (\d+)", done[-1]).group(1)
        else: it, viol = "running", "?"
        print("| %s | %s | (%s, %s) | %s | %s | %s | %s |" % (m.group(1), m.group(2), m.group(3), m.group(4), m.group(5) or "random", it, b, viol))

if __name__ == "__main__":
    {"exh": exh, "climbs": climbs}[sys.argv[1]]()
