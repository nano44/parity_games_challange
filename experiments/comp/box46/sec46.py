#!/usr/bin/env python3
"""L-COMP box 46 item 3: a genome on two SECOND engines against my win46 run.
 (i) n5b (experiments/n5-second/n5b.py, L-COMP's second N5 implementation, --mode spec) on Γ3(G) written by own34.build, from S3 given
     explicitly (own34.standard, --start): its «iterations» and «fallbacks» against my run's Ttot and F (the whole run, to the end).
 (ii) L-NEW's rfd212.py (claude/l-new 5fa64fe6, env LNEW212 = an archive; run unchanged, python3 -I, RFD_MODE=spec; n5v spec on L-NEW's
     own Γ3 builder): (T_key, #windows, W_key, stalls, tail) against mine (windows formed as in cmp46.py).
Usage: sec46.py G.json ...  -> one line per genome «<name> mine (...) n5b (...) rfd212 (...) agree True|False»"""
import sys, os, json, re, subprocess, tempfile
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, "..", "..", ".."))
sys.path[:0] = [H, os.path.join(H, "..", "box34"), os.path.join(R, "experiments", "harness")]
import win46, own34, pg
L = os.environ["LNEW212"]
f = lambda l, k: int(re.search(r"(?:^| )%s (-?\d+)" % k, l).group(1))
for fn in sys.argv[1:]:
    G = json.load(open(fn)); G = G.get("genome", G); b = os.path.basename(fn)
    c, d, first, B = win46.measure(G); ml = win46.line(b, c, d, B)
    mine = (d["Tkey"], d["nwin"], d["Wkey"], d["stalls"], d["tail_len"]); mrun = (d["Ttot"], d["F"])
    g, V = own34.build(G, True); s, t = own34.standard(G, V, g)
    with tempfile.TemporaryDirectory() as T:
        pg.write(g, os.path.join(T, "g.pg"))
        open(os.path.join(T, "st"), "w").write("SIGMA0 " + " ".join("%d:%d" % (v, w) for v, w in enumerate(s) if w >= 0) + "\nTAU0 " + " ".join("%d:%d" % (v, w) for v, w in enumerate(t) if w >= 0) + "\n")
        o = subprocess.run([sys.executable, "-I", os.path.join(R, "experiments", "n5-second", "n5b.py"), os.path.join(T, "g.pg"), "--start", os.path.join(T, "st"), "--mode", "spec"], capture_output=True, text=True).stdout
    m = re.search(r"iterations (\d+) fallbacks (\d+)", o); nb = (int(m.group(1)), int(m.group(2))) if m else None
    o = subprocess.run([sys.executable, "-I", "rfd212.py", os.path.abspath(fn)], cwd=os.path.join(L, "experiments", "new", "box212"), env=dict(os.environ, RFD_MODE="spec"), capture_output=True, text=True).stdout
    rl = next((x for x in o.splitlines() if x.startswith(b + " RFD_MODE spec")), None)
    rf = (f(rl, "T"), f(rl, "plat") + (f(rl, "tail") > 0), max(f(rl, "platmax"), f(rl, "tail")), f(rl, "stalls"), f(rl, "tail")) if rl else None
    print("%s N+M %d | mine (T_key, windows, W_key, stalls, tail) %s run (iterations, fallbacks) %s must0 %d | n5b spec (iterations, fallbacks) %s | rfd212 %s | agree %s" % (
        b, B["N"] + B["M"], mine, mrun, f(ml, "must0"), nb, rf, nb == mrun and rf == mine), flush=True)
