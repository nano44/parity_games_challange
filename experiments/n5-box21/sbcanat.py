#!/usr/bin/env python3
"""Box 21 (Lead 16:46Z): anatomy of N5-SF's σ̄ changes on friedmannsubexp (n5sf.py, verbatim L-NEW copy). Per run (start S3 or lastedge):
SF iterations, SBC_σ, DSB (distinct σ̄ values), the vertex CLASSES (letter of the PGSolver description: e cycle centre, v/w bad-entry
selectors, ...) at which σ̄ changes (count of (transition, vertex) changes per class), and the cycle-centre word: bit i = 1 iff
σ̄(e_i) = d(i,1) (Odd closes bit i's cycle), its sequence of distinct values along the run, whether it is a binary counter (consecutive
distinct words = consecutive integers, reading e_{N-1} as the top bit) and how far it gets. Regions are checked against Oink zlk.
Usage: sbcanat.py [--start s3|lastedge] GAME.pg ...   (prints one ANAT JSON line per game)"""
import json, os, re, subprocess, sys, tempfile, time
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(EXP, "n5-box20", "lnew_box54")); sys.path.insert(0, os.path.join(EXP, "harness"))
import n5sf, pg  # noqa: E402
OINK = os.path.join(EXP, "..", "tools", "oink", "build", "oink")


def main():
    a = sys.argv[1:]; mode = "s3"
    if a[0] == "--start":
        mode = a[1]; a = a[2:]
    for path in a:
        t0 = time.time(); g = pg.read(path); n = g.n; L = g.labels; cls = [re.match(r"[a-z]+", x).group(0) for x in L]
        sd = None
        if mode == "lastedge":
            from n5x import Engine, dual, start_pair
            E0, Ed0 = Engine(g), Engine(dual(g)); _, t = start_pair(g, E0, Ed0, None)
            sd = ({v: max(g.succ[v]) for v in range(n) if g.owner[v] == 0}, {v: t[v] for v in range(n) if g.owner[v] == 1})
        E, T = n5sf.trace(g, sd); T2 = [x for x in T if "lam" in x]
        ch = {}; sbc = 0
        for i in range(len(T2) - 1):
            d = [v for v in range(n) if T2[i]["sb"][v] != T2[i + 1]["sb"][v]]
            if d: sbc += 1
            for v in d: ch[cls[v]] = ch.get(cls[v], 0) + 1
        dsb = len({tuple(x["sb"]) for x in T2})
        idx = {lab: v for v, lab in enumerate(L)}; N = sum(1 for lab in L if re.fullmatch(r"e\d+", lab))
        e = [idx[f"e{i}"] for i in range(N)]; d1 = [idx[f"d({i},1)"] for i in range(N)]
        words = []
        for x in T2:
            wv = sum(1 << i for i in range(N) if x["sb"][e[i]] == d1[i])
            if not words or words[-1] != wv: words.append(wv)
        counter = all(words[k + 1] == words[k] + 1 for k in range(len(words) - 1))
        with tempfile.TemporaryDirectory() as td:
            r = subprocess.run([OINK, "--zlk", "-w", "1", path, td + "/s"], capture_output=True)
            if r.returncode: subprocess.run([OINK, "--tl", "-w", "1", path, td + "/s"], capture_output=True, check=True)
            ref = pg.read_sol(open(td + "/s").read(), n)
        vs, _ = E.evaluate(tuple(T2[-1]["s"])); ok = [E.par[x[0]] for x in vs] == list(ref) and not T[-1].get("cycle", False)
        print("ANAT", json.dumps(dict(game=os.path.basename(path), N=N, n=n, start=mode, sf_it=len(T2) - 1, sbc_sigma=sbc, dsb=dsb,
                                      changes_by_class=dict(sorted(ch.items())), e_words=words[:40], e_words_count=len(words),
                                      e_binary_counter=counter, e_max_word=max(words), e_full=(1 << N) - 1, regions_eq_oink=ok,
                                      seconds=round(time.time() - t0))), flush=True)


if __name__ == "__main__":
    main()
