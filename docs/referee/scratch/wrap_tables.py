#!/usr/bin/env python3
"""REFEREE successor 33: the tables of R-WRAP-preread.md section 5, generated from wrap_logs/ (no number is typed by hand).
Usage: wrap_tables.py            print the four tables (also written to wrap_logs/summ.out)
       wrap_tables.py splice F   replace the markers @@TABLE_MAIN@@, @@TABLE_CTRL@@, @@TABLE_F11@@, @@TABLE_INST@@, @@MAXT@@ in file F"""
import sys, os, re, glob
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wrap_logs")
fmt = lambda x: f"{x:,}"

def parse(f):
    lines = open(f).read().split("\n"); head = [l for l in lines if l.startswith("mode ")]
    if not head: return None
    h = head[0]; cnt = {}
    for l in lines:
        m = re.fullmatch(r"(\w+) (\d+)", l.strip())
        if m: cnt[m.group(1)] = int(m.group(2))
    g = re.search(r"games (\d+)", h); r = re.search(r"runs (\d+)", h); mt = re.search(r"maxT (\d+) sumT (\d+) maxF (\d+) max\|W\| (\d+)", h)
    return dict(mode=h.split()[1], perm=re.search(r"PERM (\d)", h).group(1), ctrl=re.search(r"CTRL (\d+)", h).group(1), runs=int((r or g).group(1)),
                maxT=int(mt.group(1)), sumT=int(mt.group(2)), maxF=int(mt.group(3)), maxW=int(mt.group(4)), cnt=cnt,
                fails=sum(1 for l in lines if l.startswith("FAIL")), ncnt=len(cnt))

def table_main():
    out = ["| set | mode | index order | files | runs (H, s0) | max T | sum T | max F | max \\|W\\| | sum of the 18 counters | FAIL lines |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    groups = {}; unfinished = []; maxT = 0
    for f in sorted(glob.glob(os.path.join(d, "main_*.out")) + glob.glob(os.path.join(d, "exh_*.out"))):
        b = os.path.basename(f); p = parse(f)
        if p is None: unfinished.append(b); continue
        assert p["ncnt"] == 18 and p["ctrl"] == "0", b
        if b.startswith("main_"):
            fam = b.split("_")[2]; key = ("random, family " + fam, p["mode"], p["perm"])
        else:
            n = re.search(r"_n(\d)", b).group(1); key = (f"exhaustive, {n} vertices, priorities 0-2", p["mode"], p["perm"])
        a = groups.setdefault(key, dict(files=0, runs=0, maxT=0, sumT=0, maxF=0, maxW=0, tot=0, fails=0))
        a["files"] += 1; a["runs"] += p["runs"]; a["maxT"] = max(a["maxT"], p["maxT"]); a["sumT"] += p["sumT"]; a["maxF"] = max(a["maxF"], p["maxF"])
        a["maxW"] = max(a["maxW"], p["maxW"]); a["tot"] += sum(p["cnt"].values()); a["fails"] += p["fails"]; maxT = max(maxT, p["maxT"])
    tr = tt = 0
    for key in sorted(groups):
        a = groups[key]; tr += a["runs"]; tt += a["tot"]
        tcol = (f"{a['maxT']} | {fmt(a['sumT'])}") if key[1] == "xi" else "n/a | n/a"
        out.append(f"| {key[0]} | {'N5′-xi' if key[1] == 'xi' else 'N5 (spec)'} | {'random (PERM 1)' if key[2] == '1' else 'as built'} | {a['files']} | {fmt(a['runs'])} | {tcol} | {a['maxF']} | {a['maxW']} | {a['tot']} | {a['fails']} |")
    out.append(f"| all rows | | | | {fmt(tr)} | | | | | {tt} | |")
    if unfinished: out.append("UNFINISHED: " + ", ".join(unfinished))
    return "\n".join(out), maxT, unfinished

def table_ctrl():
    out = ["| control | N5′-xi: counters that fire (count) | N5 (spec): counters that fire (count) |", "| --- | --- | --- |"]
    desc = {1: "1 best := worst in the Howard test", 2: "2 T shifted by one", 3: "3 standard state of another s0′", 4: "4 expected regions with K2 flipped",
            5: "5 wrapper: y of Ω 1, pb of Ω 2", 6: "6 wrapper without pe_o", 7: "7 wrapper with 5-edge Odd paths", 8: "8 wrapper with c_W of Ω 4",
            9: "9 inverted expectations (κ1 / κ2 swapped, K1 as a pad, v5 inverted, rem3 against 0)"}
    fired = set()
    for c in range(1, 10):
        cells = []
        for mode in ("xi", "spec"):
            p = parse(os.path.join(d, f"ctrl_{c}_{mode}.out")); nz = {k: v for k, v in p["cnt"].items() if v}; fired |= set(nz)
            cells.append(", ".join(f"{k} {fmt(v)}" for k, v in nz.items()) or "none")
        out.append(f"| {desc[c]} | {cells[0]} | {cells[1]} |")
    allc = list(parse(os.path.join(d, "ctrl_1_xi.out"))["cnt"])
    out.append(f"  Counters with no firing control: {', '.join(k for k in allc if k not in fired) or 'none'} (of {len(allc)}).")
    return "\n".join(out)

def table_f11():
    rx = re.compile(r"n (\d+) VER (\w+) nodes (\d+) edges (\d+) maxprio (\d+) \| T (\d+) 2\^n (\d+) 9\*2\^n-10 (\d+) states (\d+) \| (.*?)(?: \| WRAP (\w+) \|W\| (\d+) its (\d+) F (\d+) fallbacks (\d+) T_W (\S+) its-T (-?\d+) \| (.*))?$")
    H = {}; Wr = {}
    for f in sorted(glob.glob(os.path.join(d, "f11_*.out"))):
        b = os.path.basename(f)
        for l in open(f):
            m = rx.match(l.strip())
            if not m: continue
            n, ver = int(m.group(1)), m.group(2); hc = m.group(10).split(); hsum = sum(int(hc[i + 1]) for i in range(0, len(hc), 2))
            H.setdefault((ver, n), (m.group(3), m.group(4), m.group(5), int(m.group(6)), int(m.group(7)), int(m.group(8)), hsum))
            if m.group(11):
                wc = m.group(18).split(); wsum = sum(int(wc[i + 1]) for i in range(0, len(wc), 2)); assert len(wc) == 36, b
                Wr[(b[:-4].replace('_long7', '').replace('_long8', ''), n)] = (m.group(11), m.group(12), int(m.group(13)), int(m.group(14)), m.group(15), wsum)
    out = ["| n | nodes, edges, highest Ω (fig4) | T fig4 | T table4 | 2^n | 9·2^n − 10 | six H-counters, fig4 / table4 | \\|W^L_n\\| | N5′-xi fig4: iterations, first fallback, fallbacks, 18 counters | the same, random index order | the same, table4 | N5 (spec) fig4, my order: iterations, F, 18 counters |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    def cell(tag, n):
        w = Wr.get((tag, n))
        return "not run" if w is None else f"{fmt(w[2])}, {fmt(w[3])}, {w[4]}, {w[5]}"
    for n in sorted({k[1] for k in H}):
        a = H.get(("fig4", n)); t = H.get(("table4", n)); w = Wr.get(("f11_W_xi_fig4", n))
        out.append(f"| {n} | {a[0]}, {a[1]}, {a[2]} | {fmt(a[3])} | {fmt(t[3]) if t else 'not run'} | {fmt(a[4])} | {fmt(a[5])} | {a[6]} / {t[6] if t else 'not run'} | {fmt(int(w[1])) if w else 'not run'} | "
                   f"{cell('f11_W_xi_fig4', n)} | {cell('f11_W_xi_fig4_perm', n)} | {cell('f11_W_xi_table4', n)} | {cell('f11_W_spec_fig4', n)} |")
    return "\n".join(out)

def table_inst():
    out = ["| file (lane's frozen instance) | vertices | N5′-xi: iterations, fallbacks, first fallback, regions = my Zielonka | N5 (spec): the same | states with τ changed or Iτ ≠ ∅ (both modes) |", "| --- | --- | --- | --- | --- |"]
    rx = re.compile(r"(\S+) mode (\w+) n (\d+) iterations (\d+) fallbacks (\d+) first (\S+) regions==zielonka (\w+) tau_changed_states (\d+) Itau_nonempty_states (\d+)")
    rows = {}
    for f in sorted(glob.glob(os.path.join(d, "inst_*.out"))):
        for l in open(f):
            m = rx.match(l.strip())
            if m: rows.setdefault(m.group(1), {})[m.group(2)] = m.groups()
    def key(nm):
        m = re.match(r"([A-Z]+)_(\d+)", nm); return (m.group(1), int(m.group(2)))
    for nm in sorted(rows, key=key):
        x = rows[nm].get("xi"); s = rows[nm].get("spec"); nv = (x or s)[2]
        c = lambda r: "not run" if r is None else f"{fmt(int(r[3]))}, {r[4]}, {fmt(int(r[5]))}, {r[6]}"
        bad = sum(int(r[7]) + int(r[8]) for r in (x, s) if r is not None)
        out.append(f"| {nm} | {fmt(int(nv))} | {c(x)} | {c(s)} | {bad} |")
    return "\n".join(out)

tm, maxT, unfinished = table_main(); tc = table_ctrl(); tf = table_f11(); ti = table_inst()
text = "\n\n".join(["TABLE_MAIN\n" + tm, "TABLE_CTRL\n" + tc, "TABLE_F11\n" + tf, "TABLE_INST\n" + ti, f"MAXT {maxT}"])
if len(sys.argv) > 2 and sys.argv[1] == "splice":
    assert not unfinished, unfinished
    s = open(sys.argv[2]).read()
    for mk, val in (("@@TABLE_MAIN@@", tm), ("@@TABLE_CTRL@@", tc), ("@@TABLE_F11@@", tf), ("@@TABLE_INST@@", ti), ("@@MAXT@@", str(maxT))):
        assert s.count(mk) == 1, mk
        s = s.replace(mk, val)
    open(sys.argv[2], "w").write(s); print("spliced")
else:
    open(os.path.join(d, "summ.out"), "w").write(text + "\n"); print(text)
