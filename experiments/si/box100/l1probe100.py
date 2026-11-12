#!/usr/bin/env python3
"""L-SI box 100: L1 probe. One-player Howard runs in G_C[sbar] (Odd's face fixed at every gate of C; movers outside C fixed at their final
HOW3 choice; C = largest SCC of D(G)). Engine pieces from L-RED 65 how3_232 / r221q own.py at 59daaef2 (read-only, env RED): Gamma3 graph
(elev230.build), VJ order, own.evaluate (Odd has no choice left at C's gates). Howard: every mover of C to a best successor, keeping the
current one if best; ties else: larger index (rule "idx") or uniformly random among the best (rule "rnd").
sbar sets: "run" = every distinct sbar|C occurring in the actual HOW3 run; "rand" = K random face maps. Starts: the run's state at the
interval start (for "run") plus S random mover strategies of C. Also: maxLamSteps = max over runs of the iterations at which
some C mover's cycle top Lambda changes; maxLamGap = max over runs of consecutive iterations with no such change. Prints per instance: N_C, M_C, #sbar tried, #runs, max L1 (iterations
until no mover of C improves), max L1 / N_C, max L1 / M_C.
Usage: l1probe100.py SEED K S G.json ..."""
import sys, os, json, random, functools
R = os.environ["RED"]; sys.path.insert(0, os.path.join(R, "experiments/red/r232"))
import how3_232 as H, own
STAT = []
def howard1(gm, sig0, tau0, V, O, G, C, face, start, fixed, rng, rule, cap=10000):
    n = gm.n; ow = list(gm.owner); succ = [list(s) for s in gm.succ]
    for (x, k), f in face.items(): g = V[("g", (x, k))]; succ[g] = [f]
    vj = own.VJ(gm.prio); key = functools.cmp_to_key(vj.cmp)
    sig = [sig0[v] if (ow[v] == 0 and v in sig0) else (succ[v][0] if ow[v] == 0 else None) for v in range(n)]
    for x in range(G["N"]): sig[x] = V[("m", (x, start[x] if x in C else fixed[x]))]
    tb = {v: (succ[v][0] if len(succ[v]) == 1 else (tau0[v] if v in tau0 else succ[v][0])) for v in range(n) if ow[v] == 1}
    it = 0; lam0 = None; gap = 0; gmax = 0; lsteps = 0
    while it <= cap:
        vals, tb = own.evaluate(n, ow, succ, vj, sig, tb); ns = list(sig)
        lam = tuple(vals[x][0] for x in sorted(C))
        if lam0 is not None:
            if lam != lam0: lsteps += 1; gap = 0
            else: gap += 1; gmax = max(gmax, gap)
        lam0 = lam
        for x in C:
            cur = key(vals[sig[x]]); best = max(key(vals[w]) for w in succ[x])
            if not best > cur: continue
            B = [w for w in succ[x] if not key(vals[w]) < best and not key(vals[w]) > best]
            ns[x] = max(B) if rule == "idx" else rng.choice(B)
        if ns == sig: STAT.append((lsteps, gmax)); return it
        sig = ns; it += 1
    return it
def main():
    rng = random.Random(int(sys.argv[1])); K = int(sys.argv[2]); S = int(sys.argv[3])
    for fn in sys.argv[4:]:
        G = json.load(open(fn)); G = G.get("genome", G); G.pop("_evals", None)
        full = []; seq = H.how3(G, full=full); cs, comp, succD = H.sccs(G); C = max(cs, key=len); Cs = set(C)
        gm, sig0, tau0, V, O = H.build(G); fixed = seq[-1]
        Q = [(x, k) for x in C for k in range(len(G["opts"][x]))]
        faces = []; seen = set()
        for t, fu in enumerate(full):
            fc = tuple(fu[1][V[("g", q)]] for q in Q)
            if fc not in seen: seen.add(fc); faces.append(("run", dict(zip(Q, fc)), seq[t]))
        for _ in range(K):
            faces.append(("rand", {q: rng.choice([V[("pe", q)], V[("pbeta", q)]]) for q in Q}, None))
        mx = 0; runs = 0; del STAT[:]
        for kind, face, st in faces:
            starts = ([st] if st else []) + [[rng.randrange(len(G["opts"][x])) for x in range(G["N"])] for _ in range(S)]
            for s0 in starts:
                for rule in ("idx", "rnd"):
                    L = howard1(gm, sig0, tau0, V, O, G, Cs, face, s0, fixed, rng, rule); runs += 1; mx = max(mx, L)
        MC = len(Q)
        print(os.path.basename(fn), "N_C", len(C), "M_C", MC, "sbar", len(faces), "runs", runs, "maxL1", mx,
              "L1/N_C", round(mx / len(C), 3), "L1/M_C", round(mx / MC, 3), "maxLamSteps", max(a for a, b in STAT), "maxLamGap", max(b for a, b in STAT), flush=True)
main()
