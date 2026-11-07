#!/usr/bin/env python3
"""L-NEW box 143 CAUSE on 2-wide deg-2 IDEAL-ACYC ladders (R178 §1 rule; simulator = box139/paths.py run()).
Per genome prints:
- CELEMVIOL: steps t, movers x at which the C-element form fails: x moves to k at t  <=>  A_x(t) = k != sigma_(t-1)(x) and
  B_x(t-1) = k, where A_x(t) = the option of x toward L_(l-1)(t) (level 0: the gate-smaller option) and B_x(t-1) = the option whose
  face is strictly Xi-better at state t-1 (None on a tie).
- LEAST: classes of the least-level mover of each step t >= 2: DEL (delayed: released by the last carry s < t of level l-1, not moved
  in [s, t)), PRE (no carry of level l-1 before t; level 0 counts here), OTHER (must be 0: Lemma STEP-DELAY).
- BOUND: steps <= 1 + PRE + DELSTEPS, where DELSTEPS = steps whose least-level mover is delayed (STEP-DELAY).
- per delay (x, s'): the movers z that move at step s'-1 and lie on the Xi-play (state s'-2) of x's toward option; their levels and
  move classes (CAR = moved at a carry step of its own level - 1, DEL, PRE); NOCAUSE counts delays with no such z (must be 0).
- BFLIP: per mover, number of flips of B_x (strict Xi preference, ties skipped) and moves; DELAY(x) <= BFLIPS(x) (C-element).
Usage: cause.py genome.json ... [VERB=1 prints every delay]"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "box139", "paths.py")).read().split("def vx(G):")[0]
ns = {"__file__": os.path.join(HERE, "..", "box139", "paths.py")}; exec(src, ns); run = ns["run"]; fc = ns["fc"]
VERB = os.environ.get("VERB")
def analyse(G):
    S, CUR, KEY, why = run(G, cap=5000); N, opts, gate, lev = G["N"], G["opts"], G["gate"], G["lev"]; d = N // 2; T = len(S) - 1
    FACE = []
    for t in range(T + 1):
        val, idx, _, M = fc.values(G, list(S[t])); FACE.append([[val(N + idx[(v, k)]) for k in range(2)] for v in range(N)])
    def L(t, l):
        K = KEY[min(t, len(KEY) - 1)]; return 2 * l if K[2 * l] < K[2 * l + 1] else 2 * l + 1
    def A(t, x):
        l = lev[x]
        if l == 0: return 0 if gate[x][0] < gate[x][1] else 1
        tgt = L(t, l - 1); return 0 if opts[x][0][0] == tgt else (1 if opts[x][1][0] == tgt else None)
    def B(t, x):
        a, b = FACE[t][x]; return 0 if a > b else (1 if b > a else None)
    def play(t, x, k):
        out = []; y = opts[x][k][1]; seen = set()
        while y >= 0 and y not in seen: seen.add(y); out.append(y); y = opts[y][S[t][y]][1]
        return out
    mv = lambda t, x: S[t][x] != S[t - 1][x]
    carry = {(l, t) for l in range(d) for t in range(1, T + 1) if L(t, l) != L(t - 1, l)}
    def lastcarry(l, t):  # last carry step of level l at or before t
        c = [s for s in range(1, t + 1) if (l, s) in carry]; return c[-1] if c else None
    def cls(t, x):
        l = lev[x]
        if l > 0 and (l - 1, t) in carry: return "CAR"
        s = lastcarry(l - 1, t) if l > 0 else None
        if s is None: return "PRE"
        return "DEL" if all(not mv(u, x) for u in range(s, t)) else "OTHER"
    celem = 0
    for t in range(1, T + 1):
        for x in range(N):
            k = 1 - S[t - 1][x]; pred = A(t, x) == k and B(t - 1, x) == k
            if pred != mv(t, x): celem += 1
    least = {"DEL": 0, "PRE": 0, "OTHER": 0, "CAR": 0}; delsteps = 0; pre = 0
    for t in range(2, T + 1):
        ms = [x for x in range(N) if mv(t, x)]
        if not ms: continue
        h = min(ms, key=lambda x: lev[x]); c = cls(t, h); least[c] += 1
    # delays (as box142 lag.py: released by carry s, not moved at s, moves in (s, s*))
    dl = []; nocause = 0; causecls = {}; causelev = {}
    for l in range(1, d):
        cs = sorted(t for (ll, t) in carry if ll == l - 1)
        for i, s in enumerate(cs):
            nx = cs[i + 1] if i + 1 < len(cs) else T + 1; Lm = L(s, l - 1)
            for x in (2 * l, 2 * l + 1):
                if opts[x][S[s - 1][x]][0] == Lm or mv(s, x): continue
                for sp in range(s + 1, nx):
                    if mv(sp, x):
                        k = S[sp][x]; zs = [z for z in play(sp - 2, x, k) if mv(sp - 1, z)] if sp >= 2 else []
                        if not zs: nocause += 1
                        for z in zs[:1]:
                            c = cls(sp - 1, z); causecls[c] = causecls.get(c, 0) + 1
                            dz = lev[z] - l; causelev[dz] = causelev.get(dz, 0) + 1
                        dl.append((x, l, s, sp, zs, [cls(sp - 1, z) for z in zs]))
                        if VERB: print("  DELAY x", x, "lev", l, "carry", s, "moves", sp, "cause movers", zs, [cls(sp - 1, z) for z in zs], [lev[z] for z in zs])
                        break
    bfl = []
    for x in range(N):
        seq = [B(t, x) for t in range(T + 1) if B(t, x) is not None]
        bfl.append(sum(1 for i in range(1, len(seq)) if seq[i] != seq[i - 1]))
    moves = [sum(mv(t, x) for t in range(1, T + 1)) for x in range(N)]
    D = len(dl); pre = sum(1 for t in range(1, T + 1) for x in range(N) if mv(t, x) and cls(t, x) == "PRE")
    return dict(T=T, why=why, d=d, D=D, celem=celem, least=least, pre=pre, bound=1 + pre + least["DEL"], nocause=nocause,
                causecls=causecls, causelev=dict(sorted(causelev.items())), bflips=sum(bfl), moves=sum(moves), dl=dl)
if __name__ == "__main__":
    for p in sys.argv[1:]:
        r = analyse(json.load(open(p)))
        print(f"CAUSE {os.path.basename(p)} d {r['d']} STEPS {r['T']} STOP {r['why']} SUMDELAY {r['D']} CELEMVIOL {r['celem']} LEAST {r['least']} "
              f"PRE {r['pre']} STEPBOUND {r['bound']} NOCAUSE {r['nocause']} CAUSECLS {r['causecls']} CAUSELEVDIFF {r['causelev']} MOVES {r['moves']} BFLIPS {r['bflips']}")
