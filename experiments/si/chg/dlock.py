#!/usr/bin/env python3
"""L-SI box 28 (docs/si/N5-CHG-box28.md): anatomy of DEADLOCK steps (no last switch) of maximal REL segments, and the candidate
lemmas of the SEG-COUNT charging (note §2-§3). Sets as lay/wsink.py; L(v) = last switch in [a, b]; s_h := fW(jW h) - 1 (JOINT step).
Counters (each *_V is a failure of the named candidate):
  DLHS_V    a deadlock step where some switching vertex is not an H-sink                         (candidate DL-HSW)
  DLNEXT_V  a deadlock step t < b - 1 where t + 1 is not a W-growth step (no ready W-sink at t + 1)  (candidate DL-NEXT)
  DLEND_V   a deadlock step t = b - 1 (cannot happen: the last step finalizes every switcher)
  NOEARLY_V a deadlock step all of whose H-sinks finalize early (L(h) < s_h)                         ((a) of the charging, deadlock form)
  MATCH_V   a segment whose deadlock steps cannot be matched injectively to surplus finalizations: t -> s_h for an H-sink h at t
            with L(h) = s_h, at most |F_s| - 1 deadlock steps per final step s                       ((b) of the charging)
  ZIG_V     a deadlock step where no switching H-sink h has a W-sink at t whose H-chain ends at h      (candidate DL-ZIG)
  DLSOMEH_V a deadlock step where no H-sink switches                                         (candidate DL-SOMEH)
  DLSEP_V   two deadlock steps of one segment with no growth step (W-GROW or H-GROW) between them    (candidate DL-SEP)
  GROWFIN_V a growth step that is not a final step (Theorem SINK-STEP says never)
  GROWPERS_V a segment with a non-growth step after a growth step                                  (candidate GROW-PERSIST)
  DLFIRST_V  a segment with a deadlock step t > a                                                  (candidate DL-FIRST)
  DLRUN_V    a deadlock step t > r0, r0 the first state of its fallback-free run                    (candidate DL-RUN; implies DL-FIRST)
  ngrun_k   maximal runs of k consecutive non-growth steps
VERB=1 prints every deadlock step. Usage: dlock.py --list FILE | --one GAME [START]   (START=1 reads list column 2)"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import suffix
from suffix import segdata, rows, load, readstart
import seglast
from trace import runs
from n5x import Engine
C = Counter(); EX = []; VERB = os.environ.get("VERB") == "1"; MUT = int(os.environ.get("MUT", "0"))   # MUT=1: DL-RUN tested with t >= r0 (must bite)

def match(D, cap, edges):
    """bipartite matching of deadlock steps D to final steps with capacities cap; edges[t] = candidate final steps."""
    slots = [(s, i) for s in cap for i in range(cap[s])]; own = {}
    def aug(t, seen):
        for s in edges[t]:
            for i in range(cap.get(s, 0)):
                if (s, i) in seen: continue
                seen.add((s, i))
                if (s, i) not in own or aug(own[(s, i)], seen): own[(s, i)] = t; return True
        return False
    return sum(aug(t, set()) for t in D)

def _run(g, R, name):
    EN = Engine(g); RS = list(runs(R))
    for a, b in seglast.segs(g, R):
        if b <= a: continue
        Ev, T, JW, JH, fW, fH, L = segdata(g, R, a, b); B = R[b]
        fWj = lambda v: fW[JW[v]] if JW[v] is not None else a
        F = Counter(L.values()); D = [t for t in range(a, b) if F[t] == 0]
        def sinks(t):
            UW = {v for v in Ev if fW[v] > t}; UH = {v for v in Ev if fH[v] > t}
            return [v for v in UW if JW[v] not in UW], [v for v in UH if JH[v] not in UH], UW, UH
        def readyset(t, WS):
            I = set(EN.improving(tuple(R[t]["s"]), R[t]["vs"])); s = R[t]["s"]
            return [v for v in WS if s[v] == B["s"][v] or (v, B["s"][v]) in I]
        edges = {}
        for t in D:
            C["deadlock"] += 1; WS, HS, UW, UH = sinks(t)
            sw = [v for v in Ev if R[t]["s"][v] != R[t + 1]["s"][v]]
            if not any(v in HS for v in sw): C["DLSOMEH_V"] += 1; EX.append(("DLSOMEH", name, a, b, t, sorted(sw), sorted(HS)))
            if any(v not in HS for v in sw): C["DLHS_V"] += 1; EX.append(("DLHS", name, a, b, t, sorted(sw), sorted(HS)))
            if t == b - 1: C["DLEND_V"] += 1
            elif not readyset(t + 1, sinks(t + 1)[0]): C["DLNEXT_V"] += 1; EX.append(("DLNEXT", name, a, b, t))
            good = [h for h in HS if L.get(h) == fWj(h) - 1]
            if not good: C["NOEARLY_V"] += 1; EX.append(("NOEARLY", name, a, b, t, sorted(HS)))
            edges[t] = sorted({L[h] for h in good})
            def hend(w):
                x = w
                while JH[x] in UH: x = JH[x]
                return x
            ends = {hend(w) for w in WS if JH[w] in UH}
            if not any(h in ends for h in sw if h in HS): C["ZIG_V"] += 1; EX.append(("ZIG", name, a, b, t, sorted(sw), sorted(ends)))
            if VERB:
                print(f"{name} [{a},{b}] t={t} switch={[(v, R[t]['s'][v], R[t+1]['s'][v]) for v in sw]} WS={sorted(WS)} HS={sorted((h, L.get(h), fWj(h) - 1) for h in HS)}"
                      f" F(t+1)={sorted(v for v in L if L[v] == t + 1)} zigends={sorted(ends)}")
        grow = [t for t in range(a, b) if any(fW[v] == t + 1 or fH[v] == t + 1 for v in Ev)]
        for t1, t2 in zip(D, D[1:]):
            if not any(t1 < x < t2 for x in grow): C["DLSEP_V"] += 1; EX.append(("DLSEP", name, a, b, t1, t2))
        run = 0
        for t in range(a, b + 1):
            if t < b and t not in grow: run += 1
            else:
                if run: C["ngrun_%d" % min(run, 9)] += 1
                run = 0
        if any(t not in grow and any(x < t for x in grow) for t in range(a, b)):
            C["GROWPERS_V"] += 1; EX.append(("GROWPERS", name, a, b, "".join("G" if t in grow else ("F" if F[t] else "D") for t in range(a, b))))
        if any(t > a for t in D): C["DLFIRST_V"] += 1; EX.append(("DLFIRST", name, a, b, D))
        r0 = [x for x in RS if x[0] <= a <= x[1]][0][0]
        if any(t > r0 - MUT for t in D): C["DLRUN_V"] += 1; EX.append(("DLRUN", name, a, b, r0, D))
        C["growsteps"] += len(grow); C["finalsteps"] += len(F)
        if any(t in grow and F[t] == 0 for t in range(a, b)): C["GROWFIN_V"] += 1     # SINK-STEP: a growth step is a final step
        if D:
            cap = {s: F[s] - 1 for s in F if F[s] > 1}
            if match(D, cap, edges) < len(D): C["MATCH_V"] += 1; EX.append(("MATCH", name, a, b, D, edges, cap))
            C["segs_with_deadlock"] += 1; C["maxdead_%d" % len(D)] += 1

def run(g, name, start=None):
    E, R = rows(g, start); _run(g, R, name)

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p:
                f = os.path.join(ROOT, p[0]) if os.path.exists(os.path.join(ROOT, p[0])) else os.path.join(ROOT, "experiments", p[0])
                s = None
                if len(p) > 1 and os.environ.get("START") == "1":
                    s = os.path.join(ROOT, p[1]) if os.path.exists(os.path.join(ROOT, p[1])) else os.path.join(ROOT, "experiments", p[1])
                try: run(load(f), p[0], readstart(s) if s else None)
                except Exception as e: C["SKIPPED_input"] += 1; print("SKIP", p[0], type(e).__name__, file=sys.stderr)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for z in EX[:12]: print("EXAMPLE", z)
    for k in ("DLHS", "DLSOMEH", "DLNEXT", "DLEND", "NOEARLY", "MATCH", "ZIG", "DLSEP", "GROWFIN", "GROWPERS", "DLFIRST", "DLRUN"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__":
    main()

def dscore(g, R):
    """counters of one run (for chg/cclimb.py OBJ=GP)."""
    global C, EX
    save = (C, EX); C, EX = Counter(), []
    try: _run(g, R, "x"); return dict(C)
    finally: C, EX = save
