#!/usr/bin/env python3
"""L-RED box 7 (produced on Opus 5.5): graded fitness for L-ALG's GAP-A-M §22c/§22d targets, judged by L-ALG's
experiments/alg/dtl_rootmono.py run UNMODIFIED as a subprocess (LALGR_DIR = an l-alg checkout >= 8a2a149; order from
DTL_ORDER). Parsed: "CLEAN root transition: FAILS" (PREFIX-MONO / ROOT-BOUND prediction broken), "PI at root-e*
transitions: Ψ NOT monotone | DOES NOT RISE" (PI-RISE broken), RMONO falls per phase (badrows), max dirty per phase and
that phase's length. Modes (ROOTFIT = dirty | falls):
  dirty: 1e11 hit + 1e7 * max dirty per phase + 1e4 * (dirty phase transitions) + |G'| of that phase
  falls: 1e11 hit + 1e7 * max RV falls per phase + 1e4 * max dirty per phase
Usage: rootfit.py G.pg ... (prints score and the parsed dict)."""
import sys, os, re, subprocess, ast
JUDGE = os.path.join(os.environ.get("LALGR_DIR", ""), "experiments", "alg", "dtl_rootmono.py")


def measure(path, order=None):
    env = dict(os.environ); env["DTL_ORDER"] = order or os.environ.get("DTL_ORDER", "stable"); env["RM_DV"] = "0"
    out = subprocess.run([sys.executable, JUDGE, os.path.abspath(path)], capture_output=True, text=True, env=env,
                         timeout=600, cwd=os.path.dirname(JUDGE)).stdout
    m = dict(hit=0, maxdirty=0, phlen=0, phG=0, maxfalls=0, clean=0, dirty=0)
    for line in out.splitlines():
        if line.startswith("phases with dirty root transitions"):
            rows = ast.literal_eval(line.split(": ", 1)[1])
            if rows: m["maxdirty"], m["phlen"], m["phG"] = rows[0][1], rows[0][3], rows[0][4]
        elif line.startswith("phases where PI fails to rise"):
            rows = ast.literal_eval(line.split(": ", 1)[1].rsplit(" phases:", 1)[0])
            if rows: m["maxfalls"] = rows[0][1]
        elif line.startswith("{"):
            tab = ast.literal_eval(line)
            for k, v in tab.items():
                if k.startswith("CLEAN root transition: FAILS") or k in ("PI at root-e* transitions: Ψ NOT monotone",
                                                                          "PI at root-e* transitions: DOES NOT RISE"):
                    m["hit"] += v
                if k.startswith("CLEAN root transition"): m["clean"] += v
                if k.startswith("DIRTY root transition"): m["dirty"] += v
    if "Traceback" in out or not out.strip(): m["hit"] = 0; m["error"] = 1
    return m


def score_m(m):
    if os.environ.get("ROOTFIT", "dirty") == "falls":
        return 1e11 * (m["hit"] > 0) + 1e7 * min(m["maxfalls"], 999) + 1e4 * min(m["maxdirty"], 999)
    return 1e11 * (m["hit"] > 0) + 1e7 * min(m["maxdirty"], 9999) + 1e4 * min(m["phlen"], 999) + min(m["phG"], 9999)


def score(path):
    """dtl_search.py --fitness root entry point."""
    m = measure(path)
    return -1 if m.get("error") else int(score_m(m))


if __name__ == "__main__":
    for f in sys.argv[1:]:
        m = measure(f); print(f, int(score_m(m)), m, flush=True)
