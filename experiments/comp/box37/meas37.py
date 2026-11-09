#!/usr/bin/env python3
"""L-COMP box 37: measure gen37(n) on an engine. ENGINE=fast36 (bin/k) or own36 (Python, independent of fast36's C code).
Counters (scope: N5'-xi from S3 on Gamma3 up to the first fallback, [E-LEV]; unit = one genome gen37(n)):
  T3 = iterations up to the first fallback (total); C = max over (v, I) of #tops of one letter (per-(v, I) maximum);
  Qf/Ql = flips / lamch at gate (Q, 0) (per-gate); maxflip = per-gate MAXIMUM of flips; ratio = max_g flips/(lamch+1); k = Xi-FVS number.
Usage: meas37.py ENGINE n1 n2 ... ; writes inst/gen37_n<n>.json (sha1 printed)."""
import sys, os, json, hashlib, subprocess, time
H = os.path.dirname(os.path.abspath(__file__)); B = os.path.join(H, "..", "box36"); sys.path.insert(0, B); os.chdir(B)
import fast36, own36
_orig = fast36.one
def one96(G):
    """fast36.one with an extra W = 96 build (bin/k/fast36_w96, same source fast36.c) for n > 3072 (fast36.py's width list stops at 48)."""
    n = G["N"] + 8 * sum(len(o) for o in G["opts"]) + 10
    if n <= 64 * 48: return _orig(G, bindir="bin/k")
    import subprocess as sp
    out = sp.run([os.path.join(B, "bin/k/fast36_w96"), "one"], input=fast36.gtext(G), capture_output=True, text=True, check=True).stdout.split("\n")
    h = out[0].split(); fast36.LASTC = int(h[7]); rows = []
    for line in out[1:]:
        if line.startswith("gate"): z = line.split(); rows.append(((int(z[1]), int(z[2])), int(z[3]), int(z[4])))
    return int(h[1]), int(h[3]), sorted(rows)
eng = sys.argv[1]
for n in map(int, sys.argv[2:]):
    p = subprocess.run([sys.executable, os.path.join(H, "gen37.py"), str(n)], capture_output=True, text=True, check=True)
    G = json.loads(p.stdout); nm = json.loads(p.stderr); Q = nm["Q"]
    fn = os.path.join(H, "inst", f"gen37_n{n}.json"); s = json.dumps(G, sort_keys=True); open(fn, "w").write(s + "\n")
    t0 = time.time()
    if eng == "fast36":
        T, fb, rows = one96(G); C = fast36.LASTC
    else:
        o, rows = own36.census(G, True, True); T, C = o["T3"], o["C"]
    Qf = max([f for q, f, l in rows if tuple(q) == (Q, 0)] or [0]); Ql = max([l for q, f, l in rows if tuple(q) == (Q, 0)] or [0])
    print(f"{eng} n {n} N+M {G['N'] + sum(map(len, G['opts']))} T3 {T} C {C} Qf {Qf} Ql {Ql} maxflip {max(f for q, f, l in rows)} "
          f"ratio {max(f / (l + 1) for q, f, l in rows):g} k {own36.kfvs(G, 1)} sha1 {hashlib.sha1((s + chr(10)).encode()).hexdigest()[:8]} {time.time() - t0:.1f}s", flush=True)
