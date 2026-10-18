"""L-ALG succ. 8 (produced on Opus 5.5, 2026-10-18 box 11), GAP-A-M §25b: check A_DTL's run on the Two Counters family tc(N)
(Oink tools/oink/build/tc N) against the schema of (TC-6). Lane of bit i of player p: K_i^p = {p-i-T, p-i-S-j, p-i-A-j (j < i),
p-i-Z} (labels of tc.cpp). Schema: 6 searches, phases [3, 1, 2] (Even, Even, Odd); learned tangles in birth order per search:
Even s0 = {K_{N-1}^E, BIG}, s1 = {K_1^E .. K_{N-2}^E}, s2 = {K_0^E}; s3 none; Odd s4 = {K_1^O .. K_{N-1}^O}, s5 = {K_0^O}; dominions:
the Even half (all "Even-*" vertices) at s2, the Odd half at s5; BIG = the Even half minus the Even H/L of nothing (recorded, not
asserted). Prints per N: PASS or the first difference. Usage: RM_LIGHT=1 RM_DV=0 DTL_ORDER=oink|stable dtl_tcschema.py N1 N2 ..."""
import sys, os, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_drthr as DT
FD = DT.FD
TC = os.path.join(HERE, "..", "..", "tools", "oink", "build", "tc")

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for N in map(int, sys.argv[1:]):
        txt = subprocess.run([TC, str(N)], capture_output=True, text=True).stdout; lab = {}
        for line in txt.splitlines():
            m = re.match(r'\s*(\d+)\s+(\d+)\s+(\d)\s+[\d,]+\s+"([^"]*)"', line)
            if m: lab[int(m.group(1))] = m.group(4)
        tmp = f"/tmp/claude-0/-home-user-parity-games-challange/38b90299-6041-5d2b-9b30-739bfc675b03/scratchpad/tc/s{N}.pg"; open(tmp, "w").write(txt)
        g = pg.read(tmp); d0 = FD.P.X.build(g); d = DT.DR(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        name = lambda v: lab[d.idx[v]]
        def lane(p, i): return frozenset([f"{p}-{i}-T", f"{p}-{i}-Z"] + [f"{p}-{i}-{c}-{j}" for j in range(i) for c in "SA"])
        born = []                      # (search index, frozenset of names) per tangle in birth order
        k = 0
        for s, tr in enumerate(d.trace):
            nt = tr["recs"][-1]["ntv"] if tr["recs"] else k
            # tangles born during search s: indices from the first rec's ntv of search s to the first rec's ntv of search s+1
        starts = [tr["recs"][0]["ntv"] if tr["recs"] else None for tr in d.trace] + [len(d.tv)]
        for s in range(len(d.trace)):
            a = starts[s]; b = next(x for x in starts[s + 1:] if x is not None)
            for t in range(a, b): born.append((s, frozenset(name(v) for v, _ in d.tv[t])))
        exp = [(0, lane("Even", N - 1)), (0, "BIG")] + [(1, lane("Even", i)) for i in range(1, N - 1)] + [(2, lane("Even", 0))] \
            + [(4, lane("Odd", i)) for i in range(1, N)] + [(5, lane("Odd", 0))]
        ph = [len(p) for p in FD.phase_rows(d)]; ok = (d.iterations == 6 and ph == [3, 1, 2] and len(born) == len(exp))
        diff = None
        if ok:
            for (s1, a1), (s2, a2) in zip(born, exp):
                if s1 != s2 or (a2 != "BIG" and set(a1) != set(a2)): ok = False; diff = (s1, sorted(a1)[:6], s2, sorted(a2)[:6] if a2 != "BIG" else a2); break
        big = [sorted(a)[:4] + ["..."] + [len(a)] for s, a in born if s == 0 and len(a) > 4 * N]
        print(f"N {N} n {len(d.pr)} {os.environ.get('DTL_ORDER')}: iterations {d.iterations} phases {ph} tangles {len(born)} (schema {len(exp)}) ->",
              "PASS" if ok else f"DIFFERS {diff}", "| BIG size", [len(a) for s, a in born if s == 0 and a != lane('Even', N - 1)], flush=True)
