#!/usr/bin/env python3
"""L-RED 67 R237 (2)/(3): EXHAUSTIVE run of Lemma WRAP's six must-0 counters (wr237.check on BOTH own engines, w237.py:
n5x236 and the SPEC-exact n5s237, counters summed; tiediff = games on which the two engines' (T, iterations) differ) over EVERY
parity game H with n vertices in TARGET.md section 1's sense (owners, priorities in 0..n, every non-empty successor set, self-loops
allowed) and EVERY positional Even strategy s0. Aimed at the degenerate shapes the random lists of box 104 can miss: self-loops,
one-successor vertices, equal priorities, all-Even / all-Odd games, s0 already optimal (T = 0).
Count: (number of games with their s0) = (n + 1)^n * sum over owner vectors of prod_v (n * 2^(n-1) if Even else 2^n - 1); n = 1: 4,
n = 2: 441, n = 3: 438,976.
Env: BOX104, LNEW, LRED, LLIT (as wr237.py); CTRL=1 (control); OUT (default HERE/out); RESUME=1; TLIMIT seconds; PART=i/k (only the
games whose running index is i mod k; one checkpoint per part); XEVERY (second-engine sample, default 500; 0 = off).
Usage: exh237.py N"""
import sys, os, json, time, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "r236"))
import w237 as Wm
R = Wm.R
import pg
OUT = os.environ.get("OUT", os.path.join(HERE, "out")); TLIMIT = float(os.environ.get("TLIMIT", "1e18")); XEVERY = int(os.environ.get("XEVERY", "500"))
KEYS = ("s3fail", "nonstd", "nohoward", "fbwrong", "endwrong", "wrong")

def games(n):
    subsets = [list(s) for k in range(1, n + 1) for s in itertools.combinations(range(n), k)]
    for owner in itertools.product((0, 1), repeat=n):
        for prio in itertools.product(range(n + 1), repeat=n):
            for succ in itertools.product(subsets, repeat=n):
                for s0 in itertools.product(*[(succ[v] if owner[v] == 0 else [-1]) for v in range(n)]):
                    yield list(prio), list(owner), [list(s) for s in succ], list(s0)

if __name__ == "__main__":
    n = int(sys.argv[1]); pi, pk = (int(x) for x in os.environ.get("PART", "0/1").split("/")); os.makedirs(OUT, exist_ok=True)
    ck = os.path.join(OUT, f"ck_exh{n}_{pi}of{pk}.json"); t0 = time.time()
    S = dict(n=n, part=[pi, pk], ctrl=R.CTRL, next=0, done=0, tot={k: 0 for k in KEYS}, sumT=0, maxT=0, maxW=0, states=0, pairs=0, x=0, xdiff=0, xkill=0, cands=[], finished=False, tiediff=0, spec={k: 0 for k in Wm.SKEYS}, maxF=0, sumF=0)
    if os.environ.get("RESUME") == "1" and os.path.exists(ck): S = json.load(open(ck))
    def save():
        tmp = ck + ".tmp"; json.dump(S, open(tmp, "w")); os.replace(tmp, ck)
    def line(what):
        print(f"EXH237 n {n} part {pi}/{pk} {what}: games {S['done']} (index < {S['next']}) | " + " ".join(f"{k} {S['tot'][k]}" for k in KEYS)
              + f" | states {S['states']} pairs {S['pairs']} sumT {S['sumT']} maxT {S['maxT']} max|W| {S['maxW']} | second engine: sampled {S['x']} xdiff {S['xdiff']} xkill {S['xkill']}"
              f" | tiediff(x,s) {S['tiediff']} | N5 (spec, WRAP (v) + Remark 3): " + " ".join(f"{k} {S['spec'][k]}" for k in Wm.SKEYS) + f" maxF {S['maxF']} sumF {S['sumF']} | candidates {len(S['cands'])} ctrl {S['ctrl']}", flush=True)
    stopped = False
    for idx, (prio, owner, succ, s0) in enumerate(games(n)):
        if idx < S["next"]: continue
        if time.time() - t0 > TLIMIT: stopped = True; break
        S["next"] = idx + 1
        if idx % pk != pi: continue
        H = pg.Game(prio, owner, succ); c, T, its, wn = Wm.check(H, s0, "x"); cs, Ts, itss, _ = Wm.check(H, s0, "s"); S["done"] += 1
        S["tiediff"] += int((T, its) != (Ts, itss)); c = {k: c[k] + cs[k] for k in c}
        cv, F, itv, _ = Wm.check_spec(H, s0); S["maxF"] = max(S["maxF"], F); S["sumF"] += F
        for k in Wm.SKEYS: S["spec"][k] += cv[k]
        c["spec"] = sum(cv.values())
        for k in KEYS: S["tot"][k] += c[k]
        nE = sum(1 for o in owner if o == 0); S["sumT"] += T; S["maxT"] = max(S["maxT"], T); S["maxW"] = max(S["maxW"], wn); S["states"] += T + 1; S["pairs"] += T * nE
        if sum(c.values()) and len(S["cands"]) < 50:
            c2, T2, its2, _ = R.WR.check(H, s0); S["cands"].append(dict(idx=idx, prio=prio, owner=owner, succ=succ, s0=s0, own=dict(c=c, T=T, iterations=its), second=dict(c=c2, T=T2, iterations=its2)))
            print(f"EXH237 CANDIDATE idx {idx}: prio {prio} owner {owner} succ {succ} s0 {s0} own {c} T {T} its {its} | second engine {c2} T {T2} its {its2}", flush=True)
        elif XEVERY and S["done"] % XEVERY == 0:
            c2, T2, its2, _ = R.WR.check(H, s0); S["x"] += 1; S["xdiff"] += int((T2, its2) != (T, its)); S["xkill"] += int(sum(c2.values()) > 0)
        if S["done"] % 2000 == 0: save(); line("at")
    S["finished"] = not stopped; save(); line("END (all games)" if S["finished"] else "PAUSED (TLIMIT)")
