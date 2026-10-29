#!/usr/bin/env python3
"""L-SI box 27 (docs/si/N5-LAY-box27.md): frame-wise sinks in a maximal REL-admissible segment [a, b] (lwp/seglast.py's cutting).
U^W_t (U^H_t): Even vertices of X_b \\ T whose W-play (honest play) is NOT constant on [t, b]. jW(v) (jH(v)): the first Even vertex
outside T after v on v's W-play (honest play) at b. A W-SINK at t: v in U^W_t with jW(v) not in U^W_t (H-SINK likewise).
Counters per transition t -> t + 1:
  WSOFF_V  a W-sink with sigma_t(v) = sigma_b(v)        (Lemma SINK-OFF says never)
  HSOFF_V  an H-sink with sigma_t(v) = sigma_b(v)       (Lemma SINK-OFF says never)
  HSR_V    an H-sink whose target is not in its arena at t (step (A) of STATIC-DEPTH' says never)
  WSL_V    an arena-ready W-sink that does not keep sigma_b on [t + 1, b] (Lemma W-SINK says never, under GEN_W)
  WSR_V    no arena-ready W-sink at t                    (CONJECTURE WSINK-READY says never)
  SS_V     no W-sink and no H-sink switches to its target at t (CONJECTURE SINK-SWITCH, implied by WSINK-READY, says never)
  NOSINK_V U^W_t empty but sigma_t != sigma_(t+1) on X_b (cannot happen: the W-sink set is non-empty at every t < b)
MUT=1: W-sinks of U^W_t u U^H_t (the both-frame unsettled set of lwp/laststep.py) instead of U^W_t: WSR must bite (karena_kill_n71). Usage: wsink.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "lwp"))
import seglast
from common import rows, load, readstart
from staticdepth import walk
from relseg import cycof
from n5x import Engine
C = Counter(); EX = []; MUT = os.environ.get("MUT") == "1"

def _run(g, R, name):
    n = g.n; EN = Engine(g); Q = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2]
    for a, b in seglast.segs(g, R):
        if b <= a: continue
        B = R[b]; X, st = set(), list(Q)
        while st:
            x = st.pop()
            if x in X: continue
            X.add(x); st.extend(y for y in sum(walk(B["wn"], x), ()) + sum(walk(B["nxt"], x), ()) if g.owner[y] == 0)
        CW = frozenset().union(*[cycof(B["wn"], v) for v in X]) if X else frozenset()
        CH = frozenset().union(*[cycof(B["nxt"], v) for v in X]) if X else frozenset()
        T = {v for c in CW for v in c} | {v for c in CH for v in c}
        pw = {v: walk(B["wn"], v) for v in range(n)}; ph = {v: walk(B["nxt"], v) for v in range(n)}
        def first(v, key, p):
            s = b
            while s > a and walk(R[s - 1][key], v) == p[v]: s -= 1
            return s
        Ev = [v for v in X if v not in T]
        fW = {v: first(v, "wn", pw) for v in Ev}; fH = {v: first(v, "nxt", ph) for v in Ev}
        def jn(v, p):
            seq = list(p[v][0]) + list(p[v][1])
            for x in seq[1:]:
                if g.owner[x] == 0 and x not in T: return x
            return None
        JW = {v: jn(v, pw) for v in Ev}; JH = {v: jn(v, ph) for v in Ev}
        C["segs"] += 1
        for t in range(a, b):
            C["trans"] += 1
            I = set(EN.improving(tuple(R[t]["s"]), R[t]["vs"]))
            sig = R[t]["s"]
            def ready(v):
                return sig[v] == B["s"][v] or (v, B["s"][v]) in I
            UW = {v for v in Ev if fW[v] > t}; UH = {v for v in Ev if fH[v] > t}
            WS = [v for v in UW if JW[v] not in (UW | UH if MUT else UW)]; HS = [v for v in UH if JH[v] not in UH]
            if not UW and any(sig[v] != R[t + 1]["s"][v] for v in X): C["NOSINK_V"] += 1; EX.append(("NOSINK", name, a, b, t))
            for v in WS:
                if sig[v] == B["s"][v]: C["WSOFF_V"] += 1; EX.append(("WSOFF", name, a, b, t, v))
            for v in HS:
                if sig[v] == B["s"][v]: C["HSOFF_V"] += 1; EX.append(("HSOFF", name, a, b, t, v))
                if not ready(v): C["HSR_V"] += 1; EX.append(("HSR", name, a, b, t, v))
            rws = [v for v in WS if ready(v)]
            C["steps_unready_wsink"] += len(rws) < len(WS); C["wsinks"] += len(WS); C["wsinks_ready"] += len(rws); C["hsinks"] += len(HS)
            if not rws: C["WSR_V"] += 1; EX.append(("WSR", name, a, b, t, sorted(WS), sorted(UW)[:12]))
            for v in rws:
                if any(R[s]["s"][v] != B["s"][v] for s in range(t + 1, b + 1)): C["WSL_V"] += 1; EX.append(("WSL", name, a, b, t, v))
            nxt = R[t + 1]["s"]
            if not any(nxt[v] == B["s"][v] != sig[v] for v in WS + HS): C["SS_V"] += 1; EX.append(("SS", name, a, b, t))
            C["steps_hsink_switch"] += any(nxt[v] == B["s"][v] != sig[v] for v in HS)
            both = [v for v in WS if v in HS]
            C["steps_with_bothsink"] += bool(both)

def wsscore(g, R):
    """for lay/wclimb.py: dict of counters (sink-lemma failures LEM, SS_V, WSR_V, H-GROW failures HG, steps with no frontier vertex K,
    unready W-sinks U, steps with an unready W-sink S)."""
    global C, EX
    save = (C, EX); C, EX = Counter(), []
    try:
        _run(g, R, "x")
        return dict(LEM=sum(C[k] for k in ("WSL_V", "WSOFF_V", "HSOFF_V", "HSR_V", "NOSINK_V")), SS=C["SS_V"], WSR=C["WSR_V"],
                    HG=C["trans"] - C["steps_hsink_switch"], K=C["trans"] - C["steps_with_bothsink"], U=C["wsinks"] - C["wsinks_ready"],
                    S=C["steps_unready_wsink"])
    finally: C, EX = save

def run(g, name, start=None):
    E, R = rows(g, start); _run(g, R, name)

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p: run(load(os.path.join(ROOT, p[0])), p[0], readstart(os.path.join(ROOT, p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for z in EX[:10]: print("EXAMPLE", z)
    for k in ("WSOFF", "HSOFF", "HSR", "WSL", "WSR", "SS", "NOSINK"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__":
    main()
