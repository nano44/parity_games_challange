#!/usr/bin/env python3
"""L-RED successor 32 (R133): N5 vs N5-LZC bench. For each (family, size): generate the game (and start), run lzcmp.py (two engines,
both variants), check engine B's N5-LZC solution with new/check_sol2.py (Oink zlk + both strategies). One line per run.
Usage: bench.py OUTDIR [FAMILY ...]   (families: see GEN)"""
import sys, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, "..", ".."))
B = os.path.join(EXP, "..", "tools", "oink", "build"); PY = sys.executable
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
def sh(cmd, path, env=None):
    with open(path, "w") as f: subprocess.run(cmd, stdout=f, stderr=subprocess.DEVNULL, env=dict(os.environ, **(env or {})), check=True, timeout=600)
def oink(tool):
    return lambda N, p: (sh([os.path.join(B, tool), str(N)], p + ".pg"), None)[1]
def port(name):
    return lambda N, p: (sh([PY, os.path.join(EXP, "hard-families", "pgsolver_port.py"), name, str(N)], p + ".pg"), None)[1]
def pgp(name):
    return lambda N, p: (sh([PY, os.path.join(EXP, "red", "sf", "pgports.py"), name, str(N)], p + ".pg"), None)[1]
def km(script, env=None):
    def f(N, p):
        K, m = N
        subprocess.run([PY, os.path.join(EXP, "red", script), str(K), str(m), p + ".pg", p + ".start"], env=dict(os.environ, **(env or {})),
                       capture_output=True, check=True, timeout=600); return p + ".start"
    return f
def dbidir(N, p):
    km("span/mkrb.py")(N, p + "_b")
    subprocess.run([PY, os.path.join(EXP, "red", "ctl", "dualize.py"), p + "_b.pg", p + "_b.start", p + ".pg", p + ".start"], capture_output=True, check=True)
    return p + ".start"
def runfam(N, p):
    subprocess.run([PY, os.path.join(EXP, "si", "runlin", "mkrunfam.py"), str(N), p], capture_output=True, check=True, timeout=600)
    return p + ".start"
def dl(N, p): return (sh([PY, os.path.join(EXP, "red", "sf", "dlchain.py"), str(N), "1"], p + ".pg"), None)[1]
def fc(N, p): return (sh([PY, os.path.join(EXP, "red", "sf", "sbev.py"), str(N), "--drop", "fc"], p + ".pg"), None)[1]
def pin(name):
    def f(N, p):
        for ext in (".pg", ".start"):
            subprocess.run(["cp", os.path.join(EXP, "red", name + ext), p + ext], check=True)
        return p + ".start"
    return f
SM = [(2, 4), (3, 6), (4, 8), (6, 12), (8, 16)]
GEN = {
    "tc": (oink("tc"), [1, 2, 3, 4, 5]), "tc+": (oink("tc+"), [1, 2, 3, 4, 5]), "counter_symsi": (oink("counter_symsi"), [2, 3, 4, 5, 6]),
    "counter_rr": (oink("counter_rr"), [2, 3, 4, 5, 6]), "counter_dp": (oink("counter_dp"), [2, 3, 4, 5, 6]),
    "counter_m": (oink("counter_m"), [2, 4, 6, 8, 10]), "counter_core": (oink("counter_core"), [2, 3, 4, 5, 6]),
    "counter_rob": (oink("counter_rob"), [2, 3, 4, 5, 6]), "counter_ortl": (oink("counter_ortl"), [2, 3, 4, 5, 6]),
    "counter_qpt": (oink("counter_qpt"), [2, 3, 4, 5]),
    "recursiveladder": (port("recursiveladder"), [2, 3, 4, 5, 6]), "switchallexp": (port("switchallexp"), [2, 3, 4, 5]),
    "switchbestexp": (port("switchbestexp"), [2, 3, 4, 5]),
    "switchbestsubexp": (pgp("switchbestsubexp"), [2, 3, 4, 5, 6]), "zadehexp": (pgp("zadehexp"), [2, 3, 4]),
    "mkrb": (km("span/mkrb.py"), SM), "latew": (km("span/mkrw.py", {"LATE": "1"}), SM), "wdepth": (km("span/mkrw.py", {"LATE": "2"}), SM),
    "dbidir": (dbidir, SM), "tiedrb": (km("tree/mktied.py"), SM), "runfam": (runfam, [2, 4, 8, 16, 32]),
    "dw": (dl, [3, 4, 5, 6, 7]), "fc": (fc, [3, 4, 5, 6, 8]),
    "pins": (None, ["span/instances/spanobs_K12_m48", "span/instances/carryobs_K12_m48", "span/instances/bidir_K8_m32",
                    "span/instances/latew_K8_m32", "span/instances/wdepth_K4_m64", "span/instances/dbidir_K12_m48", "tree/instances/tiedrb_K8_m16"]),
}
fams = sys.argv[2:] or list(GEN)
for fam in fams:
    gen, sizes = GEN[fam]
    for N in sizes:
        tag = N if not isinstance(N, tuple) else f"{N[0]}_{N[1]}"
        p = os.path.join(out, f"{fam}_{tag}".replace("/", "_"))
        try:
            st = pin(N)(None, p) if fam == "pins" else gen(N, p)
            r = subprocess.run([PY, os.path.join(HERE, "lzcmp.py"), p + ".pg", p + ".sol"] + ([st] if st else []), capture_output=True, text=True, timeout=3600)
            line = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else "ERR " + r.stderr.strip().splitlines()[-1][:150]
            o = subprocess.run([PY, os.path.join(EXP, "new", "check_sol2.py"), p + ".pg", p + ".sol"], capture_output=True, text=True, timeout=3600)
            ok = (o.stdout.strip().splitlines() or ["?"])[-1]
        except Exception as e:
            line, ok = f"ERR {type(e).__name__} {str(e)[:120]}", "-"
        print(f"{fam} {tag} | {line} | {ok}", flush=True)
