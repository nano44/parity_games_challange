#!/usr/bin/env python3
"""L-RED R191 NESTCLIMB: hill-climb IDEAL-ACYC W-ladders (width w, degree D; r190/delclimb genome format and mutations) to realise a
move SCHEDULE exactly: score = length of the longest prefix of steps whose set of movers equals the schedule's (then L).
Schedule NEST(d) of R189 §2 (r189/lag/schedbmc.nest) unless SCHED=json. Usage: nestclimb.py d w D iters seed out.json"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178"), os.path.join(H, "..", "r190")]
import ideal, delclimb
def nest(d, w):
    ev = {}
    def R(l, t):
        if l == d: return 0
        ev.setdefault(t, set()).add(w * l); Dd = R(l + 1, t) or 1
        ev.setdefault(t + Dd, set()).add(w * l + 1); R(l + 1, t + Dd); return 2 * Dd
    R(0, 1); T = max(ev); return [sorted(ev.get(t, [])) for t in range(1, T + 1)]
def score(G, sched):
    S, why = ideal.traj(G, cap=len(sched) + 5); N = G["N"]; m = 0
    for t in range(1, len(S)):
        mv = [v for v in range(N) if S[t][v] != S[t - 1][v]]
        if t - 1 < len(sched) and mv == sched[t - 1]: m += 1
        else: return (m, -len(set(mv) ^ set(sched[t - 1])) if t - 1 < len(sched) else 0, len(S) - 1)
    return (m, -len(sched[m]) if m < len(sched) else 0, len(S) - 1)
if __name__ == "__main__":
    d, w, D, it, seed = map(int, sys.argv[1:6]); out = sys.argv[6]; rng = random.Random(seed)
    sched = json.loads(os.environ["SCHED"]) if os.environ.get("SCHED") else nest(d, w)
    def fresh():
        G = delclimb.rand(d, w, D, rng)
        if os.environ.get("PI") == "nest4":
            # R195 escape shape at degree 4: v_0..v_(d-2) < u_(d-2) < v_(d-1) = q < u_(d-1) = p < u_(d-3) .. u_0
            order = [w * l + 1 for l in range(d - 1)] + [w * (d - 2), w * (d - 1) + 1, w * (d - 1)] + [w * l for l in range(d - 3, -1, -1)]
            G["pi"] = [order.index(v) for v in range(G["N"])]
            for v in range(G["N"]):
                for o in G["opts"][v]: o[1] = rng.choice([u for u in range(G["N"]) if G["pi"][u] > G["pi"][v]] + [-1])
        if os.environ.get("PI") == "nest":
            # forced order (R191 §3): v_0 .. v_(d-2), v_(d-1) = q, u_(d-1) = p, u_(d-2), ..., u_0; Xi-targets re-drawn forward
            order = [w * l + 1 for l in range(d)] + [w * l for l in range(d - 1, -1, -1)]
            G["pi"] = [order.index(v) for v in range(G["N"])]
            for v in range(G["N"]):
                for o in G["opts"][v]: o[1] = rng.choice([u for u in range(G["N"]) if G["pi"][u] > G["pi"][v]] + [-1])
        return G
    G = fresh(); sc = score(G, sched); best = (sc, G)
    for i in range(it):
        if i % 20000 == 0 and i: G = json.loads(json.dumps(best[1])); sc = best[0]
        if i % 50000 == 0 and i and best[0][0] < len(sched) and rng.random() < 0.3: G = fresh(); sc = score(G, sched)
        H2 = delclimb.mutate(G, rng)
        if os.environ.get('PI') in ('nest', 'nest4') and H2['pi'] != G['pi']: continue
        s2 = score(H2, sched)
        if s2 >= sc: G, sc = H2, s2
        if sc > best[0]: best = (sc, json.loads(json.dumps(G))); json.dump(G, open(out, "w"))
        if best[0][0] == len(sched): break
    print(f"NESTCLIMB d {d} w {w} D {D} seed {seed} matched {best[0][0]} / {len(sched)} L {best[0][2]} iters {i + 1}", flush=True)
