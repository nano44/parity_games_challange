"""L-RED box 20 (produced on Opus 5.5): longest phase S of A_DTL against n. Per game and order: n, S (max searches in one phase,
L-ALG's dtl_phasestats phase convention via ../carry/spp.py, unmodified), |G'| at that phase, total iterations; plus pinned Oink
8fbf0a7 -v even / odd iterations and 'verified'. Usage: smeasure.py G.pg ...  (LALG_DIR defaults to the repo root)"""
import sys, os, subprocess, re, hashlib, importlib.util
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
os.environ.setdefault("LALG_DIR", R); sys.setrecursionlimit(100000)
spec = importlib.util.spec_from_file_location("spp", os.path.join(R, "experiments", "red", "carry", "spp.py"))
SP = importlib.util.module_from_spec(spec); spec.loader.exec_module(SP)
OINK = os.path.join(R, "tools", "oink", "build", "oink")
for f in sys.argv[1:]:
    row = [os.path.basename(f), hashlib.sha1(open(f, "rb").read()).hexdigest()[:12]]
    for o in ("stable", "oink"):
        os.environ["DTL_ORDER"] = o
        try:
            b = SP.measure(f); row.append(f"{o}: n {b['n']} S {b['spp']} G' {b['G']} it {b['iters']}")
        except Exception as e:
            row.append(f"{o}: ERROR {type(e).__name__}")
    try:
        out = subprocess.run([OINK, "--dtl", "--no-single", "--no-wcwc", "--no-loops", "-v", f], capture_output=True, text=True, timeout=600).stdout
        ev = re.search(r"even iterations: (\d+)", out); od = re.search(r"odd iterations: (\d+)", out)
        row.append(f"oink-cpp: even {ev.group(1) if ev else '?'} odd {od.group(1) if od else '?'} {'verified' if 'verified' in out else 'NOT VERIFIED'}")
    except Exception as e:
        row.append(f"oink-cpp: ERROR {e}")
    print(" | ".join(row), flush=True)
