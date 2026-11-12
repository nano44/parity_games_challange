#!/usr/bin/env python3
"""Engine comparison of `PG.Genome.IdealCycRun` (PGLemmas/Genome.lean) with the fleet's IDEAL-CYC run.

DATA about the TRANSCRIPTION, not a proof and not the Lean code: the script evaluates, in Python, the
five fields of `IdealCycRun σ τ T` exactly as Genome.lean states them (frozen, legal, opt, howard,
moves), and `FromStart`, `Stopped`, on the run that the fleet's engine produces:
  states σ_0, …, σ_T   experiments/new/box191/idealcyc.py  run(G)  (Howard at the movers of Γ(G), every
                       other Even vertex frozen at R104's start; valuation engine experiments/si/si.py);
  σ̄_t                 the counterstrategy that si.py's Engine.evaluate returns for σ_t.
A match says: the engine's run is an `IdealCycRun` in the sense of the Lean definition, as far as the
checks below reach.  It does not replace any Lean proof.

The game.  Lean's Γ(G) (`Genome.E`, `prio`, `isOdd`, `start0`, `pr`) was compared, vertex by vertex, with
experiments/red/r187/stab.py build(G, 0, kgad=True, esc=True) by check/genomecheck.py on these genomes.
Here that reference game is the Lean side (E, V0, start0, pr = 2*rank + parity with rank by
(priority, index)), and `builddiff` checks that the game idealcyc.py restricts (box189
gamma3.build(G, {})) is the same game.

Values and order.  `vals` evaluates Defs.lean's `val pr s v = (lam, pset, plen)` by walking the play of
`v` (`lam`: the vertex of largest `pr` on the play's cycle; `plen`: the first n with s^[n] v = lam;
`pset`: the vertices before that which are more relevant than `lam`).  `fastdiff` compares it with the
line-by-line transcription of Defs.lean in check/crosscheck.py at every vertex of every state of the run
(the deviations of `devfail` are evaluated by `vals` only).  `Val.lt`, `Val.le` are crosscheck.py's
transcriptions.

Counters (all must be 0 without a control); the unit is printed with each:
  builddiff    gamma3.build(G, {}) differs from stab.build(G, 0, kgad, esc) at a vertex (priority, owner,
               successor set or start); unit: vertex
  prdiff       Lean's pr differs from si.py's injective priority p'; unit: vertex
  fastdiff     `vals` differs from crosscheck.py's `val`; unit: (state t ≤ T, vertex)
  frozenfail   IdealCycRun.frozen: an Even vertex that is not a mover has σ_t(v) ≠ start0(v);
               unit: (state t ≤ T, Even non-mover)
  legalfail    IdealCycRun.legal: σ_t(mover x) ∉ E(mover x); unit: (state t ≤ T, mover)
  taufail      IdealCycRun.opt, first clause of OptCounter: σ̄_t(u) ∉ E(u) at an Odd vertex;
               unit: (state t ≤ T, Odd vertex)
  valdiff      IdealCycRun.opt, agreement with si.py's optimum: val pr (nxt t) v differs from the value
               Engine.evaluate(σ_t) gives v; unit: (state t ≤ T, vertex)
  devfail      IdealCycRun.opt, second clause of OptCounter at τ₂ := Function.update (τ t) g w, for every
               Odd vertex g and every other successor w of g: NOT Val.le (val (nxt t) v) (val (pair σ_t
               τ₂) v); unit: (state t ≤ T, vertex v, deviation (g, w))
  howardfail   IdealCycRun.howard: HowardAt pr E (nxt t) (nxt (t+1)) (mover x) fails (one of its three
               clauses); unit: (step t < T, mover)
  movesfail    IdealCycRun.moves: no mover has a successor of strictly larger value; unit: step t < T
  startfail    FromStart: σ_0(mover x) ≠ start0(mover x); unit: mover
  stopfail     Stopped at T: a mover has a successor of strictly larger value; unit: (mover, gate)
LABEL for `opt` (Lead 2026-11-12 17:22Z): «optimality checked as local optimality of a one-player
counterstrategy plus agreement with si.py's optimum; full enumeration not done».  `OptCounter`
quantifies over all Odd strategies (2^(M+1) of them); only the single-vertex deviations are evaluated.

Controls (IDEAL_CTRL):
  how   breaks HowardAt: at every step the first mover whose gates do not all tie is sent to a
        ⊴-smallest gate instead of its new successor; howardfail must fire.
  opt   makes one gate non-optimal: at every state the first gate (index order) whose switch to the other
        face changes some value is switched; devfail (and valdiff) must fire.

Usage (from the repository root):
    python3 -I lean/lemmas/check/idealcheck.py experiments/new/box191/inst/*.json
Exit code 0: without a control, every counter is 0; with a control, its counter fired.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path[:0] = [HERE, os.path.join(ROOT, "experiments", "new", "box191"),
                os.path.join(ROOT, "experiments", "red", "r187")]
import crosscheck as cc  # noqa: E402  (the line-by-line transcription of Defs.lean)
import idealcyc  # noqa: E402  (the fleet's IDEAL-CYC run; adds box189, si and harness to the path)
import gamma3  # noqa: E402
import si  # noqa: E402
import stab  # noqa: E402

cc.CTRL = False
CTRL = os.environ.get("IDEAL_CTRL", "")
NAMES = ["builddiff", "prdiff", "fastdiff", "frozenfail", "legalfail", "taufail", "valdiff", "devfail",
         "howardfail", "movesfail", "startfail", "stopfail"]
SIZES = ["vertices", "states", "steps", "fastchecks", "valchecks", "devchecks", "howardchecks", "stopchecks"]


def vals(pr, s):
    """val pr s v = (lam, pset, plen) for every v, by walking the play of v."""
    out = []
    for v in range(len(s)):
        seq, pos, u = [], {}, v
        while u not in pos:
            pos[u] = len(seq)
            seq.append(u)
            u = s[u]
        lam = max(seq[pos[u]:], key=lambda w: pr[w])      # the cycle vertex of largest priority
        k = pos[lam]                                       # the first n with s^[n] v = lam
        out.append((lam, frozenset(w for w in seq[:k] if pr[lam] < pr[w]), k))
    return out


def check(path):
    G = json.load(open(path))
    N = G["N"]
    c = dict.fromkeys(NAMES + SIZES, 0)
    # ---- the Lean side: the game genomecheck.py compared with Genome.lean
    ref, rsig, rtau = stab.build(G, 0, kgad=True, esc=True)[:3]
    n = ref.n
    odd = [ref.owner[v] == 1 for v in range(n)]
    E = [sorted(set(ref.succ[v])) for v in range(n)]
    start0 = [rtau[v] if odd[v] else rsig[v] for v in range(n)]
    order = sorted(range(n), key=lambda v: (ref.prio[v], v))
    pr = [0] * n
    for r, v in enumerate(order):
        pr[v] = 2 * r + ref.prio[v] % 2
    movers = list(range(N))                                # Lean: idx (mover x) = x
    # ---- the engine side
    gm, gsig, gtau, V = gamma3.build(G, set())
    for v in range(n):
        gstart = gtau[v] if gm.owner[v] == 1 else gsig[v]
        c["builddiff"] += (gm.n != n or gm.prio[v] != ref.prio[v] or gm.owner[v] != ref.owner[v]
                           or sorted(set(gm.succ[v])) != E[v] or gstart != start0[v])
    h, s0, emovers, _ = idealcyc.build(G)
    assert emovers == movers
    eng = si.Engine(h)
    c["prdiff"] = sum(eng.pp[v] != pr[v] for v in range(n))
    run = idealcyc.run(G)
    T = len(run) - 1
    c["vertices"], c["states"], c["steps"] = n, T + 1, T
    sig, s, val = [], [], []
    for t in range(T + 1):
        strat = list(s0)
        for x in movers:
            strat[x] = V[("g", (x, run[t][x]))]
        ev, tau = eng.evaluate(tuple(strat))
        st = [tau[v] if odd[v] else strat[v] for v in range(n)]      # nxt V0 σ τ t = pair V0 (σ t) (τ t)
        vt = vals(pr, st)
        if CTRL == "opt":                                  # one gate made non-optimal
            for g in range(N, N + (n - N - 6) // 3):       # the gates: indices N, …, N + M − 1
                if odd[g] and len(E[g]) == 2:
                    s2 = list(st)
                    s2[g] = E[g][0] if st[g] == E[g][1] else E[g][1]
                    v2 = vals(pr, s2)
                    if v2 != vt:
                        st, vt = s2, v2
                        break
        sig.append(strat)
        s.append(st)
        val.append(vt)
        # frozen, legal, the first clause of OptCounter
        for v in range(n):
            if not odd[v] and v >= N:
                c["frozenfail"] += strat[v] != start0[v]
            if odd[v]:
                c["taufail"] += st[v] not in E[v]
        for x in movers:
            c["legalfail"] += strat[x] not in E[x]
        # agreement with si.py's optimum, value by value
        for v in range(n):
            w, mask, ln = ev[v]
            c["valchecks"] += 1
            c["valdiff"] += vt[v] != (w, frozenset(u for u in range(n) if mask & eng.bit[u]), ln)
        # OptCounter at the single-vertex deviations
        for g in range(n):
            if odd[g]:
                for w in E[g]:
                    if w != st[g]:
                        s2 = list(st)
                        s2[g] = w
                        v2 = vals(pr, s2)
                        for v in range(n):
                            c["devchecks"] += 1
                            c["devfail"] += not cc.val_le(pr, vt[v], v2[v])
    # the literal transcription of Defs.lean, at every vertex of every state
    for t in range(T + 1):
        for v in range(n):
            c["fastchecks"] += 1
            c["fastdiff"] += cc.val(pr, s[t], v) != val[t][v]
    for x in movers:
        c["startfail"] += sig[0][x] != start0[x]
    for t in range(T):
        vt = val[t]
        broken = False
        better = False
        for x in movers:
            a = s[t + 1][x]
            if CTRL == "how" and not broken:
                low = min(E[x], key=lambda w: (sum(cc.val_lt(pr, vt[u], vt[w]) for u in E[x]), w))
                if cc.val_lt(pr, vt[low], vt[a]):
                    a, broken = low, True
            best_new = a in E[x] and all(cc.val_le(pr, vt[w], vt[a]) for w in E[x])
            cur_best = s[t][x] in E[x] and all(cc.val_le(pr, vt[w], vt[s[t][x]]) for w in E[x])
            c["howardchecks"] += 1
            c["howardfail"] += not (best_new and (not cur_best or a == s[t][x]))
            better = better or any(cc.val_lt(pr, vt[sig[t][x]], vt[y]) for y in E[x])
        c["movesfail"] += not better
    for x in movers:
        for y in E[x]:
            c["stopchecks"] += 1
            c["stopfail"] += cc.val_lt(pr, val[T][sig[T][x]], val[T][y])
    return c


def main():
    total = dict.fromkeys(NAMES + SIZES, 0)
    for path in sys.argv[1:]:
        c = check(path)
        for k in total:
            total[k] += c[k]
        print(f"{os.path.basename(path)}: n {c['vertices']} T {c['steps']} "
              + " ".join(f"{k} {c[k]}" for k in NAMES))
    print(f"idealcheck ctrl {CTRL or 'none'}: genomes {len(sys.argv) - 1} "
          + " ".join(f"{k} {total[k]}" for k in SIZES) + " | " + " ".join(f"{k} {total[k]}" for k in NAMES))
    print("opt: optimality checked as local optimality of a one-player counterstrategy plus agreement with "
          "si.py's optimum; full enumeration not done")
    if CTRL == "how":
        return 0 if total["howardfail"] > 0 else 1
    if CTRL == "opt":
        return 0 if total["devfail"] > 0 else 1
    return 0 if all(total[k] == 0 for k in NAMES) else 1


if __name__ == "__main__":
    sys.exit(main())
