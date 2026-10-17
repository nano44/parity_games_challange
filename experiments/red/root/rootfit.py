#!/usr/bin/env python3
"""L-RED box 7 (produced on Opus 5.5): graded fitness for L-ALG's GAP-A-M §22c/§22d targets, judged by L-ALG's
experiments/alg/dtl_rootmono.py run UNMODIFIED as a subprocess (LALGR_DIR = an l-alg checkout >= 8a2a149; order from
DTL_ORDER). Parsed: "CLEAN root transition: FAILS" (PREFIX-MONO / ROOT-BOUND prediction broken), "PI at root-e*
transitions: Ψ NOT monotone | DOES NOT RISE" (PI-RISE broken), RMONO falls per phase (badrows), max dirty per phase and
that phase's length; from l-alg >= c983b024 also "ANY-CONTEXT e*" (§22e: Ψ NOT monotone, Π DOES NOT RISE, RV falls at a
CLEAN later call, or "impossible by FDL" count as hits; ABS-pw is already dead and is NOT a hit) and the distinct
first-difference contexts per phase; from l-alg >= c8df405d also "descents of Π_R per context" (§22l (FALL)).
From l-alg >= 473edc4b with RM_EXCL=1 (set by mode steal): "RELEVANT new-steal visits per context" (§22s (RELSTEAL))
and "NEW STEALS per (context, round, top, tangle): max K" (§22t (STEAL-ONCE): K >= 2 is a hit).
"max tangles: K" = distinct tangles FIRED at one context over a phase (§22u (FIRED-R)), mode fired (RM_EXCL=1).
From l-alg >= e2f7e198 with RM_EXCL=1 RM_PREF=1 (mode stealer): "STEALER-MONO (...): FAILS" and "STOLEN-PERM (...): FAILS"
are hits (§23a).
Modes (ROOTFIT = dirty | falls | ctx | fall | steal | fired | firedr | stealer):
  dirty: 1e11 hit + 1e7 * max dirty per phase + 1e4 * (dirty phase transitions) + |G'| of that phase
  falls: 1e11 hit + 1e7 * max RV falls per phase + 1e4 * max dirty per phase
  fall:  1e11 hit + 1e7 * max descents of Π_R at one context in one phase + 1e4 * total descents + max RV falls per phase
  fired: 1e11 hit + 1e7 * max distinct fired tangles at one context + 1e4 * (max tangles/|R| in per mille)
  firedr: 1e11 hit + 1e7 * (max tangles/|R| in per mille) + max distinct fired tangles (ratio first: > 1000 needs
         more fired tangles at one context than |R|, i.e. several visits)
  stealer: 1e11 hit (STEALER-MONO / STOLEN-PERM fails) + 1e7 * max relevant steal visits at one context + STEALER-MONO checks
  steal: 1e11 hit + 1e7 * max relevant new-steal visits at one context + 1e4 * their total + max new-steal visits
  ctx:   1e11 hit + 1e7 * max distinct first-difference contexts per phase + 1e4 * that phase's transitions + |G'|
Usage: rootfit.py G.pg ... (prints score and the parsed dict)."""
import sys, os, re, subprocess, ast
JUDGE = os.path.join(os.environ.get("LALGR_DIR", ""), "experiments", "alg", "dtl_rootmono.py")


def measure(path, order=None):
    env = dict(os.environ); env["DTL_ORDER"] = order or os.environ.get("DTL_ORDER", "stable"); env["RM_DV"] = "0"
    if os.environ.get("ROOTFIT") in ("steal", "fired", "firedr", "stealer"): env["RM_EXCL"] = "1"
    if os.environ.get("ROOTFIT") == "stealer": env["RM_PREF"] = "1"
    out = subprocess.run([sys.executable, JUDGE, os.path.abspath(path)], capture_output=True, text=True, env=env,
                         timeout=600, cwd=os.path.dirname(JUDGE)).stdout
    m = dict(hit=0, maxdirty=0, phlen=0, phG=0, maxfalls=0, clean=0, dirty=0, ctx=0, ctxlen=0, ctxG=0, desc=0, desctot=0, rsteal=0, rstealtot=0, nsteal=0, once=0, fired=0, firedratio=0.0, smono=0)
    for line in out.splitlines():
        if line.startswith("phases with dirty root transitions"):
            rows = ast.literal_eval(line.split(": ", 1)[1])
            if rows: m["maxdirty"], m["phlen"], m["phG"] = rows[0][1], rows[0][3], rows[0][4]
        elif line.startswith("distinct first-difference contexts per phase"):
            rows = ast.literal_eval(line.split(": ", 1)[1].rsplit(" max contexts", 1)[0])
            if rows: m["ctx"], m["ctxlen"], m["ctxG"] = rows[0][1], rows[0][2], rows[0][3]
        elif line.startswith("RELEVANT new-steal visits per context"):
            rows = ast.literal_eval(line.split(": ", 1)[1].rsplit(" phases:", 1)[0])
            if rows: m["rsteal"], m["rstealtot"] = max(r[1] for r in rows), max(r[2] for r in rows)
        elif line.startswith("new-steal visits per context"):
            rows = ast.literal_eval(line.split(": ", 1)[1].rsplit(" phases:", 1)[0])
            if rows: m["nsteal"] = max(r[1] for r in rows)
        elif line.startswith("max tangles/|R|:"):
            x = line.split()
            m["firedratio"] = float(x[x.index("tangles/|R|:") + 1]); m["fired"] = int(x[-1])
        elif line.startswith("descents of Π_R per context"):
            rows = ast.literal_eval(line.split(": ", 1)[1].rsplit(" phases:", 1)[0])
            if rows: m["desc"], m["desctot"] = max(r[1] for r in rows), max(r[2] for r in rows)
        elif line.startswith("phases where PI fails to rise"):
            rows = ast.literal_eval(line.split(": ", 1)[1].rsplit(" phases:", 1)[0])
            if rows: m["maxfalls"] = rows[0][1]
        elif line.startswith("{"):
            tab = ast.literal_eval(line)
            for k, v in tab.items():
                if k.startswith("CLEAN root transition: FAILS") or k in ("PI at root-e* transitions: Ψ NOT monotone",
                                                                          "PI at root-e* transitions: DOES NOT RISE"):
                    m["hit"] += v
                if k.startswith("ANY-CONTEXT") and ("NOT monotone" in k or "DOES NOT RISE" in k or "impossible" in k
                                                    or ("RV falls" in k and "later call clean" in k)):
                    m["hit"] += v
                if k.startswith(("NEW STEALS per (context, round, top, tangle): max", "RELEVANT STEALS per (context, round, top, tangle): max")):
                    km = int(k.rsplit("max ", 1)[1]); m["once"] = max(m["once"], km)
                    if km >= 2: m["hit"] += v
                if ("STEALER-MONO" in k or "STOLEN-PERM" in k) and k.rstrip().endswith("FAILS"): m["hit"] += v
                if "STEALER-MONO" in k: m["smono"] += v
                if k.startswith("CLEAN root transition"): m["clean"] += v
                if k.startswith("DIRTY root transition"): m["dirty"] += v
    if "Traceback" in out or not out.strip(): m["hit"] = 0; m["error"] = 1
    return m


def score_m(m):
    if os.environ.get("ROOTFIT", "dirty") == "stealer":
        return 1e11 * (m["hit"] > 0) + 1e7 * min(m["rsteal"], 999) + min(m["smono"], 9999)
    if os.environ.get("ROOTFIT", "dirty") == "firedr":
        return 1e11 * (m["hit"] > 0) + 1e7 * min(int(1000 * m["firedratio"]), 9999) + min(m["fired"], 9999)
    if os.environ.get("ROOTFIT", "dirty") == "fired":
        return 1e11 * (m["hit"] > 0) + 1e7 * min(m["fired"], 9999) + 1e4 * min(int(1000 * m["firedratio"]), 999)
    if os.environ.get("ROOTFIT", "dirty") == "steal":
        return 1e11 * (m["hit"] > 0) + 1e7 * min(m["rsteal"], 999) + 1e4 * min(m["rstealtot"], 999) + min(m["nsteal"], 999)
    if os.environ.get("ROOTFIT", "dirty") == "fall":
        return 1e11 * (m["hit"] > 0) + 1e7 * min(m["desc"], 999) + 1e4 * min(m["desctot"], 999) + min(m["maxfalls"], 999)
    if os.environ.get("ROOTFIT", "dirty") == "ctx":
        return 1e11 * (m["hit"] > 0) + 1e7 * min(m["ctx"], 9999) + 1e4 * min(m["ctxlen"], 999) + min(m["ctxG"], 9999)
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
