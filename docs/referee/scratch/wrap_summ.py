#!/usr/bin/env python3
"""REFEREE successor 33: summary of wrap_logs/ (one line per set; a parsed table, so that no number is read by eye).
Usage: wrap_summ.py [PREFIX ...]   default: main_ exh_ ctrl_"""
import sys, os, re, glob
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wrap_logs")
pref = sys.argv[1:] or ["main_", "exh_", "ctrl_"]
for p in pref:
    agg = {}
    for f in sorted(glob.glob(os.path.join(d, p + "*.out"))):
        lines = open(f).read().split("\n"); head = [l for l in lines if l.startswith("mode ")]
        fails = sum(1 for l in lines if l.startswith("FAIL")); bad = sum(1 for l in lines if "Traceback" in l or "Error" in l)
        if not head: print(os.path.basename(f), "NO SUMMARY LINE (unfinished?)", "FAIL lines", fails, "errors", bad); continue
        h = head[0]; cnt = {}
        for l in lines:
            m = re.fullmatch(r"(\w+) (\d+)", l.strip())
            if m: cnt[m.group(1)] = int(m.group(2))
        g = re.search(r"games (\d+)", h); r = re.search(r"runs (\d+)", h); mt = re.search(r"maxT (\d+) sumT (\d+) maxF (\d+) max\|W\| (\d+)", h)
        mode = h.split()[1]; perm = re.search(r"PERM (\d)", h).group(1); ctrl = re.search(r"CTRL (\d+)", h).group(1)
        nz = {k: v for k, v in cnt.items() if v}
        print(f"{os.path.basename(f):38s} mode {mode:4s} PERM {perm} CTRL {ctrl} games {g.group(1):>6s} runs {r.group(1) if r else '-':>7s} maxT {mt.group(1):>2s} "
              f"sumT {mt.group(2):>6s} maxF {mt.group(3):>2s} max|W| {mt.group(4):>4s} counters {len(cnt)} nonzero {nz} FAIL-lines {fails} errors {bad}")
        key = (p, mode, perm, ctrl); a = agg.setdefault(key, dict(files=0, games=0, runs=0, maxT=0, sumT=0, maxF=0, maxW=0, tot=0, cnt={}))
        a["files"] += 1; a["games"] += int(g.group(1)); a["runs"] += int(r.group(1)) if r else int(g.group(1))
        a["maxT"] = max(a["maxT"], int(mt.group(1))); a["sumT"] += int(mt.group(2)); a["maxF"] = max(a["maxF"], int(mt.group(3)))
        a["maxW"] = max(a["maxW"], int(mt.group(4))); a["tot"] += sum(cnt.values())
        for k, v in cnt.items(): a["cnt"][k] = a["cnt"].get(k, 0) + v
    for key, a in sorted(agg.items()):
        print(f"TOTAL {key[0]} mode {key[1]} PERM {key[2]} CTRL {key[3]}: files {a['files']} runs {a['runs']} maxT {a['maxT']} sumT {a['sumT']} maxF {a['maxF']} "
              f"max|W| {a['maxW']} sum of all counters {a['tot']} nonzero {{k: v for k, v in a['cnt'].items() if v}}".replace("{k: v for k, v in a['cnt'].items() if v}", str({k: v for k, v in a['cnt'].items() if v})))
