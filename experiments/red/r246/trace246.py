#!/usr/bin/env python3
"""L-RED 71 R246: mover-state trace of the scheme's run on a Gamma3-type game built by g3_246 (own engine n5s237), compared with the run
on a second game of the same genome (e.g. EMODE top against r104) and with the IDEAL key run of the genome (r187 ideal.traj).
Prints, per game: its, fb, the iteration of each fallback, F = number of transitions before the first fallback, and
  nonmover  transitions before the first fallback at which a non-mover Even vertex or tau changes (must be 0 for a mover-only run)
  ideal_mism  1 if the mover states 0..L of the game run differ from the IDEAL key run's states s_0..s_L (L = L(G)); must be 0
  model_avail2_sum  sum over the IDEAL states s_0..s_L of #{movers x : |A_s(x)| >= 2} (the MODEL's count of mover ties met by S4a at
              iterations 1..L+1 on Gamma3(G), by Lemma W (iii) of P-N5-REALIZE: TIE(x) = R(x)); per state in model_avail2_per_state
  prefix_eq   length of the common prefix of the two games' mover-state sequences (when two EMODEs are given)
Usage: trace246.py MODE GENOME.json EMODE [EMODE2]"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r237"), os.path.join(HERE, "..", "r187"), os.path.join(HERE, "..", "r178")]
import n5s237, g3_246
mode, fn = sys.argv[1], sys.argv[2]; G = json.load(open(fn)); N = G["N"]
def run(emode):
    prio, own, succ, V = g3_246.build(G, emode); tr = []; fbt = []
    it, fb, win, s, sb = n5s237.run(prio, own, succ, mode, trace=tr, fbtrace=fbt)
    tr.append((s, None))
    ms = [g3_246.mover_state(G, V, st[0]) for st in tr]
    F = (fbt[0] - 1) if fbt else it
    nonmover = 0
    for j in range(1, F + 1):
        a, b = tr[j - 1], tr[j]
        if any(a[0][v] != b[0][v] for v in a[0] if v >= N) or (b[1] is not None and a[1] != b[1]): nonmover += 1
    return it, fb, fbt, F, nonmover, ms
res = {}
for em in sys.argv[3:]:
    it, fb, fbt, F, nonmover, ms = run(em); res[em] = ms
    try:
        import ideal
        st, why = ideal.traj(G); L = len(st) - 1
        mism = int([tuple(x) for x in ms[:L + 1]] != [tuple(x) for x in st])
        import fastcyc
        av = []                                                 # model count: movers with >= 2 available options, per IDEAL state
        for s_ in st:
            val, idx, _, M_ = fastcyc.values(G, list(s_)); face = lambda v, k: val(N + idx[(v, k)])
            av.append(sum(1 for v in range(N) if any(k != s_[v] and face(v, k) > face(v, s_[v]) for k in range(len(G["opts"][v])))))
        extra = f"L {L} end {why} ideal_mism {mism} model_avail2_sum {sum(av)} model_avail2_per_state {','.join(map(str, av))}"
    except Exception as e:
        extra = f"ideal_unavailable ({type(e).__name__}: {e})"
    print("TRACE246", os.path.basename(fn), "emode", em, "mode", mode, "its", it, "fb", fb, "fb_at", fbt, "F", F, "nonmover", nonmover, extra, flush=True)
if len(res) == 2:
    a, b = list(res.values()); p = 0
    while p < min(len(a), len(b)) and a[p] == b[p]: p += 1
    print("TRACE246 prefix_eq", p, "of", len(a), len(b), flush=True)
