#!/usr/bin/env python3
"""REFEREE successor 36: firing controls for successor 35's lemma counters (gk_lemck.check_state: SBAR, TAU, ESC0, ESC, W, XI, AV,
STEP of P-N5-REACH section 6 / REACH3's step, one N5 transition from the standard state of an arbitrary mover state of G_k).
The unperturbed row must be all 0; each perturbation row shows which counters it fires.
  noesc    no escape edge beta_g -> pb_g at the options whose Xi-target is a mover
  rank     the game built with the beta-ranks reversed, the model keeps br
  oddE     every e-vertex priority + 1 (odd, still above every beta)
  ungraded one option of a level-2 mover gets a level-0 W-target (game and model both built from the mutant)
  k1even   K1's priority 5 -> 4
  revE     e-indices in reversed gate order (successor 35's control)
Usage: gkx_lem.py k nstates seed"""
import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gkx
import gkx_n5
import rl_engine as eng
import gk_gamma3 as g3
import gk_lemck as LK


def main():
    k, ns, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    J, meta = gkx.rule(k)
    S, _ = gkx.run(J)
    rnd = random.Random(seed)
    states = []
    for i in range(ns):
        if rnd.random() < 0.5:
            states.append([rnd.randrange(2) for _ in range(J["N"])])
        else:
            s = list(S[rnd.randrange(len(S))])
            for _ in range(rnd.randrange(0, 4)):
                x = rnd.randrange(J["N"])
                s[x] = 1 - s[x]
            states.append(s)
    for ctl in ("", "noesc", "rank", "oddE", "ungraded", "k1even", "revE"):
        G = gkx_n5.to_dict(J)
        Gb = G
        if ctl == "rank":
            Gb = json.loads(json.dumps(G))
            M = sum(G["deg"])
            Gb["br"] = [M - 1 - r for r in G["br"]]
        if ctl == "ungraded":
            G = json.loads(json.dumps(G))
            x = meta["idx"]["u2"]
            G["wt"][x][0] = meta["idx"]["u0"]
            Gb = G
        prio, owner, succ, names, idx = g3.build3_revE(Gb) if ctl == "revE" else g3.build3(Gb)
        if ctl == "noesc":
            for x in range(G["N"]):
                for kk in range(G["deg"][x]):
                    if G["xt"][x][kk] != "X":
                        b = idx[("b", (x, kk))]
                        succ[b] = [w for w in succ[b] if w != idx[("pb", (x, kk))]]
        if ctl == "oddE":
            for x in range(G["N"]):
                for kk in range(G["deg"][x]):
                    prio[idx[("e", (x, kk))]] += 1
        if ctl == "k1even":
            prio[idx["K1"]] = 4
        g = eng.Game(prio, owner, succ)
        gd = g.dual()
        c = dict(SBAR=0, TAU=0, ESC0=0, ESC=0, W=0, XI=0, AV=0, STEP=0, moved=0, stopped=0)
        err = 0
        for s in states:
            try:
                LK.check_state(G, g, gd, idx, prio, owner, succ, s, c)
            except Exception:
                err += 1
        print(f"lem k {k} ctl {ctl or 0} states {ns} seed {seed} " + " ".join(f"{a} {c[a]}" for a in ("SBAR", "TAU", "ESC0", "ESC", "W", "XI", "AV", "STEP"))
              + f" moved {c['moved']} stopped {c['stopped']} errors {err}", flush=True)


if __name__ == "__main__":
    main()
